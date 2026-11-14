# Farm-Shop Self-Checkout — Founder Start Pack

> A rugged QR/barcode self-checkout terminal for unstaffed farm shops and honesty fridges: scan the product, show a payment QR, print or display the receipt — no lock, no cash drawer, no monthly POS licence.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Unstaffed farm shops run on an honesty box (theft, no records, no card) or on a €10,000+ vending machine ([2021 market overview via agrarheute](https://api.swissmilk.ch/wp-content/uploads/2019/05/direktvermarktung-milch-automatisch-verkaufen-artikel-agrarheute-1-2021-de.pdf)). App-based self-service systems charge €119/month plus 2% of revenue ([top agrar](https://www.topagrar.com/betriebsleitung/news/wie-hilft-ki-hofladen-bei-kassen-waagen-und-preisoptimierung-20027756.html)).
- **Customer:** Farm shops, honesty stores and village micro-markets in DE/AT/CH/NL and the Nordics; agricultural cooperatives and chambers as channel. The farmer pays; the customer at 6 a.m. uses it.
- **Product:** A €599 wall/counter terminal with a barcode/QR scanner, a 7" touch screen, PoE or WiFi, a member-card reader, a dynamic payment QR per basket (SEPA GiroCode, TWINT, iDEAL or the farmer's payment provider), optional receipt printer, daily summary to the farmer's phone, and a product list that survives a dead connection.
- **Why now:** Unstaffed direct marketing is growing in the German-speaking countries; a proposal would make digital payment mandatory for farm shops and cafés from 2027 ([top agrar](https://www.topagrar.com/betriebsleitung/news/hofladen-und-hofcafe-ab-2027-soll-digitale-zahlung-pflicht-werden-20029097.html)); payment QR standards and cheap scanners make a terminal without PCI scope feasible.
- **The ask:** ~€110k (estimate) to the first 1,000 units; route = paid regional pilots + bootstrap; chambers of agriculture and cooperative buying groups as the scaling lever.

## 2. Business plan

### Problem & customer
The farmer with a self-service shop has three pains: shrinkage (people take and don't pay), no sales record (what sold, when, which product), and cash handling. Today's choices: an honesty box; a €10–20k vending/locker machine (good for eggs and milk, bad for a shop with 80 products); a tablet with a POS app at €50–120/month plus a revenue cut; or a cash-recycling self-checkout from supermarket suppliers at €5k+. None is "a €599 box on the wall that works at 5 a.m. in a shed with bad WiFi."

Who pays vs who uses: the farm family pays (one-off, no subscription); customers use it; the chamber of agriculture or cooperative recommends it. Secondary buyers: village micro-markets (container shops), campsite shops, allotment-association kiosks.

### Market size (estimates)
- Germany has tens of thousands of direct-marketing farms; the share with an unstaffed shop or vending point is growing but uncounted (searches found local examples, no national statistic). Estimate **30k unstaffed sales points in DE/AT/CH**, 10k in NL/BE/Nordics, 20k in FR/IT/others → **60k sites**.
- **TAM:** 60k × €599 ≈ **€36 M** hardware + receipt paper/accessories.
- **SAM:** sites with a shop (not a single milk machine), card-paying customers and a shed with power — 40% → 24k → **€14 M**.
- **SOM (3 years):** 8% → ~1,900 units → **€1.1 M**, plus printers and member cards.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Honesty box / "Vertrauenskasse" ("do nothing") | The majority | Theft, no records, cash only; a proposed digital-payment duty from 2027 |
| Vending and locker machines (≥ €10k) | Established, 24/7, secure | Price, limited SKUs, no fresh/loose goods, service contracts |
| Tablet + POS app with self-service mode (~€119/month + 2% revenue) | Modern, receipts, analytics | Subscription + revenue share; tablet in a shed; needs internet |
| Supermarket-grade self-checkout with cash recycler | Reliable | €5k+; built for supermarkets; too big |
| Card terminal on the counter + paper list (SumUp/Zettle-class, €39–99 one-off, [LfL 2020](https://lfl.bayern.de/mam/cms07/iba/dateien/lfl_bargeldlose_bezahlsysteme_2020.pdf)) | Cheap card acceptance | Customer must type the amount honestly; no product scan, no record per item |
| DIY (Raspberry Pi + scanner + a web page) | A few tech-minded farmers | No support, no CE, no fiscal compliance story |

**Wedge:** one-off price, no subscription or revenue cut, works offline, payment via a QR that the farmer's own provider settles (no money ever touches the device → no PCI scope), rugged for a shed, and a daily WhatsApp-style summary that makes the farmer feel in control.

### Product & value proposition
Hardware: 7" IPS touch terminal in a powder-coated steel/ABS housing with a scanner window, 2D barcode/QR scanner module, NFC reader for member cards (regulars get a tab and a monthly invoice), PoE (one cable into the shed) with WiFi fallback and an optional LTE stick, piezo and LED, optional 58 mm receipt printer, VESA/wall mount, IP54 front. Software: product list with pictures and PLU buttons for loose goods, scale input (bought-in certified scale over USB/RS-232 for weighed goods — MID-approved scale, not ours), basket → payment QR (static EPC/GiroCode with amount and reference, or a dynamic QR from the farmer's PSP), "I paid cash" button with photo-less logging, offline queue, daily summary and CSV, admin via phone browser.

Pricing (estimates): **€599 terminal**, **€749 with printer**, €99 LTE kit, member cards €1 each. Cooperatives/chambers at 25% off for bundles of 20. No subscription; optional €49/year hosted summary service for those who want it.

### Unit economics (estimates per unit, ex-VAT, terminal without printer)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32-S3 or small Linux SoM, 7" touch, 2D scanner module, NFC, PoE PHY + PD, PSU, PCB) | €78.00 | €62.00 |
| Assembly & test (SMT, scanner alignment, touch test, PoE test) | €9.00 | €6.50 |
| Enclosure (steel back + ABS front, scanner window, VESA; tooling amortised) | €16.00 | €10.50 |
| Packaging (box, mount, screws, quick sheet) | €4.00 | €3.00 |
| Freight + duty to EU | €6.00 | €3.50 |
| Certification amortised (~€35k: RED, EMC, safety, EN 18031) | €35.00 | €7.00 |
| **Landed cost** | **€148.00** | **€92.50** |
| Sell price (direct €599 / cooperative bundle €449) | €599 | €449 |
| **Gross margin** | **€451 (75%)** | **€356.50 (79% at bundle price)** |

The 2D scanner module is the BOM swing part (€18–35 depending on vendor); qualify two.

### Go-to-market
**First 100 customers:** 5 farm shops in one region for a 2-month paid pilot (kill question: less shrinkage than the honesty box); the regional chamber of agriculture's direct-marketing adviser (they run courses and newsletters — search "Direktvermarktung Beratung" per Bundesland/canton); direct-marketing associations and their trade fairs; farm-shop Facebook groups; a two-page case study with shrinkage numbers.

**Scale channels:** chambers of agriculture and cooperative buying groups (bundle of 20), farm-shop equipment dealers (they sell fridges and shelving — add a terminal), payment providers who want unattended rural merchants, container-shop makers (they need a checkout for every box they sell).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from Core2 + QR unit + PoE unit + RFID2 in a printed case; 5 pilots live; shrinkage data. |
| Q2 | Own board + 7" terminal, steel housing, PSP integrations (2 countries), offline queue; EVT 30; pre-compliance. |
| Q3 | DVT, certification, 200-unit pilot across 3 regions; printer SKU; member cards; chamber partnership. |
| Q4 | 1,000 units; 2 cooperatives; LTE kit; second-country fiscal rules implemented. |

**Team:** 1 embedded/Linux engineer (terminal, scanner, PoE, offline logic — full-time), 1 web/backend developer (admin page, PSP integrations, summaries — full-time), founder for sales and pilots; a tax/fiscal adviser per country on contract. Three people.

**Funding to first 1,000 units (estimates):** NRE €55k (board €12k, housing tooling €18k, software €25k) + certification €35k + fiscal/legal advice €12k + 1,000 units landed ~€113k + 9 months overhead €70k ≈ **€285k**; minus pilot fees (5 × €1,000) and pilot-batch sales (200 × €549 ≈ €110k) and cooperative prepayment (~€60k) ≈ **~€110k**. Bootstrap + paid pilots + a cooperative prepayment; rural-development or digitalisation grants (regional) often cover farmer-side purchase, which helps the channel more than you.

### Top risks
| Risk | Mitigation |
|---|---|
| **Regulatory:** fiscal rules — in DE a device that records sales may count as an electronic recording system needing a certified TSE; AT has RKSV; receipt duties vary | Country-by-country decision: either integrate a cloud TSE/fiscal service via API, or position the terminal as a payment-request display that logs for the farmer and let the farmer's existing register be the fiscal system. Get written advice before pilots |
| **Market:** farmers fear tech in a shed; "my customers are 70" | Big buttons, pictures, cash button stays; pilot data; chamber endorsement |
| **Technical:** connectivity in sheds | PoE first, WiFi second, LTE kit; offline queue with later settlement; static GiroCode QR works without any connection |
| **Payment:** QR acceptance differs per country (TWINT in CH, iDEAL in NL, GiroCode in DE/AT, Bizum in ES) | Country packs; the farmer's PSP does the settlement; device never handles card data (no PCI) |
| **Regulatory:** weighed goods need a MID-approved scale | Bought-in certified scale; terminal only displays the scale's legal value |
| **Supply:** 2D scanner modules and 7" panels from few vendors | Two scanner vendors on the same connector; a standard 7" MIPI/RGB panel with alternates |
| **Theft/vandalism of the terminal** | Steel housing, tamper alert, no cash inside — nothing to steal |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit QRCode (U173) | https://www.gongbans.com/db/m5stack-unit-qrcode.html | 2D barcode/QR scanner module for the works-like | enclosure/structure only; electronics not published | Buy; a scanner module vendor for production |
| M5Stack Core2 (K010) | https://www.gongbans.com/db/m5stack-core2.html | Touch-screen terminal for the prototype | enclosure/structure only; electronics not published | Buy; own board later |
| M5Stack Unit PoESP32 (U138) | https://www.gongbans.com/db/m5stack-unit-poesp32.html | PoE/Ethernet in a shed | enclosure/structure only; electronics not published | Buy; PoE PD design for your own board |
| M5Stack Unit RFID2 (U031-B) | https://www.gongbans.com/db/m5stack-unit-rfid2.html | Member-card reading | enclosure/structure only; electronics not published | Buy; NFC reader IC reference |

**Board-fact note:** none of the four publishes main-board electronics; they are prototyping blocks. The production terminal is your own board (or a Linux SoM + carrier).

### Block diagram
```
[2D scanner module (UART/USB)]  [NFC reader]  [7" touch panel]  [optional: 58 mm printer, certified scale (RS-232/USB)]
          \                        |              |                           /
           +----------- [ESP32-S3 (LVGL UI) or Linux SoM] ------------------+
                              |          |            |
                   [PoE PD + Ethernet] [WiFi] [LTE stick, optional]
                              |
                   [product list + offline basket queue (flash/SD)]
                              |
   [payment QR: EPC/GiroCode static, or PSP dynamic QR via API] --> customer's banking app
                              |
   [daily summary + CSV -> farmer's phone (browser/email)]   [cloud TSE / fiscal API per country, if required]
```
**Engineering gap:** UI that a 70-year-old uses at 6 a.m.; offline basket queue with later settlement; PSP/QR country packs; fiscal integration decision; a housing that survives a shed. The scanner and the screen are solved problems.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 module with PSRAM (or Linux SoM at +€20) | €3.50 | Pre-certified; LVGL UI runs fine on S3 |
| 7" IPS touch panel (1024×600) | €22.00 | Qualify two panels on one connector |
| 2D scanner module | €24.00 | **Few vendors; 2 qualified**; UART; window glass |
| NFC reader IC + antenna | €2.20 | |
| PoE PD controller + Ethernet PHY + magnetics | €6.50 | 802.3af; WiFi fallback |
| Power: 12 V in alt. + 5 V/3.3 V rails | €3.00 | PoE or certified 12 V adapter |
| PCB 4-layer, passives, USB host, SD | €6.00 | |
| Steel back + ABS front + scanner window + VESA | €16.00 | **Tooling €15–20k**; sheet metal has low tooling |
| 58 mm thermal printer (SKU option) | €14.00 | ESC/POS |

### Firmware/software starting point
- **LVGL** (exists) for the touch UI on ESP32-S3; **M5Unified** (M5Stack's library, exists) for the Core2 works-like.
- Payment QR: the **EPC QR code** (GiroCode) is a published EPC standard for SEPA credit-transfer QR; TWINT, iDEAL and Bizum dynamic QRs come from each provider's merchant API — search each PSP's developer docs.
- Receipt: ESC/POS printing (search "esc-pos ESP32").
- Backend: a tiny hosted service (or none — email the CSV) for the daily summary; keep personal data out of the device (member cards = ID numbers only).
- Fiscal: cloud TSE providers in DE expose APIs; search "Cloud-TSE API" and get the adviser's verdict before integrating.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Works-like (Core2 + QR unit + PoE unit + RFID2) in a printed case with a 20-product list and a GiroCode QR; **5 farm shops in one region agree to a 2-month paid pilot** (€200 each) and give you last quarter's honesty-box revenue as a baseline |
| 3–5 | Works-like | Pilots live; offline queue works; ≥ 95% of scans succeed first try on the farmer's own labels; farmer gets a daily summary |
| 6–8 | Looks-like + EVT | Own board + 7" terminal in the steel/ABS housing; 30 units; PSP dynamic QR for one country; EMC pre-scan; shed test (−10 °C to 45 °C, dust) |
| 9–10 | DVT + pre-compliance | RED/EMC/safety pre-compliance; EN 18031 self-assessment; fiscal decision documented per country with the adviser's note; printer SKU |
| 11–12 | Pilot batch | 50 units across 3 regions; **pilot shops report less shrinkage than the honesty box** (target ≥ 20% more revenue per visit or a measured drop in unpaid items); chamber adviser writes it up |

### Certification checklist (EU)
- **CE under RED** (WiFi + NFC): EN 300 328, EN 300 330 (NFC), EN 301 489-1/-3/-17, EN 62311; **EN IEC 62368-1** (PoE is SELV; external certified adapter for the 12 V option); **EN 18031-1** mandatory (internet-connected); **-2** if any personal data (member cards → pseudonymous IDs only, but assume -2 applies); **-3** does NOT apply if the device never handles the money (the QR is settled by the bank/PSP) — document this reasoning. Est. €8–12k RED/EMC, €4–6k safety, €12–20k EN 18031.
- **RoHS, REACH, WEEE**, packaging registration.
- **Battery:** none (mains/PoE only — keep it that way).
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware, OTA, SBOM, vulnerability contact; this is a device that will be attacked (price tampering), so do it properly.
- **GDPR:** member-card IDs and purchase histories are personal data → privacy notice at the terminal, data minimisation, farmer as controller, you as processor if you host summaries. No camera, no mic.
- **Fiscal law:** DE KassenSichV/TSE question, AT RKSV, CH/NL receipt rules — adviser per country before sale. **MID:** weighed goods only via a certified scale.
- **Total certification budget estimate: €25–40k** plus €8–15k fiscal/legal.

### Validation toolkit
- **Kill question:** Do 5 farm shops in one region run it for 2 months and report less shrinkage than the honesty box?
- **Cheapest experiment (~€1,200):** 5 works-like units from catalogue modules in printed cases, a 20-product list each, GiroCode QR, and a paper sign "pay here, scan your items"; baseline = last 8 weeks of honesty-box takings vs. stock out.
- **5-question interview (farm-shop owner):** 1) How do customers pay today and how much do you think goes unpaid? 2) What's the one product you can't sell unstaffed and why? 3) Who in the family would set up the product list, and on what device? 4) What happened the last time the internet in the shed went down? 5) €599 once, no monthly fee, your bank app settles the money — what would stop you?
- **Landing page:** headline "A self-checkout for your farm shop. €599 once. No monthly fee." Bullets: "Customers scan, see a payment QR, pay with their banking app — the money goes straight to your account." / "Works without internet; daily summary to your phone." / "Steel housing, one PoE cable, member cards for regulars."
- **Pass threshold:** 5 pilots completed with shrinkage data in your favour, or 40 pre-orders at €549 from one region's direct-marketing association within 6 weeks.

### First production checklist
- Samples: 5 golden samples with scanner alignment records, touch calibration, PoE power budget log.
- DFM: scanner window glass and anti-glare, panel bonding, gasket for IP54 front, cable glands, VESA holes, anti-tamper screws.
- MOQ talk: scanner modules 500–1k (two vendors), panels 1k, PoE magnetics reel, sheet-metal 500, ABS front 1k.
- QC: AQL II 2.5/4.0; 100% scan test with 5 barcode types, touch, NFC, PoE; 24 h soak on 5%.
- Packaging: wall mount + screws + PoE note; printer SKU boxed separately.
- Incoterms: FOB Shenzhen; air for 50, sea for 1,000.

## 4. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit QRCode (U173)](/db/m5stack-unit-qrcode.html) (QR/barcode scanner module); [M5Stack Core2 (K010)](/db/m5stack-core2.html) (touch-screen terminal for the prototype); [M5Stack Unit PoESP32 (U138)](/db/m5stack-unit-poesp32.html) (PoE/Ethernet for a stable connection in a shed); [M5Stack Unit RFID2 (U031-B)](/db/m5stack-unit-rfid2.html) (member-card reading for regulars). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Pax Technology** (百富计算机技术(深圳)有限公司) · paxintl.com — Payment terminal / POS solution house: Android POS; handheld POS; smart terminal; CE/FCC/EMV. *(POS / payment terminals and barcode scanners)*
- **Newland (SZ)** (新大陆(深圳)科技有限公司) · newlandaidc.com — Barcode / RFID / POS terminal: Barcode scanner; NFC reader; POS terminal; RFID reader. *(POS / payment terminals and barcode scanners)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in section 3 is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B) — for a Farm-Shop Self-Checkout

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Farm-Shop Self-Checkout: A rugged QR/barcode self-checkout terminal for unstaffed farm shops and honesty fridges: scan the product, show a payment QR code, print or display the receipt — no lock, no cash drawer, no monthly POS licence. The design is built around your M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B).
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
主题：样品订购及批量报价 — M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B) — 用于Farm-Shop Self-Checkout

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Farm-Shop Self-Checkout：A rugged QR/barcode self-checkout terminal for unstaffed farm shops and honesty fridges: scan the product, show a payment QR code, print or display the receipt — no lock, no cash drawer, no monthly POS licence。产品设计基于贵司的M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B)。
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
Subject: PCBA quote from open design files — Farm-Shop Self-Checkout, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Farm-Shop Self-Checkout: A rugged QR/barcode self-checkout terminal for unstaffed farm shops and honesty fridges: scan the product, show a payment QR code, print or display the receipt — no lock, no cash drawer, no monthly POS licence. The design starts from published open-hardware files (M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Farm-Shop Self-Checkout，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Farm-Shop Self-Checkout：A rugged QR/barcode self-checkout terminal for unstaffed farm shops and honesty fridges: scan the product, show a payment QR code, print or display the receipt — no lock, no cash drawer, no monthly POS licence。设计基于已公开的开源硬件文件（M5Stack Unit QRCode (U173), M5Stack Core2 (K010), M5Stack Unit PoESP32 (U138), M5Stack Unit RFID2 (U031-B)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order Core2 + Unit QRCode + Unit PoESP32 + Unit RFID2 (×5) and build a basket-to-GiroCode demo; scan 20 real farm-shop products.
2. Call the direct-marketing adviser at your regional chamber of agriculture and ask for 5 unstaffed shops willing to pilot; ask them about the 2027 digital-payment proposal and fiscal rules in your country.
3. Book one hour with a tax adviser who knows KassenSichV/RKSV: "is a payment-request terminal that logs baskets a recording system?" — the answer shapes the product.

Want help sourcing or building this? Talk to us via www.gongbans.com.
