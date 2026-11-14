# Build-a-Radio Workshop Kit — Founder Start Pack

> A no-code, solder-it-yourself MW/SW/FM radio in a laser-cut wooden case for schools, makerspaces and team workshops — it plays music at the end of the afternoon.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Physics teachers must teach waves and modulation; the only kits around are either 1990s-looking plastic (and out of stock) or "smart" kits that hide everything in an MCU. A real analogue radio that the pupil builds and keeps is the classic payoff, and it's missing in a modern, classroom-ready form.
- **Customer:** Secondary-school physics departments (DE/NL/UK first), makerspaces and museum workshops, corporate team-event organisers. The school or the event organiser pays; the 14-year-old uses it.
- **Product:** Through-hole PCB laid out for beginners, numbered 4-language build sheet, laser-cut wooden case, teacher's guide mapped to curriculum topics. €45 ex-VAT per kit in class sets of 15; €49 incl. VAT to consumers.
- **Why now:** Open four-band radio design exists with schematic and PCB; STEM budgets exist; no firmware, no app, no cloud — the fastest idea in the catalogue to a saleable product (6–10 weeks).
- **The ask:** ~€30k to the first 1,000 kits; bootstrap with pre-paid class sets.

## 2. Business plan

### Problem & customer
Every curriculum in Europe covers electromagnetic waves, oscillation and modulation at 14–16. Teachers want a 90-minute to 3-hour practical that ends with something that works and goes home. Existing options: Franzis UKW kits (€24–39, consumer, German-only, often sold out), Elenco AM/FM kits (US$46, 56-page English course, superhet — too hard for a first solder), Velleman/Whadda mini kits (no case, no didactics). Nothing comes as a class set with a teacher's guide, spare-parts bag and a case the pupil is proud of.

Who pays: the physics department head from the Fachschaft budget (typically €500–2,000/year for consumables); the makerspace from course fees (participants pay €30–60 for a Saturday workshop and keep the radio); HR or an agency for team events (€80–150/head, the kit is a small part). Who uses: pupils 14+, adults in workshops.

### Market size (estimates — check them)
- **TAM:** Secondary schools: ~10,000 in Germany with a physics department (Gymnasium, Realschule, Gesamtschule), ~650 in NL, ~4,200 in the UK; plus ~2,000 makerspaces/Fablabs and museum education departments in Europe. If each bought one class set of 15 a year (€675), TAM ≈ 17,000 institutions × €675 ≈ **€11 M/year**. Consumer kit sales on top (Franzis has sold these for 20 years, so the hobby demand is real).
- **SAM:** schools and spaces reached via 3–4 educational distributors and direct in DE/NL/UK: 20% of TAM ≈ **€2.3 M/year**.
- **SOM (year 2):** 300 class sets + 3,000 single kits ≈ 7,500 kits ≈ **€330k revenue**.

### Competition (2 searches)
| Alternative | Price | Weakness |
|---|---|---|
| Franzis UKW-Radio Bausatz (DE) | €24–39 retail | Consumer, single-language, stock issues, no class set/teacher guide |
| Elenco AM/FM-108CK (US) | ~US$46 | Superhet, 56-page English course — too advanced for a first build; import |
| Velleman/Whadda mini FM kits | €15–25 | No case, no didactics |
| Crystal-radio / tin-can DIY from the web | ~€5 | Weak sound, frustrating; teacher does all the prep |
| Do nothing — PhET simulation on a laptop | €0 | No physical payoff, pupils forget it |

**Wedge:** classroom-ready: class set of 15 + spares + 4-language numbered steps + teacher's guide mapped to curricula (DE Lehrplan waves/modulation, NL natuurkunde, UK GCSE Physics P6) + wooden case. Sell to the department, not the pupil.

### Product & value proposition
- **Kit v1 "Classic":** four-band MW/SW/FM receiver derived from the open OSHWHub design; volume pot, tuning pot, band switch; through-hole parts spaced for beginners; 2× AA battery; 57 mm speaker; laser-cut plywood case that doubles as the soldering jig.
- **Kit v2 "FM-only Junior":** FM-only variant for younger groups and shorter sessions (based on the Grove FM receiver circuit).
- **Classroom speaker add-on:** 10 W amp (TDA2030 open board) and a bigger speaker for the "we built a radio station… receiver" demo.
- **Pricing:** class set of 15 + 2 spare boards + parts bag: **€675 ex-VAT (€45/kit)**. Single kit B2C €49 incl. VAT. Workshop pack for makerspaces (30 kits + guide) €1,200. Teacher's guide free as PDF (lead magnet).

### Unit economics (estimates, per kit)
| Item | 1,000 kits | 5,000 kits |
|---|---|---|
| Electronics BOM (PCB, radio IC/transistors, pots, switch, speaker, passives) | €9.50 | €7.20 |
| Kitting (bagging, labelling — no assembly) + QC sample test | €2.00 | €1.30 |
| Wooden case (laser-cut 3 mm ply, 6 parts) | €3.20 | €2.20 |
| Packaging + printed 4-language sheet | €1.80 | €1.10 |
| Freight + duty to EU | €1.50 | €0.80 |
| Certification amortised (€8k) | €8.00 | €1.60 |
| **Landed cost** | **€26.00** | **€14.20** |
| Sell price (class set, direct, ex-VAT) | €45 | €45 |
| Channel: educational distributor takes 40% of €59 list → net €35 | — | €35 |
| **Gross margin direct** | **42%** | **68%** |
| **Gross margin via distributor** | 26% | 59% |

The 1,000-unit margin is thin because certification is amortised over few units; it's a volume game — plan 5,000 as the real target and buy the wooden case in Europe to skip freight on the bulky part.

### Go-to-market
**First 100 customers (≈ 20 class sets + 300 singles):** physics teacher associations and their conferences (DE: MNU/DPG teacher days; NL: NVON; UK: ASE), teacher Facebook/Telegram groups, 5 makerspaces that run Saturday courses (offer the first 30 kits at cost in return for photos and a quote), museum education departments (technology museums run holiday workshops), two YouTube electronics channels for the consumer sale. Give 20 kits to teachers for a lesson trial and collect their worksheet corrections.

**Scale:** educational distributors (the ones that already sell lab equipment), Amazon for singles, corporate team-event agencies (they pay the most and complain the least), licensing the teacher's guide translations to local distributors in FR/IT/PL.

### 12-month plan
- **Q1:** Re-layout the open design through-hole, 20 hand-built prototypes, 3 teacher trials. Gate: 10 teachers/makerspaces order a class set at €45/kit from a one-page offer.
- **Q2:** Receiver test at a lab, first 1,000 kits, teacher's guide v1 in DE/EN/NL/FR, distributor talks.
- **Q3:** FM-only Junior variant, classroom speaker add-on, Amazon listing, first two distributors.
- **Q4:** 5,000-kit run, workshop pack for makerspaces/corporate, decide on FR/IT.

**Team:** one electronics engineer part-time (the design is done — this is DFM and sourcing), one teacher/didactics writer part-time, one founder on sales and ops. Nobody full-time until 3,000 kits.

**Funding to 1,000 kits (estimate):** NRE €12k (re-layout, laser-cut case design, test fixtures, photography) + certification €8k + 1,000 kits × €18 production cost = €18k → **~€38k**, of which pre-paid class sets can cover €13k+. Realistic cash need **~€25–30k**. Bootstrap; this does not need investors.

### Top risks
- **Technical — first-solder failure rate:** if 20% of kits don't play, the teacher never buys again. Mitigation: big pads, polarity marks, a "test before closing the case" step, spare boards in every set, a 10-minute debug card.
- **Market — budget cycles:** schools buy in spring and September. Mitigation: makerspaces and corporate events fill the gap.
- **Regulatory:** the ideas list said EMC/LVD self-declaration; I think a broadcast receiver sold as a product falls under **RED** (receivers are in scope since 2016) — verify with a lab before you print a CE mark. Battery-only, so no LVD. Not a toy if marketed 14+/education — don't put a cartoon on the box.
- **Supply:** the radio IC / discrete set and ferrite rod in the open design may be Chinese commodity parts with no EU distributor. Mitigation: buy 5,000 sets up front (cheap), qualify a second IC.
- **Licence:** OSHWHub projects are often CC BY-NC-SA. Check this project's licence; if non-commercial, re-design the schematic around the same architecture (it's a classic topology) or contact the author for permission.

## 3. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [oshwhub-retro-four-band-radio](https://www.gongbans.com/db/oshwhub-retro-four-band-radio.html) | The whole receiver: no code, volume/tuning pots, band switch, MW/SW/FM | schematic, pcb | OSHWHub — licence varies, often CC BY-NC-SA; check before selling |
| [seeed-grove-fm-receiver](https://www.gongbans.com/db/seeed-grove-fm-receiver.html) | FM-only reference for the Junior variant | schematic | Seeed wiki — check licence |
| [oshwhub-tda2030](https://www.gongbans.com/db/oshwhub-tda2030.html) | 10 W amp for the classroom speaker add-on | schematic, pcb | OSHWHub — check licence |
| [seeed-grove-speaker](https://www.gongbans.com/db/seeed-grove-speaker.html) | Speaker driver reference | schematic | Seeed wiki — check licence |

### Block diagram and engineering gap
```
[Ferrite rod / telescopic antenna] -> [Band switch] -> [Receiver front-end + IF/demod (open design)]
        -> [Volume pot] -> [Audio amp] -> [57 mm speaker]
[2x AA] -> power
Case: 6 laser-cut ply parts, PCB screws into the front panel; the case bottom is the soldering jig.
```
Gap: zero firmware. The work is through-hole re-layout for beginners, part availability in Europe, the case, and the didactics. Expect two PCB spins.

### Starter BOM (per kit, estimates)
| Part | Est. cost | Note |
|---|---|---|
| Radio receiver IC(s)/transistors per open design | €1.60 | Check EU availability; may be China-only commodity — buy ahead |
| PCB 2-layer through-hole, 100×70 mm | €1.20 | Any JLC-class fab |
| Pots ×2 + knobs, band switch | €1.40 | — |
| Ferrite rod + coil, telescopic antenna | €1.10 | Ferrite rod is the long-lead item (6–8 weeks) |
| 57 mm 8 Ω speaker | €0.90 | — |
| Passives, AA holder, wire, screws | €1.80 | — |
| Audio amp IC | €0.50 | — |
| Laser-cut ply case | €3.20 | Source in EU to avoid freight on bulk |
| Printed sheet + bag + box | €1.80 | — |

### Firmware/software starting point
None — that is the point. Software deliverables are documents: build sheet (numbered, photos per step), teacher's guide (waves, modulation, why FM sounds better, antenna length maths), debug card. Use the open schematic as the basis of a "how it works" page.

### 12-week build plan
- **Week 1–2 — validate.** Order the open PCB as-is from the fab (10 pcs), build 5, test reception in a classroom building. Send a one-page offer (€45/kit, class set of 15) to 30 teachers and 10 makerspaces. *Exit:* 10 orders or firm yeses; the radio receives FM indoors.
- **Week 3–5 — works-like.** Through-hole re-layout, bigger pads, test points; 20 kits built by non-engineers (your friends) with a stopwatch. *Exit:* 90% first-time success, median build time <2.5 h.
- **Week 6–8 — looks-like + EVT.** Laser-cut case v2, 4-language sheet, 3 teacher trials with 15 pupils each. *Exit:* teacher says "I'd buy this" and corrects the sheet; failure rate <10%.
- **Week 9–10 — DVT + pre-compliance.** Final PCB, receiver/EMC test at the lab, battery-leak and drop checks. *Exit:* test report in hand.
- **Week 11–12 — pilot batch.** 300 kits kitted, 20 class sets shipped. *Exit:* 20 paid class sets, <5% returns.

### Certification checklist (EU)
- **RED** (receive-only radio equipment is in scope): EN 303 345 series (broadcast sound receivers), EN 301 489-1 (EMC), EN 62368-1 — battery-only so safety is trivial. Self-declaration (Module A) is allowed with harmonised standards. Est. **€4–8k**.
- **RoHS** (supplier declarations), **WEEE** registration in each country you ship to, **REACH** SVHC check (plywood glue, PVC wire).
- **Not internet-connected** → no EN 18031, CRA not applicable (no digital elements with a network).
- **No Li-ion** (AA cells — supply alkaline or let the school supply).
- **Toy Directive:** out of scope if clearly marketed 14+/educational; label "Not a toy. Soldering required. 14+".
- No GDPR.

### Validation toolkit
- **Kill question:** do 10 teachers or makerspaces order a class set at €45/kit from a one-page offer? **Cheapest experiment:** €300 — 10 open PCBs built as-is, a one-pager with photos, 40 emails.
- **5-question interview:** (1) Which practical do you run for waves/modulation today, and what does it cost? (2) How long is your practical slot — 45, 90, 180 minutes? (3) Who approves a €675 purchase and how long does it take? (4) What killed the last kit you tried? (5) Would you pay more for a case the pupil keeps, or less with no case?
- **Landing-page headline:** "Build a real radio in one afternoon — class set, teacher's guide, no code." Bullets: 15 kits + spares, 4 languages · Mapped to the waves & modulation curriculum · It plays music when they're done.
- **Pre-order pass:** 10 class sets (€6,750) or 150 single kits paid within 4 weeks.

### First production checklist
Samples of every part from the chosen distributor (not photos), golden sample kit sealed, DFM on the PCB (pad size for 14-year-olds, silkscreen numbers = sheet numbers), MOQ: 1,000 kitted bags with a 5,000 forecast, QC/AQL on kitting (count and polarity of pre-formed parts; one in 50 built and tested), packaging crush test, EXW/FOB for electronics, local supplier for ply cases, you are the importer and the CE responsible person.

## 4. Next steps (this week)
1. Order 10 of the open four-band PCBs and the parts; build two tonight; check the project's licence on the OSHWHub page.
2. Write the one-page offer and send it to 30 physics teachers and 10 makerspaces.
3. Ask a test lab for a quote for a receive-only RED assessment so the certification line in the economics is a real number.

Want help sourcing or building this? Talk to us via www.gongbans.com.
