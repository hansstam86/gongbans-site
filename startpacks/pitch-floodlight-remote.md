# Pitch Floodlight Remote (LoRa) — Founder Start Pack

> Coaches switch the training-pitch floodlights on and off from a key fob or phone, per field half, from up to a kilometre away. Automatic switch-off after training and a kWh log for the club treasurer.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** At many amateur clubs the floodlights are the biggest electricity bill, and they're switched by a key switch in a cabinet at the far end of the sports park. So the first coach turns on the whole pitch, the last coach forgets to turn it off, and the lights burn until the groundskeeper notices. Nobody knows what training costs in electricity.
- **Customer:** Amateur football, hockey and rugby clubs with 1–4 lit training pitches; municipalities and sports-park operators that own the lighting and pay (or recharge) the energy. The club board/treasurer or the municipality pays; coaches use it.
- **Product:** A controller for the existing floodlight contactor cabinet (M5Stack StamPLC-class PLC driving the contactor coils through its outputs), a LoRa link (HopeRF RFM95) to rugged key fobs for coaches, and optional LoRaWAN for app/phone control and reporting. Per-field-half scenes, auto-off timers, an optional link to the pitch booking calendar, run-hour and kWh reporting. The manual switch always stays.
- **Why now:** Energy prices made floodlights a board-level topic at clubs; many clubs have just retrofitted LED (which makes "on only when needed" instant, no warm-up). LoRa reaches across a sports park without trenching new control cables.
- **The ask:** About €90–110k (estimate) to the first 1,000 cabinets. Route: pilots with 5 clubs + a municipality, funded mostly by pre-orders and an energy-efficiency or sports-facility grant; a small angel top-up.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 5 clubs show >20% lower floodlight hours in a 2-month pilot? That number sells it to municipalities.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Amateur football, hockey and rugby clubs; municipalities that own sports parks.

**The problem as the pack states it:** At many amateur clubs the floodlights are the biggest electricity bill, and they're switched by a key switch in a cabinet at the far end of the sports park. So the first coach turns on the whole pitch, the last coach forgets to turn it off, and the lights burn until the groundskeeper notices. Nobody knows what training costs in electricity.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **DOSB (DE)** · https://www.dosb.de/ — German sports confederation; the regional Landessportbund reaches the clubs.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€349–499 per cabinet (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how amateur football, hockey and rugby clubs deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Who switches the pitch floodlights on and off today, how, and when were they last left burning all night?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Coaches switch the training-pitch floodlights on and off from a key fob or phone, per field half, from up to a kilometre away, with automatic switch-off after training and a kWh log for the club treasurer. On a scale of one to ten, how likely would you be to buy that at €349–499 per cabinet (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Pitch Floodlight Remote (LoRa): would you pay €349–499 per cabinet (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Pitch Floodlight Remote (LoRa): Coaches switch the training-pitch floodlights on and off from a key fob or phone, per field half, from up to a kilometre away, with automatic switch-off after training and a kWh log for the club treasurer. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €349–499 per cabinet (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Three people care. The **coach** wants light at 18:55 without a 400 m walk to the cabinet in the dark. The **treasurer** wants the energy bill down and wants to know which team uses what. The **municipality or sports-park operator** often pays the energy for public sports parks and wants proof that lights only burn in booked slots.

**First buyer: clubs that own their floodlights and pay their own electricity** (common in DE, NL, BE, AT). The board decides; a volunteer electrician or the club's regular electrical contractor installs. **Second buyer: municipalities** that run sports parks for many clubs. They buy in tenders, slower, but 10–50 cabinets at once, and they love a kWh-per-booked-hour report.

### Market size (estimates)
- Germany alone has roughly 24,000 football clubs (national association figures); the Netherlands, Belgium, Austria and Scandinavia add many more. Assume ~60,000 clubs/sports parks with lit pitches across EU + UK + NO + CH, averaging 1.5 controllable cabinets → **~90,000 cabinets**.
- **TAM:** 90,000 × €449 (cabinet kit + 4 fobs) ≈ **€40 M**, plus optional reporting software.
- **SAM:** DACH + Benelux, clubs that pay their own energy or municipal parks with energy budgets: ~35% → **~31,000 cabinets ≈ €14 M**.
- **SOM (3 years):** 4% of SAM → **~1,250 cabinets ≈ €560k**. Small market. This is a profitable niche product or a door-opener into broader sports-park energy control (clubhouse heating, hot water, irrigation pumps), not a big standalone business.

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| Lighting-maker connected systems (e.g. Philips PerfectPlay, Schréder ITERRA, Lumosa LumosaTouch; app control, multi-user rights) | Bundled with new LED floodlight projects; typically several thousand € per site | Tied to that maker's (DALI) luminaires and a new lighting project; overkill for a club that already has lights |
| GSM/4G relay boxes (call or SMS to switch) | €60–200 + SIM | No scenes, no auto-off logic, no reporting, needs mobile coverage at the cabinet |
| Timer switches in the cabinet | €30–100 | Training times vary; lights on in cancelled sessions |
| Long control cables to the clubhouse | €2–10k trenching | Expensive, not per-half, no reporting |
| Do nothing (walk to the cabinet) | Free | Lights left on, energy bill, safety walking in the dark |

**Wedge:** works with **any existing floodlights** (switches the contactors, doesn't care about the luminaire brand), **no trenching, no SIM**, key fob for coaches who don't want another app, and a treasurer's report. Price at a level a club board can approve without a tender (under €500).

### Product & value proposition
- **Cabinet controller:** StamPLC-class PLC (ESP32-S3-based) with outputs that drive the coils of the existing contactors per field half (via interposing relays where coil currents demand it), inputs reading the manual key switch position and contactor feedback, an RTC for schedules, and an RFM95 LoRa radio with an external antenna on the cabinet.
- **Coach fob:** RFM95-based, 4 buttons (half A, half B, full, off), LED confirms the cabinet's acknowledgement (two-way, so the coach knows it worked). Rolling counter + AES-encrypted frames so nobody else switches the lights. IP65.
- **Optional LoRaWAN/app:** LoRaWAN unit for scheduled reporting and remote switching via a network server (clubhouse gateway or public network). Note: LoRaWAN Class A downlinks are slow; for instant phone control, use Class C on the mains-powered cabinet, or BLE when standing near it.
- **Logic:** auto-off after N minutes (default 120) with a 5-min warning flash (lights dip or a beacon) before switch-off; "lights only in booked slots" mode linked to the club's pitch calendar; groundskeeper master key.
- **Reporting:** run hours per half per day × installed power (entered once) = kWh estimate; optional CT-clamp energy meter input for measured kWh; monthly PDF for the treasurer.

**Pricing (estimates):** Cabinet kit (controller + antenna + 4 fobs) €449; extra fob €29; reporting app €0 (local) or €5/cabinet/month (cloud + calendar link). Installation by the club's electrician (2–3 h), or a partner installer package €300.

### Unit economics (estimates per cabinet kit incl. 4 fobs, ex-VAT)
| Item | 1k kits | 5k kits |
|---|---|---|
| BOM: controller (PLC-class board, RFM95, RTC, interposing relays, DIN-rail PSU), antenna + cable, 4 fobs (RFM95, MCU, coin/AAA cells) | €78.00 | €62.00 |
| Assembly & test (controller I/O test, RF link test per fob, fob pairing) | €6.00 | €4.50 |
| Enclosures (DIN-rail case + 4 IP65 fob cases) | €7.00 | €4.50 |
| Packaging + installation guide + wiring labels | €3.00 | €2.00 |
| Freight + duty to EU | €3.00 | €2.00 |
| Certification amortised (~€25k: RED 868 MHz for 2 devices, EMC industrial, LVD for DIN-rail unit, EN 18031) | €25.00 | €5.00 |
| **Landed cost** | **€122.00** | **€80.00** |
| Net price ex-VAT: direct €377 (from €449) / via electrical wholesaler or installer ~€265 | €377 / €265 | €377 / €265 |
| **Gross margin** | **€255 (68%) direct / €143 (54%)** | **€297 (79%) / €185 (70%)** |

Margins are healthy because the price is value-based (one season's saved energy). The constraint isn't margin, it's market size and the slow sales cycle of volunteer boards.

### Go-to-market
**First 100 customers:**
- **Your own local clubs:** one pilot club, one season, publish the before/after floodlight hours. That number is the sales tool.
- **Regional football association club-services and energy advisers:** many associations run energy-saving programmes for clubs; get into their newsletters and webinars.
- **Club treasurers' networks and club-management software communities.**
- **Groundskeeper and sports-facility trade events** in DE/NL.

**Scale channels:** electrical installers that service sports parks, floodlight retrofit companies (sell it as an add-on to LED retrofits), municipal sports departments (framework agreements), and later the club-management/pitch-booking software vendors (calendar integration as a partnership).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill-question pilot: 5 clubs, simple logger (current clamp or contactor-state logger) for 4 weeks baseline, then works-like controller + fobs for 4 weeks; measure floodlight hours |
| Q2 | Custom controller + fob PCBs; encrypted two-way protocol; reporting v1; 20 EVT kits at clubs before the autumn season |
| Q3 | DVT; RED/EMC/LVD/EN 18031 testing; first municipal pilot (5 cabinets); booking-calendar link |
| Q4 | 300–1,000 kits produced for the winter season (peak floodlight use = peak buying motivation); installer partner programme |

**Team:** founder (club sales, association partnerships), 1 embedded engineer (LoRa protocol, PLC I/O, low-power fob), part-time electrician/installer adviser (wiring guides, liability), part-time web developer for reporting.

**Funding to the first 1,000 kits (estimates):** NRE €45k (controller + fob electronics €15k, firmware €18k, reporting €7k, enclosures €5k) + certification €25k + 1,000 kits landed ex-cert ~€97k + 9 months lean costs €30k ≈ **€197k**. But sell in tranches: build 300 for the first winter (~€29k) → cash need to the first 300 ≈ **€130k**, with the next 700 funded by sales and deposits. Route: club pre-orders (40% deposit), energy-efficiency / sports-facility grants where clubs can claim the controller, a small angel round (~€80–100k).

### Top risks
| Risk | Mitigation |
|---|---|
| **Safety/liability: controller in a mains contactor cabinet** | The controller only drives contactor coils at safe voltage via interposing relays; the manual switch remains and overrides; installation only by a qualified electrician with a wiring guide; product liability insurance |
| **Technical: LoRa range through stands, trees, metal cabinets** | External antenna on the cabinet; site survey with fobs before install; optional repeater |
| **Technical: lights switched off mid-training** | 5-min warning dip/flash, fob "extend" button, never switch off within booked slots |
| **Security: someone else switches the lights** | AES-encrypted frames with rolling counter, paired fobs, revoke lost fobs |
| **Market: small, volunteer-driven, seasonal** | Sell before autumn; association partnerships; expand to clubhouse heating/hot-water control later |
| **Market: lighting makers bundle controls into retrofits** | Brand-agnostic positioning; partner with retrofit installers rather than compete |
| **Supply: RFM95 and PLC board** | RFM95 is a widely second-sourced LoRa design (SX127x-class); production controller is your own PCB, the StamPLC is for the prototype |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF RFM95/96/98(W) LoRa module | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | LoRa radio for fob and cabinet: +20 dBm max, −144 dBm sensitivity, SPI, 16×16 mm | PCB footprint, demo code, datasheet, 3D model, CE/FCC reports | MIT (HopeRF repo) |
| M5Stack StamPLC (K141) | https://www.gongbans.com/db/m5stack-stamplc.html | PLC-style controller to prototype the cabinet unit (check its I/O and relay ratings against your contactor coils) | Enclosure/structure files only (main-board electronics not published) | Dev platform; production controller is your own design |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | LoRaWAN link for app control and reporting via a network server | Enclosure/structure files only | Dev unit |

### Block diagram
```
[Coach fob: RFM95 + MCU + 4 buttons + LED]  ~~ LoRa 868 MHz, encrypted, two-way ~~
                                                         |
                                                         v
[Cabinet controller: PLC-class MCU + RFM95 + RTC] --outputs--> [interposing relays] --> [existing contactors] --> [floodlights half A / half B]
         ^  inputs: manual key switch position, contactor feedback, optional CT clamp / energy meter
         |
         `-- LoRaWAN (Class C) --> [network server] --> [app: scenes, schedule, booking calendar, kWh report]
[manual key switch] --- always overrides (hard-wired) ---------------------------> [contactors]
```
**Engineering gap:** the encrypted two-way fob protocol with acknowledgements, safe I/O design for contactor cabinets (coil voltages vary: 24 V AC/DC or 230 V AC coils, hence interposing relays), the scene/timer/warning logic, booking-calendar sync, the reporting service, and an installation guide an electrician trusts.

### Starter BOM (estimates at 1k kits)
| Part | Est. cost | Notes |
|---|---|---|
| RFM95W module × 5 (cabinet + 4 fobs) | €17.50 | ~€3.50 each; SX127x-class, multiple sources |
| Cabinet MCU board (ESP32-S3 class, RTC, I/O protection) | €12.00 | Own PCB in production |
| Interposing relays (4×) + terminals | €10.00 | Rated for contactor coils, 230 V AC |
| DIN-rail PSU 230 V → 24/5 V | €8.00 | Pre-certified PSU simplifies LVD |
| External 868 MHz antenna + bulkhead cable | €6.00 | Mount outside the metal cabinet |
| Fob MCU, buttons, LED, battery holder, PCB (× 4) | €16.00 | Coin cell or 2× AAA |
| Optional CT clamp energy input | €6.00 | Upsell |

### Firmware/software starting point
- **LoRa:** the RadioLib library (Arduino/ESP-IDF, supports SX127x/RFM95) and HopeRF's demo code in the GitHub folder; LMIC-based stacks (search "MCCI LoRaWAN LMIC") for LoRaWAN.
- **Controller:** M5Stack's StamPLC examples (search the M5Stack docs/GitHub for "StamPLC") for prototyping; ESP-IDF in production.
- **Network server:** any LoRaWAN network server (public community networks or a self-hosted open-source server such as ChirpStack).
- **Encryption:** AES-128 with a rolling counter (mbedTLS is in ESP-IDF).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question baseline:** loggers on contactor state at 5 clubs for 2 weeks + interviews with treasurers. Pass: average lights-on time ≥25% above booked training time at ≥3 of 5 clubs |
| 3–5 | Works-like | StamPLC + RFM95 + 2 dev fobs switching a test contactor board; two-way acknowledge; range test across one real sports park ≥ 800 m |
| 6–8 | Looks-like + EVT | Custom controller + fob PCBs, DIN-rail case, IP65 fob; 10 kits installed at 5 clubs by electricians; install ≤ 3 h |
| 9–10 | DVT + pre-compliance | RED pre-scan (EN 300 220), EMC (industrial environment), LVD on the DIN-rail unit; 4-week run: floodlight hours down ≥20% vs baseline, zero unwanted switch-offs during booked slots |
| 11–12 | Pilot batch | 50 kits sold; municipal reference site signed; treasurer report shows € saved per month |

### Certification checklist (EU)
- **CE under RED** for both fob and controller: EN 300 220-1/-2 (868 MHz SRD; respect the sub-band duty cycle, e.g. 1% in the common 868.0–868.6 MHz sub-band), EMC EN 301 489-1/-3, safety EN 62368-1 or EN 61010/IEC 60730-class standards for the DIN-rail controller, RF exposure. Est. **€10–15k**.
- **LVD aspects:** the DIN-rail controller connects to 230 V coil circuits: creepage/clearance, relay ratings, and a clear installation manual. The cabinet itself remains the installer's responsibility under national wiring rules (e.g. VDE/NEN installation standards).
- **RED delegated act cybersecurity EN 18031-1** (internet-connected via LoRaWAN/app). Est. **€5–8k**.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: signed firmware updates (FUOTA over LoRaWAN is slow, so plan BLE local update too), SBOM, vulnerability policy.
- **RoHS, REACH, WEEE, packaging registration.**
- **Battery Regulation** for fob cells (primary coin/AAA: labelling and take-back obligations).
- **GDPR:** minimal; fob IDs linked to coaches are personal data if you name them. Use team names, not people.
- **Total estimate: €18–25k.**

### Validation toolkit
- **Kill question:** Do 5 clubs show >20% lower floodlight hours in a 2-month pilot? That number sells it to municipalities.
- **Cheapest experiment (~€200):** 5 contactor-state loggers (a current clamp or an auxiliary contact into a cheap LoRa or GSM logger) for 2 weeks per club, compared with the training schedule. The baseline gap alone tells you if the problem exists.
- **5-question interview (treasurer / board / groundskeeper):**
  1. What did the club pay for electricity last season, and what share is floodlights?
  2. Who switches the lights on and off today, and how often are they left on?
  3. Who owns the lights and the cabinet: the club or the municipality? Who pays the bill?
  4. What would it take for the board to approve €449 for this? Who signs?
  5. Do you have an electrician you trust to install it? A club volunteer?
- **Landing-page headline:** "Floodlights on from the pitch. Off when training ends."
  - Key fob for coaches, per field half, up to ~1 km. No cables, no SIM.
  - Auto-off after training, with a warning flash first.
  - Monthly kWh report for the treasurer.
- **Pass threshold:** 5 clubs agree to a paid pilot (€199 deposit, refundable if <15% savings), and ≥20% fewer floodlight hours at ≥3 of them.

### First production checklist
- **Samples:** RF range test of production fobs and controllers on a real pitch; relay life and coil-voltage tests (24 V AC, 230 V AC).
- **Golden sample:** controller with all I/O tested, fob pair, firmware version, measured RF output power.
- **DFM review:** terminal blocks and wiring labels, antenna bulkhead sealing, fob IP65 seal and button feel with gloves, battery door.
- **MOQ talk:** RFM95 reels, relays, DIN-rail enclosures (stock parts, no tooling), fob enclosure (tooling ~€5–8k for an IP65 fob).
- **QC/AQL:** AQL II 0.65 for safety-related items (relay function, isolation), 1.0/2.5 otherwise; 100% hi-pot test on the 230 V side; 100% RF link test with the paired fobs.
- **Packaging:** controller + 4 fobs pre-paired, antenna kit, electrician's wiring guide, treasurer's quick card.
- **Incoterms:** FCA Shenzhen; ship before September for the autumn season.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceivers in fob and cabinet). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack StamPLC (K141)](/db/m5stack-stamplc.html) (PLC controller for the floodlight contactor cabinet); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (LoRaWAN unit for phone/app control via a network). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868) — for a Pitch Floodlight Remote (LoRa)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Pitch Floodlight Remote (LoRa): Coaches switch the training-pitch floodlights on and off from a key fob or phone, per field half, from up to a kilometre away, with automatic switch-off after training and a kWh log for the club treasurer. The design is built around your HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868).
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
主题：样品订购及批量报价 — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868) — 用于Pitch Floodlight Remote (LoRa)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Pitch Floodlight Remote (LoRa)：Coaches switch the training-pitch floodlights on and off from a key fob or phone, per field half, from up to a kilometre away, with automatic switch-off after training and a kWh log for the club treasurer。产品设计基于贵司的HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868)。
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
Subject: PCBA quote from open design files — Pitch Floodlight Remote (LoRa), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Pitch Floodlight Remote (LoRa): Coaches switch the training-pitch floodlights on and off from a key fob or phone, per field half, from up to a kilometre away, with automatic switch-off after training and a kWh log for the club treasurer. The design starts from published open-hardware files (HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Pitch Floodlight Remote (LoRa)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Pitch Floodlight Remote (LoRa)：Coaches switch the training-pitch floodlights on and off from a key fob or phone, per field half, from up to a kilometre away, with automatic switch-off after training and a kWh log for the club treasurer。设计基于已公开的开源硬件文件（HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Call the treasurers of 5 local clubs: ask for last season's electricity bill and floodlight share; book 2 for a baseline logger.
2. Order 6 RFM95W modules, a StamPLC and a LoRaWAN unit; get an encrypted button press acknowledged across 500 m.
3. Ask one club electrician to review a draft wiring concept (interposing relays, manual override) before you design the controller PCB.

Want help sourcing or building this? Talk to us via www.gongbans.com.
