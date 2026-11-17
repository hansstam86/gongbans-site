# LoRa Class Network Kit — Founder Start Pack

> A kit where every student builds a long-range radio sensor node, and together the class builds a school-wide network. Then they experiment with range, spreading factor, antennas and the radio rules that keep the band usable.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** IoT and radio are in every engineering curriculum, but real radio labs are expensive and teachers are short on ready lesson material. Most "IoT kits" are black boxes: students plug in a module and never see how a radio is designed, why a link works at 2 km and fails at 200 m, or why the 868 MHz band has duty-cycle rules.
- **Customer:** Vocational schools (electronics, mechatronics, IT), upper-secondary schools with technology tracks, universities of applied sciences, plus radio clubs and makerspaces. The department head or the teacher's equipment budget pays; students use it; school IT has to tolerate it.
- **Product:** A class kit of 12 student nodes (HopeRF RFM95W LoRa module + MCU + SHT31 temperature/humidity sensor + swappable antenna), a teacher hub/gateway (M5Stack Stamp C6LoRa-based, with a live dashboard on the school network), and a 6-lesson curriculum: link budget, spreading factor vs range vs airtime, duty cycle and the 868 MHz rules, star vs mesh, payload design, and a school-wide weather map. A "look inside a radio" lesson uses HopeRF's open evaluation-board schematics.
- **Why now:** HopeRF publishes module docs, demo code and evaluation-board schematics under MIT, and M5Stack publishes the Stamp C6LoRa's full electronics sources. Students can study a real, open radio design. Schools have digitalisation budgets and a push for practical STEM.
- **The ask:** About €90k (estimate) to reach 1,000 class kits' worth of nodes (~80 class kits). Route: pilot with 5 vocational schools, education-innovation grants, then education distributors. This is bootstrappable.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 5 vocational schools commit to the kit in their next year's curriculum? Teachers adopt only with ready lesson material — test the curriculum first.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Secondary and vocational schools, universities of applied sciences, radio clubs, makerspaces.

**The problem as the pack states it:** IoT and radio are in every engineering curriculum, but real radio labs are expensive and teachers are short on ready lesson material. Most "IoT kits" are black boxes: students plug in a module and never see how a radio is designed, why a link works at 2 km and fails at 200 m, or why the 868 MHz band has duty-cycle rules.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.
- **r/ScienceTeachers** · https://www.reddit.com/r/ScienceTeachers/ — secondary-school science teachers.
- **MNU (DE)** · https://www.mnu.de/ — German association of maths and science teachers; regional conferences.
- **IOP, Institute of Physics (UK)** · https://www.iop.org/ — UK physics teacher network and conferences.
- **r/amateurradio** · https://www.reddit.com/r/amateurradio/ — radio hobbyists who also teach and mentor.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€499 for 12 nodes + gateway (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how secondary and vocational schools, universities of applied sciences, radio clubs, makerspaces deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. What have your students built that communicates beyond the classroom, and what do you use today to teach radio, range and antennas?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A kit where every student builds a long-range radio sensor node and together the class builds a school-wide network — then experiments with range, spreading factor, antennas and the radio rules that keep the band usable. On a scale of one to ten, how likely would you be to buy that at €499 for 12 nodes + gateway (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: LoRa Class Network Kit: would you pay €499 for 12 nodes + gateway (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a LoRa Class Network Kit: A kit where every student builds a long-range radio sensor node and together the class builds a school-wide network — then experiments with range, spreading factor, antennas and the radio rules that keep the band usable. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €499 for 12 nodes + gateway (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Primary: **vocational schools and universities of applied sciences in DE, AT, CH, NL, BE and the Nordics**. Electronics, IT and mechatronics programmes there include networking and IoT modules and buy class sets (10–16 workstations). Teachers adopt **only when lesson material is ready**: every lesson must run in 45–90 minutes with a worksheet, an answer key and a fallback if the network fails.

Secondary: **upper-secondary schools with technology profiles**, **radio clubs** (amateur radio clubs run youth programmes), and **makerspaces** (workshops).

Who pays: the department head (equipment budget) or a funded digitalisation programme. Who decides: the teacher. Who can block it: school IT (no foreign devices on the network) — so the hub must work stand-alone with its own Wi-Fi AP.

### Market size (estimates)
- Vocational/technical schools and universities of applied sciences with electronics/IT programmes in the EU: roughly 15k–25k institutions (estimate; check national education statistics). Assume 30% run an IoT/networking module that could use a kit, 1–2 kits each.
- **TAM:** ~6k institutions × 1.5 kits × €799 ≈ **€7 M** one-off + consumables/curriculum updates. This is a niche.
- **SAM:** DACH + Benelux + Nordics with German/English/Dutch material, ~35% → **€2.5 M**.
- **SOM (3 years):** 10% of SAM → ~300 class kits → **~€240k** + add-on sensor packs. A good product line for an education-hardware company, not a standalone venture. Upside: radio clubs, universities, and the international English market.

### Competition
| Alternative | Price (listings, estimate) | Weakness we attack |
|---|---|---|
| Modular IoT starter kits for education (e.g. RAKwireless WisBlock IoT Starter Kit for Education, listed at ~$189 per kit, [RAK store](https://store.rakwireless.com/products/wisblock-iot-starter-kit)) | ~€175 per student kit | Great hardware, but per-student cost adds up; curriculum is generic; radio is a black box |
| LoRaWAN starter kits with gateway (e.g. Seeed SenseCAP LoRaWAN Starter Kit, ~$174) | €160–200 | One gateway + a few sensors; not a class set; little radio teaching |
| Dragino LoRa/LoRaWAN IoT kits, STM32 Nucleo LoRa packs | €100–200 | Developer kits, not lessons |
| Meshtastic workshop kits | €30–60 per node | Fun, but it's a messaging app; little control over radio parameters in lessons |
| DIY (Arduino + RFM95 breakouts, teacher writes the lessons) | €15–25 per node | Teacher's weekends; no gateway/dashboard; fragile |
| Online LoRaWAN training courses (e.g. vendor academies) | Varies | No hands-on hardware |

**Wedge:** **a class set + ready curriculum + teacher hub that works without school IT**, priced per class (not per student), with an open "look inside the radio" angle (open schematics from HopeRF and M5Stack) and **regulation built into the lessons** (duty cycle, band plan, why single-channel "gateways" aren't LoRaWAN).

### Product & value proposition
- **Student node:** HopeRF RFM95W (868 MHz, up to +20 dBm, −144 dBm sensitivity, 164 dB link budget, SPI, per HopeRF), a small MCU board (ESP32-C3 or RP2040 class, programmable in Arduino/MicroPython), a Grove SHT31 sensor, a 2× AA or USB power option, an SMA antenna jack + 2 antennas (stubby and ½-wave) for range experiments, and an OLED showing RSSI/SNR/SF live.
- **Teacher hub:** M5Stack Stamp C6LoRa (ESP32-C6 + LoRa, with open Altium electronics sources per M5Stack) on a carrier with its own Wi-Fi access point and dashboard: live node map, RSSI/SNR per packet, airtime and duty-cycle meter per node ("you used 0.8% of your 1% this hour"), and a weather map. It's a **single-channel LoRa hub (not a LoRaWAN gateway)**, which is itself a lesson. An optional lesson 6b connects nodes to a real LoRaWAN network via the school's or a community gateway.
- **Curriculum (6 lessons + project):** (1) link budget and dB, (2) spreading factor vs range vs airtime, (3) 868 MHz rules: duty cycle, ERP limits, sub-bands, (4) star vs mesh, retries and collisions, (5) payload design (bytes matter), (6) the school weather map project; plus "look inside a radio" with the CMT-RF_EB and RFM95 reference material.
- **Teacher pack:** worksheets, answer keys, slides, a 1-page "what if it doesn't work" checklist, in DE/EN/NL.

**Pricing (estimates):** **€799 per class kit** (12 nodes + hub + curriculum); 6-node starter €449; spare node €39; sensor add-on pack (soil moisture, light, CO₂-class) €149. Curriculum licence included; updates free. The idea's original €499 doesn't leave a margin at these volumes (see the table).

### Unit economics (estimates per class kit = 12 nodes + hub, ex-VAT)
| Item | 1k nodes (~80 kits) | 5k nodes (~400 kits) |
|---|---|---|
| Node BOM ×12 (RFM95W, MCU board, SHT31, OLED, SMA + 2 antennas, battery holder, PCB) | €228.00 | €180.00 |
| Hub (Stamp C6LoRa + carrier + antenna + PSU) | €28.00 | €22.00 |
| Assembly & test (RF check per node) | €26.00 | €18.00 |
| Enclosures (open-frame acrylic/3D-printed node trays, hub case) | €20.00 | €12.00 |
| Packaging (class case with foam, labelled slots) | €18.00 | €12.00 |
| Freight + duty to EU | €8.00 | €5.00 |
| Certification amortised (~€15k: RED via pre-certified modules + system test, EMC) | €188.00 | €38.00 |
| Curriculum development amortised (~€20k) | €250.00 | €50.00 |
| **Landed cost** | **€766.00** | **€337.00** |
| Net price (direct to schools €671 ex-VAT / education distributor €520) | €671 | €520 |
| **Gross margin** | **−€95 (loss)** | **€183 (35%)** |

The first ~80 kits pay for certification and curriculum, so treat that as an investment or get it grant-funded. From kit ~150, it's a healthy business. Spare nodes and sensor packs carry 50%+ margins.

### Go-to-market
**First 100 customers (class kits over time; first 10 matter most):**
- **5 pilot vocational schools** in one region: free kits for one semester in exchange for co-writing the lessons and a testimonial. Teachers trust teachers.
- **Teacher networks:** regional teacher-training institutes (they run in-service days, so offer a free LoRa workshop day), subject associations for technology/IT teachers, and education fairs (didacta-type).
- **Universities of applied sciences:** an IoT lab course lecturer adopting it brings the vocational schools in that region along.
- **Radio clubs:** youth radio programmes; the "duty cycle and band plan" lesson fits their training.

**Scale channels:** education distributors and school-equipment suppliers (they handle school purchasing processes and tenders), national STEM programmes, and the international English market via online shops.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: curriculum first. Write lessons 1–3, run them with 2 teachers on DIY hardware (RFM95 breakouts + dev boards). 5 school LOIs |
| Q2 | Custom node PCB + hub carrier; lessons 4–6; EVT 3 class kits in 3 pilot schools |
| Q3 | DVT; RED/EMC testing; 5 pilot schools running a full semester; distributor talks |
| Q4 | First 30 paid class kits for the next school year (school budgets are often decided in spring/early summer, so time your sales) |

**Team:** 1 embedded/RF engineer (node, hub firmware, dashboard), 1 teacher/curriculum developer (part-time, essential), the founder on school sales and distributor deals.

**Funding to the first 1,000 nodes (~80 kits) (estimates):** NRE €25k (node PCB €6k, hub carrier €4k, firmware + dashboard €15k) + certification €15k + curriculum €20k + 80 kits' hardware landed ~€27k + 9 months lean costs €40k ≈ **€127k**. Subtract pilot-school purchases and pre-orders (~€15k) and an education-innovation grant (~€20–30k) → **~€85–90k**. Route: grant + pre-orders + founder; bootstrappable alongside other work.

### Top risks
| Risk | Mitigation |
|---|---|
| **Market:** teachers don't adopt without ready material | Curriculum first (kill question), co-written with pilot teachers; include fallbacks and answer keys |
| **Technical:** 12 nodes + 30 students in one room = collisions and duty-cycle breaches | Built into the lessons; firmware enforces the duty cycle with a visible meter; the class plan staggers transmissions |
| **Regulatory:** students modifying TX power/antennas beyond ERP limits | Firmware caps TX power for the supplied antennas; lesson 3 covers ERP/legal limits; high-gain antennas aren't in the kit |
| **IT/safety:** school IT won't allow devices on the network | The hub runs its own Wi-Fi AP; no cloud needed; a data-privacy note for school admins |
| **Sales cycle:** school budgets are annual and slow | Distributor partnership; sell to teacher-training institutes and universities first; offer a 6-node starter kit for small budgets |
| **Supply:** RFM95W single source; M5Stack product lifecycle | RFM95W pin-compatible alternatives exist; the hub carrier can take another ESP32 + LoRa module (keep the dashboard portable) |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF RFM95/96/98(W) | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | Student-node radio: 868 MHz LoRa/FSK, 164 dB link budget; datasheet, demo code, footprint, 3D model, CE/FCC reports | PCB footprint, demo code, datasheet, mech | MIT (HopeRF repo) |
| HopeRF CMT-RF_EB evaluation board | https://www.gongbans.com/db/hoperf-cmt-rf-eb.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/Tools_Kit) | The "look inside a radio" reference: two board-revision schematics, STM32 demo projects, app notes incl. LoRa examples | schematic, firmware | MIT |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | Teacher hub: ESP32-C6 + LoRa on one stamp; full electronics sources | schematic, PCB, sch_lib, pcb_lib (Altium) | Check M5Stack's M5_Hardware repo licence before reusing the design |
| Seeed Grove-TempAndHumi Sensor (SHT31) | https://www.gongbans.com/db/seeed-grove-tempandhumi-sensor-sht31.html | First application sensor (school weather map) | schematic | Seeed wiki resources; check the licence |

3 of 4 boards publish schematic/PCB files; that openness is part of what you sell.

### Block diagram
```
STUDENT NODE (x12)                                                     TEACHER HUB
[SHT31 T/RH] --I2C--> [MCU (ESP32-C3/RP2040 class)] --SPI--> [RFM95W 868 MHz] -> [SMA: stubby / 1/2-wave]
[OLED: RSSI, SNR, SF, airtime] <--|                                   ~~ LoRa 868 MHz (single channel, duty-cycle capped) ~~>
[2x AA or USB]                                                           [Stamp C6LoRa (ESP32-C6 + LoRa)]
                                                                           |-> own Wi-Fi AP -> [dashboard: map, RSSI/SNR, duty-cycle meter, weather map]
                                                                           `-> optional: forward to a real LoRaWAN network (lesson 6b, via a proper gateway)
```
**Engineering gap:** all the parts exist. What's missing: a robust student-node PCB (reverse-polarity-proof, student-proof), firmware with parameters students can change safely (SF, BW, TX power within legal limits), the duty-cycle meter, the hub dashboard, and **above all the curriculum** (worksheets, answer keys, timings, fallbacks).

### Starter BOM (estimates per node at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| RFM95W-868 | €4.50 | HopeRF; pin-compatible alternatives exist |
| MCU board (ESP32-C3 or RP2040 module on the node PCB) | €2.50 | Arduino + MicroPython support matters for teachers |
| SHT31 sensor (or Grove module) | €2.20 | |
| 0.96" OLED | €1.20 | |
| SMA connector + 2 antennas | €2.40 | Legal-gain antennas only |
| Battery holder 2× AA + switch + reverse-polarity protection | €0.80 | |
| PCB + passives + headers | €2.50 | |
| Per-node share of the class case + node tray | €3.20 | |

### Firmware/software starting point
- **Node:** RadioLib (github.com/jgromes/RadioLib) supports the SX127x inside the RFM95W and runs on ESP32/RP2040 with Arduino; good for teaching because parameters are explicit. HopeRF's RFM95 demo code is in the GitHub folder.
- **MicroPython:** search "MicroPython SX127x driver" for a student-friendly path.
- **Hub:** ESP-IDF or Arduino on the ESP32-C6; M5Stack's examples for the Stamp C6LoRa; a small web dashboard served from the hub (charts via a JS chart library).
- **LoRaWAN lesson (6b):** The Things Stack community edition or ChirpStack, plus an LMIC/RadioLib LoRaWAN example on the node.
- **Airtime calculations:** the Semtech LoRa modem design guide formulas; online LoRa airtime calculators exist (search "LoRa airtime calculator") for the worksheet answer keys.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** do 5 vocational schools commit to the kit in next year's curriculum? Teachers adopt only with ready lesson material, so test the curriculum first. Lessons 1–2 drafted; 2 teachers run them on DIY hardware |
| 3–5 | Works-like | 12 DIY nodes + Stamp C6LoRa hub dashboard working in a classroom; lessons 3–4 drafted and tested; duty-cycle meter correct vs airtime calculation |
| 6–8 | Looks-like + EVT | Custom node PCB + class case; 3 class kits to pilot schools; lessons 5–6 + weather-map project; "teacher alone" test: a teacher who hasn't met you runs lesson 1 from the pack |
| 9–10 | DVT + pre-compliance | RED system test (modules pre-certified), EMC pre-scan; battery-reversal and drop tests (students will do both); IT/privacy note for schools |
| 11–12 | Pilot batch | 5 schools ran ≥3 lessons each; teacher feedback ≥4/5; 5 signed LOIs or purchase orders for the next school year |

### Certification checklist (EU)
- **CE under RED:** the RFM95W carries CE reports (in the HopeRF folder), but **your product** needs its own RED assessment: EN 300 220-1/-2 (868 MHz, ERP and duty-cycle limits for the antennas you ship), Wi-Fi on the hub (EN 300 328), EMC EN 301 489-1/-3/-17, safety EN 62368-1 (low voltage, batteries), exposure EN 62479. Pre-certified modules reduce testing, but they don't remove it. Est. **€8–14k**.
- **Reconfigurable radio:** if students can change radio parameters, the firmware must keep the device within the conformity assessment (power cap, band limits). Document that in the technical file.
- **RED delegated act (EN 18031-1):** the hub runs a local Wi-Fi AP; if it can connect to the internet (lesson 6b), EN 18031-1 applies. Offline-only by default reduces scope; get a lab opinion. Est. **€3–8k** if needed.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Update path for hub and node firmware, SBOM, vulnerability contact.
- **Toy Safety Directive:** not applicable if it's marketed and designed as **teaching equipment for students 14+** in a supervised setting (EN 71 is for toys for under-14 play). Don't market it as a toy or for younger children.
- **RoHS, REACH, WEEE** (schools are B2B or B2C depending on country; register anyway), packaging registration.
- **Battery Regulation (EU) 2023/1542:** if you ship AA cells, portable-battery obligations apply; easier to ship without batteries.
- **GDPR:** temperature data isn't personal; if the dashboard stores student names per node, keep it local and short-lived, and give the school a short privacy note.
- **Total certification budget estimate: €12–22k.**

### Validation toolkit
- **Kill question:** Do 5 vocational schools commit to the kit in next year's curriculum? Teachers adopt only with ready lesson material, so test the curriculum first.
- **Cheapest experiment (~€400):** write lesson 1 (link budget) and lesson 3 (duty cycle) with worksheets, build 6 DIY nodes from RFM95W breakouts and dev boards, and run a free workshop at a teacher-training day. Collect LOIs on the spot.
- **5-question interview (teacher/department head):** 1) Which IoT/networking topics must you teach, and with what equipment today? 2) What makes you drop a kit after one semester? 3) How long can one lesson be, and what must the worksheet include? 4) Who approves equipment purchases, when, and how much is the budget? 5) €799 for a class kit with 6 ready lessons: would you put it in next year's plan?
- **Landing page headline:** "Teach radio the way engineers learn it: build the network." Bullets: "12 student LoRa nodes + a teacher hub that works without school IT." / "6 ready lessons: link budget, spreading factor, duty cycle, mesh, payloads, a school weather map." / "Open designs: students look inside a real radio, not a black box."
- **Pass threshold:** 5 schools sign LOIs (or orders) for the next school year **and** ≥2 teachers who've never met you run a lesson successfully from the pack.

### First production checklist
- **Samples:** golden class kit (12 nodes + hub) with each node's TX power/frequency logged; curriculum version tied to the firmware version.
- **DFM review:** node PCB robustness (reverse polarity, ESD on the exposed headers, SMA strain), clear silkscreen labels for teaching, the class case layout (count-at-a-glance slots so teachers see missing nodes).
- **MOQ talk:** RFM95W reels, OLEDs, SMA antennas (legal gain), class cases (MOQ 100+).
- **QC/AQL:** AQL II 1.0/2.5; 100% RF test per node (TX power within limit, RX of a reference packet), 100% sensor reading check, kit completeness check (photo per case).
- **Packaging:** a durable class case with foam inserts, teacher quick-start on the lid, QR to the lesson materials, spares bag.
- **Incoterms:** FOB Shenzhen for electronics; consider final kitting in the EU (cases, printed material, local language) to keep flexibility for school-year timing.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver modules for student nodes); [HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003)](/db/hoperf-cmt-rf-eb.html) (open sub-GHz evaluation base board as the 'look inside a radio' reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (ESP32-C6 + LoRa stamp for the class gateway (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-TempAndHumi Sensor-SHT31](/db/seeed-grove-tempandhumi-sensor-sht31.html) (sensor for the first application). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31 — for a LoRa Class Network Kit

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a LoRa Class Network Kit: A kit where every student builds a long-range radio sensor node and together the class builds a school-wide network — then experiments with range, spreading factor, antennas and the radio rules that keep the band usable. The design is built around your HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31.

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31.
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
主题：样品订购及批量报价 — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31 — 用于LoRa Class Network Kit

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款LoRa Class Network Kit：A kit where every student builds a long-range radio sensor node and together the class builds a school-wide network — then experiments with range, spreading factor, antennas and the radio rules that keep the band usable。产品设计基于贵司的HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31。
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
Subject: PCBA quote from open design files — LoRa Class Network Kit, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a LoRa Class Network Kit: A kit where every student builds a long-range radio sensor node and together the class builds a school-wide network — then experiments with range, spreading factor, antennas and the radio rules that keep the band usable. The design starts from published open-hardware files (HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — LoRa Class Network Kit，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款LoRa Class Network Kit：A kit where every student builds a long-range radio sensor node and together the class builds a school-wide network — then experiments with range, spreading factor, antennas and the radio rules that keep the band usable。设计基于已公开的开源硬件文件（HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), M5Stack Stamp C6LoRa (S012), Seeed Grove-TempAndHumi Sensor-SHT31；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Write lesson 1 (link budget) as a 90-minute worksheet with an answer key, and test it on one friendly teacher.
2. Order 6 RFM95W breakouts + 6 dev boards + an M5Stack Stamp C6LoRa; get 6 nodes reporting RSSI/SNR to a hub web page.
3. List 20 vocational schools/universities of applied sciences in one region with IoT modules and contact their teacher-training institute about a free workshop day.

Want help sourcing or building this? Talk to us via www.gongbans.com.
