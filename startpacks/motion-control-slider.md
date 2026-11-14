# Motion-Control Slider — Founder Start Pack

> A silent, repeatable camera slider and pan-tilt head controlled by a motorised knob, for product videos, stop-motion and small studios — keyframes you can feel, not an app you fight.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Every webshop now needs product video; the cheap motorised sliders are app-driven, jerky and un-repeatable, and the good ones (Edelkrone, Zeapon with pan/tilt) cost €600–1,000+ before the head. Setting a two-axis move on a phone takes longer than the shot.
- **Customer:** Small online shops and their in-house "content person", freelance product photographers, stop-motion animators, school media labs — DE/NL/FR/UK. Buyer and user are the same person; the budget is "under €600 or I keep using my hands".
- **Product:** A 1 m carbon-rod slider + pan/tilt head driven by smart serial servos, controlled by a knob-with-screen: turn to move, press to set a keyframe, turn again for the next, press-and-hold to play. Time-lapse, stop-motion and shutter-trigger modes. Battery (NP-F style). €449–599 (estimates).
- **Why now:** Integrated smart servo motors with RS485/CAN and encoders now cost €25–40 and a knob-with-round-screen controller exists off the shelf — the parts that cost €300 of engineering five years ago are catalogue items.
- **The ask:** ~€120k to the first 1,000 units; pre-orders from a demo video are the gate, then a crowdfunding wave and two photo-retail distributors.

## 2. Business plan

### Problem & customer

A product video for a shop listing is a 3–8 second slide with a slight pan, shot 30 times a day. The person shooting is not a camera operator. They want: put the camera on, turn a knob to where the move starts, click, turn to where it ends, click, press play, done; and the same move again for the next 29 products. Apps with Bezier curves and Bluetooth drop-outs are the opposite of that.

- **Who pays / uses:** the shop owner or their content person; the freelance photographer who sells "video add-on" to shops; the animator who needs repeatability to the step; the media teacher who needs a tool that survives students.
- **What they compare you to:** a Zeapon or GVM slider with a separate motorised head (and two apps), or Edelkrone's premium modular system, or a tripod and their hands.

### Market size (estimates — check)

- **TAM:** EU online shops ≈ 1.1M (sources vary); those with physical products and >€250k revenue ≈ 300k; plus ~50k professional/semi-pro photographers and content creators buying motion gear; plus ~20k school/university media labs. At €500: **€185M** theoretical.
- **SAM:** shops and creators who already own a mirrorless camera and a tripod and shoot in-house ≈ 25% → **€45M**.
- **SOM (3 years):** 8–12k units → **€4–6M**. Year 1: 1,000–1,500 via crowdfunding + direct.

Sources used: Zeapon Micro 2 Plus with PONS pan/tilt kit ~$1,010 and pan-only ~$649 (US retailer), Zeapon Micro 3/4 M700 at €536–620 in the EU (aio.lv). Shop counts: Eurostat/ecommerce association estimates — verify.

### Competition (1 search)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing — tripod, hands, turntable | €0–60 | Shaky, not repeatable, no pan during slide |
| Manual slider (Neewer, SmallRig) | €80–200 | No motor; fine for one take, useless for 30 identical ones |
| Motorised slider + app (GVM, Neewer, Zeapon Micro 3/4 M700 €536–620) | €250–620 | App-only control, head sold separately (Zeapon PONS kit pushes it to ~€900+), limited repeatability |
| Edelkrone SliderPLUS + HeadPLUS | €1,200–2,500 | Beautiful, premium, Bluetooth app; out of the shop budget |
| Robotic arms / Motorized Precision / cinema mo-co | €5k+ | Different league |
| DIY: stepper slider + Arduino (many open designs) | €150 + weekends | Works for the maker; nobody else wants to build it |

**Wedge:** two synchronised axes (slide + pan, tilt optional) programmed by hand on a knob in 20 seconds, repeatable to the step, silent, at the price of a slider-with-app alone.

### Product & value proposition

- Rail: 1,000 mm (also 600 mm) twin 15 mm carbon rods on aluminium end blocks, belt-driven carriage, 5 kg payload horizontal, 2.5 kg at 45° with a counterweight hook.
- Motors: three integrated smart servos (RS485 bus, encoder, 12 V) — slide, pan, tilt. One cable from the controller to the rail, daisy-chained.
- Controller: knob with round screen on the end block (removable, 1.5 m cable): turn = jog selected axis, press = keyframe, long press = play; modes: video move (ease in/out), time-lapse (shoot-move-shoot), stop-motion (frame step), loop for 30 products.
- Shutter trigger: 2.5 mm jack with camera cables (Sony/Canon/Nikon), plus BLE remote for phones.
- Battery: NP-F slot (user-supplied or bundled), 12 V boost; USB-C PD in.
- **Pricing (estimates):** slider + pan head + knob €449; with tilt arm €549; 600 mm "desk" version €349. B2B/education 10+ at €380. Accessories: rail extensions, second head.

### Unit economics (estimates, EUR per unit; 1 m slide + pan + knob)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (2 smart servos €30 each €60, knob controller — ESP32-S3 + 1.28" round LCD + encoder €12, battery boost + PD + bus PCB €6, cables/connectors €5) | 83 | 68 |
| Mechanics (2× 1 m carbon rods €14, CNC end blocks + carriage €22, belt + pulleys + bearings €7, head yoke + 1/4"/3/8" plates €9) | 52 | 40 |
| Assembly + test (belt tension, repeatability test on a jig) | 7.0 | 5.0 |
| Enclosure (controller housing, motor covers — 3 small tools ~€15k) | 6.0 | 3.0 |
| Packaging (long box, foam) | 6.0 | 4.5 |
| Freight + duty to EU (1.1 m parcel — volumetric; sea at 5k) | 12 | 6.5 |
| Certification amortised (€35k: RED/BLE + EN 18031 + EMC with motors + safety + battery) | 35.0 | 7.0 |
| **Landed cost** | **201** | **134** |
| D2C net price (€449 incl. 19% VAT → €377) less €20 fulfilment (long parcel) | 357 | 357 |
| **Gross margin D2C** | **€156 (44%)** | **€223 (62%)** |
| Photo-retail distributor net €270 ex VAT | €69 (26%) | €136 (50%) |

The 1.1 m parcel is a real cost: design the rail to ship in two 55 cm halves with a joiner, and the margin picture improves by €8–10 everywhere.

### Go-to-market

**First 100 customers:** a 60-second demo video — knob, two keyframes, 30 identical product shots in a row — on YouTube and in the e-commerce communities (Shopify/WooCommerce Facebook groups in DE/NL, r/ecommerce, the German "Onlinehändler" forums), plus the stop-motion communities (Stop Motion Animation forums, Dragonframe users) and photography subreddits. Pre-order at €399 early-bird, €50 deposit; 30 pre-orders is the gate.

**Scale:** a crowdfunding campaign (this category does well), photo-retail e-tailers in DE/NL/UK, education distributors for media labs, and B2B outreach to product-photo studios and e-commerce agencies that shoot for many shops. Content partnerships with product-photography YouTubers (loan units, honest reviews).

### 12-month plan

- **Q1:** demo video + pre-orders (kill question), works-like rig from Roller485 units + M5Stack Dial + a bought manual slider, keyframe UX tested with 5 shop owners.
- **Q2:** own carriage/end-block design, bus PCB, controller firmware v1, 20 EVT units to creators and two studios; repeatability and noise measured; pre-compliance.
- **Q3:** DVT, certification (RED/BLE, EMC, safety, battery), crowdfunding campaign, pilot batch 50, two-piece rail decision.
- **Q4:** production 1,000, distributor onboarding, tilt arm and 600 mm SKU, shutter-cable set.

**Team:** founder (product + content marketing — you must be able to shoot the demo yourself), 1 firmware engineer (ESP-IDF, RS485 servo control, motion profiles), 1 mechanical engineer (rail, carriage, head — the product is 60% mechanics), part-time industrial designer, a crowdfunding/marketing freelancer for the campaign.

**Funding to 1,000 units (estimate):** NRE €35k (mechanical design + CNC prototypes €18k, tooling €15k, PCB €2k) + certification €35k + 9 months lean salaries €65k + 1,000 units at €145 landed €145k = **€280k**, less 600 crowdfunded/pre-ordered units at €399 (€240k, part of which is the units themselves) → **€120k** of pre-campaign money needed for NRE, certification and the first salaries. Route: 30 deposits (signal), a founder/angel cheque for NRE + certification, then the campaign funds the production run. Do not order 1,000 units before the campaign closes.

### Top risks

- **Technical — vibration and noise at slow speeds.** Belt resonance and servo micro-stepping show up in 4K. Mitigation: encoder-based smart servos with smooth velocity profiles, belt tension spec, rubber-mounted motor; test on video at week 4, not week 10.
- **Technical — rail flex at 1 m with 5 kg.** Carbon rods help; end blocks and the carriage are the stiffness problem. Mitigation: FEA-lite plus a payload test; publish honest payload numbers.
- **Market — "nice, but I use my phone" and seasonality (Q4 shops don't buy tools).** Mitigation: launch the campaign in spring; sell the 30-products-in-a-row story, not specs.
- **Regulatory — Li-ion.** NP-F packs are user-supplied → the Battery Regulation falls on the battery brand, but UN 38.3/shipping applies if you bundle. Mitigation: ship without battery at first; sell a certified pack as an accessory.
- **Supply — smart servos from one vendor.** Mitigation: the RS485 protocol layer abstracts the motor; qualify a second servo with the same mount; buy 3k motors with the campaign money.
- **IP — Edelkrone and others hold design patents on specific mechanisms.** Mitigation: a patent search on belt-driven slider + knob control before tooling (€2–3k).

## 3. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit Roller485 (U182) | https://www.gongbans.com/db/m5stack-unit-roller485.html | Integrated servo motor with RS485 control — slide and pan axes in the prototype | enclosure/structure files only; electronics not published | Off-the-shelf; use as bought; evaluate as a production motor or source an equivalent |
| M5Stack Unit RollerCAN (U188) | https://www.gongbans.com/db/m5stack-unit-rollercan.html | CAN variant of the same motor — if you prefer CAN for a longer bus | enclosure/structure files only | Off-the-shelf |
| M5Stack Unit Step16 (U198) | https://www.gongbans.com/db/m5stack-unit-step16.html | 16-step rotary input reference for a detented frame-step control (stop-motion) | enclosure/structure files only | Off-the-shelf |
| M5Stack Dial (K130) | https://www.gongbans.com/db/m5stack-dial.html | Knob + round screen controller — your UX prototype on day one | enclosure/structure files only | Off-the-shelf |

No electronics are published for any of these: the prototype is bought modules; production needs your own controller PCB and a motor sourcing decision.

### Block diagram

```
[Knob + round LCD controller (ESP32-S3)] --RS485 bus (1 cable)--> [slide servo] --> [pan servo] --> [tilt servo (opt)]
        |-- BLE (phone remote, firmware) 
        |-- 2.5 mm shutter trigger --> camera
        |-- USB-C PD in / NP-F battery --> 12 V boost --> servos, 5 V --> logic
Carriage on 2x 15 mm carbon rods, belt drive from the slide servo at the end block.
Modes: video keyframes (ease), time-lapse (shoot-move-shoot), stop-motion (frame step), loop.
```

**Engineering gap:** the mechanical design (carriage, end blocks, belt tensioner, head yoke) — this is the product; the keyframe UX on a single knob; synchronised multi-axis motion profiles with easing on cheap servos; shutter-trigger timing for shoot-move-shoot; a controller PCB with PD and battery management.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| Smart serial servo, 12 V, encoder, RS485 (Roller485-class) ×2–3 | €25–35 each | Single-vendor risk; qualify a second (several Shenzhen vendors make RS485 bus servos) |
| ESP32-S3 module | €3 | Multi-source |
| 1.28" round IPS LCD + rotary encoder with push | €8 | Multi-source |
| USB-C PD sink + 12 V boost + NP-F slot | €6 | |
| 15 mm carbon tubes 1 m ×2 | €14 | Multi-source (fishing-rod/drone suppliers) |
| CNC aluminium end blocks ×2 + carriage | €22 at 1k | Move to die-cast at 5k+ (tooling €20k) |
| GT2 belt, pulleys, bearings, tensioner | €7 | Commodity |
| Head yoke + Arca-compatible plate | €9 | |
| Controller housing + motor covers | €3 at 5k | Tooling €15k; or CNC/printed at 1k |

### Firmware/software starting point

- ESP-IDF; M5Stack's UnitRoller library/driver for the Roller485 protocol (check their GitHub for the current repo) to get the servos moving in a day.
- LVGL for the round-screen UI.
- Motion profiles: write your own S-curve/ease generator (small); for inspiration, the open-source "OpenMoCo"/DIY slider firmware family exists — search before reusing.
- Shutter trigger timing: a GPIO + optocoupler; camera cable pinouts are well documented online.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | 60-second demo video (Roller485 on a bought manual slider, Dial as controller) → 30 pre-orders at €399 with €50 deposits in 3 weeks; and a credible plan to ship within 8 weeks of the campaign. Under 15: stop. |
| 3–5 | Works-like | Two synchronised axes, keyframe UX usable by a shop owner without instruction in <2 min, repeatability ±0.5 mm over 1 m, noise <35 dBA at 50 cm at video speeds; 4K test footage shows no visible stutter. |
| 6–8 | Looks-like + EVT | Own carriage/end blocks (CNC), bus PCB, controller housing (SLA), 20 units with creators for 3 weeks; payload test 5 kg; EMC pre-scan with motors running. |
| 9–10 | DVT + pre-compliance | Two-piece rail decision, PCB v2, RED/EMC pre-test, safety review (pinch points, EN 62368-1), battery handling decision; patent search done. |
| 11–12 | Pilot batch | 50 units from a CM + a mechanical assembler, golden sample with repeatability certificate, crowdfunding page with certified-design date. |

### Certification checklist (EU)

- **CE / RED:** BLE → EN 300 328, EN 301 489-1/-17, EN 62311; EN 62368-1 safety (12 V, motors — pinch-point warnings, stall protection). EMC with three servos running is the hard part.
- **RED delegated act — EN 18031-1:** applies (BLE, internet-connected via phone app for firmware). Keep the connected surface small: BLE for remote and OTA only.
- **CRA:** reporting since September 2026, full December 2027; signed firmware, SBOM, disclosure policy.
- **RoHS, REACH, WEEE**, packaging registration.
- **Battery Regulation (2023/1542) + UN 38.3:** only if you bundle a Li-ion pack — then labelling, removability, carbon-footprint declarations on the horizon, and DG shipping paperwork. Start without a bundled battery.
- **Machinery Regulation:** a desktop motorised camera slider is generally treated as a consumer electrical appliance, not machinery — confirm with the test lab (there is an argument either way for moving parts).
- **GDPR:** none on device.
- **Estimated test costs:** RED/BLE €8–10k (module pre-cert helps), EMC with motors €6k, safety €4k, EN 18031 €12–15k, documentation €2k. Budget **€35k**.

### Validation toolkit

- **Kill question:** do 30 creators or shops pre-order at €399–499 from a 60-second demo, and can you ship within 8 weeks of the campaign closing? **Cheapest experiment:** two Roller485 units, a Dial, a €120 manual slider and a weekend of firmware; film 30 products in a row. Cost ≈ €250.
- **5-question interview (shop content person):** 1) How many product videos did you shoot last month and how long did each take? 2) Show me the last one — what bothered you about the move? 3) Have you bought a slider or gimbal before; is it still in use? 4) Would you rather set a move on a phone or by turning a knob — why? 5) At €449 with a pan head included, what else would need to be true for you to buy this quarter?
- **Landing page:** headline "Set a camera move by hand. Repeat it 30 times. Silent." Bullets: "Turn the knob, click two keyframes, press play — no app"; "Slide + pan synchronised, 5 kg payload, 1 m carbon rail"; "Time-lapse and stop-motion modes with camera trigger".
- **Pass threshold:** 30 deposits in 3 weeks; then 500 units in the campaign's first two weeks.

### First production checklist

- Samples: 3 works-like, 20 EVT, 50 pilot; keep two with repeatability logs.
- Golden sample: repeatability test (±0.5 mm), noise and payload numbers, UX walk-through video.
- DFM review: end-block machining tolerances vs rod fit, belt tension procedure, cable strain relief at the moving carriage, two-piece rail joiner stiffness.
- MOQ talk: servos 1k (negotiate protocol documentation and a second-source clause), CNC 500, tooling at 1k.
- QC/AQL: level II, AQL 1.0/2.5; 100% motion test on a jig; 10% noise and payload sample.
- Packaging: long box or two-half design; drop test for the carriage; foam that holds the head.
- Incoterms: FOB Shenzhen; no battery bundled → no DG.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Roller485 (U182)](/db/m5stack-unit-roller485.html) (integrated servo motor with RS485 control); [M5Stack Unit RollerCAN (U188)](/db/m5stack-unit-rollercan.html) (CAN variant of the smart motor); [M5Stack Unit Step16 (U198)](/db/m5stack-unit-step16.html) (16-step rotary input reference); [M5Stack Dial (K130)](/db/m5stack-dial.html) (knob + round screen controller). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130) — for a Motion-Control Slider

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Motion-Control Slider: A silent, repeatable camera slider and pan-tilt head controlled by a motorised knob, for product videos, stop-motion and small studios — keyframes you can feel, not an app you fight. The design is built around your M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130).
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
主题：样品订购及批量报价 — M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130) — 用于Motion-Control Slider

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Motion-Control Slider：A silent, repeatable camera slider and pan-tilt head controlled by a motorised knob, for product videos, stop-motion and small studios — keyframes you can feel, not an app you fight。产品设计基于贵司的M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130)。
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
Subject: PCBA quote from open design files — Motion-Control Slider, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Motion-Control Slider: A silent, repeatable camera slider and pan-tilt head controlled by a motorised knob, for product videos, stop-motion and small studios — keyframes you can feel, not an app you fight. The design starts from published open-hardware files (M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Motion-Control Slider，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Motion-Control Slider：A silent, repeatable camera slider and pan-tilt head controlled by a motorised knob, for product videos, stop-motion and small studios — keyframes you can feel, not an app you fight。设计基于已公开的开源硬件文件（M5Stack Unit Roller485 (U182), M5Stack Unit RollerCAN (U188), M5Stack Unit Step16 (U198), M5Stack Dial (K130)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order two Roller485 units, a Dial, a Step16 and a cheap manual slider; get the knob jogging the slide axis by the weekend.
2. Write the 60-second demo script ("30 products, one knob") and shoot it with the prototype as soon as two axes move.
3. Interview five shop owners with the five questions; ask each to show you their last product video.

Want help sourcing or building this? Talk to us via www.gongbans.com.
