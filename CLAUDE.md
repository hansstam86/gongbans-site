# www.gongbans.com

Static site on GitHub Pages. Managed by the web-master (see ~/Projects/web-master).

- Live: https://www.gongbans.com
- Repo: hansstam86/gongbans-site (branch `main`, served from repo root, legacy Pages build)
- DNS: GoDaddy (apex A records to GitHub Pages IPs, www CNAME to the owner's github.io)
- Pages: `index.html` (two doors: founders → `start.html`, investors → the briefing below; all investor content kept), `start.html` (first-time founder entry page, hand-written: gongban in 3 sentences, 4-step path, first-timer mistakes, glossary), `boards.html` (catalogue, 1,100+ boards, JS grid), `db/<slug>.html`
  (one page per board, generated), `issuers.html` (publishers + solution-house directory, generated),
  `boards-kingbrother.html` (hand-written Kingbrother SOM page), `what-are-gongbans.html` (essay),
  `ideas.html` + `ideas/<slug>.html` (product concepts built from catalogue boards; 50 generated, 16 withdrawn 2026-11-14 after the external market check (slugs in `data/ideas.json` → `removed_after_market_check`, full records in git history), 16 added the same day in round 2 (`add_ideas_round2.py`, `add_ideas_round2b.py`; market-checked before building; `data/ideas.json` → `rounds`), generated from `data/ideas.json`
  by `build_ideas.py`; board pages get a "Used in ideas" block from the same JSON),
  `startpacks/<slug>.html` + `startpacks/<slug>.md` (founder start packs: business plan + start kit per idea, rendered by
  `build_startpacks.py` from the Markdown, called by `build_ideas.py`; the .md is the "Download as Markdown" source),
  `playbook.html` (the zero-experience founder playbook shared by all ideas, written in `build_playbook.py`).
- One shared stylesheet: `assets/style.css` (palette/fonts of the original landing page: deep green
  `#021e14`, gold `#c9a84c`, copper `#b87333`, cream `#f5f2eb`; DM Serif Display / IBM Plex Sans / IBM Plex Mono).
  Every page links it; keep page-specific CSS in there too, not inline.

## Rules
- Nav/footer are defined ONCE in `build_detail_pages.py` (`NAV_ITEMS`, `nav()`, `FOOTER`): Start here · What are gongbans? · Catalogue · Who makes them (URL stays `issuers.html`) · Ideas · Playbook (+ Investors / How it works on the home page only, `HOME_EXTRA`). Generated pages call `nav(active)`; the hand-written pages (`STATIC_PAGES`: index, start, boards, what-are-gongbans, boards-kingbrother) get nav, footer and `?v=ASSET_V` rewritten by `patch_chrome()` on every `build_detail_pages.py` run, so never hand-edit a nav. Bump `ASSET_V` when CSS/JS change.
- Monetisation elements (added 2026-11-14, Hans's OK), both defined ONCE in `build_detail_pages.py`: (1) **"Get this built" CTA** — `BUILD_CTA_*` constants + `build_cta_href()` / `build_cta()`; exactly one box per idea page, start pack and board page (`db/`), a `mailto:hans@supplychat.ai` with subject `gongbans build request: <name>` and a URL-encoded intake template. To switch the intake to a web form later, change `build_cta_href()` only. It replaced the old "Want help? / talk to Hans" box on the start packs; never add a second CTA box. (2) **GONGBANS book box** — `BOOK_URL`, `BOOK_TITLE/TEXT/BUTTON`, `book_box()`; on `start.html` (between `<!-- book-box -->` / `<!-- /book-box -->`, rewritten by `patch_chrome()`) and near the end of every start pack, before the CTA. Every "The book" link (nav, footer, boxes) uses `BOOK_URL` = https://hansolo42.gumroad.com/l/gongbans. The book text may only say what the site already says about the book; there is no cover image in the repo, so none is shown. CSS: `.build-cta-box`, `.book-box` in `assets/style.css`.
- Founder wording: catalogue chips/badges and the db-page openness pill use plain language (`OPEN_LABEL` in `assets/app.js` = `OPENNESS_PLAIN` in `build_detail_pages.py`; keep them in sync). The "Beginner-friendly (free files)" quick chip = free download/hosted + schematic, PCB or Gerber published; deep link `boards.html#beginner=1` (or `?beginner=1`), used by `start.html`. The nav collapses to the menu button below 1100px (it has 9–11 links).
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
- Start packs: `startpacks/<slug>.md` is copied from `agent-assistant/.../gongban-inventor/startpacks/` (one per idea slug;
  `_progress-*` files stay out). Edit the Markdown, never the generated HTML; rerun `python3 build_ideas.py`. The renderer
  (`build_startpacks.py`) is stdlib-only and supports headings, lists, pipe tables, fenced blocks (diagrams → `<pre>`),
  bold/italic/code/links; `www.gongbans.com/...` links become site-relative. Every pack page carries the disclaimer at the
  top; a pack without an idea page aborts the build. `.nojekyll` is required so GitHub Pages serves the `.md` files as-is.
- "Validate demand first" (section 2 of every pack) is generated by `build_validate.py` from `data/ideas.json` (kill question as gate,
  audience, interview probe + pre-order message) and two hand-curated tables in the script: `WHERE` (communities per idea; only
  ones we are confident exist, otherwise generic search guidance) and `PROBE` (one problem-first question per idea). Block sits
  between `<!-- validate-demand:start/end -->`; edit the script, not the block. Pack order is fixed: 1 Summary, 2 Validate demand,
  3 Business plan, 4 Start kit, 5 Who to contact, 6 Next steps.
- External market check: `data/market-check.json` holds web-research findings per idea (verdict, summary, main risk, competitor/
  source rows; an optional `correction`). `build_market.py` writes a callout at the end of section 1 and an "External market
  check" sub-table under "### Competition" (markers `market-check` / `market-competitors`). Quote verdicts as given, never
  stronger; keep the "as researched … verify before relying on it" caveat; cite sources by name, no unverified links. A buyer
  correction is applied at the source in `data/ideas.json` (`kill_question` revised, `kill_question_original`,
  `market_correction`, audience/tags) so the idea page and section 2 pick it up; Mould-Risk Monitor is the first case.
- "Who to contact" (section 5 of every pack) is generated, not hand-written: `build_contacts.py` reads gongban.db and
  rewrites the block between `<!-- who-to-contact:start -->` / `<!-- who-to-contact:end -->` in each `.md` (and writes
  `data/contacts.json`, public columns only). Edit the script, not the block. Only *company* board publishers count as
  a match; OSHWHub designs get the "no verified contact" note; directory entries are labelled "category match, not
  idea-specific"; no MOQ/price is shown unless it is in the db (ManThink is the only one). Never add e-mail addresses,
  WeChat IDs or personal names to it, even if asked: company websites only (the `check()` assertions enforce this).
- The database itself is private and must never be committed. Never export: `contacts`, `outreach`, `fetch_log`,
  `fairs`, `sources.notes`, `solution_houses.wechat/email/notes/district`, rows with `solution_houses.excluded` set,
  anything ride-sharing / vehicle-tracking / micromobility (see `MOBILITY_RE`), e-mail addresses, personal names, WeChat IDs,
  OSHWHub author handles. `build_catalog.py` enforces these; keep its exclusion lists when editing.
- Old URLs must keep resolving: `boards.html` (now the catalogue), the 16 curated `db/*.html`, `index.html`,
  `what-are-gongbans.html`, `ideas.html`. Kingbrother's former `boards.html` content lives at `boards-kingbrother.html`.
- WPI ATU 2016 catalogue (added 2026-11-15): 100 `wpi-atu-<code>-…` rows in gongban.db (source `wpi_atu_catalogue_2016`, metadata only, imported by
  `~/Projects/gongban-db/scripts/import_atu_2016.py` from two private PDFs that must never be published or hosted). 90 are published; the 10 that
  describe a hand-curated ATU kit (same project code) are listed in `DUPLICATE_SLUGS` in `build_catalog.py`. No designer / team-member names anywhere.
- Hi-Link catalogue (added 2026-11-16, Hans OK): 155 `hilink-…` rows in gongban.db (source `hilink_brochure_2026`, issuer_type `module_maker`), imported by
  `~/Projects/gongban-db/scripts/import_hilink_2026.py` from JSON extracts of Hi-Link's English brochure (private, never hosted). Permission (Hi-Link, 16 Nov 2026)
  covers brochure content + public datasheets + photos only: no prices, no MOQ, no schematics/PCB/SDK, no personal contact data on the site. Every Hi-Link page
  carries the credit box (`SOURCE_CREDIT` in `build_catalog.py` → `credit_section()` in `build_detail_pages.py`) linking hlktech.com + the download centre.
  Openness `contact_issuer` = "Datasheet public, files via maker" (also in `assets/app.js`). Vehicle/traffic radars (LD2415L, LD2417, LD2451, LD7902) are
  excluded (mobility rule). QA: `agent-assistant/.../outputs/gongbans_hilink_qa.py`.
- Tuya modules (added 2026-11-16, Hans OK "go ahead anyway", before Tuya replied to the partnership mail): 151 `tuya-…` rows in gongban.db (source `tuya_public_docs_2026`,
  issuer_type `platform_module_maker`), imported by `~/Projects/gongban-db/scripts/import_tuya_2026.py` from JSON extracts of Tuya's PUBLIC developer docs
  (agent-assistant/.../gongban-hunt/tuya/extract/). Metadata + our own summaries only: no copied text, no hosted PDFs/images, no prices. Every page: credit box
  (`SOURCE_CREDIT` + `credit_for()` in `build_catalog.py`, incl. the per-module "Official Tuya datasheet" link) with "Listed from Tuya's public documentation; Tuya is not
  affiliated with GONGBANS unless stated." Excluded: deprecated modules, all NB-IoT/Cat.1 (datasheets target vehicle/bike tracking, mobility rule), GNSS (not extracted).
  Guide `/guides/build-with-tuya.html` is generated by `build_guides.py` (called from `build_detail_pages.py`), linked from the Tuya issuer card (`ISSUER_GUIDES`).
  QA: `agent-assistant/.../outputs/gongbans_tuya_qa.py <total>`.
