# Field-Edge Wildlife Alarm — Founder Start Pack

> A motion radar on a post at the field edge that detects wild boar or deer entering a crop at night, triggers lights or sound deterrents and pings the farmer (and the hunter) over LoRa.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

**Two honest corrections to the original idea before you start:**
1. **Range.** The Hi-Link LD016 in the catalogue is a 5.8 GHz Doppler sensor with **6–10 m detection at 3 m mounting height** (adjustable). That is not "field-edge long range". It works as a **gate sensor on known game trails** (where boar enter the field: gaps in hedges, trails out of the forest, ditch crossings), not as a perimeter scanner. Design around trails, or qualify a longer-range radar.
2. **Deterrents habituate.** Field research and hunting associations in DE/CH report that acoustic and light scarers work only for a limited time, and that hunting pressure on the damaged field is the most effective measure ([ZHAW acoustic deterrent research](https://www.zhaw.ch/de/lsfm/ueber-uns/aktuell-medien/news/detailansicht/event-news/wildschweinschaeden-mit-akustischer-methode-verhindern), [LJV Baden-Württemberg](https://www.landesjagdverband.de/fileadmin/Medien/LJV/Bilder/1__Aktuell/2026/20260527_Wenn-die-Milchreife-zur-Herausforderung-wird/Wenn-die-Milchreife-zur-Herausforderung-wird_JBW_2606.pdf)). So the core value is **the alert to the hunter at the right moment**, with deterrents as a randomised secondary function.

## 1. Summary

- **Problem:** Wild boar destroy maize, cereals and grassland in a few nights, especially when maize is in the milk stage. Farmers and hunters don't know *when* and *where* the animals enter. Hunters sit for many nights in vain; camera traps need SD-card checks or expensive 4G plans, and cameras on field edges photograph walkers (privacy).
- **Customer:** In Germany and several neighbouring countries the **hunting-ground tenant often pays for game damage on farmland** (the details depend on national/regional hunting law and the lease contract). That makes the **hunter/hunting tenant** a strong buyer, alongside **arable and maize farmers**, vineyards and orchards in DE, PL, FR, BE, AT.
- **Product:** A solar post unit with a 5.8 GHz motion radar aimed along a game trail, night-only arming, a LoRa radio that sends "movement at trail 3, 23:41" to the farmer and the hunter, and a configurable output for a light/sound deterrent or relay. Several posts per field form a simple trail map; an event log shows *when* animals come.
- **Why now:** Wild-boar populations and damage stay high; African swine fever pressure keeps authorities pushing for more effective boar hunting; LoRa radios and Doppler radars cost a few euros; no camera = no privacy problems with walkers.
- **The ask:** About €120–160k (estimate) to the first 1,000 posts, via season pre-orders from hunting associations, an agri-innovation grant and one angel from the hunting/agri-supply trade.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does a radar alert actually lead to less damage? Pilot with 3 farms and their hunting association for one season; without measurable damage reduction, it's a toy.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Arable and maize farmers, vineyards, orchards and hunting associations in DE, PL, FR, BE, AT where wild-boar damage is severe.

**The problem as the pack states it:** Wild boar destroy maize, cereals and grassland in a few nights, especially when maize is in the milk stage. Farmers and hunters don't know *when* and *where* the animals enter. Hunters sit for many nights in vain; camera traps need SD-card checks or expensive 4G plans, and cameras on field edges photograph walkers (privacy).

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **DJV, Deutscher Jagdverband (DE)** · https://www.jagdverband.de/ — German hunters' association; wild-boar damage on crops is a standing topic.
- **FACE** · https://www.face.eu/ — European federation of hunting associations.
- **Landtreff (DE)** · https://www.landtreff.de/ — German farmers' forum.
- **The Farming Forum (UK)** · https://thefarmingforum.co.uk/ — UK farmers; machinery, arable, livestock, farm diversification.
- **r/farming** · https://www.reddit.com/r/farming/ — working farmers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199 per post (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how arable and maize farmers, vineyards, orchards and hunting associations in DE, PL, FR, BE, AT where wild-boar damage is severe deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last night wild boar or deer got into a field: when did you find out, what did it cost, and what have you tried to keep them out?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A long-range motion radar on a post at the field edge that detects wild boar or deer entering a crop at night, triggers lights or sound deterrents and pings the farmer over LoRa. On a scale of one to ten, how likely would you be to buy that at €149–199 per post (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Field-Edge Wildlife Alarm: would you pay €149–199 per post (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Field-Edge Wildlife Alarm: A long-range motion radar on a post at the field edge that detects wild boar or deer entering a crop at night, triggers lights or sound deterrents and pings the farmer over LoRa. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–199 per post (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Primary buyer: the **hunting-ground tenant** (or a group of hunters sharing a district) who pays game-damage compensation and wants to sit at the right spot on the right night. Secondary: **farmers** with high-value crops (maize, vineyards, orchards, potatoes) who want proof and early warning. Third: **hunting associations / district hunting groups** for shared systems in ASF-related efforts.

User: whoever gets the alert — hunter on the phone, farmer in the morning summary.

### Market size (estimates)
- Germany alone has hundreds of thousands of licensed hunters and tens of thousands of hunting districts; similar structures exist in AT, PL, FR, BE. Assume ~150k hunting districts across the core countries with significant boar damage in maybe 30% → **~45k districts**, 4 posts each.
- **TAM:** 45k × 4 × €169 ≈ **€30 M** hardware + optional alert service.
- **SAM:** districts with LoRaWAN coverage or willing to buy a gateway, DE/AT/PL first, ~30% → **~€9 M**.
- **SOM (3 years):** 3% of SAM → ~1,600 posts → **~€270k**. A niche — but hunters spend money on equipment readily (thermal optics, cameras), and the season makes demand predictable.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| 4G trail cameras with app alerts | €150–400 + SIM/subscription | Monthly costs per camera, photograph walkers (privacy/legal issues on public paths), battery drain, no coverage in some fields |
| Acoustic/light wildlife scarers (e.g. randomised sound devices for crops) | €100–500 | Habituation; no information for the hunter; neighbours complain about noise |
| Electric fencing around high-value fields | €1–3 per metre + labour | Effective but labour-intensive; not practical around every maize field |
| Thermal binoculars + sitting every night | €1,500–5,000 + time | Works when you are there; most nights you're there for nothing |
| Do nothing: pay the damage | €100s–€1,000s per hectare damaged | That's what we reduce |

**Wedge:** **"know when they come, without a camera or a SIM"**: low-cost trail radars over LoRa, a nightly event log, and an instant alert so the hunter sits on the right nights. Deterrent output as an extra, randomised to slow habituation.

### Product & value proposition
- **Sensor:** Hi-Link HLK-LD016 — 5.725–5.875 GHz Doppler motion sensor, TX −5 dBm, 5 V / 20 mA, detection 6–10 m (adjustable), UART config, 2 GPIO, −30 to +80 °C, 20 × 20 × 12 mm. Mount low (0.6–1 m) along the trail, angled to reduce triggers from swaying crops. Test the false-alarm rate with maize moving in the wind — Doppler sensors see moving leaves.
- **Radio:** HopeRF RFM95W (868 MHz LoRa) for LoRaWAN or direct to a small farm/hunter base station. For pilots: M5Stack Unit LoRaWAN-EU868.
- **Power:** 2–3 W solar panel + LiFePO4; the radar draws ~20 mA continuously at night → ~0.25 Ah per night plus the deterrent; size for 5 dark days.
- **Logic:** night-only arming (light sensor/clock), sensitivity per trail, "event" = sustained movement for N seconds (ignore single blips), daily summary, instant alert option, deterrent output (12 V switched: light bar, sound module) with random timing.
- **Optional:** a second radar per post facing the other way; temperature for context; a "hunter mode" that suppresses the deterrent so the animals are not scared away while the hunter is coming.

**Pricing (estimates):** €169 per post (radar + LoRa + solar); €449 starter kit with 3 posts + gateway set-up help; deterrent add-on €49. Optional SMS alert service €3/post/month.

### Unit economics (estimates per post, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (LD016, RFM95W, MCU, light sensor, LiFePO4 + charger, 2–3 W panel, relay/MOSFET output, antenna, PCB) | €30.00 | €23.00 |
| Assembly & test | €4.00 | €2.80 |
| Enclosure (UV-stable, IP66) + post clamp | €7.00 | €4.80 |
| Packaging | €1.50 | €1.00 |
| Freight + duty to EU | €2.20 | €1.50 |
| Certification amortised (~€18k) | €18.00 | €3.60 |
| **Landed cost** | **€62.70** | **€36.70** |
| Net revenue (direct €142 ex-VAT; hunting-supply dealer €100) | €142 | €100 |
| **Gross margin** | **€79.30 (56%)** | **€63.30 (63%)** |

### Go-to-market
**First 100 customers:**
- **Hunting fairs** (large ones in Germany and Austria each winter/spring): demo with a radar on a post and a phone showing the alert.
- **District hunting groups / hunting association chapters:** offer a 3-district pilot in a known boar-damage region before the maize milk stage; publish the results in hunting magazines.
- **Farmer–hunter pairs:** the farmer suffers the damage, the hunter pays it → they often want to cooperate. Sell the starter kit to the pair.
- **Hunting forums and online communities**, plus the big hunting-equipment webshops' review sections.

**Scale:** hunting-supply retailers (online + stores), agri-merchants, and agricultural chambers' advisory services.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like posts; false-alarm tests (wind, crops, rain, deer vs boar); 3 pilot districts signed |
| Q2 | EVT 30 posts installed **before the maize milk stage**; alert + log app; hunting-mode logic |
| Q3 | The pilot season itself: measure alerts → successful hunts → damage area vs previous year; DVT + RED testing in parallel |
| Q4 | 1,000 posts produced for next season; dealer listings; pilot report published |

**Team:** founder with hunting/farming credibility, 1 embedded engineer (radar signal + LoRa + solar), part-time app developer (alerts, event log). A wildlife biologist as advisor for the pilot design.

**Funding to the first 1,000 posts (estimates):** NRE €45k (PCB + firmware €25k, enclosure/clamp tooling €10k, app €10k) + certification €18k + 1,000 posts landed ~€40k + pilot costs €10k + 12 months lean costs €40k ≈ **€155k**. Minus pre-orders for next season (300 × €150 ≈ €45k) and an agri/wildlife-management innovation grant (€20–50k) → **~€60–90k** funding. Route: bootstrap + pre-orders + grant + hunting-trade angel.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** false alarms from moving crops, rain, foxes, deer | Low mounting along trails, sustained-motion logic, per-post sensitivity; accept "animal" alerts and let the hunter judge |
| **Technical:** 6–10 m range only covers trails, not fields | Sell per trail; qualify a longer-range radar later; multiple posts per field |
| **Market:** no measurable damage reduction | Kill question: one-season pilot with damage measured vs previous year and vs control fields |
| **Regulatory:** hunting law (e.g. rules about electronic aids at night, feeding sites, protected periods), noise/animal-protection rules for deterrents | Position as information device; check each country's hunting law with associations; deterrents optional and within noise limits |
| **Theft/vandalism** in open fields | Low-profile housing, camouflage colours, cheap enough to lose occasionally |
| **Supply:** sole-source radar | Doppler 5.8 GHz modules are widely available; keep the footprint generic |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD016 5.8 GHz motion radar | https://www.gongbans.com/db/hilink-ld016.html | Night motion detection on a trail (6–10 m, adjustable) | **Datasheet public, files via maker** (no open schematic/PCB) | Commercial module; ask Hi-Link for the UART config protocol and RED report |
| HopeRF RFM95/96/98(W) LoRa module | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | 868 MHz LoRa/LoRaWAN alerts | PCB footprint/library, datasheet, demo code | MIT (HopeRF GitHub repo) |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | Quick LoRaWAN for the pilot units | Enclosure/structure files only — main-board electronics not published | Prototype only |

### Block diagram
```
[2-3 W solar] -> [LiFePO4 charger] -> [LiFePO4 cell] -> [3.3 V / 5 V rails]
                                                              |
[LD016 5.8 GHz radar] --GPIO/UART--> [low-power MCU] --SPI--> [RFM95W 868 MHz] ~~LoRaWAN~~> [gateway] -> [server] -> [hunter/farmer app + SMS]
[light sensor (night arming)] ----->        |
                                   [MOSFET/relay 12 V out] -> [optional light bar / sound module (random timing)]
```
**Engineering gap:** the false-alarm logic (the hardest part in fields), solar power budget with the radar on all night, the post clamp/enclosure, the alert app with hunter mode, and pilot methodology to prove damage reduction.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD016 | €2.00–3.00 | Doppler radars are widely available; second-source easily |
| RFM95W-868 | €4.50 | |
| Low-power MCU | €1.50 | |
| 2–3 W solar panel (UV-stable) | €5.00 | |
| LiFePO4 cell 3 Ah + charger | €7.00 | Block charging below 0 °C |
| MOSFET/relay output + connector | €1.50 | |
| Antenna, PCB, passives, light sensor | €3.50 | |
| Enclosure + clamp | €7.00 | Tooling ~€8–10k |

### Firmware/software starting point
- **LoRaWAN:** LoRaMac-node (github.com/Lora-net/LoRaMac-node); for Arduino prototypes, search "MCCI LoRaWAN LMIC".
- **Network server:** The Things Stack (community) for pilots; ChirpStack (open source) for a hunter's own gateway.
- **Alerts:** webhook → push/SMS; a Node-RED flow is fine for the pilot season.
- **Radar config:** Hi-Link's UART protocol (from the maker).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | 10 interviews with hunters/farmers in a high-damage region; **3 districts sign a paid pilot (€100 deposit each)**; bench: LD016 detects a person walking at 8 m, logs wind-blown plant movement |
| 3–5 | Works-like | 6 posts on real trails for 3 weeks; compare alerts with a borrowed trail camera (ground truth, on private land only); false alarms <2 per night per post |
| 6–8 | Looks-like + EVT | Custom PCB + enclosure + clamp; 30 posts; 5-dark-days power test; hunter-mode app |
| 9–10 | DVT + pre-compliance | RED pre-scan (5.8 GHz SRD + 868 MHz), EMC, IP66, −20 to +60 °C cycling |
| 11–12 | Pilot batch | 50 posts in the 3 pilot districts with a damage-measurement protocol agreed with the farmers (ha damaged vs previous year/control fields) |

### Certification checklist (EU)
- **CE under RED:** 5.8 GHz Doppler radar as SRD — confirm the harmonised standard used for the module (e.g. EN 300 440 for SRD in that band — confirm with the lab); 868 MHz: EN 300 220-1/-2 (duty cycle); EMC: EN 301 489-1/-3; safety EN 62368-1; EN 62479. Est. **€10–15k**.
- **RED delegated act (EN 18031-1):** LoRaWAN node via gateway — assume it applies; self-assessment ~€2–5k.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: update path, SBOM, vulnerability handling.
- **IP66** test (EN 60529); UV resistance.
- **RoHS, REACH, WEEE**, packaging registration.
- **Battery Regulation (EU) 2023/1542:** LiFePO4 cell labelling, removability, take-back; UN 38.3 for shipping.
- **Deterrents:** noise limits (national/municipal), animal-protection rules; some countries restrict certain scaring devices — check per market.
- **Hunting law:** use of electronic aids and alerts in hunting varies by country/state — get a written position from a hunting association before marketing "hunting support".
- **GDPR:** no camera → low risk; hunter/farmer contact data and field locations are personal data → EU hosting, privacy notice.
- **Total estimate: €15–25k.**

### Validation toolkit
- **Kill question:** Does a radar alert actually lead to less damage? One season with 3 farms and their hunters; without measurable damage reduction, it's a toy.
- **Cheapest experiment (~€500):** 3 dev-kit posts (LD016 + LoRa + powerbank) on known trails for 3 weeks, alerts by SMS to one hunter; count alerts, confirmed sightings and hunts.
- **5-question interview (hunter/farmer):** 1) How much game damage did you pay or suffer last year, and on which crops? 2) How many nights did you sit without seeing boar? 3) What do you use now: cameras, scarers, fences? What failed? 4) Would an alert at 23:41 "trail 3" make you go out? 5) At €169 per post and no subscription, how many posts would you buy before the maize season?
- **Landing page headline:** "Know when the boar come — without a camera or a SIM." Bullets: "Radar posts on game trails alert you the moment animals enter your field." / "Night log shows patterns so you sit on the right nights." / "Solar powered, LoRa, optional light/sound deterrent."
- **Pass threshold:** 3 paid pilots + 30 pre-orders (€30 deposit) for next season from hunting fairs.

### First production checklist
- **Samples:** radar modules from 2 suppliers compared on the same trail.
- **Golden sample:** with radar sensitivity setting, firmware version and false-alarm test results recorded.
- **DFM review:** radar window (no metal paint), drainage, condensation vent, clamp for wooden and metal posts, camouflage colour.
- **MOQ talk:** solar panel custom size, LiFePO4 cells, enclosure colour.
- **QC/AQL:** AQL II 1.0/2.5; 100% radar trigger test (moving target jig), 100% LoRa join, 100% charge test.
- **Packaging:** compact box, clamp hardware, quick-start with QR onboarding, trail-placement guide.
- **Incoterms:** FOB Shenzhen; ship before the season (Q1) — sea freight takes 5–7 weeks.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance)](/db/hilink-ld016.html) (5.8 GHz long-range motion radar (adjustable distance)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver for alerts to the farm). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (LoRaWAN unit for pilots). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868) — for a Field-Edge Wildlife Alarm

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Field-Edge Wildlife Alarm: A long-range motion radar on a post at the field edge that detects wild boar or deer entering a crop at night, triggers lights or sound deterrents and pings the farmer over LoRa. The design is built around your HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868).
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
主题：样品订购及批量报价 — HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868) — 用于Field-Edge Wildlife Alarm

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Field-Edge Wildlife Alarm：A long-range motion radar on a post at the field edge that detects wild boar or deer entering a crop at night, triggers lights or sound deterrents and pings the farmer over LoRa。产品设计基于贵司的HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)。
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
Subject: PCBA quote from open design files — Field-Edge Wildlife Alarm, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Field-Edge Wildlife Alarm: A long-range motion radar on a post at the field edge that detects wild boar or deer entering a crop at night, triggers lights or sound deterrents and pings the farmer over LoRa. The design starts from published open-hardware files (HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Field-Edge Wildlife Alarm，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Field-Edge Wildlife Alarm：A long-range motion radar on a post at the field edge that detects wild boar or deer entering a crop at night, triggers lights or sound deterrents and pings the farmer over LoRa。设计基于已公开的开源硬件文件（HLK-LD016 5.8 GHz long-range motion-detection radar module (adjustable distance), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Unit LoRaWAN-EU868 (U184-EU868)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 5 LD016 samples and 3 RFM95W modules; test detection range and wind false alarms in a garden hedge.
2. Call 5 hunters in a known boar-damage district and ask who paid how much damage last year.
3. Ask a regional hunting association whether they would co-run a measured pilot next season.

Want help sourcing or building this? Talk to us via www.gongbans.com.
