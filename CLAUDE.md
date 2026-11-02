# www.gongbans.com

Static site on GitHub Pages. Managed by the web-master (see ~/Projects/web-master).

- Live: https://www.gongbans.com
- Repo: hansstam86/gongbans-site (branch `main`, served from repo root, legacy Pages build)
- DNS: GoDaddy (apex A records to GitHub Pages IPs, www CNAME to the owner's github.io)
- GONGBANS DB, a static database of Chinese reference designs; `build_detail_pages.py` generates detail pages from `data/` (see README.md).

## Rules
- No build step: edit the HTML directly and push to `main` to deploy.
- Do not change `CNAME`, DNS or Pages settings without Hans's OK.
- Draft only; don't invent content, prices or claims.
- Regenerate detail pages with the script after changing data; commit the generated output.
