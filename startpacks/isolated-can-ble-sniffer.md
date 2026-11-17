# Isolated CAN-to-Bluetooth Service Dongle — Founder Start Pack

> A pocket dongle that plugs into the CAN bus of home batteries, PV inverters, heat pumps and industrial controllers, galvanically isolated, and streams frames to a phone app over Bluetooth — no laptop, no ground-loop risk.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Home batteries and hybrid inverters talk to each other over CAN. When "BMS communication fail" shows up, the installer drives out with a laptop, a non-isolated USB-CAN adapter and vendor PC tools. Wrong adapter, wrong ground, and they've blown a port or upset a live system. Many installers simply swap parts until it works.
- **Customer:** Solar and battery installers, heat-pump service technicians, industrial maintenance staff. They pay themselves (tool budget) or their company buys a set for each van. **Explicitly not for road vehicles** — no OBD connector, no car apps.
- **Product:** A rugged dongle: isolated CAN transceiver, isolated bus-side supply, a ready CAN-to-BLE 5.3 bridge module, and a phone app with frame log, filters, decoding profiles for common home-battery protocols, and CSV export. Read-only by default; transmit only in a guarded expert mode.
- **Why now:** Millions of home batteries were installed in DE, NL, IT, AT and BE since 2022, and the service wave is starting as warranties and firmware updates kick in. A ready CAN-to-BLE module and single-chip isolated CAN transceivers make a phone tool cheap.
- **The ask:** ~€85k to certification, the app and 1,000 dongles; fundable through installer pre-orders and one wholesaler.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 50 installers on a solar-installer forum pre-order at €129 if the app decodes the 5 most common home-battery protocols on day one?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Solar/battery installers, heat-pump service technicians, industrial maintenance staff. (Explicitly not for road vehicles.).

**The problem as the pack states it:** Home batteries and hybrid inverters talk to each other over CAN. When "BMS communication fail" shows up, the installer drives out with a laptop, a non-isolated USB-CAN adapter and vendor PC tools. Wrong adapter, wrong ground, and they've blown a port or upset a live system. Many installers simply swap parts until it works.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **DIY Solar Power forum** · https://diysolarforum.com/ — home battery and second-life cell builders.
- **Photovoltaikforum (DE)** · https://www.photovoltaikforum.com/ — German PV, battery, heat-pump and dynamic-tariff owners.
- **r/solar** · https://www.reddit.com/r/solar/ — PV owners.
- **r/HVAC** · https://www.reddit.com/r/HVAC/ — HVAC technicians (mostly US); installer mindset.
- **PLCtalk forum** · https://www.plctalk.net/ — industrial automation technicians and integrators.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€119–159 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how solar/battery installers, heat-pump service technicians, industrial maintenance staff deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. When did you last need to see what was on the CAN bus of a battery, inverter or heat pump on site, what did you connect with, and what went wrong?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A pocket dongle that plugs into the CAN bus of home batteries, PV inverters, heat pumps and industrial controllers, galvanically isolated, and streams frames to a phone app over Bluetooth — no laptop, no ground-loop risk. On a scale of one to ten, how likely would you be to buy that at €119–159 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Isolated CAN-to-Bluetooth Service Dongle: would you pay €119–159 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Isolated CAN-to-Bluetooth Service Dongle: A pocket dongle that plugs into the CAN bus of home batteries, PV inverters, heat pumps and industrial controllers, galvanically isolated, and streams frames to a phone app over Bluetooth — no laptop, no ground-loop risk. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €119–159 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A battery installer does 2–5 service calls a week on systems from a handful of battery and inverter brands. The CAN link between battery and inverter is the #1 commissioning headache (wrong baud rate, wrong protocol selection, termination, cable pinout). Vendor apps show "communication error" and nothing else. Installers want to *see* whether frames are flowing and what the BMS reports, on the phone they already carry.

- **Who pays:** installer companies (3–30 technicians) — a €129 tool that saves one extra site visit pays for itself on day one. Also service departments of battery/inverter brands and wholesalers bundling it.
- **Who uses:** the technician in the cellar or garage, often without good light or a table — so no laptop.
- **Guardrail:** this is a diagnostics tool for stationary energy and industrial equipment. Writing to BMS buses can damage batteries; default is listen-only.

### Market size (estimates — check)

- **TAM:** Europe has several thousand PV/battery installer companies — Germany alone has many thousands of firms installing PV (estimate; verify with trade-association data) — plus heat-pump technicians and industrial maintenance staff. Assume 60k technicians across EU who touch CAN-connected equipment; at €129 = **~€8M** hardware, plus a decoding-profile subscription.
- **SAM:** technicians in DE, NL, AT, BE, IT doing home-battery work: ~20k → **€2.6M** hardware + software.
- **SOM (3 yrs):** 3–6k dongles (5–10% of SAM technicians plus brand service teams) → **€0.4–0.8M** hardware + €5–10/month pro-app subscriptions.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / swap parts | Common, expensive | Second visits, frustrated customers |
| Non-isolated USB-CAN adapters (CANalyst-II-type, Waveshare) + PC tools (PCAN-View, SavvyCAN, cangaroo) | Cheap, flexible | Laptop needed; non-isolated adapters can be blown; raw frames, no battery decoding |
| Isolated professional adapters (PEAK PCAN-USB opto, Kvaser) | Excellent, trusted | €200–400 + laptop; engineer tools, not installer tools |
| Vendor service apps and dongles (battery/inverter brands' own tools, SolarAssistant-type monitoring) | Brand-specific, often free | One brand each; don't show the bus between two brands — exactly where the problem is |
| DIY ESP32 + CAN transceiver | Cheap, forum projects | No isolation, no app, no support |

**Wedge:** the only *isolated, phone-first* CAN tool with decoding for the 5 most common home-battery protocols out of the box. "Is the battery talking to the inverter, and what is it saying?" — answered in 30 seconds.

### Product & value proposition

- **Hardware:** 80 × 40 mm dongle, rubber bumper, CAN-H/CAN-L/GND via a short pigtail with RJ45 adapter plus screw-terminal and test-clip adapters; switchable 120 Ω termination; bus-side isolated with a 1 W isolated DC-DC; USB-C powered (power bank) or small internal primary-cell option.
- **App (iOS/Android):** live frame log, baud-rate auto-detect (listen-only), filters, decoding profiles (JSON, DBC-like) for common battery/inverter protocols, health summary (SoC, voltages, alarms if decodable), CSV/PDF export for the service report.
- **Expert mode:** transmit enabled only after a deliberate unlock + warning; logged.
- **Pricing (estimates):** dongle €119–159; free app with raw log and 2 profiles; Pro €6/month or €59/year with all profiles, PDF service report, team sharing. Van kit (dongle + adapters + case) €179.

### Unit economics (estimates, EUR per dongle)

| Item | 1k | 5k |
|---|---|---|
| HLK-B42 CAN-to-BLE module | 5.5 | 4.3 |
| Isolated CAN transceiver (CMT1042-class) | 1.6 | 1.2 |
| 1 W isolated DC-DC (B0505LS-1WR3 class) | 1.2 | 0.9 |
| Termination switch, TVS on CAN lines, USB-C, LEDs, passives | 1.5 | 1.1 |
| PCB | 0.8 | 0.5 |
| Assembly + test (CAN loopback through the barrier, BLE link, hi-pot sample) | 2.2 | 1.4 |
| Enclosure + rubber bumper | 2.8 | 1.8 |
| Pigtail + RJ45 adapter + clip leads | 3.0 | 2.2 |
| Packaging | 1.0 | 0.6 |
| Freight + duty | 1.0 | 0.6 |
| Certification amortised (€12k) | 12.0 | 2.4 |
| **Landed cost** | **32.6** | **17.0** |
| Net price direct (€139 incl. VAT → €117 ex VAT) less €6 fulfilment | 111 | 111 |
| Wholesaler margin if via electrical wholesale (30%) | −35 | −35 |
| **Gross margin direct** | **€78 (70%)** | **€94 (85%)** |
| **Gross margin via wholesale** | **€43** | **€59** |

The real cost is the app and the protocol profiles (engineering + legal care), not the hardware.

### Go-to-market

**First 100 customers:** photovoltaikforum.com (huge German PV/battery community, installers active), r/solar and r/diysolar-adjacent forums (careful: DIY users aren't your core but they evangelise), installer WhatsApp/Telegram groups, regional installer meetups and wholesaler counter days, Intersolar/The smarter E Europe in Munich (pre-book a walk-around, not a booth).

**Then scale:** electrical/PV wholesalers (they sell tools to installers), battery brands' service departments (white-label profile for their protocol), training providers for battery-installer certification courses (dongle in the training kit), heat-pump service networks.

### 12-month plan

- **Q1:** prototype on modules; app MVP (log + 1 profile); 10 installer ride-alongs; pre-order page (kill question).
- **Q2:** rev A hardware, 5 decoding profiles, beta with 30 installers.
- **Q3:** certification, 1,000-unit run, app store launch, wholesaler pilot in one country.
- **Q4:** Pro subscription, heat-pump profiles, second country.

**Team:** founder (installer background or energy-sector service), mobile app developer (full-time — the app is the product), embedded engineer (part-time), protocol researcher (part-time), Shenzhen partner for PCBA and cable assemblies.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €21k + tooling €6k + certification €12k + app dev 6 months €40k + prototypes/beta units €4k + marketing/fair visits €4k = **≈€87k**. 50 pre-orders at €129 = €6.5k (proof, not funding); wholesaler pre-order of 300 units ≈ €25k. Rest: angel from energy-services, or a regional innovation grant for energy-transition tools.

### Top risks

| Risk | Mitigation |
|---|---|
| **Safety:** user transmits to a BMS and damages a battery | Listen-only default (CAN controller in silent mode); expert mode gated, logged, with warnings; clear terms of use |
| **Legal/IP:** decoding proprietary protocols | Use publicly documented protocols first (several battery brands publish their inverter CAN protocol for integrators); clean-room for others; never ship vendor tools or keys |
| **Technical:** HLK-B42 bridge throughput/BLE latency on busy buses at 500 kbps | Measure frame drop at 250/500 kbps; on-device filtering; if insufficient, move to an MCU + BLE module with your own buffering |
| **Market:** brands bundle their own free dongles | Multi-brand is the wedge; partner with smaller brands lacking tools |
| **Supply:** HLK-B42 is single-source with design files via maker | Keep a fallback design on an MCU with integrated CAN controller + BLE (search for suitable SoCs) |
| **Scope creep into vehicles** | No OBD connector, no vehicle profiles, product name and docs say "stationary energy and industrial equipment" |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-B42 CAN-to-Bluetooth (BLE 5.3) module | https://www.gongbans.com/db/hilink-b42.html | Ready CAN-to-BLE bridge (master/slave, coded PHY), UART config | Datasheet public, design files via maker (no open schematics) | Buy as module |
| HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver | https://www.gongbans.com/db/hoperf-cmt10xx.html | Galvanic isolation between bus and logic in one chip | Schematic + PCB — HopeRF MIT GitHub folder: https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Isolator/SCH_PCB/CMT1042 | MIT licence for repo content |
| Hi-Link B_LS-1WR3 series 1 W isolated DC-DC (B0505LS-1WR3) | https://www.gongbans.com/db/hilink-b-ls-1wr3-series.html | Powers the bus-side of the isolated transceiver | Datasheet public, design files via maker (no open schematics) | Buy as module |

### Block diagram

```
CAN-H / CAN-L / GND (bus side, isolated domain)
   │ TVS + switchable 120 Ω
CMT10xx isolated CAN transceiver  ◄── bus-side 5 V ◄── B0505LS-1WR3 (1 W isolated DC-DC)
   ║ isolation barrier ║                                      ▲
   │ TXD/RXD (logic side)                                     │
HLK-B42 CAN-to-BLE module (CAN controller + BLE 5.3) ◄── 5 V/3.3 V from USB-C / battery
   │ BLE
Phone app: log, filters, decoding profiles, CSV/PDF export, guarded transmit
```

**Engineering gap:** confirm the HLK-B42's CAN interface (does it need an external transceiver — the design assumes TXD/RXD to an external isolated transceiver; verify in the datasheet), the listen-only/silent mode, BLE throughput, and the app with protocol profiles.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| HLK-B42 | €4.5–6 | **Single source**; check firmware version + config commands |
| CMT1042 or CMT1050/1052 | €1.2–1.8 | Pick variant for 3.3 V/5 V logic and speed |
| B0505LS-1WR3 | €1–1.3 | Unregulated — check transceiver supply tolerance; standard SIP footprint, alternatives exist |
| CAN TVS diode array | €0.2 | |
| Termination DIP switch | €0.15 | |
| USB-C + LiPo-free power path | €0.5 | Avoid Li-ion to stay simple; power bank via USB-C |
| Enclosure + bumper | €2–3 | |
| Pigtail, RJ45 coupler, clip leads | €2–3 | Cable assembly supplier — 4–6 week lead |

### Firmware/software starting point

- Dongle side: mostly configuration of the HLK-B42 per its datasheet (UART AT-style commands — verify).
- App: native or Flutter/React Native with a BLE library; frame decoding with a JSON/DBC-like profile format. Look at open DBC parsers (search "DBC parser" for your language) and **SavvyCAN** / **cangaroo** (open-source desktop CAN tools) for UX ideas.
- **python-can** for bench testing and generating test traffic from a laptop + isolated adapter.
- Protocol references: battery/inverter makers that publish CAN protocols for integrators — search per brand; community projects like DIY BMS-to-inverter bridges on GitHub show which protocols are common (check licences; don't copy proprietary documents).

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 installer interviews + 3 ride-alongs; pre-order page posted in the PV forum | ≥50 pre-orders at €129 (or deposits of €20) promised; top-5 protocols named by installers |
| 3–5 | **Works-like** — HLK-B42 + CMT10xx + DC-DC on a protoboard; app shows live frames from a real battery-inverter pair | Zero frame loss at 500 kbps for 10 min on a real system; listen-only confirmed (no ACKs sent) |
| 6–8 | **Looks-like + EVT** — rev A PCB, enclosure, 3 decoding profiles, 20 dongles to beta installers | 20 installers use it on ≥3 real calls each; "found the problem faster" in ≥50% |
| 9–10 | **DVT + pre-compliance** — hi-pot at claimed isolation, ESD on CAN pins, BLE pre-scan, EN 18031 checklist, app security review | Pass; no BLE pairing weaknesses; expert-mode lock reviewed |
| 11–12 | **Pilot batch** — 50 paid units, 5 profiles, PDF service report | <3% returns; ≥10 paying Pro subscribers; one wholesaler LOI |

### Certification checklist (EU)

- **CE — RED** (BLE): EN 300 328, EN 301 489-1/-17, EN 62368-1, EN 62311/62479. Module test reports help; the product still needs its own assessment. Estimate €6–9k.
- **Isolation claim:** test to the rating you print (functional isolation vs basic); don't claim "safety isolation" unless certified under EN 62368-1 for it.
- **EN 18031-1** (RED cybersecurity): BLE to a phone app that may sync to a cloud → likely in scope; -3 if payment/financial (no). Budget €2–4k. Secure pairing, no default static PIN.
- **CRA:** the dongle *and* the app are products with digital elements; reporting from 11 Sep 2026, full from 11 Dec 2027. SBOM, updates (dongle firmware via app), vulnerability contact.
- **RoHS, REACH, WEEE**, packaging EPR. No Li-ion inside → Battery Regulation avoided (if you add one later: labelling, removability, UN 38.3).
- **GDPR:** service reports may include customer addresses → app stores locally by default; if cloud sync, EU hosting and a DPA for installer companies.
- Not automotive: no UN R155/R156 issues because it's not for vehicles — state the intended use clearly.
- **Total estimate:** €10–15k.

### Validation toolkit

- **Kill question:** Will 50 installers on a solar-installer forum pre-order at €129 if the app decodes the 5 most common home-battery protocols on day one? Cheapest experiment: a forum post + 60-second video of a mock-up app showing a real decoded battery frame log (record it with a laptop tool), linking to a pre-order page.
- **Interview script (5):**
  1. When did you last have a battery–inverter communication fault? How long did it take to fix, and how?
  2. What tools do you carry for it today? Laptop? Which adapter?
  3. Which battery and inverter brands make up 80% of your installs?
  4. Have you ever damaged equipment with a diagnostic tool or wrong wiring?
  5. Would you pay €129 for the dongle plus €6/month for decoding — or should your company buy it per van?
- **Landing page:** Headline: "See what the battery tells the inverter — on your phone." Bullets: "Galvanically isolated: no ground loops, no blown ports." / "Decodes the most common home-battery protocols; read-only by default." / "Service report as PDF in one tap."
- **Pass:** 50 pre-orders (or €20 deposits) in 4 weeks, or one installer company ordering 10+ for its vans.

### First production checklist

- Samples: HLK-B42 from two lots with identical firmware; transceiver and DC-DC samples hi-pot tested.
- Golden sample: isolation tested, CAN at 125/250/500 kbps verified, enclosure drop-tested from 1.5 m.
- DFM: creepage slot under the barrier; strain relief on the pigtail; rubber bumper fit.
- MOQ: cable assemblies (often 500–1,000), modules per tray, enclosure 1k shots.
- QC/AQL: 100% CAN loopback through barrier + BLE connect test; hi-pot per sample plan; AQL 1.0/2.5.
- Packaging: dongle, adapters, pouch, quick start; "Not for road vehicles" on box and manual.
- Incoterms: FOB Shenzhen; DDP into an EU 3PL for webshop orders.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and HopeRF (华普微)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-B42 CAN-to-Bluetooth (BLE 5.3) module](/db/hilink-b42.html) (CAN-to-Bluetooth (BLE 5.3) bridge module); [Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP](/db/hilink-b-ls-1wr3-series.html) (1 W isolated DC-DC for the bus side). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver](/db/hoperf-cmt10xx.html) (isolated CAN transceiver (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Moko Technology** (深圳市摩可智能硬件有限公司) · mokosmart.com — BLE / WiFi / NB-IoT module OEM: BLE 5.0 beacon; NB-IoT tracker; WiFi module; CE/FCC/RoHS OEM/ODM. *(BLE modules and beacons)*
- **Minew Technologies** (深圳市敏芯微电子技术有限公司) · minewtech.com — BLE beacon / indoor positioning: BLE beacon; iBeacon; AoA/AoD positioning; CE/FCC modules OEM. *(BLE modules and beacons)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) websites)

```email
Subject: Sample order and volume pricing — HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver — for a Isolated CAN-to-Bluetooth Service Dongle

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Isolated CAN-to-Bluetooth Service Dongle: A pocket dongle that plugs into the CAN bus of home batteries, PV inverters, heat pumps and industrial controllers, galvanically isolated, and streams frames to a phone app over Bluetooth — no laptop, no ground-loop risk. The design is built around your HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver.
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
主题：样品订购及批量报价 — HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver — 用于Isolated CAN-to-Bluetooth Service Dongle

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Isolated CAN-to-Bluetooth Service Dongle：A pocket dongle that plugs into the CAN bus of home batteries, PV inverters, heat pumps and industrial controllers, galvanically isolated, and streams frames to a phone app over Bluetooth — no laptop, no ground-loop risk。产品设计基于贵司的HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver。
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
Subject: PCBA quote from open design files — Isolated CAN-to-Bluetooth Service Dongle, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Isolated CAN-to-Bluetooth Service Dongle: A pocket dongle that plugs into the CAN bus of home batteries, PV inverters, heat pumps and industrial controllers, galvanically isolated, and streams frames to a phone app over Bluetooth — no laptop, no ground-loop risk. The design starts from published open-hardware files (HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Isolated CAN-to-Bluetooth Service Dongle，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Isolated CAN-to-Bluetooth Service Dongle：A pocket dongle that plugs into the CAN bus of home batteries, PV inverters, heat pumps and industrial controllers, galvanically isolated, and streams frames to a phone app over Bluetooth — no laptop, no ground-loop risk。设计基于已公开的开源硬件文件（HLK-B42 CAN-to-Bluetooth (BLE 5.3) module, Hi-Link B_LS-1WR3 series (B0505LS-1WR3 etc.) 1 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT1042 / CMT1050 / CMT1052 isolated CAN transceiver；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Join two PV-installer forums/groups and ask: "Which battery–inverter CAN issues cost you a second visit?" Collect the top-5 protocol list.
2. Order HLK-B42, CMT1042/1050 samples and a B0505LS-1WR3; plus one isolated USB-CAN adapter as your reference tool.
3. Do a ride-along with one installer on a service call; time how long the CAN fault-finding takes today.

Want help sourcing or building this? Talk to us via www.gongbans.com.
