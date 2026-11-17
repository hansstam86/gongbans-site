# Livestock Trough Level (radar, LoRa) — Founder Start Pack

> A solar radar sensor that hangs over a water trough in a remote pasture and tells the farmer when the trough is low or the float valve is stuck, so nobody has to drive to every field every day.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Checking troughs is a daily chore on beef, sheep and horse farms with scattered fields. It's 30–90 minutes and a diesel bill every day, and in a heat wave an empty trough becomes an animal-welfare emergency within hours.
- **Customer:** Livestock and equestrian farms in IE, UK, FR, NL and DE with grazing away from the yard; land managers and conservation-grazing contractors. The farmer pays and uses it; for estates and contractors the farm manager signs.
- **Product:** A solar-powered unit on a bracket over the trough. A 79 GHz radar measures the water level (non-contact, no dirty probe), and a LoRa radio sends it hourly. The app/SMS alerts on low level, on no refill after a drop (stuck valve or burst pipe) and on suspected ice.
- **Why now:** mm-accurate 79 GHz level-radar modules now cost what an ultrasonic sensor did, and they don't foul. Public and community LoRaWAN coverage is spreading in rural Europe, and a €150–300 farm gateway covers the rest. Heat waves keep making the news.
- **The ask:** About €150k (estimate) to reach 1,000 units. Get there with farm-show pre-orders, an agri-innovation grant (EIP-AGRI operational groups, national rural-development schemes) and an agri-dealer partner.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 20 farmers in one region with LoRaWAN coverage pre-order at €149? Test at a livestock show with a working demo trough.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Beef, sheep and horse farmers, equestrian centres, land managers in IE, UK, FR, NL, DE.

**The problem as the pack states it:** Checking troughs is a daily chore on beef, sheep and horse farms with scattered fields. It's 30–90 minutes and a diesel bill every day, and in a heat wave an empty trough becomes an animal-welfare emergency within hours.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The Farming Forum (UK)** · https://thefarmingforum.co.uk/ — UK farmers; machinery, arable, livestock, farm diversification.
- **Landtreff (DE)** · https://www.landtreff.de/ — German farmers' forum.
- **r/farming** · https://www.reddit.com/r/farming/ — working farmers.
- **r/Equestrian** · https://www.reddit.com/r/Equestrian/ — horse owners and yard managers.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€129–169 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how beef, sheep and horse farmers, equestrian centres, land managers in IE, UK, FR, NL, DE deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you check the water troughs in your far fields today, how often do you drive out for it, and when did you last find one empty or overflowing?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A solar radar sensor that hangs over a water trough in a remote pasture and tells the farmer when the trough is low or the float valve is stuck — saving daily drives to every field. On a scale of one to ten, how likely would you be to buy that at €129–169 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Livestock Trough Level (radar, LoRa): would you pay €129–169 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Livestock Trough Level (radar, LoRa): A solar radar sensor that hangs over a water trough in a remote pasture and tells the farmer when the trough is low or the float valve is stuck — saving daily drives to every field. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €129–169 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Start with **suckler-beef and sheep farms in Ireland and the UK**: many fragmented fields, a long grazing season and plenty of float-valve troughs. The second segment is **equestrian yards and livery** in NL/DE/UK, where owners pay for welfare and peace of mind. The third is **conservation grazing** (nature-reserve contractors), who have remote sites and documentation duties.

The farmer is the user and the payer. The trigger is the hot week when a trough ran dry, or the hire of a second worker just to do rounds.

### Market size (estimates)
- EU + UK cattle and sheep holdings: ~1.5–2 M (Eurostat farm structure data puts EU bovine holdings at roughly 1 M+; treat this as an estimate). Assume 25% graze fields far enough from the yard to need checks → **~400k farms**, averaging 4 troughs worth monitoring.
- **TAM:** 400k × 4 × €149 ≈ **€240 M** hardware, plus optional connectivity/app fees.
- **SAM:** farms in IE/UK/FR/NL/DE with LoRaWAN coverage or willing to buy a gateway, ~30% → **€70 M**.
- **SOM (3 years):** 1% of SAM → ~4,700 units → **~€700k** hardware revenue.

### Competition
| Alternative | Price (listings, estimate in €) | Weakness we attack |
|---|---|---|
| Dedicated LoRa trough/tank sensors from Australian agtech (e.g. listings at AU$256–545 on the [NSW DPI AgTech catalogue](https://www.agtech.dpi.nsw.gov.au/collections/all/products/lora-water-sensor)) | €155–330 | Mostly ultrasonic (spider webs, condensation, foam); often a subscription; sold for the Australian market |
| Industrial LoRaWAN level sensors (submersible or radar, e.g. [Lobaro at €829 ex-VAT](https://iot-shop.de/en/shop/lob-3000701-lobaro-800089-lorawan-level-sensor-4981), Milesight submersibles) | €300–830 | Priced for utilities; submersible probes foul in trough water and get chewed |
| Float switch + GSM alarm | €80–150 + SIM | Binary (empty/not empty), SIM costs per field, no refill logic |
| Trail cameras pointed at the trough | €100–200 | You still have to look at the photos |
| Do nothing: drive round | Free + diesel + 1 h/day | That's the cost we replace: 1 h/day × 365 is ~€5k+/year of labour |

**Wedge:** non-contact radar (no fouling, nothing in the water), refill-logic alerts instead of a raw level graph, priced at €149 with **no mandatory subscription**, and it works on public LoRaWAN *or* your own €150–300 gateway.

### Product & value proposition
- **Sensor head:** Hi-Link LD7901B 79 GHz level radar (0.15–15 m, 1 mm theoretical accuracy, narrow 8/7° beam, UART, low current per the brochure) pointing down through a radome window. The narrow beam matters on a small trough.
- **Radio:** HopeRF RFM95W (868 MHz) for LoRaWAN, or point-to-point to a farm-yard base.
- **Power:** a small 1–2 W panel + LiFePO4 cell, or a primary lithium pack for shaded sites. Wake hourly, take 10 readings, take the median, send, sleep.
- **Smarts (in the cloud or the base):** low-level alert; **"dropped but not refilled within X min" = stuck valve or supply failure**; "constantly full + rising water use upstream" = leak (if you also meter the supply, later); temperature sensor → "ice suspected" in winter; heat-wave mode (readings every 15 min).
- **Mounting:** a galvanised bracket that clamps to the trough rim, out of reach of cattle tongues (they will lick and push it).

**Pricing (estimates):** €149 per sensor RRP (€129 early bird / show price); €249 farm gateway + 3 sensors bundle at €599; optional €2/sensor/month for SMS alerts. Agri-dealer channel at 30% off.

### Unit economics (estimates per sensor, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (LD7901B radar, RFM95W, MCU, solar panel 1–2 W, LiFePO4 + charger, temp sensor, antenna, PCB) | €38.00 | €30.00 |
| Assembly & test (incl. radar distance check on a jig) | €4.50 | €3.00 |
| Enclosure (UV-stable PC/ASA, radome window, IP67 gasket) + galvanised bracket | €9.50 | €6.50 |
| Packaging (box, cable ties, quick-start) | €1.50 | €1.00 |
| Freight + duty to EU | €2.50 | €1.60 |
| Certification amortised (~€25k: RED for 79 GHz + 868 MHz, EMC, IP67, battery docs) | €25.00 | €5.00 |
| **Landed cost** | **€81.00** | **€47.10** |
| Net price after channel (direct €123 ex-VAT / dealer €86) | €123 | €86 |
| **Gross margin** | **€42.00 (34%)** | **€38.90 (45%)** |

The bracket is a hidden cost. Source it locally (EU sheet-metal shop) if freight on steel kills you.

### Go-to-market
**First 100 customers:**
- **Livestock shows and ploughing championships** (big ones in IE, UK and FR): a working demo trough with the sensor and a phone showing the alert live. Take deposits on the stand.
- **Farmer discussion groups / knowledge-transfer groups** (common in Ireland and the UK): one group of 15 farms is a perfect pilot cohort.
- **Equestrian Facebook groups and livery-yard owners** in NL/DE.
- **Local LoRaWAN community networks** that already cover rural areas: they want useful farm use cases and will promote you.

**Scale channels:** agri-merchants and co-op stores (country stores), farm-fencing and water-system installers (they install the troughs anyway), and agri-IoT platforms that want a trough sensor in their catalogue (white label).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test at a winter/spring show; works-like on 10 troughs in one region; radar readings vs a ruler in dirty, windy, frozen conditions |
| Q2 | Custom PCB, bracket, enclosure; EVT 50 units with a farmer discussion group; LoRaWAN payload codec; alert logic tuned |
| Q3 | DVT, RED/IP67 testing; pilot 200 units before the summer heat; dealer talks |
| Q4 | 1,000 units; one agri-merchant chain; gateway bundle; winter (ice) firmware |

**Team:** 1 embedded/RF engineer (radar + LoRa + low power), 1 app/backend developer (part-time OK if you use an existing LoRaWAN network server and a simple alert app), and the founder, ideally with farm credibility, on sales. Buy in mechanical design.

**Funding to the first 1,000 units (estimates):** NRE €55k (PCB €12k, enclosure + bracket tooling €18k, firmware/app €25k) + certification €25k + 1,000 units landed ~€56k + 9 months lean costs €60k ≈ **€195k**. Subtract show pre-orders (200 × €129 ≈ €26k) and a 50% agri-innovation grant on NRE/certification (~€25–40k where available) → **~€130–150k**. Route: grant + pre-orders + an angel from the agri-supply world.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** radar on a small, splashy trough (cows drinking, foam, leaves, ice) | Median of 10 readings; ignore readings while animals drink (variance filter); ice flag from temperature + flat signal. Test 20 troughs in week 3–5 |
| **Technical:** LD7901B rated −15 °C (B version per brochure); winters can go lower | Check the datasheet with Hi-Link; heater not affordable on solar, so accept "offline below −15 °C" or qualify the C version / another module |
| **Technical:** power budget in Irish/UK winter sun | Size the cell for 3 weeks of no sun; adaptive interval (less often when level is stable) |
| **Market:** farmers won't pay for "another app" | SMS-first alerts; no subscription for basic use; demonstrate saved diesel/hours |
| **Regulatory:** 79 GHz radar is allowed for level-probing radar (LPR) and short-range radar uses, but confirm the module's exact category | Ask Hi-Link for the module's RED test report and intended-use statement; test the complete product |
| **Supply:** single-source radar module, licence of the OSHWHub solar design | Second-source a 60/80 GHz level radar; don't copy the OSHWHub zener circuit (inefficient). Use it only as a reference and design a proper MPPT/charger stage |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD7901B/LD7901C 79 GHz water-level radar | https://www.gongbans.com/db/hilink-ld7901b.html | The level measurement: 0.15–15 m, 1 mm theoretical accuracy, 8/7° beam, UART, 3.3 V | **Datasheet public, files via maker** (no open schematic/PCB) | Commercial module; buy it, check the datasheet terms |
| HopeRF RFM95/96/98(W) LoRa module | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | 868 MHz LoRa/LoRaWAN uplink, 164 dB link budget; CE/FCC reports in the folder | PCB footprint, 3D model, demo code, datasheet | MIT (HopeRF repo) |
| OSHWHub solar-to-5v-zener-regulator | https://www.gongbans.com/db/oshwhub-solar-to-5v-zener-regulator.html | Starting reference for the solar power stage (learn from it, then replace it) | schematic, PCB (EasyEDA project) | **Check the OSHWHub project licence before commercial use** |

### Block diagram
```
          [1-2 W solar panel] -> [MPPT/charger] -> [LiFePO4 cell] -> [3.3 V buck]
                                                                         |
[LD7901B 79 GHz radar] --UART--> [low-power MCU (STM32L0/L4 class)] --SPI--> [RFM95W 868 MHz] ~~LoRaWAN~~> [gateway / public network]
[temp sensor (ice flag)] ------>        |                                                                        |
                                 [load switch: radar off between readings]                         [network server -> alert app / SMS]
```
**Engineering gap:** the radar, radio and a rough power reference exist. What's missing: the power design (radar duty-cycling with a load switch, MPPT for a small panel, winter budget), signal filtering for animals and ice, the mechanical bracket/radome that survives cattle, the LoRaWAN codec and the alert logic (refill detection). Plan ~40% mechanical/field work, ~40% firmware/app, ~20% PCB.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD7901B radar module | €14–18 | **Sole-source module**; ask for the volume price and lifecycle commitment |
| RFM95W-868 | €4.50 | HopeRF; RFM95W pin-compatible alternatives exist |
| Low-power MCU (STM32L0/L4 class) | €1.80 | Or use an LoRa SoC module to merge MCU + radio |
| Solar panel 1–2 W, UV-stable | €4.00 | Specify an encapsulated panel, not a cheap PET laminate |
| LiFePO4 cell 1–1.5 Ah + charger/MPPT IC | €5.50 | LiFePO4 copes with cold charging limits better; still block charging below 0 °C |
| Temp sensor, load switch, passives, PCB | €3.00 | |
| 868 MHz antenna (external, up high) | €1.50 | Antenna height decides range |
| IP67 enclosure + radome + bracket | €9.50 | Tooling ~€12–18k |

### Firmware/software starting point
- **LoRaWAN stack:** LoRaMac-node (Semtech, github.com/Lora-net/LoRaMac-node) or the STM32 LoRaWAN middleware; for Arduino prototyping, search "MCCI LoRaWAN LMIC".
- **Network server:** The Things Stack (community or commercial) or ChirpStack (open source) for a private farm gateway.
- **Radar:** Hi-Link's UART protocol document comes with the module; request the latest one from the maker.
- **Alerts:** start with a simple webhook → SMS service (search "SMS API EU"). A Node-RED flow is fine for the pilot.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Demo trough at a show or discussion-group meeting; **20 farmers in one region with LoRaWAN coverage pre-order at €149** (deposit). Bench: radar module reading a bucket with ±5 mm repeatability |
| 3–5 | Works-like | 10 dev-kit units (radar + RFM95 + MCU, battery powered) on 10 real troughs; readings vs manual dip-stick within ±1 cm; refill/stuck-valve alert works; 0 missed packets over a week at ≥1 km |
| 6–8 | Looks-like + EVT | Custom PCB + IP67 housing + bracket; 50 units; cattle-proof bracket test; 3-week no-sun power test (dark box) |
| 9–10 | DVT + pre-compliance | RED pre-scan for 79 GHz and 868 MHz (duty cycle ≤1% in the g1 sub-band); IP67 immersion; UV/thermal cycling −20 to +60 °C |
| 11–12 | Pilot batch | 50 paid units across 10 farms; alert precision ≥95% (alerts that were real); farmer NPS; dealer interest letter |

### Certification checklist (EU)
- **CE under RED:** 79 GHz radar: check which harmonised standard the module was tested to (e.g. the EN 302 729 level-probing radar family or EN 305 550 for short-range devices in that band; confirm with the lab). 868 MHz: EN 300 220-1/-2. EMC: EN 301 489-1/-3. Safety: EN 62368-1 (low voltage). Exposure: EN 62311/62479. Est. **€12–20k**, more if the radar needs a full test at a lab with 79 GHz equipment (not every lab has it).
- **RED delegated act (EN 18031-1):** it applies if the device is "internet-connected". A LoRaWAN end node talks via a gateway to a network server; labs and notified bodies are still debating the scope. Budget for a self-assessment (~€3–6k with consultant help).
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Firmware update path (LoRaWAN FUOTA is hard; plan at least a local update via USB/BLE), SBOM, vulnerability handling.
- **IP67** (EN 60529) test report; UV resistance of plastics.
- **RoHS, REACH, WEEE**, packaging registration.
- **Battery Regulation (EU) 2023/1542:** portable battery labelling, removability (design a battery door), take-back. UN 38.3 for the cell.
- **GDPR:** low risk (water levels). The farmer's phone number and farm location are personal data; use EU hosting and a short privacy notice.
- **Animal welfare:** don't claim it *ensures* welfare compliance; it's a monitoring aid.
- **Total certification budget estimate: €20–35k.**

### Validation toolkit
- **Kill question:** Do 20 farmers in one region with LoRaWAN coverage pre-order at €149? Test at a livestock show with a working demo trough.
- **Cheapest experiment (~€600):** one works-like unit on a demo trough you can drain and refill on the stand, a phone showing the SMS alert, a price card and a deposit QR code. Pick a region where a coverage map shows public LoRaWAN, or bring a gateway.
- **5-question interview (farmer):** 1) How many troughs do you check, how often, and how long does the round take? 2) When did a trough last run dry or overflow, and what happened? 3) Is there mobile or LoRa coverage in those fields? 4) Which alert would you act on: low, stuck valve or overflow? 5) €149 per trough, no subscription: how many would you buy for this summer?
- **Landing page headline:** "Know every trough is full — without driving there." Bullets: "Radar measures the water level without touching it. Nothing to clean, nothing to chew." / "Alerts you if a trough runs low or the valve sticks." / "Solar-powered, works on LoRaWAN, no subscription."
- **Pass threshold:** 20 deposits (€25 each) from one region in 6 weeks, or one farmer discussion group committing to a 15-farm pilot.

### First production checklist
- **Samples:** golden sample with calibration record (distance jig at 0.3/0.6/1.0 m), radar firmware version noted; ask Hi-Link to freeze the module firmware for your order.
- **DFM review:** radome thickness/material tuned for 79 GHz (thin, low-loss plastic, no metallic paint); gasket design; bracket corrosion protection (hot-dip galvanised or stainless).
- **MOQ talk:** radar module MOQ and lead time; solar panel custom size MOQ (often 1k); enclosure colour.
- **QC/AQL:** AQL II 1.0/2.5; 100% radar distance test on a jig, 100% LoRa join test, 100% charge test; 5% IP67 dunk test per lot.
- **Packaging:** recyclable carton, bracket in the box, fixings, quick-start card with the QR for app onboarding (pre-registered DevEUI on a sticker).
- **Incoterms:** FOB Shenzhen for electronics; brackets sourced in the EU if cheaper landed; LiFePO4 as UN 3481 (in equipment).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and HopeRF (华普微)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD7901B/LD7901C 79 GHz water-level detection radar module (4T4R)](/db/hilink-ld7901b.html) (79 GHz water-level detection radar (low current)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver for LoRaWAN or point-to-point). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [solar-to-5v-zener-regulator](/db/oshwhub-solar-to-5v-zener-regulator.html) (simple open solar-to-5 V regulator design for the power stage).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) websites)

```email
Subject: Sample order and volume pricing — HLK-LD7901B/LD7901C 79 GHz water-level detection radar module (4T4R), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module — for a Livestock Trough Level (radar, LoRa)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Livestock Trough Level (radar, LoRa): A solar radar sensor that hangs over a water trough in a remote pasture and tells the farmer when the trough is low or the float valve is stuck — saving daily drives to every field. The design is built around your HLK-LD7901B/LD7901C 79 GHz water-level detection radar module (4T4R), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD7901B/LD7901C 79 GHz water-level detection radar module (4T4R), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module.
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
主题：样品订购及批量报价 — HLK-LD7901B/LD7901C 79 GHz water-level detection radar module (4T4R), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module — 用于Livestock Trough Level (radar, LoRa)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Livestock Trough Level (radar, LoRa)：A solar radar sensor that hangs over a water trough in a remote pasture and tells the farmer when the trough is low or the float valve is stuck — saving daily drives to every field。产品设计基于贵司的HLK-LD7901B/LD7901C 79 GHz water-level detection radar module (4T4R), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD7901B/LD7901C 79 GHz water-level detection radar module (4T4R), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module。
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
Subject: PCBA quote from open design files — Livestock Trough Level (radar, LoRa), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Livestock Trough Level (radar, LoRa): A solar radar sensor that hangs over a water trough in a remote pasture and tells the farmer when the trough is low or the float valve is stuck — saving daily drives to every field. The design starts from published open-hardware files (solar-to-5v-zener-regulator; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Livestock Trough Level (radar, LoRa)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Livestock Trough Level (radar, LoRa)：A solar radar sensor that hangs over a water trough in a remote pasture and tells the farmer when the trough is low or the float valve is stuck — saving daily drives to every field。设计基于已公开的开源硬件文件（solar-to-5v-zener-regulator；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 2× LD7901B samples, 2× RFM95W modules and an STM32 Nucleo; get a bucket reading to ±5 mm on your desk and log the current draw per reading.
2. Check LoRaWAN coverage maps for three target regions and pick the one with the best coverage and the most livestock.
3. Book a stand or a slot at the next farmer discussion group or livestock show and build the demo trough (a plastic trough, a float valve and a drain tap).

Want help sourcing or building this? Talk to us via www.gongbans.com.
