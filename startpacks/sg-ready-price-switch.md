# SG-Ready Price Switch — Founder Start Pack

> A DIN-rail box that closes a heat pump's SG-Ready or boiler contact — and up to four relays — when the hourly electricity price or your solar surplus says so, with no cloud account.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Most heat pumps sold in DE/AT/NL since ~2013 have SG-Ready contacts; almost nothing drives them. Dynamic tariffs (mandatory offer in DE since Jan 2025; 573 negative-price hours on the German day-ahead market in 2025 per Bundesnetzagentur via the sources below) make hour-shifting worth real money — vendor blogs claim up to several hundred euros a year, unverified.
- **Customer:** Homeowners with a heat pump or electric boiler on a dynamic tariff (NL/DE/AT); the heat-pump installer who fits the box; energy advisors.
- **Product:** A 4-module DIN-rail box: ESP32, four dry-contact relays (two for SG-Ready states, two spare for boiler/pool/EV), local web UI, price fetch from day-ahead markets, optional surplus logic from a P1/Modbus energy meter, guard-rails (minimum run/off times per SG-Ready rules). €129–169 (estimate).
- **Why now:** Installers are asked about dynamic tariffs weekly and answer with a Shelly and a Home Assistant forum thread. Energy-manager systems cost "several hundred to over €1,000 plus a monthly fee" (Utopia). A €149 box that does one thing fills the hole.
- **The ask:** ~€70k to a certified first 1,000; installer pre-commitments carry a big share.

## 2. Business plan

### Problem & customer

SG-Ready is a two-contact interface: four states (blocked, normal, recommended-on, forced-on). The heat pump decides what each state does; the signal source is "whatever closes the contact". Today that is a PV inverter's relay (surplus only) or a hobbyist Shelly driven by Home Assistant/evcc with Tibber/aWATTar prices. Energy-management systems from inverter brands are expensive and brand-locked.

- **Who pays:** the homeowner (through the installer's invoice, or directly online).
- **Who installs:** the electrician/heat-pump installer. The box must take 10 minutes: DIN clip, 230 V in, two wires to SG-Ready, WiFi onboarding from the phone.
- **Who uses:** nobody, after setup. It should be boring. A local web page shows "why the pump is on now".

### Market size (estimates — check)

- **TAM:** heat pumps installed in DE (~2M+), NL (~1M incl. hybrids), AT (~0.5M), plus electric boilers and hot-water heat pumps (millions). Say **4M** SG-Ready-capable devices in the three countries → at €149 **€600M** theoretical.
- **SAM (owners on or moving to dynamic tariffs with a smart meter — the bottleneck in DE):** 10–15% over the next 3 years → **400–600k** → **€60–90M**.
- **SOM (3 yrs):** 2% of SAM via installers → **8–12k units**. Year 1: 1,000–2,000.

### Competition (2 searches)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing (SG-Ready unused) | The default | Our box pays back in one winter if the vendor claims are half right |
| Shelly relay + Home Assistant/evcc/openHAB + Tibber/aWATTar price integration | ~€25 + a hobby | Needs a server, a hobbyist and maintenance; installers will not support it |
| Inverter-brand energy managers (Solarwatt Manager, SMA Home Manager, Fronius, etc.) with SG-Ready output | €300–1,000+, brand-locked, mostly surplus-driven | We are brand-agnostic, price-driven and €149 |
| Heat-pump-brand dynamic-tariff features (e.g. iDM dynamic-tariff control, Viessmann/Vaillant apps with Tibber) | Built-in for new pumps of some brands | Installed base of older pumps is ours; also boilers, pool pumps |
| Reduxi-type HEMS with EVU contact control | Full HEMS with subscription-ish pricing | Overkill for "just the heat pump" |
| Smart-dog / solar-dog hobby HEMS | Niche DIY | Same as HA |

**Wedge:** installer-friendly, brand-agnostic, no cloud account, one job. The spare relays make it a "cheap-hour box" for the boiler and the pool pump too.

### Product & value proposition

- 4 TE DIN-rail enclosure, 230 V AC input with an internal PSU (or 24 V DC SKU), ESP32-C6/S3, four relays with dry contacts (rated for control circuits, e.g. 2 A 30 V DC / 230 V AC 2 A — spec per relay datasheet), two digital inputs (inverter surplus contact, pump feedback), RS-485 for Modbus energy meters (optional).
- Logic: day-ahead price bands (cheapest N hours, threshold, percentile), SG-Ready state mapping with mandatory guard-rails (state 1 blocked max 2 h, 10-minute re-activation lock per the sources), surplus mode from P1/Modbus, schedules, holiday mode.
- Local web UI; no account; optional MQTT; signed OTA from your server.
- **Pricing (estimates):** €149 (€129 installer net), €39 Modbus meter add-on, €199 pro SKU with 24 V DC and 2 extra relays.

### Unit economics (estimates, EUR per unit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C6 module €2.5, 4 relays €4, relay drivers + opto inputs €1.5, AC/DC 3.3/5 V module 3 W €3.5, RS-485 €0.8, terminals/screw blocks €3, PCB €1.5) | 16.8 | 14.0 |
| PCBA + test (hipot on mains side) | 3.5 | 2.4 |
| Enclosure (standard 4 TE DIN housing, printed label) | 3.0 | 2.2 |
| Packaging + leaflet + QR | 1.5 | 1.1 |
| Freight + duty to EU | 1.5 | 0.8 |
| Certification amortised (€22k incl. LVD) | 22.0 | 4.4 |
| **Landed cost** | **48.3** | **24.9** |
| Net price installer channel (€129 ex VAT) | 129 | 129 |
| **Gross margin installer** | **€81 (63%)** | **€104 (81%)** |
| D2C (€149 incl. 19% VAT → €125) less €8 fulfilment | €69 (59%) | €92 (79%) |

Mains in a DIN box means LVD testing and creepage/clearance discipline — budget it, do not skimp.

### Go-to-market

**First 100 customers:** 10 heat-pump installers (via SHK-Innung lists, Haustechnikdialog, the Dutch installer forums, local Facebook installer groups) get a 10-minute demo and two boxes each at cost. Homeowners on Photovoltaikforum, Haustechnikdialog, Tweakers, akkudoktor forum. One YouTube explainer of the price logic.

**Then scale:** wholesalers (electrical wholesalers like the big German/Dutch ones — search), heat-pump distributors, dynamic-tariff retailers (bundle), energy advisors, PV installers, Amazon for the DIY tail.

### 12-month plan

- **Q1:** works-like on StamPLC + Unit 4Relay in a DIN base; price logic; 10 installer demos; two pilots in real homes through a winter month.
- **Q2:** own PCB (mains PSU, relays, isolation), DIN enclosure, 50-unit EVT with installers; Modbus meter add-on.
- **Q3:** certification (RED + LVD + EMC), 1,000 production; installer onboarding kit.
- **Q4:** wholesaler listing, 24 V pro SKU, retailer bundle talks.

**Team:** embedded engineer (full), power/safety-aware hardware engineer (half), founder with installer network, a part-time technical writer for the installer manual. Shenzhen partner for PCBA (with hipot testing) and DIN enclosure.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €27k + certification €22k + tooling (label/enclosure minor) €2k + pilots €4k + 6 months team €45k + installer marketing €6k = **≈€106k**; installer pre-orders (300 × €129 = €39k) reduce the external need to **≈€60–70k**. Route: installer pre-orders + bootstrap; energy-efficiency grants (DE/NL have installer-innovation and flexibility programmes — search); angel if a tariff retailer wants a bundle.

### Top risks

| Risk | Mitigation |
|---|---|
| **Regulatory/safety:** mains in a DIN box; relay contacts on a heat pump's low-voltage input | Only dry contacts to SG-Ready; LVD testing; clear installer-only labelling; consider a 24 V DC-only SKU first to defer LVD |
| **Technical:** every heat pump maps SG-Ready states differently | Installer wizard with brand presets built from pilots; conservative defaults (state 3 "recommended" only) |
| **Market:** heat-pump brands add dynamic tariffs natively | Installed base of older units is large; add boilers/pool/EV; be the cheap generic layer |
| **Commercial:** damaging a heat pump via wrong signals | Guard-rails hard-coded (max block time, min re-activation lock); liability insurance; installer sign-off |
| **Supply:** relay quality | Branded relays (Omron/Hongfa-class), incoming inspection |

## 3. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack StamPLC (K141) | https://www.gongbans.com/db/m5stack-stamplc.html | DIN-rail PLC-style controller for the works-like prototype | enclosure/structure only | Finished product for prototypes; own PCB for production |
| M5Stack Base DIN (M132) | https://www.gongbans.com/db/m5stack-base-din.html | DIN-rail mounting reference and form factor | enclosure/structure only | Mechanical reference |
| M5Stack Unit 4Relay (U097) | https://www.gongbans.com/db/m5stack-unit-4relay.html | Four relays for the prototype | enclosure/structure only | Module for prototypes |
| Espressif esp32-c6-devkitc-1 | https://www.gongbans.com/db/espressif-esp32-c6-devkitc-1.html | WiFi 6 MCU reference for the re-spin | reference design files per catalogue (no schematic listed in this row) | Espressif reference terms — check |

Catalogue honesty: none of these four rows publishes electronics files; this product is "prototype on modules, design your own board". The relay ratings of Unit 4Relay are not in the catalogue — check M5 docs before switching anything real.

### Block diagram

```
230 V AC ──► isolated AC/DC 3.3/5 V module ──► ESP32-C6 (WiFi)
     ESP32 ──► relay drivers ──► 4× relays (dry contacts) ──► SG-Ready 1/2, boiler, spare
     ESP32 ◄── 2× opto-isolated inputs (inverter surplus contact, feedback)
     ESP32 ◄──► RS-485 (Modbus energy meter, optional)
     WiFi ──► your price proxy (day-ahead by bidding zone) ; local web UI ; MQTT optional
DIN 4 TE housing; terminals top/bottom; status LEDs on the front
```

**Engineering gap:** mains isolation/creepage, relay sequencing with guard-rails, installer wizard with brand presets, and the price proxy (shared with the Tariff Lamp).

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-C6-WROOM-1 | €2.5 | Pre-certified |
| 4× relays 5 V coil, 2–5 A contacts (branded) | €4 | Pick a type with a safety file (UL/ENEC) |
| Relay drivers (ULN2003-class) + flyback | €0.5 | |
| Isolated AC/DC module 3 W (certified, EN 62368-1 file) | €3.5 | **Buy a certified module**; do not design the flyback yourself at this volume |
| Opto inputs ×2, RS-485 transceiver | €1.5 | |
| Screw terminals (pluggable), DIN 4 TE housing | €6 | Standard housings from several makers |
| PCB 2-layer with creepage slots | €1.5 | |

### Firmware/software starting point

- **ESP-IDF** on ESP32-C6 (or **ESPHome** for pilots — relays, inputs, web server exist).
- Price data: **ENTSO-E Transparency Platform API**; reuse the Tariff Lamp proxy.
- Surplus/metering: **Modbus RTU** libraries exist for ESP32; P1 readers via local API (HomeWizard — search).
- Logic references: **evcc** (open-source energy management with heat-pump/SG-Ready support in its docs) is worth reading for state handling; do not copy code without checking its licence.
- Brand mapping: build from pilots; the German heat-pump association (BWP) SG-Ready database lists compatible pumps — search.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — StamPLC + Unit 4Relay + Base DIN, price logic in ESPHome/ESP-IDF, 10-minute demo video; 10 installer calls | ≥10 installers agree to fit it on their next installs at €149 (or ≥5 sign a pre-order) |
| 3–5 | **Works-like** — 5 prototypes in real homes with 3 heat-pump brands; guard-rails; local UI | No unsafe states; pumps respond as expected; owners see price-shifted operation in logs |
| 6–8 | **Looks-like + EVT** — own PCB rev A with certified PSU module, DIN housing, 30 units; hipot test | Passes 3 kV hipot; creepage per EN 62368-1; relay sequencing verified |
| 9–10 | **DVT + pre-compliance** — rev B, EMC pre-scan, LVD review with the lab, EN 18031 checklist, installer manual v1 | No fails; manual reviewed by 2 installers |
| 11–12 | **Pilot batch** — 50 units with 10 installers; support line | ≤2 failures; installers report <15 min install; brand presets for ≥6 pumps |

### Certification checklist (EU)

- **CE — RED** (WiFi): EN 300 328 via module, **EN 301 489-1/-17**; because it is radio equipment, RED article 3.1(a) covers safety — the lab will test to **EN 62368-1** (or EN 61010/EN 60730-type standards depending on how you classify a control device — ask the lab) for the mains part: €10–15k. A 24 V DC-only first SKU cuts this substantially.
- **EN 18031-1** (connected): self-assess; keep the web UI password-protected, no cloud account: €2–4k.
- **CRA:** SBOM, signed OTA, disclosure contact; update support for the box's life (10 years is realistic in a fuse cabinet — plan it).
- **RoHS, WEEE (B2B/consumer), REACH, packaging.**
- No battery, no personal data beyond consumption (GDPR note in manual).
- **Total estimate:** €15–22k (mains SKU).

### Validation toolkit

- **Kill question:** Do 10 heat-pump installers agree to put it in their next installs at €149 after seeing a 10-minute demo of the price logic? Cheapest experiment: StamPLC demo rig + a laptop + 10 coffees.
- **Interview script (5):** 1) How many of your customers ask about dynamic tariffs, and what do you tell them? 2) Which heat-pump brands do you install; what do their SG-Ready states do? 3) What do you use today when a customer wants surplus/price control — and who supports it afterwards? 4) What must the box have for you to fit it in 15 minutes (terminals, wizard, docs)? 5) €129 net to you, €149 to the customer — margin enough, or do you want to rent it?
- **Landing page:** Headline: "Run your heat pump when electricity is cheap. Automatically." Bullets: "Closes the SG-Ready contact on cheap hours and solar surplus — no cloud account." / "DIN-rail, installed by your electrician in 15 minutes." / "Four relays: heat pump, boiler, pool, whatever is next."
- **Pre-order pass:** ≥10 installers pre-order ≥3 units each (≥30 units) within 6 weeks.

### First production checklist

- Samples: 5 PCBAs from an assembler that does hipot and ICT; **golden sample** with label and sealed screws.
- DFM: creepage slots, terminal torque, housing clip, LED light pipes.
- MOQ: PCBA 500; housings 500 from a standard maker; PSU modules 1k reel.
- QC/AQL: Z1.4 II, AQL 0.65 major (mains) / 2.5 minor; 100% hipot + relay click test + WiFi join.
- Packaging: installer-friendly box with wiring diagram on the lid; EU DoC + WEEE.
- Incoterms: FOB Shenzhen sea; pilot by air DAP.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Espressif).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack StamPLC (K141)](/db/m5stack-stamplc.html) (DIN-rail PLC-style controller core); [M5Stack Base DIN (M132)](/db/m5stack-base-din.html) (DIN-rail base reference); [M5Stack Unit 4Relay (U097)](/db/m5stack-unit-4relay.html) (four dry-contact relays). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c6-devkitc-1](/db/espressif-esp32-c6-devkitc-1.html) (WiFi 6 MCU for the re-spin). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Espressif websites)

```email
Subject: Sample order and volume pricing — M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1 — for a SG-Ready Price Switch

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a SG-Ready Price Switch: A DIN-rail box that closes a heat pump's SG-Ready or boiler contact — and up to four relays — when the hourly electricity price or your solar surplus says so, with no cloud account. The design is built around your M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1.
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
主题：样品订购及批量报价 — M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1 — 用于SG-Ready Price Switch

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款SG-Ready Price Switch：A DIN-rail box that closes a heat pump's SG-Ready or boiler contact — and up to four relays — when the hourly electricity price or your solar surplus says so, with no cloud account。产品设计基于贵司的M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1。
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
Subject: PCBA quote from open design files — SG-Ready Price Switch, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a SG-Ready Price Switch: A DIN-rail box that closes a heat pump's SG-Ready or boiler contact — and up to four relays — when the hourly electricity price or your solar surplus says so, with no cloud account. The design starts from published open-hardware files (M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — SG-Ready Price Switch，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款SG-Ready Price Switch：A DIN-rail box that closes a heat pump's SG-Ready or boiler contact — and up to four relays — when the hourly electricity price or your solar surplus says so, with no cloud account。设计基于已公开的开源硬件文件（M5Stack StamPLC (K141), M5Stack Base DIN (M132), M5Stack Unit 4Relay (U097), Espressif esp32-c6-devkitc-1；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order StamPLC, Base DIN and Unit 4Relay; wire a price-logic demo (ENTSO-E day-ahead, cheapest 6 hours → relay) and film the 10-minute demo.
2. List 20 heat-pump installers within an hour's drive; book 10 demos.
3. Ask two labs how they would classify a DIN-rail WiFi relay box (EN 62368-1 vs EN 60730/61010) and whether a 24 V DC-only SKU would skip the mains tests.

Want help sourcing or building this? Talk to us via www.gongbans.com.
