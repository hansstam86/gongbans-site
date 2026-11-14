# Half-Keyboard for One-Handed Typing — Founder Start Pack

> A compact one-handed mechanical keyboard with mirror-layer typing and programmable macros, built from an open one-handed keyboard design, for people with a temporary or permanent single-hand limitation.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** After a stroke, a fracture, or with a congenital limb difference, typing with one hand on a standard keyboard is slow and tiring. The dedicated one-handed keyboards cost €500–1,000 and look like they were designed in 1995 — because they were.
- **Customer:** Occupational therapists (OTs) and rehab clinics recommend; workplace-inclusion budgets, insurers and employers pay; people with one usable hand use. ~9–9.5 million stroke survivors live in Europe; ~205,000 OTs work here.
- **Product:** 44–50 key mechanical keyboard, left and right versions, "hold space to mirror the other half" firmware (QMK), 3.5 mm switch-access jack, OT-tuned low-force switches, wrist rest, web-based training. €169 incl. VAT (€142 ex-VAT).
- **Why now:** Open one-handed keyboard hardware and mature open firmware (QMK/ZMK) make a modern €149–199 device plausible; the half-QWERTY idea is decades old and the original patents should have expired — verify.
- **The ask:** ~€40k to the first 1,000 units; bootstrap plus assistive-technology dealer pre-orders.

## 2. Business plan

### Problem & customer
Half-QWERTY is simple: you type the home-hand half normally; holding space mirrors the other half onto the same keys, so your existing muscle memory works — people reach 60–80% of their two-handed speed after a few hours. The incumbents prove the demand (Maltron single-hand ~US$540–765; TiPY ~€990 + VAT; Matias Half-Keyboard ~US$595 historically, hard to find in Europe) but the price excludes anyone whose insurer says no, and the temporary-injury market (a broken wrist for 8 weeks) is unserved.

Who pays: workplace-adaptation schemes (DE: Integrationsamt/Rentenversicherung; UK: Access to Work; NL: UWV), rehab clinics buying trial units, employers, and self-payers for temporary injuries. Who recommends: OTs and ergonomists. Who uses: the person — often typing for work.

### Market size (estimates — check them)
- **TAM:** ~9–9.5 M stroke survivors in Europe (SAFE, 2017 base), of whom roughly a third have lasting upper-limb impairment and a fraction are of working age and type → say 300,000 people; plus congenital/amputation (~50,000 working-age) and ~1 M temporary upper-limb fractures per year among office workers (estimate). Keyboard TAM ≈ **€50–80 M** one-off plus replacement.
- **SAM:** reachable through OTs, assistive-tech dealers and workplace schemes in DE/UK/NL/Nordics: **~€8–12 M/year**.
- **SOM (3 years):** 6,000 units ≈ **€850k revenue**.

### Competition (1 search)
| Alternative | Price (est.) | Weakness |
|---|---|---|
| Maltron single-hand | US$540–765 | Dated design, big, hard to get in the EU |
| TiPY one-hand keyboard | ~€990 + VAT | Excellent but out of reach without funding |
| Matias Half-Keyboard | ~US$595 (historical) | Membrane feel, availability poor in Europe |
| Software: on-screen keyboards, dictation | €0 | Dictation fails in open offices and for code/spreadsheets; on-screen is slow |
| DIY: a 40% mechanical keyboard with QMK | €80–150 + weekends | No OT guidance, no switch access, no left/right version |
| Do nothing — type with one hand on a full keyboard | €0 | Slow, shoulder strain |

**Wedge:** price (a third of the incumbents), modern mechanical feel, left and right SKUs, switch-access jack, and OT-facing training material. Position as "the one your OT lends you first".

### Product & value proposition
- **Hardware:** 44–50 low-profile hot-swappable mechanical switches (35–45 g), compact 25 × 12 cm, USB-C, aluminium top plate, optional 3.5 mm jack for an assistive switch (acts as the "mirror" key or any macro), detachable wrist rest.
- **Firmware:** QMK-based: mirror layer on hold-space, tap-dance for numbers/symbols, 3 macro banks, web configurator (VIA-compatible if you keep VIA support).
- **Training:** a free web typing tutor that teaches the mirror layer in 10 lessons; OT quick-start sheet.
- **Pricing:** **€169 incl. VAT** (€142 ex-VAT) B2C; **€129 ex-VAT** to assistive-tech dealers/clinics in packs of 5; loan-fleet pricing for clinics. Wireless variant later (+€30; RED).

### Unit economics (estimates, per keyboard)
| Item | 1,000 units | 5,000 units |
|---|---|---|
| Electronics BOM (PCB, MCU, 48 switches, diodes, USB-C, jack) | €22 | €17 |
| Keycaps (48, legended both halves) | €6 | €4 |
| Assembly & test (switch insertion, key-test fixture) | €7 | €4.50 |
| Enclosure (ABS base, aluminium plate, wrist rest) | €9 | €6 |
| Packaging + cable + quick-start | €3.50 | €2.50 |
| Freight + duty to EU | €3 | €1.60 |
| Certification amortised (€6k EMC) | €6 | €1.20 |
| **Landed cost** | **€56.50** | **€36.80** |
| Sell price direct ex-VAT | €142 | €142 |
| Via AT dealer (net €129 ex-VAT; dealer sells at €199) | €129 | €129 |
| **Gross margin direct** | **60%** | **74%** |
| **Gross margin via dealer** | 56% | 71% |

### Go-to-market
**First 100 customers:** 10 OTs in stroke rehab units (national OT associations' special-interest groups on assistive technology) get two loaner boards each; the stroke-survivor associations' online communities; r/ergomechkeyboards and the one-handed-keyboard threads where people already hack this; two assistive-technology dealers per country; a demo at one rehabilitation trade fair. Make the typing tutor public so people find you before they find the incumbents.

**Scale:** assistive-tech dealer catalogues (they are the gatekeepers for funded purchases), listing in national assistive-device databases (the EASTIN-linked national databases — free listings), employer disability-inclusion programmes, Amazon for self-payers with a temporary injury.

### 12-month plan
- **Q1:** 10 prototypes from the open design with QMK mirror firmware, 10 OT trials with clients. Gate: 5 of 10 OTs would recommend it over the €500+ incumbents.
- **Q2:** Own PCB (left/right), switch-access jack, enclosure soft tool, EMC test, web tutor v1, 300 units.
- **Q3:** Dealer listings in DE/UK/NL, national database entries, 1,000 units.
- **Q4:** Wireless variant decision, employer channel, second production batch.

**Team:** one electronics/firmware engineer (part-time — QMK does the heavy lifting), one mechanical designer for 6 weeks, one OT as paid adviser, founder on sales. Add a web developer for the tutor.

**Funding to 1,000 units (estimate):** NRE €22k (PCB, tooling €10k, tutor) + certification €6k + 1,000 × €50 production = €50k → **~€78k**; dealer pre-orders and clinic packs can cover €35k → cash need **~€40k**. Bootstrap; accessibility grants (national disability-innovation funds) are a realistic add-on.

### Top risks
- **Technical — low:** this is a keyboard. The risk is key feel and the 3.5 mm switch-access input being debounced properly for people with tremor. Mitigation: OT trials early, adjustable debounce in firmware.
- **Market — funded purchases are slow:** funding bodies take months and prefer known dealers. Mitigation: price low enough to be bought out of pocket; dealers from day one; loan fleet so OTs can trial.
- **Regulatory:** EMC (EN 55032/55035) + LVD not applicable (USB-powered); RoHS/WEEE. **No medical claims** — it's a keyboard, not a medical device; don't say "rehabilitation device". Wireless variant → RED and batteries.
- **IP:** the half-QWERTY concept has old patents; they should have expired — do a 2-hour patent search before launch.
- **Licence:** the open one-handed keyboard project on OSHWHub may be non-commercial; check, and be ready to re-lay your own matrix (it's a weekend).

## 3. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [oshwhub-one-handed-keyboard](https://www.gongbans.com/db/oshwhub-one-handed-keyboard.html) | Open one-handed mechanical keyboard: layout, matrix, MCU wiring | schematic, pcb (EasyEDA Pro, clonable; files not fetched) | OSHWHub — licence varies; check the project page |
| [oshwhub-matrixkeyboard](https://www.gongbans.com/db/oshwhub-matrixkeyboard.html) | Key-matrix reference | schematic, pcb | OSHWHub — check |
| [seeed-grove-mech-keycap](https://www.gongbans.com/db/seeed-grove-mech-keycap.html) | Mechanical key + RGB reference | schematic | Seeed wiki — check |
| [oshwhub-miniusbkey](https://www.gongbans.com/db/oshwhub-miniusbkey.html) | Compact 44-key USB keyboard design | schematic, pcb | OSHWHub — check |

### Block diagram and engineering gap
```
[48-key matrix, hot-swap sockets] -> MCU (per open design; QMK-supported) -> USB-C HID
[3.5 mm switch-access jack x2] -> MCU GPIO (debounced, mapped to mirror/macros)
[per-key or indicator LEDs] 
Case: ABS base + alu plate + wrist rest; left and right mirror-image PCBs
```
Gap: left/right PCB variants, switch-access input, QMK mirror layer tuned with OTs, the web tutor, and a decent enclosure. Electronics risk is near zero.

### Starter BOM (per unit, estimates)
| Part | Est. cost | Note |
|---|---|---|
| MCU (QMK-supported, e.g. RP2040-class — follow the open design or pick RP2040) | €1.20 | Multi-source |
| 48 low-profile switches, 35–45 g | €12 | Many suppliers; keep two qualified |
| 48 hot-swap sockets + diodes | €4 | — |
| Keycaps with dual legends | €6 | Legend tooling for dye-sub/doubleshot is a one-off |
| PCB + assembly | €5 | — |
| USB-C, 3.5 mm jacks, ESD | €1.50 | — |
| ABS base + alu plate | €7 | Plate can be CNC at 1k, stamped at 5k |
| Wrist rest, cable, box | €5.50 | — |

### Firmware/software starting point
- **QMK** (exists; has a "swap hands" feature that does exactly the mirror-layer behaviour), **ZMK** for a future wireless version, **VIA/Vial** for user remapping — all real, well-maintained projects.
- Typing tutor: a static web app; search for open-source typing tutors you can fork and add the mirror lessons to.

### 12-week build plan
- **Week 1–2 — validate.** Clone the open design or build a 48-key QMK board from parts; flash the swap-hands firmware; hand two boards to two OTs and record first-hour speeds. *Exit:* an OT says "I'd lend this to a client tomorrow"; 5/10 OTs in calls say they'd recommend it over the incumbents at €169.
- **Week 3–5 — works-like.** Left/right PCBs, switch-access jack, debounce tuning, 10 units. *Exit:* 10 OTs testing with clients.
- **Week 6–8 — looks-like + EVT.** Enclosure and wrist rest, dual-legend keycaps, tutor v1. *Exit:* clients reach ≥60% of two-handed speed in week 2; no key failures.
- **Week 9–10 — DVT + pre-compliance.** Soft tooling, EMC pre-scan, 48-hour key-hammer test. *Exit:* pre-scan pass; 1 M actuations on sample keys.
- **Week 11–12 — pilot batch.** 50 units: 20 to dealers, 20 to clinics, 10 sold direct. *Exit:* 2 dealers list it; <5% returns.

### Certification checklist (EU)
- **EMC**: EN 55032/55035 (USB device); **LVD** not applicable (≤ 5 V); CE self-declaration. Est. **€3–6k**.
- **RoHS, WEEE registration, REACH** (keycap plastics, cable PVC).
- **No radio** in v1 → no RED, no EN 18031; **CRA** applies in principle to products with digital elements (firmware is updatable) — keep a changelog, a vulnerability contact and signed firmware. The wireless variant adds RED + Battery Regulation + UN 38.3.
- **No medical claims**; if you ever claim rehabilitation outcomes, MDR applies — don't.
- **GDPR:** only if the tutor stores accounts; keep it local-storage only.

### Validation toolkit
- **Kill question:** do 10 OTs trial it with clients and would 5 recommend it over the €500+ incumbents? **Cheapest experiment:** €400 — two QMK boards with the swap-hands firmware and ten OT conversations.
- **5-question interview:** (1) How many clients a year need one-handed typing, and what do you recommend today? (2) What stops them getting the €500–1,000 keyboards — funding, time, or looks? (3) Which matters more: speed in week 1 or comfort after month 3? (4) Do you need a switch-access input? (5) Would you keep two loaner units if they cost €129 each?
- **Landing-page headline:** "Type with one hand. Keep your muscle memory." Bullets: Hold space, the other half appears under your fingers · Left or right version, assistive-switch jack · €169 — a third of the price of the old guard.
- **Pre-order pass:** 50 paid pre-orders or 5 clinic/dealer purchase orders (≥10 units) in 6 weeks.

### First production checklist
Switch and keycap samples (feel test with 3 OTs), golden sample with firmware version label, DFM on plate/base fit and hot-swap socket alignment, MOQ 500 per hand with a 2,000 forecast (left:right split from pre-orders — stroke clients skew to one side, check), QC/AQL Level II + 100% key-press test on a fixture, drop test, FOB Shenzhen, EU importer + WEEE number on the label.

## 4. Next steps (this week)
1. Open the OSHWHub project page, read the licence, clone the design; order parts for two 48-key boards; flash QMK swap-hands.
2. Email the assistive-technology special-interest group of the national OT association and book 10 calls.
3. Spend two hours on a patent search for half-QWERTY/mirror typing and write down what you find.

Want help sourcing or building this? Talk to us via www.gongbans.com.
