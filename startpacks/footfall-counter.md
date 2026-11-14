# Footfall Counter (GDPR by design) — Founder Start Pack

> A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Public libraries, museums and small retailers must report visitor numbers (funding, KPIs, opening-hour decisions) but stereo-vision counters cost €500–1,500 per door plus a software contract, and anything with a lens makes the data-protection officer nervous.
- **Customer:** Municipal libraries and museums (procurement by the head of facilities or the library director, paid from a small-equipment budget), independent shops, co-working operators. The DPO is the second buyer you have to convince.
- **Product:** A dome the size of a smoke detector, PoE or 12 V, with a K230-class NPU that runs a top-down person detector and line-crossing logic on the device. Output: in/out counts per minute over MQTT/REST/CSV. No image ever leaves the housing — there is no path for one to. €299–399 per unit (estimate), optional €5/month dashboard.
- **Why now:** The AI Act and five years of GDPR enforcement have made "camera" a dirty word in public procurement, while open NPU boards now run person detection at 30 fps for under €30 of silicon. "Auditable firmware, counts only" is a real differentiator with public buyers.
- **The ask:** ~€110k to certified product and the first 1,000 units; roughly half from paid pilots with 10–20 institutions, the rest a small angel round or a regional innovation grant.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Camera-free, privacy-safe people counting is an established category (Terabee thermal / time-of-flight, FootfallCam hashing, Ariadne consent-free analytics), and the compliance angle is real and current, with the EU AI Act as a tailwind. No public pricing was found, so "a third of the incumbents' price" is unverifiable. **Main risk:** The price claim is unsupported; the differentiation must be proven on compliance and simplicity. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Run the K230 dev board + a webcam at 3 m above a friendly library entrance for a week against a manual tally. <92% after two tuning passes = stop.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Municipal libraries and museums, independent retailers, co-working spaces across the EU.

**The problem as the pack states it:** Public libraries, museums and small retailers must report visitor numbers (funding, KPIs, opening-hour decisions) but stereo-vision counters cost €500–1,500 per door plus a software contract, and anything with a lens makes the data-protection officer nervous.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/smallbusiness** · https://www.reddit.com/r/smallbusiness/ — shop and café owners.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€299–399, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how municipal libraries and museums, independent retailers, co-working spaces across the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know how many people came into the shop yesterday, and what would you change if you knew the number per hour?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops. On a scale of one to ten, how likely would you be to buy that at €299–399, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Footfall Counter (GDPR by design): looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Footfall Counter (GDPR by design): A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops. Before we spend money on tooling I want to find out whether this solves a real problem for municipal libraries and museums, independent retailers, co-working spaces across the EU.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €299–399 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

Two questions, no pitch: how do you handle this today, and what would make you say no to the above? Twenty minutes on a call this week, or a reply here, both help.
```

### Reading the signal

| Real signal | False positive |
|---|---|
| A refundable deposit, a signed LOI, a paid pilot, a calendar invite for the prototype | "Sounds cool", "I would totally buy that", likes and upvotes |
| They describe the problem unprompted and in detail, with numbers | They agree with your description of the problem |
| They have already paid for a workaround (a product, a service, their own time) | They have never tried anything and are not bothered |
| Landing-page conversion to deposit or form above the pack's pass mark, from cold traffic | Conversion from friends, family and your own network |
| A named budget and a named decision-maker (B2B) | An enthusiastic user who cannot buy |

### Go / no-go

- **Go to section 3 (business plan) and section 4 (start kit)** when the kill question above is met by your own numbers, you have 15–20 written-up conversations, and at least one real signal from the left column per segment you plan to sell to. Only then does section 5 (Who to contact) apply.
- **Change the idea** when the problem is real but the price, the buyer or the form factor in the pitch is wrong: the interviews will tell you which. Rewrite the pitch and run the fake door again; this is normal and costs a week.
- **Stop** when the kill question fails on honest numbers, or when nobody you talked to has paid for a workaround. Pick another idea on this site; the boards in the start kit are not wasted, only unused.

The full worksheet, with how to define the segment and run the fake door, is in the [playbook → validate demand](/playbook.html#validate).
<!-- validate-demand:end -->

## 3. Business plan

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

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Terabee people counting + GDPR pages | Thermal / ToF counters | Incumbent in the privacy-safe niche |
| FootfallCam privacy statement | Hashing-based counting | Incumbent |
| Ariadne consent-free footfall | Analytics without consent prompts | Incumbent |

**Verdict as researched: LIKELY.** Main risk: The price claim is unsupported; the differentiation must be proven on compliance and simplicity.
<!-- market-competitors:end -->

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

## 4. Start kit

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

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Espressif and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-p4-eye](/db/espressif-esp32-p4-eye.html) (lower-cost compute/camera reference for the lite SKU). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit PoE P4 (U213)](/db/m5stack-unit-poe-p4.html) (PoE for ceiling installs); [M5Stack Unit ToF4M (U172)](/db/m5stack-unit-tof4m.html) (ToF for ceiling-height calibration / low-light fallback). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [立创·庐山派K230-CanMV开发板](/db/oshwhub-li-chuang-lu-shan-pai-k230-canmv-kai-fa-ban.html) (fully open K230 AI-vision board (NPU, multiple camera inputs) — person detection and line crossing on device).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Forlinx Embedded** (飞凌嵌入式技术有限公司) · forlinx.com — ARM core board / SOM OEM: i.MX8M / RK3568 / AM62x SOM; carrier board; Linux BSP; OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **Toradex (SZ)** (深圳图睿达科技有限公司) · toradex.com — Industrial SOM / embedded Linux OEM: Apalis / Colibri SOM; carrier board; Yocto Linux; long-term supply. *(Edge-AI / SOM boards and Linux BSPs)*
- **iWave Systems (SZ)** (爱微电子(深圳)有限公司) · no website on file — ARM SOM / carrier board ODM: RK3568/i.MX8 SOM; carrier board; embedded Linux OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **Kangshida (Conradtech)** (深圳市康士达科技有限公司) · cstipc.com — Industrial PC / AI edge computing OEM: Industrial PC board; AI edge card; computer vision; OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Espressif and M5Stack websites)

```email
Subject: Sample order and volume pricing — Espressif esp32-p4-eye, M5Stack Unit PoE P4 (U213), M5Stack Unit ToF4M (U172) — for a Footfall Counter (GDPR by design)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Footfall Counter (GDPR by design): A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops. The design is built around your Espressif esp32-p4-eye, M5Stack Unit PoE P4 (U213), M5Stack Unit ToF4M (U172).

Could you please send:
1. Price and lead time for [10] sample units of each: Espressif esp32-p4-eye, M5Stack Unit PoE P4 (U213), M5Stack Unit ToF4M (U172).
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
主题：样品订购及批量报价 — Espressif esp32-p4-eye, M5Stack Unit PoE P4 (U213), M5Stack Unit ToF4M (U172) — 用于Footfall Counter (GDPR by design)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Footfall Counter (GDPR by design)：A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops。产品设计基于贵司的Espressif esp32-p4-eye, M5Stack Unit PoE P4 (U213), M5Stack Unit ToF4M (U172)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Espressif esp32-p4-eye, M5Stack Unit PoE P4 (U213), M5Stack Unit ToF4M (U172)。
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
Subject: PCBA quote from open design files — Footfall Counter (GDPR by design), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Footfall Counter (GDPR by design): A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops. The design starts from published open-hardware files (立创·庐山派K230-CanMV开发板; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Footfall Counter (GDPR by design)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Footfall Counter (GDPR by design)：A ceiling-mounted edge-AI counter that outputs only in/out numbers — never an image — at a third of the incumbents' price, for libraries, museums and independent shops。设计基于已公开的开源硬件文件（立创·庐山派K230-CanMV开发板；含原理图、PCB和BOM），并做了我们自己的修改。

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

## 6. Next steps (this week)

1. Order one K230 CanMV board, a USB camera and a PoE Unit; get a person detector running on it by Friday.
2. Ask two libraries you can reach for permission to hang a dev board above the entrance for a week in exchange for the data — write the 5-question script first and interview the director when you install it.
3. Draft the one-page DPIA template and the "no-image architecture" statement; send to a data-protection lawyer for a fixed-price review.

Want help sourcing or building this? Talk to us via www.gongbans.com.
