# mmWave Radar Dev Carrier — Founder Start Pack

> An open carrier board with footprints for the popular 24 GHz and 60 GHz radar modules plus an ESP32-C6, ESPHome-ready out of the box — so makers and product teams can prototype any radar idea in an afternoon.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Radar modules cost a few euros, but every project rewires UART, power, level shifting and mounting from scratch. 60 GHz modules need a beefy 3.3 V rail that a dev-kit regulator can't give. Product teams prototyping radar ideas lose days on plumbing before they test the actual idea.
- **Customer:** Home Assistant/ESPHome makers (they buy and use), hardware product teams and design houses prototyping presence/occupancy products (they buy several), university labs. Maker shops and distributors sell it.
- **Product:** One PCB with an ESP32-C6 module, a 1.5 A 3.3 V rail, switchable 3.3/5 V radar supply, footprints/sockets for several Hi-Link 24 GHz and 60 GHz modules, a light sensor, USB-C, and 3D-printable enclosures for ceiling, wall and desk. ESPHome YAML per supported module; Matter build option on the C6.
- **Why now:** mmWave presence is the hottest sensor category in DIY smart home; the Matter/Thread-capable ESP32-C6 is cheap; and product ideas built on radar keep multiplying — a common, open carrier is the missing piece.
- **The ask:** ~€40k to first 1,000 boards, mostly bootstrapped via pre-orders. Kill question: 500 maker sales within 3 months of launch.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 500 makers buy the board within 3 months of a launch on a maker marketplace? If it doesn't sell to makers, it won't seed product teams either.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Makers, Home Assistant community, product teams prototyping radar products (like many ideas on this list).

**The problem as the pack states it:** Radar modules cost a few euros, but every project rewires UART, power, level shifting and mounting from scratch. 60 GHz modules need a beefy 3.3 V rail that a dev-kit regulator can't give. Product teams prototyping radar ideas lose days on plumbing before they test the actual idea.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **r/Esphome** · https://www.reddit.com/r/Esphome/ — ESPHome builders; mmWave presence sensors are a frequent topic.
- **r/esp32** · https://www.reddit.com/r/esp32/ — ESP32 builders; good for early technical feedback, less for buyers.
- **Hackaday / hackaday.io** · https://hackaday.io/ — maker audience; visibility more than buyers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€29–39 board / 59–89 with radar (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how makers, Home Assistant community, product teams prototyping radar products deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last presence or radar sensor you wired up: which module, how long did it take to get working, and what was the fiddliest part?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] An open carrier board with footprints for the popular 24 GHz and 60 GHz radar modules plus an ESP32-C6, ESPHome-ready out of the box — so makers and product teams prototype any radar idea in an afternoon. On a scale of one to ten, how likely would you be to buy that at €29–39 board / 59–89 with radar (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: mmWave Radar Dev Carrier: would you pay €29–39 board / 59–89 with radar (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a mmWave Radar Dev Carrier: An open carrier board with footprints for the popular 24 GHz and 60 GHz radar modules plus an ESP32-C6, ESPHome-ready out of the box — so makers and product teams prototype any radar idea in an afternoon. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €29–39 board / 59–89 with radar (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A maker wants to try a 60 GHz module for a sleeping-room presence sensor. They solder jumper wires to a 1.27 mm-pitch header, power it from a dev kit's 3.3 V pin, and it browns out because the module wants up to 600 mA (per the brochure). The product team down the road wants to compare a 24 GHz and a 60 GHz module in the same housing for a client and spends a week on a test jig.

- **Who pays, makers:** Home Assistant users (D2C via shops and marketplaces), €30–60 per order.
- **Who pays, pros:** hardware startups, design houses, integrators prototyping occupancy, lighting and care products — they buy 5–20 boards plus modules and value documentation and speed over price.
- **Who uses:** firmware/hardware engineers, students in IoT courses.

### Market size (estimates — check)

- **TAM:** Home Assistant claims a very large install base (check their current public number — it's in the millions worldwide); assume 25% in Europe and 10% interested in DIY radar → order of 100k+ potential buyers in EU at ~€45 → **~€5M+**. Plus pro/edu demand.
- **SAM:** makers who buy boards rather than finished sensors + product teams: assume 30k units over 3 years → **~€1.3M**.
- **SOM (3 years):** **5–10k boards** → €0.2–0.4M. This is a funnel product (for radar-module sales, design services and community) as much as a business.

### Competition (1 search)

| Alternative | What it is | Why we can still win |
|---|---|---|
| Do nothing / dupont wires to a dev kit | Free | Brown-outs, flaky wiring, no enclosure |
| Everything Presence Lite / One | Finished ESPHome presence sensors (LD2450-based Lite ~£28–39) | Finished product, one radar; not a carrier for swapping modules |
| Apollo Automation MTR-1 / MSR | ESPHome multisensors (MTR-1 with LD2450, ~$40) | Same: one radar, not a prototyping platform |
| Generic ESP32 + LD2410 boards (AliExpress) | Cheap | Undocumented, no 60 GHz support, no enclosures |
| Chip/module vendors' eval kits | Official | One module each, vendor tools, not ESPHome-ready |

**Wedge:** the only (that we found) open carrier that takes several radar modules, both 24 and 60 GHz, with the power rail they actually need, tested ESPHome configs and printable enclosures. For product teams: "swap the module, keep the jig."

### Product & value proposition

- **Core:** ESP32-C6 module (Wi-Fi 6, BLE, 802.15.4/Thread). Alternative build with an M5Stack Stamp-C5 (open Altium files) for teams that want a stamp form factor.
- **Power:** USB-C 5 V in; 3.3 V/1.5 A buck for the 60 GHz modules; jumper or load switch for 3.3/5 V radar supply (LD2410B/C runs on 3.3 or 5 V; LD6002B on 3.3 V).
- **Radar sockets:** LD2410B/C footprint (24 GHz presence), LD6002B footprint (60 GHz 3D presence), plus a generic 2×4/1×5 UART header for other modules. One radar populated at a time (UART mux optional in rev B).
- **Extras:** light sensor, status LED, boot/reset buttons, Qwiic/Grove-style I²C connector, breakout for GPIOs.
- **Enclosures:** 3D-printable STL/STEP for ceiling, wall-angle and desk mounts with radome-friendly front (thin, no metal-flake filament).
- **Software:** ESPHome YAML per module; example dashboards; an "explore" web page that streams raw radar targets for tuning.
- **Openness:** publish your own carrier design under an open hardware licence (e.g. CERN-OHL-P/S) — check compatibility with anything you reuse.

**Pricing (estimates):** board **€35**; board + LD2410C **€59**; board + LD6002B **€89**; team pack (5 boards + 5 of each radar) €449.

### Unit economics (estimates, EUR, board without radar)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C6 module ~€2.8, 3.3 V/1.5 A buck €0.8, radar supply switch €0.5, sockets/headers €1.0, USB-C + ESD €0.5, light sensor €0.6, 4-layer PCB €1.2, buttons/LEDs €0.3) | 7.7 | 6.6 |
| PCBA assembly + test | 1.5 | 1.0 |
| Enclosure | 0 (printable files) | 0 |
| Packaging (antistatic bag, card) | 0.8 | 0.6 |
| Freight + duty to EU | 0.4 | 0.3 |
| Certification amortised (€10k) | 10.0 | 2.0 |
| **Landed cost** | **20.4** | **10.5** |
| D2C at €35 incl. VAT → €29.4 net, less €4 fulfilment | 25.4 | 25.4 |
| **Gross margin D2C, board** | **€5.0 (20%)** | **€14.9 (59%)** |
| Bundle with LD2410C at €59 (radar ~€4 landed) → €45.6 after fulfilment | €21.2 (46%) | €31.1 (68%) |
| Distributor (pays ~60% of net) — board at €35 → €17.6 | -€2.8 | €7.1 (40%) |

The money is in bundles and team packs, not the bare board. Sell bundles first.

### Go-to-market

**First 100 customers:**
- Home Assistant community forum and r/homeassistant: a build log with raw radar data and power measurements (the 60 GHz brown-out story is a good hook).
- ESPHome devices directory: get the board listed (devices.esphome.io accepts community device pages — check process).
- Maker marketplaces (Tindie, Crowd Supply, Elecrow/Seeed-type fusion shops — check fees) for the first 200.
- Direct outreach to 20 European hardware design houses and university IoT labs: "radar prototyping kit, 5-pack".

**Then scale:** EU maker distributors, bundles with the radar modules, a "radar prototyping" workshop format at makerspaces, and a funnel to custom carrier designs for product teams (paid engineering).

### 12-month plan

- **Q1:** rev 0 on hand-assembled boards; ESPHome configs for LD2410C and LD6002B; 30 beta testers.
- **Q2:** rev A, enclosures, docs site; pre-order campaign; RED/EMC pre-scan.
- **Q3:** certification, 1,000-board run; launch; team packs to design houses.
- **Q4:** add footprints for further modules (multi-target LD2450/LD2454-class, 60 GHz vital-signs modules as "wellness research" only), Matter example, second distributor.

**Team:** founder-engineer (hardware + ESPHome), part-time community/docs person, Shenzhen PCBA partner. That's it.

**Funding to first 1,000 boards (estimate):** landed hardware excl. cert (1,000 × €10.4) €10k + radar modules for bundles (500 × €4) €2k + certification €10k + prototypes/beta €3k + 4 months part-time runway €12k + samples/marketing €3k = **≈€40k**. Offsets: pre-orders (300 × €45 average = €13.5k). Net need **≈€25k**. Route: bootstrap + pre-orders.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** makers buy finished sensors (EP Lite, MTR-1) instead | Position for prototyping and product teams, not as a presence sensor; bundles + team packs |
| **Technical:** radar modules have different pinouts/voltages; future modules change | Generic UART header + adapter PCBs; version the footprints |
| **Technical:** radar performance depends on enclosure (radome) | Publish radome guidelines and tested enclosure files; measure each |
| **Regulatory:** bundles = you place a radio product on the market | Certify the bundles you sell; bare boards with the pre-certified C6 module still need RED for the board |
| **Supply:** Hi-Link modules (no open files; specs and protocols from the maker) | Keep relationships with distributors; support 2+ vendors' modules over time |
| **Community:** clones of an open design | Expected. Win on docs, configs and speed — and sell the custom-carrier service |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2410B/LD2410C 24 GHz presence radar | https://www.gongbans.com/db/hilink-ld2410b.html | 24 GHz presence/micro-motion, 3.3/5 V, UART + GPIO, 0.75–6 m, LD2410B 7×35 mm / LD2410C 16×22 mm | Datasheet public, files via maker (no open schematic) | Buy as module |
| HLK-LD6002B 60 GHz 3D presence radar (2T2R) | https://www.gongbans.com/db/hilink-ld6002b.html | 60 GHz 3D presence up to 3 persons, 3 m, 3.3 V/600 mA, UART, 25×23 mm | Datasheet public, files via maker (no open schematic) | Buy as module |
| Espressif ESP32-C6-DevKitC-1 | https://www.gongbans.com/db/espressif-esp32-c6-devkitc-1.html | Wi-Fi 6/BLE/Thread core reference | Reference files via Espressif docs (catalogue lists no file set) | Espressif docs CC BY-SA 4.0 / Apache-2.0 — check before copying schematics |
| M5Stack Stamp-C5 (S016) | https://www.gongbans.com/db/m5stack-stamp-c5.html | Alternative core as a stamp, open Altium electronics | pcb, schematic, sch_lib, pcb_lib | M5_Hardware repo — check licence |

### Block diagram

```
USB-C 5 V ─► ESD + polyfuse ─┬─► buck 3.3 V/1.5 A ─┬─► ESP32-C6 module (Wi-Fi 6 / BLE / Thread)
                             │                      │        │ UART1      │ I²C
                             └─► load switch ───────┴─► radar supply (3.3 or 5 V jumper)
                                                     │
              ┌──────────────┬──────────────┬────────┴─────────┐
        LD2410B/C socket  LD6002B socket  generic UART header  light sensor, LED, buttons, Qwiic
ESP32-C6 native USB ─► flashing + serial log; ESPHome YAML per module; optional Matter firmware
```

**Engineering gap:** clean power for 60 GHz (current spikes, ripple), radar placement on the PCB vs antenna keep-outs of the C6, a footprint plan that won't trap you when module families change, and tested, documented configs.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-C6 module (e.g. WROOM-class, pre-certified) | €2.5–3.0 | Multiple distributors |
| 3.3 V/1.5 A synchronous buck | €0.6–0.9 | Size for LD6002B peaks |
| Load switch / jumper for radar rail | €0.3–0.5 | |
| Radar sockets (1.27 mm/2.54 mm headers) | €0.8–1.2 | Or castellated adapter boards |
| Ambient light sensor | €0.4–0.6 | |
| LD2410C (bundle) | €3–4 | |
| LD6002B (bundle) | €12–18 | Ask Hi-Link; 60 GHz modules cost more |

### Firmware/software starting point

- **ESPHome**: has an `ld2410` component (LD2410/B/C) and an `ld2450` component; **check current support for the LD6002 family** (if missing, write an external component from Hi-Link's protocol document and publish it — that alone will sell boards). Check ESPHome's current ESP32-C6 support status (ESP-IDF framework).
- **ESP-IDF + esp-matter** for the Matter build option (occupancy sensor device type). Matter certification is only needed if you sell it as Matter-certified — makers' builds don't need it.
- Docs: a static site (e.g. MkDocs) with wiring, YAML, measurements, enclosure files.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — landing page + forum post with renders and a price; 10 product-team interviews | ≥300 sign-ups or ≥100 €5 deposits; ≥3 product teams say they'd buy a 5-pack |
| 3–5 | **Works-like** — rev 0 board, both radars running in ESPHome, power measurements | No brown-outs with LD6002B under Wi-Fi TX; configs stable 72 h |
| 6–8 | **Looks-like + EVT** — rev A + 3 printed enclosures, 30 beta boards | Beta testers get a radar running in <30 min from the docs |
| 9–10 | **DVT + pre-compliance** — rev B, RED/EMC pre-scan with each bundle, EN 18031 checklist | No pre-scan fails; security defaults documented (no default passwords, OTA signed) |
| 11–12 | **Pilot batch** — 200 boards + bundles on a marketplace | 200 sold; <2% returns; on track for 500 in 3 months (kill question) |

### Certification checklist (EU)

- **CE — RED** (the board contains a radio module): EN 300 328 (Wi-Fi/BLE), EN 300 440 or the relevant SRD standard for 802.15.4 if used, EN 301 489-1/-17, EN 62368-1, EN 62311. Pre-certified C6 module lets you reuse radio reports.
- **Bundles with radar:** add EN 300 440 (24 GHz) and **EN 305 550** (40–246 GHz SRD, for 60 GHz) plus EN 301 489-3. Radar modules' own reports help.
- **EN 18031-1:** yes for the finished, internet-capable product; EN 18031-2 if your default firmware processes personal data (presence is arguably personal data in a home). Ship secure defaults.
- **CRA:** product with digital elements — default firmware updates, SBOM, vulnerability contact by Dec 2027. Note: CRA has provisions for products supplied for development/testing purposes; check whether a dev board sold to makers benefits from them (don't assume).
- **RoHS, REACH, WEEE**, packaging registration.
- **GDPR:** not your data (local ESPHome), but say so; if you ever add a cloud, revisit.
- No battery, no MDR (if you add vital-signs radar modules later: research/wellness use only, no health claims — MDR boundary), no toy directive.
- **Estimated test costs:** €8–12k for board + two bundles.

### Validation toolkit

- **Kill question:** Will 500 makers buy the board within 3 months of a launch on a maker marketplace? If it doesn't sell to makers, it won't seed product teams either. **Cheapest experiment:** renders + a 2-minute video of both radars on a hand-built board, posted on the HA forum with a deposit link.
- **Interview script (5) — makers/product teams:**
  1. What was your last radar project, and what went wrong in the wiring/power?
  2. Which modules have you tried? Which do you want to try next?
  3. Would you rather buy a finished sensor or a carrier — why?
  4. What documentation would save you the most time?
  5. €35 board / €59 with a 24 GHz module / €89 with 60 GHz: which would you buy today?
- **Landing page:** Headline: "Any radar idea, running in an afternoon." Bullets: "24 GHz and 60 GHz module sockets, with the power rail 60 GHz actually needs." / "ESPHome configs and printable enclosures for ceiling, wall and desk." / "Open hardware. Swap the module, keep the jig."
- **Pre-order pass:** ≥150 deposits/pre-orders in 30 days **or** 3 product-team 5-packs paid.

### First production checklist

- **Samples:** 10 PCBAs; golden sample with measured 3.3 V rail under LD6002B load and Wi-Fi TX.
- **DFM review:** antenna keep-out, socket coplanarity, panelisation, test pads for flashing.
- **MOQ talk:** C6 modules (reel 650–1k), radar modules for bundles (ask Hi-Link for 500/1k pricing).
- **QC/AQL:** ISO 2859-1 level II, AQL 0.65/2.5; 100% flash + self-test (Wi-Fi scan, UART loopback on the radar header, rail voltages); sample radar bundle test.
- **Packaging:** ESD bag, pin-out card, QR to docs.
- **Incoterms:** FOB Shenzhen or express DAP for 1k (small parcel).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and Espressif and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410B/LD2410C 24 GHz human-presence radar module](/db/hilink-ld2410b.html) (24 GHz presence radar footprint); [HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R)](/db/hilink-ld6002b.html) (60 GHz 3D presence radar footprint). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c6-devkitc-1](/db/espressif-esp32-c6-devkitc-1.html) (Wi-Fi 6 / Thread MCU reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Stamp-C5 (S016)](/db/m5stack-stamp-c5.html) (Wi-Fi MCU stamp with open schematic + PCB as an alternative core). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and Espressif and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016) — for a mmWave Radar Dev Carrier

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a mmWave Radar Dev Carrier: An open carrier board with footprints for the popular 24 GHz and 60 GHz radar modules plus an ESP32-C6, ESPHome-ready out of the box — so makers and product teams prototype any radar idea in an afternoon. The design is built around your HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016).
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
主题：样品订购及批量报价 — HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016) — 用于mmWave Radar Dev Carrier

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款mmWave Radar Dev Carrier：An open carrier board with footprints for the popular 24 GHz and 60 GHz radar modules plus an ESP32-C6, ESPHome-ready out of the box — so makers and product teams prototype any radar idea in an afternoon。产品设计基于贵司的HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016)。
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
Subject: PCBA quote from open design files — mmWave Radar Dev Carrier, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a mmWave Radar Dev Carrier: An open carrier board with footprints for the popular 24 GHz and 60 GHz radar modules plus an ESP32-C6, ESPHome-ready out of the box — so makers and product teams prototype any radar idea in an afternoon. The design starts from published open-hardware files (HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — mmWave Radar Dev Carrier，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款mmWave Radar Dev Carrier：An open carrier board with footprints for the popular 24 GHz and 60 GHz radar modules plus an ESP32-C6, ESPHome-ready out of the box — so makers and product teams prototype any radar idea in an afternoon。设计基于已公开的开源硬件文件（HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HLK-LD6002B 60 GHz 3D human-presence radar module (2T2R), Espressif esp32-c6-devkitc-1, M5Stack Stamp-C5 (S016)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order 2× LD2410C, 2× LD6002B, an ESP32-C6-DevKitC-1 and a Stamp-C5; measure the LD6002B current profile on a scope before you draw a single trace.
2. Check ESPHome's current support for the LD6002 family; if there's none, start the external component — publish it early.
3. Post a build log on the Home Assistant forum with the power measurements and a deposit link for the carrier.

Want help sourcing or building this? Talk to us via www.gongbans.com.
