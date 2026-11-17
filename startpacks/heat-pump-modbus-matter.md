# Heat-Pump Modbus-to-Matter Bridge — Founder Start Pack

> An isolated plug-in bridge that reads (and, carefully, writes) a heat pump's Modbus registers and exposes it as a Matter thermostat / energy device. The heat pump joins the home's energy automation locally, without the maker's cloud.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of European homes now have a heat pump, solar panels, maybe a battery and a dynamic electricity tariff. The heat pump is the biggest flexible load in the house, but it's usually locked behind the maker's cloud app. Many units expose Modbus RTU on a service terminal, but connecting to it today means a DIY RS-485 dongle, a community register map and a Home Assistant hobby weekend. Non-isolated dongles in plant rooms also die from ground loops and surges.
- **Customer:** Heat-pump owners with a Matter or Home Assistant smart home (the early market); heating installers who want a standard "make it smart" add-on; smaller heat-pump brands without a Matter roadmap (OEM). Owners pay for retrofit; installers resell; brands pay per unit.
- **Product:** A DIN-rail or wall-mount bridge: an isolated RS-485 port (HopeRF CMT83085, 5 kVrms isolation, per HopeRF) with an isolated bus-side supply (Hi-Link B0505S-1WR3 class DC-DC), and a HopeRF HM-MT7201 Matter-over-Wi-Fi module. Per-model register profiles (versioned, community-contributed, vetted), exposed as a Matter thermostat plus device-energy-management features. **Read-only by default**; writes only through a whitelist in vetted profiles.
- **Why now:** Matter 1.3 added energy reporting and device-energy-management features, and Matter 1.4 added energy device types such as heat pumps, so smart-home controllers can finally speak "heat pump" natively. Meanwhile dynamic tariffs and grid rules (e.g. controllable-load schemes in Germany) make it worth shifting heat-pump load.
- **The ask:** About €150–190k (estimate) to the first 1,000 units including Matter certification. Route: crowdfunding/pre-orders in smart-home communities, an installer pilot, then an OEM conversation with a smaller heat-pump brand.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> How many of the top 20 heat-pump models sold in NL/DE expose documented Modbus registers? If fewer than 8, the addressable market is too thin.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Heat-pump owners with Home Assistant/Matter homes, installers, smaller heat-pump brands without a Matter roadmap.

**The problem as the pack states it:** Millions of European homes now have a heat pump, solar panels, maybe a battery and a dynamic electricity tariff. The heat pump is the biggest flexible load in the house, but it's usually locked behind the maker's cloud app. Many units expose Modbus RTU on a service terminal, but connecting to it today means a DIY RS-485 dongle, a community register map and a Home Assistant hobby weekend. Non-isolated dongles in plant rooms also die from ground loops and surges.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/heatpumps** · https://www.reddit.com/r/heatpumps/ — heat-pump owners and installers, EU and US.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **OpenEnergyMonitor community** · https://community.openenergymonitor.org/ — open energy-monitoring builders; heat-pump monitoring is a major topic.
- **HaustechnikDialog (DE)** · https://www.haustechnikdialog.de/ — German heating installers and owners; hydronic balancing, heat pumps, legionella.
- **Photovoltaikforum (DE)** · https://www.photovoltaikforum.com/ — German PV, battery, heat-pump and dynamic-tariff owners.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79–119 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how heat-pump owners with Home Assistant/Matter homes, installers, smaller heat-pump brands without a Matter roadmap deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How does your heat pump talk to the rest of your home automation today, and what have you tried to get local control without the maker's cloud?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] An isolated plug-in bridge that reads and writes a heat pump's Modbus registers and exposes it as a Matter thermostat / energy device — so the heat pump joins the home's energy automation locally, without the maker's cloud. On a scale of one to ten, how likely would you be to buy that at €79–119 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Heat-Pump Modbus-to-Matter Bridge: would you pay €79–119 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Heat-Pump Modbus-to-Matter Bridge: An isolated plug-in bridge that reads and writes a heat pump's Modbus registers and exposes it as a Matter thermostat / energy device — so the heat pump joins the home's energy automation locally, without the maker's cloud. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79–119 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
**Early market:** the energy-nerd homeowner with solar + heat pump + Home Assistant or a Matter controller, who wants the heat pump to run when power is cheap or the sun shines, and who's tired of the cloud app. They exist in large numbers in NL, DE, BE, the Nordics and UK, and they're very vocal in forums. They'll pay €99 for something that works reliably and doesn't need soldering.

**Scale market:** **heating installers** who are asked "can it talk to my solar/battery/app?" on every job, and **smaller heat-pump brands** (often with OEM hardware from Asia) that lack a Matter or app roadmap. For a brand, a certified Matter bridge with their register profile is a ready-made feature.

**Not the customer:** the big heat-pump brands with their own cloud, apps and EEBus/SG-Ready strategies; they may even be hostile to third-party writes.

### Market size (estimates)
- Heat pumps installed in Europe: tens of millions (EHPA-order figures, including air-to-air units); hydronic air-to-water units in the core markets (DE, NL, BE, FR, Nordics, UK, IT): assume **~8 M units**, growing ~1.5–2 M a year.
- Share with a usable Modbus interface (native or via an optional interface card) — **this is the kill question** — assume 40% → **3.2 M**; share of owners with a smart-home controller and motivation: ~10% → **~320k**.
- **TAM:** 320k × €99 ≈ **€32 M**, plus OEM: say 200k new units/yr from smaller brands × €25 ≈ **€5 M/yr**.
- **SAM:** NL, DE, BE, Nordics, UK with English/German/Dutch support: ~60% → **~€19 M**.
- **SOM (3 years):** 3% of SAM ≈ **~6,000 units ≈ €0.6 M** + one OEM deal (~10k units/yr at €25 = €0.25 M/yr).

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| DIY RS-485 dongle + Home Assistant Modbus config or ESPHome (community register maps exist for many brands) | €15–40 + hours | Non-isolated, fragile, hobbyist-only, no Matter, writes unguarded |
| Smart-home relays/controllers with Modbus RTU integrations for specific heat-pump brands (e.g. Shelly's documented local Modbus RTU integration for Midea/Clivet units) | €50–150 | Brand-specific; not a Matter heat-pump device; you configure registers yourself |
| Maker's own gateway/cloud app (Wi-Fi modules, internet gateways, some with Modbus TCP or EEBus) | €100–400 + cloud | Cloud-dependent, closed, often no local API |
| SG-Ready relay control (2 contacts: block/boost) | €20–80 | Crude 4-state control; no data, no setpoints |
| Home energy managers with heat-pump support via EEBus/SG-Ready | €300–1,000 | Expensive; only certain brands |
| Do nothing (heat pump runs on its own curve) | Free | Misses cheap/solar hours |

**Wedge:** **galvanic isolation** (survives plant rooms), **Matter-native** (works with Apple/Google/Amazon/SmartThings/Home Assistant without integrations), **local-only**, **vetted register profiles with a write whitelist** (safety and warranty story installers can accept), and plug-and-play set-up with model auto-detection where possible.

### Product & value proposition
- **Bus side:** CMT83085 isolated half-duplex RS-485 transceiver (12 Mbps, 5 kVrms isolation, CMTI 200 kV/µs, ±12 kV bus ESD, fail-safe, up to 256 nodes, SOIC-16 WB, per HopeRF) + B0505S-1WR3-class isolated 1 W DC-DC (1500 VDC isolation, per Hi-Link) for the bus-side supply, switchable termination and bias resistors.
- **Host:** HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2, 160 MHz MCU, 2 MB flash + external flash, 288 KB RAM, PCB antenna, CE/FCC reports in HopeRF's folder). Check early whether its Matter SDK and flash budget fit your bridge + multiple clusters; the SoC isn't named publicly in the catalogue, so get the SDK from HopeRF before committing. An ESP32-C6 module is the fallback (well-trodden esp-matter path, also Thread-capable).
- **Matter model:** thermostat (setpoint, mode, current temperature), plus energy features as supported by the controllers you target (device-energy-management for load shifting, electrical-energy measurement if the heat pump reports power). Domestic hot water as a separate endpoint if supported by your Matter version and controllers.
- **Profiles:** JSON register maps per model/firmware: read set (temperatures, mode, compressor state, power), write whitelist (setpoint within safe range, mode, DHW boost), rate limits (no write storms to EEPROM-backed registers). Community-contributed, vetted and signed by you before they're enabled for writing.
- **Safety by design:** read-only by default; writes require a vetted profile + explicit user confirmation; never touch legionella cycles, compressor protection or installer-level parameters.

**Pricing (estimates):** €99 RRP (€79 early bird); installer price €69; OEM €20–30 at 5k+/yr (white-label, brand's profile preloaded).

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (HM-MT7201 or ESP32-C6 module, CMT83085, B0505S, termination/bias, TVS, terminal block, 12–24 V input PSU, PCB, LEDs, button) | €19.00 | €15.00 |
| Assembly & test (isolation hi-pot, RS-485 loopback, Matter DAC provisioning) | €2.50 | €1.80 |
| Enclosure (DIN-rail case) | €1.80 | €1.20 |
| Packaging (Matter QR label) | €1.00 | €0.70 |
| Freight + duty to EU | €0.80 | €0.50 |
| Certification amortised (~€40k: RED, EMC, safety, EN 18031-1/-2, Matter certification + CSA membership share) | €40.00 | €8.00 |
| Matter device attestation certificate (estimate) | €0.20 | €0.10 |
| **Landed cost** | **€65.30** | **€27.30** |
| Net price ex-VAT: direct €83 (from €99) / installer €58 | €83 / €58 | €83 / €58 |
| **Gross margin** | **€18 (21%) direct / −€7 (loss) installer** | **€56 (67%) / €31 (53%)** |

Same pattern as every small Matter product: certification dominates at 1k. Options: (a) sell the first 1,000 direct only; (b) launch v1 as a Home Assistant/ESPHome-native bridge (certification ~€15k) and certify Matter at volume; (c) let an OEM partner co-fund Matter certification. Pick deliberately; don't sell through installers at 1k.

### Go-to-market
**First 100 customers:**
- **Home Assistant and energy-optimisation communities** (forums, Discord/Reddit-type groups, NL/DE tweakers and solar forums). The register-profile repo itself is marketing: every contributed profile brings that brand's owners.
- **Heat-pump owner groups** per brand (Facebook groups and forums exist for most popular brands).
- **Crowdfunding** in DE/NL as the kill test.
- **Energy/tariff app makers** (dynamic-tariff suppliers, home-energy-management apps) as partners: they need a heat-pump control path.

**Scale channels:** heating installers and wholesalers, dynamic-tariff energy suppliers (bundle), smaller heat-pump brands (OEM), smart-home retailers.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question: register documentation audit of the top 20 heat-pump models sold in NL/DE; 5 owners with test units (read-only) on different brands; Matter SDK check on HM-MT7201 vs ESP32-C6 |
| Q2 | Custom isolated PCB; profile format + 8 vetted profiles; Matter thermostat endpoint working with 3 controllers; crowdfunding launch |
| Q3 | DVT; RED/EMC/safety/EN 18031; Matter certification (or path b); ship backers; installer pilot (20 units) |
| Q4 | 1,000 units; 15+ profiles; OEM talks with 2 smaller heat-pump brands; tariff-app partnership |

**Team:** 1 firmware engineer with Matter experience (essential), 1 embedded/hardware engineer part-time (isolation, EMC), 1 community/profile maintainer (could be the founder), part-time heating-installer adviser (safe registers, warranty language).

**Funding to the first 1,000 units (estimates):** NRE €65k (hardware + isolation design €12k, Matter firmware €35k, profile tooling + vetting €10k, enclosure/labels €3k, test rigs €5k) + certification €40k (or ~€15k path b) + 1,000 units landed ex-cert ~€25k + 9 months lean costs €45k ≈ **€175k** (path b: ~€150k); minus crowdfunding (~700 × €79 ≈ €55k gross) → **~€100–120k** to raise. Route: crowdfunding + an angel from the energy-transition scene; energy-transition innovation grants; OEM co-funding of Matter certification.

### Top risks
| Risk | Mitigation |
|---|---|
| **Market: too few models expose documented Modbus registers** | Kill question first: audit the top 20 models; target brands with vendor-published maps; community maps only for read |
| **Safety/warranty: writes harm the heat pump or void warranty** | Read-only default; vetted write whitelist; rate limiting; no installer/protection parameters; clear disclaimer; installer adviser on every profile |
| **Technical: Matter heat-pump support varies by controller and version** | Start with the thermostat device type (broadest support); add energy features as controllers support them; test with 4 ecosystems monthly |
| **Technical: HM-MT7201 Matter SDK maturity / flash budget** | Decide in Q1; ESP32-C6 fallback footprint |
| **Electrical: ground loops, surges, wrong wiring in plant rooms** | 5 kV isolation, TVS, reverse-polarity protection, installer wiring guide, termination switch |
| **Cost: Matter certification at low volume** | Path (b) or OEM co-funding |
| **Security: a bridge that can write to the heating** | EN 18031 design, Matter's attestation and secure sessions, signed OTA, writes disabled until the user enables them locally |
| **Supply: CMT83085 single source; datasheet marked preliminary** | Footprint-compatible alternative isolated RS-485 transceivers exist from other makers; qualify one in DVT |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF CMT83085 / CMT83087 isolated RS-485 transceiver | https://www.gongbans.com/db/hoperf-cmt83085-cmt83087.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Isolator/SCH_PCB/CMT83085) | Isolated half-duplex RS-485: 5 kVrms, CMTI 200 kV/µs, ±12 kV bus ESD, 12 Mbps, fail-safe | Schematic, PCB layout, datasheet (marked preliminary) | MIT (HopeRF repo) |
| HopeRF HM-MT7201 Matter-over-Wi-Fi module | https://www.gongbans.com/db/hoperf-hm-mt7201.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT7201) | Matter over Wi-Fi + BLE 5.2 commissioning; 160 MHz MCU, 2 MB flash (ext. up to 16 MB), UART/SPI/I²C; CE/FCC reports in folder | PCB footprint, datasheet, photos, certification reports | MIT (HopeRF repo); Matter SDK from HopeRF (check its licence) |
| Hi-Link B_S series (B0505S-1WR3 etc.) isolated DC-DC | https://www.gongbans.com/db/hilink-b-s-1wr3-series.html | Bus-side isolated supply: 1 W, 1500 VDC isolation, SIP, short-circuit protection | Datasheet public; files via maker (contact Hi-Link) | Commercial module, no open design files |
| M5Stack Station-485 (K123) | https://www.gongbans.com/db/m5stack-station-485.html | Ready-made RS-485 station for register-mapping work on real heat pumps before your PCB exists | Enclosure/structure files only (main-board electronics not published) | Dev tool only |

### Block diagram
```
[heat pump Modbus RTU terminal A/B/GND]
        |  (switchable 120 Ω termination + bias, TVS)
[CMT83085 isolated RS-485]  <== 5 kVrms barrier ==>  logic side
        ^ bus-side 5 V from [B0505S isolated DC-DC]          |
                                                             | UART
                                      [HM-MT7201 Matter-over-Wi-Fi  (fallback: ESP32-C6)]
                                        |-- profile engine: read map, write whitelist, rate limits
                                        |-- Matter endpoints: thermostat (+ energy features, + DHW)
                                        `~~ Wi-Fi ~~> [Matter controllers: Apple/Google/Amazon/SmartThings/Home Assistant]
[12–24 V DC or 230 V → PSU] -> 3.3 V logic
```
**Engineering gap:** the profile engine (data types, scaling, function codes, polling plans, write whitelist, rate limits), mapping heat-pump concepts onto Matter clusters in a way controllers display sensibly, model detection, robust RS-485 behaviour (timeouts, bus errors, multiple masters if the maker's own gateway is also on the bus), Matter commissioning + DAC provisioning, and the profile vetting process.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HM-MT7201 module (or ESP32-C6 module, 4–8 MB flash) | €2.50–3.50 | Matter needs flash headroom |
| CMT83085 isolated RS-485 | €1.80 | Sole source; preliminary datasheet: get final rev |
| B0505S-1WR3 isolated DC-DC | €1.00 | |
| TVS, termination/bias switches, terminal block | €1.50 | |
| Input PSU (12–24 V DC from the heat pump's aux supply, or 230 V module) | €2–4 | Decide per target brands |
| PCB 4-layer, LEDs, button, passives | €2.00 | Isolation slot in PCB |
| External SPI flash (if HM-MT7201) | €0.50 | |
| DIN-rail enclosure | €1.80 | Stock part |

### Firmware/software starting point
- **Matter:** Espressif esp-matter (github.com/espressif/esp-matter) if you go ESP32-C6; the connectedhomeip project (github.com/project-chip/connectedhomeip) is the Matter reference SDK; HopeRF's SDK for the HM-MT7201 (ask HopeRF; not in the public folder as far as the catalogue shows).
- **Modbus:** esp-modbus (Espressif) or any small Modbus RTU master library.
- **Register maps (read references only; check licences):** community Home Assistant Modbus configs and ESPHome projects for specific brands (search "<brand> heat pump modbus home assistant"); vendor-published Modbus documents where they exist (some manufacturers publish them; others are community reverse-engineered).
- **Profile repo:** a public Git repo with a JSON schema + CI validation; contributions read-only until vetted.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** audit the top 20 heat-pump models sold in NL/DE: documented Modbus registers (vendor or reliable community map), interface needed (on-board vs extra card, cost). Pass: ≥8 of 20 with documented maps and no expensive interface card |
| 3–5 | Works-like | M5Stack Station-485 + ESP32-C6 devkit reading 3 real heat pumps (owners' homes, read-only); Matter thermostat endpoint visible in 3 controllers with live temperatures |
| 6–8 | Looks-like + EVT | Custom isolated PCB in DIN-rail case; 20 EVT units with owners across ≥5 brands; zero bus faults over 2 weeks; first vetted write profile (setpoint/mode) on 2 brands |
| 9–10 | DVT + pre-compliance | Hi-pot isolation test, EMC pre-scan (incl. surge on RS-485 lines), RED pre-scan, EN 18031 gap analysis; Matter pre-certification test run (or path b decision) |
| 11–12 | Pilot batch | 50 units sold; 8+ profiles; support tickets/unit <0.3; one installer orders 20; OEM intro meeting held |

### Certification checklist (EU)
- **CE under RED:** 2.4 GHz Wi-Fi/BLE (EN 300 328; reuse the module's reports), EMC (EN 301 489-1/-17 + immunity incl. surge/burst on the RS-485 port), safety EN 62368-1 (isolation barrier: verify creepage/clearance and hi-pot; if powered from 230 V, the PSU safety design matters), RF exposure. Est. **€8–12k**.
- **RED delegated act cybersecurity EN 18031-1 and -2** (internet-connected via the home network; processes home occupancy-related heating data). Est. **€8–12k**.
- **Matter certification** (CSA membership + authorised test lab + product certification) to use the Matter logo/claims. Budget **€15–30k** in year one (check current CSA fees). Path (b) skips this initially.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: signed OTA, SBOM, vulnerability handling, support period (heat pumps last 15–20 years; say how long you'll support the bridge).
- **RoHS, REACH, WEEE, packaging registration.**
- **GDPR:** local-only design keeps you mostly out; heating patterns reveal occupancy, so any cloud feature later is personal data.
- **Heat pump side:** you don't change the heat pump's conformity, but writes could affect its operation and warranty: vetted whitelist, documentation, installer sign-off for write mode.
- **Total estimate: €16–24k without Matter certification; €31–54k with.**

### Validation toolkit
- **Kill question:** How many of the top 20 heat-pump models sold in NL/DE expose documented Modbus registers? If fewer than 8, the addressable market is too thin.
- **Cheapest experiment (~€0–100):** a desk audit (manuals, installer docs, community threads) of the top 20 models, plus a €40 RS-485 dongle read test on 3 friends' heat pumps.
- **5-question interview (owner):**
  1. Which heat pump do you have, and how do you control it today (app, panel, installer)?
  2. What do you want it to do that it doesn't: solar surplus, cheap hours, one app for everything?
  3. Have you tried Modbus/Home Assistant yourself? Where did you give up?
  4. Would you let a bridge *write* settings to your heat pump, or only read? What would make you trust it?
  5. €99 for a certified, isolated, plug-in bridge: buy now?
- **Interview (installer):** how often customers ask for smart integration; which brands; whether a third-party bridge affects warranty; what you'd charge to fit it.
- **Landing-page headline:** "Your heat pump in Matter. Local, isolated, no cloud."
  - Reads your heat pump over Modbus and shows it in Apple Home, Google, Alexa, SmartThings and Home Assistant.
  - Run it on solar and cheap hours. Read-only until you say otherwise.
  - Industrial-grade isolation for the plant room.
- **Pass threshold:** ≥8 of 20 models documented **and** 500 crowdfunding backers (or 300 €20 deposits) in 6 weeks, with ≥5 brands represented.

### First production checklist
- **Samples:** isolation hi-pot on 100% of EVT units, RS-485 communication test with a reference Modbus slave, Matter commissioning test with 2 controllers.
- **Golden sample:** unit with recorded isolation test, Modbus loopback, Matter DAC chain verified, firmware version.
- **DFM review:** PCB isolation slot and creepage, terminal block labelling (A/B/GND), termination switch accessibility, DIN-rail clip, LED status meanings.
- **MOQ talk:** CMT83085 (final datasheet revision, reel MOQ), Wi-Fi module, isolated DC-DC, DIN-rail enclosures (stock).
- **QC/AQL:** AQL II 0.65 for isolation (100% hi-pot anyway), 1.0/2.5 otherwise; 100% Modbus loopback, 100% Wi-Fi/Matter onboarding QR check against provisioned DAC.
- **Packaging:** bridge, wiring guide per supported brand (QR to profile page), Matter QR on device + manual, "read-only by default" card.
- **Incoterms:** FCA Shenzhen; air for the crowdfunding batch.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and Hi-Link (海凌科) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver](/db/hoperf-cmt83085-cmt83087.html) (isolated RS-485 transceiver (open schematic + PCB)); [HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2)](/db/hoperf-hm-mt7201.html) (Matter-over-Wi-Fi module). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP](/db/hilink-b-s-1wr3-series.html) (1 W isolated DC-DC for the bus side). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Station-485 (K123)](/db/m5stack-station-485.html) (RS-485 station for early register-mapping work). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and Hi-Link (海凌科) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123) — for a Heat-Pump Modbus-to-Matter Bridge

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Heat-Pump Modbus-to-Matter Bridge: An isolated plug-in bridge that reads and writes a heat pump's Modbus registers and exposes it as a Matter thermostat / energy device — so the heat pump joins the home's energy automation locally, without the maker's cloud. The design is built around your HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123).

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123).
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
主题：样品订购及批量报价 — HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123) — 用于Heat-Pump Modbus-to-Matter Bridge

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Heat-Pump Modbus-to-Matter Bridge：An isolated plug-in bridge that reads and writes a heat pump's Modbus registers and exposes it as a Matter thermostat / energy device — so the heat pump joins the home's energy automation locally, without the maker's cloud。产品设计基于贵司的HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123)。
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
Subject: PCBA quote from open design files — Heat-Pump Modbus-to-Matter Bridge, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Heat-Pump Modbus-to-Matter Bridge: An isolated plug-in bridge that reads and writes a heat pump's Modbus registers and exposes it as a Matter thermostat / energy device — so the heat pump joins the home's energy automation locally, without the maker's cloud. The design starts from published open-hardware files (HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Heat-Pump Modbus-to-Matter Bridge，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Heat-Pump Modbus-to-Matter Bridge：An isolated plug-in bridge that reads and writes a heat pump's Modbus registers and exposes it as a Matter thermostat / energy device — so the heat pump joins the home's energy automation locally, without the maker's cloud。设计基于已公开的开源硬件文件（HopeRF CMT83085 / CMT83087 isolated half-duplex RS-485 transceiver, HopeRF HM-MT7201 Matter-over-Wi-Fi module (Wi-Fi 4 + BLE 5.2), Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, M5Stack Station-485 (K123)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Do the top-20 heat-pump model audit (NL/DE sales rankings × published Modbus documentation) in a spreadsheet; that answers the kill question in 2–3 days.
2. Order an M5Stack Station-485 (or any isolated RS-485 adapter) and an ESP32-C6 devkit; read 10 registers from one real heat pump.
3. Ask HopeRF for the HM-MT7201 Matter SDK, its flash/RAM budget for a bridge with 2–3 endpoints, and the final CMT83085 datasheet revision.

Want help sourcing or building this? Talk to us via www.gongbans.com.
