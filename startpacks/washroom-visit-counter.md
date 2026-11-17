# Washroom Visit Counter — Founder Start Pack

> A radar at the washroom entrance that counts visits and triggers cleaning after N uses instead of on a fixed schedule — for offices, stations, festivals and sports venues, with no camera anywhere near the toilets.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Washrooms are cleaned on fixed rounds: every two hours whether 3 or 300 people used them. Quiet washrooms get over-cleaned, busy ones are dirty by 11:00, and complaints land on the facility manager. Cameras are out of the question near toilets.
- **Customer:** Facility-service and cleaning companies (they pay, they own the SLA), and their clients: offices, stations, stadiums, event organisers. Cleaners use it through their existing task app.
- **Product:** A small doorway sensor with a 24 GHz trajectory radar that counts entries by direction, sends counts over LoRaWAN, and fires a "cleaning due" webhook after N visits. Battery or 5 V. Optional feedback button. Counts only, no images, no identities.
- **Why now:** Cleaning contracts are moving from fixed rounds to usage-based and output-based SLAs; labour is the biggest cost and the hardest to hire. LoRaWAN coverage in commercial buildings is normal now. Trajectory radar modules give directional counting for a few euros.
- **The ask:** ~€90k to certification and 1,000 units, mostly covered by a paid 20-unit pilot and a pre-ordered rollout from one cleaning company.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will one cleaning company with >50 sites pilot 20 units and agree to switch rounds to usage-based for the pilot sites?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Facility-service and cleaning companies, offices, event organisers, sports stadiums.

**The problem as the pack states it:** Washrooms are cleaned on fixed rounds: every two hours whether 3 or 300 people used them. Quiet washrooms get over-cleaned, busy ones are dirty by 11:00, and complaints land on the facility manager. Cameras are out of the question near toilets.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **EFCI** · https://www.efci.eu/ — European federation of cleaning and facility-services companies.
- **Die Gebäudedienstleister (BIV, DE)** · https://www.die-gebaeudedienstleister.de/ — German building-cleaning trade federation.
- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€99–129 + platform (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how facility-service and cleaning companies, offices, event organisers, sports stadiums deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you decide today when a washroom gets cleaned, and what happened the last time it was cleaned too late or for nothing?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A radar at the washroom entrance that counts visits and triggers cleaning after N uses rather than on a fixed schedule — for offices, stations, festivals and sports venues, with no camera in or near the toilets. On a scale of one to ten, how likely would you be to buy that at €99–129 + platform (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Washroom Visit Counter: would you pay €99–129 + platform (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Washroom Visit Counter: A radar at the washroom entrance that counts visits and triggers cleaning after N uses rather than on a fixed schedule — for offices, stations, festivals and sports venues, with no camera in or near the toilets. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €99–129 + platform (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A cleaning company with 50+ sites runs on labour: 60–80% of its cost is people. Contracts increasingly say "clean when needed" and "prove it". Existing usage-based systems (ToF counters, thermal sensors, camera-based counters at building level) are priced for airports and need a platform subscription.

- **Who pays:** the cleaning/facility-service company (as a tool to cut wasted rounds and win tenders), or the building owner who wants SLA evidence.
- **Who uses:** cleaners (receive "Washroom 3F-East due" in their task app) and the area supervisor (sees counts and response times).
- **Buyer psychology:** the operations director buys if you show labour hours saved per site per month in a pilot. Nothing else matters.

### Market size (estimates — check)

- **TAM:** Western Europe has millions of commercial washrooms. Assume 600k office/commercial buildings in DE, NL, BE, FR, UK, Nordics with an average of 4 washroom entrances → **2.4M entrances**; at €110 per sensor = **~€260M** hardware plus platform revenue.
- **SAM:** sites managed by professional cleaning companies with usage-based or output-based contracts, plus high-traffic public sites (stations, stadiums, festivals, motorway services): ~10–15% → **250–350k entrances**, ~€30–40M hardware plus €1–2/entrance/month software.
- **SOM (3 yrs):** 3–5 cleaning companies at 1,000–3,000 entrances each → **5–10k units**, €0.6–1.1M hardware + recurring.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing — fixed rounds + paper checklist on the door | Free, familiar | No data, wasted hours, dirty busy washrooms |
| Time-of-flight people counters (e.g. Terabee-type sensors) and platforms (FacilityApps, FootfallCam smart washroom, V-Count) | Proven usage-based cleaning, anonymous counting | Often priced per site with platform lock-in; installed above doors with power; good but expensive for mid-size cleaners |
| LoRaWAN IoT bundles (Milesight-based smart washroom systems with counters, consumable sensors) | Full systems for airports and big venues | Heavy, multi-sensor projects; overkill for a 50-site cleaning firm |
| Thermal/PIR "occupancy" sensors | Cheap | Presence, not count; can't tell 2 visits from 20 |
| Feedback buttons (smiley terminals) | Measures complaints | Reacts after it's dirty |

**Wedge:** a cheap, battery-capable, camera-free doorway counter that speaks plain LoRaWAN and a webhook, so it plugs into the cleaning company's *existing* task app. No new platform to sell.

### Product & value proposition

- **Hardware:** 90 × 60 mm wall/door-frame unit, LD2450 radar looking across the doorway, counts in/out by trajectory crossing a virtual line. LoRaWAN 868 MHz uplink every 15 min (count since last clean) plus immediate uplink when threshold N is reached. Optional big button: "cleaned" (resets the counter) or "report a problem".
- **Power:** the LD2450 draws ~120 mA average at 5 V (per catalogue) — that's not a battery device if it runs continuously. Two SKUs: **5 V mains-adapter/PoE-splitter version (default)**, and a battery version that duty-cycles the radar using a PIR or the low-power LD2410S as a wake-up trigger (needs validation; accuracy drops).
- **Integration:** ChirpStack or The Things Stack → small cloud function → webhook into the task app (most cleaning software has an API). Dashboard optional.
- **Pricing (estimates):** sensor €99–129 one-off; platform/webhook service €1.50–3 per entrance per month (or free if the customer runs their own LoRaWAN server). Pilot pack: 20 sensors + 6 months service €2,900.

### Unit economics (estimates, EUR per unit, 5 V SKU)

| Item | 1k | 5k |
|---|---|---|
| LD2450 radar | 6.5 | 5.0 |
| MCU + LoRa: RFM95CW-class module + small MCU (or a LoRa SoC) | 6.0 | 4.6 |
| Power (5 V input, protection, LDO), button, LED, passives | 1.8 | 1.3 |
| PCB 4-layer small | 1.0 | 0.7 |
| Assembly + test (count test with a moving target rig) | 2.5 | 1.6 |
| Enclosure (ABS, radar-transparent window, wall/frame mount) | 3.0 | 2.0 |
| USB-C 5 V adapter + cable + packaging | 3.5 | 2.8 |
| Freight + duty to EU | 1.5 | 0.9 |
| Certification amortised (€15k) | 15.0 | 3.0 |
| **Landed cost** | **40.8** | **21.9** |
| Net price B2B direct (€109) | 109 | 109 |
| Reseller/integrator margin if indirect (25%) | −27 | −27 |
| **Gross margin direct** | **€68 (62%)** | **€87 (80%)** |
| **Gross margin via integrator** | **€41** | **€60** |

Recurring service at €2/month over 36 months = €72 per unit on top, at ~80% margin if you keep the backend boring.

### Go-to-market

**First 100 customers (units):** one mid-size cleaning company (50–300 sites) with a forward-thinking operations director. Find them at cleaning trade fairs (CMS Berlin, Interclean Amsterdam), in the national cleaning trade associations, and on LinkedIn among "Operations Director, Gebäudereinigung/schoonmaak". Offer a 20-unit paid pilot across 4 sites with a before/after labour-hours report.

**Then scale:** cleaning-software vendors as partners (you become their sensor), LoRaWAN integrators and network operators (they already sell to the same buildings), event and festival toilet-rental companies (portable toilet blocks — strong use case), stations and stadium operators via tenders.

### 12-month plan

- **Q1:** bench prototype on M5 LoRaWAN unit + LD2450; counting accuracy test in 3 real doorways; recruit the pilot customer (kill question).
- **Q2:** own PCB rev A, enclosure, backend + webhook into the pilot customer's task app; 20-unit paid pilot.
- **Q3:** pilot report (labour hours, complaints), certification, 1,000-unit run against the customer's rollout order.
- **Q4:** second cleaning company, first software-vendor partnership, festival/portable-toilet pilot.

**Team:** founder on sales/ops (ideally ex-facility management), firmware/backend engineer (full-time), hardware engineer (part-time/contract), Shenzhen partner for PCBA and enclosure.

**Funding to first 1,000 units (estimate):** landed hardware excl. cert €26k + tooling €8k + certification €15k + prototypes/pilot €5k + 6 months team €40k + fairs/sales €5k = **≈€99k**. Pilot €2.9k + rollout deposit (30% of 1,000 × €99 ≈ €30k) covers about a third. Rest: bootstrap with services revenue, an angel from facility services, or a regional innovation voucher.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** counting errors (groups, people hesitating in the doorway, doors swinging through the beam) | Mount position and virtual-line logic tested in 10 doorways; publish accuracy (target ≥95% vs manual count); threshold-based cleaning tolerates small errors |
| **Technical:** power — radar is not battery-friendly at full duty | Ship 5 V SKU first; battery SKU only after a duty-cycle test proves accuracy |
| **Market:** cleaners don't trust the trigger and keep fixed rounds | Pilot contract includes switching rounds at pilot sites; measure and report hours saved |
| **Regulatory/privacy:** works councils and the public may assume "surveillance near toilets" | No camera, no images, counts only; sticker on the unit explaining it; DPIA one-pager; no identifiers in the data |
| **Supply:** LD2450 single source, design files via maker | Firmware abstraction for a second radar; buy 20% safety stock; or a ToF fallback SKU |
| **Connectivity:** no LoRaWAN coverage in basement washrooms | Bring an indoor gateway in the pilot pack (€150–250); Wi-Fi variant later |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2450 trajectory radar | https://www.gongbans.com/db/hilink-ld2450.html | Tracks up to 3 targets, X/Y + speed → directional counting | Datasheet public, design files via maker (no open schematics) | Buy as module |
| HopeRF RFM95CW 868/915 MHz LoRa module | https://www.gongbans.com/db/hoperf-rfm95cw.html | LoRa radio for the product PCB | Datasheet, demo code, mechanical, photos — HopeRF MIT GitHub folder: https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95CW | MIT licence for the repo content — keep the notice |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | Fast LoRaWAN for the first pilot prototypes | Enclosure/structure files only — main-board electronics not published | Prototyping only |

### Block diagram

```
5V USB-C (or battery + wake sensor) ──► power / LDO 3.3V
                                            │
LD2450 radar (UART) ──► MCU: trajectory → line-crossing in/out counter
                                            │ SPI
                                     RFM95CW LoRa 868 MHz ──► LoRaWAN gateway
                                            │                     │
                     button "cleaned"/"problem", LED       network server (ChirpStack/TTS)
                                                                  │
                                         webhook: "Washroom X due (N visits)" ──► cleaning task app
```

**Engineering gap:** the counting algorithm (line crossing with hysteresis, group handling), the mounting geometry, and the boring backend glue. Electronics are simple.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| LD2450 | €5–7 | **Single source**; lock firmware version |
| RFM95CW | €4–5 | LoRa transceiver; MIT reference material |
| MCU (STM32L0/ESP32-C3 class) | €1–2 | Or a LoRa SoC to merge MCU + radio |
| 5 V input protection, LDO | €0.5 | |
| Button, LED, buzzer-free | €0.4 | |
| Antenna (spring or PCB) | €0.3 | Test in metal door frames |
| Enclosure with radar window | €2–3 | Window thickness/material tuned for 24 GHz |
| USB-C adapter + cable | €2.5 | Or sell without adapter for PoE/5 V installs |

### Firmware/software starting point

- **LoRaWAN stack:** RadioLib (supports SX127x-based modules like the RFM95) or Semtech LoRaMac-node; or Arduino-LMIC (MCCI) — all exist, check licences.
- **Network server:** ChirpStack (open source) or The Things Stack.
- **Radar parsing:** LD2450 protocol from the Hi-Link datasheet; ESPHome LD2450 support in recent versions (verify) is a handy reference for the frame format.
- **Webhook glue:** any small serverless function; aim for documented integrations with 2–3 cleaning-software vendors' APIs (search which ones your pilot customer uses).

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 6 interviews with cleaning-company ops directors; manual count study (a person with a clicker) at 3 washrooms for 2 days to show variance in usage | ≥1 company agrees in writing to a paid 20-unit pilot and to switch rounds at pilot sites |
| 3–5 | **Works-like** — M5 LoRaWAN unit + LD2450 on a dev board, counting firmware, data to ChirpStack | ≥95% count accuracy vs clicker count over 500 passes in 3 doorway types |
| 6–8 | **Looks-like + EVT** — own PCB with RFM95CW, enclosure with radar window, webhook into the customer's task app; 25 units | 25/25 pass a moving-target test rig; uplinks reach gateway from 4 test washrooms |
| 9–10 | **DVT + pre-compliance** — EMC/radio pre-scan (24 GHz + 868 MHz), EN 18031 gap check, DPIA one-pager | No pre-scan fails; duty-cycle within 868 MHz band limits; DPIA reviewed by the customer's DPO |
| 11–12 | **Pilot batch** — 20 units live at 4 sites, cleaners act on the webhook | Report: ≥15% fewer cleaning rounds at equal or fewer complaints; customer signs rollout LOI |

### Certification checklist (EU)

- **CE — RED:** EN 300 440 (24 GHz SRD radar), EN 300 220-1/-2 (868 MHz SRD incl. duty cycle), EN 301 489-1/-3 (EMC), EN 62368-1 (safety), RF exposure EN 62311/62479. Estimate €8–12k.
- **EN 18031-1** (RED cybersecurity): applies to radio equipment that can communicate over the internet, directly or indirectly. A LoRaWAN device behind a network server likely falls in scope — ask the lab; budget €2–4k.
- **CRA:** reporting duties from 11 Sep 2026, full obligations 11 Dec 2027 — SBOM, secure update (LoRaWAN FUOTA or manual), vulnerability handling, support period.
- **RoHS, REACH, WEEE**, packaging EPR.
- **Battery Regulation (EU) 2023/1542** only for the battery SKU (labelling, collection, removability rules).
- **GDPR:** counts only, no images, no identifiers → likely not personal data, but document it in a DPIA-style note; works councils and site operators will ask. Never add cameras or Wi-Fi/BLE MAC sniffing to "improve accuracy".
- No medical, no toy directive.
- **Total estimate:** €12–17k.

### Validation toolkit

- **Kill question:** Will one cleaning company with >50 sites pilot 20 units and agree to switch rounds to usage-based for the pilot sites? Cheapest experiment: a 2-day manual clicker count at 3 of their washrooms, delivered as a one-page chart showing how uneven usage is — then ask for the pilot.
- **Interview script (5):**
  1. How do you plan washroom rounds today, and who decides the frequency — you or the client contract?
  2. What does a washroom complaint cost you (re-clean, penalty, lost contract)?
  3. Have you tried counters or IoT sensors? What went wrong?
  4. Which task/workforce app do your cleaners use, and does it have an API?
  5. If a €109 sensor cut 20% of washroom rounds on a site, how fast would you roll it out — and who signs that budget?
- **Landing page:** Headline: "Clean washrooms when they're used, not when the clock says so." Bullets: "Counts visits with radar — no cameras, no personal data." / "Sends 'cleaning due' straight into your team's task app." / "Battery or 5 V, LoRaWAN, installed in 10 minutes."
- **Pass:** a signed paid pilot (≥20 units at ≥€90) plus written intent to switch rounds; or 3 companies asking for pilots after the clicker study.

### First production checklist

- Samples: radar modules from two batches; RFM95CW from authorised channel (fakes of RFM95 clones exist — buy direct).
- Golden sample: counting accuracy certified on the test rig; enclosure window approved.
- DFM: radar-transparent window (no metal paint, no carbon-filled plastic), mounting bracket for door frames.
- MOQ: radar and LoRa modules per tray; enclosure 1k shots.
- QC/AQL: 100% RF test (LoRa join + uplink in a shielded box), 100% radar test (target passes), AQL 1.0/2.5.
- Packaging: unit, bracket, screws, adhesive pad, QR to install video; GDPR/no-camera statement on the box.
- Incoterms: FOB Shenzhen; DAP to the first customer for the pilot so you control the experience.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R)](/db/hilink-ld2450.html) (24 GHz trajectory radar to count in/out at the doorway). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95CW 868/915 MHz LoRa transceiver module](/db/hoperf-rfm95cw.html) (868 MHz LoRa transceiver). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (LoRaWAN unit for pilots). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868) — for a Washroom Visit Counter

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Washroom Visit Counter: A radar at the washroom entrance that counts visits and triggers cleaning after N uses rather than on a fixed schedule — for offices, stations, festivals and sports venues, with no camera in or near the toilets. The design is built around your HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868).
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
主题：样品订购及批量报价 — HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868) — 用于Washroom Visit Counter

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Washroom Visit Counter：A radar at the washroom entrance that counts visits and triggers cleaning after N uses rather than on a fixed schedule — for offices, stations, festivals and sports venues, with no camera in or near the toilets。产品设计基于贵司的HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)。
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
Subject: PCBA quote from open design files — Washroom Visit Counter, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Washroom Visit Counter: A radar at the washroom entrance that counts visits and triggers cleaning after N uses rather than on a fixed schedule — for offices, stations, festivals and sports venues, with no camera in or near the toilets. The design starts from published open-hardware files (HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Washroom Visit Counter，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Washroom Visit Counter：A radar at the washroom entrance that counts visits and triggers cleaning after N uses rather than on a fixed schedule — for offices, stations, festivals and sports venues, with no camera in or near the toilets。设计基于已公开的开源硬件文件（HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HopeRF RFM95CW 868/915 MHz LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. List 20 cleaning companies with 50+ sites in your country; message 10 operations directors asking for a 20-minute call about usage-based washroom cleaning.
2. Order 3 LD2450 radars and an M5 LoRaWAN unit; get in/out counting working across one doorway at home or in your office.
3. Do a manual clicker count at one public washroom for a day (you, a friend, a chair) — the chart is your first sales slide.

Want help sourcing or building this? Talk to us via www.gongbans.com.
