# Trail Talker — Founder Start Pack

> A solar-powered outdoor audio post that plays a local story when a visitor approaches — for nature trails, heritage sites and sculpture parks, with no app and no network.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** App-based audio guides get single-digit uptake; QR codes need a signal and a willing phone; signage can't tell a story. Existing solar audio posts are quote-only, bespoke and expensive.
- **Customer:** Municipal parks departments, heritage trusts, nature reserves, open-air museums, sculpture parks and cemeteries across Europe (they pay from interpretation/signage budgets); visitors use it by walking up.
- **Product:** An IP66 post head with a TMOS presence sensor, MP3 playback, a weatherproof speaker, solar + Li-ion power sized for a European winter, a multilingual button, and content loaded by SD or from a caretaker's phone over BLE.
- **Why now:** Presence sensing that detects a *standing* visitor (TMOS), MP3 and class-D amp boards are catalogue parts; interpretation budgets exist and are spent on signage every year anyway.
- **The ask:** ~€85k (estimate) to 1,000 posts. Route: paid pilots (5 parks × 3 posts at €399), then public-procurement framework listings; grants for heritage/accessibility projects pay for the first 100.

## 2. Business plan

### Problem & customer
Buyer: the interpretation officer or parks manager at a municipality, a national/regional park authority, a heritage trust, an open-air museum or a botanical garden. They buy signage from a handful of suppliers every year, with budgets of €5–50k per project. They want: no running costs, no network, no app, vandal resistance, easy content changes (they re-record when the exhibit changes), and accessibility (audio helps visually impaired visitors — a real procurement point).

User: the visitor who walks up. Also the caretaker who swaps content twice a year and must not need a laptop.

Incumbents: UK-style solar audio posts sold to trails and playgrounds (PIR-activated, metal or oak finishes, quote-only — [Blackbox-av solar audio post project](https://www.blackboxav.co.uk/project/solar-audio-post-kent-downs-way-national-trail/), [their note on adding audio without power](https://www.blackboxav.co.uk/2021/08/31/how-do-i-add-audio-to-outdoor-spaces-without-power/)). A student report notes motion triggering costs power and pushed their design toward mains ([Lafayette report](https://sites.lafayette.edu/egrs451-fa24/files/2025/03/KSAT-Spoken-Word-Final-Report.pdf)) — that is the engineering problem to beat.

### Market size (estimates)
- Europe has tens of thousands of protected areas and thousands of open-air/heritage sites; municipalities run far more parks and trails. Assume **~60,000 sites in EU + UK** that buy interpretive signage (estimate; EUROPARC/EEA databases give protected-area counts, not buyers).
- **TAM:** 60,000 × 5 posts × €399 ≈ **€120 M**.
- **SAM:** sites with an interpretation budget and a story worth telling (nature trails with guided content, heritage sites, sculpture parks, cemeteries) — 25% → 15,000 sites → **€30 M**.
- **SOM (3 years):** 2.5% of SAM → 375 sites × 5 posts ≈ 1,900 posts → **€750k**. Plus content services (recording, translation) resold from partners.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Bespoke solar audio posts from AV-interpretation specialists (quote-only; metal/oak posts) | Established in UK heritage | Price (hundreds to >€1,000 per post, estimated), bespoke lead times, UK-centric |
| App audio guides / QR codes to web audio | Cheap per site | Uptake is poor; needs signal and a willing visitor; excludes many older visitors |
| Handset audio guides rented at a visitor centre | Museums | Staff, logistics, not for open trails |
| Printed panels / "do nothing" | The default | No story, no accessibility |
| Consumer solar Bluetooth speakers (€90–130) | Cheap hardware | No presence trigger, no content workflow, not IP66, not vandal-resistant |
| DIY (Arduino + MP3 module) | Hobby trail projects exist | Dies in winter; nobody supports it |

**Wedge:** a catalogue product (not a quote), €349–449, sized for a northern winter, content changed by the caretaker's phone, button for languages, and procurement-ready documentation (CE, IP66, accessibility statement).

### Product & value proposition
Hardware: aluminium/polycarbonate head unit (post sold separately or supplied by the site's signage maker), 10 W solar panel on a tilt bracket, 3.7 V 10 Ah LiFePO4 or Li-ion (LiFePO4 preferred for cold and safety), MPPT/solar charge path, TMOS presence sensor (detects a standing person, not just motion), ESP32-based controller with MP3 decoding, 10–15 W class-D amp (TAS5754M-class closed-loop) into an IP66 speaker, 1–3 language buttons, microSD, BLE for content upload and status. Firmware: play on approach (debounce, cooldown), quiet hours, volume by ambient noise, battery-save modes, play counters (anonymous).

Pricing (estimates): **€399 per post head** (€349 at 10+), solar/battery kit included; mounting post via signage partner (€150–400); content pack (script, voice-over, translation) via partners at €300–900 per post; 3-year warranty. B2B only; public procurement.

### Unit economics (estimates per post head, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32 module, MP3/codec, class-D amp, TMOS sensor, MPPT/charger, LiFePO4 10 Ah, 10 W panel, IP66 speaker, buttons, PCB) | €58.00 | €47.00 |
| Assembly & test (SMT, cable assembly, audio + solar test, potting of connectors) | €9.00 | €6.50 |
| Enclosure (die-cast/CNC alu or PC head, gaskets, bracket; tooling amortised) | €24.00 | €15.00 |
| Packaging (double-wall carton, foam) | €4.50 | €3.20 |
| Freight + duty to EU (heavy; lithium) | €9.00 | €5.50 |
| Certification amortised (~€28k: RED, EMC, 62368-1, UN 38.3, IP66, EN 18031 if BLE-to-internet) | €28.00 | €5.60 |
| **Landed cost** | **€132.50** | **€82.80** |
| Sell price | €399 | €399 |
| Channel margin (direct at 1k; 25% to signage partners at 5k) | €0 | €99.75 |
| **Gross margin** | **€266.50 (67%)** | **€216.45 (54%)** |

Good margin because the alternative is bespoke. Warranty reserve: keep 5% — outdoor products come back.

### Go-to-market
**First 100 customers (sites):** 5 paid pilots from the kill question (3 posts each) with municipal parks departments and one heritage trust; interpretation and signage trade bodies and their conferences (Interpret Europe events, national parks associations, museum associations); signage manufacturers as resellers (they already sit in the procurement); accessibility grants (audio interpretation for visually impaired visitors is fundable).

**Scale channels:** signage/interpretation suppliers across EU countries (they install posts anyway), public-procurement frameworks for park furniture, landscape architects, cemetery and botanic-garden networks.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from Grove MP3 + TMOS unit + open amp + solar board in an off-the-shelf IP66 box; 3 posts on a real trail through winter weeks; pilot sign-ups (kill question). |
| Q2 | Custom controller PCB, head enclosure tooling, winter power model validated with real data; EVT 20 posts in 5 pilots. |
| Q3 | DVT, certification, IP66 and vandal tests; 100-post batch; two signage resellers. |
| Q4 | 1,000-post capacity; framework listings in 2 countries; content-partner programme. |

**Team:** 1 embedded engineer (audio, power, BLE — full-time), 1 mechanical/industrial designer (enclosure, weathering — part-time → full-time at Q2), founder for public-sector sales (patience required); content partners external. Two and a half people.

**Funding to first 1,000 posts (estimates):** NRE €60k (PCBs €10k, head tooling €30k, bracket/panel integration €8k, firmware/app €12k) + certification €28k + 1,000 posts landed ~€130k + 12 months lean overhead €90k ≈ **€308k**; minus pilots (15 × €399) and the 100-post batch sold (~€40k + €35k) and early orders (~€150k if frameworks land) ≈ **~€85k** to raise. Route: pilots + heritage/accessibility grants + a signage-company partner prepayment; angel only if you want to go faster.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** winter power — December in Northern Europe gives ~0.5–1 h equivalent sun; PIR/TMOS always-on | Size for 20 plays/day at 30 s with 10 Ah LiFePO4 and a 10 W panel, sleep current < 1 mA, low-battery "sleep until spring" mode; test one real winter before promising |
| **Technical:** false triggers (dogs, deer, wind) and vandalism | TMOS presence (standing human) + dwell time; steel grille over the speaker; tamper alarm; replaceable front |
| **Market:** public procurement is slow; demand scored 2/5 | Pilots paid from discretionary budgets; signage partners who already win tenders; patience and a 12-month pipeline view |
| **Regulatory:** noise complaints, nature-reserve rules on sound | Volume limits, quiet hours, directional speaker, a "mute for 2 h" caretaker button; check reserve bylaws |
| **Supply:** LiFePO4 cells and speakers vary; solar panel suppliers churn | Branded cells with UN 38.3; qualify 2 panel suppliers; IP66 speaker from a marine-grade supplier |
| **Licence:** two OSHWHub boards | Read both licences; use as reference and redraw your own controller — you'll need one board anyway |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Seeed Grove MP3 v2.0 | https://www.gongbans.com/db/seeed-grove-mp3-v2-0.html | MP3 playback reference (decoder + SD) | schematic | Seeed wiki resources; check licence |
| M5Stack Unit TMOS PIR (U185) | https://www.gongbans.com/db/m5stack-unit-tmos-pir.html | Presence detection incl. a standing visitor | enclosure/structure only | Buy the unit; sensor is a standard part |
| TAS5754M closed-loop digital amp (OSHWHub) | https://www.gongbans.com/db/oshwhub-tas7454-bi-huan-shuo-zi-gong-fan.html | Open class-D amp design for a weatherproof speaker | schematic, pcb (EasyEDA) | **OSHWHub licence varies — read it** |
| solar-to-5V zener regulator (OSHWHub) | https://www.gongbans.com/db/oshwhub-solar-to-5v-zener-regulator.html | Simple solar charge path reference | schematic, pcb (EasyEDA) | **OSHWHub licence varies**; replace with a proper MPPT charger for production |

### Block diagram
```
[10 W solar panel] -> [MPPT charger] -> [LiFePO4 10 Ah] -> [3.3 V / 12 V rails]
[TMOS presence] --I2C--> [ESP32 controller] --I2S--> [class-D amp] -> [IP66 speaker]
[language buttons] ------> |           |<-- [microSD content]   [BLE: caretaker phone upload/status]
                           +-> [tamper switch] [temp sensor] [play counter]
```
**Engineering gap:** the catalogue gives playback, presence, amp and a crude solar path as separate boards. Missing: one low-sleep controller board with a real MPPT charger and cold-rated battery management, the winter power model, an IP66 vandal-resistant head with acoustic design, the BLE content workflow for non-technical caretakers, and the procurement documentation. Mechanical and power engineering are the work; audio is easy.

### Starter BOM (estimates per post at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 module (I2S audio, BLE) | €2.60 | Pre-certified |
| I2S DAC/codec | €1.20 | |
| Class-D amp 15 W (TAS5754M-class or simpler) | €2.50 | |
| TMOS presence sensor | €3.50 | **Limited-source**; PIR fallback footprint |
| MPPT solar charger IC + protection | €2.80 | |
| LiFePO4 3.2 V 10 Ah cell + BMS | €14.00 | Cold-rated; UN 38.3 from vendor; **DG shipping** |
| 10 W monocrystalline panel + bracket | €9.00 | Two suppliers |
| IP66 8 Ω 15 W speaker (marine grade) | €7.00 | |
| Buttons (IP67 vandal), tamper switch, cable glands | €4.50 | |
| PCB, passives, microSD | €4.00 | |
| Head enclosure (PC/alu) + gaskets + steel grille | €24.00 | **Tooling €25–35k**; off-the-shelf IP66 box for pilots |

### Firmware/software starting point
- ESP-IDF or Arduino-ESP32; the ESP32-audioI2S library (exists on GitHub) plays MP3 from SD over I2S — enough for v1.
- TMOS sensor: the sensor vendor publishes a driver (search the sensor part number + "driver"); M5Stack has an Arduino library for the TMOS unit (search "M5Unit-TMOS").
- BLE content upload: implement a simple GATT file transfer, or use WiFi-AP mode with a captive web page (no app to maintain; a caretaker opens a web page on the phone). The web page approach avoids app-store pain.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 3 works-like posts (catalogue boards in an IP66 box with a bought panel/battery) on a real trail; **5 parks departments sign a paid 3-post pilot at €399 each within 8 weeks** (clock runs to W10) |
| 3–5 | Works-like | Presence trigger with < 10% false plays over 2 weeks; power log shows positive balance on a mixed-weather week; caretaker swaps content without help |
| 6–8 | Looks-like + EVT | Custom controller PCB v1, printed/CNC head with grille; 15 units in 5 pilots; audio intelligible at 3 m in wind; sleep current < 1 mA |
| 9–10 | DVT + pre-compliance | IP66 test, 1 m drop/impact test (IK rating target IK08+), −20 °C to +60 °C chamber, RED/EMC pre-compliance, UN 38.3 reports |
| 11–12 | Pilot batch | 30–50 posts; two pilots convert to orders; warranty-return rate < 3% after first winter month |

### Certification checklist (EU)
- **CE under RED** (BLE/WiFi): EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** (battery, outdoor); **EN 18031-1** if the post ever connects to the internet (BLE to a phone only — likely out of scope if no internet path; confirm with your assessor; if you add LTE status reporting later, it's in). Est. €6–9k RED/EMC, €3–5k safety, €0–15k EN 18031.
- **IP66 test** (EN 60529) and **IK impact rating** (EN 62262) — procurement asks: ~€2–4k.
- **RoHS, REACH, WEEE; Battery Regulation (EU) 2023/1542** (industrial/portable classification for a 10 Ah pack — check; labelling, carbon-footprint rules may apply to larger packs later) + **UN 38.3**.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027; signed firmware, update path via SD/phone, SBOM.
- **GDPR:** no camera, no mic recording, anonymous play counts — state it in the tender docs; it is a selling point.
- **Accessibility:** not mandatory for this product, but write an accessibility statement (button height, contrast, audio) — tenders reward it.
- **Noise:** local bylaws, not CE; a max-SPL spec in the manual.
- **Total certification budget estimate: €18–35k** depending on EN 18031 scope.

### Validation toolkit
- **Kill question:** Do 5 parks departments sign a paid 3-post pilot at €399 each within 8 weeks?
- **Cheapest experiment (~€900):** 3 posts from Grove MP3 + TMOS unit + the open amp + a bought 10 W panel and LiFePO4 pack in an IP66 box, on a trail you have permission for; a 60-second video; a one-page pilot offer sent to 20 parks/heritage managers.
- **5-question interview (parks/interpretation manager):** 1) What did you spend on interpretation and signage last year, and who supplied it? 2) Have you tried audio (app, QR, handsets)? What was the uptake? 3) Which three spots on your site deserve a voice? 4) Who would change the content, and how often? 5) €399 per post plus a post from your signage supplier — would you pilot 3 this season, and what approval does that need?
- **Landing page:** headline "A voice on the trail. No app, no network, no mains." Bullets: "Plays when a visitor stops — solar-powered through a northern winter." / "IP66, vandal-resistant, 3-year warranty; content changed from a phone." / "€399 per post. Pilot 3 for a season."
- **Pass threshold:** 5 paid pilots (15 posts, €6k) within 8 weeks.

### First production checklist
- Samples: 5 golden samples with audio SPL curve, power log and IP test record; one weathered on a roof for the whole project.
- DFM: gasket compression, gland torque, panel bracket adjustability, grille replaceability; potting of external connectors.
- MOQ talk: head enclosure 500–1k; panels 500; cells 1k; speakers 1k.
- QC: AQL II 2.5/4.0; 100% audio and solar-charge test; 100% leak test (pressure decay) on heads; 2% sample full IP66 water test; serial-number plates.
- Packaging: double-wall carton with foam, panel protected; lithium labels; ISTA 2A drop test.
- Incoterms: FOB Shenzhen, sea freight (heavy); DG lithium paperwork; consider shipping batteries from an EU distributor for the first 100.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Seeed Studio and M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-MP3 v2.0](/db/seeed-grove-mp3-v2-0.html) (MP3 playback reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit TMOS PIR (U185)](/db/m5stack-unit-tmos-pir.html) (presence detection, including a standing visitor). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [TAS 5754M 闭环数字功放.](/db/oshwhub-tas7454-bi-huan-shuo-zi-gong-fan.html) (open closed-loop digital amp for a weatherproof speaker); [solar-to-5v-zener-regulator](/db/oshwhub-solar-to-5v-zener-regulator.html) (solar charge path).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Jieli Technology** (珠海市杰理科技股份有限公司) · zh-jieli.com — TWS SoC chip solution house: AC69xx/AC70xx TWS SoC; 27B+ chips shipped; clients: Xiaomi / QCY / HP / Lenovo. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Fenda Technology** (深圳市奋达科技股份有限公司) · fenda.com — TWS earbuds / smart speaker ODM: TWS earbuds; smart speaker; smart home; clients: Amazon / Creative / Philips. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Haoern Acoustics** (深圳市豪恩声学股份有限公司) · haoen.cn — TWS / headphone ODM: TWS; ANC headphone; smart speaker; clients: vivo / RAZER / BEATS / HP. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Antixun** (深圳市安特信技术有限公司) · no website on file — TWS / smart audio ODM: TWS; ANC earphone; smart speaker; pivoted from solution house to ODM 2018. *(Audio: speaker / earphone ODMs and the Jieli chip house)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-MP3 v2.0, M5Stack Unit TMOS PIR (U185) — for a Trail Talker

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Trail Talker: A solar-powered outdoor audio post that plays a local story when a visitor approaches — for nature trails, heritage sites and sculpture parks, with no app and no network. The design is built around your Seeed Grove-MP3 v2.0, M5Stack Unit TMOS PIR (U185).

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-MP3 v2.0, M5Stack Unit TMOS PIR (U185).
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
主题：样品订购及批量报价 — Seeed Grove-MP3 v2.0, M5Stack Unit TMOS PIR (U185) — 用于Trail Talker

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Trail Talker：A solar-powered outdoor audio post that plays a local story when a visitor approaches — for nature trails, heritage sites and sculpture parks, with no app and no network。产品设计基于贵司的Seeed Grove-MP3 v2.0, M5Stack Unit TMOS PIR (U185)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-MP3 v2.0, M5Stack Unit TMOS PIR (U185)。
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
Subject: PCBA quote from open design files — Trail Talker, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Trail Talker: A solar-powered outdoor audio post that plays a local story when a visitor approaches — for nature trails, heritage sites and sculpture parks, with no app and no network. The design starts from published open-hardware files (TAS 5754M 闭环数字功放., solar-to-5v-zener-regulator; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Trail Talker，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Trail Talker：A solar-powered outdoor audio post that plays a local story when a visitor approaches — for nature trails, heritage sites and sculpture parks, with no app and no network。设计基于已公开的开源硬件文件（TAS 5754M 闭环数字功放., solar-to-5v-zener-regulator；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order Grove MP3, Unit TMOS PIR, the open amp PCB (or a ready TAS5754M board), a 10 W panel, a LiFePO4 pack with BMS and an IP66 box; build post #1 in a weekend.
2. Draft the one-page pilot offer and list 20 parks departments, heritage trusts and open-air museums within 2 hours' drive.
3. Read the licences of both OSHWHub projects; decide now that your production controller board is your own design.

Want help sourcing or building this? Talk to us via www.gongbans.com.
