# Frost Sentinel — Founder Start Pack

> A solar-powered post with Cat-M that texts the winegrower when canopy temperature hits the frost threshold — no platform subscription, no €1,400 weather station.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Spring frost kills a vintage in one night. The grower's choice today is a €1,400+ connected weather station with a yearly fee, a consumer thermometer they check at 3 a.m., or nothing. Small plots don't justify the station; they still lose the crop.
- **Customer:** Small and medium vineyards and orchards in DE/FR/AT/IT (and hop, berry, fruit growers). The grower pays once; the grower (or whoever is on frost duty) gets the SMS. Crop insurers and growers' associations are the channel.
- **Product:** A €169 post-mounted sensor: canopy-height temperature + humidity (dew point), solar + Li-ion, Cat-M/NB-IoT, SMS at a threshold the grower sets by replying to a text, a 5-year EU IoT SIM included. No app needed.
- **Why now:** Cat-M modules are cheap and pre-certified; the "one footprint, three module generations" design is documented; recent frost years pushed insurers toward monitoring; incumbents are quote-only and sell platforms ([Weenat](https://weenat.com/en/?p=289395), [Leova SMART](https://www.nordicsemi.com/Nordic-news/2022/11/the-leova-smart-employs-the-nrf9160-sip)).
- **The ask:** ~€85k (estimate) to the first 1,000 units; route = deposits at growers' association evenings before the season + bootstrap; an insurer co-marketing deal as the lever.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Ask 20 winegrowers at a growers' association evening: €149 one-off, SMS at −1 °C, no app — yes or no? Pass = 8 yes with a deposit.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Small and medium vineyards and orchards in DE/FR/AT/IT; crop insurers as channel.

**The problem as the pack states it:** Spring frost kills a vintage in one night. The grower's choice today is a €1,400+ connected weather station with a yearly fee, a consumer thermometer they check at 3 a.m., or nothing. Small plots don't justify the station; they still lose the crop.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The Farming Forum (UK)** · https://thefarmingforum.co.uk/ — UK farmers; machinery, arable, livestock, farm diversification.
- **Landtreff (DE)** · https://www.landtreff.de/ — German farmers' forum.
- **r/farming** · https://www.reddit.com/r/farming/ — working farmers.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–249, the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how small and medium vineyards and orchards in DE/FR/AT/IT deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about your last frost night: how did you find out it was happening, and what did you lose?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A solar-powered post with Cat-M that texts the winegrower when canopy temperature hits the frost threshold — no platform subscription, no €1,400 weather station. On a scale of one to ten, how likely would you be to buy that at €149–249, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Frost Sentinel: would you pay €149–249 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Frost Sentinel: A solar-powered post with Cat-M that texts the winegrower when canopy temperature hits the frost threshold — no platform subscription, no €1,400 weather station. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–249, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Frost protection (candles, wind machines, sprinklers, helicopters) only works if you start it in time, at the right plot. Plots differ by 2–3 °C between a hollow and a slope; the official forecast is for the town. The grower with 3–15 ha wants a cheap sensor per plot that wakes them up. They don't want a dashboard, an app, a login, or a yearly invoice.

Who pays vs who uses: the grower pays; the grower or a family member on frost duty uses it; the insurer may discount a policy; the cooperative may bulk-buy.

Segments: (1) winegrowers 2–20 ha (DE/AT/FR/IT — hundreds of thousands of holdings, most small); (2) orchards and berry growers (frost-prone blossom); (3) hop and nursery growers; (4) allotments/garden centres as a consumer spill-over.

### Market size (estimates)
- EU wine holdings: roughly 2 M holdings, most tiny; estimate **150k commercially active holdings ≥ 2 ha** in frost-prone regions; orchards/berries/hops add ~100k → **250k farms**, 2–4 sensors each → **~700k sensor sites**.
- **TAM:** 700k × €169 ≈ **€118 M** (one-off) plus SIM renewals after year 5.
- **SAM:** holdings that actively protect against frost (candles/wind/sprinklers) or are insured for frost — 25% → 175k sites → **€30 M**.
- **SOM (3 years):** 4% → 7,000 sites → **€1.2 M**, strongly seasonal (orders Dec–Mar).

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Connected ag weather stations (Sencrop, Weenat, Leova SMART — quote-only; AgTecher benchmarks field-sensor systems at €200–800 budget, €800–2,000 mid, [AgTecher](https://agtecher.com/fieldsensors/)) | Full platforms, forecasts, many sensors | Price per plot, yearly platform fee, app; built for 50 ha, not 5 |
| Frost-alarm loggers (HOBO-class kits ~€1,700) | Reliable | Price, dialler-era design |
| Consumer WiFi/BLE thermometers | €30–60 | No range in a vineyard, no SMS, no solar, no canopy mounting |
| Regional frost-warning services / forecasts ("do nothing") | Free | Town-level; 2–3 °C off per plot; no 3 a.m. wake-up |
| DIY LoRa/Cat-M sensor | Makers | No weatherproofing, no SIM logistics, nobody on call |

**Wedge:** the dumbest possible product: a post, a sensor, a text message. €169, SIM included for 5 years, threshold by SMS reply, 3 sensors per 10 ha instead of 1 station.

### Product & value proposition
Hardware: IP65 enclosure on a 1.5 m fibreglass or aluminium post with a ground spike or a clamp for existing trellis posts; radiation-shielded T/RH sensor at canopy height (shield is critical — radiant cooling fools unshielded sensors by 1–2 °C); 2 W solar panel + 2,000 mAh Li-ion (or LiFePO4 for cold); Cat-M/NB-IoT module with an EU multi-network IoT eSIM; RTC-timed wake (every 10 min in frost season, every hour otherwise), SMS when below threshold, "all clear" SMS at sunrise, daily low in one text, low-battery text. Settings by SMS reply ("SET -1" / "ADD +4917…"). Optional web page with the plot's history for those who want it.

Pricing (estimates): **€169 incl. 5-year SIM** (consumer/grower), 3-pack €449, cooperative/insurer bundles at €129 for 50+. SIM renewal after 5 years €29. No app, no subscription.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (Cat-M module €11, MCU €2, SHT3x-class T/RH €3.5, solar panel €3, Li-ion/LiFePO4 €4, charger + RTC + PCB €5) | €28.50 | €23.00 |
| 5-year IoT eSIM + SMS budget (prepaid) | €12.00 | €9.50 |
| Assembly & test (SMT, RF test, sensor check, network attach test) | €5.00 | €3.50 |
| Enclosure + radiation shield + post + clamp | €11.00 | €7.50 |
| Packaging (tube box, spike, quick card) | €2.50 | €1.80 |
| Freight + duty to EU (Li-ion DG) | €3.50 | €2.20 |
| Certification amortised (~€22k: RED via module + EN 301 489-52, safety, UN 38.3, IP65) | €22.00 | €4.40 |
| **Landed cost** | **€84.50** | **€51.90** |
| Sell price (direct €169 / bundle €129) | €169 | €129 |
| **Gross margin** | **€84.50 (50%)** | **€77.10 (60% at bundle)** |

Thin at 1k, acceptable at 5k. The SIM is the margin killer — negotiate hard (multi-network IoT eSIM at <€2/year with an SMS bundle is achievable at volume), and consider the "SIM renewal" as recurring income.

### Go-to-market
**First 100 customers:** 2–3 growers' association evenings in Jan–Feb (kill question: 8 of 20 say yes with a deposit); the regional wine institute's frost-protection advisers; cooperatives' winter meetings; vineyard-supply dealers (they sell frost candles — add a sensor); a demo video of a −1 °C night with the SMS arriving.

**Scale channels:** crop insurers (premium discount or bundle — the kill question's second half), cooperatives' bulk buys, vineyard and orchard supply catalogues, fruit-growers' associations; after one season, the orchards and hops.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 (Dec–Feb) | Works-like from Unit CatM + SHT31 Grove + a solar reference in an IP65 box on a post; association evenings; 50 deposits; 30 field units through this frost season. |
| Q2 | Own board (SIMCom footprint for 3 module generations), shield + post tooling, eSIM contract; EVT 50; pre-compliance; season data review. |
| Q3 | DVT, certification, 300-unit pilot build for next season; insurer conversation with season data. |
| Q4 | 1,000 units shipped for Dec–Feb selling; cooperative bundles; orchard variant (blossom-height mount). |

**Team:** 1 embedded/RF engineer (cellular, power budget, firmware — full-time), 1 mechanical/industrial designer (shield, post, enclosure — part-time), founder for growers and insurers, a viticulture adviser on contract for the threshold logic and the content. Two and a half people.

**Funding to first 1,000 units (estimates):** NRE €35k (PCB + RF €10k, enclosure/shield/post tooling €15k, firmware + SMS backend €10k) + certification €22k + SIM prepayment for 1,000 (€12k) + 1,000 units landed ~€85k + 9 months overhead €55k ≈ **€209k**; minus deposits/pre-season sales (~€60k) and pilot sales (~€45k) and insurer co-marketing (~€20k) ≈ **~€85k**. Bootstrap + deposits; agricultural innovation grants (regional/EU rural development) often fund the pilot season.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** sensor reads 1–2 °C high under radiant cooling → missed alarm | Proper radiation shield, canopy-height mount, compare against a reference thermometer for a season; publish accuracy |
| **Technical:** rural Cat-M coverage in hilly plots | Multi-network eSIM, NB-IoT fallback, external antenna option, "no signal" test at install via LED |
| **Technical:** winter solar budget | LiFePO4 for cold, 10-min duty only in season, deep sleep otherwise; model it, then measure a winter |
| **Market:** strongly seasonal, small ticket | Sell Dec–Mar, build Jul–Nov; orchards and hops stretch the season; SIM renewals smooth it |
| **Regulatory:** RED via module still needs EN 301 489-52 and EN 62368-1 on the product; Li-ion → UN 38.3 and battery regulation; CRA | Pre-certified module, keep RF layout to the vendor's reference, removable cell, signed firmware |
| **Liability:** "your sensor didn't text and I lost the crop" | Wording: an aid, not a guarantee; redundancy advice (2 sensors per plot); SMS delivery is best-effort — say it |
| **Supply:** cellular module generations change every 2–3 years | The SIMCom compatible-footprint approach — design the PCB to accept three module generations |
| **Licence:** OSHWHub solar board | Reference only; your own charge circuit |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit CatM (U128) | https://www.gongbans.com/db/m5stack-unit-catm.html | Cat-M/NB-IoT uplink for the works-like | enclosure/structure only; electronics not published | Buy; module vendor reference for production |
| SIMCom A7670/SIM7070/A7672X Compatible Design | https://www.gongbans.com/db/simcom-a7670-sim7070-compat-design.html | How one footprint accepts three cellular module generations | schematic | SIMCom reference — follow the vendor's terms |
| Seeed Grove TempAndHumi Sensor (SHT31) | https://www.gongbans.com/db/seeed-grove-tempandhumi-sensor-sht31.html | T/RH for dew-point and frost logic | schematic | Seeed wiki resources; check licence |
| solar-to-5v-zener-regulator (OSHWHub) | https://www.gongbans.com/db/oshwhub-solar-to-5v-zener-regulator.html | Solar charge-path reference | schematic, pcb (EasyEDA Pro on project page) | **OSHWHub — licence varies; read it**; crude regulator — use a proper MPPT-lite charger IC in production |

### Block diagram
```
[Shielded SHT3x-class T/RH at canopy height] --I2C--> [low-power MCU + RTC wake]
                                                           |
[2 W solar panel] -> [solar charger IC] -> [LiFePO4/Li-ion 2,000 mAh + protection + fuel gauge]
                                                           |
                                               [Cat-M/NB-IoT module (3-generation footprint) + eSIM + antenna]
                                                           |
                                                  SMS: alarm / all-clear / daily low / settings by reply
                                               [optional: tiny backend for history page + SIM management]
```
**Engineering gap:** the radiation shield and mounting (physics, not electronics), the winter power budget, SMS-based settings UX, the eSIM/SMS commercial deal, and the three-generation module footprint. Electronics are simple.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Cat-M/NB-IoT module (SIMCom SIM7070-class or A7672-class) | €11.00 | **Generations change; 3-footprint design**; pre-certified |
| Low-power MCU (STM32L0/ESP32-C3 in deep sleep) + RTC | €2.50 | |
| SHT3x-class T/RH sensor | €3.50 | Second-source alternatives on the same footprint |
| Solar panel 2 W + charger IC | €4.50 | |
| LiFePO4 or Li-ion cell 2,000 mAh + protection + gauge | €4.50 | UN 38.3 from vendor; LiFePO4 for −20 °C |
| Antenna (PCB or FPC) + RF passives | €1.20 | Follow module vendor layout |
| eSIM (MFF2) + 5-year multi-network plan | €12.00 | **The negotiation that decides the margin** |
| PCB 2–4 layer, passives | €2.50 | |
| IP65 enclosure + radiation shield + post + clamp | €11.00 | **Shield tooling €6–10k**; post off-the-shelf fibreglass |

### Firmware/software starting point
- Module control via AT commands; **TinyGSM** (Arduino, exists) supports SIMCom modules for a works-like; in production write a thin AT layer yourself.
- Sensirion publishes SHT3x drivers on GitHub (exists).
- SMS logic: send/receive via the module directly, or via the IoT SIM provider's SMS API (more reliable for delivery reports) — search your provider's docs.
- Dew-point and frost logic: standard formulas; the viticulture adviser sets the defaults (−1 °C wet-bulb, etc.).
- Backend (optional): a tiny service for history and SIM status; keep it optional so the product works with zero cloud.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 5 works-like units (Unit CatM + SHT31 + solar board + MCU) in IP65 boxes on posts; **20 growers asked at an association evening — 8 say yes with a €30 deposit** |
| 3–5 | Works-like | 30 units in the field through cold nights; alarm SMS within 10 min of crossing threshold; sensor within ±0.5 °C of a shielded reference overnight; battery holds through 10 cloudy days |
| 6–8 | Looks-like + EVT | Own PCB with 3-generation footprint; shield + enclosure T1; 50 units; RF pre-scan; settings-by-SMS tested by 10 growers unaided |
| 9–10 | DVT + pre-compliance | EN 301 489-52 / EN 62368-1 pre-compliance; IP65 test; UN 38.3 report; power budget modelled vs measured; eSIM contract signed |
| 11–12 | Pilot batch | 50 units to deposit holders before the next frost window; ≥ 90% of alarms delivered; 0 false "all clear" |

### Certification checklist (EU)
- **CE under RED** (cellular): module pre-certified, but the product needs **EN 301 489-1/-52**, EN 62311 (RF exposure), and **EN IEC 62368-1**; carrier approval rides on the module. Est. €6–10k RED/EMC + €3–5k safety.
- **EN 18031:** applies if the device is "internet-connected" — a Cat-M device that sends SMS only is a grey zone; if you add the optional backend it clearly applies (-1, €10–15k). Decide early; a pure SMS product keeps scope narrow — get a notified body's opinion.
- **Battery:** UN 38.3 for the cell; **EU Battery Regulation** labelling and the 18 Feb 2027 removability rules → removable cell pack.
- **RoHS, REACH, WEEE**, packaging; **IP65** test (IEC 60529) €1–2k.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027 — signed firmware, FOTA via cellular, vulnerability contact.
- **GDPR:** phone numbers of growers are personal data → minimal storage, privacy notice; no camera/mic.
- **Total certification budget estimate: €12–30k** depending on the EN 18031 decision.

### Validation toolkit
- **Kill question:** Ask 20 winegrowers at a growers' association evening: €149–169 one-off, SMS at −1 °C, no app — yes or no? Pass = 8 yes with a deposit.
- **Cheapest experiment (~€600):** 5 works-like units, a 60-second video of a frost night and the SMS arriving, a one-page sheet, and a €30 deposit QR at two association evenings in January.
- **5-question interview (grower):** 1) What did the last frost cost you, and how did you find out it was freezing? 2) How many plots do you protect, and how do you decide when to start? 3) Who is on frost duty at night, and what do they use? 4) Have you looked at a weather station — why didn't you buy one? 5) €169 once with 5 years of SMS included, threshold set by text message — would you put one on each plot?
- **Landing page:** headline "Know it's freezing in your vineyard before the forecast does." Bullets: "Canopy-height sensor on a post; a text message at your threshold, and an all-clear at sunrise." / "Solar powered, SIM included for 5 years. No app, no subscription." / "€169. Put one on every plot that behaves differently."
- **Pass threshold:** 8 of 20 deposits at the first evening, or 100 deposits before 1 March.

### First production checklist
- Samples: 5 golden samples with sensor calibration, RF attach logs on 3 networks, and a 14-day power log.
- DFM: shield airflow vs rain ingress, gland for the sensor cable, panel angle, post clamp for 40–80 mm trellis posts, battery door with a seal.
- MOQ talk: modules 1k (ask for the next generation's sample too), eSIMs 1k with the 5-year plan, cells 1k with UN 38.3, shield + enclosure 1k.
- QC: AQL II 2.5/4.0; 100% network attach + SMS loop test; 100% sensor plausibility at ambient; 5% IP spray check; 24 h solar/battery soak on 2%.
- Packaging: UN 3481 marking; post in a tube; quick card with "text SET -1".
- Incoterms: FOB Shenzhen; air (DG-rated) for 50; sea for the season batch — ship by September to sell in December.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and SIMCom and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit CatM (U128)](/db/m5stack-unit-catm.html) (Cat-M/NB-IoT uplink). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **SIMCom** — solution house; 3 boards in the catalogue; files via SIMCom module hardware designs · https://www.simcom.com/technical_files-p110.html. Boards used here: [SIMCom A7670/SIM7070/A7672X Compatible Design](/db/simcom-a7670-sim7070-compat-design.html) (shows one footprint accepting three cellular module generations). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-TempAndHumi Sensor-SHT31](/db/seeed-grove-tempandhumi-sensor-sht31.html) (T/RH for dew-point and frost logic). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [solar-to-5v-zener-regulator](/db/oshwhub-solar-to-5v-zener-regulator.html) (solar charge path reference).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Luat (Air105/Air780)** (深圳市合宙通信有限公司) · openluat.com — LTE Cat-1 / NB-IoT module OEM: Air780E Cat-1 bis module; Air105 MCU; MQTT/TLS; OEM/ODM. *(Cellular (Cat-1 / NB-IoT) modules)*
- **LILYGO** (深圳市合宙通信有限公司) · lilygo.cc — ESP32 / LoRa / cellular dev module OEM: T-SIM7670 / T-Watch / TTGO LoRa boards; OEM module supply. *(Cellular (Cat-1 / NB-IoT) modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and SIMCom and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit CatM (U128), SIMCom A7670/SIM7070/A7672X Compatible Design, Seeed Grove-TempAndHumi Sensor-SHT31 — for a Frost Sentinel

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Frost Sentinel: A solar-powered post with Cat-M that texts the winegrower when canopy temperature hits the frost threshold — no platform subscription, no €1,400 weather station. The design is built around your M5Stack Unit CatM (U128), SIMCom A7670/SIM7070/A7672X Compatible Design, Seeed Grove-TempAndHumi Sensor-SHT31.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit CatM (U128), SIMCom A7670/SIM7070/A7672X Compatible Design, Seeed Grove-TempAndHumi Sensor-SHT31.
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
主题：样品订购及批量报价 — M5Stack Unit CatM (U128), SIMCom A7670/SIM7070/A7672X Compatible Design, Seeed Grove-TempAndHumi Sensor-SHT31 — 用于Frost Sentinel

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Frost Sentinel：A solar-powered post with Cat-M that texts the winegrower when canopy temperature hits the frost threshold — no platform subscription, no €1,400 weather station。产品设计基于贵司的M5Stack Unit CatM (U128), SIMCom A7670/SIM7070/A7672X Compatible Design, Seeed Grove-TempAndHumi Sensor-SHT31。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit CatM (U128), SIMCom A7670/SIM7070/A7672X Compatible Design, Seeed Grove-TempAndHumi Sensor-SHT31。
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
Subject: PCBA quote from open design files — Frost Sentinel, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Frost Sentinel: A solar-powered post with Cat-M that texts the winegrower when canopy temperature hits the frost threshold — no platform subscription, no €1,400 weather station. The design starts from published open-hardware files (solar-to-5v-zener-regulator; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Frost Sentinel，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Frost Sentinel：A solar-powered post with Cat-M that texts the winegrower when canopy temperature hits the frost threshold — no platform subscription, no €1,400 weather station。设计基于已公开的开源硬件文件（solar-to-5v-zener-regulator；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 5× Unit CatM, 5× SHT31 Grove, a prepaid IoT SIM, 5 IP65 boxes and 5 fibreglass posts; have one unit texting you a temperature by day 7.
2. Find the next 3 growers' association or wine institute evenings in Jan–Feb in your region and get a 10-minute slot; prepare the deposit QR.
3. Request quotes from three multi-network IoT eSIM providers for 1,000 × 5 years with 500 SMS/year — the answer decides your price point.

Want help sourcing or building this? Talk to us via www.gongbans.com.
