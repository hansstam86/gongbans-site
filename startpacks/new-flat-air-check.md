# New-Flat Air Check — Founder Start Pack

> A handheld formaldehyde + VOC + CO2 meter that renters, buyers and parents use for a week after a renovation or new furniture, then return — sold to rental and real-estate channels rather than consumers.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** New flat-pack furniture, fresh laminate and a renovated flat smell — and people worry about formaldehyde. The German guideline value is 0.1 ppm (≈ 124 µg/m³, UBA Richtwert I 0.1 mg/m³); a lab measurement costs €150–250 per room, a consumer meter is €20–120 of unknown accuracy. People need an answer for one week, not an instrument for life.
- **Customer:** Furniture and flooring retailers (loan units at the till), real-estate agents and property managers (hand-over kit), and parents setting up a nursery. The retailer or agent pays and lends; the household uses. Consumer sale is the secondary channel.
- **Product:** A rugged handheld with an electrochemical HCHO sensor, a BME680-class VOC/T/RH sensor and an NDIR CO2 sensor, 7-day logging, and a "move-in report" PDF via the phone. Sold at €199, rented at €29/week; the fleet model: 5 loan units per store, annual recalibration as a service (estimates).
- **Why now:** Indoor-air awareness is mainstream, formaldehyde in furniture is a recurring consumer-press topic, and open sensor boards plus an off-the-shelf handheld dev kit make the prototype a two-week job. The gap is not the sensor — it is the calibration and the rental/report workflow.
- **The ask:** ~€85k to 1,000 units; three furniture retailers running loan fleets first, then a crowdfunding/B2C wave once the report format proves itself.

## 2. Business plan

### Problem & customer

The consumer question is "is this smell dangerous for my child?" and the honest answer is "measure it over a few days with the room closed and compare to 0.1 ppm". Nobody does that because the tools are wrong-sized: a €800–1,500 whole-flat lab analysis (one provider's range) is disproportionate; a €25 meter from a marketplace reads anything as formaldehyde. Reviews of popular consumer meters (e.g. Temtop M10, ~$115) complain that readings rise on alcohol and other gases — cross-sensitivity is the electrochemical sensor's known weakness, and cheap devices don't compensate.

- **Who pays (B2B, primary):** the furniture or flooring retailer who wants to say "take this home for a week, see for yourself" — it's a sales tool and a complaint deflector. Real-estate agents and property managers at hand-over of a renovated flat (NL/DE: 'opleveringsrapport', 'Übergabeprotokoll'). Rental platforms for tools.
- **Who uses:** the household, for 3–7 days, then returns it.
- **Who pays (B2C):** parents, chemically sensitive people, new-build buyers; they find you via "Formaldehyd neue Möbel messen".

### Market size (estimates — check)

- **TAM (devices):** EU furniture/flooring stores ≈ 60k; real-estate and property-management offices ≈ 150k; at 3–5 loan units each → 600k–1M units → **€120–200M** theoretical; B2C: ~1M households per year renovating or moving with small children → at 5% conversion, 50k units/year (€10M) or 150k rental weeks (€4M).
- **SAM:** DE/AT/CH/NL/BE/Nordics chains and independents that already lend tools or offer "healthy living" ranges ≈ 15k stores → **€12M** devices + recalibration €2M/year.
- **SOM (3 years):** 150 stores × 5 units + 5k B2C + rental revenue → **€1.6–2M**. Year 1: 500–1,000 units.

Sources used: UBA/ex-Bundesgesundheitsamt guideline values (0.1 ppm / 0.1 mg/m³), Berliner Mieterverein and consumer-protection guidance, a commercial measurement provider's price ranges (€60–250 per room, €800–1,500 per flat), Temtop M10 listings and reviews. Store counts: estimates — verify.

### Competition (2 searches)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing / "air it out and see if the headache goes" (what consumer advisers actually say) | €0 | No number, no reassurance, no documentation at hand-over |
| Passive sampler test kits (Bio-Check and similar), lab analysed | €30–80 per test | Single point in time, days of waiting, no CO2/VOC context |
| Professional indoor-air measurement (sampler + lab) | €150–250 per room; €800–1,500 per flat | Right for disputes, disproportionate for "is my new wardrobe OK" |
| Consumer meters (Temtop M10 ~€110, many €20–60 marketplace devices) | €20–120 | Known cross-sensitivity complaints, no calibration service, no report, you own a drifting sensor |
| Smart air monitors (air-Q, uHoo, Airthings) | €200–500 | Permanent install, subscription-ish, HCHO only on the top models |
| Handheld pro meters (PCE and similar) | €300–900 | Accurate-ish, no consumer UX, nobody lends them |

**Wedge:** the only device designed to be lent — rugged, lanyard, one button, a 7-day report that names the guideline value and says "indicative", with annual recalibration built into the price — sold to the people who meet the worried customer at the till or the hand-over.

### Product & value proposition

- Handheld 130 × 55 × 25 mm, rubberised, lanyard, 2,000 mAh Li-ion, USB-C, 1.14"–1.5" display, one button. Runs 7 days on a charge at a 5-minute sample interval with a small fan pulse before each HCHO reading.
- Sensors: electrochemical HCHO (ME2-CH2O-class), BME680-class gas/VOC + T/RH, NDIR CO2 (so people also learn that the room is simply under-ventilated — most of the time that's the real finding).
- Compensation: T/RH compensation for the HCHO cell, VOC-interference flag (if VOC spikes while HCHO spikes, the report says "likely cross-sensitivity — ventilate and re-check"), sensor-age model with a replace-by date.
- Report: BLE to a phone web app → 7-day PDF with the guideline lines (0.1 ppm HCHO; CO2 1,000/2,000 ppm), room notes, and "indicative — not a laboratory measurement" on every page.
- Fleet mode for retailers: 5 units, charging dock, QR check-out, annual recalibration swap.
- **Pricing (estimates):** B2C €199; retailer fleet of 5 + dock €899 + €149/year recalibration; rental €29/week via the retailer or a tool-rental platform.

### Unit economics (estimates, EUR per unit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C3/S3 module €2.5, electrochemical HCHO cell + AFE €9–12, BME680-class €6, NDIR CO2 module €9–14, display €3, Li-ion 2,000 mAh + charger/protection €4, micro-fan €1.5, PCB + passives €3.5) | 42 | 35 |
| PCBA assembly + test (gas-bench spot check, see below) | 5.0 | 3.4 |
| Enclosure (two-shot rubberised, 2 tools ~€20k) + lanyard | 7.5 | 3.6 |
| Packaging + USB-C cable + quick card | 2.4 | 1.8 |
| Freight + duty to EU (air, Li-ion DG surcharge) | 4.5 | 2.4 |
| Certification amortised (€40k: RED/BLE + EN 18031, EMC, safety, battery) | 40.0 | 8.0 |
| **Landed cost** | **101** | **54** |
| D2C net price (€199 incl. 19% VAT → €167) less €9 fulfilment | 158 | 158 |
| **Gross margin D2C** | **€57 (36%)** | **€104 (66%)** |
| Retailer fleet net €150/unit ex VAT | €49 (33%) | €96 (64%) |
| Rental: €29/week, ~25 weeks/year utilisation → €725/year/unit before recalibration | pays back in <3 months | — |

The HCHO cell and the CO2 module are two-thirds of the BOM and both drift; the recalibration service is not an upsell, it is how the product stays honest.

### Go-to-market

**First 100 customers:** three furniture retailers (the kill question) — independent "ökologische Möbel"/natural-living stores and one regional kitchen or flooring chain — with 5 loan units each at the till for a month. Reach them via the trade press for furniture retail and a direct visit with a working prototype. In parallel: real-estate agents in one city with a hand-over kit, and 50 B2C units to parents via two German/Dutch parenting forums and a Reddit AMA on indoor air.

**Scale:** furniture and flooring chains (loan fleets as a "healthy living" marketing programme), property managers and new-build developers (hand-over kit), tool-rental platforms and DIY chains' rental counters, pharmacies with a home-health range (B2C), and online via "Formaldehyd messen" SEO. Keep the lab-measurement providers as partners: when the report shows >0.1 ppm, the PDF recommends a professional measurement.

### 12-month plan

- **Q1:** kill question (3 retailers, 15 loan units built from StickC-Plus + sensor boards), compensation algorithm v1 against a reference instrument, report PDF v1, wording reviewed by a lawyer.
- **Q2:** own PCB, rubberised housing (SLA), 50 EVT units in 10 stores and 20 households, calibration jig with a reference HCHO source, pre-compliance.
- **Q3:** DVT, certification (RED/BLE, EMC, safety, battery), pilot batch 100, fleet dock, recalibration process live.
- **Q4:** production 1,000, B2C launch, rental-platform partnership, Nordic/Benelux retailers.

**Team:** founder (retail sales, content), 1 embedded engineer (ESP-IDF, sensor front ends, BLE), part-time chemist/measurement engineer (calibration, cross-sensitivity, reference comparisons — do not skip this person), part-time web developer (report app), contract ID/ME for the housing.

**Funding to 1,000 units (estimate):** NRE €32k (PCB €5k, housing + tooling €22k, calibration bench €5k) + certification €40k + 9 months lean salaries €60k + 1,000 units at €61 landed €61k = **€193k**, less first-year sales to retailers/B2C (~€110k) → **€85k** net. Route: retailer fleet deposits, a consumer-health or indoor-air innovation grant, a €50k angel; crowdfunding for the B2C wave once the retailer data proves the report resonates.

### Top risks

- **Technical — sensor accuracy and drift.** Electrochemical HCHO cells cross-react (alcohol, some VOCs), drift with humidity and age (2–3 years). Mitigation: T/RH compensation, VOC-interference flag, replace-by date, annual recalibration, and the word "indicative" everywhere. Validate against a reference instrument from day one.
- **Legal — someone makes a health decision on your number.** Mitigation: wellness/indicative wording, no health claims, the PDF recommends a professional measurement above the guideline; lawyer-reviewed disclaimer; no "safe/unsafe" language — show the guideline line and the number.
- **Market — retailers don't want a device that might tell their customer the wardrobe emits.** Mitigation: position it as "measure before and after, learn to ventilate" and as proof for low-emission (Blauer Engel-class) ranges; target stores that already sell low-emission products.
- **Regulatory — Li-ion:** Battery Regulation (removability by 2027 for portable batteries — design a user-replaceable cell now), UN 38.3, DG shipping.
- **Supply — HCHO cells and NDIR modules come from a handful of vendors with 8–12-week lead times.** Mitigation: qualify two cells (the two boards in the catalogue use different sensors — good), buy a year of cells once the compensation model is tuned to them.

## 3. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| 甲醛传感器 (OSHWHub, ME2-CH2O) | https://www.gongbans.com/db/oshwhub-me2-ch2o.html | Open electrochemical formaldehyde sensor board — the HCHO analogue front end to learn from | schematic, pcb | OSHWHub project licence — check before commercial derivation |
| BME680气体传感器 (OSHWHub) | https://www.gongbans.com/db/oshwhub-bme680.html | Open BME680 gas/VOC + T/RH board — compensation inputs and the VOC channel | schematic, pcb | OSHWHub project licence — check |
| Seeed Grove-HCHO Sensor | https://www.gongbans.com/db/seeed-grove-hcho-sensor.html | Alternative HCHO sensor reference (second cell type) | schematic | Seeed open-hardware terms; check the wiki licence |
| M5Stack StickC-Plus (K016-P) | https://www.gongbans.com/db/m5stack-stickc-plus.html | Handheld display + battery + ESP32 for the 15 loan-unit pilot | enclosure/structure files only; electronics not published | Off-the-shelf; use as bought |

### Block diagram

```
[HCHO electrochemical cell + AFE] --ADC--> |
[BME680-class VOC/T/RH] ---------I2C-----> | [ESP32-C3/S3] --> compensation (T/RH, VOC flag, age) --> 7-day log (flash)
[NDIR CO2 module] ----------------UART---> |      |-- BLE --> phone web app --> 7-day PDF report
[micro-fan pulse] <--GPIO------------------+      |-- display (number, trend, guideline marker), 1 button
[Li-ion 2,000 mAh, USB-C charge, protection] --> 3.3 V
```

**Engineering gap:** the compensation and ageing model (this is the product); a calibration bench with a reference HCHO generator or certified instrument; a rugged, lendable housing with a fan path that doesn't clog; a replace-by-date and recalibration workflow; fleet dock/check-out for retailers; and the report wording.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| Electrochemical HCHO cell (ME2-CH2O / ZE08-class or equivalent) | €8–11 | 2–3 vendors; 8–12 wk lead; shelf life — buy to plan |
| Low-noise AFE (TIA op-amp, ADC) | €1.5 | Multi-source |
| BME680 / BME688 | €6 | Single vendor (Bosch); widely stocked |
| NDIR CO2 module (SCD4x-class photoacoustic or small NDIR) | €9–14 | 2–3 vendors |
| ESP32-C3-MINI or S3 module | €2.5 | Multi-source |
| 1.14"–1.5" IPS display | €3 | |
| Li-ion 2,000 mAh pouch/18650 with protection, user-replaceable | €3.5 | Battery Regulation: design for replacement |
| Micro-fan 20 mm | €1.5 | |
| Two-shot housing + lanyard | €3.6 at 5k | Tooling €20k |

### Firmware/software starting point

- ESP-IDF; Bosch BSEC library for BME680/688 (closed binary, free licence for products — read the terms) or the open BME680 driver for raw values.
- Sensirion's embedded drivers for SCD4x on GitHub if you pick that CO2 module.
- Web Bluetooth-based phone app (no app-store dependency) for the report; any server-side PDF library.
- For the HCHO front end, the open OSHWHub board's schematic is your reference; the compensation model you write yourself with your measurement engineer.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | 3 furniture retailers agree to put 5 loan units at the till for a month; 15 units built from StickC-Plus + sensor boards; first 10 households borrow one. Fewer than 3 stores or <40% of offered units borrowed: stop or move to the real-estate channel. |
| 3–5 | Works-like | Compensation v1: within ±30% of a reference instrument between 0.03 and 0.3 ppm at 40–70% RH; VOC-interference flag works with an alcohol test; 7-day log + PDF v1; 20 borrower reports collected with a 5-question survey. |
| 6–8 | Looks-like + EVT | Own PCB v1, SLA rubberised housing with fan path, 50 units in 10 stores; battery life ≥7 days verified; EMC pre-scan. |
| 9–10 | DVT + pre-compliance | PCB v2, tooled-part samples, RED/EMC/safety pre-test, UN 38.3 for the cell, EN 18031 checklist, lawyer-approved report wording. |
| 11–12 | Pilot batch | 100 units from a CM with gas-bench spot checks (10%), golden sample, fleet dock prototype, recalibration SOP, first retailer invoices. |

### Certification checklist (EU)

- **CE / RED:** BLE → EN 300 328, EN 301 489-1/-17, EN 62311; safety EN 62368-1 (Li-ion, charging).
- **RED delegated act — EN 18031-1 and -2:** applies (BLE + internet via the phone app; -2 because the report contains room/location notes that may be personal data). Keep data on the device and in the user's phone; no account required.
- **CRA:** reporting since September 2026, full December 2027; signed firmware, SBOM, disclosure.
- **Battery Regulation (2023/1542) + UN 38.3:** Li-ion → labelling, removability/replaceability design, DG shipping; register as battery producer where required.
- **RoHS, REACH, WEEE**, packaging registration.
- **GDPR:** report data stays on the phone; if you add cloud storage, DPIA-lite and consent.
- **Not a measuring instrument under MID; not a medical device** — keep claims to "indicative indoor-air information"; no health or diagnosis language, otherwise MDR territory.
- **Estimated test costs:** RED/BLE €8–10k, EMC €4k, safety with battery €5k, UN 38.3 (if a custom pack) €3k, EN 18031-1/-2 €15–18k, documentation €2k. Budget **€40k**.

### Validation toolkit

- **Kill question:** will 3 furniture retailers put 5 loan units each at the till for a month, and do customers actually borrow them? **Cheapest experiment:** 15 units from StickC-Plus + the two sensor boards in a printed shell (~€60 each), a laminated till card, a paper check-out sheet. Cost ≈ €1,000 and 3 store visits.
- **5-question interview (store manager):** 1) How often does a customer ask about smell, emissions or "is this safe for the nursery"? 2) What do you say today, and does it close or lose the sale? 3) Do you lend anything today (tools, samples)? How does it come back? 4) If a borrowed meter showed a high value in a customer's home, what would you want the device to say? 5) Would you pay €899 for a 5-unit fleet with yearly recalibration — who decides?
- **Landing page:** headline "New furniture, new floor, new flat? Know what you're breathing — in a week." Bullets: "Formaldehyde, VOC and CO2 logged for 7 days, with the official guideline value on the chart"; "Borrow it at your furniture store or rent it for €29 — return it when you're done"; "Indicative, honest, recalibrated every year".
- **Pass threshold:** 3 stores × 5 units placed; ≥60% of units borrowed at least once in the month; 10 B2C pre-orders at €199 from the first 50 reports shared.

### First production checklist

- Samples: 15 pilot (dev-kit based), 50 EVT, 100 pilot; keep two per revision with gas-bench records.
- Golden sample: gas-bench response at two HCHO concentrations, CO2 at 400/1,000 ppm, 7-day battery log, signed.
- DFM review: fan path and membrane, cell seating and venting, battery door (replaceable), rubber over-mould adhesion, lanyard anchor strength.
- MOQ talk: HCHO cells 1k (check shelf life!), CO2 modules 500–1k, PCBA 500, tooling at 1k shots.
- QC/AQL: level II, AQL 1.0/2.5; 100% functional + BLE; 10% gas-bench spot check; 100% charging test.
- Packaging: battery labelling, UN 38.3 summary, DG-compliant outer carton.
- Incoterms: FOB Shenzhen with a DG-capable forwarder; or ship cells separately and insert in the EU.

## 4. Next steps (this week)

1. Order 3 StickC-Plus, 3 of each HCHO sensor board, 3 BME680 boards and a CO2 module; build one logger and put it next to a new piece of flat-pack furniture with the door closed for 48 hours.
2. Visit two furniture stores with a "healthy living" range and ask the five questions; ask for a one-month loan-unit trial.
3. Find a reference instrument you can borrow or rent (a university lab or a measurement provider) and schedule a comparison day; write the compensation-model plan with a measurement engineer.

Want help sourcing or building this? Talk to us via www.gongbans.com.
