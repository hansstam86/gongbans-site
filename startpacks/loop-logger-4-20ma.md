# 4–20 mA Loop Logger (LoRaWAN) — Founder Start Pack

> A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN — turning thirty-year-old instrumentation into IoT without touching the control loop.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of 4–20 mA transmitters hang on tanks, pipes and pumps across Europe, wired to a local gauge or a PLC that nobody can reach remotely. Replacing them with "smart" sensors costs thousands per point; the operator just wants the value on a dashboard and an alarm on the phone.
- **Customer:** Small water utilities and water boards, greenhouses, breweries, food plants, biogas and small process plants, and above all the **system integrators** who serve them. Integrators buy; plant operators use.
- **Product:** A two-channel 4–20 mA (and 0–10 V) to LoRaWAN node in a DIN-rail housing (24 V powered, can power the loop) and an IP65 field version (5-year battery or loop-powered pass-through), on-node threshold alarms, a standard payload codec, and a no-nonsense configuration tool. €149–199 (estimate).
- **Why now:** LoRaWAN coverage (public and private) is mature; competitors exist (Milesight UC300 at ~€125 net EU868 with 2× 4–20 mA plus lots more; Dragino PS-LB ~€56–94; Sentinum AION420; Enless; Radio Bridge) — so this is a crowded but fragmented market where a sharper, cheaper, integrator-friendly node with a loop-powered trick still wins deals.
- **The ask:** ~€60k to a certified first 1,000 nodes; integrator pilot orders carry most of it.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 5 system integrators each order a 10-unit pilot at €169 within 6 weeks?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Water utilities, greenhouses, breweries, small process plants and system integrators across Europe.

**The problem as the pack states it:** Millions of 4–20 mA transmitters hang on tanks, pipes and pumps across Europe, wired to a local gauge or a PLC that nobody can reach remotely. Replacing them with "smart" sensors costs thousands per point; the operator just wants the value on a dashboard and an alarm on the phone.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **PLCtalk forum** · https://www.plctalk.net/ — industrial automation technicians and integrators.
- **Control.com forum** · https://control.com/ — process-control and instrumentation engineers.
- **r/PLC** · https://www.reddit.com/r/PLC/ — industrial automation engineers and integrators.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

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
Thanks for the time. I am looking into how water utilities, greenhouses, breweries, small process plants and system integrators across Europe deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about a 4–20 mA sensor on site that nobody logs today: why is it not connected, and what would you do with the data?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN, turning thirty-year-old instrumentation into IoT without touching the control loop. On a scale of one to ten, how likely would you be to buy that at €149–199, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: 4–20 mA Loop Logger (LoRaWAN): looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a 4–20 mA Loop Logger (LoRaWAN): A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN, turning thirty-year-old instrumentation into IoT without touching the control loop. Before we spend money on tooling I want to find out whether this solves a real problem for water utilities, greenhouses, breweries, small process plants and system integrators across Europe.

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

Retrofit beats replacement when budgets are tight. The transmitter already works; it just talks 4–20 mA to a thing on the wall. The retrofit node sits in series (loop pass-through, so the existing PLC keeps reading) or reads a spare transmitter. The integrator wants: a node that installs in 10 minutes, a decoder that drops into their network server, and a datasheet that answers the water board's questions (isolation, IP rating, battery life, alarm behaviour).

- **Who pays:** system integrators (10–100 nodes per project) and directly small utilities/greenhouses with an in-house technician.
- **Who uses:** plant operators (dashboard/alarm), maintenance (battery/replace).
- **What they compare:** Milesight UC300 (feature-rich, DC-powered, €125 net), Dragino PS-LB (cheap, battery), Sentinum AION420 (loop-through, DE-made, premium), Enless TX 4/20 mA (5-year battery).

### Market size (estimates — check)

- **TAM:** installed 4–20 mA transmitters in the EU — no public figure found; analyst-style guesses run into tens of millions of loops. Take **20M** as a working number; 10% worth connecting → 2M points → at €169 **€340M** hardware, plus services.
- **SAM (small/mid operators and integrators in DACH/Benelux/Nordics/FR/IT where LoRaWAN is strong; water, agri, food, biogas):** ~300–500k points → **€50–85M**.
- **SOM (3 yrs):** 1% → **3–5k nodes**. Year 1: 800–1,500 via 5–10 integrators.

### Competition (2 searches)

| Alternative | Price (listings, approx.) | Why we still win |
|---|---|---|
| Milesight UC300 (EU868) | ~€125 net; 2× 4–20 mA, 2× 0–10 V, PT100, RS-485, relays | Over-featured and DC-only; our field SKU is battery/loop-powered and IP65; our DIN SKU is simpler and cheaper to configure |
| Dragino PS-LB / CS01-LB | ~€56–94 / ~€150 | Hobby-grade enclosures and docs; integrators want a datasheet, isolation and support in EU time zones |
| Sentinum AION420 (loop-through, mioty/LoRaWAN) | premium (quote) | We undercut with the same loop-through trick |
| Enless TX 4/20 mA, Radio Bridge 4–20 mA, Netvox | €100–200 | Fragmented; none owns the integrator relationship with an open codec + config tool |
| Replace the transmitter with a native LoRaWAN sensor | €300–1,500 per point | Retrofit is 5× cheaper and keeps the loop |
| Do nothing (manual rounds, local gauge) | Free | Alarm on phone pays for itself at the first overflow |

**Wedge:** loop-powered pass-through + 2 channels + on-node alarms + integrator tooling (codec, batch config, white-label label) at €149–199, from an EU company with a real datasheet.

### Product & value proposition

- **DIN SKU:** 2× 4–20 mA (16-bit, isolated), 2× 0–10 V, 24 V in, can source 24 V loop power for 2 transmitters, 1 digital input (pulse/flow), LoRaWAN EU868 (SMA antenna), USB-C config.
- **Field SKU:** IP65 polycarbonate box, 1–2 channels, loop pass-through (steals <2 V from the loop, with battery backup) or 5-year battery with transmitter power pulsing (warm-up timing configurable), cable glands.
- On-node: sampling interval, thresholds with hysteresis, rate-of-change alarms, immediate uplink on alarm, daily heartbeat with battery and loop status.
- Tooling: NFC/USB config app, CSV batch provisioning, published codec for TTN/ChirpStack/Actility/Loriot, Modbus-to-LoRaWAN later.
- **Pricing (estimates):** DIN €149, field battery €179, field loop-powered €199; integrator tiers −20/−30%; 10-pack pilot €1,490.

### Unit economics (estimates, EUR per unit; DIN SKU)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C6+LoRa core or pre-cert LoRaWAN module €7, 16-bit ADC + precision shunts + isolation €5, 24 V in + loop-power boost €3, protection/TVS €1, terminals €2.5, SMA + antenna €2, PCB €1.5) | 22.0 | 18.5 |
| PCBA + calibration test | 4.0 | 2.6 |
| Enclosure (DIN 3–4 TE housing; field: IP65 box + glands) | 4.0 (DIN) | 3.0 |
| Packaging + label + quick guide | 1.5 | 1.1 |
| Freight + duty to EU | 1.5 | 0.8 |
| Certification amortised (€18k incl. industrial EMC) | 18.0 | 3.6 |
| **Landed cost** | **51.0** | **29.6** |
| Net price integrator (−25%: €112 ex VAT) | 112 | 112 |
| **Gross margin integrator** | **€61 (54%)** | **€82 (74%)** |
| Direct (€149 ex VAT) | €98 (66%) | €119 (80%) |

The precision front end (ADC, shunts, isolation) is where you must not save; the LoRa module is the lead-time risk.

### Go-to-market

**First 100 customers (first 1,000 nodes):** five integrators — one water (a small water board's contractor), one greenhouse automation firm, one brewery/food automation shop, one biogas service company, one LoRaWAN network operator's partner. 10-unit pilot packs at €1,490. Find them in The Things Industries partner list, LoRa Alliance member list, regional automation associations, Hannover Messe/SPS/Aquatech visitor lists (search).

**Then scale:** distributors of IoT hardware in the EU (the usual LoRaWAN webshops that already list Milesight/Dragino — get listed), network operators' marketplaces, instrumentation distributors (they sell the transmitters — add the node), OEM/white-label for pump and tank makers.

### 12-month plan

- **Q1:** works-like on Stamp C6LoRa + Unit AIN4-20mA in a DIN base; codec; 5 integrator pilots (hand-built).
- **Q2:** own PCB (precision front end, isolation, loop power), DIN housing; 50-unit EVT; field IP65 prototype.
- **Q3:** certification (RED + industrial EMC), 1,000 DIN production; config tool v1.
- **Q4:** field SKU production; distributor listings; white-label talk with one tank/pump OEM.

**Team:** embedded engineer with analogue skills (full), firmware/LoRaWAN (half), founder with integrator network, technical writer (contract — the datasheet sells). Shenzhen partner for PCBA with calibration fixture and housings.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €33k + calibration fixture/tooling €8k + certification €18k + pilots €5k + 6 months team €45k + fairs/marketing €8k = **≈€117k**; five pilot packs (€7.5k) and integrator pre-orders (500 × €112 = €56k) bring the external need to **≈€50–60k**. Route: integrator pre-orders + bootstrap; regional industrial-IoT/water-innovation grants; angel optional.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** crowded; Milesight/Dragino are cheap and everywhere | Win on loop-powered pass-through, datasheet quality, EU support, integrator tooling; do not try to beat Dragino on price alone |
| **Technical:** loop-powered pass-through must not disturb the control loop (voltage burden, startup transient) | Design for <2 V burden, soft-start, pass-through even when the node is dead (fail-safe short); test on real PLC inputs |
| **Technical:** accuracy and drift (claim 0.1% FS) | 16-bit ADC, precision shunt, factory calibration with stored coefficients |
| **Regulatory:** industrial EMC (EN 61326 class) and surge on long cables | Isolation, TVS, pre-scan early; budget a re-test |
| **Supply:** LoRa module allocation | Two approved module paths |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit AIN4-20mA (U162) | https://www.gongbans.com/db/m5stack-unit-ain4-20ma.html | 4–20 mA input reference for the pilot | enclosure/structure only | Module for prototypes; own precision front end for production |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | ESP32-C6 + LoRa core with open Altium PCB and schematic — the node core | pcb, schematic | M5_Hardware repo — check licence |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | EU868 LoRaWAN stack module for pilots | enclosure/structure only | Module; production via C6LoRa path or a pre-certified module |
| M5Stack Base DIN (M132) | https://www.gongbans.com/db/m5stack-base-din.html | DIN-rail mounting reference | enclosure/structure only | Mechanical reference |

Catalogue honesty: the AIN4-20mA Unit's ADC resolution and isolation are not in the catalogue — check M5 docs; it is a pilot part, not your front end.

### Block diagram

```
24 V DC in (DIN) | loop pass-through / battery (field) ──► power stage (+ loop-power boost 24 V)
     2× 4–20 mA ──► precision shunt ──► isolated 16-bit ADC ──► ESP32-C6
     2× 0–10 V, 1× digital/pulse input ──► ESP32-C6
     ESP32-C6 ──► LoRa EU868 (SMA) ──► LoRaWAN NS (TTN/ChirpStack/Actility/Loriot) ──► integrator dashboard
     USB-C / NFC config ; on-node thresholds, hysteresis, heartbeat
```

**Engineering gap:** the analogue front end (accuracy, isolation, surge), loop-powered pass-through that fails safe, battery/transmitter warm-up timing, and the integrator tooling (codec, batch config).

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-C6 module + SX1262-class LoRa or pre-certified LoRaWAN module | €7 | **Lead-time item**; two paths |
| 16-bit ADC (ADS1115/ADS1120-class) + 0.1% shunts | €3 | |
| Isolation (digital isolator or isolated DC/DC) | €2.5 | For the DIN SKU; field SKU single-channel may skip |
| 24 V input + loop-power boost (24 V, 50 mA) | €3 | |
| TVS/surge protection, PTC | €1 | Long cables = surges |
| Pluggable screw terminals | €2.5 | |
| SMA connector + 868 MHz antenna | €2 | |
| DIN 3–4 TE housing / IP65 PC box + glands | €4 / €9 | Standard parts |
| Field battery: Li-SOCl2 D cell | €6 | Transport rules apply |

### Firmware/software starting point

- **ESP-IDF** on ESP32-C6; LoRaWAN via **RadioLib** or Semtech **LoRaMac-node**; pilot with the M5 LoRaWAN Unit.
- Network: **The Things Stack**, **ChirpStack**; codecs in JavaScript per the LoRa Alliance payload codec API; **Cayenne LPP** optional.
- Config tool: a desktop/web app over USB serial (Web Serial) — simple; NFC later.
- Dashboard for pilots: Node-RED + InfluxDB + Grafana.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 integrator calls; 3 pilot LOIs; 3 pilot nodes (Stamp C6LoRa + Unit AIN4-20mA + LoRaWAN Unit in a DIN base) on a pressure transmitter | ≥5 integrators commit to a 10-unit pilot at €1,490 within 6 weeks |
| 3–5 | **Works-like** — 15 pilot nodes at 3 sites, codec, alarms | Readings within 1% of the PLC value; alarms arrive <2 min; uptime >99% |
| 6–8 | **Looks-like + EVT** — rev A PCB (precision front end, isolation, loop power), DIN housing, 30 units; calibration fixture | Accuracy ≤0.2% FS after calibration; loop burden <2 V; fail-safe pass-through verified |
| 9–10 | **DVT + pre-compliance** — rev B, EN 300 220 + industrial EMC pre-scan (surge, ESD, RF immunity), EN 18031 checklist, datasheet v1 | No fails or a fix plan; datasheet reviewed by 2 integrators |
| 11–12 | **Pilot batch** — 50 units to 5 integrators, config tool beta | ≤2 failures; 3 of 5 integrators place a 50+ order; field SKU EVT started |

### Certification checklist (EU)

- **CE — RED:** EN 300 220-2, EN 301 489-1/-3, safety via **EN 62368-1** or **EN 61010-1** depending on classification (industrial measuring equipment — ask the lab): €9–13k.
- **Industrial EMC:** EN 61326-1 (immunity/emissions for measurement equipment) is what integrators and water boards ask for: +€4–6k.
- **EN 18031-1** (internet-connected via LoRaWAN): self-assess: €2–3k.
- **CRA:** SBOM, local update over USB, disclosure contact; 10-year support plan.
- **RoHS, WEEE (B2B), REACH, packaging.**
- **Battery Regulation** for the field SKU (Li-SOCl2 primary): registration, labelling, removability; transport paperwork.
- **GDPR:** none.
- **ATEX:** not covered — say explicitly "not for hazardous areas".
- **Total estimate:** €16–22k (both SKUs €22–28k).

### Validation toolkit

- **Kill question:** Do 5 system integrators each order a 10-unit pilot at €169 within 6 weeks? Cheapest experiment: a datasheet PDF, a codec on GitHub, and three hand-built nodes you can demo on a call.
- **Interview script (5):** 1) Which 4–20 mA points do your customers want remote, and why haven't they done it? 2) Which LoRaWAN nodes do you use today and what annoys you about them? 3) Loop-powered pass-through vs battery vs 24 V — which do you actually need? 4) What must the datasheet say for a water board to approve it (isolation, IP, accuracy, battery)? 5) €112 net for the DIN node, €149 field — margin OK, and would you white-label?
- **Landing page:** Headline: "Your old 4–20 mA sensors, on LoRaWAN, in ten minutes." Bullets: "Two channels, loop-powered or 24 V, keeps your PLC reading." / "On-node alarms, 5-year battery, IP65 field box." / "Open codec for TTN, ChirpStack, Actility, Loriot."
- **Pre-order pass:** ≥5 integrators × 10-unit pilot packs within 6 weeks.

### First production checklist

- Samples: 5 PCBAs with calibration fixture from the assembler; **golden sample** with calibration certificate.
- DFM: terminal torque, isolation gaps, antenna connector strain, gland sealing on the field SKU.
- MOQ: PCBA 500; DIN housings 500; IP65 boxes 300; LoRa modules reel.
- QC/AQL: Z1.4 II, AQL 0.65 major / 2.5 minor; 100% calibration at 4, 12, 20 mA, LoRa join, loop-power check.
- Packaging: quick guide with wiring diagrams; EU DoC + WEEE; batteries shipped separately for the field SKU.
- Incoterms: FOB Shenzhen sea; pilots by air DAP.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit AIN4-20mA (U162)](/db/m5stack-unit-ain4-20ma.html) (4–20 mA analogue input reference); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN module); [M5Stack Base DIN (M132)](/db/m5stack-base-din.html) (DIN-rail mounting reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*
- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132) — for a 4–20 mA Loop Logger (LoRaWAN)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a 4–20 mA Loop Logger (LoRaWAN): A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN, turning thirty-year-old instrumentation into IoT without touching the control loop. The design is built around your M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132).
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
主题：样品订购及批量报价 — M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132) — 用于4–20 mA Loop Logger (LoRaWAN)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款4–20 mA Loop Logger (LoRaWAN)：A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN, turning thirty-year-old instrumentation into IoT without touching the control loop。产品设计基于贵司的M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132)。
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
Subject: PCBA quote from open design files — 4–20 mA Loop Logger (LoRaWAN), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a 4–20 mA Loop Logger (LoRaWAN): A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN, turning thirty-year-old instrumentation into IoT without touching the control loop. The design starts from published open-hardware files (M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — 4–20 mA Loop Logger (LoRaWAN)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款4–20 mA Loop Logger (LoRaWAN)：A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN, turning thirty-year-old instrumentation into IoT without touching the control loop。设计基于已公开的开源硬件文件（M5Stack Unit AIN4-20mA (U162), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Base DIN (M132)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Write the two-page datasheet (specs you intend to hit, honestly marked "target") and the JavaScript codec; put both on a landing page.
2. Order Stamp C6LoRa ×3, Unit AIN4-20mA ×3, Unit LoRaWAN-EU868 ×3, Base DIN ×3; wire one to a pressure transmitter and uplink to The Things Stack.
3. Call 10 integrators from the LoRaWAN partner lists with the pilot-pack offer; aim for 3 LOIs.

Want help sourcing or building this? Talk to us via www.gongbans.com.
