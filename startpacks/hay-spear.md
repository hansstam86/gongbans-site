# Hay Spear — Founder Start Pack

> A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Hay and straw stored too wet heat up by microbial action; above ~50–60 °C the stack can ignite. Farmers probe by hand for a week after harvest, then stop. Barns, machinery and animals burn every summer; insurers in the alpine countries already expect temperature monitoring of self-igniting stores.
- **Customer:** Livestock and arable farms with hay/straw storage in DE/AT/CH/NL/FR; agricultural insurers and farm-supply dealers as channels. The farmer pays €169 per spear (or the insurer co-funds); the farmer and the family use the alarm.
- **Product:** stainless 1 m spear with 3 sensing depths, IP67 head, EU868 LoRaWAN, 5-year primary cell, threshold and rate-of-rise alarms by app/SMS; farmyard gateway bundle for farms without coverage.
- **Why now:** Open ESP32-C6 + LoRa core exists with PCB and schematic; LoRaWAN modules are cheap; the one established wireless system is a 10-probe starter kit with a reader and a subscription at a four-figure price.
- **The ask:** ~€70k to the first 1,000 spears; pre-orders at fairs plus one insurer partnership.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Self-heating hay and straw fires are real and well documented, with defined danger thresholds (about 65–95 °C / 150–200 °F). Quanturi's HAYTECH already sells a bale-insertion probe and repeater system, so this is a direct incumbent, not greenfield. **Main risk:** Incumbent pricing and MOQ, and the insurer channel's interest, are unverified. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 20 farmers at one agricultural fair pre-order at €169, and does one insurer agree to promote it?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Livestock and arable farms with hay or straw storage in DE/AT/CH/NL/FR; agricultural insurers as channel.

**The problem as the pack states it:** Hay and straw stored too wet heat up by microbial action; above ~50–60 °C the stack can ignite. Farmers probe by hand for a week after harvest, then stop. Barns, machinery and animals burn every summer; insurers in the alpine countries already expect temperature monitoring of self-igniting stores.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The Farming Forum (UK)** · https://thefarmingforum.co.uk/ — UK farmers; machinery, arable, livestock, farm diversification.
- **Landtreff (DE)** · https://www.landtreff.de/ — German farmers' forum.
- **r/farming** · https://www.reddit.com/r/farming/ — working farmers.
- **r/homestead** · https://www.reddit.com/r/homestead/ — smallholders.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199 per spear, the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how livestock and arable farms with hay or straw storage in DE/AT/CH/NL/FR deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Have you ever had a bale heat up on you? How do you check your stack today, and how often?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire. On a scale of one to ten, how likely would you be to buy that at €149–199 per spear, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Hay Spear: would you pay €149–199 per spear for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Hay Spear: A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–199 per spear, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Self-heating is slow, invisible and well understood: moisture >18–20% at baling, microbial growth, 40 °C in days, 60 °C in two weeks, and from ~70 °C a real fire risk. Prevention is boring: measure every day for 6–8 weeks after storing. Nobody does — so the stack gets probed when it smells. Insurers' loss-prevention departments know this (self-ignition is ~9–10% of farm fires by number in the sources found; no central statistic exists in Germany) and the Austrian rules quoted by the chambers of agriculture require temperature monitoring of self-igniting materials.

Who pays: the farmer (a €169 spear is cheap against a €200k barn), or the insurer as a loss-prevention subsidy (they already pay for lightning protection and fire extinguishers). Who uses: whoever has the phone — the alarm must work by SMS/app with no IT skills.

### Market size (estimates — check them)
- **TAM:** farms with hay/straw storage: DE ~130,000 livestock farms, AT ~90,000, CH ~45,000, NL ~30,000, FR ~200,000 → ~500,000 farms; average 3 spears + gateway for half of them → **~€300 M** one-off hardware potential.
- **SAM:** alpine/dairy regions with loose-hay stacks and bale barns, reached through 4–6 farm dealers and 2–3 insurers: ~80,000 farms × 3 spears × €169 ≈ **€40 M**, replacement every 5 years.
- **SOM (3 years):** 8,000 spears + 1,500 gateways ≈ **€1.8 M revenue**.

### Competition (3 searches)
| Alternative | Price (est.) | Weakness |
|---|---|---|
| Hand probe thermometer (1–2 m, analogue or digital) | €60–250 | Manual, stops after a week |
| Quanturi Haytech (40 cm probes, 433/868 radio, reader with 2G/Ethernet, premium service) | ~£600–1,200 for 10 probes + reader + 1 yr service | Starter-kit sizing, subscription, short probe; strong in big operations |
| Consumer Bluetooth logger in a PVC pipe (DIY) | €15 | Range of 10 m, no alarm away from the barn |
| Industrial stack-monitoring lances (IP67, 1.8 m) | several hundred € each | Wired, installer product |
| Do nothing — sniff and hope | €0 | Barn fires |

**Wedge:** a 1 m spear with three depths (the core heats first), LoRaWAN that reaches across the yard and into public networks, buy-once pricing (no subscription for alarms), and insurer co-funding.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Quanturi HAYTECH (via Nationwide) | Bale probe + repeater monitoring system | Direct incumbent |
| University of Kentucky / Oneida County hay-fire guides | Extension guidance with temperature thresholds | The problem is real and documented |

**Verdict as researched: LIKELY.** Main risk: Incumbent pricing and MOQ, and the insurer channel's interest, are unverified.
<!-- market-competitors:end -->

### Product & value proposition
- **Spear:** 1,000 mm × 20 mm stainless tube, pointed, three digital temperature sensors at 30/60/90 cm, PA66 head with IP67 seal and a loop for pulling out, LED + button.
- **Radio:** EU868 LoRaWAN class A; joins public networks (TTN or operator) or the farm's own gateway; 15-minute uplinks, immediate alarm uplink on rate-of-rise.
- **Power:** primary lithium (Li-SOCl2 C-cell), target 5 years.
- **Service:** free app and SMS alarms (bundled SMS budget); optional €2/month per farm for history and reports after year 1 — optional, not required for alarms.
- **Pricing:** **€169 incl. VAT per spear** (€142 ex-VAT); 3-spear pack + gateway **€599**; insurer/dealer price €119 ex-VAT at 50+.

### Unit economics (estimates, per spear)
| Item | 1,000 units | 5,000 units |
|---|---|---|
| Electronics BOM (ESP32-C6 + LoRa module €8, 3 sensors €3, PCB, antenna, cell €4) | €24 | €19 |
| Assembly & test (incl. LoRa join test, sensor check in a water bath) | €6 | €4 |
| Spear tube + tip + head enclosure + seal | €16 | €11 |
| Packaging, manual, QR card | €2.50 | €1.60 |
| Freight + duty to EU (1 m long — ship by sea; air is painful) | €4 | €2.20 |
| Certification amortised (€25k) | €25 | €5 |
| **Landed cost** | **€77.50** | **€42.80** |
| Sell price direct ex-VAT | €142 | €142 |
| Via dealer/insurer (net €119) | €119 | €119 |
| **Gross margin direct** | **45%** | **70%** |
| **Gross margin via dealer** | 35% | 64% |

Gateway bundle: an off-the-shelf indoor LoRaWAN gateway lands at ~€90–120; sell in the €599 pack. SMS/app running cost ~€1/spear/year.

### Go-to-market
**First 100 customers:** one agricultural fair per country (the big autumn machinery fairs) with a demo stack and a pre-order form at €169; chambers of agriculture loss-prevention advisers; one insurer's prevention department (they publish hay-fire warnings every June — give them a product to point at); farm Facebook groups and the dairy-farmer forums; contractors who bale for many farms.

**Scale:** farm-supply dealer chains (the shops where the farmer buys fence wire), insurer co-funding programmes, chambers' subsidised prevention lists, LoRaWAN network operators in rural areas (they need devices), FR/PL distributors.

### 12-month plan
- **Q1:** 10 prototype spears from the Stamp C6LoRa + sensors in a tube, in two real hay stacks; pre-order list at one fair or chamber event. Gate: 20 farmers pre-order at €169 and one insurer agrees to promote.
- **Q2:** Own PCB in the head, IP67 head tool, RED tests, app + SMS alarms, 300 spears for the June–August hay season.
- **Q3:** Field data from season 1, dealer listings, gateway bundle, 1,000 spears for straw season.
- **Q4:** Insurer programme, FR/PL distributor talks, silage/grain variant (same spear, different firmware).

**Team:** one embedded engineer (LoRaWAN + low power; full-time 6 months), one mechanical/sourcing person for the spear (part-time), one farm-side salesperson (part-time, ex-advisory), a backend/app contractor.

**Funding to 1,000 spears (estimate):** NRE €30k (PCB, head tool €10k, app/backend, test rig) + certification €25k + 1,000 × €52 production = €52k → **~€107k**; fair pre-orders and an insurer pilot order cover ~€35k → cash need **~€70k**. Route: pre-orders + an agri-innovation grant (rural development programmes fund fire prevention) + possibly an insurer-backed pilot. Angel money only for the multi-country push.

### Top risks
- **Technical — radio inside a hay stack:** hay is wet and absorbs 868 MHz; the antenna must be in the head, outside the stack, and the head must stay up. Mitigation: head design with the antenna on top; a repeater/gateway bundle; test in a real stack early.
- **Technical — 5-year battery:** achievable with class A, 15-minute uplinks and deep sleep on the C6, but only if you measure it. Mitigation: current profiling in week 3, derate to 3 years in marketing until proven.
- **Market — seasonality:** you sell in May–August. Mitigation: straw and silage extend the season; stock for season 1 must be ready by May.
- **Regulatory:** RED (EN 300 220), EN 301 489, EN 62368-1, IP67, **EN 18031** (it connects to the internet via LoRaWAN — assume yes), CRA, lithium-metal cell transport (UN 38.3, labels) and Battery Regulation. Mitigation: pre-certified LoRa module with a RED file; cells from a supplier with transport docs.
- **Supply:** the stainless tube and tip are simple; the IP67 head is tooled. Mitigation: first 300 with a machined/printed head.

## 4. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [m5stack-stamp-c6lora](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) | Open ESP32-C6 + LoRa core: the head electronics reference (Altium sources) | pcb, schematic | M5Stack hardware repo — check licence |
| [m5stack-unit-lorawan-eu868](https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html) | EU868 LoRaWAN module for the first prototypes | enclosure/structure only | Module |
| [m5stack-unit-kmeter-iso](https://www.gongbans.com/db/m5stack-unit-kmeter-iso.html) | Isolated thermocouple input for a high-temperature "fire-service" probe variant | enclosure/structure only | Module |
| [seeed-grove-temperature-and-humidity-sensor-pro](https://www.gongbans.com/db/seeed-grove-temperature-and-humidity-sensor-pro.html) | Ambient T/RH reference at the stack surface (for drying-rate logic) | schematic | Seeed wiki — check |

### Block diagram and engineering gap
```
[Spear tube 1 m] : sensor @30cm — sensor @60cm — sensor @90cm  (1-wire or I2C digital temp)
        |
[IP67 head] : ESP32-C6 (C6LoRa-derived) + LoRa EU868 + antenna on top + Li-SOCl2 cell + LED/button
        |--LoRaWAN--> public network or farm gateway --> backend --> app + SMS
Optional: surface T/RH node for ambient
```
Gap: mechanical spear and head (sealing, pull-out force, sensor wiring down a tube), antenna placement, deep-sleep power budget, LoRaWAN provisioning (keys, QR join), alarm logic (absolute + rate-of-rise), and a backend that sends SMS reliably.

### Starter BOM (per spear, estimates)
| Part | Est. cost | Note |
|---|---|---|
| ESP32-C6 module (certified) | €2.50 | — |
| LoRa transceiver module, EU868, pre-certified | €5.50 | Pick one with a RED test report |
| 3× digital temperature sensors on a flex/wire harness | €3.00 | Commodity |
| Li-SOCl2 C-cell (8.5 Ah) + holder | €4.50 | UN 38.3 docs required; lithium-metal shipping rules |
| PCB + assembly | €4.00 | — |
| Antenna (868 MHz, in head) | €1.00 | — |
| Stainless tube 20 × 1,000 mm + welded tip | €9.00 | EU or CN; long item — sea freight |
| IP67 PA66 head + seal + pull loop | €6.00 | Tooled; machined for pilot |
| Packaging (long box) | €2.50 | — |

### Firmware/software starting point
- **RadioLib** (exists; LoRaWAN support on ESP32) or Semtech's **LoRaMac-node** (exists) for the device; ESP-IDF deep sleep.
- Network: **The Things Stack / TTN** (public) and **ChirpStack** (self-hosted, exists) for the farm gateway bundle.
- Backend: anything that takes MQTT from the network server and sends SMS via a gateway API; keep it boring.

### 12-week build plan
- **Week 1–2 — validate.** Stamp C6LoRa + Unit LoRaWAN-EU868 + 3 sensors in a 1 m electrical conduit, pushed into a real stack; log to TTN. Pre-order form at a chamber event or fair. *Exit:* uplinks from inside a stack at 200 m; 20 pre-orders at €169; one insurer prevention person says "send me the flyer".
- **Week 3–5 — works-like.** Own head PCB, power profile measured (target <40 µA sleep), rate-of-rise alarm, SMS path. *Exit:* 5 spears in 5 stacks reporting for 3 weeks; projected battery ≥3 years.
- **Week 6–8 — looks-like + EVT.** Stainless spear, machined head, IP67 test in a bucket, app v1. *Exit:* 10 farmers use the app without a call; no water ingress.
- **Week 9–10 — DVT + pre-compliance.** Head tool, RED pre-scan (EN 300 220 limits, spurious), EN 18031 gap review. *Exit:* pre-scan pass, security checklist done.
- **Week 11–12 — pilot batch.** 50 spears + 10 gateways to pre-order farms before the hay season. *Exit:* 50 paid, <5% faults, alarms proven on at least one warm stack.

### Certification checklist (EU)
- **RED:** EN 300 220-2 (SRD 868 MHz), EN 301 489-1/-3, EN 62368-1; **EN 18031-1** (and -2/-3 if you store personal data or take payments — you store phone numbers, so plan -2) because the device connects to the internet via LoRaWAN; est. **€15–25k** total, less with a pre-certified module.
- **CRA:** reporting from Sept 2026, full obligations Dec 2027 — SBOM, secure update (LoRaWAN FUOTA or "return for update" — decide), vulnerability disclosure page.
- **RoHS, WEEE, REACH**; **IP67** test (IEC 60529) at the lab, €1–2k.
- **Battery Regulation:** applies to all batteries; primary lithium-metal: UN 38.3, transport labels, removability information. Not Li-ion, so no charging-safety work.
- **GDPR:** phone numbers for SMS alarms — privacy notice, EU hosting, deletion on request.
- No toy, no medical.

### Validation toolkit
- **Kill question:** do 20 farmers at one fair pre-order at €169, and does one insurer agree to promote it? **Cheapest experiment:** €500 — two conduit prototypes, a demo bale with a heater inside, a pre-order form, a stand at a chamber event.
- **5-question interview:** (1) How do you check your hay now and for how long after storing? (2) Have you or a neighbour had a hot stack? What happened? (3) Who in the family would get the alarm, and by SMS or app? (4) €169 per spear, €599 for three with a gateway — which, and would an insurer discount change it? (5) Where do you buy farm gear — dealer, online, co-op?
- **Landing-page headline:** "Your hay tells you before it burns." Bullets: 1 m spear, 3 depths, alarm to your phone · 5-year battery, no subscription for alarms · Works across the yard with LoRaWAN — gateway included if you need it.
- **Pre-order pass:** 20 paid pre-orders (€50 deposit) at one event, or 60 online in 6 weeks, plus one insurer letter.

### First production checklist
Tube/tip samples (pull and bend test), head samples sealed and dunked, golden sample with join keys printed on a QR label, DFM on the harness routing in the tube, MOQ 300 with a 2,000 forecast and a May delivery date written in the contract, QC/AQL Level II + 100% join test and sensor bath test, long-box drop test, sea freight FOB, lithium-metal transport paperwork, EU importer label, battery labelling per Battery Regulation.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit KMeter-ISO (U133-V11)](/db/m5stack-unit-kmeter-iso.html) (isolated thermocouple input for the long probe); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN uplink). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Temperature and Humidity Sensor Pro](/db/seeed-grove-temperature-and-humidity-sensor-pro.html) (ambient T/RH reference at the stack surface). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro — for a Hay Spear

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Hay Spear: A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire. The design is built around your M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro.
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
主题：样品订购及批量报价 — M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro — 用于Hay Spear

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hay Spear：A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire。产品设计基于贵司的M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro。
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
Subject: PCBA quote from open design files — Hay Spear, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Hay Spear: A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire. The design starts from published open-hardware files (M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Hay Spear，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hay Spear：A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire。设计基于已公开的开源硬件文件（M5Stack Unit KMeter-ISO (U133-V11), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Temperature and Humidity Sensor Pro；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order Stamp C6LoRa, Unit LoRaWAN-EU868, six digital temperature sensors and a 1 m conduit; register on TTN; find a farmer with a stack to push it into.
2. Call the chamber of agriculture's fire-prevention adviser and one insurer's loss-prevention department; ask for their hay-fire numbers and whether they'd co-fund.
3. Ask a LoRa module vendor for a module with an EN 300 220 report, and a lab for a RED + EN 18031 quote.

Want help sourcing or building this? Talk to us via www.gongbans.com.
