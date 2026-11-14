# Touchless Switch Module — Founder Start Pack

> A 25 × 25 mm wave-to-activate gesture/proximity module, built from a fully open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Small European manufacturers of soap dispensers, bathroom furniture, lamps and kitchen fittings want "touch-free" on the box, but have no optical-sensor engineer, and the €1 Alibaba IR switches false-trigger, fail EMC and come with no documentation.
- **Customer:** EU OEMs and their contract manufacturers (they pay, they design in); the end user waves a hand.
- **Product:** A documented module with a defined connector, relay or MOSFET output, false-trigger filtering, an EMC pre-test report and a design-in guide. No radio.
- **Why now:** Hygiene expectations stuck after 2020; the catalogue holds a complete gesture reference (schematic, PCB, Gerber, BOM) so the sensor front-end is a copy job, not a research project.
- **The ask:** ~€45k (estimate) to 1,000 modules, five sampled OEMs and one 1,000-piece order. Bootstrap plus OEM NRE fees; no outside money needed if the first OEM pays for samples.

## 2. Business plan

### Problem & customer
Buyer: the product manager or lead engineer at a **European OEM with 10–200 employees** making dispensers (soap, sanitiser, paper), bathroom mirrors and cabinets, kitchen lighting (under-cabinet), waste bins, drinking-water taps and small appliances. Their contract manufacturers (often in Poland, Portugal, Italy, Turkey) are the second buyer. They need a part number they can put on a BOM, a datasheet in English, and someone who answers when the sensor false-triggers under a fluorescent tube.

The user is whoever waves a hand. They never know your name. This is a **component business**: low glamour, repeatable, margin comes from volume and from NRE fees for variants.

### Market size (estimates)
- Factory-direct IR hand-wave switches list at **US$2.6–4.8** on sourcing platforms, and retail in Europe at **£9–12 / $12–58** depending on brand ([Global Sources listing](https://www.globalsources.com/product/light-sensor-switch_1194614365f.htm), [UK retail example](https://www.simplelighting.co.uk/products/white-hand-wave-sensor-switch-12-24vdc-5cm-range), [US retail example](https://marvellighting.com/product-detail-page/hand-wave-motion-sensor-switch-by-alloy-led)). That tells you the price band and that the market is real.
- **TAM (estimate):** EU + UK consumption of touchless sensor switches for dispensers, furniture lighting and small appliances — assume 15 M units/yr at ~€3 average → **~€45 M/yr**.
- **SAM (estimate):** OEMs that want a documented, EU-supported module rather than a bulk Alibaba part — maybe 15% of volume → ~2 M units → **~€7 M/yr**.
- **SOM (3-year, estimate):** 5% of SAM → 100k units/yr at €9 → **~€0.9 M/yr**. Small, but a 40%-margin component line with repeat orders is a fine first business and a door-opener for bigger design-in work.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Bulk IR switch modules from Chinese catalogue suppliers (US$0.3–5, MOQ 200+) | The default for cost-driven OEMs | No EMC report, no false-trigger spec, part changes without notice, zero support |
| Branded furniture-lighting sensor switches (German/Italian furniture-hardware brands, €5–25 trade) | Sold as finished switch, not as design-in module | Fixed form factor and connector, premium price, not for dispensers |
| Integrated proximity sensor ICs (VCNL-class, APDS-class) | What a competent OEM would use | Needs optical design, firmware, EMC work — exactly what small OEMs lack |
| Capacitive touch | Cheap, reliable | Not touchless; doesn't work through thick fronts or with gloves |
| mmWave / ToF modules | Overkill, €4–10 | Price, power, over-sensitivity |
| Do nothing (mechanical switch or pedal) | Free | "Touch-free" sells; pedals break |

**Wedge:** *documentation and support as the product*. Datasheet with real trigger distance vs. surface reflectance, an EMC pre-test report the OEM can hand to its test lab, a design-in guide (window material, aperture, mounting), and a variant programme (relay, MOSFET, logic output; 5 V/12 V/24 V) for a small NRE fee.

### Product & value proposition
- **Module A (proximity):** VCNL4020-class IR proximity sensor + small MCU, 5–24 V input, open-drain or 3 A MOSFET output, trigger distance adjustable 2–20 cm, latching/momentary/timed modes via solder jumper or a one-wire config. 25 × 25 mm, 2.0 mm pitch connector.
- **Module B (gesture):** same footprint, adds left/right swipe (for dimming lamps, cycling modes) using the open gesture reference as the starting point.
- **Module C (relay):** mains-rated relay daughterboard, for lamps and dispensers with AC loads (safety work doubles here — do it only if an OEM pays NRE).

Pricing (estimates, B2B only): **€9–15/module at 1k**, €6–8 at 10k; sample kit (5 modules + eval board + design guide) €149; variant NRE €3–8k. No B2C.

### Unit economics (estimates, Module A, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (proximity sensor, MCU, MOSFET, LDO, passives, connector, PCB) | €3.60 | €2.90 |
| Assembly & test (SMT, flash, optical functional test) | €0.90 | €0.55 |
| Enclosure (none — bare module; optional IR-pass window sold separately) | €0.00 | €0.00 |
| Packaging (tray + ESD bag, 50/tray) | €0.12 | €0.08 |
| Freight + duty to EU | €0.30 | €0.15 |
| Certification amortised (EMC pre-test + RoHS/REACH docs ~€6k) | €6.00 | €1.20 |
| **Landed cost** | **€10.92** | **€4.88** |
| Sell price | €12.00 | €9.00 |
| Channel margin (direct) | €0 | €0 (10% if via distributor) |
| **Gross margin** | **€1.08 (9%)** | **€4.12 (46%)** |

The first 1,000 units pay for the EMC report; that is normal for a component. Charge the sample kits and NRE so the first thousand aren't your money.

### Go-to-market
**First 100 customers (really: first 20 design-ins, 5 of them serious):**
1. Make a list of 100 EU OEMs: dispenser makers (DE, IT, NL, DK), bathroom-furniture and mirror makers (DE, PL, IT), kitchen-lighting brands, drinking-water tap and bin makers. Trade fairs: ISH Frankfurt (bathroom), interzum Cologne (furniture components), Light + Building, Interclean Amsterdam (hygiene). Walk the halls with a working demo on a soap dispenser.
2. Contract manufacturers and EMS in Poland/Portugal/Hungary serving these OEMs — they recommend parts.
3. A listing on a European electronics distributor's marketplace once you have a datasheet and a part number.

**Scale channels:** distributors (catalogue + long-tail), furniture-hardware wholesalers, a "touchless inside" co-branding sticker for OEMs who want the marketing.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Copy the open gesture pack into a 25 × 25 mm module; 50 hand-built samples; EMC pre-scan; datasheet v0.9. Kill question: 5 OEM sample requests, 1 PO within 3 months. |
| Q2 | Production v1 (1k), full EMC report, relay/MOSFET variants, design-in guide, eval board. Walk interzum/ISH. |
| Q3 | First OEM in production; second 2k batch; distributor listing. |
| Q4 | 5k batch; gesture variant B; first NRE-funded custom. |

**Team:** 1 hardware/firmware engineer (full-time), 1 founder for OEM sales and documentation (full-time), test-lab and layout bought in. Two people. Keep it that way for a year.

**Funding to first 1,000 units (estimates):** PCB spins and samples €6k, EMC pre-test + RoHS/REACH documentation €6k, eval boards and sample kits €4k, first 1k modules €4.5k landed, two trade fairs €8k, 9 months lean overhead €25k ≈ **€53k**; minus sample-kit and NRE income (~€10k) ≈ **€45k**. Bootstrap. If an OEM pays €5k NRE for a variant in month 3, you are funded.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** false triggers from sunlight, fluorescent flicker, shiny surfaces, steam | Modulated IR, ambient-light cancellation in the sensor, firmware hysteresis, configurable distance; publish the limits honestly in the datasheet |
| **Technical:** OEM front panels block IR | Design-in guide with window material list; sell a tested IR-pass window |
| **Market:** OEMs copy the module and go direct to a Chinese supplier after a year | Expected. Keep adding variants and support; margin is in the first two years of each design-in; move upmarket (gesture, relay, UL/CE packs) |
| **Regulatory:** the OEM's end product fails EMC with your module installed | Your pre-test report plus a hand-holding clause: you attend their EMC test for a day fee |
| **Supply:** the sensor IC is single-source | Qualify a second sensor family on the same footprint from day one; keep 6 months of ICs in stock |
| **Licence:** the open reference pack's licence | Read it. If restrictive, use it as a *reference* and redraw the schematic with your own layout — that is what you'd do anyway |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Gesture Recognition (VCNL4020 + LPC824) | https://www.gongbans.com/db/gesture-vcnl4020-lpc824.html | Full open design pack of exactly this function (hand-cream dispenser reference) | bom, gerber, pcb, schematic | Curated ATU kit, hosted files; verify redistribution terms before selling a derivative |
| Proximity Sensor (VCNL4020) | https://www.gongbans.com/db/proximity-sensor-vcnl4020.html | Simpler proximity-only variant, 1–200 mm | none listed | Documentation only; use for application reference |
| M5Stack Unit Gesture (U127) | https://www.gongbans.com/db/m5stack-unit-gesture.html | Richer gesture sensing for the premium variant; quick prototype | enclosure/structure only | Buy the unit; don't copy electronics |
| Seeed Grove IR Distance Interrupter v1.2 | https://www.gongbans.com/db/seeed-grove-ir-distance-interrupter-v1-2.html | Lowest-cost IR interrupter alternative for a €0.50 BOM version | schematic | Seeed wiki resources; check licence per file |

### Block diagram
```
 5-24 V in --> [LDO 3.3 V] --> [small MCU (LPC8xx/CH32V/STM32G0-class)]
                                    |  I2C
                             [IR proximity/gesture sensor] (IR LED + photodiode)
                                    |
                     [output stage: open-drain | 3 A MOSFET | relay board]
                     [config: solder jumpers / 1-wire]  [status LED]
```
**Engineering gap:** the open pack gives you the sensor front-end and MCU. Missing: a 5–24 V tolerant input and output stage, EMC hardening (ESD on the connector, ferrites, layout), production firmware with configurable modes and robust false-trigger filtering, the IR window spec, and the documentation set. Two to three engineer-months.

### Starter BOM (estimates per module at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| IR proximity sensor with ambient-light cancellation (VCNL4020-class) | €1.20 | **Sole-source per part number**; qualify a second family |
| Small ARM/RISC-V MCU (LPC824-class or CH32V003/STM32G0) | €0.60 | Choose on availability; the open pack uses LPC824 |
| 3 A N-MOSFET + gate drive | €0.25 | |
| LDO 3.3 V, 24 V-tolerant | €0.20 | |
| ESD/TVS, ferrite, passives | €0.35 | EMC insurance, don't skip |
| Connector 2.0 mm 4-pin | €0.15 | Pick a connector OEMs already stock |
| PCB 2-layer 25 × 25 mm | €0.35 | |
| Optional IR-pass window (sold separately) | €0.40 | Polycarbonate, 850 nm pass |

### Firmware/software starting point
- The gesture pack's firmware targets LPC824; NXP's MCUXpresso SDK exists for LPC8xx. If you switch MCU, the proximity-sensor logic is a few hundred lines — rewrite it.
- Vendor drivers for VCNL-class sensors exist as Arduino libraries (search "VCNL4020 Arduino library").
- No cloud, no app, no radio. The deliverable is a datasheet, not a repo.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Breadboard from Unit Gesture + a MOSFET on a bought soap dispenser and an under-cabinet lamp; video; sample requests from **5 OEMs** via fair/LinkedIn/distributor contacts. Kill question clock starts: 1 PO of 1,000 within 3 months |
| 3–5 | Works-like | 25 × 25 mm PCB v1 from the open pack; false-trigger test bench (sunlight lamp, fluorescent, steam, white/black/mirror targets) passes your published spec; 50 samples shipped |
| 6–8 | Looks-like + EVT | v2 with connector, output options, ESD; EMC pre-scan (EN 55032 radiated/conducted, EN 55035 ESD/EFT/surge) clean; datasheet v1.0; design-in guide |
| 9–10 | DVT + pre-compliance | 200 units from the EMS; RoHS/REACH declarations collected; full EMC report from an accredited lab; 1,000-hour burn-in on 20 units |
| 11–12 | Pilot batch | 1,000 modules produced; first OEM pilot (50 dispensers) in the field for 4 weeks with <1% false-trigger complaints |

### Certification checklist (EU)
- **CE via EMC Directive**: EN 55032 / EN 55035 (or EN IEC 61000-6-1/-3). No RED (no radio). The module alone is a component; the OEM certifies the end product — but your EMC report is your sales tool. Est. €3–5k pre-test + €4–6k full report.
- **LVD** only applies to the relay variant if the module itself carries >50 V AC — keep mains on a separate, separately-certified relay board or buy a certified relay module.
- **RoHS** (collect supplier declarations), **REACH** SVHC check, **WEEE**: as a component supplier you usually aren't the producer-of-record; confirm per country.
- **EN 18031 / RED cybersecurity:** not applicable (no radio, no internet). **CRA:** applies to "products with digital elements" — a module with firmware counts. Reporting obligations from 11 Sept 2026, full application 11 Dec 2027. Keep a vulnerability contact and an SBOM; low burden for a device with no connectivity, but document it.
- **Battery regulation:** none. **GDPR:** none. **Toy directive:** none unless an OEM puts it in a toy — state that it is not evaluated for toys.
- Photobiological safety of the IR LED (EN 62471): usually exempt-class at these powers; get a one-page assessment (~€800).
- **Total certification budget estimate: €8–12k.**

### Validation toolkit
- **Kill question:** Do 5 European OEMs request samples and does one place a 1,000-piece order within 3 months?
- **Cheapest experiment (~€400):** retrofit two bought products (soap dispenser, under-cabinet lamp) with Unit Gesture + MOSFET; a one-page datasheet PDF; 30 targeted messages to OEM engineers. Count sample requests.
- **5-question interview (OEM product/engineering lead):** 1) Do you sell or plan a touch-free product, and what sensor is in it today? 2) What went wrong with it (false triggers, supplier changes, EMC)? 3) What voltage, output and connector would make it a drop-in for you? 4) What documentation does your EMC lab or your buyer ask for? 5) At €9–12 at 1k pieces, who signs the PO and what's the annual volume?
- **Landing page:** headline "Touch-free, designed in by Friday." Bullets: "25 × 25 mm module, 5–24 V, relay or MOSFET output." / "EMC pre-test report and design-in guide included." / "Built on an open reference design — no black box, no surprise part changes."
- **Pass threshold:** 5 sample kits sold at €149 **and** one written PO/LOI for 1,000 pieces within 12 weeks.

### First production checklist
- Samples: 5 golden samples with measured trigger-distance curves attached.
- DFM with the EMS: panelisation of 25 × 25 mm boards, test-point access, programming/test jig quote.
- MOQ talk: sensor IC reels (typically 2.5k–5k per reel) — buy a reel; EMS MOQ 500–1,000.
- QC: AQL II 1.0 major for a component; 100% functional optical test on the jig; log serials.
- Packaging: ESD trays of 50, moisture-barrier bag, humidity indicator; label with part number, rev, date code.
- Incoterms: EXW/FOB from the EMS; if the EMS is in the EU (plenty in PL/HU can do this cheaply), no duty question at all — consider that seriously for a no-radio board.

## 4. Next steps (this week)
1. Download the gesture pack (schematic, PCB, Gerber, BOM), read its licence, and order 10 bare boards and parts from the BOM.
2. Buy a soap dispenser and an under-cabinet lamp; retrofit both with Unit Gesture + MOSFET and film a 30-second demo.
3. Build the 100-OEM list (dispensers, bathroom furniture, kitchen lighting, bins, taps) with the engineering contact for each, and book interzum or ISH tickets.

Want help sourcing or building this? Talk to us via www.gongbans.com.
