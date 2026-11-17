# Basement Flood Sentinel (sub-GHz) — Founder Start Pack

> A floor puck in basements, boiler rooms and storage cellars that detects water and shouts — over a sub-GHz link that gets through concrete floors where Wi-Fi dies — to a plug-in siren upstairs that can also text you.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Cellars flood from heavy rain, backed-up drains, burst pipes and failed washing-machine hoses. The damage is usually found days later. Wi-Fi leak sensors sit in the one room where Wi-Fi doesn't reach, and battery Wi-Fi sensors die in months.
- **Customer:** Homeowners with cellars in DE, AT, BE, NL (they pay and use); housing associations and property managers with storage cellars and boiler rooms (they pay, caretakers use); small archives, museums and parish halls.
- **Product:** A two-box set. An IP67 battery puck with two floor electrodes and a sub-GHz transmitter (5-year battery target, supervised heartbeat every 30 min), and a plug-in 85 dB siren upstairs that also sounds if the puck goes silent. Optional LTE-M siren that sends SMS/app alerts. No app needed for the basic set.
- **Why now:** Heavy-rain events are more frequent and insurers increasingly ask about prevention. One-way sub-GHz radios cost cents and go through floors far better than 2.4 GHz. Most 868 MHz leak sensors on the market are accessories of an alarm-panel ecosystem.
- **The ask:** ~€85k to certification and the first 1,000 sets; fund it with a paid pilot from one housing association plus D2C pre-orders, then an angel ticket only for the LTE-M SKU.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> In 20 real basements (concrete, rebar), does the puck reach the upstairs siren on the first try >99% of heartbeats? If not, add repeaters — and margin suffers.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a fake-door landing page that homeowners with cellars, housing associations, small archives and museums actually visited, with a measured conversion to a waitlist or refundable deposit, plus the interview notes behind it. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Homeowners with cellars (DE, AT, BE), housing associations, small archives and museums.

**The problem as the pack states it:** Cellars flood from heavy rain, backed-up drains, burst pipes and failed washing-machine hoses. The damage is usually found days later. Wi-Fi leak sensors sit in the one room where Wi-Fi doesn't reach, and battery Wi-Fi sensors die in months.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/HomeImprovement** · https://www.reddit.com/r/HomeImprovement/ — homeowners with damp, mould and air problems.
- **HaustechnikDialog (DE)** · https://www.haustechnikdialog.de/ — German heating installers and owners; hydronic balancing, heat pumps, legionella.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.
- **NEMO, Network of European Museum Organisations** · https://www.ne-mo.org/ — European museum associations.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (twenty people from the audience line), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€49 basic / 99 with LTE-M (estimate), the pack's estimate), and one button. For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how homeowners with cellars, housing associations, small archives and museums deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last time water got into your cellar or boiler room: how did you find out, how long had it been there, and what did it cost?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A floor puck in basements, boiler rooms and storage cellars that detects water and shouts — via a sub-GHz link that gets through concrete floors where Wi-Fi dies — to a plug-in siren upstairs that can also text you. On a scale of one to ten, how likely would you be to buy that at €49 basic / 99 with LTE-M (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Basement Flood Sentinel (sub-GHz): would you pay €49 basic / 99 with LTE-M (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Basement Flood Sentinel (sub-GHz): A floor puck in basements, boiler rooms and storage cellars that detects water and shouts — via a sub-GHz link that gets through concrete floors where Wi-Fi dies — to a plug-in siren upstairs that can also text you. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €49 basic / 99 with LTE-M (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A flooded cellar costs €2–20k (estimate) in damaged goods, drying and sometimes a heating system. The water often arrives at night or while people are away. The fix — knowing within minutes — is cheap. The reason people don't have it: the cheap leak sensors are Wi-Fi or Zigbee and either can't reach the router through a reinforced concrete slab, or need a hub that the household doesn't own.

- **Who pays, B2C (primary at launch):** owners of single-family houses and terraced houses with a cellar, often with a gas boiler, a washing machine and a freezer down there. They search "Wassermelder Keller" after a neighbour's flood or a storm warning.
- **Who pays, B2B:** housing associations and Hausverwaltungen (storage cellars, heating rooms, lift pits); small archives/museums/churches (high-value contents, no IT staff). Their caretaker wants a sound upstairs, not another app.
- **Who uses:** the household or caretaker. The siren must be self-explanatory: one test button, one mute button, LED for "puck OK / puck silent / battery low".
- **Who influences:** building insurers (some already subsidise leak detectors in other markets — check what's offered in DE/AT), plumbers and drain-cleaning firms who see every flooded cellar.

### Market size (estimates — check)

- **TAM:** Germany has ~19M residential buildings (Destatis — check); assume 55% have a cellar → ~10M. Add AT/BE/NL/CH cellars ≈ 4M. ~14M cellars × one €49–59 set = **~€700–800M** theoretical.
- **SAM:** cellars with a reason to worry (washing machine, boiler, flood-prone area, previous water event) — assume 25% → 3.5M; reachable online and via DIY/insurer channels at €55 average → **~€190M**.
- **SOM (3 years):** 0.3% of SAM ≈ **10k sets D2C** plus 2–4 housing associations at 1–2k sets each → 12–18k sets, €0.7–1.0M revenue. Year 1: 1,000–2,000 sets.

### Competition (2 searches)

| Alternative | What it is | Why we can still win |
|---|---|---|
| Do nothing / check the cellar after rain | Free | You find the water days later |
| Standalone beeping leak alarm (€10–20, 9 V battery) | Beeps in the cellar | Nobody hears a beeper two floors down |
| Homematic IP water sensor (868 MHz, local siren + app) | Good product, needs the Homematic IP access point and app | Ecosystem buy; the siren is in the cellar, not upstairs |
| Alarm-panel accessories (ABUS Secvest/Comfion, Visonic PowerG water detectors, 868 MHz) | Professional, reliable | Only useful if you already own the panel; installer price |
| Wi-Fi/Zigbee leak sensors (Aqara, Shelly Flood, Tuya) | Cheap, app-first | Signal through the slab; Wi-Fi battery life; needs a hub/app |

**Wedge:** the only set we found that is designed for the cellar-to-upstairs problem: no hub, no app, supervised link, siren where people actually are. Sell it as "the smoke alarm for your cellar".

### Product & value proposition

- **Puck:** ~60 mm round, IP67, two gold-plated stainless electrodes at 1–2 mm floor clearance plus an optional external probe lead (for sumps, behind the boiler). Battery: 2× AA lithium or one CR123A (decide in EVT). Sends "WET" immediately, repeats 3× with random spacing, heartbeat every 30 min, low-battery flag.
- **Siren:** plug-in unit (Schuko/Type F in DE/AT, Type E in BE/FR — plan two SKUs or a cable version), 85 dB at 1 m, LED status, test + mute buttons. Alarms on WET and on "puck silent > 2 h". Pairs by button press.
- **LTE-M siren (Pro):** same plus Cat-M modem and an SMS-out with a prepaid data plan included for 2 years; optional web dashboard for associations.
- **Up to 4 pucks per siren** (washing machine, boiler, sump, storage corner).

**Pricing (estimates):** Basic set (1 puck + siren) **€59 D2C**, extra puck €24. Pro set with LTE-M **€109** incl. 2 years of SMS. B2B (associations, 100+ sets): €42 basic, €85 Pro, plus €1/month after year 2 for Pro.

The idea brief said €49 basic. Blunt truth: at €49 through a retailer the numbers below don't work. Launch at €59 direct and keep €49 as a promo or an insurer-subsidised price.

### Unit economics (estimates, EUR per basic set: 1 puck + 1 siren)

| Item | 1k sets | 5k sets |
|---|---|---|
| Electronics BOM — puck (CMT2119A ~€0.35, low-power MCU €0.5, electrodes/contacts €0.6, PCB €0.4, passives €0.3, 2× AA lithium €2.2) | 4.4 | 3.7 |
| Electronics BOM — siren (CMT2219A ~€0.6, MCU €0.5, HLK-PM01 3 W AC-DC €1.8, 85 dB piezo + driver €1.2, LEDs/buttons/PCB €1.3, SAW filter/antenna €0.4) | 5.8 | 4.9 |
| PCBA assembly + RF test (both boards) | 2.4 | 1.6 |
| Enclosures (IP67 puck with gasket + plug-in siren housing with pins) | 4.8 | 3.3 |
| Packaging + leaflet + adhesive pad | 1.6 | 1.2 |
| Freight + duty to EU | 1.8 | 1.0 |
| Certification amortised (€18k) | 18.0 | 3.6 |
| **Landed cost** | **38.8** | **19.3** |
| D2C at €59 incl. 19% VAT → €49.6 net, less €6 fulfilment/payment | 43.6 | 43.6 |
| **Gross margin D2C** | **€4.8 (11%)** | **€24.3 (56%)** |
| Retail at €59 list (retailer keeps ~40%) → €29.8 to us | -€9.0 | €10.5 (35%) |

Year-one rule: D2C and B2B only. Retail and insurer bundles once you're at 5k and the cert is paid off. Tooling (two housings, ~€12–16k) is not in the per-unit numbers — it's in the funding math. The plug-in housing with integrated mains pins is the expensive tool; a cheaper start is a small desk siren with a separate certified USB power supply (moves you from LVD-heavy to SELV).

### Go-to-market

**First 100 customers:**
- Homeowner forums and communities: haustechnikdialog.de, bauexpertenforum, Facebook groups "Altbau sanieren", r/de_EDV-adjacent smart-home subreddits (frame it as "no hub needed").
- Storm-season timing: run Google/Meta ads on "Keller Wasser Alarm" in the days after heavy-rain warnings (DWD warnings are public — automate the ad budget against them).
- Plumbers and drain-cleaning firms: give 10 local firms a "leave-behind" box of 5 sets at cost; they sell it to the customer whose cellar they just pumped out. That customer is the best-qualified buyer you will ever meet.
- One housing association: 50-set paid pilot in storage cellars and heating rooms.

**Then scale:** online DIY retailers and Amazon.de (at €59+), building insurers' prevention programmes (subsidised sets), Hausverwaltungen through their regional associations, BE/NL via the same plumber leave-behind model.

### 12-month plan

- **Q1:** link test in 20 real basements (the kill question) with dev boards; 15 customer interviews; plumber-channel test with 3 firms; lab quotes.
- **Q2:** rev A puck + siren PCBs, puck enclosure (soft tool), 50-set paid pilot with an association, battery-life measurements.
- **Q3:** rev B, RED/LVD certification, hard tooling, 1,000-set run; D2C launch before autumn storm season.
- **Q4:** LTE-M Pro EVT, second association, insurer conversations with real field data (number of real alarms caught).

**Team:** founder (sales/ops), firmware engineer (part-time OK — the firmware is small), hardware/RF engineer (contract, 3–4 months), a Shenzhen partner for PCBA, enclosures and the RF test fixture.

**Funding to first 1,000 sets (estimate):** landed hardware excl. cert (1,000 × €20.8) €21k + tooling €14k + certification €18k + prototypes/link tests €5k + 6 months part-time team €35k + marketing €8k = **≈€101k**. Offsets: association pilot + pre-payment €10–20k, D2C pre-orders (300 × €49 early-bird = €15k). Net need **≈€65–75k**. Route: bootstrap + pre-orders + one regional innovation grant for climate adaptation (search current state programmes, e.g. NRW/Bavaria); angel only for the LTE-M SKU.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** link through rebar slab fails in some houses | Kill-question test in 20 basements first; 868 vs 433 MHz A/B; external antenna lead on the puck; plug-in repeater SKU as plan B (and price it in) |
| **Technical:** false alarms from condensation or cleaning | Electrode spacing/height tuned; require continuous wet for 10 s; "test" mode documented |
| **Market:** buyers expect a phone alert, not a siren | Pro SKU with LTE-M; basic SKU pitched for households that are home at night |
| **Regulatory:** RED duty-cycle limits on 868 MHz (1% in g1 sub-band) | Heartbeat is tiny; alarm repeats stay well within; document in the technical file |
| **Regulatory:** plug-in mains siren needs LVD/EN 62368-1 work | Start with a certified external USB supply; integrate the HLK-PM module only when volume justifies it |
| **Supply:** HopeRF chips single-source | CMT2119A/2219A are cheap; buy 12 months of stock at EVT; keep a footprint option for an alternative sub-GHz transceiver |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF CMT2119A (G)FSK/OOK transmitter | https://www.gongbans.com/db/hoperf-cmt2119a.html | Puck transmitter: SOT23-6, 240–960 MHz, up to +13 dBm, sleep <20 nA | pcb, schematic (+ spec, firmware) | MIT — HopeRF GitHub: github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2119A |
| HopeRF CMT2219A OOK/(G)FSK receiver | https://www.gongbans.com/db/hoperf-cmt2219a.html | Siren receiver: 300–960 MHz, SPI, 32-byte FIFO, −109 dBm @ 9.6 ksps | pcb, schematic (+ spec, firmware) | MIT — github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2219A |
| M5Stack Unit CatM (U128) | https://www.gongbans.com/db/m5stack-unit-catm.html | Prototype the LTE-M SMS path on the Pro siren | enclosure/structure only — electronics not published | Prototype only; for the product use a pre-certified Cat-M module and check which modem the unit uses |

The CMT2119A is transmit-only, so the link is one-way: the siren cannot acknowledge. That's why the heartbeat matters — "silence" is the only failure signal you get. If you want acknowledged links later, move both ends to a transceiver.

### Block diagram

```
PUCK (IP67, battery)                         SIREN (upstairs, plug-in)
2×AA ─► MCU (sleep µA) ◄─ electrode sense     CMT2219A RX ─► MCU ─► 85 dB piezo
          │ wake on wet / 30-min timer                         ├─► LED + test/mute
          ▼                                                    ├─► "puck silent >2 h" alarm
      CMT2119A TX 868 MHz ~~~~~ through slab ~~~~~►            └─► (Pro) Cat-M modem ─► SMS
                                               HLK-PM01 230 V→5 V (or external USB PSU)
```

**Engineering gap:** (1) link margin through real slabs — antenna design in a small IP67 puck is the whole game; (2) electrode sensing that ignores condensation but catches 1 mm of water; (3) packet format with puck ID, sequence counter and a simple MAC so a neighbour's set can't trigger yours; (4) 5-year power budget.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| CMT2119A transmitter | €0.35 | HopeRF — single source; stock up |
| CMT2219A receiver | €0.60 | HopeRF — single source |
| Low-power MCU (STM32L0/PY32-class) ×2 | €1.00 | Puck MCU must sleep < 2 µA |
| 26 MHz crystals, SAW/matching, PCB antennas | €0.80 | Antenna tuning = most of the RF work |
| Electrodes (stainless/gold-plated contacts) + probe jack | €0.60 | Corrosion test in salt/detergent water |
| 2× AA lithium (or CR123A) | €2.20 | Lithium for cold cellars; Battery Regulation labelling |
| HLK-PM01 3 W AC-DC | €1.80 | Or external certified USB PSU (simpler cert) |
| 85 dB piezo + driver | €1.20 | Measure dB(A) at 1 m in the housing |
| Cat-M module (Pro only) | €8–11 | Plus SIM/data cost ~€6–10 for 2 years |

### Firmware/software starting point

- HopeRF's GitHub folders for CMT2119A/CMT2219A include demo firmware and register configuration (check what's inside before you plan around it). HopeRF's RFPDK tool generates register settings — confirm availability.
- MCU: plain C on STM32Cube or the vendor SDK of your chosen low-cost MCU; the logic is a state machine (sleep → sense → TX), no RTOS needed.
- Pro siren: AT-command driver for the Cat-M modem; use an existing SMS gateway or a tiny MQTT backend (e.g. Mosquitto) for the association dashboard.
- Pairing/security: rolling counter + truncated CMAC (AES-128) — tiny, and it kills replay/neighbour triggers.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — kill-question link test: dev boards (CMT2119A TX, CMT2219A RX) in 20 basements, 868 vs 433 MHz; 15 interviews with cellar owners + 3 plumbers | ≥99% heartbeats received first try in ≥18/20 basements; ≥8/15 interviewees would pay €59 |
| 3–5 | **Works-like** — breadboard puck + siren, electrode tuning, supervision logic, pairing | 1 mm water detected in <15 s; zero false alarms in 2 weeks of humid cellar; "silent puck" alarm works |
| 6–8 | **Looks-like + EVT** — rev A PCBs, printed IP67 puck, siren housing, 20 sets; current profile | Puck average current projects >5 years; 20 sets in 20 homes |
| 9–10 | **DVT + pre-compliance** — rev B, IP67 immersion test, EMC/RF pre-scan, duty-cycle check, drop test | Pass pre-scan; IP67 (30 min, 1 m) pass; siren ≥85 dB(A) at 1 m |
| 11–12 | **Pilot batch** — 50 sets to an association + 10 plumber leave-behind boxes | ≤2% field issues in 4 weeks; association signs LOI for ≥500 sets |

### Certification checklist (EU)

- **CE — RED 2014/53/EU:** EN 300 220-1/-2 (SRD 868 MHz: g1 sub-band 868.0–868.6 MHz, 25 mW ERP, 1% duty cycle — or 433.05–434.79 MHz, 10 mW, 10%), EN 301 489-1/-3 (EMC), EN 62368-1 (safety, incl. the mains siren), EN 62311 (RF exposure). Est. €8–12k for both units.
- **Pro SKU:** cellular module pre-certified; still add EN 301 908 spot checks + EN 301 489-52. Est. +€4–6k.
- **EN 18031-1 (RED delegated act cybersecurity):** applies to radio equipment that can communicate over the internet — the Pro SKU yes (est. €2–4k assessment). The basic one-way 868 MHz set is not internet-connected; document why it's out of scope.
- **CRA:** applies from Dec 2027 to products with digital elements — Pro clearly; basic set likely too (it's a product with a data connection to another device). Plan SBOM, vulnerability contact, support period now.
- **RoHS, REACH, WEEE** (register with stiftung ear in DE before selling), packaging registration (LUCID).
- **Battery Regulation (EU) 2023/1542:** batteries supplied with the product → producer registration, labelling, take-back. Primary lithium AA: also transport rules (UN 3091 when packed with equipment).
- **IP67** test for the puck (EN 60529), est. €1–2k.
- No GDPR issue in the basic set (no personal data). Pro: phone numbers and alert history → privacy notice, EU hosting.
- **Total estimate:** €15–20k basic; €21–28k with Pro.

### Validation toolkit

- **Kill question:** In 20 real basements (concrete, rebar), does the puck reach the upstairs siren on the first try for >99% of heartbeats? If not, you need repeaters — and the margin suffers. **Cheapest experiment:** two dev boards, a battery, a laptop logging the receiver, and 20 friends-of-friends' houses over two weekends. Cost < €500.
- **Interview script (5):**
  1. Has your cellar ever had water in it? What happened, and how did you find out?
  2. What's down there that you'd hate to lose (boiler, freezer, washing machine, archives)?
  3. Do you have Wi-Fi in the cellar? Any smart-home hub? Would you install one for this?
  4. Who would you want to be warned — you upstairs, your phone, a neighbour?
  5. Would you pay €59 for a puck and an upstairs siren? €109 if it also texts you?
- **Landing page:** Headline: "Hear the water before it costs you." Bullets: "Works through concrete floors — no Wi-Fi, no hub, no app." / "Siren upstairs, where you actually are; texts you with Pro." / "Battery lasts years and the siren tells you if the puck goes quiet."
- **Pre-order pass:** ≥200 D2C deposits of €10 in 30 days from ≤€3k ads, OR one association/insurer commitment for ≥300 sets.

### First production checklist

- **Samples:** 5 PCBA samples from two assemblers; golden sample pair with measured RF output, sensitivity and current.
- **DFM review:** puck gasket and ultrasonic welding vs screws; electrode sealing; battery door that stays IP67 after 3 battery changes; siren housing creepage/clearance if mains-integrated.
- **MOQ talk:** HopeRF chips via distributor (reel of 3k is normal — buy one reel each); enclosures 1–3k shots; packaging 1k.
- **QC/AQL:** ISO 2859-1 level II, AQL 0.65 major / 2.5 minor; 100% functional test: RF TX power + frequency, RX sensitivity in a shielded box, wet-detect test with a water pad, siren dB check on sample basis, 4 h burn-in for sirens.
- **Packaging:** drop test (ISTA 1A), battery labelling, multilingual quick-start (DE/NL/FR/EN), retail-ready box for later.
- **Incoterms:** FOB Shenzhen to start; lithium batteries packed with equipment need the right shipping docs (UN 3091, PI 969) — get your forwarder to confirm.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT2119A (G)FSK/OOK transmitter](/db/hoperf-cmt2119a.html) ((G)FSK/OOK sub-GHz transmitter in the battery floor puck (open schematic + PCB)); [HopeRF CMT2219A OOK/(G)FSK receiver](/db/hoperf-cmt2219a.html) (matching sub-GHz receiver in the siren unit (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit CatM (U128)](/db/m5stack-unit-catm.html) (optional Cat-M module in the siren for SMS/app alerts). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128) — for a Basement Flood Sentinel (sub-GHz)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Basement Flood Sentinel (sub-GHz): A floor puck in basements, boiler rooms and storage cellars that detects water and shouts — via a sub-GHz link that gets through concrete floors where Wi-Fi dies — to a plug-in siren upstairs that can also text you. The design is built around your HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128).
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
主题：样品订购及批量报价 — HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128) — 用于Basement Flood Sentinel (sub-GHz)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Basement Flood Sentinel (sub-GHz)：A floor puck in basements, boiler rooms and storage cellars that detects water and shouts — via a sub-GHz link that gets through concrete floors where Wi-Fi dies — to a plug-in siren upstairs that can also text you。产品设计基于贵司的HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128)。
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
Subject: PCBA quote from open design files — Basement Flood Sentinel (sub-GHz), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Basement Flood Sentinel (sub-GHz): A floor puck in basements, boiler rooms and storage cellars that detects water and shouts — via a sub-GHz link that gets through concrete floors where Wi-Fi dies — to a plug-in siren upstairs that can also text you. The design starts from published open-hardware files (HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Basement Flood Sentinel (sub-GHz)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Basement Flood Sentinel (sub-GHz)：A floor puck in basements, boiler rooms and storage cellars that detects water and shouts — via a sub-GHz link that gets through concrete floors where Wi-Fi dies — to a plug-in siren upstairs that can also text you。设计基于已公开的开源硬件文件（HopeRF CMT2119A (G)FSK/OOK transmitter, HopeRF CMT2219A OOK/(G)FSK receiver, M5Stack Unit CatM (U128)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order CMT2119A and CMT2219A samples/eval boards (HopeRF GitHub folders have the reference schematics) and two cheap MCUs; flash a heartbeat transmitter and a logging receiver.
2. Line up 20 basements for the link test (family, colleagues, a local housing co-op) — book them before you have hardware.
3. Call three local drain-cleaning/plumbing firms and ask one question: "Would you hand this to customers after pumping out their cellar?" Record the answers.

Want help sourcing or building this? Talk to us via www.gongbans.com.
