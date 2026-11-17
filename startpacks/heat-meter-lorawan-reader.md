# Isolated Heat-Meter Reader (LoRaWAN) — Founder Start Pack

> A small isolated box that reads heat, cooling and water meters with an RS-485/Modbus output in apartment blocks and plant rooms and sends the readings over LoRaWAN. Old meters become remotely readable without being replaced.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The recast EU Energy Efficiency Directive (EU) 2023/1791 requires heat, cooling and hot-water meters to be remotely readable. Industry sources point to **1 January 2027** as the date by which installed meters must be remote-readable or replaced, unless replacement isn't cost-effective ([Brunata](https://brunata.com/solutions/eed/), [Diehl Metering](https://www.diehl.com/cms/files/Diehl_Metering_Energie_Efficiency_Directive_Brochure_EN.pdf?download=1); check the national transposition). Many working meters in plant rooms and substations have a wired output but nobody to read it remotely. Replacing a working meter costs a plumber visit plus the meter.
- **Customer:** Housing associations, district-heating operators, metering service companies and building-management firms in NL, DE, DK, PL, AT and the Nordics. The metering service company or the housing association's technical department pays; tenants receive the consumption information.
- **Product:** A DIN-rail box with a galvanically isolated RS-485 port (HopeRF CMT83085: 5 kVrms isolation), an isolated wide-input DC-DC supply, and a LoRa radio. It polls Modbus registers from common heat/cooling/water meters, buffers hourly/daily values and sends them over LoRaWAN with a published payload codec. An M-Bus variant follows.
- **Why now:** The regulatory deadline is close. LoRaWAN is already the network many metering firms use. Ground-loop failures in plant rooms kill cheap non-isolated converters; isolation is the reliability feature.
- **The ask:** About €140k (estimate) to reach 1,000 units. Route: pre-orders from 2–3 metering service companies (they need a deadline solution), an energy-efficiency innovation grant, then a strategic investor from metering.

**Positioning: not a legal-metrology device.** It transports readings; the meter stays the legal instrument.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Are enough installed heat meters Modbus-RS485 rather than wired M-Bus? Ask 3 housing associations for their meter inventory before building; if <30% Modbus, pivot to M-Bus first.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Housing associations, district-heating operators, metering service companies in NL, DE, DK, PL.

**The problem as the pack states it:** The recast EU Energy Efficiency Directive (EU) 2023/1791 requires heat, cooling and hot-water meters to be remotely readable. Industry sources point to **1 January 2027** as the date by which installed meters must be remote-readable or replaced, unless replacement isn't cost-effective ([Brunata](https://brunata.com/solutions/eed/), [Diehl Metering](https://www.diehl.com/cms/files/Diehl_Metering_Energie_Efficiency_Directive_Brochure_EN.pdf?download=1); check the national transposition). Many working meters in plant rooms and substations have a wired output but nobody to read it remotely. Replacing a working meter costs a plumber visit plus the meter.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.
- **GdW (DE)** · https://www.gdw.de/ — German federation of housing companies and cooperatives.
- **Aedes (NL)** · https://aedes.nl/ — Dutch federation of housing associations (woningcorporaties).
- **Euroheat & Power** · https://www.euroheat.org/ — European district-heating association.
- **AGFW (DE)** · https://www.agfw.de/ — German district-heating association; metering is one of its working groups.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€99–139 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how housing associations, district-heating operators, metering service companies in NL, DE, DK, PL deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How are the heat and water meters in your buildings read today, what does a reading round cost per flat, and what goes wrong with it?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A small isolated box that reads heat, cooling and water meters with an RS-485/Modbus output in apartment blocks and sends the readings over LoRaWAN — making old meters remotely readable without replacing them. On a scale of one to ten, how likely would you be to buy that at €99–139 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Isolated Heat-Meter Reader (LoRaWAN): would you pay €99–139 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Isolated Heat-Meter Reader (LoRaWAN): A small isolated box that reads heat, cooling and water meters with an RS-485/Modbus output in apartment blocks and sends the readings over LoRaWAN — making old meters remotely readable without replacing them. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €99–139 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Where the gap is:
- **Building-level and plant-room meters** (heat meters on the main heating circuit, district-heating substations, cooling meters in offices, main water meters) that have a Modbus RTU or M-Bus output that nobody reads, or only a display that someone photographs once a year.
- **Apartment meters with a wired bus** in blocks where the bus already runs to a central point.
- Owners who want to **avoid replacing working, calibrated meters** before their re-verification date.

The paying customer is the **metering service company** (they have the deadline problem in their contracts) or the **housing association's technical department**. District-heating operators are the third buyer for substations.

### Market size (estimates)
- Heat/cooling/hot-water meters installed in EU multi-apartment and non-residential buildings: tens of millions of devices; the subset that is building-level/plant-room with a wired output and not yet remote-read is much smaller. Estimate **1–2 M reading points** where a wired-output retrofit makes sense.
- **TAM:** 1.5 M × €119 ≈ **€180 M** + optional data service.
- **SAM:** NL, DE, DK, PL, AT, SE, FI (strong district heating or sub-metering), Modbus-output meters only (see kill question), ~25% → **€45 M**.
- **SOM (3 years):** 2% of SAM → ~7,500 units → **~€900k**. The window is the 2026–2028 compliance wave.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Replace meters with radio-enabled (wM-Bus/OMS/LoRaWAN) meters from the big metering brands | €150–400 per point incl. installation | Throws away working, calibrated meters; plumber needed; downtime |
| Generic RS-485/Modbus-to-LoRaWAN converters (several established IoT brands) | €80–250 | Often non-isolated or with weak isolation; generic register config by hand; no meter library |
| Wired M-Bus-to-LoRaWAN/NB-IoT converters (metering IoT specialists) | €150–400 | Fine for M-Bus, but many plant-room meters are Modbus; price |
| Building-management system (BMS) integration | €1,000s per site | Overkill for meter reading; needs a BMS |
| Manual reading / photos | Labour | Doesn't meet "remotely readable" |

**Wedge:** galvanically isolated by design (5 kVrms transceiver + isolated supply), a **ready register library for the most common Modbus-output heat/cooling/water meters** (pick the meter model in a configurator, done), a published LoRaWAN codec, and a price under the plumber visit.

### Product & value proposition
- **Interface:** HopeRF CMT83085 isolated half-duplex RS-485 transceiver (5 kVrms, CMTI 200 kV/µs, bus ESD ±12 kV, 12 Mbps, up to 256 nodes per HopeRF). Reads up to 8 meters on one bus.
- **Power:** Hi-Link 3 W wide-input isolated DC-DC (e.g. UWB 4.5–36 V input, 1500 VDC isolation per the brochure) from a 12/24 V plant-room supply, or a primary-battery variant for 1–4 meters with hourly polling.
- **Radio:** HopeRF RFM95W (868 MHz) for LoRaWAN Class A; external antenna option (plant rooms are often in basements).
- **Firmware:** a meter register library (energy, volume, flow, supply/return temperatures, error codes), hourly logging with a 30-day local buffer, daily LoRaWAN uplinks (or more often where the network allows), configuration via NFC/BLE or a local USB console, and time-sync for billing-period values.
- **Form factor:** a DIN-rail case, 2–3 modules wide, with screw terminals and a status LED.
- **M-Bus variant (v2):** an M-Bus master front end instead of RS-485, same firmware architecture.

**Pricing (estimates):** €119 per unit (list), €99 at 100+ for metering service companies; optional €1/meter/month hosted data service with EED-style monthly consumption reports. Installation by the customer's technicians (20 minutes).

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (CMT83085, Hi-Link 3 W isolated DC-DC, RFM95W, MCU with flash, NFC/BLE config, TVS/protection, terminals, PCB) | €27.00 | €21.00 |
| Assembly & test (incl. isolation hi-pot test, Modbus loopback, LoRaWAN join) | €4.00 | €2.80 |
| DIN-rail enclosure + antenna | €4.50 | €3.00 |
| Packaging | €0.80 | €0.60 |
| Freight + duty to EU | €1.20 | €0.80 |
| Certification amortised (~€25k: RED 868 MHz, EMC industrial, EN 62368-1, EN 18031 assessment) | €25.00 | €5.00 |
| **Landed cost** | **€62.50** | **€33.20** |
| Net price (direct to metering companies) | €99 | €89 |
| **Gross margin (hardware)** | **€36.50 (37%)** | **€55.80 (63%)** |

### Go-to-market
**First 100 customers (units):**
- **Three metering service companies** (regional heat-cost billing firms, not the giants) with a 2027 compliance backlog: a 30-unit pilot each on buildings where meter replacement is expensive.
- **Housing associations with in-house technical teams** (NL woningcorporaties, DE Wohnungsgenossenschaften, DK almene boliger): through their sector associations' energy working groups.
- **District-heating operators** (municipal utilities) for substations.
- **LoRaWAN network operators** that serve utilities: they want devices that generate traffic and will list you.

**Scale channels:** HVAC/plumbing wholesalers (DIN-rail products sell there), metering integrators and billing-software vendors (codec integration = the listing), and OEM/white-label for meter manufacturers that want a retrofit SKU.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question: meter inventories from 3 housing associations; register maps for the top 10 meter models; works-like on M5Stack RS485-ISO + LoRaWAN |
| Q2 | Custom PCB (isolated RS-485 + isolated DC-DC + LoRa), DIN-rail case; EVT 30 units in plant rooms |
| Q3 | DVT; RED/EMC/safety testing; pilot 300 units with metering companies; codec published on network-server device repositories |
| Q4 | 1,000 units; M-Bus variant EVT (if the inventories say so); wholesaler listing |

**Team:** 1 embedded engineer (Modbus, LoRaWAN, low-level, isolation design), 1 firmware/backend developer (register library, codec, configurator, reports), the founder on B2B sales with a metering or HVAC background.

**Funding to the first 1,000 units (estimates):** NRE €50k (PCB + isolation design €15k, case/tooling €8k, firmware + register library €17k, configurator/reports €10k) + certification €25k + 1,000 units landed ~€38k + 9 months lean costs €60k ≈ **€173k**. Subtract pilot orders (300 × €99 ≈ €30k, part upfront) → **~€140k**. Route: metering-company pre-orders, an energy-efficiency or digitalisation grant, then a strategic angel/investor from metering or HVAC distribution.

### Top risks
| Risk | Mitigation |
|---|---|
| **Market: most installed heat meters may be M-Bus or wireless M-Bus, not Modbus** | The kill question (below) before building: get real meter inventories. If <30% Modbus, build the M-Bus variant first; keep the architecture bus-agnostic |
| **Technical:** register maps differ per meter model and firmware | Start with the top 10 models from the inventories; a register-map file format that integrators can extend; test each model on real hardware |
| **Technical:** basement radio coverage | External antenna kit; private gateway option per building; LoRaWAN coverage check in the pilot |
| **Regulatory:** customers think it makes meters "EED-compliant" automatically | National rules decide what "remotely readable" means and whether retrofit devices count. Get one national body's or a billing firm's written confirmation per country before marketing compliance |
| **Legal metrology:** billing based on transmitted values | The meter stays the legal instrument; the transmitted value must match the display (integrity: counters + CRC + MAC); never compute billing values on the device |
| **Supply:** CMT83085 datasheet marked preliminary; single source | Confirm production status with HopeRF; footprint-compatible isolated RS-485 transceivers from other makers exist (SOIC-16 WB); qualify one |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF CMT83085/CMT83087 isolated RS-485 transceiver | https://www.gongbans.com/db/hoperf-cmt83085-cmt83087.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Isolator/SCH_PCB/CMT83085) | Isolated RS-485 in one chip: 5 kVrms, bus ESD ±12 kV, 256 nodes | schematic, PCB, datasheet (marked preliminary) | MIT (HopeRF repo) |
| Hi-Link WR(A)B/UR(A)B/UWB_S-3WR3 3 W isolated DC-DC | https://www.gongbans.com/db/hilink-s-3wr3-series-wr-ur-uwb.html | Isolated, regulated supply from a 12/24 V plant-room rail (UWB: 4.5–36 V input), 1500 VDC isolation, −40 to +85 °C | **Datasheet public, files via maker** | Commercial module |
| HopeRF RFM95/96/98(W) | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | LoRaWAN uplink radio; footprint, 3D model, CE/FCC reports | PCB footprint, demo code, datasheet | MIT (HopeRF repo) |
| M5Stack Unit RS485-ISO (U094) | https://www.gongbans.com/db/m5stack-unit-rs485-iso.html | Off-the-shelf isolated RS-485 for the works-like pilot | Enclosure/structure only (no main-board electronics) | Buy for prototyping |

### Block diagram
```
[12/24 V plant-room supply or battery] -> [Hi-Link 3 W isolated DC-DC] -> [MCU side 3.3 V]
                                                                             |
[heat/cooling/water meters, Modbus RTU] ==RS-485 A/B== [CMT83085 isolated transceiver] <-> [MCU: register library, logging, flash buffer]
         (isolated bus side, 5 kVrms barrier)                                                  |                 |
                                                                                  [RFM95W 868 MHz] ~~LoRaWAN~~> [network server -> codec -> billing/reporting]
                                                                                  [NFC/BLE or USB config]  [status LED]
```
**Engineering gap:** the isolation, the supply and the radio are solved parts. What's missing: the isolated board layout (creepage/clearance, the barrier under the chip), the Modbus master with per-meter register maps, timekeeping and billing-period snapshots, buffering and LoRaWAN payload compression, the configurator, and per-country "what counts as remotely readable" confirmation.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| CMT83085 | €1.80–2.50 | HopeRF, **datasheet preliminary**: confirm production status |
| Hi-Link UWB_S-3WR3 (or WRB 24 V) | €3.50–4.50 | Commercial module |
| RFM95W-868 | €4.50 | |
| MCU with ≥512 KB flash (STM32L4 class) + external flash for logs | €3.50 | |
| NFC tag (configuration) or BLE module | €1.50 | NFC keeps it radio-simple |
| TVS diodes, PTC fuses, terminals | €2.00 | Surge protection on the bus and the supply |
| PCB (4-layer, isolation slot) | €2.00 | |
| DIN-rail enclosure + SMA antenna | €4.50 | Off-the-shelf DIN cases avoid tooling |

### Firmware/software starting point
- **Modbus:** search "FreeModbus" or "nanoMODBUS" (small C Modbus libraries); the meter manufacturers publish register maps in their Modbus manuals.
- **LoRaWAN:** LoRaMac-node (github.com/Lora-net/LoRaMac-node) or the STM32 LoRaWAN middleware.
- **Network servers:** The Things Stack / ChirpStack; publish your codec in the public LoRaWAN device repository (search "TheThingsNetwork lorawan-devices") so integrators find you.
- **M-Bus variant:** search "libmbus" for the protocol side; the M-Bus master front end is hardware you design.
- **Works-like:** M5Stack Unit RS485-ISO + M5Stack Unit LoRaWAN-EU868 on an ESP32 dev kit, with Arduino Modbus libraries.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** are enough installed heat meters Modbus RS-485 rather than wired M-Bus? Get meter inventories from 3 housing associations or metering companies. If <30% Modbus, pivot the first variant to M-Bus. Works-like reads one real meter |
| 3–5 | Works-like | Top 5 meter models read correctly (values match the meter display); 10 units in plant rooms; uplink success ≥98% with an external antenna; register-map file format defined |
| 6–8 | Looks-like + EVT | Custom isolated PCB + DIN case; 30 EVT units; hi-pot test of the barrier; surge test on bus and supply; configurator v1 |
| 9–10 | DVT + pre-compliance | EMC pre-scan to industrial levels (EN 61000-6-2/-4 style immunity), RED pre-scan (868 MHz), EN 62368-1 review; EN 18031 gap analysis; codec published |
| 11–12 | Pilot batch | 50 paid units with 2 metering companies; 30 days of data matching manual readings to the last digit; written statement from one billing firm that the data is usable |

### Certification checklist (EU)
- **CE under RED:** 868 MHz EN 300 220-1/-2, EMC EN 301 489-1/-3 (plus industrial immunity where the customer asks for it: EN 61000-6-2), safety EN 62368-1 (SELV supply; the isolation barrier is functional, not a safety barrier, unless you certify it as such), exposure EN 62479. Est. **€10–16k**.
- **RED delegated act cybersecurity (EN 18031-1):** a LoRaWAN device reached via a network server is a debated scope; metering data is personal data where it relates to a household (EN 18031-2 likely). Do a gap analysis with a lab (~€5–10k).
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Secure provisioning of LoRaWAN keys, update path, SBOM, vulnerability handling; metering customers will ask for it in tenders.
- **Measuring Instruments Directive (MID) / legal metrology:** not applicable as long as the device only transports the meter's values and doesn't measure. Don't display or compute billing values on the device.
- **EED/national rules:** confirm per country whether retrofit communication modules satisfy "remotely readable" (national transpositions differ, e.g. heating-cost regulations in DE).
- **GDPR:** household consumption data is personal data. The metering company is the controller; you need a DPA if you host data. EU hosting; encryption end to end (LoRaWAN AES + your own app-layer integrity).
- **RoHS, REACH, WEEE** (B2B), packaging registration. **Battery Regulation** for the battery variant.
- **Total certification budget estimate: €20–32k.**

### Validation toolkit
- **Kill question:** Are enough installed heat meters Modbus RS-485 rather than wired M-Bus? Ask 3 housing associations for their meter inventory before building; if <30% Modbus, pivot to M-Bus first.
- **Cheapest experiment (~€0–300):** ask for the inventories (meter make/model/interface per building). It costs phone calls and an NDA. Meanwhile build one works-like reader for the most common meter model and show the live readings.
- **5-question interview (metering company / housing association technical manager):** 1) How many meters in your portfolio aren't remotely readable today, and what interfaces do they have? 2) What's your plan for the 2027 remote-reading requirement, and what does replacement cost per point? 3) Which meter models are most common in plant rooms/substations? 4) What would you need from a retrofit reader (isolation, battery, codec, certificate)? 5) At €99 per reader, how many would you order for the next heating season?
- **Landing page headline:** "Make the meters you already have remotely readable." Bullets: "Reads Modbus heat, cooling and water meters; sends over LoRaWAN." / "Galvanically isolated: no ground-loop failures in plant rooms." / "Ready register library for common meters; 20-minute install on a DIN rail."
- **Pass threshold:** inventories show ≥30% Modbus at the target customers **and** 2 metering companies commit to 30-unit paid pilots.

### First production checklist
- **Samples:** golden sample with isolation hi-pot record and a reference meter read; register library version frozen per batch.
- **DFM review:** creepage/clearance across the isolation barrier (no copper under the CMT83085's isolation gap), terminal block torque, LED visibility on the DIN rail.
- **MOQ talk:** CMT83085 (preliminary datasheet: secure supply), Hi-Link DC-DC modules, DIN-rail cases.
- **QC/AQL:** AQL II 0.65 (isolation) / 1.0 / 2.5; 100% hi-pot across the barrier, 100% Modbus loopback, 100% LoRaWAN join; unique key provisioning logged.
- **Packaging:** small box, antenna, install leaflet with wiring diagram and a QR to the register library/configurator.
- **Incoterms:** FOB Shenzhen; B2B shipments per pilot; keep EU stock for the heating-season rush.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and Hi-Link (海凌科) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver](/db/hoperf-cmt83085-cmt83087.html) (isolated half-duplex RS-485 transceiver (open schematic + PCB)); [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver for the LoRaWAN uplink). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP](/db/hilink-s-3wr3-series-wr-ur-uwb.html) (3 W wide-input isolated DC-DC converter). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit RS485-ISO (U094)](/db/m5stack-unit-rs485-iso.html) (off-the-shelf isolated RS-485 unit for the pilot). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*
- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and Hi-Link (海凌科) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094) — for a Isolated Heat-Meter Reader (LoRaWAN)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Isolated Heat-Meter Reader (LoRaWAN): A small isolated box that reads heat, cooling and water meters with an RS-485/Modbus output in apartment blocks and sends the readings over LoRaWAN — making old meters remotely readable without replacing them. The design is built around your HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094).
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
主题：样品订购及批量报价 — HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094) — 用于Isolated Heat-Meter Reader (LoRaWAN)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Isolated Heat-Meter Reader (LoRaWAN)：A small isolated box that reads heat, cooling and water meters with an RS-485/Modbus output in apartment blocks and sends the readings over LoRaWAN — making old meters remotely readable without replacing them。产品设计基于贵司的HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094)。
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
Subject: PCBA quote from open design files — Isolated Heat-Meter Reader (LoRaWAN), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Isolated Heat-Meter Reader (LoRaWAN): A small isolated box that reads heat, cooling and water meters with an RS-485/Modbus output in apartment blocks and sends the readings over LoRaWAN — making old meters remotely readable without replacing them. The design starts from published open-hardware files (HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Isolated Heat-Meter Reader (LoRaWAN)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Isolated Heat-Meter Reader (LoRaWAN)：A small isolated box that reads heat, cooling and water meters with an RS-485/Modbus output in apartment blocks and sends the readings over LoRaWAN — making old meters remotely readable without replacing them。设计基于已公开的开源硬件文件（HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, Hi-Link WR(A)B_S-3WR3 / UR(A)B_S-3WR3 / UWB_S-3WR3 3 W wide-input isolated regulated DC-DC converter, SIP, M5Stack Unit RS485-ISO (U094)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Call 3 housing associations or metering companies and ask for a meter inventory (make, model, interface) for 10 buildings. This decides Modbus vs M-Bus.
2. Order an M5Stack Unit RS485-ISO, an M5Stack Unit LoRaWAN-EU868 and an ESP32 dev kit, and read one Modbus heat meter's energy register on your bench.
3. Read the national transposition of the EED remote-reading rule in your launch country and write down exactly what "remotely readable" requires.

Want help sourcing or building this? Talk to us via www.gongbans.com.
