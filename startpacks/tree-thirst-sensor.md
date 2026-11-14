# Tree Thirst Sensor — Founder Start Pack

> A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Young city trees die in dry summers because watering rounds are scheduled, not measured; the departments that have tried sensors pay for a platform per sensor per year, and the ones that have not, water by guesswork.
- **Customer:** Municipal green-space departments (Grünflächenämter), their watering contractors, and housing associations; the department's climate-adaptation or tree-maintenance budget pays, often with regional funding.
- **Product:** A stake with moisture at two depths and soil temperature, a sealed LoRaWAN head with a five-year cell, a soil-type wizard, open decoders for TTN and city networks, and a map plus a watering list, with no per-sensor platform fee. Target price €69–99 (estimate).
- **Why now:** Cities already run funded tree-sensor programmes, the watering of young trees in dry summers is a line item every green department fights over, and the commercial sensors come with a platform fee the municipal IT would rather avoid.
- **The ask:** ~€35–45k to certification and a first 1,000 stakes (estimate); three municipal pilots cover half.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Already-funded municipal programmes exist (Vienna "Internet of Trees", Ludwigsburg, Jena, Pforzheim): live demand, not hypothetical. Treesense and FloraPulse exist as competitors but do not publish pricing. **Main risk:** Get a real competitor quote before claiming to be cheaper. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 cities' green departments order a 50-sensor paid pilot at €89 within one budget cycle? Pass = 3 purchase orders in 12 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Municipal green-space departments with climate-adaptation budgets (Vienna, Ludwigsburg, Jena and Pforzheim already run such programmes), tree-care contractors, housing associations with green space.

**The problem as the pack states it:** Young city trees die in dry summers because watering rounds are scheduled, not measured; the departments that have tried sensors pay for a platform per sensor per year, and the ones that have not, water by guesswork.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/arborists** · https://www.reddit.com/r/arborists/ — tree-care professionals, including municipal crews.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.
- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€69–99, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how municipal green-space departments with climate-adaptation budgets, tree-care contractors, housing associations with green space deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How does your crew decide which young trees get watered this week, and how many did you lose last summer?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee. On a scale of one to ten, how likely would you be to buy that at €69–99, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Tree Thirst Sensor: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Tree Thirst Sensor: A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee. Before we spend money on tooling I want to find out whether this solves a real problem for municipal green-space departments with climate-adaptation budgets, tree-care contractors, housing associations with green space.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €69–99 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

Vienna's "Internet of Trees", Ludwigsburg, Jena and Pforzheim show the demand is live, funded and municipal: sensors in the root zone tell the watering crew which trees need the tanker today. The commercial sensors (Treesense, FloraPulse and others) do not publish prices, so the cost advantage must be confirmed with a quote; what they share is a platform fee, and municipal IT departments that run their own LoRaWAN would rather see the data in their own system.

**Who pays, B2G:** the green-space department, sometimes the city's smart-city or climate programme; watering contractors buy when the city asks for measured watering. **Who uses:** the watering crew (a list of trees to water today) and the arborist (trends per tree).

### Market size (estimates — check)

- **TAM:** young street trees in EU cities (planted within the last five years): estimate 10–20M; one sensor per 5–20 trees in a monitored scheme. Theoretical €100M+.
- **SAM:** cities with a LoRaWAN network and a tree-watering programme: estimate 300 cities × 300 sensors → €8M.
- **SOM (3 yrs):** 20,000–40,000 stakes; year-1: 1,500–3,000 across three pilots and their follow-ons.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Treesense | Tree sensors with platform (whitepaper found; no public pricing) | No platform fee; open decoders; get a quote before claiming cheaper |
| FloraPulse, Agvolution, Plantcare | Agricultural and tree sensors, quote-based | Same |
| City programmes (Vienna Internet of Trees, Ludwigsburg, Jena, Pforzheim) | Already deployed sensor schemes | Demand proof and reference customers to learn from |
| TTN community tree sensors | Volunteer-built stakes | The open precedent; we add a product, a cell life and a calibration |

**Wedge:** no platform fee and open data into the city's own LoRaWAN, with a stake designed for a five-year life in a tree pit.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Vienna Internet of Trees; Ludwigsburg, Jena, Pforzheim programmes | Municipal tree-sensor deployments | Funded demand exists |
| Treesense (whitepaper) | Tree sensors + platform, no public price | Incumbent; quote needed |
| FloraPulse | Plant water-status sensors, no public price | Incumbent; quote needed |

**Verdict as researched: LIKELY.** Main risk: Get a real competitor quote before claiming to be cheaper.
<!-- market-competitors:end -->

### Product & value proposition

- Two capacitive probes (30 and 60 cm) and a temperature sensor in a glass-fibre stake; sealed head with the LoRa core and an AA-class lithium cell for five years (estimate at hourly uplinks).
- Soil-type wizard (sandy, loam, clay, substrate) from a one-off reference reading; drift compensation.
- Open decoders for TTN and the common city LoRaWAN servers; a small map with a "water today" list; CSV and API; no per-sensor fee.
- Installer kit: pilot drill, depth guide, tree-ID tag.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €15–25) | 20.0 | 16.0 |
| PCBA assembly + test | 3.0 | 2.0 |
| Enclosure / mechanics (tooling amortised separately) | 6.0 | 4.2 |
| Packaging, cable, leaflet | 2.0 | 1.5 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 2.5 | 1.2 |
| Certification amortised (€8k, estimate) | 8.0 | 1.6 |
| **Landed cost** | **41.5** | **26.5** |
| Channel cost (direct B2G and contractor channel, ~€10) | 10.0 | 10.0 |
| Net price received (€84 incl. 19% VAT → €70.6 ex VAT) | 70.6 | 70.6 |
| **Gross margin per unit** | **€19.1 (27%)** | **€34.1 (48%)** |

Lesson: the stake and the sealed head are the cost, not the electronics; design for a five-year life or the city buys twice.

### Go-to-market

**First 100 customers:**

1. Three green departments found through the cities' smart-city teams and existing programmes, each with a 50-stake paid pilot.
2. Two watering contractors who want to prove measured watering.
3. Housing associations with new plantings.

**Scale channels:** municipal associations and climate-adaptation programmes, LoRaWAN integrators, tree nurseries that supply the trees.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations with three departments; works-like stake on Stamp C6LoRa + Unit Earth; soil calibration method. |
| Q2 | Custom board and stake; EVT 50 in one city over a summer; map and watering list v0. |
| Q3 | DVT; certification; 1,000 stakes; two pilots shipped. |
| Q4 | Follow-on orders; contractor channel; 3,000 stakes. |

**Team:** one embedded engineer, one developer for decoders and the map, one founder who speaks to municipalities; stake mechanics bought in.

**Funding to first production (estimates):** NRE €14k + certification €8k + first 1,000 stakes landed ~€25k ≈ €47k; minus pilots ~€13k ≈ €34k.

### Top risks

| Risk | Mitigation |
|---|---|
| Cheap capacitive probes drift and corrode | Coated probes, drift compensation, field test over a summer; reference reading at install |
| Cities already have a vendor | No fee and open data are the switch argument; integrate with their network, not against it |
| Procurement cycles | Pilots under tender thresholds; regional funding calls |
| Vandalism / mowers | Flush stake head, bright tag, replaceable head |

## 4. Start kit

### Boards to start from

- [M5Stack Unit Earth (U019)](https://www.gongbans.com/db/m5stack-unit-earth.html) — soil moisture unit for the first prototype (design files published for the module; electronics not open)
- [M5Stack Unit Watering (U101)](https://www.gongbans.com/db/m5stack-unit-watering.html) — capacitive soil moisture + pump reference (design files published for the module; electronics not open)
- [DFRobot SEN0114](https://www.gongbans.com/db/dfrobot-sen0114.html) — soil moisture sensor, second source (open files: schematic)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — open ESP32-C6 + LoRa core (open files: pcb,schematic)
- [Seeed Grove-TemperatureAndHumidity Sensor-HDC1000](https://www.gongbans.com/db/seeed-grove-temperatureandhumidity-sensor-hdc1000.html) — soil / air temperature reference circuit (open files: schematic)

The Stamp C6LoRa publishes PCB and schematic; the M5Stack and DFRobot moisture boards give three probe options for the prototype; the Seeed sensor board is the open temperature reference.

### Block diagram

```
  TREE PIT: [capacitive probe 30 cm] [capacitive probe 60 cm] [soil temp] -> [ESP32-C6 + LoRa head, sealed] -> city LoRaWAN / TTN
                                                                    [AA lithium cell, 5 years]
  SERVER: open decoder -> map + 'water today' list -> watering crew
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| Capacitive probes ×2 (coated) | 4.0 |  |
| Temperature sensor | 1.0 |  |
| ESP32-C6 + LoRa module | 6.0 |  |
| Lithium AA-class cell | 2.5 |  |
| Stake + sealed head + tag | 6.0 |  |
| PCB, passives | 2.5 |  |

### Firmware/software starting point

- ESP-IDF; hourly uplink, daily temperature profile; soil-type model; LoRaWAN class A with ADR.
- Decoders published for TTN, ChirpStack and the common municipal servers; map and list as a small open-source app.

### 12-week build plan

1. Interviews with green departments; pilot proposal
2. Prototype stake
3. Soil calibration experiments
4. Stake mechanics
5. Custom board v1
6. Decoders and map v0
7. EVT 50 in one city
8. Summer drift review
9. Head sealing test
10. DVT
11. Pre-compliance
12. Certification; pilot deliveries

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 3 cities' green departments order a 50-sensor paid pilot at €89 within one budget cycle? Pass = 3 purchase orders in 12 weeks.
- **Cheapest experiment:** Ten prototype stakes in one city's new plantings for a summer, the watering list sent to the crew weekly; ask the department whether they would buy 50 at €89.
- **5-question interview:** 1) How do you decide which trees get watered this week? 2) Have you trialled sensors; what did the platform cost? 3) Who signs a €5k pilot and from which budget line? 4) Which LoRaWAN do you have? 5) At €89 per stake with no fee, how many trees?
- **Landing page:** headline "Water the trees that are thirsty." Bullets: two depths, five years, your LoRaWAN, no platform fee, €89. Button: request a pilot (B2G).
- **Pass threshold:** 3 purchase orders of 50 within 12 weeks.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.
- Outdoor: IP67 immersion test on heads; probe coating inspection.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and DFRobot and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Earth (U019)](/db/m5stack-unit-earth.html) (soil moisture unit for the first prototype); [M5Stack Unit Watering (U101)](/db/m5stack-unit-watering.html) (capacitive soil moisture + pump reference); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **DFRobot** — community / maker brand; 250 boards in the catalogue; files via DFRobot wiki catalog · https://wiki.dfrobot.com/. Boards used here: [DFRobot SEN0114](/db/dfrobot-sen0114.html) (soil moisture sensor, second source). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-TemperatureAndHumidity Sensor-HDC1000](/db/seeed-grove-temperatureandhumidity-sensor-hdc1000.html) (soil / air temperature reference circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and DFRobot and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000 — for a Tree Thirst Sensor

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Tree Thirst Sensor: A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee. The design is built around your M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000.
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
主题：样品订购及批量报价 — M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000 — 用于Tree Thirst Sensor

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tree Thirst Sensor：A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee。产品设计基于贵司的M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000。
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
Subject: PCBA quote from open design files — Tree Thirst Sensor, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Tree Thirst Sensor: A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee. The design starts from published open-hardware files (M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Tree Thirst Sensor，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tree Thirst Sensor：A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee。设计基于已公开的开源硬件文件（M5Stack Unit Earth (U019), M5Stack Unit Watering (U101), M5Stack Stamp C6LoRa (S012), DFRobot SEN0114, Seeed Grove-TemperatureAndHumidity Sensor-HDC1000；含原理图、PCB和BOM），并做了我们自己的修改。

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
