# Matter Lab Kit — Founder Start Pack

> A university and vocational lab kit to build a real Matter-over-Thread product from scratch: sensor board, Thread border router and a curriculum that goes from "blink" to a certified-style device in a home hub.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Matter is becoming the baseline for smart-home products, and every European IoT company needs engineers who understand Thread, the Matter data model, commissioning and device attestation. Universities still teach MQTT on an ESP8266. Vendor courses are free but online, single-vendor and not built for a 14-week semester with grading.
- **Customer:** Universities of applied sciences (Hochschulen, hogescholen), vocational IoT courses, and corporate training providers retraining embedded engineers. Lecturers choose; departments pay.
- **Product:** A per-seat kit (Matter-over-Thread EVB with onboard sensors, Thread border router with screen, a second Thread platform for comparison) plus 10 graded labs: Thread networking, Matter data model, commissioning, OTA, security (DAC/PAI certificates), power profiling. Works with any commercial hub.
- **Why now:** Matter is in all big ecosystems; CRA and EN 18031 force companies to understand security and updates; there are few hands-on, vendor-mixed teaching kits. One kit gives open schematics, onboard sensors and a ready border router.
- **The ask:** ~€45k to the first 300 seats; a lean business funded by pre-sold semester orders and one corporate training partner.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 3 universities and 1 corporate training provider each buy 10 seats for the next semester? If corporate training pays €349/seat, this is a business; if not, it's a nice open-source project.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Universities of applied sciences, vocational IoT courses, corporate training for embedded engineers moving to Matter.

**The problem as the pack states it:** Matter is becoming the baseline for smart-home products, and every European IoT company needs engineers who understand Thread, the Matter data model, commissioning and device attestation. Universities still teach MQTT on an ESP8266. Vendor courses are free but online, single-vendor and not built for a 14-week semester with grading.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **Connectivity Standards Alliance** · https://csa-iot.org/ — the body behind Matter and Zigbee; member companies, certification and training.
- **r/embedded** · https://www.reddit.com/r/embedded/ — embedded engineers.
- **mikrocontroller.net (DE)** · https://www.mikrocontroller.net/ — German-speaking electronics engineers and students.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€249–349 per seat (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how universities of applied sciences, vocational IoT courses, corporate training for embedded engineers moving to Matter deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. What hardware do your students build connected-device projects on today, how close does it get to a real product, and what do employers say is missing?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A university/vocational lab kit to build a real Matter-over-Thread product from scratch: sensor board, Thread border router and a curriculum from 'blink' to a certified-style device in a home hub. On a scale of one to ten, how likely would you be to buy that at €249–349 per seat (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Matter Lab Kit: would you pay €249–349 per seat (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Matter Lab Kit: A university/vocational lab kit to build a real Matter-over-Thread product from scratch: sensor board, Thread border router and a curriculum from 'blink' to a certified-style device in a home hub. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €249–349 per seat (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A lecturer who wants to teach Matter in the next semester has to assemble dev kits from 3 vendors, find a border router, write 10 labs and debug student setups at 9 a.m. Corporate L&D teams want a 3-day hands-on course for 12 embedded engineers and can't find one in their language.

- **Who pays:** university departments (lab equipment budgets, usually once a year), vocational schools, corporate training providers (pay per seat per course, faster decisions, higher price).
- **Who uses:** students and engineers; the lecturer/trainer runs the course.
- **The honest framing:** education is a small, slow market. Corporate training is where the margin is.

### Market size (estimates — check)

- **TAM:** EU has several hundred universities/universities of applied sciences with embedded/IoT courses, plus thousands of vocational schools, plus corporate training of embedded engineers (the EU has hundreds of thousands of embedded engineers — estimate). Assume 1,000 institutions × 20 seats × €299 = **€6M** one-off + refresh, plus corporate training.
- **SAM:** DE, NL, BE, AT, Nordics, CH: ~250 institutions + ~50 corporate trainers → **~€1.5–2M** seats plus course licences.
- **SOM (3 yrs):** 30 institutions × 15 seats + 10 corporate trainers × 40 seats/year → **~850 seats/year**, ~€250k/year. Plus paid trainer-led courses (€1,200–1,800 per engineer for 3 days) if you run them yourself.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / teach MQTT + Wi-Fi | Familiar | Graduates don't know Matter/Thread; employers notice |
| Nordic Developer Academy "Matter Fundamentals" (free, self-paced, nRF dev kits) | Excellent free online course | Single vendor, self-paced, no grading, no lab logistics, no border-router kit |
| Arduino Matter Discovery Bundle (Nano Matter + modules, 7-chapter curriculum) | Strong competitor for makers/education | Arduino abstraction hides much of Thread/Matter internals; we go deeper (certs, OTA, power, data model) |
| Silicon Labs training examples / vendor workshops | Free, good | Vendor events, not a semester course |
| Thread Group / CSA education material | Channel education, marketing level | Not hands-on engineering |
| Self-assembled dev kits | Flexible | Lecturer time; inconsistent setups |

**Wedge:** a *semester-ready, vendor-mixed* lab: two different Thread platforms (EFR32-based module and ESP32-H2) plus a border router, graded labs with answer keys, and the security/certification topics companies actually need for EN 18031/CRA. Sell the curriculum as much as the kit.

### Product & value proposition

- **Per-seat kit:** HopeRF HM-MT2401 EVB (EFR32MG24 module; contact, temperature/humidity, pressure and PIR sensors; RGB light), ESP32-H2-DevKitM-1 (second Thread/Zigbee platform), USB cables, a USB power meter for power labs. **Per 4 seats:** one M5Stack CoreS3 Thread Border Router.
- **Curriculum (10 labs):** 1) Thread mesh basics (roles, partitions), 2) Matter data model (endpoints, clusters), 3) build a temperature sensor device, 4) commissioning (QR, PASE, CASE), 5) multi-admin with 2 commercial hubs, 6) OTA updates, 7) security: DAC/PAI/PAA, test certificates, 8) power profiling a sleepy end device, 9) interop: EFR32 vs ESP32-H2 on one network, 10) capstone: build, document and "pre-certify" your own device (test-harness walkthrough).
- **Lecturer pack:** slides, answer keys, grading rubrics, VM/container with toolchains.
- **Pricing (estimates):** €249–349 per seat (kit + curriculum licence); lecturer pack free with ≥10 seats; corporate course licence €2,000/year + kits; trainer-led 3-day course €1,500 per engineer (if you deliver it).

### Unit economics (estimates, EUR per seat)

| Item | 1k seats | 5k seats |
|---|---|---|
| HM-MT2401 EVB kit | 35 | 28 |
| ESP32-H2-DevKitM-1 | 9 | 8 |
| Share of CoreS3 Thread BR (1 per 4 seats) | 16 | 14 |
| USB cables + USB power meter | 6 | 4.5 |
| Kitting, box, foam, printed quick start | 4 | 3 |
| Freight + duty | 2 | 1.5 |
| Compliance check of bundle (docs, labelling) amortised (€5k) | 5 | 1 |
| **Landed cost** | **77** | **60** |
| Net price direct (€299) | 299 | 299 |
| Distributor/education reseller margin if indirect (25%) | −75 | −75 |
| **Gross margin direct** | **€222 (74%)** | **€239 (80%)** |
| **Gross margin via reseller** | **€147** | **€164** |

Curriculum writing (~€25–35k equivalent) is the real cost — amortise it like tooling.

### Go-to-market

**First 100 customers (seats → first 300):** embedded-systems lecturers at universities of applied sciences in DE/NL/BE (find them via their course catalogues and conference talks), embedded world conference in Nuremberg (university track and exhibitor halls), Matter/Thread meetups, LinkedIn posts with a lab video, corporate L&D buyers at IoT companies (hiring pages mentioning "Matter" are your lead list).

**Then scale:** education resellers of electronics kits, a train-the-trainer programme, partnership with a corporate training provider, online cohort version for engineers.

### 12-month plan

- **Q1:** labs 1–4 written and tested with 5 student testers; 3 lecturer interviews; offer to 10 institutions (kill question).
- **Q2:** labs 5–10, lecturer pack, pilot semester with 1–2 institutions (paid), first corporate 3-day course.
- **Q3:** kit production (300 seats), sales for the winter semester, embedded-world style demo.
- **Q4:** second corporate partner, online cohort, update for the latest Matter spec release.

**Team:** founder = embedded engineer/educator writing labs (full-time), co-author lecturer (part-time), logistics/kitting partner. No hardware design needed in year 1.

**Funding to first 300 seats (estimate):** kits landed €23k + curriculum work 6 months €25k + pilot travel/demos €4k + bundle compliance review €3k = **≈€55k**. Pilot-semester orders (2 × 15 seats × €299) ≈ €9k + one corporate course (12 × €1,500) ≈ €18k. Bootstrappable with modest savings, or a small education-innovation grant.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** universities buy slowly; Arduino bundle and free vendor courses are "good enough" | Go corporate first for revenue; universities as reputation |
| **Technical:** Matter SDK versions change fast; labs break | Pin SDK versions per semester; containerised toolchains; annual update subscription |
| **Supply:** EVB kit availability and price from one maker | Keep labs portable to other EFR32MG24 boards; buy semester stock in advance |
| **Regulatory:** reselling a bundle of CE-marked kits — who is the "manufacturer"? | Sell as a kit of unchanged CE-marked dev kits for professional/educational use; get a short legal opinion |
| **Licensing:** Matter test certificates and CSA rules for teaching | Use the SDK's test PAA/DAC; teach real certification as process, don't issue real certificates |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF HM-MT2401 Matter-over-Thread EVB kit | https://www.gongbans.com/db/hoperf-hm-mt2401-evb-kit.html | Main lab board: EFR32MG24 module + contact, T/RH, pressure, PIR, RGB | Schematic + firmware — HopeRF MIT GitHub folder: https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401%20EVB%20Kit | MIT licence for repo content |
| M5Stack CoreS3 Thread BR (K149) | https://www.gongbans.com/db/m5stack-cores3-thread-br.html | Thread border router with screen, one per group | Enclosure/structure files only — main-board electronics not published | Buy as product |
| Espressif ESP32-H2-DevKitM-1 | https://www.gongbans.com/db/espressif-esp32-h2-devkitm-1.html | Second Thread/Zigbee platform for interop labs | Metadata only in catalogue (official Espressif kit) | Buy as product; reference files on Espressif's site |

### Block diagram

```
 Student seat                                   Group (4 seats)
 ┌──────────────────────────┐                   ┌─────────────────────────┐
 │ HM-MT2401 EVB (EFR32MG24)│ ── Thread mesh ── │ CoreS3 Thread Border    │── Wi-Fi/Ethernet ── lab LAN
 │ sensors + RGB            │                   │ Router (screen)         │        │
 │ ESP32-H2-DevKitM-1       │ ── Thread mesh ──►│                         │   commercial hubs
 └──────────────────────────┘                   └─────────────────────────┘   (Apple/Google/HA) +
   USB ── student laptop (toolchain container, chip-tool)                       chip-tool controller
```

**Engineering gap:** none in hardware. All the work is curriculum, toolchain packaging and a lab network design that survives university Wi-Fi (bring your own access point).

### Starter BOM (estimates, per seat)

| Part | Est. | Notes |
|---|---|---|
| HM-MT2401 EVB kit | €28–35 | Ask HopeRF for edu pricing and stock commitment |
| ESP32-H2-DevKitM-1 | €8–9 | Widely distributed |
| CoreS3 Thread BR (÷4) | €14–16 | Check firmware version consistency |
| USB-C cables ×2 | €2 | |
| USB power meter | €3 | For lab 8 |
| Lab travel router (per room) | €40 | Own SSID, no campus Wi-Fi drama |
| Box + foam | €3 | |

### Firmware/software starting point

- **connectedhomeip** (project-chip, the open Matter SDK) incl. **chip-tool** for commissioning and cluster interaction.
- **Silicon Labs Simplicity SDK / Matter extension** for EFR32MG24; HopeRF's EVB firmware from the GitHub folder above.
- **ESP-Matter** and **ESP-IDF** (Espressif) for the ESP32-H2.
- **OpenThread** and **ot-br-posix**; the CoreS3 BR firmware from M5Stack (verify which open stack it uses).
- Toolchains packaged in a container/VM image per semester.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 lecturer/L&D conversations, one-page syllabus + price | ≥3 institutions + 1 corporate provider say "10 seats next semester" in writing (kill question) |
| 3–5 | **Works-like** — labs 1–4 on 4 seats + 1 BR, run by 5 student testers | Each lab completed in ≤3 h by testers without help; toolchain install ≤30 min |
| 6–8 | **Looks-like + EVT** — labs 5–8, lecturer pack draft, kit box | 2 lecturers dry-run labs; ≥80% of steps work first time |
| 9–10 | **DVT** — labs 9–10, grading rubrics, bundle compliance review, Matter SDK version freeze | Full 10-lab run by 2 testers; written legal note on bundle CE status |
| 11–12 | **Pilot batch** — 30–50 seats delivered for a pilot course | Pilot course runs; student rating ≥4/5; reorders or second-cohort booking |

### Certification checklist (EU)

- **CE:** a bundle of *unmodified* CE-marked dev kits for educational/professional use: each kit carries its own CE (verify DoC of each: HopeRF EVB, M5Stack CoreS3 BR, Espressif ESP32-H2 kit). Some dev boards are sold as "evaluation kits for professional use" without full CE — **check each DoC**; if one lacks it, the kit is not resellable to schools as-is.
- **RED / EN 18031 / CRA:** responsibility sits with each kit's manufacturer as long as you don't modify them. If you ship your own firmware image pre-flashed, you may become the manufacturer — avoid pre-flashing, or get advice. Note: CRA reporting from 11 Sep 2026, full from 11 Dec 2027.
- **WEEE:** as the importer/distributor you may need WEEE registration in each country (B2B). Packaging EPR.
- **RoHS/REACH:** rely on supplier declarations; keep them on file.
- **Matter/CSA:** teach with test certificates; don't claim "certified"; check CSA's rules on using the Matter name in course marketing.
- **GDPR:** student data in grading tools — use the institution's systems.
- No toy directive (adult/higher education).
- **Total estimate:** €2–5k (legal review + registrations), no lab testing needed if kits are unchanged.

### Validation toolkit

- **Kill question:** Will 3 universities and 1 corporate training provider each buy 10 seats for the next semester? If corporate training pays €349/seat, this is a business; if not, it's a nice open-source project. Cheapest experiment: a one-page syllabus PDF + a 3-minute video of lab 3 (Matter sensor appears in a commercial hub), sent to 30 lecturers and 10 L&D managers.
- **Interview script (5):**
  1. What do you teach about IoT connectivity today, and what do employers ask your graduates about?
  2. How do you buy lab hardware — when is the budget decided, and who signs?
  3. What's the worst part of running hardware labs (setup, broken kits, toolchains)?
  4. Would you use a ready 10-lab curriculum with answer keys, or do you need to write your own?
  5. At €299 per seat (kit + curriculum), what would you buy for next semester — and what would make it a no?
- **Landing page:** Headline: "Teach Matter the way products are really built." Bullets: "10 graded labs from Thread basics to device attestation and OTA." / "Two Thread platforms and a border router — vendor-neutral." / "Semester-ready: slides, answer keys and toolchain image included."
- **Pass:** 40 seats ordered (or written POs/intent) for the next semester, including ≥1 corporate order at ≥€349/seat.

### First production checklist

- Samples: 5 of each kit; verify firmware versions and that labs run on all units.
- Golden sample: one complete seat + BR, frozen SDK versions, tested image.
- DFM: not applicable (no own hardware); kitting layout and labelling.
- MOQ talk: EVB kits in batches of 100–300, delivered before semester start; confirm restock lead time.
- QC/AQL: 100% power-on + commissioning test on BRs; EVB sample test per batch (AQL 1.0).
- Packaging: seat box with foam, QR to course portal, safety and disposal notes (WEEE symbol).
- Incoterms: FOB Shenzhen for EVB + BR, EU distributor for Espressif kits; kit in the EU to control quality.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and M5Stack and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-MT2401 Matter-over-Thread EVB kit](/db/hoperf-hm-mt2401-evb-kit.html) (Matter-over-Thread EVB with contact, temp/humidity, pressure, PIR and RGB (open schematic)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack CoreS3 Thread BR (K149)](/db/m5stack-cores3-thread-br.html) (Thread border router with screen). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-h2-devkitm-1](/db/espressif-esp32-h2-devkitm-1.html) (second Thread/Zigbee platform for comparison labs). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and M5Stack and Espressif websites)

```email
Subject: Sample order and volume pricing — HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1 — for a Matter Lab Kit

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Matter Lab Kit: A university/vocational lab kit to build a real Matter-over-Thread product from scratch: sensor board, Thread border router and a curriculum from 'blink' to a certified-style device in a home hub. The design is built around your HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1.

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1.
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
主题：样品订购及批量报价 — HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1 — 用于Matter Lab Kit

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Matter Lab Kit：A university/vocational lab kit to build a real Matter-over-Thread product from scratch: sensor board, Thread border router and a curriculum from 'blink' to a certified-style device in a home hub。产品设计基于贵司的HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1。
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
Subject: PCBA quote from open design files — Matter Lab Kit, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Matter Lab Kit: A university/vocational lab kit to build a real Matter-over-Thread product from scratch: sensor board, Thread border router and a curriculum from 'blink' to a certified-style device in a home hub. The design starts from published open-hardware files (HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Matter Lab Kit，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Matter Lab Kit：A university/vocational lab kit to build a real Matter-over-Thread product from scratch: sensor board, Thread border router and a curriculum from 'blink' to a certified-style device in a home hub。设计基于已公开的开源硬件文件（HopeRF HM-MT2401 Matter-over-Thread EVB kit, M5Stack CoreS3 Thread BR (K149), Espressif esp32-h2-devkitm-1；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Write the one-page syllabus (10 labs, 2 lines each) and send it to 10 lecturers and 5 L&D managers with the price.
2. Order 2 HM-MT2401 EVB kits, 2 ESP32-H2-DevKitM-1 and 1 CoreS3 Thread BR; get lab 3 working end-to-end and record the video.
3. Collect the Declarations of Conformity of all three kits — if one is missing, fix the bundle now, not after the first PO.

Want help sourcing or building this? Talk to us via www.gongbans.com.
