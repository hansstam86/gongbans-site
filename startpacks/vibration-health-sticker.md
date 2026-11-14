# Vibration Health Sticker — Founder Start Pack

> A magnet-mount battery sensor that watches vibration and temperature of pumps, fans and compressors and sends a weekly health trend over LoRaWAN — predictive maintenance for buildings that have no maintenance engineer.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** A school, a hospital's technical wing or a mid-size office has hundreds of motors (pumps, fans, compressors) and nobody listening to them. Failures are discovered when the building is cold or the ventilation is off. Industrial condition monitoring costs €500+ per point with a platform and an engineer; building owners have neither.
- **Customer:** Facility managers of schools, hospitals' technical services, property managers and HVAC service contractors in DE/NL/UK/Nordics. The owner/FM or the contractor pays; the technician who gets a red/amber/green list uses it.
- **Product:** A €89 magnet-mount node: 3-axis accelerometer and temperature, on-node RMS/peak/trend computation, LoRaWAN EU868 uplink of a few bytes a day, 5-year primary cell, IP65; a simple traffic-light dashboard per asset and a CMMS export; platform at €1/node/month.
- **Why now:** LoRaWAN is standard in buildings; MEMS accelerometers at €1–2 do what €200 piezo sensors did; an open ESP32-C6 + LoRa core exists; FM contracts increasingly require "condition-based" maintenance language.
- **The ask:** ~€100k (estimate) to the first 1,000 nodes; route = paid pilots with 3 facility managers + bootstrap; HVAC service contractors for scale.

## 2. Business plan

### Problem & customer
The HVAC pump in a school basement runs 8,000 hours a year. A bearing starts failing; vibration doubles over three months; nobody notices; it seizes in January. The replacement is an emergency call-out at 3× the price and two cold days. Industrial plants solve this with condition monitoring; buildings don't, because the systems are built for a reliability engineer and priced per point for a plant.

Who pays vs who uses: the building owner or FM company pays (capex per node + small platform fee), or the HVAC service contractor pays and bundles it into a maintenance contract (they save call-outs and win contracts with "we monitor your 40 motors"). The technician uses a list: red (look now), amber (plan), green. No spectra, no engineer.

### Market size (estimates)
- EU + UK commercial/public buildings with mechanical plant rooms: ~4 M (estimate); average 25 monitored-worthy motors → **100 M assets**; realistic candidates (≥ 1 kW, critical to comfort or hygiene) → 20% → **20 M assets**.
- **TAM:** 20 M × €89 ≈ **€1.8 B** hardware + €1/node/month platform (ceiling).
- **SAM:** buildings served by FM companies and HVAC contractors in the 4 countries → ~4 M assets → **€360 M** + platform.
- **SOM (3 years):** 0.5% → 20k nodes → **€1.8 M** hardware + ~€240k/year platform.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Industrial LoRaWAN vibration sensors (Advantech WISE-2410-class; 3-year battery at hourly uplink — [DigiKey](https://www.digikey.com/en/product-highlight/a/advantech/wise-2410sk-lorawan-starter-kit); vendor pricing opaque, accessories alone €10–50 — [Advantech EU](https://buy.advantech.eu/I-O-Devices-Communication/Industrial-Communication-LoRaWAN-Wireless-Sensor-Nodes/model-WISE-2410-EB.htm)) | Proven, industrial | Price per node, platform aimed at plants, spectra nobody in a school reads |
| Industrial wireless condition-monitoring platforms (Fluke/Treon/ABB-class) | Deep analytics, services | €500+ per point with gateways and subscriptions; built for plants |
| Milesight-class LoRaWAN building sensors (€58–82 for climate/sound/tilt — [iot-shop.de](https://iot-shop.de/en/shop/mil-ws203-868-milesight-ws203-868-lorawan-motion-humidity-and-temperature-sensor-6658), [aio.lv](https://aio.lv/en/product--milesight-ws302-868m--5074469.md)) | The building-IoT price anchor | No vibration-health product at that price with trend logic for motors |
| Quarterly technician round with a handheld vibration pen ("do nothing more") | Cheap | Four readings a year; the motor fails in between |
| BMS alarms (motor running/not running) | Already there | Binary; no early warning |
| DIY (ESP32 + accelerometer + MQTT) | A few FM tech leads | No battery life, no IP65, no trend logic, no CE |

**Wedge:** building-IoT price (€89), 5-year battery, magnet-on-and-walk-away install, on-node trend (tiny payload → battery life → price), a three-colour list instead of spectra, CMMS export, and HVAC contractors as the channel.

### Product & value proposition
Hardware: 45 mm puck, IP65, strong magnet base (and an adhesive/strap option for aluminium housings), 3-axis accelerometer (±16 g, 1.6–6.4 kHz ODR for bearing-band energy), surface temperature via the base (NTC) — the "temperature of the housing" is half the diagnosis, ESP32-C6-class MCU + LoRa (from the open C6LoRa core; a lower-power MCU in v2), primary Li-SOCl2 or Li-MnO2 cell for 5 years at 4 measurements/day, BLE for install/config. Firmware: wake 4×/day, capture 2 s at high ODR, compute RMS velocity (ISO 20816-class bands), peak, crest factor, bearing-band energy, temperature; compare to the asset's learned baseline; uplink 12 bytes; red/amber/green thresholds per asset class (pump, fan, compressor) with ISO-derived defaults. Platform: asset list, trend per node, alerts by email/webhook, CSV/CMMS export, LoRaWAN via the building's own network or a bundled gateway (bought-in).

Pricing (estimates): **€89 per node**, €79 at 50+, bundled gateway €199 (bought-in), platform €1/node/month (min €20/month) or run it on your own TTN/ChirpStack and MQTT for free. Contractors at 30% off, they add their service margin.

### Unit economics (estimates per node, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (MCU + LoRa €5.5, accelerometer €2, NTC €0.3, Li-SOCl2 AA cell €3.5, antenna + PCB + passives €4) | €15.30 | €12.00 |
| Assembly & test (SMT, vibration-table self-test, RF join test) | €3.00 | €2.00 |
| Enclosure (IP65 PC puck, magnet base, seal; tooling amortised) | €4.50 | €2.80 |
| Packaging (10-pack boxes, alcohol wipes, asset labels) | €1.00 | €0.70 |
| Freight + duty to EU (lithium primary cells — DG) | €1.50 | €0.90 |
| Certification amortised (~€28k: RED EN 300 220, EMC, EN 18031, IP65) | €28.00 | €5.60 |
| **Landed cost** | **€53.30** | **€24.00** |
| Sell price (direct €89 / contractor €62) | €89 | €62 |
| **Gross margin** | **€35.70 (40%)** | **€38 (61% at contractor price)** |

Thin at 1k because certification amortises over a cheap product; healthy at 5k. The platform fee is the business; hardware is the Trojan horse.

### Go-to-market
**First 100 customers:** 3 facility managers deploy 20 nodes each in a paid pilot (kill question: at least one caught failure in 6 months) — a school district's technical office, a hospital's technical services, a property manager with 10 office buildings; 2 HVAC service contractors who already do maintenance rounds; LoRaWAN community networks in cities (free coverage for the pilot).

**Scale channels:** HVAC and FM service contractors (bundle into maintenance contracts), building-IoT distributors (the ones selling the €60 LoRaWAN climate sensors), LoRaWAN network operators' marketplaces, public-sector framework agreements (schools, hospitals), BMS integrators (export to their dashboards).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like (Unit Accel / LIS3DH Grove + Stamp C6LoRa + LoRaWAN unit) on 60 motors in 3 pilots; baseline algorithms; dashboard v0. |
| Q2 | Own PCB (low-power MCU + LoRa), IP65 puck, magnet base; EVT 100; battery model validated; pre-compliance. |
| Q3 | DVT, certification, 500-node pilot across contractors; CMMS export; first caught failure documented. |
| Q4 | 1,000 nodes; distributor; contractor programme; v2 node with lower-power MCU for 7-year life. |

**Team:** 1 embedded engineer (low power, LoRa, DSP on-node — full-time), 1 backend/dashboard developer (platform, alerts, exports — full-time), founder for FMs and contractors; a vibration/maintenance consultant on contract for the thresholds and the asset classes. Three people.

**Funding to first 1,000 nodes (estimates):** NRE €48k (PCB €9k, puck tooling €12k, firmware/DSP €12k, platform €15k) + certification €28k + 1,000 nodes landed ~€53k + gateways (20 × €120 ≈ €2.4k) + 9 months overhead €70k ≈ **€201k**; minus pilot fees (3 × €3,000 ≈ €9k), pilot-batch sales (500 × €79 ≈ €40k), contractor prepayments (~€25k), platform fees in year one (~€10k) ≈ **~€100k**. Bootstrap + paid pilots; building-efficiency and public-sector innovation grants fit; an angel from FM/proptech is plausible once a caught failure exists.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** MEMS accelerometer vs real bearing faults — can a €2 sensor see an early fault? | Yes for RMS/peak trends and temperature, often not for very early high-frequency faults; sell "trend and temperature", not "fault diagnosis"; validate on 60 motors with a consultant's handheld as reference |
| **Technical:** 5-year battery claim | Model + measure; 4 wakes/day, 12-byte payloads, SF9–SF12 budget; publish the model; v2 with a lower-power MCU |
| **Technical:** magnet mount on painted/plastic housings; mounting position changes readings | Adhesive/strap option; install app insists on a photo of the position; relative trend not absolute level |
| **Market:** "we already have a BMS" | BMS says on/off; we say "getting worse" — show the trend of a pump that then failed |
| **Market:** low price, so the platform must sell | Free MQTT mode for the DIYers; the paid dashboard for the FM who wants a list and a PDF |
| **Regulatory:** RED (EN 300 220 duty cycle), EN 18031 for the platform-connected node, CRA; lithium primary cells (UN 3090/3091 transport) | Pre-certified module path; LoRaWAN security defaults; cells with transport docs; battery regulation labelling |
| **Supply:** accelerometer and LoRa transceiver allocation; Li-SOCl2 cells from few vendors | Two accelerometers on one footprint; two cell vendors |
| **Licence:** M5Stack C6LoRa sources, Seeed schematic | Check terms; your own board |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit Accel (U056) | https://www.gongbans.com/db/m5stack-unit-accel.html | 3-axis accelerometer module for the works-like | enclosure/structure only; electronics not published | Buy; datasheet for production |
| Seeed Grove 3-Axis Digital Accelerometer (LIS3DHTR) | https://www.gongbans.com/db/seeed-grove-3-axis-digital-accelerometer-lis3dhtr.html | Low-power accelerometer reference with schematic | schematic | Seeed wiki resources; check licence |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | Open ESP32-C6 + LoRa core — MCU + radio reference with Altium sources | pcb, schematic | M5Stack hardware repo — check licence terms |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | EU868 LoRaWAN uplink for the works-like (AT-command module) | enclosure/structure only; electronics not published | Buy; module vendor for production |

### Block diagram
```
[3-axis MEMS accelerometer, high ODR] --SPI--> [low-power MCU: 2 s capture, RMS/peak/crest/band energy, baseline compare]
[NTC in magnet base: housing temperature] ------->        |
                                                         [LoRa SX126x-class, EU868, LoRaWAN OTAA] -> gateway -> network server
                                                          |                                                   |
[Li-SOCl2 AA primary cell, 5 years @ 4 wakes/day]   [BLE for install/config (phone), off otherwise]   [platform: R/A/G list, trend, alerts, CMMS export]
[IP65 puck + magnet base / adhesive]
```
**Engineering gap:** on-node feature extraction within a tiny energy budget, asset-class thresholds and baseline learning, the 5-year battery model, mounting mechanics, and the dashboard that a non-engineer uses. Sensor and radio are solved.

### Starter BOM (estimates per node at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Low-power MCU (ESP32-C6 for v1 via the C6LoRa reference; STM32L4/WLE-class in v2) | €2.50 | The C6 is fine for v1; battery life drives v2 |
| LoRa transceiver SX1262-class (or STM32WLE integrating both) | €3.00 | Allocation cycles — two options on the board |
| 3-axis accelerometer, ±16 g, ≥ 3.2 kHz ODR, low power | €2.00 | **Two parts on one footprint** |
| NTC + thermal path in the base | €0.30 | |
| Li-SOCl2 AA 2.4 Ah + holder/tabs | €3.50 | **Two cell vendors**; UN 3090 transport docs |
| Antenna (PCB/FPC 868 MHz) + matching | €0.80 | |
| PCB 2-layer + passives | €3.00 | |
| IP65 PC puck + seal + magnet base | €4.50 | **Tooling €10–14k** |
| Gateway (bought-in, indoor LoRaWAN) | €120 | Resold at €199 or the customer uses their own network |

### Firmware/software starting point
- LoRaWAN stack: Semtech's **LoRaMac-node** (exists) or the **LoRa Basics Modem** (exists); network: **The Things Stack** / **ChirpStack** (both exist); payload decoder in JavaScript.
- Accelerometer drivers: vendor libraries exist for common parts (search "LIS3DH driver" / your chosen part); FFT on MCU: **arduinoFFT** (exists) or **CMSIS-DSP** (exists) on STM32.
- Thresholds: ISO 20816 (formerly 10816) vibration-severity zones as defaults per machine class — buy the standard, have the consultant adapt it.
- Platform: start with ChirpStack + Grafana (exists) for pilots; build the R/A/G list and PDF after the kill question.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 60 works-like nodes (Unit Accel or LIS3DH Grove + Stamp C6LoRa + LoRaWAN unit, in off-the-shelf IP65 boxes with magnets) deployed in **3 facility managers' buildings as paid pilots (€3,000 each, 20 motors each)**; baseline data flowing |
| 3–5 | Works-like | On-node RMS/peak/temperature within ±10% of a consultant's handheld on 20 motors; 12-byte payload; dashboard v0 with R/A/G; one amber asset explained |
| 6–8 | Looks-like + EVT | Own PCB + IP65 puck T1 + magnet base; 100 nodes; measured sleep current supports ≥ 5 years at 4 wakes/day; RF pre-scan; install via BLE phone page |
| 9–10 | DVT + pre-compliance | EN 300 220 / EMC pre-compliance; IP65 test; EN 18031 self-assessment; cell transport docs; CMMS export; 30-day false-alert rate ≤ 1 per 20 nodes per month |
| 11–12 | Pilot batch | 50–500 nodes to contractors; **at least one caught failure documented** (or an early red confirmed by a technician's inspection); contractor writes a case study |

### Certification checklist (EU)
- **CE under RED** (LoRa 868 MHz + BLE): **EN 300 220-1/-2** (incl. duty-cycle limits), EN 300 328 (BLE), EN 301 489-1/-3/-17, EN 62311; **EN IEC 62368-1** (battery device, low energy — light); **EN 18031-1** (the node is internet-connected via the network server — mandatory since 1 Aug 2025; LoRaWAN OTAA security defaults help; -2 not needed if no personal data). Est. €7–10k RED/EMC, €2–4k safety, €10–15k EN 18031.
- **Battery:** primary lithium cells — **UN 3090/3091** transport rules and labelling (not UN 38.3's rechargeable regime — but the cell vendor must supply test summaries), **EU Battery Regulation** labelling; the 2027 removability rules → user-replaceable cell behind a sealed door is the safe design.
- **RoHS, REACH, WEEE**, packaging. **IP65** test (IEC 60529) €1–2k.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware (FOTA over LoRaWAN is painful; plan BLE-based updates on site plus LoRaWAN FUOTA later), SBOM, vulnerability contact.
- **GDPR:** none (machine data; keep technician names out of the device). **Not safety-related, not functional safety** — an aid to planned maintenance.
- **Total certification budget estimate: €20–30k.**

### Validation toolkit
- **Kill question:** Do 3 facility managers deploy 20 nodes each in a paid pilot and report at least one caught failure in 6 months?
- **Cheapest experiment (~€2,500):** 60 works-like nodes from catalogue parts in IP65 boxes with magnets, ChirpStack + Grafana, 3 pilot agreements at €3,000; the "caught failure" takes months — so the interim pass is: 3 FMs pay, and after 8 weeks at least 3 assets show a trend that a technician confirms as real (loose mount, bearing noise, over-temperature).
- **5-question interview (facility manager / HVAC contractor):** 1) How many pumps, fans and compressors do you look after, and how do you find out one is failing? 2) What did the last emergency call-out cost, including the cold building? 3) Who would act on a red light — your own technician or a contractor? 4) Do you have a LoRaWAN network or a BMS you'd want this in? 5) €89 per motor and €1 a month — would you put 20 on your worst plant room this quarter?
- **Landing page:** headline "Know which motor is dying before the building goes cold." Bullets: "Magnet-mount sensor, 5-year battery, LoRaWAN — install in a minute, no wiring." / "Vibration and temperature trend per pump, fan and compressor; a red/amber/green list, not spectra." / "€89 per node, €1 a month, CMMS export."
- **Pass threshold:** 3 paid pilots signed (60 nodes), or 200 nodes pre-ordered by contractors in 8 weeks.

### First production checklist
- Samples: 5 golden samples with vibration-table response records, sleep-current log, RF join test on two gateways.
- DFM: seal and magnet retention, NTC thermal path to the base, antenna keep-out, cell holder vibration-proofing, label area for the asset ID/QR.
- MOQ talk: accelerometers reel (two parts qualified), LoRa transceivers reel, cells 1k (two vendors, transport docs), pucks 1k, magnets 1k.
- QC: AQL II 1.5/4.0 (it's small and cheap — tighten majors); 100% self-test on a vibration table + join test; 2% IP spray test; 1% 7-day sleep-current soak.
- Packaging: 10-pack boxes with UN 3091 marking (cells installed), alcohol wipes, asset labels, install card with the BLE page QR.
- Incoterms: FOB Shenzhen; air (DG) for 100; sea for 1,000.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Accel (U056)](/db/m5stack-unit-accel.html) (3-axis accelerometer module); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN uplink). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR](/db/seeed-grove-3-axis-digital-accelerometer-lis3dhtr.html) (low-power accelerometer reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*
- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR — for a Vibration Health Sticker

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Vibration Health Sticker: A magnet-mount battery sensor that watches vibration and temperature of pumps, fans and compressors and sends a weekly health trend over LoRaWAN — predictive maintenance for buildings that have no maintenance engineer. The design is built around your M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR.
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
主题：样品订购及批量报价 — M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR — 用于Vibration Health Sticker

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Vibration Health Sticker：A magnet-mount battery sensor that watches vibration and temperature of pumps, fans and compressors and sends a weekly health trend over LoRaWAN — predictive maintenance for buildings that have no maintenance engineer。产品设计基于贵司的M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR。
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
Subject: PCBA quote from open design files — Vibration Health Sticker, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Vibration Health Sticker: A magnet-mount battery sensor that watches vibration and temperature of pumps, fans and compressors and sends a weekly health trend over LoRaWAN — predictive maintenance for buildings that have no maintenance engineer. The design starts from published open-hardware files (M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Vibration Health Sticker，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Vibration Health Sticker：A magnet-mount battery sensor that watches vibration and temperature of pumps, fans and compressors and sends a weekly health trend over LoRaWAN — predictive maintenance for buildings that have no maintenance engineer。设计基于已公开的开源硬件文件（M5Stack Unit Accel (U056), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-3-Axis-Digital-Accelerometer-LIS3DHTR；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 10× Unit Accel (and 5× LIS3DH Grove for comparison), 10× Stamp C6LoRa, 10× Unit LoRaWAN-EU868, IP65 boxes and magnets; get one node reporting RMS from a fan to ChirpStack by day 7.
2. Approach 3 facility managers (a school district, a hospital, a property manager) with a €3,000 pilot for 20 motors; book the plant-room walk.
3. Buy ISO 20816-1 and draft the asset-class default thresholds with a maintenance consultant.

Want help sourcing or building this? Talk to us via www.gongbans.com.
