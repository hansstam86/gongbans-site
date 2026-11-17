# Radar Physics Classroom Kit — Founder Start Pack

> A classroom kit that makes radar visible: students see a live map of where classmates walk, measure the Doppler speed of a pendulum and compare 24 GHz FMCW modules, with browser-based lessons and nothing to install.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Radar sits in phones, cars, doorbells and factory lines, yet in most European secondary schools it is still a textbook figure about bats and police speed guns. The teaching kits that exist cost €300+ per set, need a PC with drivers and a teacher who knows Python. Physics teachers have no time for that.
- **Customer:** Physics and informatics departments in secondary and vocational schools (they pay from a department budget), science centres and university outreach teams. Students (14+) use it.
- **Product:** A set of off-the-shelf 24 GHz radar modules (a trajectory-tracking one and a presence one) on an ESP32-S3 controller with a screen. The controller serves a web app over Wi-Fi or Web Serial. Eight experiments with worksheets in EN/DE/NL, plus a teacher mode that puts the whole class on the beamer.
- **Why now:** Trajectory radar modules now output clean X/Y coordinates over UART for a few euros. Browsers can talk to USB serial devices (Web Serial in Chromium), so there's nothing to install. Curricula across the EU are adding "sensors and data" and digital-literacy goals, and radar is the sensor everyone owns without knowing it.
- **The ask:** ~€70k to get to 1,000 sets (≈125 class packs), mostly funded by pre-orders from early-adopter schools plus an education-innovation grant.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 10 physics teachers who see the demo at a teacher conference order a class pack within one budget cycle?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Secondary schools (physics, informatics), vocational schools, science centres, university outreach.

**The problem as the pack states it:** Radar sits in phones, cars, doorbells and factory lines, yet in most European secondary schools it is still a textbook figure about bats and police speed guns. The teaching kits that exist cost €300+ per set, need a PC with drivers and a teacher who knows Python. Physics teachers have no time for that.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/ScienceTeachers** · https://www.reddit.com/r/ScienceTeachers/ — secondary-school science teachers.
- **AAPT** · https://www.aapt.org/ — American Association of Physics Teachers.
- **IOP, Institute of Physics (UK)** · https://www.iop.org/ — UK physics teacher network and conferences.
- **MNU (DE)** · https://www.mnu.de/ — German association of maths and science teachers; regional conferences.
- **Tes Community (UK)** · https://community.tes.com/ — UK teachers' forum.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€89–119 per set, class pack of 8 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how secondary schools, vocational schools, science centres, university outreach deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you teach waves and the Doppler effect today, what do students measure with their own hands, and what equipment would you replace if you could?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A classroom kit that makes radar visible: students see a live map of where classmates walk, measure Doppler speed of a pendulum and compare 24 GHz FMCW modules — with browser-based lessons, no software install. On a scale of one to ten, how likely would you be to buy that at €89–119 per set, class pack of 8 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Radar Physics Classroom Kit: would you pay €89–119 per set, class pack of 8 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Radar Physics Classroom Kit: A classroom kit that makes radar visible: students see a live map of where classmates walk, measure Doppler speed of a pendulum and compare 24 GHz FMCW modules — with browser-based lessons, no software install. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €89–119 per set, class pack of 8 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A physics teacher wants experiments that work in a 45-minute lesson, first time, with 28 teenagers. Radar fails that test today: kits are either expensive lab instruments (university level) or hobby modules that need Arduino code before anything happens.

- **Who pays:** the school's physics/STEM department (budget €500–3,000/year for consumables and kit in many DE/NL/BE schools; bigger one-off pots come from digitalisation programmes). Science centres and university outreach teams buy for workshops and pay faster.
- **Who uses:** students aged 14–19 in pairs; the teacher runs the class display.
- **Who decides:** the head of department, usually after seeing a demo at a teacher conference or in a colleague's classroom. Word of mouth between teachers is the strongest channel in education.

### Market size (estimates — check)

- **TAM:** EU has roughly 30,000+ upper-secondary/vocational schools teaching physics (estimate from national statistics; verify per country). One class pack (8 sets) per school at ~€800 = **~€24M** one-off, plus refresh every ~7 years.
- **SAM:** DE, NL, BE, AT, Nordics, where budgets and English/German materials fit: ~10,000 schools → **~€8M**.
- **SOM (3 years):** 300–600 schools plus 50 science centres/outreach teams → **€0.3–0.5M revenue**. This is a nice small business or a product line inside an existing educational-supplies company, not a venture rocket. Be honest about that.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / textbook + video | Free | No measurement, no data; students forget it |
| Commercial teaching radars (e.g. Pasternack 2.4 GHz demo kit, ME1500-type university courseware) | CW/FMCW/Doppler lab kits with lesson guides | University-level, PC software, priced for labs, not 8 sets per class |
| Red Pitaya STEMlab-based radar kit / MIT-style build-your-own radar (~€300–360 per kit reported) | Open, great for signal processing | Needs Python/Jupyter and a skilled teacher; one kit per group is too expensive for a whole class |
| DIY: Arduino + HB100 Doppler or LD2410 module | Cheap | Teacher must write code, debug drivers, write worksheets; works for the one enthusiast teacher only |
| Generic sensor kits (data loggers from school-science suppliers) | Trusted brand, curriculum fit | Usually no radar at all |

**Wedge:** the only radar kit priced per *class* (8 sets under €900) that runs in a browser in 5 minutes and comes with ready worksheets in the teacher's language, including a privacy lesson on what radar can and cannot see.

### Product & value proposition

- **Set:** AtomS3 controller with screen, LD2450 trajectory radar (up to 3 targets, X/Y + speed), LD2410B presence radar (moving vs still targets), USB-C cable, a small stand with angle markings, a corner-reflector card and a pendulum clip.
- **Software:** a static web app (hosted, also downloadable for offline schools) that connects via Web Serial or to the AtomS3's own Wi-Fi access point. Live plots: map of targets, range vs time, speed vs time, presence energy per range gate.
- **Experiments (8):** 1) Where am I? (live X/Y map), 2) Walking speed and Doppler, 3) Pendulum: period from radar vs stopwatch, 4) What blocks 24 GHz? (cardboard, water bottle, metal, wall), 5) Breathing-still vs moving (presence radar energy, framed as physics, not health), 6) Range resolution: two people close together, 7) Angle of view, 8) Privacy: what does radar know about you and what not?
- **Teacher mode:** class dashboard collects anonymised results from all sets; one-click export to CSV.
- **Pricing (estimates):** single set €99–119; class pack of 8 €790–890; science-centre pack with spare parts and a carry case €1,190. Worksheets free (marketing), teacher training webinar €0 for buyers.

### Unit economics (estimates, EUR per set, sold as class pack)

| Item | 1k sets | 5k sets |
|---|---|---|
| Electronics: AtomS3-class controller (or own ESP32-S3 board at 5k) | 12.0 | 7.5 |
| LD2450 trajectory radar | 6.5 | 5.0 |
| LD2410B presence radar | 2.5 | 1.9 |
| Cables, connector board, passives | 2.0 | 1.4 |
| Stand, reflector card, pendulum clip (injection/laser-cut) | 3.5 | 1.8 |
| Assembly + functional test (radar sees a reflector at 2 m) | 2.0 | 1.2 |
| Packaging (class box, foam, printed quick start) | 2.5 | 1.6 |
| Freight + duty to EU | 1.8 | 1.0 |
| Certification amortised (€12k) | 12.0 | 2.4 |
| **Landed cost** | **44.8** | **23.8** |
| Net price via direct school sales (€849 class pack ex VAT / 8) | 106 | 106 |
| Reseller margin if sold through a school-science distributor (30–35%) | −35 | −35 |
| **Gross margin direct** | **€61 (58%)** | **€82 (78%)** |
| **Gross margin via distributor** | **€26 (37% of net)** | **€47** |

The software and worksheets are the product; the hardware is mostly bought modules. That's why margins look good — and why the real cost is curriculum writing and teacher support, not BOM.

### Go-to-market

**First 100 customers:**
- Teacher conferences and fairs: MNU (Germany's association of maths/science teachers) regional meetings, NVON in the Netherlands, didacta in Germany. One live demo with students walking in front of a beamer sells more than any ad.
- Teacher Facebook groups and forums (physics teachers per country), Twitter/X and Bluesky "physics teacher" communities, Reddit r/PhysicsTeachers.
- Science centres and university outreach (they have budgets and run the same workshop 50 times a year).
- Free worksheets on the website that work with a €10 DIY module: teachers download them, then buy the kit to avoid the hassle.

**Scale:** school-science distributors (in DE, NL, BE and the Nordics there are established catalogue suppliers to schools) on 30–35% margin; national digital-education programmes; teacher-training institutes (Lehrerfortbildung) running a "radar in class" course with kits included.

### 12-month plan

- **Q1:** 10 hand-built sets, 3 experiments, test in 3 classrooms; teacher feedback; demo at one regional teacher meeting. Kill question below.
- **Q2:** all 8 experiments, worksheets EN/DE/NL, teacher mode; stand and box design; 30 pilot sets sold to science centres at full price.
- **Q3:** certification, 1,000-set production run timed for school budget season; didacta-style fair booth (shared with a distributor if possible).
- **Q4:** distributor deal in 2 countries, teacher webinar series, Nordic and French translations.

**Team:** founder (ex-teacher or teacher partner is gold), a front-end/firmware developer (full-time 6 months), a curriculum writer (part-time, a working physics teacher on freelance basis), Shenzhen partner for module sourcing and kitting.

**Funding to first 1,000 sets (estimate):** hardware landed excl. cert €33k + tooling/stand/box €6k + certification €12k + dev 6 months €30k + curriculum writing €6k + fairs/demo travel €6k = **≈€93k**. Pilot and pre-orders (30 science-centre sets + 40 class-pack pre-orders with 30% deposit) ≈ €15–20k. Rest: an education-innovation or digitalisation grant, or one angel from ed-tech. Bootstrappable if one distributor pre-pays.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** schools buy slowly (one budget cycle = up to 12 months) | Sell to science centres and outreach first; sell class packs at fairs with "deliver after budget" invoices |
| **Technical:** classroom chaos (28 students, metal desks, multipath) makes trajectories jump | Experiments designed for 2–3 m zones; teach multipath as a feature (experiment 4) |
| **Technical:** Web Serial only in Chromium browsers; school iPads can't do it | Wi-Fi AP mode as fallback; test on locked-down school laptops early |
| **Regulatory:** toy directive if marketed to under-14s | Market explicitly "for educational use, age 14+, under teacher supervision"; get a written opinion from the test lab |
| **Supply:** both radar modules from one maker, contact-only design files | Keep the firmware module-agnostic; qualify a second 24 GHz module; buy 1,200 at EVT |
| **Privacy:** parents worry about "radar tracking kids" | The privacy lesson is the answer; no data leaves the classroom; no cloud |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2450 24 GHz trajectory-tracking radar (1T2R) | https://www.gongbans.com/db/hilink-ld2450.html | Up to 3 targets with coordinates and speed over UART, 5 V, 6 m range | Datasheet public, design files via maker (no open schematics) | Buy as a finished module; protocol from datasheet |
| HLK-LD2410B/LD2410C 24 GHz presence radar | https://www.gongbans.com/db/hilink-ld2410b.html | Moving/still detection and per-gate energy for the "stillness" experiments | Datasheet public, design files via maker (no open schematics) | Buy as module |
| M5Stack AtomS3 (C123) | https://www.gongbans.com/db/m5stack-atoms3.html | ESP32-S3 controller with screen, USB, Wi-Fi; serves the web app | Enclosure/structure files only — main-board electronics not published | Use as bought module; check M5 terms for resale in a kit |

If you later replace the AtomS3 with your own board at 5k sets, start from the open Espressif ESP32-S3-DevKitC-1 reference (https://www.gongbans.com/db/espressif-esp32-s3-devkitc-1.html, schematic + PCB published).

### Block diagram

```
USB-C 5V ──► AtomS3 (ESP32-S3, screen, Wi-Fi AP / USB CDC)
                 │ UART1                 │ UART2
           LD2450 trajectory        LD2410B presence
           (X,Y,v ×3 targets)       (moving/still, gate energy)
                 │
     Web Serial (Chromium) or Wi-Fi AP ──► browser lesson app
                 │                              │
       on-device display: target count     teacher dashboard (class view, CSV)
```

**Engineering gap:** small. A carrier PCB (two UARTs, 5 V for the LD2450, header), the parsing firmware, and the web app. The real work is the eight experiments that actually work in a noisy classroom, and worksheets teachers trust.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| AtomS3 or ESP32-S3 module | €7–12 | Module route avoids RF design |
| LD2450 | €5–7 | **Single source (Hi-Link)**; check firmware version consistency between batches |
| LD2410B | €2–3 | Single source; alternatives exist from other radar makers |
| Carrier PCB + headers | €1.2 | |
| USB-C cable | €0.6 | |
| Stand, angle scale, reflector card, pendulum clip | €2–3.5 | Laser-cut/printed first, moulded later |
| Box + foam for class pack | €2.5 | Teachers love a box that stacks |

### Firmware/software starting point

- **ESP-IDF** or **Arduino-ESP32** for the controller; the LD2450 and LD2410 serial protocols are in the Hi-Link datasheets.
- **ESPHome** has an `ld2410` component; LD2450 support exists in recent ESPHome versions — verify — useful for quick parsing references, but write your own lightweight parser for the lesson app.
- **Web Serial API** (Chromium) for the browser link; plotting with an open charting library (e.g. uPlot or Chart.js).
- Community parsers for LD2450 on GitHub: search "LD2450 Arduino" — check licences before copying.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — demo video + 2 live demos to physics teachers; one-page offer with class-pack price | ≥5 teachers ask for a pilot set; ≥2 say "I'd order in this budget year" |
| 3–5 | **Works-like** — breadboard sets (AtomS3 + both modules), web app with live map and speed plot, 3 experiments | 3 experiments run in a real classroom in <45 min, first time, without the founder touching anything |
| 6–8 | **Looks-like + EVT** — carrier PCB, stand, box; 20 sets; all 8 experiments drafted | 20/20 sets pass a 2 m reflector test; teacher completes setup in <5 min from the box |
| 9–10 | **DVT + pre-compliance** — EMC pre-scan, safety review, worksheets reviewed by 2 teachers, translation | No pre-scan fails; worksheets pass teacher review; lab confirms toy directive not applicable for 14+ edu framing |
| 11–12 | **Pilot batch** — 50 sets (6 class packs) to schools/science centres, paid | ≥5 of 6 pilot sites run ≥3 lessons; ≥2 re-orders or referrals |

### Certification checklist (EU)

- **CE — RED** (24 GHz radar modules + Wi-Fi/BLE in the ESP32): EN 300 440 (24 GHz SRD), EN 300 328 (2.4 GHz), EN 301 489-1/-3/-17 (EMC), EN 62368-1 (safety), EN 62311/62479 (RF exposure). Using modules with their own test reports reduces work, but **the kit as a combination is your product** — the lab must assess it. Estimate €7–10k.
- **EN 18031-1** (RED delegated act cybersecurity, applies since 1 Aug 2025): the controller is internet-capable (Wi-Fi). If the kit only runs a local AP and never connects to the internet, discuss scope with the lab; plan €2–3k for the assessment anyway.
- **CRA:** reporting obligations from 11 Sep 2026, full application 11 Dec 2027 — SBOM, update mechanism, vulnerability contact. Simple because the device is local-only.
- **RoHS, REACH, WEEE** (register in each country you sell into), packaging EPR.
- **Toy Safety Directive/Regulation:** likely not applicable if designed and marketed for educational use under supervision for 14+. State it on the box and in the manual; get the lab's opinion in writing.
- **GDPR:** no personal data — radar positions are anonymous and stay in the classroom. Teacher-mode exports contain no names. Write that down; schools will ask.
- No battery (USB-powered) → no Battery Regulation issue.
- **Total estimate:** €10–14k.

### Validation toolkit

- **Kill question:** Will 10 physics teachers who see the demo at a teacher conference order a class pack within one budget cycle? Cheapest experiment: book a 20-minute workshop slot at a regional MNU/NVON-type meeting with 3 hand-built sets, take named "pilot interest" sign-ups with a €0 reservation and a written price.
- **Interview script (5):**
  1. Which topics in waves/oscillations do your students find most abstract, and how do you teach them now?
  2. Which experiment kit did you buy last, how much did it cost, and who approved it?
  3. How long does setup take before a kit is "too much hassle" for a 45-minute lesson?
  4. What runs on your school laptops/iPads — can students use Chrome, can you plug in USB devices?
  5. If this kit cost €849 for 8 sets with worksheets, would you buy this year, next year, or never — and what would make it "this year"?
- **Landing page:** Headline: "Radar your students can see." Bullets: "Live map of everyone in the room — in the browser, nothing to install." / "8 experiments with worksheets in English, German and Dutch." / "Class pack of 8 sets, ready in 5 minutes."
- **Pass:** 10 class-pack orders (or written purchase intent with a school stamp) within one budget cycle, or 20 science-centre/outreach set orders at full price in 3 months.

### First production checklist

- Samples: 5 of each radar module from two batches; check firmware version and protocol are identical.
- Golden sample: complete set incl. stand and box, signed off by a teacher, with a printed test protocol.
- DFM: carrier PCB with keyed connectors (students will plug things wrong); stand in one moulded part later.
- MOQ talk: radar modules usually sold per reel/tray — agree on 1,000 with a split delivery; AtomS3 through a distributor or direct.
- QC/AQL: 100% functional test (reflector at 2 m, both radars respond); AQL 1.0 cosmetic on packaging.
- Packaging: class box of 8, foam inserts, printed quick start + QR to worksheets; age/edu-use statement.
- Incoterms: FOB Shenzhen to start, kitting either in Shenzhen (cheaper) or in the EU (faster replacement parts).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R)](/db/hilink-ld2450.html) (24 GHz trajectory-tracking radar (up to 3 targets)); [HLK-LD2410B/LD2410C 24 GHz human-presence radar module](/db/hilink-ld2410b.html) (presence/micro-motion radar for the 'stillness' experiments). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack AtomS3 (C123)](/db/m5stack-atoms3.html) (ESP32-S3 controller with screen, serves the web app). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123) — for a Radar Physics Classroom Kit

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Radar Physics Classroom Kit: A classroom kit that makes radar visible: students see a live map of where classmates walk, measure Doppler speed of a pendulum and compare 24 GHz FMCW modules — with browser-based lessons, no software install. The design is built around your HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123).
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
主题：样品订购及批量报价 — HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123) — 用于Radar Physics Classroom Kit

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Radar Physics Classroom Kit：A classroom kit that makes radar visible: students see a live map of where classmates walk, measure Doppler speed of a pendulum and compare 24 GHz FMCW modules — with browser-based lessons, no software install。产品设计基于贵司的HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123)。
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
Subject: PCBA quote from open design files — Radar Physics Classroom Kit, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Radar Physics Classroom Kit: A classroom kit that makes radar visible: students see a live map of where classmates walk, measure Doppler speed of a pendulum and compare 24 GHz FMCW modules — with browser-based lessons, no software install. The design starts from published open-hardware files (HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Radar Physics Classroom Kit，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Radar Physics Classroom Kit：A classroom kit that makes radar visible: students see a live map of where classmates walk, measure Doppler speed of a pendulum and compare 24 GHz FMCW modules — with browser-based lessons, no software install。设计基于已公开的开源硬件文件（HLK-LD2450 24 GHz trajectory-tracking radar module (1T2R), HLK-LD2410B/LD2410C 24 GHz human-presence radar module, M5Stack AtomS3 (C123)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order 3 LD2450, 3 LD2410B and 3 AtomS3; get one live X/Y map in a browser via Web Serial. That demo is your whole sales pitch.
2. Ask two physics teachers you know for 30 minutes each with the interview script; ask them which teacher meeting or fair is next in their region.
3. Write experiment 1 ("Where am I?") as a one-page worksheet and test it with a teenager at home before you write the other seven.

Want help sourcing or building this? Talk to us via www.gongbans.com.
