# Makerspace Soldering & Rework Station — Founder Start Pack

> A CE-ready low-voltage soldering station, hot-air controller and DC pre-heater built on open controller boards, sold as a bundle to European makerspaces and schools with a maintenance-friendly design.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Labs buy either €40 no-name stations that die in a semester (and have a mains heater and a dubious earth) or €400–800 branded ones they can't afford ten of. Open controller designs with cartridge-tip support exist but have no European safety file, no spare-parts supply and no lock-out for a classroom.
- **Customer:** Makerspaces, FabLabs, vocational schools (Berufsschulen, ROCs, lycées pro), university labs and the education distributors that supply them. The lab manager specifies; the school or the association pays.
- **Product:** A metal, ESD-safe bench set: cartridge-tip soldering station (C210/C245-class, 24 V), DC pre-heater plate, and — in v2 — a hot-air unit with its own certified heater module. One external CE-marked PSU keeps mains out of the box. Classroom features: temperature lock-out, auto-sleep, tip counter, spares stocked in the EU. €249 station, €299 station + pre-heater bundle (estimates).
- **Why now:** Cartridge tips are now commodity (C245 clones at €4), the open controller boards publish schematic + PCB, and labs across Europe are re-equipping for electronics curricula. Nobody sells the "boring, repairable, documented" tier.
- **The ask:** ~€75k to the first 1,000 stations; pre-orders from 10 makerspaces fund the first batch, no tooling beyond a sheet-metal case.

## 2. Business plan

### Problem & customer

Walk into any makerspace: four stations work, two have a broken handle, one is a Pinecil someone brought. The lab manager wants ten identical stations that survive students, tips they can order next week, a temperature cap so nobody runs 450 °C all day, and a device the facility manager won't question when the fire-safety inspector asks about mains inside a cheap plastic box.

- **Who pays:** the makerspace association (membership fees, grants), the school's equipment budget (often via a distributor with a framework agreement), the university department.
- **Who uses:** members and students — careless, constant, unsupervised. Design for abuse.
- **Who specifies:** the lab manager / teacher; the distributor's catalogue is the gate.

### Market size (estimates — check)

- **TAM:** EU makerspaces/FabLabs ≈ 2,500; vocational schools with electronics ≈ 8,000; universities with EE/physics labs ≈ 1,500 departments; plus hobbyist tail. At 8 stations per site: 96k stations; at €249 → **€24M** per refresh cycle (5–7 years). The hobby market (≈ €200M for irons/stations EU-wide, rough) is upside, not the target.
- **SAM:** DE/NL/AT/FR/Nordic institutions buying through education distributors ≈ 60% → **€14M**.
- **SOM (3 years):** 6–9k stations → **€1.5–2.2M**. Year 1: 800–1,200.

Sources used: price comparisons on tomshardware / atomic14 / microcontrollerslab (Hakko FX-888D ~$105–135 and discontinued in favour of FX-888DX; JBC CD-B ~$600–850; Aixun T3A ~$60–110; Pinecil ~$26–40; KSGER T12 ~$54). Institution counts: estimates from national FabLab registries and education statistics — verify.

### Competition (1 search)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing — keep the mixed fleet | €0 | Downtime and spares chaos; the manager's problem, not the budget's |
| No-name 60 W mains stations / 858D clones | €25–60 | Mains heater and triac in a plastic box, no spares, die fast |
| Pinecil V2 / TS101 USB-C irons | €30–45 | Great tool, no station, no lock-out, walks out the door |
| KSGER T12, Aixun T3A/T420D, Sugon T36 (cartridge clones) | €55–130 | Good heat; no CE file worth the name, no EU spares, no classroom mode |
| Hakko FX-888DX / Weller WE1010 | €130–200 | Trusted, but a conical 900-series tip and slower; no classroom lock-out |
| JBC CD-B / Weller WT / Ersa i-CON | €450–850 | The benchmark; a lab can afford two, not ten |

**Wedge:** JBC-class cartridge heat and recovery at Hakko money, in an all-DC metal box with a real EU safety file, classroom lock-out, and tips/handles/heaters on a shelf in Europe.

### Product & value proposition

- **Station:** 24 V input (external 150 W CE-marked desktop PSU, the kind every laptop brand already certifies), C245-compatible handle, 1.8" colour display, PID with tip-type detection, sleep-in-stand, lock-out via PIN or NFC tag (teacher sets a max of e.g. 380 °C), tip-life counter, USB-C for firmware and logs.
- **Pre-heater:** 24 V DC heating plate (100 × 100 mm, up to 200 °C) with its own controller from the open DC heating-plate design; shares the PSU connector and firmware family.
- **Hot-air (v2):** a 700 W heater does not fit an all-DC story — be honest. Option A: mains heater inside a separately certified heater module with the open 858-class controller driving a certified SSR; option B: a weaker 24 V/150 W hot-air pencil for SMD rework only. Decide after the station sells.
- ESD-safe powder-coated steel case, grounded tip, replaceable handle cable with a locking connector.
- **Pricing (estimates):** station €249 (education net €199 in 5+); pre-heater €119; bundle €329; spares: C245 tips €9, handle €39, heater €25. Hobby web price €279.

### Unit economics (estimates, EUR per station)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (MCU €1.5, display 1.8" €3.5, precision op-amp + ADC front end €2.5, MOSFET stage + protection €2.5, 24 V→5/3.3 V regulators €1.5, connectors incl. locking handle socket €4, PCB + passives €4) | 19.5 | 16.5 |
| C245-compatible handle + 1 cartridge tip + stand | 18 | 14 |
| External 24 V/150 W CE/UKCA PSU | 11 | 9 |
| PCBA assembly + test (heat-up/recovery test on a jig) | 3.5 | 2.4 |
| Enclosure (sheet-metal, powder coat, laser-cut — no tooling) | 9.0 | 6.5 |
| Packaging + manual + tip card | 2.5 | 1.8 |
| Freight + duty to EU (heavy-ish, sea for 5k) | 4.5 | 2.2 |
| Certification amortised (€14k: EMC + safety on the DC side, RoHS/REACH; PSU already certified) | 14.0 | 2.8 |
| **Landed cost** | **82** | **55.2** |
| Education net €199 ex VAT, less €8 fulfilment | 191 | 191 |
| **Gross margin education** | **€109 (57%)** | **€136 (71%)** |
| Distributor net €160 ex VAT | €78 (49%) | €105 (66%) |

Spares are the second business: tips and handles at 60%+ margin, every semester, forever.

### Go-to-market

**First 100 customers:** 10 makerspaces pre-ordering a 5-station class set (the kill question). Reach them via the FabLab networks (national FabLab associations in DE/NL/FR, the Verbund Offener Werkstätten), the makerspace managers' mailing lists and Discord servers, and the two or three European makerspace conferences. Offer: €249 per station, delivery in 10 weeks, free spares kit for the first ten labs that write a review.

**Scale:** education distributors (the ones with framework agreements for school labs in DE/NL/FR), electronics retailers' education channels, hobby e-tailers for the €279 web SKU, university procurement portals once you have references. Content: a "soldering station buyer's guide for labs" that ranks yourself honestly against JBC.

### 12-month plan

- **Q1:** kill question (10 pre-orders), works-like station from the open controller board + C245 handle, PID tuning, lock-out firmware, pre-heater prototype from the open DC plate.
- **Q2:** own PCB (controller + handle socket + USB-C), sheet-metal case, 20 EVT units in 4 labs, pre-compliance EMC; spares supply chain set up (tips, handles, heaters) with an EU stock point.
- **Q3:** DVT, EMC/LVD certification, pilot batch 50 (the 10 class sets), first distributor listing.
- **Q4:** production 500–1,000, pre-heater launch, hot-air decision, hobby SKU online.

**Team:** founder (product, education sales), 1 embedded engineer (control loop, display, lock-out), part-time mechanical/sheet-metal designer, a fulfilment partner holding spares in the EU, a teacher as paid advisor for the classroom mode.

**Funding to 1,000 units (estimate):** NRE €15k (PCB, case design, jig) + certification €14k + 9 months lean salaries €45k + 1,000 stations at €68 landed €68k + initial spares stock €8k = **€150k**, less 50 pre-ordered class-set stations (€12k) and ongoing sales during the year (~€60k) → **€75k** net. Route: pre-orders + bootstrap; an education-focused angel or a maker-hardware crowdfunding campaign for the hobby SKU if you want speed. No tooling makes this one of the cheaper packs to start.

### Top risks

- **Technical — cartridge compatibility.** C245 clones vary; thermocouple position and heater resistance differ. Mitigation: calibrate per tip type, publish the supported-tip list, stock your own tips.
- **Safety — hot surfaces, students.** EN 62368-1 touch-temperature limits apply to the station body, not the tip; design the stand so the tip can't touch the case. Sleep-in-stand is a safety feature as much as a tip saver.
- **Market — distributors like brands with 30 years.** Mitigation: references from ten labs, a 3-year warranty, spares guarantee in writing.
- **Regulatory — a hot-air unit with a mains heater changes the file** (LVD on a mains appliance, more tests). Mitigation: keep it out of v1.
- **Supply — handles and heaters from small Shenzhen vendors.** Mitigation: qualify two handle vendors, hold 6 months of spares in the EU.
- **IP — "C245" is JBC's design; clones are tolerated but not endorsed.** Mitigation: call it "C245-compatible", never use the JBC name in marketing beyond compatibility, and watch the trademark line.

## 3. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| 数控智能焊台 (OSHWHub) | https://www.gongbans.com/db/oshwhub-shuo-kong-gao-pin-zhi-neng-han-tai.html | Open digital soldering-station controller — your control loop and front-end starting point | schematic, pcb | OSHWHub project licence — check the project page before commercial derivation |
| 54X-AT热风枪控制器主板模块858 (OSHWHub) | https://www.gongbans.com/db/oshwhub-re-feng-qiang-kong-zhi-qi-mo-kuai.html | Open 858-class hot-air controller: OPA336 front end, CX32 MCU, 1.8" display, PID, relay protection — the v2 hot-air brain | schematic, pcb | OSHWHub project licence — check |
| 直流低压加热台 DC/Mini (OSHWHub) | https://www.gongbans.com/db/oshwhub-zhi-liu-di-ya-jia-re-tai-v1.html | Open DC low-voltage heating plate — the pre-heater | schematic, pcb | OSHWHub project licence — check |
| TPS63020 (OSHWHub) | https://www.gongbans.com/db/oshwhub-tps63020.html | Buck-boost regulator reference for the logic rails | schematic, pcb | OSHWHub project licence — check |

All four publish schematic and PCB — rare luck. Still redraw for production: CE needs your own documented design, and you want the handle connector and USB-C your way.

### Block diagram

```
[24 V / 150 W external CE PSU] --> [station PCB]
   |-- 24 V --> [MOSFET heater stage] --> [C245 cartridge heater]
   |-- TC sense <-- [precision op-amp + ADC] <-- cartridge thermocouple
   |-- [MCU: PID, tip detect, sleep, lock-out] --> [1.8" display] [encoder/buttons] [buzzer]
   |-- [stand switch] [NFC/PIN lock-out] [USB-C: firmware, logs]
   |-- aux 24 V out --> [pre-heater controller + 100x100 heating plate]
Case: steel, earthed; tip earthed via handle; no mains inside.
```

**Engineering gap:** tip-type detection and per-tip calibration tables; the classroom lock-out and a teacher UX that takes 20 seconds; a locking, abuse-proof handle socket; a thermal design for the 150 W stage; and the hot-air decision.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| 32-bit MCU (STM32G0/CX32-class) | €1.5 | Multi-source; pick one with an ESP-less toolchain you like |
| Precision op-amp + 16-bit ADC | €2.5 | Multi-source |
| Power MOSFET + driver, fuse, TVS | €2.5 | |
| 1.8" TFT 160×128 SPI | €3.5 | Many panel houses |
| C245-compatible handle + stand + 1 tip | €18 | Qualify two vendors; this is your spares business |
| Locking handle connector (GX16/aviation or custom) | €2 | Pick a standard, long-life type |
| 24 V/150 W desktop PSU, CE/UKCA, IEC C8 inlet | €11 | Buy certified; demand the test report |
| Sheet-metal case, powder coat, silk screen | €9 at 1k | Laser-cut + bent; no tooling |
| 100×100 mm aluminium heating plate 24 V 120 W + controller | €12 | For the pre-heater SKU |

### Firmware/software starting point

- IronOS (open-source firmware for Pinecil/TS100-class irons) — not for your hardware, but the best-documented reference for PID, sleep and tip handling logic; search the repo.
- The firmware in the open OSHWHub projects above (check what the authors published and under which licence).
- STM32 HAL/LL or the CX32 vendor SDK; LVGL is overkill for a 1.8" panel — a small graphics lib is fine.
- For logs/lock-out: a simple USB-C CDC console; NFC via a cheap NTAG reader if you want tag-based teacher mode.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | 10 makerspaces pre-order a 5-station class set at €249/station (deposit €50/station). Fewer than 5 sets: stop or re-price. Meanwhile one open controller board + C245 handle on the bench: heat-up to 350 °C in <10 s, recovery after a big joint <3 s. |
| 3–5 | Works-like | PID stable across three tip geometries, sleep-in-stand, PIN lock-out, tip counter, running on the open board + hacked case; pre-heater plate holds 150 °C ±5. |
| 6–8 | Looks-like + EVT | Own PCB v1, sheet-metal case v1, 20 units in 4 labs for 3 weeks; failures logged; touch temperatures measured; EMC pre-scan (switching heater stage). |
| 9–10 | DVT + pre-compliance | PCB v2 and case v2, LVD/EMC pre-test clean, drop test, handle connector life test 5,000 cycles, spares catalogue finalised. |
| 11–12 | Pilot batch | 50 stations (the 10 class sets) from a CM, golden sample, calibration jig, teacher guide, 3-year warranty terms. |

### Certification checklist (EU)

- **CE:** EMC Directive (EN 55014-1/-2 or EN 55032/35 — ask the lab which family fits a soldering station) + LVD via EN 62368-1 or EN 60335-2-45 (the standard for soldering irons — check applicability for a 24 V device; the PSU carries its own LVD). Document hot-surface and touch-temperature compliance.
- **No radio** → no RED, no EN 18031. Keep it that way for the station (USB-C only). If you ever add WiFi, RED and CRA apply fully.
- **CRA:** a non-connected device with a USB port has minimal obligations; still provide a firmware-update policy because the lock-out is a security feature.
- **RoHS, REACH, WEEE** registration; packaging registration.
- **Battery regulation:** not applicable.
- **Machinery Regulation:** not applicable to hand soldering tools (check with the lab).
- **Hot-air v2 with a mains heater:** full LVD on a mains appliance, likely EN 60335-2-45 — budget a separate €10–15k file.
- **Estimated test costs:** EMC €5–7k, safety (DC side, touch temperatures, abnormal-operation tests) €5k, RoHS/REACH documentation €2k. Budget **€14k** for the station; pre-heater adds €4k.

### Validation toolkit

- **Kill question:** will 10 makerspaces pre-order a 5-station class set at €249 per station? **Cheapest experiment:** a one-page offer with photos of the open controller + handle on the bench, a spec table against Hakko/JBC/Aixun, and 30 emails/DMs to lab managers. Cost < €200.
- **5-question interview (lab manager):** 1) How many stations do you have, and how many work right now? 2) What died last — tip, handle, controller, PSU? 3) Who orders spares and how long does it take? 4) Has anyone ever asked you about the safety file or the earth on your stations? 5) At €249 with a 3-year warranty and spares in the EU, how many would you order and who signs?
- **Landing page:** headline "The lab soldering station that survives students." Bullets: "Cartridge-tip heat and recovery at a quarter of the branded price"; "All-DC metal box, external CE-certified supply — nothing scary inside"; "Teacher lock-out, auto-sleep, and spares shipped from Europe within a week".
- **Pass threshold:** 10 class sets (50 stations) with €50/station deposits in 4 weeks.

### First production checklist

- Samples: 3 bench units, 20 EVT, 50 pilot; keep one per revision.
- Golden sample: heat-up/recovery curves on a jig, touch temperatures, lock-out behaviour, signed by you and the CM.
- DFM review: case tolerances for the PCB and connector, powder-coat masking for earth points, handle socket retention, PSU cable strain relief.
- MOQ talk: PCBA 500; handles 500; PSU 500 (certified models have MOQs); sheet metal 300.
- QC/AQL: level II, AQL 1.0/2.5; 100% functional heat test; 100% earth continuity test (tip to PSU earth).
- Packaging: double-wall box, foam insert, tip card, warranty card, QR to the teacher guide.
- Incoterms: FOB Shenzhen; declare the PSU separately on the invoice (different HS code).

## 4. Who to contact

<!-- who-to-contact:start -->
**No verified company contact on file yet for this idea.** Every board it is built from is a community design on OSHWHub, where the author is an individual, not a supplier. Nothing has been invented to fill the gap: use the manufacturing houses and the directory entries below, follow the [zero-experience founder playbook](/playbook.html), and treat the first quote you get as the real data. Company websites only; no personal contacts are published.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [数控智能焊台](/db/oshwhub-shuo-kong-gao-pin-zhi-neng-han-tai.html) (open digital soldering-station controller); [54X-AT热风枪控制器主板模块858](/db/oshwhub-re-feng-qiang-kong-zhi-qi-mo-kuai.html) (open hot-air gun controller main board); [直流低压加热台 DC/Mini](/db/oshwhub-zhi-liu-di-ya-jia-re-tai-v1.html) (open DC low-voltage heating plate); [TPS63020](/db/oshwhub-tps63020.html) (buck-boost regulator reference).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**B. To a PCBA / EMS house — quote from the open design files** (send to Kingbrother, Foxlink or any assembler you vet; see the [playbook](/playbook.html#manufacturer))

```email
Subject: PCBA quote from open design files — Makerspace Soldering & Rework Station, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Makerspace Soldering & Rework Station: A CE-ready low-voltage soldering station, hot-air controller and DC pre-heater built on open controller boards, sold as a bundle to European makerspaces and schools with a maintenance-friendly design. The design starts from published open-hardware files (数控智能焊台, 54X-AT热风枪控制器主板模块858, 直流低压加热台 DC/Mini, TPS63020; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Makerspace Soldering & Rework Station，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Makerspace Soldering & Rework Station：A CE-ready low-voltage soldering station, hot-air controller and DC pre-heater built on open controller boards, sold as a bundle to European makerspaces and schools with a maintenance-friendly design。设计基于已公开的开源硬件文件（数控智能焊台, 54X-AT热风枪控制器主板模块858, 直流低压加热台 DC/Mini, TPS63020；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order the open soldering-station controller PCB (from the OSHWHub files) plus a C245-compatible handle, two tips and a 24 V/150 W desktop PSU; get it heating by the weekend.
2. Write the one-page class-set offer with a spec table against Hakko FX-888DX, Aixun T3A and JBC CD-B; send it to 30 makerspace managers.
3. Read EN 60335-2-45 scope and EN 62368-1 touch-temperature clauses (or ask a test lab for a 30-minute pre-assessment) to settle which safety standard applies to a 24 V station.

Want help sourcing or building this? Talk to us via www.gongbans.com.
