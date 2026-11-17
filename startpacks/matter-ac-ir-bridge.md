# Matter Bridge for Old Air-Conditioners — Founder Start Pack

> A small IR puck that makes any infrared-remote split air-conditioner or air-to-air heat pump show up as a Matter thermostat, with a radar so it switches off when the room is empty.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of split ACs and air-to-air heat pumps in Europe are controlled only by an IR remote. They run in empty rooms, react to the temperature at the ceiling unit instead of where people sit, and can't join a smart home without a vendor Wi-Fi kit (often €80–150, cloud-only, if it exists at all).
- **Customer:** Households in southern Europe with split ACs; the fast-growing base of air-to-air heat pumps in NL, the Nordics and DE; holiday-rental hosts; small offices. The owner pays.
- **Product:** A USB-C puck with an IR blaster, room temperature/humidity sensor and 24 GHz presence radar on a Matter-over-Wi-Fi module. Shows up in Apple Home, Google Home, Alexa, SmartThings or Home Assistant as a thermostat/room-AC. Closes the loop on real room temperature; sets back after N minutes with nobody in the room. Local Matter, no vendor cloud.
- **Why now:** Air-to-air heat pumps are the cheapest heat-pump retrofit; Matter 1.2+ defines thermostat and room-air-conditioner device types supported by the big ecosystems; energy prices made "don't heat/cool an empty room" a real saving.
- **The ask:** ~€130k to Matter certification and 1,000 units. Pre-sales via smart-home communities, then retail.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Can we reliably decode/encode the IR protocols of the 15 best-selling split units in EU retail? If fewer than 12 work out of the box, the support cost kills the margin.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Southern-European flats and the fast-growing base of air-to-air heat pumps in NL/Nordics; holiday rentals; small offices.

**The problem as the pack states it:** Millions of split ACs and air-to-air heat pumps in Europe are controlled only by an IR remote. They run in empty rooms, react to the temperature at the ceiling unit instead of where people sit, and can't join a smart home without a vendor Wi-Fi kit (often €80–150, cloud-only, if it exists at all).

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/heatpumps** · https://www.reddit.com/r/heatpumps/ — heat-pump owners and installers, EU and US.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.
- **r/HomeKit** · https://www.reddit.com/r/HomeKit/ — Apple Home users; Matter and Thread devices are a main topic.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€49–69 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how southern-European flats and the fast-growing base of air-to-air heat pumps in NL/Nordics deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you control your air-conditioner or air-to-air heat pump today, and how often is it running in an empty room?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A small IR puck that makes any infrared-remote split air-conditioner or air-to-air heat pump show up as a Matter thermostat, with a radar so it switches off when the room is empty. On a scale of one to ten, how likely would you be to buy that at €49–69 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Matter Bridge for Old Air-Conditioners: would you pay €49–69 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Matter Bridge for Old Air-Conditioners: A small IR puck that makes any infrared-remote split air-conditioner or air-to-air heat pump show up as a Matter thermostat, with a radar so it switches off when the room is empty. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €49–69 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

The split unit in the living room of a flat in Madrid, or the air-to-air heat pump in a Swedish summer house, is the biggest electricity user in the home and the dumbest device in it. Owners want: control from the phone, schedules, "off when nobody is here", and the temperature measured where they sit.

- **Who pays:** the homeowner/tenant (B2C), holiday-rental hosts (they hate guests leaving AC on all day with the windows open), small offices.
- **Who uses:** the household, through the smart-home app they already use.
- **Key promise:** "Works with the AC you already have, and with the app you already use. No new account."

### Market size (estimates — check)

- **TAM:** Europe has tens of millions of installed split ACs/air-to-air heat pumps (southern Europe heavy; Nordics have high air-to-air heat-pump penetration). Assume 40M IR-only indoor units; at €59 per puck = **~€2.4B** theoretical.
- **SAM:** households with a Matter-capable ecosystem and willingness to buy smart-home devices: ~10% → **4M units**, ~€240M.
- **SOM (3 yrs):** **20–40k units** via online direct, Amazon and 1–2 regional retailers; plus holiday-rental bundles.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing — IR remote, manual | Free | Empty-room waste, no scheduling |
| Manufacturer Wi-Fi adapters | Native control, full feature set | €80–150, cloud app per brand, often not Matter, not available for older units |
| SwitchBot Hub 2 / Hub Mini Matter / Universal Remote (~$50–60) | IR hub with Matter bridging, temp/humidity on Hub 2 | Strong competitor. Generic IR remote via its own app/cloud; AC exposed via bridging; no presence radar, not designed as a closed-loop AC thermostat |
| Sensibo-type AC controllers | Polished AC-specific app, climate-react features | Cloud account and app, subscription features; Matter support limited/unclear (verify) |
| Tuya/generic IR blasters | €15–25 | Cloud, flaky AC code support, no presence |
| Home Assistant + ESPHome IR + SmartIR | Free/cheap DIY | For enthusiasts only |

**Wedge:** an AC-specific Matter thermostat with *room-temperature closed loop + presence setback* built in, fully local, no account. Competitors are generic IR hubs with an app; this is a thermostat that happens to speak IR.

### Product & value proposition

- **Hardware:** 55 mm puck, USB-C powered (no mains inside), wide-angle IR LED array (5–8 m), SHT31-class T/RH sensor away from heat sources, LD2410B radar (moving + still people), HM-MT7201 Matter-over-Wi-Fi module with BLE commissioning.
- **Behaviour:** exposes a Matter Thermostat (and/or Room Air Conditioner) device; user sets 21 °C in their app; the puck sends IR commands to hold 21 °C *at the puck*, not at the ceiling. Empty-room setback after N minutes (configurable). Open-window detection (fast temperature drop) as v2.
- **AC codes:** library for top EU-sold brands (from open IR databases + own captures) plus a "learn" mode.
- **Pricing (estimates):** €49–69 retail; holiday-rental 5-pack €249; B2B via installers €39 at volume.

### Unit economics (estimates, EUR per unit)

| Item | 1k | 5k |
|---|---|---|
| HM-MT7201 Matter-over-Wi-Fi module | 3.2 | 2.6 |
| LD2410B radar | 2.5 | 1.9 |
| SHT31-class T/RH | 1.5 | 1.2 |
| IR LEDs ×4 + driver MOSFET + receiver (learning) | 0.8 | 0.6 |
| USB-C, LED, button, passives, PCB | 1.6 | 1.1 |
| Assembly + test (IR output, Matter commissioning, radar) | 2.0 | 1.3 |
| Enclosure (IR-transparent front) | 2.0 | 1.3 |
| USB-C cable + adapter + retail box | 3.8 | 3.0 |
| Freight + duty | 1.0 | 0.6 |
| Certification amortised (CE €12k + Matter €15k = €27k) | 27.0 | 5.4 |
| **Landed cost** | **45.4** | **19.0** |
| Net D2C (€59 incl. VAT ~€49.6 ex VAT) less €5 fulfilment | 44.6 | 44.6 |
| Retail/Amazon margin if indirect (~35% of net) | −17.4 | −17.4 |
| **Gross margin D2C** | **−€0.8 (loss at 1k)** | **€25.6 (57%)** |
| **Gross margin via retail** | **negative** | **€8 (thin)** |

Brutal truth: Matter certification amortised over 1,000 units kills the first batch. Plan for 5k+ in year one, or launch first as "Matter-ready, uncertified" for Home Assistant users (legally fine if you don't use the Matter logo — check the CSA rules) and certify when volume is visible.

### Go-to-market

**First 100 customers:** Home Assistant community forum and subreddit, Matter-focused news sites and communities (e.g. Matter Alpha community), Spanish/Italian/Portuguese smart-home forums and YouTube reviewers, Swedish/Norwegian heat-pump forums (air-to-air "luft-luft värmepump" owners are very active online). Holiday-rental host groups on Facebook (Airbnb hosts in Spain/Italy/Greece).

**Then scale:** Amazon EU, electronics retailers' smart-home shelves, heat-pump installers (sell with every new air-to-air install), utility energy-saving programmes (presence setback = measurable saving).

### 12-month plan

- **Q1:** IR code coverage test on the 15 best-selling split units (kill question); prototype on HM-MT7201 + Grove IR + Grove SHT31 + LD2410B.
- **Q2:** own PCB, Matter firmware with thermostat device type, closed-loop control, 50-unit beta with HA users and 10 holiday rentals.
- **Q3:** CE + Matter certification, 2,000-unit run, D2C launch.
- **Q4:** Amazon EU, installer channel in one Nordic country, open-window detection.

**Team:** embedded/Matter engineer (full-time), IR/AC protocol engineer (part-time, the hard bit), founder on marketing/community, support person part-time after launch. Shenzhen partner for PCBA and enclosure.

**Funding to first 1,000 units (estimate):** landed hardware excl. cert €18k + tooling €10k + CE €12k + Matter (CSA membership + test lab) €15k + IR library work + 8 months team €60k + beta units €3k + launch marketing €8k = **≈€126k**. Pre-orders (500 × €49) ≈ €25k. Rest: angel or a smart-home/energy pre-seed fund; or delay Matter certification to cut €15k.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** IR protocols — ACs use stateful long codes per brand; partial support = support hell | Kill question first; launch only with ≥12 of top 15 working; learning mode as fallback |
| **Technical:** open-loop IR (no feedback if AC actually received the command) | Temperature trend check; resend logic; place guidance (line of sight) in the app |
| **Market:** SwitchBot-type hubs good enough | Differentiate on presence setback + closed loop + no account; show kWh saved |
| **Cost:** Matter certification and CSA membership | Certify one product family; "works with Home Assistant" first if volumes are uncertain |
| **Regulatory:** EN 18031 + CRA for a Wi-Fi device | Security-by-default Matter stack, signed OTA, published support period |
| **Supply:** HM-MT7201 SoC not named in catalogue; LD2410B single source | Ask HopeRF for long-term supply statement; firmware portable to another Matter Wi-Fi SoC |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2) | https://www.gongbans.com/db/hoperf-hm-mt7201.html | Matter over Wi-Fi + BLE commissioning, runs the app | PCB library — HopeRF MIT GitHub folder: https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT7201 | MIT licence for repo content |
| Seeed Grove-Infrared Emitter | https://www.gongbans.com/db/seeed-grove-infrared-emitter.html | IR LED driver reference | Schematic (open download) | Seeed wiki resources — check licence |
| Seeed Grove-TempAndHumi Sensor-SHT31 | https://www.gongbans.com/db/seeed-grove-tempandhumi-sensor-sht31.html | Room T/RH for the closed loop | Schematic (open download) | Seeed wiki resources — check licence |
| HLK-LD2410B/LD2410C presence radar | https://www.gongbans.com/db/hilink-ld2410b.html | Empty-room detection incl. still people | Datasheet public, design files via maker (no open schematics) | Buy as module |

### Block diagram

```
USB-C 5V ──► LDO 3.3V ──► HM-MT7201 (Matter over Wi-Fi, BLE commissioning)
                              │ GPIO/PWM 38 kHz        │ I²C            │ UART
                     IR LED array (4× wide angle)   SHT31 T/RH     LD2410B radar
                     + IR receiver (learn mode)
                              │
      Matter Thermostat / Room AC device ◄──► Apple / Google / Alexa / SmartThings / Home Assistant
      control loop: setpoint vs room T → IR command (mode, temp, fan); presence → setback
```

**Engineering gap:** the AC IR code library and state machine (each AC remote sends full state, not deltas), placing the temperature sensor away from module and LED heat, and Matter device-type mapping.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| HM-MT7201 | €2.5–3.5 | Ask for SDK + long-term availability |
| LD2410B | €2–3 | Single source |
| SHT31/SHT40 | €1.2–1.6 | Thermally isolate (PCB slot) |
| IR LEDs 940 nm ×4 + MOSFET | €0.6 | Wide coverage matters more than power |
| IR receiver (38 kHz) | €0.2 | For learn mode |
| USB-C, LED, button | €0.6 | |
| Enclosure with IR window | €1.5–2 | Tinted PC, IR transparent |
| Retail box, cable, 5 V adapter | €3–4 | Or sell without adapter |

### Firmware/software starting point

- **Matter SDK:** project-chip/connectedhomeip (the open Matter SDK) — HopeRF's module SDK should be based on it; get their SDK and examples (ask the maker).
- **IR codes:** **IRremoteESP8266** (crankyoldgit, open source, large AC protocol coverage — useful as a protocol reference even if you're not on ESP), **SmartIR** for Home Assistant (community AC code JSONs), IRDB-style databases — check licences before shipping codes in a commercial product.
- Control logic: simple hysteresis or PI loop on room temperature with AC mode awareness.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — buy/borrow remotes or test the top 15 EU split units (showrooms, friends, rentals) with an ESP32 + IRremoteESP8266 | ≥12 of 15 units controllable (mode, setpoint, fan, off) — **kill question** |
| 3–5 | **Works-like** — HM-MT7201 dev board + IR + SHT31 + LD2410B; Matter thermostat in 2 ecosystems | Commission in Apple Home + Home Assistant; holds ±0.7 °C room temperature over 24 h |
| 6–8 | **Looks-like + EVT** — own PCB, enclosure, 30 units to beta homes (incl. Nordic air-to-air and Spanish split) | 30 units running 2 weeks; ≥20% runtime reduction from presence setback measured |
| 9–10 | **DVT + pre-compliance** — RED pre-scan (Wi-Fi/BLE + 24 GHz), EN 18031 checklist, Matter pre-test at an authorised lab | No fails; Matter test plan agreed |
| 11–12 | **Pilot batch** — 100 units to pre-order customers | ≤5% "my AC doesn't work" tickets; NPS ≥40; 500 pre-orders for the main run |

### Certification checklist (EU)

- **CE — RED:** EN 300 328 (Wi-Fi/BLE), EN 300 440 (24 GHz radar), EN 301 489-1/-3/-17, EN 62368-1, EN 62311/62479. Estimate €8–12k.
- **EN 18031-1/-2** (RED cybersecurity, mandatory since 1 Aug 2025): internet-connected device processing data about the home (presence = personal data) → both apply. Budget €3–5k. Matter's security model (DAC, PASE/CASE) helps; document it.
- **CRA:** reporting from 11 Sep 2026, full from 11 Dec 2027 — SBOM, OTA updates for the support period, vulnerability handling.
- **Matter certification** (CSA): membership + authorised test lab; estimate €10–20k first product — check the current CSA fee schedule. Needed to use the Matter logo.
- **RoHS, REACH, WEEE**, packaging EPR. No battery. No mains inside (USB-C) → no LVD for the puck itself; the adapter must be CE/ErP compliant (buy a certified one).
- **Ecodesign/energy claims:** if you claim % savings, have test data; avoid greenwashing claims under consumer law.
- **GDPR:** presence data stays local (Matter), no cloud → good. If you add an app/cloud later: EU hosting, privacy policy.
- **Total estimate:** €21–37k incl. Matter.

### Validation toolkit

- **Kill question:** Can we reliably decode/encode the IR protocols of the 15 best-selling split units in EU retail? If fewer than 12 work out of the box, the support cost kills the margin. Cheapest experiment: an ESP32 + IR LED + IRremoteESP8266 sketch, two weekends of testing in electronics-store showrooms (ask politely) and friends' homes.
- **Interview script (5):**
  1. Which AC/heat pump do you have (brand, model, year), and how do you control it today?
  2. How often does it run with nobody in the room? How do you know?
  3. Did you look at the manufacturer's Wi-Fi kit? Why didn't you buy it?
  4. Which smart-home app do you use daily?
  5. Would you pay €59 for "your AC in your smart home, switches off when the room is empty, no new account"?
- **Landing page:** Headline: "Your old air-conditioner, now a smart thermostat." Bullets: "Works with Apple Home, Google Home, Alexa and Home Assistant via Matter." / "Measures the temperature where you sit, not at the ceiling." / "Turns off by itself when the room is empty. No account, no cloud."
- **Pass:** 300 deposits (€10) in 6 weeks from a waitlist of smart-home and heat-pump communities, with ≥70% of them owning a unit from your supported list.

### First production checklist

- Samples: module + radar + sensor from production lots; Matter DAC/PAI provisioning process agreed with the factory (each unit needs a unique attestation certificate — plan this with the module maker early).
- Golden sample: IR output pattern measured, temperature offset calibrated in the enclosure.
- DFM: thermal slot around the sensor, IR window, radar window, wall/shelf mount.
- MOQ: module MOQ, enclosure 1k–2k shots, retail box 2k.
- QC/AQL: 100% IR + radar + commissioning test (QR code readable, Matter pairing code correct); AQL 1.0 functional / 2.5 cosmetic.
- Packaging: Matter QR code on device and box (keep them matched!), quick-start with supported-brand list.
- Incoterms: FOB Shenzhen; DDP to Amazon EU fulfilment later.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and Seeed Studio and Hi-Link (海凌科)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2)](/db/hoperf-hm-mt7201.html) (Matter-over-Wi-Fi module (Wi-Fi 4 + BLE commissioning)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Infrared Emitter](/db/seeed-grove-infrared-emitter.html) (IR LED driver reference); [Seeed Grove-TempAndHumi Sensor-SHT31](/db/seeed-grove-tempandhumi-sensor-sht31.html) (room temperature/humidity for closed-loop setpoint). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410B/LD2410C 24 GHz human-presence radar module](/db/hilink-ld2410b.html) (presence radar for empty-room setback). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and Seeed Studio and Hi-Link (海凌科) websites)

```email
Subject: Sample order and volume pricing — HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module — for a Matter Bridge for Old Air-Conditioners

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Matter Bridge for Old Air-Conditioners: A small IR puck that makes any infrared-remote split air-conditioner or air-to-air heat pump show up as a Matter thermostat, with a radar so it switches off when the room is empty. The design is built around your HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module.

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module.
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
主题：样品订购及批量报价 — HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module — 用于Matter Bridge for Old Air-Conditioners

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Matter Bridge for Old Air-Conditioners：A small IR puck that makes any infrared-remote split air-conditioner or air-to-air heat pump show up as a Matter thermostat, with a radar so it switches off when the room is empty。产品设计基于贵司的HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module。
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
Subject: PCBA quote from open design files — Matter Bridge for Old Air-Conditioners, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Matter Bridge for Old Air-Conditioners: A small IR puck that makes any infrared-remote split air-conditioner or air-to-air heat pump show up as a Matter thermostat, with a radar so it switches off when the room is empty. The design starts from published open-hardware files (HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Matter Bridge for Old Air-Conditioners，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Matter Bridge for Old Air-Conditioners：A small IR puck that makes any infrared-remote split air-conditioner or air-to-air heat pump show up as a Matter thermostat, with a radar so it switches off when the room is empty。设计基于已公开的开源硬件文件（HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Seeed Grove-Infrared Emitter, Seeed Grove-TempAndHumi Sensor-SHT31, HLK-LD2410B/LD2410C 24 GHz human-presence radar module；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Make the list of the 15 best-selling split/air-to-air units in your target country (retailer bestseller pages) — this is the kill-question test list.
2. Build an ESP32 + IR LED test rig with IRremoteESP8266 and test 3 units this weekend.
3. Order the HM-MT7201 samples and ask HopeRF for the Matter SDK, example thermostat app and DAC provisioning process.

Want help sourcing or building this? Talk to us via www.gongbans.com.
