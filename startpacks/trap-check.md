# Trap Check — Founder Start Pack

> A €39 LoRaWAN sensor that clips onto any snap or box trap and tells the pest controller which traps actually need a visit — a no-poison, no-truck-roll upgrade for independents.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Independent pest controllers drive to every trap on a schedule to check it. Most are empty. The big chains have proprietary connected traps; independents can't buy them, and the LoRaWAN traps that are for sale cost $160–195 per trap.
- **Customer:** Pest-control SMEs (1–30 technicians) across DE, NL, BE, FR, UK, Nordics; facility managers of food warehouses and food plants under HACCP audits. They pay; their technicians use it.
- **Product:** A clip-on, universal trap sensor (shock + lever detection), 3–5-year primary cell, EU868 LoRaWAN, with a plain dashboard and CSV/API export to pest-control CRMs. Not a trap, not a biocide.
- **Why now:** EU pressure to reduce permanent rodenticide baiting pushes toward monitored mechanical traps; public LoRaWAN coverage and €50 indoor gateways make the network a non-issue; the catalogue has an open ESP32-C6 + LoRa stamp.
- **The ask:** ~€110k (estimate) to 1,000 nodes, firmware with multi-year battery life, and 10 paying SMEs. Route: pre-orders from the kill-question calls + a regional IoT/agritech grant + one angel from the facility-services world.

## 2. Business plan

### Problem & customer
A regional pest-control firm with 8 technicians services maybe 2,000 bait and trap points. A technician's day is 60% driving. Contracts with food businesses require documented inspections — the paperwork is as painful as the driving. The buyer is the owner (money, contract renewal, insurance). The user is the technician (needs: it clips on in 10 seconds and never cries wolf). The food-plant facility manager is the influencer: he wants the audit report to show monitored traps.

Europe's pest-control services market is estimated around **US$6.5 B (2024)** by one analyst house ([IMARC](https://imarcgroup.com/europe-pest-control-market)); the CEPA certification scheme alone has **>840 certified companies** ([BPCA/CEPA](https://bpca.org.uk/news-and-blog/sector/Page-74/will-you-be-cepa-400/187167)). The number of independent SMEs is not published; national associations list a few thousand per large country. Assume **~15,000 pest-control SMEs in EU + UK** (estimate).

### Market size (estimates)
- **TAM:** 15,000 SMEs × 500 monitored points = 7.5 M points × €39 ≈ **€290 M** hardware, plus €2/node/month ≈ €180 M/yr recurring if every point were monitored. It won't be; this is the ceiling.
- **SAM:** points in food-sector contracts (audit pressure justifies the €2/month) — assume 20% → 1.5 M nodes → **€58 M hardware + €36 M/yr**.
- **SOM (3-year):** 3% of SAM → 45k nodes → **€1.75 M hardware + €1.1 M/yr recurring**. That is a real company.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Proprietary chain systems (connected traps sold only with the chain's service) | Market-defining, well funded | Not available to independents; lock-in |
| LoRaWAN smart traps ($160–195 per trap; [Victor Smart-Kill LoRaWAN listing](https://www.embeddedworks.net/sens551e/)) | Sold as a complete trap | 4× our price; replaces the trap the customer already owns |
| Retrofit LoRaWAN trap sensors from EU IoT vendors (sold via distributors, ~€60–90 est.) | Closest competitor | Distributor-only, dashboard is an afterthought, no CRM export |
| BLE/RF-433 trap alarms | Cheap | Range measured in metres; needs someone on site |
| Manual rounds / "do nothing" | The default | Driving, paper, missed catches that start to smell |
| DIY (ESP32 + reed switch) | Hobbyist | No battery life, no dashboard, no audit trail |

**Wedge:** price (€39 + €2), universal clip that fits the snap and box traps the technician already uses, 3–5-year battery, and an export the technician's CRM can ingest so the inspection report writes itself. Sources also: [TTI rodent-trap business case](https://partners.thethingsindustries.com/business-cases/rodent-trap-monitoring/).

### Product & value proposition
Hardware: 55 × 30 × 15 mm IP65 pod, universal clip/strap, 3-axis accelerometer (shock = snap fired), optional reed/lever input for box traps, EU868 LoRaWAN Class A, 1× AA Li-FeS2 or ½AA Li-SOCl2 primary cell, magnet-swipe pairing. Firmware: event uplink on trigger, daily heartbeat (battery, temperature), downlink config. Dashboard: map/list of traps per site, alert by push/SMS/email, inspection log with timestamps, CSV and REST export. Works on public LoRaWAN, TTN, or a €60 indoor gateway you sell with the kit.

Pricing (estimates, B2B): **€39/node** (€35 at 100+), **€2/node/month** platform (min €20/month per account), starter kit (10 nodes + gateway) €449. Food-plant direct: same hardware, €3/node/month with audit-report module.

### Unit economics (estimates per node, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (LoRa SoC/module, accelerometer, reed, cell holder, antenna, PCB) | €10.80 | €8.60 |
| Primary cell (Li-FeS2 AA or ½AA Li-SOCl2) | €1.60 | €1.30 |
| Assembly & test (SMT, flash, RF test, provisioning keys) | €2.40 | €1.60 |
| Enclosure (IP65 case, gasket, clip/strap; tooling amortised) | €2.90 | €1.80 |
| Packaging (10-pack) | €0.40 | €0.25 |
| Freight + duty to EU (lithium cells → DG surcharge) | €1.30 | €0.70 |
| Certification amortised (~€28k: RED, EMC, EN 18031, battery transport) | €28.00 | €5.60 |
| **Landed cost** | **€47.40** | **€19.85** |
| Sell price | €39 | €39 |
| Channel margin (direct at 1k; 20% to distributors at 5k) | €0 | €7.80 |
| **Gross margin** | **–€8.40 (loss)** | **€11.35 (29%)** |

Hardware loses money until ~2k units and only earns modestly after; the **€24/node/year recurring at ~85% margin** is the business. Price the starter kit to cover certification; sell the hardware at cost if the customer commits to 24 months of platform.

### Go-to-market
**First 100 customers (really: first 10 SMEs, ~1,000 nodes):**
1. Ten regional pest-control firms from the kill-question calls; offer the founding-customer deal (nodes at €29, platform €2, 24-month term).
2. National association meetings and trade days (DE: Deutscher Schädlingsbekämpfer-Verband events; UK: PestEx; NL/BE: KAD/NVPB days). Bring a trap that texts the room when it snaps.
3. Food-safety consultants who audit factories — they recommend monitoring.

**Scale channels:** pest-control wholesalers (the distributors who sell traps and bait), CRM vendors' integration marketplaces, LoRaWAN network operators' partner programmes (several European utilities/telcos run LoRaWAN and want devices).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | 10 kill-question calls; works-like on Stamp C6LoRa + LoRaWAN unit + Unit Limit; 20 nodes in 2 firms for 6 weeks; dashboard v0 on TTN. |
| Q2 | Custom node PCB with a low-power LoRa SoC; enclosure tooling; EVT 100; battery-life model validated; RED pre-compliance. |
| Q3 | DVT; full certification; pilot 500 nodes across 8 firms; CRM CSV export; gateway bundle. |
| Q4 | 1,000+ nodes shipped; distributor signed; platform MRR ≥ €2.5k. |

**Team:** 1 firmware/RF engineer (LoRaWAN, low power — full-time), 1 backend/web developer (full-time from Q2), founder for sales/ops. Mechanical design and RF test bought in.

**Funding to first 1,000 units (estimates):** NRE €45k (PCB spins €10k, tooling €15k, antenna/RF work €8k, dashboard contractor €12k) + certification €28k + first 1,000 nodes landed ~€20k + 9 months lean salaries/overheads €70k ≈ **€163k**; minus pre-orders/pilot income (~€50k) ≈ **~€110k**. Route: pre-orders (kill question), regional IoT/innovation grants (LoRaWAN and "smart agri/food" programmes exist in NL, DE, FR), then an angel with facility-services background. Keep VC for when MRR is real.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** 3–5-year battery is a promise; the ESP32-C6 is not the lowest-power LoRa MCU | Use the C6LoRa stamp for prototypes only; design the production node around a dedicated LoRa SoC or module; measure sleep current in week 4, not week 40 |
| **Technical:** false triggers (forklift bumps, doors slamming near a trap) | Accelerometer threshold + pattern; lever/reed input for box traps as the "truth" channel; configurable per site |
| **Market:** independents aren't tech buyers; wholesalers take a year | Sell the audit report, not IoT; let the food-plant customer pull it through the pest firm |
| **Regulatory:** RED with EN 300 220 is routine via a pre-certified module; EN 18031 adds cost | Use a module with its own RED report; budget EN 18031 from day one |
| **Supply:** primary lithium cells have DG shipping rules and allocation issues | Qualify two cell brands; ship cells separately for the first batch if needed |
| **Scope:** customers ask you to make the trap | Don't. Traps have humane-trapping rules; you are a sensor |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | Open ESP32-C6 + LoRa stamp: the prototype node core | pcb, schematic (Altium) | M5Stack repo licence — check before copying into a commercial board |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | EU868 LoRaWAN module with AT-command stack for the first run | enclosure/structure only | Buy the unit; its module vendor sells the module directly for production |
| M5Stack Unit Limit (U145) | https://www.gongbans.com/db/m5stack-unit-limit.html | Mechanical lever detection for box traps | enclosure/structure only | Buy for prototype |
| Seeed Grove Collision Sensor | https://www.gongbans.com/db/seeed-grove-collision-sensor.html | Shock detection alternative | schematic | Seeed wiki resources; check licence |

### Block diagram
```
[snap trap] --shock--> [3-axis accel, interrupt] --+
[box trap lever] --> [reed/microswitch] -----------+--> [LoRa SoC / module + MCU] --868 MHz--> [gateway] --> [LNS: TTN/ChirpStack] --> [dashboard, alerts, CSV/API]
[AA Li-FeS2 cell] --> [LDO/boost] ------------------+
[magnet swipe] --> [reed: pairing/test] ------------+
```
**Engineering gap:** the catalogue gives you radio + sensors as modules. Missing: a sub-10 µA sleep design, antenna tuned inside a plastic pod lying on concrete, a universal clip that fits five trap families, false-trigger logic, provisioning at scale (DevEUI/keys), and the dashboard with CRM export. The firmware power budget is the heart of the product.

### Starter BOM (estimates per node at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| LoRaWAN module (pre-certified, EU868) or LoRa SoC | €4.50 / €3.20 | Module is faster to certify; SoC is cheaper at 5k+. **Lead times 8–16 weeks on allocation** |
| Low-power MCU (if not in module) | €0.90 | |
| 3-axis accelerometer with interrupt | €0.70 | Multi-source |
| Reed switch ×2 | €0.20 | |
| AA Li-FeS2 or ½AA Li-SOCl2 cell + holder | €1.60 | DG goods; two brands qualified |
| PCB antenna or 868 MHz chip antenna + matching | €0.40 | Tune in the enclosure |
| PCB 2-layer | €0.60 | |
| IP65 enclosure + gasket + clip/strap | €2.90 | **Tooling €12–18k**; use an off-the-shelf IP65 box for the first 100 |

### Firmware/software starting point
- Node: LoRaMac-node (Semtech reference LoRaWAN stack, exists on GitHub) or the module vendor's AT firmware. For ESP32-C6 prototypes, M5Stack's Unit LoRaWAN Arduino library (search "M5Unit-LoRaWAN").
- Network server: The Things Stack (TTN public or self-hosted) or ChirpStack — both exist, both open.
- Dashboard: Node-RED + Grafana for the pilot; your own web app after. CRM export: CSV first, REST later.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 10 calls to regional pest-control firms with the €39 + €2 offer. Kill question: average intended month-one deployment ≥ 50 nodes. Also: works-like node from C6LoRa + LoRaWAN unit + Unit Limit on TTN sending "snap" to a phone |
| 3–5 | Works-like | 20 prototype nodes in off-the-shelf boxes in 2 firms; >95% of real snaps detected, <1 false alarm/node/month; dashboard v0 |
| 6–8 | Looks-like + EVT | Custom PCB v1 around production radio; printed/CNC pod with clip; sleep current < 10 µA measured; antenna tuned in pod; RED pre-scan |
| 9–10 | DVT + pre-compliance | 100 units; EN 300 220 / EN 301 489 pre-compliance; EN 18031 self-assessment; drop and IP65 tests; battery model confirms ≥3 years at 1 event/day + daily heartbeat |
| 11–12 | Pilot batch | 300–500 nodes across 8 firms; two firms sign 24-month platform terms; MRR starts |

### Certification checklist (EU)
- **CE under RED:** EN 300 220-2 (868 MHz SRD), EN 301 489-1/-3, EN 62311 (exposure), EN IEC 62368-1 or EN 62368-1 safety (battery device). Using a pre-certified LoRaWAN module cuts radio testing to a "module integration" check (~€3–5k); full module-less RED ~€8–12k.
- **EN 18031-1** (RED delegated act, cybersecurity, mandatory since 1 Aug 2025 for internet-connected radio equipment — LoRaWAN nodes connected via a gateway count; most assessors treat them as in scope). Est. €8–15k incl. notified body where needed.
- **CRA:** reporting duties from 11 Sept 2026, full application 11 Dec 2027. Secure join procedure (LoRaWAN 1.0.4/1.1 keys), signed firmware, SBOM, vulnerability disclosure page.
- **RoHS, REACH, WEEE** (register as producer in each country you sell in).
- **Battery Regulation (EU) 2023/1542** + **UN 38.3** for lithium primary cells; transport labelling (UN 3090/3091); user-replaceable AA design keeps you on the easy side.
- **GDPR:** trap data isn't personal; technician location/time stamps in the dashboard are — minimal, but write the privacy notice.
- Not a biocide, not a trap; **state clearly it is a monitoring accessory**.
- **Total certification budget estimate: €22–32k.**

### Validation toolkit
- **Kill question:** Ten calls to regional pest-control firms — "€39 per sensor, €2/month, works with your existing traps — how many would you deploy in month one?" Pass = average ≥ 50 nodes.
- **Cheapest experiment (~€600):** 5 C6LoRa + LoRaWAN-unit nodes taped to real traps in a warehouse, TTN public network, a free Node-RED dashboard; a 90-second video of a trap snapping and a phone buzzing. Use it in the calls.
- **5-question interview (owner of a pest-control SME):** 1) How many trap/bait points do you service, and how often are they checked? 2) What share of visits find an empty trap? 3) Which customers demand documentation, and how do you produce it today? 4) Which CRM/route software do you use? 5) At €39 + €2/month per point, which 50 points would you connect first, and what would make you say no?
- **Landing page:** headline "Only drive to the traps that caught something." Bullets: "Clips on any snap or box trap you already own." / "Battery for 3–5 years, works on public LoRaWAN or our €60 gateway." / "Audit-ready inspection log, exported straight to your CRM."
- **Pass threshold:** 5 firms place paid pre-orders totalling ≥ 500 nodes (deposit €10/node) within 8 weeks.

### First production checklist
- Samples: 10 golden samples with RF power/frequency measured and recorded; one per enclosure colour.
- DFM with EMS: antenna keep-out, test pads for current measurement, programming + key-provisioning jig; agree who holds the DevEUI/AppKey database (you do).
- MOQ talk: module MOQ 500–1k; enclosure 1k; cells 1k. Get a 5k price step in writing.
- QC: AQL II 2.5/4.0; 100% RF test (TX power, frequency error) and sleep-current test; 1% IP65 sample dunk test.
- Packaging: 10-pack with lithium-battery handling labels; cells installed or separate per your DG decision.
- Incoterms: FOB Shenzhen; DG surcharge for lithium — get the forwarder quote before you promise a delivery date.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa stamp: the node core); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN module for the prototype run); [M5Stack Unit Limit (U145)](/db/m5stack-unit-limit.html) (mechanical trap-triggered detection). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Collision Sensor](/db/seeed-grove-collision-sensor.html) (alternative shock detection). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor — for a Trap Check

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Trap Check: A €39 LoRaWAN sensor that clips onto any snap or box trap and tells the pest controller which traps actually need a visit — a no-poison, no-truck-roll upgrade. The design is built around your M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor.
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
主题：样品订购及批量报价 — M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor — 用于Trap Check

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Trap Check：A €39 LoRaWAN sensor that clips onto any snap or box trap and tells the pest controller which traps actually need a visit — a no-poison, no-truck-roll upgrade。产品设计基于贵司的M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor。
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
Subject: PCBA quote from open design files — Trap Check, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Trap Check: A €39 LoRaWAN sensor that clips onto any snap or box trap and tells the pest controller which traps actually need a visit — a no-poison, no-truck-roll upgrade. The design starts from published open-hardware files (M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Trap Check，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Trap Check：A €39 LoRaWAN sensor that clips onto any snap or box trap and tells the pest controller which traps actually need a visit — a no-poison, no-truck-roll upgrade。设计基于已公开的开源硬件文件（M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit Limit (U145), Seeed Grove-Collision Sensor；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 5× Stamp C6LoRa, 5× Unit LoRaWAN-EU868, 5× Unit Limit and a TTN-compatible indoor gateway; have one node sending "snap" by day 5.
2. Write the 10-call script and the founding-customer offer; make the list of 30 regional pest firms (you'll need 30 to get 10 conversations).
3. Ask a LoRaWAN module vendor for its EU868 module datasheet, RED report, and lead time — the production radio decision is the long pole.

Want help sourcing or building this? Talk to us via www.gongbans.com.
