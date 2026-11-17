# Beehive Scale (sub-GHz) — Founder Start Pack

> A flat scale under a beehive that reports weight, temperature and air pressure over LoRa, so beekeepers see nectar flow, swarming and winter food without opening the hive.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Beekeepers open hives to find out what a scale could tell them from the kitchen: is the nectar flow on, did the colony just swarm, is there enough winter food? Every opening costs time, stresses the colony and, in winter, can kill it. Apiaries are often kilometres away from home.
- **Customer:** Serious hobby beekeepers (10–50 colonies) and small professionals in DE, AT, CZ, SI and FR. Beekeeping associations buy for teaching apiaries and for the "Trachtbeobachtung" (forage-flow reporting) networks some of them already run. Agri-research institutes buy small fleets.
- **Product:** A low, flat 4-load-cell frame under one "reference hive", with a LoRa radio, temperature, humidity and pressure. It reports every 15–60 minutes over a public or association LoRaWAN gateway. The app shows the daily weight delta, a swarm alert (sudden drop of 1–3 kg in minutes) and a winter-food curve.
- **Why now:** Weight is the single most useful remote hive metric, but commercial hive scales are mostly GSM, cost several hundred euros and carry a SIM subscription. LoRa radios cost a few euros, community LoRaWAN coverage is growing, and one association gateway can cover several apiaries.
- **The ask:** About €120–150k (estimate) to the first 1,000 units, mostly from association group buys (pre-orders), a regional agri/biodiversity grant and one angel from the beekeeping-supply trade.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will a beekeepers' association with 500+ members order a 30-unit group buy? Beekeepers are frugal; price must beat existing scales by half.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Hobby and professional beekeepers (very large hobby base in DE, AT, CZ, SI, FR), beekeeping associations, agri-research.

**The problem as the pack states it:** Beekeepers open hives to find out what a scale could tell them from the kitchen: is the nectar flow on, did the colony just swarm, is there enough winter food? Every opening costs time, stresses the colony and, in winter, can kill it. Apiaries are often kilometres away from home.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/Beekeeping** · https://www.reddit.com/r/Beekeeping/ — beekeepers.
- **Deutscher Imkerbund (DE)** · https://deutscherimkerbund.de/ — German beekeepers' federation; local Imkervereine meet monthly.
- **BBKA, British Beekeepers Association** · https://www.bbka.org.uk/ — UK beekeepers; local associations and the spring convention.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how hobby and professional beekeepers, beekeeping associations, agri-research deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know today what is happening inside a hive without opening it, and when did you last lose a colony or a swarm you wish you had seen coming?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A flat scale under a beehive that reports weight, temperature and air pressure over LoRa so beekeepers see nectar flow, swarming and winter-food levels without opening the hive. On a scale of one to ten, how likely would you be to buy that at €149–199 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Beehive Scale (sub-GHz): would you pay €149–199 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Beehive Scale (sub-GHz): A flat scale under a beehive that reports weight, temperature and air pressure over LoRa so beekeepers see nectar flow, swarming and winter-food levels without opening the hive. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–199 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The first customer is the **ambitious hobby beekeeper with 10–40 colonies on 2–4 sites** in Germany and Austria. They are technical, they are in associations, and they talk to each other on forums and at monthly meetings. They pay and they use it. They are also frugal: a €400 scale for one hive is hard to justify when a colony earns €100–300 a year in honey.

The second customer is the **association** (Imkerverein, local section): it buys 5–30 units for a forage-flow map that all members can see. The board pays, the members use it. This is the lever: one association decision = 20–30 units, and the map makes the product visible.

The third is **research and extension** (bee institutes, agri-universities): small fleets, they care about data export and calibration, they pay more.

### Market size (estimates)
- EU beekeepers: roughly 600k+, with roughly 18–20 M hives (order of magnitude from EU apiculture reporting; check current figures). Germany alone has well over 100k association beekeepers.
- Assume 10% are "monitoring-curious" and would put a scale under 1–2 reference hives: **~60–90k units → TAM ≈ €10–15 M** hardware at €169 average, plus optional association-map subscriptions.
- **SAM** (DE/AT/CZ/SI/FR, LoRaWAN coverage or willing to buy a gateway, ~40%): **~€5 M**.
- **SOM (3 years):** 5% of SAM ≈ 1,500 units ≈ **€250k** hardware. Honest conclusion: this is a niche, nice business, not a venture-scale one unless it becomes the platform for association-wide data.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Commercial GSM/NB-IoT hive scales from German/Austrian/Slovenian makers | €300–600 + SIM/year | Price, subscription, often one hive per modem |
| Open-source hive-monitoring kits (e.g. the BEEP project's base, community TTN builds with HX711 + load cells — see the [TTN beehive thread](https://www.thethingsnetwork.org/forum/t/the-beehive-topic/25599)) | €80–200 in parts + many hours | Needs soldering, calibration and drift fixing; most beekeepers won't |
| Hive-sensor startups focused on pollination services / commercial migratory beekeeping | Subscription, B2B | Aimed at big US/commercial operations, not the European hobby base |
| Bathroom-scale method (lift the back of the hive with a luggage scale) | €15 | Works, but you have to drive there |
| Do nothing: open the hive | Free | Time, colony stress, missed swarms |

**Wedge:** half the price of the GSM scales, **no SIM, no mandatory subscription**, and an **association map** that turns 30 scales into a regional nectar-flow dashboard. Sell to the association, not the individual.

### Product & value proposition
- **Frame:** low (≤40 mm) galvanised or aluminium frame, 4 load cells (one per corner), fits Deutsch Normal, Zander, Dadant and Langstroth footprints via adapters.
- **Electronics:** MCU + HX711-class 24-bit ADC (the M5Stack Weight-I2C unit is the prototype shortcut), HopeRF RFM95W for 868 MHz LoRa(WAN), HopeRF TH09C temperature/humidity, HopeRF HP303B pressure for weather-front context.
- **Power:** 2× AA lithium or a small LiFePO4 + 1 W panel; target 1 year on primaries.
- **Smarts:** temperature-compensated weight (load cells drift with temperature, which is the hard part); daily delta; swarm alert; "winter food below X kg" alert; export to CSV; optional association map.
- **Not legal-for-trade:** weighing for information only. Say so on the box.

**Pricing (estimates):** €169 RRP single scale; association bundle 10 scales + 1 gateway €1,690; research version with data export and calibration certificate €249. Association map: free for the first year, then €2/scale/month or a flat €99/year per association.

### Unit economics (estimates per scale, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM electronics (MCU, 24-bit ADC, RFM95W, TH09C, HP303B, antenna, PCB, batteries) | €16.00 | €12.50 |
| Load cells (4×, 50 kg class) + cabling | €8.00 | €6.00 |
| Frame (steel/alu, galvanised) + footprint adapters | €12.00 | €8.50 |
| Electronics enclosure (IP65) | €2.50 | €1.60 |
| Assembly, calibration & test | €5.00 | €3.50 |
| Packaging | €1.50 | €1.00 |
| Freight + duty to EU (heavy, flat) | €4.50 | €3.50 |
| Certification amortised (~€15k) | €15.00 | €3.00 |
| **Landed cost** | **€64.50** | **€39.60** |
| Net revenue (direct €142 ex-VAT; association/dealer €110) | €142 | €110 |
| **Gross margin** | **€77.50 (55%)** | **€70.40 (64%)** |

The frame is the cost risk: it is heavy to ship. Get a quote from an EU sheet-metal shop before committing to Shenzhen frames.

### Go-to-market
**First 100 customers:**
- **Three associations as launch partners.** Offer a teaching-apiary set at cost in exchange for a talk at their monthly meeting and a presence on the regional map.
- **Beekeeping fairs and regional bee days** (Germany has several large ones each winter/spring). Live demo: a hive body on the scale, put a 2 kg bag on and take it off, phone shows the "swarm" alert.
- **Beekeeping forums and the beekeeping trade press** (German-language forums are very active). One honest long-term test by a respected beekeeper beats any ad.
- **Local LoRaWAN communities** (TTN communities): they love bee projects and will host gateways near apiaries.

**Scale:** beekeeping-supply dealers (catalogue + webshop), association group buys every spring, research tenders.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test with 2–3 associations (group-buy offer); 10 works-like scales on real hives through late winter; temperature drift measured |
| Q2 | Custom PCB + frame; EVT 50 units in 3 association apiaries during the spring flow and swarm season (best possible test window) |
| Q3 | DVT, RED/EMC, IP65; association map v1; pilot 200 units |
| Q4 | 1,000 units ready for the next spring; dealer listing; research version |

**Team:** founder (beekeeper credibility matters, ideally a beekeeper themselves), 1 embedded engineer (load cells + low power + LoRaWAN, part-time OK), 1 web developer part-time for the map. Buy in mechanical design for the frame.

**Funding to the first 1,000 units (estimates):** NRE €45k (PCB + firmware €20k, frame/enclosure tooling €10k, app/map €15k) + certification €15k + 1,000 units landed ~€50k + 9 months lean costs €40k ≈ **€150k**. Minus association pre-orders (300 × €150 deposit-backed ≈ €45k) and a regional biodiversity/agri grant (€20–40k where available) → **~€70–90k** of real funding. Route: bootstrap + pre-orders + grant; a beekeeping-supply dealer as strategic angel.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** load-cell temperature drift (a 0.5 kg day/night swing hides the nectar signal) | Temperature-compensate in firmware using the on-board sensor; calibrate each unit across two temperatures; compare daily deltas at the same hour |
| **Technical:** creep and moisture in cheap load cells over a full year outdoors | Use sealed load cells; potting; a one-year outdoor test in Q1–Q4 before scaling |
| **Market:** beekeepers are frugal; €169 may still be too high | Association bundle pricing; position as "one reference hive per apiary", not one per hive |
| **Regulatory:** "scale" invites legal-metrology questions | State "not legal-for-trade" clearly; never market for selling honey by weight |
| **Supply:** frame cost and freight | Local EU frame supplier; flat-pack design |
| **Coverage:** no LoRaWAN near the apiary | Sell a €150–250 gateway bundle; or point-to-point LoRa to a home base |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF RFM95/96/98(W) LoRa module | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | 868 MHz LoRa/LoRaWAN uplink | PCB footprint/library, datasheet, demo code | MIT (HopeRF GitHub repo) |
| M5Stack Unit Weight-I2C (U180) | https://www.gongbans.com/db/m5stack-unit-weight-i2c.html | Load-cell interface for the works-like prototype | Enclosure/structure files only — main-board electronics not published | Check M5Stack's repo licence; design your own ADC stage for production |
| HopeRF TH09C humidity/temperature sensor | https://www.gongbans.com/db/hoperf-th09c.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sensor/TH09C) | Temperature (for drift compensation) + humidity | Datasheet, demo code | MIT (HopeRF GitHub repo) |
| HopeRF HP303B barometric sensor | https://www.gongbans.com/db/hoperf-hp303b.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sensor/HP303B) | Pressure for weather-front context (rain explains weight changes) | Datasheet | MIT (HopeRF GitHub repo) |

### Block diagram
```
[4x load cells] -> [24-bit bridge ADC (HX711 class)] --+
[TH09C temp/RH] --I2C-----------------------------------+--> [low-power MCU] --SPI--> [RFM95W 868 MHz] ~~LoRaWAN~~> [gateway] -> [network server] -> [app + association map]
[HP303B pressure] --I2C---------------------------------+          |
                                               [2x AA Li or LiFePO4 + 1 W solar]
```
**Engineering gap:** none of the four boards publishes a full schematic you can drop in. You design one small PCB (MCU, bridge ADC with a clean reference, sensors, RFM95W footprint), the frame, and above all the **drift compensation and calibration procedure**. Split: ~35% mechanical/frame, ~40% firmware + calibration, ~25% app/map.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| 4× sealed load cells (50 kg) | €8.00 | Quality varies wildly; buy samples from 3 suppliers and test drift |
| 24-bit bridge ADC (HX711 or better) | €0.60 | Consider a better ADC if drift tests disappoint |
| Low-power MCU | €1.50 | Or a LoRa SoC module to merge MCU + radio |
| RFM95W-868 | €4.50 | HopeRF; pin-compatible alternatives exist |
| TH09C + HP303B | €1.20 | HopeRF |
| Antenna, PCB, passives | €3.00 | External antenna above the hive roof improves range a lot |
| Batteries (2× AA lithium) | €4.00 | Or LiFePO4 + panel (+€5) |
| Frame + adapters | €12.00 | Heaviest cost item; source locally if freight hurts |

### Firmware/software starting point
- **LoRaWAN:** LoRaMac-node (github.com/Lora-net/LoRaMac-node) or, for Arduino prototyping, search "MCCI LoRaWAN LMIC".
- **Network server:** The Things Stack (community edition for pilots) or ChirpStack (open source) for association gateways.
- **Reference project:** the open-source BEEP beekeeping platform and the TTN beehive threads are worth studying for payload formats and lessons on drift (search "BEEP base hive monitoring").
- **Load cells:** search "HX711 library" for your MCU; do your own temperature-compensation curve.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Pitch to 3 associations; **one association commits to a 30-unit group buy** (signed order or deposits). Bench: 4 load cells + ADC reading a 40 kg weight with ±50 g repeatability |
| 3–5 | Works-like | 10 dev-kit scales on real hives; daily weight curves sensible; swarm simulation (remove 2 kg) detected; LoRa uplink from the apiary ≥95% delivered |
| 6–8 | Looks-like + EVT | Custom PCB, IP65 box, frame with footprint adapters; 30 units; drift <200 g over a 15 °C day/night swing after compensation |
| 9–10 | DVT + pre-compliance | RED pre-scan (868 MHz, duty cycle), EMC, IP65 spray test, −20 to +50 °C cycle |
| 11–12 | Pilot batch | 50 units in 3 association apiaries; map live; 80% of pilot users still checking the app weekly after 4 weeks |

### Certification checklist (EU)
- **CE under RED:** EN 300 220-1/-2 (868 MHz SRD, duty cycle ≤1% in the main sub-band), EN 301 489-1/-3 (EMC), EN 62368-1 (safety, battery-powered so light), EN 62479 (exposure). Est. **€8–12k**.
- **RED delegated act / EN 18031:** applies to internet-connected radio equipment; a LoRaWAN node reaches the internet via a gateway, so assume it applies and do a self-assessment (~€2–5k with help).
- **CRA:** reporting duties from 11 Sept 2026, full obligations from 11 Dec 2027. Plan a firmware-update path (local via USB/BLE at minimum), SBOM and a vulnerability-reporting contact.
- **RoHS, REACH, WEEE** registration in each country you sell to; packaging registration (e.g. LUCID in Germany).
- **Battery Regulation (EU) 2023/1542:** user-replaceable batteries, labelling, take-back; UN 38.3 if you ship lithium cells.
- **Legal metrology:** not a legal-for-trade scale; no NAWI conformity needed as long as you never claim it.
- **GDPR:** low risk (hive data). Apiary location + owner contact are personal data: EU hosting, privacy notice, opt-in for the public map (show apiaries coarsely, never exact coordinates — theft of hives is real).
- **Total certification estimate: €12–20k.**

### Validation toolkit
- **Kill question:** Will a beekeepers' association with 500+ members order a 30-unit group buy at a price that beats existing scales by half?
- **Cheapest experiment (~€500):** two works-like scales on real hives for 4 weeks, a one-page offer, a 10-minute slot at three association meetings. Ask for a signed group-buy order with a small deposit.
- **5-question interview:** 1) How often do you drive to your apiaries, and why? 2) When did you last miss a swarm, or lose a colony over winter? 3) Have you looked at hive scales before — what stopped you? 4) Would you trust a shared regional nectar-flow map, and would you share your data? 5) At €169 with no subscription, how many would you buy, and would your association co-fund it?
- **Landing page headline:** "Know what your bees are doing — without opening the hive." Bullets: "See nectar flow and winter food as a daily weight curve." / "Get an alert when a colony swarms." / "No SIM, no subscription. Works with your association's LoRa gateway."
- **Pass threshold:** one 30-unit association order, or 50 individual deposits (€30) within 6 weeks of the first talk.

### First production checklist
- **Samples:** load cells from 3 suppliers, 30-day drift test each; golden sample with calibration record (0/10/40/80 kg).
- **Golden sample:** frame + electronics + firmware version + calibration procedure frozen and signed.
- **DFM review:** frame welding/stamping, corrosion protection, cable glands, condensation (vent membrane), foot pads.
- **MOQ talk:** load cells (often 1k MOQ), frame (local shops: small MOQ but higher unit price), enclosure colour.
- **QC/AQL:** AQL II 1.0/2.5; 100% calibration and LoRa join test; 100% linearity check at 2 weights.
- **Packaging:** flat box, frame and electronics separated, quick-start with QR for onboarding (DevEUI sticker).
- **Incoterms:** FOB Shenzhen for electronics; DAP for EU-made frames; lithium AA shipped as UN 3091/3090 rules apply.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver); [HopeRF TH09C relative humidity and temperature sensor](/db/hoperf-th09c.html) (temperature/humidity sensor); [HopeRF HP303B barometric pressure and temperature sensor](/db/hoperf-hp303b.html) (barometric pressure sensor (weather-front context)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Weight-I2C (U180)](/db/m5stack-unit-weight-i2c.html) (load-cell interface). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180) — for a Beehive Scale (sub-GHz)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Beehive Scale (sub-GHz): A flat scale under a beehive that reports weight, temperature and air pressure over LoRa so beekeepers see nectar flow, swarming and winter-food levels without opening the hive. The design is built around your HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180).
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
主题：样品订购及批量报价 — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180) — 用于Beehive Scale (sub-GHz)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Beehive Scale (sub-GHz)：A flat scale under a beehive that reports weight, temperature and air pressure over LoRa so beekeepers see nectar flow, swarming and winter-food levels without opening the hive。产品设计基于贵司的HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180)。
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
Subject: PCBA quote from open design files — Beehive Scale (sub-GHz), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Beehive Scale (sub-GHz): A flat scale under a beehive that reports weight, temperature and air pressure over LoRa so beekeepers see nectar flow, swarming and winter-food levels without opening the hive. The design starts from published open-hardware files (HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Beehive Scale (sub-GHz)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Beehive Scale (sub-GHz)：A flat scale under a beehive that reports weight, temperature and air pressure over LoRa so beekeepers see nectar flow, swarming and winter-food levels without opening the hive。设计基于已公开的开源硬件文件（HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, HopeRF HP303B barometric pressure and temperature sensor, M5Stack Unit Weight-I2C (U180)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Buy 4 sealed load cells from 2 suppliers, an HX711 board, an RFM95W and an MCU dev board; log weight vs temperature on your balcony for 7 days to see the drift you need to beat.
2. Call the chairs of three local beekeeping associations and ask for a 10-minute slot at their next meeting.
3. Check LoRaWAN coverage maps around those associations' teaching apiaries; if none, price a gateway bundle.

Want help sourcing or building this? Talk to us via www.gongbans.com.
