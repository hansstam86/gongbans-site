# Balance Kit — Founder Start Pack

> Eight clip-on flow/return pipe-temperature nodes plus a tablet app that shows every radiator's spread live, so an installer does a hydraulic balance in one visit instead of three.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Hydraulic balancing (hydraulischer Abgleich) is a legal and subsidy requirement in Germany, but the measurement step is done with two clamp thermometers, a notepad and three visits. Labour is 80% of the €650–1,250 the customer pays.
- **Customer:** German heating installers (SHK-Betriebe, ~48,000 firms) and energy consultants; heat-pump installers in DE/AT/NL/UK who must prove the Spreizung (flow–return delta) on every install. The firm owner pays; the fitter uses it.
- **Product:** 8 battery BLE nodes with spring clamps for 10–22 mm pipe, a charging case, and an Android/iPad app that walks the installer through the procedure and spits out the PDF the subsidy office wants. €699 per kit to trade, or €99/month rental.
- **Why now:** GEG §60c makes balancing mandatory for many larger existing buildings by 30 Sept 2027 and a condition for BEG subsidies and every heat-pump install; EU heat-pump sales were ~2.6–2.9 M units in 2025 and every one needs a commissioning check.
- **The ask:** ~€95k to get to 1,000 kits (first 50 pilot kits ~€25k). Bootstrap plus paid pilots; grant money (German ZIM/EXIST-type programmes) fits because this is energy-efficiency tooling.

## 2. Business plan

### Problem & customer
The balancing job has two halves: the calculation (Verfahren A or B — software from valve makers does this fine) and the measurement/verification: is every radiator actually getting its design flow? Today the fitter clamps a thermometer on flow and return, reads a delta, moves to the next radiator, comes back the next day when the system has settled. Nobody can see eight radiators at once. A wireless sensor set that shows all spreads simultaneously, logs for an hour, and produces the report turns a 3-visit job into a 1-visit job. On a €650 service that saves maybe €200 of labour per house. The kit pays back in 4 jobs.

Who pays: the owner of a 5–30 person installer firm (Meister), who already spends €2–5k a year on Testo/Wöhler instruments. Who uses: the fitter and the apprentice. Secondary customer: independent energy consultants (Energieberater) who certify the balancing for subsidy files but don't own the valves.

### Market size (estimates — check them)
- **TAM:** ~48,000 SHK firms in Germany (ZVSHK, 2024/25) plus roughly the same again across AT/CH/NL/UK/FR heating trades → ~100,000 firms. At one kit per firm at €699 → **~€70 M** one-off, plus consumables/rental.
- **SAM:** Firms that actively do heat-pump installs and GEG balancing — call it 25% of German firms (~12,000) plus 8,000 abroad = 20,000 firms → **~€14 M**.
- **SOM (3 years):** 5% of SAM = 1,000 kits ≈ **€0.7 M** revenue, plus rental and a second kit for bigger firms. Small but very profitable for a 3-person company, and a stepping stone to a heat-pump commissioning tool.

Sources: ZVSHK Bilanz 2025 (48,050 firms), co2online cost figures (€650 service / €925 with valves), EHPA 2025 sales (2.63 M in 16 countries).

### Competition (3 searches)
| Alternative | What it is | Price (est.) | Weakness |
|---|---|---|---|
| Two clamp thermometers + notebook ("do nothing") | Status quo | €0 extra | 2–3 visits, no report |
| Testo 115i Smart Probes | BLE clamp thermometer, phone app | ~€75–100 each | 1–2 points at a time, app not built for balancing, no PDF for the subsidy file |
| Afriso CAPBs valve-balancing set | Differential pressure/flow at the valve | several hundred € | Measures flow at the valve, needs presettable valves; one point at a time |
| myWarm (868 MHz sensors + server + actuators) | Full-service balancing system, installer must be trained partner | not public | Closed ecosystem, service-based, not a tool you own |
| Valve-maker software (Danfoss and others) | Calculation only (Verfahren B) | free | No measurement; this is the complement, not the competitor |

**Wedge:** eight points at once, built for the balancing workflow, and the PDF output. Nobody sells "the measurement half" as a product for the fitter's toolbox.

### Product & value proposition
- 8 nodes, each: ESP32-S3 (from the open Stamp-S3Bat design), contact NTC in a spring clamp with an IR option, 500 mAh Li-ion, magnet, LED. 8-hour runtime, charged in the case.
- Case: 8 bays, USB-C PD input, foam insert, fits in a Systainer-style box.
- App: pairs the 8 nodes, labels them per radiator (photo), shows live spreads, 60-minute logging, Verfahren A/B checklist, exports PDF (German first, then NL/EN).
- Pricing: **€699 ex-VAT per kit to trade (direct)**, €899 list via wholesalers; **€99/month rental** with 6-month minimum for firms that only need it for the 2027 rush. Consumable: replacement clamps €15.

### Unit economics (estimates, per 8-node kit)
| Item | 1,000 kits | 5,000 kits |
|---|---|---|
| Electronics BOM (8 nodes) | €112 (€14/node) | €88 (€11/node) |
| Case electronics + cells | €30 | €24 |
| Assembly & test | €28 | €18 |
| Enclosure (8 clamp housings + case) | €38 | €26 |
| Packaging, manual, labels | €8 | €5 |
| Freight + duty to EU (air at 1k, sea at 5k) | €18 | €9 |
| Certification amortised (€25k RED/EMC/UN38.3) | €25 | €5 |
| **Landed cost** | **€259** | **€175** |
| Sell price (direct, ex-VAT) | €699 | €699 |
| Channel margin (wholesaler 30% on €899 list → net €629) | — | €629 net |
| **Gross margin direct** | **63%** | **75%** |
| **Gross margin via wholesaler** | 59% | 72% |

Rental case: €99/month × 12 months = €1,188 per kit per year on a €259 asset. Fine if you can collect.

### Go-to-market
**First 100 customers:** local SHK-Innung (trade guild) meetings — bring a radiator and a demo; the Haustechnikdialog forum; heat-pump manufacturer installer-training days (they want installers to pass commissioning); 2–3 regional SHK wholesalers (Großhandel) as a stocked item; energy-consultant associations; a YouTube demo in German showing one house in one visit. Paid pilot: €299 deposit, keep the kit at €699.

**Scale:** wholesaler listings (the installer buys where he buys pipe), bundling with a valve maker's software, rental via tool-rental counters at wholesalers, then NL/AT/UK with localised PDF.

### 12-month plan
- **Q1:** 10 installer interviews, 4-node breadboard on a real system, accuracy test (contact NTC vs IR vs Testo reference). Gate: ±0.5 °C on bare pipe and 4/10 installers say yes to €699.
- **Q2:** 20 works-like kits, app alpha, 5 paid pilots at €299 deposit, start RED/EMC pre-compliance.
- **Q3:** Looks-like clamp housing and case tooling (soft tool), 50-unit pilot batch, certification, first wholesaler meeting.
- **Q4:** 300–1,000 kits, PDF validated with two subsidy consultants, rental programme launch.

**Team:** hardware/firmware lead (full-time), app developer (full-time or strong contractor), a part-time ex-installer who sells and writes the procedure, part-time ops/sourcing.

**Funding to 1,000 kits (estimate):** NRE €60k (ID + tooling €25k, cert €25k, test fixtures €10k) + working capital for 1,000 kits × €259 = €259k, of which 60% pre-funded by trade pre-orders and wholesaler POs → cash need ≈ €60k + €105k ≈ **€165k**; with staged batches of 300 the peak cash need is closer to **€95k**. Route: bootstrap + paid pilots + an energy-efficiency grant; an angel only if you want to go to five countries at once.

### Top risks
- **Technical — thermal coupling:** shiny copper and painted steel read differently; you need ±0.5 °C to see a 5 K spread. Mitigation: contact NTC with spring force and a thermal pad; IR as the "quick look" only; calibrate every node against a bath at end-of-line.
- **Market — conservative trade:** installers buy what the wholesaler stocks. Mitigation: wholesaler route from month 6; rental lowers the risk for them.
- **Regulatory:** RED for BLE, Li-ion cells → UN 38.3 and Battery Regulation labels, CRA because there is an app. Not a MID instrument (no billing). Mitigation: use a pre-certified module for v1 to lean on the module's RED file; cells from a supplier with UN 38.3 reports.
- **Supply:** NTC clamps and springs are commodity; the risk is the case and foam, which are tooled parts. Mitigation: start with an off-the-shelf tool case + CNC foam.

## 3. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [m5stack-stamp-s3bat](https://www.gongbans.com/db/m5stack-stamp-s3bat.html) | ESP32-S3 + battery path; the per-node core. Altium sources published | pcb, schematic | M5Stack hardware repo — check the repo licence before copying the layout |
| [m5stack-unit-ncir2](https://www.gongbans.com/db/m5stack-unit-ncir2.html) | Non-contact IR temperature for the quick-look mode | enclosure/structure only | Module, electronics not published; buy it for prototypes |
| [seeed-grove-digital-infrared-temperature-sensor](https://www.gongbans.com/db/seeed-grove-digital-infrared-temperature-sensor.html) | IR temperature reference circuit if you integrate IR on your own PCB | schematic | Seeed wiki resources — check licence |
| [m5stack-unit-kmeter-iso](https://www.gongbans.com/db/m5stack-unit-kmeter-iso.html) | Isolated thermocouple input for a "pro probe" variant on hot pipes | enclosure/structure only | Module only |

### Block diagram and engineering gap
```
[NTC clamp]--+                      [Charging case: USB-C PD -> 8x charger -> LEDs]
[IR sensor]--+--> ESP32-S3 (Stamp-S3Bat derived) --BLE--> Tablet app --> PDF
[Li-ion 500mAh + charger + fuel gauge]                      |
[Magnet, LED, 1 button]                                     +--> cloud optional (CRA scope)
```
Gap: sensor-to-pipe coupling and calibration (±0.5 °C), 8-node BLE sync on consumer tablets, the clamp mechanics for 10–22 mm, and the app/PDF — which is half the work.

### Starter BOM (per node, estimates)
| Part | Est. cost | Note |
|---|---|---|
| ESP32-S3 module (certified) | €2.80 | Multi-source; module with RED file saves cert money |
| NTC 10k 1% glass bead with clamp spring | €1.20 | Commodity |
| IR temp sensor (optional) | €3.50 | Sole-ish source, 8–12 week lead; drop if contact NTC wins |
| Li-ion 500 mAh with UN38.3 | €1.60 | Insist on the test report |
| Charger + fuel gauge + LDO | €1.10 | — |
| PCB 4-layer + assembly | €2.50 | — |
| Clamp housing (2 shots + spring + pad) | €2.80 | Tooled part, 6–8 weeks |
| Misc (magnet, button, LED, label) | €0.60 | — |
| **Node total** | **~€16** | at 1k volume, 8 nodes ≈ €128 incl. IR |

### Firmware/software starting point
- ESP-IDF or Arduino-ESP32 with NimBLE for the node; ESPHome if you want to prototype fast (it exists and supports NTC and BLE).
- App: Flutter with flutter_blue_plus (exists) for Android + iPad; PDF via a standard PDF library. For Verfahren A/B worksheets, copy the public spreadsheets the VdZ/subsidy programmes publish — search for the current form.

### 12-week build plan
- **Week 1–2 — validate.** Buy 4 Stamp-S3Bat, 4 NCIR2, 4 NTC clamps; build 4 nodes on a laptop dashboard; test on a real radiator loop against a Testo reference. In parallel: 10 installer calls. *Exit:* ±0.5 °C on bare pipe, ≥4/10 want it at €699 or sign a pilot.
- **Week 3–5 — works-like.** Own node PCB (copy the Stamp power path), 8 nodes, app alpha with live spreads. *Exit:* 8 nodes streaming for 60 minutes on one tablet.
- **Week 6–8 — looks-like + EVT.** Clamp housing 3D-printed in 3 sizes, charging case from an off-the-shelf tool case, app PDF export. 5 kits to 5 pilot installers. *Exit:* an installer finishes a house in one visit without you present.
- **Week 9–10 — DVT + pre-compliance.** Design freeze, pre-scan EMC, battery drop/charge tests, calibration fixture. *Exit:* pre-scan passes, calibration <3 minutes per kit.
- **Week 11–12 — pilot batch.** 20–50 kits, golden sample, wholesaler demo. *Exit:* 20 paid kits in the field, <5% returns.

### Certification checklist (EU)
- **CE under RED** (BLE): EN 300 328 radio, EN 301 489-1/-17 EMC, EN 62368-1 safety; ~€8–15k if your module already has a RED file and you only test the host.
- **RoHS, WEEE registration** (per country, e.g. stiftung ear in DE), **REACH** SVHC declaration from suppliers.
- **RED delegated act / EN 18031** cybersecurity: applies because the kit connects to the internet via the app — plan €5–10k and design secure boot/updates from day 1. **CRA** obligations phase in from 2026 (reporting) with full application in Dec 2027 — have an SBOM and an update plan.
- **Battery Regulation** (EU 2023/1542): labels, removability information, due diligence later; **UN 38.3** for the cells and pack, plus transport docs.
- **Not** a measuring instrument under MID (no billing). No GDPR issues beyond the installer's customer address on the PDF — keep data on the tablet.
- Estimated total test cost: **€20–30k**.

### Validation toolkit
- **Kill question:** will 4 out of 10 installers say "yes, €699" without being pushed? **Cheapest experiment:** €500 — 4 breadboard nodes and ten 20-minute calls via the local Innung.
- **5-question interview:** (1) How do you measure spreads today and how many visits does a balancing job take? (2) What do you charge and what's the labour share? (3) What tool would you buy tomorrow if it cut one visit? (4) Would €699 or €99/month be easier to say yes to — and who in the firm decides? (5) What does the subsidy consultant ask you for that you hate producing?
- **Landing-page headline:** "Hydraulischer Abgleich in einem Termin." Bullets: 8 Funk-Fühler, alle Heizkörper gleichzeitig · Protokoll-PDF für BAFA/KfW in 1 Klick · Rechnet sich nach 4 Aufträgen.
- **Pre-order target that counts as a pass:** 20 paid €299 deposits from installer firms (not hobbyists) within 4 weeks.

### First production checklist
Samples (3 rounds), golden sample signed with the EMS, DFM review on the clamp housing (undercuts, spring insertion), MOQ talk (ask for 300 with a 1,000 forecast), QC/AQL (Level II, 0/1.0/2.5), calibration record per kit, packaging drop test, incoterms FOB Shenzhen for air at 1k then FCA/sea at 5k, EU importer of record named on the label.

## 4. Next steps (this week)
1. Order 4× Stamp-S3Bat, 4× NCIR2, 4 NTC clamp probes and a reference clamp thermometer; book a friendly installer's boiler room for a Saturday.
2. Call the local SHK-Innung and get 10 twenty-minute installer calls in the diary.
3. Download the current Verfahren A/B subsidy forms and draft the PDF the app must produce — before writing any app code.

Want help sourcing or building this? Talk to us via www.gongbans.com.
