# Google Scholar and GitHub Stats Crawler

This crawler refreshes the dynamic stats used by the homepage badges.

It collects:
- total Google Scholar citations;
- first-author paper citations;
- selected paper citation counts;
- first-author GitHub project stars.

The GitHub Action runs daily and pushes `gs_data.json` to the
`google-scholar-stats` branch. The homepage reads that JSON through Shields'
`dynamic/json` badges.

## Citation Updates

The Scholar fetch configuration follows
[Xiaoxi-Li1's crawler](https://github.com/Xiaoxi-Li1/Xiaoxi-Li1.github.io/tree/main/google_scholar_crawler):
`scholarly==1.7.11` with `httpx==0.23.3`. Newer httpx releases remove the
`proxies` argument that this scholarly version needs. CI uses Python 3.12.
`bibtexparser==1.4.3` is also pinned because scholarly imports v1-only modules
that are absent in bibtexparser 2.
If the free-proxy service fails, the crawler also tries a direct Scholar
connection before falling back to a saved snapshot.

- The daily schedule is 00:00 UTC (08:00 China time); actual starts may be delayed.
  A push to `main`, a page build, or a manual workflow dispatch also triggers it.
- A successful fetch uses Google's current total and per-paper citation counts,
  including downward corrections. First-author citations sum the five selected
  first-author papers. Existing `publication_metrics` keys remain compatible with
  the homepage badges.
- Only a failed fetch falls back to the previous snapshot. An unmatched paper
  retains its previous count separately. Neither case silently claims a refresh:
  GitHub Actions emits a warning.
- `scholar_fetch_status` is `live` or `fallback`; `scholar_updated` records the
  last successful Scholar fetch (null if unknown). Per-paper `data_source` records
  unmatched-paper fallbacks. The existing `updated` field is the combined stats
  generation time, which can advance when only GitHub stars are refreshed.

This is a daily snapshot, not a request to Google Scholar on every page visit.
Shields/GitHub caches may delay badge changes after the JSON updates.

## Local Run

```bash
cd google_scholar_crawler
python -m pip install -r requirements.txt
python -m pip check
python -m unittest discover -s tests -v
GOOGLE_SCHOLAR_ID=XqQp-fkAAAAJ GITHUB_REPOSITORY=lgy0404/lgy0404.github.io GITHUB_USERNAME=lgy0404 python main.py
```

The generated files are written to `google_scholar_crawler/results/`.

## Maintenance

When a new first-author paper or first-author project appears, update
`FIRST_AUTHOR_SLUGS`, `SELECTED_PUBLICATIONS`, and `FIRST_AUTHOR_REPOS` in
`main.py`.
