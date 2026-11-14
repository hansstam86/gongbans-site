# Vitrine Log — Founder Start Pack

> A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Museums must prove the climate around borrowed and owned objects, lenders ask for continuous records as a loan condition, and the institutional loggers that produce them cost £487–617 each plus annual software, so small museums log with a pen or borrow a logger for the loan.
- **Customer:** Regional, municipal and university museums, archives, historic houses, instrument collections and churches that lend or borrow objects; conservators and registrars specify, the collections budget pays.
- **Product:** A palm-sized logger (T, RH, lux, UV) with two years on a cell, LoRaWAN or BLE readout, calibration certificate, and a report tool that produces the per-object climate PDF a lender's registrar expects; no per-logger licence. Target price €149–199 (estimate).
- **Why now:** Loan agreements routinely require continuous climate records (the UK Government Indemnity Scheme is the citable case, currently under review), institutional loggers cost £487–617 each plus software, and the sensors are catalogue parts.
- **The ask:** ~€45–60k to certification and a first 1,000 loggers (estimate); three museum orders cover a third.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** The UK Government Indemnity Scheme (National Heritage Act 1980) genuinely requires RH, temperature and light monitoring for loan periods, a citable requirement, and Testo 160 THL (about £487–617) confirms a 2–3× price gap. The specific GIS environmental-conditions rule is reported under active review (suspended through at least March 2023, status unclear). **Main risk:** Verify current GIS requirements before leaning on them as a hard mandate; lenders' own loan conditions carry the demand regardless. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 regional museums buy 10 loggers each at €169 after one loan cycle with the PDF report? Pass = 3 orders in 10 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Regional and university museums, archives, instrument and art collections, churches holding artworks; conservators and registrars; the museum's collections budget pays.

**The problem as the pack states it:** Museums must prove the climate around borrowed and owned objects, lenders ask for continuous records as a loan condition, and the institutional loggers that produce them cost £487–617 each plus annual software, so small museums log with a pen or borrow a logger for the loan.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/MuseumPros** · https://www.reddit.com/r/MuseumPros/ — museum staff.
- **NEMO, Network of European Museum Organisations** · https://www.ne-mo.org/ — European museum associations.
- **MCN, Museum Computer Network** · https://mcn.edu/ — museum technology staff.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how regional and university museums, archives, instrument and art collections, churches holding artworks deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. What did the last lender ask you for about the climate, and how did you produce it?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices. On a scale of one to ten, how likely would you be to buy that at €149–199, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Vitrine Log: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Vitrine Log: A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices. Before we spend money on tooling I want to find out whether this solves a real problem for regional and university museums, archives, instrument and art collections, churches holding artworks.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €149–199 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

The UK Government Indemnity Scheme (National Heritage Act 1980) genuinely requires relative humidity, temperature and light monitoring for the loan period; the specific environmental-conditions rule has been reported under active review (suspended through at least March 2023 with its status unclear), so verify the current requirement before leaning on it as a hard mandate. Lender loan policies (the Walters Art Museum's is a public example) ask for the same records regardless. The incumbent loggers (Testo 160 THL at about £487–617, Hanwell, ELTEK) are good and institutional; small museums own two and need twenty.

**Who pays, B2B/B2G:** the museum's collections or facilities budget; a loan can also carry the cost into the exhibition budget. **Who uses:** the registrar and conservator; the report must look like what they already send.

### Market size (estimates — check)

- **TAM:** ~20,000 museums in Europe plus archives and historic houses; 10–50 loggers each in the professional tier. Theoretical €50–100M.
- **SAM:** museums that lend and borrow and lack a monitoring system: estimate 5,000 institutions × 15 loggers → €13M.
- **SOM (3 yrs):** 8,000–15,000 loggers; year-1: 1,000–1,500 across 50–100 museums.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Testo 160 THL | Institutional T/RH/lux/UV logger; about £487–617 (research, Nov 2026) | A third of the price with the same four quantities and the report |
| Hanwell, ELTEK, Meaco | Museum monitoring systems with receivers and annual software | No per-logger licence; LoRaWAN uses the building's own gateway |
| Blue Maestro and consumer BLE loggers | Cheap T/RH only, phone app | No lux/UV, no calibration, no loan report |
| Pen and paper / borrowed logger for the loan | Free | The report generator is the product |

**Wedge:** the loan report at a third of the institutional price, four quantities in one logger, no software licence.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| UK Government Indemnity Scheme (ICOM UK on the GIS review) | Climate monitoring required for loans; environmental rule under review | Compliance pull, but verify current status |
| Walters Art Museum loan policy | Lender requires climate records | Demand regardless of GIS |
| Testo 160 THL | About £487–617 | Incumbent, 2–3× the target |

**Verdict as researched: LIKELY.** Main risk: Verify current GIS requirements before leaning on them as a hard mandate; lenders' own loan conditions carry the demand regardless.
<!-- market-competitors:end -->

### Product & value proposition

- T/RH (±0.2 °C / ±2% RH class), lux and UV sensors; calibrated per unit with a certificate; two-year cell (estimate at 10-minute logging).
- LoRaWAN (museum gateway or TTN) or BLE readout by phone for museums without a network; local server or hosted at cost.
- Report generator: per object or case, date range, set-point bands, excursions, graphs, PDF matching the registrar's expectations; CSV export.
- Discreet case in white or black, magnet and museum-putty mounts, no blinking lights in the vitrine.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €25–40) | 32.5 | 26.0 |
| PCBA assembly + test | 3.5 | 2.3 |
| Enclosure / mechanics (tooling amortised separately) | 5.0 | 3.5 |
| Packaging, cable, leaflet | 2.5 | 1.9 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 3.0 | 1.5 |
| Certification amortised (€10k, estimate) | 10.0 | 2.0 |
| **Landed cost** | **56.5** | **37.1** |
| Channel cost (direct to museums and conservation suppliers, ~€15) | 15.0 | 15.0 |
| Net price received (€174 incl. 19% VAT → €146.2 ex VAT) | 146.2 | 146.2 |
| **Gross margin per unit** | **€74.7 (51%)** | **€94.1 (64%)** |

Lesson: the calibration step is a real production cost (a chamber and an hour per batch); price it in and sell the yearly re-calibration as a service.

### Go-to-market

**First 100 customers:**

1. Three regional museums with upcoming loans, offered ten loggers and the report for one loan cycle.
2. Conservators' associations and museum federations (NEMO members, national museum associations) for newsletters and conferences.
3. Conservation suppliers as resellers.

**Scale channels:** museum federations, conservation suppliers, LoRaWAN integrators working with municipalities.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations with registrars; works-like logger on Stamp C6LoRa + HDC1000 + UV + DLight; report generator v0 with one museum's loan template. |
| Q2 | Custom PCB; calibration procedure; EVT 30 in three museums; BLE variant. |
| Q3 | DVT; certification; 500 loggers; first three orders shipped with reports. |
| Q4 | Conservation-supplier listing; 1,500 loggers; re-calibration service. |

**Team:** one embedded engineer, one developer for the report tool, one founder who speaks to registrars; calibration set-up bought in.

**Funding to first production (estimates):** NRE €16k + calibration rig €6k + certification €9k + first 1,000 loggers landed ~€35k ≈ €66k; minus museum pre-orders ~€15k ≈ €50k.

### Top risks

| Risk | Mitigation |
|---|---|
| The GIS environmental rule is under review | Do not sell on the mandate; sell on lenders' loan conditions, which exist regardless; verify the current GIS text before quoting it |
| Sensor drift over two years | Calibration certificate; re-calibration service; sensor choice |
| Museums have no LoRaWAN | BLE readout by phone; gateway bundle with a municipal network |
| Report format rejected by a lender | Build it with two registrars; keep it editable |

## 4. Start kit

### Boards to start from

- [Seeed Grove-TemperatureAndHumidity Sensor-HDC1000](https://www.gongbans.com/db/seeed-grove-temperatureandhumidity-sensor-hdc1000.html) — HDC1000 temperature/humidity reference circuit (open files: schematic)
- [Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0](https://www.gongbans.com/db/seeed-grove-temptureandhumidity-sensor-high-accuracy-andmini-v1-0.html) — high-accuracy T/RH alternative (open files: schematic)
- [M5Stack Unit ENV-Pro (U169)](https://www.gongbans.com/db/m5stack-unit-env-pro.html) — BME688-class environmental unit for the prototype (design files published for the module; electronics not open)
- [Seeed Grove-UV Sensor](https://www.gongbans.com/db/seeed-grove-uv-sensor.html) — UV sensor reference circuit (open files: schematic)
- [M5Stack Unit DLight (U136)](https://www.gongbans.com/db/m5stack-unit-dlight.html) — lux measurement (design files published for the module; electronics not open)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — open ESP32-C6 + LoRa core for the logger (open files: pcb,schematic)
- [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html) — EU868 LoRaWAN module for the prototype run (design files published for the module; electronics not open)

The Seeed sensor boards publish schematics; the Stamp C6LoRa (open PCB and schematic) is the core; the M5Stack units are the quickest prototype path for lux and the environmental sensor.

### Block diagram

```
  [T/RH sensor] [lux sensor] [UV sensor] -> [ESP32-C6 + LoRa (Stamp C6LoRa)] -> LoRaWAN gateway / TTN  or  BLE -> phone
                                                   |  [cell, 2 years]  [microSD backup]
  SERVER: per-object records -> report generator -> loan PDF, CSV
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| T/RH sensor (HDC1000 / SHT4x class) | 2.5 |  |
| Lux + UV sensors | 3.0 |  |
| ESP32-C6 + LoRa module | 6.0 |  |
| Lithium cell (AA-class, 2 years) | 3.0 |  |
| Enclosure, mounts | 5.0 |  |
| PCB, microSD, passives | 4.0 |  |
| Calibration (labour share) | 4.0 |  |

### Firmware/software starting point

- ESP-IDF; 10-minute logging to flash and uplink; LoRaWAN class A; BLE advertising with last values and a connect-to-download mode.
- Server: open-source ingest, per-object assignment, excursion rules, PDF generation; hosted at cost or self-hosted.
- Calibration constants per unit in NVS; certificate PDF generated at production.

### 12-week build plan

1. Interviews with registrars; fake door
2. Prototype logger
3. Report generator v0 from a real loan template
4. Calibration procedure
5. Custom PCB v1
6. Enclosure
7. EVT 30 in three museums
8. One loan cycle with reports
9. BLE variant
10. DVT
11. Pre-compliance
12. Certification; order fulfilment

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 3 regional museums buy 10 loggers each at €169 after one loan cycle with the PDF report? Pass = 3 orders in 10 weeks.
- **Cheapest experiment:** Five prototypes in one museum's vitrines for a loan period, the report delivered to the lender; ask the registrar whether they would buy ten at €169.
- **5-question interview:** 1) What do lenders ask you for and how do you produce it today? 2) How many loggers do you own and what did they cost with software? 3) Who decides and from which budget? 4) What would make a conservator distrust a cheaper logger? 5) At €169 with a calibration certificate and the report, how many?
- **Landing page:** headline "The loan report, from a €169 logger." Bullets: temperature, humidity, lux, UV; two years on a cell; LoRaWAN or phone; PDF your lender accepts. Button: request a trial set (B2B).
- **Pass threshold:** 3 orders of 10 within 10 weeks.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.
- Calibration batch record per unit; certificate in the box.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Seeed Studio and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-TemperatureAndHumidity Sensor-HDC1000](/db/seeed-grove-temperatureandhumidity-sensor-hdc1000.html) (HDC1000 temperature/humidity reference circuit); [Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0](/db/seeed-grove-temptureandhumidity-sensor-high-accuracy-andmini-v1-0.html) (high-accuracy T/RH alternative); [Seeed Grove-UV Sensor](/db/seeed-grove-uv-sensor.html) (UV sensor reference circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit ENV-Pro (U169)](/db/m5stack-unit-env-pro.html) (BME688-class environmental unit for the prototype); [M5Stack Unit DLight (U136)](/db/m5stack-unit-dlight.html) (lux measurement); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core for the logger); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN module for the prototype run). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868) — for a Vitrine Log

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Vitrine Log: A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices. The design is built around your Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868).

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868).
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
主题：样品订购及批量报价 — Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868) — 用于Vitrine Log

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Vitrine Log：A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices。产品设计基于贵司的Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868)。
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
Subject: PCBA quote from open design files — Vitrine Log, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Vitrine Log: A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices. The design starts from published open-hardware files (Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Vitrine Log，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Vitrine Log：A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices。设计基于已公开的开源硬件文件（Seeed Grove-TemperatureAndHumidity Sensor-HDC1000, Seeed Grove-TemptureAndHumidity Sensor-High-Accuracy AndMini-v1.0, Seeed Grove-UV Sensor, M5Stack Unit ENV-Pro (U169), M5Stack Unit DLight (U136), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868)；含原理图、PCB和BOM），并做了我们自己的修改。

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
