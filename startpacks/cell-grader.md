# Cell Grader — Founder Start Pack

> A bench tool that measures capacity, internal resistance and self-discharge of salvaged 18650 / 21700 cells and prints a grade label, so repair cafés and pack rebuilders can reuse cells safely.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of perfectly good lithium cells go to the shredder every year because nobody outside a battery plant can grade them cheaply and repeatably. The €25 four-slot "capacity testers" from marketplaces give random internal-resistance numbers; the industrial cyclers start at a few thousand euros and need a lab.
- **Customer:** Battery-pack rebuilders, repair cafés and repair shops, e-waste handlers with a reuse line, and DIY solar-storage builders across the EU. The shop owner or the association pays; the volunteer or technician uses it.
- **Product:** A €249 four-slot cycler: charge, discharge at a defined current, DC and 1 kHz-class IR, a 7-day self-discharge mode, per-slot temperature cut-off, a grade (A/B/C/scrap) printed on a label, CSV export so matched cells go into one pack.
- **Why now:** The EU Battery Regulation (2023/1542) explicitly covers repurposed and remanufactured batteries and pushes reuse; right-to-repair makes pack rebuilding a legal trade; the measurement chips (INA226-class) and open charge-path boards are commodity.
- **The ask:** ~€95k (estimate) to the first 1,000 units; route = deposits from rebuilders and repair-café networks + bootstrap, with a circular-economy grant as the upside.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Dedicated 18650/21700 testers already exist commercially (ZB206+, generic capacity and internal-resistance testers), confirming the technology is real and buildable, but no evidence was found of repair cafés or rebuild shops actively seeking grading tools. **Main risk:** Demand is unverified rather than contradicted; the kill question's fifteen commitments are the test. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 15 repair cafés or rebuilders in one country commit to buy at €249 after a video of a 4-slot grade run?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Repair cafés, e-waste recyclers, battery-pack rebuilders and DIY solar-storage builders across the EU.

**The problem as the pack states it:** Millions of perfectly good lithium cells go to the shredder every year because nobody outside a battery plant can grade them cheaply and repeatably. The €25 four-slot "capacity testers" from marketplaces give random internal-resistance numbers; the industrial cyclers start at a few thousand euros and need a lab.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/18650masterrace** · https://www.reddit.com/r/18650masterrace/ — cell harvesters and pack builders.
- **DIY Solar Power forum** · https://diysolarforum.com/ — home battery and second-life cell builders.
- **Endless Sphere forum** · https://endless-sphere.com/ — e-bike and battery-pack builders.
- **r/batteries** · https://www.reddit.com/r/batteries/ — battery hobbyists.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€199–299, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how repair cafés, e-waste recyclers, battery-pack rebuilders and DIY solar-storage builders across the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about your last batch of harvested cells: how did you grade them, how long did it take, and how many did you throw away later?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A bench tool that measures capacity, internal resistance and self-discharge of salvaged 18650 / 21700 cells and prints a grade label, so repair cafés and pack rebuilders can reuse cells safely. On a scale of one to ten, how likely would you be to buy that at €199–299, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Cell Grader: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Cell Grader: A bench tool that measures capacity, internal resistance and self-discharge of salvaged 18650 / 21700 cells and prints a grade label, so repair cafés and pack rebuilders can reuse cells safely. Before we spend money on tooling I want to find out whether this solves a real problem for repair cafés, e-waste recyclers, battery-pack rebuilders and DIY solar-storage builders across the EU.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €199–299 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

Two questions, no pitch: how do you handle this today, and what would make you say no to the above? Twenty minutes on a call this week, or a reply here, both help.
```

### Reading the signal

| Real signal | False positive |
|---|---|
| A refundable deposit, a signed LOI, a paid pilot, a calendar invite for the prototype | "Sounds cool", "I would totally buy that", likes and upvotes |
| They describe the problem unprompted and in detail, with numbers | They agree with your description of the problem |
| They have already paid for a workaround (a product, a service, their own time) | They have never tried anything and are not bothered |
| Landing-page conversion to deposit or form above the pack's pass mark, from cold traffic | Conversion from friends, family and your own network |
| A named budget and a named decision-maker (B2B) | An enthusiastic user who cannot buy |

### Go / no-go

- **Go to section 3 (business plan) and section 4 (start kit)** when the kill question above is met by your own numbers, you have 15–20 written-up conversations, and at least one real signal from the left column per segment you plan to sell to. Only then does section 5 (Who to contact) apply.
- **Change the idea** when the problem is real but the price, the buyer or the form factor in the pitch is wrong: the interviews will tell you which. Rewrite the pitch and run the fake door again; this is normal and costs a week.
- **Stop** when the kill question fails on honest numbers, or when nobody you talked to has paid for a workaround. Pick another idea on this site; the boards in the start kit are not wasted, only unused.

The full worksheet, with how to define the segment and run the fake door, is in the [playbook → validate demand](/playbook.html#validate).
<!-- validate-demand:end -->

## 3. Business plan

### Problem & customer
Three groups, same tool, different pitch:
1. **Pack rebuilders and battery-repair shops** (power-tool, garden-tool, household-appliance and solar-storage packs; e-waste reuse lines). They test cells all day on hobby chargers and a spreadsheet. They pay for speed, repeatability and a label they can show the customer. Buys 2–5 units.
2. **Repair cafés and repair associations** — ~3,800 Repair Cafés are registered worldwide, 87% of survey responses come from Europe ([4th Global Repair Café Survey](https://cfsd.org.uk/wp-content/uploads/2026/06/4th-Global-Repair-Cafe-Survey-Results.pdf)). They need a safe answer to "is this cell still good?" and a tool that volunteers can't misuse. Buys 1 unit, often grant-funded.
3. **DIY solar-storage builders** — the "powerwall from laptop cells" crowd. Price-sensitive, forum-driven, loud. Great for launch noise; bad for margin.

Who pays vs who uses: the shop owner/association pays; the technician/volunteer uses it. The buyer wants fewer returns and no fires; the user wants fewer button presses.

### Market size (estimates)
- EU + UK: ~2,500 repair cafés and repair associations (estimate from the ~3,800 global figure); ~6,000 battery-repair and power-tool/garden-tool shops that rebuild packs (estimate); ~1,500 e-waste handlers with a reuse line (estimate); ~40,000 active DIY storage builders (estimate from forum sizes). Call it **50k potential seats**.
- **TAM:** 50k × €249 ≈ **€12.5 M** (one-off hardware; labels and electrode consumables add ~10%).
- **SAM:** sites that grade ≥ 50 cells a month and have a budget — 30% of the professional segments plus 10% of DIY → ~6,500 → **€1.6 M**.
- **SOM (3 years):** 20% of SAM → 1,300 units → **€325k**, plus consumables. Small. The upside is the data: a grading standard that insurers and the Battery Regulation "repurposing" operators can cite. Don't pitch this as a big-market company; pitch it as a profitable niche tool with a standards angle.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Marketplace 4-slot "capacity testers" (€25–55, [sigmanortec](https://sigmanortec.ro/en/18650-battery-tester-color-lcd-4-channels-charge-discharge-and-internal-resistance), [Fruugo listings](https://www.fruugo.ca/4-channel-battery-capacity-tester-lcd-display-battery-capacity-tester-18650-mah-battery-internal-resistance-tester/p-448823300)) | Cheap, everywhere | IR readings "spurious" per forum testers ([BLF](https://budgetlightforum.com/t/best-li-ion-capacity-tester/51896?page=2)); no log, no label, no thermal cut-off, no CE file |
| Analysing chargers (Lii-500 class, €20–35) | Good enough for hobbyists | Same: no repeatable IR, no export, no self-discharge test |
| Industrial cyclers / battery analysers (€2,000–20,000) | Accurate | Price, size, needs a lab tech |
| Spreadsheet + multimeter + hobby charger ("do nothing") | The default today | Slow, no record, volunteer-dependent, fires happen |
| DIY ESP32 + INA226 testers | Makers build them | Nobody certifies or maintains them; no label |

**Wedge:** repeatable grade + printed label + CSV, with thermal cut-off per slot and a CE file, at a tenth of the industrial price. "Grading you can show the customer."

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Zbotic cell-grading guide | How-to with existing testers | Technique established |
| Sigma Nortec 18650 tester module; ZB206+ | Commercial testers | Component-level substitutes exist |

**Verdict as researched: LIKELY.** Main risk: Demand is unverified rather than contradicted; the kill question's fifteen commitments are the test.
<!-- market-competitors:end -->

### Product & value proposition
Hardware: desktop box, 4 slots (18650 and 21700 with a spring contact), 5 V/4 A USB-C PD or 12 V certified PSU, per-slot: CC/CV charge to 4.20 V, constant-current discharge 0.5–1.5 A into a resistive load with a fan, INA226-class voltage/current monitoring, NTC per slot, electronic fuse. Firmware: DC-IR (pulse method) and optional AC-IR add-on, capacity in mAh/Wh, self-discharge mode (charge, rest 7 days, re-measure OCV), grade thresholds editable, thermal label printer over USB (common 58 mm thermal printers) or QR on screen, CSV to SD/USB and a desktop page. A later 8-slot "Pro" at €449.

Pricing (estimates): **€249 direct**, **€449 8-slot Pro**, labels €12 per roll; B2B/distribution at 35–40% off. No subscription.

### Unit economics (estimates per unit, ex-VAT, 4-slot)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (MCU, 4× INA226-class, 4× charge/discharge stage, load resistors, fan, 2.8" LCD, PCB) | €46.00 | €36.00 |
| Assembly & test (SMT, per-slot calibration against a reference cell, fan test) | €7.50 | €5.00 |
| Enclosure (ABS 2-shell, 4 slot inserts, heat path; tooling amortised) | €7.00 | €4.20 |
| Packaging (box, USB cable, quick sheet; PSU separate) | €3.00 | €2.20 |
| Freight + duty to EU | €3.50 | €2.00 |
| Certification amortised (~€22k: EMC, LVD/EN 62368-1 energy-hazard review, RoHS) | €22.00 | €4.40 |
| **Landed cost** | **€89.00** | **€53.80** |
| Sell price (direct €249 / distributor €155) | €249 | €155 |
| **Gross margin** | **€160 (64%)** | **€101 (65% at distributor)** |

Margin is fine for a tool. The 8-slot Pro roughly doubles BOM and adds €200 of price.

### Go-to-market
**First 100 customers:** 15 pack rebuilders in one country (kill question) with a video of a 4-slot run; national repair-café networks (Repair Café International's registered list, the Restarters community in the UK, Reparatur-Initiativen in DE); DIY powerwall forums and YouTube channels (send 5 review units); power-tool and garden-tool repair shops via their trade associations; e-waste reuse pilots funded by municipalities.

**Scale channels:** electronics distributors that sell to repair shops (test-equipment category); repair-tool web shops; battery-recycling consortia (they are being pushed to reuse by the regulation and need a grade); vocational schools teaching battery repair.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like 4-slot from the open meter board + INA226 units; grading algorithm validated against a reference cycler; 15 rebuilder commitments at €249 (kill question). |
| Q2 | Custom PCB, tooled case, label printer support; EVT 50; thermal abuse tests; pre-compliance. |
| Q3 | DVT, certification, 300-unit pilot to deposit holders; CSV/pack-matching tool; repair-café network listing. |
| Q4 | 1,000 units; 8-slot Pro EVT; one distributor; publish the grading method openly so it becomes "the" method. |

**Team:** 1 power/analogue engineer (charge/discharge stages, thermal, calibration — full-time), 1 firmware/desktop developer (part-time → full-time), founder for sales and the repair community; a battery-safety consultant for a week to review the energy-hazard design.

**Funding to first 1,000 units (estimates):** NRE €38k (PCB €9k, tooling €12k, firmware/desktop €14k, safety review €3k) + certification €22k + 1,000 units landed ~€67k + 9 months lean overhead €60k ≈ **€187k**; minus deposits (~€30k) and pilot sales (~€62k) ≈ **~€95k**. Route: deposits + bootstrap; circular-economy and repair grants (national and EU-regional) fit this product unusually well; an angel only if you want the 8-slot Pro faster.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** IR measurement repeatability (contact resistance dominates) | 4-wire Kelvin contacts in the slot; gold-plated spring pins; calibrate each slot with a reference; publish ±5% spec |
| **Technical:** heat — 4 cells discharging at 1 A is ~15 W into resistors | Metal heat-spreader, fan, per-slot NTC cut-off at 45 °C cell surface; derate on fan failure |
| **Safety/regulatory:** a cell vents on your bench | Electronic fuse per slot, slot cover, no charging above 4.20 V, "never leave unattended" wording, EN 62368-1 energy-hazard review; liability insurance |
| **Market:** DIY crowd wants it at €99 | Serve them with the open method, not the hardware; sell the tool to shops |
| **Market:** niche is small | Keep NRE small; the Pro and the label/consumable line carry the margin |
| **Supply:** INA226-class allocation; thermal printer vendors change USB protocols | Second-source monitor IC footprint; support ESC/POS printers generically |
| **Licence:** the two OSHWHub designs | Read each project's licence; redraw your own board — they are references, not production files |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| CN3300 4-series pack board (OSHWHub) | https://www.gongbans.com/db/oshwhub-dian-chi-zu-ban-copy-copy.html | Open charge-path reference for a multi-cell board | schematic, pcb | **OSHWHub — licence varies per project; read it** |
| M5Stack Unit INA226-10A (U200) | https://www.gongbans.com/db/m5stack-unit-ina226-10a.html | Precision current/voltage measurement for the works-like | enclosure/structure only; electronics not published | Buy the unit; use the INA226 datasheet for your own board |
| STC8H3K dual-channel V/I/capacity meter (OSHWHub) | https://www.gongbans.com/db/oshwhub-stc8h3k-tssop20-dian-ya-dian-liu-biao-copy-copy-copy.html | Open dual-channel voltage/current/capacity meter with 12864 LCD — the closest thing to a cell tester in the catalogue | schematic, pcb | OSHWHub — check licence |
| M5Stack VAMeter (K136) | https://www.gongbans.com/db/m5stack-vameter.html | Display + measurement reference for a handheld single-slot variant | enclosure/structure only; electronics not published | Buy; documentation reference |

**Board-fact note:** no board in the catalogue is a complete charge/discharge cycler. The discharge stage (load + control) is your own design.

### Block diagram
```
[Slot 1..4: Kelvin contacts + NTC] --+--> [INA226-class V/I monitor per slot]
       |                             |
 [Charge stage per slot: CC/CV 4.20 V, 1 A]   [Discharge stage per slot: MOSFET + 1-4 ohm load, 0.5-1.5 A]
       |                             |
       +----------- [MCU (ESP32-S3 or STM32G4)] -----------+
                        |          |          |
                 [2.8" LCD + 3 buttons] [USB-C: PSU 5 V/4 A PD or 12 V jack] [USB host -> thermal label printer]
                        |
              [microSD CSV] [optional BLE for the desktop page]
              [fan + heat spreader under the loads]
```
**Engineering gap:** the per-slot bidirectional stage (charge + controlled discharge), the Kelvin slot mechanics, the thermal path, the IR pulse method, the grade algorithm, and the label/CSV pipeline. The measurement ICs and charge references exist; the product is the slot and the method.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 module (or STM32G4 + separate BLE later) | €2.60 | Pre-certified module; BLE optional |
| 4× INA226-class V/I monitor | €4.80 | Second-source footprint (other shunt monitors) |
| 4× Li-ion charger stage (CC/CV IC or MCU-controlled buck) | €4.40 | Keep to 4.20 V max; thermal foldback |
| 4× discharge MOSFET + power resistors + heat spreader | €6.00 | Resistors are the hot part; aluminium plate |
| 4× 18650/21700 slot with Kelvin spring pins | €7.00 | **Custom mechanics; sole-source risk — qualify two pin vendors** |
| 2.8" LCD + buttons | €4.50 | |
| Fan 40 mm + NTCs + eFuse parts | €2.70 | |
| PCB 4-layer, passives, USB-C PD, SD | €5.50 | |
| Enclosure ABS 2-shell | €7.00 | **Tooling €10–14k** |
| Certified PSU (USB-C PD 45 W or 12 V 4 A) | €4.00 | Buy certified; don't design mains |

### Firmware/software starting point
- ESP-IDF or Arduino; INA226 driver libraries exist for both (search "INA226 Arduino library"). 
- Charge/discharge control, IR pulse method (ΔV/ΔI over a 10 ms–1 s pulse) and self-discharge scheduling: write yourself; the maths is simple, the edge cases (contact bounce, temperature) are the work.
- Labels: ESC/POS over USB host to common 58 mm thermal printers (search "ESC/POS ESP32 USB host"); QR on screen as the fallback.
- Desktop: a static web page reading CSV for pack matching (sort by capacity and IR, propose groups). No cloud.
- Reference: open hobby cell-tester projects exist on GitHub — search "18650 capacity tester open source" and read a few before you decide on the load stage.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Bench rig (open meter board + 4× INA226 units + resistors) grades 20 cells; video of a 4-slot run; **15 rebuilders/repair cafés in one country commit at €249** (deposits accepted; runs to W6) |
| 3–5 | Works-like | 4-slot rig with Kelvin pins; capacity within ±3% of a reference cycler; IR repeatable within ±5% across 10 re-insertions; thermal cut-off demonstrated |
| 6–8 | Looks-like + EVT | Custom PCB v1, tooled case T1, label printer working; 50 units; abuse tests (shorted slot, reversed cell, cell at 60 °C) pass without smoke |
| 9–10 | DVT + pre-compliance | EMC pre-scan; EN 62368-1 energy-hazard review by a lab; 7-day self-discharge mode validated; CSV/pack-matching page done |
| 11–12 | Pilot batch | 50 units to deposit holders; ≥ 500 cells graded in the field; grade agreement with re-tests ≥ 95% |

### Certification checklist (EU)
- **CE under EMC + LVD** (no radio in the base SKU): EN IEC 61000-6-1/-3, **EN IEC 62368-1** with an energy-source review of the slots (ES/PS classes) and the discharge loads; if the certified PSU stays external, mains stays out of your box. Est. €5–8k EMC, €4–7k safety review. If you add BLE: RED (EN 300 328, EN 301 489) +€4–6k and **EN 18031** if it connects to the internet (it shouldn't — keep it local).
- **RoHS, REACH, WEEE** registration per country; **packaging** registration.
- **Battery regulation:** the device contains no battery; the *cells your customers test* are theirs. Still: wording that the tool is not a certification of a cell for resale, and a safety sheet on handling Li-ion. If you later sell a battery-backed handheld: UN 38.3 + labelling.
- **CRA:** applies to products with digital elements; reporting obligations from 11 Sept 2026, full application 11 Dec 2027 — signed firmware, update path over USB, vulnerability contact.
- **GDPR:** none (no personal data). **Toy directive:** no.
- **Total certification budget estimate: €12–18k** (no radio), €22k with BLE.

### Validation toolkit
- **Kill question:** Do 15 repair cafés or rebuilders in one country commit to buy at €249 after a video of a 4-slot grade run?
- **Cheapest experiment (~€400 + a weekend):** bench rig from the open meter board and 4 INA226 units, 20 salvaged cells, a 3-minute video, a one-page spec sheet with the grade definition; email it to 60 shops/cafés with a €49 refundable deposit link.
- **5-question interview (rebuilder / repair-café lead):** 1) How many cells do you test a month, and with what? 2) What do you do with a cell whose IR you don't trust? 3) Has a reused cell ever come back or failed — what happened? 4) Would a printed grade label change what you can sell or promise? 5) €249 for 4 slots, label and CSV — what would make you say no?
- **Landing page:** headline "Grade salvaged cells like a factory does — on a repair bench." Bullets: "Capacity, internal resistance and 7-day self-discharge, four cells at a time." / "Prints a grade label and exports CSV so matched cells go into one pack." / "Per-slot temperature cut-off and an electronic fuse. €249, no subscription."
- **Pass threshold:** 15 commitments with deposit in one country, or 80 deposits in total within 4 weeks.

### First production checklist
- Samples: 5 golden samples with per-slot calibration records against a reference cell and cycler.
- DFM: slot pin life (≥ 10,000 insertions), heat spreader contact, fan intake, PSU strain relief; test jig with four dummy loads and a reference source.
- MOQ talk: slot pins 2k; power resistors reel; LCD 1k; case 1k; certified PSU 1k.
- QC: AQL II 2.5/4.0; 100% functional test (each slot charges and discharges a dummy, NTC plausibility); 2% full-cycle burn-in.
- Packaging: no lithium in the box; PSU separate; quick sheet with the safety wording.
- Incoterms: FOB Shenzhen; air for the first 100; sea afterwards.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit INA226-10A (U200)](/db/m5stack-unit-ina226-10a.html) (precision current/voltage measurement); [M5Stack VAMeter (K136)](/db/m5stack-vameter.html) (display + measurement reference for the handheld variant). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [CN3300 4串电池组板](/db/oshwhub-dian-chi-zu-ban-copy-copy.html) (open CN3300 4-cell pack board as charge-path reference); [STC8H3K64S2制作12864LCD双路电压电流容量表](/db/oshwhub-stc8h3k-tssop20-dian-ya-dian-liu-biao-copy-copy-copy.html) (open dual-channel voltage/current/capacity meter).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit INA226-10A (U200), M5Stack VAMeter (K136) — for a Cell Grader

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Cell Grader: A bench tool that measures capacity, internal resistance and self-discharge of salvaged 18650 / 21700 cells and prints a grade label, so repair cafés and pack rebuilders can reuse cells safely. The design is built around your M5Stack Unit INA226-10A (U200), M5Stack VAMeter (K136).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit INA226-10A (U200), M5Stack VAMeter (K136).
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
主题：样品订购及批量报价 — M5Stack Unit INA226-10A (U200), M5Stack VAMeter (K136) — 用于Cell Grader

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Cell Grader：A bench tool that measures capacity, internal resistance and self-discharge of salvaged 18650 / 21700 cells and prints a grade label, so repair cafés and pack rebuilders can reuse cells safely。产品设计基于贵司的M5Stack Unit INA226-10A (U200), M5Stack VAMeter (K136)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit INA226-10A (U200), M5Stack VAMeter (K136)。
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
Subject: PCBA quote from open design files — Cell Grader, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Cell Grader: A bench tool that measures capacity, internal resistance and self-discharge of salvaged 18650 / 21700 cells and prints a grade label, so repair cafés and pack rebuilders can reuse cells safely. The design starts from published open-hardware files (CN3300 4串电池组板, STC8H3K64S2制作12864LCD双路电压电流容量表; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Cell Grader，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Cell Grader：A bench tool that measures capacity, internal resistance and self-discharge of salvaged 18650 / 21700 cells and prints a grade label, so repair cafés and pack rebuilders can reuse cells safely。设计基于已公开的开源硬件文件（CN3300 4串电池组板, STC8H3K64S2制作12864LCD双路电压电流容量表；含原理图、PCB和BOM），并做了我们自己的修改。

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

## 6. Next steps (this week)
1. Fab or buy the open meter board, order 4× Unit INA226-10A, 8 power resistors and a fan; have 4 cells cycling on a bench by day 7 and film it.
2. Pull a list of 60 battery-repair shops, power-tool/garden-tool repairers and repair cafés in your country; write the deposit email with the grade definition on one page.
3. Read Regulation (EU) 2023/1542's articles on repurposed and remanufactured batteries ([EUR-Lex consolidated text](https://eur-lex.europa.eu/eli/reg/2023/1542/2025-07-31/eng/pdf)) and note exactly which claims a grader may and may not make.

Want help sourcing or building this? Talk to us via www.gongbans.com.
