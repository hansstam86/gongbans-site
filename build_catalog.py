#!/usr/bin/env python3
"""
build_catalog.py — import public boards from the gongban.db master database
into data/gongbans.json, next to the hand-curated entries, and write the
slim files the site loads.

    python3 build_catalog.py [/path/to/gongban.db]
    python3 build_detail_pages.py          # then render db/*.html, issuers.html, stats

Outputs
- data/gongbans.json   source of truth (curated entries kept byte-for-byte + imports)
- data/catalog.json    slim grid data for boards.html
- data/issuers.json    publishers of the boards + public solution-house directory
- data/stats.json      counts used on the home page

Behaviour
- Hand-curated entries (anything without "origin": "db") are kept byte-for-byte.
- All previously imported DB entries are dropped and re-imported (idempotent).
- Tables read: boards, files, sources (name/type/url only — never sources.notes),
  solution_houses (public columns only: company_en, company_cn, category,
  subcategory, website, key_products; rows with `excluded` set are skipped).
  contacts, outreach, fetch_log and fairs are never touched.
- Exclusions (never published): boards tied to shared mobility / GPS tracking /
  e-scooters / e-bikes, the three ATU kits that duplicate curated entries, and
  anything matching an excluded solution-house name. E-mail addresses and FAE
  names are scrubbed from notes. OSHWHub author handles are not published; where
  a handle looks like a phone or QQ number the project link is withheld too.
- Nothing is invented: fields the database does not have stay empty.
"""

import html
import json
import re
import sqlite3
import sys
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
MANIFEST = ROOT / "data" / "gongbans.json"
CATALOG = ROOT / "data" / "catalog.json"
ISSUERS = ROOT / "data" / "issuers.json"
STATS = ROOT / "data" / "stats.json"
DEFAULT_DB = Path.home() / "Projects" / "gongban-db" / "gongban.db"

# ---------------------------------------------------------------------------
# Category grouping: 30+ database categories -> the catalogue's chip set.
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
    "hosted": "Hosted on this site",
}
OPENNESS_SHORT = {
    "open_download": "Open download", "registration": "Registration",
    "with_purchase": "With purchase", "contact_atu": "Via distributor", "community": "Community",
    "hosted": "Hosted here",
}
ISSUER_TYPE_LABEL = {
    "chip_house": "Chip house", "distributor": "Distributor", "solution_house": "Solution house",
    "community": "Community / maker brand", "leak_channel": "Circulating design",
}

# ---------------------------------------------------------------------------
# Exclusions
# ---------------------------------------------------------------------------
DUPLICATE_SLUGS = {"atu-p15-090-ble", "atu-p15-096-uv-sensor", "atu-p15-097-gesture-hub",
                   # WPI ATU 2016 catalogue rows that describe a hand-curated ATU kit (same project code)
                   "wpi-atu-p15-043-wifi-zigbee-gateway-lpc54102", "wpi-atu-p15-080-fis1100-sports-wearable",
                   "wpi-atu-p15-087-zigbee-pir-sensor", "wpi-atu-p15-094-quark-d2000-smart-home-hub",
                   "wpi-atu-p15-098-vcnl4020-proximity-demo", "wpi-atu-p15-099-veml6040-rgbw-demo",
                   "wpi-atu-p16-008-isd9160-voice-recognition-board", "wpi-atu-p16-016-qn9022-ble-module",
                   "wpi-atu-p16-037-zigbee-light-module", "wpi-atu-p16-052-zigbee-module-base-board"}

MOBILITY_RE = re.compile(
    r"scooter|e-?bike|ebike|gps[\s-]?track|\btracker\b|telematic|shared[\s-]?mobility|"
    r"bike[\s-]?shar|云狗|车联网|共享单车|共享电单车|balance_scooter|t-?box",
    re.I)
EXCLUDED_HOUSES_RE = re.compile(
    r"jimi|concox|tbit|queclink|omni smart|eelink|vodofo|meitrack|coban|sinotrack|"
    r"suntech|jointech|bofan|xexun|huabao|teltonika|votol|fardriver|kelly controls|"
    r"lishui|daly|jkbms|topband|linglong|coreride|rikcon|huivision|hosmart|seg navigation|saige",
    re.I)

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
FAE_RE = re.compile(r"\s*FAE:\s*[^.;|]+[.;]?")
CONTACT_RE = re.compile(r"\s*Contact\s+<email>\.?", re.I)
PERSONAL_HANDLE_RE = re.compile(r"^\d{7,}|qq", re.I)      # phone / QQ-number style handles

WPI_SUFFIX_RE = re.compile(r"\s*:\s*(热点频道|熱點頻道)::.*$")
WPI_CHANNELS = ["汽车电子", "汽車電子", "穿戴装置", "穿戴裝置", "智能家居", "智慧家居", "工业电子", "工業電子",
                "LED照明", "记忆体", "記憶體", "电脑及周边", "電腦及周邊", "能源", "电源", "電源", "智能手机",
                "智慧手機", "安全监控", "安全監控", "主机板", "主機板", "医疗电子", "醫療電子", "电视", "電視"]
WPI_PREFIX_RE = re.compile(r"^.{0,40}?(推出|力推)[：:]?\s*")
OSHWHUB_BOILERPLATE = "嘉立创EDA开源硬件平台，开源广场汇集了多种类型的电路设计工程，快速实现资源共享！"
OSHWHUB_NAME_SUFFIX_RE = re.compile(r"\s*[-–—]?\s*立创EDA开源硬件平台\s*$")
DESIGN_KINDS = {"schematic", "pcb", "gerber", "bom", "sch_lib", "pcb_lib"}
MAX_LINKS = 12
CURATED_ISSUER = "ATU kit (curated)"


def safe_slug(slug):
    s = slug.replace("‑", "-").replace("&", "-").replace("°", "deg")
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


def clean_firefly_name(name):
    """Firefly entries are named after the spec PDF: drop the extension and the
    '产品规格书' (product spec) suffix."""
    n = re.sub(r"\.pdf$", "", name, flags=re.I)
    n = re.sub(r"[-_ ]*(产品)?规格书$", "", n).strip(" -_")
    return n.replace("_", " ")


def map_category(b):
    base = CATEGORY_MAP.get(b["category"] or "", "Dev Board")
    if b["source_id"] == "wpi_atu_pages" and (b["category"] or "") in SOFT_WPI_CATEGORIES:
        text = f'{b["name"]} {b["chip"] or ""}'
        for rx, cat in WPI_RULES:
            if rx.search(text):
                return cat
    return base


def dfrobot_hint(file_rows):
    for f in file_rows:
        m = re.search(r"/(?:DFR|SEN|TEL|FIT|TOY|KIT|ROB|SKU)\w*?_([a-z0-9][a-z0-9.-]+?)_schematic", f["url"] or "", re.I)
        if m:
            return m.group(1).replace("-", " ").strip()
    return ""


def application_text(b):
    notes = scrub(b["notes"])
    if b["source_id"] == "oshwhub":
        head = notes.split(" | ")[0].strip()
        return head if head and head != OSHWHUB_BOILERPLATE else ""
    if b["source_id"] == "wpi_atu_pages":
        head = notes.split(" | ")[0].strip()
        return head if not head.startswith("Recovered from") else ""
    return notes


def website_link(site):
    """solution_houses.website is a bare domain, '—', or 'domain (note)'."""
    if not site or site.strip() in {"—", "-", ""}:
        return ""
    m = re.match(r"([a-z0-9.-]+\.[a-z]{2,})", site.strip(), re.I)
    return m.group(1).lower() if m else ""


def main():
    db_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DB
    if not db_path.exists():
        sys.exit(f"database not found: {db_path}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    curated = [g for g in manifest["gongbans"] if g.get("origin") != "db"]
    curated_slugs = {g["slug"] for g in curated}
    for g in curated:                                   # hosted packs must really exist
        for key, rel in (g.get("files") or {}).items():
            if not (ROOT / rel).exists():
                print(f"WARNING: {g['slug']}: files.{key} -> {rel} does not exist")

    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    sources = {r["id"]: dict(r) for r in con.execute("SELECT id, name, issuer_type, url FROM sources")}
    files = {}
    for r in con.execute("SELECT board_slug, kind, url, local_path FROM files ORDER BY kind, url"):
        files.setdefault(r["board_slug"], []).append(dict(r))

    imported, excluded, link_withheld = [], [], 0
    used_slugs = set()
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
        if b["source_id"] == "oshwhub" and (slug.endswith("-undefined") or (b["name"] or "").strip() in {"工程", "undefined", ""}):
            excluded.append((slug, "empty scrape (no project title)")); continue

        src = sources.get(b["source_id"], {})
        rows = files.get(b["slug"], [])
        issuer, name, source_url, source_note = b["issuer"], b["name"], b["source_url"] or "", ""

        if b["source_id"] == "oshwhub":
            handle = issuer.split("·", 1)[1].strip() if "·" in issuer else ""
            issuer = "OSHWHub"                        # author handles are not published
            name = OSHWHUB_NAME_SUFFIX_RE.sub("", html.unescape(name)).strip() or name
            hslug = handle.lower().replace("_", "-")
            if handle and slug.startswith(f"oshwhub-{hslug}-"):
                slug = "oshwhub-" + slug[len(f"oshwhub-{hslug}-"):]
            if handle and PERSONAL_HANDLE_RE.search(handle):
                source_url = ""                       # URL would expose a phone/QQ-style handle
                source_note = "Project page link withheld (author handle looks like a personal number); search the project title on oshwhub.com."
                link_withheld += 1
        elif b["source_id"] == "wpi_atu_pages":
            name = clean_wpi_name(name)
        elif b["source_id"] == "firefly":
            name = clean_firefly_name(name)
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", slug):
            slug = safe_slug(slug)
        if slug in used_slugs or slug in curated_slugs:      # e.g. two OSHWHub projects with the same name
            n = 2
            while f"{slug}-{n}" in used_slugs:
                n += 1
            slug = f"{slug}-{n}"
        used_slugs.add(slug)

        try:
            files_avail = json.loads(b["files_avail"] or "[]")
        except json.JSONDecodeError:
            files_avail = []
        links, seen = [], set()
        for f in rows:
            if f["url"] and f["url"] not in seen:
                seen.add(f["url"])
                links.append({"kind": f["kind"], "url": f["url"],
                              "name": html.unescape(f["url"].rstrip("/").split("/")[-1]).replace("%20", " ")})
        more = max(0, len(links) - MAX_LINKS)
        links = links[:MAX_LINKS]
        for k in {f["kind"] for f in rows}:
            if k not in files_avail:
                files_avail.append(k)

        hint = dfrobot_hint(rows) if b["source_id"] == "dfrobot_wiki" else ""
        category = map_category(b)
        openness = b["openness"] or ""
        design_kinds = sorted(k for k in files_avail if k in DESIGN_KINDS)
        status = "source-files" if (design_kinds or links) else "metadata-only"

        tags = [t for t in [b["category"], OPENNESS_LABEL.get(openness, openness).lower(),
                            (src.get("issuer_type") or "").replace("_", " ")] if t]
        if hint:
            tags.append(hint)

        imported.append({
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
            "origin": "db",
            "issuer": issuer,
            "issuer_type": src.get("issuer_type", ""),
            "source_name": src.get("name", ""),
            "source_url": source_url,
            "source_note": source_note,
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
        })

    # ---- issuers of the boards ----
    board_issuers = OrderedDict()
    for g in imported:
        it = board_issuers.setdefault(g["issuer"], {"name": g["issuer"], "type": g["issuer_type"],
                                                   "type_label": ISSUER_TYPE_LABEL.get(g["issuer_type"], g["issuer_type"]),
                                                   "count": 0, "sources": OrderedDict(), "categories": Counter(), "region": Counter()})
        it["count"] += 1
        it["categories"][g["category"]] += 1
        if g["region"]:
            it["region"][g["region"]] += 1
        src_url = sources.get(next((k for k, s in sources.items() if s["name"] == g["source_name"]), ""), {}).get("url", "")
        if src_url and src_url.startswith("http"):
            it["sources"][g["source_name"]] = src_url
    board_issuers[CURATED_ISSUER] = {"name": CURATED_ISSUER, "type": "distributor", "type_label": "Distributor kits (hand-curated)",
                                     "count": len(curated), "sources": {}, "categories": Counter(g["category"] for g in curated), "region": Counter({"TW": len(curated)})}
    issuers_out = []
    for it in sorted(board_issuers.values(), key=lambda x: -x["count"]):
        issuers_out.append({
            "name": it["name"], "type": it["type"], "type_label": it["type_label"], "count": it["count"],
            "sources": [{"name": n, "url": u} for n, u in it["sources"].items()],
            "categories": [c for c, _ in it["categories"].most_common()],
            "region": it["region"].most_common(1)[0][0] if it["region"] else "",
        })

    # ---- solution-house directory (public columns only, excluded rows skipped) ----
    houses = []
    for r in con.execute("""SELECT company_en, company_cn, category, subcategory, website, key_products
                            FROM solution_houses WHERE excluded IS NULL OR excluded = ''
                            ORDER BY category, company_en"""):
        h = dict(r)
        blob = " ".join(str(v or "") for v in h.values())
        assert not EMAIL_RE.search(blob), f"e-mail in solution house {h['company_en']}"
        assert not EXCLUDED_HOUSES_RE.search(blob), f"excluded house leaked: {h['company_en']}"
        houses.append({
            "company_en": (h["company_en"] or "").strip(),
            "company_cn": (h["company_cn"] or "").strip(),
            "category": (h["category"] or "").strip(),
            "subcategory": (h["subcategory"] or "").strip(),
            "website": website_link(h["website"]),
            "key_products": [p.strip() for p in (h["key_products"] or "").split(";") if p.strip()],
        })
    con.close()

    # ---- write manifest ----
    all_entries = curated + imported
    assert len({g["slug"] for g in all_entries}) == len(all_entries), "duplicate slugs"
    for g in all_entries:
        assert not EMAIL_RE.search(json.dumps(g, ensure_ascii=False)), f"e-mail leaked in {g['slug']}"
    manifest["gongbans"] = all_entries
    manifest["version"] = "0.3.0"
    manifest["updated"] = date.today().isoformat()
    manifest["categories"] = CATEGORY_ORDER
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # ---- slim grid data ----
    slim = []
    for g in all_entries:
        app_text = g.get("application") or ""
        if g.get("origin") == "db" and len(app_text) > 220:
            app_text = app_text[:217].rstrip() + "…"
        curated_entry = g.get("origin") != "db"
        kinds = sorted((g.get("files") or {}).keys()) if curated_entry and g.get("files_available") else list(g.get("files_avail") or [])
        openness = "hosted" if (curated_entry and g.get("files_available")) else (g.get("openness") or "")
        slim.append({
            "slug": g["slug"], "project_no": g.get("project_no", ""), "name": g["name"],
            "category": g["category"], "issuer": g.get("issuer") or (CURATED_ISSUER if curated_entry else ""),
            "chip": g.get("chip", ""), "chip_brand": g.get("chip_brand", ""), "application": app_text,
            "status": "full-pack" if g.get("files_available") else g.get("status", "metadata-only"),
            "openness": openness, "openness_label": OPENNESS_SHORT.get(openness, g.get("openness_label", "")),
            "kinds": kinds, "links": len(g.get("files_at_source") or []) + (len(g.get("files") or {}) if curated_entry else 0),
            "year": g.get("year"), "price": g.get("chip_price_5k_usd"), "tags": g.get("tags", []), "hint": g.get("hint", ""),
        })
    # curated / hosted packs first, then entries with files, then the rest; alphabetical within
    rank = {"full-pack": 0, "source-files": 1, "metadata-only": 2}
    slim.sort(key=lambda s: (0 if s["project_no"] else 1, rank[s["status"]], s["issuer"].lower(), s["name"].lower()))
    CATALOG.write_text(json.dumps({"version": manifest["version"], "updated": manifest["updated"],
                                   "categories": CATEGORY_ORDER, "total": len(slim), "gongbans": slim},
                                  ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")

    # ---- issuers + stats ----
    ISSUERS.write_text(json.dumps({"updated": manifest["updated"], "board_issuers": issuers_out, "solution_houses": houses},
                                  ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    per_cat = Counter(s["category"] for s in slim)
    stats = {
        "updated": manifest["updated"],
        "boards": len(slim),
        "curated": len(curated),
        "imported": len(imported),
        "issuers": len(issuers_out),
        "solution_houses": len(houses),
        "categories": len([c for c in CATEGORY_ORDER if per_cat[c]]),
        "full_packs": sum(1 for s in slim if s["status"] == "full-pack"),
        "with_design_files": sum(1 for s in slim if s["status"] != "metadata-only"),
        "with_schematic": sum(1 for s in slim if "schematic" in s["kinds"]),
        "with_pcb": sum(1 for s in slim if "pcb" in s["kinds"]),
        "direct_links": sum(1 for s in slim if s["links"]),
        "open_download": sum(1 for s in slim if s["openness"] in ("open_download", "hosted")),
        "per_category": [{"name": c, "count": per_cat[c]} for c in CATEGORY_ORDER if per_cat[c]],
        "top_issuers": [{"name": i["name"], "count": i["count"]} for i in issuers_out[:8]],
        "excluded": len(excluded),
    }
    STATS.write_text(json.dumps(stats, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"curated kept: {len(curated)}   imported: {len(imported)}   excluded: {len(excluded)}   oshwhub links withheld: {link_withheld}")
    for slug, why in excluded:
        print(f"  - {slug}: {why}")
    print("per category:", ", ".join(f"{c['name']} {c['count']}" for c in stats["per_category"]))
    print(f"issuers: {len(issuers_out)}   solution houses: {len(houses)}")
    print(f"wrote {MANIFEST.name} ({MANIFEST.stat().st_size/1e3:.0f} KB), {CATALOG.name} ({CATALOG.stat().st_size/1e3:.0f} KB), {ISSUERS.name}, {STATS.name}")


if __name__ == "__main__":
    main()
