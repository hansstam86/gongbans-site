# Tool Check Wand — Founder Start Pack

> A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** A technician drives off without the €600 drill and finds out at the next job, or the van is opened overnight and nobody knows what was in it; the trades company has no inventory of what is in which van, and the tools that offer tracking only track their own brand.
- **Customer:** Small and mid-sized trades companies with a few to a few dozen vans, workshop managers in facilities and manufacturing, tool-hire counters; the owner or operations lead pays.
- **Product:** A battery wand with a UHF reader: one sweep of the van or the shelf reads every tagged tool and lists what is missing against that van's list; buzzer, local app, end-of-day check-in, tags for every brand; no subscription. Read reliability on metal tools is measured in the pilot before any claim. Target price €199–249 (estimate).
- **Why now:** Van tool theft is large and documented (UK police data: 44,514 incidents in 2023, about £98m stolen), the existing answers are either locked to one tool brand (Milwaukee One-Key) or enterprise-priced (Hilti ON!Track subscription, Zebra readers at $900–1,900+), and the catalogue has a UHF reader unit.
- **The ask:** ~€55–70k to certification and a first 500 wands plus tags (estimate); ten trial purchases cover a tenth.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Van tool theft is a confirmed, large pain point (UK police data: 44,514 incidents in 2023, about £98m stolen). A genuine gap exists between Milwaukee One-Key (cheap but locked to Milwaukee tools) and Hilti ON!Track / Zebra RFD40 (enterprise: readers $900–1,900+, ON!Track about $120 a month). **Main risk:** UHF tags on metal tools are a real, unresolved reliability risk; on-metal tags cost more than standard tags, which could undercut the "tag everything cheaply" pitch. Needs real-world testing before claiming it works; the pack measures it first. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 10 trades companies tag one van each with 50 tags, achieve a reliable sweep (95%+ of tagged tools read in three sweeps, measured), and buy the wand at €229 after a two-week trial? Pass = 10 purchases and the read-rate met on real vans.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Trades companies with 3–30 vans (electricians, plumbers, HVAC, builders), workshop managers, tool-hire counters; the owner pays after the second lost or stolen tool.

**The problem as the pack states it:** A technician drives off without the €600 drill and finds out at the next job, or the van is opened overnight and nobody knows what was in it; the trades company has no inventory of what is in which van, and the tools that offer tracking only track their own brand.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/electricians** · https://www.reddit.com/r/electricians/ — working electricians.
- **r/Plumbing** · https://www.reddit.com/r/Plumbing/ — plumbers and heating engineers.
- **r/HVAC** · https://www.reddit.com/r/HVAC/ — HVAC technicians (mostly US); installer mindset.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€199–249, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how trades companies with 3–30 vans, workshop managers, tool-hire counters deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last tool that went missing from a van: when did you notice, what did it cost, and how do you know what is in each van today?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim. On a scale of one to ten, how likely would you be to buy that at €199–249, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Tool Check Wand: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Tool Check Wand: A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim. Before we spend money on tooling I want to find out whether this solves a real problem for trades companies with 3–30 vans, workshop managers, tool-hire counters.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €199–249 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

The pain is documented: UK police figures put van tool theft at 44,514 incidents in 2023 and about £98m stolen, and every tradesperson has a story. Milwaukee One-Key tracks cheaply but only Milwaukee tools; Hilti ON!Track is a managed service at roughly $120 a month; enterprise UHF readers such as the Zebra RFD40 cost $900–1,900+ before software. Between them is the small trades company with mixed brands and no budget line. The technical risk is equally real: UHF tags on metal tools need on-metal tags, which cost more than standard labels and still read unevenly in a packed van; this pack treats read reliability as the first thing to measure, not something to assume.

**Who pays, B2B:** the company owner or operations lead, usually after a loss; insurers may discount for inventory evidence (unverified). **Who uses:** the technician at the end of the day and the storeman at the counter; a sweep must take seconds or it will not happen.

### Market size (estimates — check)

- **TAM:** trades and service vans in DE/UK/NL/FR: estimate 5–8M; workshops and hire counters on top. Theoretical €1B+ at €229 plus tags.
- **SAM:** companies with 3–30 vans and a recent loss: estimate 300,000 companies → €70M for wands plus tag revenue.
- **SOM (3 yrs):** 15,000–30,000 wands and millions of tags; year-1: 500–1,000 wands through trade suppliers and insurers.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Milwaukee One-Key | Cheap tags and app, locked to Milwaukee tools | Any brand, any tool; local list |
| Hilti ON!Track | Managed asset tracking, about $120 a month (research, Nov 2026) | No subscription; sized for a 5-van company |
| Zebra RFD40 and enterprise UHF readers | $900–1,900+ per reader plus software | A quarter of the price, with the van list built in |
| ToolWatch and asset-management software | Software subscriptions with barcode or RFID | Hardware first, no subscription; export to their software if wanted |
| A photo of the van and memory | Free | The ten-second sweep is the product |

**Wedge:** a brand-agnostic ten-second van inventory at a quarter of enterprise reader prices and no subscription, if and only if the on-metal read rate holds in a real van.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Direct Line / Fleetnews tool-theft data | 44,514 incidents, ~£98m stolen (UK, 2023) | The pain is large and documented |
| Hilti ON!Track (pricing discussion) | Managed service, ~$120/month | Enterprise incumbent with subscription |
| Milwaukee One-Key (tag pricing) | Cheap tags, Milwaukee tools only | Brand-locked incumbent |
| Zebra RFD40 (pricing) | $900–1,900+ per reader | Enterprise incumbent, 4× the target |

**Verdict as researched: LIKELY.** Main risk: UHF tags on metal tools are a real, unresolved reliability risk; on-metal tags cost more than standard tags, which could undercut the "tag everything cheaply" pitch. Needs real-world testing before claiming it works; the pack measures it first.
<!-- market-competitors:end -->

### Product & value proposition

- Wand: UHF reader (EU 865–868 MHz) with a directional antenna, BLE to the phone or an on-wand screen, buzzer, 8-hour battery; sweep mode and single-tag mode.
- Lists: per van, per technician, per job kit; missing-tool list after a sweep; check-in at end of day; export CSV; optional sync to the company's existing software.
- Tags: standard UHF labels for cases and plastic tools, on-metal tags for drills and metal tools, priced separately and honestly; a tagging guide per tool type.
- Read-rate test built into the app: the pilot measures it on each van and the company sees the number before buying more.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €40–60) | 50.0 | 40.0 |
| PCBA assembly + test | 6.0 | 3.9 |
| Enclosure / mechanics (tooling amortised separately) | 10.0 | 7.0 |
| Packaging, cable, leaflet | 4.0 | 3.0 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 4.0 | 2.0 |
| Certification amortised (€12k, estimate) | 12.0 | 2.4 |
| **Landed cost** | **86.0** | **58.3** |
| Channel cost (trade suppliers and direct, ~€30) | 30.0 | 30.0 |
| Net price received (€224 incl. 19% VAT → €188.2 ex VAT) | 188.2 | 188.2 |
| **Gross margin per unit** | **€72.2 (38%)** | **€99.9 (53%)** |

Lesson: the wand margin is modest; tags are the volume line (on-metal tags cost multiples of labels, so price them per type). Do not promise read rates before the pilot numbers.

### Go-to-market

**First 100 customers:**

1. Ten trades companies, one van each, two-week trials with the read-rate measured.
2. One trade supplier (electrical or plumbing wholesaler) as the shelf.
3. One insurer's loss-prevention team as the referrer.

**Scale channels:** trade wholesalers, van-fitting companies, insurers, hire counters.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question trials; works-like wand on Core2 + UHF unit; read-rate tests on three real vans with standard and on-metal tags. |
| Q2 | Custom wand board and antenna; EVT 20 in ten companies; tagging guide. |
| Q3 | DVT; certification (UHF reader); 300 wands; trade-supplier listing. |
| Q4 | Insurer channel; 1,000 wands; sync integrations. |

**Team:** one RF/embedded engineer, one app developer, one founder from the trades or trade supply.

**Funding to first production (estimates):** NRE €25k (antenna and wand mechanics) + certification €12k + first 500 wands and tags landed ~€35k ≈ €72k; minus trial purchases ~€2k ≈ €70k.

### Top risks

| Risk | Mitigation |
|---|---|
| UHF read rate on metal tools in a packed van | Measure first; on-metal tags; antenna design; sweep technique in the guide; do not claim until measured |
| Tag cost undermines 'tag everything' | Tag only the valuable tools; price tags per type; say so |
| Milwaukee or Hilti move down-market | Brand-agnostic and no-subscription remain the wedge |
| Technicians skip the sweep | Ten-second target; end-of-day reminder; the missing list is the reward |

## 4. Start kit

### Boards to start from

- [M5Stack Unit UHF-RFID (U107)](https://www.gongbans.com/db/m5stack-unit-uhf-rfid.html) — UHF RFID reader unit: the wand's front end (design files published for the module; electronics not open)
- [M5Stack Core2 (K010)](https://www.gongbans.com/db/m5stack-core2.html) — touch-screen controller for the prototype wand (design files published for the module; electronics not open)
- [M5Stack Cardputer (K132)](https://www.gongbans.com/db/m5stack-cardputer.html) — keyboard handheld alternative for the list (design files published for the module; electronics not open)
- [M5Stack Unit Buzzer (U132)](https://www.gongbans.com/db/m5stack-unit-buzzer.html) — missing-tool alert (design files published for the module; electronics not open)
- [M5Stack StickC-Plus (K016-P)](https://www.gongbans.com/db/m5stack-stickc-plus.html) — compact handheld core for a second prototype (design files published for the module; electronics not open)

All M5Stack products with published module files; the UHF-RFID unit is the reader front end for prototyping, the production wand needs its own antenna design.

### Block diagram

```
  [UHF reader + directional antenna] -> [ESP32 core, 8 h cell] -> BLE -> phone app (lists per van / technician)
           sweep 10 s -> read tags -> compare with the van list -> missing tools -> [buzzer] [screen]
  tags: standard labels (cases, plastic) | on-metal tags (drills, metal tools)  read rate measured per van
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| UHF RFID reader module | 18.0 |  |
| Directional antenna | 6.0 | custom |
| ESP32-S3 module + BLE | 3.0 |  |
| Li-ion cell + charger + USB-C | 5.0 |  |
| Wand enclosure + trigger + buzzer | 12.0 |  |
| PCB, screen option, passives | 6.0 |  |

### Firmware/software starting point

- ESP-IDF; reader driver (EPC Gen2), inventory rounds with session management, RSSI filtering; BLE to the app; local lists in flash.
- App: vans, technicians, kits, sweep results, read-rate test, CSV export, optional sync.

### 12-week build plan

1. Interviews with ten companies; trial design
2. Prototype wand
3. Read-rate tests on three vans (standard vs on-metal tags)
4. Antenna design
5. Wand board v1
6. App v0 with lists and sweep
7. EVT 20 in ten companies
8. Read-rate review; tagging guide
9. Enclosure tooling decision
10. DVT
11. Pre-compliance (UHF)
12. Certification; supplier listing

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.
- UHF RFID reader: EN 302 208 radio testing; power limits for EU 865–868 MHz; antenna is part of the certified design.

### Validation toolkit

- **Kill question:** Do 10 trades companies tag one van each with 50 tags, achieve a reliable sweep (95%+ of tagged tools read in three sweeps, measured), and buy the wand at €229 after a two-week trial? Pass = 10 purchases and the read-rate met on real vans.
- **Cheapest experiment:** One prototype wand and 50 tags on one friendly company's van for two weeks; publish the read rate; ask ten companies whether they would buy at €229 given that number.
- **5-question interview:** 1) What did you last lose or have stolen from a van, and what did it cost? 2) How do you know what is in each van today? 3) Have you tried One-Key, ON!Track or anything else; what stopped you? 4) What brands are your tools? 5) At €229 per wand plus tags, how many vans?
- **Landing page:** headline "Know what left the van before it leaves." Bullets: ten-second sweep; any brand; no subscription; read rate measured in your van first. Button: request a two-week trial (B2B).
- **Pass threshold:** 10 purchases after trials with the read-rate target met on real vans.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.
- RF: antenna tuning per batch; read-rate test fixture on the line.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit UHF-RFID (U107)](/db/m5stack-unit-uhf-rfid.html) (UHF RFID reader unit: the wand's front end); [M5Stack Core2 (K010)](/db/m5stack-core2.html) (touch-screen controller for the prototype wand); [M5Stack Cardputer (K132)](/db/m5stack-cardputer.html) (keyboard handheld alternative for the list); [M5Stack Unit Buzzer (U132)](/db/m5stack-unit-buzzer.html) (missing-tool alert); [M5Stack StickC-Plus (K016-P)](/db/m5stack-stickc-plus.html) (compact handheld core for a second prototype). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*
- **Newland (SZ)** (新大陆(深圳)科技有限公司) · newlandaidc.com — Barcode / RFID / POS terminal: Barcode scanner; NFC reader; POS terminal; RFID reader. *(NFC / RFID readers)*
- **Szrfid Technology** (深圳市新中讯网络技术有限公司) · szrfid.com — RFID reader / UHF solution house: UHF RFID reader; RFID module; OEM/ODM for logistics + retail + access. *(NFC / RFID readers)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P) — for a Tool Check Wand

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Tool Check Wand: A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim. The design is built around your M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P).
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
主题：样品订购及批量报价 — M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P) — 用于Tool Check Wand

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tool Check Wand：A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim。产品设计基于贵司的M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P)。
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
Subject: PCBA quote from open design files — Tool Check Wand, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Tool Check Wand: A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim. The design starts from published open-hardware files (M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Tool Check Wand，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tool Check Wand：A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim。设计基于已公开的开源硬件文件（M5Stack Unit UHF-RFID (U107), M5Stack Core2 (K010), M5Stack Cardputer (K132), M5Stack Unit Buzzer (U132), M5Stack StickC-Plus (K016-P)；含原理图、PCB和BOM），并做了我们自己的修改。

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
