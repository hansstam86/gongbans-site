# Club Timing Gates — Founder Start Pack

> A pair of wireless laser gates plus a big display that time sprints, ski runs and agility courses to the millisecond, for €199 instead of €700–3,000.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Clubs and PE teachers time sprints with a stopwatch and a thumb (±0.2 s). Proper electronic timing starts at ~$540–700 for a basic set and runs to $2,500+ ([retailer listing, Brower TC/TCi](https://www.performbetter.com/Brower-TC-Timing-System/), [Freelap packs](https://store.simplifaster.com/product-category/freelap/freelap-athletic-timing-systems/)).
- **Customer:** Athletics, football, alpine-ski and dog-agility clubs; PE departments; personal trainers. Germany alone has ~86,000 sports clubs ([DOSB 2025](https://www.deutschland.de/en/topic/life/sports-clubs-statistics-germany)). Clubs pay from equipment budgets and grassroots grants; coaches use.
- **Product:** Two tripod-mount gates with modulated break-beam lasers, ESP-NOW time sync to ±1 ms, a readable LED-matrix display, battery for a full training day, optional phone app for results.
- **Why now:** Open ESP32-S3 battery stamp and an open P3 LED-matrix driver are in the catalogue; laser TX/RX units are cheap modules; grassroots sport funding is explicitly for equipment.
- **The ask:** ~€65k (estimate) to 1,000 sets. Route: pre-orders at athletics meets (the kill question) + bootstrap; a sports-federation partnership if the demo lands.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Demo at one regional athletics meet and take €199 pre-orders. 15 in a day = go.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a fake-door landing page that athletics, alpine-ski, football and dog-agility clubs across Europe actually visited, with a measured conversion to a waitlist or refundable deposit, plus the interview notes behind it. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Athletics, alpine-ski, football and dog-agility clubs across Europe; PE departments.

**The problem as the pack states it:** Clubs and PE teachers time sprints with a stopwatch and a thumb (±0.2 s). Proper electronic timing starts at ~$540–700 for a basic set and runs to $2,500+ ([retailer listing, Brower TC/TCi](https://www.performbetter.com/Brower-TC-Timing-System/), [Freelap packs](https://store.simplifaster.com/product-category/freelap/freelap-athletic-timing-systems/)).

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/trackandfield** · https://www.reddit.com/r/trackandfield/ — athletes and coaches.
- **DOSB (DE)** · https://www.dosb.de/ — German sports confederation; the regional Landessportbund reaches the clubs.
- **r/ScienceTeachers** · https://www.reddit.com/r/ScienceTeachers/ — secondary-school science teachers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (twenty people from the audience line), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€199–249, the pack's estimate), and one button. For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how athletics, alpine-ski, football and dog-agility clubs across Europe deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you time sprints or laps at training today, and what do you do with the times afterwards?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A pair of laser gates plus a display that time sprints, ski runs or agility courses to the millisecond, wireless, for €199 instead of €1,000+. On a scale of one to ten, how likely would you be to buy that at €199–249, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Club Timing Gates: would you pay €199–249 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Club Timing Gates: A pair of laser gates plus a display that time sprints, ski runs or agility courses to the millisecond, wireless, for €199 instead of €1,000+. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €199–249, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The buyer is the club's coach or equipment officer; the signature comes from the board. Budget per purchase: €150–300 without a committee, more needs a meeting. PE departments buy through school procurement (slow, but repeat). Dog-agility clubs are a surprisingly good niche: they run timed courses every weekend and currently rent or borrow timing gear. Alpine-ski clubs time kids' training runs on a slope with no power.

Users are coaches who set up in 2 minutes on grass or snow in the cold, with gloves. Everything about the product follows from that.

### Market size (estimates)
- Germany ~86k clubs; extrapolate EU + UK to **~500k sports clubs** (estimate). Timing-relevant disciplines (athletics, football/rugby/hockey conditioning, skiing, agility, cycling, swimming-dryland) maybe 30% → 150k clubs, plus ~60k secondary schools with PE.
- **TAM:** 210k × €219 ≈ **€46 M** (one set each).
- **SAM:** clubs with a budget and a coach who cares about speed training — 25% → 52k → **€11 M**.
- **SOM (3 years):** 6% of SAM → 3,100 sets → **€680k**. Plus accessories (extra gates, mats, reaction-start button) ~20% on top.

### Competition
| Alternative | Price (retail listings) | Weakness we attack |
|---|---|---|
| Wearable-chip timing systems (Freelap-class) | ~$665–695 basic pack, ~$2,500–2,700 pro ([retailer](https://store.simplifaster.com/brand/sprint-faster)) | Needs a chip per athlete; price |
| Photocell gate systems (Brower TC/TCi-class) | ~$540–1,765 depending on config ([Perform Better](https://www.performbetter.com/Brower-TC-Timing-System/)) | Price; proprietary displays |
| Pro light-barrier systems (Microgate Witty-class, ±0.4 ms) | Quote-only, used by universities ([TUM equipment sheet](https://www.hs.mh.tum.de/fileadmin/w00bbr/mh/Lehr-_Lernzentrum/Geraeteliste_NEU_2023/Witty_Lichtschranken_EN.pdf)) | Price; overkill for clubs |
| Phone-camera timing apps | Free–€30 | Needs a person per gate, ±50 ms, no display |
| Stopwatch / "do nothing" | €10 | ±200 ms, coach can't coach while timing |
| DIY Arduino gates (many web guides) | €40 parts | No sun immunity, no sync, no case |

**Wedge:** a finished, weather-tolerant €199–249 product with a display athletes can read from 30 m, no chips to lose, and a 2-minute setup. The dog-agility and ski niches are underserved and talkative.

### Product & value proposition
Set: 2 gates (each: modulated laser TX + RX with reflector option, ESP32-S3, 18650 cell, tripod thread, 10 h runtime), 1 display (64×32 P3 LED matrix, 18650 ×2 or USB-C PD, readable in daylight at 30 m), ESP-NOW mesh with ±1 ms sync, start modes (break-beam start, button start, reaction start with a tone), split times with up to 6 gates. App (BLE) optional for athlete lists and CSV export — v1 ships without it.

Pricing (estimates): **€219 B2C for the 2-gate + display set**, €249 with the app unlock and carry bag; extra gate €69; school/federation bundles (5 sets) at 15% off. B2B via sports-equipment dealers at 35–40% off RRP.

### Unit economics (estimates per set, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (3× ESP32-S3 module, laser TX/RX modules ×2, P3 matrix panel + driver, 3× 18650 + protection, chargers, PCBs) | €44.00 | €36.00 |
| Assembly & test (3 PCBAs, laser alignment, sync test) | €7.50 | €5.20 |
| Enclosure (2 gate housings, display housing, tripod inserts, reflectors; tooling amortised) | €9.80 | €6.40 |
| Packaging (carry case + box) | €4.50 | €3.20 |
| Freight + duty to EU (bulky; 3 lithium cells per set) | €5.50 | €3.30 |
| Certification amortised (~€25k: RED, EMC, 62368-1, laser class, UN 38.3) | €25.00 | €5.00 |
| **Landed cost** | **€96.30** | **€59.10** |
| Sell price (direct) | €219 | €219 |
| Channel margin (direct at 1k; 35% to dealers at 5k) | €0 | €76.65 |
| **Gross margin** | **€122.70 (56%)** | **€83.25 (38%, via dealers)** |

Direct sales keep the margin; dealers get you the schools. Mix accordingly.

### Go-to-market
**First 100 customers:** regional athletics meets and ski-club training camps with a live demo lane (the kill question: 15 pre-orders in a day), dog-agility weekends, coaching forums and speed-training YouTubers (send 10 sets), national coaching associations' newsletters. Schools via PE-teacher associations and their annual conferences.

**Scale channels:** sports-equipment dealers and catalogue suppliers to schools; federations (buy 50 for their youth programmes); grassroots-sport grant lists (clubs look for things to spend grants on — make the product grant-shaped with an invoice template).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from Laser TX/RX + Stamp-S3Bat + matrix driver; demo at 2 meets; pre-orders (kill question). |
| Q2 | Custom gate PCB, modulation + sunlight immunity, tooled housings, EVT 50 sets; laser classification; pre-compliance. |
| Q3 | DVT, certification, 300-set pilot batch to pre-order customers and 10 reviewers; app beta. |
| Q4 | 1,000 sets; two dealers; federation bundle; ski-season marketing. |

**Team:** 1 embedded engineer (ESP-NOW sync, optics, power — full-time), 1 mechanical/industrial designer (part-time), founder with a coaching network for sales and demos; app developer contracted. Two and a half people.

**Funding to first 1,000 sets (estimates):** NRE €40k (PCBs €8k, tooling €18k for 3 housings, optics/sync work €6k, app €8k) + certification €25k + 1,000 sets landed ~€71k + 9 months lean overhead €55k ≈ **€191k**; minus pre-orders (300 sets × €199 = €60k) and pilot sales ≈ **~€65k** net if the pre-orders come. Bootstrap + pre-orders; a federation deal or a sports-equipment dealer's prepayment replaces an angel.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** sunlight and snow glare blind the receiver | Modulated beam (kHz carrier) with synchronous detection; narrow optical bandpass; hood; test at noon on snow in week 4 |
| **Technical:** ±1 ms sync across ESP-NOW with 3+ nodes | Timestamp at the gate on the beam-break interrupt; exchange timestamps, not events; periodic clock-offset correction; characterise jitter early |
| **Market:** demand scored 2/5; small ticket, seasonal | Pre-order gate is strict (15 in a day); dog-agility and ski niches extend the season; accessories raise ticket size |
| **Regulatory:** laser classification and labelling (EN 60825-1); kids around beams | Class 1 if possible (eye-safe), Class 2 at most with labels; IR laser needs extra care — visible red is safer for alignment and classification; **state in the manual that it's not a toy** |
| **Regulatory:** BLE app → RED + EN 18031 | Ship v1 without BLE enabled; add the app SKU after certification |
| **Supply:** P3 LED matrix panels and 18650 cells vary batch to batch | Specify panel brand and binning; use branded cells with UN 38.3 reports |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit Laser TX (U066) | https://www.gongbans.com/db/m5stack-unit-laser-tx.html | Break-beam transmitter for the prototype | enclosure/structure only | Buy; redesign the optics yourself |
| M5Stack Unit Laser RX (U065) | https://www.gongbans.com/db/m5stack-unit-laser-rx.html | Break-beam receiver for the prototype | enclosure/structure only | Buy |
| M5Stack Stamp-S3Bat (S015) | https://www.gongbans.com/db/m5stack-stamp-s3bat.html | Open ESP32-S3 + battery node; ESP-NOW between gates | pcb, schematic (Altium) | M5Stack repo licence — check before copying |
| MATRIX LED 64×32 P3 driver board (OSHWHub) | https://www.gongbans.com/db/oshwhub-matrixled.html | Open P3 LED-matrix driver for the display | schematic, pcb (EasyEDA) | **OSHWHub project licence varies — read it; some are non-commercial** |

### Block diagram
```
GATE A: [laser TX, modulated] ===beam===> [photodiode RX + bandpass + comparator] -> [ESP32-S3 (Stamp-S3Bat)] 
GATE B: same                                                                                  |  ESP-NOW (timestamps)
DISPLAY: [ESP32-S3] -> [HUB75 driver (open matrix board)] -> [64x32 P3 panel]   <------------+
         [18650 x2 / USB-C PD]  [buzzer start tone]  [buttons]  (option: BLE -> phone app)
```
**Engineering gap:** the catalogue parts give you unmodulated laser units and a matrix driver. Missing: a modulated, sunlight-immune beam path (optics, filter, synchronous detection), the sync protocol, rugged tripod-mount housings, a daylight-readable display power budget, and the laser classification file. Optics and timing are the work.

### Starter BOM (estimates per set at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 module ×3 | €7.50 | Pre-certified |
| Laser diode module (visible red, <1 mW) ×2 + driver with modulation | €3.00 | Class 1/2 depends on power and aperture — buy with a power spec |
| Photodiode + optical bandpass + TIA/comparator ×2 | €3.20 | Filter is the sunlight-immunity part |
| 64×32 P3 LED matrix panel | €9.50 | Specify brand; brightness ≥ 1,500 nits for daylight |
| HUB75 driver (from the open board) | €1.80 | |
| 18650 cells ×3 + protection + chargers | €9.00 | Branded, UN 38.3 report |
| PCBs ×3 | €3.00 | |
| Housings ×3 + tripod inserts + reflectors | €9.80 | **Tooling €15–20k**; printed for the first 50 |
| Carry case | €4.50 | Off-the-shelf blow-moulded case with cut foam |

### Firmware/software starting point
- ESP-IDF with ESP-NOW (Espressif's own protocol, documented and with examples in esp-idf).
- Matrix display: the ESP32-HUB75-MatrixPanel-DMA library (exists on GitHub) drives P3 panels from an ESP32.
- Sync: write your own — a few hundred lines of timestamp exchange; search "ESP-NOW time synchronization" for prior art.
- App (later): BLE GATT + a simple Flutter/React Native app; or skip the app and export CSV over USB.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Prototype from Laser TX/RX + Stamp-S3Bat + matrix board; demo lane at a regional athletics meet or agility weekend; **15 pre-orders at €199 in a day** = go |
| 3–5 | Works-like | Modulated beam works in direct noon sun at 5 m gate width; sync jitter < 1 ms measured with a scope across 3 nodes; 8 h runtime |
| 6–8 | Looks-like + EVT | Custom gate PCB, printed/CNC housings with tripod mounts; 20 sets; drop test 1 m onto grass and tarmac; display readable at 30 m in sun; EMC pre-scan |
| 9–10 | DVT + pre-compliance | Laser classification measurement and labels (EN 60825-1); RED/EMC pre-compliance; UN 38.3 reports; cold test at −10 °C (ski clubs) |
| 11–12 | Pilot batch | 50 sets to pre-order customers; ≤ 2 field failures; 10 coach testimonials; reorder/extra-gate attach rate measured |

### Certification checklist (EU)
- **CE under RED** (ESP-NOW is WiFi-band radio): EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** safety incl. laser clauses; **EN 60825-1** laser classification (aim for Class 1; Class 2 requires labels and visible wavelength). Est. €6–9k RED/EMC, €3–5k safety, €2–4k laser measurement/report.
- **EN 18031-1** only if internet-connected; a gate-to-display ESP-NOW link with no internet and no app is arguably out of scope — confirm with your assessor; the BLE-app SKU is in scope (~€8–15k). That is why v1 ships without the app.
- **RoHS, REACH, WEEE.** **Battery Regulation (EU) 2023/1542** + **UN 38.3** for the cells; 18650 in a holder = user-removable, good.
- **CRA:** firmware-bearing product; reporting from 11 Sept 2026, full from 11 Dec 2027; low burden without connectivity — document.
- **GDPR:** athlete names in the app = personal data (children!). Keep names local to the phone; no cloud in v1.
- **Toy directive:** not a toy — but it will be used by children; say "not a toy, adult supervision" and keep laser Class 1 so it doesn't matter.
- **Total certification budget estimate: €18–25k (v1), +€10–15k for the app SKU.**

### Validation toolkit
- **Kill question:** Demo at one regional athletics meet and take €199 pre-orders. 15 in a day = go.
- **Cheapest experiment (~€350):** Laser TX/RX + 2× Stamp-S3Bat + matrix board on two camera tripods and a battery pack; a Stripe pre-order link on a QR poster; a lane next to the warm-up area with permission.
- **5-question interview (coach):** 1) How do you time sprints today, and how much do you trust the numbers? 2) Have you priced electronic timing? What stopped you? 3) How many athletes per session, and how many splits do you want? 4) Where do you train — grass, track, snow, indoors — and who carries the kit? 5) At €199–249, who signs, and would a grant pay for it?
- **Landing page:** headline "Millisecond timing for the price of a pair of spikes." Bullets: "Two wireless laser gates and a display you can read from 30 m." / "Set up in 2 minutes on track, grass or snow — no chips, no wires." / "€219. Add gates for splits; results on your phone (coming soon)."
- **Pass threshold:** 15 pre-orders in one demo day, or 100 pre-orders at €199 from a 4-week campaign.

### First production checklist
- Samples: 5 golden sets, each with beam power measured and logged (laser class file), sync jitter recorded.
- DFM: lens/filter alignment features in the housing, tripod insert torque, battery door with gloves, panel mounting without hot spots.
- MOQ talk: panels 500–1k; housings 1k per part; cells 3k (3 per set). Ask for the 5k step.
- QC: AQL II 2.5/4.0; 100% beam power test (laser class), 100% sync test on a jig, 100% charge test; 2% cold-chamber sample.
- Packaging: foam-cut case; drop test ISTA 1A; lithium labels.
- Incoterms: FOB Shenzhen; bulky + lithium → sea freight even at 1k; plan 8 weeks door to door.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Laser TX (U066)](/db/m5stack-unit-laser-tx.html) (break-beam transmitter); [M5Stack Unit Laser RX (U065)](/db/m5stack-unit-laser-rx.html) (break-beam receiver); [M5Stack Stamp-S3Bat (S015)](/db/m5stack-stamp-s3bat.html) (open ESP32-S3 + battery node; ESP-NOW between gates). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [MATRIX LED 64*32 P3 全彩显示屏驱动板](/db/oshwhub-matrixled.html) (open P3 LED-matrix driver for a big readable time display).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit Laser TX (U066), M5Stack Unit Laser RX (U065), M5Stack Stamp-S3Bat (S015) — for a Club Timing Gates

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Club Timing Gates: A pair of laser gates plus a display that time sprints, ski runs or agility courses to the millisecond, wireless, for €199 instead of €1,000+. The design is built around your M5Stack Unit Laser TX (U066), M5Stack Unit Laser RX (U065), M5Stack Stamp-S3Bat (S015).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Laser TX (U066), M5Stack Unit Laser RX (U065), M5Stack Stamp-S3Bat (S015).
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
主题：样品订购及批量报价 — M5Stack Unit Laser TX (U066), M5Stack Unit Laser RX (U065), M5Stack Stamp-S3Bat (S015) — 用于Club Timing Gates

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Club Timing Gates：A pair of laser gates plus a display that time sprints, ski runs or agility courses to the millisecond, wireless, for €199 instead of €1,000+。产品设计基于贵司的M5Stack Unit Laser TX (U066), M5Stack Unit Laser RX (U065), M5Stack Stamp-S3Bat (S015)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Laser TX (U066), M5Stack Unit Laser RX (U065), M5Stack Stamp-S3Bat (S015)。
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
Subject: PCBA quote from open design files — Club Timing Gates, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Club Timing Gates: A pair of laser gates plus a display that time sprints, ski runs or agility courses to the millisecond, wireless, for €199 instead of €1,000+. The design starts from published open-hardware files (MATRIX LED 64*32 P3 全彩显示屏驱动板; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Club Timing Gates，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Club Timing Gates：A pair of laser gates plus a display that time sprints, ski runs or agility courses to the millisecond, wireless, for €199 instead of €1,000+。设计基于已公开的开源硬件文件（MATRIX LED 64*32 P3 全彩显示屏驱动板；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 2× Unit Laser TX, 2× Unit Laser RX, 3× Stamp-S3Bat and fabricate the open matrix driver board; buy a P3 panel and two cheap tripods.
2. Find the next regional athletics meet or agility weekend within 6 weeks and ask the organiser for a demo lane.
3. Read the OSHWHub matrix project's licence and M5Stack's repo licence; if either is non-commercial, note that you're redrawing your own HUB75 driver (it is a small board).

Want help sourcing or building this? Talk to us via www.gongbans.com.
