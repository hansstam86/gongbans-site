# Precise Wayfinding Beacons — Founder Start Pack

> Battery beacons on doors, lifts and toilets in public buildings that a phone app can measure the real distance to ("accessible toilet, 4 metres ahead, door on your left") for blind and low-vision visitors.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

**The make-or-break fact:** Bluetooth Channel Sounding (CS) only helps if the visitor's phone supports it. Today that is a minority of phones. Reports say Apple is adding CS support for its newest iPhones only (via iOS 27, on models with Apple's newest wireless chip — [Novel Bits summary](https://newsletter.novelbits.io/archive/ios-27-brings-channel-sounding-to-the-iphone/)), and Android support depends on the chipset. Blind users skew to iPhone (VoiceOver), often keep phones for years, and many won't have a CS-capable phone in 2027. Design the product so it **works with plain RSSI beacons on every phone, and gets precise on CS phones**. If you sell "precision" only, you sell to a minority.

## 1. Summary

- **Problem:** Blind and low-vision visitors can't find the specific door, lift, counter or accessible toilet in a public building without help. GPS doesn't work indoors. Signal-strength (RSSI) beacons can say "you're near the toilets" but not "4 metres, on your left", so people walk past doors.
- **Customer:** Building operators that serve the public: town halls, libraries, museums, public areas of hospitals, train and bus stations, universities. The operator pays (facility or accessibility budget); visitors use the free app. Accessibility consultants and organisations of the blind influence the purchase.
- **Product:** Small battery beacons (5-year target) mounted next to key points. Each has a precise BLE 6.0 Channel Sounding module for distance ranging, plus a cheap identification-only variant for rooms that just need "this is room 1.14". A building-map tool for the operator, an open app SDK, and a reference app that speaks distance and direction. A dashboard shows beacon battery status.
- **Why now:** Bluetooth 6.0 Channel Sounding gives distance with far better accuracy than RSSI. Phone support is beginning (newest iPhones and Android flagships). Accessibility of public services has become a compliance topic: the European Accessibility Act applies to many services since June 2025, and national building and equality laws cover public buildings. Operators need visible, measurable improvements.
- **The ask:** About €250–300k (estimate) to the first 1,000 beacons and 10 reference buildings. B2G sales are slow: fund with pilot contracts, accessibility/innovation grants and an impact angel.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> How many phones in the hands of blind users in 2027 support Channel Sounding? If below 30%, fall back to RSSI beacons and the precision story dies.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Town halls, libraries, museums, hospitals' public areas, train stations; organisations for the blind; accessibility consultants.

**The problem as the pack states it:** Blind and low-vision visitors can't find the specific door, lift, counter or accessible toilet in a public building without help. GPS doesn't work indoors. Signal-strength (RSSI) beacons can say "you're near the toilets" but not "4 metres, on your left", so people walk past doors.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **European Blind Union** · https://www.euroblind.org/ — umbrella of the national organisations of the blind; find your country's member there.
- **RNIB (UK)** · https://www.rnib.org.uk/ — blind and partially sighted people; RNIB Connect community.
- **DBSV (DE)** · https://www.dbsv.org/ — German federation of the blind and visually impaired.
- **r/Blind** · https://www.reddit.com/r/Blind/ — blind and low-vision users; ask, do not pitch.
- **AppleVis** · https://www.applevis.com/ — blind and low-vision technology users; the most tech-literate part of the audience.
- **NEMO, Network of European Museum Organisations** · https://www.ne-mo.org/ — European museum associations.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€49–69 per beacon + set-up (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how town halls, libraries, museums, hospitals' public areas, train stations deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last time you had to find a specific door, lift or accessible toilet in a public building you did not know: what did you rely on, and where did it fail?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Battery beacons on doors, lifts and toilets in public buildings that a phone app can measure the real distance to — 'accessible toilet, 4 metres ahead, door on your left' — for blind and low-vision visitors. On a scale of one to ten, how likely would you be to buy that at €49–69 per beacon + set-up (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Precise Wayfinding Beacons: would you pay €49–69 per beacon + set-up (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Precise Wayfinding Beacons: Battery beacons on doors, lifts and toilets in public buildings that a phone app can measure the real distance to — 'accessible toilet, 4 metres ahead, door on your left' — for blind and low-vision visitors. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €49–69 per beacon + set-up (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The paying customer is the **public-building operator**: municipal facility management, library and museum services, transport operators. They buy through procurement (small pilots under direct-award thresholds first). The influencers are **organisations for blind and partially sighted people** (national associations, local groups) and **accessibility consultants** who write the specs. The user is the visitor with a phone, using VoiceOver/TalkBack.

Start with **museums and libraries**: they run pilots more easily than hospitals or stations, they have digital/inclusion budgets and they like to publicise accessibility work.

### Market size (estimates)
- EU public-service buildings with significant visitor traffic (town halls, libraries, museums, stations, hospitals' public areas, universities): assume ~150k.
- Assume 20 beacons per building + set-up → ~€1,500–2,500 per building in hardware + €500–1,000 set-up + €200–400/year software.
- **TAM:** 150k × ~€2,500 ≈ **€375 M** + recurring.
- **SAM:** DACH/Benelux/Nordics, larger buildings with an accessibility programme, ~10% → **~€35–40 M**.
- **SOM (3 years):** 300 buildings → **~€1 M** cumulative + ~€100k/year recurring.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Large-format QR/colour-code signage for blind users (camera-based apps that read special codes from a distance) | Low per sign | Needs the camera pointed in the right direction; no "behind you" or around-the-corner |
| RSSI BLE beacon wayfinding platforms | €20–50/beacon + software | Room-level accuracy only; "near" is not "4 m to the door" |
| Tactile floor guidance + Braille/tactile signs | €100s per metre/sign | Essential, but doesn't tell you *which* door; fixed, expensive to change |
| Staff assistance / booking an escort | Staff time | Dependence; not always available |
| Generic indoor maps in big-tech map apps | Free | Few buildings mapped, no last-metre precision |
| Do nothing | Free | Visitors give up or don't come |

**Wedge:** **last-metre precision** on CS phones ("door in 4 m, on your left") with graceful fallback on all phones, an **open SDK** so existing accessibility apps can integrate the beacons, and a **set-up tool a facility manager can use**.

### Product & value proposition
- **Precise beacon:** HopeRF HM-BT2401DA — BLE 6.0 Channel Sounding (RTT + PBR), Cortex-M33 78 MHz, 1 MB flash, dual PCB antennas, deep sleep 1.3 µA, +10 dBm max. Note: CS works as an *initiator/reflector* exchange — the phone and beacon actively range. Beacons must be connectable/discoverable for CS sessions, which costs battery; budget accordingly.
- **ID-only beacon:** HopeRF HM-BT4531(B) — BLE 5.2 (CMT4531, Coded PHY, deep sleep 1.4 µA, UART AT commands) for rooms that only need identification. Note: it's a transparent-UART module, so beaconing needs a small host MCU or the vendor's firmware options — check.
- **Power:** primary lithium (e.g. 2× AA or a CR123-class cell), 5-year target with adaptive advertising (more often during opening hours).
- **App/SDK:** speaks "accessible toilet, 4 metres, slightly left" using phone compass + CS distance; falls back to "near" with RSSI; works with VoiceOver/TalkBack; SDK for existing accessibility apps.
- **Operator tools:** a web map editor (place beacons, name points, write the spoken descriptions with an accessibility consultant), battery dashboard (beacons report battery to phones passing by → back-end).

**Pricing (estimates):** €59 per CS beacon, €29 per ID beacon; set-up package (survey + map + voice descriptions + training) €1,500 per building; software €300/year per building incl. battery monitoring.

### Unit economics (estimates per CS beacon, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (HM-BT2401DA, battery, holder, PCB, passives, tamper switch) | €11.00 | €8.50 |
| Assembly & test (CS ranging test at fixed distance) | €2.00 | €1.40 |
| Enclosure (tamper-resistant, adhesive + screw mount, tactile marker) | €2.50 | €1.60 |
| Packaging (bulk) | €0.40 | €0.25 |
| Freight + duty to EU | €0.40 | €0.30 |
| Certification amortised (~€20k) | €20.00 | €4.00 |
| **Landed cost** | **€36.30** | **€16.05** |
| Net revenue (direct to operator / via integrator at 25% margin) | €59 | €44 |
| **Gross margin** | **€22.70 (38%)** | **€27.95 (64%)** |

The real money is in set-up and software, not the beacons. A 20-beacon building = ~€1,000 beacons + €1,500 set-up + €300/year.

### Go-to-market
**First 100 customers (= ~10 buildings):**
- **Partner with one national or regional organisation for the blind** for testing and credibility; pay their testers.
- **Museums and libraries in one city** — one municipality with an accessibility officer can open 5–10 buildings.
- **Accessibility consultants** who write specs for public buildings: give them a spec text and demo kit.
- **Accessibility conferences and the assistive-tech community** (blind tech podcasts, mailing lists, app communities).

**Scale:** integrators that already install signage/BMS in public buildings; framework contracts with municipalities; transport operators.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: share of CS-capable phones among 50 blind users; RSSI fallback quality; pilot partner LOI (museum/library) |
| Q2 | Works-like: 20 beacons in one building, reference app (iOS first), 10 test users |
| Q3 | EVT/DVT beacon; RED testing; operator map tool; 3 buildings |
| Q4 | 1,000 beacons; 10 buildings; SDK released |

**Team:** 1 BLE/embedded engineer (CS is new — needs someone who reads the spec), 1 iOS + Android developer (accessibility-native), 1 accessibility specialist (part-time, ideally a blind expert user), founder on B2G sales.

**Funding to the first 1,000 beacons + 10 buildings (estimates):** NRE €110k (beacon hardware + firmware €40k, apps + SDK €50k, map tool €20k) + certification €20k + 1,000 beacons landed ~€16–20k + user testing €15k + 12 months lean costs €80k ≈ **€245k**. Minus pilot fees (10 buildings × €2,500 ≈ €25k) and accessibility/innovation grants (€50–150k in several countries) → **~€100–170k** from founders/impact angels.

### Top risks
| Risk | Mitigation |
|---|---|
| **Market/technical:** too few users have CS-capable phones in 2027 | Product works with RSSI on all phones; CS is a precision upgrade; measure the real share in Q1 |
| **Technical:** CS ranging needs connections/sessions — battery life and how many phones a beacon can serve at once | Range only when the app requests it near the target; adaptive advertising; test with 5 simultaneous users |
| **Technical:** phone OS support for CS APIs varies by OS version | Use OS ranging APIs where available; track API changes; keep fallback |
| **Market:** procurement is slow | Start under direct-award thresholds; pilots paid from innovation budgets |
| **Regulatory:** apps used by public bodies must meet accessibility standards (EN 301 549) | Build with blind developers/testers; publish an accessibility statement |
| **Privacy:** location of visitors with a disability | No visitor tracking; ranging happens on the phone; anonymous battery reports only |
| **Supply:** CS modules are new; firmware maturity | Second-source a BLE 6.0 CS module from another maker; keep the app protocol vendor-neutral |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF HM-BT2401DA BLE 6.0 Channel Sounding module | https://www.gongbans.com/db/hoperf-hm-bt2401da.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/BLE/HM-BT2401DA) | Distance ranging (RTT + PBR) with the phone | Datasheet, photos | MIT (HopeRF GitHub repo) |
| HopeRF HM-BT4531(B) BLE 5.2 UART module | https://www.gongbans.com/db/hoperf-hm-bt4531b.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/BLE/HM-BT4531%28B%29) | Low-cost ID-only beacon variant | PCB footprint/library, 3D model, datasheet | MIT (HopeRF GitHub repo) |

### Block diagram
```
 CS beacon:   [primary Li cell] -> [HM-BT2401DA (BLE 6.0 CS, M33)] <~~ CS ranging session ~~> [phone app]
                                        |-- tamper switch, battery ADC                          |
 ID beacon:   [primary Li cell] -> [HM-BT4531B] ~~ BLE advertising ~~>                          |
                                                                                                v
  [operator map tool] -> [building map + spoken descriptions] -> [app: "toilet, 4 m, slightly left"]
                                    [anonymous battery reports via passing phones] -> [dashboard]
```
**Engineering gap:** CS reflector firmware on the module, the phone side (CS APIs on iOS/Android, plus RSSI fallback), direction (CS gives distance, not direction — combine with phone compass and the map), the map/description tool, and battery life with CS sessions. Hardware is simple; software is 75% of the work.

### Starter BOM (estimates at 1k, CS beacon)
| Part | Est. cost | Notes |
|---|---|---|
| HM-BT2401DA | €4.00–6.00 | New module category; ask HopeRF for volume price and firmware/SDK support |
| Primary lithium cell(s) + holder | €3.00–4.00 | Size from measured CS session current |
| PCB, passives, tamper switch | €1.50 | |
| Enclosure + mount + tactile marker | €2.50 | Vandal-resistant screws in public areas |
| ID beacon alternative: HM-BT4531B + small MCU | €3.00 | Check whether vendor firmware can advertise standalone |

### Firmware/software starting point
- **Module SDK:** the HM-BT2401DA is built on a BLE 6.0 SoC — get the vendor SDK and CS examples from HopeRF; search the chip vendor's Channel Sounding examples once HopeRF confirms the SoC family.
- **Zephyr RTOS** (github.com/zephyrproject-rtos/zephyr) has Bluetooth Channel Sounding support work in progress — check if your SoC is supported.
- **Phone side:** Apple's Nearby Interaction documentation has a Channel Sounding capability check (`supportsBluetoothChannelSounding`); Android: search "Android Bluetooth channel sounding API" for the current status.
- **Indoor maps:** search "IndoorEqual" / OpenStreetMap indoor tagging (Simple Indoor Tagging) for an open map format.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill test:** survey 50 blind/low-vision phone users via an association — phone model + OS + upgrade plans → estimated CS share in 2027. If <30%: product = RSSI + "CS-ready". Plus one museum/library LOI |
| 3–5 | Works-like | 2 HM-BT2401DA + CS-capable phone: distance error <0.5 m at 1–10 m in a corridor; RSSI fallback app finds 10 points in one floor |
| 6–8 | Looks-like + EVT | Beacon PCB + enclosure; 30 units in one building; 5 blind testers find the accessible toilet unaided from the entrance |
| 9–10 | DVT + pre-compliance | RED pre-scan (EN 300 328), battery-life model from measured currents (≥3 years), app accessibility audit (VoiceOver/TalkBack) |
| 11–12 | Pilot batch | 50 beacons in 2 buildings; ≥80% task success for 10 testers; operator can edit the map without help |

### Certification checklist (EU)
- **CE under RED:** EN 300 328 (2.4 GHz wideband), EN 301 489-1/-17, EN 62368-1, EN 62479. Reuse module reports where accepted. Est. **€6–10k**.
- **RED delegated act (EN 18031-1/-2):** beacons themselves usually aren't internet-connected, but the app/back-end handle data — assess; €2–4k.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027 — the beacons have firmware and a radio: plan update path (BLE OTA), SBOM, vulnerability handling. The app is also a "product with digital elements" if sold.
- **Accessibility:** EN 301 549 for the app; WCAG 2.1 AA for the operator web tool (public bodies must procure accessible ICT).
- **RoHS, REACH, WEEE**, packaging.
- **Battery Regulation (EU) 2023/1542:** portable batteries — labelling, removability, take-back.
- **GDPR:** no tracking of visitors; ranging happens on the phone; battery reports anonymous. Publish a privacy notice anyway (users are a protected group).
- **Total estimate: €12–20k.**

### Validation toolkit
- **Kill question:** How many phones in the hands of blind users in 2027 support Channel Sounding? Below 30% → RSSI-first product, and the precision story is a bonus.
- **Cheapest experiment (~€0–200):** an online/phone survey with an association for the blind (accessible form!) + 2 CS dev modules in a corridor with one CS-capable phone.
- **5-question interview (blind visitor):** 1) Which public buildings do you avoid because finding your way is too hard? 2) What do you use today indoors (cane, guide dog, apps, staff)? 3) How exact must an instruction be to be useful? 4) Which phone and OS version do you use, and when will you replace it? 5) Would you install a free app for this, or should it be inside an app you already use?
- **5-question interview (operator):** budget owner, current accessibility plan, number of key points, procurement route, pilot appetite.
- **Landing page headline (operator):** "Let blind visitors find every door in your building on their own." Bullets: "Speaks the way: 'accessible toilet, 4 metres, on your left'." / "Works on every phone, more precise on new ones." / "Battery beacons, installed in a day, battery status in one dashboard."
- **Pass threshold:** 2 paid pilot buildings (≥€2,000 each) or signed LOIs + one association partnership.

### First production checklist
- **Samples:** CS modules from 2 lots; measure ranging bias per lot (calibration constant?).
- **Golden sample:** firmware version, antenna orientation in the enclosure, measured ranging error.
- **DFM review:** antenna clearance (dual PCB antennas — keep metal, screws and batteries away), enclosure for wall/door-frame mounting, tamper switch.
- **MOQ talk:** module MOQ (new modules may have low stock), primary cell supplier.
- **QC/AQL:** AQL II 1.0/2.5; 100% CS ranging test at a fixed distance on a jig; 100% battery-current check in sleep.
- **Packaging:** bulk installer packs of 10–20, each beacon labelled with ID + QR for the map tool.
- **Incoterms:** FOB Shenzhen; lithium primary cells shipped as UN 3091 (in equipment) or installed on site.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (HopeRF (华普微)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module](/db/hoperf-hm-bt2401da.html) (BLE 6.0 Channel Sounding module for distance ranging); [HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module](/db/hoperf-hm-bt4531b.html) (low-cost BLE beacon variant for rooms that only need identification). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Moko Technology** (深圳市摩可智能硬件有限公司) · mokosmart.com — BLE / WiFi / NB-IoT module OEM: BLE 5.0 beacon; NB-IoT tracker; WiFi module; CE/FCC/RoHS OEM/ODM. *(BLE modules and beacons)*
- **Minew Technologies** (深圳市敏芯微电子技术有限公司) · minewtech.com — BLE beacon / indoor positioning: BLE beacon; iBeacon; AoA/AoD positioning; CE/FCC modules OEM. *(BLE modules and beacons)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) website)

```email
Subject: Sample order and volume pricing — HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module — for a Precise Wayfinding Beacons

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Precise Wayfinding Beacons: Battery beacons on doors, lifts and toilets in public buildings that a phone app can measure the real distance to — 'accessible toilet, 4 metres ahead, door on your left' — for blind and low-vision visitors. The design is built around your HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module.

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module.
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
主题：样品订购及批量报价 — HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module — 用于Precise Wayfinding Beacons

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Precise Wayfinding Beacons：Battery beacons on doors, lifts and toilets in public buildings that a phone app can measure the real distance to — 'accessible toilet, 4 metres ahead, door on your left' — for blind and low-vision visitors。产品设计基于贵司的HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module。
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
Subject: PCBA quote from open design files — Precise Wayfinding Beacons, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Precise Wayfinding Beacons: Battery beacons on doors, lifts and toilets in public buildings that a phone app can measure the real distance to — 'accessible toilet, 4 metres ahead, door on your left' — for blind and low-vision visitors. The design starts from published open-hardware files (HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Precise Wayfinding Beacons，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Precise Wayfinding Beacons：Battery beacons on doors, lifts and toilets in public buildings that a phone app can measure the real distance to — 'accessible toilet, 4 metres ahead, door on your left' — for blind and low-vision visitors。设计基于已公开的开源硬件文件（HopeRF HM-BT2401DA BLE 6.0 Channel Sounding (distance ranging) module, HopeRF HM-BT4531(B) BLE 5.2 transparent-UART module；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 2 HM-BT2401DA modules and ask HopeRF for the SDK, CS example firmware and a volume price.
2. Contact one organisation for the blind and ask them to circulate a 5-question phone/OS survey to 50 members.
3. Ask one museum or library with an accessibility officer for a 1-hour site visit to map 15 key points.

Want help sourcing or building this? Talk to us via www.gongbans.com.
