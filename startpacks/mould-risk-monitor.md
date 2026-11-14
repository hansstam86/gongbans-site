# Mould-Risk Monitor — Founder Start Pack

> A wall puck that measures room humidity and the actual surface temperature of the cold outer wall, computes the dew point and tells tenants when to ventilate — before mould appears, and with a log that settles the landlord-tenant argument.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Lower heating and less ventilation since 2022 have driven mould complaints in rented flats across Germany and the Netherlands. Disputes come down to "did the tenant ventilate or is the wall badly insulated" — and nobody has data. A €8 hygrometer measures room air, not the cold wall where mould actually grows.
- **Customer:** Housing associations and private landlords (they pay), tenants (they use). Second channel: building-energy consultants and mould surveyors who want a logger they can leave behind.
- **Product:** A battery wall puck: room T/RH plus a non-contact IR reading of the wall surface it points at. Computes surface dew-point margin, shows a traffic light, logs 90 days, exports a PDF. WiFi/BLE basic; LoRaWAN variant for associations. €59–79 B2C; €45–55 B2B at volume (estimates).
- **Why now:** Energy prices, the German "richtig heizen und lüften" campaigns, and a wave of landlord-tenant disputes. Existing B2B sensors (e.g. Sentinum Febris SCW) sit at professional prices and need a platform; no cheap standalone device with a dispute-grade log exists that we found.
- **The ask:** ~€95k to certification and 1,000 units; half via a housing-association paid pilot and a second via regional building-energy grants.

## 2. Business plan

### Problem & customer

Mould grows when the surface relative humidity at the wall exceeds ~80% for sustained periods — which happens at a cold outer wall or corner even when the room centre reads a comfortable 55%. Consumer hygrometers miss this entirely; Verbraucherzentrale explicitly says a normal hygrometer cannot judge the wall. The surveyor's answer is a visit with a Testo, once. The problem is continuous.

- **Who pays, B2B (primary):** housing associations (NL: woningcorporaties, ~2.3M homes; DE: Wohnungsunternehmen in GdW, ~6M homes). Their cost of one mould case (inspection, remediation, legal, rent reduction) is easily €2–5k. A €50 device per at-risk flat is noise.
- **Who pays, B2C:** tenants in a dispute (want evidence they ventilated), owners of older flats, parents' bedrooms with condensation on windows. They find you via Google "Schimmel Mietwohnung wer ist schuld".
- **Who uses:** the tenant. The device must be dumb-simple: traffic light, one button, no app required for the basic promise.

### Market size (estimates — check)

- **TAM:** rented homes in NL + DE + AT ≈ 27M. Older stock (pre-1995, uninsulated outer walls) ≈ 50% → ~13M homes. One device per home at €50 = **€650M** theoretical.
- **SAM:** flats in professional housing stock with a history of mould complaints — industry anecdotes put complaint rates at 5–10% of stock per year → **600k–1.3M flats** in NL/DE/AT; at €50 B2B that is €30–65M, plus the B2C tail.
- **SOM (3 yrs):** 3–5 housing associations at 1–3k units each plus 5k B2C → **15–25k units**. Year-1: 1,000–3,000.

### Competition (2 searches)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / open window on schedule | Verbraucherzentrale leaflets: 3–4× daily Stoßlüften | No feedback loop; still ends in dispute |
| €8–30 thermo-hygrometer (TFA Dostmann etc., some with "mould alarm") | Room RH only, some calculate dew point from room values | Blind to the wall surface temperature — which is the whole point |
| Sentinum Febris SCW and similar LoRaWAN wall sensors | Professional, dew-point at the wall, platform-based | Professional pricing and platform required; no consumer or standalone PDF-log version |
| Smart-home climate sensors (Aqara, Shelly H&T, Netatmo) + Homey/HA dew-point apps | DIY dew-point logic | Needs a hub and an enthusiast; no wall temperature; no dispute export |
| Surveyor visit with a Testo | Accurate, once | €150–300 per visit, no history |

**Wedge:** the only device under €80 that measures the wall, not the air, and produces a tamper-evident log both parties accept.

### Product & value proposition

- Puck ~70 mm, battery (2× AA or a Li-ion cell — pick AA for the Battery Regulation simplicity), mounts 10–20 cm from the suspected cold spot, IR sensor aimed at it.
- Computes room dew point and surface RH; three LED states: green (margin >3 K), amber (1–3 K), red (<1 K → ventilate/heat now). Button press = quick "did I ventilate" marker.
- Log 90 days at 10-minute intervals in flash; export over BLE to a phone web-app that renders a PDF with hashes (tamper evidence). LoRaWAN SKU uplinks hourly to the association's dashboard.
- **Pricing (estimates):** B2C €69 (WiFi/BLE). B2B €49 (BLE-only, 1k+) / €65 (LoRaWAN) plus optional dashboard €0.50 per device-month. Consultant kit of 5 + PDF tool €349.

### Unit economics (estimates, EUR per unit; BLE/WiFi SKU)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C3-class module €2.3, SHT3x/SHT4x T/RH €1.8, MLX90614-class IR thermometer €4.5–6, LEDs/button/passives €0.8, PCB €0.7) | 11.5 | 9.6 |
| PCBA assembly + test (incl. IR calibration check) | 2.6 | 1.7 |
| Enclosure (two-shot ABS puck + IR window + battery door) | 3.2 | 2.1 |
| Packaging + 2× AA + mounting strip + leaflet | 2.6 | 2.0 |
| Freight + duty to EU | 2.3 | 1.1 |
| Certification amortised (€16k) | 16.0 | 3.2 |
| **Landed cost** | **38.2** | **19.7** |
| D2C net price (€69 incl. 19% VAT → €58) less €8 fulfilment | 50.0 | 50.0 |
| **Gross margin D2C** | **€11.8 (24%)** | **€30.3 (61%)** |
| B2B at €49 ex VAT (direct, no retail) | €10.8 (22%) | €29.3 (60%) |

The IR sensor is the BOM lever: a factory-calibrated MLX90614-class part is €4–6; a cheaper thermopile is €2–3 but you then own the calibration. Pilots with the accurate part; cost-down later.

### Go-to-market

**First 100 customers:** one Dutch woningcorporatie or German Wohnungsbaugesellschaft with a known mould backlog — their technical manager, pitched as a 100-unit paid pilot (€4,900). In parallel, B2C: Mieterverein/Mieterbund newsletters, the bauexpertenforum and bau.de forums, r/Finanzen-adjacent housing subreddits, a Google ad on "Schimmel Mietwohnung Beweis".

**Then scale:** housing associations via their trade bodies (GdW regional associations, Aedes in NL), property managers (Hausverwaltungen), insurers (building insurers lose money on mould claims — co-funded devices), building-energy consultants as a channel (they leave the device after a visit), Amazon.de for B2C.

### 12-month plan

- **Q1:** survey in one association (kill question), 10 hand-built prototypes on Stamp-C3 + Unit NCIR2 + Grove SHT31, deploy in 10 problem flats for 6 weeks. Lab quotes.
- **Q2:** own PCB (rev A), enclosure design, 100-unit paid pilot with the association; PDF export; firmware hardening.
- **Q3:** rev B, certification, 1,000-unit run; LoRaWAN SKU EVT.
- **Q4:** second association, consultant kits, B2C launch in DE; insurer conversation.

**Team:** firmware engineer (full-time), hardware engineer (half), founder on sales with a building-physics advisor (consultant, a few days). Shenzhen partner for PCBA, IR-sensor sourcing and enclosure.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €22k + tooling €9k + certification €16k + prototypes/pilot €6k + 6 months team €45k + sales travel/marketing €6k = **≈€104k**. Pilot revenue €5–10k plus association pre-payment for the 1,000 (€49k if they commit) covers half. Route: paid pilot + pre-payment; regional grants for housing innovation (DE: regional Wohnungsbau-Innovationsfonds; NL: provincial energy-transition schemes — search current ones); angel only to add the LoRaWAN platform.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** IR surface reading drifts with emissivity, dust, sun on the wall | Fix emissivity for painted walls (~0.95), shade logic, and compare with a contact NTC in the pilot; publish accuracy honestly |
| **Market:** associations buy only with a platform, not a puck | Offer the BLE puck + CSV first; add LoRaWAN only when a pilot asks and pays |
| **Legal:** data used in disputes → "is your log admissible?" | Don't claim legal weight; claim tamper-evident physics. Keep raw data on-device, hashed exports |
| **Regulatory:** GDPR — ventilation behaviour is personal data about a tenant | Device stores no identity; association dashboard pseudonymises by flat; DPIA template in the box |
| **Supply:** IR thermopile lead times (8–16 weeks, few sources) | Two approved parts; buy 1,200 at EVT |

No medical claims: this is building physics and comfort. Say "mould risk", never "health".

## 3. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Seeed Grove-TempAndHumi Sensor-SHT31 | https://www.gongbans.com/db/seeed-grove-tempandhumi-sensor-sht31.html | Room T/RH reference circuit (SHT31, I²C) | schematic | Seeed wiki resources — check |
| M5Stack Unit NCIR2 (U150) | https://www.gongbans.com/db/m5stack-unit-ncir2.html | Non-contact IR surface temperature; prototype module | enclosure/structure only — electronics not published | Buy as module; design your own IR stage for the product |
| M5Stack Unit ENV-Pro (U169) | https://www.gongbans.com/db/m5stack-unit-env-pro.html | Alternative high-accuracy environmental sensor for A/B in pilot | enclosure/structure only | Module for prototyping only |
| M5Stack Stamp-C3 (C056-B) | https://www.gongbans.com/db/m5stack-stamp-c3.html | WiFi/BLE MCU; open Altium PCB to copy module footprint/antenna | pcb (Altium) | M5_Hardware repo — check licence |

Sensor chip inside NCIR2 is not in the catalogue; verify on M5 docs before you design around it.

### Block diagram

```
2×AA (or Li-ion) ──► boost/LDO 3.3V ──► ESP32-C3 (BLE/WiFi, flash log)
                                           │ I²C
                      ┌────────────────────┼────────────────┐
                 SHT3x room T/RH    IR thermometer (wall)   RGB LED + button
                                           │
                     dew point(T,RH) vs wall T → margin → colour; 10-min log
BLE ──► phone web-app (PDF export, hashed) ; optional LoRaWAN uplink hourly
```

**Engineering gap:** the IR optics (field of view vs mounting distance), power budget to reach 12 months on 2×AA with hourly BLE adverts, and a boring, trustworthy PDF.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-C3 module | €2.3 | Pre-certified |
| SHT40/SHT31 | €1.8 | Sensirion — reliable supply |
| MLX90614-class IR thermometer (medical-grade not needed) | €4.5–6 | **Long-lead, few sources**; alternative thermopiles from Chinese vendors €2–3 |
| LDO/boost + reverse-battery protection | €0.6 | |
| RGB LED, tact switch, passives | €0.5 | |
| PCB 2-layer 55 mm | €0.7 | |
| Enclosure + IR window (PE film or Ge-free lens) | €3.2 | Window material affects IR reading — test |
| 2× AA alkaline | €0.5 | |

### Firmware/software starting point

- **ESP-IDF** with NimBLE for the BLE log transfer; **ESPHome** for the pilot (SHT3x and MLX90614 components exist in ESPHome — verify versions).
- Dew point: Magnus formula; surface RH from wall temperature — standard building-physics equations (DIN 4108-2 context for Germany — read it).
- PDF: generate client-side in the web app (jsPDF exists) so no server holds tenant data.
- LoRaWAN SKU: **RadioLib** or Semtech **LoRaMac-node**; **ChirpStack** or **The Things Stack** for the association backend.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 300-tenant survey via one association + 10 interviews; bench test: Stamp-C3 + NCIR2 + Grove SHT31 against a contact probe on a real cold wall | ≥30/300 would pay €59; IR vs contact within ±0.7 K on painted wall |
| 3–5 | **Works-like** — 10 pucks (printed housing) in 10 problem flats, BLE log, basic CSV | 10/10 log 6 weeks; traffic light matches surveyor assessment in ≥8/10 |
| 6–8 | **Looks-like + EVT** — rev A PCB, IR window tested, enclosure printed; 30 units; battery current profile | Sleep current <30 µA average incl. adverts; projected 12 months on AA |
| 9–10 | **DVT + pre-compliance** — rev B, pre-scan EMC, EN 18031 checklist (BLE/WiFi), PDF export with hashes | No EMC fails; export verified by an independent engineer; DPIA template drafted |
| 11–12 | **Pilot batch** — 50–100 units to the association, dashboard CSV, training leaflet for tenants | ≤2% field failure; association signs the 1,000-unit order or a letter of intent |

### Certification checklist (EU)

- **CE — RED** (BLE/WiFi via module): EN 301 489-1/-17, EN 62368-1 (battery, low voltage): €6–9k. LoRaWAN SKU adds EN 300 220 checks (module pre-cert helps): +€3–5k.
- **EN 18031** if WiFi-connected (the BLE-only puck arguably also falls under RED cyber if it processes personal data — ask the lab): €2–4k review.
- **CRA:** SBOM, update path, vulnerability contact.
- **RoHS, WEEE, REACH, packaging registration.**
- **Battery Regulation:** AA alkaline = portable batteries you place on the market → registration and labelling; if Li-ion, add UN 38.3 and user-replaceability design for 2027.
- **GDPR:** ventilation behaviour per flat is personal data → DPIA, pseudonymisation on the dashboard, tenant information sheet.
- No toy directive; no medical claims (MDR not applicable if you stay on building physics).
- **Total estimate:** €14–18k first year (both SKUs €20–24k).

### Validation toolkit

- **Kill question:** Do 30 of 300 tenants in one housing association's survey say they would pay €59 for a device that documents ventilation behaviour? Cheapest experiment: the association sends a 5-question survey in their newsletter; you offer 10 free pilot devices as the incentive.
- **Interview script (5):** 1) When did you last have condensation or mould, and where exactly? 2) What did the landlord say was the cause? What did you say? 3) How do you decide when to open the windows today? 4) If a puck showed red at the corner, would you act — and what would make you ignore it? 5) Would you pay €59, or should your landlord pay — and would you accept the landlord seeing the data?
- **Landing page:** Headline: "Know when your wall is about to grow mould." Bullets: "Measures the cold wall, not just the air." / "Green, amber, red — ventilate when it matters." / "90-day log you can hand to your landlord (or your tenant)."
- **Pre-order pass:** one association pilot order ≥100 units at ≥€39, OR ≥150 B2C deposits of €10 in 30 days.

### First production checklist

- Samples: 5 PCBAs from two assemblers; golden sample with IR reading verified against a blackbody reference at 15 °C and 25 °C.
- DFM: IR window seal, battery door, wall-mount pattern (adhesive + screw).
- MOQ: PCBA 500; IR sensor reel 1k; enclosure 1k shots.
- QC/AQL: Z1.4 II, AQL 1.0/2.5; 100% functional test with a warm/cold target plate; RH check at ambient within ±3%.
- Packaging: AA batteries included → battery labelling; drop test.
- Incoterms: FOB Shenzhen; batteries change the shipping paperwork even for alkaline (declare).

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Seeed Studio and M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-TempAndHumi Sensor-SHT31](/db/seeed-grove-tempandhumi-sensor-sht31.html) (room T/RH reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit NCIR2 (U150)](/db/m5stack-unit-ncir2.html) (non-contact surface temperature of the wall); [M5Stack Unit ENV-Pro (U169)](/db/m5stack-unit-env-pro.html) (alternative high-accuracy environmental sensor); [M5Stack Stamp-C3 (C056-B)](/db/m5stack-stamp-c3.html) (WiFi/BLE MCU). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B) — for a Mould-Risk Monitor

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Mould-Risk Monitor: A wall puck that measures room humidity and the actual surface temperature of the cold outer wall, computes the dew point and tells tenants when to ventilate — before mould appears. The design is built around your Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B).

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B).
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
主题：样品订购及批量报价 — Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B) — 用于Mould-Risk Monitor

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Mould-Risk Monitor：A wall puck that measures room humidity and the actual surface temperature of the cold outer wall, computes the dew point and tells tenants when to ventilate — before mould appears。产品设计基于贵司的Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B)。
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
Subject: PCBA quote from open design files — Mould-Risk Monitor, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Mould-Risk Monitor: A wall puck that measures room humidity and the actual surface temperature of the cold outer wall, computes the dew point and tells tenants when to ventilate — before mould appears. The design starts from published open-hardware files (Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Mould-Risk Monitor，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Mould-Risk Monitor：A wall puck that measures room humidity and the actual surface temperature of the cold outer wall, computes the dew point and tells tenants when to ventilate — before mould appears。设计基于已公开的开源硬件文件（Seeed Grove-TempAndHumi Sensor-SHT31, M5Stack Unit NCIR2 (U150), M5Stack Unit ENV-Pro (U169), M5Stack Stamp-C3 (C056-B)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Call the technical manager of one housing association you can reach and ask for a newsletter survey plus 10 pilot flats; draft the 5 survey questions today.
2. Order Stamp-C3, Unit NCIR2, Unit ENV-Pro and a Grove SHT31; build one puck and tape it to the coldest corner you know; log a week against a contact thermometer.
3. Read DIN 4108-2 / the Verbraucherzentrale mould guidance and write the one-page "how we compute risk" note — this becomes your marketing and your legal protection.

Want help sourcing or building this? Talk to us via www.gongbans.com.
