# Proofing-Cabinet Controller — Founder Start Pack

> A drop-in controller for bakery proofing and retarder cabinets. It holds temperature and humidity on a schedule ("retard overnight, proof from 4 a.m.") and lets the baker check from bed.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Overnight retarding (cold-holding dough, then proofing it automatically before the shift) saves artisan bakers hours of night work. But many small bakeries, pizzerias and cafés run old proofing or retarder cabinets with a dumb thermostat and a humidity knob. They come in at 3 a.m. to switch modes, or they lose a batch when the humidity drifts or a door is left ajar.
- **Customer:** Two routes. (1) **Small bakery-equipment makers and refrigeration/bakery service companies** who want a connected controller for new or refurbished cabinets (OEM/retrofit partner). (2) **Artisan bakeries, pizzerias, cafés baking on site** buying via those service companies. The owner-baker pays; the baker and staff use it.
- **Product:** A controller with a Tuya CBU Wi-Fi + BLE module (BK7231N), a HopeRF TH09C humidity/temperature sensor, switching outputs for the cooling stage (via the existing contactor), heater and humidifier, and a small isolated AC-DC supply. Two-stage programmes (retard → proof), door-open detection, humidity-drift alarms, HACCP-style temperature history export. A local display and buttons keep full control without the app.
- **Why now:** Bakers are short of staff and nobody wants to start at 2 a.m. any more. Tuya's white-label app lets a small equipment maker offer "an app" in weeks without an app team, which is exactly what a 20-person equipment maker can't build.
- **The ask:** About €110–140k (estimate) to the first 1,000 controllers, financed mostly by 2 OEM/service-partner pilot orders.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 2 bakery-equipment makers or service companies buy a 20-unit pilot? And is a Tuya-cloud app acceptable to their customers? Ask before building.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Artisan bakeries, pizzerias, cafés baking on site; small equipment makers wanting a connected controller.

**The problem as the pack states it:** Overnight retarding (cold-holding dough, then proofing it automatically before the shift) saves artisan bakers hours of night work. But many small bakeries, pizzerias and cafés run old proofing or retarder cabinets with a dumb thermostat and a humidity knob. They come in at 3 a.m. to switch modes, or they lose a batch when the humidity drifts or a door is left ajar.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/Breadit** · https://www.reddit.com/r/Breadit/ — bread bakers, home and professional.
- **Zentralverband des Deutschen Bäckerhandwerks (DE)** · https://www.baeckerhandwerk.de/ — German bakers' trade federation; the local Bäckerinnung is the way in.
- **r/restaurateur** · https://www.reddit.com/r/restaurateur/ — restaurant owners.
- **r/KitchenConfidential** · https://www.reddit.com/r/KitchenConfidential/ — chefs and kitchen staff; the people who do the fridge log.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199 retrofit, or OEM price (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how artisan bakeries, pizzerias, cafés baking on site deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about your last ruined batch in the proofer or retarder: what went wrong with temperature, humidity or timing, and how would you have known earlier?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A drop-in controller for bakery proofing and retarder cabinets that holds temperature and humidity on a schedule ('retard overnight, proof from 4 a.m.') and lets the baker check from bed. On a scale of one to ten, how likely would you be to buy that at €149–199 retrofit, or OEM price (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Proofing-Cabinet Controller: would you pay €149–199 retrofit, or OEM price (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Proofing-Cabinet Controller: A drop-in controller for bakery proofing and retarder cabinets that holds temperature and humidity on a schedule ('retard overnight, proof from 4 a.m.') and lets the baker check from bed. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–199 retrofit, or OEM price (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Bakers don't buy controllers; **they buy cabinets and service.** So the realistic customer is the company that builds, refurbishes or services proofing/retarder cabinets: small regional equipment makers, refrigeration service firms, used-equipment refurbishers. They know which customers have 15-year-old cabinets with a dying thermostat, and they're the ones legally allowed to rewire a commercial appliance.

Direct sales to bakers are possible for a "plug-in" variant (a controller that switches a simple proofer via its mains plug), but anything with a compressor must go through a qualified technician. Don't sell retrofit kits for refrigeration circuits to bakers as DIY.

### Market size (estimates)
- Craft bakeries: Germany has roughly 9,000–10,000 craft bakery businesses (trade-association figures), France on the order of 30,000+ boulangeries, plus Italy, Benelux, Austria, Nordics; add pizzerias and cafés baking on site with proofers. Assume **~150,000 businesses** in EU-core with at least one proofing/retarder cabinet, ~1.5 cabinets each → **~225,000 cabinets**.
- **TAM:** 225,000 × €179 ≈ **€40 M** retrofit, plus new-cabinet OEM volume.
- **SAM:** cabinets >7 years old with mechanical/basic controllers in DACH, Benelux, France: ~35% → **~79,000 cabinets ≈ €14 M**.
- **SOM (3 years):** 2–3 service/OEM partners × ~1,500 units → **~4,500 units ≈ €0.5–0.8 M**. A niche, and a good one only if partners carry the sales.

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| New retarder-proofer cabinet with programmable controls (several big bakery-equipment brands offer remote portals as accessories) | €4,000–15,000 per cabinet | Replacing a working cabinet just for the controller |
| Industrial refrigeration controllers with connectivity (e.g. Dixell/Eliwell-class controllers, added by a technician) | €150–500 + gateway/subscription | Built for cold rooms, not two-stage retard/proof with humidity; technician-only UI |
| Home proofers with Wi-Fi (e.g. Brod & Taylor Proofer Pro, set up through the SmartLife/Tuya app) | €200–400 | Home size; shows the app pattern works, but not for a bakery cabinet |
| DIY temperature controllers (Inkbird-class plug-in controllers) | €40–80 | Temperature only, no schedule, no humidity, no history |
| Do nothing: baker switches modes at 3 a.m. | Free | Sleep, lost batches |

**Wedge:** a **bakery-specific two-stage programme** with humidity control and a phone app, sold **through the people who already service the cabinets**, at a price below one lost night's production. HACCP-style temperature log as a bonus for inspections.

### Product & value proposition
- **Programmes:** e.g. "Retard 3 °C until 02:30 → ramp → proof 26 °C / 80 %RH until 05:30 → hold 10 °C". Up to 10 stored programmes with names ("Baguette weekday", "Croissant Sunday").
- **Sensors:** TH09C (I²C, ±2 %RH, ±0.15 °C typical per HopeRF), mounted in a vented, condensation-protected probe housing; optional second probe; door contact input.
- **Outputs:** cooling stage (drive the existing compressor contactor, never the compressor directly), heater, humidifier/steam generator, fan. Safety devices of the original cabinet (high-pressure switch, thermal fuses, heater limiter) stay in the chain.
- **Connectivity:** Tuya CBU (BK7231N, Wi-Fi 4 + BLE 5.2, 21 pins, per Tuya's datasheet) for the app: current state, programme start/change, alerts (humidity drift, door open, temperature out of range), history export.
- **Local UI:** small segment/LCD display + 4 buttons; everything essential works without Wi-Fi.

**Pricing (estimates):** Retrofit controller €179 (via service partner; partner adds installation), OEM price €55–75 at 1k+/yr, history/HACCP export free (Tuya app) or €2/month for multi-cabinet bakeries with a web dashboard.

### Tuya: the cloud question
- **Why Tuya here:** an equipment maker gets a branded app, cloud, OTA and push notifications without hiring an app team. For 20–50-person bakery-equipment makers, that's the whole point.
- **The dependency:** remote monitoring, programme changes from the phone, alerts and history depend on **Tuya's cloud**. If the cloud or the commercial relationship ends, the app features stop. The controller must keep baking: programmes run locally.
- **Data residency / GDPR:** cabinet data isn't sensitive, but door-open events and app log-ins are linked to staff and owners. Pick Tuya's European data region, sign a DPA, document data flows; offer a data-export function so the bakery owns its HACCP records.
- **Tuya-free alternative:** the same PCB with an ESP32-C3 module (footprint-compatible design) and your own firmware with a local web UI or Home Assistant/ESPHome, or open firmware on the BK7231N (the OpenBeken project supports BK7231-family modules; search "OpenBK7231T_App"). Some equipment makers will want their own cloud anyway; offer that SKU at a higher NRE.

### Unit economics (estimates per controller, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (CBU module, TH09C + probe housing, 3–4 relays/SSR, isolated AC-DC 5 W, display, buttons, terminals, PCB) | €24.00 | €19.00 |
| Assembly & test (relay switching, sensor calibration check at 2 points, Wi-Fi pairing) | €3.00 | €2.20 |
| Enclosure (panel-mount front + rear cover, IP54 front) | €3.50 | €2.00 |
| Packaging + wiring diagram set | €1.20 | €0.80 |
| Freight + duty to EU | €1.00 | €0.70 |
| Certification amortised (~€28k: EN 60730 / LVD, EMC, RED, EN 18031) | €28.00 | €5.60 |
| Tuya licence/cloud (estimate, confirm current terms) | €1.00 | €0.80 |
| **Landed cost** | **€61.70** | **€31.10** |
| Net price ex-VAT: to service partner €110 (partner sells at €179 + install) / OEM €65 | €110 / €65 | €110 / €60 |
| **Gross margin** | **€48 (44%) partner / €3 (5%) OEM** | **€79 (72%) partner / €29 (48%) OEM** |

Clear message: at 1k units, OEM pricing doesn't work because certification is front-loaded. Start with the service-partner retrofit route; offer OEM pricing from 5k/yr commitments.

### Go-to-market
**First 100 customers:**
- **Refrigeration and bakery-equipment service companies** in one region (DE/AT or NL/BE): visit 10, demo on a real cabinet, offer a 20-unit pilot price.
- **Bakery trade fairs and bakery-guild events** (the large international bakery fair in Germany and national trade shows); bakery trade press.
- **Bread and pizza communities:** artisan-baker forums and social groups where people discuss retarding schedules. They generate demand that service partners then fulfil.
- **Bakery schools and master-baker training centres:** they influence what young bakers buy.

**Scale channels:** OEM integration with 1–2 small cabinet makers, used-equipment refurbishers ("refurbished cabinet with app"), and bakery-equipment dealer networks.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question: 10 service/equipment companies interviewed; 2 pilot commitments; works-like controller on one real retarder-proofer in a partner workshop |
| Q2 | Custom PCB, probe housing for condensing environments, Tuya app (or own UI); EVT 20 units in 10 bakeries via partners |
| Q3 | DVT; EN 60730/LVD, EMC, RED, EN 18031 testing; programme library from real bakers |
| Q4 | 1,000 units; partner training; first OEM design-in conversation with data from 6 months in the field |

**Team:** founder (B2B sales to service companies, bakery domain helps a lot), 1 embedded engineer (control loops, mains I/O, safety), part-time refrigeration technician adviser (wiring, safety chain), part-time app integrator.

**Funding to the first 1,000 units (estimates):** NRE €55k (electronics + safety €20k, firmware incl. control loops €20k, Tuya app configuration/branding €5k, enclosure + probe tooling €10k) + certification €28k + 1,000 units landed ex-cert ~€33k + 9 months lean costs €35k ≈ **€151k**; minus partner pilot deposits (~€25k) → **~€125k**. Route: partner pre-orders, food-tech/craft innovation grants, a small angel from the bakery-equipment world.

### Top risks
| Risk | Mitigation |
|---|---|
| **Safety/liability: modifying a commercial appliance** | Technician-installed only; controller never bypasses the cabinet's safety chain; wiring guides per cabinet type; product liability insurance; the installer documents the modification |
| **Technical: humidity sensor in a condensing, flour-dusty environment** | Protective PTFE filter cap, heated or ventilated probe housing, drift check against a reference each service visit, sensor as a replaceable part |
| **Technical: control quality (overshoot, humidity spikes when the door opens)** | PID per stage with door-open hold; tune on 3 cabinet types |
| **Cloud dependency (Tuya)** | Local-first logic; Tuya-free SKU; contract on data region and continuity |
| **Market: service companies don't want a new product to support** | Give them margin (installation + resale), training, and a remote-diagnosis view (fewer call-outs) |
| **Food safety claims** | "HACCP-style temperature history" = a record, not a certified HACCP system; the bakery stays responsible |
| **Supply: Tuya module, TH09C** | Dual footprint (Tuya/ESP32); a second humidity sensor footprint (common I²C RH sensors) |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Tuya CBU Wi-Fi + BLE module | https://www.gongbans.com/db/tuya-cbu.html | Certified Wi-Fi 4 + BLE 5.2 (BK7231N), ADC, SPI, 5 PWM, 2 UART, 21 pins; Tuya app/cloud | Datasheet public (Tuya developer docs); design files via maker | Tuya developer account + commercial terms; app features depend on Tuya cloud |
| HopeRF TH09C humidity/temperature sensor | https://www.gongbans.com/db/hoperf-th09c.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sensor/TH09C) | Cabinet T/RH: I²C, ±2 %RH, ±0.15 °C typical, 1.71–3.6 V | Datasheet + demo code | MIT (HopeRF repo) |
| Seeed Grove-Solid State Relay V2 | https://www.gongbans.com/db/seeed-grove-solid-state-relay-v2.html | Reference SSR drive circuit for heater/humidifier switching | Schematic | Seeed open hardware licence; check before copying |
| Hi-Link HLK-5LSxx 5 W isolated AC-DC | https://www.gongbans.com/db/hilink-5lsxx.html | Isolated supply for the controller: 85–265 VAC in, 3.3/5/12 V out, 3000 VAC isolation, 26.4×17.5×10 mm (per Hi-Link) | Datasheet public; files via maker | Commercial module; CE/RoHS per Hi-Link, keep their reports for your file |

### Block diagram
```
[TH09C T/RH probe (filtered housing)] --I2C--> [Tuya CBU (BK7231N)  OR  ESP32-C3 (Tuya-free)]
[door contact] --GPIO-->                         |  local programmes, PID per stage, alarms
[display + 4 buttons] <-->                       |
                                                 |--> [relay] --> existing compressor CONTACTOR (cabinet safety chain untouched)
                                                 |--> [SSR]   --> heater (with cabinet's thermal limiter in series)
                                                 |--> [SSR/relay] --> humidifier / steam generator
                                                 `--> [relay] --> fan
[230 V] -> [HLK-5LSxx isolated 5 W] -> 5 V / 3.3 V
                                                 ~~ Wi-Fi ~~> [Tuya cloud + white-label app]  OR  [local web UI / own cloud]
```
**Engineering gap:** two-stage control (cool/heat/humidify with interlocks: never heat and cool at once, compressor anti-short-cycle timer), humidity control with condensation-proof sensing, door-open handling, programme editor that bakers understand, history storage and export, wiring kits per cabinet family, and the Tuya data-point model or your own UI.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Tuya CBU module (or ESP32-C3 module) | €1.80–2.50 | Tuya terms per device |
| TH09C sensor + PTFE-filtered probe housing + cable | €3.50 | Probe housing is the hard part, not the chip |
| Relays 16 A ×2 + SSR ×2 with heatsink | €7.00 | Derate for hours-long heater duty |
| HLK-5LS05 (5 W) isolated AC-DC | €2.00 | |
| Display (segment LCD or small OLED) + buttons | €2.50 | Readable with flour on the front |
| Terminals, fuse, MOV, PCB, door-contact input | €3.00 | |
| Enclosure (panel cut-out standard size) | €3.50 | Fit common thermostat cut-outs where possible |

### Firmware/software starting point
- **Tuya SKU:** TuyaOS/Tuya device SDK for the CBU (search Tuya developer docs for "CBU" and "TuyaOS"), define data points per stage; Tuya's white-label app configurator for the partner's brand.
- **Tuya-free SKU:** ESP-IDF or ESPHome on ESP32-C3 (ESPHome has PID climate and humidity components); or OpenBeken for BK7231N (search "OpenBK7231T_App"; check the licence before commercial use).
- **Sensor:** HopeRF's TH09C demo code in the GitHub folder.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** interview 10 equipment/service companies; ask for a 20-unit pilot and whether a Tuya-cloud app is acceptable to their customers. Pass: 2 pilot commitments (paid or LOI with price) |
| 3–5 | Works-like | Devkit controller wired to one real retarder-proofer in a partner workshop: holds 3 ± 1 °C overnight, proofs at 26 ± 1 °C / 80 ± 5 %RH, switches stage on schedule; app shows state |
| 6–8 | Looks-like + EVT | Custom PCB, panel enclosure, filtered probe; 10 units in 5 bakeries via partners; zero lost batches attributable to the controller |
| 9–10 | DVT + pre-compliance | EN 60730 pre-assessment (temperature rise, creepage, relay endurance), EMC pre-scan, RED/EN 18031 gap analysis; humidity sensor drift after 4 weeks < 3 %RH |
| 11–12 | Pilot batch | 30–50 units installed by 2 partners; each partner orders the next 50; programme library with ≥10 baker-made programmes |

### Certification checklist (EU)
- **LVD / safety:** EN 60730-1 (+ relevant part 2) for the controller as an automatic electrical control. The modified cabinet must still meet its appliance standard (EN 60335-1 plus the relevant part 2 for commercial refrigerating or catering appliances: check which applies); the installer/partner documents the modification. Est. **€7–10k**.
- **EMC:** EN 301 489 (radio) + EN 55014-1/-2 (appliance controls). Est. **€4–6k**.
- **CE under RED:** 2.4 GHz Wi-Fi/BLE (EN 300 328; reuse Tuya's module reports), RF exposure. Est. **€3–5k**.
- **RED delegated act cybersecurity EN 18031-1 (and -2 if staff/owner accounts and data are processed).** Est. **€6–10k**. Request Tuya's security documentation.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: OTA, SBOM, vulnerability handling, support period (bakery equipment lives 15+ years, so commit to a realistic period and say what happens after).
- **RoHS, REACH, WEEE, packaging registration.**
- **Food:** the controller doesn't touch food. The probe housing inside the cabinet should use food-area-suitable materials (check EU 1935/2004 if it can contact dough or trays). Temperature history supports, but doesn't replace, the bakery's HACCP plan.
- **GDPR:** staff/owner app accounts; Tuya EU region + DPA, or self-hosted.
- **Total estimate: €20–31k.**

### Validation toolkit
- **Kill question:** Will 2 bakery-equipment makers or service companies buy a 20-unit pilot? And is a Tuya-cloud app acceptable to their customers? Ask before building.
- **Cheapest experiment (~€150):** a devkit with a T/RH logger in 3 bakeries' existing cabinets for 2 weeks, showing the real temperature/humidity swings overnight. Bring that chart to service companies.
- **5-question interview (service company / equipment maker):**
  1. How many proofing/retarder cabinets do you service, and how old are their controllers?
  2. What do bakers complain about most: night shifts, humidity, breakdowns?
  3. Do you replace controllers today? Which ones, at what price?
  4. Would your customers accept an app that runs on a Chinese IoT cloud, or do they need local-only?
  5. 20 controllers at €110 each for a pilot: who signs that, and when?
- **Landing-page headline (for bakers, routed to partners):** "Sleep until 5. Your dough doesn't need you at 3."
  - Retards overnight, proofs on schedule, holds humidity.
  - Alerts if the door's open or humidity drifts.
  - Temperature history for your HACCP folder. Installed by your service technician.
- **Pass threshold:** 2 paid partner pilots (20 units each) within 8 weeks; ≥50 baker sign-ups on the landing page in one region to show partners the pull.

### First production checklist
- **Samples:** relay endurance test (≥100k cycles at rated load for the compressor contactor coil), TH09C batch accuracy at 75–85 %RH, probe housing condensation test.
- **Golden sample:** fully wired controller with tested programmes, measured temperature rise, firmware version / Tuya product ID.
- **DFM review:** creepage/clearance, terminal block spacing for technicians, front panel sealing against flour and wipe-down, probe cable strain relief.
- **MOQ talk:** Tuya module (licence quantities, product ID registration), relays, LCD, probe housings.
- **QC/AQL:** AQL II 0.65 safety (100% hi-pot, relay function), 1.0/2.5 otherwise; 100% sensor check against a reference chamber point; 100% Wi-Fi pairing.
- **Packaging:** controller, probe, door contact, wiring diagrams for the 3 most common cabinet types, partner installation checklist.
- **Incoterms:** FCA Shenzhen; small air shipments for pilots; consider DDP for partners who don't import.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 4 board publishers (Tuya Smart (涂鸦智能) and HopeRF (华普微) and Seeed Studio and Hi-Link (海凌科)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Tuya Smart (涂鸦智能)** (涂鸦智能模组部门, developer.tuya.com) — platform + module maker; 151 boards in the catalogue; files via Tuya Smart public module documentation · https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber. Directory entry: WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side. Boards used here: [Tuya CBU Wi-Fi + Bluetooth LE module](/db/tuya-cbu.html) (Wi-Fi + BLE module running the app connection). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF TH09C relative humidity and temperature sensor](/db/hoperf-th09c.html) (humidity and temperature sensor). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Solid State Relay V2](/db/seeed-grove-solid-state-relay-v2.html) (heater / humidifier switching reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)](/db/hilink-5lsxx.html) (isolated AC-DC for the controller). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Tuya Smart (涂鸦智能) and HopeRF (华普微) and Seeed Studio and Hi-Link (海凌科) websites)

```email
Subject: Sample order and volume pricing — Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS) — for a Proofing-Cabinet Controller

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Proofing-Cabinet Controller: A drop-in controller for bakery proofing and retarder cabinets that holds temperature and humidity on a schedule ('retard overnight, proof from 4 a.m.') and lets the baker check from bed. The design is built around your Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS).

Could you please send:
1. Price and lead time for [10] sample units of each: Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS).
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
主题：样品订购及批量报价 — Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS) — 用于Proofing-Cabinet Controller

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Proofing-Cabinet Controller：A drop-in controller for bakery proofing and retarder cabinets that holds temperature and humidity on a schedule ('retard overnight, proof from 4 a.m.') and lets the baker check from bed。产品设计基于贵司的Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)。
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
Subject: PCBA quote from open design files — Proofing-Cabinet Controller, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Proofing-Cabinet Controller: A drop-in controller for bakery proofing and retarder cabinets that holds temperature and humidity on a schedule ('retard overnight, proof from 4 a.m.') and lets the baker check from bed. The design starts from published open-hardware files (Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Proofing-Cabinet Controller，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Proofing-Cabinet Controller：A drop-in controller for bakery proofing and retarder cabinets that holds temperature and humidity on a schedule ('retard overnight, proof from 4 a.m.') and lets the baker check from bed。设计基于已公开的开源硬件文件（Tuya CBU Wi-Fi + Bluetooth LE module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Solid State Relay V2, HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. List 15 bakery-equipment service companies in one region and book 10 calls; ask the Tuya-cloud question directly.
2. Order a Tuya CBU dev kit, 5 TH09C samples (or any I²C RH sensor for now) and an ESP32-C3 devkit; log a real cabinet overnight.
3. Get a 30-minute review from a refrigeration technician on the safety chain and wiring concept before drawing the PCB.

Want help sourcing or building this? Talk to us via www.gongbans.com.
