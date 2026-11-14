# www.gongbans.com

Static site on GitHub Pages. Managed by the web-master (see ~/Projects/web-master).

- Live: https://www.gongbans.com
- Repo: hansstam86/gongbans-site (branch `main`, served from repo root, legacy Pages build)
- DNS: GoDaddy (apex A records to GitHub Pages IPs, www CNAME to the owner's github.io)
- Pages: `index.html` (investor landing), `boards.html` (catalogue, 1,100+ boards, JS grid), `db/<slug>.html`
  (one page per board, generated), `issuers.html` (publishers + solution-house directory, generated),
  `boards-kingbrother.html` (hand-written Kingbrother SOM page), `what-are-gongbans.html` (essay),
  `ideas.html` + `ideas/<slug>.html` (50 product concepts built from catalogue boards, generated from `data/ideas.json`
  by `build_ideas.py`; board pages get a "Used in ideas" block from the same JSON).
- One shared stylesheet: `assets/style.css` (palette/fonts of the original landing page: deep green
  `#021e14`, gold `#c9a84c`, copper `#b87333`, cream `#f5f2eb`; DM Serif Display / IBM Plex Sans / IBM Plex Mono).
  Every page links it; keep page-specific CSS in there too, not inline.

## Rules
- No build step at runtime: GitHub Pages serves the committed HTML. The generator scripts run locally and their
  output is committed.
- Do not change `CNAME`, DNS or Pages settings without Hans's OK.
- Draft only; don't invent content, prices or claims. Numbers on the home page come from `data/stats.json`
  via `<span data-stat="…">` (patched by `build_detail_pages.py`), never typed by hand.
- Rebuild after data changes: `python3 build_catalog.py` (reads `~/Projects/gongban-db/gongban.db`, writes
  `data/*.json`; curated entries are kept verbatim) then `python3 build_detail_pages.py` (writes `db/*.html`,
  `issuers.html`, patches stats) then `python3 build_ideas.py` (writes `ideas.html`, `ideas/*.html`, patches the
  idea count/top list on `index.html`). Commit the generated output.
- Ideas are concepts from the gongban-inventor workspace, not products: keep the disclaimer on every idea page, label
  every number as an estimate, never add medical, shared-mobility or vehicle-tracking ideas, and keep the
  `check-licence` tag on anything that uses OSHWHub boards. Source of truth: `data/ideas.json`
  (copied from `agent-assistant/.../gongban-inventor/ideas/ideas50.json`).
- The database itself is private and must never be committed. Never export: `contacts`, `outreach`, `fetch_log`,
  `fairs`, `sources.notes`, `solution_houses.wechat/email/notes/district`, rows with `solution_houses.excluded` set,
  anything ride-sharing / vehicle-tracking / micromobility (see `MOBILITY_RE`), e-mail addresses, personal names, WeChat IDs,
  OSHWHub author handles. `build_catalog.py` enforces these; keep its exclusion lists when editing.
- Old URLs must keep resolving: `boards.html` (now the catalogue), the 16 curated `db/*.html`, `index.html`,
  `what-are-gongbans.html`, `ideas.html`. Kingbrother's former `boards.html` content lives at `boards-kingbrother.html`.
