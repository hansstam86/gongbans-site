# EU-Brand Camera Pet Feeder — Founder Start Pack

> A ready reference design for European pet brands: a portion-controlled dry-food feeder with a 2 MP camera, two-way audio and bowl weighing, so a pet-food or accessories brand can launch its own connected feeder in months.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

**This is a B2B design business, not a consumer gadget.** You don't fight the big Asian feeder brands on Amazon. You sell a finished, certifiable design (plus production) to a European pet brand that wants its *own* connected feeder. The go/no-go is not the hardware. It is whether a brand's legal team accepts a Tuya-cloud camera in EU homes, or pays for the Tuya-free version.

## 1. Summary

- **Problem:** European pet-food and pet-accessory brands see connected feeders selling well, but under Asian brands that own the app, the customer data and the relationship. Building a camera feeder in-house takes 18+ months and a firmware/cloud team they don't have. Private-label "white box" feeders exist, but they come with someone else's app and unclear data handling.
- **Customer:** Mid-sized European pet-food brands (premium dry food especially), pet-accessory brands, pet retail chains' own labels. The brand pays (NRE + per-unit), its customers use it.
- **Product:** A reference design and production package: dry-food hopper with an auger, jam detection, a 2 MP camera with two-way audio (Tuya PET103-W02 core board), bowl weighing ("ate / didn't eat"), local schedule that keeps feeding without Wi-Fi, and a branded app via Tuya's white-label tools. A Tuya-free variant for brands that want their own cloud.
- **Why now:** Connected feeders are a fast-growing pet category. Brands want direct-to-consumer data (what does the pet eat, when does the bag run out → subscription refills). A camera core board designed specifically for feeders exists off the shelf.
- **The ask:** About €150–250k (estimate) of working capital, mostly covered by brand NRE (€60–120k per brand) and the first production order. This is an ODM-style business: get the first brand's purchase order before you scale.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will one EU pet brand sign a design contract — and is their legal team OK with a Tuya-cloud camera product in EU homes? That's the go/no-go, not the hardware.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** European pet-food and pet-accessory brands, pet retail chains' own labels.

**The problem as the pack states it:** European pet-food and pet-accessory brands see connected feeders selling well, but under Asian brands that own the app, the customer data and the relationship. Building a camera feeder in-house takes 18+ months and a firmware/cloud team they don't have. Private-label "white box" feeders exist, but they come with someone else's app and unclear data handling.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **FEDIAF, European Pet Food** · https://europeanpetfood.org/ — European pet-food industry federation; its members are the brands.
- **Interzoo (Nuremberg)** · https://www.interzoo.com/ — the main European pet-industry trade fair; exhibitor list = buyer list.
- **r/cats** · https://www.reddit.com/r/cats/ — cat owners.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€129–179 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how European pet-food and pet-accessory brands, pet retail chains' own labels deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Has your brand looked at selling a connected feeder or other device, and what stopped you or went wrong when you tried?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A ready reference design for European pet brands: a portion-controlled dry-food feeder with a 2 MP camera, two-way audio and bowl weighing — so a pet-food or accessories brand can launch its own connected feeder in months. On a scale of one to ten, how likely would you be to buy that at €129–179 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: EU-Brand Camera Pet Feeder: would you pay €129–179 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a EU-Brand Camera Pet Feeder: A ready reference design for European pet brands: a portion-controlled dry-food feeder with a 2 MP camera, two-way audio and bowl weighing — so a pet-food or accessories brand can launch its own connected feeder in months. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €129–179 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The buyer is the **head of product / digital at a European pet-food or accessory brand**. Their real goal is not a feeder; it is **a refill subscription and data on feeding behaviour**. The feeder knows when the hopper runs low → the brand ships the next bag. Pitch the feeder as a *channel*.

Secondary buyer: **pet retail chains' private labels** (they want margin and an own-brand "smart" range).

The user: cat and small-dog owners who are out at work or travel, plus multi-pet homes where one pet steals food (camera + weight helps).

### Market size (estimates)
- EU has roughly 125–130 M cats and dogs (order of magnitude from pet-industry federation reporting — check the latest). Assume 3% of pet homes buy a connected feeder in the next 5 years, ~1 feeder each → **~3 M units → TAM ~€450 M** at €149.
- **SAM:** the share sold under European brands' own labels if they had a product: assume 10% → **~€45 M over 5 years**.
- **SOM:** 2–3 brand customers, 10–20k units/year each by year 3 → **€1.5–4 M/year** in unit sales to brands (at ~€60–75 per unit ex-works + NRE).

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Camera feeders from large Asian pet-tech brands | €90–200 retail | Brand owns the app and the customer; a European brand can't use them for its own subscription |
| White-label feeders from Shenzhen ODMs with a stock app | €35–60 ex-works | Stock app, little control over data processing, generic look, weak EU compliance files |
| Brand builds in-house | €500k+ and 18+ months | Most pet brands have no hardware/firmware team |
| Non-camera timed feeders | €40–80 | No "did my pet eat" information |
| Do nothing: brand sells only food | — | Loses the D2C data and subscription channel |

**Wedge:** **"your brand, your app, EU compliance done"** — an industrial design adaptable to the brand, a **compliance file** (RED, LVD, EMC, CRA/EN 18031, food-contact, GDPR/DPA documentation) and **two cloud options**: Tuya white-label (fast, cheaper) or Tuya-free (brand-owned/EU cloud).

### Product & value proposition
- **Camera/Wi-Fi core:** Tuya PET103-W02 — 2 MP camera core board, Wi-Fi 4 2.4 GHz, AK3918EV330L, 38 × 38 mm, debug/user UART, speaker, mic, IR-cut, IR LED and microSD interfaces, designed for pet feeders and litter boxes (per Tuya's public datasheet).
- **Feeder controller:** small MCU on the motor board: auger motor driver (Seeed Grove-I2C Motor Driver as the prototype reference), jam detection (motor current + optical portion sensor), hopper-level sensor, real-time clock + local schedule, desiccant chamber.
- **Bowl weighing:** load cell + bridge ADC (M5Stack Weight-I2C unit for the prototype) → "ate / didn't eat / how much".
- **Power:** 5 V adapter + 3× D-cell or Li-ion backup for feeding during outages (camera off on battery).
- **App (Tuya route):** Tuya's white-label app and cloud: live view, two-way audio, schedule, feeding log, low-food alert → hook for the brand's refill shop.
- **Tuya cloud dependency explained:** with the PET103 core, video streaming, remote access, the app and OTA updates run through Tuya's cloud platform. Local feeding continues without internet; the camera and app do not. **Tuya-free alternative:** replace the PET103 with a camera SoC module you control (several Shenzhen camera-SoC vendors offer feeder/IPC reference boards) and run the brand's own back-end, or a third-party EU-hosted IoT/video platform. That costs ~3–6 months and €100–200k more NRE, but the brand owns the data path.

**Pricing (estimates):** to brands: NRE €60–120k (design adaptation, branding, certification) + €62–75 per unit ex-works at 5k units. Brand retail price €129–179, often bundled with a food subscription.

### Unit economics (estimates per unit, ex-VAT; ex-works price to brand)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (PET103-W02, motor board + MCU, auger motor, load cell + ADC, sensors, IR LEDs, speaker/mic, backup battery holder, cables) | €34.00 | €27.00 |
| Assembly & test (camera, audio, auger cycle, scale calibration) | €5.00 | €3.50 |
| Enclosure + hopper + bowl (food-contact plastics, stainless bowl) | €10.00 | €7.00 |
| Adapter (certified) | €2.50 | €1.90 |
| Packaging (retail box, brand print) | €3.00 | €2.00 |
| Freight + duty to EU (bulky) | €4.50 | €3.50 |
| Certification amortised (~€35k, normally paid via NRE → shown here for honesty) | €35.00 | €7.00 |
| **Landed cost** | **€94.00** | **€50.90** |
| Price to brand (ex-works + freight) | €85 + NRE | €70 |
| **Gross margin** | **NRE-dependent (loss on units at 1k unless NRE covers certification)** | **€19.10 (27%)** |

ODM margins are thin; the NRE carries the early phase. Keep certification in the NRE quote.

### Go-to-market
**First customers (B2B: 2–3 brands = first 10–20k units):**
- **Target list of 40 European pet brands** (premium dry food, D2C pet-food startups, accessory brands, retail private labels). Lead with the refill-subscription business case, not the camera.
- **Pet-industry trade fairs** (the big European pet trade fair in Nuremberg and national ones) — show a working, brandable feeder with a demo app in their colours.
- **D2C pet-food startups** are the fastest decision-makers: smaller teams, digital-first, subscription models already.

**Scale:** each brand becomes a repeat customer (new versions every 18–24 months); retail private-label tenders.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: 10 brand conversations, 1 signed design contract or paid feasibility; legal/DPO review of the Tuya route with that brand |
| Q2 | Works-like (PET103 + auger + scale), demo app in brand colours; brand user test with 20 pet homes |
| Q3 | Looks-like + EVT/DVT; certification; food-contact testing |
| Q4 | First production run 2–5k units for brand #1; brand #2 in design |

**Team:** founder (B2B sales into consumer brands), 1 mechanical engineer (augers and jams are the hard part — kibble varies), 1 embedded/app integrator (Tuya platform, later own back-end), a Shenzhen production partner. Compliance consultant for food-contact + CRA.

**Funding (estimates):** pre-NRE work to a convincing demo €60k; then per brand: NRE €60–120k paid 50% at signing / 50% at DVT, production paid 30% deposit / 70% before shipping. Working capital needed ≈ **€150–250k** to bridge deposits and the demo. Route: founder capital + brand NRE + trade finance for production; avoid equity until 2 brands are signed.

### Top risks
| Risk | Mitigation |
|---|---|
| **Tuya cloud / GDPR / data residency:** a camera with mic in EU homes, video and audio processed via a Chinese-headquartered platform; brand = controller, Tuya = processor | Offer the Tuya-free route; for Tuya route: brand signs a DPA with Tuya, verifies the EU data region and subprocessors, runs a DPIA, privacy-by-default (camera off/privacy shutter, no cloud recording by default) |
| **CRA / EN 18031:** connected camera = high scrutiny (default passwords, updates, data protection) | Security-by-default settings, signed OTA, documented update support period; check whether Tuya provides the CRA/EN 18031 evidence you need |
| **Technical:** kibble jams, different kibble sizes, humidity | Auger designed for 2–15 mm kibble; jam detection + reverse; test 10 kibble types (the brand's own first) |
| **Market:** brand says yes in the meeting, then legal stalls | Make the DPO review part of the kill question in month 1 |
| **Regulatory:** food-contact materials (hopper, bowl) | Food-contact plastics with declarations of compliance; stainless bowl |
| **Supply:** PET103 is Tuya-only; camera SoC sole source | Keep the Tuya-free design path documented; multi-source motors and load cells |
| **Animal welfare/liability:** pet not fed due to a failure | Battery backup, jam alerts, "missed meal" alarm; clear "not a replacement for care" statement |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Tuya PET103-W02 Wi-Fi camera core board | https://www.gongbans.com/db/tuya-pet103-w02.html | 2 MP camera, Wi-Fi, audio I/O, IR-cut, microSD — designed for feeders | **Datasheet public, files via maker** (no open schematic/PCB) | Tuya platform terms; cloud dependency |
| M5Stack Unit Weight-I2C (U180) | https://www.gongbans.com/db/m5stack-unit-weight-i2c.html | Bowl weighing for the prototype | Enclosure/structure files only — main-board electronics not published | Prototype only; own ADC design for production |
| Seeed Grove-I2C Motor Driver V1.3 | https://www.gongbans.com/db/seeed-grove-i2c-motor-driver-v1-3.html | Auger motor driver reference | Schematic | Check Seeed's licence for the wiki design files |

### Block diagram
```
                     [Tuya PET103-W02: camera, Wi-Fi, mic, speaker, IR] ~~Wi-Fi~~> [Tuya cloud] -> [brand app]
                                    | UART (feed commands, status)                    (or Tuya-free: own camera SoC -> brand EU cloud)
[RTC + local schedule] -> [feeder MCU] --PWM--> [motor driver] -> [auger motor]
                              |<-- motor current (jam) / portion IR sensor / hopper level
                              |<-- [load cell + bridge ADC] (bowl weight)
            [5 V adapter] + [battery backup: feeding continues, camera off]
```
**Engineering gap:** the feeder mechanics (auger, jam handling, desiccant, cleanable hopper), the UART protocol between the Tuya core and the feeder MCU (Tuya's MCU-SDK model), bowl-weight logic, food-contact material selection, and the Tuya-free variant if a brand wants it.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Tuya PET103-W02 | €12–16 | **Sole-source (Tuya)**; price and MOQ via Tuya sales |
| Feeder MCU + motor driver + RTC | €2.00 | |
| Auger motor (gear motor, 5 V) | €3.00 | Lifetime test at 10k cycles |
| Load cell + 24-bit ADC | €2.50 | |
| IR portion sensor, hopper-level sensor | €1.20 | |
| Speaker + mic (if not on core) + IR LEDs | €1.50 | |
| Battery holder / backup circuit | €1.50 | |
| Hopper, bowl (stainless), enclosure | €10.00 | Tooling €25–40k (several large parts) |

### Firmware/software starting point
- **Tuya route:** Tuya's developer platform (product creation, panel/app white-label, "MCU SDK" for the feeder MCU talking to the Tuya module over UART). Requires a Tuya developer account; use Tuya's pet-feeder product category templates.
- **Feeder MCU:** any Cortex-M with a simple scheduler; search "Tuya MCU SDK" for the serial protocol implementation.
- **Tuya-free route:** search for camera-SoC IPC SDKs from your chosen vendor; for streaming, WebRTC-based stacks (e.g. search "libpeer WebRTC embedded"); an EU-hosted back-end of the brand's choice.
- **Bowl scale:** search "HX711 library"; implement "meal event" detection (weight drop while pet present).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill test:** one EU pet brand signs a design contract or a paid feasibility (≥€10k), *and* their legal/DPO gives written feedback on the Tuya-cloud route (yes / yes-with-conditions / Tuya-free only) |
| 3–5 | Works-like | PET103 + auger rig + scale; 1,000 feeding cycles with the brand's kibble, ≤1 jam unrecovered; live view + two-way audio in a demo app |
| 6–8 | Looks-like + EVT | Brand-styled enclosure (3D-printed/CNC), 20 units in pet homes for 3 weeks; "ate / didn't eat" correct ≥90% |
| 9–10 | DVT + pre-compliance | RED/EMC/LVD pre-scan, EN 18031 gap analysis, food-contact declarations from material suppliers, drop test, 10k-cycle auger life test |
| 11–12 | Pilot batch | 50 units with the brand's beta customers; refill-subscription link tested; <5% returns |

### Certification checklist (EU)
- **CE under RED:** EN 300 328 (Wi-Fi 2.4 GHz), EN 301 489-1/-17, EN 62368-1 (safety, plus the adapter's own CE), EN 62311. Est. **€10–15k**.
- **RED delegated act — EN 18031-1/-2 (mandatory since 1 Aug 2025 for internet-connected radio equipment):** -1 network protection, -2 personal data (camera + mic). Notified-body involvement may be required if you deviate from the harmonised standard. Est. **€8–15k** incl. consultant.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. A home camera is the kind of product CRA scrutiny focuses on: secure defaults, updates for the support period, SBOM (incl. Tuya components), vulnerability handling. Clarify with Tuya who provides what evidence.
- **Food contact:** Regulation (EC) 1935/2004, plastics Regulation (EU) 10/2011 with declarations of compliance + migration tests for hopper and bowl. Est. **€3–6k**.
- **RoHS, REACH, WEEE**, packaging registration (per country).
- **Battery Regulation (EU) 2023/1542** if a rechargeable backup is included (or design for user-supplied D cells).
- **GDPR:** brand is controller; DPIA (video + audio in homes); DPA with Tuya (or own cloud provider); data location; retention; privacy shutter or camera-off switch.
- **Total certification estimate: €25–40k** (normally recovered via NRE).

### Validation toolkit
- **Kill question:** Will one EU pet brand sign a design contract — and is their legal team OK with a Tuya-cloud camera product in EU homes?
- **Cheapest experiment (~€1,500):** one working prototype (PET103 dev kit + a modified off-the-shelf feeder mechanism) + a 10-slide business case "feeder → refill subscription" with a demo app skinned in the target brand's colours. Pitch to 10 brands.
- **5-question interview (brand):** 1) Do you have a D2C subscription today, and what's its churn? 2) Would you launch a connected feeder under your brand? Why not yet? 3) Who in your company must approve a camera product (legal, DPO, IT security)? 4) Cloud: is a Tuya-based app acceptable, or must data stay in your own/EU cloud? 5) What volume and retail price would make it worth it for you?
- **Landing page headline (for brands):** "Your own connected pet feeder. Your app. EU compliance done." Bullets: "Camera, two-way audio and bowl weighing, adapted to your brand." / "Feeding data and refill alerts that drive your food subscription." / "Fast-track Tuya version or fully brand-owned EU cloud."
- **Pass threshold:** one signed contract or paid feasibility ≥€10k, plus a written DPO position that allows at least one of the two cloud routes.

### First production checklist
- **Samples:** PET103 samples from Tuya with the production firmware; auger motor life-tested; food-contact declarations collected before tooling.
- **Golden sample:** brand-approved and signed (colour, logo, packaging) — the brand signs, not you.
- **DFM review:** hopper draft angles and sealing (kibble dust), cleanability (dishwasher-safe bowl), cable routing, camera window (anti-fog, IR reflection).
- **MOQ talk:** Tuya module MOQ, plastic colour (brand colours = custom masterbatch MOQ), retail packaging print runs.
- **QC/AQL:** AQL II 1.0/2.5; 100% camera/audio/Wi-Fi test, 100% auger cycle test, 100% scale calibration; 10k-cycle reliability on a sample per lot.
- **Packaging:** brand retail box, multilingual quick start, privacy notice, refill-subscription insert.
- **Incoterms:** FOB Shenzhen or DDP to the brand's EU warehouse (brands usually prefer DDP — price it in).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Tuya Smart (涂鸦智能) and M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Tuya Smart (涂鸦智能)** (涂鸦智能模组部门, developer.tuya.com) — platform + module maker; 151 boards in the catalogue; files via Tuya Smart public module documentation · https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber. Directory entry: WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side. Boards used here: [Tuya PET103-W02 Wi-Fi module](/db/tuya-pet103-w02.html) (2 MP Wi-Fi camera core board designed for pet feeders). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Weight-I2C (U180)](/db/m5stack-unit-weight-i2c.html) (bowl weighing (did the pet actually eat?)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-I2C Motor Driver V1.3](/db/seeed-grove-i2c-motor-driver-v1-3.html) (auger motor driver reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Tuya Smart (涂鸦智能) and M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3 — for a EU-Brand Camera Pet Feeder

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a EU-Brand Camera Pet Feeder: A ready reference design for European pet brands: a portion-controlled dry-food feeder with a 2 MP camera, two-way audio and bowl weighing — so a pet-food or accessories brand can launch its own connected feeder in months. The design is built around your Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3.

Could you please send:
1. Price and lead time for [10] sample units of each: Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3.
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
主题：样品订购及批量报价 — Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3 — 用于EU-Brand Camera Pet Feeder

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款EU-Brand Camera Pet Feeder：A ready reference design for European pet brands: a portion-controlled dry-food feeder with a 2 MP camera, two-way audio and bowl weighing — so a pet-food or accessories brand can launch its own connected feeder in months。产品设计基于贵司的Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3。

请提供以下信息：
1. 各[10]片样品的单价和交期：Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3。
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
Subject: PCBA quote from open design files — EU-Brand Camera Pet Feeder, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a EU-Brand Camera Pet Feeder: A ready reference design for European pet brands: a portion-controlled dry-food feeder with a 2 MP camera, two-way audio and bowl weighing — so a pet-food or accessories brand can launch its own connected feeder in months. The design starts from published open-hardware files (Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — EU-Brand Camera Pet Feeder，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款EU-Brand Camera Pet Feeder：A ready reference design for European pet brands: a portion-controlled dry-food feeder with a 2 MP camera, two-way audio and bowl weighing — so a pet-food or accessories brand can launch its own connected feeder in months。设计基于已公开的开源硬件文件（Tuya PET103-W02 Wi-Fi module, M5Stack Unit Weight-I2C (U180), Seeed Grove-I2C Motor Driver V1.3；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Request PET103-W02 samples and the datasheet/MCU-SDK documentation via Tuya's developer platform.
2. Build a target list of 40 European pet brands with D2C subscriptions; prepare the "feeder → refill subscription" business case.
3. Write a one-page data-flow diagram (Tuya route vs Tuya-free route) that a brand's DPO can review in 10 minutes.

Want help sourcing or building this? Talk to us via www.gongbans.com.
