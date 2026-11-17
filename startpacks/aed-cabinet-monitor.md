# AED Cabinet Monitor — Founder Start Pack

> A retrofit sensor for public AED cabinets at sports clubs, village halls and shops that reports "door opened", "cabinet too cold or too hot" and its own battery status — so the volunteer who looks after the cabinet knows it's ready without walking past it every week.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Tens of thousands of public AEDs in Europe hang in outdoor cabinets maintained by volunteers who check them on foot. Frost (AED batteries and pads have temperature limits), heat, vandalism and theft make some cabinets useless — and nobody finds out until someone needs it.
- **Customer:** Sports clubs, village councils, municipalities and the regional AED volunteer networks that register and maintain public AEDs (they pay, often from donations); the volunteer custodian (uses).
- **Product:** A battery sensor that you screw or cable-tie inside any existing cabinet: door contact, temperature/humidity, LoRaWAN uplink (Cat-M variant where there's no coverage). Door-open event ("AED may be in use — check afterwards"), out-of-range temperature alert, weekly heartbeat, simple map and e-mail/SMS for the volunteer group. It never touches the AED.
- **Why now:** AED networks grew fast after national campaigns and dispatch apps that send volunteers to the nearest AED; maintenance didn't scale with them. LoRaWAN coverage (public and community networks) now reaches most towns, and a LoRa sensor costs a fraction of a connected cabinet.
- **The ask:** ~€70k to first 1,000 units; the kill question is whether one regional volunteer network trials 20 cabinets and pays from its donation budget.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will one regional AED volunteer network trial 20 cabinets and pay for them out of their donation budget?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Sports clubs, village councils and the local AED-network volunteers who maintain public defibrillator cabinets.

**The problem as the pack states it:** Tens of thousands of public AEDs in Europe hang in outdoor cabinets maintained by volunteers who check them on foot. Frost (AED batteries and pads have temperature limits), heat, vandalism and theft make some cabinets useless — and nobody finds out until someone needs it.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The Circuit (UK)** · https://www.thecircuit.uk/ — the UK national defibrillator network; the people who register and look after public AEDs.
- **Resuscitation Council UK** · https://www.resus.org.uk/ — UK resuscitation guidance body.
- **European Resuscitation Council** · https://www.erc.edu/ — European resuscitation guidelines; national councils are members.
- **German Resuscitation Council (GRC, DE)** · https://www.grc-org.de/ — German resuscitation council.
- **DOSB (DE)** · https://www.dosb.de/ — German sports confederation; the regional Landessportbund reaches the clubs.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79–99 + network (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how sports clubs, village councils and the local AED-network volunteers who maintain public defibrillator cabinets deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Who checks your defibrillator cabinet, how often, and what did they find the last time something was wrong with it?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A retrofit sensor for public AED cabinets at sports clubs, village halls and shops that reports door opened, cabinet too cold or too hot, and battery status — so the volunteer who owns it knows it's ready. On a scale of one to ten, how likely would you be to buy that at €79–99 + network (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: AED Cabinet Monitor: would you pay €79–99 + network (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a AED Cabinet Monitor: A retrofit sensor for public AED cabinets at sports clubs, village halls and shops that reports door opened, cabinet too cold or too hot, and battery status — so the volunteer who owns it knows it's ready. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79–99 + network (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A heated outdoor cabinet with a broken heater, an unheated cabinet in January, a door that didn't latch, an AED that was used and never returned: each makes the device on the dispatch map a lie. The custodian is usually one volunteer per cabinet, and their "monitoring" is walking past.

- **Who pays:** (1) sports clubs and village councils that own a cabinet; (2) municipalities with 20–200 public AEDs; (3) regional volunteer networks and first-responder associations that coordinate many cabinets and fundraise for them; (4) AED distributors/service companies who sell maintenance contracts.
- **Who uses:** the custodian (gets the alert), the coordinator (sees the map).
- **What they value:** "I know it's OK without driving there", and proof for donors/councils that the devices are maintained.

### Market size (estimates — check)

- **TAM:** public-access AEDs in DE+NL+BE+AT+Nordics+UK: order of magnitude 300–500k (national registries publish partial counts — check NL and UK registries for hard numbers). Assume 40% are in outdoor/24-h cabinets → **~150k cabinets** × €89 = **~€13M** hardware + €24/yr service = €3.6M/yr recurring.
- **SAM:** cabinets owned by clubs, councils and networks without a connected cabinet already: assume 60% → **~90k cabinets**, €8M hardware + €2.2M/yr.
- **SOM (3 years):** 3–5% → **3–4.5k units**, €0.3–0.4M hardware + ~€100k/yr service. Small. This is a niche business or a feature inside a bigger AED-service company — say that to yourself up front.

### Competition (1 search)

| Alternative | What it is | Why we can still win |
|---|---|---|
| Do nothing / weekly walk-past | Volunteer time | Misses frost, theft, unlatched doors between visits |
| Connected cabinets (e.g. Rotaid 24/7, AIVIA with server monitoring, CardiAct Connect, SaveStation) | New cabinet with built-in monitoring, often AED-presence detection | Means replacing the cabinet; several hundred euros plus subscription — check current prices |
| Retrofit monitors from cabinet makers (e.g. DefibMonitor-type products: temperature, humidity, door, AED presence) | Retrofit, often cellular | Our wedge is LoRaWAN cost and running on free/community networks; check their pricing and coverage |
| AEDs that report self-test status via cellular/Wi-Fi (some manufacturers' models) | AED tells you it's healthy | Only for that brand/model; doesn't report cabinet temperature or door |
| Camera-based AED monitoring | Cellular camera in the cabinet | Pricey, privacy questions for a public spot |

**Wedge:** retrofit into any existing cabinet in 10 minutes, under €100, runs on LoRaWAN where available, no new cabinet, no camera. A volunteer network can monitor its whole fleet for less than one new connected cabinet.

### Product & value proposition

- **Sensor:** ~80×50×25 mm IP65 box, 5–8-year battery target, reed switch + magnet on the door, temperature/humidity sensor, LoRaWAN class A (EU868).
- **Events:** door open (immediate), door left open > 10 min, temperature below/above your thresholds (defaults from typical AED operating ranges — let the custodian set the AED's actual range from its manual), low battery, missed heartbeat.
- **Service:** web map for the network coordinator, e-mail/SMS to the custodian group, monthly "all OK" report for donors/councils. €24/year per cabinet after year 1.
- **Cat-M variant:** for cabinets without LoRaWAN coverage; data plan included 3 years.
- **Optional later:** AED-presence detection (light/IR proximity in the cabinet bay) — keep it physical presence only.

**Pricing (estimates):** LoRaWAN sensor **€89** incl. 1 year service; Cat-M **€139** incl. 3 years data; service €24/year; network bundles of 20 at €75 each.

### Unit economics (estimates, EUR per LoRaWAN unit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (RFM95W ~€4.5, low-power MCU €1.2, TH09C T/RH ~€0.8, reed switch + magnet €0.6, antenna €0.8, PCB/passives €1.0, Li-SOCl₂/lithium AA cell €2.5) | 11.4 | 9.6 |
| PCBA assembly + test (incl. LoRa RF check) | 2.0 | 1.4 |
| Enclosure (IP65 box, magnet holder, mounting kit) | 3.0 | 2.1 |
| Packaging + leaflet | 1.2 | 0.9 |
| Freight + duty to EU | 1.2 | 0.7 |
| Certification amortised (€14k) | 14.0 | 2.8 |
| **Landed cost** | **32.8** | **17.5** |
| Direct at €89 incl. VAT → €74.8 net, less €5 fulfilment | 69.8 | 69.8 |
| **Gross margin direct** | **€37.0 (53%)** | **€52.3 (75%)** |
| Via AED distributor/service company (30% channel) → €52.4 | €19.6 (37%) | €34.9 (67%) |
| Service €24/yr, cost ~€4/yr (hosting, LNS, SMS) | +€20/yr | +€20/yr |

Good margins, small volume. The money is in the recurring service and in bundles to networks and municipalities.

### Go-to-market

**First 100 customers:**
- One regional AED volunteer network: offer a 20-cabinet trial, free for 3 months, then they buy (the kill question).
- Sports clubs that already fundraised for an AED: club board evenings of a regional football/hockey association; national first-aid organisations' local chapters.
- Municipal safety officers in 3 small towns that own AEDs: one-page offer "monitor all your cabinets for less than one new cabinet".
- LoRaWAN communities (The Things Network local communities) — they love a civic use case and will show it at meetups.

**Then scale:** AED distributors and service companies (white-label the sensor in their maintenance contract), insurers of clubs, NL/BE/UK networks, integrations with national AED registries' APIs (where offered — check).

### 12-month plan

- **Q1:** 10 prototypes in 10 cabinets (2 clubs, 1 network); coverage survey; interviews with 10 custodians and 3 coordinators.
- **Q2:** 20-cabinet network trial; rev A PCB; web map + alerts MVP; lab quotes.
- **Q3:** rev B, certification, 1,000-unit run; distributor conversations.
- **Q4:** Cat-M variant; first municipality order; second region/country.

**Team:** founder (sales into networks/municipalities), firmware engineer (part-time, LoRaWAN), web developer (part-time, map + alerts), Shenzhen partner. Advisory: one experienced AED custodian or network coordinator (paid, a few hours/month).

**Funding to first 1,000 units (estimate):** landed hardware excl. cert (1,000 × €18.8) €19k + tooling (small box, maybe off-the-shelf enclosure first) €5k + certification €14k + prototypes/trial €4k + 6 months part-time team €30k + travel/marketing €4k = **≈€76k**. Offsets: network/municipality orders with pre-payment €10–20k. Net need **≈€55–65k**. Route: bootstrap + pre-orders; civic/community-safety grants and club sponsorship (a regional bank or insurer funding "every club AED monitored" is a realistic deal); no VC — the market is too small for it.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** cabinet is metal → antenna inside a Faraday box | Test in 5 cabinet types; external flat antenna through the cable gland; Cat-M variant |
| **Technical:** LoRaWAN coverage gaps in villages | Coverage check before sale (TTN mapper, operator maps); one community gateway per cluster as an add-on |
| **Market:** volunteers don't want another alert stream | Defaults tuned for few alerts; monthly "all OK" summary is the main output |
| **Regulatory (MDR boundary):** if marketed as monitoring the AED itself (readiness, self-test, battery of the AED), it can be argued to be an accessory to a medical device | Monitor the cabinet only; never read, connect to or claim anything about the AED's function. Copy: "cabinet monitor" |
| **Market:** connected cabinets get cheaper | Stay the cheap retrofit; partner with cabinet makers rather than fight them |
| **Supply:** RFM95 module single source (HopeRF) | Common footprint; alternative LoRa modules (e.g. SX1262-based) on the rev B layout |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF RFM95/96/98(W) LoRa module | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html | LoRaWAN EU868 uplink, +20 dBm max, −144 dBm sensitivity, SPI, 16×16 mm | pcb_lib (+ spec, firmware, mech, photos) | MIT — github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29 |
| HopeRF TH09C temperature/humidity sensor | https://www.gongbans.com/db/hoperf-th09c.html | Cabinet T/RH: ±2 %RH, ±0.15 °C, I²C, 6.6 µA @ 1 Hz | spec + demo code (no schematic needed) | MIT — github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sensor/TH09C |
| Seeed Grove-Magnetic Switch | https://www.gongbans.com/db/seeed-grove-magnetic-switch.html | Door-contact reference circuit | schematic | Seeed wiki resources — check licence |
| M5Stack Unit CatM (U128) | https://www.gongbans.com/db/m5stack-unit-catm.html | Prototype the Cat-M variant | enclosure/structure only — electronics not published | Prototype only; use a pre-certified Cat-M module in the product |

### Block diagram

```
Li cell (3.6 V) ─► low-power MCU (sleep ~2 µA) ◄── reed switch (door, interrupt)
                        │ I²C ◄── TH09C (T/RH, every 15 min)
                        │ SPI
                        ▼
                  RFM95W LoRa ─► EU868 ─► gateway ─► LoRaWAN network server ─► our app
                                                                            ├─► map for coordinator
                                                                            └─► e-mail/SMS to custodians
(Cat-M variant: Cat-M module replaces RFM95W, same MCU logic)
```

**Engineering gap:** RF out of a metal cabinet; 5–8-year power budget with door events; secure provisioning (LoRaWAN OTAA keys per device); a dead-simple onboarding (scan QR, put pin on map, set thresholds).

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| RFM95W | €4–5 | HopeRF; keep footprint for an SX1262 alternative |
| MCU (STM32L0/L4-class) | €1.2 | Or an STM32WL SoC (MCU + LoRa in one) for rev B cost-down |
| TH09C | €0.8 | Check availability via distributors |
| Reed switch + magnet | €0.6 | Test with steel cabinet doors |
| Li-SOCl₂ AA (ER14505) | €2.5 | High pulse current → add a capacitor; Battery Regulation |
| Antenna (PCB or flexible external) | €0.8 | External lead for metal cabinets |
| IP65 box (off-the-shelf at first) | €2–3 | Custom tool only at >3k |

### Firmware/software starting point

- **LoRaWAN stacks:** Semtech **LoRaMac-node**, **RadioLib** (Arduino/PlatformIO), or MCCI **LMIC** — all well known; pick one and stick with it.
- **Network server:** **The Things Stack** (community or commercial plan) or **ChirpStack** self-hosted.
- **App:** a small web app (map with Leaflet + OpenStreetMap, alert rules, e-mail via a transactional e-mail provider, SMS via an EU SMS gateway). Keep it boring.
- HopeRF's RFM95 GitHub folder includes demo firmware — useful for RF bring-up.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — talk to 3 network coordinators + 10 custodians; check LoRaWAN coverage at 20 real cabinet locations | One network agrees to a 20-cabinet trial with a purchase decision after 3 months; ≥15/20 sites have coverage |
| 3–5 | **Works-like** — 10 dev-board units in cabinets (RFM95 + MCU + TH09C + reed) | ≥98% uplinks received over 3 weeks; door events delivered < 1 min |
| 6–8 | **Looks-like + EVT** — rev A PCB, IP65 box, 25 units; web map MVP | Battery projection ≥5 years; installation < 10 min by a volunteer with the leaflet |
| 9–10 | **DVT + pre-compliance** — rev B, −25 °C to +60 °C cycling, RED/EMC pre-scan, EN 18031 gap check | Works at −25 °C; no pre-scan fails |
| 11–12 | **Pilot batch** — 20–50 units across the trial network | Network signs order for its cabinets; < 2% hardware issues |

### Certification checklist (EU)

- **CE — RED:** EN 300 220-1/-2 (868 MHz SRD, duty cycle), EN 301 489-1/-3, EN 62368-1 (battery-powered low voltage), EN 62311. With a pre-certified LoRa module, partial reuse of reports. Est. €6–9k. Cat-M variant: +€4–6k (module pre-certified; EN 301 908 spot checks).
- **EN 18031-1:** yes — a LoRaWAN device communicates over the internet via the gateway ("directly or via any other equipment" in the delegated act). Est. €2–4k assessment.
- **CRA:** product with digital elements and a cloud backend; vulnerability handling, SBOM, support period by Dec 2027. Plan FUOTA or document why not.
- **RoHS, REACH, WEEE**, packaging registration.
- **Battery Regulation:** primary lithium cell supplied → registration, labelling, take-back; transport as UN 3091.
- **IP65** (EN 60529).
- **GDPR:** custodian names, phone numbers, e-mail → privacy notice, EU hosting, DPA with the network.
- **MDR boundary:** the product monitors a cabinet (door, temperature). It does not connect to, read or influence the AED, and makes no claim about the AED's readiness. Keep it that way. If you ever add "AED self-test/battery status" by reading the AED, get a regulatory opinion first — that is the step that could make it an accessory to a medical device.
- **Estimated test costs:** €10–14k (LoRaWAN), +€4–6k Cat-M.

### Validation toolkit

- **Kill question:** Will one regional AED volunteer network trial 20 cabinets and pay for them out of their donation budget? **Cheapest experiment:** a one-page offer + one working unit in a cabinet + a call with the coordinator. Total cost < €300.
- **Interview script (5) — custodians/coordinators:**
  1. How do you check your cabinet(s) today, and how often?
  2. Tell me about the last time something was wrong (cold, broken, stolen, used and not returned). How did you find out?
  3. Who gets told when the AED is used, and who refills pads afterwards?
  4. Where does the money for cabinets and maintenance come from? Who signs off €1,800 for 20 sensors?
  5. Would you rather have a monthly "all OK" report, or alerts only?
- **Landing page:** Headline: "Know your AED cabinet is ready — without walking past it." Bullets: "Door opened? Too cold? Instant alert to your volunteer group." / "Fits any existing cabinet in 10 minutes. No new cabinet, no camera." / "€89 per cabinet. Runs for years on one battery."
- **Pre-order pass:** one network or municipality order ≥20 units at ≥€75, plus 2 more in negotiation.

### First production checklist

- **Samples:** 5 PCBAs; golden sample with RF output, sensitivity and sleep current measured; temperature calibration check at −20/0/25/50 °C on 10 units.
- **DFM review:** gasket, battery holder retention under vibration (doors slam), magnet alignment tolerance, antenna lead strain relief.
- **MOQ talk:** RFM95 via distributor (1k fine), batteries 1k, enclosure off-the-shelf until 3k.
- **QC/AQL:** ISO 2859-1 level II, AQL 0.65/2.5; 100% test: LoRa join on a test gateway, door event, T/RH sanity, sleep current < 5 µA.
- **Packaging:** QR code per device (DevEUI) for onboarding, mounting kit, 1-page multilingual install guide.
- **Incoterms:** FOB Shenzhen; lithium-cell shipping docs (PI 969/UN 3091).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and Seeed Studio and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver for LoRaWAN uplink); [HopeRF TH09C relative humidity and temperature sensor](/db/hoperf-th09c.html) (cabinet temperature/humidity). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Magnetic Switch](/db/seeed-grove-magnetic-switch.html) (door-open contact). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit CatM (U128)](/db/m5stack-unit-catm.html) (Cat-M alternative where there is no LoRaWAN). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and Seeed Studio and M5Stack websites)

```email
Subject: Sample order and volume pricing — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128) — for a AED Cabinet Monitor

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a AED Cabinet Monitor: A retrofit sensor for public AED cabinets at sports clubs, village halls and shops that reports door opened, cabinet too cold or too hot, and battery status — so the volunteer who owns it knows it's ready. The design is built around your HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128).
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
主题：样品订购及批量报价 — HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128) — 用于AED Cabinet Monitor

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款AED Cabinet Monitor：A retrofit sensor for public AED cabinets at sports clubs, village halls and shops that reports door opened, cabinet too cold or too hot, and battery status — so the volunteer who owns it knows it's ready。产品设计基于贵司的HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128)。
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
Subject: PCBA quote from open design files — AED Cabinet Monitor, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a AED Cabinet Monitor: A retrofit sensor for public AED cabinets at sports clubs, village halls and shops that reports door opened, cabinet too cold or too hot, and battery status — so the volunteer who owns it knows it's ready. The design starts from published open-hardware files (HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — AED Cabinet Monitor，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款AED Cabinet Monitor：A retrofit sensor for public AED cabinets at sports clubs, village halls and shops that reports door opened, cabinet too cold or too hot, and battery status — so the volunteer who owns it knows it's ready。设计基于已公开的开源硬件文件（HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, HopeRF TH09C relative humidity and temperature sensor, Seeed Grove-Magnetic Switch, M5Stack Unit CatM (U128)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Find the coordinator of one regional AED volunteer network or first-responder association and book a 30-minute call with the kill question.
2. Order 3× RFM95W, 3× TH09C samples, reed switches and an MCU dev board; get one unit to join The Things Network and send door events.
3. Visit 3 cabinets near you (club, town hall, shop): photograph the inside, measure space, check LoRaWAN coverage with a phone app or a TTN mapper. That's your design input.

Want help sourcing or building this? Talk to us via www.gongbans.com.
