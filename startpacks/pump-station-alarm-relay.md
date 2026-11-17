# Pump-Station Alarm Relay (sub-GHz) — Founder Start Pack

> A two-box kit for installers: a transmitter wired to the high-level float (or alarm contact) of a sewage or drainage pump pit sends the alarm up to hundreds of metres to a plug-in buzzer in the house — no cable trench, no app, no SIM card.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Domestic sewage lifting stations, pressure-sewer pump pits, drainage sumps and septic pumps have a high-level alarm — often a buzzer or lamp on a control box in the garden or the cellar, where nobody hears it. Running an alarm cable to the house means a trench. Overflows are expensive, smelly and sometimes an insurance fight.
- **Customer:** Installers and distributors of pump stations and drainage systems (they buy and fit), homeowners with pump pits in rural and hillside areas (they pay through the installer or buy the retrofit kit).
- **Product:** Transmitter: IP68 box with a cable gland and a dry-contact input, battery powered, sends "ALARM" plus an hourly "I'm alive". Receiver: plug-in indoor unit with 85 dB buzzer, LEDs, mute, test and a relay output (to a smart-home input or a GSM dialler). 433 MHz OOK, built on encoder/decoder radio chips — almost no firmware.
- **Why now:** More pressure-sewer systems in rural areas, more heavy rain on drainage pumps, and very cheap stand-alone OOK transmitter/receiver chips with open reference designs. US wireless pit alarms sell at $150–600; we found little in the EU at installer-friendly prices.
- **The ask:** ~€65k to first 1,000 kits; kill question: will 2 pump-station distributors stock it as an add-on at €89?

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 2 pump-station distributors stock it as an add-on at €89? Ask with a sample at a trade fair; installers buy what their distributor shows.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Installers and suppliers of domestic sewage pump stations, septic and drainage systems in rural areas; homeowners with pump pits.

**The problem as the pack states it:** Domestic sewage lifting stations, pressure-sewer pump pits, drainage sumps and septic pumps have a high-level alarm — often a buzzer or lamp on a control box in the garden or the cellar, where nobody hears it. Running an alarm cable to the house means a trench. Overflows are expensive, smelly and sometimes an insurance fight.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/septic** · https://www.reddit.com/r/septic/ — homeowners and installers with septic tanks and pump pits.
- **r/Plumbing** · https://www.reddit.com/r/Plumbing/ — plumbers and heating engineers.
- **ZVSHK** · https://www.zvshk.de/ — German plumbing/heating installer federation; the local Innung is the way in.
- **HaustechnikDialog (DE)** · https://www.haustechnikdialog.de/ — German heating installers and owners; hydronic balancing, heat pumps, legionella.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79–99 kit (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how installers and suppliers of domestic sewage pump stations, septic and drainage systems in rural areas deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last pump-pit callout where the high-level alarm went unnoticed: where was the alarm, why did nobody hear it, and what did the cleanup cost?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A two-box kit for installers: a transmitter wired to the high-level float of a sewage or drainage pump pit sends the alarm up to hundreds of metres to a plug-in buzzer in the house — no cable trench, no app. On a scale of one to ten, how likely would you be to buy that at €79–99 kit (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Pump-Station Alarm Relay (sub-GHz): would you pay €79–99 kit (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Pump-Station Alarm Relay (sub-GHz): A two-box kit for installers: a transmitter wired to the high-level float of a sewage or drainage pump pit sends the alarm up to hundreds of metres to a plug-in buzzer in the house — no cable trench, no app. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79–99 kit (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A pump pit alarm that nobody hears is a decorative alarm. Pump stations sit where the gravity sewer can't reach: basements below sewer level, houses on slopes, rural properties on pressure sewer networks, holiday homes. The alarm panel is often fitted to the pit or a post in the garden. Installers know it; they also know a trench for a cable costs more than the alarm.

- **Who pays:** (1) installers/plumbers adding it to every new pump station (€89 is noise on a €2–6k installation); (2) homeowners retrofitting after a scare; (3) municipalities/utilities that operate pressure-sewer pumps on private land (they want households to report alarms quickly).
- **Who sells:** pump-station distributors and the plumbing wholesale trade — installers buy what their wholesaler shows them.
- **Who uses:** the household: buzzer, mute, "call the installer" sticker.

### Market size (estimates — check)

- **TAM:** domestic pump pits (lifting stations, pressure-sewer pits, drainage sumps, septic pumps) in DE, AT, NL, BE, Nordics, UK/IE, FR: order of **2–3M** (rough; no single source — check pressure-sewer statistics and pump makers' annual volumes). Kit at €89 → **~€180–270M** theoretical.
- **SAM:** pits whose alarm can't be heard in the house and new installations per year: assume 25% of the base + ~100k new installations/year → ~600k → **~€53M**.
- **SOM (3 years):** 2–3 distributors, **6–10k kits** → €0.3–0.5M at trade prices. Year 1: 1,000.

### Competition (1 search + trade knowledge)

| Alternative | What it is | Why we can still win |
|---|---|---|
| Do nothing / panel buzzer in the garden | Already installed | Nobody hears it at night or in winter |
| Cable from panel to house | Reliable | Trench, cost, often skipped |
| GSM alarm diallers/modules on the panel | SMS on alarm | SIM card, subscription, coverage in the cellar/pit; €150–300 (estimate) |
| US wireless pit alarms (e.g. Alderon VersAlarm, Liberty wireless kits, SJE Xpert Alert RF) | Exactly this, for US septic | 115 V US products, not CE-marked for EU, $150–600 |
| Wi-Fi sump alarms | Alerts via app | Wi-Fi doesn't reach the pit; app fatigue |
| Generic 433 MHz door-chime/alarm kits | Cheap | No supervision, not IP68, not for a sewage pit |

**Wedge:** supervised, IP68, installer-grade, €89, CE-marked, no SIM — and sold through the wholesaler the installer already uses.

### Product & value proposition

- **Transmitter (outdoor):** IP68 ABS/PC box with a cable gland; dry-contact input (high-level float or the panel's alarm relay), optionally a second input (pump fault). Antenna in the box lid — mount the box **above** ground (on the panel post or pit lid underside with the antenna out); a box under a concrete pit lid won't transmit. 5-year battery target (lithium AA).
- **Supervision:** "alarm" code on contact close (repeated for 30 s, then every 10 min while active), "alive" code every hour from a nano-power timer. Receiver alarms after 3 missed heartbeats (amber "link lost").
- **Receiver (indoor):** plug-in unit, 85 dB buzzer, LEDs (link OK / alarm / link lost / TX battery low), mute (re-sounds after 8 h if still active), test button, volt-free relay output (to a GSM dialler, smart-home input or building management).
- **Range:** up to a few hundred metres line-of-sight; real gardens with walls: test. Repeater SKU later if needed.
- **Band:** **433.92 MHz** — the HopeRF stand-alone encoder transmitter (CMT2150A) covers 240–480 MHz and the stand-alone receiver (CMT2210A) 300–480 MHz, so the idea's "868 MHz" isn't possible with these two chips. For 868 MHz, use the CMT2119A/CMT2219A pair (with an MCU) instead.

**Pricing (estimates):** kit **€89** retail / installer price ~€59; extra receiver €39; trade distributor buys at ~€37–40.

### Unit economics (estimates, EUR per kit: TX + RX)

| Item | 1k | 5k |
|---|---|---|
| TX BOM (CMT2150A ~€0.3, nano-power timer for heartbeat €0.4, 2× lithium AA €2.5, dry-contact input protection €0.4, antenna €0.3, PCB €0.4) | 4.3 | 3.6 |
| RX BOM (CMT2210A ~€0.35, small MCU decoder €0.4, HLK-PM05 3 W AC-DC €1.8, 85 dB buzzer €1.0, relay €0.6, LEDs/buttons €0.4, PCB €0.6, SAW filter €0.3) | 5.5 | 4.7 |
| PCBA assembly + RF test | 2.0 | 1.4 |
| Enclosures (IP68 TX with gland + plug-in RX housing) | 5.0 | 3.5 |
| Packaging + installer leaflet | 1.5 | 1.1 |
| Freight + duty to EU | 1.2 | 0.7 |
| Certification amortised (€15k) | 15.0 | 3.0 |
| **Landed cost** | **34.5** | **18.0** |
| Trade: distributor buys at ~50% of €74.8 net retail → €37.4 | €2.9 (8%) | €19.4 (52%) |
| D2C retrofit at €89 → €74.8 net, less €6 fulfilment = €68.8 | €34.3 (50%) | €50.8 (74%) |

Trade is the channel that scales and it's thin until 5k. D2C retrofit sales fund the first year. The plug-in RX housing with integrated pins is the costly tool; v1 can use a certified external 5 V adaptor and a desk/wall housing (cheaper cert and tooling).

### Go-to-market

**First 100 customers:**
- Ten installers who do pump stations in one rural region: hand them 3 kits each at installer price, ask them to fit one on the next job and call you after.
- Pressure-sewer operators (municipal utilities) in 2 municipalities: offer 20 kits for households with known alarm incidents.
- D2C retrofit: homeowners searching for "Hebeanlage Alarm Funk" / "pompput alarm draadloos"; a short installer video; DIY/plumbing forums (haustechnikdialog.de).

**Then scale:** pump-station distributors and plumbing wholesale (the kill question), OEM deals with pump-station makers (their own-brand alarm accessory), trade fairs (SHK Essen, IFAT Munich for the utility side — check dates), Nordics (private sewage pumps are common), UK septic/pump market (UKCA).

### 12-month plan

- **Q1:** link tests at 15 real pits (range, lid, garden walls); 10 installer interviews; trade-fair or wholesaler meetings with a sample.
- **Q2:** rev A kits, 50 kits through 10 installers; supervision tuning.
- **Q3:** rev B, certification, 1,000-kit run; first distributor listing.
- **Q4:** relay/GSM add-on partner, repeater if field data asks for it, second country.

**Team:** founder (trade sales; ideally someone who has sold to installers), hardware/RF engineer (contract), tiny firmware for the receiver (part-time), Shenzhen partner.

**Funding to first 1,000 kits (estimate):** landed hardware excl. cert (1,000 × €19.5) €20k + tooling €14k + certification €15k + prototypes/field tests €4k + 6 months part-time team €25k + trade fair/samples €6k = **≈€84k**. Offsets: installer and D2C pre-orders (200 × €70) €14k, distributor first order (300 × €37) €11k. Net need **≈€60k**. Route: bootstrap + trade pre-orders; an OEM deal with a pump-station maker could fund tooling. No VC.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** TX inside a buried pit under a concrete/cast-iron lid can't transmit | Install rule: TX on the panel post or lid with antenna above ground; external antenna lead SKU; link-check mode on the receiver (shows signal quality) |
| **Technical:** 433 MHz is crowded (weather stations, remotes) → missed or false codes | Fixed code learned at pairing, repeats, supervision; receiver ignores unknown codes; 1527 codes are simple — consider a rolling-code upgrade with an MCU on TX in rev B |
| **Market:** distributors won't stock a no-name accessory | Bundle installer leaflets, 2-year warranty, OEM own-brand option |
| **Regulatory:** 433 MHz duty cycle and power limits (10 mW ERP) | Alarm repeats within limits; document duty cycle in the technical file |
| **Liability:** "the alarm didn't go off and my cellar flooded" | Supervision + link-lost alarm, clear "supplementary alarm" wording, test button and yearly test reminder in the manual; product liability insurance |
| **Supply:** HopeRF chips single-source | Footprint-compatible OOK encoder/decoder alternatives exist in the 1527 ecosystem; keep the layout generic |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF CMT2150A/CMT2157A OOK transmitter with encoder | https://www.gongbans.com/db/hoperf-cmt2150a-cmt2157a.html | Stand-alone TX, no MCU: up to 7 button inputs, 1527/2262 encoding, 240–480 MHz, up to +13 dBm, sleep <20 nA, SOP14 | pcb, schematic (+ spec) | MIT — github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2150A_CMT2157A |
| HopeRF CMT2210A OOK stand-alone receiver | https://www.gongbans.com/db/hoperf-cmt2210a.html | Stand-alone RX: antenna in, data out, −113 dBm @ 1 ksps, 300–480 MHz, RX 3.8 mA | pcb, schematic (+ spec, firmware) | MIT — github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2210A |
| HLK-PM01/PM03/PM12 3 W AC-DC | https://www.gongbans.com/db/hilink-pmxx.html | Indoor unit supply: 85–265 VAC in, 3,000 VAC isolation, short-circuit protected; "-C" variants with EMC circuit | Datasheet public, files via maker (no open schematic) | Buy as module; product still needs its own LVD/EMC test |

### Block diagram

```
OUTDOOR TX (IP68, 2× Li AA)                          INDOOR RX (plug-in)
float/alarm contact ─► input protection ─► K1 pin ┐   CMT2210A ─► data ─► small MCU (1527 decode,
nano-power timer (1 h) ─► pulse ──────────► K2 pin ├─► CMT2150A ~~~ 433.92 MHz ~~~►   pairing, supervision timers)
                                                   ┘                                   ├─► 85 dB buzzer, LEDs, mute/test
                                                                                       └─► volt-free relay out
                                                                    HLK-PM05 230 V → 5 V (or external adaptor)
K1 code = ALARM (repeats), K2 code = ALIVE (hourly). RX: 3 missed ALIVE → "link lost".
```

**Engineering gap:** the "no firmware" story holds only for the transmitter (encoder chip + a nano-power timer for the heartbeat). The receiver needs a small MCU to decode 1527 frames, learn the TX code and run the supervision timers — the stand-alone receiver outputs raw demodulated data, not "alarm/no alarm". Also: antenna in a small IP68 box, battery life with hourly heartbeats, and installer-proof pairing.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| CMT2150A | €0.25–0.35 | HopeRF; EEPROM-programmed code/ID |
| CMT2210A | €0.30–0.40 | HopeRF |
| Nano-power timer (TPL5110-class) | €0.4 | Or a €0.2 MCU if you want rolling codes |
| 2× lithium AA | €2.5 | −20 °C capable; Battery Regulation |
| 433.92 MHz crystal/SAW, antennas | €0.6 | Helical or PCB antenna — tune in the housing |
| Small MCU (receiver) | €0.3–0.5 | |
| HLK-PM05 (or external 5 V adaptor) | €1.8 | |
| 85 dB buzzer, relay | €1.6 | |
| IP68 housing + cable gland | €2.5–3.5 | Off-the-shelf at first |

### Firmware/software starting point

- Transmitter: none (chip configured via EEPROM using HopeRF's programmer/tooling — check the GitHub folder and HopeRF's RFPDK for what's needed).
- Receiver: 1527/EV1527 decoding is widely documented; libraries such as **rc-switch** (Arduino) decode these codes — use it to prototype, then write ~300 lines of C for the production MCU.
- No app, no cloud. The relay output is the integration point.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — sample (dev boards in a box) shown to 2–3 distributors/wholesalers and 10 installers; link test at 5 real pits | 2 distributors say "we'd stock it at €37–40"; link works at ≥4/5 pits |
| 3–5 | **Works-like** — TX + RX on own PCBs (rev 0), supervision, pairing; 15 pits | Alarm received in <5 s at ≥14/15 pits; zero false alarms in 3 weeks |
| 6–8 | **Looks-like + EVT** — rev A, IP68 housing, RX housing, 30 kits; installer leaflet | IP68 immersion pass (internal); installer fits it in <20 min |
| 9–10 | **DVT + pre-compliance** — rev B, RED/EMC/LVD pre-scan, duty-cycle check, −20 °C battery test | No pre-scan fails; heartbeat at −20 °C OK |
| 11–12 | **Pilot batch** — 50 kits via 10 installers + 1 utility | ≥45 working after 4 weeks; distributor PO for the first 300 |

### Certification checklist (EU)

- **CE — RED:** EN 300 220-1/-2 (433.05–434.79 MHz, 10 mW ERP, duty-cycle limits per the band — check ERC/REC 70-03), EN 301 489-1/-3, EN 62368-1 (indoor mains unit; the battery TX too), EN 62311. Est. €7–10k for both units.
- **LVD:** covered via EN 62368-1 for the mains indoor unit (or avoid with an external certified adaptor).
- **IP68** (EN 60529) for the TX: specify depth/duration (e.g. 1 m, 24 h) and test. Est. €1–2k.
- **EN 18031:** not internet-connected → out of scope; write that down in the technical file.
- **CRA:** the receiver has a microcontroller and a radio data link → likely a product with digital elements (default category). Obligations are light for a closed, non-networked device, but not zero: risk assessment, SBOM, support period, vulnerability contact by Dec 2027.
- **RoHS, REACH, WEEE**, packaging registration.
- **Battery Regulation:** lithium AA supplied → registration, labelling, take-back; transport UN 3091.
- No GDPR (no personal data), no MDR, no toy directive. Not an intrusion alarm (don't market as security equipment).
- **Estimated test costs:** €10–15k.

### Validation toolkit

- **Kill question:** Will 2 pump-station distributors stock it as an add-on at €89 retail? Installers buy what their distributor shows. **Cheapest experiment:** a dev-board sample in a printed box, a one-page sell sheet, and meetings at a trade fair or the distributor's branch.
- **Interview script (5) — installers:**
  1. Where do you usually put the alarm on a domestic pump station? Do customers hear it?
  2. How often do you get called to an overflow that the customer didn't notice? What does it cost them?
  3. What do you fit today when a customer wants the alarm in the house — cable, GSM dialler, nothing?
  4. Would you fit a wireless kit on every new installation at €59 installer price?
  5. Where do you buy it — which wholesaler, and would they need to stock it for you to use it?
- **Landing page:** Headline: "Hear your pump pit alarm in the house — without digging a trench." Bullets: "Wire it to the high-level float; the buzzer goes inside." / "Checks the link every hour and warns you if it's lost." / "No app, no SIM card, no subscription."
- **Pre-order pass:** 2 distributor listings with a first PO ≥300 kits total, **or** 10 installers re-ordering after the first kits.

### First production checklist

- **Samples:** 10 kits; golden pair with measured TX power, frequency, RX sensitivity and TX sleep current.
- **DFM review:** IP68 sealing (gasket vs potting — potting kills battery replacement), cable gland range, antenna position relative to the lid, battery holder vibration.
- **MOQ talk:** HopeRF chips (one reel each), housings (off-the-shelf IP68 first), lithium AA (1k).
- **QC/AQL:** ISO 2859-1 level II, AQL 0.65/2.5; 100% pair test (ALARM + ALIVE received in a shielded box at reduced level), buzzer check, relay check; hipot on RX units.
- **Packaging:** kits pre-paired in the factory (installer just fits it), installer leaflet + homeowner sticker, wholesaler-friendly carton with EAN.
- **Incoterms:** FOB Shenzhen; lithium batteries packed with equipment — PI 969/UN 3091 docs.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (HopeRF (华普微) and Hi-Link (海凌科)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder](/db/hoperf-cmt2150a-cmt2157a.html) (OOK transmitter with built-in encoder (open schematic + PCB)); [HopeRF CMT2210A OOK stand-alone receiver](/db/hoperf-cmt2210a.html) (stand-alone OOK receiver (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)](/db/hilink-pmxx.html) (3 W isolated AC-DC for the indoor buzzer unit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and Hi-Link (海凌科) websites)

```email
Subject: Sample order and volume pricing — HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit) — for a Pump-Station Alarm Relay (sub-GHz)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Pump-Station Alarm Relay (sub-GHz): A two-box kit for installers: a transmitter wired to the high-level float of a sewage or drainage pump pit sends the alarm up to hundreds of metres to a plug-in buzzer in the house — no cable trench, no app. The design is built around your HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit).
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
主题：样品订购及批量报价 — HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit) — 用于Pump-Station Alarm Relay (sub-GHz)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Pump-Station Alarm Relay (sub-GHz)：A two-box kit for installers: a transmitter wired to the high-level float of a sewage or drainage pump pit sends the alarm up to hundreds of metres to a plug-in buzzer in the house — no cable trench, no app。产品设计基于贵司的HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)。
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
Subject: PCBA quote from open design files — Pump-Station Alarm Relay (sub-GHz), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Pump-Station Alarm Relay (sub-GHz): A two-box kit for installers: a transmitter wired to the high-level float of a sewage or drainage pump pit sends the alarm up to hundreds of metres to a plug-in buzzer in the house — no cable trench, no app. The design starts from published open-hardware files (HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Pump-Station Alarm Relay (sub-GHz)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Pump-Station Alarm Relay (sub-GHz)：A two-box kit for installers: a transmitter wired to the high-level float of a sewage or drainage pump pit sends the alarm up to hundreds of metres to a plug-in buzzer in the house — no cable trench, no app。设计基于已公开的开源硬件文件（HopeRF CMT2150A / CMT2157A OOK transmitter with built-in encoder, HopeRF CMT2210A OOK stand-alone receiver, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order CMT2150A and CMT2210A samples (reference schematics and PCBs are on HopeRF's GitHub, MIT); build one TX/RX pair with an Arduino decoder and test it from your own (or a friend's) garden pit to the bedroom.
2. Call 5 installers who fit domestic lifting/pressure-sewer stations and ask the interview questions — especially question 5 (which wholesaler).
3. Get the ERC/REC 70-03 annex for 433 MHz and write down the duty-cycle budget for your alarm repeats and hourly heartbeats.

Want help sourcing or building this? Talk to us via www.gongbans.com.
