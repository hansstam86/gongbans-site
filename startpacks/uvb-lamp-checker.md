# UVB Lamp Checker — Founder Start Pack

> A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail, and the only real meters cost €300–500.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** UVB output of terrarium lamps drops 30–50% long before the lamp looks dim. Keepers replace lamps by calendar (too late or too early). The one trusted meter costs £317–350 in the UK and ~€480+ on the continent; the cheap "UV meters" are junk.
- **Customer:** Reptile, tortoise and parrot keepers in DE, UK, NL, FR (buyers and users); reptile shops and zoos (buyers, as a counter tool and resale item).
- **Product:** A €69–89 pocket meter with a UVA/UVB sensor, lamp-type profiles, a distance guide and a replace/keep verdict; logging per terrarium via BLE; retail counter display.
- **Why now:** The open UV reference pack (sensor + MCU, with Gerbers and BOM) is in the catalogue; UV photodiode sensors are now €2–4; the hobby has moved to "evidence-based husbandry" forums where UV index charts are standard.
- **The ask:** ~€70k (estimate) to 1,000 units in 20 shops, plus a consumer web shop. Route: bootstrap + shop consignment + a small pre-order campaign in the hobby forums.

## 2. Business plan

### Problem & customer
Germany has the largest reptile-keeping community in Europe (the national pet-trade association counts terrariums together with aquariums; the combined "ornamental fish and terrariums" figure was ~1.1 M in 2024 — [Interzoo market report](https://www.interzoo.com/en/news/2025/article/the-german-pet-market-2024)). France reported ~2.1 M pet reptiles (FEDIAF, 2022, via [Statista](https://de.statista.com/statistik/daten/studie/454104/umfrage/reptilien-in-europa-nach-laendern)). The UK has a large tortoise and bearded-dragon community. Parrot keepers are the second group: bird UVB lamps have the same fade problem.

Who pays: the keeper (€69–89 is a fraction of a €150 UVB setup and one vet visit). Reptile shops pay for a counter unit and buy stock at wholesale. Zoos and breeders buy one per keeper. Who uses: the same people, weekly, for 30 seconds.

### Market size (estimates)
- Assume **~4 M terrariums/UVB-dependent enclosures in EU + UK** (DE ~1 M, FR ~1 M incl. reptiles kept without UVB, UK ~0.8 M, rest ~1.2 M — rough). Add ~0.5 M parrot households using UV lighting.
- **TAM:** 4.5 M × €79 ≈ **€355 M** if everyone bought one meter. Nobody buys a meter for a corn snake; UVB-dependent species (lizards, tortoises, chameleons, some birds) are maybe 40% → **€140 M** realistic ceiling.
- **SAM:** engaged keepers who read forums/follow UV-index husbandry — 15% of the UVB group → 270k → **€21 M**.
- **SOM (3 years):** 5% of SAM → 13,500 units → **€1.1 M**. Plus consumables upsell (calibration check cards, lamp bundles) via shops.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Specialist UV-index radiometer (NIST-traceable, 9 V battery; UK retail £317–350, continental listings €480–540 — [Reptile Centre](https://www.reptilecentre.com/products/solarmeter-65r-uvi-radiometer), [Peregrine](https://peregrine.co.uk/?p=2533), [Desertcart BE](https://www.desertcart.be/products/70068772-6-5r-reptile-uv-index-meter.md)) | The gold standard; forums trust it | Price; no logging; no lamp profiles; a shop can't stock ten |
| Cheap "UV meters" (€15–40, generic UVA photodiodes) | Flood the marketplaces | Not UVB-weighted, not UV-index; forums warn against them |
| Lamp replacement by calendar (6–12 months) | "Do nothing" | Wastes lamps or risks animals |
| UV test cards (colour-change) | €5 | Qualitative, unreliable with age |
| Shops' own meter at the counter | Some shops own one | Doesn't travel home with the customer; our counter unit *is* the sales tool |

**Wedge:** price (~1/4 of the incumbent), a verdict instead of a number ("replace / fine / too far from the basking spot"), per-terrarium logging, and the shop as the channel: shops sell lamps on evidence instead of arguments.

### Product & value proposition
Hardware: 70 × 40 × 15 mm, UVA/UVB sensor behind a PTFE diffuser, small OLED/segment display, one button, CR2032 or 300 mAh Li-ion, optional BLE. Firmware: UV index with a species/lamp-profile library (T5 HO, compact fluorescent, mercury-vapour, metal-halide), distance guide (hold at basking-spot distance), trend per terrarium, "replace" when output drops below a user-set % of the baseline you measured when the lamp was new. **Indicative measurement, not a calibrated radiometer** — say so on the box. Zoo/breeder version: BLE + app log + exported CSV.

Pricing (estimates): **B2C €79** (web shop), **B2B wholesale €42–48** to shops (RRP €79–89), counter display with 6 units + demo lamp + poster €299. Pro version with BLE €119.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (UV sensor, MCU, OLED, button, battery/holder, PCB) | €9.80 | €7.60 |
| Assembly & test (SMT, flash, **optical calibration against a reference lamp**) | €3.50 | €2.40 |
| Enclosure (ABS 2-part, PTFE window, tooling amortised) | €2.60 | €1.50 |
| Packaging (retail box, quick-start card) | €0.90 | €0.60 |
| Freight + duty to EU | €1.20 | €0.70 |
| Certification amortised (~€12k: EMC, safety, RoHS/REACH; +€8k if BLE) | €12.00 | €2.40 |
| **Landed cost** | **€30.00** | **€15.20** |
| Sell price (wholesale to shop / direct) | €45 / €79 | €45 / €79 |
| Channel margin (shop keeps RRP–wholesale; direct none) | — | — |
| **Gross margin (wholesale)** | **€15.00 (33%)** | **€29.80 (66%)** |
| **Gross margin (direct)** | **€49.00 (62%)** | **€63.80 (81%)** |

Skip BLE on the base model: it adds RED + EN 18031 cost (~€15–20k) that 1k units can't carry. Add it in the Pro version once volume exists.

### Go-to-market
**First 100 customers:** 20 reptile shops × 5 units on consignment (the kill question), via a visit tour of DE/NL/UK shops and the national reptile fairs (Terraristika Hamm is the big one in Europe; also Houten NL, Doncaster UK). Hobby forums and the big German/English reptile Facebook groups and YouTube husbandry channels — send 10 review units to the evidence-based husbandry crowd; they are the influencers, and they are brutal, so the meter must be honest.

**Scale channels:** reptile-supply wholesalers (DE/NL/UK), pet e-commerce, parrot-supply shops, lamp manufacturers (co-marketing: "check your lamp with…").

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from the UV pack + StickC-Plus; correlate against a reference radiometer on 10 lamp types; 20 shops take 5 units each on consignment (hand-built, printed cases). |
| Q2 | Custom PCB + tooled case; EVT 100; calibration jig; shop sell-through data. |
| Q3 | Certification (EMC/LVD, RoHS); 1,000 units; web shop; fair season. |
| Q4 | Wholesaler listing in DE and UK; Pro/BLE version EVT; lamp-brand co-marketing. |

**Team:** 1 hardware/firmware engineer (part-time is fine — this is a small board), 1 founder who knows the hobby and does shops/fairs/content, calibration and optics advice bought in (a day with a photometry lab). Two people, one part-time.

**Funding to first 1,000 units (estimates):** PCB spins €5k, tooling €8k, calibration jig + reference radiometer €3k, firmware/app contractor €8k, certification €12k, 1,000 units landed €18k, fairs + review units €6k, 9 months lean overhead €25k ≈ **€85k**; minus consignment and pre-order income (~€15k) ≈ **~€70k**. Bootstrap + consignment + a pre-order run on the web shop. Too small for grants to be worth the paperwork; a hobby-sector angel is plausible.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** UV sensor response doesn't match the UV-index (erythemal/vitamin-D) weighting; reading differs from the reference by lamp type | Lamp-type profiles with per-type correction factors; calibrate each unit against a reference lamp; publish the correlation chart; call it indicative |
| **Technical:** sensor and diffuser degrade under UV | PTFE window, sensor rated for UV exposure; a yearly "self-check" routine |
| **Market:** the forums destroy you if the numbers are off | Send units to the toughest reviewers first; don't launch until the correlation is within ±15% on the main lamp types |
| **Market:** low demand — scored 2/5 for a reason | The shop channel decides: if sell-through in 6 weeks is poor, stop at 1k units and keep it as a side product |
| **Regulatory:** none heavy, but claiming "radiometer" or "calibrated" invites metrology trouble | "Indicative UV-index checker" everywhere |
| **Supply:** UV sensor IC is a limited-source part | Qualify two sensor families; buy a year's reel |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| UV Sensor Demo (VEML6075 + LPC824) | https://www.gongbans.com/db/uv-sensor-veml6075-lpc824.html | Full open design pack: UVA/UVB sensor + MCU, UV-index firmware starting point | bom, gerber, pcb, schematic | Curated ATU kit, hosted; verify redistribution terms before commercial derivative |
| Seeed Grove UV Sensor | https://www.gongbans.com/db/seeed-grove-uv-sensor.html | Alternative analogue UV front-end | schematic | Seeed wiki resources; check licence |
| Seeed Grove Sunlight Sensor | https://www.gongbans.com/db/seeed-grove-sunlight-sensor.html | Visible/IR channel for lamp-type detection | schematic | Seeed wiki resources |
| M5Stack StickC-Plus (K016-P) | https://www.gongbans.com/db/m5stack-stickc-plus.html | Display + battery + ESP32 for the works-like prototype | enclosure/structure only | Buy; don't copy |

**Board-fact caution:** the VEML6075 appears in the catalogue as the sensor in the UV pack. Check its current availability with distributors; if it's end-of-life, pick a current UVA/UVB sensor with the same I2C approach — the firmware math is the same.

### Block diagram
```
UVB lamp ~~~> [PTFE diffuser] -> [UVA/UVB sensor, I2C] -> [MCU] -> [OLED 0.96"] 
                                 [visible/IR sensor]  ---/   |-> [button]
                                 [CR2032 or Li-ion + charger] |-> (Pro: BLE -> phone app log)
```
**Engineering gap:** the open pack measures UV index. Missing: the diffuser/aperture optics so the reading is distance- and angle-consistent, lamp-type correction factors derived from measurements against a reference radiometer, the verdict logic, a calibration jig for production, and a case that keeps sunlight out of the sensor except through the window. Mostly optics and measurement discipline, not electronics.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| UVA/UVB I2C sensor | €2.80 | **Limited-source**; qualify two |
| Visible/IR sensor (optional, lamp-type detection) | €0.90 | |
| MCU (LPC8xx-class or ESP32-C3 if Pro) | €0.80 / €1.90 | |
| 0.96" OLED | €1.60 | Commodity |
| PTFE window disc, 10 mm | €0.30 | Virgin PTFE only |
| CR2032 holder + cell (or 300 mAh Li-ion + charger IC) | €0.50 / €1.80 | Li-ion adds UN 38.3 + battery-regulation work — CR2032 for the base model |
| Button, passives, PCB | €1.00 | |
| ABS 2-shell case | €2.60 | **Tooling €6–9k** |
| Calibration lamp + reference radiometer (one-off for the jig) | €1,200 | Buy the incumbent meter; it is your reference |

### Firmware/software starting point
- The UV pack's firmware targets LPC824 (NXP MCUXpresso SDK exists). Sensor vendor application notes describe UV-index calculation from UVA/UVB channels — follow them.
- Arduino libraries for the VEML6075 exist (search "VEML6075 Arduino library"); fine for the StickC-Plus prototype.
- Pro version app: a simple BLE logger; search for an open ESP32 BLE + Flutter/React Native template, or skip the app and log to CSV via USB.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | StickC-Plus + UV pack board in a printed case; correlation against a reference radiometer on 10 lamp types within ±20%; 20 shops agree to take 5 units on consignment (the kill question runs W6–12) |
| 3–5 | Works-like | 100 hand-built units; diffuser geometry fixed; lamp profiles v1; verdict logic; ship to 20 shops |
| 6–8 | Looks-like + EVT | Custom PCB v1; tooled case T1; calibration jig; 50 EVT units ±15% vs reference across profiles; EMC pre-scan |
| 9–10 | DVT + pre-compliance | Sell-through data from shops (target: 50% of consigned units sold in 6 weeks); EMC/LVD pre-compliance; RoHS declarations |
| 11–12 | Pilot batch | 300 units; web shop live; 10 review units with the husbandry influencers; reorder from ≥8 shops |

### Certification checklist (EU)
- **CE via EMC Directive** (EN 55032/55035) and **LVD** does not apply below 50 V — but **EN IEC 62368-1** is still your safety reference, especially with a Li-ion cell. Est. €3–5k EMC + €2–3k safety assessment.
- **If BLE (Pro):** RED (EN 300 328, EN 301 489-1/-17, EN 62311) ~€5–8k with a pre-certified module, plus **EN 18031-1** if it connects to the internet through the phone app (~€8–15k). That is why the base model has no radio.
- **RoHS, REACH, WEEE** registration in each country of sale (DE: stiftung ear; UK: separate scheme).
- **Battery Regulation (EU) 2023/1542:** CR2032 is a portable battery — labelling, take-back info; Li-ion adds UN 38.3 (~€2–3k).
- **CRA:** applies to products with digital elements; low-risk class, self-assessment; reporting obligations from 11 Sept 2026, full from 11 Dec 2027. Firmware update path is optional for a device with no connectivity — document the decision.
- **GDPR:** none without the app; with the app, a privacy notice (terrarium logs aren't personal data; account emails are).
- **Toy directive:** no. **Metrology (MID):** no — never call it a calibrated instrument.
- **Total certification budget estimate: €7–10k (base), €25–35k (Pro with BLE).**

### Validation toolkit
- **Kill question:** Do 20 reptile shops take 5 units each on consignment, and do they sell through in 6 weeks?
- **Cheapest experiment (~€900):** buy the incumbent meter (your reference, you need it anyway), build 5 StickC-Plus prototypes, visit 5 shops and 1 fair; ask for consignment commitments on the spot.
- **5-question interview (shop owner / keeper):** 1) How do you decide when a UVB lamp is replaced? 2) Have you had an animal with a UV-related problem (MBD) where the lamp turned out to be dead? 3) Do you own a UV meter? Which? Why/why not? 4) Would a €79 checker with a replace/keep verdict change how you sell (or buy) lamps? 5) Would you stock 5 on consignment and put one on the counter?
- **Landing page:** headline "Is your UVB lamp still working? Know in 10 seconds." Bullets: "UV index at the basking spot, with lamp profiles for T5, compact and mercury-vapour." / "Replace/keep verdict based on your lamp's own baseline." / "€79 instead of €350 — indicative checker, not a lab instrument."
- **Pass threshold:** 20 shops consign (100 units) **and** ≥50 sell in 6 weeks, or 150 web pre-orders at €69 in 4 weeks.

### First production checklist
- Samples: 5 golden samples each with a calibration certificate against your reference; one stays at the factory.
- DFM: window press-fit tolerance, sensor height vs window, light leaks; test-jig design with a stable UV source (LED-based, not fluorescent).
- MOQ talk: case 1k; sensor reel 2.5k; OLED 1k. Negotiate the 5k step.
- QC: AQL II 2.5/4.0; 100% calibration on the jig with logged correction factor per serial; 2% sample re-check after 24 h.
- Packaging: retail box with window, EAN barcode, counter display design for 6 units.
- Incoterms: FOB Shenzhen; small volume → air freight consolidated.

## 4. Next steps (this week)
1. Buy the reference radiometer and three different UVB lamps; order the UV pack boards (Gerber + BOM) and 3× StickC-Plus.
2. Draft the lamp-profile measurement protocol (distance steps, lamp age, warm-up) — you'll live by this spreadsheet.
3. List 30 reptile shops within driving distance and the dates of the next three reptile fairs; book a table at one.

Want help sourcing or building this? Talk to us via www.gongbans.com.
