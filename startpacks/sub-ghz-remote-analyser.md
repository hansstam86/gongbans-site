# Sub-GHz Remote Analyser — Founder Start Pack

> A receive-only handheld that shows what an unknown 433/868 MHz remote, sensor or doorbell is sending: frequency, modulation, timing and a protocol guess. Built for repair technicians, home-automation tinkerers and radio students.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Every European home has a drawer full of sub-GHz gadgets (remote sockets, doorbells, weather stations, awning remotes, window sensors). When one stops working, or someone wants to automate it, nobody can see what it actually sends. Repairers guess and hobbyists buy a €180 hacking multi-tool or fight with an SDR on a laptop.
- **Customer:** Repair cafés and independent electronics repairers, smart-home installers, home-automation hobbyists, and vocational and university radio/IoT courses. The person who uses it is usually the person who pays, except in schools, where the teacher's budget pays.
- **Product:** A pocket handheld built around a HopeRF CMT2219B receiver and an ESP32-S3 with a small screen. It covers 433.92 and 868 MHz (plus 315 for imports), with a spectrum sweep, OOK/FSK timing capture, a protocol guess for common fixed-code devices, and export to a PC or home-automation tools. **Receive-only by design: no transmit, no replay.**
- **Why now:** HopeRF publishes the receiver's schematic, PCB and demo code under MIT on GitHub. The transmit-capable multi-tools carry a "hacker" image that schools, repair cafés and some marketplaces don't want. Repair (right-to-repair rules, repair bonuses in several EU countries) is mainstream.
- **The ask:** About €95k (estimate) to reach 1,000 units. Fund it with a crowdfunding pre-order, a small maker-community angel and an education reseller's first order.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 300 people pre-order a receive-only tool when transmit-capable multi-tools exist? The pitch is 'legal, simple, cheap' — test with repair-café networks.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Electronics repairers, home-automation hobbyists, smart-home installers, radio and IoT students.

**The problem as the pack states it:** Every European home has a drawer full of sub-GHz gadgets (remote sockets, doorbells, weather stations, awning remotes, window sensors). When one stops working, or someone wants to automate it, nobody can see what it actually sends. Repairers guess and hobbyists buy a €180 hacking multi-tool or fight with an SDR on a laptop.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/RTLSDR** · https://www.reddit.com/r/RTLSDR/ — software-defined-radio hobbyists; 433 MHz decoding with rtl_433 is common.
- **r/flipperzero** · https://www.reddit.com/r/flipperzero/ — owners of the Flipper Zero, the people already poking at sub-GHz remotes.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Repair Café International** · https://www.repaircafe.org/ — network of volunteer repair cafés; the local café is the way in.
- **r/amateurradio** · https://www.reddit.com/r/amateurradio/ — radio hobbyists who also teach and mentor.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€59–79 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how electronics repairers, home-automation hobbyists, smart-home installers, radio and IoT students deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last 433 or 868 MHz remote, doorbell or sensor you had to figure out: what did you use to see what it was sending, and how long did it take?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A receive-only handheld that shows what an unknown 433/868 MHz remote, sensor or doorbell is sending — frequency, modulation, timing, protocol guess — for repair technicians, home-automation tinkerers and radio students. On a scale of one to ten, how likely would you be to buy that at €59–79 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Sub-GHz Remote Analyser: would you pay €59–79 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Sub-GHz Remote Analyser: A receive-only handheld that shows what an unknown 433/868 MHz remote, sensor or doorbell is sending — frequency, modulation, timing, protocol guess — for repair technicians, home-automation tinkerers and radio students. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €59–79 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Segment 1, the first buyers, is **home-automation hobbyists in DE, NL, AT, CH and the Nordics**. They run Home Assistant, ioBroker or openHAB and own cheap 433 MHz gear from DIY stores. Today they use an RTL-SDR dongle plus rtl_433 on a laptop. It works, but it isn't a 30-second answer in the hallway.

Segment 2 is **repairers**: repair-café volunteers (thousands of cafés in Europe) and small TV/appliance repair shops asked "my remote doesn't work". The first question is always "is it sending at all?" A €10 RF field-strength meter gives a beep and nothing more.

Segment 3 is **education**: vocational electronics schools and universities of applied sciences teaching IoT and radio. They buy class sets of 10–15 and want a tool that can't be used to open a neighbour's garage.

### Market size (estimates)
- Home-automation hobbyists in Europe: assume ~1 M+ active open-source home-automation installs worldwide (estimate, check current public install statistics). Assume ~40% are in Europe and ~20% of those have sub-GHz gear they care about, which gives **~80k–100k potential hobby buyers**.
- Repair cafés plus small repair shops in the EU: **~30k** sites (estimate). Vocational/technical schools and universities with electronics programmes: **~10k** (estimate).
- **TAM:** ~140k × €69 ≈ **€10 M** one-off. This is a niche tool, so be honest about that.
- **SAM:** buyers reachable in German/Dutch/English communities with a reason to buy this year, ~40% → **€4 M**.
- **SOM (3 years):** 5% of SAM → ~3,000 units → **~€200k** revenue. It's a good first product or a side line, not a venture-scale company on its own. The upside is a product family: the export link to a 433 MHz-to-Matter bridge (a sister concept) and a classroom bundle.

### Competition
| Alternative | Price (estimate / listings) | Weakness we attack |
|---|---|---|
| Transmit-capable multi-tools (e.g. Flipper Zero, ~€165–190 at EU resellers such as [Lab401](https://lab401.com/collections/all/flipper-zero)) | €165–190 | Expensive; transmit/replay features get it banned from some marketplaces and make schools nervous; sub-GHz analysis is one feature among many |
| RTL-SDR dongle + rtl_433 / Universal Radio Hacker on a laptop | €30–45 + laptop | Powerful but needs a laptop, drivers and know-how; not a hallway tool |
| RF field-strength / "remote tester" pens | €8–20 | Beep only: no frequency, no modulation, no protocol |
| Sonoff-style RF bridges in sniff mode | €11–25 | 433 only, fixed-code subset, no timing view, needs an app/cloud |
| Do nothing: throw out the remote, buy a new set | €15–40 | Waste, and the repair never happens |

**Wedge:** "The legal, simple, €69 answer to *what is this remote sending?*" It's receive-only, has a screen, needs no laptop and works out of the box, and it's safe enough to buy for a classroom.

### Product & value proposition
- **Hardware:** CMT2219B receiver (127–1020 MHz, −121 dBm at 2 kbps per the HopeRF folder) on a small RF board with a switchable 433/868 matching network (two SAW filters or one wideband front end; decide in week 3). ESP32-S3 module with a 1.3–2" colour screen and 3 buttons. USB-C charging with a 500–800 mAh Li-ion pouch cell, or 2× AAA if you want to avoid the battery work. A whip antenna on an SMA connector so students can swap antennas.
- **Modes:** (1) **Sweep:** step the frequency and plot RSSI to find "where is it sending?"; (2) **Capture:** OOK/FSK pulse train with timing histogram; (3) **Identify:** match against a protocol library of common fixed-code encoders (EV1527/PT2262-class, common weather-station formats); (4) **Export:** USB/Wi-Fi JSON, plus a code snippet for ESPHome/rtl_433-style configs.
- **Deliberately absent:** transmitter, replay, brute-force, rolling-code analysis. Rolling-code frames are shown as "rolling code: not decoded". Put this in the marketing, because it's the product.

**Pricing (estimates):** €69 RRP consumer (€59 early bird), €590 class set of 10 with lesson sheets, €15 antenna pack. B2B to electronics distributors and education resellers at 35–40% off.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (CMT2219B + front end/SAW, ESP32-S3 module, 1.5" TFT, Li-ion + charger, SMA, PCB) | €19.50 | €15.00 |
| Assembly & test (SMT + RF sensitivity check with a signal source) | €3.20 | €2.20 |
| Enclosure (2-part ABS, button caps, tooling amortised) | €3.80 | €1.90 |
| Packaging (box, antenna, quick-start card) | €1.40 | €1.00 |
| Freight + duty to EU (Li-ion in equipment) | €1.60 | €1.10 |
| Certification amortised (~€14k: RED receiver, EMC, battery docs, EN 18031 if Wi-Fi export) | €14.00 | €2.80 |
| **Landed cost** | **€43.50** | **€24.00** |
| Net price after channel (direct €58 ex-VAT / distributor €38) | €58 | €38 |
| **Gross margin** | **€14.50 (25%)** | **€14.00 (37%)** |

At 1k, certification eats the margin. Sell the first batch direct (crowdfunding, own shop) so you keep the full €58. Cut the cost by doing the pilot with USB-only export and no Wi-Fi, which takes EN 18031 out of scope.

### Go-to-market
**First 100 customers:**
- Home Assistant and ioBroker forums (German-language communities are large and very hardware-friendly). Post a teardown-style "what does your doorbell send?" thread with real captures.
- Repair-café networks: offer 20 free units to café coordinators in exchange for a monthly "what we found" report. That becomes your content.
- Maker fairs and the hacker-camp circuit in DE/NL, with a demo table: "bring your remote".
- Two vocational schools: a free class set for one semester in exchange for a testimonial and a lesson plan.

**Scale channels:** European electronics/maker distributors, education resellers, Tindie/Kickstarter-style shops for international reach, YouTube electronics channels (send units, no paid placements needed at first).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test (below); works-like on the CMT-RF_EB + AtomS3; protocol library v0 (10 encoders); 30 hobbyists testing firmware |
| Q2 | Custom PCB (receiver + ESP32-S3 + screen), housing, EVT 30 units; RF pre-scan; crowdfunding page live |
| Q3 | DVT, RED/EMC testing, pilot 300 units to backers; class-set lesson sheets |
| Q4 | 1,000 units; distributor listing; firmware v1 with the export bridge |

**Team:** 1 RF/embedded engineer (part-time OK, it's a small design), 1 firmware/UI developer, and the founder on community and sales. Buy in mechanical design and compliance.

**Funding to the first 1,000 units (estimates):** NRE €30k (RF board €10k, housing tooling €8k, firmware €12k) + certification €14k + 1,000 units landed at ~€30k (excluding the cert line) + 9 months of lean costs €40k ≈ **€115k**. Subtract crowdfunding pre-orders (400 × €59 ≈ €24k) → **~€90–95k** to raise. Route: crowdfunding first (it's also the kill test), then a maker-community angel or founder savings. This is too small for VC and that's fine.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** one receiver chip with good sensitivity on both 433 and 868 bands; sweep speed | Measure in week 3 with the HopeRF eval board; if wideband loses >6 dB, use switched matching networks; sweep in coarse steps then zoom |
| **Technical:** protocol guessing is a long tail | Ship with the 10 most common encoders; show raw timing for the rest; let the community add decoders (open protocol file format) |
| **Market:** "why not just buy the multi-tool?" | Price, legality, simplicity and school-safety. If the kill test fails, pivot to the class-set/education product |
| **Regulatory:** misuse perception | Receive-only hardware (no PA, no TX path on the PCB); rolling codes not decoded; clear statement in the manual |
| **Regulatory:** if you adapt rtl_433 decoders (GPL-2.0), the firmware must be GPL | Decide on day one: open firmware (good for this community) or write decoders from datasheets |
| **Supply:** CMT2219B single-source (HopeRF) | Lay out the footprint so a CMT2300A (transceiver, used RX-only with the PA unpopulated) or another vendor's receiver can drop in; keep 6 months of chip stock |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF CMT2219B receiver | https://www.gongbans.com/db/hoperf-cmt2219b.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2219B) | The receiver: OOK/(G)FSK, 127–1020 MHz, SPI, FIFO, RSSI | schematic, PCB, demo code, datasheet (marked preliminary) | MIT (HopeRF Product_Portfolio repo) |
| HopeRF CMT-RF_EB evaluation board | https://www.gongbans.com/db/hoperf-cmt-rf-eb.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/Tools_Kit) | STM32 base board + demo projects, RFPDK config tool, app notes for 1527/1920 encoder pairs (useful for the protocol library) | schematic, firmware | MIT |
| M5Stack AtomS3 (C123) | https://www.gongbans.com/db/m5stack-atoms3.html | ESP32-S3 with a small screen for the works-like UI | enclosure/structure only (no main-board electronics) | Buy as a dev kit; design your own S3 board for production |

### Block diagram
```
[SMA whip antenna] -> [433/868 matching / SAW] -> [CMT2219B RX] --SPI + DOUT(GPIO)--> [ESP32-S3]
                                                                                   |-> [1.5" TFT + 3 buttons]
[USB-C] -> [Li-ion charger] -> [500 mAh cell] -> [3.3 V LDO]                       |-> [USB / Wi-Fi export: JSON]
        (NO transmitter, NO PA on the board)                                        `-> [protocol library in flash]
```
**Engineering gap:** the receiver reference design and demo code exist. What's missing: a front end that covers both bands without losing sensitivity, a fast RSSI sweep routine, raw OOK capture via the chip's direct data output with µs timestamps on the ESP32, the decoder library, and a UI that a repair-café volunteer understands. The firmware is ~70% of the work.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| CMT2219B | €0.70–1.00 | **Sole-source (HopeRF)**; datasheet preliminary, so confirm the production status |
| 433 + 868 SAW filters / matching, RF switch | €1.20 | Murata/other SAWs; 6–10 week lead time on some |
| ESP32-S3 module (pre-certified) | €2.80 | Multi-source modules |
| 1.3–1.5" IPS TFT | €2.50 | Many sources |
| Li-ion 500–800 mAh + charger IC + protection | €2.60 | UN 38.3 report from the cell supplier |
| SMA connector + whip antenna | €1.10 | |
| PCB 4-layer, passives, buttons, USB-C | €3.50 | 4 layers help RF |
| Enclosure + button caps | €3.80 | Tooling ~€6–9k |

### Firmware/software starting point
- HopeRF demo code for the CMT2219B and the CMT-RF_EB projects (in the GitHub folders above). Use the RFPDK tool to generate register settings per band and modulation.
- ESP-IDF or Arduino-ESP32 for the S3; LVGL for the UI.
- **rtl_433** (github.com/merbanan/rtl_433) is the reference for protocol formats and timings. It's GPL-2.0, so either open-source your firmware or use it only as a reference.
- Universal Radio Hacker (github.com/jopohl/urh) is useful on your bench to verify captures.
- Export format: a JSON with frequency, modulation, pulse timings and decoded bits. Search "ESPHome remote_receiver" for the downstream format hobbyists want.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Kill test running (see below). AtomS3 + CMT-RF_EB capture a 433 MHz EV1527-class remote and show its timing on screen |
| 3–5 | Works-like | Sweep + capture + identify for 10 encoders; sensitivity measured on both bands vs datasheet (within 6 dB); 30 testers' captures collected |
| 6–8 | Looks-like + EVT | Custom PCB (S3 + receiver + screen + charger), printed housing, 30 EVT units; 6-hour battery life in capture mode; drop test |
| 9–10 | DVT + pre-compliance | Receiver blocking/spurious emissions pre-scan (EN 300 220 receiver parameters), EMC pre-scan, battery charging safety; firmware signed update path |
| 11–12 | Pilot batch | 50 units to early backers and 2 schools; <5% returns; decoder hit-rate report from real homes (target: identify ≥70% of fixed-code devices brought in) |

### Certification checklist (EU)
- **CE under RED (2014/53/EU):** receivers are in scope. Expect EN 300 220-1/-2 receiver requirements (receiver category, blocking), EN 301 489-1/-3 (EMC), EN 62368-1 (safety; low-voltage, so mostly the battery), EN 62311 (trivial with no TX). If you add Wi-Fi export: EN 300 328 + the ESP32 module report. Est. **€6–10k**.
- **RED delegated act (cybersecurity), EN 18031-1:** applies only if the device can talk to the internet (Wi-Fi). USB-only export keeps it out of scope. With Wi-Fi: est. **€5–10k** extra.
- **CRA:** products with digital elements, with reporting obligations from 11 Sept 2026 and full application from 11 Dec 2027. Plan signed firmware updates, an SBOM and a vulnerability contact from day one.
- **RoHS, REACH (SVHC declaration from suppliers), WEEE** registration in every country you sell to (DE: stiftung ear), packaging registration (DE: LUCID).
- **Battery Regulation (EU) 2023/1542:** portable Li-ion, so labelling, a user-replaceable design requirement (applies from Feb 2027; design for it now), take-back. Cell UN 38.3 from the supplier.
- **GDPR:** not really in play; captures are radio frames, not personal data. Don't build a cloud.
- **Not a toy:** don't market to under-14s. For the class set, sell to schools as teaching equipment.
- **Total certification budget estimate: €10–20k.**

### Validation toolkit
- **Kill question:** Will 300 people pre-order a receive-only tool when transmit-capable multi-tools exist?
- **Cheapest experiment (~€400):** a landing page with a 60-second video of the AtomS3 + eval board identifying a doorbell, posted in 3 German/Dutch home-automation forums and sent to 30 repair-café coordinators. Take €10 refundable deposits.
- **5-question interview (hobbyist/repairer):** 1) The last time a radio remote or sensor puzzled you, what did you do? 2) What tools do you own for this today (SDR, multi-tool, nothing)? 3) Which matters more: receive-only/legal, or everything a multi-tool does? 4) What would it need to show to save you 30 minutes? 5) €69: buy now, wait for reviews, or never?
- **Landing page headline:** "See what your remote is saying." Bullets: "433 and 868 MHz: frequency, modulation and timing on a pocket screen." / "Identifies common remotes, sockets and sensors, and exports them to your smart home." / "Receive-only by design. Legal, simple, classroom-safe."
- **Pass threshold:** 300 deposits in 6 weeks, **or** 3 schools signing a letter of intent for class sets.

### First production checklist
- **Samples:** 5 golden samples with a measured sensitivity at 433.92 and 868.3 MHz; keep one sealed as the reference.
- **DFM review:** antenna connector strain relief, screen gluing, battery bay; RF ground and shielding can.
- **MOQ talk:** CMT2219B reels (ask HopeRF's distributor for small-reel pricing), screens (MOQ 1k is typical), SAW filters (lead time).
- **QC/AQL:** AQL II 1.0 (major) / 2.5 (minor); 100% functional test with a calibrated signal generator at −100 dBm on both bands; 100% charge test; firmware version check.
- **Packaging:** small box, antenna, card with QR to the docs; Li-ion label (UN 3481, packed with/in equipment).
- **Incoterms:** FOB Shenzhen for the first batch with your own forwarder; DDP quotes once you have volume; insist on the battery MSDS + UN 38.3 summary.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver](/db/hoperf-cmt2219b.html) (OOK/(G)FSK/(G)MSK sub-GHz receiver (open schematic + PCB)); [HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003)](/db/hoperf-cmt-rf-eb.html) (radio evaluation base board + demo code). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack AtomS3 (C123)](/db/m5stack-atoms3.html) (ESP32-S3 with screen for the UI). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123) — for a Sub-GHz Remote Analyser

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Sub-GHz Remote Analyser: A receive-only handheld that shows what an unknown 433/868 MHz remote, sensor or doorbell is sending — frequency, modulation, timing, protocol guess — for repair technicians, home-automation tinkerers and radio students. The design is built around your HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123).
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
主题：样品订购及批量报价 — HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123) — 用于Sub-GHz Remote Analyser

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sub-GHz Remote Analyser：A receive-only handheld that shows what an unknown 433/868 MHz remote, sensor or doorbell is sending — frequency, modulation, timing, protocol guess — for repair technicians, home-automation tinkerers and radio students。产品设计基于贵司的HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123)。
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
Subject: PCBA quote from open design files — Sub-GHz Remote Analyser, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Sub-GHz Remote Analyser: A receive-only handheld that shows what an unknown 433/868 MHz remote, sensor or doorbell is sending — frequency, modulation, timing, protocol guess — for repair technicians, home-automation tinkerers and radio students. The design starts from published open-hardware files (HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Sub-GHz Remote Analyser，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sub-GHz Remote Analyser：A receive-only handheld that shows what an unknown 433/868 MHz remote, sensor or doorbell is sending — frequency, modulation, timing, protocol guess — for repair technicians, home-automation tinkerers and radio students。设计基于已公开的开源硬件文件（HopeRF CMT2219B OOK/(G)FSK/(G)MSK receiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack AtomS3 (C123)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order the HopeRF CMT-RF_EB kit (or a CMT2219B sample module), an M5Stack AtomS3 and three cheap 433 MHz remotes/sockets from a DIY store. Get raw OOK timing on screen.
2. Write the landing page and shoot the 60-second "what does my doorbell send?" video. Post it in two home-automation forums and email repair-café coordinators with the deposit link.
3. Decide the firmware licence (GPL with rtl_433 heritage vs your own decoders) before writing decoder code, because it's hard to undo.

Want help sourcing or building this? Talk to us via www.gongbans.com.
