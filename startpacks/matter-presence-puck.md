# Matter Presence Puck — Founder Start Pack

> A coin-sized ceiling puck that knows someone is still in the room — reading, on the sofa — unlike PIR, and reports occupancy over Matter-over-Thread to any EU smart-home hub. Fully local, no app account.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The #1 complaint about motion-sensor lighting: the light switches off while you sit still. PIR sees motion, not people. Presence radars fix it, but most are Zigbee/Wi-Fi with a vendor app, or DIY ESPHome boards on a breadboard.
- **Customer:** Home Assistant, Apple Home and Google Home households in NL, DE, BE and the Nordics (they pay and install); electricians fitting lighting automation in new builds (B2B2C).
- **Product:** A 30 mm PCB in a small ceiling/wall puck: low-power 24 GHz presence radar + Matter-over-Thread module. Maps radar "moving/still/none" to the Matter OccupancySensing cluster with tunable hold time; sensitivity set from the hub. USB-C or 2×AA. No cloud, no account.
- **Why now:** Thread border routers ship inside common speakers, TVs and hubs; Matter occupancy sensors work in all big ecosystems; low-power 24 GHz radar (~100 µA average per catalogue) makes a battery puck possible.
- **The ask:** ~€140k to Matter certification and 2,000 units, with a 200-deposit gate before spending on certification.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 200 Home Assistant users put down a €10 deposit for a €49 Matter radar puck when DIY ESPHome radar sensors already cost €15? Pass = 200 deposits in 6 weeks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Home Assistant / Apple Home / Google Home households in NL, DE, BE, Nordics; electricians fitting lighting automation in new builds.

**The problem as the pack states it:** The #1 complaint about motion-sensor lighting: the light switches off while you sit still. PIR sees motion, not people. Presence radars fix it, but most are Zigbee/Wi-Fi with a vendor app, or DIY ESPHome boards on a breadboard.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **r/HomeKit** · https://www.reddit.com/r/HomeKit/ — Apple Home users; Matter and Thread devices are a main topic.
- **r/smarthome** · https://www.reddit.com/r/smarthome/ — less technical smart-home buyers.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€39–59 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how home Assistant / Apple Home / Google Home households in NL, DE, BE, Nordics deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last time your lights or automations switched off while someone was still in the room: what sensor was it, and what did you try to fix it?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A coin-sized ceiling puck that knows someone is still in the room (reading, on the sofa) — unlike PIR — and reports occupancy over Matter-over-Thread to any EU smart-home hub, fully local, no app account. On a scale of one to ten, how likely would you be to buy that at €39–59 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Matter Presence Puck: would you pay €39–59 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Matter Presence Puck: A coin-sized ceiling puck that knows someone is still in the room (reading, on the sofa) — unlike PIR — and reports occupancy over Matter-over-Thread to any EU smart-home hub, fully local, no app account. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €39–59 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

People who automate lights hit the PIR wall within a week. The fix today: a mains-powered mmWave sensor with its own app, or an ESPHome DIY board, or a premium Matter multi-sensor.

- **Who pays:** smart-home enthusiasts (early market, loud, review-driven), then mainstream Apple/Google Home users; electricians and smart-home installers in new builds and renovations.
- **Who uses:** the household — the product succeeds when they forget it exists.
- **Buying trigger:** "the bathroom/office/living-room light keeps turning off on me."

### Market size (estimates — check)

- **TAM:** EU households with a smart-home hub/ecosystem: tens of millions; assume 25M with at least one lighting automation, average 2 rooms that need presence → 50M sockets; at €49 = **~€2.4B** theoretical.
- **SAM:** Matter/Thread-capable households in NL, DE, BE, Nordics buying sensors online: ~3M households × 2 = **6M units**, ~€290M.
- **SOM (3 yrs):** **30–60k units** via own webshop, Amazon, smart-home specialist retailers and installer channels.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / PIR + long timeout | Cheap | Lights stay on for nothing or go off on you |
| Aqara Presence Multi-Sensor FP300 (~€50, PIR + 60 GHz radar, Matter over Thread, battery, launched Nov 2025) | **Strongest competitor** — same price, same protocol, big brand | Compete on: small size, ceiling mount, zone tuning from the hub, open documentation, EU support. Honestly: hard. Need a sharper niche (installers, ceiling flush mount, USB-powered always-on fast response) |
| Mains mmWave sensors (Aqara FP2, Tuya/Zigbee radar sensors, Meross MS605-type hybrid) | Good detection | Wi-Fi/Zigbee, apps, cloud accounts, mains install |
| DIY ESPHome + LD2410 (~€15) | Cheap, flexible | Breadboard look, Wi-Fi, no Matter certification, no enclosure for a ceiling |
| Ceiling presence detectors for KNX/DALI (professional) | Excellent | €100–250, professional bus systems |

**Wedge (must be validated):** the *installer-grade* Matter presence sensor: flush/ceiling-mount format that fits standard 60 mm boxes or a ceiling hole, USB/5 V-powered for instant response (no battery-saving latency), zone and hold-time configurable from the hub, plus a battery SKU for retrofit. Sell to electricians who fit Matter lighting in new builds — the brands chasing consumers ignore them.

### Product & value proposition

- **Hardware:** 30 mm PCB: LD2410S low-power radar, HM-MT2401 (EFR32MG24) module running the Matter app on Thread; ceiling flush-mount bezel (68 mm hole) and surface puck variants; USB-C or 5–24 V DC terminal (installer SKU), 2×AA (retrofit SKU).
- **Firmware:** OccupancySensing cluster; hold time and sensitivity via Matter attributes (check what each hub exposes — some hide vendor attributes; fallback: button sequence or a local web/BLE config page); optional illuminance later.
- **No cloud:** commissioning via Matter QR; no account.
- **Pricing (estimates):** €39–59 retail; installer 10-pack €349 (€35/unit); flush-mount kit €59.

### Unit economics (estimates, EUR per unit)

| Item | 1k | 5k |
|---|---|---|
| LD2410S radar | 3.5 | 2.7 |
| HM-MT2401 Thread module | 4.5 | 3.5 |
| Power (USB-C/5–24 V buck or battery path), LED, button, passives | 1.4 | 1.0 |
| PCB 30 mm 4-layer | 0.6 | 0.4 |
| Assembly + test (radar, Thread join, DAC provisioned) | 2.0 | 1.3 |
| Enclosure + bezel | 2.2 | 1.4 |
| Retail box + mounting kit + leaflet | 1.8 | 1.3 |
| Freight + duty | 0.8 | 0.5 |
| Certification amortised (CE €12k + Matter €15k = €27k) | 27.0 | 5.4 |
| **Landed cost** | **43.8** | **17.5** |
| Net D2C (€49 incl. VAT ≈ €41.2) less €4 fulfilment | 37.2 | 37.2 |
| Retail/Amazon margin if indirect (~35% of net) | −14.4 | −14.4 |
| **Gross margin D2C** | **−€6.6 (loss at 1k)** | **€19.7 (53%)** |
| **Gross margin via retail** | **negative** | **€5 (too thin)** |

Same lesson as every Matter consumer device: certification amortisation and a €50 market price mean you need 5k+ units and mostly direct/installer sales. If you can't see 5k units in year one, don't certify yet.

### Go-to-market

**First 100 customers:** Home Assistant community forum and r/homeassistant (show detection vs PIR side by side), Dutch Tweakers forum, German smart-home forums and YouTubers, Apple Home communities (r/HomeKit). Deposit page with €10 reservation.

**Then scale:** smart-home specialist webshops in NL/DE/Nordics, electricians via wholesalers and installer trainings ("Matter for electricians"), Amazon EU after reviews, new-build developers' smart-home packages.

### 12-month plan

- **Q1:** deposit campaign (kill question); prototype on HM-MT2401 EVB + LD2410S; side-by-side video vs PIR.
- **Q2:** own 30 mm PCB, battery profiling, enclosure + flush bezel, 50-unit beta in 3 ecosystems.
- **Q3:** CE + Matter certification, 2,000-unit run, D2C launch.
- **Q4:** installer 10-packs via 1 wholesaler, illuminance variant EVT.

**Team:** Matter/Thread embedded engineer (full-time), mechanical/industrial designer (contract), founder on community and installer sales, Shenzhen partner for PCBA/enclosure.

**Funding to first 2,000 units (estimate):** landed hardware excl. cert 2,000 × €12.5 = €25k + tooling €12k + CE €12k + Matter €15k + 8 months team €65k + beta/marketing €8k = **≈€137k**. 200 deposits → ~€10k cash, mostly proof. Real money: angel / smart-home pre-seed, or a partner brand (lighting maker) paying NRE for a white-label version.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** Aqara FP300 and other big brands at the same price | Installer/flush-mount niche + white-label for lighting brands; don't fight on Amazon in year 1 |
| **Technical:** battery life vs response time (radar wake + Thread sleepy device) | USB/5–24 V SKU first; battery SKU only if ≥12 months proven |
| **Technical:** false occupancy (fans, curtains, pets) | Zone/gate limits, pet-height tuning, hold-time attribute; publish known limits |
| **Ecosystem:** hubs differ in which occupancy attributes they show | Test in Apple, Google, SmartThings, Home Assistant; config fallback via BLE/web page |
| **Cost:** Matter certification + DAC provisioning process | Plan DAC with the module maker; certify once a deposit signal is strong |
| **Supply:** LD2410S single source, design files via maker | Firmware abstraction; second radar qualified |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2410S low-power presence radar | https://www.gongbans.com/db/hilink-ld2410s.html | Still + moving people at ~100 µA average; GPIO + UART | Datasheet public, design files via maker (no open schematics) | Buy as module |
| HopeRF HM-MT2401 Matter-over-Thread module | https://www.gongbans.com/db/hoperf-hm-mt2401.html | EFR32MG24 runs the Matter app | PCB library — HopeRF MIT GitHub folder: https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401 | MIT licence for repo content |
| HopeRF HM-MT2401 EVB kit | https://www.gongbans.com/db/hoperf-hm-mt2401-evb-kit.html | Reference schematic for module + sensor base board; dev platform | Schematic + firmware — https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401%20EVB%20Kit | MIT licence for repo content |

### Block diagram

```
USB-C / 5–24 V (installer SKU)  or  2×AA (retrofit SKU)
          │
     power path / buck ──► HM-MT2401 (EFR32MG24, Matter over Thread)
                                │ UART + GPIO (presence change interrupt)
                          LD2410S radar (gates tuned to room zone)
                                │
   Thread ──► border router (in speaker/TV/hub) ──► Matter controllers:
                Apple Home / Google Home / SmartThings / Home Assistant
   Cluster: OccupancySensing (occupied/unoccupied, hold time); config via attributes or BLE page
```

**Engineering gap:** the presence-to-occupancy logic (hold time, still detection thresholds), power budget for the battery SKU, the flush-mount mechanicals, and Matter certification logistics (DAC provisioning on the line).

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| LD2410S | €3–4 | Single source |
| HM-MT2401 | €4–5 | EFR32MG24 inside |
| 5–24 V buck (installer SKU) | €0.5 | |
| Battery holder + 2×AA (retrofit SKU) | €1.2 | |
| LED, button, passives | €0.4 | |
| Enclosure + flush bezel | €2–2.5 | Radar window: no metal, check plastic loss at 24 GHz |
| Retail box | €1 | |

### Firmware/software starting point

- **connectedhomeip** (project-chip) — the open Matter SDK; occupancy-sensor example apps exist in the SDK examples (verify for EFR32).
- **Silicon Labs Simplicity SDK / Matter extension** for EFR32MG24; HopeRF's EVB firmware as the board support starting point.
- **ESPHome `ld2410` component** as a reference for LD2410-family serial framing (check the S-variant differences in the datasheet).
- Test controller: **chip-tool** from the Matter SDK; plus real hubs.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — deposit page + side-by-side video (prototype radar vs PIR) in HA and Tweakers communities | **Kill question**: 200 deposits of €10 in 6 weeks (start now; decision at week 6) |
| 3–5 | **Works-like** — EVB + LD2410S as Matter occupancy sensor in Apple Home and Home Assistant | Detects a still reader for 30 min without dropping; hold time adjustable |
| 6–8 | **Looks-like + EVT** — 30 mm PCB, enclosure + flush bezel, 30 units; battery current profile | Battery SKU projection ≥12 months, or decide USB-only; installers fit flush mount in <5 min |
| 9–10 | **DVT + pre-compliance** — RED pre-scan, EN 18031 checklist, Matter pre-test, DAC provisioning trial | No pre-scan fails; test lab slot booked; provisioning works on 30 units |
| 11–12 | **Pilot batch** — 100 units to depositors (as beta, before Matter logo) | ≥90% working in their ecosystem; reviews ≥4/5; deposits converting ≥60% |

### Certification checklist (EU)

- **CE — RED:** EN 300 440 (24 GHz SRD — confirm which harmonised standard the radar module's own test report covers), EN 300 328 (2.4 GHz Thread), EN 301 489-1/-3/-17, EN 62368-1, EN 62311/62479. Estimate €8–12k.
- **EN 18031-1/-2** (RED cybersecurity, mandatory since 1 Aug 2025): internet-connected via border router; occupancy in a home is personal data → -2 applies. Budget €3–5k.
- **CRA:** reporting from 11 Sep 2026, full from 11 Dec 2027 — SBOM, OTA updates (Matter OTA), vulnerability handling, support period.
- **Matter certification** (CSA membership + authorised test lab): estimate €10–20k for the first product — check the current CSA fee schedule. Required for the Matter logo.
- **LVD:** not applicable at 5–24 V DC; the USB adapter (if supplied) must be CE/ErP compliant.
- **RoHS, REACH, WEEE**, packaging EPR. **Battery Regulation** if you supply AA cells (labelling, take-back).
- **GDPR:** data stays local in the home's Matter fabric — say so; no cloud processing by you.
- **Total estimate:** €21–37k incl. Matter.

### Validation toolkit

- **Kill question:** Will 200 Home Assistant users put down a €10 deposit for a €49 Matter radar puck when DIY ESPHome radar sensors already cost €15 and big brands sell Matter presence sensors at ~€50? Pass = 200 deposits in 6 weeks.
- **Interview script (5):**
  1. Which rooms have motion-controlled lights, and what annoys you about them?
  2. What sensors have you tried (PIR, mmWave, DIY)? Why did you keep or drop them?
  3. Which ecosystem/hub do you use, and do you have a Thread border router?
  4. Battery or powered — where would you mount it (ceiling, wall, shelf)?
  5. At €49, why would you pick this over a big-brand sensor at the same price?
- **Landing page:** Headline: "Lights that know you're still in the room." Bullets: "24 GHz radar detects people sitting still — PIR can't." / "Matter over Thread: Apple Home, Google Home, Home Assistant. No app, no account." / "Fits a ceiling hole or sits on a shelf; powered or battery."
- **Pass:** 200 deposits in 6 weeks, or one lighting brand/installer company ordering ≥500 units for white-label.

### First production checklist

- Samples: LD2410S + HM-MT2401 from production lots; check radar firmware version.
- Golden sample: detection pattern mapped in a test room; Matter certification build frozen.
- DFM: radar window thickness, flush bezel spring clips, battery door.
- MOQ: modules per tray; enclosure 2k shots; retail box 2k.
- QC/AQL: 100% commissioning test with QR verification, radar response test; AQL 1.0 functional / 2.5 cosmetic.
- Packaging: Matter QR on device + box + leaflet (all three must match); recycling marks.
- Incoterms: FOB Shenzhen; batteries shipped separately or declared correctly.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and HopeRF (华普微)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410S 24 GHz low-power human-presence radar module](/db/hilink-ld2410s.html) (low-power 24 GHz presence radar (static + moving people)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder)](/db/hoperf-hm-mt2401.html) (Matter-over-Thread module running the application); [HopeRF HM-MT2401 Matter-over-Thread EVB kit](/db/hoperf-hm-mt2401-evb-kit.html) (reference schematic for the Thread module + sensor base board). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) websites)

```email
Subject: Sample order and volume pricing — HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit — for a Matter Presence Puck

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Matter Presence Puck: A coin-sized ceiling puck that knows someone is still in the room (reading, on the sofa) — unlike PIR — and reports occupancy over Matter-over-Thread to any EU smart-home hub, fully local, no app account. The design is built around your HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit.
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
主题：样品订购及批量报价 — HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit — 用于Matter Presence Puck

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Matter Presence Puck：A coin-sized ceiling puck that knows someone is still in the room (reading, on the sofa) — unlike PIR — and reports occupancy over Matter-over-Thread to any EU smart-home hub, fully local, no app account。产品设计基于贵司的HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit。
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
Subject: PCBA quote from open design files — Matter Presence Puck, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Matter Presence Puck: A coin-sized ceiling puck that knows someone is still in the room (reading, on the sofa) — unlike PIR — and reports occupancy over Matter-over-Thread to any EU smart-home hub, fully local, no app account. The design starts from published open-hardware files (HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Matter Presence Puck，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Matter Presence Puck：A coin-sized ceiling puck that knows someone is still in the room (reading, on the sofa) — unlike PIR — and reports occupancy over Matter-over-Thread to any EU smart-home hub, fully local, no app account。设计基于已公开的开源硬件文件（HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HopeRF HM-MT2401 Matter-over-Thread EVB kit；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Put up the deposit page with a 30-second side-by-side video (borrow an LD2410 dev board + any PIR) and post it in two communities.
2. Order an HM-MT2401 EVB kit and 3 LD2410S; get an occupancy sensor commissioned in Home Assistant via Matter.
3. Call 3 electricians who do smart lighting: would they fit a €35 Matter presence sensor in a ceiling hole, and through which wholesaler do they buy?

Want help sourcing or building this? Talk to us via www.gongbans.com.
