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

## 4. Next steps (this week)
1. Order 10× Unit Accel (and 5× LIS3DH Grove for comparison), 10× Stamp C6LoRa, 10× Unit LoRaWAN-EU868, IP65 boxes and magnets; get one node reporting RMS from a fan to ChirpStack by day 7.
2. Approach 3 facility managers (a school district, a hospital, a property manager) with a €3,000 pilot for 20 motors; book the plant-room walk.
3. Buy ISO 20816-1 and draft the asset-class default thresholds with a maintenance consultant.

Want help sourcing or building this? Talk to us via www.gongbans.com.
