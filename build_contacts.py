#!/usr/bin/env python3
"""
build_contacts.py — "Who to contact" for every founder start pack, from gongban.db.

    data/contacts.json          the public supplier directory slice used by the packs
    startpacks/<slug>.md        section "## 4. Who to contact" inserted/refreshed between the
                                <!-- who-to-contact:start --> … <!-- who-to-contact:end --> markers
                                (the old "## 4. Next steps" becomes "## 5. Next steps")

Matching is deliberately conservative and transparent:

  board publishers   every board an idea is built from is traced to boards.issuer → sources in
                     gongban.db. A publisher is a *company* (M5Stack, Seeed Studio, Espressif,
                     SIMCom, Jieli, WPI ATU) or a *community platform* (OSHWHub, where the author
                     is an individual and no company exists). Only company publishers count as a
                     match.
  directory          solution_houses rows (public columns only, `excluded` rows skipped) matched
                     to the idea by product category / tag. Always labelled "category match, not
                     idea-specific" on the page — these are real companies on file, not verified
                     suppliers for the idea.
  manufacturing      the PCBA/EMS houses on file (Kingbrother source, Foxlink directory row).

Never exported (see CLAUDE.md): contacts, outreach, fairs, fetch_log, sources.notes,
solution_houses.wechat/email/notes/district, excluded rows, e-mail addresses, personal names,
WeChat IDs, OSHWHub author handles, OSHWHub project links. `check()` asserts that.

Run from the repo root:  python3 build_contacts.py        (needs ~/Projects/gongban-db/gongban.db;
                                                           without it, the committed JSON is reused)
build_ideas.py calls patch_packs() before rendering the packs.
"""

import json
import re
import sqlite3
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
DB = Path.home() / "Projects" / "gongban-db" / "gongban.db"
IDEAS_JSON = ROOT / "data" / "ideas.json"
CONTACTS_JSON = ROOT / "data" / "contacts.json"
CATALOG_JSON = ROOT / "data" / "catalog.json"
PACK_DIR = ROOT / "startpacks"

START = "<!-- who-to-contact:start -->"
END = "<!-- who-to-contact:end -->"
SECTION_RE = re.compile(r"^## 4\. Who to contact\s*$", re.M)
NEXT_RE = re.compile(r"^## \d\. Next steps", re.M)

# issuer (boards.issuer / catalog issuer) → how it is presented. Only facts that are in the db.
PUBLISHER_KIND = {
    "M5Stack": "company", "Seeed Studio": "company", "Espressif": "company", "SIMCom": "company",
    "Jieli 杰理": "company", "ATU kit (curated)": "company", "DFRobot": "company", "OSHWHub": "platform",
    "Hi-Link": "company", "HopeRF": "company", "Tuya": "company",          # round-2 ideas (17 Nov 2026)
}
ISSUER_SOURCE = {   # issuer → sources.id (boards in the db carry it; curated ATU kits do not)
    "M5Stack": "m5stack_github", "Seeed Studio": "seeed_wiki", "Espressif": "espressif_github",
    "SIMCom": "simcom", "Jieli 杰理": "jieli_circulating", "ATU kit (curated)": "wpi_atu_pages", "DFRobot": "dfrobot_wiki", "OSHWHub": "oshwhub",
    "Hi-Link": "hilink_brochure_2026", "HopeRF": "hoperf_github_2026", "Tuya": "tuya_public_docs_2026",
}
ISSUER_HOUSE = {    # issuer → solution_houses.id of the same company, when the directory has it
    "Seeed Studio": 97, "Jieli 杰理": 53, "ATU kit (curated)": 62,
    "Hi-Link": 101, "HopeRF": 102, "Tuya": 55,
}
PUBLISHER_LABEL = {
    "M5Stack": "M5Stack", "Seeed Studio": "Seeed Studio", "Espressif": "Espressif", "SIMCom": "SIMCom",
    "Jieli 杰理": "Jieli Technology (杰理)", "ATU kit (curated)": "WPI ATU (distributor kits)", "DFRobot": "DFRobot", "OSHWHub": "OSHWHub community designs",
    "Hi-Link": "Hi-Link (海凌科)", "HopeRF": "HopeRF (华普微)", "Tuya": "Tuya Smart (涂鸦智能)",
}
ISSUER_TYPE_LABEL = {"chip_house": "Chip house", "distributor": "Distributor", "solution_house": "Solution house",
                     "community": "Community / maker brand", "leak_channel": "Circulating schematic (not an official release)",
                     "module_maker": "Module maker", "platform_module_maker": "Platform + module maker"}
WHAT_TO_ASK = {
    "company": "sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.",
}

# directory matches: (label shown on the page, predicate over the idea, solution_houses ids)
EMS_HOUSE_IDS = [85]            # Foxlink (SZ) — PCBA + cable assembly EMS
DIRECTORY_RULES = [
    ("LoRaWAN gateways / modules", lambda i: "lorawan" in i["tags"], [38, 39]),
    ("E-ink display modules", lambda i: "e-paper" in i["tags"], [88]),
    ("Smart-metering / energy IoT", lambda i: "energy" in i["tags"], [100]),
    ("Industrial RS485 / Modbus gateways", lambda i: {"rs485", "industrial"} & set(i["tags"]), [59, 60]),
    ("Edge-AI / SOM boards and Linux BSPs", lambda i: {"ai-edge", "sbc", "linux"} & set(i["tags"]), [95, 96, 94, 61]),
    ("Smart-home modules and app platform", lambda i: "smart-home" in i["tags"], [33, 55]),
    ("Audio: speaker / earphone ODMs and the Jieli chip house", lambda i: "audio" in i["tags"], [53, 25, 26, 31]),
    ("Custom Li-Po / NiMH batteries", lambda i: "battery" in i["tags"] or "Battery" in i["certification"], [84]),
    ("ESP32 / ESP8266 modules", lambda i: "wifi" in i["tags"] or any(b["issuer"] == "Espressif" for b in i["built_from"]), [35]),
    ("BLE modules and beacons", lambda i: "ble" in i["tags"], [36, 37]),
    ("Cellular (Cat-1 / NB-IoT) modules", lambda i: "cellular" in i["tags"], [99, 98]),
    ("NFC / RFID readers", lambda i: {"nfc", "rfid"} & set(i["tags"]), [70, 68]),
    ("POS / payment terminals and barcode scanners", lambda i: "pos" in i["tags"], [91, 70]),
    ("Commercial displays / signage", lambda i: "displays" in i["tags"] and "e-paper" not in i["tags"], [67]),
    ("mmWave radar sensor modules", lambda i: "radar" in i["tags"], [101]),
    ("LoRa / sub-GHz radio chips and modules", lambda i: {"lora", "sub-ghz"} & set(i["tags"]), [102]),
    ("Matter / Tuya smart-home modules and app platform", lambda i: {"matter", "tuya-cloud"} & set(i["tags"]), [33, 55]),
]

# ---------------------------------------------------------------------------
# export from the db (public columns only)
# ---------------------------------------------------------------------------

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
FORBIDDEN_WORDS = re.compile(r"wechat|微信|whatsapp|\bqq\b|handle", re.I)


def site(s):
    """solution_houses.website is a bare domain, '—', '' or 'domain (note)'."""
    s = (s or "").strip()
    if not s or s == "—":
        return ""
    return s.split(" ")[0]


def export(con, ideas):
    """Return the contacts.json dict from the live db."""
    sources = {r["id"]: dict(r) for r in con.execute("SELECT id, name, issuer_type, url FROM sources")}
    houses = {}
    for r in con.execute("""SELECT id, company_en, company_cn, category, subcategory, website, key_products
                            FROM solution_houses WHERE excluded IS NULL OR excluded = '' ORDER BY id"""):
        houses[r["id"]] = {
            "id": r["id"], "company_en": r["company_en"], "company_cn": r["company_cn"] or "",
            "category": r["category"] or "", "subcategory": r["subcategory"] or "",
            "website": site(r["website"]),
            "key_products": [p.strip() for p in (r["key_products"] or "").split(";") if p.strip()],
        }
    counts = dict(con.execute("SELECT issuer, COUNT(*) FROM boards GROUP BY issuer").fetchall())
    counts["ATU kit (curated)"] = sum(1 for g in json.loads(CATALOG_JSON.read_text())["gongbans"] if g.get("issuer") == "ATU kit (curated)")

    publishers = {}
    for issuer, kind in PUBLISHER_KIND.items():
        src = sources[ISSUER_SOURCE[issuer]]
        h = houses.get(ISSUER_HOUSE.get(issuer))
        publishers[issuer] = {
            "label": PUBLISHER_LABEL[issuer], "kind": kind,
            "issuer_type": ISSUER_TYPE_LABEL.get(src["issuer_type"], src["issuer_type"]),
            "source_name": src["name"], "source_url": src["url"] if src["url"].startswith("http") else "",
            "boards_in_catalogue": counts.get(issuer, 0),
            "house": h,
        }

    # manufacturing on file: Kingbrother is a source (PCB fab + EMS) with its own site page; Foxlink is a directory row
    kb = sources["kingbrother"]
    manufacturing = [{"label": "Kingbrother / King Brother Technology", "what": "PCB fab + EMS", "website": kb["url"],
                      "site_page": "/boards-kingbrother.html", "source_name": kb["name"]}]
    for hid in EMS_HOUSE_IDS:
        h = houses[hid]
        manufacturing.append({"label": h["company_en"], "company_cn": h["company_cn"], "what": h["subcategory"],
                              "website": h["website"], "key_products": h["key_products"]})

    # ManThink: a supplier that submitted its own open gateway, with a reference price in the board notes.
    # The notes are the only MOQ/price data in the whole db; quoted here as "supplier reference price".
    mt = con.execute("SELECT slug, name, notes FROM boards WHERE source_id = 'manthink_direct'").fetchone()
    manthink = None
    if mt:
        m = re.search(r"Supplier reference price \(([^)]*)\): (.*?)\. EU band", mt["notes"])
        manthink = {"label": "ManThink", "website": sources["manthink_direct"]["url"], "board_slug": mt["slug"], "board_name": mt["name"],
                    "what": "open-source LoRaWAN gateway (direct supplier submission)",
                    "reference_price": (f"Supplier reference price ({m.group(1)}): {m.group(2)}. MOQ and lead time on request." if m else "")}

    return {"generated": date.today().isoformat(), "source": "gongban.db (public columns only)",
            "publishers": publishers, "houses": houses, "manufacturing": manufacturing, "manthink": manthink}


def check(data):
    """Refuse to write anything that looks like a private contact."""
    blob = json.dumps(data, ensure_ascii=False)
    assert not EMAIL_RE.search(blob), "e-mail address in contacts export"
    assert not FORBIDDEN_WORDS.search(blob), "private channel word in contacts export"
    assert "oshwhub.com/project" not in blob, "OSHWHub project link in contacts export"
    for key in ("person", "wechat", "email", "district", "notes", "handle"):
        assert f'"{key}"' not in blob, f"private column {key} in contacts export"


# ---------------------------------------------------------------------------
# per-idea matching
# ---------------------------------------------------------------------------

def match(idea, data):
    pubs = {}
    for b in idea["built_from"]:
        pubs.setdefault(b["issuer"], []).append(b)
    company = [iss for iss in pubs if data["publishers"].get(iss, {}).get("kind") == "company"]
    platform = [iss for iss in pubs if data["publishers"].get(iss, {}).get("kind") == "platform"]
    unknown = [iss for iss in pubs if iss not in data["publishers"]]
    directory = []
    seen = {data["publishers"][iss]["house"]["id"] for iss in company if data["publishers"][iss].get("house")}
    for label, pred, ids in DIRECTORY_RULES:
        if pred(idea):
            rows = [data["houses"][i] for i in ids if i in data["houses"]]
            rows = [r for r in rows if r["id"] not in seen]
            seen.update(r["id"] for r in rows)
            if rows:
                directory.append((label, rows))
    return {"company": company, "platform": platform, "unknown": unknown, "boards": pubs, "directory": directory,
            "status": "matched" if company else "unmatched"}


# ---------------------------------------------------------------------------
# markdown for the section
# ---------------------------------------------------------------------------

def board_link(b):
    return f'[{b["board_name"]}](/db/{b["board_slug"]}.html)'


def house_line(h, prefix="**"):
    cn = f" ({h['company_cn']})" if h.get("company_cn") else ""
    web = f" · {h['website']}" if h.get("website") else " · no website on file"
    prods = "; ".join(h.get("key_products", [])[:4])
    sub = h.get("subcategory") or h.get("category") or ""
    return f"{prefix}{h['company_en']}{prefix}{cn}{web} — {sub}: {prods}."


def email_blocks(idea, m, data):
    boards = [b for iss in m["company"] for b in m["boards"][iss]]
    board_list = ", ".join(dict.fromkeys(b["board_name"] for b in boards)) if boards else "[board names]"
    open_boards = [b for iss in m["platform"] for b in m["boards"][iss]]
    open_list = ", ".join(dict.fromkeys(b["board_name"] for b in open_boards)) or board_list
    pitch = idea["pitch"].rstrip(".")
    title = idea["title"]
    out = []
    if m["company"]:
        out.append(f"""**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the {" and ".join(data["publishers"][i]["label"] for i in m["company"])} website{"s" if len(m["company"]) > 1 else ""})

```email
Subject: Sample order and volume pricing — {board_list} — for a {title}

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a {title}: {pitch}. The design is built around your {board_list}.

Could you please send:
1. Price and lead time for [10] sample units of each: {board_list}.
2. Unit pricing at 100 / 500 / 1,000 pieces, EXW Shenzhen and DDP [your city], including packaging.
3. Whether a customised variant is possible (our enclosure, connector, or firmware pre-loaded), with the NRE and MOQ for it.
4. Radio test reports or module certification documents, if available, so we can plan EU (CE/RED) certification.
5. Payment terms and accepted methods for a first order.

We can share our block diagram and target quantities under NDA if that helps.

Best regards,
[your name] · [your company] · [website] · [phone / WhatsApp]
```

**A. 中文版**

```email
主题：样品订购及批量报价 — {board_list} — 用于{title}

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款{title}：{pitch}。产品设计基于贵司的{board_list}。

请提供以下信息：
1. 各[10]片样品的单价和交期：{board_list}。
2. 100 / 500 / 1,000 片的批量单价（深圳EXW及DDP到[城市]），含包装。
3. 是否可以定制（外壳、接口或预烧录固件），以及定制的NRE费用和最小起订量（MOQ）。
4. 如有，请提供射频测试报告或模组认证文件，以便我们规划欧盟CE/RED认证。
5. 首单的付款方式和条件。

如有需要，我们可在签署NDA后提供框图和目标数量。

祝好，
[姓名] · [公司] · [网站] · [电话 / WhatsApp]
```
""")
    out.append(f"""**B. To a PCBA / EMS house — quote from the open design files** (send to Kingbrother, Foxlink or any assembler you vet; see the [playbook](/playbook.html#manufacturer))

```email
Subject: PCBA quote from open design files — {title}, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a {title}: {pitch}. The design starts from published open-hardware files ({open_list}; schematic, PCB and BOM available) with our own modifications.

Could you quote:
1. PCB fabrication + SMT assembly for [50] prototype units and [500 / 1,000] production units, including component sourcing (we provide the BOM with manufacturer part numbers).
2. NRE, stencil and test-fixture costs, and your DFM review fee if any.
3. Lead time from file approval to shipment, and your QC / functional-test process.
4. Box build (enclosure, cable, packaging) if you offer it.
5. Terms: EXW / FOB Shenzhen or DDP [your city]; payment terms for a first order.

Design files: [link to Gerber, BOM and pick-and-place files].

Best regards,
[your name] · [your company] · [website] · [phone / WhatsApp]
```

**B. 中文版**

```email
主题：基于开源设计文件的PCBA报价 — {title}，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款{title}：{pitch}。设计基于已公开的开源硬件文件（{open_list}；含原理图、PCB和BOM），并做了我们自己的修改。

请报价：
1. [50]台样机和[500 / 1,000]台量产的PCB制板+SMT贴片，含元器件采购（我们提供带厂商料号的BOM）。
2. NRE、钢网和测试治具费用，以及DFM评审费用（如有）。
3. 从文件确认到出货的交期，以及贵司的QC/功能测试流程。
4. 如可提供，整机组装（外壳、线材、包装）报价。
5. 贸易条款：深圳EXW/FOB或DDP到[城市]；首单付款条件。

设计文件：[Gerber、BOM和坐标文件链接]。

祝好，
[姓名] · [公司] · [网站] · [电话 / WhatsApp]
```
""")
    return "\n".join(out)


def section_md(idea, m, data):
    L = []
    n_company = len(m["company"])
    if m["status"] == "matched":
        who = " and ".join(data["publishers"][i]["label"] for i in m["company"])
        L.append(f"**On file: {n_company} board publisher{'s' if n_company != 1 else ''} ({who}).** "
                 "Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards "
                 "this idea is built from, the manufacturers on file, and directory entries in the same product category. "
                 "None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. "
                 "Company websites only; no personal contacts are published.")
    else:
        L.append("**No verified company contact on file yet for this idea.** Every board it is built from is a community design on OSHWHub, "
                 "where the author is an individual, not a supplier. Nothing has been invented to fill the gap: once section 2 (validate demand) has passed, use the manufacturing houses "
                 "and the directory entries below, follow the [zero-experience founder playbook](/playbook.html), and treat the first quote "
                 "you get as the real data. Company websites only; no personal contacts are published.")
    L.append("")
    # board publishers
    if m["company"]:
        L.append("### Board publishers (direct)")
        L.append("")
        for iss in m["company"]:
            p = data["publishers"][iss]
            h = p["house"]
            head = f"**{p['label']}**"
            if h:
                head += f" ({h['company_cn']}" + (f", {h['website']}" if h["website"] else "") + ")"
            parts = [f"{head} — {p['issuer_type'].lower()}; {p['boards_in_catalogue']} boards in the catalogue; files via {p['source_name']}"
                     + (f" · {p['source_url']}" if p["source_url"] else "") + "."]
            if h:
                parts.append(f"Directory entry: {h['subcategory']}: {'; '.join(h['key_products'][:5])}.")
            if iss == "Jieli 杰理":
                parts.append("The schematic in the catalogue is a circulating standard design, not an official release; ask the company for the current reference design.")
            if iss == "ATU kit (curated)":
                parts.append("The kit files are hosted here; WPI's application unit published them for its distribution customers.")
            if iss == "Hi-Link":
                parts.append("Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly.")
            if iss == "Tuya":
                parts.append("Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side.")
            if iss == "HopeRF":
                parts.append("HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence).")
            boards = "; ".join(f"{board_link(b)} ({b['role']})" for b in m["boards"][iss])
            parts.append(f"Boards used here: {boards}.")
            parts.append(f"What to ask for: {WHAT_TO_ASK['company']}")
            L.append("- " + " ".join(parts))
        L.append("")
    if m["platform"]:
        L.append("### Open-hardware boards without a company behind them")
        L.append("")
        for iss in m["platform"]:
            p = data["publishers"][iss]
            boards = "; ".join(f"{board_link(b)} ({b['role']})" for b in m["boards"][iss])
            L.append(f"- **{p['label']}** — community projects on {p['source_name']} · {p['source_url']} . The author is an individual, "
                     f"not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) "
                     f"and check each project's licence first. Boards used here: {boards}.")
        L.append("")
    # manufacturing
    L.append("### Manufacturing (PCBA / EMS) on file")
    L.append("")
    for mf in data["manufacturing"]:
        cn = f" ({mf['company_cn']})" if mf.get("company_cn") else ""
        extra = f"; see the [Kingbrother SOM page]({mf['site_page']}) on this site" if mf.get("site_page") else ""
        prods = f": {'; '.join(mf['key_products'][:4])}" if mf.get("key_products") else ""
        L.append(f"- **{mf['label']}**{cn} · {mf['website']} — {mf['what']}{prods}{extra}.")
    if "lorawan" in idea["tags"] and data.get("manthink"):
        mt = data["manthink"]
        L.append(f"- **{mt['label']}** · {mt['website']} — {mt['what']}: [{mt['board_name']}](/db/{mt['board_slug']}.html). {mt['reference_price']}")
    L.append("")
    # directory
    if m["directory"]:
        L.append("### Also in the directory (category match, not idea-specific)")
        L.append("")
        L.append("Companies in the gongban.db solution-house directory whose product category overlaps this idea. "
                 "They were matched on the idea's tags, not on this design; none has seen it.")
        L.append("")
        for label, rows in m["directory"]:
            for h in rows:
                L.append(f"- {house_line(h)} *({label})*")
        L.append("")
    # MOQ / landed cost
    L.append("### MOQ and landed cost")
    L.append("")
    has_mt = "lorawan" in idea["tags"] and data.get("manthink")
    L.append(("Apart from the ManThink reference price above, " if has_mt else "") +
             "gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. "
             "Get the numbers from the quote (the e-mail below asks for them) and run them through the "
             "[landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.")
    L.append("")
    L.append("### Outreach e-mail, ready to send")
    L.append("")
    L.append("Fill in the [brackets], keep it short, and send it to the sales or \"contact us\" address on the company's own website. "
             "The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).")
    L.append("")
    L.append(email_blocks(idea, m, data))
    return "\n".join(L).rstrip() + "\n"


# ---------------------------------------------------------------------------
# patch the pack markdown
# ---------------------------------------------------------------------------

def patch_md(md, section):
    block = f"{START}\n{section}{END}"
    if START in md and END in md:
        md = md[:md.index(START)] + block + md[md.index(END) + len(END):]
    else:
        md = re.sub(r"^## 4\. Next steps", "## 5. Next steps", md, count=1, flags=re.M)
        m = NEXT_RE.search(md)
        if not m:
            raise SystemExit("pack has no Next steps section")
        md = md[:m.start()] + "## 4. Who to contact\n\n" + block + "\n\n" + md[m.start():]
    return md


def load_data(con=None):
    ideas = json.loads(IDEAS_JSON.read_text(encoding="utf-8"))["ideas"]
    if con is None and DB.exists():
        con = sqlite3.connect(DB)
        con.row_factory = sqlite3.Row
    if con is not None:
        data = export(con, ideas)
        check(data)
        CONTACTS_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"data/contacts.json: {len(data['publishers'])} publishers, {len(data['houses'])} directory rows, {len(data['manufacturing'])} manufacturers (from gongban.db)")
    else:
        data = json.loads(CONTACTS_JSON.read_text(encoding="utf-8"))
        print("data/contacts.json: gongban.db not found, reusing the committed export")
    data["houses"] = {int(k): v for k, v in data["houses"].items()}
    return ideas, data


def patch_packs():
    ideas, data = load_data()
    matched, unmatched = [], []
    for idea in ideas:
        path = PACK_DIR / f"{idea['slug']}.md"
        if not path.exists():
            continue
        m = match(idea, data)
        assert not m["unknown"], f"{idea['slug']}: issuer not in db: {m['unknown']}"
        (matched if m["status"] == "matched" else unmatched).append(idea["slug"])
        md = path.read_text(encoding="utf-8")
        new = patch_md(md, section_md(idea, m, data))
        assert not EMAIL_RE.search(new[new.index(START):new.index(END)]), f"{idea['slug']}: e-mail address in generated section"
        if new != md:
            path.write_text(new, encoding="utf-8")
    packed = [i["slug"] for i in ideas if (PACK_DIR / f"{i['slug']}.md").exists()]
    no_block = [s for s in packed if START not in (PACK_DIR / f"{s}.md").read_text(encoding="utf-8")]
    assert not no_block, f"'Who to contact' missing in: {no_block}"
    assert len(matched) + len(unmatched) == len(packed)
    print(f"startpacks/: 'Who to contact' in {len(matched) + len(unmatched)} packs — {len(matched)} with a company publisher on file, "
          f"{len(unmatched)} with the no-verified-contact note ({', '.join(unmatched)})")
    return matched, unmatched


if __name__ == "__main__":
    patch_packs()
