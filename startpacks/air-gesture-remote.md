# Air-Gesture Home Remote — Founder Start Pack

> A bedside or wheelchair-tray sensor that turns small hand gestures in the air (a wave, a push, a circle) into TV, light and call commands, for people who can't press small remote buttons or speak clearly.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

**Regulatory fork you must decide early:** the EU Medical Device Regulation (MDR 2017/745) covers devices intended for the "compensation for ... a disability". An environmental control unit sold *as an aid for people with disabilities*, especially via health-insurance reimbursement, is often placed on the market as a (class I) medical device. Sold as a general "gesture remote for everyone", it is consumer electronics. Same hardware, two very different companies. This pack plans the consumer route first and treats the MDR route as a deliberate later step.

## 1. Summary

- **Problem:** People with limited hand function (MS, ALS, stroke, cerebral palsy, severe arthritis, tremor) or unclear speech can't use small remote buttons, touchscreens or voice assistants. Professional environmental control units exist, but they are specialist, expensive, slow to get through funding and often need switches mounted precisely on the body or the chair.
- **Customer:** Users themselves and their families; occupational therapists (OTs) who recommend devices; assistive-technology dealers; care homes and supported-living providers who want residents to control their own room.
- **Product:** A small sensor (bedside, table or wheelchair tray) with a 60 GHz gesture radar. 4–6 gestures map to actions: TV (IR), lights/plugs/blinds (Matter over Thread), and a "call for help" gesture to a pager, phone or nurse-call input. A therapist sets it up in a local web page, adjusts sensitivity for tremor, and every action gets a spoken/audible confirmation.
- **Why now:** 60 GHz gesture radars work without touch, light or a camera, and cost a fraction of a specialist sensor. Matter means one device controls most new lights, plugs and blinds; IR still covers TVs.
- **The ask:** About €180–220k (estimate) to the first 1,000 units, via a pilot with OT clinics/care providers, accessibility grants and social-impact angels.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Can 10 users with limited hand function trigger 4 distinct gestures with >90% success after 15 minutes' practice? Test with an OT clinic before anything else.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** People with limited hand function or speech (MS, ALS, stroke, cerebral palsy), occupational therapists, assistive-tech dealers and care homes.

**The problem as the pack states it:** People with limited hand function (MS, ALS, stroke, cerebral palsy, severe arthritis, tremor) or unclear speech can't use small remote buttons, touchscreens or voice assistants. Professional environmental control units exist, but they are specialist, expensive, slow to get through funding and often need switches mounted precisely on the body or the chair.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/OccupationalTherapy** · https://www.reddit.com/r/OccupationalTherapy/ — occupational therapists, the people who recommend assistive devices.
- **RCOT, Royal College of Occupational Therapists (UK)** · https://www.rcot.co.uk/ — UK occupational therapists.
- **DVE, Deutscher Verband Ergotherapie (DE)** · https://www.dve.info/ — German occupational-therapy association.
- **AAATE** · https://aaate.net/ — European association for assistive technology; researchers, therapists and makers.
- **r/disability** · https://www.reddit.com/r/disability/ — disabled users and carers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€199–299 (estimate; often reimbursed via assistive-device budgets), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how people with limited hand function or speech, occupational therapists, assistive-tech dealers and care homes deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the people you work with who cannot use a normal remote or a voice assistant: what do they use today to control the TV, lights or a call button, and where does it fail?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A bedside or wheelchair-tray sensor that turns small hand gestures in the air — a wave, a push, a circle — into TV, light and call commands, for people who can't press small remote buttons or speak clearly. On a scale of one to ten, how likely would you be to buy that at €199–299 (estimate; often reimbursed via assistive-device budgets), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Air-Gesture Home Remote: would you pay €199–299 (estimate; often reimbursed via assistive-device budgets) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Air-Gesture Home Remote: A bedside or wheelchair-tray sensor that turns small hand gestures in the air — a wave, a push, a circle — into TV, light and call commands, for people who can't press small remote buttons or speak clearly. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €199–299 (estimate; often reimbursed via assistive-device budgets), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The first buyer is the **family or the user** (private purchase, ~€249), recommended by an **OT**. The OT is the key influencer: if one OT practice trusts the device, it recommends it to dozens of clients per year. Second buyer: **care homes / supported living**, which want resident independence and fewer "can you switch the TV?" calls. Third, later: **reimbursement** through health or social-care budgets (which usually requires the medical-device route, a listing such as an assistive-aid register, and evidence).

The user is the person in bed or in the chair. The payer is the family, the care provider, or (later) an insurer or social-care fund.

### Market size (estimates)
- Europe has tens of millions of people with a disability; a smaller group (estimate: 1–2 M in the EU) has severe upper-limb or speech limitations that make standard remotes and voice control hard.
- Assume 10% are reachable and would use a gesture remote → **100–200k potential users → TAM ~€25–50 M** at €249.
- **SAM:** DE/AT/NL/Nordics/UK, private + care-provider purchase → **~€8–12 M**.
- **SOM (3 years):** 3–5% of SAM → **~€300–500k/year**. Small, but loyal, with low competition from big tech. Upside: care-provider fleets and reimbursement.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Professional environmental control units (ECUs) with switch/scanning input, provided via specialist services (e.g. NHS environmental-control services in the UK) | €1,000–5,000+ incl. installation | Expensive, slow assessment/funding, often needs body-mounted switches |
| Switch-adapted remotes ([US retail ~$160](https://enablingdevices.com/product-tag/environmental-control/)) | €100–200 | Still needs a reliable press on a big switch |
| Voice assistants (cloud smart speakers) | €30–100 | Fail with dysarthric speech; privacy concerns in care settings |
| Eye-gaze systems | €3,000–10,000+ | Powerful but expensive; overkill for TV/lights |
| Camera-based gesture devices | €100–300 | Camera in a bedroom/care room; lighting-dependent |
| Do nothing: ask a carer | Free | Dependence, loss of dignity, carer time |

**Wedge:** no touch, no camera, no voice — **works in the dark, through a duvet edge, with tremor-tolerant settings**, at a consumer price. Set up by an OT in 15 minutes.

### Product & value proposition
- **Sensor:** Hi-Link HLK-LD6003G (58–64 GHz FMCW, 3D presence + gesture recognition, up to 3 persons, <6 m range, 0–2 m side-mounted, ±60°, 3.3 V / 200 mA typ, 850 mA max, UART). Its built-in gesture set may not match what users with limited motion can do — test early; you may need the module's raw/point data and your own gesture classifier.
- **Outputs:** IR emitter (Seeed Grove-Infrared Emitter for prototyping; production = IR LEDs on the main PCB, learning-IR receiver optional) for TVs; HopeRF HM-MT2401 Matter-over-Thread module (MG24) as a Matter controller/client via bindings for lights, plugs, blinds; dry-contact output for a nurse-call or pager.
- **UX:** big gesture set-up wizard in a local web page (therapist mode), per-user sensitivity and "hold time" for tremor, audible confirmation (speaker: "TV on"), a "lock" gesture to prevent accidental triggers during sleep.
- **Power:** USB-C (certified adapter); optional battery backup for the call function.
- **Privacy:** radar only, no camera or mic; nothing leaves the home.

**Pricing (estimates):** €249 consumer; €299 care version (nurse-call contact, wall/rail mount, multi-user profiles); care-provider bundle with setup training. Reimbursed version: later, at a price set by that route.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (LD6003G, HM-MT2401, IR LEDs + learning receiver, speaker + amp, MCU/host, relay output, PCB) | €32.00 | €25.00 |
| USB-C adapter + cable | €3.50 | €2.60 |
| Assembly & test (radar gesture jig + IR + Thread test) | €4.00 | €2.80 |
| Enclosure + mounts (tray clamp, bed rail clamp, table stand) | €7.00 | €4.50 |
| Packaging | €2.00 | €1.40 |
| Freight + duty to EU | €1.80 | €1.20 |
| Certification amortised (~€30k) | €30.00 | €6.00 |
| **Landed cost** | **€80.30** | **€43.50** |
| Net revenue (direct €209 ex-VAT; AT-dealer ~€145 after 30% margin) | €209 | €145 |
| **Gross margin** | **€128.70 (62%)** | **€101.50 (70%)** |

Healthy margins, but you need them: OT training, support calls and returns in this market are expensive. Budget ~€20 per unit for support.

### Go-to-market
**First 100 customers:**
- **Two OT clinics or rehab centres as development partners** (neuro-rehab, MS centres, ALS clinics). They give you test users and credibility. Offer them free devices and co-authorship of an outcome report.
- **Patient associations** (MS societies, ALS associations, stroke associations) — their newsletters and events reach families directly.
- **Assistive-technology fairs** (e.g. the large rehab/care fairs in Germany) and OT conferences — live demo with a TV and a lamp.
- **Accessibility/maker communities** that already adapt devices for disabled users.

**Scale:** assistive-technology dealers (they also do installation and support), care-provider groups, and the reimbursement route in 1–2 countries.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | **Kill test with an OT clinic:** 10 users, 4 gestures, >90% success after 15 min practice; decide consumer vs MDR route |
| Q2 | Works-like with IR + Matter + call output; therapist web set-up; 20 home trials |
| Q3 | Looks-like + EVT; RED/EMC testing; usability study write-up (evidence for dealers) |
| Q4 | 1,000 units; 3 dealers; 2 care-provider pilots |

**Team:** founder (ideally with an OT or assistive-tech background), 1 embedded/radar signal engineer, 1 web/firmware engineer part-time (set-up UI, Matter), an OT advisor (paid, a few days/month). Regulatory consultant if you choose the MDR route.

**Funding to the first 1,000 units (estimates):** NRE €75k (hardware €25k, gesture firmware + set-up UI €40k, enclosure €10k) + certification €30k + usability study €10k + 1,000 units landed ~€50k + 9 months lean costs €50k ≈ **€215k**. Minus accessibility/social-innovation grants (€30–80k in several EU countries) and pre-orders from care providers → **~€100–150k**. Route: grant + social-impact angels; avoid VC until reimbursement is proven.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** built-in gestures don't fit users with limited range/tremor | Kill test first; custom gesture classifier on raw radar output if needed; "dwell/hold" gestures instead of fast swipes |
| **Technical:** false triggers (turning over in bed, carers walking by) | Lock gesture, distance gating (radar range), confirmation tone, carer "pause" button |
| **Safety:** a "call for help" gesture people rely on | Call function is a convenience, not a safety system — say so; supervise the link; low-battery and offline warnings; never replace a nurse-call system |
| **Regulatory:** MDR applies if intended use = compensation for disability | Decide the route deliberately; consumer wording ("hands-free gesture remote") vs MDR class I with QMS, technical file, PMS |
| **Market:** long sales cycles via OTs/dealers | Sell direct to families in parallel; content with real users (with consent) |
| **Supply:** sole-source radar module | Qualify a second 60 GHz gesture module in Q3 |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD6003G 60 GHz gesture radar | https://www.gongbans.com/db/hilink-ld6003g.html | Gesture recognition + 3D presence over UART | **Datasheet public, files via maker** (no open schematic/PCB) | Commercial module; ask Hi-Link for the gesture protocol and raw-data access |
| Seeed Grove-Infrared Emitter | https://www.gongbans.com/db/seeed-grove-infrared-emitter.html | IR output reference for TVs | Schematic | Check Seeed's licence on the wiki files before copying the circuit |
| HopeRF HM-MT2401 Matter-over-Thread module | https://www.gongbans.com/db/hoperf-hm-mt2401.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401) | Matter control of lights, plugs, blinds | PCB footprint/library, datasheet | MIT (HopeRF GitHub repo) |

### Block diagram
```
[LD6003G 60 GHz gesture radar] --UART--> [HM-MT2401 (MG24) as main MCU] ~~Thread/Matter~~> [lights, plugs, blinds]
                                                |--PWM--> [IR LEDs] ~~IR~~> [TV / set-top box / old devices]
                                                |--I2S/PWM--> [speaker: "TV on"]
                                                |--GPIO--> [relay / dry contact] --> [nurse call / pager]
                                                |--BLE--> [therapist set-up page on phone/tablet]
                        [USB-C 5 V] -> [3.3 V, sized for 850 mA radar peaks] (+ optional backup cell)
```
**Engineering gap:** gesture robustness for real users (maybe a custom classifier), the Matter controller side (bindings, commissioning UX for non-technical families), an IR code library for TVs, a therapist set-up UI, and mechanical mounts. The radar and radios are off the shelf.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD6003G | €14–18 | **Sole-source**; volume price + firmware freeze + raw-data access |
| HM-MT2401 | €3.50–4.50 | MG24 modules from several makers |
| IR LEDs (×3, wide angle) + driver + learning receiver | €1.20 | |
| Speaker + class-D amp | €1.50 | Loud and clear matters for confirmation |
| Relay/dry contact, buttons, LEDs | €1.20 | |
| PCB + regulator + passives | €3.00 | |
| Enclosure + mounts | €7.00 | Mounts are where the real-world value is |

### Firmware/software starting point
- **Matter:** Silicon Labs Matter extension for the MG24, and the open-source **connectedhomeip** SDK (github.com/project-chip/connectedhomeip) — start from the "light-switch-app" example, which already uses bindings to control other devices.
- **IR:** search "IRremote library" (Arduino) or port an IR protocol encoder; a TV code database is needed (search for open IR code databases and check their licences).
- **Radar:** Hi-Link's UART protocol and PC tool (from the maker).
- **Set-up UI:** a BLE-served or Web-Bluetooth page; keep it big-font and WCAG-friendly.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill test:** 10 users with limited hand function at an OT clinic trigger 4 distinct gestures with >90% success after 15 min practice (LD6003G dev setup + laptop). Plus: 5 OT interviews |
| 3–5 | Works-like | Gesture → IR TV control + 1 Matter light + call contact; 5 home trials; false triggers <1 per night |
| 6–8 | Looks-like + EVT | Custom PCB, enclosure, 3 mounts; therapist set-up page; 20 units |
| 9–10 | DVT + pre-compliance | RED pre-scan (60 GHz + 2.4 GHz), EMC, usability review (big-font, audio feedback), mount drop/strength tests |
| 11–12 | Pilot batch | 50 units across 2 clinics + 2 care homes; ≥80% still in daily use after 4 weeks; OT outcome notes collected |

### Certification checklist (EU)
- **Route decision (MDR):** consumer route = intended use "hands-free gesture remote for TV, lights and home devices", no disability-compensation claims, no reimbursement. MDR route = class I medical device (self-declared, but with QMS, technical file, risk management ISO 14971, usability IEC 62366, post-market surveillance, EUDAMED registration) — needed for many reimbursement paths. Budget €40–80k + time for the MDR route.
- **CE under RED:** 60 GHz radar (confirm the module's harmonised standard with the lab), EN 300 328 (Thread/BLE at 2.4 GHz), EN 301 489-1/-3/-17, EN 62368-1, EN 62311. Est. **€15–25k**.
- **RED delegated act (EN 18031-1):** applies if internet-connected (Thread via border router); self-assessment ~€3–6k.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027 — secure updates, SBOM, vulnerability handling.
- **Accessibility:** the European Accessibility Act targets specific products/services, but design the set-up UI to WCAG / EN 301 549 anyway — dealers and public buyers ask for it.
- **RoHS, REACH, WEEE**, packaging. Battery Regulation only if you add a backup cell.
- **GDPR:** no camera/mic, local only → low; if you add remote set-up or logs, it's health-adjacent data (disability) → consent, EU hosting.
- **Total estimate: €20–35k (consumer route).**

### Validation toolkit
- **Kill question:** Can 10 users with limited hand function trigger 4 distinct gestures with >90% success after 15 minutes' practice?
- **Cheapest experiment (~€300 + a clinic day):** LD6003G dev board on a laptop with a big on-screen display of the recognised gesture; an OT runs the session; score each attempt.
- **5-question interview (OT / user / family):** 1) Which daily device actions does the person most need help with? 2) What have you tried (switches, voice, eye-gaze), and why did it fail or stick? 3) What movements are reliable for this person on a bad day? 4) Who would pay — the family, the provider, insurance? 5) At €249, would you buy it after a 2-week home trial?
- **Landing page headline:** "Control your TV and lights with a small wave of the hand." Bullets: "No buttons to press, no voice needed, no camera." / "Set up by your therapist in 15 minutes, tuned to how you move." / "Works with your TV and Matter lights, plugs and blinds."
- **Pass threshold:** kill test passed + 2 OT practices willing to recommend + 30 home-trial requests with a deposit.

### First production checklist
- **Samples:** radar modules from 2 lots — gesture performance can vary with firmware; lock the firmware version.
- **Golden sample:** including mounts; record the gesture-jig results.
- **DFM review:** radome in front of the radar (no metal, no thick texture), mount strength, cleanability (care settings: wipe-down plastics, no crevices).
- **MOQ talk:** radar module, speaker, enclosure colour; mounts may be better made in the EU in small batches.
- **QC/AQL:** AQL II 1.0/2.5; 100% radar gesture test with a robot-arm or rotating-plate jig, IR output test, Thread commissioning test.
- **Packaging:** easy-open (users with limited hand function!), large-print quick start, video QR code, OT set-up guide.
- **Incoterms:** FOB Shenzhen; mounts possibly DAP from an EU workshop.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and Seeed Studio and HopeRF (华普微)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R)](/db/hilink-ld6003g.html) (60 GHz gesture-recognition radar). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Infrared Emitter](/db/seeed-grove-infrared-emitter.html) (IR output for TVs and older devices). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder)](/db/hoperf-hm-mt2401.html) (Matter-over-Thread for lights, plugs and blinds). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and Seeed Studio and HopeRF (华普微) websites)

```email
Subject: Sample order and volume pricing — HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder) — for a Air-Gesture Home Remote

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Air-Gesture Home Remote: A bedside or wheelchair-tray sensor that turns small hand gestures in the air — a wave, a push, a circle — into TV, light and call commands, for people who can't press small remote buttons or speak clearly. The design is built around your HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder).
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
主题：样品订购及批量报价 — HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder) — 用于Air-Gesture Home Remote

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Air-Gesture Home Remote：A bedside or wheelchair-tray sensor that turns small hand gestures in the air — a wave, a push, a circle — into TV, light and call commands, for people who can't press small remote buttons or speak clearly。产品设计基于贵司的HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder)。
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
Subject: PCBA quote from open design files — Air-Gesture Home Remote, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Air-Gesture Home Remote: A bedside or wheelchair-tray sensor that turns small hand gestures in the air — a wave, a push, a circle — into TV, light and call commands, for people who can't press small remote buttons or speak clearly. The design starts from published open-hardware files (HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Air-Gesture Home Remote，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Air-Gesture Home Remote：A bedside or wheelchair-tray sensor that turns small hand gestures in the air — a wave, a push, a circle — into TV, light and call commands, for people who can't press small remote buttons or speak clearly。设计基于已公开的开源硬件文件（HLK-LD6003G 60 GHz gesture-recognition radar module (2T2R), Seeed Grove-Infrared Emitter, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 2 HLK-LD6003G samples and an HM-MT2401 EVB; ask Hi-Link which gestures are built in and whether raw/point data is accessible.
2. Contact two neuro-rehab or MS clinics and ask an OT for one afternoon with 5–10 users for the kill test.
3. Decide (provisionally) consumer vs MDR route and write the intended-use sentence that matches it.

Want help sourcing or building this? Talk to us via www.gongbans.com.
