# Switchboard Hot-Spot Watch — Founder Start Pack

> A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** About a quarter of building fires have an electrical origin (European Fire Academy estimate as cited by [Schneider Electric](https://www.electrical-installation.org/enwiki/State-of-the-art_solutions_for_electrical_fire_prevention,_beyond_the_standards)); the standard defence is one thermographic inspection a year by a person with a handheld camera. Loose terminals heat up in weeks, not years. Continuous thermal monitoring exists — for switchgear rooms, at switchgear prices.
- **Customer:** Facility managers and electrical contractors maintaining commercial and multi-tenant residential distribution boards in the EU; property owners and insurers who pay for the risk. The owner/FM pays; the electrician installs; the insurer asks for the report.
- **Product:** A €349 DIN-clip thermal watcher: a 32×24 thermal array looking across the board's breakers and busbars, per-zone baselines and ΔT alarms, powered from the board's auxiliary 24 V or a small supply, LoRaWAN or WiFi uplink, a monthly thermal report PDF for the insurer. Installed by the electrician in 15 minutes.
- **Why now:** Low-resolution thermal arrays (MLX90640-class) are cheap and good enough to see a breaker 15 K above its neighbours; an open thermal + visual camera design exists; LoRaWAN is standard in commercial buildings; insurers are actively pushing electrical fire prevention.
- **The ask:** ~€120k (estimate) to the first 1,000 units; route = paid contractor pilots + bootstrap; an insurer discount or endorsement as the scaling lever.

## 2. Business plan

### Problem & customer
A commercial building has 5–50 distribution boards. Each has 20–100 terminals that can loosen (thermal cycling, vibration, bad torque on install). The failure mode is slow heating → insulation damage → arc → fire. Today: annual (or less frequent) thermography by a contractor, €150–400 per board, a PDF nobody reads, and nothing in between. Continuous monitoring exists from the big switchgear vendors for MV/LV switchgear — wireless sensors on busbars, integrated into their systems, quoted per project and priced accordingly.

Who pays vs who uses: the building owner/facility manager pays; the electrical contractor installs and monitors (and would like a recurring service); the insurer requests, discounts or requires. Secondary: data centres' small rooms, hotels, schools, hospitals' technical services, farms with large boards (fire risk in barns), EV-charging hubs' distribution boards.

### Market size (estimates)
- EU commercial/public/multi-tenant buildings: ~15 M (estimate); average 6 boards worth monitoring → **90 M boards**; realistic candidates (boards above ~100 A, or in buildings with insurer pressure) → 15% → **13.5 M boards**.
- **TAM:** 13.5 M × €349 ≈ **€4.7 B** hardware (ceiling) + reports.
- **SAM:** boards maintained by contractors in DE/NL/UK/Nordics/FR who already sell thermography → ~2 M → **€700 M**.
- **SOM (3 years):** 0.3% → 6,000 boards → **€2.1 M** + a report service (€3/board/month → €200k/year at 6k boards).

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Annual handheld thermography by a contractor ("do nothing more") | The standard; required by some insurers | Once a year; faults develop in weeks; costs €150–400 per board per visit |
| Switchgear-vendor continuous thermal monitoring (wireless busbar sensors + their software; vendor claims 2.5× cost-effectiveness vs IR over 20 years — [Schneider white paper](https://download.schneider-electric.com/doc/998-2132737_GMA/998-2132737_HeatTag_GMA_eWhitePaper(1).pdf)) | Credible, integrated | Project-priced for MV/LV switchgear; not for 200 small boards in an office block |
| Thermal "gas/particle" sensors that sniff overheating insulation (HeatTag-class) | Clever, early warning | Vendor-locked, price, per-cabinet |
| IR-window thermography sensors / DIN-rail thermography sensors ([InfraSensing](https://infrasensing.com/sensors/sensor_thermography_din.asp)) | Closest to us; IT-room oriented | Needs their base unit and software; not LoRaWAN; price per point |
| Fixed-point temperature sensors on terminals | Cheap | One terminal each; installation labour; miss the one you didn't instrument |
| DIY MLX90640 + ESP32 | Makers | No baselines, no DIN mount, no report, no installation rules |

**Wedge:** one array sees the whole board (not one terminal), DIN-clip install in 15 minutes by the electrician who already services the board, LoRaWAN/WiFi to the FM's existing network, per-zone learning baselines, and a monthly PDF the insurer accepts — at a price that makes sense for a €200 office board.

### Product & value proposition
Hardware: DIN-rail clip or magnetic/adhesive mount on the board's enclosure facing the breakers (field of view 55°/110° variants), MLX90640-class 32×24 thermal array, a low-res visual camera optional (for the zone map — can be disabled for privacy, though inside a board there's nothing personal), ambient T/RH, ESP32-C6-class MCU with LoRa (from the Stamp C6LoRa reference) or WiFi, powered from 24 V aux (common in larger boards) or a DIN-rail 230 V → 5 V supply (bought-in certified, installed by the electrician), optional battery/supercap for a "lost power" alert. Firmware: zone map set up on a phone at install (draw boxes over the thermal image), baseline learning per zone vs ambient and vs load (if a meter is available over Modbus later), ΔT and absolute alarms, daily max per zone, LoRaWAN uplink (zone maxima only — tiny payload), monthly PDF per building, alarm by email/SMS/webhook via the FM's platform or ours.

Pricing (estimates): **€349 per unit**, €399 wide-angle, installer 10-pack €2,990; report service €3/board/month or €30/year (optional; the device works stand-alone with WiFi/MQTT). Contractors at 30% off; they resell with installation.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (thermal array €28, ESP32-C6 + LoRa €6, optional VGA camera €3, T/RH €1.5, power + protection €4, PCB €4) | €46.50 | €38.00 |
| Assembly & test (SMT, thermal calibration against a black-body reference, RF test) | €7.00 | €5.00 |
| Enclosure (flame-retardant V-0 ABS/PC, DIN clip, lens window; tooling amortised) | €7.50 | €4.80 |
| Packaging (box, clip, zone-map card) | €2.50 | €1.80 |
| Freight + duty to EU | €3.00 | €1.80 |
| Certification amortised (~€35k: RED, EMC incl. installation environment, safety, EN 18031) | €35.00 | €7.00 |
| **Landed cost** | **€101.50** | **€58.40** |
| Sell price (direct €349 / contractor €245) | €349 | €245 |
| **Gross margin** | **€247.50 (71%)** | **€186.60 (76% at contractor price)** |

The thermal array is the BOM — one vendor family dominates; negotiate at 5k, and qualify an alternative array even if it's worse.

### Go-to-market
**First 100 customers:** 5 electrical contractors install a paid pilot in 10 boards each (kill question) — found via electrical-contractor associations and the firms that already sell thermography; 1 insurer's loss-prevention engineer (they exist at every commercial insurer) who agrees to review the monthly PDF; 2 facility-management companies with mixed portfolios; a case study where a loose terminal was found.

**Scale channels:** electrical wholesalers (the contractor buys everything there), contractor associations' member offers, insurer loss-prevention programmes (discount or mandate), FM platforms (integration), switchboard builders (factory-fit option), EV-charging hub installers.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from Unit Thermal2 + Stamp C6LoRa in a DIN box; 50 boards in paid pilots across 5 contractors; first caught hot spot. |
| Q2 | Own PCB + V-0 enclosure, zone-map app, baselines; EVT 50; EMC in a live board; insurer PDF v1. |
| Q3 | DVT, certification, 300-unit pilot; wholesaler listing; report service live. |
| Q4 | 1,000 units; insurer programme; wide-angle SKU; Modbus load correlation. |

**Team:** 1 embedded engineer (thermal processing, LoRa, power — full-time), 1 software developer (zone-map app, backend, PDF — full-time), founder for contractors and insurers; a licensed electrician/consultant on contract for installation rules and EN 61439 guidance. Three people.

**Funding to first 1,000 units (estimates):** NRE €55k (PCB €10k, V-0 tooling €16k, app + backend €22k, electrician guidance €7k) + certification €35k + 1,000 units landed ~€75k + 9 months overhead €75k ≈ **€240k**; minus pilot fees (5 contractors × €2,500 ≈ €12.5k), pilot-batch sales (300 × €299 ≈ €90k), wholesaler/contractor prepayments (~€20k) ≈ **~€120k**. Bootstrap + paid pilots; building-safety/insurtech angels are a real option here; a loss-prevention grant from an insurer association is worth a try.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** emissivity, reflections and field of view — a shiny busbar reads cold, a plastic breaker reads right | Zone baselines (relative, not absolute), ΔT vs neighbours and vs ambient, install guide for placement; publish detection tests on a test board with a deliberately loose terminal |
| **Technical:** load-dependent heating looks like a fault | Learn daily patterns; optional Modbus/CT load correlation; alarm on deviation from baseline at similar load |
| **Regulatory/installation:** anything inside a board is the electrician's domain (EN 61439 assembly rules, national wiring rules) | Device is a monitoring accessory mounted on the enclosure, SELV-powered via a certified DIN supply; installed by a licensed electrician; written guidance reviewed by a consultant; never touch the busbars |
| **EMC:** a radio inside a metal board with contactors | External antenna option through a gland; EMC testing in a representative board; LoRa penetrates better than WiFi — lead with LoRaWAN |
| **Market:** "the insurer doesn't require it" | Start with contractors who sell thermography anyway (they add recurring revenue); bring the insurer the PDF and a caught fault |
| **Liability:** "your sensor didn't see the fire" | Position: early warning aid, not a fire-detection system (not EN 54); wording and insurance |
| **Supply:** thermal array sole-source family | Qualify a second array; buy ahead |
| **Licence:** the open thermal camera is OSHWHub | Read the licence; your own board — the Melexis driver and fusion approach are the learning |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| YuzukiIRC low-cost thermal + visual fusion camera (OSHWHub) | https://www.gongbans.com/db/oshwhub-yuzuki-infrared-camera.html | Open MLX90640 + OV9732 fusion camera on a V831 — the thermal/visual zone-map idea, proven | schematic, pcb | **OSHWHub — licence varies; read it** |
| M5Stack Unit Thermal2 (U149) | https://www.gongbans.com/db/m5stack-unit-thermal2.html | Thermal-array unit for the works-like | enclosure/structure only; electronics not published | Buy; array vendor's datasheet for production |
| M5Stack Hat Thermal (U062) | https://www.gongbans.com/db/m5stack-hat-thermal.html | Alternative thermal-array form factor | enclosure/structure only; electronics not published | Buy; prototype only |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | Open ESP32-C6 + LoRa core — the uplink | pcb, schematic (Altium) | M5Stack hardware repo — check licence terms |

### Block diagram
```
[MLX90640-class 32x24 thermal array, 55/110 deg lens] --I2C--> [ESP32-C6: zone maxima, baselines, dT alarms]
[optional low-res visual camera for the zone map]  --------->        |          |
[ambient T/RH]                                                        |          |
                                              [LoRaWAN EU868 (from C6LoRa ref) or WiFi]   [BLE: phone app at install]
                                                                      |
[24 V aux or certified DIN 230->5 V supply] -> [protected 5 V/3.3 V]  [supercap: "power lost" uplink]
                                                                      |
                                   [backend: alarms -> email/SMS/webhook; monthly PDF per building]
```
**Engineering gap:** the zone-map install flow, baseline learning that doesn't false-alarm on load cycles, placement/field-of-view rules per board type, V-0 enclosure and DIN clip, EMC inside a board, the insurer-grade PDF. The sensor and radio are solved.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| MLX90640-class thermal array (32×24, 55° or 110°) | €28.00 | **Dominant vendor; long lead (12–20 weeks); qualify an alternative** |
| ESP32-C6 module + LoRa transceiver (SX1262-class) + antenna | €6.50 | Pre-certified module; follow the C6LoRa reference |
| Low-res camera (optional SKU) | €3.00 | Can be omitted; zone map from thermal only |
| T/RH sensor | €1.50 | |
| Power: 24 V input + protection, or certified DIN 230 V → 5 V supply (bought-in) | €4.00 (+€8 DIN PSU) | **Never design the mains part yourself** |
| Supercap for power-loss uplink | €1.00 | |
| PCB 4-layer + passives + USB-C service port | €4.00 | |
| V-0 PC/ABS enclosure + DIN clip + IR-transparent window | €7.50 | **Tooling €12–16k**; window material must pass IR |

### Firmware/software starting point
- Melexis publishes an MLX90640 driver library on GitHub (exists); Adafruit's MLX90640 library (exists) for the works-like.
- LoRaWAN: Semtech's **LoRaMac-node** (exists) or an ESP-IDF LoRaWAN stack; network via **The Things Stack** or **ChirpStack** (both exist); payload = zone maxima + ambient, every 10 min.
- Baselines/alarms: your own; keep it on-device so a stand-alone WiFi/MQTT mode works.
- Zone-map app: a BLE-connected phone web app (Web Bluetooth) or a small native app; PDF from the backend.
- Reference for the fusion approach: the YuzukiIRC project page (MaixPy3-based) — read, don't copy.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 10 works-like units (Unit Thermal2 + Stamp C6LoRa in a DIN box) on a test board with a deliberately loose terminal: detects +15 K at 1 m; **5 electrical contractors sign a paid pilot (10 boards each, €500) and 1 insurer agrees to review the PDF** (runs to W8) |
| 3–5 | Works-like | 50 boards live; zone maxima uplinked every 10 min; baseline learning running; ≤ 1 false alarm per board per week after 7 days |
| 6–8 | Looks-like + EVT | Own PCB + V-0 enclosure T1 + DIN clip; 50 units; zone-map app; EMC pre-scan inside a live board with contactors; first PDF to the insurer |
| 9–10 | DVT + pre-compliance | RED/EMC/safety pre-compliance; EN 18031 self-assessment; installation guidance reviewed by the electrician consultant; 60-day false-alarm statistics |
| 11–12 | Pilot batch | 50 units to new contractors; ≥ 1 genuine hot spot caught and fixed; insurer gives a written view on a discount or endorsement |

### Certification checklist (EU)
- **CE under RED** (LoRa 868 MHz and/or WiFi/BLE): EN 300 220 (LoRa), EN 300 328 (2.4 GHz), EN 301 489-1/-3/-17, EN 62311; **EN IEC 62368-1** (SELV device; the DIN supply is a certified bought-in part); EMC for the installation environment (industrial levels — EN IEC 61000-6-2/-4 — are the sensible choice inside a board); **EN 18031-1** (internet-connected, mandatory since 1 Aug 2025), -2 not needed if no personal data (don't store the visual image in the cloud). Est. €8–12k RED/EMC, €4–6k safety, €12–18k EN 18031.
- **Installation:** EN 61439 is for the assembly builder; your device is an accessory — provide instructions compliant with national wiring rules, installed by a licensed electrician; a consultant signs the guide.
- **Not a fire-detection product (EN 54), not safety-related control** — say so.
- **RoHS, REACH, WEEE**, packaging. **Battery:** none (supercap) — keep it so.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware, FOTA, SBOM, vulnerability contact; a building-safety device gets scrutiny.
- **GDPR:** the optional camera looks inside a closed board — no people; document that it's disabled by default and never streams.
- **Total certification budget estimate: €25–38k.**

### Validation toolkit
- **Kill question:** Do 5 electrical contractors install a paid pilot in 10 boards each, and does one insurer offer a premium discount (or written endorsement) for it?
- **Cheapest experiment (~€1,500):** 10 works-like units, a test board with a loose terminal under load (video the thermal image heating), a one-page pilot offer at €500 per contractor, a draft monthly PDF to show the insurer's loss-prevention engineer.
- **5-question interview (electrical contractor / FM):** 1) How often are your boards thermographed, by whom, at what price? 2) What did the last report find, and what happened next? 3) Who asks for it — owner, insurer, nobody? 4) If a sensor in each board emailed you when a zone ran hot, what would you do with that, and would you sell it as a service? 5) €349 per board plus 15 minutes of your time — pilot 10 boards for €500?
- **Landing page:** headline "See every breaker's temperature. Every day. Not once a year." Bullets: "A thermal array on a DIN clip watches the whole board; alarms on a zone running hot vs its neighbours." / "LoRaWAN or WiFi; installed by your electrician in 15 minutes; no busbar contact." / "€349 per board; a monthly thermal report your insurer can read."
- **Pass threshold:** 5 paid pilots signed and one insurer in the loop, or 100 units pre-ordered by contractors in 8 weeks.

### First production checklist
- Samples: 5 golden samples with thermal calibration against a black-body at 2 temperatures, RF test, false-alarm log.
- DFM: IR window material and seal, lens alignment, DIN-clip retention on 35 mm rail, antenna placement/gland, V-0 material certificate.
- MOQ talk: thermal arrays 1k (long lead — order at EVT), modules reel, DIN supplies 500 from a certified vendor, enclosures 1k.
- QC: AQL II 2.5/4.0; 100% thermal image test against a heated target + RF join test; 2% 48 h soak at 50 °C.
- Packaging: zone-map card, installation guide (electrician only), DIN supply boxed as an accessory.
- Incoterms: FOB Shenzhen; air for 50; sea for 1,000.

## 4. Next steps (this week)
1. Order 5× Unit Thermal2 and 5× Stamp C6LoRa, a DIN box and a cheap test board with a 16 A breaker and a heater load; loosen one terminal and film the thermal image.
2. List 15 electrical contractors who advertise thermography and 2 insurers' loss-prevention departments; write the €500 pilot offer.
3. Spend an hour with a licensed electrician on where in a board a sensor can legally and practically sit, and what the installation guide must say.

Want help sourcing or building this? Talk to us via www.gongbans.com.
