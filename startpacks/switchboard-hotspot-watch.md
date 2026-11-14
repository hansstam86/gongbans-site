# Switchboard Hot-Spot Watch — Founder Start Pack

> A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** About a quarter of building fires have an electrical origin (European Fire Academy estimate as cited by [Schneider Electric](https://www.electrical-installation.org/enwiki/State-of-the-art_solutions_for_electrical_fire_prevention,_beyond_the_standards)); the standard defence is one thermographic inspection a year by a person with a handheld camera. Loose terminals heat up in weeks, not years. Continuous thermal monitoring exists — for switchgear rooms, at switchgear prices.
- **Customer:** Facility managers and electrical contractors maintaining commercial and multi-tenant residential distribution boards in the EU; property owners and insurers who pay for the risk. The owner/FM pays; the electrician installs; the insurer asks for the report.
- **Product:** A €349 DIN-clip thermal watcher: a 32×24 thermal array looking across the board's breakers and busbars, per-zone baselines and ΔT alarms, powered from the board's auxiliary 24 V or a small supply, LoRaWAN or WiFi uplink, a monthly thermal report PDF for the insurer. Installed by the electrician in 15 minutes.
- **Why now:** Low-resolution thermal arrays (MLX90640-class) are cheap and good enough to see a breaker 15 K above its neighbours; an open thermal + visual camera design exists; LoRaWAN is standard in commercial buildings; insurers are actively pushing electrical fire prevention.
- **The ask:** ~€120k (estimate) to the first 1,000 units; route = paid contractor pilots + bootstrap; an insurer discount or endorsement as the scaling lever.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 5 electrical contractors install a paid pilot in 10 boards each, and does one insurer offer a premium discount for it?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Facility managers, electrical contractors, insurers and property owners of commercial buildings in the EU.

**The problem as the pack states it:** About a quarter of building fires have an electrical origin (European Fire Academy estimate as cited by [Schneider Electric](https://www.electrical-installation.org/enwiki/State-of-the-art_solutions_for_electrical_fire_prevention,_beyond_the_standards)); the standard defence is one thermographic inspection a year by a person with a handheld camera. Loose terminals heat up in weeks, not years. Continuous thermal monitoring exists — for switchgear rooms, at switchgear prices.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/electricians** · https://www.reddit.com/r/electricians/ — working electricians.
- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€299–399, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how facility managers, electrical contractors, insurers and property owners of commercial buildings in the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. When did you last have an overheating connection in a distribution board, how was it found, and what did it cost?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire. On a scale of one to ten, how likely would you be to buy that at €299–399, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Switchboard Hot-Spot Watch: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Switchboard Hot-Spot Watch: A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire. Before we spend money on tooling I want to find out whether this solves a real problem for facility managers, electrical contractors, insurers and property owners of commercial buildings in the EU.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €299–399 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

Two questions, no pitch: how do you handle this today, and what would make you say no to the above? Twenty minutes on a call this week, or a reply here, both help.
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
A commercial building has 5–50 distribution boards. Each has 20–100 terminals that can loosen (thermal cycling, vibration, bad torque on install). The failure mode is slow heating → insulation damage → arc → fire. Today: annual (or less frequent) thermography by a contractor, €150–400 per board, a PDF nobody reads, and nothing in between. Continuous monitoring exists from the big switchgear vendors for MV/LV switchgear — wireless sensors on busbars, integrated into their systems, quoted per project and priced accordingly.

Who pays vs who uses: the building owner/facility manager pays; the electrical contractor installs and monitors (and would like a recurring service); the insurer requests, discounts or requires. Secondary: data centres' small rooms, hotels, schools, hospitals' technical services, farms with large boards (fire risk in barns), EV-charging hubs' distribution boards.

### Market size (estimates)
- EU commercial/public/multi-tenant buildings: ~15 M (estimate); average 6 boards worth monitoring → **90 M boards**; realistic candidates (boards above ~100 A, or in buildings with insurer pressure) → 15% → **13.5 M boards**.
- **TAM:** 13.5 M × €349 ≈ **€4.7 B** hardware (ceiling) + reports.
- **SAM:** boards maintained by contractors in DE/NL/UK/Nordics/FR who already sell thermography → ~2 M → **€700 M**.
- **SOM (3 years):** 0.3% → 6,000 boards → **€2.1 M** + a report service (€3/board/month → €200k/year at 6k boards).

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Annual handheld thermography by a contractor ("do nothing more") | The standard; required by some insurers | Once a year; faults develop in weeks; costs €150–400 per board per visit |
| Switchgear-vendor continuous thermal monitoring (wireless busbar sensors + their software; vendor claims 2.5× cost-effectiveness vs IR over 20 years — [Schneider white paper](https://download.schneider-electric.com/doc/998-2132737_GMA/998-2132737_HeatTag_GMA_eWhitePaper(1).pdf)) | Credible, integrated | Project-priced for MV/LV switchgear; not for 200 small boards in an office block |
| Thermal "gas/particle" sensors that sniff overheating insulation (HeatTag-class) | Clever, early warning | Vendor-locked, price, per-cabinet |
| IR-window thermography sensors / DIN-rail thermography sensors ([InfraSensing](https://infrasensing.com/sensors/sensor_thermography_din.asp)) | Closest to us; IT-room oriented | Needs their base unit and software; not LoRaWAN; price per point |
| Fixed-point temperature sensors on terminals | Cheap | One terminal each; installation labour; miss the one you didn't instrument |
| DIY MLX90640 + ESP32 | Makers | No baselines, no DIN mount, no report, no installation rules |

**Wedge:** one array sees the whole board (not one terminal), DIN-clip install in 15 minutes by the electrician who already services the board, LoRaWAN/WiFi to the FM's existing network, per-zone learning baselines, and a monthly PDF the insurer accepts — at a price that makes sense for a €200 office board.

### Product & value proposition
Hardware: DIN-rail clip or magnetic/adhesive mount on the board's enclosure facing the breakers (field of view 55°/110° variants), MLX90640-class 32×24 thermal array, a low-res visual camera optional (for the zone map — can be disabled for privacy, though inside a board there's nothing personal), ambient T/RH, ESP32-C6-class MCU with LoRa (from the Stamp C6LoRa reference) or WiFi, powered from 24 V aux (common in larger boards) or a DIN-rail 230 V → 5 V supply (bought-in certified, installed by the electrician), optional battery/supercap for a "lost power" alert. Firmware: zone map set up on a phone at install (draw boxes over the thermal image), baseline learning per zone vs ambient and vs load (if a meter is available over Modbus later), ΔT and absolute alarms, daily max per zone, LoRaWAN uplink (zone maxima only — tiny payload), monthly PDF per building, alarm by email/SMS/webhook via the FM's platform or ours.

Pricing (estimates): **€349 per unit**, €399 wide-angle, installer 10-pack €2,990; report service €3/board/month or €30/year (optional; the device works stand-alone with WiFi/MQTT). Contractors at 30% off; they resell with installation.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (thermal array €28, ESP32-C6 + LoRa €6, optional VGA camera €3, T/RH €1.5, power + protection €4, PCB €4) | €46.50 | €38.00 |
| Assembly & test (SMT, thermal calibration against a black-body reference, RF test) | €7.00 | €5.00 |
| Enclosure (flame-retardant V-0 ABS/PC, DIN clip, lens window; tooling amortised) | €7.50 | €4.80 |
| Packaging (box, clip, zone-map card) | €2.50 | €1.80 |
| Freight + duty to EU | €3.00 | €1.80 |
| Certification amortised (~€35k: RED, EMC incl. installation environment, safety, EN 18031) | €35.00 | €7.00 |
| **Landed cost** | **€101.50** | **€58.40** |
| Sell price (direct €349 / contractor €245) | €349 | €245 |
| **Gross margin** | **€247.50 (71%)** | **€186.60 (76% at contractor price)** |

The thermal array is the BOM — one vendor family dominates; negotiate at 5k, and qualify an alternative array even if it's worse.

### Go-to-market
**First 100 customers:** 5 electrical contractors install a paid pilot in 10 boards each (kill question) — found via electrical-contractor associations and the firms that already sell thermography; 1 insurer's loss-prevention engineer (they exist at every commercial insurer) who agrees to review the monthly PDF; 2 facility-management companies with mixed portfolios; a case study where a loose terminal was found.

**Scale channels:** electrical wholesalers (the contractor buys everything there), contractor associations' member offers, insurer loss-prevention programmes (discount or mandate), FM platforms (integration), switchboard builders (factory-fit option), EV-charging hub installers.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from Unit Thermal2 + Stamp C6LoRa in a DIN box; 50 boards in paid pilots across 5 contractors; first caught hot spot. |
| Q2 | Own PCB + V-0 enclosure, zone-map app, baselines; EVT 50; EMC in a live board; insurer PDF v1. |
| Q3 | DVT, certification, 300-unit pilot; wholesaler listing; report service live. |
| Q4 | 1,000 units; insurer programme; wide-angle SKU; Modbus load correlation. |

**Team:** 1 embedded engineer (thermal processing, LoRa, power — full-time), 1 software developer (zone-map app, backend, PDF — full-time), founder for contractors and insurers; a licensed electrician/consultant on contract for installation rules and EN 61439 guidance. Three people.

**Funding to first 1,000 units (estimates):** NRE €55k (PCB €10k, V-0 tooling €16k, app + backend €22k, electrician guidance €7k) + certification €35k + 1,000 units landed ~€75k + 9 months overhead €75k ≈ **€240k**; minus pilot fees (5 contractors × €2,500 ≈ €12.5k), pilot-batch sales (300 × €299 ≈ €90k), wholesaler/contractor prepayments (~€20k) ≈ **~€120k**. Bootstrap + paid pilots; building-safety/insurtech angels are a real option here; a loss-prevention grant from an insurer association is worth a try.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** emissivity, reflections and field of view — a shiny busbar reads cold, a plastic breaker reads right | Zone baselines (relative, not absolute), ΔT vs neighbours and vs ambient, install guide for placement; publish detection tests on a test board with a deliberately loose terminal |
| **Technical:** load-dependent heating looks like a fault | Learn daily patterns; optional Modbus/CT load correlation; alarm on deviation from baseline at similar load |
| **Regulatory/installation:** anything inside a board is the electrician's domain (EN 61439 assembly rules, national wiring rules) | Device is a monitoring accessory mounted on the enclosure, SELV-powered via a certified DIN supply; installed by a licensed electrician; written guidance reviewed by a consultant; never touch the busbars |
| **EMC:** a radio inside a metal board with contactors | External antenna option through a gland; EMC testing in a representative board; LoRa penetrates better than WiFi — lead with LoRaWAN |
| **Market:** "the insurer doesn't require it" | Start with contractors who sell thermography anyway (they add recurring revenue); bring the insurer the PDF and a caught fault |
| **Liability:** "your sensor didn't see the fire" | Position: early warning aid, not a fire-detection system (not EN 54); wording and insurance |
| **Supply:** thermal array sole-source family | Qualify a second array; buy ahead |
| **Licence:** the open thermal camera is OSHWHub | Read the licence; your own board — the Melexis driver and fusion approach are the learning |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| YuzukiIRC low-cost thermal + visual fusion camera (OSHWHub) | https://www.gongbans.com/db/oshwhub-yuzuki-infrared-camera.html | Open MLX90640 + OV9732 fusion camera on a V831 — the thermal/visual zone-map idea, proven | schematic, pcb | **OSHWHub — licence varies; read it** |
| M5Stack Unit Thermal2 (U149) | https://www.gongbans.com/db/m5stack-unit-thermal2.html | Thermal-array unit for the works-like | enclosure/structure only; electronics not published | Buy; array vendor's datasheet for production |
| M5Stack Hat Thermal (U062) | https://www.gongbans.com/db/m5stack-hat-thermal.html | Alternative thermal-array form factor | enclosure/structure only; electronics not published | Buy; prototype only |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | Open ESP32-C6 + LoRa core — the uplink | pcb, schematic (Altium) | M5Stack hardware repo — check licence terms |

### Block diagram
```
[MLX90640-class 32x24 thermal array, 55/110 deg lens] --I2C--> [ESP32-C6: zone maxima, baselines, dT alarms]
[optional low-res visual camera for the zone map]  --------->        |          |
[ambient T/RH]                                                        |          |
                                              [LoRaWAN EU868 (from C6LoRa ref) or WiFi]   [BLE: phone app at install]
                                                                      |
[24 V aux or certified DIN 230->5 V supply] -> [protected 5 V/3.3 V]  [supercap: "power lost" uplink]
                                                                      |
                                   [backend: alarms -> email/SMS/webhook; monthly PDF per building]
```
**Engineering gap:** the zone-map install flow, baseline learning that doesn't false-alarm on load cycles, placement/field-of-view rules per board type, V-0 enclosure and DIN clip, EMC inside a board, the insurer-grade PDF. The sensor and radio are solved.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| MLX90640-class thermal array (32×24, 55° or 110°) | €28.00 | **Dominant vendor; long lead (12–20 weeks); qualify an alternative** |
| ESP32-C6 module + LoRa transceiver (SX1262-class) + antenna | €6.50 | Pre-certified module; follow the C6LoRa reference |
| Low-res camera (optional SKU) | €3.00 | Can be omitted; zone map from thermal only |
| T/RH sensor | €1.50 | |
| Power: 24 V input + protection, or certified DIN 230 V → 5 V supply (bought-in) | €4.00 (+€8 DIN PSU) | **Never design the mains part yourself** |
| Supercap for power-loss uplink | €1.00 | |
| PCB 4-layer + passives + USB-C service port | €4.00 | |
| V-0 PC/ABS enclosure + DIN clip + IR-transparent window | €7.50 | **Tooling €12–16k**; window material must pass IR |

### Firmware/software starting point
- Melexis publishes an MLX90640 driver library on GitHub (exists); Adafruit's MLX90640 library (exists) for the works-like.
- LoRaWAN: Semtech's **LoRaMac-node** (exists) or an ESP-IDF LoRaWAN stack; network via **The Things Stack** or **ChirpStack** (both exist); payload = zone maxima + ambient, every 10 min.
- Baselines/alarms: your own; keep it on-device so a stand-alone WiFi/MQTT mode works.
- Zone-map app: a BLE-connected phone web app (Web Bluetooth) or a small native app; PDF from the backend.
- Reference for the fusion approach: the YuzukiIRC project page (MaixPy3-based) — read, don't copy.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 10 works-like units (Unit Thermal2 + Stamp C6LoRa in a DIN box) on a test board with a deliberately loose terminal: detects +15 K at 1 m; **5 electrical contractors sign a paid pilot (10 boards each, €500) and 1 insurer agrees to review the PDF** (runs to W8) |
| 3–5 | Works-like | 50 boards live; zone maxima uplinked every 10 min; baseline learning running; ≤ 1 false alarm per board per week after 7 days |
| 6–8 | Looks-like + EVT | Own PCB + V-0 enclosure T1 + DIN clip; 50 units; zone-map app; EMC pre-scan inside a live board with contactors; first PDF to the insurer |
| 9–10 | DVT + pre-compliance | RED/EMC/safety pre-compliance; EN 18031 self-assessment; installation guidance reviewed by the electrician consultant; 60-day false-alarm statistics |
| 11–12 | Pilot batch | 50 units to new contractors; ≥ 1 genuine hot spot caught and fixed; insurer gives a written view on a discount or endorsement |

### Certification checklist (EU)
- **CE under RED** (LoRa 868 MHz and/or WiFi/BLE): EN 300 220 (LoRa), EN 300 328 (2.4 GHz), EN 301 489-1/-3/-17, EN 62311; **EN IEC 62368-1** (SELV device; the DIN supply is a certified bought-in part); EMC for the installation environment (industrial levels — EN IEC 61000-6-2/-4 — are the sensible choice inside a board); **EN 18031-1** (internet-connected, mandatory since 1 Aug 2025), -2 not needed if no personal data (don't store the visual image in the cloud). Est. €8–12k RED/EMC, €4–6k safety, €12–18k EN 18031.
- **Installation:** EN 61439 is for the assembly builder; your device is an accessory — provide instructions compliant with national wiring rules, installed by a licensed electrician; a consultant signs the guide.
- **Not a fire-detection product (EN 54), not safety-related control** — say so.
- **RoHS, REACH, WEEE**, packaging. **Battery:** none (supercap) — keep it so.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware, FOTA, SBOM, vulnerability contact; a building-safety device gets scrutiny.
- **GDPR:** the optional camera looks inside a closed board — no people; document that it's disabled by default and never streams.
- **Total certification budget estimate: €25–38k.**

### Validation toolkit
- **Kill question:** Do 5 electrical contractors install a paid pilot in 10 boards each, and does one insurer offer a premium discount (or written endorsement) for it?
- **Cheapest experiment (~€1,500):** 10 works-like units, a test board with a loose terminal under load (video the thermal image heating), a one-page pilot offer at €500 per contractor, a draft monthly PDF to show the insurer's loss-prevention engineer.
- **5-question interview (electrical contractor / FM):** 1) How often are your boards thermographed, by whom, at what price? 2) What did the last report find, and what happened next? 3) Who asks for it — owner, insurer, nobody? 4) If a sensor in each board emailed you when a zone ran hot, what would you do with that, and would you sell it as a service? 5) €349 per board plus 15 minutes of your time — pilot 10 boards for €500?
- **Landing page:** headline "See every breaker's temperature. Every day. Not once a year." Bullets: "A thermal array on a DIN clip watches the whole board; alarms on a zone running hot vs its neighbours." / "LoRaWAN or WiFi; installed by your electrician in 15 minutes; no busbar contact." / "€349 per board; a monthly thermal report your insurer can read."
- **Pass threshold:** 5 paid pilots signed and one insurer in the loop, or 100 units pre-ordered by contractors in 8 weeks.

### First production checklist
- Samples: 5 golden samples with thermal calibration against a black-body at 2 temperatures, RF test, false-alarm log.
- DFM: IR window material and seal, lens alignment, DIN-clip retention on 35 mm rail, antenna placement/gland, V-0 material certificate.
- MOQ talk: thermal arrays 1k (long lead — order at EVT), modules reel, DIN supplies 500 from a certified vendor, enclosures 1k.
- QC: AQL II 2.5/4.0; 100% thermal image test against a heated target + RF join test; 2% 48 h soak at 50 °C.
- Packaging: zone-map card, installation guide (electrician only), DIN supply boxed as an accessory.
- Incoterms: FOB Shenzhen; air for 50; sea for 1,000.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Thermal2 (U149)](/db/m5stack-unit-thermal2.html) (thermal-array unit for the prototype); [M5Stack Hat Thermal (U062)](/db/m5stack-hat-thermal.html) (alternative thermal-array form factor); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [YuzukiIRC 低成本视觉增强热成像仪](/db/oshwhub-yuzuki-infrared-camera.html) (open MLX90640 thermal + visual fusion camera).

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit Thermal2 (U149), M5Stack Hat Thermal (U062), M5Stack Stamp C6LoRa (S012) — for a Switchboard Hot-Spot Watch

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Switchboard Hot-Spot Watch: A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire. The design is built around your M5Stack Unit Thermal2 (U149), M5Stack Hat Thermal (U062), M5Stack Stamp C6LoRa (S012).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Thermal2 (U149), M5Stack Hat Thermal (U062), M5Stack Stamp C6LoRa (S012).
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
主题：样品订购及批量报价 — M5Stack Unit Thermal2 (U149), M5Stack Hat Thermal (U062), M5Stack Stamp C6LoRa (S012) — 用于Switchboard Hot-Spot Watch

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Switchboard Hot-Spot Watch：A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire。产品设计基于贵司的M5Stack Unit Thermal2 (U149), M5Stack Hat Thermal (U062), M5Stack Stamp C6LoRa (S012)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Thermal2 (U149), M5Stack Hat Thermal (U062), M5Stack Stamp C6LoRa (S012)。
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
Subject: PCBA quote from open design files — Switchboard Hot-Spot Watch, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Switchboard Hot-Spot Watch: A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire. The design starts from published open-hardware files (YuzukiIRC 低成本视觉增强热成像仪; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Switchboard Hot-Spot Watch，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Switchboard Hot-Spot Watch：A thermal-array sensor mounted inside a distribution board that watches every breaker and busbar for hot spots and alerts long before a loose connection becomes an electrical fire。设计基于已公开的开源硬件文件（YuzukiIRC 低成本视觉增强热成像仪；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 5× Unit Thermal2 and 5× Stamp C6LoRa, a DIN box and a cheap test board with a 16 A breaker and a heater load; loosen one terminal and film the thermal image.
2. List 15 electrical contractors who advertise thermography and 2 insurers' loss-prevention departments; write the €500 pilot offer.
3. Spend an hour with a licensed electrician on where in a board a sensor can legally and practically sit, and what the installation guide must say.

Want help sourcing or building this? Talk to us via www.gongbans.com.
