# Hot-Water Compliance Logger — Founder Start Pack

> Clamp-on hot-water temperature loggers for multi-family buildings that produce the proof the housing manager needs (≥55/60 °C hold, circulation checks) without a plumber walking the basement.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** German and Austrian landlords with central hot water ("Großanlage": >400 L storage or >3 L in any pipe run) must have Legionella sampled every three years, and the technical rules expect ≥60 °C at the tank outlet and ≥55 °C on the circulation return. Energy-saving pressure pushes temperatures down; nobody has a continuous record until the lab result comes back bad and the health office asks for the logs.
- **Customer:** Property managers (Hausverwaltungen) and housing associations with 6–30-unit buildings — too small for a BMS, too many buildings to walk. They pay; the caretaker and the sampling lab use it.
- **Product:** A DIN-rail hub next to the boiler with four clamp-on thermocouple probes (tank outlet, circulation return, cold inlet, one riser), optional RS485 to the heat meter/pump, LoRaWAN uplink to a portal that emits a monthly compliance PDF per building. €399 per building kit + €9/month (estimates).
- **Why now:** TrinkwV 2023 tightened operator duties; heat-pump retrofits and "Absenkung" debates make 55 °C a daily argument; LoRaWAN coverage in German cities is now routine (municipal utilities' networks) and private gateways cost €100.
- **The ask:** ~€95k to 1,000 building kits; three paid pilots first, then a housing-association framework deal and a regional digitalisation grant.

## 2. Business plan

### Problem & customer

The Trinkwasserverordnung puts the duty on the "Betreiber" — the landlord. Sampling every three years (annually for public buildings) is the visible cost (€150–400 per building per round). The invisible cost is the failed sample: >100 CFU/100 ml triggers notification to the Gesundheitsamt, a risk assessment, thermal disinfection, re-sampling and — if the cause was "tank set to 50 °C to save gas" — a liability argument with the tenants. A continuous temperature log is what every risk-assessment template asks for and almost nobody has below the BMS class.

- **Who pays:** the Hausverwaltung (bills it to the owners as operating cost, Betriebskosten, where allowed), the Wohnungsgenossenschaft's technical department, or the WEG's board. Decision maker: the technical property manager who signs sampling contracts today.
- **Who uses:** the caretaker (looks at a traffic light), the sampling lab (asks for the log when a result is marginal), the health office (reads the PDF).
- **Adjacent users:** heating contractors who maintain the boiler and would install the kit for €150.

### Market size (estimates — check)

- **TAM:** Germany has ≈ 3.3M multi-family buildings; roughly 40% have central hot water with a Großanlage → ~1.3M buildings; Austria adds ~0.15M. At €399 + €108/year → **€580M** hardware + **€155M/year** recurring theoretical.
- **SAM:** buildings managed professionally (managers with ≥20 buildings) in DE/AT ≈ 500k → **€200M** + €54M/year.
- **SOM (3 years):** 6–10k buildings via 30–50 managers and two associations → **€2.5–4M** hardware + €0.7–1M/year recurring. Year 1: 500–1,000 kits.

Sources used: Hamburg and Mannheim city information sheets on TrinkwV 2023 (Großanlage thresholds, 3-year interval, 100 CFU/100 ml action value), Berlin tenants' association guidance, LoRaWAN sensor prices at m2mgermany/reichelt/antratek. Building-stock split: estimate from census data — verify.

### Competition (2 searches)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing — sample every 3 years, hope | €150–400 per round | No evidence when a sample fails; the question is only "what did the tank do last winter" |
| Boiler controller's own log (Viessmann, Vaillant, Buderus) | €0 | Logs the tank, not the circulation return; no export, no PDF, proprietary portal |
| Standalone LoRaWAN pipe sensors: Senlab T TEM-LAB-24NS (€194–230), Dragino D20S-LB (~€55), Milesight | €55–230 per sensor | Sensor only; you still need a gateway, a platform and someone to write the compliance logic — managers don't |
| Metering companies' Legionella services (sampling + reporting) | €200–500 per building per round | Periodic, not continuous; our log makes their report better — partner, don't fight |
| BMS / DDC for large buildings | €5–20k | Not viable below 30 units |
| Caretaker with a contact thermometer and a clipboard | labour | Done monthly at best, undocumented |

**Wedge:** the only sub-€500 kit whose output is the document the health office wants, installed by the existing heating contractor in 30 minutes without opening a pipe.

### Product & value proposition

- Hub: DIN-rail controller (StamPLC-class: ESP32-S3, relays/inputs, RS485) with a LoRaWAN module, mains adapter from the boiler-room socket.
- Probes: four K-type surface thermocouples with pipe clamps or thermal paste + insulation sleeve; the isolated KMeter-class input handles long leads and the boiler's earth potential. Surface-mounted → no drinking-water-contact approval needed.
- Optional: RS485 (M-Bus adapter later) to read the heat meter and the circulation pump status — proves the pump actually ran.
- Rules engine: ≥60 °C tank outlet, ≥55 °C return, tank "Legionellenschaltung" peak detected weekly, circulation pump duty; exceptions logged with duration.
- Portal: building list, traffic lights, monthly PDF per building with the limit lines, export to the manager's software (CSV/API). Sampling-lab share link.
- **Pricing (estimates):** €399 per building kit (hub + 4 probes + gateway-less if the city has coverage), €149 private gateway if not; €9/month/building for the portal; install by a contractor €150 (their revenue).

### Unit economics (estimates, EUR per building kit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-S3 module €3, isolated 4-ch thermocouple front end €9, LoRaWAN module EU868 €7, RS485 transceiver isolated €2, DIN enclosure + terminals €6, PSU 230 V→12 V external adapter €4, PCB + passives €5) | 36 | 30 |
| 4× K-type surface probes with clamps + 3 m leads | 14 | 10 |
| PCBA assembly + test (thermocouple channel calibration in a water bath jig) | 5.0 | 3.2 |
| Enclosure (standard DIN housing, printed label — no tooling) | 0 | 0 |
| Packaging + insulation sleeves + install guide | 3.5 | 2.6 |
| Freight + duty to EU | 2.6 | 1.3 |
| Certification amortised (€30k: RED with pre-certified module, EMC, safety, EN 18031) | 30.0 | 6.0 |
| **Landed cost** | **91** | **53** |
| Direct sale at €399 ex VAT, less €15 fulfilment/support | 384 | 384 |
| **Gross margin hardware** | **€293 (76%)** | **€331 (86%)** |
| Portal €9/month → €108/year at ~€1.50/building/month hosting + support | €90/year (83%) | €90/year (83%) |

Hardware margin is fine; the business is the recurring €9. Price the hardware so the manager's approval is trivial, not so you get rich on it.

### Go-to-market

**First 100 customers:** three Hausverwaltungen in one city (the kill question), reached through the regional property-manager association (VDIV/IVD regional groups), the sampling labs (they know every landlord with a bad result) and two heating contractors who maintain boilers in multi-family buildings. Offer: €399 pilot per building, 3 buildings each, portal free for 6 months, you install the first ones yourself and learn.

**Scale:** housing-association frameworks (GdW member companies in DE, gemeinnützige Bauvereinigungen in AT), sampling labs as resellers (bundle "sampling + continuous log"), heating-contractor networks (installer margin €60 per kit + install fee), municipal utilities that run LoRaWAN networks and sell smart-building services.

### 12-month plan

- **Q1:** kill question (3 paid pilots), works-like kit from StamPLC + KMeter-ISO + LoRaWAN Unit, rules engine, PDF v1, legal review of the TrinkwV/DVGW W 551 wording in the report.
- **Q2:** own PCB (hub with 4 isolated TC channels + LoRa module + RS485), 30 buildings live, portal v1, contractor install guide.
- **Q3:** certification (RED with module, EMC, safety, EN 18031), pilot batch 50, first association framework, sampling-lab partnership.
- **Q4:** production 500–1,000, AT launch, M-Bus/heat-meter reading, API to two property-management software packages.

**Team:** founder (sales to managers, domain), 1 embedded engineer (ESP-IDF, LoRaWAN, thermocouple front end), 1 web developer (portal, PDF, API), part-time building-services engineer (SHK background) for the rules and the install guide.

**Funding to 1,000 units (estimate):** NRE €20k (PCB, DIN housing adaptation, probe sourcing, water-bath jig) + certification €30k + portal development €25k + 9 months lean salaries €55k + 1,000 kits at €61 landed €61k = **€190k**, less revenue from the first 300 kits (€120k) and portal fees → **€95k** net. Route: pilots paid up front, a regional "Digitalisierung Wohnungswirtschaft" grant, and a €50–75k angel from the property sector. Bootstrap-able if the founder sells first and builds second.

### Top risks

- **Technical — surface probes read 2–5 K below water temperature.** Mitigation: insulation sleeve over the probe, calibrated offset per pipe size, and report "surface temperature, corrected" with the method stated; validate against immersion readings in the pilots.
- **Market — managers say "the sampling company handles it".** Mitigation: partner with the sampling labs; the log makes their risk assessment faster and the failed-sample conversation shorter.
- **Regulatory — you are producing compliance evidence.** Never claim "TrinkwV-compliant device"; claim "continuous documentation supporting the operator's duties under TrinkwV and DVGW W 551". Lawyer reviews the PDF wording once.
- **Regulatory — tenants' data.** Temperatures are building-level, not personal; keep it that way (no per-flat consumption).
- **Supply — LoRaWAN module and thermocouple front-end ICs.** Both multi-source; the isolated TC amplifier has 2–3 drop-in alternatives. Buy 1k with the first production.
- **Coverage — LoRaWAN in basements.** Mitigation: external antenna on the hub, private gateway SKU, optional NB-IoT variant in year 2.

## 3. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit KMeter-ISO (U133-V11) | https://www.gongbans.com/db/m5stack-unit-kmeter-iso.html | Isolated thermocouple input; proves the measurement chain on pipes above 60 °C | enclosure/structure files only; electronics not published | Off-the-shelf module; use as bought in the pilot, design your own 4-ch front end for production |
| M5Stack StamPLC (K141) | https://www.gongbans.com/db/m5stack-stamplc.html | DIN-rail hub next to the boiler: inputs, relays, RS485, ESP32-S3 | enclosure/structure files only | Off-the-shelf; pilot hub |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | Basement-to-gateway uplink in the pilot | enclosure/structure files only | Off-the-shelf module; in production use a pre-certified LoRaWAN module |
| M5Stack Unit RS485-ISO (U094) | https://www.gongbans.com/db/m5stack-unit-rs485-iso.html | Reads heat meters and circulation pumps (Modbus RTU) | enclosure/structure files only | Off-the-shelf module |

None of the four publish electronics — the pilot is assembled from bought modules; production is your own board. Plan for that from day one.

### Block diagram

```
[TC1 tank outlet] [TC2 circ. return] [TC3 cold inlet] [TC4 riser]
        \              |                |               /
         [4-ch isolated thermocouple front end] --SPI--> [ESP32-S3 hub, DIN rail] --UART--> [LoRaWAN EU868 module] ~~> gateway ~~> portal
[heat meter / pump] --RS485 (isolated)----------------------^   |
[230 V socket] --> [external 12 V adapter] --> 3.3 V -----------+
Portal: rules (≥60/≥55 °C, weekly peak, pump duty) -> monthly PDF per building -> manager / lab / health office
```

**Engineering gap:** a 4-channel isolated thermocouple board (the Unit is single-channel), surface-probe accuracy method, the rules engine mapped to DVGW W 551 practice, the PDF nobody argues with, Modbus profiles for the common heat meters, and LoRaWAN fleet management (join, keys, downlinks for config).

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| ESP32-S3-WROOM-1 | €3 | Multi-source |
| Thermocouple-to-digital converter ×4 (MAX31855/MAX31856-class) + digital isolator | €9 | 2–3 alternatives; watch lead times |
| LoRaWAN module EU868, pre-certified (RAK/Seeed/Murata-class) | €7 | Multi-source; pre-certification saves €8k |
| Isolated RS485 transceiver | €2 | Multi-source |
| K-type surface probe, pipe-clamp, 3 m fibreglass lead ×4 | €14 | Many suppliers; specify tolerance class 1 |
| DIN-rail enclosure 6 TE + pluggable terminals | €6 | Standard catalogue parts |
| 12 V/1 A wall adapter, CE-marked | €4 | Buy certified |
| SMA bulkhead + 868 MHz antenna | €2.5 | |

### Firmware/software starting point

- ESP-IDF with the LoRaWAN stack of your module vendor (most pre-certified modules run AT commands or LoRaMac-node; search for the vendor's reference).
- ChirpStack (open-source LoRaWAN network server) or The Things Stack for the pilot; many German municipal utilities offer TTN/TTS coverage.
- Node-RED for the first rules engine, then a proper service; Grafana for the internal view.
- PDF generation: any server-side library (search for your stack); the content matters more than the tool.
- Modbus RTU: libmodbus or the ESP-IDF Modbus component.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | Three property managers agree to a paid €399 pilot within 4 weeks of first contact (the kill question). Fewer than three: stop or change the buyer (try sampling labs). Meanwhile one StamPLC + KMeter-ISO + LoRaWAN kit logs your own or a friend's boiler room. |
| 3–5 | Works-like | 4-channel kit from modules, surface vs immersion comparison on three pipe sizes within ±2 K after correction, LoRaWAN uplink every 10 min, PDF v1 reviewed by one sampling lab. |
| 6–8 | Looks-like + EVT | Own hub PCB v1 in a DIN housing, 9 buildings live (3 managers × 3), contractor installs one in under 30 min from the guide; EMC pre-scan. |
| 9–10 | DVT + pre-compliance | PCB v2, RED/EMC/safety pre-test, EN 18031 checklist, water-bath calibration jig built, lawyer-reviewed report wording. |
| 11–12 | Pilot batch | 50 kits from a CM, golden sample, 30 buildings live, first manager converts to the €9/month portal; pump/heat-meter reading demonstrated on two brands. |

### Certification checklist (EU)

- **CE / RED:** LoRaWAN → EN 300 220 (radio), EN 301 489-1/-3 (EMC), EN 62368-1 (safety; low voltage only, external certified adapter). A pre-certified module reduces radio testing to a system-level check.
- **RED delegated act — EN 18031-1 (and -2 if personal data: building-level temperatures are not, keep it that way):** applies; LoRaWAN devices are internet-connected via the gateway.
- **CRA:** reporting duties in force since September 2026, full obligations December 2027; signed firmware over LoRaWAN downlink (small payloads — plan a local USB update path too), SBOM, disclosure policy.
- **RoHS, REACH, WEEE** registration (DE: stiftung ear; AT: EAK); packaging (LUCID).
- **Battery regulation:** not applicable (mains-powered hub); if you add a battery-powered riser node later, the Battery Regulation and UN 38.3 apply.
- **GDPR:** no personal data on device; portal has manager accounts → standard processor agreement.
- **Drinking-water regulations:** surface-mounted probes → no DVGW/UBA contact approval. Do not move the probe into the water.
- **Estimated test costs:** RED system test with pre-certified module €6–9k, EMC €5k, safety €3k, EN 18031 €12–18k, documentation €2k. Budget **€30k**.

### Validation toolkit

- **Kill question:** do three property managers sign a paid €399 pilot within 4 weeks of first contact? **Cheapest experiment:** a one-page offer with a sample monthly PDF (mock data from your own boiler room, made with the Unit kit) and 15 phone calls. Cost < €400 and your time.
- **5-question interview (technical property manager):** 1) How many of your buildings have central hot water, and who sets the tank temperature? 2) What happened the last time a Legionella sample came back positive — hours, euros, letters? 3) Do you have any temperature record between sampling rounds? 4) Who would install a clamp-on sensor — your caretaker, the heating contractor, or nobody? 5) Would a monthly PDF per building for €9 be something you'd forward to the owners, and who approves €399 per building?
- **Landing page:** headline "Proof your hot water stayed above 60 °C — every day, every building." Bullets: "Clamp-on sensors, 30-minute install, no pipe opened"; "Monthly compliance PDF per building for the health office and the lab"; "€399 per building + €9/month — no BMS, no plumber".
- **Pass threshold:** 3 paid pilots in 4 weeks; then 30 buildings under contract within 3 months of pilot start.

### First production checklist

- Samples: 3 module kits, 10 EVT hubs, 50 pilot kits; archive two.
- Golden sample: water-bath calibration record per channel, LoRaWAN link budget test from a basement, signed.
- DFM review: terminal pitch for thermocouple wire, isolation creepage on the TC front end, antenna cable routing, DIN clip strength.
- MOQ talk: PCBA 500; LoRa module 1k reel; probes 1k; DIN housings are catalogue parts.
- QC/AQL: level II, AQL 1.0/2.5; 100% channel test at two temperatures; 100% LoRaWAN join test.
- Packaging: kit box with probes coiled, insulation sleeves, clamps, printed install guide with QR to the portal.
- Incoterms: FOB Shenzhen; no batteries.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit KMeter-ISO (U133-V11)](/db/m5stack-unit-kmeter-iso.html) (isolated thermocouple input, good above 100 °C pipes); [M5Stack StamPLC (K141)](/db/m5stack-stamplc.html) (DIN-rail hub next to the boiler); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (basement-to-roof range); [M5Stack Unit RS485-ISO (U094)](/db/m5stack-unit-rs485-iso.html) (read existing heat meters and pumps). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*
- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094) — for a Hot-Water Compliance Logger

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Hot-Water Compliance Logger: Clamp-on hot-water temperature loggers for multi-family buildings that produce the proof the housing manager needs (≥55/60 °C hold, circulation checks) without a plumber walking the basement. The design is built around your M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094).
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
主题：样品订购及批量报价 — M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094) — 用于Hot-Water Compliance Logger

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hot-Water Compliance Logger：Clamp-on hot-water temperature loggers for multi-family buildings that produce the proof the housing manager needs (≥55/60 °C hold, circulation checks) without a plumber walking the basement。产品设计基于贵司的M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094)。
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
Subject: PCBA quote from open design files — Hot-Water Compliance Logger, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Hot-Water Compliance Logger: Clamp-on hot-water temperature loggers for multi-family buildings that produce the proof the housing manager needs (≥55/60 °C hold, circulation checks) without a plumber walking the basement. The design starts from published open-hardware files (M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Hot-Water Compliance Logger，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hot-Water Compliance Logger：Clamp-on hot-water temperature loggers for multi-family buildings that produce the proof the housing manager needs (≥55/60 °C hold, circulation checks) without a plumber walking the basement。设计基于已公开的开源硬件文件（M5Stack Unit KMeter-ISO (U133-V11), M5Stack StamPLC (K141), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit RS485-ISO (U094)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order StamPLC, KMeter-ISO, LoRaWAN-EU868 and RS485-ISO units plus four K-type surface probes; clamp them on the nearest boiler room you can access and log for a week.
2. Draft the one-page monthly compliance PDF with mock data and the TrinkwV/DVGW W 551 limit lines; show it to one sampling lab and ask what they'd change.
3. Call 15 property managers from the regional association list with the pilot offer; book the three.

Want help sourcing or building this? Talk to us via www.gongbans.com.
