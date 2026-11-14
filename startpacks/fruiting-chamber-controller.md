# Fruiting-Chamber Controller — Founder Start Pack

> One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Gourmet mushrooms (oyster, lion's mane, shiitake) fruit well only at 85–95% RH with fresh air. Hobby and micro-farm growers hack together a humidity plug, a timer fan and a US-import controller whose sensor is rated to 85% RH — exactly where mushrooms start.
- **Customer:** Home and urban mushroom growers and micro-farms in DE/NL/FR/UK; grow-shop retailers and grow-kit sellers as channel. The grower pays €139–199; the kit seller bundles it.
- **Product:** 12/24 V DC controller with a sealed NDIR CO2 + T/RH sensor pod on a cable, outputs for an ultrasonic fogger and a fan, fungi-tuned hysteresis, EU PSU, optional WiFi logging.
- **Why now:** The gourmet-mushroom wave is real (grow-kit market estimates US$0.4–1.2 B globally in 2025, Europe ~28%); incumbents are US-centric and not built for saturated humidity; every part exists in the catalogue.
- **The ask:** ~€45k to the first 1,000 units; pre-orders from grower communities fund half.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Real DIY precedent: ShroomBox (Blynk) and Raspberry Pi builds combine Inkbird CO2 and humidity controllers to hit the stated RH and CO2 targets, and a documented "fan and humidifier fighting each other" failure mode is exactly what a purpose-built controller fixes. **Main risk:** Inkbird units cost under €50 each; the integrated unit must clearly beat "buy two Inkbirds and wire them yourself". *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Post in the three biggest German/Dutch mushroom-growing groups with a €139 pre-order: 60 deposits in two weeks = go.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a fake-door landing page that home and urban mushroom growers and micro-farms in DE/NL/FR/UK actually visited, with a measured conversion to a waitlist or refundable deposit, plus the interview notes behind it. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Home and urban mushroom growers and micro-farms in DE/NL/FR/UK; grow-shop retailers.

**The problem as the pack states it:** Gourmet mushrooms (oyster, lion's mane, shiitake) fruit well only at 85–95% RH with fresh air. Hobby and micro-farm growers hack together a humidity plug, a timer fan and a US-import controller whose sensor is rated to 85% RH — exactly where mushrooms start.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/MushroomGrowers** · https://www.reddit.com/r/MushroomGrowers/ — hobby and small-farm mushroom growers.
- **Shroomery** · https://www.shroomery.org/forums/ — long-running mushroom-cultivation forum.
- **r/mycology** · https://www.reddit.com/r/mycology/ — mycology hobbyists.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (twenty people from the audience line), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€129–199, the pack's estimate), and one button. For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how home and urban mushroom growers and micro-farms in DE/NL/FR/UK deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about your last failed flush: what do you think went wrong with humidity, CO2 or temperature, and how would you have known earlier?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app. On a scale of one to ten, how likely would you be to buy that at €129–199, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Fruiting-Chamber Controller: would you pay €129–199 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Fruiting-Chamber Controller: One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €129–199, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
A fruiting chamber (a tub, a tent, a converted fridge, or a 10 m² room in a micro-farm) needs three things controlled: humidity (fogger/humidifier on-off), CO2 (fresh-air exchange fan), and sometimes temperature. The hobby solution is an Inkbird humidity controller (€50–85) that switches a mains humidifier and a timer-driven fan, with no CO2 sensing — so growers either over-ventilate (dry pins) or under-ventilate (long stems, small caps). The US controller brands offer good apps but their T/RH probes are rated to 85% RH, no CO2 at the hobby price, US plugs on grey imports, and no EU support.

Who pays: the grower (B2C, €139–199 — the price of two grow kits); micro-farms (B2B, 2–10 units per farm); grow-kit and spawn shops who want a controller to upsell.

### Market size (estimates — check them)
- **TAM:** Grow-kit market estimates for 2025 range US$0.4–1.2 B globally with Europe ~28% → **€100–300 M/year** of kit spend in Europe; controllers are an accessory to maybe 5% of serious growers. Plus ~2,000–4,000 micro-farms/urban farms in Europe (estimate).
- **SAM:** Growers who build a chamber (not just open a kit on the kitchen counter): say 150,000 households in DE/NL/FR/UK + 2,000 micro-farms; replacement/upgrade cycle 3 years → ~50,000 controller sales/year × €150 ≈ **€7.5 M/year**.
- **SOM (year 2):** 4,000 units ≈ **€560k revenue**.

### Competition (3 searches)
| Alternative | Price (EU, est.) | Weakness |
|---|---|---|
| Inkbird IHC-200 humidity controller + timer fan ("DIY standard") | €50–85 | Humidity only, mains switching in a wet place, no CO2 |
| AC Infinity Controller 69 Pro | €98–139 | No CO2 at that price, probe rated 35–85% RH, US-centric app and support |
| Home Assistant / Arduino DIY with an SCD41 | €40 in parts + weekends | Only for tinkerers |
| Commercial farm controllers | €1,000+ | Overkill for a tent |
| Do nothing — mist by hand twice a day | €0 | Pins dry out, no consistency |

**Wedge:** real NDIR CO2 + a sensor pod built to live at 95% RH, DC-only outputs (safe in a wet tent), EU plugs and support, fungi presets. The 85% RH probe rating of the incumbents is the headline.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Mercy for Animals fruiting-room guide | Grower guidance on RH/CO2 targets | Confirms the targets in the pitch |
| ShroomBox IoT build (Blynk) and Pi builds | DIY controllers | Demand signal and the DIY substitute |
| Inkbird humidity / CO2 controllers | Under €50 each | The component-level substitute to beat |

**Verdict as researched: LIKELY.** Main risk: Inkbird units cost under €50 each; the integrated unit must clearly beat "buy two Inkbirds and wire them yourself".
<!-- market-competitors:end -->

### Product & value proposition
- **Controller box:** ESP32-C3, 2 PWM/switched 12/24 V outputs (fogger, fan) + 1 spare (light/heater), 2-line OLED + knob, RJ11 sensor cable.
- **Sensor pod:** SCD41 (NDIR CO2 + T/RH) in a hydrophobic-membrane housing with a tiny heater pulse to shed condensation; replaceable.
- **Logic:** humidity hysteresis (e.g. 88–92%), CO2 ceiling with fan duty, "fresh-air flush" schedule, species presets (oyster, lion's mane, shiitake), manual override.
- **Optional WiFi:** logging to a simple web page/MQTT; works fully offline.
- **Pricing:** controller + pod **€139 incl. VAT** (B2C); bundle with 12 V fogger disc driver + 120 mm fan + EU PSU **€199**; micro-farm pack (3 controllers) €349 ex-VAT; replacement pod €39.

### Unit economics (estimates, controller + pod)
| Item | 1,000 units | 5,000 units |
|---|---|---|
| Electronics BOM (SCD41 €12, ESP32-C3 €2, drivers, OLED, PSU-less) | €27 | €22 |
| Assembly & test (incl. CO2 check in ambient air) | €5 | €3.50 |
| Enclosures (controller box + sealed pod with membrane) | €5 | €3.20 |
| Packaging, cables, EU PSU 24 V 2 A (certified) | €7.50 | €5.50 |
| Freight + duty to EU | €2.50 | €1.30 |
| Certification amortised (€15k) | €15 | €3 |
| **Landed cost** | **€62** | **€38.50** |
| Sell price ex-VAT (from €139 incl. 19% VAT) | €117 | €117 |
| Via grow shop (40% of €139 → net €70 ex-VAT) | — | €70 |
| **Gross margin direct** | **47%** | **67%** |
| **Gross margin via grow shop** | 11% | 45% |

Lesson: at 1k units sell direct only; the grow-shop channel works from 5k. The bundle (€199) carries better margin because fogger/fan/PSU are cheap.

### Go-to-market
**First 100 customers:** the three biggest German and Dutch mushroom-growing Facebook groups and the big English-language mushroom forums/subreddits; two YouTube growers for a review unit; grow-kit sellers' newsletters (give them an affiliate cut); one micro-farm as a pilot with photos of yield before/after.

**Scale:** grow shops (hydroponics retailers already stock the US brands), grow-kit sellers bundling the controller, Amazon.de/.nl/.fr, a "chamber in a box" partner (tent + fogger + controller).

### 12-month plan
- **Q1:** Breadboard with the Grove SCD41 + C3 devkit on a real tub, pre-order post in the groups. Gate: 60 deposits at €139 in two weeks.
- **Q2:** Own PCB, pod with membrane, 3 months of humidity-chamber testing (drift!), RED/EMC tests, first 300 units.
- **Q3:** 1,000 units, bundle SKU, first 10 grow shops, Amazon.
- **Q4:** Micro-farm pack, WiFi logging, second sensor variant (temperature/heater output).

**Team:** one firmware/hardware engineer (full-time for 6 months), one grower-marketer part-time (community, content), founder on ops. The enclosure/pod needs a mechanical freelancer for 4 weeks.

**Funding to 1,000 units (estimate):** NRE €20k (PCB, pod tooling €8k, test chamber) + certification €15k + 1,000 × €47 production = €47k → **~€82k**; 60 deposits + a 300-unit pre-order round covers ~€40k → cash need **~€45k**. Bootstrap/pre-orders; no investor needed.

### Top risks
- **Technical — sensor at saturation:** SCD41 drifts and condensation kills readings. Mitigation: membrane housing, periodic heater pulse, automatic self-calibration disabled and a weekly fresh-air calibration routine, replaceable pod at €39.
- **Market — hobby niche, incumbents could ship an EU version:** they already sell in Europe; mitigation is the 95% RH pod and CO2, and the community relationship.
- **Regulatory:** RED + EN 18031 if WiFi; EMC; EN 62368-1 at low voltage only (the PSU carries its own CE); CRA for the connected version. Mitigation: ship v1 offline-capable; WiFi as a firmware option after EN 18031.
- **Supply:** SCD41 is a sole-source part with 8–16 week lead times at times. Mitigation: order 2,000 early; design the pod footprint to accept the cheaper SCD40 too.

## 4. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [seeed-grove-co2-temperature-humidity-sensor-scd41](https://www.gongbans.com/db/seeed-grove-co2-temperature-humidity-sensor-scd41.html) | True NDIR CO2 + T/RH; the sensor pod reference circuit | schematic | Seeed wiki — check licence |
| [seeed-grove-water-atomization](https://www.gongbans.com/db/seeed-grove-water-atomization.html) | Ultrasonic fogger disc driver reference | schematic | Seeed wiki — check licence |
| [m5stack-unit-fan](https://www.gongbans.com/db/m5stack-unit-fan.html) | 12 V fan drive for prototypes | enclosure/structure only | Module |
| [espressif-esp32-c3-devkitm-1](https://www.gongbans.com/db/espressif-esp32-c3-devkitm-1.html) | Controller MCU reference design | schematic | Espressif reference files — permissive, check the download terms |

### Block diagram and engineering gap
```
[Sensor pod: SCD41 + membrane + heater] --I2C/RJ11--> ESP32-C3
ESP32-C3 --> [MOSFET out 1: fogger disc driver 24 V]  
         --> [MOSFET out 2: 120 mm fan, PWM]
         --> [MOSFET out 3: spare (light/heater)]
         --> [OLED + knob]      --WiFi optional--> web page / MQTT
[24 V 2 A EU PSU, certified] --> box; nothing above 24 V inside
```
Gap: the pod (condensation survival), fungi control logic and presets, DC-only power architecture, and a box that survives a wet tent (IP54 for the controller, pod IP67 with a breathable membrane).

### Starter BOM (per unit, estimates)
| Part | Est. cost | Note |
|---|---|---|
| SCD41 CO2/T/RH | €12 | Sole source, long lead — order early; footprint-compatible SCD40 as fallback |
| ESP32-C3 module (certified) | €2.00 | — |
| 3× N-MOSFET outputs + protection | €1.50 | — |
| OLED 0.96" + encoder knob | €2.20 | — |
| PCB + assembly | €4.50 | — |
| Pod housing + PTFE membrane + heater resistor | €3.00 | Membrane is a specialist part; 2 suppliers |
| Controller box, IP54, cable glands | €3.00 | Off-the-shelf box first |
| 24 V 2 A EU PSU (certified) | €4.50 | Buy certified; don't design mains |
| Fogger disc + driver, 120 mm fan (bundle) | €9.00 | Bundle only |

### Firmware/software starting point
- ESPHome (exists; supports SCD4x, PWM outputs, climate/hysteresis components) is a legitimate v1 firmware and gives Home Assistant users a free integration. Move to ESP-IDF when you need custom pod heater logic.
- Mycodo (exists; open-source environmental regulation for Raspberry Pi) is worth reading for grower control logic.
- Web page: a static page served from the ESP32 — no app.

### 12-week build plan
- **Week 1–2 — validate.** Grove SCD41 + C3 devkit + Unit Fan + a fogger on a 60 L tub of oyster mushrooms; post the €139 pre-order in three groups. *Exit:* 60 deposits in two weeks; the breadboard holds 88–92% RH and <1,000 ppm for a week.
- **Week 3–5 — works-like.** Own PCB, 3 outputs, OLED menu, pod v1 with membrane. *Exit:* 5 units running on 5 community testers' chambers.
- **Week 6–8 — looks-like + EVT.** Box and pod housings printed in the final geometry, presets tuned from tester data. *Exit:* 2 weeks without a sensor fault at 95% RH.
- **Week 9–10 — DVT + pre-compliance.** Pod tool, EMC pre-scan, PSU and cable qualification. *Exit:* pre-scan pass; pod drift <5% RH over 30 days.
- **Week 11–12 — pilot batch.** 50 units to depositors, logs collected. *Exit:* <5% support tickets, yield feedback positive.

### Certification checklist (EU)
- **RED** if WiFi enabled: EN 300 328, EN 301 489-1/-17, EN 62368-1 (SELV only). **EMC-only route** (EN 55032/55035) if you ship the no-WiFi SKU first. Est. **€8–15k**.
- **EN 18031** (RED delegated act) if the WiFi version talks to the internet; **CRA** — reporting obligations from Sept 2026, full in Dec 2027: SBOM, update path, vulnerability handling.
- **RoHS, WEEE, REACH**; the PSU must carry its own CE and be from a reputable supplier.
- No battery, no camera, no personal data (unless you add accounts — don't).
- Not a toy, not a medical device. Don't claim food-safety outcomes.

### Validation toolkit
- **Kill question:** 60 paid deposits at €139 within two weeks from three grower communities? **Cheapest experiment:** €250 — breadboard, a photo of it holding 90% RH, a pre-order page.
- **5-question interview:** (1) What's your chamber and how do you control humidity today? (2) What went wrong in your last flush — dry pins, long stems, contamination? (3) Do you know your CO2 level? Would you pay to? (4) €139 for the controller or €199 with fogger and fan — which? (5) Where did you buy your last grow gear?
- **Landing-page headline:** "The first fruiting-chamber controller built for 95% humidity." Bullets: Real NDIR CO2 + a sensor pod that doesn't drown · 24 V only — nothing mains in your wet tent · EU plug, EU support, works offline.
- **Pre-order pass:** 60 deposits of €30 (or 30 full pre-payments) in 14 days.

### First production checklist
Sensor samples from the distributor (not grey market — fakes exist), golden sample with logged 7-day RH/CO2 trace, DFM on the pod (membrane welding, strain relief), MOQ 500 with a 2,000 forecast, QC/AQL Level II + 100% functional test in ambient CO2, drop/humidity packaging test, FOB Shenzhen, EU importer on the label, PSU batch certificates filed.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Seeed Studio and M5Stack and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41](/db/seeed-grove-co2-temperature-humidity-sensor-scd41.html) (true NDIR CO2 + T/RH); [Seeed Grove-Water Atomization](/db/seeed-grove-water-atomization.html) (ultrasonic fogger driver reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Fan (U063)](/db/m5stack-unit-fan.html) (12 V fan drive). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c3-devkitm-1](/db/espressif-esp32-c3-devkitm-1.html) (controller MCU). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack and Espressif websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1 — for a Fruiting-Chamber Controller

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Fruiting-Chamber Controller: One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app. The design is built around your Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1.

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1.
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
主题：样品订购及批量报价 — Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1 — 用于Fruiting-Chamber Controller

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fruiting-Chamber Controller：One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app。产品设计基于贵司的Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1。
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
Subject: PCBA quote from open design files — Fruiting-Chamber Controller, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Fruiting-Chamber Controller: One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app. The design starts from published open-hardware files (Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Fruiting-Chamber Controller，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fruiting-Chamber Controller：One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app。设计基于已公开的开源硬件文件（Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Water Atomization, M5Stack Unit Fan (U063), Espressif esp32-c3-devkitm-1；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order the Grove SCD41, C3 devkit, Unit Fan, a 24 V fogger disc and a 60 L tub; start an oyster block.
2. Draft the pre-order post and page (€139, ships in 16 weeks) and get admin permission in three grower groups.
3. Email the SCD41 distributor for 2,000-piece lead time and price; ask a lab for a RED-vs-EMC quote.

Want help sourcing or building this? Talk to us via www.gongbans.com.
