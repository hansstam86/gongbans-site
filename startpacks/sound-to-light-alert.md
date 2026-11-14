# Sound-to-Light Alert Kit — Founder Start Pack

> Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** A deaf or hard-of-hearing person misses the doorbell, the smoke alarm and the baby. Specialist alerting systems cost €200–600 per setup (a flash receiver alone lists around $250, a vibrating pager ~$240 — [adcohearing](https://adcohearing.com/products/bellman-pager-receiver-be1230-charging-bay-bundle)), need a transmitter wired to each source, and reimbursement is a fight ([German case law on Lichtsignalanlagen](https://www.rechtslupe.de/sozialrecht/lichtsignalanlage-und-gehoerlosennotruf-39393)).
- **Customer:** Deaf and hard-of-hearing people and their families in DE/UK/NL/Nordics; hearing-aid shops, deaf associations and social-care budgets as channels. The household (or a care budget) pays; the person and their partner use it.
- **Product:** A €149 three-piece kit: two plug-in "listeners" that classify sounds on-device (doorbell, smoke alarm, baby cry, oven timer — and you can record your own), and a bedside pad with a bright flash and a strong vibration, battery-backed; colour-coded flashes per event; mesh between rooms. No wiring to the doorbell, no cloud.
- **Why now:** On-device sound classification on an ESP32-class chip is routine; Thread/Zigbee low-power radios are cheap; the incumbents still sell 433 MHz transmitters per source; EU accessibility pressure is rising.
- **The ask:** ~€95k (estimate) to the first 1,000 kits; route = association trials + member pre-orders + bootstrap; hearing-aid shop channel for scale.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Sonic Alert is a real, established incumbent selling individual components at about $64–224 each (one bundle discontinued) rather than one cheap integrated kit. "A third of today's prices" is roughly plausible: a full Sonic Alert setup is $150–250+ in parts against one €129–179 kit. **Main risk:** A discontinued Sonic Alert all-in-one starter kit suggests this exact sub-segment may have been tried and pulled before; find out why. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 deaf associations test a kit for a month and recommend it to members; do 50 members pre-order at €149?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Deaf and hard-of-hearing people, their families, social-care budgets and hearing-aid shops in DE/UK/NL/Nordics.

**The problem as the pack states it:** A deaf or hard-of-hearing person misses the doorbell, the smoke alarm and the baby. Specialist alerting systems cost €200–600 per setup (a flash receiver alone lists around $250, a vibrating pager ~$240 — [adcohearing](https://adcohearing.com/products/bellman-pager-receiver-be1230-charging-bay-bundle)), need a transmitter wired to each source, and reimbursement is a fight ([German case law on Lichtsignalanlagen](https://www.rechtslupe.de/sozialrecht/lichtsignalanlage-und-gehoerlosennotruf-39393)).

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/deaf** · https://www.reddit.com/r/deaf/ — Deaf community; read the rules on hearing-person posts first.
- **r/hardofhearing** · https://www.reddit.com/r/hardofhearing/ — hard-of-hearing adults, many late-deafened.
- **HLAA, Hearing Loss Association of America** · https://www.hearingloss.org/ — hard-of-hearing adults; local chapters.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€129–179, the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how Deaf and hard-of-hearing people, their families, social-care budgets and hearing-aid shops in DE/UK/NL/Nordics deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you notice the doorbell, a smoke alarm or a crying child at night today, and what have you tried that did not work?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices. On a scale of one to ten, how likely would you be to buy that at €129–179, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Sound-to-Light Alert Kit: would you pay €129–179 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Sound-to-Light Alert Kit: Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €129–179, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

Either way, two questions: how do you deal with this today, and what would make you say no? Honest answers are worth more to me than deposits.
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

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Sonic Alert components (Diglo, MaxiAids) | About $64–224 per component | Incumbent sold piecemeal |
| Sonic Alert all-in-one starter kit | Discontinued | The integrated-kit segment was tried before |
| Alerting-devices cost guide | Market overview | Supports the price comparison |

**Verdict as researched: LIKELY.** Main risk: A discontinued Sonic Alert all-in-one starter kit suggests this exact sub-segment may have been tried and pulled before; find out why.
<!-- market-competitors:end -->

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

## 4. Start kit

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

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Seeed Studio and M5Stack and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Sound Sensor](/db/seeed-grove-sound-sensor.html) (microphone/sound level front-end); [Seeed Grove-Haptic Motor](/db/seeed-grove-haptic-motor.html) (haptic driver reference for the wrist/pad variant). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Vibrator (U059)](/db/m5stack-unit-vibrator.html) (bedside vibration pad reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-h2-devkitm-1](/db/espressif-esp32-h2-devkitm-1.html) (Thread/Zigbee low-power sensor nodes). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*
- **Jieli Technology** (珠海市杰理科技股份有限公司) · zh-jieli.com — TWS SoC chip solution house: AC69xx/AC70xx TWS SoC; 27B+ chips shipped; clients: Xiaomi / QCY / HP / Lenovo. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Fenda Technology** (深圳市奋达科技股份有限公司) · fenda.com — TWS earbuds / smart speaker ODM: TWS earbuds; smart speaker; smart home; clients: Amazon / Creative / Philips. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Haoern Acoustics** (深圳市豪恩声学股份有限公司) · haoen.cn — TWS / headphone ODM: TWS; ANC headphone; smart speaker; clients: vivo / RAZER / BEATS / HP. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **Antixun** (深圳市安特信技术有限公司) · no website on file — TWS / smart audio ODM: TWS; ANC earphone; smart speaker; pivoted from solution house to ODM 2018. *(Audio: speaker / earphone ODMs and the Jieli chip house)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack and Espressif websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1 — for a Sound-to-Light Alert Kit

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Sound-to-Light Alert Kit: Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices. The design is built around your Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1.

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1.
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
主题：样品订购及批量报价 — Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1 — 用于Sound-to-Light Alert Kit

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sound-to-Light Alert Kit：Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices。产品设计基于贵司的Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1。
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
Subject: PCBA quote from open design files — Sound-to-Light Alert Kit, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Sound-to-Light Alert Kit: Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices. The design starts from published open-hardware files (Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Sound-to-Light Alert Kit，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sound-to-Light Alert Kit：Small listeners that recognise the doorbell, smoke alarm or baby monitor and flash a lamp or buzz a bedside pad — a plug-and-play alert kit for deaf and hard-of-hearing households at a third of today's prices。设计基于已公开的开源硬件文件（Seeed Grove-Sound Sensor, Seeed Grove-Haptic Motor, M5Stack Unit Vibrator (U059), Espressif esp32-h2-devkitm-1；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 2× Grove Sound Sensor, 2× ESP32-S3 dev kits, 3× ESP32-H2-DevKitM-1, a Unit Vibrator and a high-power LED; record 20 doorbells and 5 smoke alarms as your first dataset.
2. Write to 3 deaf/hard-of-hearing associations proposing a one-month trial (offer the kits free, ask only for feedback) — and hire a deaf or hard-of-hearing consultant for the project.
3. Train a first doorbell/smoke-alarm classifier on the dev kit and film the pad flashing; caption and sign the video.

Want help sourcing or building this? Talk to us via www.gongbans.com.
