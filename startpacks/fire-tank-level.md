# Fire-Water Tank Level (radar, LoRaWAN) — Founder Start Pack

> A battery radar sensor on the hatch of a sprinkler or fire-water tank that reports the level over LoRaWAN, so the facility manager knows the reserve is full without climbing onto the tank.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Thousands of fire-water reserves in Europe (underground fire-water tanks, above-ground sprinkler tanks, fire ponds on farms, campsites, industrial estates, wind farms and rural villages) are checked by hand: someone lifts a hatch, looks or dips a stick, and writes it down. Leaks, evaporation, theft of water and failed refill valves go unnoticed until an inspection or, worse, a fire.
- **Customer:** Fire-protection service companies (sprinkler and fire-water maintenance contractors) buy, install and bundle it into inspection contracts. Facility managers of warehouses, farms, campsites and industrial estates pay. Municipalities own the rural fire ponds and underground tanks.
- **Product:** A battery-powered sensor that mounts in the hatch or a vent opening. A 24 GHz liquid-level radar (Hi-Link LD2413, ±3 mm, −40 to +85 °C per the brochure) measures once or twice a day, and a LoRa radio sends it over public or private LoRaWAN. Outputs: a daily level, a "leak trend" alert, tamper/hatch-open and battery status, and a monthly PDF report for the inspection file.
- **Why now:** Insurers and fire authorities want documented proof of the reserve; inspections are manual and staff are scarce. A low-power 24 GHz level-radar module that names fire-water tanks as an application exists. LoRaWAN coverage is good in much of NL, DE, BE, FR and the Nordics.
- **The ask:** About €130k (estimate) to reach 1,000 units. Route: pilot contracts with 3 fire-protection service companies (they pre-pay their first batch), a regional innovation grant, then a strategic investor from the fire-protection or metering world.

**Positioning: a monitoring aid, not a certified fire-safety component.** It doesn't replace the wired low-level switches that sprinkler standards require, or the mandated inspections.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 3 fire-protection service companies trial 10 units each and bundle them into their inspection contracts?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Facility managers of warehouses, farms, industrial estates and campsites with fire-water reserves; fire-protection service companies.

**The problem as the pack states it:** Thousands of fire-water reserves in Europe (underground fire-water tanks, above-ground sprinkler tanks, fire ponds on farms, campsites, industrial estates, wind farms and rural villages) are checked by hand: someone lifts a hatch, looks or dips a stick, and writes it down. Leaks, evaporation, theft of water and failed refill valves go unnoticed until an inspection or, worse, a fire.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **FPA, Fire Protection Association (UK)** · https://www.thefpa.co.uk/ — fire-safety professionals.
- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199 + network (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how facility managers of warehouses, farms, industrial estates and campsites with fire-water reserves deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you check the level of your fire-water tank today, who climbs up to do it, and what did the last inspection say?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A battery radar sensor on the hatch of a sprinkler or fire-water tank that reports level over LoRaWAN — so the facility manager knows the reserve is full without climbing on the tank. On a scale of one to ten, how likely would you be to buy that at €149–199 + network (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Fire-Water Tank Level (radar, LoRaWAN): would you pay €149–199 + network (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Fire-Water Tank Level (radar, LoRaWAN): A battery radar sensor on the hatch of a sprinkler or fire-water tank that reports level over LoRaWAN — so the facility manager knows the reserve is full without climbing on the tank. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–199 + network (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Sprinkler tanks in larger buildings usually already have **wired level switches into the fire panel**. Don't fight that. The real gap is **unwired reserves**:
- Underground fire-water tanks (in Germany built to DIN 14230) at rural industrial estates, farms, logistics sites and wind farms.
- Fire ponds and open reserves in villages without a strong hydrant network (municipal fire-safety duty).
- Above-ground tanks at campsites, holiday parks, farms with straw/hay storage, and agricultural cooperatives.
- Secondary/backup reserves at sites where the sprinkler tank is wired but the second reserve isn't.

Buyer: **the fire-protection service company** that inspects these reserves. Every manual visit costs them travel and time, and they lose contracts when a reserve fails. With a sensor they can sell "remote monitoring + annual visit" instead of quarterly visits. The facility manager pays a monthly fee through the service contract.

### Market size (estimates)
- Unwired fire-water reserves in the EU (tanks, ponds, cisterns at industrial, agricultural, municipal and leisure sites): no clean statistic; estimate **300k–600k** reserves (Germany alone has a large number of Löschwasserbehälter and fire ponds; check with national fire-service associations).
- **TAM:** 450k × €179 ≈ **€80 M** hardware + €3/month monitoring ≈ €16 M/year.
- **SAM:** NL, DE, BE, AT, FR, DK with LoRaWAN coverage and an active fire-protection service industry, ~35% → **€28 M** hardware.
- **SOM (3 years):** 3% of SAM → ~4,700 units → **~€840k** hardware + ~€170k/year service.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Industrial radar level transmitters (4–20 mA/HART) wired to a PLC or telemetry unit | €800–2,500 + cabling + telemetry | Overkill and needs power and cabling at a remote tank |
| LoRaWAN level sensors for utilities/industry (e.g. [Lobaro at ~€830 ex-VAT](https://iot-shop.de/en/shop/lob-3000701-lobaro-800089-lorawan-level-sensor-4981), submersible probes) | €300–830 | Expensive; submersible probes need maintenance; generic, not fire-reserve reports |
| Ultrasonic LoRaWAN tank sensors | €150–300 | Condensation and wide beams in narrow shafts; not built for this use case |
| Float switch + GSM alarm | €100–250 + SIM | Binary: only knows "below the switch"; no trend, no leak detection |
| Manual inspection (hatch + dipstick) | Labour €40–120 per visit (estimate) | That's what we replace and document |

**Wedge:** €179, battery-powered (5+ years target at 2 readings/day), installs through a standard hatch in 15 minutes, needs no cabling, and produces a **fire-reserve report** the inspector and insurer understand. Sold through the service companies who already visit these tanks.

### Product & value proposition
- **Radar:** Hi-Link LD2413 24 GHz liquid-level radar (0.15–10 m, ±3 mm, ±12° beam, 3.3 V at 23 mA for a 160 ms measurement, UART, −40 to +85 °C, per the brochure). The low energy per reading makes a multi-year primary battery feasible.
- **Radio:** HopeRF RFM95W LoRa (868 MHz) for LoRaWAN Class A; the M5Stack Unit LoRaWAN-EU868 for the pilot.
- **Power:** Li-SOCl2 D-cell or a 2× C pack; 2 readings/day + 1 uplink/day; adaptive (more often if the level drops fast).
- **Mechanics:** IP67/IP68 housing for the hatch (humid, sometimes flooded shafts), a universal hatch bracket, an external antenna option for underground tanks (the antenna must reach above ground level or into the hatch frame).
- **Software:** a LoRaWAN codec, a web dashboard for service companies (multi-site, multi-customer), alerts (below threshold, leak trend over 7 days, no reading 48 h, hatch open/tamper via an accelerometer or light sensor), and an automatic monthly PDF per reserve.

**Pricing (estimates):** €179 sensor (list), €149 to service companies; €3/month per reserve for the dashboard + reports (or white-labelled for the service company at €2). Installation by the service company (their margin).

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (LD2413 radar, RFM95W, low-power MCU, accelerometer, Li-SOCl2 D-cell, antenna + cable, PCB) | €34.00 | €27.00 |
| Assembly & test (radar distance jig, LoRaWAN join test, potting) | €4.00 | €2.80 |
| Enclosure IP68 + hatch bracket + radome | €8.00 | €5.20 |
| Packaging | €1.20 | €0.80 |
| Freight + duty to EU (lithium cells → DG) | €2.80 | €1.80 |
| Certification amortised (~€22k: RED 24 GHz + 868 MHz, EMC, IP68, battery docs) | €22.00 | €4.40 |
| **Landed cost** | **€72.00** | **€42.00** |
| Net price to service company | €149 | €135 |
| **Gross margin (hardware)** | **€77.00 (52%)** | **€93.00 (69%)** |
| Dashboard service (€3/month, ~€0.40 cost incl. network fees) | ~€31/year | ~€31/year |

### Go-to-market
**First 100 customers (units):**
- **3 fire-protection service companies** (regional, 20–100 staff) in NL/DE: 10 free units each on their worst-to-reach reserves for 6 months. Success = they bundle the sensor into renewals.
- **Rural municipalities** with fire ponds and underground tanks: a pilot through the municipal fire-safety officer, with LoRaWAN coverage from a regional or community network.
- **Wind-farm and solar-park operators** (they're often required to provide fire water on remote sites).
- **Trade fairs** for fire protection (Interschutz-type events) and facility-management events.

**Scale channels:** national associations of fire-protection service companies, tank manufacturers (factory-fit the sensor option on new underground fire-water tanks), metering/IoT integrators, and insurers' risk-engineering teams (who recommend it to policyholders).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question asked to 10 service companies; 10 works-like units in 3 real tanks/ponds; radar behaviour in narrow shafts tested |
| Q2 | Custom PCB + IP68 housing; dashboard v1 + PDF; EVT 30 units with 3 service companies |
| Q3 | DVT; RED/IP68 testing; pilot 300 units; first renewal bundled |
| Q4 | 1,000 units; tank-manufacturer factory-fit talks; second country |

**Team:** 1 embedded/RF engineer (low power, radar, LoRaWAN), 1 full-stack developer (dashboard, reports, multi-tenant), the founder on B2B sales into the fire-protection trade (a former fire-protection technician is ideal). Buy in mechanical design.

**Funding to the first 1,000 units (estimates):** NRE €50k (PCB €10k, IP68 tooling + bracket €15k, firmware €10k, dashboard €15k) + certification €22k + 1,000 units landed ~€50k + 9 months lean costs €60k ≈ **€182k**. Subtract service-company first orders (300 × €149 ≈ €45k, 50% upfront) and a regional innovation voucher (~€10–20k) → **~€130k**. Route: customer prepayments + grant + an angel from fire protection or metering.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** radar in narrow shafts (riser walls, ladders, inlet pipes inside the ±12° beam) | False-echo mapping at install ("learn empty structures" routine), mount position guidance; test in 10 different tanks before EVT |
| **Technical:** LoRaWAN from underground tanks | External antenna in the hatch frame or a short cable to a pole; check coverage per site; private gateway option for estates |
| **Technical:** condensation/foam/ice on the surface or the radome | Hydrophobic radome, slight tilt; ice detection via temperature + flat-line signal; −40 °C rated radar |
| **Regulatory:** customers treat it as a certified fire-safety device | Clear labelling: "monitoring aid; doesn't replace required level switches, fire-panel connections or inspections". Contract terms with service companies |
| **Market:** service companies see it as a threat to visit revenue | Position it as a contract-renewal tool and a premium service; let them white-label the dashboard |
| **Supply:** single-source radar; long life expected (10 years in the field) | Ask Hi-Link for lifecycle info; design for a second-source 24 GHz level radar; stock for spares |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD2413 24 GHz liquid-level radar | https://www.gongbans.com/db/hilink-ld2413.html | Level measurement 0.15–10 m, ±3 mm, low energy per reading, −40 to +85 °C; fire-water tanks named as an application | **Datasheet public, files via maker** (no open schematic/PCB) | Commercial module |
| HopeRF RFM95/96/98(W) | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | LoRaWAN radio for the production design; CE/FCC reports, footprint and 3D model in the folder | PCB footprint, demo code, datasheet | MIT (HopeRF repo) |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | Ready LoRaWAN EU868 unit for the works-like pilot | Enclosure/structure only (no main-board electronics) | Buy for prototyping |

0 of 3 boards publish full schematic/PCB files; HopeRF publishes the footprint and docs under MIT.

### Block diagram
```
                     [Li-SOCl2 D-cell (+ buffer cap)] -> [load switches]
                                                             |
[LD2413 24 GHz radar] --UART--> [low-power MCU] --SPI--> [RFM95W 868 MHz] -> [antenna: hatch frame / cable to pole]
[accelerometer / light sensor: hatch-open tamper] -->    |            ~~LoRaWAN~~> [network server] -> [dashboard + alerts + monthly PDF]
[temperature sensor: ice flag] ----------------------->  |
```
**Engineering gap:** the measurement and the radio exist. What's missing: a multi-year power design (radar and radio fully switched off between readings), false-echo handling for real tanks, an install routine, the IP68 mechanics and antenna solution for underground hatches, and the service-company dashboard and report. Half the value is the software.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD2413 | €12–16 | **Sole-source module**; request the lifecycle statement |
| RFM95W-868 | €4.50 | Or a LoRa SoC module to merge MCU + radio |
| Low-power MCU (STM32L0/L4 class) | €1.80 | |
| Li-SOCl2 D-cell 19 Ah + hybrid layer capacitor | €7.50 | DG shipping; EU sourcing possible |
| Accelerometer + temp sensor | €0.80 | |
| Antenna + 1 m cable + connector | €2.50 | |
| PCB, load switches, passives, potting | €3.00 | |
| IP68 housing + bracket + radome | €8.00 | Tooling ~€10–15k |

### Firmware/software starting point
- **LoRaWAN:** LoRaMac-node (github.com/Lora-net/LoRaMac-node) or the STM32CubeWL/LoRaWAN middleware; for quick tests use the M5Stack Unit LoRaWAN-EU868's AT commands from any MCU.
- **Network server:** The Things Stack or ChirpStack (open source) for private deployments; public LoRaWAN operators exist in several EU countries.
- **Radar:** LD2413 UART protocol document from Hi-Link.
- **Dashboard:** any time-series DB + a small multi-tenant web app; PDF via a server-side HTML-to-PDF tool. Search "LoRaWAN payload codec TTN" for the codec format.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** will 3 fire-protection service companies trial 10 units each and consider bundling them into their inspection contracts? Interview 10, get 3 signed trial letters. Bench: LD2413 reading a water barrel ±5 mm |
| 3–5 | Works-like | 10 units (radar + M5 LoRaWAN unit + battery) in 3+ real tanks/ponds; readings vs dipstick within ±1 cm; uplink success ≥98% incl. underground sites; energy per day measured → ≥5-year battery model |
| 6–8 | Looks-like + EVT | Custom PCB, IP68 housing, hatch bracket, antenna solution; 30 EVT units across the 3 service companies; dashboard + first monthly PDF |
| 9–10 | DVT + pre-compliance | RED pre-scan (24 GHz + 868 MHz), EMC; IP68 immersion; −30 °C cold test; false-echo routine validated in 5 tank types |
| 11–12 | Pilot batch | 50 paid units; service companies' feedback on reports; ≥1 company quotes "remote monitoring" in a renewal |

### Certification checklist (EU)
- **CE under RED:** 24 GHz radar (module's standard per Hi-Link, e.g. EN 300 440 or EN 302 372/EN 302 729 for tank/level-probing radar; **ask the lab which applies to an in-tank sensor**), 868 MHz EN 300 220-1/-2 (duty cycle!), EMC EN 301 489-1/-3, safety EN 62368-1 (battery-only, light), exposure EN 62479. Est. **€10–16k**.
- **RED delegated act (EN 18031-1):** LoRaWAN end nodes connected via a network server are in a debated scope. Do a gap analysis/self-assessment (~€3–6k).
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Secure join keys per device, an update path (at least local), SBOM, vulnerability contact.
- **IP68** (EN 60529) with stated depth/time; UV resistance if outdoors.
- **Battery Regulation (EU) 2023/1542:** an industrial or portable battery depending on size and use; labelling, take-back, removability. UN 3091 shipping (lithium metal in equipment).
- **Explosion protection:** fire-water tanks are normally non-Ex, but some sites (fuel depots, chemical plants) are ATEX zones. **Exclude Ex zones** in your terms unless you certify ATEX (expensive).
- **Fire-safety standards:** the product isn't a component under EN 12845 (sprinklers) or DIN 14230 (underground fire-water tanks). Say so, and let the service company decide how it fits their inspection regime.
- **RoHS, REACH, WEEE**, packaging registration. **GDPR:** low (site contacts only).
- **Total certification budget estimate: €18–28k.**

### Validation toolkit
- **Kill question:** Will 3 fire-protection service companies trial 10 units each and bundle them into their inspection contracts?
- **Cheapest experiment (~€800):** 3 works-like units in a weatherproof box (LD2413 + M5 LoRaWAN unit + battery) on 3 reserves owned by one friendly service company or farm, plus a hand-made monthly PDF. Show the PDF to 10 service companies.
- **5-question interview (service company owner):** 1) How many unwired fire-water reserves do you look after, and how often do you visit them? 2) What does one visit cost you, and who pays? 3) When did a reserve last turn out to be low, and what happened? 4) Would your customers pay €3/month for a daily level + monthly report? 5) Would you install 10 units this quarter at €149 each?
- **Landing page headline:** "Is your fire-water reserve full? Know it every day." Bullets: "Radar level sensor for tanks, cisterns and fire ponds, battery-powered for years." / "Daily level, leak-trend and tamper alerts over LoRaWAN, no cabling." / "A monthly report for your inspection file and your insurer."
- **Pass threshold:** 3 service companies sign trial letters **and** at least 1 commits to a paid batch of 30+ after the trial.

### First production checklist
- **Samples:** golden sample with distance calibration (0.5/2/5 m on a jig), LoRaWAN join keys provisioning procedure, radar firmware frozen.
- **DFM review:** radome material/thickness for 24 GHz, potting vs gasket, cable gland, bracket for common hatch sizes.
- **MOQ talk:** radar modules, Li-SOCl2 cells (EU distributor for batch one), housing colours.
- **QC/AQL:** AQL II 1.0/2.5; 100% radar distance check, 100% LoRaWAN join + uplink, 100% current-in-sleep check (catch leakage early); 5% IP68 immersion per lot.
- **Packaging:** carton with bracket, fixings, install card + QR with DevEUI/JoinEUI on a label, battery warnings.
- **Incoterms:** FOB Shenzhen; ship units without cells and insert cells in the EU if DG costs are high.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2413 24 GHz liquid-level detection radar module](/db/hilink-ld2413.html) (24 GHz liquid-level radar (low power, specified for fire water tanks)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver for LoRaWAN uplink). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (ready LoRaWAN EU868 unit for the pilot run). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868) — for a Fire-Water Tank Level (radar, LoRaWAN)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Fire-Water Tank Level (radar, LoRaWAN): A battery radar sensor on the hatch of a sprinkler or fire-water tank that reports level over LoRaWAN — so the facility manager knows the reserve is full without climbing on the tank. The design is built around your HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868).
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
主题：样品订购及批量报价 — HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868) — 用于Fire-Water Tank Level (radar, LoRaWAN)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fire-Water Tank Level (radar, LoRaWAN)：A battery radar sensor on the hatch of a sprinkler or fire-water tank that reports level over LoRaWAN — so the facility manager knows the reserve is full without climbing on the tank。产品设计基于贵司的HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)。
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
Subject: PCBA quote from open design files — Fire-Water Tank Level (radar, LoRaWAN), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Fire-Water Tank Level (radar, LoRaWAN): A battery radar sensor on the hatch of a sprinkler or fire-water tank that reports level over LoRaWAN — so the facility manager knows the reserve is full without climbing on the tank. The design starts from published open-hardware files (HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Fire-Water Tank Level (radar, LoRaWAN)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fire-Water Tank Level (radar, LoRaWAN)：A battery radar sensor on the hatch of a sprinkler or fire-water tank that reports level over LoRaWAN — so the facility manager knows the reserve is full without climbing on the tank。设计基于已公开的开源硬件文件（HLK-LD2413 24 GHz liquid-level detection radar module, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 3× LD2413 samples and an M5Stack Unit LoRaWAN-EU868; measure a water barrel and log the energy per reading.
2. Call 10 regional fire-protection service companies with the interview script and ask for 3 trial reserves each.
3. Check LoRaWAN coverage at 5 candidate reserves (coverage maps, then a field test with the unit in a car).

Want help sourcing or building this? Talk to us via www.gongbans.com.
