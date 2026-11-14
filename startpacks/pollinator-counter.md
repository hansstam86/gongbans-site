# Pollinator Counter — Founder Start Pack

> A solar camera post that counts and classifies flying insects on a flower patch with on-device vision and uploads only counts — field data for biodiversity monitoring, farms and research.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The EU Pollinator Monitoring Scheme (adopted late 2025) obliges member states to run standardised monitoring of bees, butterflies, hoverflies and moths by 16 December 2026, and the Nature Restoration Regulation asks them to reverse pollinator decline by 2030. The core method is people walking transects — expensive, weather-bound, and there aren't enough trained surveyors. Existing camera traps (DIOPSIS-class, €500–700+ a few years ago, quote-only now) send images to the cloud and are built for research, not fleets.
- **Customer:** Ecological consultancies that deliver monitoring to agencies and farms, agri-environment scheme operators, universities and NGOs running monitoring programmes; later, food companies with biodiversity KPIs. Agencies and farm schemes pay; consultancies specify and deploy.
- **Product:** A weatherproof post with a downward camera over a 1 m² flower patch, an NPU running an insect detector/classifier on device, solar + battery, LoRaWAN or Cat-M uplink of counts per class per 15 minutes — no images leave the post unless the researcher asks for a sample. €599–899 per post + data service (estimates).
- **Why now:** The regulatory clock (Dec 2026), farm-subsidy biodiversity evidence, and open NPU vision boards with schematics that run detection at a few watts. The gap is a season of validated field data against manual transects — not hardware.
- **The ask:** ~€140k to the first 300 posts (a season of validation comes before any volume; 1,000-unit math shown for reference), funded by one paid consultancy trial, a research/biodiversity grant and a small angel ticket.

## 2. Business plan

### Problem & customer

Transect walks (the EU-PoMS core) are done by trained people in good weather between 10:00 and 17:00; moths need light traps and night visits. A camera that watches one flower patch continuously is not a transect replacement — the scientists will tell you that — but it is a complementary module that gives continuous abundance and activity data at sites nobody can visit weekly. The commercial buyer is not the ministry; it is the consultancy that wins the monitoring contract and needs to cover 50 sites with 3 people.

- **Who pays:** agencies via consultancies (contract monitoring), farm schemes and cooperatives (evidence for subsidy/certification), food and retail groups (sustainability KPIs), research projects (grant money, per-unit purchase).
- **Who uses:** field ecologists (install, maintain, validate), data scientists (the open data format), and the farmer who looks at a dashboard once.
- **What they fear:** a black box whose counts a reviewer won't accept. Open data, published validation and a sample-image mode are your credibility.

### Market size (estimates — check)

- **TAM:** EU-PoMS core sites across 27 member states (the delegated act defines sampling designs per country — verify the counts; thousands of sites EU-wide) + agri-environment monitoring + research. Say 20k candidate sites × 1.5 posts × €750 = **€22M** hardware + data service €150–300/post/year.
- **SAM:** consultancies and schemes in DE/NL/FR/DK/AT/BE/UK plus EU research projects ≈ 40% → **€9M** + services.
- **SOM (3 years):** 1,500–2,500 posts → **€1.1–1.9M** + €0.3M/year data. Year 1: 100–300 (validation year).

Sources used: European Commission news (26 Nov 2025) and CREAF/CETAF pages on EU-PoMS adoption and the 16 Dec 2026 implementation deadline; Naturalis/Faunabit DIOPSIS pages (quote-only, 8 MP camera, 4G, 12 V 20 Ah battery + solar option) and a WildLabs forum post (€500–700, ~4 years old); a 2021 Methods in Ecology and Evolution paper noting €400 to several thousand per insect camera trap and a <$100 DIY alternative. Site counts: estimates — pull the delegated act from EUR-Lex.

### Competition (2 searches)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing — transect walks and pan traps by trained surveyors | labour (€300–600 per site visit incl. travel) | The core method, but capacity-limited; continuous data impossible |
| DIOPSIS insect camera (Naturalis/Faunabit) | quote-only; historically €500–700 + 4G + cloud | Research-grade, cloud image analysis, built for the Dutch programme; not a counts-only fleet device |
| AMI (Automated Monitoring of Insects) system — open-source, UK-led, nocturnal/moth focus | open design; build cost in the hundreds | Moths with a light; open and respected — partner on data formats, don't compete |
| PICT-style DIY camera traps (<$100 parts) | <€100 + labour | Research prototypes; no classification on device, no weatherproof fleet |
| Acoustic/optical insect sensors (various start-ups) | project pricing | Different signal; limited taxonomic resolution; mostly agricultural pest focus |
| Generic wildlife trail cameras | €100–300 | Not for insects; motion trigger fails on small targets |

**Wedge:** counts-only on device (tiny data, LoRaWAN-able, GDPR-light), solar fleet hardware under €900 with an open data format, and a published validation against transects — positioned as the EU-PoMS "complementary module" tool for consultancies.

### Product & value proposition

- Post: 1.2 m aluminium pole with ground spike, camera head at 0.6–0.8 m above a 1 m² flower patch (or a standard planted "pollinator panel" you supply for comparability), 20 W solar panel, 12 V 12–20 Ah LiFePO4 (cold-tolerant, safer than Li-ion), IP66 head, anti-theft bolts.
- Vision: 5 MP camera with a fixed lens, K230-class NPU running a two-stage detector/classifier (bee / bumblebee / butterfly / hoverfly / other) at 2–5 fps during daylight; motion gating to save power; a nightly self-check image stored locally.
- Uplink: counts per class per 15 minutes + weather context (T/RH/light) over LoRaWAN (farm gateways or public networks) or Cat-M; sample images on request over Cat-M only.
- Data: open JSON/CSV schema, API, and a Darwin Core-compatible export for researchers; dashboard for consultancies with site maps and QA flags.
- **Pricing (estimates):** post €699 (LoRaWAN) / €899 (Cat-M); data service €199/post/year; validation kit (pollinator panel + protocol) €149; research discount 15%.

### Unit economics (estimates, EUR per post; LoRaWAN model)

| Item | 300 | 1,000 |
|---|---|---|
| Electronics BOM (K230-class SoC + DDR €20, 5 MP camera module €9, LoRaWAN module €7, env. sensor €3, solar charge controller + LiFePO4 BMS €9, PCB + passives €6) | 54 | 46 |
| Power (20 W panel €14, 12 V 12 Ah LiFePO4 €38) | 52 | 45 |
| Mechanics (pole, spike, head housing IP66, bracket, anti-theft hardware) | 48 | 36 |
| Assembly + test (camera focus, IP test sample, join test) | 14 | 9 |
| Enclosure tooling share (head housing die-cast/moulded only at 1k; CNC/off-the-shelf box at 300) | 0 | 6 |
| Packaging (long box) | 9 | 6 |
| Freight + duty to EU (bulky; LiFePO4 DG) | 22 | 12 |
| Certification amortised (€40k) | 133 | 40 |
| **Landed cost** | **332** | **200** |
| Direct sale €699 ex VAT, less €30 fulfilment/support | 669 | 669 |
| **Gross margin direct** | **€337 (50%)** | **€469 (70%)** |
| Via consultancy partner at €560 net | €198 (37%) | €330 (61%) |
| Data service €199/year at ~€25/year cost | +€174/year | +€174/year |

The battery and the pole are a third of the cost — source the LiFePO4 pack from a certified vendor and the pole from an EU aluminium extruder (freight on 1.2 m poles is silly from China).

### Go-to-market

**First customers (20–50 posts):** one ecological consultancy running a season-long trial against their own transect counts (the kill question), recruited via the national ecological-consultant associations and the pollinator research networks; a university group studying pollinators for the validation paper; a farm cooperative with a biodiversity scheme for 10 posts.

**Scale:** consultancies as channel partners (they sell monitoring, you supply posts and data), national EU-PoMS implementing agencies through their complementary-module procurement, agri-environment scheme operators and certification bodies, food groups' sustainability programmes, Horizon-type research consortia. Publish the validation, open the data format, speak at the pollinator-monitoring conferences.

### 12-month plan

- **Q1 (winter):** works-like post from the K230 dev board + camera + solar reference; model v1 trained on public insect datasets (search for open flower-visitor image sets) + your own 20k frames from a greenhouse/botanical garden; sign the consultancy trial for the season.
- **Q2 (spring):** 20 EVT posts in the field at 10 sites paired with transects; LoRaWAN uplink; data schema v1; power budget verified through April weather.
- **Q3 (summer):** season data; model v2; DVT hardware; certification; pilot batch 50; first agency conversation with data in hand.
- **Q4 (autumn):** validation report (within 20% of transects?), production 100–300 for next season, Cat-M SKU, data-service launch.

**Team:** founder (ecology-literate, sells to consultancies), 1 ML/embedded engineer (K230 toolchain, model training, power management), 1 hardware engineer (solar/battery, IP66 mechanics, LoRaWAN), part-time entomologist (labelling protocol, validation design — non-negotiable), part-time data engineer (schema, dashboard).

**Funding to the first 300 posts (estimate):** NRE €45k (carrier PCB €8k, head housing €10k, pole/bracket €5k, dataset + labelling €15k, test rigs €7k) + certification €40k + 12 months salaries (seasonal product — plan a year) €120k + 300 posts at ~€200 landed (ex-certification) €60k = **€265k**, less trial, grant-funded research units and first sales (~€125k) → **€140k** net. Route: paid consultancy trial, biodiversity/agri-tech grants (national and EU — the monitoring scheme itself funds capacity building), an impact angel. Not a bootstrap: a season of validation precedes revenue.

### Top risks

- **Scientific — counts don't match transects within 20%.** A camera over 1 m² sees different things than a 50 m walk. Mitigation: design the trial with the entomologist as a complementary measure (activity index, phenology), not a one-to-one replacement; publish honestly; the regulatory module language supports "complementary methods".
- **Technical — small, fast, back-lit insects on a moving flower.** Mitigation: fixed camera height, a standard pollinator panel for comparability, higher fps bursts on motion, a two-stage model (detect → crop → classify), and the sample-image mode for reviewer audits.
- **Technical — power in April in Denmark.** Mitigation: LiFePO4 sized for 5 days of no sun, duty cycling (daylight only; night = moths later with a light module), measured power budget by week 5.
- **Regulatory — GDPR if a public path is in view.** Mitigation: camera points down at 0.7 m over flowers; field of view documented; DPIA template; counts-only default.
- **Regulatory — batteries and radios.** LiFePO4 → Battery Regulation + UN 38.3; LoRaWAN/Cat-M → RED + EN 18031.
- **Supply — K230 single-source; LiFePO4 cells.** Mitigation: ESP32-P4 lite SKU as plan B; two pack vendors.
- **Theft and vandalism.** Mitigation: anti-theft bolts, no GPS and no location tracking (deliberately), insurance via the consultancy; design to be cheap enough to lose one.

## 3. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| 立创·庐山派K230-CanMV开发板 (OSHWHub) | https://www.gongbans.com/db/oshwhub-li-chuang-lu-shan-pai-k230-canmv-kai-fa-ban.html | Open K230 AI-vision board with NPU and multiple camera inputs — the detector/classifier runs here | schematic, pcb | OSHWHub project licence — check before commercial derivation |
| Espressif esp32-p4-eye | https://www.gongbans.com/db/espressif-esp32-p4-eye.html | Lower-power camera/compute reference for a lite SKU | reference design files from Espressif (per catalogue) | Espressif reference-design terms; check |
| M5Stack Unit CamS3-5MP (U174-B) | https://www.gongbans.com/db/m5stack-unit-cams3-5mp.html | 5 MP camera module reference for optics and sensor choice | enclosure/structure files only; electronics not published | Off-the-shelf; use as bought |
| solar-to-5v-zener-regulator (OSHWHub) | https://www.gongbans.com/db/oshwhub-solar-to-5v-zener-regulator.html | Solar charge-path reference (simple regulator) — a starting point, not your final MPPT/BMS | schematic, pcb (EasyEDA source on the project page) | OSHWHub project licence — check |

### Block diagram

```
[20 W solar panel] --> [MPPT charger + LiFePO4 12 V 12 Ah + BMS] --> 5 V/3.3 V rails (daylight schedule)
[5 MP camera, fixed lens, 0.7 m over 1 m2 patch] --MIPI--> [K230-class SoC + NPU] --> detect -> crop -> classify (5 classes) -> counts/15 min
[T/RH/light sensor] --I2C--------------------------------------^   |
                                                     [LoRaWAN EU868 or Cat-M module] ~~> network ~~> data service (open schema, API, Darwin Core export)
Images: never uploaded by default; nightly self-check image stored locally; sample-image mode on request (Cat-M).
```

**Engineering gap:** the insect model and the labelled dataset (the product); power management for a northern spring; an IP66 head with a lens that stays clean (hydrophobic window, hood); a production carrier for the K230 with the radio and the charger; the validation protocol and open schema; and a pole/bracket that a field ecologist installs alone in 10 minutes.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| K230 SoC + LPDDR | €20 | Single-source (Canaan); 12–16 wk; buy ahead |
| 5 MP MIPI camera module, fixed-focus M12 lens | €9 | Multi-source; choose a sensor with a CanMV driver |
| LoRaWAN EU868 module (pre-certified) or Cat-M module | €7 / €18 | Multi-source |
| T/RH/light sensor | €3 | |
| MPPT solar charger + LiFePO4 BMS board | €9 | Multi-source |
| 12 V 12 Ah LiFePO4 pack (certified, UN 38.3) | €38 | Two vendors |
| 20 W mono solar panel, framed | €14 | Commodity |
| IP66 head housing (die-cast or ASA moulded), hydrophobic window | €12 at 1k | Tooling €18k; off-the-shelf box at 300 |
| 1.2 m aluminium pole + spike + bracket | €24 | EU extruder — freight |

### Firmware/software starting point

- CanMV firmware and examples for the K230; Canaan's nncase toolchain to compile models for the NPU.
- Ultralytics YOLO for detection training; a small classifier (MobileNet-class) for the crop stage; export ONNX → nncase.
- Public datasets: search for open flower-visitor / pollinator image datasets from the research community (several exist from European projects; licences vary) — and label your own.
- ChirpStack or The Things Stack for LoRaWAN; a Darwin Core-compatible export for biodiversity data (GBIF documents the standard).
- The AMI system's open-source software and data conventions as a reference for interoperability with the moth-monitoring community — search the project's repositories.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | One ecological consultancy signs a paid season-long trial (10 sites, posts + transects); an entomologist agrees to co-design the protocol. Meanwhile the K230 dev board + camera over a flowering plant in a greenhouse or botanical garden collects 5k frames. No consultancy in 4 weeks: stop or pivot to a research-only product. |
| 3–5 | Works-like | Detector v1 running on the dev board at ≥2 fps; 5-class classifier ≥80% top-1 on your held-out greenhouse set; counts over LoRaWAN; power budget measured and a 5-day no-sun calculation done. |
| 6–8 | Looks-like + EVT | Carrier PCB v1, IP66 head (off-the-shelf box + custom window), pole and bracket, solar + LiFePO4; 20 posts in the field at 10 sites paired with transects; install time <10 min; EMC pre-scan. |
| 9–10 | DVT + pre-compliance | PCB v2, head housing v2, RED/EMC/safety pre-tests, IP66 test, UN 38.3 report from the pack vendor, EN 18031 checklist, DPIA template for public-view sites. |
| 11–12 | Pilot batch | 50 posts assembled (EU final assembly), golden sample, open data schema v1 published, mid-season interim comparison with transects reported to the consultancy. |

### Certification checklist (EU)

- **CE / RED:** LoRaWAN → EN 300 220 + EN 301 489-1/-3; Cat-M → the module's certification plus EN 301 489-52 system considerations; EN 62368-1 safety (battery, solar input); EN 62311 RF exposure.
- **RED delegated act — EN 18031-1:** applies (internet-connected via LoRaWAN/Cat-M). -2 only if images with persons could be transmitted — keep counts-only default and sample-image mode consent-gated.
- **CRA:** reporting since September 2026, full December 2027; signed firmware, SBOM, disclosure policy, field-update plan (LoRaWAN downlinks are tiny — plan a local USB/BLE update path).
- **Battery Regulation (2023/1542) + UN 38.3:** LiFePO4 is still a lithium battery — labelling, removability, producer registration, DG shipping.
- **IP66 (EN 60529)** test for the head; UV/weathering of the housing material (ASA or coated die-cast).
- **GDPR:** DPIA template for sites with a public path in view; camera geometry documented; counts-only default.
- **RoHS, REACH, WEEE**, packaging registration; outdoor electronics disposal notes.
- **Not a GPS/fleet tracker** — do not add location tracking beyond a static site coordinate entered by the installer.
- **Estimated test costs:** RED (LoRaWAN with pre-certified module) €7–9k, EMC €5k, safety €4k, IP66 €2k, UN 38.3 (vendor report; verify) €0–4k, EN 18031 €12–15k, legal €3k. Budget **€40k**.

### Validation toolkit

- **Kill question:** does a season-long trial with one ecological consultancy match manual transect counts within 20% (or produce a complementary index the consultancy's clients accept)? **Cheapest pre-experiment before the season:** K230 dev board + camera over a flowering patch in a botanical garden for 2 weeks alongside 10 manual 10-minute counts by a volunteer; ≥80% detection agreement on bees and butterflies. Cost < €300.
- **5-question interview (consultancy director):** 1) How many sites do you monitor for pollinators, how often, with how many people? 2) What did the last tender ask for that you struggled to deliver — frequency, night data, remote sites? 3) Would your clients accept counts from a camera if the method were published and auditable? 4) What data format do you deliver today, and who reviews it? 5) At €699 per post plus €199/year, how many posts would you deploy next season — and what would your client need to see first?
- **Landing page:** headline "Continuous pollinator counts from any flower patch. Counts only, solar, open data." Bullets: "On-device classification of bees, bumblebees, butterflies and hoverflies — no images uploaded"; "Solar-powered post, LoRaWAN or Cat-M, installed in 10 minutes"; "Open data schema and published validation — built for EU-PoMS complementary monitoring".
- **Pass threshold:** 1 paid season trial + 2 letters of intent from consultancies or schemes for 20+ posts each for the following season.

### First production checklist

- Samples: 1 greenhouse rig, 20 EVT posts, 50 pilot; keep 3 per revision with field logs.
- Golden sample: detection/classification score on a fixed test video, power log over 7 days, IP test record, join test — signed.
- DFM review: window sealing and anti-fog, lens hood, cable glands, bracket tolerance on the pole, battery compartment drainage, anti-theft fasteners.
- MOQ talk: K230 300 then 1k; packs 300; panels 300; housing tooling only after a validated season.
- QC/AQL: level II, AQL 1.0/2.5; 100% camera focus + model self-test; 100% radio join; IP sample test 5%.
- Packaging: head + electronics in a DG-compliant carton; poles and panels sourced/shipped within the EU.
- Incoterms: FOB Shenzhen for electronics with a DG forwarder; EU final assembly.

## 4. Next steps (this week)

1. Order the K230 CanMV board and a 5 MP camera; mount them 0.7 m above the most flowering plant you can find (a greenhouse or a garden centre will let you) and start collecting frames.
2. Pull the EU-PoMS delegated act from EUR-Lex and read the complementary-module section; write a one-page "camera module" positioning note in its language.
3. Email five ecological consultancies and two university pollinator groups with the trial offer and the five questions; ask the entomologist you find there to co-design the protocol.

Want help sourcing or building this? Talk to us via www.gongbans.com.
