# Village Stop Display — Founder Start Pack

> A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Outside cities, a bus stop is a pole and a laminated sheet; when the bus is late nobody knows, and the agency displays that could tell them cost €2,000–5,000 each plus a service contract, so rural stops never get one.
- **Customer:** Landkreise and regional transport associations (B2G) in regions whose operators publish GTFS and GTFS-Realtime; municipalities that co-fund stop furniture; dial-a-ride and community bus operators. The transport association's passenger-information budget pays.
- **Product:** An A4-class e-paper sign in an IP65 housing with solar panel and buffer cell, Cat-M (or LoRaWAN where a town network exists), showing the scheduled departures from GTFS at all times and live times where GTFS-Realtime exists for that stop, with the source stated on screen. Target price €599–899 (estimate).
- **Why now:** Rural stops have paper timetables and no information at all when a bus is late; agency displays cost €2,000–5,000 with service contracts; e-paper, Cat-M and solar make a €800 sign possible, and open GTFS data is spreading region by region.
- **The ask:** ~€90–120k to certification and a first 200 signs (estimate); two paid pilots cover a third.

<!-- market-check:start -->
> **External market check (November 2026): UNCERTAIN.** A real technical blocker: live GTFS-Realtime requires on-board vehicle equipment that rural and small-contractor bus fleets often lack (confirmed in a Südtirol example), so buses without it show only scheduled times, in exactly the rural markets targeted. Municipal e-paper stop displays (Meisenheim, Ludwigsburg) and regional GTFS-RT open data (VBN) exist. **Main risk:** The pitch was reworked before building: scheduled always, live where available, with the source labelled on screen; scope sales to regions that already publish GTFS-RT. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
>
> **Built with the research fix applied (November 2026).** The research found that live departure data needs on-board equipment many rural fleets lack, so a sign promising live times everywhere would fail in its own target market. This pack is therefore scoped to "scheduled always, live where the operator broadcasts it", the sign labels which it shows, and the kill question only counts regions that already publish GTFS-Realtime for their stops. As researched November 2026 by web search; verify before relying on it.
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 2 Landkreise or transport associations whose operators already publish GTFS-Realtime sign a paid 10-stop pilot at €799 per sign within 8 weeks? Pass = 2 signed pilots; a region without GTFS-RT at its stops does not count.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Landkreise and regional transport associations whose operators already publish GTFS-Realtime (for example VBN and other open-data regions), small municipalities, rural bus operators; B2G procurement.

**The problem as the pack states it:** Outside cities, a bus stop is a pole and a laminated sheet; when the bus is late nobody knows, and the agency displays that could tell them cost €2,000–5,000 each plus a service contract, so rural stops never get one.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/transit** · https://www.reddit.com/r/transit/ — public-transport enthusiasts.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€599–899, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how landkreise and regional transport associations whose operators already publish GTFS-Realtime, small municipalities, rural bus operators deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Which of your stops have any passenger information today, what did it cost per stop, and do your operators broadcast live positions?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays. On a scale of one to ten, how likely would you be to buy that at €599–899, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Village Stop Display: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Village Stop Display: A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays. Before we spend money on tooling I want to find out whether this solves a real problem for landkreise and regional transport associations whose operators already publish GTFS-Realtime, small municipalities, rural bus operators.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €599–899 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

Research for this pack confirmed the catch: live departure data needs on-board equipment in the vehicle, and rural or small-contractor fleets often lack it, so a sign that promises "live" everywhere lies in exactly the places that need it most. The product is therefore scoped: timetable always, live where the operator broadcasts it, and the sign says which. Even the scheduled-only mode replaces a laminated sheet that is often out of date, and the live overlay arrives as operators equip their fleets (regions such as VBN already publish GTFS-Realtime as open data).

**Who pays, B2G (primary):** transport associations and Landkreise from passenger-information and stop-furniture budgets, often with regional or EU funding for rural mobility. **Who uses:** passengers, including older people without a smartphone, which is the political argument for the sign.

### Market size (estimates — check)

- **TAM:** ~300,000 bus stops in Germany, the large majority without any display; similar density in AT/CH/NL/FR. Theoretical €200M+ at €800.
- **SAM:** stops in regions with open GTFS feeds and a rural-mobility programme: estimate 30,000 stops → €25M.
- **SOM (3 yrs):** 1,500–3,000 signs across 10–20 regions. Year-1: 100–200 signs in two pilots and two follow-on orders.

### Competition (4 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Papercast, Luminator, ConnectPoint | Agency-grade e-paper and LED stop displays, €2,000–5,000 per sign plus service (quote-based) | A third to a fifth of the price, no service contract, open data in |
| Paper timetable | Free, out of date | We show the same timetable, always current, plus live where it exists |
| Municipal pilot displays (Meisenheim, Ludwigsburg examples) | Individual municipalities already trial e-paper stop displays | Demand signal and a procurement precedent |
| DIY e-paper transit boards (the hallway-board family) | Hobby builds | Proof of the display idea; not an outdoor product |

**Wedge:** price and honesty: a quarter of the agency display, no service contract, and a sign that says "scheduled" or "live" so the passenger can trust it.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Südtirol real-time caveat | Buses without on-board equipment do not report live positions | The 'live' promise cannot hold everywhere; pitch reworked |
| Meisenheim, Ludwigsburg municipal display examples | Municipalities trialling e-paper stop displays | Demand and procurement precedent |
| VBN GTFS-Realtime open data | Regional live feed published openly | Target regions exist |
| Papercast, Luminator, ConnectPoint | Agency displays, quote-based €2–5k | Incumbents at a multiple of the target |

**Verdict as researched: UNCERTAIN.** Main risk: The pitch was reworked before building: scheduled always, live where available, with the source labelled on screen; scope sales to regions that already publish GTFS-RT.
<!-- market-competitors:end -->

### Product & value proposition

- 7.5–13.3 inch e-paper, readable in sunlight, backlight for night, in a vandal-resistant IP65 housing on a standard pole clamp.
- Solar panel and buffer cell sized for a northern winter at ten refreshes an hour (estimate; validate in December).
- Cat-M modem with an operator SIM or the region's IoT SIM; LoRaWAN variant where a town network exists.
- Firmware: GTFS static for the stop, GTFS-Realtime overlay when the feed carries that stop's trips, a "scheduled / live" label, disruption text, QR to the operator's app.
- Fleet dashboard for the association: battery, last refresh, uptime; open API; no per-sign licence.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €120–180) | 150.0 | 120.0 |
| PCBA assembly + test | 15.0 | 9.8 |
| Enclosure / mechanics (tooling amortised separately) | 60.0 | 42.0 |
| Packaging, cable, leaflet | 8.0 | 6.0 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 12.0 | 6.0 |
| Certification amortised (€15k, estimate) | 15.0 | 3.0 |
| **Landed cost** | **260.0** | **186.8** |
| Channel cost (direct B2G, tender support and installation partner, ~€60) | 60.0 | 60.0 |
| Net price received (€749 incl. 19% VAT → €629.4 ex VAT) | 629.4 | 629.4 |
| **Gross margin per unit** | **€309.4 (49%)** | **€382.7 (61%)** |

Lesson: the housing and the pole mount cost as much as the electronics; design one housing for two display sizes. Procurement support time is the hidden cost; price it into the pilot.

### Go-to-market

**First 100 customers:**

1. Two transport associations with open GTFS-Realtime, found through their open-data portals, offered a paid ten-stop pilot.
2. Municipalities that already trialled e-paper stop displays, offered the cheaper second generation.
3. Dial-a-ride and community-bus operators that need a sign at a handful of stops.

**Scale channels:** regional mobility programmes and funding calls, stop-furniture suppliers, the association's own roll-out plans.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations with four associations; works-like sign on PaperS3 + Unit CatM reading one region's GTFS and GTFS-RT; December solar test. |
| Q2 | Custom board, housing, pole mount; EVT 5 signs at real stops with one association. |
| Q3 | DVT; certification; 50 signs; first paid pilot shipped and installed. |
| Q4 | Second pilot; fleet dashboard; 200 signs; funding-call partnerships. |

**Team:** one embedded engineer, one backend developer (GTFS, dashboard), one founder for B2G sales; housing design and installation partner bought in.

**Funding to first production (estimates):** NRE €40k (board, housing tooling, mount) + certification €15k + first 200 signs landed ~€50k ≈ €105k; minus two pilots ~€16k ≈ €90k.

### Top risks

| Risk | Mitigation |
|---|---|
| Regions without GTFS-Realtime at their stops | Scope to regions that publish it; scheduled-only mode is honest and still useful; say which mode on screen |
| Winter solar budget | Measure in December before DVT; larger panel or mains option |
| Vandalism and weather | Polycarbonate window, tamper alert, replaceable front; warranty terms |
| Procurement cycles of 6–18 months | Paid pilots under tender thresholds first; partner with a stop-furniture supplier |

## 4. Start kit

### Boards to start from

- [M5Stack PaperS3 (C139)](https://www.gongbans.com/db/m5stack-papers3.html) — ESP32-S3 e-paper device for the prototype sign (design files published for the module; electronics not open)
- [M5Stack PaperColor (C151)](https://www.gongbans.com/db/m5stack-papercolor.html) — colour e-paper variant for line colours (design files published for the module; electronics not open)
- [SIMCom A7672X/A7670X Series Hardware Design](https://www.gongbans.com/db/simcom-a7670x-hw-design.html) — Cat-1/Cat-M cellular module hardware design for the backhaul (open files: schematic)
- [M5Stack Unit CatM (U128)](https://www.gongbans.com/db/m5stack-unit-catm.html) — Cat-M unit for the prototype (design files published for the module; electronics not open)
- [DFRobot DFR0535](https://www.gongbans.com/db/dfrobot-dfr0535.html) — solar power manager for the off-grid post (open files: schematic)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — LoRaWAN backhaul where a town network exists (open files: pcb,schematic)

The PaperS3 and PaperColor give the display path; the SIMCom A7672X hardware design is the openly mirrored reference for the cellular section; the DFRobot solar power manager covers the off-grid power path for prototypes.

### Block diagram

```
  [solar panel] -> [solar power manager + LiFePO4 cell] -> [ESP32-S3]
                                                            |  SPI
  [Cat-M modem (A767x)] <-- GTFS / GTFS-RT every 6 min --> [e-paper 7.5–13.3"]
  [temp sensor] [tamper switch]        label on screen: SCHEDULED | LIVE
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| E-paper 7.5–13.3 inch + driver | 45.0 | size per stop |
| ESP32-S3 module | 3.0 |  |
| Cat-M modem + antenna + SIM holder | 15.0 |  |
| Solar panel 10–20 W + power manager | 20.0 |  |
| LiFePO4 cell | 12.0 |  |
| IP65 housing + pole clamp + polycarbonate window | 60.0 | two display sizes, one housing family |
| PCB, sensors, passives | 8.0 |  |

### Firmware/software starting point

- ESP-IDF; GTFS static parsed server-side per stop and pushed as a compact schedule; GTFS-RT polled server-side and pushed only when the stop's trips are in the feed.
- Partial e-paper refresh; deep sleep between refreshes; battery and temperature telemetry.
- Server: small open-source service per region (GTFS ingest, per-stop API, fleet dashboard); no per-sign licence.

### 12-week build plan

1. Interviews with associations; fake door for B2G
2. Prototype on PaperS3 + CatM with one region's GTFS
3. GTFS-RT overlay and the scheduled/live label
4. Solar budget measurement
5. Custom board v1
6. Housing and mount design
7. EVT 5 at real stops
8. Association feedback; dashboard v0
9. Housing tooling decision
10. DVT signs
11. Pre-compliance
12. Certification; pilot contract

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 2 Landkreise or transport associations whose operators already publish GTFS-Realtime sign a paid 10-stop pilot at €799 per sign within 8 weeks? Pass = 2 signed pilots; a region without GTFS-RT at its stops does not count.
- **Cheapest experiment:** One PaperS3 in a weatherproof box at one rural stop for a month with the association's blessing, showing scheduled times; count the passengers who ask for it to stay.
- **5-question interview:** 1) Which of your stops have any display today and what did it cost per stop? 2) Does your GTFS-Realtime feed cover rural lines; which operators are equipped? 3) Who decides on stop furniture and from which budget? 4) What would a sign need to do for you to put ten on poles? 5) At €799 per sign without a service contract, how many stops in a pilot?
- **Landing page:** headline "A departure sign every stop can afford." Bullets: timetable always, live where your buses report, solar, €799, no service contract. Button: request a pilot (B2G form).
- **Pass threshold:** 2 signed ten-stop pilots in regions with GTFS-RT within 8 weeks.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.
- Outdoor: IP65 ingress test on samples, UV-stable window, salt-spray on the clamp if coastal.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and SIMCom and DFRobot).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (ESP32-S3 e-paper device for the prototype sign); [M5Stack PaperColor (C151)](/db/m5stack-papercolor.html) (colour e-paper variant for line colours); [M5Stack Unit CatM (U128)](/db/m5stack-unit-catm.html) (Cat-M unit for the prototype); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (LoRaWAN backhaul where a town network exists). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **SIMCom** — solution house; 3 boards in the catalogue; files via SIMCom module hardware designs · https://www.simcom.com/technical_files-p110.html. Boards used here: [SIMCom A7672X/A7670X Series Hardware Design](/db/simcom-a7670x-hw-design.html) (Cat-1/Cat-M cellular module hardware design for the backhaul). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **DFRobot** — community / maker brand; 250 boards in the catalogue; files via DFRobot wiki catalog · https://wiki.dfrobot.com/. Boards used here: [DFRobot DFR0535](/db/dfrobot-dfr0535.html) (solar power manager for the off-grid post). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **iDisc Technology** (深圳市艾迪思科技有限公司) · no website on file — E-ink display module / e-reader OEM: E-ink display module; e-reader gongban; retail price tag; OEM/ODM. *(E-ink display modules)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*
- **Luat (Air105/Air780)** (深圳市合宙通信有限公司) · openluat.com — LTE Cat-1 / NB-IoT module OEM: Air780E Cat-1 bis module; Air105 MCU; MQTT/TLS; OEM/ODM. *(Cellular (Cat-1 / NB-IoT) modules)*
- **LILYGO** (深圳市合宙通信有限公司) · lilygo.cc — ESP32 / LoRa / cellular dev module OEM: T-SIM7670 / T-Watch / TTGO LoRa boards; OEM module supply. *(Cellular (Cat-1 / NB-IoT) modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and SIMCom and DFRobot websites)

```email
Subject: Sample order and volume pricing — M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535 — for a Village Stop Display

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Village Stop Display: A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays. The design is built around your M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535.
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
主题：样品订购及批量报价 — M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535 — 用于Village Stop Display

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Village Stop Display：A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays。产品设计基于贵司的M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535。
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
Subject: PCBA quote from open design files — Village Stop Display, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Village Stop Display: A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays. The design starts from published open-hardware files (M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Village Stop Display，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Village Stop Display：A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays。设计基于已公开的开源硬件文件（M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack Unit CatM (U128), M5Stack Stamp C6LoRa (S012), SIMCom A7672X/A7670X Series Hardware Design, DFRobot DFR0535；含原理图、PCB和BOM），并做了我们自己的修改。

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
