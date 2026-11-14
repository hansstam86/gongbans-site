# School Scope — Founder Start Pack

> A €59 pocket oscilloscope + voltmeter kit designed for physics classrooms: safe banana inputs, pre-loaded experiments and a teacher dashboard instead of a 200-page manual.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Schools replace their dying analogue scopes with €30 pocket scopes that students can't operate and teachers can't teach with, or with €400+ bench scopes they can't afford sixteen of. Nobody designs a measurement tool for a 15-year-old and a 45-minute lesson.
- **Customer:** Secondary-school physics departments and vocational schools in DE/NL/UK/Nordics; education-supply distributors as the channel. The school (or the department head with a budget) pays; teachers and students use it.
- **Product:** A €59–69 handheld with ±30 V protected banana inputs (no mains, ever), scope + voltmeter + signal generator, an "experiment mode" that walks the class through RC charging, AC vs DC, sound waves, diode rectification, with USB export to the class spreadsheet; sold as 16-unit class sets with a charging box.
- **Why now:** Four open scope/voltmeter designs with schematics and PCB exist in the catalogue, including a small handheld and an STM32H750-class portable; pocket scopes have proven the price point (FNIRSI DSO152 at ~€27–37, [eleshop](https://eleshop.eu/fnirsi-dso152-oscilloscope.html), [aio.lv](https://aio.lv/en/product--fnirsi-dso152--11618311.md)) but not the classroom; curricula push measurement and data literacy.
- **The ask:** ~€90k (estimate) to the first 1,000 units; route = teacher trials → class-set pre-orders + bootstrap; education distributors for scale.

## 2. Business plan

### Problem & customer
The physics teacher has 16 benches, one lesson, 30 students and a cupboard of scopes from 1990. They need every bench to see a waveform in 3 minutes, students to record a value without breaking anything, and a worksheet that matches the device. The department head signs for €1,000–1,500 a year; a class set has to fit that. The distributor needs a catalogue SKU with CE, a spare-parts line, and a 3-year warranty.

Who pays vs who uses: the school pays via the distributor; teachers prepare, students use. The vocational school (electrical trades) is the second buyer with slightly higher specs.

### Market size (estimates)
- EU + UK: ~60k secondary schools and ~15k vocational schools (estimate); say 70% teach physics/electronics with a lab → ~52k schools; one class set each → **52k class sets × 16 = 830k units**. Replacement every ~8 years.
- **TAM:** 830k × €64 ≈ **€53 M** (+ class-set boxes, probes).
- **SAM:** schools in DE/NL/UK/Nordics served by the distributors we can reach — ~35% → **€18 M**.
- **SOM (3 years):** 3% of SAM → ~9,000 units (560 class sets) → **€580k** + accessories.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Pocket scopes (FNIRSI DSO152-class, €27–37; 200 kHz single-channel per [atomic14](https://www.atomic14.com/bench/scopes/fnirsi-dso152/)) | Cheap, surprisingly OK | Unprotected inputs, cryptic UI, no curriculum, no class-set logistics, no export |
| Entry bench scopes (€300–500) | Real instruments | 16 of them = €6k; mains-powered; 200-page manual |
| PC/USB scopes for education (PicoScope-class) | Good software | Needs a PC per bench; price per seat |
| Phone apps + audio jack / "do nothing" with multimeters | Free | Can't show a waveform safely; no AC measurement for most |
| Datalogger ecosystems from education suppliers (sensor + interface) | Curriculum-aligned | €200–400 per bench; closed; slow |
| DIY (DSO138 kits etc.) | Teachers build them with students | Unprotected, fragile, no export |

**Wedge:** curriculum-first UI, protected banana inputs, class-set hardware (charging box, labelled units, spares), USB export to a spreadsheet, at pocket-scope money.

### Product & value proposition
Hardware: 2.8" colour LCD, 2 analogue channels (one is enough for most lessons; two for phase/rectifier lessons), ~1 MSa/s class (audio to a few hundred kHz is all a school needs — say it), 4 mm shrouded banana inputs with ±30 V clamping and a fuse-less protection network, built-in signal generator (sine/square/triangle to 20 kHz) on a third banana pair, voltmeter mode (DC/AC RMS, 3.5 digits — the "5½-digit" open design informs the precision path but the school unit doesn't need it), Li-ion with USB-C, rubber bumper, lanyard. Software: Scope / Meter / Generator / Experiment modes; experiment mode shows a diagram, the expected curve, and a "record" button that writes a CSV; teacher dashboard = a USB "class box" that collects CSVs from 16 units and merges them into one sheet. Class set: 16 units, charging box, 16 lead sets, spares, teacher guide with 12 lessons.

Pricing (estimates): **€69 single**, **class set of 16 at €999** (≈ €62/unit) with charging box, vocational variant €89 (higher bandwidth, 2 ch, probe clips). Distributors at 35–40% off.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (MCU with ADC €2.5, analogue front-end + protection €3, 2.8" LCD €4.5, Li-ion + charger €3, banana jacks €2, PCB + passives €4) | €19.00 | €15.00 |
| Assembly & test (SMT, gain/offset calibration, protection test) | €3.50 | €2.40 |
| Enclosure (ABS + rubber bumper; tooling amortised) | €3.80 | €2.40 |
| Packaging (box, 2 lead sets, quick card; class-set box separate) | €2.20 | €1.60 |
| Freight + duty to EU (Li-ion) | €2.00 | €1.30 |
| Certification amortised (~€16k: EMC/LVD, EN 61010 input wording, UN 38.3, RoHS) | €16.00 | €3.20 |
| **Landed cost** | **€46.50** | **€25.90** |
| Sell price (direct €69 / distributor €42) | €69 | €42 |
| **Gross margin** | **€22.50 (33%)** | **€16.10 (38% at distributor)** |

Honest: at 1k units this is thin. The class-set box (~€40 BOM, sold at €150 inside the set), lead sets, the vocational variant, and 5k+ volumes make it work. Don't launch below €69 single / €999 set.

### Go-to-market
**First 100 customers:** 10 physics teachers who trial a 16-unit set for one lesson and then order (kill question) — found via physics-teacher associations and their conferences, teacher forums and social groups, university teacher-training departments; 2 education-supply distributors' product managers early (they tell you the price and the catalogue deadline); a lesson video shot in a real classroom.

**Scale channels:** education-supply distributors (the catalogues schools order from — their deadlines are 6–9 months before print), teacher-association conferences, vocational-school equipment suppliers, textbook publishers (worksheet bundles), national STEM programmes and grants.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from the mini handheld open design + protection front-end; experiment mode v0 (4 lessons); 10 teacher trials → class-set orders. |
| Q2 | Own PCB, tooled case, class box; EVT 100 (6 class sets); teacher guide v1 (12 lessons); pre-compliance; distributor samples. |
| Q3 | DVT, certification, 500-unit pilot (30 sets) for the autumn term; distributor listing for next catalogue. |
| Q4 | 1,000+ units; vocational variant EVT; second country's curriculum mapping. |

**Team:** 1 embedded/analogue engineer (front-end, protection, firmware — full-time), 1 UI/educational-software developer (experiment mode, class box merge — part-time → full-time), a physics teacher-author on contract for the lessons, founder for distributors and teacher community. Three people.

**Funding to first 1,000 units (estimates):** NRE €42k (PCB €8k, case + class box tooling €16k, firmware/UI €12k, lesson content €6k) + certification €16k + 1,000 units landed ~€47k + 9 months overhead €55k ≈ **€160k**; minus class-set pre-orders (10 × €999 ≈ €10k), pilot sales (30 sets ≈ €28k) and a distributor's first order prepayment (~€30k) ≈ **~€90k**. Bootstrap + pre-orders; STEM-education grants exist in most countries and fit the lesson-content part.

### Top risks
| Risk | Mitigation |
|---|---|
| **Safety:** a student connects it to mains | ±30 V clamping + series protection on every input; shrouded 4 mm jacks; no mains probes supplied; big "no mains" label; EN 61010 wording; the teacher guide forbids it |
| **Technical:** cheap ADC = noisy traces that confuse students | Oversampling, auto-set, averaging on by default; it's a teaching tool, not a 100 MHz scope — set expectations |
| **Market:** thin margin at low volume | Class-set pricing, accessories, vocational variant; don't do single-unit retail below €69 |
| **Market:** distributor catalogue cycles are slow | Get samples to product managers in Q1 for next year's catalogue; sell direct to early-adopter teachers meanwhile |
| **Regulatory:** Li-ion in a school device — transport, battery regulation, charging box safety | UN 38.3 cell, removable cell for 2027 rules, class box with a certified multi-port USB supply |
| **Supply:** 2.8" LCD panels change often | Two panels on one connector; buy a year ahead for the class sets |
| **Licence:** four OSHWHub designs | Read each licence; they are references — your own schematic, your own firmware |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| MINI handheld oscilloscope, ultra-mini version (OSHWHub) | https://www.gongbans.com/db/oshwhub-mini-shou-chi-shi-bo-qi5-0.html | Open ultra-mini handheld scope — the form factor and front-end starting point | schematic, pcb | **OSHWHub — licence varies; read it** |
| Simple oscilloscope, training-camp project (OSHWHub) | https://www.gongbans.com/db/oshwhub-simple-oscilloscope.html | Open simple scope — the entry/educational variant | schematic, pcb | OSHWHub — check licence |
| Portable oscilloscope + STM32H750 core board re-engraving (OSHWHub) | https://www.gongbans.com/db/oshwhub-training-camp-portable-oscilloscope-re-engraving.html | Open portable scope with an STM32H750 core (two boards: core + scope expansion) — the vocational "pro" variant | schematic, pcb | OSHWHub — check licence |
| 5½-digit voltmeter (OSHWHub) | https://www.gongbans.com/db/oshwhub-wu-wei-ban-dian-ya-biao.html | Open precision voltmeter — informs the meter mode (the school unit uses a simpler path) | schematic, pcb | OSHWHub — check licence |

### Block diagram
```
[Banana CH1] [Banana CH2] -> [protection: series R + clamps to ±30 V, ESD] -> [attenuator + op-amp front-end] -> [MCU ADC ~1 MSa/s]
[Banana GEN out] <- [DAC/PWM generator: sine/square/triangle to 20 kHz]                 |
                                                   [MCU (STM32H7/G4-class or ESP32-S3 without radio)] 
                                                      |            |            |
                                           [2.8" LCD + 5 buttons]  [USB-C: charge + CSV mass storage]  [Li-ion 1S + charger + gauge]
[Class box: 16 USB-C ports from a certified supply + a small hub MCU that merges 16 CSVs into one sheet]
```
**Engineering gap:** the protection front-end that survives abuse, the experiment-mode UI and lessons, the CSV/class-box merge, a case that survives being dropped by teenagers, and class-set logistics. The scope core exists.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| MCU with fast ADC (STM32G4/H7-class) | €3.00 | Second-source: ESP32-S3 variant without radio enabled would drag RED in — avoid |
| Analogue front-end (op-amps, attenuator, clamps, series R) | €3.00 | Protection parts must be rated; test to ±60 V surge |
| 2.8" LCD 320×240 | €4.50 | **Two panels on one connector** |
| Li-ion 1,000 mAh + charger + gauge | €3.00 | UN 38.3; removable for 2027 |
| 4 mm shrouded banana jacks ×6 | €2.00 | Multi-source |
| PCB + passives + USB-C | €3.50 | |
| ABS case + rubber bumper + lanyard | €3.80 | **Tooling €9–12k** |
| Lead sets (2× 4 mm to crocodile) | €1.50 | Consumable; sell spares |
| Class box (per 16): case, certified 16-port USB supply, hub MCU | €40.00 | Sold inside the set |

### Firmware/software starting point
- The OSHWHub projects publish firmware on their pages — read for ADC/DMA and display handling; the JYE Tech DSO138 open design (exists) is another documented reference for a minimal scope.
- Your own: experiment mode (state machine + diagrams), auto-set, RMS meter, generator, USB mass-storage CSV (TinyUSB exists), and the class-box merge.
- Lessons: write with the teacher-author; map to the national curriculum per country (DE Bundesländer differ — pick 2 to start).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 16 units from the open mini-scope design + a protection board, 4 experiment worksheets; **10 physics teachers run one lesson; pass if ≥ 10 order a class set at €69/unit** (runs to W8) |
| 3–5 | Works-like | Own front-end: survives ±60 V for 1 minute and a 230 V touch for 1 s without damage (then a lab confirms); experiment mode v0; CSV export; auto-set |
| 6–8 | Looks-like + EVT | Case T1 + bumper, class box v1; 100 units (6 sets); 3 classrooms run 2 lessons each; EMC pre-scan |
| 9–10 | DVT + pre-compliance | EMC/LVD pre-compliance; EN 61010 input-safety review of wording and protection; UN 38.3 report; drop test 1 m × 6 faces; teacher guide v1 |
| 11–12 | Pilot batch | 30 sets (480 units) to trial schools + distributor samples; ≥ 80% of students complete the RC-charging lesson; ≤ 2% field failures |

### Certification checklist (EU)
- **CE under EMC + LVD** (no radio): EN IEC 61000-6-1/-3; **EN IEC 61010-1** is the measuring-equipment safety standard — a battery device with ≤ 30 V inputs falls below most hazardous-voltage clauses, but use its wording for input ratings (CAT none, "not for mains") and get a lab to review the protection; **EN IEC 62368-1** for the charging box. Est. €5–8k EMC, €3–5k safety review, €2–3k charging box.
- **No radio** → no RED, no EN 18031. Keep it so; export is USB.
- **Battery:** UN 38.3 for the cell, **EU Battery Regulation** labelling, removability by 18 Feb 2027 — removable cell behind a screw door.
- **RoHS, REACH, WEEE**, packaging registration.
- **CRA:** non-connected product with digital elements — low exposure; USB firmware update, vulnerability contact, reporting from 11 Sept 2026, full 11 Dec 2027.
- **GDPR:** CSVs may contain student names if teachers type them — default to bench numbers. **Toy directive:** not a toy — "educational equipment, 12+ under supervision"; stay out of toy channels.
- **Total certification budget estimate: €10–16k.**

### Validation toolkit
- **Kill question:** Do 10 physics teachers order a 16-unit class set at €69 each after a one-lesson trial?
- **Cheapest experiment (~€1,500):** 16 open-design mini scopes + protection boards in printed cases, 4 worksheets, a loan box; lend to 10 teachers for one lesson each; order form at €999 per set, delivery next term.
- **5-question interview (physics teacher):** 1) What do you use today to show a waveform, and how many benches get to use it? 2) What's the one experiment you skip because the equipment is a hassle? 3) How much can you spend without asking anyone, and how much with the head's signature? 4) What breaks in your lab, and who fixes it? 5) €999 for 16 units with lessons and a charging box — would you order for next term?
- **Landing page:** headline "A scope every bench can use in 3 minutes." Bullets: "Protected ±30 V banana inputs, scope + meter + generator, experiment mode with the curve students should see." / "USB export; the class box merges 16 units into one spreadsheet." / "€999 per class set of 16 with charging box and 12 lessons."
- **Pass threshold:** 10 class-set orders from 10 trials, or 25 sets reserved by teachers in 8 weeks.

### First production checklist
- Samples: 5 golden samples with gain/offset calibration records and a protection-test certificate.
- DFM: banana-jack retention, bumper fit, battery door screws, LCD bonding, drop-test survival, lead-set strain relief.
- MOQ talk: LCDs 1k–2k (two panels), MCUs reel, jacks 10k, cells 1k with UN 38.3, cases 1k, class boxes 100.
- QC: AQL II 2.5/4.0; 100% calibration + input-protection pulse test; 100% charge test; 1% drop test.
- Packaging: UN 3481 marking; class-set box with labelled unit slots (1–16) and spares.
- Incoterms: FOB Shenzhen; air for samples; sea for the term batch — order 6 months before September.

## 4. Who to contact

<!-- who-to-contact:start -->
**No verified company contact on file yet for this idea.** Every board it is built from is a community design on OSHWHub, where the author is an individual, not a supplier. Nothing has been invented to fill the gap: use the manufacturing houses and the directory entries below, follow the [zero-experience founder playbook](/playbook.html), and treat the first quote you get as the real data. Company websites only; no personal contacts are published.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [MINI手持示波器 超MINI版](/db/oshwhub-mini-shou-chi-shi-bo-qi5-0.html) (open ultra-mini handheld oscilloscope); [#训练营#简易示波器](/db/oshwhub-simple-oscilloscope.html) (open simple oscilloscope design for the entry variant); [仪器训练营便携示波器及H750核心板复刻](/db/oshwhub-training-camp-portable-oscilloscope-re-engraving.html) (open portable scope with STM32H750 core for the pro variant); [五位半电压表](/db/oshwhub-wu-wei-ban-dian-ya-biao.html) (open 5½-digit voltmeter for the precision mode).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**B. To a PCBA / EMS house — quote from the open design files** (send to Kingbrother, Foxlink or any assembler you vet; see the [playbook](/playbook.html#manufacturer))

```email
Subject: PCBA quote from open design files — School Scope, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a School Scope: A €59 pocket oscilloscope + voltmeter kit designed for physics classrooms: safe banana inputs, pre-loaded experiments and a teacher dashboard instead of a 200-page manual. The design starts from published open-hardware files (MINI手持示波器 超MINI版, #训练营#简易示波器, 仪器训练营便携示波器及H750核心板复刻, 五位半电压表; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — School Scope，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款School Scope：A €59 pocket oscilloscope + voltmeter kit designed for physics classrooms: safe banana inputs, pre-loaded experiments and a teacher dashboard instead of a 200-page manual。设计基于已公开的开源硬件文件（MINI手持示波器 超MINI版, #训练营#简易示波器, 仪器训练营便携示波器及H750核心板复刻, 五位半电压表；含原理图、PCB和BOM），并做了我们自己的修改。

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

## 5. Next steps (this week)
1. Fab the mini handheld open design and the simple scope, add a protection breadboard; show an RC-charging curve on one by day 10.
2. Write 4 one-page worksheets (RC charging, AC vs DC, sound, rectifier) with a physics teacher; print them.
3. Contact your national physics-teacher association for the next conference date and email 20 teachers a one-lesson trial offer.

Want help sourcing or building this? Talk to us via www.gongbans.com.
