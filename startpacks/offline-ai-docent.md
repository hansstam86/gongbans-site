# Offline AI Docent — Founder Start Pack

> A tabletop voice kiosk for museums and visitor centres that answers questions about the exhibition from a curated local knowledge base — fully offline, no cloud, no visitor data.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Visitors ask "where is the toilet", "why is this painting here" and "what did this machine do" — and the one guide is busy. Cloud chatbots exist (Ask Mona-style deployments in France and elsewhere), but a public institution putting visitors' voices into a US cloud triggers GDPR, procurement and AI-Act conversations that take longer than the exhibition runs.
- **Customer:** Small and mid-size museums, visitor centres, science centres, company showrooms and libraries in the EU. The curator or head of visitor experience wants it; the director and the data-protection officer approve it; the budget is "exhibition technology", usually €1,500–5,000 per interactive.
- **Product:** A kiosk the size of a table lamp: far-field microphones, a speaker, a touch display for text fallback and admin, and an edge-LLM compute module (AX630C-class NPU, 3.2 TOPS INT8) running a small language model with strict retrieval over the curator's PDFs and labels. Wake word, multilingual, answers with the source shown. Nothing recorded, nothing uploaded. €1,499–2,499 per kiosk (estimates) plus optional content-service.
- **Why now:** Edge LLM modules at €70–90 run 0.5–1.5B-parameter models (Qwen2.5-0.5B/1.5B, Llama3.2-1B listed by the module maker) with Whisper speech recognition and local TTS; retrieval-only prompting makes a small model usable for a bounded exhibition; the AI Act and GDPR make "offline" the easiest compliance story.
- **The ask:** ~€120k to the first 100 kiosks (a €2,000 product does not need 1,000 units to be a business; the 1,000-unit math is shown for reference); one paid museum pilot first.

## 2. Business plan

### Problem & customer

A museum has three kinds of questions: logistics (toilets, café, opening hours), orientation (where is X, what's on this floor) and content (why, how, who). Staff answer the first two 200 times a day; the third goes unanswered unless a guide is nearby. Audio guides answer pre-recorded content, not questions. Cloud chatbots answer everything — including things that aren't true about your collection — and require a data-protection assessment the DPO doesn't want to write.

- **Who pays:** the museum (exhibition budget, digital-strategy budget), often with regional culture funding; visitor centres (municipal, nature parks); company showrooms (marketing budget — the least price-sensitive).
- **Who uses:** visitors of all ages, in several languages, for 30 seconds each; the curator who maintains the knowledge base (must take an afternoon, not a project).
- **Who approves:** the DPO (offline = short conversation) and the director (AI Act transparency notice = one sticker and a paragraph).

### Market size (estimates — check)

- **TAM:** EU museums ≈ 30k (EGMUS-type counts), visitor and science centres ≈ 5k, company showrooms and libraries with exhibitions ≈ 20k. At 1.5 kiosks per site, €2,000 → **€165M** theoretical; refresh every 5 years; content-service €300–600/year.
- **SAM:** institutions with >20k visitors/year and an exhibition-technology budget in DE/NL/FR/AT/CH/Nordics/BE ≈ 8k → **€24M**.
- **SOM (3 years):** 400–700 kiosks → **€0.8–1.4M** + services. Year 1: 60–100.

Sources used: M5Stack LLM630 Compute Kit specifications and price (AX630C, 3.2 TOPS INT8 / 12.8 TOPS INT4, 4 GB LPDDR4, listed models; ~$70 / €90 retail), Ask Mona and other vendors' museum case studies (cloud, no public pricing), an offline-first museum character deployment in Montreal. Museum counts: EGMUS/national statistics — verify.

### Competition (2 searches)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing — staff, signage, printed guide | labour | Staff answer logistics all day; content questions go unanswered |
| Audio guides / app guides (Nubart, Orpheo-class, custom apps) | €2–5k setup + per-device | One-way; no questions; app download friction |
| Cloud conversational guides (Ask Mona and peers; GPT-based pilots) | project pricing, subscription | Strong content UX; cloud processing of visitor voice/text → DPIA, transfer questions, hallucination risk beyond your collection |
| Touchscreen kiosks with menus (Intuiface-class) | €3–8k per kiosk | No free-form questions; content authoring is a project |
| Tablet with a generic voice assistant | €300 | Not your content, not controllable, cloud |
| DIY: Raspberry Pi + an open LLM | €150 + months | Latency, no enclosure, no admin UI, nobody maintains it |

**Wedge:** the only question-answering kiosk that is provably offline (unplug the network — it still works), answers only from the curator's documents with the source shown, needs no app, and gives the DPO and the AI Act officer a one-page file.

### Product & value proposition

- Hardware: edge-LLM compute module (AX630C-class, 4 GB, eMMC) + a 4-mic far-field front end (ESP32-S3-class audio board handling wake word, AEC and beamforming) + a 5" touch display (text input, text answer, admin) + 5 W speaker + Ethernet/WiFi (admin only; can be physically disconnected) + optional presence sensor to wake the display.
- Software: wake word ("Hello, Museum" in several languages), Whisper-class ASR on device, retrieval over the curator's knowledge base (PDFs, label texts, FAQ) with a small LLM allowed to answer only from retrieved passages, source citation on screen, local TTS, "I don't know — ask staff at the desk" when retrieval is thin. Admin: drag-and-drop documents, test questions, usage counters (question topics, languages; no audio, no text stored unless the curator enables anonymised logging).
- Housing: powder-coated steel/aluminium lamp-like body, tamper-proof, lockable; floor-stand and counter variants.
- **Pricing (estimates):** Kiosk €1,999 (counter) / €2,499 (floor stand, presence sensor, larger speaker); content on-boarding service €490 one-off; update/support €390/year optional; showroom edition with branding €2,999.

### Unit economics (estimates, EUR per kiosk; counter model)

| Item | 100 | 1,000 |
|---|---|---|
| Electronics BOM (edge-LLM module €75, far-field audio board ESP32-S3 + 4 MEMS mics + codec €18, 5" touch display €22, speaker + 5 W amp €6, PSU 12 V external CE €8, presence sensor €4, PCB/interconnect €10) | 143 | 118 |
| Assembly + test (acoustic test, model load, QA question set) | 35 | 18 |
| Enclosure (sheet metal + CNC, no tooling at 100; 2 tools at 1k) | 60 | 28 |
| Packaging | 10 | 6 |
| Freight + duty to EU | 18 | 9 |
| Certification amortised (€45k) | 450 | 45 |
| **Landed cost** | **716** | **224** |
| Direct sale €1,999 ex VAT, less €60 install/support allowance | 1,939 | 1,939 |
| **Gross margin direct** | **€1,223 (63%)** | **€1,715 (88%)** |
| Via exhibition integrator at €1,500 net | €784 (54%) | €1,276 (85%) |

At 100 units the certification dominates — which is why you sell the first 100 at a service-heavy price and not at €999. The real cost is software: budget 1 FTE forever.

### Go-to-market

**First customers (10–20 kiosks):** one museum pilot (the kill question) found through your own network, the regional museum association, or a science centre with a digital lab. Then the museum-tech conferences (the European museum-technology circuit), the museum associations' newsletters in DE/NL/FR, and the exhibition designers/integrators who specify interactives — they are your real channel.

**Scale:** exhibition integrators and AV companies (they install, you supply), regional culture-digitalisation funds (many fund "AI in museums" pilots — write the proposal template for your customers), company showrooms via experiential agencies, libraries via their supply resellers, visitor centres of national parks.

### 12-month plan

- **Q1:** works-like kiosk from the compute kit + far-field dev board + tablet; retrieval pipeline over one museum's PDFs; 2-week pilot; curator rates ≥80% of answers acceptable (kill question).
- **Q2:** own carrier/interconnect board, enclosure v1, admin UI, 5 kiosks in 3 institutions for 8 weeks; language set (DE/EN/FR/NL + local); pre-compliance.
- **Q3:** DVT, certification (RED, EMC, safety, EN 18031), pilot batch 20, two integrators signed, AI Act transparency pack and DPIA template.
- **Q4:** production 50–100, floor-stand SKU, content-service team, showroom edition.

**Team:** founder (museum sales, content), 1 ML/edge engineer (model quantisation for the NPU, retrieval, ASR/TTS pipeline), 1 embedded/audio engineer (far-field front end, carrier board), 1 full-stack developer (admin UI), part-time museum educator for the content-onboarding method, ID/ME contract for the housing.

**Funding to the first 100 kiosks (estimate):** NRE €40k (carrier board €8k, enclosure €12k, acoustic tuning €5k, ID €8k, test fixtures €7k) + certification €45k + 9 months salaries (3 engineers lean) €110k + 100 kiosks at ~€270 landed €27k = **€222k**, less first-year sales of ~60 kiosks and services (~€140k) → **€120k** net; by the time you reach 1,000 kiosks (≈ 4–5 years) the hardware funds itself. Route: one paid pilot (€4–6k incl. onboarding), a culture-tech or AI-Act-compliance innovation grant, an angel from the museum/AV world. Not a bootstrap — the ML work precedes revenue.

### Top risks

- **Technical — a 0.5–1.5B model is dumb.** It will paraphrase badly and hallucinate if allowed. Mitigation: retrieval-only prompting with an answer-from-passage rule, short answers, a confidence gate that defers to staff, and a curator test set of 200 questions per site; show the source on screen. Measure, don't hope.
- **Technical — far-field speech in a reverberant hall with 40 schoolchildren.** Mitigation: a 4-mic array with AEC and beamforming, a push-to-talk ring as fallback, text input on the display; test in a real museum in week 3.
- **Market — museums are slow and love pilots, hate purchase orders.** Mitigation: a fixed-price pilot that converts to purchase; sell through integrators who already have the PO relationship; grant-proposal template.
- **Regulatory — GDPR and AI Act.** Offline by design keeps GDPR simple (no storage, no transfer) but voice is personal data while processed → DPIA template anyway; AI Act: a chatbot must disclose it is AI (Article 50-type transparency) — a sticker and a spoken intro. Deepfake/emotion features: never.
- **Supply — the edge-LLM module is a single vendor with a young toolchain.** Mitigation: keep the pipeline portable (ONNX/GGUF), qualify an RK3588-class SBC as plan B (more power, more cost).
- **Reputation — one viral wrong answer in a Holocaust museum ends the company.** Mitigation: content boundaries per site, refusal behaviour, curator sign-off, and don't sell into sensitive-history exhibitions until the system has a year of track record.

## 3. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack LLM630 Compute Kit (K143) | https://www.gongbans.com/db/m5stack-llm630-compute-kit.html | Edge LLM compute kit (AX630C NPU, 4 GB, Ethernet, WiFi 6 via ESP32-C6) — runs the model, ASR and TTS | enclosure/structure files only; electronics not published | Off-the-shelf; use as bought; production = module on your carrier |
| M5Stack Module LLM (M140) | https://www.gongbans.com/db/m5stack-module-llm.html | LLM module for a stackable variant / second form factor | enclosure/structure files only | Off-the-shelf |
| Espressif esp32-s31-korvo-1 | https://www.gongbans.com/db/espressif-esp32-s31-korvo-1.html | Far-field voice front-end reference (mic array, wake word, AEC) | reference design files from Espressif (per catalogue) | Espressif reference-design terms; check |
| M5Stack Tab5 (C145) | https://www.gongbans.com/db/m5stack-tab5.html | Touch display for text fallback and the admin UI in the prototype | enclosure/structure files only | Off-the-shelf |

### Block diagram

```
[4-MEMS mic array + codec] --> [ESP32-S3 audio front end: wake word, AEC, beamforming] --I2S/USB--> |
[presence sensor] -------------------------------------------------------------------------> | [Edge-LLM module (AX630C-class, 4 GB)]
[5" touch display] <--------------------------------------------------------------------------> |   ASR (Whisper-class) -> retrieval (local index) -> small LLM (answer-from-passages) -> TTS
[speaker + 5 W amp] <-------------------------------------------------------------------------- |   admin web UI over local Ethernet (optional; removable)
[12 V external CE PSU] --> power board --> 5 V / 3.3 V rails
Nothing stored: audio buffers cleared after each turn; counters only.
```

**Engineering gap:** the end-to-end latency budget (target <3 s from end of speech to first spoken word) on a 3.2 TOPS NPU — model quantisation and pipelining; far-field performance in halls; a carrier board that puts module, audio front end, display and power on one PCB; the admin UI a curator can use; the multilingual wake word and TTS set; the AI Act/GDPR pack.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| Edge-LLM module (AX630C-class SoM, 4 GB LPDDR4, 32 GB eMMC) | €75 | Single vendor; plan B RK3588-class |
| ESP32-S3 audio module + 4 MEMS mics + codec with AEC reference | €18 | Multi-source parts; design from the Korvo reference |
| 5" IPS touch display (MIPI/HDMI/USB touch) | €22 | Multi-source |
| 5 W Class-D amp + full-range speaker | €6 | Commodity |
| Presence sensor (mmWave or ToF) | €4 | Multi-source |
| 12 V/3 A external PSU, CE | €8 | Buy certified |
| Carrier PCB + connectors | €10 | |
| Sheet-metal/CNC housing | €60 at 100; €28 at 1k with tooling | Tooling €25k later |

### Firmware/software starting point

- The module vendor's StackFlow/LLM framework and model list (search M5Stack's LLM630 / Module LLM documentation and GitHub for the current SDK) — Qwen2.5-0.5B/1.5B, Llama3.2-1B, Whisper and MeloTTS are listed as supported.
- Espressif ESP-SR (wake word, AEC, beamforming) and ESP-ADF for the audio front end; the Korvo-class examples run these out of the box.
- Retrieval: a small embedding model + a local vector store (search for lightweight options that run on ARM; FAISS-class libraries compile for Linux-on-ARM).
- Axera's Pulsar toolchain for quantising your own models to the NPU — search Axera's developer resources.
- Admin UI: any web stack served from the module over local Ethernet.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | Compute kit + Korvo-class board + tablet on a table in one museum for 2 weeks with the curator's documents loaded. Curator rates ≥80% of logged question-answer pairs acceptable; director says a €1,999 price is plausible. Below 70%: stop or move to a text-only kiosk. |
| 3–5 | Works-like | End-to-end latency <4 s median; wake word in 3 languages; retrieval-only answers with source shown; "ask staff" refusal working; far-field test in a reverberant hall at 2 m with background noise. |
| 6–8 | Looks-like + EVT | Carrier board v1, housing v1 (sheet metal), 5 kiosks in 3 institutions for 8 weeks; usage counters; curator admin UI used by a non-engineer; EMC pre-scan. |
| 9–10 | DVT + pre-compliance | Carrier v2, acoustic tuning, RED/EMC/safety pre-tests, EN 18031 checklist, AI Act transparency pack and DPIA template reviewed by a lawyer; 200-question test set ≥85% acceptable at 2 sites. |
| 11–12 | Pilot batch | 20 kiosks assembled (EU assembly is fine at this volume), golden sample with acoustic and QA records, two integrator agreements, content-onboarding SOP. |

### Certification checklist (EU)

- **CE / RED:** WiFi/BLE on the module → EN 300 328, EN 301 489-1/-17, EN 62311; EN 62368-1 safety (12 V, speaker, display). If you ship Ethernet-only and physically disable radio, RED falls away — but the module's radio is there; test it.
- **RED delegated act — EN 18031-1 (and -2: voice is personal data during processing):** applies if the radio is active and internet-connected. Keep admin on local Ethernet, radio off by default, and the -2 argument becomes short.
- **CRA:** reporting since September 2026, full December 2027; a Linux device in a public space — signed images, update policy, SBOM, disclosure.
- **GDPR:** voice processed on device and discarded → still a DPIA for the institution (you supply the template); no storage by default; anonymised topic counters only; signage.
- **EU AI Act:** transparency obligation for AI systems interacting with people (disclose it is AI — spoken intro + sticker); keep away from emotion recognition and biometric features. Minimal-risk otherwise; keep a technical file.
- **RoHS, REACH, WEEE**, packaging registration; no battery.
- **Accessibility:** public-sector buyers will ask (European Accessibility Act applies to some self-service terminals from 2025 — check applicability): text display, volume control, height for wheelchair users.
- **Estimated test costs:** RED €10k, EMC €5k, safety €4k, EN 18031-1/-2 €18–22k, legal (DPIA, AI Act pack) €5k. Budget **€45k**.

### Validation toolkit

- **Kill question:** does a 2-week pilot in one museum answer ≥80% of visitor questions acceptably per the curator — and would they pay €1,999? **Cheapest experiment:** the compute kit (~€90), a Korvo-class audio board, a tablet, a borrowed table; load the museum's PDFs; log every Q&A pair (with signage and consent); curator reviews the log. Cost < €400 and two weeks.
- **5-question interview (head of visitor experience):** 1) What are the ten questions your floor staff answer most? 2) What happened the last time you evaluated a chatbot or app guide — who stopped it and why? 3) Who maintains your label texts and in what format? 4) Would your DPO accept a device that provably never connects to the internet? 5) What budget line would a €1,999 kiosk come from, and when is it decided?
- **Landing page:** headline "A docent that answers visitors' questions — and never leaves the building." Bullets: "Runs entirely offline: unplug the network and it still works"; "Answers only from your own texts, with the source on screen"; "€1,999 per kiosk, curator-maintained in an afternoon — GDPR and AI Act file included".
- **Pass threshold:** 1 paid pilot converted to purchase + 5 institutions signing letters of intent at €1,999 within 8 weeks of the pilot report.

### First production checklist

- Samples: 1 pilot rig, 5 EVT, 20 pilot kiosks; keep 2 per revision with acoustic measurements.
- Golden sample: acoustic test (wake-word rate at 2 m in 65 dBA noise), latency, 200-question QA score, image hash — signed.
- DFM review: mic port geometry and gasket, speaker enclosure volume, display bonding, cable strain, tamper screws, thermal path for the module.
- MOQ talk: modules 100 (then 500), displays 100, sheet metal 50; tooling only after 100 sold.
- QC/AQL: 100% acoustic + QA test at this volume; AQL sampling only above 500/year.
- Packaging: single kiosk box with a printed AI-transparency sticker set and the DPIA template QR.
- Incoterms: FOB Shenzhen for the module/display kits; final assembly in the EU for the first 100.

## 4. Next steps (this week)

1. Order the LLM630 Compute Kit, a Korvo-class far-field board and a Tab5; get Whisper → retrieval → Qwen → TTS running end to end on a table, with your own 20-page PDF as the knowledge base.
2. Ask one museum or visitor centre you can reach for a 2-week table-top pilot; write the signage and the consent note first.
3. Build the 200-question evaluation set format (question, expected source, acceptable answer) — this file is your product's quality system.

Want help sourcing or building this? Talk to us via www.gongbans.com.
