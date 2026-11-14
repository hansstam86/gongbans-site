#!/usr/bin/env python3
"""
build_catalog.py — import public boards from the gongban.db master database
into data/gongbans.json, next to the hand-curated entries.

    python3 build_catalog.py [/path/to/gongban.db]

Behaviour
- Hand-curated entries (anything without "origin": "db") are kept byte-for-byte.
- All previously imported DB entries are dropped and re-imported, so the run is
  idempotent. Re-run after the database changes, then build_detail_pages.py.
- Only the `boards`, `files` and `sources` tables are read. contacts, outreach,
  fetch_log, fairs and solution_houses are never touched.
- Exclusions (never published): boards tied to shared mobility / GPS tracking /
  e-scooters / e-bikes, the three ATU kits that duplicate curated entries, and
  anything matching an excluded solution-house name. E-mail addresses and FAE
  names are scrubbed from notes; OSHWHub author handles are not published.
- Nothing is invented: fields the database does not have stay empty.
"""

import html
import json
import re
import sqlite3
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = ROOT / "data" / "gongbans.json"
DEFAULT_DB = Path.home() / "Projects" / "gongban-db" / "gongban.db"

# ---------------------------------------------------------------------------
# Category grouping: 30+ database categories -> the catalogue's chip set.
# Existing site categories (IoT, Wearable, E-Lock) are kept as they are.
# ---------------------------------------------------------------------------
CATEGORY_MAP = {
    "dev_board": "Dev Board", "shield": "Dev Board", "sensor_module": "Dev Board",
    "adapter": "Dev Board", "comms_module": "Dev Board", "motor_driver": "Dev Board",
    "robot_controller": "Dev Board",
    "community_project": "Community",
    "sbc": "SBC / SOM",
    "module_board": "Module", "module_design": "Module", "tof_module": "Module",
    "reference_design": "Reference Design",
    "industrial": "Industrial & Auto", "automotive": "Industrial & Auto",
    "energy": "Industrial & Auto", "medical": "Industrial & Auto",
    "wearable": "Wearable", "smartwatch": "Wearable", "smartband": "Wearable",
    "smart_home": "IoT", "security": "IoT", "led_lighting": "IoT",
    "smart_lock": "E-Lock",
    "phone": "Consumer", "tv": "Consumer", "pc": "Consumer", "bt_speaker": "Consumer",
    "tws": "Consumer", "power_adapter": "Consumer", "memory": "Consumer",
}
CATEGORY_ORDER = ["IoT", "Wearable", "E-Lock", "Dev Board", "Community", "SBC / SOM",
                  "Module", "Reference Design", "Industrial & Auto", "Consumer"]

# WPI's archived "hot channel" pages were filed under the page's channel
# (memory, PC...) rather than the product. Re-file the soft ones by keyword.
SOFT_WPI_CATEGORIES = {"memory", "pc", "industrial", "security", "smart_home",
                       "phone", "tv", "led_lighting"}
WPI_RULES = [
    (re.compile(r"车载|車載|automotive|autobody|mirror|后视镜|後視鏡|行车记录", re.I), "Industrial & Auto"),
    (re.compile(r"网关|網關|gateway|homesecurity|安防|security|智能家居|smart ?home|lighting|照明|ip ?camera|surveillance|网络摄像", re.I), "IoT"),
    (re.compile(r"手机|手機|smartphone|平板|tablet|电视|電視|\btv\b", re.I), "Consumer"),
    (re.compile(r"server|ipc|工业电脑|工業電腦", re.I), "Industrial & Auto"),
]

OPENNESS_LABEL = {
    "open_download": "Open download",
    "registration": "Free registration",
    "with_purchase": "With purchase",
    "contact_atu": "Via distributor (ATU)",
    "community": "Community",
}

OPENNESS_SHORT = {
    "open_download": "Open download", "registration": "Registration",
    "with_purchase": "With purchase", "contact_atu": "Via distributor", "community": "Community",
}

# ---------------------------------------------------------------------------
# Exclusions
# ---------------------------------------------------------------------------
# Duplicates of hand-curated entries (P15-090 / P15-096 / P15-097 packs).
DUPLICATE_SLUGS = {"atu-p15-090-ble", "atu-p15-096-uv-sensor", "atu-p15-097-gesture-hub"}

# Shared mobility / GPS tracking / e-scooter / e-bike — never published.
MOBILITY_RE = re.compile(
    r"scooter|e-?bike|ebike|gps[\s-]?track|\btracker\b|telematic|shared[\s-]?mobility|"
    r"bike[\s-]?shar|云狗|车联网|共享单车|共享电单车|balance_scooter|t-?box",
    re.I)
# Excluded solution houses (solution_houses.excluded = 'voi-mobility') — by name.
EXCLUDED_HOUSES_RE = re.compile(
    r"jimi|concox|tbit|queclink|omni smart|eelink|vodofo|meitrack|coban|sinotrack|"
    r"suntech|jointech|bofan|xexun|huabao|teltonika|votol|fardriver|kelly controls|"
    r"lishui|daly|jkbms|topband|linglong|coreride|rikcon|huivision|hosmart|seg navigation|saige",
    re.I)

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
FAE_RE = re.compile(r"\s*FAE:\s*[^.;|]+[.;]?")
CONTACT_RE = re.compile(r"\s*Contact\s+<email>\.?", re.I)
PHONE_LIKE_RE = re.compile(r"^\d{7,}")

WPI_SUFFIX_RE = re.compile(r"\s*:\s*(热点频道|熱點頻道)::.*$")
WPI_CHANNELS = ["汽车电子", "汽車電子", "穿戴装置", "穿戴裝置", "智能家居", "智慧家居", "工业电子", "工業電子",
                "LED照明", "记忆体", "記憶體", "电脑及周边", "電腦及周邊", "能源", "电源", "電源", "智能手机",
                "智慧手機", "安全监控", "安全監控", "主机板", "主機板", "医疗电子", "醫療電子", "电视", "電視"]
WPI_PREFIX_RE = re.compile(r"^.{0,40}?(推出|力推)[：:]?\s*")
OSHWHUB_BOILERPLATE = "嘉立创EDA开源硬件平台，开源广场汇集了多种类型的电路设计工程，快速实现资源共享！"
DESIGN_KINDS = {"schematic", "pcb", "gerber", "bom", "sch_lib", "pcb_lib"}
MAX_LINKS = 12


def safe_slug(slug):
    """File-system/URL-safe slug for the handful of DB slugs with odd characters."""
    s = slug.replace("\u2011", "-").replace("&", "-").replace("\u00b0", "deg")
    s = re.sub(r"[^a-z0-9._-]+", "-", s.lower())
    return re.sub(r"-{2,}", "-", s).strip("-")


def scrub(text):
    """Remove e-mail addresses and named contacts from free text."""
    if not text:
        return ""
    text = EMAIL_RE.sub("<email>", text)
    text = CONTACT_RE.sub("", text)
    text = text.replace("<email>", "")
    text = FAE_RE.sub("", text)
    text = html.unescape(text).replace("\xa0", " ")
    return re.sub(r"[ \t]+", " ", text).strip()


def clean_wpi_name(name):
    name = html.unescape(name).replace("\xa0", " ")
    name = WPI_SUFFIX_RE.sub("", name).strip()
    for ch in WPI_CHANNELS:
        if name.startswith(ch + "-"):
            name = name[len(ch) + 1:]
            break
    for ch in WPI_CHANNELS:
        if name.endswith(ch) and len(name) > len(ch) + 4:
            name = name[: -len(ch)]
            break
    name = WPI_PREFIX_RE.sub("", name, count=1)
    return name.strip(" -~：:")


def map_category(b):
    base = CATEGORY_MAP.get(b["category"] or "", "Dev Board")
    if b["source_id"] == "wpi_atu_pages" and (b["category"] or "") in SOFT_WPI_CATEGORIES:
        text = f'{b["name"]} {b["chip"] or ""}'
        for rx, cat in WPI_RULES:
            if rx.search(text):
                return cat
    return base


def dfrobot_hint(file_rows):
    """DFRobot boards are named by SKU only; the schematic file name carries
    the product name (DFR0979_ch423-io-expansion_schematics_1.0.pdf)."""
    for f in file_rows:
        m = re.search(r"/(?:DFR|SEN|TEL|FIT|TOY|DFR|KIT|ROB|SKU)\w*?_([a-z0-9][a-z0-9.-]+?)_schematic", f["url"] or "", re.I)
        if m:
            return m.group(1).replace("-", " ").strip()
    return ""


def application_text(b):
    notes = scrub(b["notes"])
    if b["source_id"] == "oshwhub":
        head = notes.split(" | ")[0].strip()
        if head and head != OSHWHUB_BOILERPLATE:
            return head
        return ""
    if b["source_id"] == "wpi_atu_pages":
        head = notes.split(" | ")[0].strip()
        # keep the product description, drop the ingestion provenance tail
        return head if not head.startswith("Recovered from") else ""
    return notes


def main():
    db_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DB
    if not db_path.exists():
        sys.exit(f"database not found: {db_path}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    curated = [g for g in manifest["gongbans"] if g.get("origin") != "db"]
    curated_slugs = {g["slug"] for g in curated}

    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    sources = {r["id"]: dict(r) for r in con.execute("SELECT id, name, issuer_type, url FROM sources")}
    files = {}
    for r in con.execute("SELECT board_slug, kind, url, local_path FROM files ORDER BY kind, url"):
        files.setdefault(r["board_slug"], []).append(dict(r))

    imported, excluded, stats = [], [], {}
    for r in con.execute("SELECT * FROM boards ORDER BY issuer, name"):
        b = dict(r)
        slug = b["slug"]
        probe = " ".join(str(b.get(k) or "") for k in ("slug", "name", "issuer", "chip", "category", "notes"))

        if slug in DUPLICATE_SLUGS:
            excluded.append((slug, "duplicate of curated entry")); continue
        if MOBILITY_RE.search(probe):
            excluded.append((slug, "shared-mobility / tracking")); continue
        if EXCLUDED_HOUSES_RE.search(probe):
            excluded.append((slug, "excluded solution house")); continue
        if slug in curated_slugs:
            excluded.append((slug, "slug collides with curated entry")); continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", slug):
            slug = safe_slug(slug)                    # e.g. "m5stack-hat-env‑iii" (U+2011 hyphen)

        src = sources.get(b["source_id"], {})
        try:
            files_avail = json.loads(b["files_avail"] or "[]")
        except json.JSONDecodeError:
            files_avail = []
        rows = files.get(slug, [])
        links, seen = [], set()
        for f in rows:
            if f["url"] and f["url"] not in seen:
                seen.add(f["url"])
                links.append({"kind": f["kind"], "url": f["url"],
                              "name": html.unescape(f["url"].rstrip("/").split("/")[-1]).replace("%20", " ")})
        more = max(0, len(links) - MAX_LINKS)
        links = links[:MAX_LINKS]

        issuer = b["issuer"]
        if b["source_id"] == "oshwhub":
            issuer = "OSHWHub"                        # author handles are not published
        name = b["name"]
        if b["source_id"] == "wpi_atu_pages":
            name = clean_wpi_name(name)
        hint = dfrobot_hint(rows) if b["source_id"] == "dfrobot_wiki" else ""

        category = map_category(b)
        openness = b["openness"] or ""
        design_kinds = sorted(k for k in files_avail if k in DESIGN_KINDS)
        if design_kinds or links:
            status = "source-files"
        else:
            status = "metadata-only"

        tags = [t for t in [b["category"], OPENNESS_LABEL.get(openness, openness).lower(),
                            src.get("issuer_type", "").replace("_", " ")] if t]
        if hint:
            tags.append(hint)

        entry = {
            "slug": slug,
            "db_slug": b["slug"],
            "project_no": "",
            "name": name,
            "category": category,
            "tags": tags,
            "chip": b["chip"] or "",
            "chip_brand": "",
            "chip_role": "",
            "datasheet_url": "",
            "chip_price_5k_usd": None,
            "application": application_text(b),
            "files_available": False,
            "hans_notes": "",
            # --- fields added for database imports ---
            "origin": "db",
            "issuer": issuer,
            "issuer_type": src.get("issuer_type", ""),
            "source_name": src.get("name", ""),
            "source_url": b["source_url"] or "",
            "db_category": b["category"] or "",
            "openness": openness,
            "openness_label": OPENNESS_LABEL.get(openness, openness),
            "year": b["year"],
            "region": b["region"] or "",
            "license": b["license"] or "",
            "files_avail": files_avail,
            "files_at_source": links,
            "files_at_source_more": more,
            "status": status,
            "notes": scrub(b["notes"]),
            "hint": hint,
        }
        imported.append(entry)
        stats[category] = stats.get(category, 0) + 1

    con.close()

    all_entries = curated + imported
    assert len({g["slug"] for g in all_entries}) == len(all_entries), "duplicate slugs"
    for g in all_entries:
        assert not EMAIL_RE.search(json.dumps(g, ensure_ascii=False)), f"e-mail leaked in {g['slug']}"

    manifest["gongbans"] = all_entries
    manifest["version"] = "0.2.0"
    manifest["updated"] = date.today().isoformat()
    manifest["categories"] = CATEGORY_ORDER
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    CATALOG = ROOT / "data" / "catalog.json"
    slim = []
    for g in all_entries:
        app_text = g.get("application") or ""
        if g.get("origin") == "db" and len(app_text) > 220:
            app_text = app_text[:217].rstrip() + "…"
        slim.append({
            "slug": g["slug"], "project_no": g.get("project_no", ""), "name": g["name"],
            "category": g["category"], "issuer": g.get("issuer", ""), "chip": g.get("chip", ""),
            "chip_brand": g.get("chip_brand", ""), "application": app_text,
            "status": "full-pack" if g.get("files_available") else g.get("status", "metadata-only"),
            "openness_label": OPENNESS_SHORT.get(g.get("openness", ""), g.get("openness_label", "")), "year": g.get("year"),
            "price": g.get("chip_price_5k_usd"), "tags": g.get("tags", []), "hint": g.get("hint", ""),
        })
    CATALOG.write_text(json.dumps({"version": manifest["version"], "updated": manifest["updated"],
                                   "categories": CATEGORY_ORDER, "total": len(slim), "gongbans": slim},
                                  ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"wrote {CATALOG} ({CATALOG.stat().st_size/1e3:.0f} KB, grid data)")
    print(f"curated kept: {len(curated)}   imported: {len(imported)}   excluded: {len(excluded)}")
    for slug, why in excluded:
        print(f"  - {slug}: {why}")
    print("per category (all entries):")
    for g in curated:
        stats[g["category"]] = stats.get(g["category"], 0) + 1
    for c in CATEGORY_ORDER:
        print(f"  {c:18s} {stats.get(c, 0)}")
    print(f"wrote {MANIFEST} ({MANIFEST.stat().st_size/1e3:.0f} KB)")


if __name__ == "__main__":
    main()
