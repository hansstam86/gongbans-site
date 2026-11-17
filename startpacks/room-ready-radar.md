# Room-Ready Radar for Housekeeping — Founder Start Pack

> A small ceiling sensor per hotel room that tells housekeeping "guest is out" right now, so staff stop knocking on occupied rooms, and the energy system can set back the heating. Radar only: no camera, no microphone.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Housekeeping wastes trips. Staff knock, the guest is asleep or working, the room gets skipped, the cart comes back later, and the afternoon shift overruns. Meanwhile heating and cooling run at full comfort in rooms that are empty for 8 hours. Key-card pockets were meant to fix the energy side, but guests leave a second card in the slot.
- **Customer:** Independent and mid-size hotels (40–250 rooms), aparthotels and serviced apartments, student housing operators in EU cities. The general manager or operations director pays; housekeeping supervisors and room attendants use it.
- **Product:** A ceiling unit per room: Hi-Link LD2460 24 GHz multi-target status radar (moving / subtle / stationary people, per Hi-Link, aimed at homes, offices and hotels), a HopeRF RFM95 LoRa radio to a building gateway (no dependence on guest Wi-Fi), and a Hi-Link 10 W isolated AC-DC module. States: occupied / vacant / probably asleep, with 5-minute confirmation. Housekeeping board on a tablet, webhook for the property-management system (PMS) and the room thermostat.
- **Why now:** Staff shortages make every wasted housekeeping trip expensive; many hotels moved to "cleaning on request" and need to know when a room is free to service. Cameras in rooms are out (privacy), and multi-target status radar modules are now made specifically for this.
- **The ask:** About €130–170k (estimate) to the first 1,000 rooms. Hotels buy only after a pilot in their own building, so budget for 3 paid pilots before volume.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will one 60-room hotel run a 20-room pilot and report fewer than 2 wrong 'vacant' calls per week? Hotel managers only buy after a pilot in their own building.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Independent and mid-size hotels, aparthotels, student housing in EU cities.

**The problem as the pack states it:** Housekeeping wastes trips. Staff knock, the guest is asleep or working, the room gets skipped, the cart comes back later, and the afternoon shift overruns. Meanwhile heating and cooling run at full comfort in rooms that are empty for 8 hours. Key-card pockets were meant to fix the energy side, but guests leave a second card in the slot.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **HOTREC** · https://www.hotrec.eu/ — European umbrella of national hotel and restaurant associations.
- **DEHOGA (DE)** · https://www.dehoga-bundesverband.de/ — German hotel and restaurant association.
- **UKHospitality** · https://www.ukhospitality.org.uk/ — UK hospitality trade body.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€89–129 per room + optional software (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how independent and mid-size hotels, aparthotels, student housing in EU cities deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How does housekeeping know today whether a guest is in the room, and how many knocks on occupied rooms or wasted trips happen in a normal day?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A small ceiling sensor per hotel room that tells housekeeping 'guest is out' right now — so staff stop knocking on occupied rooms — and the energy system can set back heating. Radar, no camera, no microphone. On a scale of one to ten, how likely would you be to buy that at €89–129 per room + optional software (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Room-Ready Radar for Housekeeping: would you pay €89–129 per room + optional software (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Room-Ready Radar for Housekeeping: A small ceiling sensor per hotel room that tells housekeeping 'guest is out' right now — so staff stop knocking on occupied rooms — and the energy system can set back heating. Radar, no camera, no microphone. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €89–129 per room + optional software (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The value has two halves. **Housekeeping productivity:** fewer wasted trips and faster turnaround on stay-overs and early check-ins. **Energy:** setting back HVAC in vacant rooms. Vendors claim savings of around 10% or more from vacancy setback; treat that as a claim and measure it in your pilot.

**Buyer:** the GM or operations director of an independent or small-group hotel. Chains with brand standards buy guest-room management systems (GRMS) through integrators, so don't start there. **Aparthotels and student housing** are attractive too: fewer staff per room, more need for "is it free?".

**Users:** housekeeping supervisors (the tablet board) and attendants (the phone view). If attendants don't trust it after week one, the product is dead. Accuracy is the product.

### Market size (estimates)
- Hotel rooms in the EU: roughly 6–7 million (Eurostat-order figure; check current data). Independent and small-group hotels hold a large share, say ~50% → **~3.2 M rooms**.
- **TAM:** 3.2 M × €109 ≈ **€350 M** hardware, plus software (€1.50/room/month ≈ €58 M/yr).
- **SAM:** DE, AT, CH, NL, BE, Nordics, Spain/Portugal city hotels without a GRMS, 40+ rooms: ~15% → **~480k rooms ≈ €52 M**.
- **SOM (3 years):** 1.5% of SAM → **~7,000 rooms ≈ €0.76 M hardware + ~€125k/yr software**.

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| Guest-room management systems (GRMS; lighting/HVAC/door-contact systems from big building-control vendors, some with guest presence detection) | €300–1,000+ per room installed | Integrator project, usually at renovation; overkill for a 60-room independent |
| KNX/DALI radar presence detectors (e.g. breathing-sensitive detectors sold for hotels) | €150–300 + KNX installation | Needs a KNX building; no housekeeping workflow |
| Key-card energy pockets | €50–150 per room | Bypassed with a second card; says nothing about presence |
| Door hangers / "make up room" buttons | Cheap | Guests forget; no real-time view |
| Wi-Fi association (guest phone on the network) | Software only | Guests leave phones behind or turn Wi-Fi off; privacy-touchy |
| Do nothing (knock and come back) | Staff hours | The problem |

**Wedge:** **battery-free retrofit in a ceiling (fed from a permanent lighting circuit), no Wi-Fi dependence (LoRa), no camera/mic**, a housekeeping board that works on day one without PMS integration, and a per-room price under €130. Install in a day per floor.

### Product & value proposition
- **Sensor unit:** LD2460 radar (24 GHz FMCW; static detection ≥5 m, dynamic ≥6 m; ±60° H / ±45° V; wall or ceiling mount; UART; 5 V, average ≤250 mA per Hi-Link) + a small MCU + RFM95 LoRa (EU868) + HLK-10Mxx isolated AC-DC (85–265 VAC in, 10 W, potted, per Hi-Link; a 10 W supply is oversized for ~1.5 W of load, so a smaller module may do).
- **Critical install detail:** feed it from a **permanent** circuit, not the key-card-switched lighting circuit. Otherwise it dies the moment the guest leaves.
- **States:** occupied (motion or stationary person), vacant (no detection for 5 min after a door event, or 15 min otherwise), "probably asleep" (stationary, night hours). Optional door contact for higher confidence (door opened + no presence afterwards = left).
- **Building gateway:** LoRaWAN gateway(s) per building (1 per ~3–6 floors depending on construction), connected to the hotel LAN or LTE.
- **Software:** housekeeping board (floor plan colour-coded), attendant phone view, PMS webhook (room status), thermostat/BMS hook for setback, daily reports (wasted knocks avoided, vacancy hours).
- **Privacy:** the device only knows "person present / not present" in the room. **But** once linked to a booking, that is personal data about a guest (see GDPR below). Don't claim "no personal data".

**Pricing (estimates):** €109 per room (hardware), €1.50/room/month software, gateway €390 each, pilot package 20 rooms + gateway + 3 months for €2,500 (credited on rollout).

### Unit economics (estimates per room unit, ex-VAT)
| Item | 1k rooms | 5k rooms |
|---|---|---|
| BOM (LD2460, MCU, RFM95, AC-DC module, terminals, PCB, optional door contact) | €30.00 | €24.00 |
| Assembly & test (radar functional, LoRa join, hi-pot on mains side) | €3.00 | €2.20 |
| Enclosure (ceiling mount, radar-transparent, fire-rated plastic) | €2.50 | €1.50 |
| Packaging | €0.80 | €0.50 |
| Freight + duty to EU | €1.00 | €0.70 |
| Certification amortised (~€30k: RED 24 GHz + 868 MHz, LVD/EMC mains, EN 18031) | €30.00 | €6.00 |
| **Landed cost** | **€67.30** | **€34.90** |
| Net price ex-VAT (B2B, prices quoted ex-VAT): direct €109 / via hotel-tech integrator ~€80 | €109 / €80 | €99 / €75 |
| **Gross margin (hardware)** | **€42 (38%) direct / €13 (16%) integrator** | **€64 (65%) / €40 (53%)** |

Software at 1,000 rooms ≈ €18k/yr; it pays for support and the PMS integrations. Installation (electrician, ~20–30 min per room) is the hotel's cost or a partner's line item; don't hide it.

### Go-to-market
**First 100 customers (rooms, then hotels):**
- **Hotel associations and independent-hotel groups** in one city: GMs talk to each other, and one successful pilot spreads.
- **Housekeeping and hotel-operations communities** (executive housekeeper associations, hotel-ops LinkedIn groups, hospitality trade fairs). Pitch the supervisors' pain, not the tech.
- **Aparthotel and student-housing operators:** central operations, many buildings, fewer staff.
- **Hotel-tech marketplaces** of the common PMS vendors: an integration listing makes you findable.

**Scale channels:** hotel-tech integrators and electrical contractors that do hotel renovations, energy-service companies (ESCOs) selling HVAC savings, and PMS/housekeeping-app vendors (white-label sensor).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question: 20-room pilot at one 60-room hotel with works-like units (devkits in ceiling boxes) and a simple board; measure wrong "vacant" calls per week |
| Q2 | Custom PCB + ceiling enclosure; LoRaWAN gateway set-up; housekeeping board v1; 2 more pilot hotels (paid) |
| Q3 | DVT; RED/LVD/EMC/EN 18031 testing; PMS integration #1; thermostat setback integration with one common room-controller brand |
| Q4 | 1,000 rooms installed across ~10 hotels; integrator/ESCO partnership; energy case study |

**Team:** founder (hotel sales; hospitality operations background is a big advantage), 1 embedded engineer (radar state machine, LoRa, mains design), 1 full-stack developer (board, PMS integration), part-time installer partner.

**Funding to the first 1,000 rooms (estimates):** NRE €65k (electronics + mains safety €18k, firmware/state machine €17k, board + PMS integration €22k, enclosure €8k) + certification €30k + 1,000 units landed ex-cert ~€37k + 15 gateways €4k + 9 months lean costs €45k ≈ **€181k**; minus pilot fees and deposits (~€25k) → **~€155k**. Route: paid pilots, hospitality-focused angels, energy-efficiency programmes for SMEs (hotels can often claim efficiency measures).

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: wrong "vacant" while a guest sleeps still or sits in the bathroom** | Status radar for stationary people; "probably asleep" state never shown as vacant at night; door-contact logic; optional bathroom unit for suites; kill threshold <2 wrong calls/week per 20 rooms |
| **Install: sensor on the key-card circuit loses power** | Install guide + electrician checklist: permanent circuit only; heartbeat alarm if a unit goes silent |
| **Privacy/GDPR: presence linked to a booked room is guest personal data** | Guest notice (in-room card + website/booking info), legitimate-interest assessment, minimal retention (states for the day, aggregates after), no per-guest history, DPA with hotels |
| **Staff trust** | Week-one accuracy in the pilot, attendant feedback button ("was wrong"), visible improvement |
| **Market: GRMS vendors at renovations** | Target hotels that aren't renovating; price and install speed; ESCO partnerships |
| **LoRa coverage in concrete hotels** | Gateway site survey; more gateways (cheap) rather than higher power |
| **Supply: LD2460 sole source** | Radar abstraction layer; qualify a second multi-target status radar |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD2460 multi-target status radar | https://www.gongbans.com/db/hilink-ld2460.html | Moving / subtle / stationary people; static ≥5 m, dynamic ≥6 m; ±60° H / ±45° V; wall or ceiling mount; UART; 5 V ≤250 mA (per Hi-Link) | Datasheet public; schematics/files via maker (contact Hi-Link) | Commercial module, no open design files |
| HopeRF RFM95/96/98(W) LoRa module | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | LoRaWAN EU868 uplink to the building gateway, SPI, +20 dBm max, −144 dBm | PCB footprint, demo code, datasheet, 3D model, CE/FCC reports | MIT (HopeRF repo) |
| Hi-Link HLK-10Mxx 10 W isolated AC-DC | https://www.gongbans.com/db/hilink-10mxx.html | Mains supply from a permanent lighting circuit: 85–265 VAC, 3000 VAC isolation, potted, short-circuit protection, CE/RoHS per Hi-Link | Datasheet public; files via maker | Commercial module; keep Hi-Link's safety reports for your file. Consider the smaller 5 W class (HLK-5LSxx) |

### Block diagram
```
[permanent 230 V circuit, NOT key-card switched] -> [HLK-10Mxx / 5 W isolated AC-DC] -> 5 V
                                                                                    |
[LD2460 status radar, ceiling] --UART--> [MCU] --SPI--> [RFM95 LoRa] ~~868 MHz~~> [LoRaWAN gateway per 3–6 floors]
[optional door contact]        --GPIO-->   |  state machine: occupied / vacant / asleep           |
                                           `  heartbeat every 15 min                               v
                                                                         [server: housekeeping board, PMS webhook,
                                                                          thermostat/BMS setback, daily report]
```
**Engineering gap:** a robust room-state machine (radar + door contact + time of day) tuned with real attendant feedback, ceiling mounting and radar zoning that ignores the corridor and the bathroom door, LoRaWAN provisioning at hotel scale (QR per unit → room number), the housekeeping board UX, PMS/thermostat integrations, and mains-safety design in a small ceiling enclosure.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD2460 radar | €12–16 | Biggest line; sole source (Hi-Link); get volume quote |
| RFM95W LoRa module | €3.50 | SX127x-class; multiple sources |
| MCU (Cortex-M0+/M4 or ESP32-C3) | €1.00–2.00 | ESP32 if you want BLE commissioning |
| Isolated AC-DC (5–10 W class) | €2.50–4.00 | Smaller is fine for ~1.5 W load |
| Terminals, fuse, MOV, PCB, antenna | €3.00 | |
| Door contact (reed, wired) | €1.50 | Optional |
| Ceiling enclosure (V-0 plastic) | €2.50 | Fire rating matters in hotels |

### Firmware/software starting point
- **LoRaWAN:** LoRaMac-node (Semtech reference stack) or the MCCI LMIC library (search either), or RadioLib's LoRaWAN support; HopeRF demo code in the GitHub folder.
- **Network server:** a self-hosted open-source LoRaWAN server (e.g. ChirpStack) on the hotel's server or your EU cloud.
- **Radar:** Hi-Link's LD2460 serial protocol (user manual); ask Hi-Link for their PC configuration tool.
- **Board:** any web stack; PMS integration via each vendor's API (search the PMS vendor's developer portal for "room status API").

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question set-up:** one 60-room hotel agrees to a 20-room pilot; baseline: count wasted knocks/skips per day (attendant tally sheet for 1 week) |
| 3–5 | Works-like | Devkit units (LD2460 + MCU + RFM95, USB-powered) in 20 rooms + 1 gateway; board on a tablet. Pass: <2 wrong "vacant" calls per week across 20 rooms by week 5 |
| 6–8 | Looks-like + EVT | Custom mains PCB + ceiling enclosure; 20 units replaced; attendants use the board daily; skipped-room trips down ≥30% vs baseline |
| 9–10 | DVT + pre-compliance | LVD/EMC pre-scan (mains), RED pre-scan (24 GHz + 868 MHz), EN 18031 gap analysis; guest notice and DPIA template reviewed by a privacy lawyer |
| 11–12 | Pilot batch | 50 units across 2–3 hotels; PMS webhook live at 1 hotel; one hotel commits to a full rollout |

### Certification checklist (EU)
- **CE under RED:** 24 GHz radar (EN 300 440), 868 MHz LoRa (EN 300 220-1/-2, duty cycle per sub-band), EMC (EN 301 489-1/-3), safety EN 62368-1 (mains-powered: creepage/clearance, enclosure flammability), RF exposure. As a radio device, LVD safety objectives are covered under RED. Est. **€12–18k**.
- **RED delegated act cybersecurity EN 18031-1 and -2** (connected; processes data about guests' presence). Est. **€6–10k**.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: FUOTA over LoRaWAN is slow, so plan a local update path; SBOM; vulnerability handling; support period ≥5 years (hotels keep things long).
- **RoHS, REACH, WEEE (B2B), packaging registration.**
- **GDPR:** presence in a booked room is personal data about the guest. Legal basis: legitimate interest (service + energy), documented in an LIA; transparent guest information (in-room card, booking confirmation/website); retention short (current state + daily aggregates); no profiling; DPA between you and the hotel. In some countries also check staff-monitoring rules (the board shows attendant activity indirectly).
- **Building/fire:** ceiling devices in hotel rooms must not interfere with fire detection; enclosure material V-0; install by an electrician per national wiring rules.
- **Total estimate: €18–28k.**

### Validation toolkit
- **Kill question:** Will one 60-room hotel run a 20-room pilot and report fewer than 2 wrong "vacant" calls per week? Hotel managers only buy after a pilot in their own building.
- **Cheapest experiment (~€600):** 20 devkit units (radar + LoRa) on USB power bricks in ceiling-mounted boxes + one gateway, for 4 weeks. Attendants mark each "wrong" status.
- **5-question interview (GM / executive housekeeper):**
  1. How many times a day does an attendant knock on an occupied room or come back to a skipped one?
  2. How do you plan stay-over cleaning today: door hangers, app requests, guesswork?
  3. What do vacant rooms cost you in heating/cooling, and do you set back today?
  4. How would guests react to a "presence sensor, no camera, no microphone" notice?
  5. A 20-room pilot at €2,500, credited if you roll out: yes, and who signs?
- **Landing-page headline:** "Know which rooms are free to clean. Right now."
  - Ceiling radar sees if anyone is in the room. No camera, no microphone.
  - Housekeeping board on a tablet, no PMS project needed.
  - Set back heating in empty rooms automatically.
- **Pass threshold:** 3 paid pilots in 8 weeks; at least one pilot ends with a full-hotel order.

### First production checklist
- **Samples:** radar lot sample test (stationary person at 4 m), AC-DC module batch reports, LoRa RF output check.
- **Golden sample:** unit with measured radar thresholds, hi-pot result, LoRa keys provisioning procedure, firmware hash.
- **DFM review:** mains/low-voltage separation in a small ceiling box, terminal access for electricians, radar window, ceiling clip and cable entry, V-0 material certificates.
- **MOQ talk:** LD2460 (price at 1k/5k), RFM95, AC-DC modules, enclosure tooling (~€6–10k).
- **QC/AQL:** AQL II 0.65 safety (100% hi-pot), 1.0/2.5 otherwise; 100% radar presence test with a reference target, 100% LoRaWAN join test; unique DevEUI/key labels as QR.
- **Packaging:** units in 10-packs labelled by floor/room on install; installer guide (permanent circuit!), guest notice cards.
- **Incoterms:** FCA Shenzhen; DDP for small hotel batches if you don't want to be importer of record yourself.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and HopeRF (华普微)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2460 24 GHz multi-target status-detection radar module](/db/hilink-ld2460.html) (multi-target status radar (moving / subtle / stationary people)); [HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package)](/db/hilink-10mxx.html) (isolated AC-DC from the room lighting circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa link to a building gateway, no guest-Wi-Fi dependency). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) websites)

```email
Subject: Sample order and volume pricing — HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module — for a Room-Ready Radar for Housekeeping

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Room-Ready Radar for Housekeeping: A small ceiling sensor per hotel room that tells housekeeping 'guest is out' right now — so staff stop knocking on occupied rooms — and the energy system can set back heating. Radar, no camera, no microphone. The design is built around your HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module.
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
主题：样品订购及批量报价 — HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module — 用于Room-Ready Radar for Housekeeping

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Room-Ready Radar for Housekeeping：A small ceiling sensor per hotel room that tells housekeeping 'guest is out' right now — so staff stop knocking on occupied rooms — and the energy system can set back heating. Radar, no camera, no microphone。产品设计基于贵司的HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module。
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
Subject: PCBA quote from open design files — Room-Ready Radar for Housekeeping, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Room-Ready Radar for Housekeeping: A small ceiling sensor per hotel room that tells housekeeping 'guest is out' right now — so staff stop knocking on occupied rooms — and the energy system can set back heating. Radar, no camera, no microphone. The design starts from published open-hardware files (HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Room-Ready Radar for Housekeeping，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Room-Ready Radar for Housekeeping：A small ceiling sensor per hotel room that tells housekeeping 'guest is out' right now — so staff stop knocking on occupied rooms — and the energy system can set back heating. Radar, no camera, no microphone。设计基于已公开的开源硬件文件（HLK-LD2460 24 GHz multi-target status-detection radar module, HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Find one independent 60-room hotel GM (your own network, local hotel association) willing to host the 20-room pilot; start the attendant tally sheet now.
2. Order 3 LD2460 modules, 3 RFM95W and an off-the-shelf LoRaWAN gateway; get a stationary person detected for 60 minutes without a drop-out.
3. Draft the guest notice and the legitimate-interest assessment; get a one-hour review from a privacy lawyer in your launch country.

Want help sourcing or building this? Talk to us via www.gongbans.com.
