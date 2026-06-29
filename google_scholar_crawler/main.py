from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

import requests
from scholarly import ProxyGenerator, scholarly


INITIAL_DATA: dict[str, Any] = {
    "name": "Guangyi Liu",
    "citedby": 375,
    "first_author_citations": 107,
    "first_author_repo_stars": 582,
    "first_author_repo_stars_k": "0.6k",
    "github_stars": 582,
    "github_stars_k": "0.6k",
    "publication_metrics": {
        "memgui_bench": {"num_citations": 11},
        "learnact": {"num_citations": 36},
        "phone_gui_survey": {"num_citations": 60},
        "ui_r1": {"num_citations": 195},
        "a3": {"num_citations": 42},
        "mas_bench": {"num_citations": 4},
        "fedmabench": {"num_citations": 10},
        "mobilea3gent": {"num_citations": 13},
    },
}

SELECTED_PUBLICATIONS: dict[str, dict[str, Any]] = {
    "mobileforge": {
        "title_patterns": ["MobileForge"],
        "fallback_citations": 0,
    },
    "memgui_agent": {
        "title_patterns": ["MemGUI-Agent"],
        "fallback_citations": 0,
    },
    "memgui_bench": {
        "title_patterns": ["MemGUI-Bench"],
        "fallback_citations": 11,
    },
    "learnact": {
        "title_patterns": ["LearnAct"],
        "fallback_citations": 36,
    },
    "phone_gui_survey": {
        "title_patterns": [
            "LLM-Powered GUI Agents in Phone Automation",
            "Surveying Progress and Prospects",
        ],
        "fallback_citations": 60,
    },
    "ui_r1": {
        "title_patterns": ["UI-R1", "Enhancing Efficient Action Prediction"],
        "fallback_citations": 195,
    },
    "a3": {
        "title_patterns": ["A3", "Android Agent Arena"],
        "fallback_citations": 42,
    },
    "fedgui": {
        "title_patterns": ["FedGUI"],
        "fallback_citations": 0,
    },
    "ui_copilot": {
        "title_patterns": ["UI-Copilot", "Tool-Integrated Policy Optimization"],
        "fallback_citations": 0,
    },
    "mas_bench": {
        "title_patterns": ["MAS-Bench", "Shortcut-Augmented Hybrid Mobile GUI Agents"],
        "fallback_citations": 4,
    },
    "fedmabench": {
        "title_patterns": ["FedMABench"],
        "fallback_citations": 10,
    },
    "mobilea3gent": {
        "title_patterns": ["MobileA3gent"],
        "fallback_citations": 13,
    },
}

FIRST_AUTHOR_SLUGS = [
    "mobileforge",
    "memgui_agent",
    "memgui_bench",
    "learnact",
    "phone_gui_survey",
]

FIRST_AUTHOR_REPOS = [
    ("PhoneLLM", "Awesome-LLM-Powered-Phone-GUI-Agents"),
    ("lgy0404", "MemGUI-Bench"),
    ("kwai", "MemGUI-Agent"),
    ("kwai", "MobileForge"),
    ("lgy0404", "LearnAct"),
    ("lgy0404", "d2l-2023"),
]


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def format_stars_k(value: int) -> str:
    k_value = (Decimal(value) / Decimal("1000")).quantize(
        Decimal("0.1"), rounding=ROUND_HALF_UP
    )
    return f"{k_value}k"


def fetch_previous_author_data() -> dict[str, Any]:
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not repo:
        raise RuntimeError("GITHUB_REPOSITORY is not set.")

    url = f"https://raw.githubusercontent.com/{repo}/google-scholar-stats/gs_data.json"
    response = requests.get(url, timeout=20)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch previous gs_data.json: {response.status_code}")
    return response.json()


def fetch_author_data_with_retries(google_scholar_id: str, attempts: int = 5) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            proxy_generator = ProxyGenerator()
            proxy_generator.FreeProxies()
            scholarly.use_proxy(proxy_generator)

            author = scholarly.search_author_id(google_scholar_id)
            scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
            return author
        except Exception as exc:
            last_error = exc
            print(f"[scholarly] attempt {attempt}/{attempts} failed: {exc}")
            time.sleep(min(5 * attempt, 20))
    raise RuntimeError(f"scholarly failed after {attempts} attempts: {last_error}")


def publications_as_dict(author: dict[str, Any]) -> dict[str, Any]:
    publications = author.get("publications", {})
    if isinstance(publications, dict):
        return publications
    if isinstance(publications, list):
        return {
            publication.get("author_pub_id", f"pub_{idx}"): publication
            for idx, publication in enumerate(publications)
        }
    return {}


def publication_title(publication: dict[str, Any]) -> str:
    bib = publication.get("bib", {})
    if isinstance(bib, dict):
        return str(bib.get("title", ""))
    return ""


def match_publication(publications: dict[str, Any], patterns: list[str]) -> tuple[str, dict[str, Any]] | tuple[None, None]:
    normalized_patterns = [normalize_text(pattern) for pattern in patterns]
    for pub_id, publication in publications.items():
        title = normalize_text(publication_title(publication))
        if all(pattern in title for pattern in normalized_patterns):
            return pub_id, publication
    for pub_id, publication in publications.items():
        title = normalize_text(publication_title(publication))
        if any(pattern in title for pattern in normalized_patterns):
            return pub_id, publication
    return None, None


def build_publication_metrics(author: dict[str, Any], previous: dict[str, Any]) -> dict[str, Any]:
    publications = publications_as_dict(author)
    previous_metrics = previous.get("publication_metrics", {})
    metrics: dict[str, Any] = {}

    for slug, spec in SELECTED_PUBLICATIONS.items():
        pub_id, publication = match_publication(publications, spec["title_patterns"])
        previous_count = previous_metrics.get(slug, {}).get("num_citations")
        fallback_count = spec.get("fallback_citations", 0)
        num_citations = int(previous_count if previous_count is not None else fallback_count)

        if publication:
            num_citations = int(publication.get("num_citations", num_citations) or 0)

        metrics[slug] = {
            "num_citations": num_citations,
            "author_pub_id": pub_id,
            "title": publication_title(publication) if publication else spec["title_patterns"][0],
        }

    return metrics


def github_headers() -> dict[str, str]:
    github_pat = os.environ.get("GITHUB_PAT", "")
    github_token = github_pat or os.environ.get("GITHUB_TOKEN", "")
    if github_token:
        return {"Authorization": f"token {github_token}"}
    return {}


def fetch_repo_stars(owner: str, repo: str, headers: dict[str, str]) -> int | None:
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=headers,
        timeout=20,
    )
    if response.status_code != 200:
        print(f"Failed to fetch repo {owner}/{repo}: {response.status_code}")
        return None
    return int(response.json().get("stargazers_count", 0) or 0)


def add_github_stats(author: dict[str, Any], previous: dict[str, Any]) -> None:
    headers = github_headers()
    repo_metrics = {}
    previous_repo_metrics = previous.get("repo_metrics", {})
    first_author_repo_stars = 0

    for owner, repo in FIRST_AUTHOR_REPOS:
        full_name = f"{owner}/{repo}"
        stars = fetch_repo_stars(owner, repo, headers)
        if stars is None:
            stars = previous_repo_metrics.get(full_name, {}).get("stargazers_count")
        if stars is None:
            stars = 0
        repo_metrics[full_name] = {"stargazers_count": int(stars)}
        first_author_repo_stars += stars

    if first_author_repo_stars == 0 and previous.get("first_author_repo_stars"):
        first_author_repo_stars = int(previous["first_author_repo_stars"])

    author["repo_metrics"] = repo_metrics
    author["first_author_repo_stars"] = first_author_repo_stars
    author["first_author_repo_stars_k"] = format_stars_k(first_author_repo_stars)
    author["github_stars"] = first_author_repo_stars
    author["github_stars_k"] = author["first_author_repo_stars_k"]


def load_author_data() -> dict[str, Any]:
    google_scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "XqQp-fkAAAAJ")
    try:
        return fetch_author_data_with_retries(google_scholar_id)
    except Exception as exc:
        print(f"[scholarly] giving up, fallback to previous gs_data.json. reason: {exc}")
        try:
            return fetch_previous_author_data()
        except Exception as previous_exc:
            print(f"[fallback] previous gs_data.json unavailable: {previous_exc}")
            return dict(INITIAL_DATA)


def main() -> None:
    author = load_author_data()
    try:
        previous = fetch_previous_author_data() if os.environ.get("GITHUB_REPOSITORY") else INITIAL_DATA
    except Exception as exc:
        print(f"[fallback] using initial metrics because previous data is unavailable: {exc}")
        previous = INITIAL_DATA

    author["updated"] = datetime.now(timezone.utc).isoformat()
    author["publications"] = publications_as_dict(author)
    author["publication_metrics"] = build_publication_metrics(author, previous)
    author["first_author_citations"] = sum(
        int(author["publication_metrics"][slug]["num_citations"])
        for slug in FIRST_AUTHOR_SLUGS
    )
    add_github_stats(author, previous)

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author.get('citedby', 0)}",
    }
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)

    print(json.dumps(author, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
