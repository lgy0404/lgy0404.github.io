import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

import httpx

import main as crawler


def live_profile():
    return {
        "name": "Guangyi Liu",
        "citedby": 100,
        "publications": [
            {
                "author_pub_id": f"test:{slug}",
                "bib": {"title": " ".join(spec["title_patterns"])},
                "num_citations": 0 if slug == "memgui_agent" else 1,
            }
            for slug, spec in crawler.SELECTED_PUBLICATIONS.items()
        ],
    }


class CitationTests(unittest.TestCase):
    def test_scholarly_httpx_compatibility(self):
        self.assertEqual(httpx.__version__, "0.23.3")
        with httpx.Client(proxies={}):
            pass
        crawler.ProxyGenerator()

    def test_live_counts_allow_decreases_and_zero(self):
        previous = deepcopy(crawler.INITIAL_DATA)
        with patch.object(crawler, "fetch_author_data_with_retries", return_value=live_profile()):
            author = crawler.load_author_data(previous)
        self.assertEqual(author["citedby"], 100)
        self.assertEqual(author["first_author_citations"], 4)
        self.assertEqual(author["publication_metrics"]["phone_gui_survey"]["num_citations"], 1)
        self.assertEqual(author["publication_metrics"]["memgui_agent"]["num_citations"], 0)
        self.assertEqual(author["scholar_fetch_status"], "live")
        self.assertIsNotNone(author["scholar_updated"])
        self.assertEqual(previous, crawler.INITIAL_DATA)

    def test_unmatched_paper_preserves_previous_zero_without_floor(self):
        profile = live_profile()
        profile["publications"] = [
            pub for pub in profile["publications"] if pub["author_pub_id"] != "test:learnact"
        ]
        previous = {"publication_metrics": {"learnact": {"num_citations": 0, "author_pub_id": "old:id"}}}
        output = io.StringIO()
        with redirect_stdout(output):
            metrics = crawler.build_publication_metrics(profile, previous)
        self.assertEqual(metrics["learnact"]["num_citations"], 0)
        self.assertEqual(metrics["learnact"]["author_pub_id"], "old:id")
        self.assertEqual(metrics["learnact"]["data_source"], "fallback")
        self.assertIn("::warning::", output.getvalue())

    def test_fallback_preserves_snapshot_and_successful_fetch_date(self):
        previous = deepcopy(crawler.INITIAL_DATA)
        previous.update(live_profile())
        previous["scholar_updated"] = "2026-08-01T00:00:00+00:00"
        before = deepcopy(previous)
        output = io.StringIO()
        with patch.object(crawler, "fetch_author_data_with_retries", side_effect=RuntimeError("blocked")):
            with redirect_stdout(output):
                author = crawler.load_author_data(previous)
        self.assertEqual(author["scholar_fetch_status"], "fallback")
        self.assertEqual(author["scholar_updated"], before["scholar_updated"])
        for key in ("citedby", "first_author_citations", "publication_metrics", "publications"):
            self.assertEqual(author[key], before[key])
        self.assertEqual(previous, before)
        self.assertIn("NOT been refreshed", output.getvalue())

    def test_legacy_fallback_does_not_invent_a_successful_fetch_date(self):
        previous = deepcopy(crawler.INITIAL_DATA)
        previous["updated"] = "2026-09-07T00:00:00+00:00"
        with patch.object(crawler, "fetch_author_data_with_retries", side_effect=RuntimeError("blocked")):
            with redirect_stdout(io.StringIO()):
                author = crawler.load_author_data(previous)
        self.assertIsNone(author["scholar_updated"])

    def test_incomplete_profile_is_retried(self):
        with patch.object(crawler, "ProxyGenerator"), patch.object(crawler, "scholarly") as scholar:
            scholar.search_author_id.side_effect = [{"citedby": 999}, live_profile()]
            with patch.object(crawler.time, "sleep") as sleep, redirect_stdout(io.StringIO()):
                author = crawler.fetch_author_data_with_retries("test", attempts=2)
        self.assertEqual(author["citedby"], 100)
        sleep.assert_called_once_with(5)

    def test_proxy_service_failure_still_attempts_scholar_directly(self):
        from unittest.mock import MagicMock

        for failure in (RuntimeError("proxy list unavailable"), None):
            with self.subTest(failure=failure):
                free_proxy, direct = MagicMock(), MagicMock()
                free_proxy.FreeProxies.side_effect = failure
                free_proxy.FreeProxies.return_value = False
                with patch.object(crawler, "ProxyGenerator", side_effect=[free_proxy, direct]):
                    with patch.object(crawler, "scholarly") as scholar, redirect_stdout(io.StringIO()):
                        scholar.search_author_id.return_value = live_profile()
                        author = crawler.fetch_author_data_with_retries("test", attempts=1)
                self.assertEqual(author["citedby"], 100)
                scholar.use_proxy.assert_called_once_with(direct, direct)

    def test_working_proxy_is_used_for_both_scholar_sessions(self):
        with patch.object(crawler, "ProxyGenerator") as factory, patch.object(crawler, "scholarly") as scholar:
            factory.return_value.FreeProxies.return_value = True
            scholar.search_author_id.return_value = live_profile()
            crawler.fetch_author_data_with_retries("test", attempts=1)
        scholar.use_proxy.assert_called_once_with(factory.return_value, factory.return_value)

    def test_retries_stop_without_sleeping_after_final_failure(self):
        with patch.object(crawler, "ProxyGenerator", side_effect=RuntimeError("network")):
            with patch.object(crawler.time, "sleep") as sleep, redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(RuntimeError, "after 2 attempts"):
                    crawler.fetch_author_data_with_retries("test", attempts=2)
        sleep.assert_called_once_with(5)

    def test_output_preserves_badge_contract(self):
        original_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                with patch.object(crawler, "fetch_author_data_with_retries", return_value=live_profile()):
                    with patch.object(crawler, "fetch_previous_author_data", return_value=deepcopy(crawler.INITIAL_DATA)):
                        with patch.object(crawler, "add_github_stats") as stars, redirect_stdout(io.StringIO()):
                            crawler.main()
                data = json.loads(Path("results/gs_data.json").read_text())
                badge = json.loads(Path("results/gs_data_shieldsio.json").read_text())
                self.assertEqual(badge["message"], "100")
                self.assertEqual(data["first_author_citations"], 4)
                self.assertEqual(set(data["publication_metrics"]), set(crawler.SELECTED_PUBLICATIONS))
                self.assertEqual(data["scholar_fetch_status"], "live")
                stars.assert_called_once()
            finally:
                os.chdir(original_cwd)


if __name__ == "__main__":
    unittest.main()
