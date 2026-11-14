# Cue Lights for Small Stages — Founder Start Pack

> A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Small stages have no cue lights: the stage manager whispers, waves or texts, and missed cues follow. Professional sets exist but cost $485–985 and are sized for venues with a budget line for them.
- **Customer:** Amateur dramatic societies (thousands in DE/UK/NL), school and university theatres, churches staging productions, small AV and event-hire companies. The society treasurer, the school drama department or the hire company pays.
- **Product:** A stage-manager master with four lit channel buttons and four battery outstations with a big lit button and a buzzer; standby flashes, go is solid, the operator acknowledges; ESP-NOW link with retries and a link-health light; charges over USB-C. Target price €349–449 (estimate).
- **Why now:** Amateur and school stages run cues by whisper and WhatsApp; the professional cue-light systems start around $485 and go to $985 (research, Nov 2026); ESP-NOW and lit buttons make a reliable set buildable from catalogue parts.
- **The ask:** ~€45–60k to certification and a first 500 sets (estimate); federation pre-orders cover a third.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY (CONTESTED).** The real incumbent, DSan PerfectCue / CueLight, sells at $485–985, not the £1.5–4k first assumed; the gap holds at 30–55% cheaper but is smaller than first thought. Blue Room forum threads and a Hackaday cue-light project show DIY demand. **Main risk:** A smaller price gap than assumed: the package and simplicity for amateur groups must carry the pitch alongside price. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 10 amateur groups from one federation pre-order the five-piece set at €399 after a video demo? Pass = 10 deposits in 6 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Amateur theatre federations (BDAT in Germany, Little Theatre Guild in the UK), school and university theatres, churches with productions, small AV hire companies.

**The problem as the pack states it:** Small stages have no cue lights: the stage manager whispers, waves or texts, and missed cues follow. Professional sets exist but cost $485–985 and are sized for venues with a budget line for them.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/techtheatre** · https://www.reddit.com/r/techtheatre/ — stage managers and technicians, many in schools and amateur theatre.
- **The Blue Room (UK)** · https://www.blue-room.org.uk/ — UK technical-theatre forum; DIY cue-light threads live here.
- **Hackaday / hackaday.io** · https://hackaday.io/ — maker audience; visibility more than buyers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€349–449, the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how amateur theatre federations, school and university theatres, churches with productions, small AV hire companies deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Walk me through how cues were called at your last show and what went wrong.
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems. On a scale of one to ten, how likely would you be to buy that at €349–449, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Cue Lights for Small Stages: would you pay €349–449 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Cue Lights for Small Stages: A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €349–449, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

Cue lights are the standard way a stage manager tells lighting, sound, fly and stage crew when to stand by and when to go. Professional venues wire them in; everyone below that improvises. The professional portable systems (DSan PerfectCue and CueLight, $485–985) are good but priced for professionals; amateur groups, schools and churches, which stage most of the productions in Europe by number, run without.

**Who pays:** the society or school (B2B-ish, small budgets, grant-funded equipment purchases), the AV hire company (buys several sets, rents them). **Who uses:** volunteers, so set-up must be nothing: switch on, pair, go.

### Market size (estimates — check)

- **TAM:** amateur theatre groups in DE (~2,500 in BDAT), UK (~2,500 affiliated), NL/AT/CH, plus schools with a stage (tens of thousands) and churches. Theoretical €10–20M.
- **SAM:** groups that stage two or more productions a year and own some kit: estimate 10,000 → €4M.
- **SOM (3 yrs):** 2,000–3,000 sets; year-1: 400–600, mostly through two federations and one hire company.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| DSan PerfectCue / CueLight | Professional portable cue lights; $485–985 (research, Nov 2026) | 30–55% cheaper with the same standby/go/acknowledge logic; sized and priced for amateurs |
| Interspace Industries and wired venue systems | Installed systems, quote-based | Different market; we are portable and battery |
| WhatsApp, headsets, hand signals | Free | Missed cues; headsets cost more than our set |
| DIY cue-light projects (Blue Room forum, Hackaday) | Arduino / ESP32 builds | Demand signal; nobody ships a boxed set |

**Wedge:** a boxed, charged, paired-out-of-the-box set at €399 for the people who today whisper; the gap against the entry-level professional set is 30–55%, not a multiple, so the simplicity matters as much as the price.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| DSan PerfectCue / CueLight | $485–985 portable cue lights | Incumbent; the target is 30–55% below it |
| Blue Room forum DIY threads | Technicians building their own | Demand signal |
| Hackaday cue-light project | Maker build | Demand signal, no boxed product |

**Verdict as researched: LIKELY (CONTESTED).** Main risk: A smaller price gap than assumed: the package and simplicity for amateur groups must carry the pitch alongside price.
<!-- market-competitors:end -->

### Product & value proposition

- Master: four channels, lit buttons (amber standby, green go), per-channel acknowledge indication, link-health light, USB-C charged.
- Outstation: one big lit button, buzzer (switchable), belt clip and magnet, 20-hour battery (estimate).
- Radio: ESP-NOW on 2.4 GHz with acknowledgements and retries; channel scan at start; range tested across a 30 m hall with walls.
- Expand to eight outstations; no app, no WiFi needed; firmware update over USB.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €60–90) | 75.0 | 60.0 |
| PCBA assembly + test | 8.0 | 5.2 |
| Enclosure / mechanics (tooling amortised separately) | 14.0 | 9.8 |
| Packaging, cable, leaflet | 6.0 | 4.5 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 5.0 | 2.5 |
| Certification amortised (€10k, estimate) | 10.0 | 2.0 |
| **Landed cost** | **118.0** | **84.0** |
| Channel cost (direct + theatre suppliers, ~€30 per set) | 30.0 | 30.0 |
| Net price received (€399 incl. 19% VAT → €335.3 ex VAT) | 335.3 | 335.3 |
| **Gross margin per unit** | **€187.3 (56%)** | **€221.3 (66%)** |

Lesson: a five-piece set carries five enclosures and five batteries; the margin lives in the second run and in extra outstations sold separately.

### Go-to-market

**First 100 customers:**

1. Ten groups from one federation after a video demo and a loaner set at a festival weekend.
2. One AV hire company buying five sets.
3. Drama departments via their teachers' association.

**Scale channels:** theatre suppliers (Thomann, Stage Depot), federation newsletters and festivals, school equipment catalogues.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations; works-like set on five AtomS3 + ByteButton/Button units; range test in a hall. |
| Q2 | Custom PCBs (master, outstation); enclosures; EVT 10 sets with two groups. |
| Q3 | DVT; certification; 200 sets; federation pre-orders shipped. |
| Q4 | Supplier listing; 500 sets; eight-channel master. |

**Team:** one embedded engineer, one founder from the theatre world; enclosure design bought in.

**Funding to first production (estimates):** NRE €22k (two PCBs, two enclosures) + certification €10k + first 500 sets landed ~€45k ≈ €77k; minus pre-orders ~€20k ≈ €57k.

### Top risks

| Risk | Mitigation |
|---|---|
| Gap against DSan is smaller than hoped | Compete on the amateur-sized package and simplicity; do not overclaim the price gap |
| Radio reliability in a steel-framed hall | Acknowledged protocol, retries, link-health light, channel scan; test early |
| Battery and enclosure cost of five pieces | Shared enclosure for master and outstation; one battery type |
| Volunteers lose outstations | Sell singles; magnet and clip; bright colour |

## 4. Start kit

### Boards to start from

- [M5Stack AtomS3-Lite (C124)](https://www.gongbans.com/db/m5stack-atoms3-lite.html) — ESP32-S3 core for master and outstations (ESP-NOW) (design files published for the module; electronics not open)
- [M5Stack Unit ByteButton (U192)](https://www.gongbans.com/db/m5stack-unit-bytebutton.html) — RGB-lit button bar for the master (design files published for the module; electronics not open)
- [M5Stack Unit Button (U027)](https://www.gongbans.com/db/m5stack-unit-button.html) — single big button for an outstation (design files published for the module; electronics not open)
- [M5Stack Unit Buzzer (U132)](https://www.gongbans.com/db/m5stack-unit-buzzer.html) — acknowledge beep (design files published for the module; electronics not open)
- [Seeed Grove-Chainable RGB LED](https://www.gongbans.com/db/seeed-grove-chainable-rgb-led.html) — open RGB indicator circuit for the outstation lamp (open files: schematic)

The AtomS3 Lite and the button units are M5Stack products with published module files; the Seeed RGB board gives the open indicator circuit. Two PCBs: master and outstation.

### Block diagram

```
  MASTER: [4 lit buttons] -> [ESP32-S3] -> ESP-NOW ->  OUTSTATION 1..8: [ESP32-S3] -> [big lit button] [buzzer]
           [link light]       [USB-C + cell]                            [USB-C + cell] [clip/magnet]
  standby = flashing amber, go = solid green, ack = button press echoed to master
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| ESP32-S3 modules ×5 | 12.5 |  |
| Lit buttons (master 4 + outstations 4) | 10.0 |  |
| Li-ion cells + chargers ×5 | 12.0 |  |
| Buzzers ×4 | 2.0 |  |
| Enclosures ×5 | 14.0 | one shared design |
| PCBs, USB-C, passives | 8.0 |  |
| Case / pouch for the set | 6.0 |  |

### Firmware/software starting point

- ESP-IDF, ESP-NOW with application-level acks and sequence numbers; channel selection at power-up; pairing by holding buttons.
- State machine per channel: idle / standby / go / acknowledged; buzzer patterns.
- Battery gauge and low-battery flash; USB firmware update.

### 12-week build plan

1. Interviews; fake door with a demo video
2. Prototype five units
3. Protocol: acks, retries, range test
4. Button and lamp design
5. Two PCBs v1
6. Enclosure design
7. EVT 10 sets
8. Two productions run with it
9. Tooling decision
10. DVT sets
11. Pre-compliance
12. Certification; pre-order shipping

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 10 amateur groups from one federation pre-order the five-piece set at €399 after a video demo? Pass = 10 deposits in 6 weeks.
- **Cheapest experiment:** Film a 60-second demo of the five-unit prototype in a real tech rehearsal; post it in two federation groups with a €399 pre-order link.
- **5-question interview:** 1) How do you call cues today and what went wrong last show? 2) Have you priced cue lights; which and why not? 3) Who signs off equipment purchases and from what budget? 4) How many positions need a light? 5) At €399 for master plus four, would you order for the next production?
- **Landing page:** headline "Standby. Go. No whispering." Bullets: five pieces, charged, paired; works through walls; €399. Button: refundable €50 deposit.
- **Pass threshold:** 10 deposits from one federation in 6 weeks.

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

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack AtomS3-Lite (C124)](/db/m5stack-atoms3-lite.html) (ESP32-S3 core for master and outstations (ESP-NOW)); [M5Stack Unit ByteButton (U192)](/db/m5stack-unit-bytebutton.html) (RGB-lit button bar for the master); [M5Stack Unit Button (U027)](/db/m5stack-unit-button.html) (single big button for an outstation); [M5Stack Unit Buzzer (U132)](/db/m5stack-unit-buzzer.html) (acknowledge beep). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Chainable RGB LED](/db/seeed-grove-chainable-rgb-led.html) (open RGB indicator circuit for the outstation lamp). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED — for a Cue Lights for Small Stages

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Cue Lights for Small Stages: A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems. The design is built around your M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED.
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
主题：样品订购及批量报价 — M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED — 用于Cue Lights for Small Stages

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Cue Lights for Small Stages：A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems。产品设计基于贵司的M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED。
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
Subject: PCBA quote from open design files — Cue Lights for Small Stages, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Cue Lights for Small Stages: A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems. The design starts from published open-hardware files (M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Cue Lights for Small Stages，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Cue Lights for Small Stages：A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems。设计基于已公开的开源硬件文件（M5Stack AtomS3-Lite (C124), M5Stack Unit ByteButton (U192), M5Stack Unit Button (U027), M5Stack Unit Buzzer (U132), Seeed Grove-Chainable RGB LED；含原理图、PCB和BOM），并做了我们自己的修改。

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
