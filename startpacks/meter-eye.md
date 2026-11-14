# Meter Eye — Founder Start Pack

> A finished plug-in camera module that reads your analogue water, gas or heat meter on-device and pushes consumption to your app or local hub — the polished version of the popular DIY edge-AI meter reader.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Most water meters and many gas and heat meters in DE/AT/CH have no digital output. Households that became obsessive about consumption after the energy crisis read them by torchlight. The open-source "AI-on-the-edge" ESP32-CAM project reads dials beautifully — if you 3D-print a mount, tune regions of interest and accept a weekend of fiddling.
- **Customer:** German, Austrian and Swiss homeowners and small landlords with mechanical meters; Home Assistant users; heating-cost allocators and small property managers as B2B.
- **Product:** A complete kit: camera module with fixed-focus optics and an anti-glare LED ring, a universal strap mount for common meter diameters, zero-touch onboarding, on-device recognition, local MQTT/HA and an optional app. WiFi (USB-C) and PoE variants. €79–129 (estimate).
- **Why now:** The open firmware has a large community but no complete product with housing, lighting and mount; a Czech maker sells a bare PoE board. The gap between "board" and "box that works on my meter in 5 minutes" is the business.
- **The ask:** ~€80k to a certified first 1,000; but the first €700 and two weeks decide everything (licence + recognition test).

## 2. Business plan

### Problem & customer

The DIY path works for engineers: ESP32-CAM, printed adapter from Printables (there are adapters per meter model, e.g. for a Sensus 620), flash the firmware, set ROIs in a web UI, wait for the model to learn. Everyone else bounces at the mount or the ROI step. The product is the mechanical universality and the "it just read my meter" first minute.

- **Who pays (B2C):** the HA/Smart-home household in DACH (several hundred thousand active HA installs in DE alone, estimate), owners of single-family homes with a water meter in the cellar, people with sub-meters for gardens or tenants.
- **Who pays (B2B):** small landlords and property managers who read 5–50 sub-meters a year; heating-cost allocators for legacy meters they cannot yet replace; craft breweries and small businesses with water sub-metering.
- **Who uses:** the same person; installation takes place once, in a cellar.

### Market size (estimates — check)

- **TAM:** ~45M water meters in DE+AT+CH plus ~20M gas meters, the large majority mechanical. Say 50M readable analogue meters → at €99 **€5B** theoretical.
- **SAM (smart-home-active households and small landlords that would spend €99 on a sub-meter reader):** ~1.5–2.5M → **€150–250M**.
- **SOM (3 yrs):** 1% → **15–25k units**. Year 1: 2,000–4,000 (the existing community is a ready-made launch audience).

### Competition (1 search + round-1 notes)

| Alternative | What it is | Why we still win |
|---|---|---|
| DIY AI-on-the-edge (ESP32-CAM + printed adapter) | €15 of parts, free firmware, big community | Weekend of fiddling; adapter per meter model; no lighting control; licence now restricts commercial use (see risks) |
| Bare commercial boards (e.g. the ESP32-S3 PoE AI-on-the-edge cam sold via Tindie/Elecrow) | ~€40–60 board | No housing, no mount, no onboarding — our complement, or our competitor if they add a box |
| Pulse/reed add-ons for meters (water meter pulse sensors, gas meter magnet sensors, inductive readers for Ferraris) | €20–60 | Work only for specific meters with a magnet/pulse disc; no absolute reading |
| Utility smart-meter rollout | Free-ish eventually | Years away for water in most of DACH; sub-meters never |
| Do nothing (read monthly by hand) | Free | The majority — our ad is "never go to the cellar again" |

**Wedge:** universal mount + controlled lighting + zero-touch recognition. Second wedge: PoE for cellars without WiFi.

### Product & value proposition

- Puck-shaped camera module, fixed focal distance set by the mount (~60–80 mm), 6–8 LED ring with polariser/diffuser against glass glare, USB-C (5 V) or PoE SKU.
- Universal strap mount: elastic strap + three-point jaw for 60–110 mm meter bodies, plus flat-meter adapter for gas bellows meters.
- On-device recognition (digits + pointers) with a cloud-free default; local MQTT + Home Assistant discovery; optional app with graphs and leak alerts (continuous flow at night).
- **Pricing (estimates):** €89 WiFi, €129 PoE, €149 landlord 2-pack, B2B 10-pack €749.

### Unit economics (estimates, EUR per unit; WiFi SKU)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-S3 module 16 MB/8 MB PSRAM €4.5, OV2640/GC0308-class camera €3, LED ring + driver €1.2, USB-C + power €1, PCB €1) | 10.7 | 8.9 |
| PCBA + test (incl. camera focus check) | 3.0 | 2.0 |
| Enclosure (ABS puck, lens window, diffuser ring, strap mount parts) | 5.0 | 3.4 |
| Packaging + strap + adapters + USB cable | 3.0 | 2.3 |
| Freight + duty to EU | 2.0 | 1.0 |
| Certification amortised (€16k) | 16.0 | 3.2 |
| **Landed cost** | **39.7** | **20.8** |
| Net price D2C (€89 incl. 19% VAT → €74.8) less €8 fulfilment | 66.8 | 66.8 |
| **Gross margin D2C** | **€27 (41%)** | **€46 (69%)** |
| Via retail/Amazon (fees ~25%: €56 net) | €16 (29%) | €35 (63%) |

Licence cost of the recognition firmware (if negotiated) is not in this table — it could be a per-unit royalty; see risks.

### Go-to-market

**First 100 customers:** the project's own community (forum/GitHub discussions — only after you have settled the licence relationship), Home Assistant DE community, Photovoltaikforum, Haustechnikdialog, r/homeassistant, akkudoktor forum. Launch video: a meter in a dark cellar, 5 minutes to first reading.

**Then scale:** Amazon.de (strong category: "Wasserzähler auslesen"), smart-home retailers, electricians/installers (PoE SKU), property-management software marketplaces, heating-cost allocators (B2B pilot), Switzerland via Galaxus/Digitec-type retailers.

### 12-month plan

- **Q1:** licence conversation with the firmware maintainers (or decision to build your own recognition); 10-meter recognition test; mount prototypes.
- **Q2:** own PCB derived from the open ESP32-S3 camera board (strip LCD/audio), lens/LED ring, mount tooling design, 50-unit EVT in community homes.
- **Q3:** certification, 1,000 production; app v1; PoE SKU EVT.
- **Q4:** Amazon launch, landlord pack, allocator pilot.

**Team:** embedded/vision engineer (full), mechanical designer (half — the mount is the product), app/backend developer (half), founder on community and sales. Shenzhen partner for camera module sourcing, optics and the puck.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €24k + tooling (puck, ring, mount jaws) €14k + certification €16k + meters/test rig €1k + 6 months team €50k + marketing €5k = **≈€110k**; community pre-orders of 600 × €89 (€45k ex VAT) bring the external need to **≈€60–70k**. Route: pre-orders + bootstrap; angel is reasonable here because the community makes demand visible early.

### Top risks

| Risk | Mitigation |
|---|---|
| **Legal:** the open firmware's licence — evidence suggests it moved away from plain MIT and that commercial use needs a separate agreement with the authors | Read the LICENSE file and the project's statement first; either negotiate a written commercial licence/royalty or build your own recognition on your own trained model (TFLite Micro). Do not ship without this settled. |
| **Technical:** recognition accuracy across meter brands → returns | The 10-meter test; ship only meter families you have verified; publish a compatibility list |
| **Technical:** glare, condensation, dark cellars | Polarised LED ring, lens heater not needed but anti-fog film; test in a cold damp cellar |
| **Market:** utility smart-meter rollout | Slow for water; sub-meters remain; position for landlords |
| **Regulatory:** camera → GDPR questions | It looks at a dial; images never leave the device by default; say so in the manual and DPIA note |
| **Supply:** camera module variants change silently | Lock sensor part and lens; incoming optical test |

## 3. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| OSHWHub 立创·实战派 ESP32-S3 dev board | https://www.gongbans.com/db/oshwhub-li-chuang-shi-zhan-pai-esp32-s3-kai-fa-ban.html | Open ESP32-S3 (16 MB flash, 8 MB PSRAM) with GC0308 camera, per catalogue — keep camera path and power, drop LCD/audio/USB-hub | schematic, pcb (EasyEDA) | OSHWHub project licence — check on the project page before deriving |
| M5Stack TimerCamera-X (U082-X) | https://www.gongbans.com/db/m5stack-timercamera-x.html | Battery camera module for the prototype run (mount and lighting tests) | enclosure/structure only | Finished module for prototypes |
| M5Stack Unit PoESP32 (U138) | https://www.gongbans.com/db/m5stack-unit-poesp32.html | PoE reference for the cellar variant | enclosure/structure only | Module; production PoE needs its own PSE/PD design |
| M5Stack Unit FlashLight (U152) | https://www.gongbans.com/db/m5stack-unit-flashlight.html | Ring-light reference for even dial illumination | enclosure/structure only | Module for prototypes |

Catalogue honesty: the GC0308 camera in the open board is a modest sensor; verify resolution/lens suit the dial. The chip rows for M5 units are empty.

### Block diagram

```
USB-C 5V (or PoE PD module) ──► 3.3V ──► ESP32-S3 (16 MB flash, 8 MB PSRAM)
     ESP32-S3 ──DVP──► camera (fixed-focus lens at ~70 mm) ──► on-device digit/pointer recognition
     ESP32-S3 ──GPIO──► LED ring (6–8 LEDs, polarised/diffused) on during capture only
     ESP32-S3 ──WiFi──► MQTT/Home Assistant (local) ; optional cloud app via your proxy
Mount: strap + 3-point jaw holds the puck concentric with the dial at fixed distance
```

**Engineering gap:** optics and mount tolerances (the DIY version fails here), lighting against glass glare, and a recognition pipeline you are legally allowed to ship.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-S3-WROOM-1 N16R8 | €4.5 | Pre-certified; PSRAM essential for images |
| Camera module OV2640/OV5640 or GC0308-class with M12 fixed lens | €3–5 | **Lock sensor + lens**; vendors swap silently |
| 6–8 white LEDs + driver + polariser film | €1.2 | |
| USB-C + ESD + 3.3 V regulator | €1 | |
| PoE SKU: 802.3af PD module | +€6–8 | Few sources; pre-certified PD modules exist |
| PCB 4-layer (camera DVP routing) | €1.5 | |
| ABS puck + clear window + diffuser ring | €3 | Tooling €8–10k |
| Strap + jaw mount (3 adapters) | €2 | Tooling €4k |

### Firmware/software starting point

- **AI-on-the-edge-device** (jomjol, GitHub) — the reference; **licence: verify before any commercial use; evidence points to a separate agreement being required**.
- Clean-room option: **esp32-camera** (Espressif) for capture + **esp-tflite-micro** (TensorFlow Lite Micro for ESP32) with your own digit/pointer models trained on your meter photos; **ESP-IDF**.
- Local integration: MQTT + **Home Assistant** MQTT discovery; **ESPHome** has a camera component for quick pilots (not for recognition).
- App/backend: small; most buyers want HA/MQTT first.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — buy 10 used meters; 2× open ESP32-S3 boards / TimerCamera-X; printed mount + LED ring; run the open firmware; **read the licence and write to the maintainers** | ≥8/10 meters read correctly with zero manual ROI tuning; licence path clear (agreement or own model decision) |
| 3–5 | **Works-like** — 10 kits in community homes (DE/AT/CH), MQTT/HA, remote logs | ≥90% correct readings over 2 weeks; <10 min install median |
| 6–8 | **Looks-like + EVT** — own PCB rev A (camera path from the open board), puck + ring + mount printed, 30 units | Optical focus repeatable ±3 mm across the mount range; glare test passed on 5 glass covers |
| 9–10 | **DVT + pre-compliance** — rev B, EMC pre-scan, EN 18031 checklist, GDPR note, PoE PD trial | No fails; checklist complete; thermal OK in a closed puck at 30 °C |
| 11–12 | **Pilot batch** — 50 units with packaging to pre-order customers; compatibility list v1 | ≤3 returns; compatibility list ≥20 meter models; NPS ≥40 |

### Certification checklist (EU)

- **CE — RED:** EN 300 328 via module; **EN 301 489-1/-17**; **EN 62368-1** (USB) — PoE SKU adds safety scrutiny of the PD stage: €7–11k.
- **EN 18031-1/-2** (connected, consumption data = personal data at household level): self-assess, secure by default (no open camera stream without auth): €2–4k.
- **CRA:** SBOM, signed OTA, disclosure contact.
- **RoHS, WEEE (consumer), REACH, packaging.**
- **GDPR:** images stay on device by default; consumption data in the app under your DPA; DPIA note in the manual.
- No battery in the USB/PoE SKUs (TimerCamera prototypes have one — not for sale).
- **Total estimate:** €13–18k (both SKUs €18–24k).

### Validation toolkit

- **Kill question:** Buy 10 different used meters, build one mount, run the open firmware for a week. Pass = ≥8/10 read correctly with zero manual tuning. Cost ≈€700 incl. boards.
- **Interview script (5):** 1) Which meters do you have, where, and how often do you read them? 2) What have you tried to automate it (pulse sensor, ESP32-CAM, app)? Where did it stop? 3) Is there WiFi at the meter? Power? 4) What would you do with daily readings — leak alerts, tenant billing, curiosity? 5) €89 WiFi / €129 PoE — buy, wait, or "only with a Home Assistant integration"?
- **Landing page:** Headline: "Read your water meter without going to the cellar." Bullets: "Straps onto most meters in 5 minutes — no printing, no tuning." / "Reads the dial on the device; images never leave your home." / "Works with Home Assistant, MQTT and our app."
- **Pre-order pass:** ≥150 waitlist sign-ups and ≥60 paid pre-orders at €79 within 30 days of publishing the real accuracy number.

### First production checklist

- Samples: 3 camera modules from two vendors imaged on the same dial; 5 PCBAs; **golden sample** with reference photos of focus and lighting.
- DFM: lens window clarity and sealing, LED diffuser, strap anchor strength, jaw tolerance.
- MOQ: PCBA 500; camera modules 1k; puck 1k shots (negotiate 500); straps 1k.
- QC/AQL: Z1.4 II, AQL 1.0/2.5; 100% test: capture a test target at fixed distance and verify sharpness score; WiFi join; LED ring.
- Packaging: adapters and strap in a tray; EU DoC + WEEE; QR to compatibility list.
- Incoterms: FOB Shenzhen sea; first 50 by air DAP.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack TimerCamera‑X (U082‑X)](/db/m5stack-timercamera-x.html) (battery camera module for the prototype run); [M5Stack Unit PoESP32 (U138)](/db/m5stack-unit-poesp32.html) (PoE variant for basements without WiFi); [M5Stack Unit FlashLight (U152)](/db/m5stack-unit-flashlight.html) (ring-light reference for even dial illumination). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [立创·实战派ESP32-S3开发板](/db/oshwhub-li-chuang-shi-zhan-pai-esp32-s3-kai-fa-ban.html) (open ESP32-S3 board with camera — keep camera path and power, drop LCD/audio).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Forlinx Embedded** (飞凌嵌入式技术有限公司) · forlinx.com — ARM core board / SOM OEM: i.MX8M / RK3568 / AM62x SOM; carrier board; Linux BSP; OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **Toradex (SZ)** (深圳图睿达科技有限公司) · toradex.com — Industrial SOM / embedded Linux OEM: Apalis / Colibri SOM; carrier board; Yocto Linux; long-term supply. *(Edge-AI / SOM boards and Linux BSPs)*
- **iWave Systems (SZ)** (爱微电子(深圳)有限公司) · no website on file — ARM SOM / carrier board ODM: RK3568/i.MX8 SOM; carrier board; embedded Linux OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **Kangshida (Conradtech)** (深圳市康士达科技有限公司) · cstipc.com — Industrial PC / AI edge computing OEM: Industrial PC board; AI edge card; computer vision; OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack TimerCamera‑X (U082‑X), M5Stack Unit PoESP32 (U138), M5Stack Unit FlashLight (U152) — for a Meter Eye

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Meter Eye: A finished plug-in camera module that reads your analogue water, gas or heat meter on-device and pushes consumption to your app or local hub — the polished version of the popular DIY edge-AI meter reader. The design is built around your M5Stack TimerCamera‑X (U082‑X), M5Stack Unit PoESP32 (U138), M5Stack Unit FlashLight (U152).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack TimerCamera‑X (U082‑X), M5Stack Unit PoESP32 (U138), M5Stack Unit FlashLight (U152).
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
主题：样品订购及批量报价 — M5Stack TimerCamera‑X (U082‑X), M5Stack Unit PoESP32 (U138), M5Stack Unit FlashLight (U152) — 用于Meter Eye

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Meter Eye：A finished plug-in camera module that reads your analogue water, gas or heat meter on-device and pushes consumption to your app or local hub — the polished version of the popular DIY edge-AI meter reader。产品设计基于贵司的M5Stack TimerCamera‑X (U082‑X), M5Stack Unit PoESP32 (U138), M5Stack Unit FlashLight (U152)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack TimerCamera‑X (U082‑X), M5Stack Unit PoESP32 (U138), M5Stack Unit FlashLight (U152)。
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
Subject: PCBA quote from open design files — Meter Eye, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Meter Eye: A finished plug-in camera module that reads your analogue water, gas or heat meter on-device and pushes consumption to your app or local hub — the polished version of the popular DIY edge-AI meter reader. The design starts from published open-hardware files (立创·实战派ESP32-S3开发板; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Meter Eye，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Meter Eye：A finished plug-in camera module that reads your analogue water, gas or heat meter on-device and pushes consumption to your app or local hub — the polished version of the popular DIY edge-AI meter reader。设计基于已公开的开源硬件文件（立创·实战派ESP32-S3开发板；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Open the LICENSE file and the project README of the open firmware, write down the exact commercial terms you find, and prepare the question you would ask the maintainers (do not send it from this job — the founder sends it).
2. Buy 10 used meters (water, gas, heat; different brands) and 2 open ESP32-S3 camera boards or TimerCamera-X; print a strap mount; start the 10-meter test.
3. Draft the compatibility-list template and the GDPR one-liner for the manual.

Want help sourcing or building this? Talk to us via www.gongbans.com.
