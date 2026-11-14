# Backstage Relay — Founder Start Pack

> A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** In a small venue the dressing rooms cannot hear the show and the stage manager cannot call 'five minutes to places' without running; the professional show-relay and paging systems that solve it are installed products priced for theatres with a technical budget.
- **Customer:** Amateur dramatic societies, school and university stages, churches with performances, small event venues; the society or the drama department pays, often together with the cue-light set.
- **Product:** A stage microphone station with a page button and three battery speakers that play the stage feed quietly and switch to announcements at full volume, over WiFi or ESP-NOW, pairing in a minute; positioned for paging and listening in, with the latency stated, never for calling cues. Target price €299–399 (estimate).
- **Why now:** Technical-theatre forums (ControlBooth among them) carry active threads from ultra-low-budget groups asking for exactly this and ready to build it, while professional show-relay and paging systems run into the thousands; WiFi audio over catalogue parts is cheap, as long as it is sold for what it does.
- **The ask:** ~€45–60k to certification and a first 500 sets (estimate); pre-orders paired with the cue-light set cover a third.

<!-- market-check:start -->
> **External market check (November 2026): UNCERTAIN.** Real DIY community interest is confirmed (ControlBooth forum threads, including ultra-low-budget groups open to DIY), but a venue reported in a forum thread that WiFi / ESP-NOW-style paging was "virtually useless for cueing" because of latency, a documented failure. **Main risk:** Repositioned before building as a paging and show-relay intercom for non-time-critical communication, paired with the cue-light set rather than replacing it; 2.4 GHz interference with wireless microphones stays unverified and needs on-site testing. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
>
> **Built with the research fix applied (November 2026).** The research found a venue reporting WiFi-style paging as useless for cueing because of latency. This pack therefore sells the set as a paging and show-relay intercom for announcements and listening in, states the latency, and leaves split-second cues to the cue-light set it pairs with. Coexistence of 2.4 GHz audio with wireless microphones was not resolved by the research and is treated as an on-site test, not an assumption. As researched November 2026 by web search; verify before relying on it.
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 10 amateur groups or schools pre-order at €349 after a video demo that states the latency and the 'paging, not cueing' scope, and do 5 of them already own or pre-order the cue-light set? Pass = 10 deposits, 5 paired, in 6 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Amateur theatres, school and university stages, churches with performances, small event venues; the same buyers as the cue-light set, which this pairs with.

**The problem as the pack states it:** In a small venue the dressing rooms cannot hear the show and the stage manager cannot call 'five minutes to places' without running; the professional show-relay and paging systems that solve it are installed products priced for theatres with a technical budget.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **ControlBooth** · https://www.controlbooth.com/ — technical-theatre forum; the show-relay and paging threads live here.
- **r/techtheatre** · https://www.reddit.com/r/techtheatre/ — stage managers and technicians, many in schools and amateur theatre.
- **The Blue Room (UK)** · https://www.blue-room.org.uk/ — UK technical-theatre forum; DIY cue-light threads live here.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€299–399, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how amateur theatres, school and university stages, churches with performances, small event venues deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do the dressing rooms hear the show and the calls today, and what have you improvised that failed?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights. On a scale of one to ten, how likely would you be to buy that at €299–399, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Backstage Relay: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Backstage Relay: A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights. Before we spend money on tooling I want to find out whether this solves a real problem for amateur theatres, school and university stages, churches with performances, small event venues.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €299–399 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

ControlBooth and similar forums show the demand: groups with no budget asking how to get the show into the dressing rooms and announcements back out, and ready to build it. The research also found the failure to avoid: a venue reported that WiFi and ESP-NOW-style paging was "virtually useless for cueing" because of latency. That is right, and it is why this product is not a cueing system: paging and show relay tolerate a half second; cues do not and stay with the cue-light set. A second open point stays open: 2.4 GHz coexistence with the venue's wireless microphones was not resolved by the research or a clean comparison, so the pack calls for an on-site test and does not assume it is fine.

**Who pays:** the society or school (small budgets, equipment grants); bundled with the cue-light set the buyer is the same stage manager. **Who uses:** actors in the dressing rooms (listen), the stage manager (page), front of house (page).

### Market size (estimates — check)

- **TAM:** amateur theatre groups, schools with a stage and small venues across DE/UK/NL/AT/CH: tens of thousands. Theoretical €10–20M.
- **SAM:** groups that already own some technical kit and stage two or more productions a year: estimate 10,000 → €3.5M.
- **SOM (3 yrs):** 1,500–2,500 sets, half of them with the cue-light set; year-1: 300–500.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Clear-Com / Tecpro show relay and paging | Installed professional systems, thousands of euros | A tenth of the price, portable, battery |
| Williams AV and assistive-listening transmitters | Professional audio distribution | Different purpose and price class |
| Baby monitors and walkie-talkies | Cheap improvisations found on the forums | Multi-room, page button, proper speakers, pairs with the cue lights |
| DIY builds on ControlBooth and similar | Groups building their own | Demand signal; we ship the box and state the limits |

**Wedge:** a boxed, honest paging and show-relay set at a tenth of professional prices, sold alongside the cue lights so each does the job it can do.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| ControlBooth forum threads | Low-budget groups asking for and building show relay / paging | Demand signal |
| Venue report on WiFi / ESP-NOW paging latency | "Virtually useless for cueing" | Scope fixed: paging, not cues |
| Clear-Com / Tecpro show relay | Professional installed systems, thousands of euros | Incumbent at a multiple of the target |

**Verdict as researched: UNCERTAIN.** Main risk: Repositioned before building as a paging and show-relay intercom for non-time-critical communication, paired with the cue-light set rather than replacing it; 2.4 GHz interference with wireless microphones stays unverified and needs on-site testing.
<!-- market-competitors:end -->

### Product & value proposition

- Stage station: microphone (switchable stage pickup), page button, level control, USB-C power; optional front-of-house station.
- Speakers: battery (one show per charge, estimate), quiet show-relay level with page override at full volume, wall hook and stand; three in the set, up to eight.
- Link: WiFi (venue network) or ESP-NOW point-to-multipoint; latency stated on the box (target under 300 ms; measured value published); not for cues.
- Coexistence: a built-in channel scan and a printed on-site test procedure for venues with wireless microphones; recommendation to test before the first show.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €60–90) | 75.0 | 60.0 |
| PCBA assembly + test | 7.0 | 4.5 |
| Enclosure / mechanics (tooling amortised separately) | 14.0 | 9.8 |
| Packaging, cable, leaflet | 5.0 | 3.8 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 5.0 | 2.5 |
| Certification amortised (€10k, estimate) | 10.0 | 2.0 |
| **Landed cost** | **116.0** | **82.6** |
| Channel cost (direct + theatre suppliers, ~€28 per set) | 28.0 | 28.0 |
| Net price received (€349 incl. 19% VAT → €293.3 ex VAT) | 293.3 | 293.3 |
| **Gross margin per unit** | **€149.3 (51%)** | **€182.7 (62%)** |

Lesson: four enclosures and three cells per set; bundle with the cue-light set to share the sales effort and the shipping box.

### Go-to-market

**First 100 customers:**

1. Ten groups from one federation, half of them existing cue-light pre-orderers, after a video demo that shows the latency honestly.
2. Drama departments through their teachers' association.
3. Small venues and churches via AV hire companies.

**Scale channels:** theatre suppliers, federation festivals, the cue-light customer list.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question pre-orders; works-like set on AtomS3 + MIC + Speaker-Plus; latency measured and published; coexistence test with a borrowed wireless-mic rack. |
| Q2 | Custom boards (station, speaker); enclosures; EVT 10 sets with two groups. |
| Q3 | DVT; certification; 200 sets; bundle with cue lights. |
| Q4 | Supplier listing; 500 sets; eight-speaker option. |

**Team:** one embedded engineer with audio experience, one founder from the theatre world (shared with the cue-light pack); enclosure design bought in.

**Funding to first production (estimates):** NRE €22k + certification €10k + first 500 sets landed ~€45k ≈ €77k; minus pre-orders ~€20k ≈ €57k.

### Top risks

| Risk | Mitigation |
|---|---|
| Buyers expect it to call cues | Say 'paging and show relay, not cues' everywhere; bundle with the cue lights; publish the latency |
| 2.4 GHz interference with wireless microphones | On-site test procedure; channel scan; do not claim coexistence until tested in real venues |
| Audio quality and dropouts over WiFi | Codec and buffer choice; ESP-NOW mode; EVT in steel-framed halls |
| Battery life for a long show | One show per charge target; USB-C power option for fixed speakers |

## 4. Start kit

### Boards to start from

- [M5Stack Unit MIC (U096)](https://www.gongbans.com/db/m5stack-unit-mic.html) — microphone unit for the stage talk station (design files published for the module; electronics not open)
- [M5Stack Unit Mini PDM (U089)](https://www.gongbans.com/db/m5stack-unit-mini-pdm.html) — digital microphone alternative (design files published for the module; electronics not open)
- [Seeed Grove-Speaker-Plus](https://www.gongbans.com/db/seeed-grove-speaker-plus.html) — open amplified speaker reference circuit (open files: schematic)
- [M5Stack AtomS3-Lite (C124)](https://www.gongbans.com/db/m5stack-atoms3-lite.html) — ESP32-S3 core for stations and speakers (design files published for the module; electronics not open)
- [M5Stack Unit Button (U027)](https://www.gongbans.com/db/m5stack-unit-button.html) — push-to-page button (design files published for the module; electronics not open)

The Seeed speaker board publishes its schematic; the M5Stack microphone and core units are the prototype path; two PCBs (station, speaker).

### Block diagram

```
  STAGE STATION: [mic] [page button] -> [ESP32-S3] -> WiFi / ESP-NOW -> SPEAKERS 1..8: [ESP32-S3] -> [amp + speaker] [cell]
                                            quiet show relay  |  page = full volume     latency stated; not for cues
  pair with: cue-light set (standby / go)
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| Microphone + preamp | 4.0 |  |
| ESP32-S3 modules ×4 | 10.0 |  |
| Amplifier + speaker ×3 | 18.0 |  |
| Li-ion cells + chargers ×3 | 12.0 |  |
| Enclosures ×4 | 16.0 |  |
| PCBs, buttons, USB-C, passives | 10.0 |  |

### Firmware/software starting point

- ESP-IDF; I2S capture, low-bit-rate codec, multicast over WiFi or ESP-NOW with jitter buffer; page override; channel scan; latency measurement mode.
- Pairing by button; no app required; optional web page for levels.

### 12-week build plan

1. Pre-orders with an honest demo video; interviews
2. Prototype set
3. Latency and dropout measurements
4. Coexistence test with wireless mics
5. Two PCBs v1
6. Enclosures
7. EVT 10 sets in two venues
8. Show feedback
9. Tooling decision
10. DVT
11. Pre-compliance
12. Certification; bundle fulfilment

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal.

### Validation toolkit

- **Kill question:** Do 10 amateur groups or schools pre-order at €349 after a video demo that states the latency and the 'paging, not cueing' scope, and do 5 of them already own or pre-order the cue-light set? Pass = 10 deposits, 5 paired, in 6 weeks.
- **Cheapest experiment:** A three-speaker prototype in one group's dressing rooms for one production, latency and interference noted; ask ten groups whether they would buy at €349 knowing it does not call cues.
- **5-question interview:** 1) How do your dressing rooms hear the show and the calls today? 2) What have you improvised and what failed? 3) Do you use wireless microphones; how many channels? 4) Who pays for kit and when? 5) At €349 for a station and three speakers, paging only, would you order?
- **Landing page:** headline "Five minutes to places, heard in every dressing room." Bullets: show relay and paging; three battery speakers; pairs with the cue lights; not for cues; €349. Button: refundable €50 deposit.
- **Pass threshold:** 10 deposits, 5 of them paired with the cue-light set, in 6 weeks.

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

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit MIC (U096)](/db/m5stack-unit-mic.html) (microphone unit for the stage talk station); [M5Stack Unit Mini PDM (U089)](/db/m5stack-unit-mini-pdm.html) (digital microphone alternative); [M5Stack AtomS3-Lite (C124)](/db/m5stack-atoms3-lite.html) (ESP32-S3 core for stations and speakers); [M5Stack Unit Button (U027)](/db/m5stack-unit-button.html) (push-to-page button). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Speaker-Plus](/db/seeed-grove-speaker-plus.html) (open amplified speaker reference circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Jieli Technology** (珠海市杰理科技股份有限公司) · zh-jieli.com — TWS SoC chip solution house: AC69xx/AC70xx TWS SoC; 27B+ chips shipped; clients: Xiaomi / QCY / HP / Lenovo. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Fenda Technology** (深圳市奋达科技股份有限公司) · fenda.com — TWS earbuds / smart speaker ODM: TWS earbuds; smart speaker; smart home; clients: Amazon / Creative / Philips. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Haoern Acoustics** (深圳市豪恩声学股份有限公司) · haoen.cn — TWS / headphone ODM: TWS; ANC headphone; smart speaker; clients: vivo / RAZER / BEATS / HP. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Antixun** (深圳市安特信技术有限公司) · no website on file — TWS / smart audio ODM: TWS; ANC earphone; smart speaker; pivoted from solution house to ODM 2018. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus — for a Backstage Relay

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Backstage Relay: A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights. The design is built around your M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus.
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
主题：样品订购及批量报价 — M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus — 用于Backstage Relay

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Backstage Relay：A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights。产品设计基于贵司的M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus。
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
Subject: PCBA quote from open design files — Backstage Relay, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Backstage Relay: A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights. The design starts from published open-hardware files (M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Backstage Relay，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Backstage Relay：A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights。设计基于已公开的开源硬件文件（M5Stack Unit MIC (U096), M5Stack Unit Mini PDM (U089), M5Stack AtomS3-Lite (C124), M5Stack Unit Button (U027), Seeed Grove-Speaker-Plus；含原理图、PCB和BOM），并做了我们自己的修改。

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
