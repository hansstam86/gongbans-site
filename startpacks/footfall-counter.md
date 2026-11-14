# Footfall Counter (GDPR by design) — Founder Start Pack

> A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Public libraries, museums and small retailers must report visitor numbers (funding, KPIs, opening-hour decisions) but stereo-vision counters cost €500–1,500 per door plus a software contract, and anything with a lens makes the data-protection officer nervous.
- **Customer:** Municipal libraries and museums (procurement by the head of facilities or the library director, paid from a small-equipment budget), independent shops, co-working operators. The DPO is the second buyer you have to convince.
- **Product:** A dome the size of a smoke detector, PoE or 12 V, with a K230-class NPU that runs a top-down person detector and line-crossing logic on the device. Output: in/out counts per minute over MQTT/REST/CSV. No image ever leaves the housing — there is no path for one to. €299–399 per unit (estimate), optional €5/month dashboard.
- **Why now:** The AI Act and five years of GDPR enforcement have made "camera" a dirty word in public procurement, while open NPU boards now run person detection at 30 fps for under €30 of silicon. "Auditable firmware, counts only" is a real differentiator with public buyers.
- **The ask:** ~€110k to certified product and the first 1,000 units; roughly half from paid pilots with 10–20 institutions, the rest a small angel round or a regional innovation grant.

## 2. Business plan

### Problem & customer

Every German public library reports to the Deutsche Bibliotheksstatistik; Dutch libraries report to the KB; museums report to their funders. Most of them count with a break-beam at the door (counts a pushchair as two and a group as one), a turnstile, or a volunteer with a clicker. The ones that bought stereo counters did so through a specialist (one German reseller claims 500+ library customers) at a price that only the city library could afford; the branch libraries kept the clicker.

- **Who pays:** the institution (library director, museum operations manager, facilities), typically below the tender threshold — one or two units per site. Shops: the owner. Co-working: the operations lead.
- **Who uses:** the same person, monthly, exporting a CSV for the report. The DPO reviews it once.
- **What they actually want:** a number they can defend, a device nobody can accuse of filming, and zero IT work. The dashboard is secondary; CSV export and an MQTT topic are mandatory.

### Market size (estimates — check)

- **TAM:** EU public libraries ≈ 65k service points (German DBS lists ~9k, France ~16k, the rest spread), museums ≈ 30k, independent retail with staffed doors ≈ 2M. Taking only libraries + museums + co-working at 1.5 doors per site at €350 = **€50M** of hardware, refreshed every 7–8 years.
- **SAM:** sites that need counts for funding and can buy below tender thresholds in DE/NL/AT/BE/Nordics ≈ 25k sites → **€13M**, plus retail tail.
- **SOM (3 years):** 3,000–5,000 units through two or three library-supply resellers and direct → **€1–1.7M** revenue. Year 1: 500–1,000 units.

Sources used: Eastek reseller claims (eastek.de), Sensource people-counting overview, Storetraffic and destination.one price pages. Statistics-reporting duty per country: verify with the national library association.

### Competition (2 searches)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing / clicker / turnstile | €0–2k | Inaccurate, labour, no time-of-day data |
| Break-beam / IR counters (Eastek Counteasy and similar) | €150–500 | Can't separate groups, direction errors; still the library default |
| 3D stereo counters: Axis P8815-2, Hella APS-90E, Xovis, FootfallCam | €800–1,500 + licence | 97–99% accuracy, but quote-only pricing, software contracts, and a camera a DPO has to assess |
| Mid-range 2D/3D: Storetraffic 3D Scope II LC (~$1,150), PEARL (~$500), destination.one 3D counter (€499) | €450–1,100 | Mostly cloud-tied; some stream video for calibration |
| WiFi/BLE probe counting | €100–300 | Random MACs made it useless; privacy problem |
| DIY: Raspberry Pi + OpenCV | €120 + weekends | No enclosure, no CE, nobody maintains it after the intern leaves |

**Wedge:** the only counter under €400 with a signed statement that the device cannot export images, a one-page DPIA template, and plain MQTT/CSV output. Sell the paperwork as much as the dome.

### Product & value proposition

- Dome 110 mm, white ABS, mounts to a standard ceiling box or with 3M adhesive; 2.5–4 m ceiling height; 90° lens looking straight down.
- Inside: K230-class SoC with NPU (see start kit), 2 MP global-shutter or rolling-shutter sensor, PoE (802.3af) or 12 V barrel. Optional ToF for ceiling-height auto-calibration.
- Firmware: person detection → tracking → virtual line crossing → counts aggregated per minute. Frame buffer is never written to flash; debug port physically absent on production units; a signed firmware hash is printed on the label.
- Outputs: MQTT, REST pull, CSV on a web page, optional LoRaWAN uplink for sites without Ethernet.
- **Pricing (estimates):** B2B list €349 (PoE) / €399 (PoE + LoRaWAN). Reseller net €260. Optional hosted dashboard €5 per device-month. Lite SKU on ESP32-P4 at €199 for shops once the model is proven.

### Unit economics (estimates, EUR per unit; K230 PoE SKU)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (K230 SoC + DDR €18–22, image sensor + lens €6, PoE PD + magnetics €4.5, Ethernet PHY €1.5, PCB 4-layer €2.5, passives/connectors €3) | 38 | 31 |
| PCBA assembly + functional test (camera focus + count test on a jig) | 5.5 | 3.8 |
| Enclosure (dome + base, 2 tools, ~€12k tooling amortised in 1k column) | 6.5 | 3.0 |
| Packaging + mounting kit + leaflet | 2.2 | 1.6 |
| Freight + duty to EU (air 1k, sea 5k; duty 0% on most 8471/8525 — verify HS code) | 3.5 | 1.6 |
| Certification amortised (€28k incl. EMC/LVD/PoE, RoHS, EN 18031 if WiFi — see below) | 28.0 | 5.6 |
| **Landed cost** | **83.7** | **46.6** |
| Direct sale at €349 ex VAT, less €12 fulfilment/support | 337 | 337 |
| **Gross margin direct** | **€253 (75%)** | **€290 (86%)** |
| Reseller net €260 ex VAT | €176 (68%) | €213 (82%) |

Software is where the margin disappears: budget 0.3 FTE of firmware maintenance per year forever. The hosted dashboard pays for that.

### Go-to-market

**First 100 customers:** 20 paid pilots at €249 (device + 3 months dashboard, convertible to purchase) with libraries in one region — Dutch "bibliotheken" (via the provincial support organisations), German Stadtbibliotheken (via the library association's mailing list and the Bibliothekartag exhibition). Co-working: the big operators have a facilities lead on LinkedIn — 10 cold messages. Shops: two Dutch retail-tech newsletters and a Chamber of Commerce "retail innovation" event.

**Scale:** library-supply resellers (the ones selling RFID gates and self-checkout already visit every library), museum-tech integrators, electrical wholesalers' PoE catalogue, and the Home Assistant/open-hardware crowd for the Lite SKU. Public-sector marketplaces in DE (e.g. the municipal procurement platforms) once you have three references.

### 12-month plan

- **Q1:** kill-question experiment (see toolkit), works-like prototype on the K230 dev board, model trained on top-down data from two friendly sites, DPIA template drafted with a data-protection lawyer (€2–3k).
- **Q2:** EVT boards (own carrier for the K230 module), dome tooling, 20 pilot units in the field, pre-compliance EMC.
- **Q3:** DVT, full EMC/LVD/PoE certification, pilot batch 50, first reseller signed, dashboard v1.
- **Q4:** production batch 500–1,000, library-association conference, Lite SKU on ESP32-P4 in development.

**Team:** founder (product + sales to institutions), 1 embedded/ML engineer (K230 toolchain, CanMV or Linux), 0.5 web developer (dashboard, MQTT bridge), contract ME for the dome, contract data-protection lawyer.

**Funding to 1,000 units (estimate):** NRE €25k (ML dataset + model work €8k, carrier PCB design €7k, dome tooling €12k) + certification €28k + salaries 9 months × €7k (two people, lean) €63k + first 1,000 units at €56 landed ≈ €56k. Total ≈ **€170k**, less €40k of pilot and pre-order revenue → **€130k** net. Route: 20 pilots paid up front, regional innovation grant (many German states and the Dutch MIT scheme fund "AI + privacy" products), and a €75–100k angel ticket. Keep bootstrapping possible by shipping the 50-unit pilot batch from hand assembly.

### Top risks

- **Technical — accuracy below 95% at real doors** (glass reflections, hats, kids, trolleys). Mitigation: collect 20k frames at three real sites before committing to the model; add the ToF height channel; set the honest spec at 95% and document it.
- **Market — libraries buy slowly and from incumbents.** Mitigation: price below the tender threshold, sell through the reseller they already know, lead with the DPIA template.
- **Regulatory — AI Act, GDPR.** Counting people without identification is not biometric identification and should be minimal-risk, but you must document it (Article 4-style literacy note, technical documentation). Have the lawyer confirm; publish the firmware hash and the "no image path" architecture statement.
- **Supply — K230 is a single-source Chinese SoC with an immature toolchain.** Mitigation: ESP32-P4 Lite SKU as a second platform; buy 1,000 SoCs when you commit; keep the model portable (ONNX → both NPUs).
- **Commercial — software support cost.** Mitigation: dashboard subscription; keep the device dumb (counts only) so firmware churn is low.

## 3. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| 立创·庐山派K230-CanMV开发板 (OSHWHub) | https://www.gongbans.com/db/oshwhub-li-chuang-lu-shan-pai-k230-canmv-kai-fa-ban.html | Open K230 AI-vision board: NPU, three camera inputs, CanMV — your person detector runs here first | schematic, pcb | OSHWHub project licence — check on the project page before deriving a commercial carrier |
| Espressif esp32-p4-eye | https://www.gongbans.com/db/espressif-esp32-p4-eye.html | Reference for the lower-cost Lite SKU (camera + P4 compute) | reference design files from Espressif (per catalogue) | Espressif reference-design terms; check |
| M5Stack Unit PoE P4 (U213) | https://www.gongbans.com/db/m5stack-unit-poe-p4.html | PoE power path for ceiling installs, prototype stage | enclosure/structure files only; electronics not published | Off-the-shelf module; use as bought, do not copy |
| M5Stack Unit ToF4M (U172) | https://www.gongbans.com/db/m5stack-unit-tof4m.html | Ceiling-height calibration / low-light fallback | enclosure/structure files only | Off-the-shelf module |

### Block diagram

```
[2 MP image sensor] --MIPI--> [K230 SoC + NPU] --> person det. --> tracker --> line crossing --> counts/min
[ToF4M (optional)] --I2C-----^      |                                                     |
[PoE PD 802.3af] --> 5V/3.3V -------+                                    [Ethernet PHY] --> MQTT / REST / CSV
                                                                          [LoRaWAN (opt)] --> counts only
No frame buffer written to flash. No video output. Debug UART unpopulated in production.
```

**Engineering gap:** (1) a top-down person-detection model tuned for 2.5–4 m ceilings — public datasets are side-view; you must collect your own; (2) a production carrier board with PoE and no debug ports, derived from the open K230 schematic; (3) tracking/line-crossing logic that handles groups and reversals; (4) the thermal budget inside a sealed dome (the K230 runs warm — plan a metal insert).

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| K230 SoC + LPDDR | €18–22 | Sole-source (Canaan); 12–16 wk lead reported — buy ahead |
| 2 MP MIPI image sensor + M12 lens (90° FoV) | €6 | Several second sources; pick a sensor with a CanMV driver |
| PoE PD controller + flyback + magnetics | €4.5 | Standard parts, multi-source |
| Ethernet PHY (RMII) | €1.5 | Multi-source |
| ToF sensor (optional) | €3–5 | Buy the Unit for prototypes only |
| eMMC/SD boot + flash | €2.5 | |
| 4-layer PCB 80 × 80 mm | €2.5 | |
| Dome + base (ABS, UV-stable white) | €3.0 at 5k | Tooling €12k |
| Mounting plate + screws + 3M pad | €0.8 | |

### Firmware/software starting point

- CanMV firmware and examples for the K230 (Canaan's official CanMV project) — the fastest route to a running detector.
- Ultralytics YOLO (train a small detection model on your top-down dataset; export ONNX, then convert with the K230 nncase toolchain).
- Norfair or ByteTrack (Python trackers; port the logic to C on the device).
- Eclipse Mosquitto for MQTT, Node-RED or Grafana for the pilot dashboard.
- For the Lite SKU: ESP-IDF plus Espressif's ESP-DL / ESP-WHO examples — search for the current P4 human-detection example before relying on it.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | K230 dev board + webcam at 3 m above a friendly library entrance for one week against a manual tally; after two tuning passes ≥92% daily agreement. Below 92%: stop or change the sensing approach. Five library directors say they would pay ≥€250. |
| 3–5 | Works-like | Own dataset (≥10k frames, 3 sites), trained model, tracker + line-crossing running on the dev board at ≥15 fps, counts published to MQTT; ≥95% on a held-out day. |
| 6–8 | Looks-like + EVT | Carrier PCB v1 with PoE, dome prototype (SLA), 10 units in the field for 2 weeks; thermal ≤70 °C SoC at 30 °C ambient; pre-EMC scan. |
| 9–10 | DVT + pre-compliance | PCB v2, EMC pre-scan clean with 6 dB margin, PoE PD compliance check, DPIA template reviewed by a lawyer, firmware hash and no-image statement documented. |
| 11–12 | Pilot batch | 30–50 units from a contract manufacturer, golden sample signed, 20 paying pilots installed, accuracy audit at 3 sites ≥95%. |

### Certification checklist (EU)

- **CE:** EMC Directive (EN 55032/55035) + LVD (EN 62368-1) for the PoE/12 V SKU. **RED** (EN 300 328 + EN 301 489 + EN 62311) only if you add WiFi; LoRaWAN variant → RED with EN 300 220.
- **RED delegated act / EN 18031:** applies if the device connects to the internet directly (WiFi or LoRaWAN uplink). Ethernet-only PoE devices are outside RED but inside the **CRA** anyway: reporting obligations since September 2026, full conformity December 2027 — build secure boot, signed updates, a vulnerability-disclosure page now.
- **RoHS, REACH (SVHC declaration), WEEE** registration in each country of sale (DE: stiftung ear; NL: via a compliance scheme).
- **GDPR:** even counts-only, the device processes images transiently → provide the DPIA template, a data-flow diagram and the "no image can leave" architecture statement. Do not add face or demographic features — that would change everything.
- **EU AI Act:** people counting without identification is minimal-risk; keep a technical file and a short transparency note anyway. Avoid any "biometric categorisation" feature.
- **Estimated test costs:** EMC + LVD €8–12k; PoE interoperability check €2k; RED if WiFi +€10k; EN 18031 self-assessment with notified-body review €15–25k (only if WiFi/LoRa); RoHS/REACH documentation €2k; legal (DPIA, AI Act note) €3k. Budget **€28k** for the PoE SKU, €55k if you add radio.

### Validation toolkit

- **Kill question:** does an off-the-shelf K230 board + webcam at 3 m match a human tally to ≥92% after two tuning passes? **Cheapest experiment:** one dev board (~€60), a USB webcam, a tripod cross-bar on a bookshelf, and a volunteer with a clicker for 2 hours a day over a week. Cost < €300.
- **5-question interview (library director / museum ops):** 1) How do you count visitors today and how long does the monthly report take? 2) What happened the last time someone questioned the numbers? 3) Has a data-protection officer ever blocked a camera or sensor purchase — why? 4) What is your limit for buying a device without a tender? 5) If a counter cost €350 and came with a signed data-protection file, who would need to approve it?
- **Landing page:** headline "Visitor counts you can defend. No camera footage, ever." Bullets: "Counts in/out, nothing else — physically cannot export images"; "€349, plug into PoE, CSV and MQTT out of the box"; "DPIA template included — your data-protection officer signs in ten minutes".
- **Pass threshold:** 20 paid pilots at €249 within 6 weeks, or 50 pre-orders at €299 with a €50 deposit.

### First production checklist

- Samples: 5 EVT, 10 DVT, 30–50 pilot; keep two of each.
- Golden sample: signed by you and the factory, with a count-accuracy test video and firmware hash.
- DFM review: dome draft angles, lens alignment to the sensor (±0.5 mm), heat path from SoC to the base plate, PoE magnetics placement.
- MOQ talk: PCBA 500 (K230 reel 1k is the real constraint), dome 1k shots, image sensor 1k.
- QC/AQL: ISO 2859-1 level II, AQL 1.0 major / 2.5 minor; 100% functional test on a jig with a moving target; sample focus check.
- Packaging: single-unit box, mounting kit, printed firmware hash and DPIA QR code.
- Incoterms: FOB Shenzhen for the first batches; move to DAP once volumes justify a forwarder contract.

## 4. Next steps (this week)

1. Order one K230 CanMV board, a USB camera and a PoE Unit; get a person detector running on it by Friday.
2. Ask two libraries you can reach for permission to hang a dev board above the entrance for a week in exchange for the data — write the 5-question script first and interview the director when you install it.
3. Draft the one-page DPIA template and the "no-image architecture" statement; send to a data-protection lawyer for a fixed-price review.

Want help sourcing or building this? Talk to us via www.gongbans.com.
