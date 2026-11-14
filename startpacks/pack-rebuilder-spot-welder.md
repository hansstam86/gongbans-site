# Pack-Rebuilder Spot Welder — Founder Start Pack

> A compact super-capacitor spot welder with current display and foot switch for rebuilding power-tool, household and solar battery packs — sold with a safety course to repair shops.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Anyone rebuilding a battery pack in Europe today welds with either a €40 marketplace box with no documentation and no CE file, a car battery and an Arduino kit, or a €500–2,000+ professional capacitive-discharge welder ([pricing guide](https://themakerschest.com/blogs/spot-welding-hub/how-much-does-a-battery-spot-welder-cost-2026-pricing-guide)). Repair shops want the middle: repeatable, documented, legal to put on a bench an employee uses.
- **Customer:** Battery-repair shops and pack rebuilders (power tools, garden tools, vacuum cleaners, solar storage), repair cafés, vocational schools in DE/NL/FR/UK/Nordics. The shop owner or school pays; the technician or student uses it.
- **Product:** A €199 bench welder: super-capacitor bank charged from a certified PSU, bipolar pulse, a pulse table for 0.1–0.2 mm nickel strip, current display, weld counter with QA log over USB, interlocked enclosure, foot switch, EU-stocked electrodes — and a 2-hour online safety course included.
- **Why now:** Right-to-repair rules and the EU Battery Regulation make pack rebuilding a legitimate trade that needs legitimate tools; two open super-capacitor welder designs with schematics and PCB exist; hobby welders have proven the market at the low end.
- **The ask:** ~€65k (estimate) to the first 1,000 units; route = live-demo deposits from repair shops + bootstrap; the safety course is the differentiator and a small recurring line.

## 2. Business plan

### Problem & customer
Rebuilding a pack means welding 20–100 nickel-strip joints onto cells without overheating them. A bad weld fails later; a hot weld damages the cell; a shorted strip is a fire. Pros use capacitive-discharge welders with calibrated energy; hobbyists use whatever. The repair shop in between — a two-person business fixing power-tool packs, a repair café, a vocational class — wants consistency, a log, and a tool that passes a workplace-safety look.

Who pays vs who uses: the owner/school pays; the technician/student uses it; the insurer and the labour inspector look at it. The safety course makes the owner comfortable putting a 17-year-old apprentice in front of it.

### Market size (estimates)
- EU + UK: ~6,000 battery/pack repair shops (estimate), ~2,500 repair cafés and repair associations (estimate from ~3,800 globally with most in Europe — [Global Repair Café Survey](https://cfsd.org.uk/wp-content/uploads/2026/06/4th-Global-Repair-Cafe-Survey-Results.pdf)), ~3,000 vocational schools and training centres with an electrical workshop (estimate), ~50k serious DIY builders (estimate) → **~60k seats**.
- **TAM:** 60k × €199 ≈ **€12 M** plus electrodes/strip consumables (~15%/year).
- **SAM:** professional segments only (shops, cafés, schools) → 11.5k → **€2.3 M** + consumables.
- **SOM (3 years):** 15% → 1,700 units → **€340k** + consumables ~€60k/year. A niche tool; profitable, not venture-scale. Pairs with the Cell Grader as a "rebuilder bench".

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Marketplace mini welders (€30–80, "Tier 1" in the [buyer's guide](https://themakerschest.com/blogs/spot-welding-hub/best-battery-spot-welders-in-2026-from-diy-to-production-grade)) | Cheap, everywhere | Random energy, no docs, no CE file, exposed terminals; shops can't defend them |
| kWeld-class kits (~$170 unit + $130 supercap unit, [forum](https://endless-sphere.com/sphere/threads/real-spot-welding-machines-which-is-the-better-deal.121064/latest)) | Excellent, respected, measured energy | Kit form, needs its own power source, no enclosure/interlock, no course |
| Malectrics-class Arduino welders (~$150–240 kit) | Open, popular | Needs a car battery or LiPo; hobby form factor |
| Professional CD welders ($500–2,000+; industrial $8,900+ — [Sunstone](https://sunstonewelders.com/collections/battery-welders)) | Calibrated, certified | Price; built for production lines |
| Solder or screw-terminal holders ("do nothing") | Some repairers | Heat damage, bad contacts; unprofessional |
| DIY from the open designs | Makers | No interlock, no PSU certification, nobody liable |

**Wedge:** a finished, enclosed, interlocked welder with measured current and a QA log at €199, plus a course and EU-stocked consumables — the first welder a shop owner can hand to an employee.

### Product & value proposition
Hardware: steel/ABS enclosure with a capacitor bank (super-caps, 2.7 V series bank or a single 3 V bank with balancing), half-bridge bipolar discharge (from the open bipolar design), charge from a certified 12 V / 5 A external PSU, pulse control by MCU with a current sensor (shunt + fast ADC or a Hall sensor), 2.4" display with strip-thickness presets, foot switch input, probe electrodes with copper tips (EU-stocked replacements), interlock: discharge disabled when the lid is open or the probes aren't both in contact, auto-bleed of the bank at power-off, weld counter and per-weld energy log over USB (CSV). Entry SKU: the low-power open design in the same enclosure at €129 for strip up to 0.15 mm.

Pricing (estimates): **€199 standard** (course included), **€129 entry**, €249 with a dual-probe pen handle, electrodes €19 per pair, nickel strip rolls at a margin; school 5-pack €849. No subscription; course renewal for new staff €29.

### Unit economics (estimates per unit, ex-VAT, standard SKU)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (super-cap bank €12, MOSFET half-bridge + drivers €6, MCU + display €5, current sense €2, PSU 12 V/5 A certified €5, PCB + copper bus €6) | €36.00 | €28.00 |
| Assembly & test (SMT, bus-bar assembly, pulse calibration on a test strip, interlock test) | €7.00 | €5.00 |
| Enclosure (steel base + ABS top, lid switch, probe holders; tooling amortised) | €9.00 | €6.00 |
| Packaging (box, probes, foot switch, 2 m strip sample, course card) | €4.50 | €3.50 |
| Freight + duty to EU | €4.00 | €2.50 |
| Certification amortised (~€18k: LVD/EN 62368-1 energy-hazard, EMC, RoHS) | €18.00 | €3.60 |
| **Landed cost** | **€78.50** | **€48.60** |
| Sell price (direct €199 / distributor €130) | €199 | €130 |
| **Gross margin** | **€120.50 (61%)** | **€81.40 (63% at distributor)** |

Consumables (electrodes, strip) at 50–60% margin make the repeat business.

### Go-to-market
**First 100 customers:** live weld demos at 10 battery-repair shops (kill question), a national repair-café network meeting, 3 vocational schools' electrical departments; DIY powerwall and e-tool repair forums and YouTube (5 review units — this crowd makes or breaks hobby tools); the trade association of electrical repairers.

**Scale channels:** repair-tool web shops and electronics distributors (test & tools category), vocational-training suppliers, battery-recycling/reuse consortia, cell and strip wholesalers (bundle), the Cell Grader customer list.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Build both open designs; pulse tables for 0.1/0.15/0.2 mm; 10 shop demos → deposits; lab pre-review of the energy-hazard design. |
| Q2 | Own PCB + bus-bar, enclosure with interlock, current logging; EVT 50; course v1 recorded; pre-compliance. |
| Q3 | DVT, certification, 300-unit pilot; electrodes and strip stocked in the EU; school 5-pack. |
| Q4 | 1,000 units; distributor; entry SKU; dual-probe pen. |

**Team:** 1 power-electronics engineer (bank, bridge, current sensing, interlock — full-time), 1 firmware/mechanical generalist (display, log, enclosure — part-time → full-time), founder for demos and sales; a workplace-safety trainer on contract for the course. Two and a half people.

**Funding to first 1,000 units (estimates):** NRE €32k (PCB + bus €8k, enclosure tooling €12k, firmware €6k, course production €6k) + certification €18k + 1,000 units landed ~€60k + 9 months overhead €50k ≈ **€160k**; minus demo deposits (~€25k), pilot sales (300 × €189 ≈ €57k) and consumables (~€13k) ≈ **~€65k**. Bootstrap + deposits; repair/circular-economy grants fit.

### Top risks
| Risk | Mitigation |
|---|---|
| **Safety/regulatory:** a capacitor bank storing tens of joules at hundreds of amps is an energy hazard under EN 62368-1; a lab may reject the design | Lab pre-review in Q1 (the second half of the kill question); interlock, auto-bleed, insulated bus, no exposed metal at bank potential; document the energy classes |
| **Technical:** weld consistency across strip, cell cap plating and electrode wear | Measured current + energy per pulse (not just time); electrode-wear counter; pulse tables validated on 500 welds with pull tests |
| **Market:** hobby crowd compares to €40 boxes | Sell to shops and schools; the hobby crowd buys the entry SKU or nothing |
| **Market:** niche | Keep NRE low; consumables and the course add margin; bundle with the Cell Grader |
| **Regulatory:** EMC — a 500 A pulse radiates | Short bus, twisted probe leads, filtering on the PSU input; EMC pre-scan early |
| **Supply:** super-caps from few vendors; MOSFETs in allocation cycles | Two cap vendors with the same can size; bridge footprint fits two MOSFET families |
| **Licence:** both open designs are OSHWHub | Read each licence; your own board — they prove the topology |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Bipolar super-capacitor spot welder (OSHWHub) | https://www.gongbans.com/db/oshwhub-bipolar-super-capacitor-spot-wel.html | Open half-bridge bipolar super-cap welder, 8 A charging, current display (STC 8051-class MCU) — the standard SKU's topology | schematic, pcb | **OSHWHub — licence varies; read it** |
| Low-power farad-capacitor spot welder (OSHWHub) | https://www.gongbans.com/db/oshwhub-kai-yuan-xiao-gong-lv-fa-la-dian-rong-dian-han-ji.html | Open low-power capacitor welder — the entry SKU | schematic, pcb | OSHWHub — check licence |
| M5Stack Unit INA226-10A (U200) | https://www.gongbans.com/db/m5stack-unit-ina226-10a.html | Logging of charge current/voltage on the bench rig (not the weld pulse — too fast) | enclosure/structure only; electronics not published | Buy; use the datasheet |

**Board-fact note:** the weld-pulse current (hundreds of amps, milliseconds) needs a fast shunt/Hall front-end of your own design; INA226-class parts are for the charge side.

### Block diagram
```
[Certified 12 V / 5 A PSU] -> [cap-bank charger, current-limited, balancing] -> [super-cap bank, auto-bleed on power-off]
                                                                                       |
[Foot switch] [Lid interlock] [Probe-contact detect] -> [MCU: pulse table, bipolar timing] -> [half-bridge MOSFET array + gate drivers]
                                                                 |                                   |
                                                [fast current sense: shunt/Hall + ADC]      [copper bus -> probe leads -> electrodes]
                                                                 |
                                            [2.4" display: thickness preset, last-weld current/energy, counter]
                                            [USB: CSV weld log]  [buzzer, fault LED]
```
**Engineering gap:** the safety architecture (interlock, bleed, energy classes), measured-energy control instead of time-only, bus-bar mechanics, electrode wear handling, the pulse tables and pull-test data, the course. The topology is proven.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Super-capacitor bank (e.g. 6× 2.7 V 100–200 F or equivalent) | €12.00 | **Two vendors, same can size**; lead time 8–12 weeks |
| MOSFETs for the half-bridge (8–12 high-current) + gate drivers | €6.00 | Footprint for two MOSFET families |
| MCU (STM32G0/ESP32-C3 without radio use) + 2.4" display | €5.00 | No radio in the product |
| Fast current sense (shunt + amp or Hall) | €2.00 | |
| Copper bus-bar + probe leads + 2 electrodes | €6.00 | EU-stocked consumable; copper price risk |
| Certified 12 V / 5 A PSU (external) | €5.00 | Buy certified; keep mains out |
| PCB 2 oz copper, passives, USB | €4.00 | |
| Steel base + ABS top + lid switch + probe holders | €9.00 | **Tooling €10–14k**; steel has low tooling |
| Foot switch | €2.50 | Off-the-shelf |

### Firmware/software starting point
- The two OSHWHub projects publish firmware on their pages (STC MCU) — read for timing, then rewrite for your MCU.
- The Malectrics open-source Arduino spot-welder firmware exists on GitHub (search "Arduino spot welder Malectrics") — a good reference for pulse/pre-pulse logic.
- Your own: measured-energy control, pulse tables, interlock state machine (fail-safe: any fault → bridge off, bank bleed), CSV log over USB.
- Course: slides + video; include electrode care, pack layout, cell venting response, PPE.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Both open designs built; 100 welds on 0.15 mm strip with pull tests; **10 battery-repair shops see a live demo — pass if ≥ 6 deposit €50 at €199**; a safety lab gives a written first opinion on the energy-hazard concept (runs to W6) |
| 3–5 | Works-like | Own bridge + bank + fast current sense; measured-energy pulses within ±5% shot to shot; 500 welds, pull-test pass ≥ 95%; interlock and auto-bleed work |
| 6–8 | Looks-like + EVT | Enclosure T1 with lid switch and probe holders; 50 units; EMC pre-scan; electrode-wear counter; course v1 |
| 9–10 | DVT + pre-compliance | EN 62368-1 energy-hazard review passes; EMC pre-compliance; 2,000-weld endurance on 3 units; CSV log validated |
| 11–12 | Pilot batch | 50 units to depositors + 2 vocational schools; ≥ 90% "would recommend"; 0 safety incidents; consumables reorder from ≥ 5 shops |

### Certification checklist (EU)
- **CE under LVD + EMC** (no radio): **EN IEC 62368-1** — the capacitor bank is an electrical energy source (ES/PS classification) and the discharge is a thermal/burn hazard; expect the lab to want the interlock, bleed, and insulation documented; **EN IEC 61000-6-1/-3** with attention to the pulse. Est. €5–8k safety, €4–6k EMC. If the external PSU is certified, mains stays out of your box.
- **Machinery Regulation?** A hand-held/foot-operated bench tool with no moving parts is generally not machinery — confirm with the lab; welding-equipment standards (EN IEC 60974 series) are for arc welding and don't fit; document why 62368-1 is the route.
- **RoHS, REACH, WEEE**, packaging registration. **Battery regulation:** no battery in the device (super-caps are not batteries) — keep it so.
- **CRA:** a device with digital elements that is not network-connected is low exposure; still: firmware update over USB, vulnerability contact, reporting duties from 11 Sept 2026, full application 11 Dec 2027.
- **GDPR:** none. **Toy directive:** no (professional tool, 16+/trained use wording).
- **Workplace:** the course covers PPE, ventilation, Li-ion handling; it is your sales argument and your liability shield — have a safety trainer sign off.
- **Total certification budget estimate: €12–18k.**

### Validation toolkit
- **Kill question:** Do 10 battery-repair shops buy at €199 after a live weld demo, and does a lab accept the capacitor energy-hazard design on first review?
- **Cheapest experiment (~€500 + a lab hour ~€300):** one open-design welder in a printed case with a lid switch, a bag of strip and 20 dead cells, a pull-test gauge; visit 10 shops; one hour with a safety lab engineer with your block diagram.
- **5-question interview (shop owner):** 1) What do you weld with today and what went wrong last time? 2) Who in the shop welds, and how were they trained? 3) Has an insurer, inspector or customer ever asked about your tools? 4) What would a weld log be worth to you — warranty, proof, nothing? 5) €199 with a 2-hour safety course and EU-stocked electrodes — deposit today?
- **Landing page:** headline "The spot welder you can hand to your apprentice." Bullets: "Super-capacitor bipolar pulses with measured current; presets for 0.1–0.2 mm nickel strip." / "Interlocked enclosure, auto-discharge, weld counter and QA log — and a 2-hour safety course included." / "€199. Electrodes and strip stocked in the EU."
- **Pass threshold:** 6 of 10 shops deposit, plus a positive lab first opinion; or 60 deposits from shops/schools in 6 weeks.

### First production checklist
- Samples: 5 golden samples with pulse calibration (energy vs preset), interlock test record, 500-weld pull-test sheet.
- DFM: bus-bar torque and plating, cap-bank mounting against vibration, lid switch alignment, probe-lead strain relief, PSU connector keyed.
- MOQ talk: super-caps 1k (two vendors), MOSFETs reel, display 1k, steel 500, ABS 1k, electrodes 5k pairs, strip rolls.
- QC: AQL II 2.5/4.0; 100% pulse test on a dummy load with current check; 100% interlock + bleed test; 2% 1,000-weld endurance.
- Packaging: probes and foot switch in the box; course access card; safety sheet; no lithium.
- Incoterms: FOB Shenzhen; air for 50; sea for 1,000.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit INA226-10A (U200)](/db/m5stack-unit-ina226-10a.html) (current/voltage logging of weld pulses). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [【开源】双极性超级电容点焊机](/db/oshwhub-bipolar-super-capacitor-spot-wel.html) (open bipolar super-capacitor spot welder with current display); [【开源】小功率法拉电容点焊机](/db/oshwhub-kai-yuan-xiao-gong-lv-fa-la-dian-rong-dian-han-ji.html) (open low-power capacitor welder (entry SKU)).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit INA226-10A (U200) — for a Pack-Rebuilder Spot Welder

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Pack-Rebuilder Spot Welder: A compact super-capacitor spot welder with current display and foot switch for rebuilding power-tool, household and solar battery packs — sold with a safety course to repair shops. The design is built around your M5Stack Unit INA226-10A (U200).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit INA226-10A (U200).
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
主题：样品订购及批量报价 — M5Stack Unit INA226-10A (U200) — 用于Pack-Rebuilder Spot Welder

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Pack-Rebuilder Spot Welder：A compact super-capacitor spot welder with current display and foot switch for rebuilding power-tool, household and solar battery packs — sold with a safety course to repair shops。产品设计基于贵司的M5Stack Unit INA226-10A (U200)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit INA226-10A (U200)。
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
Subject: PCBA quote from open design files — Pack-Rebuilder Spot Welder, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Pack-Rebuilder Spot Welder: A compact super-capacitor spot welder with current display and foot switch for rebuilding power-tool, household and solar battery packs — sold with a safety course to repair shops. The design starts from published open-hardware files (【开源】双极性超级电容点焊机, 【开源】小功率法拉电容点焊机; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Pack-Rebuilder Spot Welder，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Pack-Rebuilder Spot Welder：A compact super-capacitor spot welder with current display and foot switch for rebuilding power-tool, household and solar battery packs — sold with a safety course to repair shops。设计基于已公开的开源硬件文件（【开源】双极性超级电容点焊机, 【开源】小功率法拉电容点焊机；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Fab both OSHWHub boards (or clone the EasyEDA projects), order super-caps, MOSFETs and nickel strip; weld 100 joints and pull-test them by day 10.
2. Book one hour with a safety lab engineer; bring the block diagram and ask the energy-hazard question explicitly.
3. List 10 battery-repair shops within driving distance and book live demos for weeks 3–5; print a one-page spec with the course outline.

Want help sourcing or building this? Talk to us via www.gongbans.com.
