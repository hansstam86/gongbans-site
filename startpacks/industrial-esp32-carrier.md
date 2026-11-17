# Industrial ESP32 DIN Carrier — Founder Start Pack

> An open DIN-rail carrier board for ESP32 projects in real control panels: 9–36 V input, isolated power, isolated RS-485, digital isolators on the I/O — the "make it survive a cabinet" board that makers and integrators keep re-inventing.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** ESP32 and ESPHome are everywhere in light automation, but hobby boards die in cabinets: 24 V spikes, ground loops through RS-485, a contactor switching next door. Integrators either hand-build protection on perfboard or pay PLC prices for a simple Modbus-to-Wi-Fi job.
- **Customer:** System integrators and small OEMs doing 10–500 units, building-automation installers, makers moving Home Assistant/ESPHome projects into real panels. The integrator pays and installs.
- **Product:** One open-hardware PCB in a standard DIN-rail case: 9–36 V wide input with an isolated regulated DC-DC, isolated RS-485 transceiver, quad digital isolator on GPIO, surge/ESD protection, pluggable screw terminals, ESP32-S3. ESPHome and Arduino board definitions. A documented isolation barrier is the selling point.
- **Why now:** Isolated DC-DC and isolated RS-485 transceivers are now cheap modules; ESPHome added Modbus and is the default for small integrators; CRA pressure pushes integrators to use documented, updatable hardware instead of mystery boards.
- **The ask:** ~€60k to certification and 1,000 boards; fundable by pre-orders on a crowdfunding platform popular with makers plus integrator volume orders.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 300 integrators buy a board at €89 when cheaper industrial ESP32 boards exist? The pitch is documented isolation — check with 10 integrators whether that's worth the premium.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** System integrators, OEMs doing small runs, makers moving ESPHome/Arduino projects into control cabinets.

**The problem as the pack states it:** ESP32 and ESPHome are everywhere in light automation, but hobby boards die in cabinets: 24 V spikes, ground loops through RS-485, a contactor switching next door. Integrators either hand-build protection on perfboard or pay PLC prices for a simple Modbus-to-Wi-Fi job.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **PLCtalk forum** · https://www.plctalk.net/ — industrial automation technicians and integrators.
- **r/PLC** · https://www.reddit.com/r/PLC/ — industrial automation engineers and integrators.
- **r/esp32** · https://www.reddit.com/r/esp32/ — ESP32 builders; good for early technical feedback, less for buyers.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **EEVblog forum** · https://www.eevblog.com/forum/ — electronics engineers and serious hobbyists; test-equipment and soldering opinions.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79–109 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how system integrators, OEMs doing small runs, makers moving ESPHome/Arduino projects into control cabinets deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last ESP32 or microcontroller project you put into a control cabinet: what did you build around it for power, isolation and RS-485, and what failed?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] An open DIN-rail carrier board for ESP32 projects in real panels: 9–36 V input, isolated 5/3.3 V, isolated RS-485, digital isolators on the I/O — the 'make it survive a control cabinet' board makers and integrators keep re-inventing. On a scale of one to ten, how likely would you be to buy that at €79–109 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Industrial ESP32 DIN Carrier: would you pay €79–109 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Industrial ESP32 DIN Carrier: An open DIN-rail carrier board for ESP32 projects in real panels: 9–36 V input, isolated 5/3.3 V, isolated RS-485, digital isolators on the I/O — the 'make it survive a control cabinet' board makers and integrators keep re-inventing. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79–109 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

The integrator's job: read a heat meter, inverter or energy meter over Modbus RTU and put it into Home Assistant, a BMS or MQTT. The ESP32 does the work in an afternoon. Then it has to live five years in a cabinet with 24 V supplies, long RS-485 cable runs to another building, and earth differences. That's where it fails.

- **Who pays:** integrators (per project, 1–50 boards), small OEMs (100–1,000/year as their controller), makers (single units, high volume of orders, low per-order value).
- **Who uses:** the integrator's technician at install; the end customer never sees it.
- **Decision trigger:** "I need it in the cabinet next week and I don't want to come back."

### Market size (estimates — check)

- **TAM:** global market for small DIN-rail IoT controllers/gateways in light commercial and residential automation is large and fragmented; for Europe assume 2–3M units/year of small "PLC-light" and gateway devices.
- **SAM:** ESP32-based, open, Modbus-centric, integrator/maker segment in EU: maybe 100–200k units/year (estimate based on the size of the ESPHome/Home Assistant installer community — verify).
- **SOM (3 yrs):** 3–8k boards/year → **€0.3–0.8M revenue/year**. A good small hardware business with very low support cost if the docs are excellent.

### Competition (1 search)

| Alternative | What it is | Why we still win |
|---|---|---|
| DIY: dev board + cheap RS-485 module + buck converter on DIN adapter | €15, everyone does it | No isolation, dies in the field, no documentation for the customer |
| Waveshare ESP32-S3 industrial relay modules (isolated RS-485, DIN case) | Cheap, available | Relay-centric; isolation details and surge ratings thinly documented |
| DFRobot Edge101 (~$40) / ESP32 PLC module (~$239) | ESP32 controllers with isolated RS-485/CAN | Edge101 is a good competitor — beat it on open files, ESPHome definitions and documented isolation; PLC module is expensive |
| LILYGO T-Connect Pro and similar | Feature-rich (Ethernet, LoRa, CAN, screen) | Many features, less focus on documented isolation and surge |
| Real PLCs / commercial Modbus gateways | Certified, robust | €150–500+, closed, not ESPHome |

**Wedge:** *open* schematics + a published isolation and surge test report + first-class ESPHome support. Integrators can show the customer the paperwork. Compete on documentation and trust, not on price.

### Product & value proposition

- **Board:** ESP32-S3 module; 9–36 V input (4:1 isolated regulated DC-DC, 10 W class) → isolated 5 V/3.3 V logic domain; isolated RS-485 with built-in isolated supply and ESD; 4-channel digital isolator for 2 inputs + 2 outputs (open-drain or SSR driver); TVS + reverse polarity + fuse on input; pluggable 5.08 mm terminals; USB-C for flashing; optional Ethernet SKU later.
- **Case:** standard 2–3 module DIN housing (buy, don't tool).
- **Docs:** isolation diagram, creepage/clearance table, surge test results, ESPHome YAML examples for 10 common meters, Arduino board package.
- **Pricing (estimates):** €79–109 single unit; €69 at 10+; OEM pricing €45–55 at 500+ without case. Bare PCB + files free (open hardware sells hardware).

### Unit economics (estimates, EUR per board incl. DIN case)

| Item | 1k | 5k |
|---|---|---|
| ESP32-S3 module | 3.0 | 2.6 |
| Isolated DC-DC 10 W wide-input (LD-10WR3 class) | 6.5 | 5.2 |
| Isolated RS-485 module (TD521D485H-A class) | 4.5 | 3.6 |
| Quad digital isolator (CMT804X class) | 1.2 | 0.9 |
| Protection (TVS, fuse, reverse-polarity), terminals, USB-C, passives | 3.5 | 2.6 |
| PCB 4-layer | 1.5 | 1.0 |
| Assembly + test (isolation hi-pot sample + functional) | 3.0 | 2.0 |
| DIN case (bought) | 3.0 | 2.2 |
| Packaging | 0.8 | 0.5 |
| Freight + duty | 1.2 | 0.8 |
| Certification amortised (€12k) | 12.0 | 2.4 |
| **Landed cost** | **40.2** | **23.8** |
| Net price direct webshop (€89 incl. VAT → €75 ex VAT) less €5 fulfilment | 70 | 70 |
| Distributor margin if via an electronics distributor (35%) | −26 | −26 |
| **Gross margin direct** | **€29.8 (43%)** | **€46.2 (66%)** |
| **Gross margin via distributor** | **€3.5 — too thin at 1k** | **€20** |

Lesson: sell direct until 5k volume; distributors only after cost-down.

### Go-to-market

**First 100 customers:** Home Assistant community forum and ESPHome Discord (show the isolation test video), r/homeassistant and r/PLC, German-language forums for building automation (e.g. KNX-user-forum, photovoltaikforum for meter-reading use cases), Tindie/Elecrow/Crowd Supply-style launch for makers. Integrators: 20 targeted demos to small electrical/automation firms doing heat-pump and PV monitoring.

**Then scale:** OEM deals (small heat-pump, ventilation or battery-storage makers needing a controller), electronics distributors with maker programmes, ESPHome "made for ESPHome"-style listing (check the current programme), integrator training webinars.

### 12-month plan

- **Q1:** schematic and layout from open references; 10 rev-A boards; interview 10 integrators (kill question); publish schematics on GitHub.
- **Q2:** surge/ESD/isolation tests at a lab; rev B; pre-order campaign (target 300 boards).
- **Q3:** CE (EMC industrial + RED via module), 1,000-board run, webshop.
- **Q4:** Ethernet SKU EVT, 2 OEM pilots, distributor talks.

**Team:** hardware engineer-founder (power/isolation experience is essential), firmware/docs person (part-time, ESPHome contributor ideal), community/sales (founder). Shenzhen partner for PCBA and module sourcing.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €28k + certification + surge testing €12k + prototypes €4k + 6 months part-time team €20k + launch marketing €3k = **≈€67k**. 300 pre-orders × €79 = €24k; integrator pre-payments €10–15k. Bootstrappable with a small angel or founder savings for the gap.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** €89 too high vs €40 Edge101-class boards | Interview 10 integrators before layout; if they won't pay for documented isolation, pivot to OEM-only |
| **Technical:** isolation barrier claims wrong (creepage, coupling capacitance, ESP32 antenna near barrier) | Follow module datasheet layouts; independent hi-pot and surge tests; publish results |
| **Regulatory:** "board" vs "finished product" — CE and CRA obligations apply once sold to end users | Sell in a case as a finished product with CE; bare boards labelled for professional integration |
| **Supply:** Hi-Link DC-DC and RS-485 modules are design-files-via-maker | Pin-compatible alternatives exist from several isolated-module makers (SIP/DIP standard footprints) — qualify one |
| **Support:** integrators expect help with every meter | ESPHome YAML library + community forum; paid support only for OEMs |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link LD-10WR3 series wide-input isolated DC-DC (10 W, 4:1, 9–36 V) | https://www.gongbans.com/db/hilink-ld-10wr3-series.html | 9–36 V input → isolated regulated rail | Datasheet public, design files via maker (no open schematics) | Buy as module |
| Hi-Link TD521D485H-A isolated RS-485 transceiver module | https://www.gongbans.com/db/hilink-td521d485h-a.html | RS-485 with built-in isolated supply, signal isolation, ESD; auto direction | Datasheet public, design files via maker (no open schematics) | Buy as module |
| HopeRF CMT804X quad digital isolator | https://www.gongbans.com/db/hoperf-cmt804x.html | Isolated GPIO channels | Schematic + PCB — HopeRF MIT GitHub folder: https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Isolator/SCH_PCB/CMT804X | MIT licence for repo content |
| Espressif ESP32-S3-DevKitC-1 | https://www.gongbans.com/db/espressif-esp32-s3-devkitc-1.html | ESP32-S3 reference (USB, boot, module placement) | Schematic + PCB (open download) | Espressif reference design — check the terms on the download |

### Block diagram

```
 9–36 V DC ──► fuse + TVS + reverse-polarity ──► LD-10WR3 isolated DC-DC ──► 5 V ─► LDO 3.3 V
 (field side)                 ║ isolation barrier ║                              (logic side)
                                                                                    │
 RS-485 A/B/GND_iso ◄──► TD521D485H-A (isolated, ESD) ◄── UART ──► ESP32-S3 module (Wi-Fi/BLE)
 2× DI / 2× DO (field) ◄─► CMT804X quad isolator ◄── GPIO ──┘          │
                                                                   USB-C (flash/debug)
 DIN-rail case, pluggable terminals, status LEDs
```

**Engineering gap:** the barrier layout (creepage/clearance per EN 62368-1 for the voltages you claim), input surge design for EN 61000-6-2 levels, and grounding of the field-side GND for the I/O. Plus the documentation — that is the product.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-S3-WROOM-1 module | €2.6–3 | Pre-certified radio |
| LD-10WR3 (UR, 24 V nominal 9–36 V) | €5–7 | Standard DIP footprint, alternatives exist |
| TD521D485H-A | €4–5 | Check 5 V vs 3.3 V logic variant (TD521 vs TD321) |
| CMT804X | €1–1.5 | Choose channel direction variant to match DI/DO |
| TVS (SMBJ33A-class), PTC fuse, reverse-polarity MOSFET | €0.8 | |
| Pluggable terminal blocks | €1.5 | Long lead in some colours — order early |
| DIN-rail case (3-module) | €2–3 | Buy standard; no tooling |
| PCB 4-layer, 1.6 mm | €1.5 | |

### Firmware/software starting point

- **ESPHome** (board definition + `modbus_controller` component — exists) and **Arduino-ESP32** board package.
- **ESP-IDF** for OEM firmware; Modbus libraries exist for both (e.g. esp-modbus from Espressif — verify).
- Publish your own repo with KiCad files, YAML examples per meter, and the isolation test report.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 integrator interviews; landing page with price and "notify me" | ≥5 of 10 say they'd pay ≥€79 for documented isolation; ≥100 sign-ups |
| 3–5 | **Works-like** — dev-kit + modules on a protoboard in a real cabinet reading 2 meters via Modbus | 2 weeks stable reading in a real panel; no resets during contactor switching |
| 6–8 | **Looks-like + EVT** — rev A PCB in DIN case; 20 boards to 10 integrators | All 20 boards running; feedback on terminals/LEDs; hi-pot passes at claimed isolation on samples |
| 9–10 | **DVT + pre-compliance** — surge/burst/ESD pre-test to EN 61000-4-2/-4/-5, radiated emissions pre-scan | Pass at industrial immunity levels with margin; docs v1 published |
| 11–12 | **Pilot batch** — 50 boards sold to pre-order customers | <2% returns; 5 public write-ups/forum posts; pre-orders for the 1k run ≥300 |

### Certification checklist (EU)

- **CE — RED** (Wi-Fi/BLE via the ESP32-S3 module): EN 300 328, EN 301 489-1/-17, EN 62368-1, EN 62311. Module certification helps but the product still needs its own assessment. Estimate €5–8k.
- **EMC industrial:** EN 61000-6-2 (immunity) and EN 61000-6-4 or -6-3 (emissions) depending on where you claim use. Surge/burst tests are where boards fail — budget €3–5k.
- **EN 18031-1** (RED cybersecurity): Wi-Fi device → in scope. ESPHome supports encrypted API and OTA passwords; document secure defaults. Budget €2–4k.
- **CRA:** finished products with digital elements — SBOM, vulnerability handling, security updates for the support period; reporting from 11 Sep 2026, full application 11 Dec 2027. Open firmware helps but doesn't remove your obligations as manufacturer.
- **RoHS, REACH, WEEE** (B2B registration), packaging EPR.
- No battery, no personal data by default (if customers log meter data of households, that's their GDPR job — say so in the docs).
- **Total estimate:** €10–16k.

### Validation toolkit

- **Kill question:** Will 300 integrators/makers buy a board at €89 when cheaper industrial ESP32 boards exist? The pitch is documented isolation — check with 10 integrators whether that's worth the premium. Cheapest experiment: landing page with the block diagram, price and a "reserve for €10" button, posted in the Home Assistant forum and 2 integrator groups.
- **Interview script (5):**
  1. Which ESP32/Modbus jobs did you do this year, and what board did you use?
  2. Have you had a field failure from spikes, ground loops or RS-485 issues? What did it cost you?
  3. What do you show your customer about the hardware (documents, CE, test reports)?
  4. What would make you trust a new board in a cabinet you have to guarantee for 2 years?
  5. Price: €69, €89 or €109 — at which price is it a no-brainer, and at which do you go back to DIY?
- **Landing page:** Headline: "The ESP32 board that survives the cabinet." Bullets: "9–36 V input, isolated power and isolated RS-485." / "Open schematics and a published surge and isolation test report." / "ESPHome and Arduino ready, DIN-rail case included."
- **Pass:** ≥300 reservations (or 150 paid pre-orders) in 6 weeks, or 2 OEMs committing to ≥200 units each.

### First production checklist

- Samples: 10 of each isolated module from two lots; hi-pot test each sample at the rated isolation.
- Golden sample: full surge/ESD pass, documented; terminal torque and labelling checked.
- DFM: barrier slot in PCB if needed for creepage, conformal coating option, LED light pipes in the case.
- MOQ: isolated modules often MOQ 500–1,000; terminals 1k; case 1k.
- QC/AQL: 100% functional (RS-485 loopback, DI/DO, Wi-Fi join), hi-pot on a sample per lot (or 100% if you claim reinforced), AQL 0.65 functional / 2.5 cosmetic.
- Packaging: anti-static bag + box, printed isolation diagram, QR to docs.
- Incoterms: FOB Shenzhen; DDP for webshop stock to the EU warehouse.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and HopeRF (华普微) and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP](/db/hilink-ld-10wr3-series.html) (10 W 4:1 wide-input isolated DC-DC converter); [Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module](/db/hilink-td521d485h-a.html) (isolated RS-485 transceiver module). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT804X quad-channel digital isolator](/db/hoperf-cmt804x.html) (quad-channel digital isolator for I/O (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-s3-devkitc-1](/db/espressif-esp32-s3-devkitc-1.html) (ESP32-S3 reference design (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) and Espressif websites)

```email
Subject: Sample order and volume pricing — Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1 — for a Industrial ESP32 DIN Carrier

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Industrial ESP32 DIN Carrier: An open DIN-rail carrier board for ESP32 projects in real panels: 9–36 V input, isolated 5/3.3 V, isolated RS-485, digital isolators on the I/O — the 'make it survive a control cabinet' board makers and integrators keep re-inventing. The design is built around your Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1.

Could you please send:
1. Price and lead time for [10] sample units of each: Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1.
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
主题：样品订购及批量报价 — Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1 — 用于Industrial ESP32 DIN Carrier

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Industrial ESP32 DIN Carrier：An open DIN-rail carrier board for ESP32 projects in real panels: 9–36 V input, isolated 5/3.3 V, isolated RS-485, digital isolators on the I/O — the 'make it survive a control cabinet' board makers and integrators keep re-inventing。产品设计基于贵司的Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1。
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
Subject: PCBA quote from open design files — Industrial ESP32 DIN Carrier, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Industrial ESP32 DIN Carrier: An open DIN-rail carrier board for ESP32 projects in real panels: 9–36 V input, isolated 5/3.3 V, isolated RS-485, digital isolators on the I/O — the 'make it survive a control cabinet' board makers and integrators keep re-inventing. The design starts from published open-hardware files (Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Industrial ESP32 DIN Carrier，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Industrial ESP32 DIN Carrier：An open DIN-rail carrier board for ESP32 projects in real panels: 9–36 V input, isolated 5/3.3 V, isolated RS-485, digital isolators on the I/O — the 'make it survive a control cabinet' board makers and integrators keep re-inventing。设计基于已公开的开源硬件文件（Hi-Link VR(A)B/UR(A)B_LD-10WR3 10 W wide-input isolated regulated DC-DC converter, DIP, Hi-Link TD521D485H-A / TD321D485H-A isolated RS-485 transceiver module, HopeRF CMT804X quad-channel digital isolator, Espressif esp32-s3-devkitc-1；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Call or message 10 integrators who do Modbus/meter jobs; ask questions 2 and 5 from the script.
2. Download the ESP32-S3-DevKitC-1 files and the CMT804X folder; order samples of an LD-10WR3 (24 V UR variant) and a TD521D485H-A; build the protoboard version.
3. Draft the isolation diagram and test plan as a one-page PDF — publish it before the board exists; it is your marketing.

Want help sourcing or building this? Talk to us via www.gongbans.com.
