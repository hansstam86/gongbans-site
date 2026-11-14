# Bedroom Audit Box — Founder Start Pack

> A rental box that logs noise, light, CO2, temperature and humidity in a bedroom for seven nights and produces a plain-language sleep-environment report — rented out by mattress and sleep shops as an advisory service.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Sleep trackers measure the body; nobody measures the room. Peer-reviewed work links bedroom CO2, temperature and noise to lower sleep efficiency, yet the customer in a mattress shop is told to buy a firmer mattress.
- **Customer:** Mattress and bedding retailers, sleep coaches, wellness hotels (they buy or lease the fleet); consumers rent for a week (they use).
- **Product:** A one-button box with CO2, T/RH, light and sound-level sensors (no audio recording), a 7-night report with concrete recommendations, and fleet software that resets each box for the next renter.
- **Why now:** Sleep is the growth wellness category; NDIR CO2 sensors fell under €15; retailers need an advisory service that justifies a visit and drives ventilation, blackout and climate upsell.
- **The ask:** ~€120k (estimate) to a 1,000-box fleet across 150 shops. Route: pilot fees from 5 shops, then a retailer-partner or angel; leasing to shops makes the hardware a financed asset.

## 2. Business plan

### Problem & customer
A European mattress retailer (independent or small chain, DE/NL/BE/AT/CH/Nordics/UK) sells a €1,500 mattress and loses the customer for 10 years. A "sleep environment check" gives them a reason to return, a report to discuss, and a shelf of things to sell (blackout, pillows, climate duvets, air purifiers, ventilation advice). Who pays: the shop (fleet of 3–10 boxes, bought or leased) or the consumer (€25/week rental, often refunded against a purchase). Who uses: the consumer, who presses one button at bedtime for seven nights. Second buyer: sleep coaches and wellness hotels (box in the room, report at checkout).

The science isn't marketing: an observational actigraphy study of 62 adults found higher bedroom CO2, temperature and noise each associated with lower sleep efficiency (noise the largest effect) — [PubMed](https://pubmed.ncbi.nlm.nih.gov/37076419/). A 2025 review notes light and noise are the most commonly monitored factors by low-cost tools ([MDPI Applied Sciences](https://mdpi.com/2076-3417/15/3/1188)). Stay on *environment* and *comfort*; never say "diagnoses sleep disorders".

### Market size (estimates)
- Assume **~25,000 mattress/bedding retail outlets in EU + UK** (estimate; DE alone has several thousand bed shops) plus ~5,000 sleep coaches and wellness-hotel properties that would run a box.
- **TAM:** 30,000 locations × 5 boxes × €199 ≈ **€30 M** hardware, plus software/reports at €10/report ≈ 30,000 × 5 × 40 rentals/yr × €10 ≈ €60 M/yr theoretical.
- **SAM:** independents and small chains that run advisory selling (not discount warehouses) — 25% → 7,500 locations → **€7.5 M hardware + ~€15 M/yr** reports.
- **SOM (3 years):** 3% of SAM → 225 locations × 5 boxes ≈ 1,100 boxes → **€220k hardware + ~€450k/yr** in report/software fees if the boxes are actually rented 40 weeks a year (they won't be at first — plan on 20).

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Consumer air-quality monitors marketed for sleep (CO2, T/RH, noise, light; ~€130–250 — e.g. [Airthings Wave Enhance](https://www.airthings.com/wave-enhance)) | Good sensors, app-based | Consumer buys, no report, no retailer involvement, requires app + WiFi setup |
| Premium multi-sensor home hubs (~$549 incl. PM2.5, CO2, VOC, noise, light) | Lifestyle device | Price; not a rental workflow |
| Budget CO2 monitors (~$159, 4-year battery, no noise/light) | Popular, trusted | Single parameter, no report |
| Sleep trackers / wearables / under-mattress pads | Measure the body | Can't tell you *why* the room is bad |
| Sleep coach with a questionnaire / "do nothing" | The default advisory | No data; the customer forgets |
| DIY (ESP32 + sensors + Home Assistant) | Hobbyist | Not a retail service |

**Wedge:** the *service*, not the sensor: one button, zero setup, no WiFi needed at the customer's home (data stays on the box, uploads when returned to the shop), a report written for a shop conversation, and fleet management (auto-reset, hygiene wipe checklist, loss tracking). Source for device landscape: [T3 on bedroom monitors](https://t3.com/home-living/smart-home/this-tiny-smart-monitor-tracks-your-bedrooms-air-quality-to-help-improve-your-sleep).

### Product & value proposition
Hardware: 90 × 90 × 40 mm box, NDIR CO2, SHT3x-class T/RH, ambient-light sensor (lux, with colour-temperature if cheap), MEMS mic → dBA level only (no audio stored), e-paper or LED status, one button, 2,000 mAh Li-ion (7 nights + margin), USB-C. Software: on-box logging; dock/USB or WiFi upload at the shop; report generator (PDF + shop screen) with per-night charts and 3–5 recommendations; fleet console (which box is where, battery, reset, wipe log). Retailer branding on the report.

Pricing (estimates): **€199 per box to the shop** (or lease €12/month), **€5 per report** generated (or €25/month/box unlimited), consumer rental suggested at €25/week. Hotel/coach pack: 3 boxes + console €649.

### Unit economics (estimates per box, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32-S3 module, NDIR CO2, T/RH, light, MEMS mic + codec, e-paper 2.13", Li-ion 2,000 mAh, charger, PCB) | €46.00 | €37.50 |
| Assembly & test (SMT, flash, sensor sanity test, CO2 fresh-air check) | €5.50 | €3.80 |
| Enclosure (2-shell ABS/PC, light-sensor window, acoustic port, tooling amortised) | €5.20 | €3.20 |
| Packaging (reusable rental pouch + box) | €2.50 | €1.80 |
| Freight + duty to EU | €3.20 | €1.90 |
| Certification amortised (~€30k: RED, EMC, 62368-1, UN 38.3, EN 18031) | €30.00 | €6.00 |
| **Landed cost** | **€92.40** | **€54.20** |
| Sell price to shop | €199 | €199 |
| Channel margin (direct at 1k; 15% via bedding wholesalers at 5k) | €0 | €29.85 |
| **Gross margin** | **€106.60 (54%)** | **€114.95 (58%)** |

Plus report/software fees at ~90% margin. Hardware margin is healthy because the shop is paying for a service tool, not a gadget. Rental churn (lost/damaged boxes) is on the shop.

### Go-to-market
**First 100 customers (shops):** 5 pilot shops from the kill question (3 boxes each, 2 months, €450 pilot fee), then the national bedding-trade fairs and associations (DE: the bedding and sleep trade events in Cologne; NL/BE: independent bed-shop buying groups; UK: the bed-retail trade bodies). Sleep-coach networks and sleep-literacy influencers for the service story. A branded report template per chain.

**Scale channels:** bedding wholesalers and buying groups (they aggregate hundreds of independents), mattress brands (co-funded fleets: "free sleep-environment check with your purchase"), wellness-hotel suppliers.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from catalogue units; 15 boxes to 5 shops for 2 months; report v1; measure whether the report changes purchases (kill question). |
| Q2 | Custom PCB + tooled case; EVT 50; fleet console v1; pilot results into a case study. |
| Q3 | DVT, certification, 500 boxes to 50 shops; wholesaler talks. |
| Q4 | 1,000 boxes in ~150 shops; report fees flowing; hotel pack launched. |

**Team:** 1 embedded engineer (sensors, power, logging — full-time), 1 full-stack developer (report generator + fleet console — full-time), founder for retail sales; an industrial designer and a sleep scientist as advisers/part-time (the report must be credible). Three people.

**Funding to first 1,000 units (estimates):** NRE €55k (PCB €10k, tooling €15k, report/console software €25k, design €5k) + certification €30k + 1,000 boxes landed ~€62k + 9 months salaries/overheads €85k ≈ **€232k**; minus pilot fees and shop pre-payments (~€110k if 50 shops pre-pay 5 boxes at €199) ≈ **~€120k**. Route: pilots + pre-payment from shops, then an angel from retail or a mattress brand as strategic partner. Leasing boxes to shops via a small leasing partner turns the fleet into financed inventory.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** NDIR CO2 drift and the need for fresh-air calibration; mic-level calibration | Automatic baseline calibration at the shop dock; factory calibration; publish accuracy (±50 ppm, ±3 dBA) |
| **Technical:** 7 nights on battery with CO2 sampling | Sample CO2 every 5 min, not continuously; 2,000 mAh is plenty if the radio stays off at home |
| **Market:** shops don't push the rental; boxes sit in a drawer | Pilot metric is "rentals per box per month"; build the report into the sales script; mattress-brand co-funding |
| **Market:** the consumer finds the report obvious ("open a window") | Specific, quantified: "CO2 exceeded 1,500 ppm for 4.2 h on 5 of 7 nights; your window was closed on those nights" |
| **Regulatory:** a mic in a bedroom = GDPR anxiety | Compute dBA on the device, store levels only, no audio buffer beyond 125 ms; put it in the privacy notice and on the box; EN 18031-2 covers it |
| **Regulatory:** wellness vs medical | No sleep-disorder, apnoea or health claims; "sleep environment" only |
| **Supply:** NDIR CO2 sensors have had allocation issues | Qualify two sensor families on the same footprint |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Seeed Grove Loudness Sensor | https://www.gongbans.com/db/seeed-grove-loudness-sensor.html | Sound-level front-end reference (level only) | schematic | Seeed wiki resources; check licence |
| M5Stack Unit CO2L (U104) | https://www.gongbans.com/db/m5stack-unit-co2l.html | NDIR CO2 for the prototype | enclosure/structure only | Buy the unit; design your own board around the sensor later |
| M5Stack Unit DLight (U136) | https://www.gongbans.com/db/m5stack-unit-dlight.html | Ambient-light (lux) reference | enclosure/structure only | Buy for prototype |
| Seeed Grove TempAndHumi Sensor (SHT31) | https://www.gongbans.com/db/seeed-grove-tempandhumi-sensor-sht31.html | ±0.3 °C T/RH reference circuit | schematic | Seeed wiki resources |

For the prototype MCU/display use any ESP32-S3 dev board with battery support from the catalogue (M5Stack Core-class or Stamp-S3Bat — the latter publishes pcb+schematic).

### Block diagram
```
[NDIR CO2]  [SHT3x T/RH]  [lux sensor]  [MEMS mic -> dBA on MCU, no audio stored]
     \          |             |              /
      ----------+-------------+-------------
                | I2C / I2S
            [ESP32-S3] --> [flash log 7 nights] --> (at shop) USB-C/WiFi --> [report generator] --> PDF + fleet console
            [2.13" e-paper / LED]  [1 button]  [2,000 mAh Li-ion + charger, USB-C]
```
**Engineering gap:** all sensors exist as modules; nothing in the catalogue does on-device dBA, 7-night power budgeting, or the report. The work is firmware (sampling schedule, dBA computation, data model), the report engine (the actual product), and the fleet workflow.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| NDIR CO2 sensor (SCD4x-class or similar) | €14.00 | **Allocation risk**; two families qualified |
| T/RH sensor (SHT3x-class) | €1.80 | Multi-source |
| Ambient-light sensor | €0.60 | |
| MEMS microphone (I2S or analogue) | €0.90 | Multi-source |
| ESP32-S3 module | €2.60 | RED pre-certified |
| 2.13" e-paper + driver (or 4 LEDs for the cheap version) | €6.50 / €0.40 | E-paper lead times 6–10 weeks |
| Li-ion 2,000 mAh with PCM + charger IC | €4.20 | UN 38.3 report from the cell vendor |
| PCB 4-layer, passives, USB-C, button | €3.80 | |
| Enclosure 2-shell + windows + acoustic mesh | €5.20 | **Tooling €12–18k** |

### Firmware/software starting point
- ESP-IDF; vendor drivers for SCD4x and SHT3x exist (Sensirion publishes embedded drivers on GitHub). M5Stack Arduino libraries for Unit CO2L/DLight for the prototype (search "M5Unit-ENV").
- dBA: implement A-weighting on I2S samples — several open ESP32 sound-level-meter projects exist (search "ESP32 I2S sound level meter A-weighting").
- Report generator: Python + a PDF library; fleet console: any web framework. Nothing exotic.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 15 boxes from catalogue units in printed cases; 5 shops rent 3 each (runs to W10). Kill question: do the shops keep renting them out, and does the report change what customers buy (shop reports ≥1 upsell per 3 rentals)? |
| 3–5 | Works-like | 7 nights on battery; CO2/T/RH/lux/dBA logged every 1–5 min; report v1 generated from a USB dump in <2 min |
| 6–8 | Looks-like + EVT | Custom PCB v1, tooled case T1, 50 units; dBA within ±3 dB of a class-2 meter; CO2 within ±50 ppm of reference; EMC pre-scan |
| 9–10 | DVT + pre-compliance | RED/EMC pre-compliance; EN 18031 self-assessment (-1, -2); UN 38.3; GDPR DPIA; fleet console with reset/wipe log |
| 11–12 | Pilot batch | 50 boxes to 15 shops; rentals per box per month ≥ 2; report NPS from consumers ≥ 40 |

### Certification checklist (EU)
- **CE under RED** (WiFi/BLE): EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** safety; **EN 18031-1 and -2** (internet-connected, processes personal data — mandatory since 1 Aug 2025). Est. €6–9k RED/EMC, €3–5k safety, €10–18k EN 18031 incl. notified body.
- **RoHS, REACH, WEEE** (producer registration per country; the box is a rental asset, still WEEE).
- **Battery Regulation (EU) 2023/1542** + **UN 38.3**; design the cell to be replaceable by a technician (2027 removability requirement).
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027: signed firmware, update mechanism (via the dock), SBOM, disclosure policy.
- **GDPR:** sound *levels* and room data are low-risk, but combined with a renter's name in the fleet console they are personal data. Controller: the shop; you: processor. DPA, DPIA, no audio recording — state it on the device.
- **Not medical** as long as claims stay environmental. **Toy directive:** no.
- **Total certification budget estimate: €25–35k.**

### Validation toolkit
- **Kill question:** Do 5 mattress shops rent out 3 boxes each for 2 months, and does the report change what customers buy?
- **Cheapest experiment (~€1,500):** 15 boxes from Unit CO2L + DLight + Grove loudness + SHT31 on an ESP32-S3 dev board in printed cases; reports made by hand in a spreadsheet template for the first 20 rentals. Count rentals and upsells.
- **5-question interview (shop owner/manager):** 1) How often does a mattress customer come back within a year, and why? 2) Do customers mention noise, heat, stuffiness or light when they describe bad sleep? 3) Do you sell anything today that addresses the room (blackout, climate duvets, pillows, air)? 4) Would you rent a box for €25/week, refunded on purchase? Would you pay €199 per box or €12/month? 5) What would the report have to say for you to trust it in front of a customer?
- **Landing page (for shops):** headline "Sell the sleep, not just the mattress." Bullets: "A 7-night room check your customer takes home — one button, no app." / "A plain-language report that opens the conversation about ventilation, light and noise." / "Fleet of 3–10 boxes, auto-reset, your logo on every report."
- **Pass threshold:** 5 shops pay the €450 pilot fee within 4 weeks and ≥ 60% of pilot boxes are rented out in any given week of month two.

### First production checklist
- Samples: 5 golden samples with sensor calibration records; acoustic port and light window checked against the reference.
- DFM: sensor venting (CO2 needs airflow, mic needs an acoustic path, light sensor needs a clear window), battery compartment serviceability.
- MOQ talk: CO2 sensor 500–1k; e-paper 1k; case 1k; cells 1k. Price steps at 5k in writing.
- QC: AQL II 2.5/4.0; 100% sensor sanity test (fresh-air CO2 band, T/RH plausibility, mic level with a tone source); 5% 7-night battery sample test per batch.
- Packaging: rental pouch that survives 50 cycles; printed quick-start on the pouch, not a leaflet.
- Incoterms: FOB Shenzhen; lithium → DG surcharge; consolidate with sea freight at 5k.

## 4. Next steps (this week)
1. Order 15 sets (Unit CO2L, Unit DLight, Grove Loudness, Grove SHT31, ESP32-S3 battery dev board) and print 15 cases; get one logging 7 nights by day 10.
2. Write the report template with a sleep scientist friend or a published guideline as the source for every recommendation — the report is the product.
3. Visit 10 independent mattress shops with a mock report and the pilot offer (3 boxes, 2 months, €450).

Want help sourcing or building this? Talk to us via www.gongbans.com.
