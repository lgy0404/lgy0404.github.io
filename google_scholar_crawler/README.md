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

## Local Run

```bash
cd google_scholar_crawler
pip install -r requirements.txt
GOOGLE_SCHOLAR_ID=XqQp-fkAAAAJ GITHUB_USERNAME=lgy0404 python main.py
```

The generated files are written to `google_scholar_crawler/results/`.

## Maintenance

When a new first-author paper or first-author project appears, update
`FIRST_AUTHOR_SLUGS`, `SELECTED_PUBLICATIONS`, and `FIRST_AUTHOR_REPOS` in
`main.py`.
