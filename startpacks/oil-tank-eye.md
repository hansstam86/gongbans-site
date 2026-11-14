# Tank Eye — Founder Start Pack

> A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of households heat with oil and read the tank with a dipstick or a float gauge in the cellar; the connected sensors on the market charge a monthly fee for a number that changes once a day.
- **Customer:** Oil-heated households in DE/AT/CH (and pellet-store and rainwater-cistern owners with the same problem), holiday-home owners who want to know from afar, heating-oil dealers who would like to know when to call. The homeowner pays; Home Assistant users buy first.
- **Product:** A sensor that screws into a spare lid opening, a small display puck for the hallway, a local web page and MQTT, consumption trend and low-level alerts by e-mail, LoRa option for tanks out of WiFi range; no account, no fee. Target price €79–99 (estimate).
- **Why now:** The two known connected tank sensors bill a subscription on top of the device, oil prices made households watch their tank, and the ESPHome community has built this sensor hundreds of times without anyone boxing it.
- **The ask:** ~€35–45k to certification and a first 1,000 units (estimate); forum pre-orders cover a third.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Oilfox is confirmed subscription-based (about £6 a month) and Boilerjuice Connected costs £75 plus £4.99 a month, a real no-subscription wedge; the ESPHome / Home Assistant DIY precedent is strong and active (simon42, rogerfrost and multiple build threads). **Main risk:** Explosion-safety (ATEX) requirements for a sensor in an oil-tank headspace are unverified; a compliance check is needed before launch and the pack does not claim it is fine. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> 100 members of a German heating forum offered it at €89 with "no account, no subscription": 30 refundable deposits in 3 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a fake-door landing page that the roughly five million oil-heated homes in DE/AT/CH, holiday-home owners, small heating-oil dealers as a channel actually visited, with a measured conversion to a waitlist or refundable deposit, plus the interview notes behind it. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** The roughly five million oil-heated homes in DE/AT/CH, holiday-home owners, small heating-oil dealers as a channel; Home Assistant users as the first buyers.

**The problem as the pack states it:** Millions of households heat with oil and read the tank with a dipstick or a float gauge in the cellar; the connected sensors on the market charge a monthly fee for a number that changes once a day.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **HaustechnikDialog (DE)** · https://www.haustechnikdialog.de/ — German heating installers and owners; hydronic balancing, heat pumps, legionella.
- **Photovoltaikforum (DE)** · https://www.photovoltaikforum.com/ — German PV, battery, heat-pump and dynamic-tariff owners.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (twenty people from the audience line), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79–99, the pack's estimate), and one button. For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how the roughly five million oil-heated homes in DE/AT/CH, holiday-home owners, small heating-oil dealers as a channel deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you check your tank today, how often, and when did you last run low unexpectedly?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription. On a scale of one to ten, how likely would you be to buy that at €79–99, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Tank Eye: would you pay €79–99 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Tank Eye: A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79–99, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

Oilfox (device plus a yearly subscription) and Boilerjuice Connected (£75 plus £4.99 a month) have shown that people pay to see their tank from the phone, and that they resent the fee. On the Home Assistant and ESPHome forums the same device is built again and again from an ESP32 and an ultrasonic or ToF sensor; the threads are long because the tank-shape maths and the mounting are fiddly. A boxed version with a tank wizard is the missing product.

**Who pays:** the homeowner (B2C) and the holiday-home owner; heating-oil dealers as a channel that may subsidise the device for the order signal. **Who uses:** everyone in the house, via the hallway puck.

### Market size (estimates — check)

- **TAM:** ~5M oil-heated homes in DE plus AT/CH, plus pellet stores and cisterns. Theoretical €400M+.
- **SAM:** households that already own a smart-home device or buy from an online heating-oil dealer: estimate 1M → €90M.
- **SOM (3 yrs):** 20,000–40,000 units; year-1: 2,000–4,000 through forums, Home Assistant channels and one dealer partnership.

### Competition (3 searches, incl. the November 2026 external market check)

| Alternative | What it is / price found | Why we still win |
|---|---|---|
| Oilfox | Connected tank sensor; device plus subscription (about £6 a month, research Nov 2026) | No fee, no account; local data |
| Boilerjuice Connected (UK) | £75 + £4.99 a month | Same |
| Watchman Sonic Advanced | Ultrasonic sender + receiver, no app | We add the trend, the alert and MQTT at a similar price |
| Tecson and similar ultrasonic gauges | €150–250, wired display | Half the price with WiFi |
| ESPHome / Home Assistant DIY builds (simon42, rogerfrost and many threads) | Free if you have a weekend | The customer wants the box and the tank wizard |

**Wedge:** the DIY device everyone builds, boxed, with a tank-shape wizard and no subscription.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Oilfox | Device + subscription (~£6/month) | Incumbent with the fee |
| Boilerjuice Connected | £75 + £4.99/month | Incumbent with the fee |
| Watchman Sonic Advanced | Ultrasonic sender + receiver | Incumbent without app |
| simon42 / rogerfrost ESPHome builds and Home Assistant threads | DIY tank sensors | Strong demand signal, no boxed product |

**Verdict as researched: LIKELY.** Main risk: Explosion-safety (ATEX) requirements for a sensor in an oil-tank headspace are unverified; a compliance check is needed before launch and the pack does not claim it is fine.
<!-- market-competitors:end -->

### Product & value proposition

- Sensor head for the standard 2-inch (G2) lid opening and a universal flange; ultrasonic for large tanks, ToF for small ones; sealed against vapour.
- Tank wizard: cylinder, cuboid, battery of tanks, custom table; litres and days-to-empty.
- Hallway puck with an OLED showing litres and trend; WiFi local page; MQTT; e-mail alert at a set level; no cloud.
- LoRa variant for the barn or the garden cistern.
- Pellet-store and rainwater modes are the same device with a different wizard.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (estimate, mid of €14–20) | 17.0 | 13.6 |
| PCBA assembly + test | 2.5 | 1.6 |
| Enclosure / mechanics (tooling amortised separately) | 4.5 | 3.1 |
| Packaging, cable, leaflet | 2.0 | 1.5 |
| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | 2.0 | 1.0 |
| Certification amortised (€9k, estimate) | 9.0 | 1.8 |
| **Landed cost** | **37.0** | **22.7** |
| Channel cost (direct and dealer channel, ~€8) | 8.0 | 8.0 |
| Net price received (€89 incl. 19% VAT → €74.8 ex VAT) | 74.8 | 74.8 |
| **Gross margin per unit** | **€29.8 (40%)** | **€44.1 (59%)** |

Lesson: the sensor head and the puck are two small enclosures; keep the puck optional to hit €79 for the Home Assistant crowd.

### Go-to-market

**First 100 customers:**

1. Pre-orders from two German heating forums and the Home Assistant community.
2. One online heating-oil dealer offering it to customers.
3. Holiday-home owners via vacation-rental forums.

**Scale channels:** heating-oil dealers (they want the order signal), smart-home retailers, heating installers.

### 12-month plan

| Quarter | Milestones |
|---|---|
| Q1 | Kill-question pre-orders; works-like prototype on Unit Ultrasonic + AtomS3 on a real tank; tank wizard. |
| Q2 | Custom PCB and sensor head; EVT 30 in forum members' cellars; ATEX question answered with a notified body or a test house. |
| Q3 | DVT; certification; 500 units; pre-orders shipped. |
| Q4 | Dealer partnership; LoRa variant; 2,000 units. |

**Team:** one embedded engineer, one founder; mechanical design of the sensor head bought in.

**Funding to first production (estimates):** NRE €15k + certification and the ATEX assessment €10–14k + first 1,000 units landed ~€22k ≈ €50k; minus pre-orders ~€12k ≈ €38k.

### Top risks

| Risk | Mitigation |
|---|---|
| Explosion-safety rules for a sensor in a tank headspace | Verify before launch: heating oil's flash point is above 55 °C, but confirm whether any ATEX zoning applies to the lid opening; design for intrinsically low energy either way; do not claim it is fine until a test house says so |
| Vapour fouls the sensor | Sealed head; ToF behind a window; field test over a winter |
| Oilfox cuts its fee | Our wedge is also local data and the puck; stay cheaper |
| Tank-shape maths wrong | Wizard with a dipstick calibration step |

## 4. Start kit

### Boards to start from

- [M5Stack Unit Ultrasonic-I2C (U098-B1)](https://www.gongbans.com/db/m5stack-unit-ultrasonic-i2c.html) — ultrasonic distance unit for the tank lid (design files published for the module; electronics not open)
- [M5Stack Unit ToF (U010)](https://www.gongbans.com/db/m5stack-unit-tof.html) — time-of-flight alternative for small tanks (design files published for the module; electronics not open)
- [Seeed Grove-Ultrasonic Ranger](https://www.gongbans.com/db/seeed-grove-ultrasonic-ranger.html) — open ultrasonic ranger reference circuit (open files: schematic)
- [M5Stack AtomS3-Lite (C124)](https://www.gongbans.com/db/m5stack-atoms3-lite.html) — ESP32-S3 WiFi core (design files published for the module; electronics not open)
- [M5Stack Stamp C6LoRa (S012)](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) — LoRa variant for tanks out of WiFi range (open files: pcb,schematic)
- [M5Stack Unit OLED (U119)](https://www.gongbans.com/db/m5stack-unit-oled.html) — local display at the tank or in the hallway (design files published for the module; electronics not open)

The Seeed ultrasonic ranger publishes its schematic; the M5Stack units and the AtomS3 give the fastest prototype; the Stamp C6LoRa (open files) is the LoRa variant's core.

### Block diagram

```
  TANK LID: [ultrasonic / ToF sensor, sealed] -> [ESP32-S3] -> WiFi -> local page, MQTT, e-mail alert
                                                   |  LoRa variant: [Stamp C6LoRa] -> gateway in the house
  HALLWAY: [OLED puck: litres, trend, days left]
```

### Starter BOM (estimates)

| Part | Est. € (1k) | Note |
|---|---|---|
| Ultrasonic or ToF sensor | 3.0 | ToF for small tanks |
| ESP32-S3 module | 2.5 |  |
| Sensor head enclosure + G2 thread + seal | 4.5 |  |
| Hallway puck: OLED + ESP32-C3 + enclosure | 6.0 | optional |
| PCB, USB-C, passives | 2.0 |  |

### Firmware/software starting point

- ESPHome-compatible firmware (the community can keep using its own) plus a stock firmware with the wizard and the local page.
- Median filtering, temperature compensation, tank geometry tables; MQTT discovery for Home Assistant.
- E-mail alert through the user's own SMTP or a free relay; no cloud of ours.

### 12-week build plan

1. Forum pre-orders live
2. Prototype on a real tank
3. Tank wizard and filtering
4. Sensor head design
5. ATEX question to a test house
6. Custom PCB v1
7. EVT 30 in volunteers' cellars
8. Winter fouling check
9. Puck design
10. DVT
11. Pre-compliance
12. Certification; shipping plan

### Certification checklist (EU)

- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.
- Test with the DVT build in the real enclosure; budget a re-spin for EMC.
- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).
- **Explosion safety:** obtain a written assessment for the sensor position in a heating-oil tank before sale; if zoning applies, the design changes (intrinsically safe) or the product is scoped to pellet and water tanks first.

### Validation toolkit

- **Kill question:** 100 members of a German heating forum offered it at €89 with "no account, no subscription": 30 refundable deposits in 3 weeks.
- **Cheapest experiment:** Post the prototype and a 60-second video in two heating forums with a €89 pre-order link and "no account, no subscription" in the title.
- **5-question interview:** 1) How do you check your tank today and how often? 2) Have you looked at Oilfox or similar; what stopped you? 3) What would you do with a daily consumption number? 4) Where is the tank: WiFi reach, lid openings free? 5) At €89 once, would you order?
- **Landing page:** headline "See your tank. No app account, no monthly fee." Bullets: fits a spare lid opening; litres and days left in the hallway; works with Home Assistant. Button: refundable €20 deposit.
- **Pass threshold:** 30 deposits from 100 forum members within 3 weeks.

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

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Ultrasonic-I2C (U098-B1)](/db/m5stack-unit-ultrasonic-i2c.html) (ultrasonic distance unit for the tank lid); [M5Stack Unit ToF (U010)](/db/m5stack-unit-tof.html) (time-of-flight alternative for small tanks); [M5Stack AtomS3-Lite (C124)](/db/m5stack-atoms3-lite.html) (ESP32-S3 WiFi core); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (LoRa variant for tanks out of WiFi range); [M5Stack Unit OLED (U119)](/db/m5stack-unit-oled.html) (local display at the tank or in the hallway). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Ultrasonic Ranger](/db/seeed-grove-ultrasonic-ranger.html) (open ultrasonic ranger reference circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger — for a Tank Eye

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Tank Eye: A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription. The design is built around your M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger.
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
主题：样品订购及批量报价 — M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger — 用于Tank Eye

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tank Eye：A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription。产品设计基于贵司的M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger。
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
Subject: PCBA quote from open design files — Tank Eye, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Tank Eye: A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription. The design starts from published open-hardware files (M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Tank Eye，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tank Eye：A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription。设计基于已公开的开源硬件文件（M5Stack Unit Ultrasonic-I2C (U098-B1), M5Stack Unit ToF (U010), M5Stack AtomS3-Lite (C124), M5Stack Stamp C6LoRa (S012), M5Stack Unit OLED (U119), Seeed Grove-Ultrasonic Ranger；含原理图、PCB和BOM），并做了我们自己的修改。

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
