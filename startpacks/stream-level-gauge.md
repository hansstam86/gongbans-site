# Stream Level Gauge — Founder Start Pack

> A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The official gauge network covers the big rivers; the stream that floods the village underpass has no gauge, and the official instruments that could watch it cost €2,000–6,000 each, so the fire brigade finds out from a phone call.
- **Customer:** Municipalities (civil protection and public works), water boards, volunteer fire brigades, and the TTN communities already building sensors with them; the municipality's flood-protection or smart-city budget pays.
- **Product:** An IP67 ultrasonic level sensor on a bridge rail or post, solar-powered, reporting every 10 minutes (every minute when rising fast) over LoRaWAN or Cat-M to a public dashboard with alert rules; advisory status stated on every screen and in the contract. Target price €399–599 (estimate).
- **Why now:** Hennef installed a community-built level sensor on a public bridge feeding its smart-city map, and Bergisch Gladbach gauges the Strunde the same way: municipalities take these sensors up when they exist; the official gauges cost thousands and are placed only on larger rivers.
- **The ask:** ~€60–80k to certification and a first 300 gauges (estimate); three pilots cover a fifth.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Strong confirmed precedent: a community-built sensor in Hennef was installed by the city on a public bridge and feeds a public smart-city map, real institutional pickup; TTN Bergisch Gladbach gauges the Strunde the same way. OTT ecoLog represents the official instrument class. **Main risk:** Liability: positioned as advisory, not an official gauge, given the flood-safety stakes; the pack says so in contract, manual and dashboard. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 municipalities or one water board sign a paid 10-gauge advisory pilot at €499 within one budget cycle, with the advisory status accepted in writing? Pass = 3 signed pilots (or 1 water board) in 12 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Municipalities, water boards and volunteer fire brigades in flood-prone regions (post-2021 budgets in DE/BE/NL; EU Floods Directive planning), TTN communities that already build such sensors.

**The problem as the pack states it:** The official gauge network covers the big rivers; the stream that floods the village underpass has no gauge, and the official instruments that could watch it cost €2,000–6,000 each, so the fire brigade finds out from a phone call.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€399–599, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how municipalities, water boards and volunteer fire brigades in flood-prone regions (post-2021 budgets in DE/BE/NL deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last time the stream flooded: how did you find out, and how early could you have known?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge. On a scale of one to ten, how likely would you be to buy that at €399–599, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Stream Level Gauge: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Stream Level Gauge: A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge. Before we spend money on tooling I want to find out whether this solves a real problem for municipalities, water boards and volunteer fire brigades in flood-prone regions (post-2021 budgets in DE/BE/NL.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €399–599 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

The precedent is strong and institutional: TTN Rhein-Sieg's sensor in Hennef was installed by the city on a public bridge and feeds its public smart-city map; TTN Bergisch Gladbach gauges the Strunde. Official instruments (OTT ecoLog and similar) are excellent and priced for the state gauge network. The liability point must be plain: this is an advisory sensor for local awareness and early mobilisation, not an official gauge and not a substitute for the state warning service; the pack, the dashboard and the contract say so.

**Who pays, B2G:** the municipality or water board; sometimes the fire brigade's association or a regional flood-protection programme. **Who uses:** the fire brigade's duty officer (alerts), public works (trends), residents (the public map).

### Market size (estimates — check)

- **TAM:** small streams with flood history in DE/BE/NL/AT/CH: estimate 50,000 sites worth gauging; theoretical €25M at €499.
- **SAM:** municipalities with a flood-protection budget and a LoRaWAN or willingness to use Cat-M: estimate 3,000 municipalities × 5 gauges → €7.5M.
- **SOM (3 yrs):** 2,000–4,000 gauges; year-1: 150–300 across three pilots and a water board.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| OTT ecoLog and official gauge loggers (SEBA, Hydro-Met) | €2,000–6,000 class instruments for the state network (research, Nov 2026) | A tenth of the price for advisory use; we do not compete for official gauges |
| TTN community sensors (Hennef / Rhein-Sieg, Bergisch Gladbach Strunde) | Volunteer-built, city-installed | The precedent; we add a product, a warranty and the dashboard |
| State warning services (Hochwasserzentralen) | Official, river-scale | We are upstream of them, on streams they do not cover; link to them, never replace |
| Phone calls and a resident who looks out of the window | Free | The alert at 3 a.m. is the product |

**Wedge:** an advisory gauge at a tenth of the official price, building on the sensor municipalities already accepted from their TTN communities, with alerts the fire brigade can act on.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| TTN Rhein-Sieg Hennef sensor | Community sensor installed by the city on a public bridge, public map | Institutional pickup confirmed |
| TTN Bergisch Gladbach Strunde sensor | Community stream gauge | Precedent |
| OTT ecoLog | Official gauge logger class | Incumbent for official gauges, €2–6k class |

**Verdict as researched: LIKELY.** Main risk: Liability: positioned as advisory, not an official gauge, given the flood-safety stakes; the pack says so in contract, manual and dashboard.
<!-- market-competitors:end -->

### Product & value proposition

- Downward ultrasonic sensor (0.3–6 m), temperature-compensated, surface-noise filtering; mounting kit for bridge rails and posts; IP67.
- Solar panel and cell for a northern winter at 10-minute uplinks, 1-minute when rising fast (estimate; validate in December).
- LoRaWAN (city or TTN) or Cat-M; store-and-forward on link loss.
- Dashboard: public map and graph, alert rules (level, rate of rise), SMS/e-mail/app to the duty officer; "advisory sensor, not an official gauge" on every screen; API for the city's systems.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €80–130) | 105.0 | 84.0 |
| PCBA assembly + test | 10.0 | 6.5 |
| Enclosure / mechanics (tooling amortised separately) | 35.0 | 24.5 |
| Packaging, cable, leaflet | 6.0 | 4.5 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 8.0 | 4.0 |
| Certification amortised (€12k, estimate) | 12.0 | 2.4 |
| **Landed cost** | **176.0** | **125.9** |
| Channel cost (direct B2G and integrator channel, ~€45) | 45.0 | 45.0 |
| Net price received (€499 incl. 19% VAT → €419.3 ex VAT) | 419.3 | 419.3 |
| **Gross margin per unit** | **€198.3 (47%)** | **€248.4 (59%)** |

Lesson: the mount and the housing are half the cost; one housing for rail and post. Dashboard hosting at cost; the alert rules are what the brigade pays attention to.

### Go-to-market

**First 100 customers:**

1. Three municipalities with recent flood damage, approached with their TTN community and their fire brigade.
2. One water board for a catchment of ten streams.
3. Regional flood-protection programmes that fund municipal sensors.

**Scale channels:** municipal associations, TTN communities, LoRaWAN integrators, fire-brigade associations.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations with municipalities and one water board; works-like gauge on Stamp C6LoRa + Unit Ultrasonic at one stream; advisory wording agreed with a municipal lawyer. |
| Q2 | Custom board; housing and mounts; EVT 10 at real sites over a wet season; dashboard v0. |
| Q3 | DVT; certification; 100 gauges; pilots shipped. |
| Q4 | Water-board catchment; 300 gauges; alert integrations. |

**Team:** one embedded engineer, one backend developer, one founder who speaks to municipalities and fire brigades; housing design bought in.

**Funding to first production (estimates):** NRE €24k + certification €10k + first 300 gauges landed ~€40k ≈ €74k; minus pilots ~€15k ≈ €60k.

### Top risks

| Risk | Mitigation |
|---|---|
| Liability if a flood is not warned | Advisory status in contract, dashboard and manual; no safety claim; the brigade's own procedures stay; insurance priced in |
| Accuracy in wind, foam, ice | Filtering, mounting guidance, temperature compensation; rate-of-rise is the robust signal |
| Winter power budget | Measure in December; larger panel or mains where available |
| Permits to mount on bridges | Municipality owns the bridge in the pilot; mounting kit for rails without drilling |

## 4. Start kit

### Boards to start from

- [M5Stack Unit Ultrasonic-I2C (U098-B1)](https://www.gongbans.com/db/m5stack-unit-ultrasonic-i2c.html) — ultrasonic distance to the water surface (design files published for the module; electronics not open)
- [Seeed Grove-Ultrasonic Ranger](https://www.gongbans.com/db/seeed-grove-ultrasonic-ranger.html) — open ultrasonic ranger reference circuit (open files: schematic)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — open ESP32-C6 + LoRa core (open files: pcb,schematic)
- [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html) — EU868 LoRaWAN module for the prototype (design files published for the module; electronics not open)
- [M5Stack Unit CatM (U128)](https://www.gongbans.com/db/m5stack-unit-catm.html) — Cat-M fallback where no LoRaWAN exists (design files published for the module; electronics not open)
- [DFRobot DFR0535](https://www.gongbans.com/db/dfrobot-dfr0535.html) — solar power manager for the post (open files: schematic)

The Stamp C6LoRa publishes PCB and schematic; the Seeed ranger publishes its schematic; the M5Stack units and the DFRobot solar manager are the quickest prototype path.

### Block diagram

```
  BRIDGE RAIL: [ultrasonic sensor, downward] -> [ESP32-C6 + LoRa / Cat-M] -> LoRaWAN / cellular -> dashboard
               [solar panel + cell]  [temp sensor]   every 10 min; 1 min when rising fast
  DASHBOARD: public map + graph; alert rules -> fire brigade duty officer;  'advisory, not an official gauge'
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| Ultrasonic sensor, outdoor grade | 18.0 |  |
| ESP32-C6 + LoRa module (or + Cat-M) | 8.0 | +15 for Cat-M |
| Solar panel 5–10 W + power manager | 15.0 |  |
| LiFePO4 cell | 10.0 |  |
| IP67 housing + rail/post mount | 35.0 |  |
| PCB, temp sensor, passives | 6.0 |  |

### Firmware/software starting point

- ESP-IDF; median and outlier filtering, temperature compensation, adaptive uplink rate on rate of rise; store-and-forward.
- Dashboard: open-source ingest, public map, alert engine (level, rate), SMS/e-mail; API; advisory label hard-coded.

### 12-week build plan

1. Interviews with municipalities, brigade, water board; advisory wording
2. Prototype at one stream
3. Filtering and rate-of-rise logic
4. Housing and mount
5. Custom board v1
6. Dashboard v0 and alerts
7. EVT 10 over a wet season
8. Brigade feedback
9. Winter power check
10. DVT
11. Pre-compliance
12. Certification; pilot deliveries

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.
- Not a measuring instrument under metrology law and not a safety device: say so in the manual, the contract and on the dashboard.

### Validation toolkit

- **Kill question:** Do 3 municipalities or one water board sign a paid 10-gauge advisory pilot at €499 within one budget cycle, with the advisory status accepted in writing? Pass = 3 signed pilots (or 1 water board) in 12 weeks.
- **Cheapest experiment:** One prototype on the bridge of the stream that last flooded, data on a public page for a season; ask the municipality and the brigade whether they would buy ten at €499 as advisory sensors.
- **5-question interview:** 1) Tell me about the last flood on a stream without a gauge: how did you find out? 2) What do official gauges cost you and where are they? 3) Who decides on civil-protection purchases and what is the budget? 4) Would an advisory sensor fit your procedures, and what wording would your lawyer want? 5) At €499 per gauge, how many streams?
- **Landing page:** headline "Watch the stream before it reaches the village." Bullets: solar, LoRaWAN or cellular, public map, alerts to the brigade; advisory sensor, not an official gauge; €499. Button: request a pilot (B2G).
- **Pass threshold:** 3 signed advisory pilots (or one water board) within 12 weeks.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.
- Outdoor: IP67 immersion test; mount load test; label with the advisory statement.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and Seeed Studio and DFRobot).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Ultrasonic-I2C (U098-B1)](/db/m5stack-unit-ultrasonic-i2c.html) (ultrasonic distance to the water surface); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN module for the prototype); [M5Stack Unit CatM (U128)](/db/m5stack-unit-catm.html) (Cat-M fallback where no LoRaWAN exists). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Ultrasonic Ranger](/db/seeed-grove-ultrasonic-ranger.html) (open ultrasonic ranger reference circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **DFRobot** — community / maker brand; 250 boards in the catalogue; files via DFRobot wiki catalog · https://wiki.dfrobot.com/. Boards used here: [DFRobot DFR0535](/db/dfrobot-dfr0535.html) (solar power manager for the post). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio and DFRobot websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535 — for a Stream Level Gauge

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Stream Level Gauge: A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge. The design is built around your M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535.
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
主题：样品订购及批量报价 — M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535 — 用于Stream Level Gauge

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Stream Level Gauge：A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge。产品设计基于贵司的M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535。
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
Subject: PCBA quote from open design files — Stream Level Gauge, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Stream Level Gauge: A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge. The design starts from published open-hardware files (M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Stream Level Gauge，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Stream Level Gauge：A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge。设计基于已公开的开源硬件文件（M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit CatM (U128), Seeed Grove-Ultrasonic Ranger, DFRobot DFR0535；含原理图、PCB和BOM），并做了我们自己的修改。

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
