# Emergency Light Test Logger — Founder Start Pack

> A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Emergency lighting must be tested and the tests logged; in older buildings an electrician walks round with a clipboard, and the self-test systems that would automate it are sold with new luminaires, not for the thousands already on the ceiling.
- **Customer:** Facility managers and housing associations with older buildings, and the electrical contractors who perform the tests for them; the facility or maintenance budget pays, the contractor installs and reads the log.
- **Product:** A coin-cell light-sensor node stuck to each luminaire, reporting over LoRaWAN whether and how long the lamp lit during the function and duration tests, and a server that assembles the per-building test log; sold as evidence that supports the mandatory record. Target price €49–79 (estimate).
- **Why now:** EN 50172 / DIN VDE 0108 require periodic, logged emergency-lighting tests, self-test systems (IEC 62034) only come with new installations, and the building stock is full of old luminaires whose test log is a clipboard walked round by an electrician.
- **The ask:** ~€35–45k to certification and a first 2,000 nodes (estimate); three pilots cover a fifth.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** EN 50172 / DIN VDE 0108 genuinely require periodic tested-and-logged emergency-lighting checks, and self-test systems (Zumtobel, Legrand and others under IEC 62034) only cover new installations, which confirms the older-luminaire gap. **Main risk:** A light-sensor "it lit" reading is not the standard's duration test (which concerns battery-backed runtime); whether inspectors accept this log as compliance evidence is a genuinely open question, stated in the pack and asked in the kill question. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 facility managers or 2 electrical contractors install a paid pilot of 50 nodes at €59, run one quarterly cycle, and does at least one inspector or insurer accept the generated log alongside the manual record? Pass = 3 pilots and 1 written acceptance in 12 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Facility managers of schools, housing blocks, offices and halls with older emergency lighting; electrical contractors who perform and log the tests; housing associations.

**The problem as the pack states it:** Emergency lighting must be tested and the tests logged; in older buildings an electrician walks round with a clipboard, and the self-test systems that would automate it are sold with new luminaires, not for the thousands already on the ceiling.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.
- **r/electricians** · https://www.reddit.com/r/electricians/ — working electricians.
- **FPA, Fire Protection Association (UK)** · https://www.thefpa.co.uk/ — fire-safety professionals.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€49–79, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how facility managers of schools, housing blocks, offices and halls with older emergency lighting deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you test and log the emergency lighting today, how long does a round take, and what did the last inspection say about the log?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself. On a scale of one to ten, how likely would you be to buy that at €49–79, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Emergency Light Test Logger: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Emergency Light Test Logger: A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself. Before we spend money on tooling I want to find out whether this solves a real problem for facility managers of schools, housing blocks, offices and halls with older emergency lighting.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €49–79 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

EN 50172 and DIN VDE 0108 (and their national equivalents) require a monthly function test and an annual duration test of every emergency luminaire, with a log. Self-test systems under IEC 62034 do this automatically, but only in new installations (Zumtobel, Legrand, Eaton and others sell them with the luminaires). For the older stock the test is manual and the log is paper. One thing this pack states plainly and does not resolve: a light sensor reading "it lit for 61 minutes" is evidence that light was emitted during a test, not the standard's duration test itself, which concerns the battery-backed runtime of the luminaire; whether an inspector or insurer accepts the generated log as compliance evidence is a genuinely open question, and the kill question asks it.

**Who pays, B2B:** the facility manager or housing association; electrical contractors buy for their customers and resell the service. **Who uses:** the contractor on test day and the facility manager when the inspector comes.

### Market size (estimates — check)

- **TAM:** emergency luminaires in EU non-residential and multi-family buildings without self-test: estimate 50–100M. Theoretical €3B+ at €59.
- **SAM:** buildings managed by professional facility managers with a LoRaWAN or willing to add a gateway: estimate 5M luminaires → €300M.
- **SOM (3 yrs):** 100,000–200,000 nodes; year-1: 5,000–10,000 across three pilots and two contractors.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Self-test / DALI emergency systems (Zumtobel, Legrand, Eaton; IEC 62034) | Automatic testing built into new luminaires | Retrofit on old luminaires without replacing them; we complement new-build systems |
| Inspection and maintenance software subscriptions | Digital clipboards for the contractor | We add the sensor evidence; can feed their logs |
| Replacing luminaires with self-test models | €100–300 per luminaire installed (estimate) | A fraction of that per point |
| The clipboard | Free | No evidence, no timestamps, no duration record |

**Wedge:** sensor evidence for the mandatory test log on the luminaires nobody will replace, at a tenth of a replacement, with the limits of that evidence stated.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Eaton emergency-lighting inspection and maintenance guide | Periodic function and duration tests with a log | Compliance pull confirmed |
| DIN VDE 0108 test-log guidance (Whitecroft) | Log requirements | Same |
| Fagerhult self-test / EN 62034 explainer | Self-test systems for new luminaires | Gap for older stock confirmed |

**Verdict as researched: LIKELY.** Main risk: A light-sensor "it lit" reading is not the standard's duration test (which concerns battery-backed runtime); whether inspectors accept this log as compliance evidence is a genuinely open question, stated in the pack and asked in the kill question.
<!-- market-competitors:end -->

### Product & value proposition

- Node: light sensor facing the luminaire, coin cell for two years (estimate), LoRaWAN uplink of light-on / light-off timestamps; adhesive and magnetic mounts; tamper flag.
- Test flow unchanged: the electrician triggers the function or duration test as today; the nodes record who lit and for how long; the server builds the per-building log with exceptions (did not light, lit under 60/180 minutes).
- Export in the format the contractor's log already uses; API; no per-node licence.
- Clear statement in manual and log: supports the record; the duration test's battery criterion remains the luminaire's own; acceptance by inspectors to be confirmed locally.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €8–14) | 11.0 | 8.8 |
| PCBA assembly + test | 1.5 | 1.0 |
| Enclosure / mechanics (tooling amortised separately) | 2.0 | 1.4 |
| Packaging, cable, leaflet | 1.0 | 0.8 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 1.0 | 0.5 |
| Certification amortised (€8k, estimate) | 8.0 | 1.6 |
| **Landed cost** | **24.5** | **14.0** |
| Channel cost (contractor channel, ~€8) | 8.0 | 8.0 |
| Net price received (€64 incl. 19% VAT → €53.8 ex VAT) | 53.8 | 53.8 |
| **Gross margin per unit** | **€21.3 (40%)** | **€31.8 (59%)** |

Lesson: a node is cheap; the gateway and the server are per building and should be priced as a kit; volume comes in hundreds per building.

### Go-to-market

**First 100 customers:**

1. Three facility managers with old stock and an upcoming inspection, each a 50-node paid pilot.
2. Two electrical contractors who test for many buildings and resell the service.
3. A housing association as the multi-building reference.

**Scale channels:** electrical contractors, facility-management associations (GEFMA, IFMA), LoRaWAN integrators, insurers' loss-prevention teams.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations incl. an inspector; works-like node on Stamp C6LoRa + DLight; log format from one contractor. |
| Q2 | Custom node PCB; EVT 100 nodes in two buildings; one quarterly cycle logged. |
| Q3 | DVT; certification; 5,000 nodes; pilots shipped; inspector feedback documented. |
| Q4 | Contractor channel; 20,000 nodes; insurer conversation. |

**Team:** one embedded engineer, one backend developer, one founder with facility-management or electrical-contracting background.

**Funding to first production (estimates):** NRE €12k + certification €8k + first 2,000 nodes landed ~€24k ≈ €44k; minus pilots ~€9k ≈ €35k.

### Top risks

| Risk | Mitigation |
|---|---|
| Inspectors do not accept the sensor log as evidence | State the limit up front; sell as support to the manual record; get one written acceptance in the pilot before scaling |
| Light sensor reads ambient light instead of the luminaire | Mounting guidance, shielded sensor, baseline reading per node |
| Buildings have no LoRaWAN | Gateway in the kit; Cat-M gateway option |
| Coin-cell life | Report only on events; two-year estimate validated in EVT |

## 4. Start kit

### Boards to start from

- [M5Stack Unit DLight (U136)](https://www.gongbans.com/db/m5stack-unit-dlight.html) — ambient-light unit for the first prototype node (design files published for the module; electronics not open)
- [Seeed Grove-Digital Light Sensor](https://www.gongbans.com/db/seeed-grove-digital-light-sensor.html) — open digital light-sensor reference circuit (open files: schematic)
- [M5Stack Unit Light (U021)](https://www.gongbans.com/db/m5stack-unit-light.html) — simple light sensor, second source (design files published for the module; electronics not open)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — open ESP32-C6 + LoRa core for the node (open files: pcb,schematic)
- [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html) — EU868 LoRaWAN module for the prototype run (design files published for the module; electronics not open)

The Seeed light sensor publishes its schematic; the M5Stack light units are the prototype path; the Stamp C6LoRa (open PCB and schematic) is the node core.

### Block diagram

```
  LUMINAIRE: [light sensor facing the lamp] -> [ESP32-C6 + LoRa node, coin cell] -> LoRaWAN gateway (building)
  TEST DAY: electrician triggers test as today -> nodes report lit / not lit / duration
  SERVER: per-building test log, exceptions, export to the contractor's record  (evidence, not the duration test itself)
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| Light sensor | 1.0 |  |
| ESP32-C6 + LoRa module | 5.0 |  |
| Coin cell + holder | 1.0 |  |
| Enclosure + adhesive/magnet | 2.0 |  |
| PCB, passives | 1.5 |  |

### Firmware/software starting point

- ESP-IDF; light threshold with per-node baseline; event-based uplinks (lit, off, duration); deep sleep; LoRaWAN class A.
- Server: building and luminaire register, test sessions, exception rules, export in the contractor's log format; API.

### 12-week build plan

1. Interviews incl. an inspector and two contractors; pilot proposals
2. Prototype node
3. Baseline and threshold logic
4. Mounting tests on luminaire types
5. Node PCB v1
6. Server and log format
7. EVT 100 nodes in two buildings
8. One test cycle logged
9. Inspector review of the log
10. DVT
11. Pre-compliance
12. Certification; pilot roll-out

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.
- Not emergency-lighting equipment: the node does not alter the luminaire; say so in the manual.

### Validation toolkit

- **Kill question:** Do 3 facility managers or 2 electrical contractors install a paid pilot of 50 nodes at €59, run one quarterly cycle, and does at least one inspector or insurer accept the generated log alongside the manual record? Pass = 3 pilots and 1 written acceptance in 12 weeks.
- **Cheapest experiment:** Twenty prototype nodes in one building for one monthly function test, the log shown to the contractor and, if possible, the inspector; ask whether they would pay €59 per point.
- **5-question interview:** 1) How do you test and log emergency lighting today, and how long does a round take? 2) What did the last inspection say about the log? 3) Who pays for the testing and what does it cost per year? 4) Would an automated log of 'lit / duration' help, and who would need to accept it? 5) At €59 per luminaire, how many buildings?
- **Landing page:** headline "The emergency-lighting test log, from a €59 sticker." Bullets: works on the luminaires you have; function and duration tests recorded; your contractor's format; evidence for the record, not a replacement for the test. Button: request a pilot (B2B).
- **Pass threshold:** 3 pilots and one written acceptance by an inspector or insurer within 12 weeks.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit DLight (U136)](/db/m5stack-unit-dlight.html) (ambient-light unit for the first prototype node); [M5Stack Unit Light (U021)](/db/m5stack-unit-light.html) (simple light sensor, second source); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core for the node); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN module for the prototype run). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Digital Light Sensor](/db/seeed-grove-digital-light-sensor.html) (open digital light-sensor reference circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor — for a Emergency Light Test Logger

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Emergency Light Test Logger: A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself. The design is built around your M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor.
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
主题：样品订购及批量报价 — M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor — 用于Emergency Light Test Logger

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Emergency Light Test Logger：A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself。产品设计基于贵司的M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor。
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
Subject: PCBA quote from open design files — Emergency Light Test Logger, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Emergency Light Test Logger: A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself. The design starts from published open-hardware files (M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Emergency Light Test Logger，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Emergency Light Test Logger：A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself。设计基于已公开的开源硬件文件（M5Stack Unit DLight (U136), M5Stack Unit Light (U021), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Digital Light Sensor；含原理图、PCB和BOM），并做了我们自己的修改。

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
