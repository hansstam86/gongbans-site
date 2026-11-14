# Workshop Air & Noise Sentinel — Founder Start Pack

> A wall unit for makerspaces, school workshops and small joineries that logs VOC, CO2, temperature and noise exposure, shows a traffic light across the room, and produces the documentation small workshops need for a health-and-safety visit.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Small workshops must document exposure (solvents, dust, noise, ventilation) under occupational-safety rules, but industrial monitors cost €1,000+ and consumer air monitors don't log shifts or trigger extraction.
- **Customer:** Makerspaces/FabLabs (800+ makerspaces in Europe per the JRC network, ~400 FabLabs by one count — [JRC EU Makerspaces](https://cop-demos.jrc.ec.europa.eu/eu-makerspaces), [IOP Alliance report](https://iop-alliance.github.io/data_reports/reports/make_europe.html)), school and vocational workshops, small joineries, print shops, nail/paint booths. The operator or school pays; the safety officer and the people in the room use it.
- **Product:** €249–329 wall unit: VOC (BME680-class), true NDIR CO2 (SCD41-class), temperature/humidity, A-weighted noise level, a big traffic light, a relay to start the extraction fan, shift logging and a PDF for the safety officer. PM2.5 is a bought-in add-on (state the gap honestly).
- **Why now:** The sensors are catalogue parts (open BME680 board, SCD41 Grove, loudness Grove); makerspaces and schools are buying air monitors anyway since 2020; "indicative monitor with documentation" is a slot between €150 consumer gadgets and €1,000 instruments.
- **The ask:** ~€80k (estimate) to 1,000 units. Route: trial-unit programme (kill question) + bootstrap; education-supply distributors and a maker-community pre-order run.

<!-- market-check:start -->
> **External market check (November 2026): UNCERTAIN.** The underlying hazards are well documented (NIOSH and CDC on 3D-printer VOCs in makerspaces), but no regulated indoor-air-quality standard for small workshops was found, which undercuts the "documentation for health-and-safety visits" framing. **Main risk:** Demand may be real but voluntary, not compliance-forced. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 10 makerspaces or school workshops buy at €279 after a two-week trial unit?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Makerspaces, school and vocational workshops, small joineries and print shops in the EU.

**The problem as the pack states it:** Small workshops must document exposure (solvents, dust, noise, ventilation) under occupational-safety rules, but industrial monitors cost €1,000+ and consumer air monitors don't log shifts or trigger extraction.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/woodworking** · https://www.reddit.com/r/woodworking/ — hobby and small-shop woodworkers.
- **UKworkshop** · https://www.ukworkshop.co.uk/ — UK woodworkers and small shops.
- **Festool Owners Group** · https://www.festoolownersgroup.com/ — dust-extraction-conscious woodworkers.
- **Verbund Offener Werkstätten (DE)** · https://www.offene-werkstaetten.org/ — German network of open workshops and makerspaces.
- **hackerspaces.org wiki** · https://wiki.hackerspaces.org/ — directory of makerspaces worldwide; e-mail the ones near you.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€249–329, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how makerspaces, school and vocational workshops, small joineries and print shops in the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know whether your dust extraction is actually working at the machine you are using, and when did you last check?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A wall unit for makerspaces, school workshops and small joineries that logs VOC, CO2, temperature and noise exposure and shows a traffic light — the documentation small workshops need for health-and-safety visits. On a scale of one to ten, how likely would you be to buy that at €249–329, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Workshop Air & Noise Sentinel: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Workshop Air & Noise Sentinel: A wall unit for makerspaces, school workshops and small joineries that logs VOC, CO2, temperature and noise exposure and shows a traffic light — the documentation small workshops need for health-and-safety visits. Before we spend money on tooling I want to find out whether this solves a real problem for makerspaces, school and vocational workshops, small joineries and print shops in the EU.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €249–329 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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
Three segments, one product:
1. **Makerspaces/FabLabs/community workshops** — a manager with a small budget and a board that worries about liability. Buys 1–3 units. Talkative community; good for launch.
2. **School and vocational-training workshops** — the school buys via education-supply catalogues; the safety officer inspects yearly. Buys per workshop (wood, metal, paint). Slow but repeat.
3. **Small joineries, print shops, nail/paint studios** — the owner buys when the safety inspector or the insurer asks for documentation. Buys 1 unit, wants a PDF.

The pain is twofold: the room is bad (headaches, dust, noise) and nobody can prove anything either way. The traffic light handles the first; the shift log and PDF handle the second.

### Market size (estimates)
- EU + UK: ~1,200 makerspaces/FabLabs (estimate), ~150k schools with a workshop or lab (vocational and secondary — estimate), ~300k small workshops in wood/metal/print/paint trades (estimate). Call it **450k rooms**.
- **TAM:** 450k × €289 ≈ **€130 M**.
- **SAM:** rooms whose operator has faced a safety inspection or insurer question and has a budget ≥ €300 — 20% → 90k → **€26 M**.
- **SOM (3 years):** 4% → 3,600 units → **€1 M**, plus PM add-on and relay accessories (~15%).

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Consumer/prosumer air monitors (CO2 ~$159 [Aranet4-class](https://www.aranet.com/en/pro/blog/aranet4-home-vs-aranet4-pro); multi-sensor $130–250 [Airthings-class](https://smarthomecompared.com/air-quality-monitors/airthings-wave-enhance-vs-aranet-aranet4-home)) | Well made, app-based | No noise exposure, no shift log, no relay, no PDF, no wall-visible traffic light |
| Business air-quality platforms (multi-sensor + dashboard + subscription) | Office-oriented | Subscription, cloud-dependent, no noise-exposure logic, no extraction relay |
| Industrial multi-gas / noise dosimeters (€1,000+) | Certified instruments | Price; one parameter each; not continuous wall monitors |
| CO2 traffic lights for classrooms (€80–150) | Common since 2020 | CO2 only |
| Paper checklists / "do nothing" | The default | No evidence when the inspector or insurer asks |
| DIY (ESP32 + sensors + Home Assistant) | Makerspaces do this | No PDF, no relay rating, nobody maintains it; we sell to the ones who tried |

**Wedge:** noise + VOC + CO2 in one wall unit with a room-visible light, an extraction-fan relay, and shift-based documentation; honest "indicative, not a certified instrument" positioning with a calibration-check routine.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| NIOSH makerspace guide | Hazard guidance | The hazard is documented |
| ASU EHS makerspace guidance | University safety guidance | Same |
| Chemical Insights 3D Makerspace report | VOC exposure study | Same; no regulatory threshold for small workshops found |

**Verdict as researched: UNCERTAIN.** Main risk: Demand may be real but voluntary, not compliance-forced.
<!-- market-competitors:end -->

### Product & value proposition
Hardware: 160 × 100 × 40 mm wall unit, 12 V PSU, BME680-class gas/VOC + T/RH, SCD41-class NDIR CO2, MEMS mic → dBA + LAeq per shift (no audio stored), 3-colour LED bar readable at 10 m, 2.9" e-paper or small LCD, relay 10 A for the extraction fan (dry contact), microSD, WiFi/Ethernet optional, BLE for setup. Firmware: thresholds per parameter, traffic light logic (worst-of), shift start/stop (button or schedule), daily/weekly summary, PDF/CSV export via web page or email, PM2.5 add-on over a connector (bought-in laser PM sensor). Wellness/safety-documentation positioning; **not a certified occupational-exposure instrument** — say it everywhere.

Pricing (estimates): **€289 B2C/direct**, €329 with PM2.5 add-on, €249 education pricing, €499 "pro" with Ethernet and 2 relays. B2B via education-supply distributors at 30–35% off.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32-S3 module, BME680-class, SCD41-class, MEMS mic, LED bar, 2.9" e-paper, relay, PSU 12 V, PCB) | €44.00 | €35.00 |
| Assembly & test (SMT, sensor warm-up test, mic level test, relay test) | €6.50 | €4.50 |
| Enclosure (2-shell ABS with vents, light diffuser, wall bracket; tooling amortised) | €6.80 | €4.20 |
| Packaging (box, bracket, screws, PSU) | €3.50 | €2.60 |
| Freight + duty to EU | €3.20 | €1.90 |
| Certification amortised (~€30k: RED, EMC, LVD/62368-1 for relay + PSU, EN 18031) | €30.00 | €6.00 |
| **Landed cost** | **€94.00** | **€54.20** |
| Sell price (direct €289 / distributor €195) | €289 | €195 |
| **Gross margin** | **€195.00 (67%)** | **€140.80 (72% at distributor)** |

Solid. The PM2.5 add-on (bought-in laser sensor ~€12–18, sold at €49) adds margin and plugs the gap honestly.

### Go-to-market
**First 100 customers:** 20 trial units to makerspaces/FabLabs and school workshops (kill question: 10 of 20 buy at €279 after two weeks); maker-community channels (FabLab network forums, makerspace associations, hackerspace mailing lists), vocational-teacher associations, woodworking-trade guilds and their insurers' safety advisers (they recommend equipment), trade fairs for education supply and for woodworking (Ligna-class) — one each.

**Scale channels:** education-supply distributors (catalogues schools order from), occupational-safety consultancies (they sell audits and can resell the unit), trade-guild member offers, extraction-system installers (bundle the relay feature).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like from the open BME680 board + SCD41 Grove + loudness Grove + AtomS3; 20 trial units in printed cases; kill question. |
| Q2 | Custom PCB, tooled case, relay/PSU safety design; EVT 50; PDF/web export; pre-compliance. |
| Q3 | DVT, certification, 300-unit pilot; education distributor listing; PM add-on. |
| Q4 | 1,000 units; two distributors; safety-consultancy partner programme. |

**Team:** 1 embedded engineer (sensors, dBA, power — full-time), 1 web/firmware developer (web UI, PDF, shift logic — part-time → full-time), founder for community and distributor sales; an occupational-safety adviser part-time to make the documentation credible. Two and a half people.

**Funding to first 1,000 units (estimates):** NRE €42k (PCB €8k, tooling €14k, software €15k, safety-adviser content €5k) + certification €30k + 1,000 units landed ~€64k + 9 months lean overhead €65k ≈ **€201k**; minus trial-to-sale and pre-orders (~€45k) and pilot batch sales (~€75k) ≈ **~€80k**. Bootstrap + maker-community pre-orders + an education-distributor prepayment. Education/innovation grants exist for "safe learning environments" in several countries.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** metal-oxide VOC sensors give an index, not ppm; buyers expect numbers | Present "VOC index + trend + threshold" honestly; map to "ventilate now" actions; offer the PM add-on for dust, which is what joineries actually need |
| **Technical:** noise measurement accuracy vs class-2 meters; mic ageing | Factory level calibration with a calibrator; publish ±3 dB; annual self-check routine; never call it a dosimeter |
| **Market:** "indicative" scares safety officers; "instrument" invites liability | Position as early warning + documentation support; the official measurement remains the consultant's job — partner with them |
| **Regulatory:** relay switching mains fans → LVD/62368-1 and installer rules | Dry-contact relay only; fan contactor installed by an electrician; or ship a certified plug-in relay socket |
| **Regulatory:** EN 18031 + CRA for a connected device | Pre-certified module, local-first design, budget it |
| **Supply:** SCD41-class and BME680-class have had allocation issues; e-paper lead times | Second-source footprints; order panels early |
| **Licence:** the open BME680 board is OSHWHub | Read the licence; it's a breakout — redraw your own |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| BME680 gas sensor board (OSHWHub) | https://www.gongbans.com/db/oshwhub-bme680.html | Open BME680 gas/VOC + T/RH breakout reference | schematic, pcb (EasyEDA) | **OSHWHub licence varies — read it**; trivial to redraw |
| Seeed Grove CO2-Temperature-Humidity Sensor (SCD41) | https://www.gongbans.com/db/seeed-grove-co2-temperature-humidity-sensor-scd41.html | True NDIR CO2 reference | schematic | Seeed wiki resources; check licence |
| Seeed Grove Loudness Sensor | https://www.gongbans.com/db/seeed-grove-loudness-sensor.html | Noise-level front-end (prototype only; production uses a MEMS mic + DSP) | schematic | Seeed wiki resources |
| M5Stack AtomS3 (C123) | https://www.gongbans.com/db/m5stack-atoms3.html | ESP32-S3 with small display for the works-like | enclosure/structure only | Buy; your own board later |

**Board-fact note:** no particulate (PM2.5) sensor exists in the catalogue. The PM add-on is a bought-in laser-scattering module from a sensor vendor.

### Block diagram
```
[BME680-class VOC/T/RH] [SCD41-class NDIR CO2] [MEMS mic -> dBA/LAeq on MCU] [PM2.5 add-on connector]
         \                    |                    |                            /
          ---------------- I2C / I2S --------------+---------------------------
                                     [ESP32-S3] -> [LED bar: green/amber/red] [2.9" e-paper]
                                         |-> [relay 10 A dry contact -> extraction fan contactor]
                                         |-> [microSD shift log] [WiFi/BLE -> web page: PDF/CSV, settings]
                                     [12 V PSU (certified adapter)]
```
**Engineering gap:** sensors and MCU exist; the product is the exposure logic (shift LAeq, thresholds, traffic-light rules), the dBA DSP, the relay/PSU safety design, the web UI and PDF, and a case with proper airflow past the sensors without self-heating. Sensor placement and the documentation content are the real work.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 module | €2.60 | Pre-certified |
| BME680/BME688-class gas sensor | €6.50 | **Single-vendor family**; alternative MOX VOC sensor on a second footprint |
| SCD4x-class NDIR CO2 | €14.00 | **Allocation risk**; second family qualified |
| MEMS microphone I2S | €0.90 | Multi-source |
| LED bar (12× RGB, diffused) | €1.20 | |
| 2.9" e-paper + driver | €7.50 | Lead time 6–10 weeks |
| Relay 10 A + driver + terminal block | €1.80 | Dry contact only |
| 12 V 1 A certified PSU adapter | €2.50 | Buy certified; don't design mains |
| PCB 4-layer, passives, SD slot, USB-C, buttons | €4.50 | |
| Enclosure 2-shell + diffuser + bracket | €6.80 | **Tooling €10–16k** |
| PM2.5 laser sensor (add-on, optional) | €12–18 | Bought-in; limited vendors |

### Firmware/software starting point
- ESP-IDF; Bosch publishes the BSEC library for BME680/688 (binary, licence terms apply — read them; the raw-resistance route is licence-free but cruder); Sensirion publishes SCD4x drivers on GitHub.
- dBA/LAeq: open ESP32 I2S sound-level-meter projects exist (search "ESP32 I2S sound level meter A-weighting"); implement LAeq integration per shift yourself.
- Web UI + PDF: ESP32 web server + a JS PDF library (search "jsPDF") so the PDF renders in the browser; CSV from SD.
- Home Assistant/MQTT output is a cheap bonus the makerspace crowd will ask for.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 20 works-like units (open BME680 board + SCD41 Grove + loudness Grove + AtomS3 in printed cases) placed as two-week trials; **10 of 20 buy at €279** (runs to W6) |
| 3–5 | Works-like | Traffic light + shift log + CSV on SD; dBA within ±3 dB of a class-2 meter; CO2 within ±50 ppm; relay triggers a test fan |
| 6–8 | Looks-like + EVT | Custom PCB v1, tooled case T1 with validated airflow (sensor self-heating < 1 °C); 50 units; web UI + PDF; EMC pre-scan |
| 9–10 | DVT + pre-compliance | RED/EMC pre-compliance; EN IEC 62368-1 review of the relay/PSU; EN 18031 self-assessment; documentation reviewed by an occupational-safety adviser |
| 11–12 | Pilot batch | 50 units to trial converts + 10 schools; safety-officer feedback from ≥ 3 inspections; relay in use at ≥ 5 sites |

### Certification checklist (EU)
- **CE under RED** (WiFi/BLE): EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** (relay contacts, PSU — using a certified adapter keeps mains out of your box; the relay's dry contact must be rated and the terminal block finger-safe); **EN 18031-1** (internet-connected, mandatory since 1 Aug 2025; -2 if staff names are logged). Est. €6–9k RED/EMC, €4–6k safety, €10–18k EN 18031.
- **RoHS, REACH, WEEE** per country; **Packaging** registration.
- **Battery regulation:** none if mains-only (keep it mains-only; a backup cell adds UN 38.3 and the 2027 removability rules).
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027; signed firmware, OTA via web upload, SBOM, vulnerability contact.
- **GDPR:** noise *levels* only, no audio; shift logs may include a person's name if you let users tag shifts — avoid or add a privacy notice; schools are sensitive.
- **Not an occupational-exposure instrument** (no IEC 61672 class claim, no gas-detector EN 50271 claim); it supports documentation, it doesn't replace the measurement a safety consultant does. **Not a toy** (schools: fine, it's equipment).
- **Total certification budget estimate: €22–35k.**

### Validation toolkit
- **Kill question:** Do 10 makerspaces or school workshops buy at €279 after a two-week trial unit?
- **Cheapest experiment (~€1,800):** 20 works-like units in printed cases shipped with a return label and a one-page "what the light means" sheet; a buy-or-return email at day 14. Count buys.
- **5-question interview (workshop manager / safety officer):** 1) When was your last safety inspection and what did they ask to see? 2) What's the worst thing about the air or noise in your workshop, and when? 3) Do you have extraction, and who switches it on? 4) Would a traffic light on the wall change behaviour in the room? 5) €279 for the unit with shift logs and a PDF — whose budget, and what would stop the purchase?
- **Landing page:** headline "Know when the workshop air is bad — and prove it." Bullets: "VOC, CO2, temperature and noise exposure, with a traffic light the whole room can see." / "Starts your extraction fan automatically; logs every shift to a PDF for the safety officer." / "€279. Indicative monitor — early warning and documentation, not a lab instrument."
- **Pass threshold:** 10 of 20 trial units bought, or 100 pre-orders at €249 from the maker community in 4 weeks.

### First production checklist
- Samples: 5 golden samples with sensor calibration records (CO2 at 2 points, mic level with a calibrator) and relay test.
- DFM: vent geometry, sensor isolation from the PSU heat, diffuser uniformity, wall-bracket keyholes; test jig with reference CO2 and a tone source.
- MOQ talk: CO2 sensor 500–1k; gas sensor reel 1k; e-paper 1k; case 1k; certified PSU 1k.
- QC: AQL II 2.5/4.0; 100% sensor plausibility + mic level + relay test; 24 h burn-in on 5%; 2% re-check CO2 after burn-in.
- Packaging: box with bracket, screws, PSU, quick sheet; no lithium.
- Incoterms: FOB Shenzhen; air for the first 300; sea after.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Seeed Studio and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41](/db/seeed-grove-co2-temperature-humidity-sensor-scd41.html) (true NDIR CO2); [Seeed Grove-Loudness Sensor](/db/seeed-grove-loudness-sensor.html) (noise level reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack AtomS3 (C123)](/db/m5stack-atoms3.html) (MCU with small display for the prototype). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [BME680气体传感器](/db/oshwhub-bme680.html) (open BME680 gas/VOC + T/RH board).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Loudness Sensor, M5Stack AtomS3 (C123) — for a Workshop Air & Noise Sentinel

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Workshop Air & Noise Sentinel: A wall unit for makerspaces, school workshops and small joineries that logs VOC, CO2, temperature and noise exposure and shows a traffic light — the documentation small workshops need for health-and-safety visits. The design is built around your Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Loudness Sensor, M5Stack AtomS3 (C123).

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Loudness Sensor, M5Stack AtomS3 (C123).
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
主题：样品订购及批量报价 — Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Loudness Sensor, M5Stack AtomS3 (C123) — 用于Workshop Air & Noise Sentinel

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Workshop Air & Noise Sentinel：A wall unit for makerspaces, school workshops and small joineries that logs VOC, CO2, temperature and noise exposure and shows a traffic light — the documentation small workshops need for health-and-safety visits。产品设计基于贵司的Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Loudness Sensor, M5Stack AtomS3 (C123)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-Loudness Sensor, M5Stack AtomS3 (C123)。
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
Subject: PCBA quote from open design files — Workshop Air & Noise Sentinel, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Workshop Air & Noise Sentinel: A wall unit for makerspaces, school workshops and small joineries that logs VOC, CO2, temperature and noise exposure and shows a traffic light — the documentation small workshops need for health-and-safety visits. The design starts from published open-hardware files (BME680气体传感器; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Workshop Air & Noise Sentinel，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Workshop Air & Noise Sentinel：A wall unit for makerspaces, school workshops and small joineries that logs VOC, CO2, temperature and noise exposure and shows a traffic light — the documentation small workshops need for health-and-safety visits。设计基于已公开的开源硬件文件（BME680气体传感器；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 20 sets (open BME680 board fabbed or a BME680 breakout, SCD41 Grove, loudness Grove, AtomS3) and print 20 cases; have one unit showing a traffic light by day 7.
2. List 40 makerspaces, FabLabs and school workshops in your language area and write the two-week trial email (unit, return label, buy-or-return at day 14).
3. Read your country's small-workshop occupational-safety guidance (noise, solvents, ventilation) and turn the limits into the threshold table — and have a safety adviser sanity-check it.

Want help sourcing or building this? Talk to us via www.gongbans.com.
