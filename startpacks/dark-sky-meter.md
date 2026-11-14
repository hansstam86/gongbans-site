# Dark-Sky Meter — Founder Start Pack

> A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Measuring sky brightness is the entry ticket to every dark-sky programme and to enforcing new lighting rules, and the only instruments in use are two small-volume meters at €200–290 each; a club or a municipality that wants ten measurement points does not buy ten.
- **Customer:** Astronomy clubs (hundreds across DE/FR/UK/NL), municipalities and nature parks applying for DarkSky certification or reporting under national light-pollution rules, ecologists and university departments. The club treasurer or the municipal environment officer pays.
- **Product:** A handheld meter with a narrow-field light sensor, a mag/arcsec² readout, logging to SD and phone, and a fixed LoRaWAN post variant for continuous monitoring; each unit ships with a transfer calibration against a reference meter. Target price €79–99 (estimate).
- **Why now:** Light-pollution rules and DarkSky certifications now ask for measured sky brightness, the two meters everyone uses (Unihedron SQM-L, TESS-W) cost €200–290, and the sensor inside them is a €3 part the catalogue carries on three boards.
- **The ask:** ~€40–55k to certification and a first 1,000 units (estimate), ideally a third from club pre-orders and one municipal pilot.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Unihedron SQM-L ($198–290) and TESS-W (about €275 assembled) confirm a real 2.5–3× price gap. TESS-W is already a finished open-hardware product at a similar price to the SQM-L, so the wedge is price and simplicity, not novelty. **Main risk:** A finished open product exists; the handheld form, the calibration certificate and the price must carry the pitch. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 10 astronomy clubs or 3 municipal dark-sky projects pre-order at €89 after a side-by-side reading against a Unihedron SQM-L? Pass = 10 deposits or 3 purchase orders in 6 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Astronomy clubs and societies; municipalities and nature parks pursuing DarkSky certification or complying with light-pollution rules (France's 2018 decree, Slovenia, Croatia); ecologists studying light at night.

**The problem as the pack states it:** Measuring sky brightness is the entry ticket to every dark-sky programme and to enforcing new lighting rules, and the only instruments in use are two small-volume meters at €200–290 each; a club or a municipality that wants ten measurement points does not buy ten.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/Astronomy** · https://www.reddit.com/r/Astronomy/ — amateur astronomers; light pollution is a constant topic.
- **VdS, Vereinigung der Sternfreunde (DE)** · https://www.vds-astro.de/ — German amateur-astronomy federation with a light-pollution working group.
- **DarkSky International** · https://darksky.org/ — the certification body and its European chapters; municipalities and parks come through here.
- **iNaturalist forum** · https://forum.inaturalist.org/ — citizen scientists and ecologists.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79–99, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how astronomy clubs and societies deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How did you last measure the sky at your observing site or in your municipality, with what, and who asked for the number?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today. On a scale of one to ten, how likely would you be to buy that at €79–99, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Dark-Sky Meter: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Dark-Sky Meter: A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today. Before we spend money on tooling I want to find out whether this solves a real problem for astronomy clubs and societies.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €79–99 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

Sky-quality meters read the brightness of the night sky in magnitudes per square arcsecond; DarkSky International's certifications, France's 2018 lighting decree and the Slovenian and Croatian laws all lean on such measurements. The two meters in actual use, Unihedron's SQM-L and the open TESS-W, cost €200–290, which is why most clubs own one and most municipalities own none. Continuous monitoring, the thing that shows whether a lighting change worked, is rarer still.

**Who pays, B2B/B2G (primary):** municipalities and parks with a dark-sky project (a certification needs a baseline and a yearly re-measurement across many points), universities and ecological consultancies. **Who pays, B2C:** amateur astronomers and clubs buying one or several. The user is often a volunteer with a clipboard at 1 a.m.; the device must be one-button.

### Market size (estimates — check)

- **TAM:** amateur astronomy clubs in the EU (estimate: 3,000–5,000) plus ~200 dark-sky places and candidate municipalities worldwide; one to ten meters each. Theoretical €5–10M.
- **SAM:** clubs and municipalities in DE/FR/UK/NL/AT/CH active in light-pollution work: estimate 1,500 organisations, 3 meters each → €400k.
- **SOM (3 yrs):** 2,000–4,000 units across clubs, a dozen municipal networks and the LoRaWAN post variant. Year-1: 500–1,000 units.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Unihedron SQM-L | The reference handheld; $198–290 (research, Nov 2026) | Same sensor class at a third of the price; logging and phone export built in |
| TESS-W (Stars4All) | Finished open-hardware photometer, about €275 assembled; fixed station with WiFi | A finished product already exists, so the wedge is price and the handheld form, not novelty |
| Smartphone apps (Dark Sky Meter, Loss of the Night) | Camera-based estimates | Not accepted as a measurement by certification bodies |
| DIY TSL2591 / TSL2561 builds | Forum and GitHub projects | Need a case, a lens, a calibration and a battery; our customer wants to buy that |

**Wedge:** price and one-button simplicity against a single-vendor legacy meter, with the calibration certificate that makes a club or a council trust the number. Not novelty: TESS-W already proves the open approach.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Unihedron SQM-L | $198–290 handheld | Legacy reference meter, 2.5–3× the target |
| TESS-W (Stars4All) | About €275 assembled, open hardware, fixed station | Finished open product already exists |
| France 2018 light-pollution decree (overview) | Regulation requiring lighting controls and measurements | Institutional pull |

**Verdict as researched: LIKELY.** Main risk: A finished open product exists; the handheld form, the calibration certificate and the price must carry the pitch.
<!-- market-competitors:end -->

### Product & value proposition

- Narrow-field (about 20°) sensor behind a lens; readout in mag/arcsec², with Bortle class shown for non-experts.
- Long integration at dark sites (10–30 s) with a clear "measuring" indicator; result logged with time and, if the phone is connected, position.
- Transfer calibration per unit against a reference SQM-L, certificate in the box; yearly re-calibration service as a small recurring line.
- Post variant: same sensor in an IP65 tube with a Stamp C6LoRa, solar-charged, reporting every 10 minutes over LoRaWAN or TTN.
- Open data format; CSV export; no account needed.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €12–18) | 15.0 | 12.0 |
| PCBA assembly + test | 2.5 | 1.6 |
| Enclosure / mechanics (tooling amortised separately) | 4.0 | 2.8 |
| Packaging, cable, leaflet | 2.0 | 1.5 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 2.0 | 1.0 |
| Certification amortised (€10k, estimate) | 10.0 | 2.0 |
| **Landed cost** | **35.5** | **20.9** |
| Channel cost (direct + club resellers, ~€7 per unit) | 7.0 | 7.0 |
| Net price received (€89 incl. 19% VAT → €74.8 ex VAT) | 74.8 | 74.8 |
| **Gross margin per unit** | **€32.3 (43%)** | **€46.9 (63%)** |

Lesson: the first thousand pays for certification and the calibration jig; margin appears at the second run. The calibration service is the recurring line that makes the business more than a one-off gadget.

### Go-to-market

**First 100 customers:**

1. Ten astronomy clubs met through their national federation newsletters (VdS in Germany, SAF in France, FAS in the UK), each buying one meter and running a side-by-side with their SQM-L.
2. Two municipal dark-sky candidates found via DarkSky International's European chapters, buying a ten-point network.
3. University ecology departments studying artificial light at night.

**Scale channels:** astronomy retailers (Teleskop-Service, Astroshop), the DarkSky community, environmental consultancies.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations; works-like prototype on the Digital Light Sensor + AtomS3; calibration method agreed with one club that owns an SQM-L. |
| Q2 | Custom PCB with the lens barrel; EVT 20; pre-compliance; post variant on Stamp C6LoRa. |
| Q3 | DVT; certification; 300-unit run; club pre-orders shipped; first municipal network installed. |
| Q4 | 1,000 units; retailer listing; calibration service live. |

**Team:** one embedded engineer (optics and calibration experience helps), one founder for clubs and councils; mechanical design and the lens barrel bought in.

**Funding to first production (estimates):** NRE €18k (PCB spins, lens tooling, calibration rig) + certification €8–10k + first 1,000 units landed ~€25k ≈ €50–55k; minus pre-orders ~€15k ≈ €35–40k.

### Top risks

| Risk | Mitigation |
|---|---|
| Sensitivity at very dark skies (above 21 mag/arcsec²) needs long integration and a low-noise sensor | Characterise the TSL2561 and TSL2591 early; state the measuring range on the box; the post variant integrates longer |
| Clubs trust the SQM-L and nothing else | Side-by-side data published per unit; calibration certificate; invite a federation to test |
| Municipal sales cycles are slow | Sell to clubs first; councils follow the club's data |
| TESS-W is open and good | Compete on the handheld form, price and the service; do not pretend it does not exist |

## 4. Start kit

### Boards to start from

- [Seeed Grove-Digital Light Sensor](https://www.gongbans.com/db/seeed-grove-digital-light-sensor.html) — TSL2561 digital light sensor: the measuring front end (open files: schematic)
- [M5Stack Unit DLight (U136)](https://www.gongbans.com/db/m5stack-unit-dlight.html) — alternative ambient-light unit for a quick first prototype (design files published for the module; electronics not open)
- [DFRobot SEN0097](https://www.gongbans.com/db/dfrobot-sen0097.html) — BH1750 light sensor, second-source option (open files: schematic)
- [M5Stack AtomS3-Lite (C124)](https://www.gongbans.com/db/m5stack-atoms3-lite.html) — ESP32-S3 core with display-less button for the handheld (design files published for the module; electronics not open)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — LoRaWAN variant for a fixed monitoring post (open files: pcb,schematic)
- [M5Stack Unit RTC (U126)](https://www.gongbans.com/db/m5stack-unit-rtc.html) — timestamped logging without network (design files published for the module; electronics not open)

The Seeed Grove Digital Light Sensor publishes its schematic; the M5Stack DLight unit and the DFRobot board are second sources for the same job. The Stamp C6LoRa (open PCB + schematic) is the core of the post variant.

### Block diagram

```
  [lens + baffle] -> [TSL2561 / BH1750 light sensor]
                           |  I2C
  [button] -> [ESP32-S3 AtomS3 core] -> [OLED / phone BLE]
                           |
                  [RTC] [microSD] [Li-ion + USB-C charge]
  post variant: [sensor] -> [Stamp C6LoRa] -> LoRaWAN / TTN,  [solar + cell]
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| TSL2561 / BH1750 sensor board | 2.0 | or TSL2591 for more dark-sky range |
| ESP32-S3 module | 2.5 | pre-certified |
| Lens + baffle tube | 2.0 | stock plastic lens; tolerance matters |
| Li-ion cell + charger + USB-C | 3.0 | handheld variant |
| RTC + microSD | 1.5 |  |
| Enclosure | 3.5 | injection moulded at volume; printed for EVT |
| PCB + passives | 1.5 |  |

### Firmware/software starting point

- ESP-IDF or Arduino; integration-time control, dark-current subtraction, conversion to mag/arcsec² with per-unit calibration constants stored in NVS.
- BLE to a small web app (Web Bluetooth) for logging and export; no account.
- Post variant: LoRaWAN uplink every 10 minutes, Cayenne LPP, TTN decoder published.

### 12-week build plan

1. Interviews and fake door live
2. Sensor characterisation against an SQM-L at a dark site
3. Prototype on AtomS3 + Grove sensor
4. Lens barrel and baffle design
5. Custom PCB v1
6. Calibration rig and procedure
7. EVT 20 built
8. Field test with two clubs
9. Enclosure tooling decision
10. DVT build in enclosure
11. Pre-compliance EMC/radio
12. Certification submission; pre-order shipping plan

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 10 astronomy clubs or 3 municipal dark-sky projects pre-order at €89 after a side-by-side reading against a Unihedron SQM-L? Pass = 10 deposits or 3 purchase orders in 6 weeks.
- **Cheapest experiment:** Borrow a club's SQM-L, build one prototype, publish 30 nights of side-by-side readings; ask ten clubs whether that data would make them buy at €89.
- **5-question interview:** 1) How many measurements did you take last year and with what? 2) What did they cost you, including the meter? 3) Who asks you for the numbers (council, certification, your own records)? 4) What would make you distrust a cheaper meter? 5) At €89 with a calibration certificate, how many would you buy?
- **Landing page:** headline "Measure your sky. €89, calibrated, logs to your phone." Bullets: side-by-side with SQM-L; Bortle class and mag/arcsec²; LoRaWAN post for councils. Button: refundable €20 deposit.
- **Pass threshold:** 10 club deposits or 3 municipal purchase orders within 6 weeks.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Seeed Studio and M5Stack and DFRobot).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Digital Light Sensor](/db/seeed-grove-digital-light-sensor.html) (TSL2561 digital light sensor: the measuring front end). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit DLight (U136)](/db/m5stack-unit-dlight.html) (alternative ambient-light unit for a quick first prototype); [M5Stack AtomS3-Lite (C124)](/db/m5stack-atoms3-lite.html) (ESP32-S3 core with display-less button for the handheld); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (LoRaWAN variant for a fixed monitoring post); [M5Stack Unit RTC (U126)](/db/m5stack-unit-rtc.html) (timestamped logging without network). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **DFRobot** — community / maker brand; 250 boards in the catalogue; files via DFRobot wiki catalog · https://wiki.dfrobot.com/. Boards used here: [DFRobot SEN0097](/db/dfrobot-sen0097.html) (BH1750 light sensor, second-source option). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack and DFRobot websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097 — for a Dark-Sky Meter

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Dark-Sky Meter: A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today. The design is built around your Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097.

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097.
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
主题：样品订购及批量报价 — Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097 — 用于Dark-Sky Meter

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Dark-Sky Meter：A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today。产品设计基于贵司的Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097。
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
Subject: PCBA quote from open design files — Dark-Sky Meter, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Dark-Sky Meter: A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today. The design starts from published open-hardware files (Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Dark-Sky Meter，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Dark-Sky Meter：A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today。设计基于已公开的开源硬件文件（Seeed Grove-Digital Light Sensor, M5Stack Unit DLight (U136), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit RTC (U126), DFRobot SEN0097；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Run section 2 (validate demand): book the first ten conversations and put the fake door up before touching a board.
2. Order the sample boards in the start kit (three of each) and build the works-like prototype on the desk.
3. Send e-mail A to the board publisher and e-mail B to one PCBA house (section on who to contact) to learn the real numbers behind the estimates above.
