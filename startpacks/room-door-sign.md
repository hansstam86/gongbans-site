# Door Sign, No Subscription — Founder Start Pack

> An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Every office with more than two meeting rooms wants a sign on the door that shows whether the room is free and lets you grab it, and the products that do it bill a subscription per room or cost as much as a laptop.
- **Customer:** SMEs with 3–30 rooms, co-working operators, schools and universities, churches and community centres with bookable halls; IT resellers and managed-service providers who install for them. Office management or IT pays.
- **Product:** A 4.7–7.5 inch e-paper sign with a battery that lasts months, reading the room's calendar from CalDAV, Google or Microsoft 365, showing free/busy and the next bookings, with book-now and end-early buttons; mounts on glass or wall; no per-room fee ever. Target price €149–199 (estimate).
- **Why now:** Room signs from Joan and Evoko bill per device per month or cost up to several thousand euros; the e-paper plus calendar build is one of the most repeated Home Assistant and ESPHome projects; the devices in the catalogue already have the display, battery and radio.
- **The ask:** ~€45–60k to certification and a first 1,000 units (estimate); pre-orders of 3+ cover a third.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Joan (about €5–20 per device per month) and Evoko Naso ($800–3,600 plus licensing) are confirmed subscription-attached, a real wedge; the DIY precedent is confirmed (ESPHome-ePaper-Calendar and relatives). **Main risk:** The risk is the sales cycle, not the market: Microsoft 365 / Google app consent and IT security review will be the real bottleneck. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 10 co-working spaces or SMEs pre-order 3 signs each at €169 from a landing page within 30 days? Pass = 10 orders of 3 or more.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** SMEs, co-working spaces, schools, churches and community centres that book rooms; IT resellers and managed-service providers as the channel.

**The problem as the pack states it:** Every office with more than two meeting rooms wants a sign on the door that shows whether the room is free and lets you grab it, and the products that do it bill a subscription per room or cost as much as a laptop.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/sysadmin** · https://www.reddit.com/r/sysadmin/ — the IT people who approve or block a calendar integration.
- **r/msp** · https://www.reddit.com/r/msp/ — managed-service providers: the reseller channel for office devices.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.

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
Thanks for the time. I am looking into how sMEs, co-working spaces, schools, churches and community centres that book rooms deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do people find a free room in your office today, and what happened the last time two groups wanted the same one?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room. On a scale of one to ten, how likely would you be to buy that at €149–199, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Door Sign, No Subscription: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Door Sign, No Subscription: An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room. Before we spend money on tooling I want to find out whether this solves a real problem for sMEs, co-working spaces, schools, churches and community centres that book rooms.

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

Joan charges per device per month; Evoko's Naso costs $800–3,600 plus licensing; both work well and both are the reason small organisations use paper on the door. The DIY world has solved the display side many times over (ESPHome-ePaper-Calendar and its relatives). What stops those builds becoming products is not hardware but the calendar plumbing: Microsoft 365 and Google app consent, the IT security review, and tenant admin approvals. That is the real work in this pack, and the real sales bottleneck.

**Who pays, B2B:** office management or IT; resellers and MSPs buy ten at a time for their customers. **Who uses:** everyone walking past the door; the sign must be readable at three metres and obvious without a manual.

### Market size (estimates — check)

- **TAM:** meeting rooms in EU organisations with 10–500 staff: estimate 5–8M rooms. Theoretical €1B at €169.
- **SAM:** rooms in organisations already on Microsoft 365 or Google Workspace with an IT contact who installs things: estimate 1M rooms → €170M.
- **SOM (3 yrs):** 15,000–30,000 signs through direct sales and 20–50 resellers; year-1: 1,500–3,000.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Joan | E-paper room sign; about €5–20 per device per month (research, Nov 2026) | No subscription; comparable hardware |
| Evoko Naso (Biamp) | $800–3,600 per device plus licensing | A tenth of the price |
| Meetio, Robin, tablets on the wall | Subscription software on an iPad or Android panel | No tablet, no mains cable, no fee |
| ESPHome-ePaper-Calendar and similar DIY | Free if you can run Home Assistant and register an app | We do the calendar plumbing and the IT paperwork once, for everyone |

**Wedge:** no per-room fee, months of battery, and the calendar integrations already approved and documented for IT, which is what the DIY builds cannot offer an office.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Joan | E-paper room sign, ~€5–20/device/month | Incumbent with subscription |
| Evoko Naso (Biamp) | $800–3,600 + licensing | Incumbent at a multiple of the target |
| ESPHome-ePaper-Calendar | DIY e-paper calendar sign | Demand signal, no boxed product |

**Verdict as researched: LIKELY.** Main risk: The risk is the sales cycle, not the market: Microsoft 365 / Google app consent and IT security review will be the real bottleneck.
<!-- market-competitors:end -->

### Product & value proposition

- 4.7-inch (PaperS3) and 7.5-inch sizes; status colour band (PaperColor variant) or LED edge for free/busy visible down the corridor.
- Calendar: CalDAV direct; Google and Microsoft 365 through a small self-hosted or hosted bridge with a published app registration and security documentation; per-room service accounts.
- Book-now (15/30/60 min) and end-early buttons; check-in to release no-shows (optional).
- 2–4 months per charge at 5-minute refreshes (estimate); USB-C; glass mount with VHB, wall plate with screws.
- Fleet page: battery, last sync, firmware; open API; no per-room licence.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €35–55) | 45.0 | 36.0 |
| PCBA assembly + test | 4.0 | 2.6 |
| Enclosure / mechanics (tooling amortised separately) | 8.0 | 5.6 |
| Packaging, cable, leaflet | 3.0 | 2.2 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 3.0 | 1.5 |
| Certification amortised (€10k, estimate) | 10.0 | 2.0 |
| **Landed cost** | **73.0** | **50.0** |
| Channel cost (direct and reseller margin, ~€20) | 20.0 | 20.0 |
| Net price received (€174 incl. 19% VAT → €146.2 ex VAT) | 146.2 | 146.2 |
| **Gross margin per unit** | **€53.2 (36%)** | **€76.3 (52%)** |

Lesson: the e-paper panel is half the BOM; the 7.5-inch version needs a higher price. The reseller margin is the cost of scaling without a sales team.

### Go-to-market

**First 100 customers:**

1. Ten co-working spaces and SMEs from a landing page and direct outreach, each buying three signs.
2. Two MSPs that install them for their customers.
3. One school or university testing the CalDAV path.

**Scale channels:** MSPs and IT resellers, office-furniture dealers, Microsoft and Google marketplace listings once the app registrations are verified.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question pre-orders; works-like sign on PaperS3 with CalDAV; Microsoft and Google app registrations started (the long pole). |
| Q2 | Bridge service; verified app publisher status; EVT 20 signs in three offices; security documentation written. |
| Q3 | DVT; certification; 500 signs; reseller programme. |
| Q4 | 7.5-inch size; 2,000 signs; marketplace listings. |

**Team:** one embedded engineer, one backend developer who has done OAuth app verification before, one founder selling to offices and MSPs.

**Funding to first production (estimates):** NRE €18k + app verification, security review and pen-test €12k + certification €8k + first 1,000 signs landed ~€45k ≈ €83k; minus pre-orders ~€25k ≈ €58k.

### Top risks

| Risk | Mitigation |
|---|---|
| Microsoft 365 / Google app consent and IT security review stall sales | Start verification in month one; publish a security whitepaper; offer the CalDAV and self-hosted bridge path for strict IT |
| Battery life claims | Measure at 5-minute refresh over a month before claiming; show the number on the fleet page |
| Joan drops its price | Our wedge is also the no-licence model; keep the hardware margin healthy |
| Glass mounting failures | VHB spec and a wall plate; replacement mounts in the box |

## 4. Start kit

### Boards to start from

- [M5Stack PaperS3 (C139)](https://www.gongbans.com/db/m5stack-papers3.html) — ESP32-S3 e-paper device for the sign (design files published for the module; electronics not open)
- [M5Stack CoreInk (K048)](https://www.gongbans.com/db/m5stack-coreink.html) — small e-paper variant for narrow door frames (design files published for the module; electronics not open)
- [M5Stack PaperColor (C151)](https://www.gongbans.com/db/m5stack-papercolor.html) — colour variant for status colours (design files published for the module; electronics not open)

All three are M5Stack e-paper devices with published module files (electronics not open); the first product can ship on a customised PaperS3 before a custom board exists.

### Block diagram

```
  [calendar: CalDAV | Google | Microsoft 365] -> [bridge service (self-hosted or hosted)] -> WiFi -> [ESP32-S3 + e-paper 4.7"/7.5"]
                                                                                              |
                                                   [buttons: book 15/30/60, end early]   [battery 2–4 months, USB-C]
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| E-paper 4.7 inch + driver (7.5 inch: +€15) | 18.0 |  |
| ESP32-S3 module | 2.5 |  |
| Li-ion cell 2,000–3,000 mAh + charger | 5.0 |  |
| Enclosure + glass/wall mount | 8.0 |  |
| Buttons, LED edge, PCB, USB-C | 4.0 |  |
| Packaging | 2.0 |  |

### Firmware/software starting point

- ESP-IDF; deep sleep; partial refresh; HTTPS to the bridge; buttons wake the device.
- Bridge: small open-source service (CalDAV client, Google Calendar API, Microsoft Graph) with per-room tokens; self-host or our hosting at cost; fleet page.
- App registrations: verified publisher on both platforms; documented scopes (calendar read/write for the room resource only).

### 12-week build plan

1. Pre-orders live; interviews with office managers and two MSPs
2. Prototype on PaperS3 + CalDAV
3. Bridge v0 with Google and Microsoft sandbox tenants
4. App registrations and verification submitted
5. Enclosure and mount design
6. Custom board or customised PaperS3 decision
7. EVT 20 in three offices
8. Battery measurement month
9. Security documentation
10. DVT
11. Pre-compliance
12. Certification; reseller kit

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 10 co-working spaces or SMEs pre-order 3 signs each at €169 from a landing page within 30 days? Pass = 10 orders of 3 or more.
- **Cheapest experiment:** Three PaperS3 signs with CalDAV on three doors of one co-working space for a month; ask the operator whether they would buy ten at €169.
- **5-question interview:** 1) How do people find a free room today and what goes wrong? 2) Have you priced Joan or Evoko; what stopped you? 3) Who would approve a calendar integration in your IT; what would they ask for? 4) How many rooms and doors? 5) At €169 per sign with no fee, how many?
- **Landing page:** headline "The room sign without the subscription." Bullets: months on a charge; Microsoft 365, Google, CalDAV; book from the door; €169. Button: pre-order 3 (refundable deposit).
- **Pass threshold:** 10 orders of 3 or more within 30 days.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (ESP32-S3 e-paper device for the sign); [M5Stack CoreInk (K048)](/db/m5stack-coreink.html) (small e-paper variant for narrow door frames); [M5Stack PaperColor (C151)](/db/m5stack-papercolor.html) (colour variant for status colours). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151) — for a Door Sign, No Subscription

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Door Sign, No Subscription: An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room. The design is built around your M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151).
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
主题：样品订购及批量报价 — M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151) — 用于Door Sign, No Subscription

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Door Sign, No Subscription：An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room。产品设计基于贵司的M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151)。
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
Subject: PCBA quote from open design files — Door Sign, No Subscription, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Door Sign, No Subscription: An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room. The design starts from published open-hardware files (M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Door Sign, No Subscription，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Door Sign, No Subscription：An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room。设计基于已公开的开源硬件文件（M5Stack PaperS3 (C139), M5Stack CoreInk (K048), M5Stack PaperColor (C151)；含原理图、PCB和BOM），并做了我们自己的修改。

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
