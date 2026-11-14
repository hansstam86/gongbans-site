# NFC Voice Labels — Founder Start Pack

> A pen-sized reader and a pack of washable NFC stickers: record a voice note onto any tin, folder or medicine box and hear it back with a tap — for blind and visually impaired users and people with memory loss.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Which tin is beans, which box is the morning pills, which folder is the tax file? Blind and partially sighted people (30 M in wider Europe, 90% over 60) label with braille, rubber bands and memory. The one established talking-label pen costs ~£108 and locks you into its own labels.
- **Customer:** Blind and partially sighted people and their support organisations, care homes and dementia-care services in the EU. Organisations and councils buy in bulk; families buy single pens; the user taps.
- **Product:** a one-button tactile pen (record/play, nothing else), a loud speaker, 1,000 notes on board, USB-C, and packs of washable/freezer-safe NFC stickers that cost cents. €89 incl. VAT; tag packs from €9.90.
- **Why now:** NFC reader, recorder and audio-player circuits are catalogue parts; NTAG-class stickers are a commodity; the incumbent's price and proprietary labels are the opening.
- **The ask:** ~€55k to the first 1,000 pens; bulk pre-orders from 3 support organisations fund half.

## 2. Business plan

### Problem & customer
The use case is proven — the incumbent has sold this product for 15 years through sight-loss charities — but at £90–108 plus proprietary labels it's bought once, with charity help, and the labels run out. Beyond sight loss, the same pen helps people with early-stage memory loss ("this is your Tuesday box"), people who can't read the local language, and care staff who need a resident's drawer labelled in the resident's own voice.

Who pays: sight-loss organisations and their shops (they resell to members, often VAT-exempt as a disability aid), municipal assistive-technology budgets (NL/Nordics), care-home groups (10–50 pens per group), families (B2C online). Who uses: the person, often with limited dexterity — one big button, strong tactile cues, loud playback.

### Market size (estimates — check them)
- **TAM:** 30 M blind/partially sighted in wider Europe (EBU; ~26 M in the WHO 2010 baseline) + 9 M people with dementia in the EU27 (Alzheimer Europe, 2025). If 3% ever buy a voice labeller at €89 → **~€100 M** one-off, plus label packs (~€20/year).
- **SAM:** reachable through sight-loss organisation shops and assistive-tech dealers in DE/UK/NL/FR/Nordics plus care-home groups: ~10% of TAM → **~€10 M** plus consumables.
- **SOM (3 years):** 15,000 pens + 60,000 tag packs ≈ **€1.6 M revenue**.

### Competition (1 search)
| Alternative | Price (est.) | Weakness |
|---|---|---|
| PenFriend 3 (incumbent talking labeller) | ~£108 (£90 ex-VAT) + proprietary labels | Price, labels, 2010 design |
| Talking tin lids / recordable buttons | £5–10 each | One message per device, bulky |
| Smartphone + NFC tags + an app | €0 + tags | Needs a smartphone, eyesight for the app, and both hands |
| Braille labeller (Dymo-style) | €20–40 | Only 10–20% of blind people read braille fluently |
| Do nothing — rubber bands, memory, a sighted helper | €0 | Dependence |

**Wedge:** half the price, commodity stickers (any NTAG-class sticker works, we sell nice washable ones), louder, one button, and a typed-label path for carers (type text on a PC, drop it on the pen, it speaks it).

### Product & value proposition
- **Pen:** 150 × 25 mm, one large concave button (press = play, hold = record), tactile ring, 1 W speaker, mic, 3.5 mm jack, USB-C charge/data, Li-ion 500 mAh (weeks of use), vibration confirm, mass-storage mode (notes as files).
- **Tags:** NTAG-class 13.56 MHz stickers, 25 mm round and 20 × 40 mm, washable/freezer-safe laminate, tactile dot, packs of 30/100; magnets and clip tags for clothes.
- **Carer path (v1, no radio):** connect by USB-C, drop a text file per tag → the PC tool generates speech (offline TTS) → the pen stores it. **Later:** phone app over BLE (adds RED cyber work).
- **Pricing:** **€89 incl. VAT** (VAT-exempt for eligible buyers where national rules allow); organisation price €59 ex-VAT at 50+; tag packs €9.90/30 and €24.90/100; care-home starter (5 pens + 300 tags) €349 ex-VAT.

### Unit economics (estimates, per pen)
| Item | 1,000 units | 5,000 units |
|---|---|---|
| Electronics BOM (ESP32-S3 €3, NFC reader IC + antenna €3, codec/amp €1.5, mic, speaker, flash, PCB) | €15 | €12 |
| Li-ion 500 mAh (UN 38.3) + charger | €2.20 | €1.80 |
| Assembly & test (read a tag, record/play, audio level) | €4.50 | €3 |
| Enclosure (2-part ABS + TPU button, lanyard) | €3.50 | €2.20 |
| Packaging + 30 tags + tactile quick-start | €3.50 | €2.50 |
| Freight + duty to EU | €1.50 | €0.80 |
| Certification amortised (€20k RED/EMC/UN38.3) | €20 | €4 |
| **Landed cost** | **€50.20** | **€26.30** |
| Sell price ex-VAT direct (from €89 incl.) | €75 | €75 |
| Organisation/bulk price | €59 | €59 |
| **Gross margin direct** | **33%** | **65%** |
| **Gross margin bulk** | 15% | 55% |

At 1,000 units the certification load makes bulk pricing thin — so year-1 bulk deals should be at €69 or in exchange for a case study, and tags (70%+ margin) carry the relationship.

### Go-to-market
**First 100 customers:** 3 sight-loss organisations' assistive-technology teams (offer 10 pens each for a 4-week trial with a feedback sheet), 2 dementia-care providers (activity coordinators), the online low-vision communities and forums, a radio spot on the sight-loss community stations/podcasts (your users don't watch YouTube), the accessible-technology fairs.

**Scale:** sight-loss organisation shops (they are the Amazon of this market), assistive-tech dealers and national assistive-device databases, care-home group procurement, pharmacies for the "medicine box" use, Amazon with an accessible listing, FR/IT/ES organisations with localised TTS.

### 12-month plan
- **Q1:** 15 prototypes from Unit NFC + Grove recorder + ESP32, 3 organisations trial 10 pens each for a month. Gate: at least one bulk order (≥50) at €79/€59.
- **Q2:** Own PCB, enclosure tool, RED/EMC/UN38.3, PC tool with offline TTS, 500 pens + 20,000 tags.
- **Q3:** Organisation shop listings in 3 countries, care-home starter kit, 1,500 pens.
- **Q4:** BLE app decision (with EN 18031 budget), pharmacies pilot, clothing clip tags.

**Team:** embedded/audio engineer (full-time 6 months), industrial designer for 8 weeks (tactile UX is the product), a part-time accessibility consultant who is a user, founder on sales and sourcing, a contractor for the PC tool.

**Funding to 1,000 pens (estimate):** NRE €25k (PCB, enclosure tool €10k, PC tool, audio tuning) + certification €20k + 1,000 × €30 production + tags €5k = €35k → **~€80k**; organisation pre-orders ~€25k → cash need **~€55k**. Route: pre-orders + disability-innovation grants (several EU countries and the EU accessibility programmes fund exactly this) + an angel from the sight-loss community if you want speed.

### Top risks
- **Technical — audio and NFC in a pen:** a 1 W speaker in a 25 mm tube is quiet; NFC read range with a small antenna is 1–2 cm (fine — tapping is the UX). Mitigation: ported enclosure, ADPCM at 16 kHz for clarity, antenna in the tip.
- **Market — the incumbent's channel loyalty:** organisation shops have sold one product for 15 years. Mitigation: price, commodity tags, trials with their AT teams, a VAT-exempt path.
- **Regulatory:** RED for NFC (EN 300 330) + EMC + EN 62368-1; Li-ion UN 38.3 + Battery Regulation; keep v1 free of BLE/WiFi so EN 18031 doesn't apply; CRA still applies (firmware with updates by USB). **No medical claims** — "memory aid" is fine, "dementia treatment" is not. GDPR: voice notes are personal data but stay on the device; the PC tool must not upload anything.
- **Supply:** NFC reader IC families have had long lead times; mitigation: two reader footprints or a pin-compatible pair; tags from two converters.
- **Licence:** M5Stack units are modules (no electronics files) — you design your own PCB anyway; the Grove recorder schematic is the reference — check its licence.

## 3. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [m5stack-unit-nfc](https://www.gongbans.com/db/m5stack-unit-nfc.html) | NFC reader/writer for prototypes | enclosure/structure only | Module |
| [m5stack-unit-rfid2](https://www.gongbans.com/db/m5stack-unit-rfid2.html) | Alternative 13.56 MHz reader for prototypes | enclosure/structure only | Module |
| [seeed-grove-recorder-v3-0](https://www.gongbans.com/db/seeed-grove-recorder-v3-0.html) | Voice recording reference circuit | schematic | Seeed wiki — check licence |
| [m5stack-unit-audioplayer](https://www.gongbans.com/db/m5stack-unit-audioplayer.html) | Playback reference for prototypes | enclosure/structure only | Module |

### Block diagram and engineering gap
```
[NFC antenna in tip] -> [13.56 MHz reader IC] -> ESP32-S3 <- [MEMS mic] 
                                                    |-> [I2S codec/amp] -> [1 W speaker] / 3.5 mm jack
                                                    |-> [flash 128 MB: notes keyed by tag UID]
[1 big button, vibration motor, LED] ; [Li-ion 500 mAh + charger] ; USB-C (charge + mass storage)
```
Gap: the pen mechanics and tactile UX, audio loudness in a small tube, the file/UID scheme (notes keyed by UID so any sticker works), the offline-TTS PC tool, and battery life.

### Starter BOM (per pen, estimates)
| Part | Est. cost | Note |
|---|---|---|
| ESP32-S3 module (certified, with PSRAM) | €3.00 | — |
| NFC reader IC (PN532/ST25R-class) + matching network + antenna | €3.00 | Lead times vary; dual footprint |
| I2S codec + 1 W class-D amp | €1.50 | — |
| MEMS microphone | €0.40 | — |
| 20 mm speaker 1 W | €0.80 | Audio tuning needed |
| 128 MB NAND/NOR flash | €1.20 | — |
| Li-ion 500 mAh + charger IC | €2.20 | UN 38.3 report mandatory |
| PCB (long, narrow) + assembly | €4.00 | — |
| ABS tube + TPU button + lanyard | €3.50 | Tool €10k |
| NTAG-class stickers, laminated (per 30) | €2.50 | Two converters |

### Firmware/software starting point
- ESP-IDF with its I2S and USB MSC (mass storage) components; ADPCM/Opus encoding libraries exist for ESP32 — search "esp-adf" (Espressif's audio framework, exists) for codecs and the audio pipeline. NFC: driver libraries for PN532 exist in Arduino/ESP-IDF ecosystems.
- PC tool: a small desktop app using an offline TTS engine — search for current open-source offline TTS (several exist; pick one with EU languages and a permissive licence).

### 12-week build plan
- **Week 1–2 — validate.** ESP32-S3 devkit + Unit NFC + Grove recorder + a speaker in a 3D-printed tube; 10 pens; hand them to 3 organisations' AT teams. *Exit:* users record and play unaided within 5 minutes; one organisation asks for a bulk quote.
- **Week 3–5 — works-like.** Own PCB, USB mass storage of notes, button/vibration UX, loudness test. *Exit:* 30 users, 2 weeks, ≥80% "would keep it".
- **Week 6–8 — looks-like + EVT.** Enclosure in final geometry, tags laminated, PC tool alpha with TTS. *Exit:* a carer types 20 labels and the pen speaks them.
- **Week 9–10 — DVT + pre-compliance.** Tool, RED pre-scan (NFC field strength EN 300 330), battery tests. *Exit:* pass; 3 weeks' battery at 50 plays/day.
- **Week 11–12 — pilot batch.** 100 pens + 3,000 tags to the three organisations and 30 families. *Exit:* bulk order ≥50 at €59–69; <5% returns.

### Certification checklist (EU)
- **RED:** EN 300 330 (13.56 MHz inductive), EN 301 489-1/-3, EN 62368-1; if BLE added later: EN 300 328 and **EN 18031**. Est. **€10–18k** for v1.
- **RoHS, WEEE, REACH** (TPU button, laminate adhesives).
- **Battery Regulation** + **UN 38.3** for the Li-ion cell; removability info in the manual.
- **CRA:** firmware updatable via USB → SBOM, vulnerability contact, update notes.
- **GDPR:** voice notes on-device only; PC tool offline; privacy notice anyway. **No medical claims.** Not a toy. Accessibility: EU Accessibility Act applies to some consumer electronics — the product is accessible by design; keep the manual in large print and audio.

### Validation toolkit
- **Kill question:** do 3 sight-loss organisations trial 10 pens for a month and place a bulk order at €79 (or €59 ex-VAT)? **Cheapest experiment:** €600 — 10 devkit pens in printed tubes, 300 stickers, three emails to AT teams.
- **5-question interview:** (1) How do you label food, medicines and documents today? (2) What's wrong with the talking pen you know — price, labels, loudness, size? (3) Who would buy it for you — you, a charity, the council? (4) Would a carer typing labels on a computer be useful? (5) Which 20 things would you label first?
- **Landing-page headline:** "Tap it. Hear it. Label anything in your own voice." Bullets: One button, loud speaker, 1,000 notes · Washable, freezer-safe stickers from €9.90 — no proprietary labels · €89, half the price of the old pen.
- **Pre-order pass:** one organisation order of ≥50 pens or 150 family pre-orders in 6 weeks.

### First production checklist
Speaker and NFC IC samples with loudness/read-range measurements, golden sample with a reference set of tags, DFM review on the tube (button travel, speaker port, antenna clearance from the battery), MOQ 500 pens + 50,000 tags with a 2,000/200,000 forecast, QC/AQL Level II + 100% record/play/read test and audio level check, drop test, FOB Shenzhen air for 500, EU importer, battery labels, tactile quick-start in the box.

## 4. Next steps (this week)
1. Order an ESP32-S3 devkit, Unit NFC, the Grove recorder, a 20 mm speaker and 100 NTAG stickers; print a tube; get record/play working.
2. Email the assistive-technology teams of three sight-loss organisations and one dementia-care provider and offer a 10-pen trial.
3. Ask a lab for an EN 300 330 + EN 62368-1 quote and a cell supplier for a UN 38.3 report.

Want help sourcing or building this? Talk to us via www.gongbans.com.
