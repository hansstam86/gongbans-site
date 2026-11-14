# Hall Heat Scheduler — Founder Start Pack

> A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Halls are heated on a weekly timer set years ago: the Tuesday training that moved, the cancelled Saturday tournament and the empty Monday all get heated, and the club pays. Nobody sells a small controller that reads the booking calendar.
- **Customer:** Sports clubs (the treasurer and the hall warden), parishes with a parish hall, municipalities running community halls, with electricians and heating installers as the fitters. The heating bill payer pays; the saving is the argument.
- **Product:** A DIN-rail box that reads the booking calendar and a presence sensor, keeps a frost guard, pre-heats before bookings and drops the set-point when the hall is empty, drives the boiler enable or a zone valve, and reports heating hours saved on a local page; no cloud. Target price €299–399 (estimate).
- **Why now:** Clubs manually fight heated empty halls (German sports-federation guidance describes exactly this), energy prices made the bill visible, and the building-automation rules that exist are sized for far bigger buildings, so nothing forces a solution and nobody sells a small one.
- **The ask:** ~€55–70k to certification and a first 500 units (estimate); five paid pilots cover a quarter.

<!-- market-check:start -->
> **External market check (November 2026): UNCERTAIN.** The compliance angle does not hold: EU EPBD building-automation thresholds (70–290 kW) are sized for buildings much bigger than a typical sports or parish hall. German sports-federation guidance (DFB) confirms clubs manually fight this exact problem today, so the pain is real, but cost-driven, not compliance-driven. **Main risk:** Pitch reworked before building: sold on measured heating savings and the B2B buyer only; no mandate is claimed. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
>
> **Built with the research fix applied (November 2026).** The research found that the EU building-automation requirements (EPBD, 70–290 kW thresholds) do not apply to halls this size, so this pack claims no compliance pull. It is sold on the heating hours it measurably saves, to the club or parish that pays the bill, with the installer as the channel; the kill question requires a measured saving. As researched November 2026 by web search; verify before relying on it.
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 5 clubs or parishes install a paid pilot at €349 and measure heating hours saved for one month? Pass = 5 pilots and a measured saving in at least 3.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Sports clubs, parishes and municipal hall managers who pay the heating bill; electricians and heating installers who fit it. Sold on cost savings, not on compliance.

**The problem as the pack states it:** Halls are heated on a weekly timer set years ago: the Tuesday training that moved, the cancelled Saturday tournament and the empty Monday all get heated, and the club pays. Nobody sells a small controller that reads the booking calendar.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **DOSB (DE)** · https://www.dosb.de/ — German sports confederation; the regional Landessportbund reaches the clubs.
- **HaustechnikDialog (DE)** · https://www.haustechnikdialog.de/ — German heating installers and owners; hydronic balancing, heat pumps, legionella.
- **ZVSHK** · https://www.zvshk.de/ — German plumbing/heating installer federation; the local Innung is the way in.

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
Thanks for the time. I am looking into how sports clubs, parishes and municipal hall managers who pay the heating bill deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Who sets the hall heating, when was it last changed, and what did heating cost you last winter?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody. On a scale of one to ten, how likely would you be to buy that at €299–399, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Hall Heat Scheduler: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Hall Heat Scheduler: A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody. Before we spend money on tooling I want to find out whether this solves a real problem for sports clubs, parishes and municipal hall managers who pay the heating bill.

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

German sports-federation guidance (DFB) confirms that clubs manually fight this exact problem: someone remembers to turn the heating down, or does not. The underlying pain is cost, not compliance: the research found that the EU's building-automation requirements (EPBD thresholds at 70–290 kW) are sized for buildings far bigger than a parish or sports hall, so this pack does not claim a mandate and does not need one; a hall heated 30 fewer hours a month pays for the box in a season (estimate; verify with the pilot).

**Who pays:** the club or parish (B2B with small budgets and energy-saving grants), the municipality for its halls. **Who installs:** an electrician or heating installer, who also becomes the channel. **Who uses:** the hall warden, via a local page and the booking calendar they already keep.

### Market size (estimates — check)

- **TAM:** ~90,000 sports clubs in Germany, tens of thousands of parish and community halls across DE/NL/UK/AT/CH. Theoretical €50M+ at €349.
- **SAM:** halls with a gas or oil boiler and a digital booking calendar: estimate 40,000 → €14M.
- **SOM (3 yrs):** 4,000–8,000 units through installers and federations; year-1: 300–500.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Building-management systems (Siemens, Honeywell and integrators) | Quote-based, €5k and up, sized for large buildings | A tenth of the price, sized for one hall |
| Smart thermostats (tado°, Netatmo) | Consumer, cloud, schedule-based | Calendar-driven and presence-aware; no cloud account for a club |
| Church-heating specialists | Installed systems, quote-based | Retrofit box on the existing boiler |
| The weekly timer and the warden's memory | Free | That is the cost we remove |

**Wedge:** the booking calendar as the heating schedule, in a box an installer fits in an afternoon, sold on the saving it measures itself.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| EU EPBD building-automation thresholds (70–290 kW) | Apply to large buildings only | No compliance pull for halls; claim dropped |
| DFB (German football federation) guidance on hall heating | Clubs manually manage heating of empty halls | The pain is real and cost-driven |

**Verdict as researched: UNCERTAIN.** Main risk: Pitch reworked before building: sold on measured heating savings and the B2B buyer only; no mandate is claimed.
<!-- market-competitors:end -->

### Product & value proposition

- Inputs: booking calendar (CalDAV, Google, common club booking tools via ICS), presence (PIR / thermal), hall temperature, outside temperature from the net or a sensor.
- Logic: pre-heat time learned per hall, set-back when empty, frost guard, manual boost button for the unplanned use, holiday mode.
- Outputs: boiler enable contact or zone valve through an SSR / relay rated for the signal, never the burner mains; optional second zone.
- Reporting: local page with heating hours by week, estimated saving; CSV; no cloud.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €60–90) | 75.0 | 60.0 |
| PCBA assembly + test | 6.0 | 3.9 |
| Enclosure / mechanics (tooling amortised separately) | 10.0 | 7.0 |
| Packaging, cable, leaflet | 3.0 | 2.2 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 4.0 | 2.0 |
| Certification amortised (€15k, estimate) | 15.0 | 3.0 |
| **Landed cost** | **113.0** | **78.2** |
| Channel cost (installer channel margin, ~€40) | 40.0 | 40.0 |
| Net price received (€349 incl. 19% VAT → €293.3 ex VAT) | 293.3 | 293.3 |
| **Gross margin per unit** | **€140.3 (48%)** | **€175.1 (60%)** |

Lesson: certification for a mains-connected controller is the big first-run item; the installer's margin is what makes the channel work. Price the second zone as an add-on.

### Go-to-market

**First 100 customers:**

1. Five clubs or parishes in one region, each a paid pilot with a one-month measurement.
2. Two heating installers who fit the pilots and quote it afterwards.
3. A regional sports federation newsletter once the savings are measured.

**Scale channels:** heating installers and electricians, sports federations (Landessportbünde), church administrations, municipal energy advisers.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question conversations; works-like controller on StamPLC + PIR + ENV-III reading one club's calendar; pilot contracts. |
| Q2 | Custom board; enclosure; EVT 5 pilots installed by one installer; saving measured. |
| Q3 | DVT; certification; 200 units; installer kit. |
| Q4 | Federation channel; 500 units; second-zone option. |

**Team:** one embedded engineer, one developer for calendar integrations, one founder who knows clubs and installers.

**Funding to first production (estimates):** NRE €20k + certification €15k + first 500 units landed ~€40k ≈ €75k; minus pilots ~€9k ≈ €66k.

### Top risks

| Risk | Mitigation |
|---|---|
| Savings smaller than hoped | Measure in the pilot before scaling; pick halls with the worst timers first |
| Boiler interfaces vary | Support the standard enable contact and a zone valve; installer decides; document the common boilers |
| Clubs do not keep a digital calendar | ICS from any tool; a simple built-in weekly schedule with exceptions as fallback |
| Installer-fitted product with certification cost | Quote the lab first; design to the standard |

## 4. Start kit

### Boards to start from

- [M5Stack StamPLC AC (A160)](https://www.gongbans.com/db/m5stack-stamplc-ac.html) — mains-powered DIN controller core (design files published for the module; electronics not open)
- [M5Stack StamPLC (K141)](https://www.gongbans.com/db/m5stack-stamplc.html) — DIN-rail PLC-style controller (design files published for the module; electronics not open)
- [M5Stack Unit PIR (U004)](https://www.gongbans.com/db/m5stack-unit-pir.html) — presence detection in the hall (design files published for the module; electronics not open)
- [M5Stack Unit TMOS PIR (U185)](https://www.gongbans.com/db/m5stack-unit-tmos-pir.html) — thermal presence that sees a still person (design files published for the module; electronics not open)
- [Seeed Grove-Solid State Relay V2](https://www.gongbans.com/db/seeed-grove-solid-state-relay-v2.html) — open SSR reference for the boiler enable signal (open files: schematic)
- [M5Stack Unit ENV-III (U001-C)](https://www.gongbans.com/db/m5stack-unit-env-iii.html) — hall temperature and humidity (design files published for the module; electronics not open)
- [M5Stack Unit RTC (U126)](https://www.gongbans.com/db/m5stack-unit-rtc.html) — schedule keeping without network (design files published for the module; electronics not open)

The StamPLC family is the DIN controller; the Seeed SSR board publishes its schematic as the enable-output reference; the M5Stack presence and environment units are the sensors for the prototype.

### Block diagram

```
  [booking calendar: CalDAV / ICS]  [PIR / thermal presence]  [hall temp]  [outside temp]
                 \                 |                  /             /
                  -> [StamPLC controller: pre-heat, set-back, frost guard] -> [SSR] -> boiler enable / zone valve
                                   |  local page: heating hours, saving        [boost button in the hall]
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| ESP32-S3 DIN controller board (StamPLC-class) | 14.0 |  |
| PIR / thermal presence unit | 6.0 |  |
| T/RH sensor | 2.0 |  |
| SSR / relay for the enable signal | 4.0 |  |
| Certified mains PSU module | 7.0 |  |
| DIN enclosure, terminals, boost button | 14.0 |  |
| PCB, RTC, passives | 6.0 |  |

### Firmware/software starting point

- ESP-IDF; ICS/CalDAV parsing locally; schedule engine with learned pre-heat; presence hold-off; frost guard independent of network.
- Local web page; CSV; MQTT optional; no cloud.
- Safe states on power loss and network loss (timer fallback).

### 12-week build plan

1. Interviews with clubs and installers; pilot proposals
2. Prototype on StamPLC
3. Calendar engine and pre-heat learning
4. Enclosure and terminals
5. Custom board v1
6. Certification quotes and standard study
7. EVT 5 pilots installed
8. One month of measurement
9. Installer manual
10. DVT
11. Pre-compliance and safety tests
12. Certification submission

### Certification checklist (EU)

- Everything in the standard list (RED if radio, EMC, RoHS/REACH, WEEE, CRA) **plus LVD / EN 62368-1 or EN 60730-1 for a mains-connected control device**; the switched load goes through an installer-fitted contactor or SSR rated for it, never through the box's own relay above its rating.
- Installer-fitted product: write the installation manual for an electrician, not a consumer; label the box accordingly.
- Budget the lab at the high end (estimate; get two quotes) and allow one re-spin.

### Validation toolkit

- **Kill question:** Do 5 clubs or parishes install a paid pilot at €349 and measure heating hours saved for one month? Pass = 5 pilots and a measured saving in at least 3.
- **Cheapest experiment:** One prototype in one club hall for a month, logging boiler hours against the previous month's timer; show the number to five clubs with a €349 price.
- **5-question interview:** 1) Who sets the hall heating and when did they last change it? 2) What did heating cost last winter? 3) Do you keep bookings in a calendar; which? 4) Who would fit something on the boiler? 5) If it saved 30 hours a month, would you pay €349 plus fitting?
- **Landing page:** headline "Heat the hall when the calendar says so." Bullets: reads your bookings; knows when the hall is empty; shows the hours saved; €349 fitted by your installer. Button: request a pilot (B2B).
- **Pass threshold:** 5 paid pilots and a measured saving in at least 3 within 10 weeks.

### First production checklist

- 10 golden samples measured and photographed; one per enclosure colour.
- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).
- MOQ talk: module, enclosure, packaging; get the next price break in writing.
- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.
- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.
- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.
- Safety: 100% hi-pot and relay test; installer note in every box.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack StamPLC AC (A160)](/db/m5stack-stamplc-ac.html) (mains-powered DIN controller core); [M5Stack StamPLC (K141)](/db/m5stack-stamplc.html) (DIN-rail PLC-style controller); [M5Stack Unit PIR (U004)](/db/m5stack-unit-pir.html) (presence detection in the hall); [M5Stack Unit TMOS PIR (U185)](/db/m5stack-unit-tmos-pir.html) (thermal presence that sees a still person); [M5Stack Unit ENV-III (U001-C)](/db/m5stack-unit-env-iii.html) (hall temperature and humidity); [M5Stack Unit RTC (U126)](/db/m5stack-unit-rtc.html) (schedule keeping without network). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Solid State Relay V2](/db/seeed-grove-solid-state-relay-v2.html) (open SSR reference for the boiler enable signal). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2 — for a Hall Heat Scheduler

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Hall Heat Scheduler: A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody. The design is built around your M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2.
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
主题：样品订购及批量报价 — M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2 — 用于Hall Heat Scheduler

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hall Heat Scheduler：A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody。产品设计基于贵司的M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2。
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
Subject: PCBA quote from open design files — Hall Heat Scheduler, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Hall Heat Scheduler: A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody. The design starts from published open-hardware files (M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Hall Heat Scheduler，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hall Heat Scheduler：A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody。设计基于已公开的开源硬件文件（M5Stack StamPLC AC (A160), M5Stack StamPLC (K141), M5Stack Unit PIR (U004), M5Stack Unit TMOS PIR (U185), M5Stack Unit ENV-III (U001-C), M5Stack Unit RTC (U126), Seeed Grove-Solid State Relay V2；含原理图、PCB和BOM），并做了我们自己的修改。

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
