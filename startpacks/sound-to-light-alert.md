# Sound-to-Light Alert Kit — Founder Start Pack

> Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** A deaf or hard-of-hearing person misses the doorbell, the smoke alarm and the baby. Specialist alerting systems cost €200–600 per setup (a flash receiver alone lists around $250, a vibrating pager ~$240 — [adcohearing](https://adcohearing.com/products/bellman-pager-receiver-be1230-charging-bay-bundle)), need a transmitter wired to each source, and reimbursement is a fight ([German case law on Lichtsignalanlagen](https://www.rechtslupe.de/sozialrecht/lichtsignalanlage-und-gehoerlosennotruf-39393)).
- **Customer:** Deaf and hard-of-hearing people and their families in DE/UK/NL/Nordics; hearing-aid shops, deaf associations and social-care budgets as channels. The household (or a care budget) pays; the person and their partner use it.
- **Product:** A €149 three-piece kit: two plug-in "listeners" that classify sounds on-device (doorbell, smoke alarm, baby cry, oven timer — and you can record your own), and a bedside pad with a bright flash and a strong vibration, battery-backed; colour-coded flashes per event; mesh between rooms. No wiring to the doorbell, no cloud.
- **Why now:** On-device sound classification on an ESP32-class chip is routine; Thread/Zigbee low-power radios are cheap; the incumbents still sell 433 MHz transmitters per source; EU accessibility pressure is rising.
- **The ask:** ~€95k (estimate) to the first 1,000 kits; route = association trials + member pre-orders + bootstrap; hearing-aid shop channel for scale.

## 2. Business plan

### Problem & customer
Hearing-impaired households today: a flashing doorbell wired by an electrician, a smoke alarm with a strobe (expensive, often not fitted), a baby monitor with vibration, and a "visit"-type system that needs a transmitter per source — €600+ for a full house. Insurers sometimes pay for one item after a doctor's prescription and an appeal; many people just don't bother and rely on a hearing partner.

Who pays vs who uses: the household pays (B2C, often with support from a partner or adult child); in some countries a care budget or statutory insurer pays after prescription (DE Hilfsmittel route for "Lichtsignalanlage" — slow but real); hearing-aid shops resell; deaf associations recommend. The user is the deaf person; the partner sets it up.

Positioning: a **convenience alert**, not a safety-critical device and not a smoke alarm. The smoke alarm stays the smoke alarm; we notice it going off.

### Market size (estimates)
- WHO-class estimates put disabling hearing loss at roughly 5% of the population; in EU + UK (~520 M) that's ~25 M, of whom profoundly deaf or severe ~3–4 M. Households that would buy an alert kit: estimate **4 M** (severe + part of moderate-to-severe living alone or with a hearing partner who travels).
- **TAM:** 4 M × €149 ≈ **€600 M** (ceiling).
- **SAM:** the 4 target countries, households reachable via associations and hearing-aid shops — ~1.2 M → **€180 M**.
- **SOM (3 years):** 1% of SAM → 12k kits → **€1.8 M**, plus extra listeners/pads (~20%).

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Specialist alerting systems (Bellman Visit-class; flash receiver ~$250, pager ~$240, bundles higher — [adcohearing](https://adcohearing.com/products/bellman-pager-receiver-be1230-charging-bay-bundle), [Connevans bundles](https://www.connevans.co.uk/catalogue/271/Bellman-Visit-Pager-System-bundles)) | Reliable, dealer network, decades of trust | Price per source, transmitter wiring, 433 MHz, no learning |
| Smart-home DIY (smart doorbell + smart bulb + phone notifications) | Cheap-ish, popular with younger users | Phone-dependent, cloud, no bedside vibration, no smoke-alarm recognition |
| Phone sound-recognition features (iOS/Android) | Free | Phone must be awake and nearby; no bedside pad; no multi-room |
| Vibrating alarm clocks + strobe smoke alarms (separate products) | Reimbursable in places | Not integrated; still miss the doorbell |
| Nothing / relying on a hearing partner ("do nothing") | The majority | Fails when the partner is out |

**Wedge:** no wiring and no transmitters — listeners recognise existing sounds; trainable (record your own doorbell); one bedside pad for everything; mesh between rooms; a third of the price; hearing-aid shops can demo it in 2 minutes.

### Product & value proposition
Hardware: **Listener** — wall-plug (USB-C or integrated plug) puck with a MEMS mic, ESP32-S3-class MCU for on-device classification, Thread/Zigbee (ESP32-H2-class) or BLE mesh to the pad, LED ring for local flash, battery backup for 24 h. **Pad** — bedside unit with a high-brightness multi-colour flash, a strong vibration motor (under-pillow disc option), a big dismiss button, 3-colour event legend, Li-ion backup, USB-C. **Portable pager** (later SKU) — wrist/pocket vibrator. Software: on-device models for doorbell/smoke-alarm/baby-cry/oven-timer/knock; "teach" mode (play your doorbell 5×); per-event colour and vibration pattern; mesh pairing by button; optional phone notification via a local bridge (not required). Privacy: no audio leaves the device, ever — that's a feature on the box.

Pricing (estimates): **€149 kit** (2 listeners + pad), extra listener €49, pager €59, €199 "house" kit (4 listeners + pad + pager). Hearing-aid shops at 35% off; association member price €129.

### Unit economics (estimates per 3-piece kit, ex-VAT)
| Item | 1k kits | 5k kits |
|---|---|---|
| Electronics BOM (2× listener: ESP32-S3 + H2-class radio + mic + LED ring + backup cell ≈ €9 each; pad: MCU + radio + high-power LEDs + vibration motor + Li-ion + charger ≈ €12) | €30.00 | €24.00 |
| Assembly & test (SMT ×3, mic sensitivity test, radio pairing test, flash/vibration test) | €6.00 | €4.20 |
| Enclosures (3 pieces; plug housing, diffuser, pad; tooling amortised) | €7.50 | €4.80 |
| Packaging (box, cables, quick card in large print) | €3.00 | €2.20 |
| Freight + duty to EU (Li-ion) | €3.50 | €2.20 |
| Certification amortised (~€40k: RED incl. Thread/BLE, EMC, safety, UN 38.3, EN 18031) | €40.00 | €8.00 |
| **Landed cost** | **€90.00** | **€45.40** |
| Sell price (direct €149 / shop €97) | €149 | €97 |
| **Gross margin** | **€59 (40%)** | **€51.60 (53% at shop price)** |

Tight at 1k because of certification across three radios/devices — keep to one radio family (Thread on H2-class for all three) and certify the kit as a system. Extra listeners and pagers carry better margin.

### Go-to-market
**First 100 customers:** 3 deaf/hard-of-hearing associations test kits for a month and recommend (kill question); 50 member pre-orders at €149; hearing-aid shops in 2 cities (demo kit on the counter); parents' groups of deaf parents (baby cry is the hook); accessibility bloggers and sign-language YouTube channels (make the video with captions and signing).

**Scale channels:** hearing-aid chains and independents (demo + commission), associations' shops and newsletters, social-care equipment suppliers (the catalogues occupational therapists order from), the Hilfsmittel/assistive-tech route in DE (slow; start the paperwork after 500 units), online marketplaces with accessibility categories.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like (Grove sound sensor → S3 dev kit; H2 dev kits for mesh; Vibrator unit in a pad mock-up); 3 association trials; 50 pre-orders. |
| Q2 | Own listener + pad PCBs, housings, trainable models; EVT 50 kits; pre-compliance; shop demos. |
| Q3 | DVT, certification, 300-kit pilot; hearing-aid chain pilot in one country; pager EVT. |
| Q4 | 1,000 kits; second country; Hilfsmittel application started; local bridge for phone notifications. |

**Team:** 1 embedded ML engineer (classification, mic front-end — full-time), 1 embedded/radio engineer (Thread mesh, power, pad — full-time), an industrial designer (contract) because the pad must look like a bedside object, founder for associations and shops; an accessibility consultant who is deaf or hard-of-hearing on contract — non-negotiable. Three to four people.

**Funding to first 1,000 kits (estimates):** NRE €65k (PCBs €14k, tooling 3 housings €24k, ML + firmware €20k, design €7k) + certification €40k + 1,000 kits landed ~€50k + 9 months overhead €75k ≈ **€230k**; minus pre-orders (50 × €149 ≈ €7k), pilot sales (300 × €139 ≈ €42k), shop channel prepayment (~€25k), and accessibility/inclusion grants (commonly €30–60k in this field) ≈ **~€95k**. Bootstrap + grants + pre-orders; an angel with an accessibility thesis is plausible here.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** false negatives (missed smoke alarm) and false positives (TV doorbell) | Smoke-alarm class = 3 kHz-class T3 pattern, high recall; "teach" mode for your own doorbell; TV filter via duration/repetition; publish test results per class; never claim safety |
| **Regulatory/liability:** being seen as a smoke-alarm accessory → EN 14604 territory | Wording "convenience alert — does not replace a smoke alarm"; the pad never silences anything; legal review of packaging |
| **Technical:** mic always on → privacy fear | On-device only, no audio stored or sent, no WiFi needed; say it on the box; lab-verifiable |
| **Market:** incumbents have the dealer trust and reimbursement codes | Start B2C and associations; add dealers with a demo kit and commission; apply for Hilfsmittel codes later |
| **Regulatory:** three radio devices → RED + EN 18031 + CRA, Li-ion in all three | One radio family, kit certified as a system; local-only networking narrows EN 18031 scope; removable cells |
| **Supply:** high-brightness LEDs and vibration motors | Multi-source; LED array instead of a single xenon-class strobe |
| **Licence:** Seeed/Espressif references | Seeed wiki files and Espressif dev-kit files are references; your own boards |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Seeed Grove Sound Sensor | https://www.gongbans.com/db/seeed-grove-sound-sensor.html | Microphone/sound-level front-end for the works-like | schematic | Seeed wiki resources; check licence |
| M5Stack Unit Vibrator (U059) | https://www.gongbans.com/db/m5stack-unit-vibrator.html | Bedside vibration pad reference | enclosure/structure only; electronics not published | Buy; motor driver reference |
| Seeed Grove Haptic Motor | https://www.gongbans.com/db/seeed-grove-haptic-motor.html | Haptic driver reference for the wrist/pad variant | schematic | Seeed wiki resources; check licence |
| Espressif ESP32-H2-DevKitM-1 | https://www.gongbans.com/db/espressif-esp32-h2-devkitm-1.html | Thread/Zigbee low-power radio nodes (official dev kit; reference files from Espressif) | reference design files (dev kit) | Espressif terms; module for production |

**Board-fact note:** the works-like uses an analogue sound sensor; the product needs a digital MEMS mic (I2S/PDM) for classification. The pad's high-power flash is your own design.

### Block diagram
```
LISTENER (x2):  [MEMS mic I2S] -> [ESP32-S3-class: feature extraction + classifier] -> event
                     |-> [ESP32-H2-class Thread radio]  [LED ring local flash]  [USB-C/plug + 24 h backup cell]
                                   |
                              Thread mesh (local, no internet)
                                   |
PAD:            [ESP32-H2-class] -> [high-power RGB LED array flash] [vibration motor + under-pillow disc]
                     |-> [big dismiss button] [3-colour legend] [Li-ion + charger, USB-C]
OPTIONAL BRIDGE: [Thread border router -> phone notification]  (not required for the kit to work)
```
**Engineering gap:** the classifier (data collection across European doorbells and smoke alarms, on-device inference, recall targets), the "teach" mode UX for non-technical users, the pad's industrial design and flash brightness vs eye comfort, mesh pairing without a phone, and battery backup behaviour. Radios and motors are off-the-shelf.

### Starter BOM (estimates per kit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| 2× ESP32-S3 module (classification) | €5.20 | Pre-certified; or a single S3 with Thread via H2 co-module |
| 3× ESP32-H2-class module (Thread) | €6.60 | Pre-certified; one radio family across the kit |
| 2× MEMS mic I2S | €1.60 | Multi-source |
| 2× LED ring + drivers | €2.00 | |
| Pad: high-power RGB LED array + driver | €3.50 | Multi-source; diffuser matters |
| Pad: vibration motor + under-pillow disc | €3.00 | Multi-source |
| 3× Li-ion backup cells + chargers + gauges | €6.00 | UN 38.3; removable |
| 3× PCB + passives + USB-C | €5.50 | |
| 3 housings (2 plug pucks + pad) | €7.50 | **Tooling €20–26k** |

### Firmware/software starting point
- **ESP-IDF** with **OpenThread** (Espressif supports Thread on ESP32-H2/C6 in ESP-IDF; exists).
- Classification: **Edge Impulse** (exists) for data collection and model export to ESP32; or **TensorFlow Lite Micro** via Espressif's esp-tflite-micro (exists); Google's **YAMNet** (exists) as a feature/label reference, too big to run as-is — distil.
- Espressif's **ESP-SR** (exists) is for speech; useful for the audio front-end, not the classes.
- Data: record 200+ European doorbells, 30 smoke-alarm models, baby cries (consented), ovens; build the test set first.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 5 works-like kits (Grove sound sensor + S3 dev kit listeners, H2 dev kits for mesh, Vibrator unit in a pad mock-up); **3 associations agree to a one-month trial; 50 members pre-order at €149 after a captioned/signed video** (runs to W8) |
| 3–5 | Works-like | Classifier: ≥ 95% recall on smoke-alarm patterns and ≥ 90% on 20 doorbells in a test flat, ≤ 1 false alert per day with TV on; mesh across 3 rooms; teach mode works for 5 testers |
| 6–8 | Looks-like + EVT | Own listener + pad PCBs, housings T1; 50 kits; 24 h backup verified; RF pre-scan; 10 deaf/hard-of-hearing testers set up a kit unaided |
| 9–10 | DVT + pre-compliance | RED/EMC/safety pre-compliance as a system; EN 18031 self-assessment (local-only); UN 38.3; photosensitivity review of the flash pattern; legal review of claims |
| 11–12 | Pilot batch | 50 kits to trial members + 2 hearing-aid shops; ≥ 80% still installed after 4 weeks; ≥ 1 association recommends in writing |

### Certification checklist (EU)
- **CE under RED** (Thread 2.4 GHz + any BLE): EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** for all three devices (plug-in housing → pin and insulation requirements if the plug is integrated — using a certified USB-C adapter is simpler); **EN 18031-1** applies if any part can reach the internet — a local-only Thread mesh with no border router keeps the scope narrow; if you ship the optional bridge, -1 and -2 apply to it. Est. €10–15k RED/EMC (3 devices, one family), €5–8k safety, €0–15k EN 18031 depending on the bridge.
- **Battery:** UN 38.3 for the cells; **EU Battery Regulation** labelling and removability by 18 Feb 2027.
- **RoHS, REACH, WEEE**, packaging registration.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware, update via the bridge or USB, SBOM, vulnerability contact.
- **GDPR:** a microphone in the home — on-device processing only, no audio stored or transmitted; state it in a privacy notice; "teach" recordings stay on-device.
- **Not a smoke alarm (EN 14604), not a medical device (MDR) — an assistive convenience product.** Have a lawyer check the box copy. **Toy directive:** no.
- **Photosensitive epilepsy:** keep flash rates outside 3–60 Hz risk ranges (single or ≤ 2 Hz pulses) — document it.
- **Total certification budget estimate: €25–40k.**

### Validation toolkit
- **Kill question:** Do 3 deaf associations test a kit for a month and recommend it to members; do 50 members pre-order at €149?
- **Cheapest experiment (~€900):** 5 works-like kits from catalogue parts, a 90-second captioned and signed video of a doorbell → pad flash and a smoke-alarm test → red flash + vibration; offer trials to 3 associations and a €30 deposit pre-order to members.
- **5-question interview (deaf/hard-of-hearing person, ideally in their preferred language with an interpreter):** 1) Which sounds do you miss at home, and what happened last time? 2) What alerting equipment do you have, who paid, and how long did it take? 3) Would you trust a device that *listens* for the doorbell rather than being wired to it? 4) Where would the pad live, and what should it do at night? 5) €149 for two listeners and a pad, no wiring — pre-order, and what would you need to see first?
- **Landing page:** headline "Your home's sounds, as light and vibration. No wiring." Bullets: "Two listeners recognise the doorbell, smoke alarm, baby and timer — or teach them your own sounds." / "A bedside pad flashes in colour and vibrates under the pillow; battery backup; works without internet." / "€149 for the kit. Nothing you say ever leaves the device."
- **Pass threshold:** 50 pre-orders with deposit plus one association's recommendation, or 150 deposits in 8 weeks.

### First production checklist
- Samples: 5 golden kits with mic sensitivity records, classifier test results, flash luminance and vibration amplitude measurements.
- DFM: mic port acoustic path and dust mesh, LED diffuser uniformity, pad button feel, pillow-disc cable strain, cell doors.
- MOQ talk: modules 3k (one family), mics 2k, LEDs reel, motors 1k, cells 3k with UN 38.3, housings 1k each.
- QC: AQL II 2.5/4.0; 100% mic test with a tone + pairing test + flash/vibration test; 5% 24 h backup test; sample classifier test with recorded doorbells.
- Packaging: UN 3481 marking; large-print quick card; visual (not audio) setup instructions; no "smoke alarm" wording on the box.
- Incoterms: FOB Shenzhen; air (DG) for 50; sea for 1,000.

## 4. Next steps (this week)
1. Order 2× Grove Sound Sensor, 2× ESP32-S3 dev kits, 3× ESP32-H2-DevKitM-1, a Unit Vibrator and a high-power LED; record 20 doorbells and 5 smoke alarms as your first dataset.
2. Write to 3 deaf/hard-of-hearing associations proposing a one-month trial (offer the kits free, ask only for feedback) — and hire a deaf or hard-of-hearing consultant for the project.
3. Train a first doorbell/smoke-alarm classifier on the dev kit and film the pad flashing; caption and sign the video.

Want help sourcing or building this? Talk to us via www.gongbans.com.
