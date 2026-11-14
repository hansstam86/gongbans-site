# UVB Lamp Checker — Founder Start Pack

> A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail, and the only real meters cost €300–500.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** UVB output of terrarium lamps drops 30–50% long before the lamp looks dim. Keepers replace lamps by calendar (too late or too early). The one trusted meter costs £317–350 in the UK and ~€480+ on the continent; the cheap "UV meters" are junk.
- **Customer:** Reptile, tortoise and parrot keepers in DE, UK, NL, FR (buyers and users); reptile shops and zoos (buyers, as a counter tool and resale item).
- **Product:** A €69–89 pocket meter with a UVA/UVB sensor, lamp-type profiles, a distance guide and a replace/keep verdict; logging per terrarium via BLE; retail counter display.
- **Why now:** The open UV reference pack (sensor + MCU, with Gerbers and BOM) is in the catalogue; UV photodiode sensors are now €2–4; the hobby has moved to "evidence-based husbandry" forums where UV index charts are standard.
- **The ask:** ~€70k (estimate) to 1,000 units in 20 shops, plus a consumer web shop. Route: bootstrap + shop consignment + a small pre-order campaign in the hobby forums.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY (STRONG).** Solarmeter 6.5R, the established incumbent, sells at about $228–280 (up to about €488 in the EU), three to five times the €59–89 target: a genuine price gap. Lamp fade is the real stated problem and the reason this meter category exists. **Main risk:** Solarmeter is trusted in a safety-relevant niche (animal welfare); a cheaper entrant must earn accuracy trust, not just win on price. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 20 reptile shops take 5 units each on consignment, and do they sell through in 6 weeks?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a fake-door landing page that reptile, tortoise and parrot keepers, pet shops and zoos in DE/UK/NL actually visited, with a measured conversion to a waitlist or refundable deposit, plus the interview notes behind it. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Reptile, tortoise and parrot keepers, pet shops and zoos in DE/UK/NL (Germany has the largest reptile-keeping community in Europe).

**The problem as the pack states it:** UVB output of terrarium lamps drops 30–50% long before the lamp looks dim. Keepers replace lamps by calendar (too late or too early). The one trusted meter costs £317–350 in the UK and ~€480+ on the continent; the cheap "UV meters" are junk.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/BeardedDragons** · https://www.reddit.com/r/BeardedDragons/ — the single largest UVB-dependent pet community.
- **r/reptiles** · https://www.reddit.com/r/reptiles/ — reptile keepers.
- **r/leopardgeckos** · https://www.reddit.com/r/leopardgeckos/ — gecko keepers.
- **Reptile Forums (UK)** · https://www.reptileforums.co.uk/ — UK reptile keepers.
- **DGHT (DE)** · https://www.dght.de/ — German herpetological society; regional groups of reptile keepers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (twenty people from the audience line), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€59–89, the pack's estimate), and one button. For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how reptile, tortoise and parrot keepers, pet shops and zoos in DE/UK/NL deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you decide when to replace your UVB bulb, and have you ever had an animal get sick that you later linked to the lamp?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail. On a scale of one to ten, how likely would you be to buy that at €59–89, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: UVB Lamp Checker: would you pay €59–89 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a UVB Lamp Checker: A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €59–89, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Solarmeter 6.5R (PetSmart $250, Chewy, Walmart $280) | UV-index meter for reptile keepers | Incumbent at 3–5× the target price |

**Verdict as researched: LIKELY (STRONG).** Main risk: Solarmeter is trusted in a safety-relevant niche (animal welfare); a cheaper entrant must earn accuracy trust, not just win on price.
<!-- market-competitors:end -->

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

## 4. Start kit

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

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (WPI ATU (distributor kits) and Seeed Studio and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **WPI ATU (distributor kits)** (WPI Group, wpigroup.com) — distributor; 16 boards in the catalogue; files via WPI ATU solution pages (WPG hot channel / tech-highlights / press releases) · https://wpig.wpgholdings.com/tech-highlights/zhcn. Directory entry: Smartphone reference design (MediaTek): MediaTek smartphone + tablet gongban; 1000+ reference designs; billions of devices. The kit files are hosted here; WPI's application unit published them for its distribution customers. Boards used here: [UV Sensor Demo (VEML6075 + LPC824)](/db/uv-sensor-veml6075-lpc824.html) (full open design pack: UV-A/UV-B sensor + MCU). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-UV Sensor](/db/seeed-grove-uv-sensor.html) (alternative UV sensor reference); [Seeed Grove-Sunlight Sensor](/db/seeed-grove-sunlight-sensor.html) (visible/IR reference for lamp-type detection). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack StickC-Plus (K016-P)](/db/m5stack-stickc-plus.html) (display + battery for the prototype). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the WPI ATU (distributor kits) and Seeed Studio and M5Stack websites)

```email
Subject: Sample order and volume pricing — UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P) — for a UVB Lamp Checker

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a UVB Lamp Checker: A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail. The design is built around your UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P).

Could you please send:
1. Price and lead time for [10] sample units of each: UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P).
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
主题：样品订购及批量报价 — UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P) — 用于UVB Lamp Checker

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款UVB Lamp Checker：A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail。产品设计基于贵司的UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P)。

请提供以下信息：
1. 各[10]片样品的单价和交期：UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P)。
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
Subject: PCBA quote from open design files — UVB Lamp Checker, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a UVB Lamp Checker: A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail. The design starts from published open-hardware files (UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — UVB Lamp Checker，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款UVB Lamp Checker：A pocket UV-index meter that tells reptile and bird keepers whether the terrarium UVB lamp still delivers — lamps fade invisibly months before they fail。设计基于已公开的开源硬件文件（UV Sensor Demo (VEML6075 + LPC824), Seeed Grove-UV Sensor, Seeed Grove-Sunlight Sensor, M5Stack StickC-Plus (K016-P)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Buy the reference radiometer and three different UVB lamps; order the UV pack boards (Gerber + BOM) and 3× StickC-Plus.
2. Draft the lamp-profile measurement protocol (distance steps, lamp age, warm-up) — you'll live by this spreadsheet.
3. List 30 reptile shops within driving distance and the dates of the next three reptile fairs; book a table at one.

Want help sourcing or building this? Talk to us via www.gongbans.com.
