# Heat-Pump COP Monitor Lite — Founder Start Pack

> A clip-on kit (two pipe temperature sensors + one power clamp) that shows your heat pump's real daily efficiency so owners catch bad settings and installers prove their work.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of new heat-pump owners want to know one number — how efficient is it really — and the manufacturer's app hides or fakes it. The only honest open monitor needs a plumber-installed heat meter and costs ~£460–550 + VAT ([OpenEnergyMonitor community](https://community.openenergymonitor.org/t/heatpump-monitor-update/999/6)).
- **Customer:** Heat-pump owners in DE/NL/UK/Nordics who hang out in forums and run Home Assistant; installers who need a cheap diagnostic to prove a commissioning. The owner pays; the owner uses it; the installer buys five.
- **Product:** A €199 kit: two clip-on pipe temperature sensors, one CT clamp for the outdoor unit's supply, a small hub with WiFi and RS485, and an honest "indicative efficiency ±15%" estimate without a heat meter — plus a Pro path with a bought-in flow meter later.
- **Why now:** 2.6–2.9 M residential heat pumps sold in Europe in 2025 alone, ~28 M installed ([EHPA via pv magazine](https://www.pv-magazine.com/2026/03/23/european-residential-heat-pump-sales-increased-in-2025/), [IIR](https://iifiir.org/en/news/european-heat-pump-market-shows-signs-of-recovery-in-2025-after-two-year-decline)); the local-first smart-home crowd is huge; CT clamps and pipe sensors are commodities.
- **The ask:** ~€75k (estimate) to the first 1,000 units; route = forum pre-orders (the kill question is the funding) + bootstrap.

## 2. Business plan

### Problem & customer
A heat pump's efficiency depends on settings the owner controls: flow temperature, heating curve, cycling, hot-water schedule. Owners who see their daily COP fix these things; owners who don't, pay 20–40% more electricity. The manufacturer app shows "energy used" at best. The forum answer is "install an emonHP with a heat meter" — a plumber visit and £500+. Most won't.

Who pays vs who uses: the owner pays and uses (B2C); installers buy 5–10 as a diagnostic they move between jobs, and can leave one behind as an upsell (B2B). The data stays local (Home Assistant/MQTT) with an optional hosted page for the non-technical.

### Market size (estimates)
- Installed base ~28 M in Europe; new sales ~2.8 M/year. The addressable owner is the one who cares and has WiFi near the pump: estimate **15% of the installed base** → 4.2 M.
- **TAM:** 4.2 M × €199 ≈ **€840 M** (clearly not all reachable; label it the ceiling).
- **SAM:** owners active in heat-pump forums, HA communities and owner clubs in DE/NL/UK/Nordics — estimate 600k → **€120 M**; installers ~60k firms × 3 kits → €36 M.
- **SOM (3 years):** 1% of SAM → 6,000 owner kits + 1,500 installer kits → **~€1.5 M**.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| OpenEnergyMonitor emonHP Level 3 bundle (~£462–539 + VAT, [OEM community](https://community.openenergymonitor.org/t/heatpump-monitor-update/999/6); HeatpumpMonitor.org) | Accurate, open, respected; needs a MID heat meter plumbed in | Price, plumber visit; supply has lagged demand |
| OEM ESP8266 WiFi heat-pump monitor kit (~£36 ex VAT, no meter/enclosure) | Cheap, for tinkerers | Still needs a heat meter for COP; bare board |
| Manufacturer apps / cloud integrations | Free | Hide or estimate COP; cloud-only; no cross-brand truth |
| Smart meter + spreadsheet ("do nothing") | Free | Electricity only; no heat side |
| Installer's commissioning sheet | Required anyway | One day, one reading, no trend |
| DIY: ESP32 + DS18B20 + CT clamp + ESPHome | Thousands do it | No calibration, no clamp accuracy, no installer PDF, no CE |

**Wedge:** €199, no plumber, 30-minute install, honest ±15% label, local-first, installer PDF — and a Pro path (flow meter) for the ones who then want ±5%.

### Product & value proposition
Hardware: hub (ESP32-S3 or -C6, WiFi, RS485 isolated, 2 sensor inputs, CT input, small e-paper or LEDs), two clamp-on pipe temperature sensors (NTC or PT1000 in a spring clamp with thermal pad, insulated cover — contact beats IR on shiny pipes), one split-core CT clamp (certified bought-in part, installer-fitted wording), USB-C PSU. Firmware: flow estimate from pump curve/ΔT with the brand's circulation pump data or a user-entered flow (from the commissioning sheet — many owners have it), daily/weekly indicative efficiency, cycling counter, defrost detection from ΔT patterns, hot-water vs heating split, MQTT/Home Assistant native, optional RS485/Modbus read from pumps and meters that expose it (the Pro way to get real electricity and sometimes real flow), installer PDF.

Pricing (estimates): **€199 Lite kit**, **€349 Pro** (adds a bought-in ultrasonic/vortex flow meter — not in the catalogue), €29 extra pipe-sensor pair, installer 5-pack €799. B2B via heat-pump wholesalers later.

### Unit economics (estimates per Lite kit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32 module, isolated RS485, ADC front-end, 2× clamp sensors €6, CT clamp €5, e-paper/LEDs, PSU, PCB) | €31.00 | €24.00 |
| Assembly & test (SMT, 2-point temperature calibration, CT calibration) | €5.50 | €3.80 |
| Enclosure (hub ABS + 2 sensor clamps + insulation covers) | €6.50 | €4.20 |
| Packaging (box, cable ties, pads, quick sheet) | €2.50 | €1.80 |
| Freight + duty to EU | €3.00 | €1.80 |
| Certification amortised (~€28k: RED, EMC, safety, EN 18031) | €28.00 | €5.60 |
| **Landed cost** | **€76.50** | **€41.20** |
| Sell price (direct €199 / installer pack €160) | €199 | €160 |
| **Gross margin** | **€122.50 (62%)** | **€118.80 (74% at installer price)** |

### Go-to-market
**First 100 customers:** 100 forum members offered the Lite kit at €199 with the ±15% caveat in bold (kill question) — German heat-pump forums and owner clubs, the Dutch heat-pump forum, UK renewable-heating forums, Home Assistant communities; 5 YouTube/blog reviewers; 10 installers from the same forums who already recommend monitoring.

**Scale channels:** heat-pump wholesalers (installer 5-packs), installer associations' member shops, energy cooperatives and consumer-advice organisations (they love "check your settings"), Home Assistant add-on store listing, the Pro kit via the open-monitoring community (position as complementary, not competing: Lite for the many, Level-3 for the accurate).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from AC Measure unit + NCIR2/NTC clamps + RS485-ISO + an ESP32 dev kit; 100-member forum offer (kill question); estimate validated against 5 homes with heat meters. |
| Q2 | Own hub PCB, clamp sensor tooling, MQTT/HA integration, installer PDF; EVT 50; pre-compliance. |
| Q3 | DVT, certification, 300-unit pilot; Pro kit EVT with a bought-in flow meter; wholesaler conversation. |
| Q4 | 1,000 units; installer 5-packs; Modbus profiles for the 5 most common pump brands. |

**Team:** 1 embedded engineer (ADC front-end, calibration, Modbus — full-time), 1 software developer (estimation model, HA integration, PDF — full-time), founder for community and installers; a heating engineer on contract for the pump-curve database. Three people.

**Funding to first 1,000 units (estimates):** NRE €38k (PCB €8k, clamp tooling €10k, software €20k) + certification €28k + 1,000 units landed ~€55k + 9 months overhead €60k ≈ **€181k**; minus 100 forum pre-orders (€20k), pilot sales (300 × €189 ≈ €57k) and installer packs (~€30k) ≈ **~€75k**. Bootstrap + pre-orders; this one is pre-order-fundable because the community is online and loud.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** flow estimate is wrong → forum credibility dies | Label ±15% in bold everywhere; let users enter commissioning flow; publish the method; Pro kit with a real flow meter for the accurate crowd |
| **Technical:** pipe sensor coupling on insulated/shiny pipes | Spring clamp + thermal pad + insulating cover; test NTC vs IR; publish ±0.3 °C spec |
| **Market:** the serious buyer wants a heat meter | They're the Level-3 customer; don't fight — recommend it, sell the Lite to the other 90% |
| **Regulatory:** CT clamp on a live conductor; "installer-fitted" | Certified split-core clamp, Class II insulation, wording and pictures; never open a consumer unit in your manual |
| **Regulatory:** RED + EN 18031 + CRA for a WiFi device | Pre-certified module; local-first; budget it |
| **Market:** manufacturers add real COP to their apps | Some will; the cross-brand, local, honest number stays yours; Modbus read-out makes you the owner's dashboard anyway |
| **Supply:** CT clamps and e-paper | Multi-source clamps on a 3.5 mm jack; LEDs instead of e-paper as a fallback |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit AC Measure (U164) | https://www.gongbans.com/db/m5stack-unit-ac-measure.html | Power-measurement reference for the works-like | enclosure/structure only; electronics not published | Buy; measurement IC reference for your own board |
| Seeed Grove Electricity Sensor | https://www.gongbans.com/db/seeed-grove-electricity-sensor.html | CT-clamp current-sensing front-end reference | schematic | Seeed wiki resources; check licence |
| M5Stack Unit NCIR2 (U150) | https://www.gongbans.com/db/m5stack-unit-ncir2.html | Non-contact pipe temperature for the A/B test against contact NTC | enclosure/structure only; electronics not published | Buy; prototype only |
| M5Stack Unit RS485-ISO (U094) | https://www.gongbans.com/db/m5stack-unit-rs485-iso.html | Isolated Modbus read from pumps/meters that expose it | enclosure/structure only; electronics not published | Buy; isolated transceiver reference |

**Board-fact note:** no flow meter exists in the catalogue; the Pro SKU uses a bought-in flow meter.

### Block diagram
```
[Clamp T sensor: flow pipe]  [Clamp T sensor: return pipe]  [Split-core CT clamp on outdoor-unit supply]
          \                          |                               /
           +---- [precision ADC / NTC front-end + CT burden + RMS] ----+
                                     |
                   [ESP32-S3/C6: estimation model, cycling, defrost detect]
                     |            |              |               |
             [isolated RS485: Modbus from pump / meter]  [WiFi: MQTT/HA, web UI, installer PDF]
                     |
            [e-paper or LED bar: today's indicative efficiency]   [USB-C PSU (certified)]
```
**Engineering gap:** the estimation model and its honesty (pump-curve database, user flow entry, uncertainty display), sensor coupling mechanics, Modbus profiles per brand, and the installer PDF. The electronics are standard.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 or -C6 module | €2.60 | Pre-certified |
| Precision ADC (24-bit) or NTC front-end | €2.20 | Second-source footprint |
| 2× clamp pipe sensors (PT1000/NTC in spring clamp + pad + cover) | €6.00 | **Custom clamp tooling €8–10k** |
| Split-core CT clamp 50–100 A, 3.5 mm jack | €5.00 | **Buy certified; multi-source** |
| Isolated RS485 transceiver + protection | €2.00 | |
| E-paper 2.13" or LED bar | €4.00 | LEDs as fallback |
| PCB 4-layer, passives, USB-C, terminal blocks | €4.50 | |
| Hub enclosure ABS | €3.50 | Tooling €8–12k |
| Certified USB-C PSU | €2.50 | |
| Pro: ultrasonic/vortex flow meter (bought-in) | €60–120 | Not in catalogue; qualify 2 vendors |

### Firmware/software starting point
- **ESPHome** (exists) is the fastest route to a Home Assistant-native works-like; production firmware in ESP-IDF with MQTT.
- **OpenEnergyMonitor / HeatpumpMonitor.org** (exist) publish their COP methodology and emonHP firmware — read them, cite them, don't copy the product.
- Modbus: a standard Modbus-RTU library (search "esp-modbus"); brand register maps are mostly community-documented — search per brand.
- Estimation: your own; publish a notebook comparing estimate vs heat-meter truth from the 5 reference homes.
- Installer PDF: render in the browser from the device's JSON (search "jsPDF").

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Works-like on your own or a friend's heat pump next to a heat meter; **100 forum members offered the Lite at €199 with the ±15% caveat in bold — pass if ≥ 30 pre-order** (runs to W5) |
| 3–5 | Works-like | 5 homes with heat meters: estimate within ±15% daily on ≥ 4 of 5; NTC clamp vs IR decided; MQTT into HA |
| 6–8 | Looks-like + EVT | Hub PCB v1, clamp sensors T1, 50 units; installer PDF; 2 Modbus profiles; EMC pre-scan |
| 9–10 | DVT + pre-compliance | RED/EMC pre-compliance; EN 62368-1 review (CT input isolation); EN 18031 self-assessment; 30-day stability in 20 homes |
| 11–12 | Pilot batch | 50 units to pre-order holders + 10 installers; ≥ 80% installed without support; ≥ 5 users report changing a setting because of the number |

### Certification checklist (EU)
- **CE under RED** (WiFi): EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** (hub; CT input is a measurement input — the clamp itself is a certified bought-in part with its own insulation class); **EN 18031-1** (internet-connected, mandatory since 1 Aug 2025; -2 if you store household data on a hosted page). Est. €6–9k RED/EMC, €3–5k safety, €10–18k EN 18031.
- **Not MID** (no billing); say "indicative" and never "metering". **Not a measuring instrument** under any legal metrology.
- **RoHS, REACH, WEEE**, packaging registration. **Battery:** none (mains-powered — keep it so).
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware, OTA, SBOM, vulnerability contact.
- **GDPR:** energy data of a household is personal data when hosted → local-first by default; hosted page opt-in with a privacy notice.
- **Total certification budget estimate: €20–32k.**

### Validation toolkit
- **Kill question:** Offer the Lite kit at €199 to 100 heat-pump forum members with the ±15% caveat in bold. If ≥ 30 still pre-order, the market accepts "indicative".
- **Cheapest experiment (~€500):** one works-like on a real heat pump, a 2-minute video showing the daily number next to a heat meter's number, a one-page spec with the caveat, a pre-order page; post in 3 forums.
- **5-question interview (owner):** 1) What do you look at today to judge your heat pump, and how often? 2) Have you changed a setting in the last year — why, and what happened? 3) Would you accept a ±15% number if it's consistent day to day? 4) Do you run Home Assistant or similar? 5) €199, 30-minute install, no plumber — pre-order or not, and why?
- **Landing page:** headline "See your heat pump's real efficiency every day. No plumber needed." Bullets: "Two clip-on pipe sensors and one power clamp; 30-minute install." / "Indicative efficiency ±15%, local-first, Home Assistant native; Pro kit with a flow meter if you want ±5%." / "€199, no subscription."
- **Pass threshold:** 30 pre-orders out of 100 offers, or 150 pre-orders from open forum posts in 4 weeks.

### First production checklist
- Samples: 5 golden samples with 2-point temperature calibration and CT calibration against a reference meter.
- DFM: clamp spring force vs pipe range 15–35 mm, pad compression, cover insulation, hub terminal block strain relief; test jig with two thermal references and a current loop.
- MOQ talk: clamps 1k (multi-source), sensors 2k, ADC reel, e-paper 1k, hub case 1k.
- QC: AQL II 2.5/4.0; 100% calibration + WiFi test; 5% 24 h burn-in; CT clamp incoming inspection against the vendor's cert.
- Packaging: clamps separate from the hub; cable ties and pads; quick sheet with the caveat.
- Incoterms: FOB Shenzhen; air for 50; sea for 1,000.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit AC Measure (U164)](/db/m5stack-unit-ac-measure.html) (power measurement reference); [M5Stack Unit NCIR2 (U150)](/db/m5stack-unit-ncir2.html) (flow/return pipe temperatures); [M5Stack Unit RS485-ISO (U094)](/db/m5stack-unit-rs485-iso.html) (read Modbus from pumps and meters that expose it). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Electricity Sensor](/db/seeed-grove-electricity-sensor.html) (CT-clamp current sensing reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor — for a Heat-Pump COP Monitor Lite

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Heat-Pump COP Monitor Lite: A clip-on kit (two pipe temperature sensors + one power clamp) that shows your heat pump's real daily efficiency so owners catch bad settings and installers prove their work. The design is built around your M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor.
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
主题：样品订购及批量报价 — M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor — 用于Heat-Pump COP Monitor Lite

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Heat-Pump COP Monitor Lite：A clip-on kit (two pipe temperature sensors + one power clamp) that shows your heat pump's real daily efficiency so owners catch bad settings and installers prove their work。产品设计基于贵司的M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor。
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
Subject: PCBA quote from open design files — Heat-Pump COP Monitor Lite, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Heat-Pump COP Monitor Lite: A clip-on kit (two pipe temperature sensors + one power clamp) that shows your heat pump's real daily efficiency so owners catch bad settings and installers prove their work. The design starts from published open-hardware files (M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Heat-Pump COP Monitor Lite，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Heat-Pump COP Monitor Lite：A clip-on kit (two pipe temperature sensors + one power clamp) that shows your heat pump's real daily efficiency so owners catch bad settings and installers prove their work。设计基于已公开的开源硬件文件（M5Stack Unit AC Measure (U164), M5Stack Unit NCIR2 (U150), M5Stack Unit RS485-ISO (U094), Seeed Grove-Electricity Sensor；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order Unit AC Measure, Unit NCIR2, Unit RS485-ISO, two NTC clamp probes and an ESP32 dev kit; get ΔT and power into Home Assistant on a real heat pump by day 7.
2. Find 5 forum members who have a heat meter installed and will host a works-like for 4 weeks — they are your truth set.
3. Draft the pre-order post with the caveat in bold and a price; post it in one forum and count.

Want help sourcing or building this? Talk to us via www.gongbans.com.
