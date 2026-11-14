# HACCP Fridge Logger — Founder Start Pack

> Stick-on fridge and freezer sensors plus a kitchen e-paper display that keeps the legally required HACCP temperature log and emails the PDF weekly — buy once, no monthly fee.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** EU food-hygiene rules (Regulation 852/2004 and national HACCP guidance) require small kitchens to record fridge and freezer temperatures. Most still do it twice a day on a clipboard, often from memory, and panic before the inspector comes.
- **Customer:** Restaurants, bakeries, food trucks, cafés, care-home and school kitchens, small food retailers across the EU (~1.6 M food and drink establishments in the EU-27, [Statista/Eurostat](https://www.statista.com/topics/3966/restaurant-industry-in-europe)). The owner pays; the kitchen crew and the inspector use.
- **Product:** Hub with a 4.7"-class e-paper display and buzzer + 3 magnetic IP54 sensor pods (≥1-year battery), HACCP firmware (limits per unit, corrective-action prompts, signed PDF, 2 years local storage), weekly email. Starter kit €249–299, no subscription.
- **Why now:** Incumbents are subscription-based cloud systems (starter kits ~€410 plus credits) or single-fridge Bluetooth loggers (~€54–65); the "multi-fridge, WiFi-independent, zero-subscription, inspector-readable display" slot is empty. ESP32-C6 brings WiFi + 802.15.4 in one chip.
- **The ask:** ~€140k (estimate) to 1,000 kits. Route: pre-orders from cash-and-carry mornings (kill question), a food-tech or digitalisation grant, then an angel from hospitality supply.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> A morning outside a cash-and-carry with the mock-up and a €249 price card: do 10 of 50 owners leave a card for pre-order?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** EU restaurants, bakeries, food trucks, care-home and school kitchens.

**The problem as the pack states it:** EU food-hygiene rules (Regulation 852/2004 and national HACCP guidance) require small kitchens to record fridge and freezer temperatures. Most still do it twice a day on a clipboard, often from memory, and panic before the inspector comes.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/KitchenConfidential** · https://www.reddit.com/r/KitchenConfidential/ — chefs and kitchen staff; the people who do the fridge log.
- **r/restaurateur** · https://www.reddit.com/r/restaurateur/ — restaurant owners.
- **DEHOGA (DE)** · https://www.dehoga-bundesverband.de/ — German hotel and restaurant association.
- **UKHospitality** · https://www.ukhospitality.org.uk/ — UK hospitality trade body.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€249–299 starter kit, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how EU restaurants, bakeries, food trucks, care-home and school kitchens deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Walk me through your fridge temperature log: who writes it, when, and what happened at your last inspection?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Stick-on fridge and freezer sensors plus a kitchen e-paper display that keeps the legally required HACCP temperature log and emails the PDF weekly — buy once, no monthly fee. On a scale of one to ten, how likely would you be to buy that at €249–299 starter kit, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: HACCP Fridge Logger: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a HACCP Fridge Logger: Stick-on fridge and freezer sensors plus a kitchen e-paper display that keeps the legally required HACCP temperature log and emails the PDF weekly — buy once, no monthly fee. Before we spend money on tooling I want to find out whether this solves a real problem for EU restaurants, bakeries, food trucks, care-home and school kitchens.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €249–299 starter kit per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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
Segment: **independent food businesses with 2–8 cold units**, in DE, NL, BE, FR, IT, ES, AT, Nordics and the UK (similar rules post-Brexit). The owner-operator signs; the sous-chef sets limits; the inspector reads the display or the PDF. Care-home and school kitchens are the second segment: they are more process-driven and buy through facility managers — same product, longer sales cycle, bigger orders.

The emotional buyer is the owner who was once written up for missing records. The practical buyer wants to stop paying someone to walk to the walk-in at 6 a.m.

### Market size (estimates)
- ~1.6 M food and drink establishments in the EU-27 ([Statista](https://statista.com/statistics/684198/number-of-enterprises-in-the-food-and-beverage-service-industry-in-the-eu)); add ~0.2 M UK; add institutional kitchens (~0.3 M). Call it **2 M kitchens with HACCP obligations**.
- **TAM:** 2 M × €279 ≈ **€560 M** one-off, plus sensors (avg 2 extra pods × €39) ≈ €150 M.
- **SAM:** kitchens with ≥2 cold units, an owner who has internet in the kitchen, and no existing system — 40% → 800k → **€220 M**.
- **SOM (3 years):** 0.5% → 4,000 kits → **€1.1 M** plus ~€0.3 M sensors/probes/calibration certs.

### Competition
| Alternative | Price points (listings) | Weakness we attack |
|---|---|---|
| Cloud HACCP monitoring systems (professional, sold with yearly credits/subscription; starter kit ~€410 + credits — [AiroSensor via Avantor](https://www.avantorsciences.com/export/en/product/17056899/wireless-temperature-and-humidity-data-loggers-airosensor); [Testo Saveris 2](https://testo.com/en-UK/applications/food-restaurants-gastronomy-saveris-2)) | Trusted by chains | Subscription; needs the cloud; overkill for a bistro |
| WiFi loggers with a 1-year included subscription (~€65 — [Elitech RCW-800W](https://www.elitecheu.com/products/elitech-rcw-800w-5m-tde-eu-wireless-temperature-data-logger)) | Cheap entry | One fridge each, app-only, subscription after year one |
| Bluetooth HACCP loggers (~€54 — [GGM TMPX-01](https://www.ggmgastro.com/en-de-eur/commercial-bluetooth-automatic-haccp-temperature-logger-app-connected-fridge-freezer-thermometer-tmpx-01)) | Sold by catering wholesalers | Someone must walk by with a phone; no multi-fridge log |
| Paper clipboard / "do nothing" | Free | Fines, closures, lost reputation; staff time |
| DIY (ESP32 + DS18B20 + Home Assistant) | €30 | No audit trail, no signature, nobody in a kitchen wants to maintain it |

**Wedge:** buy once; a wall display the inspector can read; works without WiFi (sensors talk to the hub on 802.15.4 or sub-GHz, the hub stores 2 years; WiFi only for the weekly email); corrective-action workflow that makes the PDF audit-grade.

### Product & value proposition
- **Hub:** ESP32-S3/C6, 4.7"-class e-paper (always-on, readable, no glow), buzzer, USB-C power, 2 years of logs in flash, WiFi for email/PDF, local web page as backup; door-open and out-of-range alarms; "acknowledge + corrective action" buttons.
- **Sensor pod:** ESP32-C6 (802.15.4) or sub-GHz module, SHT3x-class T/RH inside + optional external NTC probe (glycol-bottle probe for the walk-in, probe-through-door for freezers), magnetic IP54 housing, 2× AA lithium primary ≥ 1 year inside a steel fridge (external antenna lead to the door seal is the trick).
- **Software:** limits per unit, 15-min interval, 2 excursions/day summarised, corrective-action prompts, PDF signed with a device key, weekly email, CSV export. No account required; optional free cloud backup later.

Pricing (estimates): **Starter kit (hub + 3 pods) €279 RRP** (€249 launch), extra pod €39, door-probe pod €49, annual calibration certificate €29/pod (upsell, with a reference thermometer check). B2B to wholesalers at 35% off.

### Unit economics (estimates per starter kit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (hub: ESP32 module, e-paper 4.7", buzzer, PSU; 3 pods: C6 module, SHT3x, NTC, AA holders, antenna, PCB) | €62.00 | €49.00 |
| Primary cells (6× AA Li-FeS2) | €7.20 | €5.80 |
| Assembly & test (4 PCBAs, RF test, pairing at factory) | €9.50 | €6.50 |
| Enclosure (hub shell, 3 IP54 pods with magnets/gaskets; tooling amortised) | €10.50 | €6.80 |
| Packaging (kit box, quick-start, probe bottle) | €3.20 | €2.20 |
| Freight + duty to EU (lithium cells → DG) | €5.00 | €2.80 |
| Certification amortised (~€35k: RED, EMC, 62368-1, EN 18031, battery/transport) | €35.00 | €7.00 |
| **Landed cost** | **€132.40** | **€80.10** |
| Sell price (direct €279 / wholesale €181) | €279 | €181 (via wholesalers) |
| **Gross margin** | **€146.60 (53%)** | **€100.90 (56%)** |

Primary-cell design means no battery charger, no UN 38.3 on a pack, but DG shipping rules for lithium metal. Extra pods at €39 with ~€12 landed cost are the sweet margin.

### Go-to-market
**First 100 customers:** mornings outside cash-and-carry wholesalers with a mock-up and a €249 price card (kill question: 10 of 50 owners leave a card); local restaurant associations and HACCP trainers (they teach the course where owners learn they need records — your flyer belongs in that course); food-truck meetups; the catering-equipment dealers who sell fridges (bundle: "logger included").

**Scale channels:** catering wholesalers and their web shops (the same ones selling the €54 BT logger), commercial-fridge manufacturers (OEM bundle), HACCP software vendors (API integration), national hospitality associations' member offers.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Cash-and-carry mornings + 20 kitchens with works-like kits (dev boards in printed cases) for 8 weeks; firmware v0 with PDF. |
| Q2 | Custom hub and pod PCBs; antenna work in steel fridges; tooling; EVT 50 kits; pre-compliance. |
| Q3 | DVT, certification, 300-kit pilot; wholesaler listing; calibration-cert service. |
| Q4 | 1,000 kits; fridge-OEM bundle talk; two countries' HACCP guidance mapped into firmware templates. |

**Team:** 1 embedded/RF engineer (802.15.4, low power, e-paper — full-time), 1 firmware/web developer (HACCP workflow, PDF, email — full-time), founder for sales/ops with hospitality contacts; mechanical and compliance bought in. Three people.

**Funding to first 1,000 kits (estimates):** NRE €65k (PCBs €15k, tooling for 2 housings €22k, antenna/RF €8k, software €20k) + certification €35k + 1,000 kits landed ~€100k + 9 months salaries/overheads €90k ≈ **€290k**; minus pre-orders (300 × €249 ≈ €75k) and pilot sales (~€75k) ≈ **~€140k**. Route: pre-orders + a food-tech/SME digitalisation grant (several EU countries subsidise digital HACCP for SMEs) + an angel from hospitality supply. The 16–20-week effort estimate is honest; don't promise a quarter.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** radio out of a steel fridge; ≥1-year battery | Pod body outside the fridge, probe inside (door-seal cable) as the default; internal pod as the "easy" option with a reduced-range warning; measure in 5 real fridges in week 3 |
| **Technical:** e-paper in a hot, greasy kitchen; USB power loss | Rated e-paper, IP-rated front; supercap/small cell for power-loss logging; hub keeps logging pods' data when power returns |
| **Market:** owners buy the €54 BT logger instead | Sell the inspector-readable wall display and the PDF; demo "the inspector walks in" scenario |
| **Regulatory:** national HACCP guidance differs (intervals, limits) | Templates per country; configurable; state that the business remains responsible for its HACCP plan |
| **Regulatory:** accuracy claims | ±0.5 °C stated, not legal metrology; offer calibration certs against a reference thermometer |
| **Supply:** e-paper panels have long lead times; Li-FeS2 AA DG shipping | Order panels at EVT; qualify two cell brands; consider shipping cells from an EU distributor |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Seeed Grove TempAndHumi Sensor (SHT31) | https://www.gongbans.com/db/seeed-grove-tempandhumi-sensor-sht31.html | ±0.3 °C T/RH reference circuit for the pod | schematic | Seeed wiki resources; check licence |
| Espressif ESP32-C6-DevKitC-1 | https://www.gongbans.com/db/espressif-esp32-c6-devkitc-1.html | Hub/pod MCU reference: WiFi 6 + 802.15.4 (Thread/Zigbee) for sensor links | reference design files per catalogue | Espressif reference designs; module-based production is standard |
| M5Stack PaperS3 (C139) | https://www.gongbans.com/db/m5stack-papers3.html | E-paper hub for the first batches (ESP32-S3, 4.7"-class) | enclosure/structure only | Buy for pilot; your own hub PCB later |
| M5Stack Unit Buzzer (U132) | https://www.gongbans.com/db/m5stack-unit-buzzer.html | Local alarm reference | enclosure/structure only | Buy |

### Block diagram
```
POD (x3):  [SHT3x in pod] [NTC probe, optional] -> [ESP32-C6] --802.15.4 (Thread/Zigbee)--> HUB
           [2x AA Li-FeS2] -> [LDO]   [magnet IP54 case] [antenna lead to door seal]
HUB:       [ESP32-S3/C6] -> [4.7" e-paper] [buzzer] [2 buttons: ack / corrective action]
           [flash: 2 yrs log] --WiFi (optional)--> [weekly PDF e-mail, CSV]  [USB-C 5 V]
```
**Engineering gap:** the catalogue has the sensors and the radios, nothing for the kitchen. Missing: pod mechanical/antenna design that survives steel, grease and a 1-year battery; an 802.15.4 link with factory pairing; the HACCP workflow firmware and PDF signing; the e-paper UI an inspector understands in 5 seconds. Firmware is more than half the effort.

### Starter BOM (estimates per kit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-C6 module ×3 (pods) | €6.60 | Pre-certified; multi-source modules exist |
| ESP32-S3 (or C6) module for hub | €2.60 | |
| SHT3x-class T/RH ×3 | €5.40 | Multi-source |
| NTC probe with 1 m cable ×1 (freezer) | €2.50 | Food-grade stainless tip; probe in a glycol bottle avoids food contact |
| 4.7"-class e-paper panel + driver | €22.00 | **Lead time 6–12 weeks; single-source per panel model** |
| AA Li-FeS2 ×6 + holders | €8.40 | DG goods; two brands |
| Buzzer, buttons, USB-C PSU, passives, PCBs ×4 | €9.50 | |
| Hub shell + 3 IP54 pods with magnets and gaskets | €10.50 | **Tooling €18–25k** (two moulds) |

### Firmware/software starting point
- ESP-IDF; OpenThread is integrated in ESP-IDF for the C6 (Espressif's esp-thread examples exist); Zigbee via esp-zigbee-sdk. Thread is simpler for a private hub–pod network.
- E-paper: M5Stack's M5EPD/M5Unified libraries for PaperS3 in the pilot; for your own hub, search for an ESP32 e-paper driver matching your panel (vendor sample code is normal).
- Sensirion publishes SHT3x embedded drivers on GitHub.
- PDF generation on-device is painful: generate a compact log and render the PDF on a tiny server or in the hub's web page with a JS PDF library (search "jsPDF"). Email via SMTP from ESP32 is feasible (search "ESP-Mail-Client").

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 3 mornings at cash-and-carry entrances with a PaperS3 mock-up and a price card; **10 of 50 owners leave a pre-order card**. Also: works-like with C6 devkit pods + PaperS3 hub logging 3 fridges |
| 3–5 | Works-like | 20 kitchens running works-like kits; weekly PDF emailed; link reliability > 99% from inside 5 fridge models with the door-seal antenna; power budget model says ≥ 12 months |
| 6–8 | Looks-like + EVT | Custom pod + hub PCBs; printed/soft-tooled housings; 50 kits; IP54 test; grease/heat soak; EMC pre-scan |
| 9–10 | DVT + pre-compliance | RED/EMC pre-compliance; EN 18031 self-assessment; battery life measured at −20 °C; PDF signing and tamper-evidence reviewed by a HACCP consultant |
| 11–12 | Pilot batch | 50 kits sold to pre-order customers; inspector feedback from ≥ 3 inspections; ≤ 3% support tickets per week |

### Certification checklist (EU)
- **CE under RED:** EN 300 328 (2.4 GHz WiFi + 802.15.4), EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** safety (mains PSU: buy a certified adapter); **EN 18031-1** (internet-connected via WiFi) — mandatory since 1 Aug 2025; -2 not needed if no personal data (don't collect staff names on device, or if you do, add -2). Est. €6–9k RED/EMC, €3–5k safety, €10–18k EN 18031.
- **RoHS, REACH, WEEE** per country; **Packaging** waste registration (DE LUCID etc.).
- **Battery Regulation (EU) 2023/1542**: AA lithium metal cells = portable batteries, labelling + removable (they are). Transport: UN 3091 "contained in equipment" — labels and forwarder paperwork; no UN 38.3 on a pack if cells are off-the-shelf tested cells.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: signed OTA, SBOM, vulnerability contact — the signed PDF chain is a selling point here.
- **GDPR:** temperatures aren't personal; the owner's email and any staff "acknowledged by" entry are — minimal privacy notice; keep data on the hub.
- **Food contact:** none if probes sit in a glycol bottle; a stainless food probe needs a food-contact declaration (EU 1935/2004) from the probe supplier.
- **Metrology:** not a legal measuring instrument; state accuracy and offer calibration certificates.
- **Total certification budget estimate: €25–40k.**

### Validation toolkit
- **Kill question:** A morning outside a cash-and-carry with the mock-up and a €249 price card: do 10 of 50 owners leave a card for pre-order?
- **Cheapest experiment (~€700):** PaperS3 + 3 C6 devkits + Grove SHT31 in printed pods, a fake PDF report printed on paper, a price card, and 3 mornings. Collect cards with a €1 deposit via QR to make it real.
- **5-question interview (owner/chef):** 1) How do you record fridge temperatures today, and who does it? 2) When was your last inspection and what did they ask for? 3) How many cold units, and which one worries you (walk-in, chest freezer)? 4) Do you have WiFi in the kitchen that actually works? 5) €249 once, no subscription — would you buy today, and what would make you say no?
- **Landing page:** headline "Your HACCP temperature log, done. No subscription." Bullets: "Stick-on sensors for every fridge and freezer; a wall display the inspector can read." / "Weekly signed PDF by email, 2 years stored on the device." / "€249 once. Extra sensors €39."
- **Pass threshold:** 50 pre-orders with a €25 deposit in 6 weeks, or 10 of 50 cards in one morning.

### First production checklist
- Samples: 5 golden kits with sensor calibration records (ice bath + reference thermometer), RF range logs, PDF samples.
- DFM: pod gasket and magnet retention, antenna lead strain relief, hub e-paper mounting without pressure points; test jig with a cold plate.
- MOQ talk: e-paper 500–1k (order early); housings 1k each; cells via EU distributor to dodge DG shipping for batch one.
- QC: AQL II 2.5/4.0; 100% RF + pairing test; 100% sensor check at one temperature; 5% sample at −20 °C; IP54 sample test.
- Packaging: kit box with quick-start printed inside the lid; glycol bottle included; lithium labels.
- Incoterms: FOB Shenzhen; DG lithium surcharge; consider EU final assembly of pods (insert cells, pack) to simplify DG and let you offer "assembled in EU".

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Seeed Studio and Espressif and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-TempAndHumi Sensor-SHT31](/db/seeed-grove-tempandhumi-sensor-sht31.html) (±0.3 °C temperature/humidity sensor reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c6-devkitc-1](/db/espressif-esp32-c6-devkitc-1.html) (hub MCU: WiFi 6 plus 802.15.4 for sensor links when kitchen WiFi is flaky). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (e-paper hub display for the first batches); [M5Stack Unit Buzzer (U132)](/db/m5stack-unit-buzzer.html) (local alarm when a fridge drifts). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **iDisc Technology** (深圳市艾迪思科技有限公司) · no website on file — E-ink display module / e-reader OEM: E-ink display module; e-reader gongban; retail price tag; OEM/ODM. *(E-ink display modules)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and Espressif and M5Stack websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132) — for a HACCP Fridge Logger

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a HACCP Fridge Logger: Stick-on fridge and freezer sensors plus a kitchen e-paper display that keeps the legally required HACCP temperature log and emails the PDF weekly — buy once, no monthly fee. The design is built around your Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132).

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132).
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
主题：样品订购及批量报价 — Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132) — 用于HACCP Fridge Logger

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款HACCP Fridge Logger：Stick-on fridge and freezer sensors plus a kitchen e-paper display that keeps the legally required HACCP temperature log and emails the PDF weekly — buy once, no monthly fee。产品设计基于贵司的Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132)。
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
Subject: PCBA quote from open design files — HACCP Fridge Logger, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a HACCP Fridge Logger: Stick-on fridge and freezer sensors plus a kitchen e-paper display that keeps the legally required HACCP temperature log and emails the PDF weekly — buy once, no monthly fee. The design starts from published open-hardware files (Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — HACCP Fridge Logger，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款HACCP Fridge Logger：Stick-on fridge and freezer sensors plus a kitchen e-paper display that keeps the legally required HACCP temperature log and emails the PDF weekly — buy once, no monthly fee。设计基于已公开的开源硬件文件（Seeed Grove-TempAndHumi Sensor-SHT31, Espressif esp32-c6-devkitc-1, M5Stack PaperS3 (C139), M5Stack Unit Buzzer (U132)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order a PaperS3, 3× ESP32-C6 devkits, 3× Grove SHT31 and 10 AA lithium cells; get one pod reporting from inside your own fridge to the e-paper.
2. Print a price card and a mock PDF; book three mornings at a cash-and-carry (ask permission at the entrance desk).
3. Download your country's official HACCP guidance for small kitchens and turn the temperature rules into the firmware limit table — it is your spec.

Want help sourcing or building this? Talk to us via www.gongbans.com.
