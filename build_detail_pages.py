#!/usr/bin/env python3
"""
build_detail_pages.py — render the generated parts of the site from data/:

    db/<slug>.html   one page per board (data/gongbans.json)
    issuers.html     publishers of the boards + solution-house directory (data/issuers.json)
    stats            numbers inside <span data-stat="…"> on index.html / what-are-gongbans.html
                     and the category list between <!-- stat-cats --> markers (data/stats.json)

Run from the repo root after build_catalog.py:
    python3 build_detail_pages.py

Pages use the shared light theme (assets/style.css). Fields that are empty
are simply not rendered — nothing is invented.
"""

import html
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
MANIFEST = ROOT / "data" / "gongbans.json"
ISSUERS = ROOT / "data" / "issuers.json"
STATS = ROOT / "data" / "stats.json"
IDEAS = ROOT / "data" / "ideas.json"   # optional: ideas built on the boards (build_ideas.py renders their pages)
DB_DIR = ROOT / "db"
DB_DIR.mkdir(exist_ok=True)

ASSET_V = "20261114d"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Crect width='100' height='100' fill='%23021e14'/%3E%3Ccircle cx='50' cy='50' r='30' fill='none' "
           "stroke='%23c9a84c' stroke-width='6'/%3E%3Ccircle cx='50' cy='50' r='10' fill='%23c9a84c'/%3E%3C/svg%3E")

KIND_ICON = {
    "schematic": "SCH", "pcb": "PCB", "gerber": "GBR", "bom": "BOM", "spec": "SPEC",
    "firmware": "FW", "bsp": "BSP", "enclosure": "3D", "mech": "MECH", "photos": "IMG",
    "block_diagram": "BLK", "pcb_lib": "LIB", "sch_lib": "LIB", "artwork": "ART",
    "presentation": "PPT", "datasheets": "DS",
}
KIND_LABEL = {
    "schematic": "Schematic", "pcb": "PCB layout", "gerber": "Gerber files", "bom": "Bill of materials",
    "spec": "Specification / manual", "firmware": "Firmware", "bsp": "BSP / software", "enclosure": "Enclosure (3D)",
    "mech": "Mechanical drawings", "photos": "Photos", "block_diagram": "Block diagram",
    "pcb_lib": "PCB library", "sch_lib": "Schematic library", "artwork": "Artwork",
    "presentation": "Reference presentation", "datasheets": "Component datasheets",
}
OPENNESS_TEXT = {
    "open_download": "Published for open download by the issuer.",
    "registration": "Available after free registration on the issuer's site.",
    "with_purchase": "Design files are handed over with a purchase of the board.",
    "contact_atu": "Design files are released through the distributor's field-application channel (WPI / ATU), not published openly.",
    "community": "Circulates through community channels rather than an official publication.",
}
OPENNESS_CLASS = {"open_download": "", "community": "neutral", "registration": "gated", "with_purchase": "gated", "contact_atu": "gated", "hosted": ""}
# plain-language labels (same wording as the catalogue chips in assets/app.js)
OPENNESS_PLAIN = {"open_download": "Free download", "registration": "Free account needed", "with_purchase": "Comes with purchase",
                  "contact_atu": "Ask the distributor (ATU)", "community": "Community project", "hosted": "Download here (full pack)"}
CURATED_FILE_TYPES = [
    ("schematic", "SCH", "Schematic", "Protel / Altium .sch"),
    ("pcb", "PCB", "PCB layout", "Protel / Altium .pcb"),
    ("gerber", "GBR", "Gerber files", ""),
    ("bom", "BOM", "Bill of materials", ".xlsx"),
    ("spec", "SPEC", "Specification document", ".docx"),
    ("presentation", "PPT", "Reference presentation", ".pptx"),
]


def e(s) -> str:
    return html.escape(str(s if s is not None else ""))


def ext_link(url: str, label: str) -> str:
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(label)}</a>'


def head(title, description, canonical, og_type="article", extra=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="https://www.gongbans.com/{canonical}">
<link rel="canonical" href="https://www.gongbans.com/{canonical}">
<link rel="icon" href="{FAVICON}">
{FONTS}
<link rel="stylesheet" href="/assets/style.css?v={ASSET_V}">{extra}
</head>'''


ACTIVE = ' class="active"'


NAV_ITEMS = [("/start.html", "Start here", "start"), ("/what-are-gongbans.html", "What are gongbans?", "what"),
             ("/boards.html", "Catalogue", "boards"), ("/issuers.html", "Who makes them", "issuers"),
             ("/ideas.html", "Ideas", "ideas"), ("/playbook.html", "Playbook", "playbook")]
NAV_TAIL = [("https://hansolo42.gumroad.com/l/gongbans", "The book", ""), ("https://hansstam.eu", "Hans Stam", "")]
HOME_EXTRA = [("#investors", "Investors"), ("#how-it-works", "How it works")]   # investor anchors, home page only


def nav(active="", extra=()):
    """Site nav, identical on every page. `extra` = (href, label) pairs inserted before the book link
    (the home page uses it for its investor anchors)."""
    items = NAV_ITEMS + [(h, l, "") for h, l in extra] + NAV_TAIL
    links = "\n".join(f'    <a href="{href}"{ACTIVE if key and key == active else ""}>{label}</a>' for href, label, key in items)
    return f'''<nav class="site-nav">
  <a href="/" class="logo">GONGBANS<span>/公板</span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-links">Menu</button>
  <div class="links" id="site-links">
{links}
    <a href="/#download" class="cta">Download PDF</a>
  </div>
</nav>'''


FOOTER = f'''<footer class="site-footer">
  <p class="foot-links"><a href="/">Home</a><a href="/start.html">Start here</a><a href="/what-are-gongbans.html">What are gongbans?</a><a href="/boards.html">Catalogue</a><a href="/issuers.html">Who makes them</a><a href="/ideas.html">Ideas</a><a href="/playbook.html">Playbook</a><a href="/boards-kingbrother.html">Kingbrother SOMs</a></p>
  <p><a href="https://hansstam.eu">Hans Stam</a> · Berlin / Shenzhen · 20 years in China manufacturing · Author of <a href="https://hansolo42.gumroad.com/l/gongbans">GONGBANS</a> · <a href="mailto:hans.stam@gmail.com">hans.stam@gmail.com</a></p>
</footer>
<script src="/assets/site.js?v={ASSET_V}"></script>'''


# ---------------------------------------------------------------------------
# detail page sections
# ---------------------------------------------------------------------------
def file_link(label, icon, href, sub="", external=False, download=False):
    attrs = ' target="_blank" rel="noopener"' if external else (" download" if download else "")
    sub_html = f"<small>{e(sub)}</small>" if sub else ""
    return f'<a class="file-link" href="{e(href)}"{attrs}><span class="file-icon">{e(icon)}</span><span class="file-name">{e(label)}{sub_html}</span></a>'


def hosted_files_section(g):
    files = g.get("files") or {}
    items = []
    for key, icon, label, sub in CURATED_FILE_TYPES:
        if key in files:
            p = ROOT / files[key]
            size = f"{p.stat().st_size/1e6:.1f} MB" if p.exists() and p.stat().st_size > 1e6 else (f"{p.stat().st_size/1e3:.0f} KB" if p.exists() else "")
            ext = p.suffix.lstrip(".").upper()
            items.append(file_link(label, icon, "/" + files[key], " · ".join(x for x in [sub or ext, size] if x), download=True))
    if "datasheets" in files:
        d = ROOT / files["datasheets"]
        for ds in sorted(d.glob("*")) if d.is_dir() else []:
            if ds.is_file() and not ds.name.startswith("."):
                items.append(file_link(ds.name, "DS", "/" + files["datasheets"].rstrip("/") + "/" + ds.name,
                                       f"datasheet · {ds.stat().st_size/1e6:.1f} MB" if ds.stat().st_size > 1e6 else f"datasheet · {ds.stat().st_size/1e3:.0f} KB", download=True))
    return f'''
  <section class="dsection" id="files">
    <div class="dsection-label">Files · hosted on this site</div>
    <h2>Full design pack</h2>
    <p>Schematic, PCB layout, Gerbers, BOM and the original spec document, as handed over by the distributor. Use it as a starting point, not a drop-in production design.</p>
    <div class="files-list">{"".join(items)}</div>
  </section>'''


def source_files_section(g):
    links = g.get("files_at_source") or []
    kinds = g.get("files_avail") or []
    source_url = g.get("source_url", "")
    openness_text = OPENNESS_TEXT.get(g.get("openness", ""), "")
    kinds_txt = ", ".join(KIND_LABEL.get(k, k) for k in kinds)
    if links:
        items = [file_link(f.get("name") or f["url"], KIND_ICON.get(f["kind"], f["kind"][:4].upper()), f["url"],
                           sub=KIND_LABEL.get(f["kind"], f["kind"]), external=True) for f in links]
        more = g.get("files_at_source_more") or 0
        more_html = f'<p>+{more} more file(s) on the {ext_link(source_url, "source page")}.</p>' if more and source_url else ""
        return f'''
  <section class="dsection" id="files">
    <div class="dsection-label">Files · published by the issuer</div>
    <h2>Design files at source</h2>
    <p>Published as: <strong>{e(kinds_txt)}</strong>. Links open the issuer's own files — nothing is re-hosted here.</p>
    <div class="files-list">{"".join(items)}</div>
    {more_html}
  </section>'''
    if kinds:
        where = f' Open the {ext_link(source_url, "source page")} to get them.' if source_url else ""
        return f'''
  <section class="dsection" id="files">
    <div class="dsection-label">Files · published by the issuer</div>
    <h2>Design files at source</h2>
    <p>Published as: <strong>{e(kinds_txt)}</strong>. Not mirrored on this site.{where}</p>
    {f"<p>{e(openness_text)}</p>" if openness_text else ""}
  </section>'''
    where = f' See the {ext_link(source_url, "source page")}.' if source_url else ""
    return f'''
  <section class="dsection" id="files">
    <div class="dsection-label">Files</div>
    <h2>No design files published</h2>
    <p class="muted">Catalogue metadata only for this entry.{where}</p>
    {f"<p>{e(openness_text)}</p>" if openness_text else ""}
  </section>'''


def bom_section(g):
    bom = g.get("bom_summary")
    if not bom:
        return ""
    rows = "".join(f"<tr><td>{e(k.replace('_', ' '))}</td><td>{e(v)}</td></tr>" for k, v in bom.items())
    return f'''
  <section class="dsection" id="bom">
    <div class="dsection-label">BOM</div>
    <h2>BOM summary</h2>
    <p>Top-level components only. The full bill of materials — every passive, value, package and brand reference — is in the downloadable XLSX above.</p>
    <table class="kv-table"><tbody>{rows}</tbody></table>
  </section>'''


def source_section(g):
    if g.get("origin") != "db":
        return ""
    rows = []
    def row(label, value_html):
        if value_html:
            rows.append(f"<tr><td>{e(label)}</td><td>{value_html}</td></tr>")
    row("Issuer", e(g.get("issuer")))
    if g.get("source_url"):
        u = g["source_url"]
        row("Source page", ext_link(u, u[:90] + ("…" if len(u) > 90 else "")))
    elif g.get("source_note"):
        row("Source page", e(g["source_note"]))
    row("Indexed from", e(g.get("source_name")))
    row("Issuer type", e((g.get("issuer_type") or "").replace("_", " ")))
    row("Openness", e(OPENNESS_PLAIN.get(g.get("openness") or "", g.get("openness_label"))))
    row("Year", e(g.get("year")))
    row("Region", e(g.get("region")))
    row("License", e(g.get("license")))
    row("Database category", e(g.get("db_category")))
    notes = (g.get("notes") or "").strip()
    notes_html = f'<p style="margin-top:16px">{e(notes)}</p>' if notes and notes != g.get("application") else ""
    return f'''
  <section class="dsection" id="source">
    <div class="dsection-label">Provenance</div>
    <h2>Source</h2>
    <table class="kv-table"><tbody>{"".join(rows)}</tbody></table>
    {notes_html}
  </section>'''


def hans_note_section(g):
    note = (g.get("hans_notes") or "").strip()
    if not note:
        return ""
    pending = note.lower().startswith("hans note pending")
    return f'''
  <section class="dsection" id="notes">
    <div class="dsection-label">Sourcing</div>
    <h2>Notes from Hans</h2>
    <div class="hans-note{" pending" if pending else ""}">
      <div class="hans-note-label">{"Sourcing note — pending" if pending else "Hans's sourcing note"}</div>
      <p>{e(note)}</p>
    </div>
  </section>'''


def silicon_section(g):
    chip, brand, role, price = g.get("chip"), g.get("chip_brand"), g.get("chip_role"), g.get("chip_price_5k_usd")
    if not chip or g.get("origin") == "db":
        return ""
    price_html = ""
    if price:
        price_html = f'''<p style="margin-top:16px">Spot price reference at 5k-unit volume: <strong>${price:.2f}</strong>. Actual price depends on distributor (Avnet / Arrow / Future / WPG / local) and current allocation. For the real-time China market check {ext_link("https://www.hqew.com", "hqew.com")} or {ext_link("https://www.lcsc.com", "LCSC")}.</p>'''
    ds = f'<p>{ext_link(g["datasheet_url"], f"{brand} datasheet (PDF)".strip())}</p>' if g.get("datasheet_url") else ""
    mcu_brand = f" ({e(g['mcu_brand'])})" if g.get("mcu_brand") else ""
    mcu = f'<p>Host MCU: <strong>{e(g["mcu_chip"])}</strong>{mcu_brand}.</p>' if g.get("mcu_chip") else ""
    return f'''
  <section class="dsection" id="silicon">
    <div class="dsection-label">Silicon</div>
    <h2>Hero chip</h2>
    <div class="chip-card">
      {f'<div class="chip-brand">{e(brand)}</div>' if brand else ''}
      <div class="chip-name">{e(chip)}</div>
      {f'<div class="chip-role">{e(role)}</div>' if role else ''}
    </div>
    {mcu}{price_html}{ds}
  </section>'''


def chip_key(chip):
    return re.sub(r"[^a-z0-9]", "", (chip or "").lower())


class RelatedIndex:
    def __init__(self, gongbans):
        self.by_chip = defaultdict(list)
        self.by_issuer_cat = defaultdict(list)
        self.by_brand = defaultdict(list)
        for g in gongbans:
            if chip_key(g.get("chip")):
                self.by_chip[chip_key(g["chip"])].append(g)
            issuer = g.get("issuer") or g.get("chip_brand")
            if issuer:
                self.by_issuer_cat[(issuer, g.get("category"))].append(g)
            if g.get("chip_brand"):
                self.by_brand[g["chip_brand"]].append(g)

    def related(self, g, limit=4):
        out, seen = [], {g["slug"]}
        def add(cands):
            for c in cands:
                if c["slug"] not in seen and len(out) < limit:
                    seen.add(c["slug"]); out.append(c)
        if chip_key(g.get("chip")):
            add(self.by_chip[chip_key(g["chip"])])
        if g.get("chip_brand"):
            tags = set(g.get("tags", []))
            add([c for c in self.by_brand[g["chip_brand"]] if set(c.get("tags", [])) & tags])
        issuer = g.get("issuer") or g.get("chip_brand")
        if issuer:
            add(self.by_issuer_cat[(issuer, g.get("category"))])
        return out


def related_section(g, index):
    related = index.related(g)
    if not related:
        return ""
    cards = []
    for r in related:
        status = "full-pack" if r.get("files_available") else r.get("status", "metadata-only")
        cards.append(f'''
      <a class="board {status}" href="/db/{e(r["slug"])}.html">
        <div class="board-id">{e(r.get("project_no") or r.get("issuer") or "")}</div>
        <h3 class="board-name" style="font-size:19px">{e(r["name"])}</h3>
        <div class="board-tag" style="margin-bottom:0">{e(" · ".join(x for x in [r.get("category"), r.get("chip")] if x))}</div>
      </a>''')
    return f'''
  <section class="dsection" id="related">
    <div class="dsection-label">See also</div>
    <h2>Related boards</h2>
    <p>Other entries that share this chip, issuer or application area.</p>
    <div class="boards-grid">{"".join(cards)}</div>
  </section>'''


def load_ideas_by_board():
    """board slug -> [(idea, role)] from data/ideas.json; empty if the file is absent."""
    by_board = defaultdict(list)
    if not IDEAS.exists():
        return by_board
    ideas = json.loads(IDEAS.read_text(encoding="utf-8"))["ideas"]
    for i in sorted(ideas, key=lambda x: (-x.get("score_total", 0), x["title"])):
        for b in i.get("built_from", []):
            by_board[b["board_slug"]].append((i, b.get("role", "")))
    return by_board


def ideas_section(g, ideas_by_board):
    uses = ideas_by_board.get(g["slug"]) or []
    if not uses:
        return ""
    items = "".join(
        f'<a class="file-link" href="/ideas/{e(i["slug"])}.html"><span class="file-icon">IDEA</span>'
        f'<span class="file-name">{e(i["title"])}<small>{e(role)}</small></span></a>' for i, role in uses)
    return f'''
  <section class="dsection" id="ideas">
    <div class="dsection-label">Ideas</div>
    <h2>Used in ideas</h2>
    <p>Product concepts from the <a href="/ideas.html">GONGBANS inventor</a> that build on this board — concepts, not products; not validated.</p>
    <div class="files-list">{items}</div>
  </section>'''


def render_board(g, index, ideas_by_board=None):
    curated = g.get("origin") != "db"
    issuer = g.get("issuer") or ("ATU (Taiwan distributor) · hand-curated kit" if curated else "")
    head_id = g.get("project_no") or g.get("issuer") or ""
    description = (g.get("application") or f'{g["name"]} — {issuer}'.strip(" —"))[:200]
    status = "full-pack" if g.get("files_available") else g.get("status", "metadata-only")
    openness = "hosted" if g.get("files_available") else g.get("openness", "")
    openness_label = OPENNESS_PLAIN.get(openness) or g.get("openness_label", "")

    meta = []
    def item(label, value_html, cls=""):
        if value_html:
            meta.append(f'<div class="detail-meta-item"><span class="detail-meta-label">{e(label)}</span><span class="detail-meta-value{(" " + cls) if cls else ""}">{value_html}</span></div>')
    item("Category", f'<a href="/boards.html#cat={quote(g["category"])}">{e(g["category"])}</a>')
    item("Issuer", f'<a href="/boards.html#issuer={quote(g["issuer"])}">{e(g["issuer"])}</a>' if g.get("issuer") else e(issuer))
    item("Chip", e(g.get("chip")), "gold")
    item("Chip brand", e(g.get("chip_brand")))
    item("Host MCU", e(g.get("mcu_chip")), "gold")
    if g.get("chip_price_5k_usd"):
        item("Chip price · 5k pcs", f"${g['chip_price_5k_usd']:.2f}", "gold")
    if openness_label:
        item("Openness", f'<span class="openness-pill {OPENNESS_CLASS.get(openness, "neutral")}">{e(openness_label)}</span>')
    item("Year", e(g.get("year")))
    kinds = sorted((g.get("files") or {}).keys()) if g.get("files_available") else (g.get("files_avail") or [])
    if kinds:
        item("Files", e(", ".join(KIND_LABEL.get(k, k) for k in kinds)))
    if g.get("source_url"):
        item("Source", ext_link(g["source_url"], "Issuer page ↗"))
    if g.get("datasheet_url"):
        item("Datasheet", ext_link(g["datasheet_url"], "PDF ↗"))

    app = (g.get("application") or "").strip()
    app_html = f"<p>{e(app)}</p>" if app else ""
    if g.get("hint"):
        app_html += f"<p>Product name per the issuer's schematic file: <strong>{e(g['hint'])}</strong>.</p>"
    if not app_html:
        app_html = "<p class='muted'>No description published by the issuer — see the source link.</p>"
    tags = " · ".join(e(t) for t in g.get("tags", []))

    files_html = hosted_files_section(g) if g.get("files_available") else source_files_section(g)
    title = f'{g["name"]}{f" — {head_id}" if head_id and head_id != g["name"] else ""} · GONGBANS catalogue'
    return f'''{head(title, description, f"db/{g['slug']}.html")}
<body>
{nav("boards")}

<div class="page-header">
  <div class="page-header-inner">
    <div class="crumbs"><a href="/boards.html">Catalogue</a><span class="sep">/</span><a href="/boards.html#cat={quote(g["category"])}">{e(g["category"])}</a><span class="sep">/</span><span>{e(head_id or g["name"])}</span></div>
    {f'<div class="header-id">{e(head_id)}</div>' if head_id else ''}
    <h1>{e(g["name"])}</h1>
    <p class="sub">{e(description if app else (issuer or ""))}</p>
  </div>
</div>

<main class="detail">
  <div class="detail-meta">{"".join(meta)}</div>

  <section class="dsection" id="application">
    <div class="dsection-label">What it is</div>
    <h2>Application</h2>
    {app_html}
    {f'<div class="tags">TAGS · {tags}</div>' if tags else ''}
  </section>
{silicon_section(g)}
{files_html}
{bom_section(g)}
{source_section(g)}
{hans_note_section(g)}
{related_section(g, index)}{ideas_section(g, ideas_by_board or {})}
  <p class="catalogue-note">Entry <code>{e(g["slug"])}</code>{" · status: " + e(status)}. Catalogue entries are indexed from publishers' public pages; the site re-hosts nothing except the hand-curated design packs. Spotted an error? <a href="https://hansstam.eu">Get in touch via hansstam.eu</a>.</p>
</main>

{FOOTER}
</body>
</html>
'''


# ---------------------------------------------------------------------------
# issuers page
# ---------------------------------------------------------------------------
def render_issuers(data, stats):
    cards = []
    for it in data["board_issuers"]:
        srcs = " · ".join(ext_link(s["url"], "source ↗") for s in it["sources"][:2])
        cats = ", ".join(it["categories"][:3])
        region = f" · {e(it['region'])}" if it.get("region") else ""
        cards.append(f'''
    <article class="issuer">
      <div class="issuer-type">{e(it["type_label"])}{region}</div>
      <div class="issuer-name">{e(it["name"])}</div>
      <div class="issuer-products">{e(cats)}</div>
      <div class="issuer-foot"><span><a href="/boards.html#issuer={quote(it["name"])}"><strong>{it["count"]:,}</strong> board{"s" if it["count"] != 1 else ""} →</a></span><span>{srcs}</span></div>
    </article>''')

    groups = defaultdict(list)
    for h in data["solution_houses"]:
        groups[h["category"]].append(h)
    house_html = []
    for cat in sorted(groups):
        items = []
        for h in groups[cat]:
            site = ext_link("https://" + h["website"], h["website"]) if h["website"] else ""
            items.append(f'''
      <article class="issuer">
        <div class="issuer-type">{e(h["subcategory"] or cat)}</div>
        <div class="issuer-name">{e(h["company_en"])}</div>
        {f'<div class="issuer-cn" lang="zh">{e(h["company_cn"])}</div>' if h["company_cn"] else ''}
        <div class="issuer-products">{e(" · ".join(h["key_products"]))}</div>
        <div class="issuer-foot"><span>{site}</span><span>{e(cat)}</span></div>
      </article>''')
        house_html.append(f'''
  <div class="sh-group">
    <h3>{e(cat)} <span>{len(items)} compan{"ies" if len(items) != 1 else "y"}</span></h3>
    <div class="issuer-grid">{"".join(items)}</div>
  </div>''')

    n_iss, n_houses = len(data["board_issuers"]), len(data["solution_houses"])
    desc = f"Who publishes gongbans: the {n_iss} chip houses, distributors, module houses and maker brands behind the {stats['boards']:,} boards in the catalogue, plus a directory of {n_houses} Shenzhen solution houses with public company information."
    return f'''{head("Issuers — who publishes gongbans — GONGBANS", desc, "issuers.html", "website")}
<body>
{nav("issuers")}

<div class="page-header">
  <div class="page-header-inner wide">
    <div class="page-header-tag">Issuers · publishers &amp; solution houses</div>
    <h1>Who <em>publishes</em> gongbans</h1>
    <p class="sub">The catalogue indexes {stats['boards']:,} boards from {n_iss} publishers — chip houses, distributors, module houses, maker brands and one open-hardware community. Below them, a directory of {n_houses} Shenzhen-area solution houses and ODMs that design to order. Public company information only: names, category, website, key products.</p>
  </div>
</div>

<div class="context-bar">
  <div class="context-inner">
    <div class="context-note"><strong>How to read it:</strong> a <em>publisher</em> put design files or documentation online — click the board count to open its boards in the catalogue. A <em>solution house</em> is a company that designs and manufactures to order; most of them never publish a file, which is exactly why a directory is useful. Industrial SOM platforms from Kingbrother are on <a href="/boards-kingbrother.html">their own page</a>.</div>
    <div class="context-source">Source · <span>gongban.db · {e(data["updated"])}</span></div>
  </div>
</div>

<main class="catalogue">
  <section class="category" id="publishers">
    <div class="category-head">
      <h2 class="category-title">Publishers in the catalogue</h2>
      <span class="category-meta">{n_iss} publishers · {stats['boards']:,} boards</span>
    </div>
    <div class="issuer-grid">{"".join(cards)}</div>
  </section>

  <section class="category" id="solution-houses">
    <div class="category-head">
      <h2 class="category-title">Solution-house directory</h2>
      <span class="category-meta">{n_houses} companies · {len(groups)} categories</span>
    </div>
    <p class="catalogue-note" style="margin:0 0 28px;font-size:14px">Shenzhen-area design houses, ODMs and module makers grouped by what they build. Company names in English and Chinese, website and key products as stated publicly. No contact details are published here; use the company website.</p>
    {"".join(house_html)}
  </section>
</main>

{FOOTER}
</body>
</html>
'''


# ---------------------------------------------------------------------------
# stats patching for hand-written pages
# ---------------------------------------------------------------------------
def patch_stats(path, stats):
    if not path.exists():
        return 0
    src = path.read_text(encoding="utf-8")
    n = 0
    def repl(m):
        nonlocal n
        key = m.group(1)
        val = stats.get(key)
        if val is None:
            return m.group(0)
        n += 1
        return f'{m.group(0).split(">", 1)[0]}>{val:,}</span>' if isinstance(val, int) else f'{m.group(0).split(">", 1)[0]}>{e(val)}</span>'
    out = re.sub(r'<span data-stat="([a-z_]+)"[^>]*>[^<]*</span>', repl, src)
    cats = "".join(f'<a href="/boards.html#cat={quote(c["name"])}">{e(c["name"])}<small>{c["count"]:,}</small></a>' for c in stats["per_category"])
    out, k = re.subn(r"(<!-- stat-cats -->).*?(<!-- /stat-cats -->)", lambda m: f"{m.group(1)}{cats}{m.group(2)}", out, flags=re.S)
    if out != src:
        path.write_text(out, encoding="utf-8")
    return n + k


# hand-written pages: nav, footer and asset version are rewritten so they match the generated pages
STATIC_PAGES = {"index.html": ("", HOME_EXTRA), "start.html": ("start", ()), "boards.html": ("boards", ()),
                "what-are-gongbans.html": ("what", ()), "boards-kingbrother.html": ("boards", ())}


def patch_chrome(path, active, extra=()):
    if not path.exists():
        return 0
    src = path.read_text(encoding="utf-8")
    out, n1 = re.subn(r'<nav class="site-nav">.*?</nav>', lambda m: nav(active, extra), src, count=1, flags=re.S)
    out, n2 = re.subn(r'<footer class="site-footer">.*?</footer>\s*<script src="/assets/site\.js[^"]*"></script>',
                      lambda m: FOOTER, out, count=1, flags=re.S)
    out = re.sub(r'(/assets/[a-z]+\.(?:css|js)\?v=)[0-9A-Za-z]+', lambda m: m.group(1) + ASSET_V, out)
    if out != src:
        path.write_text(out, encoding="utf-8")
    return n1 + n2


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    gongbans = manifest["gongbans"]
    stats = json.loads(STATS.read_text(encoding="utf-8"))
    index = RelatedIndex(gongbans)
    ideas_by_board = load_ideas_by_board()

    wanted = set()
    for g in gongbans:
        out = DB_DIR / f"{g['slug']}.html"
        wanted.add(out.name)
        out.write_text(render_board(g, index, ideas_by_board), encoding="utf-8")
    stale = [p for p in DB_DIR.glob("*.html") if p.name not in wanted]
    for p in stale:
        p.unlink()
    print(f"db/: {len(wanted)} pages written, {len(stale)} stale removed, {sum(1 for g in gongbans if g['slug'] in ideas_by_board)} with 'Used in ideas'")

    issuers = json.loads(ISSUERS.read_text(encoding="utf-8"))
    (ROOT / "issuers.html").write_text(render_issuers(issuers, stats), encoding="utf-8")
    print(f"issuers.html: {len(issuers['board_issuers'])} publishers, {len(issuers['solution_houses'])} solution houses")

    for name, (active, extra) in STATIC_PAGES.items():
        k = patch_chrome(ROOT / name, active, extra)
        print(f"{name}: nav/footer {'patched' if k == 2 else 'NOT patched (' + str(k) + '/2)'}, {patch_stats(ROOT / name, stats)} stat(s) patched")


if __name__ == "__main__":
    main()
