# GONGBANS DB

A static, no-build database of Chinese factory reference designs (gongbans / 公板) — the off-the-shelf hardware that quietly powers consumer electronics. Companion to the book [GONGBANS](https://hansolo42.gumroad.com/l/gongbans).

## What's here

```
gongbans-db/
├── index.html            ← catalog, all 16 entries, filter + search
├── data/gongbans.json    ← the database (single source of truth)
├── db/                   ← one HTML page per gongban (auto-generated)
├── files/                ← downloadable hardware packs
│   ├── uv-sensor-veml6075-lpc824/        [SCH PCB Gerber BOM Spec PPT + 8 datasheets]
│   ├── gesture-vcnl4020-lpc824/          [SCH PCB Gerber BOM Spec PPT + 5 datasheets]
│   └── ble-reference-design-qn9022/      [SCH PCB Gerber BOM Spec PPT + datasheets]
├── assets/
│   ├── style.css         ← PCB-aesthetic theme (solder mask green, ENIG gold, copper)
│   └── app.js            ← catalog filter / search (vanilla, no framework)
├── build_detail_pages.py ← regenerates /db/*.html from gongbans.json
└── README.md
```

## Run locally

```bash
cd gongbans-db
python3 -m http.server 8000
# open http://localhost:8000
```

(Opening `index.html` directly via `file://` won't work — `fetch()` of `data/gongbans.json` needs a real HTTP origin.)

## Adding a new gongban

1. Add an entry to `data/gongbans.json` following the schema (slug, project_no, name, category, chip, etc.).
2. If you have hardware files, drop them in `files/<slug>/` with conventional names: `schematic.sch`, `pcb.pcb`, `gerber.zip`, `bom.xlsx`, `spec.docx`, `presentation.pptx`, `datasheets/*.pdf`.
3. Set `files_available: true` in the manifest.
4. Run `python3 build_detail_pages.py` to regenerate detail pages.

## Editing Hans's sourcing notes

Right now most entries say `"hans_notes": "Hans note pending — ..."`. Each is a placeholder waiting for your real sourcing voice. The detail-page renderer flags pending notes visually so you can see at a glance which ones still need writing.

When you write a real note, the markup automatically switches from "Sourcing Note — Pending" to "Hans's Sourcing Note" in red, with the note styled as a real callout.

## Schema (gongbans.json)

```jsonc
{
  "slug": "uv-sensor-veml6075-lpc824",       // URL-safe identifier
  "project_no": "P15-096",                    // factory project number
  "name": "UV Sensor Demo (VEML6075 + LPC824)",
  "category": "IoT",                          // IoT | Wearable | E-Lock | ...
  "tags": ["sensor", "uv", "i2c"],
  "chip": "VEML6075",                         // hero chip
  "chip_brand": "Vishay",
  "chip_role": "UV-A + UV-B light sensor (I²C)",
  "mcu_chip": "LPC824JHI33",                  // optional, if there's a separate MCU
  "mcu_brand": "NXP",
  "datasheet_url": "https://…",
  "chip_price_5k_usd": 1.09,
  "application": "Reference design for UV index measurement…",
  "files_available": true,
  "files": { /* paths relative to repo root */ },
  "bom_summary": { /* top-level component breakdown */ },
  "hans_notes": "Your sourcing intel goes here."
}
```

## Deploy to GitHub Pages

This is the same setup as the existing gongbans.com (vanilla static, GitHub Pages). Either:

- **Replace** the current gongbans.com repo with this one (book sales page becomes one section linked from the new landing).
- Or **subdirectory** approach: drop this whole folder as `/db/` inside the existing repo and it serves at `gongbans.com/db/`.

Recommend the first: this becomes the new gongbans.com identity, with the book linked prominently in the header (already wired up — see `index.html` nav). The DB is the lead magnet, the book is the depth.

## Why static / no framework

- Drops into any GitHub Pages / Cloudflare Pages / Netlify deploy with zero config.
- No npm, no node_modules, no build step before commit.
- Loads in <50ms over decent connection.
- Anyone can read the source and edit raw HTML.
- Matches the spirit of GONGBANS — physical, honest, no abstractions.

## Roadmap ideas

- Add **photos** of populated boards (each card has a slot for one).
- Add the firmware source repos as Git submodules under `/firmware/<slug>/`.
- Build a **DXT-style firmware browser** (the BLE Reference Design has full WeChat AirSync SDK, would be useful as a reference).
- Add an **RSS/Atom feed** when new gongbans get added.
- Hook up **Pagefind** for full-text search across Hans's sourcing notes (only when there's enough note content to make it worthwhile — ~15+ filled notes).

---

Maintained by [Hans Stam](https://hansstam.eu) · Berlin / Shenzhen / Taipei.
