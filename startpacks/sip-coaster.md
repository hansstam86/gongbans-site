# Sip Coaster — Founder Start Pack

> A weighing coaster that knows how much was actually drunk from whatever glass or cup stands on it, and glows gently when it has been too long since the last sip — for care homes, offices and anyone who forgets to drink.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Dehydration in care homes is documented by hand on paper fluid charts, twice or three times a day, by staff who are already short of time. The charts are guesses. Offices have the same problem without the paperwork.
- **Customer:** Care-home operators and home-care services (they pay; residents and carers use it). Second tier: wellness retailers and corporate-wellbeing buyers.
- **Product:** A dishwasher-safe-top coaster with a load cell, BLE, a soft RGB ring and wireless charging. Works with the resident's own cup. Logs every sip to a care tablet; nudges with light, not sound.
- **Why now:** Smart cups exist but force residents to use a specific vessel. Load cells, ESP32-C3 BLE and RGB rings are now a few euros. Care regulators in several EU countries treat hydration logging as a quality indicator.
- **The ask:** ~€95k (estimate) to get to 1,000 units, two care-home pilots and a care-tablet app. Route: pre-paid pilots plus a regional innovation grant, angel top-up if the pilots renew.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** A real, funded category: Aquarate / Hydracare is live in UK care homes, Person Centred Software sells weighing "smart cups", and Aquatime was EU-funded. The incumbents are smart cups that measure actual consumption, not coasters, so a more direct solution already exists; a Nottingham Trent student project built almost exactly this coaster. **Main risk:** Must win on cost and simplicity against institutionally adopted smart-cup competitors. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do two care homes run 20 coasters for a month and want to keep them at €59 each?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Care homes and home-care services (hydration logging is a care KPI), offices, wellness retailers.

**The problem as the pack states it:** Dehydration in care homes is documented by hand on paper fluid charts, twice or three times a day, by staff who are already short of time. The charts are guesses. Offices have the same problem without the paperwork.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/AgingParents** · https://www.reddit.com/r/AgingParents/ — adult children caring for parents: the buyer for most elderly-care devices.
- **r/CaregiverSupport** · https://www.reddit.com/r/CaregiverSupport/ — family carers.
- **Carers UK forum** · https://www.carersuk.org/forum/ — family carers in the UK.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€49–69 (care-home bundle 10 + tablet app), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how care homes and home-care services, offices, wellness retailers deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know today whether your parent or resident drank enough, and what happened the last time they did not?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A weighing coaster that knows how much you actually drank from the glass or bottle on it and glows gently when it has been too long since the last sip — for care homes, offices and anyone who forgets to drink. On a scale of one to ten, how likely would you be to buy that at €49–69 (care-home bundle 10 + tablet app), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Sip Coaster: would you pay €49–69 (care-home bundle 10 + tablet app) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Sip Coaster: A weighing coaster that knows how much you actually drank from the glass or bottle on it and glows gently when it has been too long since the last sip — for care homes, offices and anyone who forgets to drink. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €49–69 (care-home bundle 10 + tablet app), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

Either way, two questions: how do you deal with this today, and what would make you say no? Honest answers are worth more to me than deposits.
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
The specific segment is **residential elderly care in DE, NL, UK, Nordics** — homes with 40–120 beds that already use a digital care-record system on tablets. Who pays: the operator's facility manager or quality lead (budget line: care quality / digitalisation). Who uses: the carer who glances at the tablet, and the resident who sees the glow. Home-care services (district nursing) are a second buyer: a coaster on the kitchen table of a client living alone, reported to the next visiting nurse.

Offices and consumers are a nice-to-have; they are not the business. A €59 coaster competes with a €15 hydration app reminder in a consumer's head. In a care home it competes with a paper form and a fine from the inspector.

### Market size (estimates)
- Germany alone has roughly 900k care-home beds (Savills, 2022 report); the Netherlands has the highest long-term-care bed density in the EU (~1,390 per 100k people, Eurostat 2024). Take **~3.5 M long-term care beds across the EU + UK** as a working assumption.
- **TAM (estimate):** 3.5 M beds × one coaster per bed × €59 ≈ **€200 M** one-off hardware, plus a software line.
- **SAM (estimate):** homes that already run a digital care record and are in DE/NL/UK/Nordics — call it 30% of beds → ~1 M beds → **€60 M**.
- **SOM (3-year, estimate):** 0.5% of SAM = 5,000 beds ≈ **€300k hardware + ~€60k/yr software**. That is a small, honest business or a feature that a care-software vendor buys from you.

Sources used: [Savills care-home research](https://en.savills.pt/research_articles/254204/333726-0), [Brussels Times on Eurostat LTC beds](https://www.brusselstimes.com/2227716/eu-hospital-beds-continue-steady-decline-lowest-rates-in-nordic-countries).

### Competition
| Alternative | What it is | Weakness we attack |
|---|---|---|
| Paper fluid charts / "do nothing" | The default in most homes | Inaccurate, labour-heavy, no alerts |
| Smart cups for care (several UK/DK vendors: cup-based systems sold with care-record software, pricing on request) | Instrumented drinking cup, cloud dashboard | Resident must use *their* cup; cups get lost, break, go through dishwashers badly; vendor lock-in to one care-record system |
| Consumer smart bottles / reminder bases (~$125 kit for a US reminder-cup system; ~$29 consumer weighing coasters) | Consumer hydration gadgets | Not fleet-managed, not multi-resident, no carer view |
| Hydration apps / timer reminders | Free | Residents with dementia do not use phones |
| Student/DIY load-cell coaster projects | Demo-grade | Not a product |

**Wedge:** vessel-agnostic (tare on lift-off, works with the resident's favourite mug), fleet of 20–100 coasters per home on one tablet, open API/CSV so any care-record vendor can import, and a light-only nudge that does not add noise to a ward. Sources: [smart coaster for hospital dehydration](https://www.healthcare-management.uk/smart-coaster-tackle-hidden-epidemic-hospital-dehydration), [care-home smart cup via care software](https://personcentredsoftware.com/resources/a-smart-way-to-track-fluid-intake-and-prevent-dehydration), [consumer reminder cup pricing](https://www.epill.com/dropletsmartcup.html).

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Aquarate / Hydracare | Smart cups in UK care homes | Incumbent, more direct measurement |
| Person Centred Software smart cups | Weighing cups tied to care software | Incumbent with the care-record integration |
| Aquatime (AAL Europe) | EU-funded hydration project | Funded interest in the problem |
| Nottingham Trent University coaster project | Student prototype | Concept precedent, not a product |

**Verdict as researched: LIKELY.** Main risk: Must win on cost and simplicity against institutionally adopted smart-cup competitors.
<!-- market-competitors:end -->

### Product & value proposition
Hardware: 95 mm coaster, glass or ceramic top plate (dishwasher-safe), silicone skirt, 1× 5 kg load cell under the plate, ESP32-C3 BLE, 12-LED RGB ring diffused through the skirt, 500 mAh Li-ion, Qi receiver, charging tray that holds 10 coasters. Software: BLE gateway (a cheap tablet or an ESP32 hub) → local server or cloud → per-resident daily total, "no sip in 90 min" nudge, CSV/API export. **Wellness/care-logging only. No medical claims, no dehydration diagnosis.** If you ever say "detects dehydration", MDR applies. Don't.

Pricing (estimates):
- B2B care bundle: **10 coasters + charging tray + hub + 12 months software = €790** (≈€59/coaster + €200 tray/hub/software). Software renewal €1.50/coaster/month.
- Home-care single: €79 incl. 12 months.
- Consumer/office: €69 retail, later, if ever.

### Unit economics (estimates, per coaster, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32-C3 module, load cell + HX711-class ADC, 12 RGB LEDs, Qi RX, charger IC, Li-ion 500 mAh, PCB) | €13.50 | €10.80 |
| Assembly & test (SMT, load-cell calibration, functional test) | €3.20 | €2.30 |
| Enclosure (glass top, PC body, silicone skirt, tooling amortised) | €4.80 | €3.10 |
| Packaging (bundle of 10 shares a box) | €0.90 | €0.60 |
| Freight + duty to EU (air at 1k, sea at 5k; duty ~0–3.7%) | €2.10 | €1.20 |
| Certification amortised (~€22k total: RED, EMC, 62368-1, UN38.3, EN 18031) | €22.00 | €4.40 |
| **Landed cost** | **€46.50** | **€22.40** |
| Sell price to care home (bundle-equivalent) | €59 | €59 |
| Channel margin (direct at 1k; 20% to care-tech resellers at 5k) | €0 | €11.80 |
| **Gross margin** | **€12.50 (21%)** | **€24.80 (42%)** |

At 1k units the hardware barely pays; the business is the software line (€18/coaster/year) and the charging tray/hub (~€120 margin per 10-pack). Don't kid yourself: below 5k units, certification kills the hardware margin. Build the certification cost into the pilot price.

### Go-to-market
**First 100 customers (really: first 10 homes = ~500 coasters):**
1. Two paid pilots with mid-size operators (20 coasters each, €1,500 per pilot, 3 months). Find them via national care-innovation programmes (NL: Zorginnovatie/regional care labs; DE: Pflegeinnovationszentren; UK: care-tech accelerators run with the national care regulator).
2. Care-record software vendors: offer a free integration. They have the install base; you have a sensor. Two or three of these will give you 100 homes faster than you can sell direct.
3. Trade fairs: ALTENPFLEGE (DE), Zorg & ICT (NL), Care Show (UK). One stand a year is enough.

**Scale channels:** care-tech distributors and the software vendors' marketplaces; later a consumer SKU via wellness e-commerce.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill-question test (20 coasters, 2 homes, 1 month). Works-like on M5Stack parts. Tablet web app v0. Decide go/no-go. |
| Q2 | Custom PCB, enclosure tooling (soft tool), EVT 50 units, pre-compliance. Second pilot pair. |
| Q3 | DVT, full CE/RED/EN 18031 testing, pilot batch 300 units for 6 homes. First software renewals. |
| Q4 | Production 1,000 units, 2 reseller/software partners signed, care fair presence. |

**Team:** 1 embedded engineer (ESP32 + load-cell firmware, full-time), 1 web/app developer (part-time → full-time at Q3), 1 founder doing care-home sales and ops. Industrial design and compliance bought in.

**Funding to first 1,000 units (estimates):** NRE €38k (PCB spins €8k, enclosure soft tooling €12k, firmware/app contractors €18k) + certification €22k + first 1,000 units landed ~€30k (at ~€30/unit before amortisation, part paid from pilots) + 9 months of lean salaries/overheads €60k ≈ **€150k** gross; minus pilot and pre-order income (~€55k) = **~€95k** to raise. Route: pre-paid pilots + regional innovation voucher/grant (care digitalisation grants exist in DE/NL) + one angel from the care sector. Don't take VC for this; it is too small for them and the dilution isn't worth it.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** load-cell drift with temperature, wet tables and dishwasher cycles; false "sip" from the cup being wiped | Tare on every lift-off; ignore events < 5 g; temperature-compensate; the glass top is the only part that sees the dishwasher |
| **Market:** carers don't look at the tablet; coasters go into the dishwasher whole | Light nudge on the coaster itself (doesn't need the tablet); IP67 body, survive one dishwasher cycle as a design target |
| **Regulatory:** per-resident intake logs are health-related personal data under GDPR Art. 9 | Local-first storage, pseudonymous IDs on the device, DPA template for operators; no cloud by default |
| **Supply:** Qi receiver coils and load cells are commodity but the glass top is a custom part | Dual-source the glass; keep a printed-PC top as fallback |
| **Scope creep:** someone asks for "dehydration risk score" | Say no. That is a medical device. |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit Mini Scales (U177) | https://www.gongbans.com/db/m5stack-unit-mini-scales.html | Load-cell + ADC reference; proves the weighing resolution you need | enclosure/structure only | Buy the unit for prototypes; electronics not published — you design your own board later |
| M5Stack Unit Weight-I2C (U180) | https://www.gongbans.com/db/m5stack-unit-weight-i2c.html | I2C weight interface for your own load cell | enclosure/structure only | Same as above |
| M5Stack Stamp-C3 (C056-B) | https://www.gongbans.com/db/m5stack-stamp-c3.html | ESP32-C3 BLE/WiFi MCU; the compute | pcb | Altium PCB source published by M5Stack; check their repo licence before copying into a commercial board |
| M5Stack Unit RGB (U003) | https://www.gongbans.com/db/m5stack-unit-rgb.html | Addressable RGB reference for the nudge ring | enclosure/structure only | Buy for prototype; trivial to redesign |

### Block diagram
```
[Glass top] -> [5 kg load cell] -> [24-bit ADC] -> [ESP32-C3] -> BLE -> [Hub/tablet] -> [local server / cloud]
                                                     |  \-> [12x RGB ring]
[Qi RX coil] -> [Li-ion charger] -> [500 mAh cell] ---+
```
**Engineering gap:** nothing in the catalogue combines weighing, Qi charging and sealed construction. The work is (1) a sealed, cleanable mechanical stack where the load cell sees the cup but not the seal, (2) sip-detection firmware robust to lift/tare/wipe, (3) a fleet gateway and care-tablet web app. Hardware is easy; the sip-event algorithm and the mechanical seal are the real engineering.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-C3 module (e.g. ESP32-C3-MINI-1) | €1.90 | Multi-source, RED pre-certified module |
| 5 kg single-point load cell | €1.80 | Commodity; qualify two suppliers |
| 24-bit load-cell ADC (HX711-class) | €0.45 | Many clones; pick one with a datasheet you trust |
| 12× RGB addressable LEDs | €0.90 | Commodity |
| Qi receiver coil + RX IC | €2.40 | Qi certification of the *charger* side is extra if you claim "Qi" — call it "wireless charging" |
| Li-ion 500 mAh pouch/cylindrical with PCM | €1.60 | Use a cell with UN 38.3 report; **long-lead for custom pouch** |
| Charger + 3.3 V regulator | €0.60 | |
| PCB 2-layer | €0.80 | |
| Glass top + silicone skirt + PC body | €4.80 | **Custom tooling €8–12k**; glass is the long-lead item |
| 10-slot charging tray (per coaster share) | €2.50 | Separate product; USB-C PD input |

### Firmware/software starting point
- ESP-IDF or Arduino-ESP32 for the C3; NimBLE for BLE GATT.
- M5Stack publishes Arduino libraries for its Units (search "M5Unit-Scales" / "M5Unit-Weight"); use them for the works-like phase only.
- HX711 Arduino libraries exist in many forms (search "HX711 Arduino library").
- Hub: an ESP32 BLE-to-MQTT gateway or a cheap Android tablet; Home Assistant is a fine pilot dashboard. For the care app: search — write your own, it's a table and a traffic light.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 20 coasters built from Stamp-C3 + Mini Scales + Unit RGB in a 3D-printed body; two care homes run them for a month (overlaps W3–6). Kill question: do both homes want to **keep them at €59 each** at the end? |
| 3–5 | Works-like | Sip-detection algorithm hits >90% agreement with a manually logged test set; BLE fleet of 20 coasters reports to one hub; 7-day battery |
| 6–8 | Looks-like + EVT | Custom PCB v1, soft-tooled body, glass top; 30 units; survives 10 dishwasher cycles of the top plate and a 1 m drop; EMC pre-scan clean |
| 9–10 | DVT + pre-compliance | 50 units; RED/EMC pre-compliance passed; UN 38.3 report from cell vendor; EN 18031 self-assessment documented; GDPR DPIA drafted |
| 11–12 | Pilot batch | 30–50 units in 3 homes with the care-tablet app; renewal intent ≥2 of 3 homes; ≤5% field failures |

### Certification checklist (EU)
- **CE under RED** (BLE): EN 300 328, EN 301 489-1/-17, EN 62311 exposure; **EN IEC 62368-1** safety; **EN 18031-1/-2** (RED delegated act, in force since 1 Aug 2025 — applies because it is internet-connected via the hub and processes personal data; -2 for personal-data protection). Est. test cost: €6–9k RED/EMC + €3–5k safety + €8–15k EN 18031 (notified body likely needed where the standard's conditions aren't met).
- **RoHS, REACH (SVHC), WEEE** registration per country (producer register, ~€1–3k/yr admin).
- **Battery Regulation (EU) 2023/1542**: labelling, removability design requirement for portable batteries from 2027 — design the cell to be removable by a technician. **UN 38.3** for the cell/pack (~€2–3k if not already covered).
- **CRA:** reporting obligations from 11 Sept 2026; full conformity from 11 Dec 2027. Plan secure boot, signed OTA, vulnerability handling, SBOM now.
- **GDPR:** per-resident intake logs = health-related data (Art. 9). You are a processor; the home is the controller. DPA, DPIA, local storage option.
- Not a medical device if you stay on "hydration logging and reminders". No toy directive. No food-contact claim needed for the coaster (the cup touches the food, not you) — but use a food-grade silicone anyway, buyers ask.
- **Total certification budget estimate: €20–30k.**

### Validation toolkit
- **Kill question:** Do two care homes run 20 coasters for a month and want to keep them at €59 each?
- **Cheapest experiment (~€1,200):** 20 Stamp-C3 + Mini Scales + Unit RGB builds in printed bodies, USB charging, a Google Sheet as the dashboard. Four weeks. If carers stop charging them in week 2, you have your answer.
- **5-question interview (facility/quality manager):** 1) How do you log fluid intake today and how long does it take per resident per day? 2) When did a fluid chart last cause a problem (inspection, hospital admission)? 3) Would residents accept a different cup? Would staff? 4) Which care-record software do you use, and who decides on add-ons? 5) If this cost €59 per resident plus €1.50 a month, who signs and what would stop them?
- **Landing page:** headline "Fluid charts that fill themselves in." Bullets: "Works with any cup — residents keep their own mug." / "A soft glow reminds, no alarms on the ward." / "Daily totals on your care tablet, exportable to your care record."
- **Pass threshold:** 2 pilot homes pre-pay €1,500 each, or 5 homes leave a €300 deposit for a 10-pack, within 6 weeks.

### First production checklist
- Samples: 5 golden samples signed off (weighing accuracy ±2 g, glow colour, seal), one kept by you, one by the factory.
- DFM review with the EMS before the production PCB order; load-cell mounting torque spec on the drawing.
- MOQ talk: glass top MOQ is usually 1k–3k; negotiate 1k with a price step at 5k. Cells: MOQ 1k.
- QC: AQL II, 2.5 major / 4.0 minor; 100% functional test incl. a calibration weight; 5% sample dishwasher test of tops.
- Packaging: 10-pack with tray in one carton, drop-test ISTA 1A.
- Incoterms: FOB Shenzhen for the first batch (you control freight and learn the duty codes); DDP only once volumes justify a forwarder contract.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Mini Scales (U177)](/db/m5stack-unit-mini-scales.html) (load-cell weighing reference); [M5Stack Unit Weight-I2C (U180)](/db/m5stack-unit-weight-i2c.html) (alternative weight sensor interface); [M5Stack Stamp-C3 (C056-B)](/db/m5stack-stamp-c3.html) (BLE/WiFi MCU); [M5Stack Unit RGB (U003)](/db/m5stack-unit-rgb.html) (gentle reminder light ring). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003) — for a Sip Coaster

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Sip Coaster: A weighing coaster that knows how much you actually drank from the glass or bottle on it and glows gently when it has been too long since the last sip — for care homes, offices and anyone who forgets to drink. The design is built around your M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003).
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
主题：样品订购及批量报价 — M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003) — 用于Sip Coaster

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sip Coaster：A weighing coaster that knows how much you actually drank from the glass or bottle on it and glows gently when it has been too long since the last sip — for care homes, offices and anyone who forgets to drink。产品设计基于贵司的M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003)。
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
Subject: PCBA quote from open design files — Sip Coaster, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Sip Coaster: A weighing coaster that knows how much you actually drank from the glass or bottle on it and glows gently when it has been too long since the last sip — for care homes, offices and anyone who forgets to drink. The design starts from published open-hardware files (M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Sip Coaster，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sip Coaster：A weighing coaster that knows how much you actually drank from the glass or bottle on it and glows gently when it has been too long since the last sip — for care homes, offices and anyone who forgets to drink。设计基于已公开的开源硬件文件（M5Stack Unit Mini Scales (U177), M5Stack Unit Weight-I2C (U180), M5Stack Stamp-C3 (C056-B), M5Stack Unit RGB (U003)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 20× Stamp-C3, Unit Mini Scales and Unit RGB and print 20 bodies; have the works-like running by day 10.
2. List 10 care operators in your region that run a digital care record and write the one-page pilot offer (€1,500, 20 coasters, 3 months, exit interview). Call the quality lead, not the IT department.
3. Write the one-page GDPR/DPIA note now; it will be the first thing a quality manager asks for.

Want help sourcing or building this? Talk to us via www.gongbans.com.
