# Phone-Booth Fan & Light Controller — Founder Start Pack

> A controller for office phone booths and acoustic pods that keeps the fan and light on while someone sits still on a call, ramps ventilation by CO2, and reports usage — because PIR timers in pods switch off on quiet people.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Acoustic pods and phone booths are in every hybrid office, and "stuffy pod" is the main complaint. Pods use PIR timers that switch light and fan off on people sitting still on a long call, or fans that run in empty pods all day. A single-person booth can reach well over 2,000 ppm CO2 within minutes if the fan is off or too slow (one public measurement on a well-known booth saw ~2,700 ppm with ventilation disabled).
- **Customer:** Acoustic-pod and office-furniture makers (OEM design-in — they pay); facility managers retrofitting existing booths (second channel). Office workers use it without knowing.
- **Product:** A compact controller: 24 GHz presence radar (still people), CO2/temperature/humidity sensor, mains-to-low-voltage isolated supply, PWM fan drive with a quiet curve, LED dimming, "occupied" light outside, optional usage data over Wi-Fi.
- **Why now:** Pod volumes boomed with hybrid work; buyers ask about air quality; CO2 sensors (photoacoustic NDIR) and still-person radar cost a few euros.
- **The ask:** ~€75k to EVT, certification and the first 1,000 controllers, ideally co-funded by an OEM's NRE for a design-in.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 2 pod manufacturers do a design-in for next year's model? OEM cycles are slow — get a letter of intent before tooling.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Acoustic-pod and office-furniture makers (OEM), facility managers retrofitting existing booths.

**The problem as the pack states it:** Acoustic pods and phone booths are in every hybrid office, and "stuffy pod" is the main complaint. Pods use PIR timers that switch light and fan off on people sitting still on a long call, or fans that run in empty pods all day. A single-person booth can reach well over 2,000 ppm CO2 within minutes if the fan is off or too slow (one public measurement on a well-known booth saw ~2,700 ppm with ventilation disabled).

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€OEM 49–69 / retrofit 129 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how acoustic-pod and office-furniture makers, facility managers retrofitting existing booths deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. What do people complain about in your phone booths or pods, and how do you know how often they are actually used?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A controller for office phone booths and acoustic pods that keeps the fan and light on while someone sits still on a call, ramps ventilation by CO2, and reports usage — PIR timers in pods switch off on quiet people. On a scale of one to ten, how likely would you be to buy that at €OEM 49–69 / retrofit 129 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Phone-Booth Fan & Light Controller: would you pay €OEM 49–69 / retrofit 129 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Phone-Booth Fan & Light Controller: A controller for office phone booths and acoustic pods that keeps the fan and light on while someone sits still on a call, ramps ventilation by CO2, and reports usage — PIR timers in pods switch off on quiet people. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €OEM 49–69 / retrofit 129 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

Pod makers compete on acoustics and design, and the electronics are often an afterthought: a PIR, a timer relay and a fan running at one speed. Customers then complain: too loud, too stuffy, or dark mid-call.

- **Who pays (primary):** pod makers — tens of brands in Europe, especially in the Nordics, Baltics, Poland, Germany and the Netherlands. They buy a controller per pod (OEM price) and want EN 62368-1 reports and a stable supply.
- **Who pays (secondary):** facility managers retrofitting existing pods (higher price, smaller volume, install effort).
- **Who uses:** the person on the call — success is when they never think about the fan.
- **Reality:** OEM design-in cycles are slow (6–18 months). Get a letter of intent before tooling.

### Market size (estimates — check)

- **TAM:** European office pod/booth market: assume 150–250k units sold per year across brands (estimate — verify with industry reports), plus an installed base of ~1M. Controller at €55 OEM = **€8–14M/year** new + retrofit potential ~€50–100M.
- **SAM:** pod makers without an in-house electronics team (most small and mid-size brands): ~50% → €4–7M/year.
- **SOM (3 yrs):** 3–5 OEM brands → **5–15k controllers/year**, plus 1–2k retrofit kits.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / PIR + timer relay | Cheap, standard in many pods | Switches off on still people; fixed fan speed |
| Pod makers' in-house controllers (some premium brands have motion-based shut-off after e.g. 30 min, manual override) | Integrated, branded | Usually PIR-based; CO2-driven ventilation is rare at mid-range |
| Generic demand-controlled ventilation controllers (building HVAC world, CO2 transmitters + occupancy) | Proven in rooms | Sized for rooms/BMS, not a pod's 12–24 V fan and LED strip |
| DIY: smart plug + CO2 monitor | Cheap | Not integrated, not certified for furniture |
| Facility "air quality" sensors (stand-alone CO2 monitors) | Measure only | Don't control anything |

**Wedge:** a drop-in OEM controller with still-person radar + CO2 fan curve + quiet mode, delivered with test reports and a wiring harness to the pod maker's spec. "We fix your #1 complaint without you hiring an electronics team."

### Product & value proposition

- **Hardware:** one PCB in a small DIN-less enclosure that screws into the pod ceiling cavity. Mains input (100–240 VAC) → isolated 12 or 24 V via a 20 W AC-DC module; PWM drive for 1–2 DC fans (12/24 V), LED dimming channel, "occupied" indicator output; LD2410B radar facing the seat; SCD41 CO2/T/RH sensor in the airflow path (not right at the fan outlet).
- **Logic:** presence holds light + fan; fan curve by CO2 (e.g. min speed at <800 ppm, ramp to max at 1,200 ppm), quiet mode cap; off after N minutes with nobody; post-occupancy purge for 2–5 minutes.
- **Options:** Wi-Fi/BLE for usage data (occupancy minutes per pod, CO2 history) — sell as a data add-on to facility managers.
- **Pricing (estimates):** OEM €49–69 per controller (incl. harness); retrofit kit €129 (controller + adapter + mounting + instructions for an electrician); data add-on €1–2/pod/month.

### Unit economics (estimates, EUR per controller, OEM version without Wi-Fi)

| Item | 1k | 5k |
|---|---|---|
| HLK-20M12/20M24-class 20 W AC-DC module | 5.0 | 4.0 |
| SCD41 CO2/T/RH sensor | 12.0 | 9.5 |
| LD2410B radar | 2.5 | 1.9 |
| MCU, fan/LED MOSFET drivers, fuse, varistor, terminals, passives | 3.5 | 2.6 |
| PCB 2-layer | 1.0 | 0.6 |
| Assembly + test (hi-pot on mains side, fan PWM, CO2 sanity) | 3.0 | 2.0 |
| Enclosure (flame-rated plastic, mains-side cover) | 2.5 | 1.6 |
| Wiring harness to OEM spec | 3.0 | 2.2 |
| Packaging (bulk) | 0.5 | 0.3 |
| Freight + duty | 1.2 | 0.8 |
| Certification amortised (€14k) | 14.0 | 2.8 |
| **Landed cost** | **48.2** | **28.3** |
| OEM net price (€59) | 59 | 59 |
| **Gross margin OEM** | **€10.8 (18%)** | **€30.7 (52%)** |
| Retrofit kit (€129 ex VAT, via reseller −30%, +€8 adapter/mounting) | 42 | 56 |

The CO2 sensor is a third of the BOM — it's the cost lever. A cheaper NDIR at €6–8 can work for a pod (accuracy needs are modest); qualify one by DVT.

### Go-to-market

**First 100 customers (controllers → first OEM):** list every pod/booth maker in Europe (Orgatec in Cologne and Stockholm Furniture Fair exhibitor lists are a ready-made lead list), call product managers, offer to retrofit 3 of their showroom/demo pods for free with CO2 logging before/after. Their sales teams love a "CO2 stays below 1,000 ppm" claim.

**Then scale:** OEM design-ins (annual model updates), office-furniture dealers selling retrofit kits, facility-service companies, workplace-analytics vendors buying the data add-on.

### 12-month plan

- **Q1:** retrofit 3 demo pods with prototypes (Grove SCD41 + LD2410B + dev board + lab supply); CO2 before/after report; 10 OEM conversations (kill question).
- **Q2:** own PCB rev A (mains-side design per EN 62368-1), harness, 20 units for 2 OEM evaluations.
- **Q3:** rev B, certification (LVD/EMC/RED if radio), LOI → first 1,000-unit order.
- **Q4:** retrofit kit via 1 furniture dealer; Wi-Fi data add-on EVT.

**Team:** founder on OEM sales (furniture industry contacts are gold), hardware engineer with mains-power experience (essential — contract is fine), firmware engineer (part-time), Shenzhen partner for PCBA + harness.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €34k + tooling €6k + certification €14k + prototypes/evaluations €4k + 6 months part-time team €25k + fairs €4k = **≈€87k**. OEM NRE (€10–20k for customisation) + 30% deposit on a 1,000-unit order (~€18k) covers a third to half. Rest: bootstrap/angel; OEM payment terms are usually net 30–60, so plan working capital.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** OEM cycles are slow; LOI takes a year | Retrofit kits and demo-pod reports generate early revenue and proof |
| **Safety:** mains inside furniture — fire and shock risk | Use a certified AC-DC module, proper creepage, fuse + varistor, flame-rated enclosure; EN 62368-1 report; recommend electrician install for retrofit |
| **Technical:** radar sees through pod walls (people passing outside) | Mount facing the seat, limit range gates, test in glass-walled pods |
| **Technical:** CO2 sensor drift (ABC self-calibration assumes fresh air periods) | Pods get fresh air when empty — ABC works; document calibration |
| **Supply:** SCD41 sole source (Sensirion) and price; Hi-Link modules contact-only design files | Qualify a second NDIR sensor; AC-DC modules are standard footprints with alternatives |
| **Noise:** the fan curve makes noise on calls | Quiet mode cap + slow ramps; test with the OEM's acoustic engineer |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2410B/LD2410C presence radar | https://www.gongbans.com/db/hilink-ld2410b.html | Detects people sitting still | Datasheet public, design files via maker (no open schematics) | Buy as module |
| Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41 | https://www.gongbans.com/db/seeed-grove-co2-temperature-humidity-sensor-scd41.html | CO2/T/RH sensing reference | Schematic (open download) | Seeed wiki resources — check licence |
| HLK-20Mxx 20 W AC-DC isolated module (incl. 20W-B, 20W-C) | https://www.gongbans.com/db/hilink-20mxx.html | Mains → 12/24 V isolated for fan and LEDs | Datasheet public, design files via maker (no open schematics) | Buy as module; check its own safety approvals |
| Seeed Grove-MOSFET | https://www.gongbans.com/db/seeed-grove-mosfet.html | Fan/LED PWM drive reference | Schematic (open download) | Seeed wiki resources — check licence |

### Block diagram

```
100–240 VAC ─► fuse + varistor ─► HLK-20Mxx (20 W, isolated) ─► 12/24 V rail
                        ║ isolation (in module) ║                    │
                                                         ┌───────────┼──────────────┐
                                                    buck 3.3 V    MOSFET PWM     MOSFET PWM
                                                         │        fan(s)         LED strip
                                                        MCU ──────────────────────┘
                                          UART │          │ I²C        │ GPIO
                                      LD2410B radar   SCD41 CO2/T/RH   "occupied" light out
                                          (optional Wi-Fi/BLE for usage data)
```

**Engineering gap:** mains-side layout and safety (creepage, fusing, enclosure), fan acoustic tuning, sensor placement in the airflow, and the OEM harness.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| HLK-20M24 (or 20M12) | €4–5 | Check its own certifications (CE/UL/CB) — matters for your report |
| SCD41 | €9–12 | **Sole source (Sensirion)**; alternatives: other NDIR modules |
| LD2410B | €2–3 | Single source |
| MCU (e.g. small ARM or ESP32-C3 if Wi-Fi SKU) | €0.8–2 | |
| 2× logic-level MOSFET + gate drivers | €0.6 | |
| Fuse, varistor, X-cap, terminals | €1.5 | Mains terminals: use approved types |
| Enclosure V-0 plastic | €2–2.5 | |
| Harness | €2–3 | To OEM spec; 4–6 week lead |

### Firmware/software starting point

- **ESPHome** for prototypes (has `scd4x` and `ld2410` components — exist) on an ESP32 dev board: fastest way to the demo-pod CO2 report.
- Production: simple bare-metal or Zephyr/ESP-IDF firmware; Sensirion publishes open embedded drivers for the SCD4x (search "Sensirion embedded-i2c-scd4x").
- Fan curve + presence state machine: your own code — small and testable.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 OEM product-manager calls; CO2 log in 3 existing pods (borrow an office) | ≥2 OEMs agree to a demo-pod retrofit; measured CO2 peaks documented |
| 3–5 | **Works-like** — ESPHome prototype (SCD41 + LD2410B + MOSFET + bench 24 V) in 3 demo pods | CO2 held <1,000 ppm during 60-min calls; zero light-off events on still users |
| 6–8 | **Looks-like + EVT** — rev A PCB with mains input, enclosure, harness; 20 units to 2 OEMs | OEM acoustic/usability sign-off; hi-pot pass on all 20 |
| 9–10 | **DVT + pre-compliance** — EMC pre-scan (conducted + radiated), EN 62368-1 pre-assessment, radar RED pre-scan | No fails; lab confirms test plan; **LOI from ≥1 OEM** (kill question) |
| 11–12 | **Pilot batch** — 50 controllers in an OEM's pilot production run | ≤1% install failures on the OEM line; OEM confirms order for next model year |

### Certification checklist (EU)

- **LVD** (mains-powered): EN 62368-1 safety report — furniture makers will ask for it. Using a pre-certified AC-DC module helps but the controller needs its own assessment. Estimate €4–6k.
- **EMC Directive:** EN 55032/55035 (or EN 61000-6-1/-6-3), conducted emissions from the PWM fan drive, harmonics/flicker EN 61000-3-2/-3-3. Estimate €3–5k.
- **RED** because of the 24 GHz radar (and Wi-Fi/BLE if the data SKU): EN 300 440, EN 301 489-1/-3, EN 62311/62479 (+ EN 300 328/EN 301 489-17 for Wi-Fi/BLE). With a radio inside, RED replaces LVD/EMC as the legal route but the same safety/EMC standards apply. Estimate €4–6k.
- **EN 18031** + **CRA** only for the connected (Wi-Fi) SKU: SBOM, updates, vulnerability handling; CRA reporting from 11 Sep 2026, full from 11 Dec 2027.
- **RoHS, REACH, WEEE** (B2B; the OEM may take over WEEE as the final product maker — agree in the contract), packaging EPR.
- **Ecodesign:** the external fan/LED loads are the OEM's; your standby consumption should be low (<0.5 W target) — check applicable ecodesign standby rules.
- **GDPR:** usage data per pod is anonymous occupancy; works councils may still ask — provide a one-page data description.
- No battery, no medical, no toy.
- **Total estimate:** €12–18k.

### Validation toolkit

- **Kill question:** Will 2 pod manufacturers do a design-in for next year's model? OEM cycles are slow — get a letter of intent before tooling. Cheapest experiment: retrofit one OEM's demo pod with the ESPHome prototype for 2 weeks and hand them the CO2 + occupancy report.
- **Interview script (5) — for pod makers:**
  1. What are the top 3 complaints you get from customers about your pods?
  2. What controls fan and light today, and who designed it?
  3. Do buyers ask about CO2 or air quality in tenders? Do you have numbers?
  4. When is the next model update, and when do you freeze the electronics?
  5. At €59 per controller with harness and test reports, what volume would you design in — and what would stop you?
- **Landing page (OEM-facing):** Headline: "Fresh air and light that stay on for people sitting still." Bullets: "Radar presence — no more lights off mid-call." / "CO2-driven fan curve with a quiet mode." / "Drop-in controller with harness and EN 62368-1 report."
- **Pass:** one signed LOI for ≥500 controllers/year, or 2 OEMs paying for evaluation units + NRE.

### First production checklist

- Samples: AC-DC modules with their certificates; SCD41 from authorised distribution.
- Golden sample: hi-pot, EMC pass, OEM-approved acoustic fan curve, harness fit.
- DFM: creepage/clearance on mains side, keyed connectors, strain relief, label with ratings.
- MOQ: sensor MOQ via distributor, harness 500–1k, enclosure 1k shots.
- QC/AQL: 100% hi-pot + functional (fan PWM, LED dimming, radar, CO2 reading in range), AQL 0.65 for safety items.
- Packaging: bulk trays to the OEM line; installation sheet for retrofit kit (electrician install).
- Incoterms: FOB Shenzhen; OEM may prefer DAP to their factory (Poland/Baltics/Nordics).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410B/LD2410C 24 GHz human-presence radar module](/db/hilink-ld2410b.html) (24 GHz presence radar (still people)); [HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C](/db/hilink-20mxx.html) (20 W isolated AC-DC supply for fan and LEDs). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41](/db/seeed-grove-co2-temperature-humidity-sensor-scd41.html) (CO2 / temperature / humidity sensing); [Seeed Grove-MOSFET](/db/seeed-grove-mosfet.html) (fan PWM drive reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET — for a Phone-Booth Fan & Light Controller

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Phone-Booth Fan & Light Controller: A controller for office phone booths and acoustic pods that keeps the fan and light on while someone sits still on a call, ramps ventilation by CO2, and reports usage — PIR timers in pods switch off on quiet people. The design is built around your HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET.
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
主题：样品订购及批量报价 — HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET — 用于Phone-Booth Fan & Light Controller

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Phone-Booth Fan & Light Controller：A controller for office phone booths and acoustic pods that keeps the fan and light on while someone sits still on a call, ramps ventilation by CO2, and reports usage — PIR timers in pods switch off on quiet people。产品设计基于贵司的HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET。
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
Subject: PCBA quote from open design files — Phone-Booth Fan & Light Controller, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Phone-Booth Fan & Light Controller: A controller for office phone booths and acoustic pods that keeps the fan and light on while someone sits still on a call, ramps ventilation by CO2, and reports usage — PIR timers in pods switch off on quiet people. The design starts from published open-hardware files (HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Phone-Booth Fan & Light Controller，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Phone-Booth Fan & Light Controller：A controller for office phone booths and acoustic pods that keeps the fan and light on while someone sits still on a call, ramps ventilation by CO2, and reports usage — PIR timers in pods switch off on quiet people。设计基于已公开的开源硬件文件（HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-20Mxx 20W AC-DC isolated power module, incl. 20W-B and 20W-C, Seeed Grove-CO2-Temperature-Humidity-Sensor-SCD41, Seeed Grove-MOSFET；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Build the lead list: every pod/booth exhibitor at the last Orgatec and Stockholm Furniture Fair; call 5 product managers with the interview script.
2. Put a CO2 logger in 2 office phone booths for a day; screenshot the curve — that chart opens doors.
3. Order a Grove SCD41, 2 LD2410B and a 24 V PSU; get the ESPHome fan-curve prototype running on a bench fan.

Want help sourcing or building this? Talk to us via www.gongbans.com.
