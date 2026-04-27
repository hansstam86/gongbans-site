#!/usr/bin/env python3
"""
build_detail_pages.py — generate one HTML page per gongban
from data/gongbans.json into db/<slug>.html

Run from the gongbans-db root directory:
    python3 build_detail_pages.py
"""

import json
import html
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = ROOT / "data" / "gongbans.json"
DB_DIR = ROOT / "db"

DB_DIR.mkdir(exist_ok=True)


def file_link_html(label: str, file_type: str, path: str) -> str:
    return f'''
        <a class="file-link" href="../{path}" download>
          <span class="file-icon">{file_type}</span>
          <span class="file-name">{html.escape(label)}</span>
        </a>'''


def files_section(g: dict) -> str:
    if not g.get("files_available"):
        return f'''
    <section class="section" id="files">
      <h3 class="section-label">Files</h3>
      <div class="section-body">
        <p style="color: var(--silkscreen-faded); font-style: italic;">
          No design pack uploaded yet for this entry. Catalog metadata only —
          chip identification and datasheet link are above.
        </p>
      </div>
    </section>'''

    files = g.get("files", {})
    links = []
    type_map = {
        "schematic": ("SCH", "Schematic"),
        "pcb":       ("PCB", "PCB Layout"),
        "gerber":    ("ZIP", "Gerber files"),
        "bom":       ("XLSX", "Bill of Materials"),
        "spec":      ("DOCX", "Specification document"),
        "presentation": ("PPTX", "Reference presentation"),
        "datasheets": ("DIR", "Component datasheets"),
    }
    for key, (icon, label) in type_map.items():
        if key in files:
            links.append(file_link_html(label, icon, files[key]))

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


def bom_section(g: dict) -> str:
    bom = g.get("bom_summary")
    if not bom:
        return ""

    rows = []
    for k, v in bom.items():
        label = k.replace("_", " ").upper()
        rows.append(f"<tr><td>{html.escape(label)}</td><td>{html.escape(str(v))}</td></tr>")

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


def hans_note_section(g: dict) -> str:
    note = g.get("hans_notes", "").strip()
    is_pending = note.lower().startswith("hans note pending")
    cls = "hans-note pending" if is_pending else "hans-note"
    label = "Sourcing Note — Pending" if is_pending else "Hans's Sourcing Note"

    return f'''
    <section class="section" id="notes">
      <h3 class="section-label">Notes from Hans</h3>
      <div class="section-body">
        <div class="{cls}">
          <div class="hans-note-label">{label}</div>
          <p class="hans-note-body">{html.escape(note)}</p>
        </div>
      </div>
    </section>'''


def related_section(g: dict, all_gongbans: list) -> str:
    """Find related entries by chip brand or shared tags."""
    related = []
    for other in all_gongbans:
        if other["slug"] == g["slug"]:
            continue
        if other["chip"] == g["chip"] or (
            other.get("chip_brand") == g.get("chip_brand")
            and set(other.get("tags", [])) & set(g.get("tags", []))
        ):
            related.append(other)

    if not related:
        return ""

    related = related[:4]
    items = []
    for r in related:
        items.append(f'''
          <a class="file-link" href="{r["slug"]}.html">
            <span class="file-icon">{html.escape(r["project_no"][:8])}</span>
            <span class="file-name">{html.escape(r["name"])}</span>
          </a>''')

    return f'''
    <section class="section" id="related">
      <h3 class="section-label">Related Gongbans</h3>
      <div class="section-body">
        <p style="margin-bottom: 1.25rem;">
          Other entries that share this chip, brand, or application area.
        </p>
        <div class="files-list">{"".join(items)}</div>
      </div>
    </section>'''


def render_page(g: dict, all_gongbans: list) -> str:
    name = html.escape(g["name"])
    chip = html.escape(g["chip"])
    brand = html.escape(g.get("chip_brand", ""))
    role = html.escape(g.get("chip_role", ""))
    app = html.escape(g["application"])
    price = g.get("chip_price_5k_usd")
    price_html = f"${price:.2f}" if price else "—"
    datasheet = g.get("datasheet_url", "")

    mcu_block = ""
    if g.get("mcu_chip"):
        mcu_block = f'''
        <div class="detail-meta-item">
          <span class="detail-meta-label">Host MCU</span>
          <span class="detail-meta-value">{html.escape(g["mcu_chip"])}</span>
        </div>'''

    tags_block = ""
    if g.get("tags"):
        tags_block = " · ".join(html.escape(t) for t in g["tags"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — {g["project_no"]} · GONGBANS DB</title>
<meta name="description" content="{html.escape(g["application"])[:200]}">
<link rel="stylesheet" href="../assets/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%230a3d22'/%3E%3Ccircle cx='50' cy='50' r='30' fill='none' stroke='%23d4b06a' stroke-width='6'/%3E%3Ccircle cx='50' cy='50' r='10' fill='%230a3d22'/%3E%3C/svg%3E">
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="../index.html" class="brand">
      <span class="brand-mark">GONGBANS<span style="color: var(--silkscreen);">/</span>DB</span>
      <span class="brand-sub">公板数据库</span>
    </a>
    <nav class="site-nav">
      <a href="../index.html">Catalog</a>
      <a href="https://hansolo42.gumroad.com/l/gongbans" target="_blank" rel="noopener">The Book ↗</a>
      <a href="https://hansstam.eu" target="_blank" rel="noopener">Hans</a>
    </nav>
  </div>
</header>

<main class="detail">
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="../index.html">Catalog</a>
    <span class="breadcrumb-sep">/</span>
    <span>{html.escape(g["category"])}</span>
    <span class="breadcrumb-sep">/</span>
    <span>{name}</span>
  </nav>

  <span class="detail-projno">{html.escape(g["project_no"])}</span>
  <h1 class="detail-title">{name}</h1>

  <div class="detail-meta">
    <div class="detail-meta-item">
      <span class="detail-meta-label">Category</span>
      <span class="detail-meta-value">{html.escape(g["category"])}</span>
    </div>
    <div class="detail-meta-item">
      <span class="detail-meta-label">Chip</span>
      <span class="detail-meta-value gold">{chip}</span>
    </div>
    <div class="detail-meta-item">
      <span class="detail-meta-label">Brand</span>
      <span class="detail-meta-value">{brand}</span>
    </div>
    {mcu_block}
    <div class="detail-meta-item">
      <span class="detail-meta-label">Chip price · 5k pcs</span>
      <span class="detail-meta-value gold">{price_html}</span>
    </div>
    <div class="detail-meta-item">
      <span class="detail-meta-label">Datasheet</span>
      <span class="detail-meta-value">
        <a href="{datasheet}" target="_blank" rel="noopener" class="ext" style="color: var(--enig-bright);">{brand} PDF</a>
      </span>
    </div>
  </div>

  <section class="section" id="application">
    <h3 class="section-label">Application</h3>
    <div class="section-body">
      <p>{app}</p>
      {f"<p style='margin-top: 1rem; font-family: var(--font-mono); font-size: 0.78rem; color: var(--silkscreen-faded); letter-spacing: 0.08em;'>TAGS: {tags_block}</p>" if tags_block else ""}
    </div>
  </section>

  <section class="section" id="silicon">
    <h3 class="section-label">Silicon</h3>
    <div class="section-body">
      <div class="card-chip" style="max-width: 360px; margin: 0;">
        <div class="chip-brand">{brand}</div>
        <div class="chip-name">{chip}</div>
        <div class="chip-role">{role}</div>
      </div>
      <p style="margin-top: 1.25rem;">
        Spot price reference at 5k unit volume:
        <strong>${price:.2f}</strong>. Actual price depends on
        distributor (Avnet / Arrow / Future / WPG / local) and current
        allocation. For real-time China market check
        <a href="https://www.hqew.com" target="_blank" rel="noopener" class="ext" style="color: var(--enig-bright);">hqew.com</a>
        or <a href="https://www.lcsc.com" target="_blank" rel="noopener" class="ext" style="color: var(--enig-bright);">LCSC</a>.
      </p>
    </div>
  </section>

  {files_section(g)}
  {bom_section(g)}
  {hans_note_section(g)}
  {related_section(g, all_gongbans)}

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

    for g in gongbans:
        out = DB_DIR / f"{g['slug']}.html"
        html_content = render_page(g, gongbans)
        out.write_text(html_content, encoding="utf-8")
        status = "📦" if g.get("files_available") else "📋"
        print(f"  {status}  {out.relative_to(ROOT)}")

    print(f"\n✓ Done. Open index.html via a local server:")
    print(f"    cd {ROOT.name} && python3 -m http.server 8000")


if __name__ == "__main__":
    main()
