#!/usr/bin/env python3
"""
build_detail_pages.py — generate one HTML page per gongban
from data/gongbans.json into db/<slug>.html

Run from the repo root:
    python3 build_detail_pages.py

Handles both the hand-curated entries (chip, price, datasheet, local design
pack, Hans's notes) and the entries imported from gongban.db by
build_catalog.py (issuer, source page, openness, files published at source).
Fields that are empty are simply not rendered — nothing is invented.
"""

import json
import html
import re
from urllib.parse import urlencode
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = ROOT / "data" / "gongbans.json"
DB_DIR = ROOT / "db"

DB_DIR.mkdir(exist_ok=True)

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Crect width='100' height='100' fill='%230a3d22'/%3E%3Ccircle cx='50' cy='50' r='30' fill='none' "
           "stroke='%23d4b06a' stroke-width='6'/%3E%3Ccircle cx='50' cy='50' r='10' fill='%230a3d22'/%3E%3C/svg%3E")

KIND_ICON = {
    "schematic": "SCH", "pcb": "PCB", "gerber": "GBR", "bom": "BOM", "spec": "SPEC",
    "firmware": "FW", "bsp": "BSP", "enclosure": "3D", "mech": "MECH", "photos": "IMG",
    "block_diagram": "BLK", "pcb_lib": "LIB", "sch_lib": "LIB", "artwork": "ART",
}
KIND_LABEL = {
    "schematic": "Schematic", "pcb": "PCB layout", "gerber": "Gerber files", "bom": "Bill of materials",
    "spec": "Specification", "firmware": "Firmware", "bsp": "BSP / software", "enclosure": "Enclosure (3D)",
    "mech": "Mechanical drawings", "photos": "Photos", "block_diagram": "Block diagram",
    "pcb_lib": "PCB library", "sch_lib": "Schematic library", "artwork": "Artwork",
}
OPENNESS_TEXT = {
    "open_download": "Published for open download by the issuer.",
    "registration": "Available after free registration on the issuer's site.",
    "with_purchase": "Design files are handed over with a purchase of the board.",
    "contact_atu": "Design files are released through the distributor's FAE channel (WPI / ATU), not published.",
    "community": "Circulates through community channels rather than an official publication.",
}


def e(s) -> str:
    return html.escape(str(s or ""))


def ext_link(url: str, label: str) -> str:
    return (f'<a href="{e(url)}" target="_blank" rel="noopener" class="ext" '
            f'style="color: var(--enig-bright); word-break: break-all;">{e(label)}</a>')


def file_link_html(label: str, file_type: str, path: str, download=True, external=False) -> str:
    attrs = ' download' if download else ''
    name_style = ''
    if external:
        attrs = ' target="_blank" rel="noopener"'
        name_style = ' style="word-break: break-all; font-size: 0.8rem;"'
    return f'''
        <a class="file-link" href="{e(path)}"{attrs}>
          <span class="file-icon">{e(file_type)}</span>
          <span class="file-name"{name_style}>{e(label)}</span>
        </a>'''


def files_section(g: dict) -> str:
    # 1) curated entry with a design pack hosted on this site
    if g.get("files_available"):
        files = g.get("files", {})
        type_map = {
            "schematic": ("SCH", "Schematic"),
            "pcb":       ("PCB", "PCB Layout"),
            "gerber":    ("ZIP", "Gerber files"),
            "bom":       ("XLSX", "Bill of Materials"),
            "spec":      ("DOCX", "Specification document"),
            "presentation": ("PPTX", "Reference presentation"),
            "datasheets": ("DIR", "Component datasheets"),
        }
        links = [file_link_html(label, icon, "../" + files[key]) for key, (icon, label) in type_map.items() if key in files]
        return f'''
    <section class="section" id="files">
      <h3 class="section-label">Files</h3>
      <div class="section-body">
        <p style="margin-bottom: 1.25rem;">
          Full design pack — schematic, PCB, gerber, BOM, firmware reference,
          and the original spec document. Use as a starting point, not a
          drop-in production design.
        </p>
        <div class="files-list">{"".join(links)}</div>
      </div>
    </section>'''

    # 2) imported entry: files published by the issuer
    links = g.get("files_at_source") or []
    kinds = g.get("files_avail") or []
    source_url = g.get("source_url", "")
    openness_text = OPENNESS_TEXT.get(g.get("openness", ""), "")

    if links:
        items = [file_link_html(f.get("name") or f["url"], KIND_ICON.get(f["kind"], f["kind"][:4].upper()),
                                f["url"], download=False, external=True) for f in links]
        more = g.get("files_at_source_more") or 0
        more_html = (f'<p style="margin-top: 1rem;">+{more} more file(s) on the {ext_link(source_url, "source page")}.</p>'
                     if more and source_url else "")
        kinds_html = (f'<p style="margin-bottom: 1.25rem;">Published by the issuer as: '
                      f'<strong>{e(", ".join(KIND_LABEL.get(k, k) for k in kinds))}</strong>. '
                      f'Links open the issuer\'s own files — nothing is re-hosted here.</p>')
        return f'''
    <section class="section" id="files">
      <h3 class="section-label">Design files at source</h3>
      <div class="section-body">
        {kinds_html}
        <div class="files-list">{"".join(items)}</div>
        {more_html}
      </div>
    </section>'''

    if kinds:
        where = f' Open the {ext_link(source_url, "source page")} to get them.' if source_url else ""
        return f'''
    <section class="section" id="files">
      <h3 class="section-label">Design files at source</h3>
      <div class="section-body">
        <p>Published by the issuer as: <strong>{e(", ".join(KIND_LABEL.get(k, k) for k in kinds))}</strong>.
        Not mirrored on this site.{where}</p>
        {f"<p>{e(openness_text)}</p>" if openness_text else ""}
      </div>
    </section>'''

    where = f' See the {ext_link(source_url, "source page")}.' if source_url else ""
    return f'''
    <section class="section" id="files">
      <h3 class="section-label">Files</h3>
      <div class="section-body">
        <p style="color: var(--silkscreen-faded); font-style: italic;">
          No design files are published for this entry — catalog metadata only.{where}
        </p>
        {f"<p>{e(openness_text)}</p>" if openness_text else ""}
      </div>
    </section>'''


def bom_section(g: dict) -> str:
    bom = g.get("bom_summary")
    if not bom:
        return ""
    rows = [f"<tr><td>{e(k.replace('_', ' ').upper())}</td><td>{e(v)}</td></tr>" for k, v in bom.items()]
    return f'''
    <section class="section" id="bom">
      <h3 class="section-label">BOM Summary</h3>
      <div class="section-body">
        <p style="margin-bottom: 1.25rem;">
          Top-level components only. Full bill of materials is in the
          downloadable XLSX above — including every passive, value, package,
          tolerance, and brand reference.
        </p>
        <table class="bom-table">
          <thead><tr><th>Designator</th><th>Part</th></tr></thead>
          <tbody>{"".join(rows)}</tbody>
        </table>
      </div>
    </section>'''


def source_section(g: dict) -> str:
    """Provenance block for entries imported from gongban.db."""
    if g.get("origin") != "db":
        return ""
    rows = []
    def row(label, value_html):
        if value_html:
            rows.append(f"<tr><td>{e(label)}</td><td>{value_html}</td></tr>")
    row("Issuer", e(g.get("issuer")))
    if g.get("source_url"):
        row("Source page", ext_link(g["source_url"], g["source_url"][:90] + ("…" if len(g["source_url"]) > 90 else "")))
    row("Source", e(g.get("source_name")))
    row("Issuer type", e((g.get("issuer_type") or "").replace("_", " ")))
    row("Openness", e(g.get("openness_label")))
    row("Year", e(g.get("year")))
    row("Region", e(g.get("region")))
    row("License", e(g.get("license")))
    row("Database category", e(g.get("db_category")))
    notes = (g.get("notes") or "").strip()
    notes_html = f'<p style="margin-top: 1.25rem;">{e(notes)}</p>' if notes and notes != g.get("application") else ""
    return f'''
    <section class="section" id="source">
      <h3 class="section-label">Source</h3>
      <div class="section-body">
        <table class="bom-table">
          <tbody>{"".join(rows)}</tbody>
        </table>
        {notes_html}
      </div>
    </section>'''


def hans_note_section(g: dict) -> str:
    note = (g.get("hans_notes") or "").strip()
    if not note:
        return ""
    is_pending = note.lower().startswith("hans note pending")
    cls = "hans-note pending" if is_pending else "hans-note"
    label = "Sourcing Note — Pending" if is_pending else "Hans's Sourcing Note"
    return f'''
    <section class="section" id="notes">
      <h3 class="section-label">Notes from Hans</h3>
      <div class="section-body">
        <div class="{cls}">
          <div class="hans-note-label">{label}</div>
          <p class="hans-note-body">{e(note)}</p>
        </div>
      </div>
    </section>'''


def chip_key(chip: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (chip or "").lower())


class RelatedIndex:
    """Pre-indexed lookups so 1,100+ pages don't cost O(n²)."""

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


def related_section(g: dict, index: RelatedIndex) -> str:
    related = index.related(g)
    if not related:
        return ""
    items = []
    for r in related:
        tag = (r.get("project_no") or r.get("issuer") or r.get("category") or "")[:10]
        items.append(f'''
          <a class="file-link" href="{e(r["slug"])}.html">
            <span class="file-icon">{e(tag)}</span>
            <span class="file-name">{e(r["name"])}</span>
          </a>''')
    return f'''
    <section class="section" id="related">
      <h3 class="section-label">Related Gongbans</h3>
      <div class="section-body">
        <p style="margin-bottom: 1.25rem;">
          Other entries that share this chip, issuer, or application area.
        </p>
        <div class="files-list">{"".join(items)}</div>
      </div>
    </section>'''


def silicon_section(g: dict, brand: str, chip: str, role: str, price) -> str:
    if not chip:
        return ""
    price_html = ""
    if price:
        price_html = f'''
      <p style="margin-top: 1.25rem;">
        Spot price reference at 5k unit volume:
        <strong>${price:.2f}</strong>. Actual price depends on
        distributor (Avnet / Arrow / Future / WPG / local) and current
        allocation. For real-time China market check
        {ext_link("https://www.hqew.com", "hqew.com")}
        or {ext_link("https://www.lcsc.com", "LCSC")}.
      </p>'''
    return f'''
  <section class="section" id="silicon">
    <h3 class="section-label">Silicon</h3>
    <div class="section-body">
      <div class="card-chip" style="max-width: 360px; margin: 0;">
        {f'<div class="chip-brand">{brand}</div>' if brand else ''}
        <div class="chip-name">{chip}</div>
        {f'<div class="chip-role">{role}</div>' if role else ''}
      </div>{price_html}
    </div>
  </section>'''


def render_page(g: dict, index: RelatedIndex) -> str:
    name = e(g["name"])
    chip = e(g.get("chip"))
    brand = e(g.get("chip_brand"))
    role = e(g.get("chip_role"))
    app = e(g.get("application"))
    price = g.get("chip_price_5k_usd")
    datasheet = g.get("datasheet_url", "")
    project_no = g.get("project_no") or ""
    issuer = g.get("issuer") or ""
    head_id = project_no or issuer
    description = (g.get("application") or f'{g["name"]} — {issuer}'.strip(" —"))[:200]

    meta_items = [f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Category</span>
      <span class="detail-meta-value">{e(g["category"])}</span>
    </div>''']
    if issuer:
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Issuer</span>
      <span class="detail-meta-value">{e(issuer)}</span>
    </div>''')
    if chip:
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Chip</span>
      <span class="detail-meta-value gold">{chip}</span>
    </div>''')
    if brand:
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Brand</span>
      <span class="detail-meta-value">{brand}</span>
    </div>''')
    if g.get("mcu_chip"):
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Host MCU</span>
      <span class="detail-meta-value">{e(g["mcu_chip"])}</span>
    </div>''')
    if price:
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Chip price · 5k pcs</span>
      <span class="detail-meta-value gold">${price:.2f}</span>
    </div>''')
    if datasheet:
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Datasheet</span>
      <span class="detail-meta-value">{ext_link(datasheet, f"{g.get('chip_brand', '')} PDF".strip())}</span>
    </div>''')
    if g.get("openness_label"):
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Openness</span>
      <span class="detail-meta-value">{e(g["openness_label"])}</span>
    </div>''')
    if g.get("year"):
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Year</span>
      <span class="detail-meta-value">{e(g["year"])}</span>
    </div>''')
    if g.get("source_url"):
        meta_items.append(f'''
    <div class="detail-meta-item">
      <span class="detail-meta-label">Source</span>
      <span class="detail-meta-value">{ext_link(g["source_url"], "Issuer page")}</span>
    </div>''')

    tags_block = " · ".join(e(t) for t in g.get("tags", []))
    app_block = f"<p>{app}</p>" if app else ""
    if g.get("hint"):
        app_block += f"<p style='margin-top: 1rem;'>Product name per the issuer's schematic file: <strong>{e(g['hint'])}</strong>.</p>"
    if not app_block and not tags_block:
        app_block = "<p style='color: var(--silkscreen-faded); font-style: italic;'>No description published — see the source page.</p>"

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name}{f" — {e(head_id)}" if head_id else ""} · GONGBANS DB</title>
<meta name="description" content="{e(description)}">
<link rel="stylesheet" href="../assets/style.css">
<link rel="icon" href="{FAVICON}">
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="../boards.html" class="brand">
      <span class="brand-mark">GONGBANS<span style="color: var(--silkscreen);">/</span>DB</span>
      <span class="brand-sub">公板数据库</span>
    </a>
    <nav class="site-nav">
      <a href="../boards.html">Catalog</a>
      <a href="../what-are-gongbans.html" class="nav-secondary">What are gongbans?</a>
      <a href="https://hansolo42.gumroad.com/l/gongbans" target="_blank" rel="noopener">The Book ↗</a>
      <a href="https://hansstam.eu" target="_blank" rel="noopener">Hans</a>
    </nav>
  </div>
</header>

<main class="detail">
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="../boards.html">Catalog</a>
    <span class="breadcrumb-sep">/</span>
    <a href="../boards.html#{e(urlencode({"cat": g["category"]}))}">{e(g["category"])}</a>
    <span class="breadcrumb-sep">/</span>
    <span>{name}</span>
  </nav>

  {f'<span class="detail-projno">{e(head_id)}</span>' if head_id else ''}
  <h1 class="detail-title">{name}</h1>

  <div class="detail-meta">{"".join(meta_items)}
  </div>

  <section class="section" id="application">
    <h3 class="section-label">Application</h3>
    <div class="section-body">
      {app_block}
      {f"<p style='margin-top: 1rem; font-family: var(--font-mono); font-size: 0.78rem; color: var(--silkscreen-faded); letter-spacing: 0.08em;'>TAGS: {tags_block}</p>" if tags_block else ""}
    </div>
  </section>
{silicon_section(g, brand, chip, role, price)}
  {files_section(g)}
  {bom_section(g)}
  {source_section(g)}
  {hans_note_section(g)}
  {related_section(g, index)}

</main>

<footer class="site-footer">
  <div class="site-footer-inner">
    <div>
      Maintained by <a href="https://hansstam.eu" target="_blank" rel="noopener">Hans Stam</a> · Berlin · Shenzhen
    </div>
    <div>
      Companion to <a href="https://hansolo42.gumroad.com/l/gongbans" target="_blank" rel="noopener">GONGBANS — the book</a>
    </div>
  </div>
</footer>

</body>
</html>
'''


def main():
    with open(MANIFEST, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    gongbans = manifest["gongbans"]
    print(f"Building {len(gongbans)} detail pages...")
    index = RelatedIndex(gongbans)

    wanted = set()
    for g in gongbans:
        out = DB_DIR / f"{g['slug']}.html"
        wanted.add(out.name)
        out.write_text(render_page(g, index), encoding="utf-8")

    # remove pages for entries that no longer exist (e.g. newly excluded boards)
    stale = [p for p in DB_DIR.glob("*.html") if p.name not in wanted]
    for p in stale:
        p.unlink()

    packs = sum(1 for g in gongbans if g.get("files_available"))
    print(f"  📦 {packs} with design packs · 📋 {len(gongbans) - packs} catalog entries · 🗑 {len(stale)} stale pages removed")
    print(f"\n✓ Done. Open boards.html via a local server:")
    print(f"    cd {ROOT.name} && python3 -m http.server 8000")


if __name__ == "__main__":
    main()
