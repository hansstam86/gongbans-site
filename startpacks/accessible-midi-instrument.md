# One-Switch MIDI Instrument — Founder Start Pack

> A tabletop instrument with big faders, encoders and a joystick that any single movement can play, outputting MIDI and built-in synth sound — for music therapy, special-needs schools and inclusive bands.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** A child with cerebral palsy or an adult after a stroke can move one thing — a hand an inch, a head, a knee. Making music with that movement today means either a £2,500–3,500 ultrasonic system, a discontinued squishy cube, or a therapist improvising with an iPad and tape.
- **Customer:** Music therapists, special-needs schools, inclusive-music charities and community music centres in UK/DE/NL/Nordics. Schools and charities pay from arts/inclusion budgets; therapists recommend and use; the player plays.
- **Product:** a rugged tabletop box with 4 big faders, 4 encoders with light rings, a joystick, 2 arcade buttons and 2 assistive-switch jacks; scale/chord quantisation so every gesture sounds right; built-in General-MIDI synth and speaker; USB and 5-pin MIDI out; wheelchair-tray mount. €299 incl. VAT.
- **Why now:** MIDI, synth, fader and encoder units are off-the-shelf catalogue parts; inclusive music is funded by arts councils and schools; the price gap between €300 and €3,000 is empty.
- **The ask:** ~€60k to the first 1,000 units; school/charity pre-orders fund a third.

## 2. Business plan

### Problem & customer
Music therapists and inclusive-music teachers need instruments that (a) respond to tiny or gross movements, (b) never sound wrong (quantise to a scale/chord so the player is always "in"), (c) connect to the switches and mounts they already own (3.5 mm assistive switches, wheelchair tray clamps), and (d) make sound by themselves — a laptop is one more thing to fail. The high end (Soundbeam 6: solo £2,505, group £3,525 ex-VAT) is excellent and funded by grants; the low end (Skoog 2.0 at ~US$380, discontinued at some retailers) was loved and is going away; the charity-built accessible instrument is software-first. In between there is nothing a school can buy three of.

Who pays: special-needs schools (equipment budgets, often with charity top-ups), inclusive-music charities and orchestras, music therapy practices (self-employed therapists buy their own tools), community music centres; some national health/education bodies fund assistive music tech. Who uses: therapists in sessions; players at home in the second year.

### Market size (estimates — check them)
- **TAM:** >5,500 music therapists in Europe (EMTC, 2015 — surely more now), ~1,000-class in the UK alone (HCPC registrations), plus ~15,000 special-needs schools and units in the EU/UK (estimate) and ~2,000 inclusive-music organisations. If each therapist owns one and each school two → ~40,000 units ≈ **€12 M** one-off, plus a home-player market behind it.
- **SAM:** UK/DE/NL/Nordics via therapist associations, SEN school suppliers and charities → ~40% → **~€5 M**, replacement every 5–6 years.
- **SOM (3 years):** 4,000 units ≈ **€1 M revenue**.

### Competition (1 search)
| Alternative | Price (est.) | Weakness |
|---|---|---|
| Soundbeam 6 (ultrasonic movement-to-sound) | £2,505–3,525 ex-VAT | Price, needs a trained operator; brilliant but grant-only |
| Skoog 2.0 (tactile cube, iOS/Mac) | ~US$380, discontinued at some retailers | Needs an iPad, availability uncertain |
| Clarion (charity, software, played by touch/mouse/head/eye) | low cost (price not found) | Software-first; needs a computer and setup |
| iPad apps (GarageBand, touch synths) + a stand | €0–30 + iPad | Flat glass, no tactile feedback, hard to switch-adapt |
| Switch-adapted toys/percussion | €50–200 | One sound, no musical range |
| Do nothing — tambourine | €10 | — |

**Wedge:** tactile, rugged, self-sounding, switch-ready, quantised, €299. Sell to the therapist who wants three, not the grant committee.

### Product & value proposition
- **Hardware:** 300 × 200 mm ABS/aluminium box; 4× 60 mm faders with big caps, 4 encoders with RGB rings, 1 joystick (spring return), 2× 60 mm arcade buttons, 2× 3.5 mm assistive-switch jacks (plus 1 expression-pedal jack), built-in GM synth + 3 W speaker, line out, USB-C (USB MIDI class device + power), 5-pin MIDI out, BLE MIDI as a later SKU, tray/stand mounting inserts.
- **Firmware:** every control maps to notes in the chosen scale/chord; "one-switch" mode steps through a melody or chord progression per press; "any movement" mode on the joystick; therapist presets (10 slots) and a simple web configurator (USB, no cloud).
- **Pricing:** **€299 incl. VAT** (€249 ex-VAT); school/charity 3-pack €699 ex-VAT; therapist price €229 ex-VAT via associations; mount kit €39; BLE MIDI SKU +€40.

### Unit economics (estimates, per unit)
| Item | 1,000 units | 5,000 units |
|---|---|---|
| Electronics BOM (ESP32-S3 €3, GM synth IC €5, codec/amp, 4 faders €8, 4 encoders+RGB €6, joystick €3, buttons €4, jacks, PCB) | €42 | €33 |
| Assembly & test (all controls + audio) | €9 | €6 |
| Enclosure (ABS base, alu top plate, large caps) | €12 | €8 |
| Packaging + preset card | €4 | €3 |
| Freight + duty to EU | €3.50 | €2 |
| Certification amortised (€8k EMC; +€10k if BLE) | €8 | €1.60 |
| **Landed cost** | **€78.50** | **€53.60** |
| Sell price ex-VAT direct | €249 | €249 |
| Therapist/3-pack net | €229–233 | €229–233 |
| **Gross margin direct** | **68%** | **78%** |
| **Gross margin via SEN supplier (net €160)** | 51% | 66% |

### Go-to-market
**First 100 customers:** 5 music therapists trial a prototype for a month (the kill question); the national music-therapy associations' conferences and newsletters; inclusive-music charities' practitioner networks (they run training days — bring 5 units); SEN school music coordinators via the SEN teacher forums; a video of a one-switch player leading a band.

**Scale:** SEN school suppliers' catalogues, music-therapy equipment dealers, inclusive-orchestra programmes, music retailers' education desks, DE/NL/Nordic therapist associations; the home-player SKU via Amazon once the therapist base exists.

### 12-month plan
- **Q1:** Prototypes from Unit MIDI + Unit Synth + 8Encoder + Fader on an ESP32-S3 in a laser-cut box; 5 therapists, 1 month. Gate: 3 of 5 would buy two at €299.
- **Q2:** Own PCB, enclosure tooling, quantisation firmware with therapist presets, EMC test, 300 units.
- **Q3:** Association listings, charity training days, 3-pack, mount kit, 1,000 units.
- **Q4:** BLE MIDI SKU (RED + EN 18031 budget), home-player packaging, FR/DE presets.

**Team:** embedded/audio engineer (full-time 6 months), mechanical designer (8 weeks), a music therapist as paid co-designer (critical), founder on sales. A web developer for the configurator.

**Funding to 1,000 units (estimate):** NRE €30k (PCB, tooling €12k, configurator, presets with therapists) + certification €8k + 1,000 × €67 production = €67k → **~€105k**; school/charity pre-orders and 3-packs ~€40k → cash need **~€60k**. Route: pre-orders + arts/inclusion grants (arts councils and disability-innovation funds like this product) + possibly a charity partnership that pre-buys 100 units.

### Top risks
- **Technical — low:** controls + MIDI + a synth IC. The risks are mechanical robustness (faders get yanked, buttons get hit with a fist — spec for it) and latency (keep audio in the synth IC; <10 ms).
- **Market — budgets are institutional and slow:** Mitigation: €299 is under most "no approval needed" thresholds; therapists buy their own tools; 3-pack for schools.
- **Regulatory:** EMC/LVD (USB or external PSU, SELV), RoHS/WEEE; RED only with BLE; **not a medical device** (music-making; don't claim therapy outcomes); **Toy Directive:** players include children under 14 — keep it an educational/musical instrument marketed to institutions and adults, not "a toy", and get a written opinion; EN 71 testing on caps as a precaution is cheap.
- **Supply:** the GM synth IC in the catalogue unit is a single-source part (check the Unit Synth datasheet for the exact IC); faders with 60 mm travel from two makers. Mitigation: buy 2,000 synth ICs early or design a software-synth fallback on the ESP32-S3.
- **Licence:** all four boards are modules without electronics files — you design your own PCB; nothing to infringe, but nothing to copy either.

## 3. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [m5stack-unit-midi](https://www.gongbans.com/db/m5stack-unit-midi.html) | MIDI in/out interface for prototypes | enclosure/structure only | Module |
| [m5stack-unit-synth](https://www.gongbans.com/db/m5stack-unit-synth.html) | Built-in GM synthesizer so it sounds without a laptop | enclosure/structure only | Module |
| [m5stack-unit-8encoder](https://www.gongbans.com/db/m5stack-unit-8encoder.html) | Eight encoders with RGB feedback — prototype the encoder bank | enclosure/structure only | Module |
| [m5stack-unit-fader](https://www.gongbans.com/db/m5stack-unit-fader.html) | Large fader reference | enclosure/structure only | Module |

### Block diagram and engineering gap
```
[4 faders][4 encoders+RGB][joystick][2 arcade buttons][2x 3.5mm switch jacks][expression jack]
            |
        ESP32-S3: quantiser (scale/chord), presets, USB MIDI device, 5-pin MIDI out, (BLE MIDI later)
            |-> [GM synth IC] -> [codec/amp] -> [3 W speaker] / line out
USB-C power/data ; optional 9 V PSU ; tray-mount inserts
```
Gap: the control panel mechanics (robust, big caps), quantisation and preset design with therapists, USB MIDI class device, the configurator, and the enclosure.

### Starter BOM (per unit, estimates)
| Part | Est. cost | Note |
|---|---|---|
| ESP32-S3 module (certified, USB OTG) | €3.00 | — |
| GM synth IC (per Unit Synth datasheet) | €5.00 | Single source; stock early |
| 4× 60 mm faders + big caps | €8.00 | Two makers |
| 4× encoders + RGB rings | €6.00 | — |
| Joystick (spring-return, gated) | €3.00 | Arcade-grade |
| 2× 60 mm arcade buttons | €4.00 | — |
| 3× 3.5 mm jacks + 5-pin DIN + USB-C | €2.00 | — |
| Codec + 3 W amp + speaker | €3.50 | — |
| PCB + assembly | €8.00 | — |
| ABS base + alu plate + caps | €12 | Tool €12k |

### Firmware/software starting point
- **TinyUSB** (exists; USB MIDI class) and the **Arduino MIDI Library** (exists) or **Control Surface** (exists; MIDI controllers on Arduino/ESP32). M5Stack publishes libraries for its Units (useful for the prototype). For scale quantisation, write it yourself — it's 50 lines.
- Configurator: Web MIDI in the browser (exists in Chromium browsers) — no app store, no cloud.

### 12-week build plan
- **Week 1–2 — validate.** ESP32-S3 devkit + Unit Synth + Unit MIDI + 8Encoder + Fader + a joystick in a laser-cut box; quantiser v0; 5 therapists for a month (start recruiting day 1). *Exit:* 3 of 5 would buy two at €299; players respond within the first session.
- **Week 3–5 — works-like.** Own PCB, all controls, switch jacks, USB MIDI device, presets. *Exit:* a one-switch player leads a 4-chord song.
- **Week 6–8 — looks-like + EVT.** Enclosure in final form, big caps, tray mount, configurator alpha. *Exit:* survives a fist-and-drop test; therapists set presets without you.
- **Week 9–10 — DVT + pre-compliance.** Tooling, EMC pre-scan, mechanical life test (faders 50k cycles). *Exit:* pass.
- **Week 11–12 — pilot batch.** 50 units: 20 therapists, 10 schools (3-packs), charity training day. *Exit:* 40 paid, <5% faults, 2 school 3-packs.

### Certification checklist (EU)
- **EMC/LVD route** (no radio): EN 55032/55035, EN 62368-1 (USB/SELV); self-declaration. Est. **€4–8k**.
- **RED** for the BLE MIDI SKU: EN 300 328, EN 301 489; **EN 18031** only if it connects to the internet via the phone — assume the lab will say yes; budget €10k.
- **RoHS, WEEE, REACH**.
- **CRA:** updatable firmware → SBOM, update path (USB), vulnerability contact.
- **Toy Directive:** get a written opinion; market as a musical instrument for institutions and adults; EN 71-3 on the caps as a cheap precaution.
- **Not a medical device** — no therapy-outcome claims. No battery in v1 (USB/PSU). No GDPR (no accounts).

### Validation toolkit
- **Kill question:** do 5 music therapists use a prototype for a month and would 3 of them buy two units at €299? **Cheapest experiment:** €700 — 5 laser-cut prototypes from catalogue units and 5 therapist loans.
- **5-question interview:** (1) Which players can't use your current instruments, and what do you do for them? (2) What would an instrument need so the player is always "in tune"? (3) Switch jacks, joystick, faders — which first? (4) €299 — your own purchase, the school's, or a grant? (5) What broke on the last accessible instrument you had?
- **Landing-page headline:** "Any movement makes music. Always in key." Bullets: Big faders, encoders, joystick and assistive-switch jacks · Built-in sounds — no laptop, no app · €299, built for sessions, mounts on a wheelchair tray.
- **Pre-order pass:** 30 therapist pre-orders or 10 school 3-packs in 6 weeks.

### First production checklist
Fader/encoder/button samples with life-test results, synth IC from the authorised distributor, golden sample with preset bank v1, DFM on plate cut-outs and cap fits, MOQ 300 with a 2,000 forecast, QC/AQL Level II + 100% control sweep and audio test on a fixture, drop test in packaging (it will be dropped), FOB Shenzhen air for 300, EU importer + WEEE label, quick-start in large print with pictograms.

## 4. Next steps (this week)
1. Order an ESP32-S3 devkit, Unit Synth, Unit MIDI, Unit 8Encoder, Unit Fader and an arcade joystick; get a quantised scale playing from one fader.
2. Email the national music-therapy association and one inclusive-music charity; recruit 5 therapists for a one-month trial in Q1.
3. Read the Unit Synth datasheet to identify the synth IC and ask a distributor for 2,000-piece lead time; ask a lab for an EMC quote and a written opinion on the Toy Directive.

Want help sourcing or building this? Talk to us via www.gongbans.com.
