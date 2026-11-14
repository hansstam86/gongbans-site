# Laundry Room Notifier — Founder Start Pack

> Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Residents of blocks with a shared laundry room carry the basket down to find every machine running, and operators field the complaints; the booking systems that solve it are expensive card infrastructures sold with the machines.
- **Customer:** Housing associations, student-housing operators and co-ops with shared laundry rooms (the norm in Switzerland, common in Germany and the Nordics); the facility or property manager pays per room, residents use the board and the page.
- **Product:** Clip-on sensor nodes per machine (power draw, or vibration where the plug is unreachable), an e-paper board at the laundry-room door showing each machine's state and expected finish, an optional resident page or push, a LoRa link for basements; no per-room fee. Target price €249–349 (estimate).
- **Why now:** Washer-done detection is one of the most repeated Home Assistant projects, shared laundry rooms are a daily friction for millions of residents, and the professional booking systems are expensive and tied to card infrastructure.
- **The ask:** ~€45–55k to certification and a first 300 rooms (estimate); three pilots cover a fifth.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** A confirmed, active Home Assistant DIY pattern (multiple forum threads and GitHub projects for washer/dryer notification): real demand. No public pricing was found for Miele, Electrolux or Waschkarten systems, so the competitive gap must be verified. **Main risk:** Ask in the demand interviews whether housing associations want detection layered on existing booking or card systems or consider the problem solved; verify incumbent pricing before claiming a gap. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 housing associations or student-housing operators install a paid pilot in 5 laundry rooms at €299 per room, and do residents say in week 3 that they check the board before carrying the basket? Pass = 3 pilots and a majority yes.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Housing associations, student-housing operators and housing co-ops in CH/DE/Nordics where shared laundry rooms are standard; facility managers buy, residents use.

**The problem as the pack states it:** Residents of blocks with a shared laundry room carry the basket down to find every machine running, and operators field the complaints; the booking systems that solve it are expensive card infrastructures sold with the machines.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/PropertyManagement** · https://www.reddit.com/r/PropertyManagement/ — property and facility managers.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€249–349, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how housing associations, student-housing operators and housing co-ops in CH/DE/Nordics where shared laundry rooms are standard deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do residents find out whether a machine is free, and what do they complain about to you?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription. On a scale of one to ten, how likely would you be to buy that at €249–349, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Laundry Room Notifier: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Laundry Room Notifier: Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription. Before we spend money on tooling I want to find out whether this solves a real problem for housing associations, student-housing operators and housing co-ops in CH/DE/Nordics where shared laundry rooms are standard.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €249–349 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

The Home Assistant forums carry multiple long threads and GitHub projects for detecting a washer's cycle from its power draw or vibration; the pattern is proven at home. In a shared room the same information is worth more and nobody provides it except full booking systems (Miele and Electrolux Professional, Aptus, the Swiss card systems), whose prices were not found publicly and must be verified. The open question the demand interviews must settle: do operators want detection layered on an existing booking or card system, or do they consider the problem solved by it?

**Who pays, B2B:** the operator, per room, from the facility budget or the laundry-room income. **Who uses:** residents, who must get the answer without an app (the board) and may get it on the phone (the page).

### Market size (estimates — check)

- **TAM:** shared laundry rooms in CH (most apartment blocks), DE and the Nordics (student housing, co-ops): estimate 500,000+ rooms. Theoretical €150M at €299.
- **SAM:** rooms run by professional operators with more than 20 units: estimate 150,000 → €45M.
- **SOM (3 yrs):** 5,000–10,000 rooms; year-1: 300–500 through three operators.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Miele / Electrolux Professional booking systems | Card or app booking tied to the machines; pricing not public | Retrofit on any machine, no card infrastructure; verify their pricing before claiming a gap |
| Aptus and Swiss Waschkarten systems | Access and booking systems, pricing not public | Same; we may layer on top of them |
| Smart plugs + Home Assistant (washer/dryer notify blueprints, GitHub washer-notifier) | DIY at home | Proven detection; we make it a product for a shared room |
| A whiteboard on the door | Free | Nobody updates it |

**Wedge:** retrofit detection on any machine with a door-side board residents trust, sold per room without a fee; it layers on existing booking systems rather than replacing them.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Home Assistant forum threads (laundry sensors; washer/dryer notify blueprint) | DIY detection at home | Proven pattern, demand signal |
| GitHub washer-notifier project | DIY project | Same |
| Miele / Electrolux Professional, Aptus, Waschkarten systems | Booking systems, pricing not public | Incumbents; gap unverified |

**Verdict as researched: LIKELY.** Main risk: Ask in the demand interviews whether housing associations want detection layered on existing booking or card systems or consider the problem solved; verify incumbent pricing before claiming a gap.
<!-- market-competitors:end -->

### Product & value proposition

- Sensor node: clip-on current transformer on the machine's cable or a plug-through power meter where allowed; vibration node (accelerometer, magnet-mounted) for machines with inaccessible plugs; cycle classification (running, final spin, finished, idle).
- Door board: e-paper listing machines, state, expected finish, last updated; battery or USB.
- Resident page: QR on the board, no login; optional push via the operator's existing app or e-mail.
- Link: WiFi where it reaches, LoRa node-to-board for basements; operator dashboard with utilisation per machine (helps plan machine counts).

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €50–80) | 65.0 | 52.0 |
| PCBA assembly + test | 6.0 | 3.9 |
| Enclosure / mechanics (tooling amortised separately) | 10.0 | 7.0 |
| Packaging, cable, leaflet | 4.0 | 3.0 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 4.0 | 2.0 |
| Certification amortised (€9k, estimate) | 9.0 | 1.8 |
| **Landed cost** | **98.0** | **69.7** |
| Channel cost (direct to operators and facility-service channel, ~€25) | 25.0 | 25.0 |
| Net price received (€299 incl. 19% VAT → €251.3 ex VAT) | 251.3 | 251.3 |
| **Gross margin per unit** | **€128.3 (51%)** | **€156.6 (62%)** |

Lesson: a room is four nodes and a board; the utilisation data for the operator is the upsell that pays for support.

### Go-to-market

**First 100 customers:**

1. Three operators (one Swiss housing association, one student-housing operator, one co-op) with five-room paid pilots.
2. Facility-service companies that run laundry rooms for operators.
3. Co-ops via their federations.

**Scale channels:** housing-association federations, facility-service firms, laundry-machine dealers for retrofit.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations with operators (including the layering question); works-like nodes on Unit AC Measure + AtomS3 and a PaperS3 board in one room. |
| Q2 | Custom node PCB; vibration node; EVT in 5 rooms; resident feedback. |
| Q3 | DVT; certification; 150 rooms; three pilots shipped. |
| Q4 | Operator dashboard; 500 rooms; dealer channel. |

**Team:** one embedded engineer, one developer for the board and page, one founder selling to operators.

**Funding to first production (estimates):** NRE €16k + certification €9k + first 300 rooms landed ~€30k ≈ €55k; minus pilots ~€9k ≈ €46k.

### Top risks

| Risk | Mitigation |
|---|---|
| Operators see the problem as solved by booking systems | Ask it in the first ten interviews; position as a layer; target rooms without booking first |
| Cycle detection errors (false 'finished') | Classifier tuned per machine type; final-spin detection; expected-finish shown as estimate |
| Residents ignore the board | Place at eye level by the door; QR page; week-3 question in the kill question |
| Electrical rules for clip-on and plug-through sensors | Clip-on CT needs no mains contact; plug-through only with a certified socket module |

## 4. Start kit

### Boards to start from

- [M5Stack Unit AC Measure (U164)](https://www.gongbans.com/db/m5stack-unit-ac-measure.html) — AC power measurement per machine (design files published for the module; electronics not open)
- [DFRobot SEN0098](https://www.gongbans.com/db/dfrobot-sen0098.html) — AC current sensor alternative (open files: schematic)
- [M5Stack Unit Accel (U056)](https://www.gongbans.com/db/m5stack-unit-accel.html) — vibration-based detection where the plug is not accessible (design files published for the module; electronics not open)
- [M5Stack PaperS3 (C139)](https://www.gongbans.com/db/m5stack-papers3.html) — e-paper status board at the laundry-room door (design files published for the module; electronics not open)
- [M5Stack CoreInk (K048)](https://www.gongbans.com/db/m5stack-coreink.html) — small e-paper variant (design files published for the module; electronics not open)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — LoRa link from basement laundry rooms (open files: pcb,schematic)
- [M5Stack AtomS3-Lite (C124)](https://www.gongbans.com/db/m5stack-atoms3-lite.html) — ESP32-S3 sensor node core (design files published for the module; electronics not open)

The M5Stack measurement, e-paper and core units carry published module files; the DFRobot current sensor is the second source; the Stamp C6LoRa (open files) is the basement link.

### Block diagram

```
  per machine: [clip-on CT or plug-through meter | accelerometer] -> [ESP32 node] -> WiFi / LoRa
                                                                                  |
  door: [e-paper board: W1 running 23 min | W2 free | D1 finished]  <- [bridge] -> resident page (QR), operator dashboard
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| Current transformer + ADC or plug-through meter module (×4) | 16.0 | per room |
| ESP32 nodes ×4 | 10.0 |  |
| Accelerometer option | +3.0 |  |
| E-paper board + ESP32 + enclosure | 22.0 |  |
| Node enclosures, cables | 8.0 |  |
| LoRa bridge option | +8.0 | basement rooms |

### Firmware/software starting point

- ESP-IDF; power/vibration sampling, cycle state machine per machine type; LoRa or WiFi uplink; board renders states and estimates.
- Small server: states, resident page, operator dashboard, utilisation CSV; self-hosted or hosted at cost.

### 12-week build plan

1. Interviews with operators (layering question first); pilot proposals
2. Prototype nodes and board in one room
3. Cycle classifier
4. Node PCB v1
5. Vibration node
6. Board enclosure
7. EVT in 5 rooms
8. Resident survey in week 3
9. Dashboard v0
10. DVT
11. Pre-compliance
12. Certification; pilot roll-out

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 3 housing associations or student-housing operators install a paid pilot in 5 laundry rooms at €299 per room, and do residents say in week 3 that they check the board before carrying the basket? Pass = 3 pilots and a majority yes.
- **Cheapest experiment:** Four smart-plug sensors and a PaperS3 board in one laundry room for three weeks; ask residents at the door whether they checked it, and the operator whether they would pay €299 per room.
- **5-question interview:** 1) How do residents find out whether a machine is free today, and what do they complain about? 2) Do you run a booking or card system; what did it cost and does it tell people when a cycle ends? 3) Who approves a per-room purchase? 4) Where are the rooms (basement, WiFi)? 5) At €299 per room with no fee, how many rooms?
- **Landing page:** headline "Know before you carry the basket." Bullets: works with your machines; board at the door; page on the phone; €299 per room, no fee. Button: request a pilot (B2B).
- **Pass threshold:** 3 pilots and a resident majority saying they check the board by week 3.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and DFRobot).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit AC Measure (U164)](/db/m5stack-unit-ac-measure.html) (AC power measurement per machine); [M5Stack Unit Accel (U056)](/db/m5stack-unit-accel.html) (vibration-based detection where the plug is not accessible); [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (e-paper status board at the laundry-room door); [M5Stack CoreInk (K048)](/db/m5stack-coreink.html) (small e-paper variant); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (LoRa link from basement laundry rooms); [M5Stack AtomS3-Lite (C124)](/db/m5stack-atoms3-lite.html) (ESP32-S3 sensor node core). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **DFRobot** — community / maker brand; 250 boards in the catalogue; files via DFRobot wiki catalog · https://wiki.dfrobot.com/. Boards used here: [DFRobot SEN0098](/db/dfrobot-sen0098.html) (AC current sensor alternative). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*
- **iDisc Technology** (深圳市艾迪思科技有限公司) · no website on file — E-ink display module / e-reader OEM: E-ink display module; e-reader gongban; retail price tag; OEM/ODM. *(E-ink display modules)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and DFRobot websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098 — for a Laundry Room Notifier

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Laundry Room Notifier: Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription. The design is built around your M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098.
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
主题：样品订购及批量报价 — M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098 — 用于Laundry Room Notifier

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Laundry Room Notifier：Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription。产品设计基于贵司的M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098。
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
Subject: PCBA quote from open design files — Laundry Room Notifier, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Laundry Room Notifier: Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription. The design starts from published open-hardware files (M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Laundry Room Notifier，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Laundry Room Notifier：Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription。设计基于已公开的开源硬件文件（M5Stack Unit AC Measure (U164), M5Stack Unit Accel (U056), M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack Stamp C6LoRa (S012), M5Stack AtomS3-Lite (C124), DFRobot SEN0098；含原理图、PCB和BOM），并做了我们自己的修改。

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
