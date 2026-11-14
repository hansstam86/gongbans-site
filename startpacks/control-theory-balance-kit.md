# Control-Theory Balance Kit — Founder Start Pack

> A self-balancing reaction-wheel triangle and a BLDC momentum-wheel module with open firmware, so engineering students tune a real PID/LQR loop on their desk instead of in simulation.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Control-engineering labs run on inverted pendulums that cost €2,000+ per station and sit behind a booking sheet; most students never touch a real loop. The cheap alternative is a two-wheel balancing robot that teaches nothing about state-space.
- **Customer:** Universities and universities of applied sciences (control, mechatronics, robotics), engineering bootcamps and serious makers in DE/NL/UK/Nordics/FR. The department or lab budget pays; lecturers and students use it.
- **Product:** A €299 station: a Reuleaux-triangle reaction-wheel balancer (ESP32, rechargeable) plus a swappable BLDC momentum-wheel module, a safety cage, a lab manual with 8 experiments, and live parameter streaming to a browser plot. Sold as 10-station class sets.
- **Why now:** Three open reaction-wheel designs exist with schematics and PCB files; the physics is visually compelling (it balances on a corner); departments buy class sets each summer; the cheapest commercial rotary pendulum kit is ~€130–170 and still needs a bench supply and a PC, the "real" ones are quote-only with 16-week lead times.
- **The ask:** ~€70k (estimate) to the first 1,000 units; route = lecturer pre-orders for next semester + bootstrap; education-innovation grants fit.

## 2. Business plan

### Problem & customer
The lecturer owns the problem: a course on PID/LQR/state estimation, 60–200 students, a lab with 4–8 stations of expensive gear, and a lab assistant who repairs it. They want each student pair to own a loop for a semester, break it, and fix it. The procurement office wants a quote, CE, and a supplier that invoices. The student wants it to balance on day one and still be interesting in week 12.

Segments: (1) **universities of applied sciences** (Fachhochschulen, hogescholen, polytechnics) — practical, buy class sets, decide fast; (2) **research universities** — bigger budgets, slower, want LQR/Kalman depth and MATLAB/Python hooks; (3) **bootcamps/makerspaces/individuals** — small, pay retail, generate content.

### Market size (estimates)
- EU + UK: ~1,500 institutions teaching control or mechatronics (estimate); say 2 courses × 10 stations each → **30k stations** TAM × €299 ≈ **€9 M**, replacement every ~6 years. Add individuals/makers: ~5k units over 3 years.
- **SAM:** institutions in the 6 countries above with a hands-on lab culture and English or local-language manuals we ship — 40% → **€3.6 M**.
- **SOM (3 years):** 10% of SAM → ~1,200 stations → **€360k**, plus individuals ~€250k. A lifestyle-scale company unless you expand into a family (pendulum, cart, drone-on-a-stick) — which is the plan: the firmware, plotting and manual are reusable across platforms.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Quanser-class rotary pendulum / teaching labs ([Quanser](https://www.quanser.com/products/introduction-to-controls-teaching-lab/), [QNET on NI ELVIS](https://www.ni.com/en/shop/hardware/academic-accessory-boards/model-quanser-qnet-rotary-inverted-pendulum-board-2-0-for-ni-elvis-ii-ii-)) | The gold standard; quote-only, 16–17-week lead time on the NI listing | Price per seat, needs a PC + DAQ + amplifier, one station per group |
| STMicro STEVAL-EDUKIT01 rotary pendulum (~$133–174, [ST](https://estore.st.com/en/steval-edukit01-cpn.html), [DigiKey](https://www.digikey.co.uk/en/product-highlight/s/stmicroelectronics/steval-edukit01-evaluation-kit)) | Cheap, open course material | Stepper + Nucleo, needs a PC, not self-contained, no reaction-wheel dynamics, no class-set logistics |
| ESP32 two-wheel balancing robots (M5Stack BALA-C ~$54–95, Elektor Mini-Wheelie €79.95 — [Core Electronics](https://core-electronics.com.au/bala-c-plus-esp32-self-balancing-robot-kit.html.md), [Elektor](https://www.elektor.com/21087)) | Fun, cheap | Toy-class; no manual mapped to a syllabus; a single PID, no model |
| Academic DIY builds (ASEE "under $100 kit", [paper](https://peer.asee.org/affordable-lab-kit-for-controls-education)) | Every department has one | Built by a PhD who left; no spares, no CE |
| Simulation only (MATLAB/Simulink, Python) — "do nothing" | Free, scalable | Students never feel sensor noise, saturation, or a motor that gets hot |

**Wedge:** a self-contained reaction-wheel station (no PC needed to run; browser plot to tune), a manual that maps to a real syllabus (PID → cascade → state-space → LQR → observer → disturbance), class-set packaging with a charging case, and a price that lets every pair have one.

### Product & value proposition
Hardware: Reuleaux-triangle body (CNC aluminium or thick PCB-sandwich), brushless reaction wheel with a proper 3-phase driver, IMU, ESP32 (WiFi/BLE), Li-ion cell with USB-C charging, a clear acrylic cage so a spinning wheel never meets a finger. Module B: standalone BLDC momentum-wheel on a pendulum arm for the "simple" first weeks. Firmware: swappable controllers (PID, cascade, LQR, user-written C or Python-generated gains), 200 Hz parameter streaming to a browser page over WiFi, CSV logging, "disturbance" button, safety limits (wheel speed, tilt). Manual: 8 experiments, each with model, expected plot, and questions. Teacher dashboard optional (class set only).

Pricing (estimates): **€299 per station retail**, **€2,690 per 10-station class set** with charging case and spares (≈ €269/station), momentum-wheel-only module €129, manual free (PDF). B2B via education distributors at 30% off.

### Unit economics (estimates per station, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32 module, 3-phase driver, BLDC motor, IMU, Li-ion cell, charger, PCB) | €34.00 | €27.00 |
| Assembly & test (SMT, motor fit, IMU calibration, balance test) | €7.00 | €5.00 |
| Enclosure/mechanics (machined or cast body, flywheel, acrylic cage) | €14.00 | €9.00 |
| Packaging (box, USB-C cable, quick card) | €2.80 | €2.00 |
| Freight + duty to EU (with Li-ion: DG surcharge) | €4.50 | €2.80 |
| Certification amortised (~€28k: RED, EMC, safety, UN 38.3, EN 18031) | €28.00 | €5.60 |
| **Landed cost** | **€90.30** | **€51.40** |
| Sell price (retail €299 / distributor €209) | €299 | €209 |
| **Gross margin** | **€208.70 (70%)** | **€157.60 (75% at distributor)** |

Class-set price lowers it to ~€269; still > 65%.

### Go-to-market
**First 100 customers:** 5 lecturers who order a class set for next semester (kill question) — found through control-engineering course pages, IFAC/EUCA mailing lists, and the people who post lab videos; 20 individual pre-orders from robotics/control communities (r/ControlTheory-type forums, hackaday-style blogs, YouTube control channels); a conference demo table at a control-education workshop.

**Scale channels:** education-equipment distributors (the ones who sell Nucleo/ELVIS gear to labs), textbook authors (bundle "the kit for chapter 7–12"), university framework tenders, a yearly summer "new semester" campaign.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Build 10 units from the open triangle design; manual v0 (4 experiments); 5 lecturers commit for next semester. |
| Q2 | Own PCB (driver + ESP32 + IMU), machined body, cage; EVT 30; browser plotting; pre-compliance. |
| Q3 | DVT, certification, 200-unit pilot = first class sets delivered before term starts; manual v1 (8 experiments). |
| Q4 | 1,000 units; distributor; momentum-wheel module; second platform spec (cart-pole or pendulum) using the same electronics. |

**Team:** 1 embedded/control engineer (driver, IMU, controllers — full-time), 1 mechanical engineer (part-time: body, cage, DFM), 1 lecturer-author for the manual (contract), founder for sales. Three people, one and a half full-time.

**Funding to first 1,000 units (estimates):** NRE €45k (PCB €10k, mechanics/tooling €15k, firmware/plotting €12k, manual €8k) + certification €28k + 1,000 units landed ~€62k + 9 months overhead €55k ≈ **€190k**; minus class-set pre-orders (5 sets ≈ €13k) and pilot sales (~€55k) and individual pre-orders (~€20k) ≈ **~€100k**; with a national education-innovation grant typically covering €30–50k of the manual/content, **~€70k** net. Bootstrap + pre-orders; angels only if you commit to the platform family.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** motor heat and wheel speed limits make "LQR on a hot motor" look like a defect | Design for 20-minute continuous sessions; thermal cut-back with an on-screen explanation (it's a lesson, not a bug) |
| **Technical:** IMU drift, mechanical tolerances → every unit balances differently | Factory calibration routine; publish per-unit parameters; the manual turns variation into an identification exercise |
| **Safety:** spinning flywheel near students | Cage, speed limit in firmware, EN 62368-1 mechanical hazard review; no exposed wheel ever |
| **Market:** procurement cycles are yearly; you miss September | Pre-order in Feb–May for September delivery; sell individuals year-round |
| **Regulatory:** WiFi/BLE → RED + EN 18031 + CRA; Li-ion → UN 38.3, battery regulation | Pre-certified module; local-only networking (no internet needed) narrows EN 18031 scope; a removable cell meets the 2027 removability rules |
| **Supply:** small BLDC motors and 3-phase drivers from a few vendors | Qualify two motors with identical mounting; driver IC with a second-source footprint |
| **Licence:** three OSHWHub designs | Read each licence; your own PCB and body — use them as proofs, not production files |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Self-balancing Reuleaux triangle, ESP32, rechargeable, 10×10 (OSHWHub) | https://www.gongbans.com/db/oshwhub-zi-ping-heng-di-lai-luo-san-jiao-10-10-ban-ben.html | The core: proven ESP32 reaction-wheel balancer with charging | schematic, pcb | **OSHWHub — licence varies; read it** |
| Reuleaux triangle V2, ESP32, brushless drive EG2133 (OSHWHub) | https://www.gongbans.com/db/oshwhub-zi-ping-heng-di-lai-luo-san-jiao-10-10-ban-ben-copy.html | Brushless version — the production direction | schematic, pcb | OSHWHub — check licence |
| Reuleaux-triangle momentum wheel (OSHWHub) | https://www.gongbans.com/db/oshwhub-lai-luo-san-jiao-dong-liang-lun.html | Momentum-wheel module reference | schematic, pcb | OSHWHub — check licence |
| M5Stack Unit BLDC Driver (U181) | https://www.gongbans.com/db/m5stack-unit-bldc-driver.html | BLDC driver reference for the works-like | enclosure/structure only; electronics not published | Buy; documentation only |

### Block diagram
```
[IMU 6-axis] --I2C/SPI--> [ESP32 (WiFi/BLE)] --PWM x3--> [3-phase gate driver + MOSFETs] --> [BLDC + flywheel]
                              |   ^-- [motor current sense / hall or sensorless]
                              |--> [USB-C: charge + serial]  [Li-ion 1S + protection + fuel gauge]
                              |--> [WiFi AP: browser plot/tuning page, CSV]  [3 LEDs, 1 button: disturbance]
[Acrylic cage]  [Aluminium or PCB-sandwich Reuleaux body]  [Momentum-wheel module: same driver board on a pendulum arm]
```
**Engineering gap:** the open designs balance; the product is the controller framework (swappable, parameterised, streamed), the thermal/speed safety envelope, the body and cage mechanics at class-set cost, the calibration routine, and the manual. Expect 60% of the effort in firmware + manual.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 module | €2.60 | Pre-certified |
| 3-phase gate driver IC + 6 MOSFETs | €3.20 | Second-source footprint for the driver |
| BLDC outrunner motor (gimbal-class, 2204–2806) | €7.50 | **Two vendors qualified; mounting identical** |
| Flywheel (machined brass/steel) | €4.00 | Balance it; sole-source machining risk → 2 shops |
| IMU 6-axis | €1.80 | Multi-source footprint |
| Li-ion 18650 or pouch 1S + protection + charger + fuel gauge | €5.00 | UN 38.3 from the cell vendor; removable cell |
| PCB 4-layer + passives + USB-C | €4.50 | |
| Body (CNC aluminium or PCB-sandwich) + cage | €10.00 | PCB-sandwich body avoids tooling for the first 1k |
| Charging case (class set only, per 10) | €40.00 | Off-the-shelf case + custom foam |

### Firmware/software starting point
- **SimpleFOC** (Arduino FOC library for BLDC; exists on GitHub) — the fastest way to a torque-controlled wheel on ESP32.
- ESP-IDF/Arduino for the rest; **Teleplot** (VS Code extension, exists) for early plotting; later your own browser page over WebSocket.
- Controllers: write PID/LQR yourself (it's the product); generate LQR gains in Python (python-control exists) and paste them in; publish the model and the notebooks.
- OSHWHub project pages usually include firmware — read it for the sensor fusion and driver details, then rewrite under your own licence.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 10 units built from the open design balance for 10 minutes; manual v0 (4 experiments); **5 lecturers commit to a class set at €299/station for next semester** (runs to W8) |
| 3–5 | Works-like | Own driver+ESP32 board; SimpleFOC torque control; swappable PID/LQR with browser tuning at 200 Hz; thermal cut-back working |
| 6–8 | Looks-like + EVT | Body + cage v1; 30 units; a student group runs experiments 1–4 unsupervised and nobody touches the wheel; EMC pre-scan |
| 9–10 | DVT + pre-compliance | RED/EMC pre-compliance; EN 62368-1 mechanical hazard review; UN 38.3 report from the cell vendor; EN 18031 self-assessment (local AP only) |
| 11–12 | Pilot batch | 50 units = 5 class sets delivered; 2 lecturers run a full lab session; ≥ 80% of groups finish experiment 3 in one session |

### Certification checklist (EU)
- **CE under RED** (WiFi/BLE): EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** incl. mechanical hazard (flywheel) and battery; **EN 18031-1** if it can connect to the internet — design it as a local AP/BLE device and document that; -2/-3 not needed if no personal data or payments. Est. €6–9k RED/EMC, €4–6k safety, €0–12k EN 18031 depending on scope.
- **Battery:** UN 38.3 for the cell (vendor report), transport docs, **EU Battery Regulation** labelling and the 18 Feb 2027 removability/replaceability rules — use a removable cell.
- **RoHS, REACH, WEEE**, packaging registration.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware, update path, SBOM, vulnerability contact.
- **GDPR:** none if the plot page stores no names. **Toy directive:** not a toy — label 14+ / educational equipment; keep it out of toy channels.
- **Total certification budget estimate: €18–30k.**

### Validation toolkit
- **Kill question:** Do 5 control-engineering lecturers order a class set at €299 per station for next semester?
- **Cheapest experiment (~€900):** 10 units from the open design in printed bodies, a 4-experiment PDF, a 2-minute video of a student tuning a loop in a browser; email 50 lecturers with a "reserve a class set for September" form (€500 deposit per set).
- **5-question interview (lecturer):** 1) What hardware does your control lab use today, how many stations, how old? 2) What do students actually do hands-on in the course, and what do you wish they did? 3) Who approves a €3k purchase and how long does it take? 4) What would make a kit unusable for you — safety, language, software, spares? 5) If 10 stations cost €2,690 with a manual mapped to your syllabus, would you order for next semester?
- **Landing page:** headline "Tune a real control loop on every desk." Bullets: "A reaction-wheel balancer that runs PID, cascade and LQR — swap the controller, watch the plot in your browser." / "8 experiments mapped to a control course, with models and expected results." / "€299 per station, €2,690 per class set of 10 with charging case and spares."
- **Pass threshold:** 5 class-set reservations with deposit, or 60 individual pre-orders at €279 within 6 weeks.

### First production checklist
- Samples: 5 golden samples with IMU calibration data, motor KV, balance time, and a thermal log.
- DFM: flywheel balance spec, motor mount tolerance, cage fit, cell holder retention, USB-C strain.
- MOQ talk: motors 1k (ask for 2 vendors), flywheels 1k, driver ICs reel, cells 1k with UN 38.3, cases per 100.
- QC: AQL II 2.5/4.0; 100% balance test (60 s upright on a jig), 100% charge test; 5% 20-minute thermal soak.
- Packaging: cell inside → UN 3481 marking; class-set case with foam; quick card.
- Incoterms: FOB Shenzhen; air (DG-rated) for the first 200; sea later.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit BLDC Driver (U181)](/db/m5stack-unit-bldc-driver.html) (BLDC driver reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [自平衡的莱洛三角_esp32_可充电_10*10版本](/db/oshwhub-zi-ping-heng-di-lai-luo-san-jiao-10-10-ban-ben.html) (open self-balancing Reuleaux triangle (ESP32, rechargeable)); [莱洛三角V2-esp32-无刷驱动EG2133](/db/oshwhub-zi-ping-heng-di-lai-luo-san-jiao-10-10-ban-ben-copy.html) (V2 with brushless drive); [莱洛三角动量轮](/db/oshwhub-lai-luo-san-jiao-dong-liang-lun.html) (momentum-wheel module).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit BLDC Driver (U181) — for a Control-Theory Balance Kit

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Control-Theory Balance Kit: A self-balancing reaction-wheel triangle and a BLDC momentum-wheel module with open firmware, so engineering students tune a real PID/LQR loop on their desk instead of in simulation. The design is built around your M5Stack Unit BLDC Driver (U181).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit BLDC Driver (U181).
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
主题：样品订购及批量报价 — M5Stack Unit BLDC Driver (U181) — 用于Control-Theory Balance Kit

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Control-Theory Balance Kit：A self-balancing reaction-wheel triangle and a BLDC momentum-wheel module with open firmware, so engineering students tune a real PID/LQR loop on their desk instead of in simulation。产品设计基于贵司的M5Stack Unit BLDC Driver (U181)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit BLDC Driver (U181)。
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
Subject: PCBA quote from open design files — Control-Theory Balance Kit, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Control-Theory Balance Kit: A self-balancing reaction-wheel triangle and a BLDC momentum-wheel module with open firmware, so engineering students tune a real PID/LQR loop on their desk instead of in simulation. The design starts from published open-hardware files (自平衡的莱洛三角_esp32_可充电_10*10版本, 莱洛三角V2-esp32-无刷驱动EG2133, 莱洛三角动量轮; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Control-Theory Balance Kit，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Control-Theory Balance Kit：A self-balancing reaction-wheel triangle and a BLDC momentum-wheel module with open firmware, so engineering students tune a real PID/LQR loop on their desk instead of in simulation。设计基于已公开的开源硬件文件（自平衡的莱洛三角_esp32_可充电_10*10版本, 莱洛三角V2-esp32-无刷驱动EG2133, 莱洛三角动量轮；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Fab the open triangle board and V2 brushless board from the OSHWHub files, order motors and IMUs; get one balancing by day 10.
2. Write the 4-experiment manual outline (PID on the momentum wheel → PID balance → cascade → LQR) and film the first one.
3. List 50 lecturers from course pages in your 2 nearest countries; send the "reserve a class set for September" email with the video.

Want help sourcing or building this? Talk to us via www.gongbans.com.
