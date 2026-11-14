# Hallway Transit Board — Founder Start Pack

> A framed e-paper panel by the door showing the next five departures from your bus, tram or train stop — live, running for months on one charge.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The last thing you do before leaving is check the transit app — phone in one hand, keys in the other, child in the third. A glance at the wall is faster, and the whole household sees it.
- **Customer:** Urban commuters and families in NL/DE/CH/AT/Nordics with excellent open transit data; hotels, hostels and co-working lobbies as a B2B SKU.
- **Product:** A 7.5" (later 10.3") e-paper panel in a wooden or aluminium frame, ESP32, battery, WiFi. Shows the next five departures from your chosen stop(s) with delays, plus side tiles (weather, electricity price). Set up by picking your stop on a phone. €119–149 (estimate).
- **Why now:** Open transit APIs in these countries are mature; glance e-paper devices (TRMNL at ~$139) proved people pay for "one screen, one job"; searches found no consumer transit board sold in continental Europe — only operator stop displays and operator web widgets for lobbies.
- **The ask:** ~€60k to certification and the first 1,000 units; a 50-unit hand-built pre-sale answers the kill question first.

## 2. Business plan

### Problem & customer

Transit associations already offer "departure monitor" web widgets (VRS, MDV) meant for screens in lobbies and shops. That tells you two things: the data is there and the use case is recognised — but it is served as a web page you must put on a powered TV or tablet. Nobody sells the quiet, battery-powered, framed object for the hallway.

- **Who pays (B2C):** the commuter household, 25–45, renting or owning in a city, uses the same stop 10 times a week; gift buyers at Christmas.
- **Who pays (B2B):** boutique hotels, hostels, co-working spaces, serviced apartments, dentist waiting rooms — a framed board at reception replaces the printed timetable and looks premium.
- **Who uses:** everyone walking past the door.

### Market size (estimates — check)

- **TAM:** urban households in NL/DE/CH/AT/DK/SE/NO/FI within walking distance of a frequent stop: ~25–30M. At €129 → **€3B+** theoretical.
- **SAM (households that already own a smart-home gadget and commute by transit; plus ~200k hospitality/co-working lobbies):** ~2–3M households + 200k B2B → **€250–400M**.
- **SOM (3 yrs):** 0.5% → **10–15k units**. Year 1: 1,000–2,000.

### Competition (1 search + round-1 notes)

| Alternative | What it is | Why we still win |
|---|---|---|
| The phone app (DB Navigator, 9292, SBB, Rejseplanen) | Free, excellent | Not glanceable, not shared, not on the wall |
| TRMNL and similar e-paper "glance" devices (~$139 + optional plugins) | General-purpose e-paper dashboards | Generic; transit plugins depend on hobby maintainers; no stop-picker onboarding; US-centric |
| Operator departure-monitor web widgets (VRS, MDV, etc.) on a TV/tablet | Free | Needs a powered screen; ugly in a hallway |
| UK hobby rail boards (Pi-based, eBay) | £100–300 | UK-only data, mains-powered, maker aesthetic |
| DIY: ESP32 + e-paper + Home Assistant | Weekend project | Our customer does not solder |
| Do nothing | — | Reality for 99%; the gift market is the way in |

**Wedge:** zero-config stop picker across 10+ national APIs, a frame that belongs in a hallway, months of battery, and a B2B lobby SKU with a branded header.

### Product & value proposition

- 7.5" 800×480 e-paper (mono first; colour SKU later via PaperColor-class panels), ESP32-S3 or C6, 3,000 mAh Li-ion (user-replaceable 18650 for the 2027 battery rule), WiFi.
- Refresh every 60–120 s while the household is awake (configurable "quiet hours"), partial refresh for minutes; months of battery estimate depends heavily on refresh cadence — publish honest numbers.
- Stop picker: phone opens a captive portal, you type your street, pick the stop(s) and lines; optional walking-time offset ("leave in 4 min").
- Side tiles: weather, electricity price (sister product: Tariff Lamp), a line for a second stop.
- Proxy service: holds API keys, caches, normalises 10+ APIs into one feed; the device only talks to your proxy.
- **Pricing (estimates):** €129 mono 7.5" framed; €179 colour; B2B lobby €199 with branded header and PoE/USB power; €9/year optional "Plus" for extra tiles (not required).

### Unit economics (estimates, EUR per unit; mono 7.5")

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (7.5" e-paper panel €18–22, ESP32-S3 module €3, e-paper driver/boost €1.5, charger + 18650 holder €1.5, 18650 cell €2.5, PCB €1.2) | 29.0 | 25.0 |
| PCBA + test | 2.8 | 1.9 |
| Enclosure (wood or aluminium frame, acrylic, back plate, wall hook) | 7.0 | 5.0 |
| Packaging (gift-grade box, cable, leaflet) | 3.0 | 2.2 |
| Freight + duty to EU | 2.8 | 1.4 |
| Certification amortised (€18k incl. battery) | 18.0 | 3.6 |
| **Landed cost** | **62.6** | **39.1** |
| Net price D2C (€129 incl. 21% VAT → €106.6) less €9 fulfilment | 97.6 | 97.6 |
| **Gross margin D2C** | **€35 (36%)** | **€58.5 (60%)** |
| Via retail (40%: €64 net) | ≈€1 (break-even) | €25 (39%) |

The panel is 60% of the BOM and its price swings; lock two panel vendors. Retail only after 5k.

### Go-to-market

**First 100 customers:** 50 hand-assembled PaperS3-based units sold in two cities (e.g. Amsterdam and Berlin) via a landing page, local subreddits (r/Amsterdam, r/berlin), Tweakers, local Instagram design accounts, and one co-working space that puts it in the lobby with a QR code. Design-store pop-up for a weekend.

**Then scale:** design/concept stores and museum shops (margin-heavy but perfect audience), hospitality suppliers, gift guides at Christmas, Amazon.de/.nl, transit operators' own merch shops (some sell branded goods), Kickstarter for the colour SKU.

### 12-month plan

- **Q1:** 50 hand-built units (PaperS3 + frame), proxy for NL + DE + CH, landing page, sell them; kill decision at 30 days.
- **Q2:** own PCB (ESP32-C6 + 7.5" panel + 18650), frame design, 50-unit EVT; add AT, DK, SE, NO, FI, BE feeds.
- **Q3:** certification incl. battery; 1,000 production; ship for Christmas.
- **Q4:** B2B lobby SKU, colour SKU EVT, retail talks.

**Team:** firmware engineer (full), backend developer for the proxy (half), industrial designer (contract) for the frame, founder on marketing and partnerships. Shenzhen partner for panel sourcing, PCBA and frame.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €45k + tooling/frame jigs €5k + certification €18k + first 50 hand-built (sold at cost) €0 net + 6 months team €45k + marketing €8k + proxy hosting €1k = **≈€122k**; pre-sales of 500 units at €129 (€53k ex VAT) bring external need to **≈€60–70k**. Route: pre-orders + bootstrap; creative-industry/design grants in NL/DE (search); angel if B2B hospitality traction appears.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** "the phone already does it" | The 50-unit pre-sale is the test; position as furniture and gift, not as a gadget |
| **Technical/commercial:** API dependency — keys, rate limits, terms of use, operators changing endpoints | Proxy you control; use official open-data portals (e.g. opentransportdata.swiss, Rejseplanen, DB and NS developer portals — check terms); fall back to GTFS-RT where published |
| **Technical:** battery life claims vs e-paper refresh reality | Measure and publish; quiet hours; ship a USB-C cable for the "always-on lobby" mode |
| **Regulatory:** Li-ion → UN 38.3, Battery Regulation, user-replaceability | 18650 in a holder from day one |
| **Supply:** e-paper panel price and allocation | Two qualified panel vendors; buy 1,200 panels at EVT |

GDPR: the device knows your stop, i.e. roughly where you live. Keep it on the device and in your proxy under your own account; no third-party analytics.

## 3. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack PaperS3 (C139) | https://www.gongbans.com/db/m5stack-papers3.html | ESP32-S3 e-paper device with battery — the first 50–300 units as-is in your frame | enclosure/structure only | Buy as a finished device; your frame + firmware |
| M5Stack PaperColor (C151) | https://www.gongbans.com/db/m5stack-papercolor.html | Colour e-paper device for the line-colour SKU | enclosure/structure only | Same |
| Espressif esp32-c6-devkitc-1 | https://www.gongbans.com/db/espressif-esp32-c6-devkitc-1.html | MCU reference for the 7.5" re-spin (WiFi 6, low power) | reference design files per catalogue (no schematic listed in this row) | Espressif reference terms — check |
| OSHWHub 18650-powered ESP32 IoT clock | https://www.gongbans.com/db/oshwhub-ji-yuesp32-di-wu-lian-wang-tian-qi-shi-zhong-bai-jian.html | Open ESP32 + 18650 charging path (IP5219 per the catalogue description) — copy the battery/charger section | schematic, pcb (EasyEDA) | OSHWHub project licence — check on project page |

Catalogue honesty: panel sizes and resolutions of PaperS3/PaperColor are not in the catalogue — check M5 docs before promising a screen size.

### Block diagram

```
18650 Li-ion ──► charger (IP5219-class per open ref) ──► 3.3V ──► ESP32-S3/C6
      ESP32 ──SPI──► e-paper driver/boost ──► 7.5" e-paper panel
      ESP32 ──WiFi──► your proxy ──► transit APIs (NS/9292-OVapi, DB, SBB, VBB/HAFAS, Rejseplanen, Entur...)
      button (refresh/setup) ; RTC deep sleep between refreshes
Frame: wood/aluminium, acrylic, wall hook, USB-C port hidden at the bottom
```

**Engineering gap:** the proxy and the stop picker (data work, not hardware), e-paper partial refresh without ghosting, and a battery estimate you can defend.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| 7.5" 800×480 e-paper panel (mono) | €18–22 | **Price-volatile; few makers**; qualify two |
| ESP32-S3 or C6 module | €3 | |
| E-paper driver (boost + level) | €1.5 | Reference in open e-paper drivers; or an integrated driver HAT design |
| Charger IC + protection + 18650 holder | €1.5 | Copy from the open 18650 clock |
| 18650 2,600–3,000 mAh cell (branded) | €2.5 | UN 38.3 report from the cell vendor |
| PCB 2-layer | €1.2 | |
| Frame + acrylic + back + hook | €7 | EU-made wood frame possible for small runs |
| Gift box + USB-C cable | €3 | |

### Firmware/software starting point

- Device: **ESP-IDF** or Arduino-ESP32 with **GxEPD2** (e-paper driver library) or **epdiy** for larger panels; **M5Unified/M5GFX** for the PaperS3 pilot.
- Proxy: a small Node/Python service; data sources: **opentransportdata.swiss** (CH), **Rejseplanen API** (DK), **Entur** (NO), **Trafiklab** (SE), **DB API Marketplace** (DE), **OVapi / NS API** (NL) — each has terms; check before launch. **GTFS-RT** feeds where published.
- Rendering: render the image server-side (PNG/1-bit) and push to the device — simpler firmware, easier layout changes.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 5 PaperS3 units in frames, proxy for 2 cities, landing page selling 50 at €129 | ≥20 sold in 30 days (≥50 = strong); below 20 = kill |
| 3–5 | **Works-like** — 50 hand-built units shipped; stop picker v1; battery logging | 50 shipped; <5% support tickets about setup; measured battery ≥6 weeks at 90 s daytime refresh |
| 6–8 | **Looks-like + EVT** — own PCB rev A (7.5", 18650), frame design, 30 units | Rev A works; ghosting acceptable; frame survives shipping drop |
| 9–10 | **DVT + pre-compliance** — rev B, EMC pre-scan, battery safety review, EN 18031 checklist, cell UN 38.3 docs | No fails; checklist complete; replaceable cell verified |
| 11–12 | **Pilot batch** — 50 units with full packaging to buyers and 3 lobbies | ≤2 failures; NPS ≥40; 2 lobbies buy more |

### Certification checklist (EU)

- **CE — RED:** EN 300 328 via module; **EN 301 489-1/-17**; **EN 62368-1** incl. battery charging circuit: €7–10k.
- **EN 18031-1/-2** (connected, holds the user's stop = personal data): self-assess; €2–4k review.
- **CRA:** SBOM, signed OTA, disclosure.
- **Battery:** **UN 38.3** for the cell/pack (use a cell with an existing report), **EU Battery Regulation** (producer registration, labelling, removability by 2027 — the 18650 holder solves it), lithium shipping paperwork.
- **RoHS, WEEE (consumer), REACH, packaging (DE LUCID).**
- **GDPR:** stop location ≈ home location → privacy notice, no third-party trackers, data minimisation on the proxy.
- **Total estimate:** €14–20k.

### Validation toolkit

- **Kill question:** Sell 50 hand-assembled units at €129 via a landing page in two cities within 30 days. Below 20 = kill. Cheapest experiment: 5 units, one landing page, €300 of local ads, one co-working lobby demo.
- **Interview script (5):** 1) How do you check departures before leaving, and how often does it go wrong? 2) Who else in the household would look at a board by the door? 3) Which stop(s) and lines matter; do you ever need a second stop? 4) Would you hang it on the wall or lean it on a shelf, and does it need to match your interior? 5) €99, €129 or €179 — and would you buy it as a gift?
- **Landing page:** Headline: "Your stop, on your wall." Bullets: "Next five departures, live, with delays — no phone needed." / "E-paper that runs for months on a charge." / "Pick your stop in two minutes. Works with NS, DB, SBB and more."
- **Pre-order pass:** ≥20 paid units in 30 days (≥50 = proceed to own PCB immediately).

### First production checklist

- Samples: 3 panels from two vendors tested for ghosting and temperature; 3 PCBAs; **golden sample** framed unit with photo reference.
- DFM: panel bonding to acrylic, frame tolerances for the panel's flex cable, hidden USB-C, hook position.
- MOQ: panels 500–1,000; PCBA 500; frames 300 (EU) or 1,000 (CN).
- QC/AQL: Z1.4 II, AQL 1.0/2.5; 100% test: full-screen pattern, WiFi join, charge/discharge check, no dead rows.
- Packaging: gift-grade; ISTA 1A; battery labelling; EU DoC + WEEE.
- Incoterms: FOB Shenzhen sea; lithium cells → dangerous-goods paperwork (ship cells installed at <30% SoC per carrier rules — check).

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Espressif).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (ESP32-S3 e-paper device with battery for the first 300 units); [M5Stack PaperColor (C151)](/db/m5stack-papercolor.html) (colour e-paper SKU for line colours). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c6-devkitc-1](/db/espressif-esp32-c6-devkitc-1.html) (MCU for the 7.5-inch re-spin). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [【训练营】采用18650供电的ESP32物联网时钟](/db/oshwhub-ji-yuesp32-di-wu-lian-wang-tian-qi-shi-zhong-bai-jian.html) (open ESP32 + 18650 charging reference for the battery path).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **iDisc Technology** (深圳市艾迪思科技有限公司) · no website on file — E-ink display module / e-reader OEM: E-ink display module; e-reader gongban; retail price tag; OEM/ODM. *(E-ink display modules)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Espressif websites)

```email
Subject: Sample order and volume pricing — M5Stack PaperS3 (C139), M5Stack PaperColor (C151), Espressif esp32-c6-devkitc-1 — for a Hallway Transit Board

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Hallway Transit Board: A framed e-paper panel by the door showing the next five departures from your bus, tram or train stop, live, running for months on one charge. The design is built around your M5Stack PaperS3 (C139), M5Stack PaperColor (C151), Espressif esp32-c6-devkitc-1.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack PaperS3 (C139), M5Stack PaperColor (C151), Espressif esp32-c6-devkitc-1.
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
主题：样品订购及批量报价 — M5Stack PaperS3 (C139), M5Stack PaperColor (C151), Espressif esp32-c6-devkitc-1 — 用于Hallway Transit Board

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hallway Transit Board：A framed e-paper panel by the door showing the next five departures from your bus, tram or train stop, live, running for months on one charge。产品设计基于贵司的M5Stack PaperS3 (C139), M5Stack PaperColor (C151), Espressif esp32-c6-devkitc-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack PaperS3 (C139), M5Stack PaperColor (C151), Espressif esp32-c6-devkitc-1。
2. 100 / 500 / 1,000 片的批量单价（深圳EXW及DDP到[城市]），含包装。
3. 是否可以定制（外壳、接口或预烧录固件），以及定制的NRE费用和最小起订量（MOQ）。
4. 如有，请提供射频测试报告或模组认证文件，以便我们规划欧盟CE/RED认证。
5. 首单的付款方式和条件。

如有需要，我们可在签署NDA后提供框图和目标数量。

祝好，
[姓名] · [公司] · [网站] · [电话 / WhatsApp]
```

**B. To a PCBA / EMS house — quote from the open design files** (send to Kingbrother, Foxlink or any assembler you vet; see the [playbook](/playbook.html#manufacturer))

```email
Subject: PCBA quote from open design files — Hallway Transit Board, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Hallway Transit Board: A framed e-paper panel by the door showing the next five departures from your bus, tram or train stop, live, running for months on one charge. The design starts from published open-hardware files (【训练营】采用18650供电的ESP32物联网时钟; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Hallway Transit Board，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hallway Transit Board：A framed e-paper panel by the door showing the next five departures from your bus, tram or train stop, live, running for months on one charge。设计基于已公开的开源硬件文件（【训练营】采用18650供电的ESP32物联网时钟；含原理图、PCB和BOM），并做了我们自己的修改。

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
<!-- who-to-contact:end -->

## 5. Next steps (this week)

1. Buy 5× PaperS3 and 5 cheap frames; write the proxy for one Dutch and one German city using the official open-data APIs; get live departures on paper by Sunday.
2. Put up the landing page with a photo of the real unit on a real wall, €129, limit 50; post in two city subreddits and one local design account.
3. Ask one co-working space to host a unit in its lobby with a QR code and record sign-ups.

Want help sourcing or building this? Talk to us via www.gongbans.com.
