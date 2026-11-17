# Bathroom Fall Alert (radar, no camera) — Founder Start Pack

> A splash-proof ceiling sensor for the bathroom that alerts family or a neighbour when it sees someone go down and not get up. It uses 60 GHz radar: no camera, and no wearable to forget.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The bathroom is where older people living alone are most likely to fall (wet floors, getting in and out of the shower, getting up at night). It's also where pendants come off and where nobody accepts a camera. A person lying on the floor for hours turns a fall into a crisis.
- **Customer:** Adult children (45–65) of parents living alone in NL, DE and the Nordics pay; the parent lives with it. In the B2B segment, housing associations and home-care organisations buy non-medical safety tech for their tenants or clients.
- **Product:** A ceiling-mounted, mains-powered sensor with a 60 GHz fall-detection radar module (bathroom profile, 2 m range) and an LTE-M link, so it works without home Wi-Fi. When the radar reports a fall, the sensor plays a 60-second "are you OK?" voice prompt with a big cancel button, then sends an SMS/app alert to 3 contacts. A daily heartbeat confirms it's alive. Only events leave the device.
- **Why now:** Off-the-shelf 60 GHz fall-detection radar modules with a toilet/bathroom profile exist (Hi-Link LD6002C). LTE-M is cheap and widely deployed in Europe. Ageing in place is policy in every EU country, and home-care staff are scarce.
- **The ask:** About €250k (estimate) to reach 1,000 units, because field validation is the expensive part. Route: an ageing/eHealth innovation grant, a pilot contract with a housing association, then angels.

**Positioning in one line: a safety alert, not a medical device.** It doesn't diagnose, monitor health or replace professional care or social-alarm services.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> What is the real false-alarm rate over 30 nights in 10 real bathrooms (showers, towels, pets)? More than one false alert a week = families switch it off.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Adult children of parents living alone (NL/DE/Nordics), housing associations, home-care organisations buying non-medical safety tech.

**The problem as the pack states it:** The bathroom is where older people living alone are most likely to fall (wet floors, getting in and out of the shower, getting up at night). It's also where pendants come off and where nobody accepts a camera. A person lying on the floor for hours turns a fall into a crisis.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/AgingParents** · https://www.reddit.com/r/AgingParents/ — adult children caring for parents: the buyer for most elderly-care devices.
- **r/CaregiverSupport** · https://www.reddit.com/r/CaregiverSupport/ — family carers.
- **Carers UK forum** · https://www.carersuk.org/forum/ — family carers in the UK.
- **TSA, TEC Services Association (UK)** · https://www.tsa-voice.org.uk/ — UK trade body for technology-enabled care (telecare); the buyers in councils and housing providers.
- **AGE Platform Europe** · https://www.age-platform.eu/ — EU network of organisations of and for older people.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199 + optional €5/month alerts (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how adult children of parents living alone, housing associations, home-care organisations buying non-medical safety tech deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Your parent lives alone: what happens today if they slip in the bathroom and cannot get up, and have you tried anything (a pendant, a call routine) that did not stick?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A splash-proof ceiling sensor for the bathroom that alerts family or a neighbour when it sees someone go down and not get up — 60 GHz radar, no camera, no wearable to forget. On a scale of one to ten, how likely would you be to buy that at €149–199 + optional €5/month alerts (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Bathroom Fall Alert (radar, no camera): would you pay €149–199 + optional €5/month alerts (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Bathroom Fall Alert (radar, no camera): A splash-proof ceiling sensor for the bathroom that alerts family or a neighbour when it sees someone go down and not get up — 60 GHz radar, no camera, no wearable to forget. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–199 + optional €5/month alerts (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Primary buyer: **the adult daughter or son** living 30–300 km away, who already worries, already tried a pendant ("Mum won't wear it in the shower") and refuses cameras. The user, the parent, must accept it, so "no camera, nothing to wear" is the whole pitch.

B2B buyer: **housing associations with senior housing** (NL: woningcorporaties; DE: Wohnungsbaugenossenschaften), and **home-care providers** who want fewer emergency visits and better peace of mind for families. They buy in batches of 50–500 and need installation, a portal and a support process.

### Market size (estimates)
- EU people aged 75+ living alone: roughly 10–12 M (estimate from Eurostat household data; check the current figure).
- **TAM:** 11 M × €179 ≈ **€2 B** hardware, plus €5/month service ≈ €660 M/year.
- **SAM:** NL, DE, BE, AT and the Nordics (high willingness to pay, good LTE-M coverage, families comfortable buying tech), ~25% → **€500 M** hardware.
- **SOM (3 years):** 0.2% of SAM → ~5,500 units → **~€1 M** hardware + ~€0.3 M/year service.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Social-alarm pendants with a monitoring centre (Hausnotruf-type services, in some countries partly reimbursed) | €0–40/month | Pendants come off in the bathroom; pressing a button requires being conscious |
| Smartwatches with fall detection | €250–450 + phone | Taken off in the shower and at night; charging; older people don't wear them |
| Consumer presence radars with a fall mode (e.g. Aqara FP2, ceiling-mount fall mode; needs a hub/app and Wi-Fi) | €70–90 | Wi-Fi-dependent, app-centric, generic; configuring a fall zone is a hobbyist task |
| Professional radar fall sensors (e.g. Vayyar Walabot Home; Milesight VS373 at ~€300 net, LoRaWAN, B2B) | €300+ | Expensive, B2B integration, aimed at care homes |
| Cameras with AI fall detection | €50–200 | Unacceptable in a bathroom |
| Do nothing / daily phone call | Free | Hours on the floor until the next call |

**Wedge:** bathroom-specific, mounts once, has its own LTE-M link (no Wi-Fi, no smartphone needed for the parent), a "cancel" prompt that kills most false alarms locally, and an honest published false-alarm rate. Priced as a family purchase, not a care-home system.

### Product & value proposition
- **Sensing:** Hi-Link LD6002C 60 GHz fall-detection radar (per brochure: 2 m range, 1 person, 90% accuracy, ±60°, UART, 3.3 V at up to 600 mA, so it has to be mains-powered).
- **Logic:** ESP32-S3 (AtomS3-Lite for the works-like) runs the alert chain. Radar fall event → speaker prompt + flashing LED ring + big cancel button by the door/toilet (a wireless button, or a pull cord) → if not cancelled within 60 s → SMS + app push to 3 contacts with "possible fall, bathroom, 07:42" → escalation if nobody acknowledges within 10 min.
- **Connectivity:** LTE-M (M5Stack Unit CatM for the works-like) with an eSIM/iSIM bundle, so it needs no Wi-Fi and no smartphone at the parent's home.
- **Power:** HLK-10Mxx isolated AC-DC (85–265 VAC in, 3000 VAC isolation, potted, per brochure) for a fixed ceiling install by an electrician, or a plug-in USB-C variant with a ceiling cable cover for DIY.
- **Privacy:** no camera, no microphone recording (speaker only), no raw radar data leaves the device. Event log only.

**Pricing (estimates):** €179 device RRP + €5/month alert service (SMS, connectivity, escalation). B2B: €149/unit + €3/month at 100+ units, plus installation. Alternative: €299 with 3 years' service included (families like "pay once").

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (LD6002C, ESP32-S3 module, LTE-M module + SIM, speaker/amp, LED ring, AC-DC 10 W module, PCB) | €46.00 | €37.00 |
| Wireless cancel button (sub-GHz or BLE, coin cell) | €4.50 | €3.20 |
| Assembly & test (incl. radar fall-simulation jig, LTE attach test) | €5.50 | €3.80 |
| Enclosure (ceiling dome IP44, radome window, mounting plate) | €6.00 | €3.80 |
| Packaging (box, button, fixings, guide) | €2.00 | €1.40 |
| Freight + duty to EU | €2.20 | €1.50 |
| Certification amortised (~€45k: RED for 60 GHz + LTE, LVD/mains, EMC, EN 18031, IP44) | €45.00 | €9.00 |
| **Landed cost** | **€111.20** | **€59.70** |
| Net device price after channel (direct €148 ex-VAT / B2B €125) | €148 | €125 |
| **Gross margin on hardware** | **€36.80 (25%)** | **€65.30 (52%)** |
| Service margin (€4.13/month ex-VAT minus ~€1.20 connectivity+SMS) | ~€35/year | ~€35/year |

The service is what makes this a business. At 1k units the hardware barely pays for certification.

### Go-to-market
**First 100 customers:**
- **One housing association pilot** (NL/DE senior housing, 50 flats). They have a budget line for safety, and their tenant-board approval is a great reference.
- **Family caregiver communities:** Facebook groups and forums for adult children caring for parents at a distance; informal-carer support organisations (they run newsletters and events).
- **Pharmacies and home-care equipment shops** (stair lifts, grab rails): they already sell bathroom safety. Put a demo unit on the counter.
- **Bathroom-adaptation installers** (walk-in shower conversions): bundle the sensor with the renovation.

**Scale channels:** home-care providers (white label), social-alarm service providers (add it as a "bathroom sensor" to their existing service, which makes them partners not competitors), insurers' ageing-in-place programmes, and housing-association framework tenders.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: false-alarm study in 10 real bathrooms for 30 nights; housing-association LOI; works-like units |
| Q2 | Custom PCB + ceiling enclosure; alert service v1 (SMS + app); EVT 50 units in a pilot building |
| Q3 | DVT; RED/LVD/EN 18031 testing; pilot 200 units (housing association + families) |
| Q4 | 1,000 units; first B2B framework contract; second country |

**Team:** 1 embedded engineer (radar + LTE-M + low-level), 1 backend/app developer (alert service, escalation, portal), 1 founder for B2B sales with a care or housing background, plus a part-time field-trial coordinator. A regulatory consultant to check the MDR boundary (a few days of work).

**Funding to the first 1,000 units (estimates):** NRE €80k (PCB/RF €20k, enclosure tooling €15k, firmware €15k, alert service + app €30k) + certification €45k + field validation (10 bathrooms × 30 nights + 50-unit pilot) €25k + 1,000 units landed ~€66k + 12 months of costs €100k ≈ **€315k**. Subtract the housing-association pilot (~€15k) and a 50% innovation grant on NRE/validation (~€50k) → **~€250k**. Route: grant (national ageing/eHealth innovation programmes, EU-level calls for ageing in place) + pilot contract + angels with care-sector backgrounds.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: false alarms** (showering, bending to dry feet, towels, a pet, two people) | The local "are you OK?" prompt with cancel; per-room tuning; publish your measured rate. Kill criterion: >1 false alert/week |
| **Technical: missed falls** (slow slides down a wall, falls outside the 2 m zone, falls in the shower behind glass) | Mount centrally over the danger zone; state the coverage clearly; test with stunt mats and a dummy + volunteers; never claim 100% |
| **Regulatory: MDR creep** | Intended use = safety alert. No "detects medical emergencies", no health monitoring, no vital signs. Get a regulatory consultant to review the IFU, website and app text before launch |
| **Regulatory: GDPR** | A fall event in a person's home is likely health-related personal data (special category). Lawful basis = explicit consent of the person; data minimisation (events only); EU hosting; DPIA before the pilot |
| **Market:** families buy a cheaper Wi-Fi radar | Sell on "no Wi-Fi, no app for Mum, works day one", the cancel prompt and the escalation service |
| **Supply:** single-source radar module; LTE-M module and SIM provider lock-in | Second-source a 60 GHz fall module; pick a multi-network eSIM provider; keep the radar firmware version frozen |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD6002C 60 GHz fall-detection radar | https://www.gongbans.com/db/hilink-ld6002c.html | Fall detection with a toilet/bathroom profile, 2 m, UART | **Datasheet public, files via maker** (no open schematic/PCB) | Commercial module; get the protocol doc and test reports from Hi-Link |
| M5Stack Unit CatM (U128) | https://www.gongbans.com/db/m5stack-unit-catm.html | LTE-M link for the works-like: alerts without home Wi-Fi | Enclosure/structure only (no main-board electronics) | Buy for prototyping; use a certified LTE-M module in production |
| M5Stack AtomS3-Lite (C124) | https://www.gongbans.com/db/m5stack-atoms3-lite.html | ESP32-S3 controller for alert logic and setup | Enclosure/structure only | Buy for prototyping |
| Hi-Link HLK-10Mxx 10 W AC-DC module | https://www.gongbans.com/db/hilink-10mxx.html | Isolated mains supply for a fixed ceiling install (3000 VAC isolation, potted, CE per brochure) | **Datasheet public, files via maker** | Commercial module; the end product still needs its own LVD/EMC testing |

0 of 4 boards publish schematic/PCB files. This is a module-integration product: the value is in the alert logic, the validation data and the service.

### Block diagram
```
[230 VAC ceiling feed] -> [HLK-10M05 isolated AC-DC] -> [5 V / 3.3 V rails]
                                                            |
[LD6002C 60 GHz fall radar] --UART--> [ESP32-S3] --UART/AT--> [LTE-M module + eSIM] ~~> [alert service: SMS/app/escalation]
                                       |   |   \
                         [speaker + amp]  [LED ring]  [sub-GHz/BLE RX] <~~ [wireless CANCEL button by the door]
                                       |
                              [setup via BLE / phone app (installer only)]
```
**Engineering gap:** the sensing and the communication are bought in. What's missing: the alert state machine (fall → prompt → cancel → escalate → acknowledge), field tuning for real bathrooms, the voice prompt (multilingual), the cancel button pairing, the heartbeat/self-test, the backend with escalation and audit trail, and **the validation data set**. That data set is your moat and your biggest cost.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD6002C radar | €20–28 | **Sole-source**; current draw up to 600 mA per brochure, so size the PSU and heat accordingly |
| ESP32-S3 module | €2.80 | Multi-source |
| LTE-M module (certified, EU bands) + eSIM | €9–12 | Long lead times possible; choose a module with existing CE/RED reports |
| HLK-10M05 AC-DC | €3.50 | Or a USB-C plug-in variant for the DIY SKU |
| Speaker + class-D amp | €1.60 | |
| LED ring + light pipe | €1.20 | |
| Sub-GHz/BLE receiver for the cancel button | €1.50 | |
| PCB, connectors, passives | €3.50 | |
| Ceiling enclosure IP44 + radome | €6.00 | Tooling ~€12–15k |

### Firmware/software starting point
- ESP-IDF (or Arduino-ESP32) on the S3; M5Stack's libraries for the AtomS3-Lite and Unit CatM in the works-like phase.
- LTE-M: AT command set of the chosen module; search "ESP32 LTE-M MQTT" for examples. Use MQTT over TLS to your own EU-hosted broker.
- Radar: the LD6002C UART protocol document from Hi-Link (request the latest version and the configuration tool).
- Backend: any EU-hosted MQTT broker + a small service for escalation; SMS via an EU SMS API. Search "open-source alerting escalation" if you don't want to build it.
- OTA: ESP-IDF secure boot + signed OTA (you will need it for the CRA).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Recruit 10 households (friends' parents, one housing association) for a 30-night study; works-like rigs built (radar + AtomS3-Lite + logging); DPIA draft and consent forms |
| 3–5 | Works-like | 10 bathrooms logging events (local logging only); daily review with the household ("did someone fall?"); **kill question answered: ≤1 false alert per week per bathroom after the cancel prompt**; 20 staged falls on mats detected ≥85% |
| 6–8 | Looks-like + EVT | Custom PCB + ceiling dome, cancel button, LTE-M + alert service; 30 EVT units; installer setup flow <15 min |
| 9–10 | DVT + pre-compliance | RED pre-scan (60 GHz + LTE-M), LVD/EMC pre-scan with the AC-DC; IP44 test; MDR-boundary review of all texts; EN 18031 gap analysis |
| 11–12 | Pilot batch | 50 units in a housing-association building; escalation tested end to end monthly; published false-alarm and detection numbers |

### Certification checklist (EU)
- **MDR boundary (read this first):** under the MDR (EU) 2017/745, software or hardware is a medical device if the *manufacturer's intended purpose* is medical (diagnosis, prevention, monitoring, prediction or treatment of disease or injury). A fall *alert* for safety and peace of mind, with no health monitoring, no vital signs and no clinical claims, is generally positioned outside the MDR. Claims like "monitors your health", "detects medical emergencies", "prevents injury" or "for patients" can pull it in. Write a one-page intended-use statement, keep every text consistent with it, and have a regulatory consultant review it (~€2–5k). Don't add breathing or heart-rate features to this product.
- **CE under RED:** 60 GHz radar (the module's test standard per Hi-Link; e.g. EN 305 550 for 40–246 GHz short-range devices, confirm with the lab), LTE-M (EN 301 908 series via a pre-certified module), BLE/sub-GHz for the cancel button (EN 300 328 / EN 300 220), EMC EN 301 489-1/-17/-52, exposure EN 62311/62479. Est. **€15–25k**.
- **LVD / safety:** EN 62368-1 for the mains-powered product, even with a certified potted AC-DC module. Est. **€4–6k**. Ceiling install by an electrician per national wiring rules; the DIY SKU uses a certified USB-C adapter.
- **RED delegated act cybersecurity: EN 18031-1 and EN 18031-2** (internet-connected **and** processes personal data). Mandatory since 1 Aug 2025. Est. **€10–18k**.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Signed OTA, SBOM, vulnerability disclosure, security updates for the support period.
- **GDPR:** special-category risk (health-related). Explicit consent from the person being monitored (not just the paying child), DPIA, EU hosting, retention limits (e.g. events kept 90 days), access for the person.
- **IP44** (EN 60529) for bathroom use outside the splash zones; check national bathroom-zone wiring rules for the ceiling location.
- **RoHS, REACH, WEEE**, packaging registration; **Battery Regulation** for the cancel button's coin cell (portable battery labelling).
- **Total certification + regulatory budget estimate: €35–55k.**

### Validation toolkit
- **Kill question:** What is the real false-alarm rate over 30 nights in 10 real bathrooms (showers, towels, pets)? More than one false alert a week and families switch it off.
- **Cheapest experiment (~€1,500):** 10 rigs (LD6002C + AtomS3-Lite + SD-card logging + USB power) installed in volunteers' bathrooms for 30 nights. No alerts are sent; you just log events and ask every morning. Add 20 staged falls on a crash mat with consenting adult volunteers.
- **5-question interview (adult child):** 1) What do you do today to know your parent is OK? 2) Has your parent fallen, and how long did it take before someone knew? 3) What happened with pendants or watches? 4) Would your parent accept a sensor in the bathroom if it has no camera and nothing to wear? 5) €179 plus €5/month: who pays, and would you order today?
- **Landing page headline:** "If Mum falls in the bathroom, you'll know." Bullets: "No camera, no microphone recording, nothing to wear." / "Asks 'are you OK?' first, then alerts up to 3 people by SMS." / "Works without Wi-Fi or a smartphone, installed in 15 minutes." Small print: "A safety alert, not a medical device."
- **Pass threshold:** false-alarm rate ≤1/week/bathroom **and** 100 families on a deposit list (€20) **or** one housing association LOI for 50 units.

### First production checklist
- **Samples:** golden sample with radar firmware version, LTE-M firmware version and alert-chain test log; agree a firmware-freeze process with Hi-Link and the LTE-M module maker.
- **DFM review:** radome window material/thickness for 60 GHz, thermal path for the radar (600 mA) and the AC-DC in a closed dome, cable entry, mounting plate.
- **MOQ talk:** radar modules (lead time and lifecycle), LTE-M modules (allocations happen), eSIM provider contract (minimum commitments).
- **QC/AQL:** AQL II 0.65 (critical: mains safety) / 1.0 / 2.5; 100% hi-pot test, 100% radar self-test on a jig, 100% LTE attach + test SMS, 100% speaker/LED/cancel pairing.
- **Packaging:** consumer box for families, bulk pack for B2B; installation guide with ceiling-position template; privacy leaflet.
- **Incoterms:** FOB Shenzhen with your forwarder; SIM activation happens at first boot in the EU (avoid roaming fees during logistics).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD6002C 60 GHz human fall-detection radar module (2T2R)](/db/hilink-ld6002c.html) (60 GHz fall-detection radar (bathroom/toilet profile, 2 m)); [HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package)](/db/hilink-10mxx.html) (10 W isolated AC-DC module for a fixed ceiling install). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit CatM (U128)](/db/m5stack-unit-catm.html) (Cat-M link so alerts work without home Wi-Fi); [M5Stack AtomS3-Lite (C124)](/db/m5stack-atoms3-lite.html) (ESP32-S3 controller for alert logic and setup). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124) — for a Bathroom Fall Alert (radar, no camera)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Bathroom Fall Alert (radar, no camera): A splash-proof ceiling sensor for the bathroom that alerts family or a neighbour when it sees someone go down and not get up — 60 GHz radar, no camera, no wearable to forget. The design is built around your HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124).
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
主题：样品订购及批量报价 — HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124) — 用于Bathroom Fall Alert (radar, no camera)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Bathroom Fall Alert (radar, no camera)：A splash-proof ceiling sensor for the bathroom that alerts family or a neighbour when it sees someone go down and not get up — 60 GHz radar, no camera, no wearable to forget。产品设计基于贵司的HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124)。
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
Subject: PCBA quote from open design files — Bathroom Fall Alert (radar, no camera), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Bathroom Fall Alert (radar, no camera): A splash-proof ceiling sensor for the bathroom that alerts family or a neighbour when it sees someone go down and not get up — 60 GHz radar, no camera, no wearable to forget. The design starts from published open-hardware files (HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Bathroom Fall Alert (radar, no camera)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Bathroom Fall Alert (radar, no camera)：A splash-proof ceiling sensor for the bathroom that alerts family or a neighbour when it sees someone go down and not get up — 60 GHz radar, no camera, no wearable to forget。设计基于已公开的开源硬件文件（HLK-LD6002C 60 GHz human fall-detection radar module (2T2R), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), M5Stack Unit CatM (U128), M5Stack AtomS3-Lite (C124)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 10× LD6002C, 10× AtomS3-Lite and SD-card loggers; build one logging rig and test it in your own bathroom for 3 nights.
2. Write the one-page intended-use statement ("safety alert, not a medical device") and a consent form, and get a regulatory consultant quote for an MDR-boundary review.
3. Email two housing associations with senior housing asking for a 10-bathroom, 30-night study (no alerts, logging only) in exchange for free units later.

Want help sourcing or building this? Talk to us via www.gongbans.com.
