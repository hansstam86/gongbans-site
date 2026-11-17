# Thread Switch Insert — Founder Start Pack

> A relay insert that sits behind the existing European wall switch in a 60 mm flush box and turns any dumb light into a Matter-over-Thread light. Keep the switch you like, gain automations.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

**Blunt warning up front:** this is mains equipment in a closed box behind a wall. Thermal and safety testing (EN 60669-2-1) is the real project, not the radio. And the market is no longer empty: big European switch brands and established insert makers are launching Matter-over-Thread inserts in 2026. Read the competition section before you spend a euro.

## 1. Summary

- **Problem:** People want automations (lights off when everyone leaves, presence scenes, timers) but don't want to rip out the switch range they chose, or put a plastic "smart switch" faceplate in a listed or designer interior. Most flush-box inserts sold in Europe are still Wi-Fi with a vendor cloud: they're slow to reconnect, clog the router and die when the vendor's cloud changes.
- **Customer:** Electricians and small installers doing whole-house retrofits in DE/AT/NL/BE/Nordics; homeowners with premium switch ranges; **switch-range and lighting brands that want a white-label Matter insert** without building a radio team.
- **Product:** A small insert (fits a 60 mm round flush box behind the switch, needs neutral): latching relay, zero-cross switching, sensing for the existing switch (toggle or momentary), optional power metering, Matter-over-Thread with router role. Local control, no account needed.
- **Why now:** Thread border routers now ship inside many smart speakers, TVs and hubs, so Thread is "already there" in many homes. Matter makes one insert work with all major ecosystems. EFR32MG24-class modules with open reference designs are off the shelf.
- **The ask:** About €250–350k (estimate) to the first 1,000 certified units. Electrical-safety certification and Matter certification are fixed costs you pay before you sell anything. The best route is a **white-label/ODM deal with a European switch or lighting brand** that co-funds certification.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Can the insert stay below its temperature limit in a sealed 60 mm box at 10 A for 8 hours? If thermal tests fail at a sane size, kill it before tooling.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Renters and owners who don't want 'smart switch' faceplates; electricians doing whole-house retrofits; switch-range brands wanting a Matter insert.

**The problem as the pack states it:** People want automations (lights off when everyone leaves, presence scenes, timers) but don't want to rip out the switch range they chose, or put a plastic "smart switch" faceplate in a listed or designer interior. Most flush-box inserts sold in Europe are still Wi-Fi with a vendor cloud: they're slow to reconnect, clog the router and die when the vendor's cloud changes.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **r/electricians** · https://www.reddit.com/r/electricians/ — working electricians.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.
- **r/HomeKit** · https://www.reddit.com/r/HomeKit/ — Apple Home users; Matter and Thread devices are a main topic.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€35–49 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how renters and owners who don't want 'smart switch' faceplates deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last light you wanted to automate: why did or didn't you replace the switch, and what put you off the smart switches you looked at?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A relay insert that fits behind the existing European wall switch in a 60 mm flush box and turns any dumb light into a Matter-over-Thread light — keep the switch you like, gain automations. On a scale of one to ten, how likely would you be to buy that at €35–49 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Thread Switch Insert: would you pay €35–49 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Thread Switch Insert: A relay insert that fits behind the existing European wall switch in a 60 mm flush box and turns any dumb light into a Matter-over-Thread light — keep the switch you like, gain automations. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €35–49 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Lead with **B2B**: a mid-sized European switch-range or lighting brand that has no Matter insert yet, or an installer wholesaler that wants a private-label product. They pay; installers fit it; homeowners use it. Selling to consumers directly means fighting established brands on Amazon with a mains product that, in many countries, must be installed by an electrician.

Secondary: **installer-direct** (electrical wholesale, installer communities). Installers care about: fits the box, terminals that are easy to wire, no app needed to commission (Matter QR code), doesn't come back as a warranty case.

### Market size (estimates)
- EU households: ~200 M; assume 5–8% will have at least one smart relay insert in 5 years, ~5 inserts each → **50–80 M units over 5 years** → **TAM ~€2 B** at €35 average (all protocols).
- **SAM:** Matter-over-Thread inserts in DACH/Benelux/Nordics, assume 15% of that → **~€300 M** over 5 years.
- **SOM:** a niche white-label player: 30–60k units/year by year 3 → **€1–2 M/year**. Realistic only with 1–2 brand customers.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Wi-Fi relay inserts (Shelly-class and countless Tuya-based ones) | €15–30 | Wi-Fi + vendor cloud/app; router load; no mesh. But: cheap and installers know them |
| New Matter-over-Thread inserts from European switch/installation brands (e.g. [WAGO, Hager announced 2026 products](https://matter-smarthome.de/en/products/new-switch-series-from-hager-featuring-matter/), Warema Xeenos Go certified in 2026) | €50–90 | Brand-locked ranges, premium price, sold through their channels |
| Existing Thread relay modules (e.g. [Sunricher SR-MT9041A-R listing](https://www.domadoo.fr/en/smart-home-products/8792-sunricher-module-relais-onoff-matter-thread-230v-sr-mt9041a-r.html?ae=2&aev=shopify), rated around 4.3 A resistive) | €30–45 | Low current ratings; generic |
| Zigbee inserts + hub | €20–40 + hub | Needs a hub; not Matter-native |
| Smart bulbs | €10–25/bulb | Wall switch kills the power; useless with existing fittings |
| Do nothing | Free | — |

**Wedge (be honest, it's narrow):** a **white-label, high-current (10 A) Matter-over-Thread insert** for brands that don't have one — delivered with the safety and Matter certification files, so the brand can put its name on it in months. Not "a better Shelly" for consumers.

### Product & value proposition
- **Radio + MCU:** HopeRF HM-MT2401C (EFR32MG24, Matter over Thread / OpenThread / Zigbee / BLE 5.3, 1,536 KB flash, 256 KB RAM, IPEX antenna connector). The IPEX version lets you route a small antenna to the side of the insert that faces the front, away from the metal box/screws. The HM-MT2401 EVB kit gives a reference schematic.
- **Power:** isolated AC-DC (Hi-Link HLK-10LSxx is listed in the catalogue: 26.4 × 17.5 × 10 mm, 3000 VAC isolation). Honest note: 10 W is far more than you need (a latching relay + MG24 needs well under 1 W). Use it for the prototype; for production pick or design a smaller ~1–2 W supply to cut heat and space.
- **Switching:** latching relay (no coil current while on → less heat), zero-cross switching to protect contacts on LED loads, inrush handling.
- **Inputs:** sense the existing switch (toggle or push-button), configurable.
- **Options:** power metering (shunt or Hall), 2-channel version, dimmer version later (much harder: trailing-edge dimming in a closed box).
- **Tuya variant (only if a brand asks):** Tuya's TS24-U (same MG24 chip in Tuya's 20 × 16 mm footprint) lets a brand use Tuya's white-label app and cloud tools. **This adds a Tuya cloud dependency** for the app features (remote access, branding, OTA through Tuya); Matter local control can still work without it. The **Tuya-free default** is the HopeRF module with your own Silicon Labs Matter firmware: no third-party cloud at all, commissioning through any Matter controller. If a brand chooses Tuya: disclose the cloud dependency, sign a DPA, and check where data is processed (see risks).

**Pricing (estimates):** white-label to brands €14–18 per unit at 5k+ (brand retails at €39–59). Own-brand installer version €39 RRP.

### Unit economics (estimates per unit, ex-VAT; own-brand installer channel)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (MG24 module, AC-DC supply, latching relay 10 A, zero-cross, input sensing, fuse/varistor, terminals, PCB) | €9.50 | €7.50 |
| Assembly & test (incl. hi-pot and relay test) | €1.80 | €1.20 |
| Enclosure (flame-retardant V-0 PC, terminal block) | €1.20 | €0.80 |
| Packaging | €0.60 | €0.40 |
| Freight + duty to EU | €0.50 | €0.35 |
| Matter certification + DCL/attestation, amortised (~€20k incl. lab + membership share) | €20.00 | €4.00 |
| Safety/EMC/RED certification amortised (~€35k) | €35.00 | €7.00 |
| **Landed cost** | **€68.60** | **€21.25** |
| Net revenue (wholesale to installer channel ~€22; white-label ~€16) | €22 | €16 |
| **Gross margin** | **−€46.60 (loss)** | **−€5.25 (loss) own channel; needs 10k+ or brand-paid certification** |

**Read this table carefully:** at these volumes the fixed certification costs kill the unit economics. Two ways out: (1) a brand pays certification/NRE up front (typical in ODM deals), or (2) volume ≥15–20k units. Without either, don't start. (Matter certification also needs Connectivity Standards Alliance membership — check current fees, they're the biggest fixed item for a small company.)

### Go-to-market
**First 100 customers (B2B logic: "100 customers" = 1–2 brands + ~50 installers):**
- **Make a target list of 30 European switch-range, lighting and installation-product brands** without a Matter-over-Thread insert. Approach their product managers with a working sample and a certification plan.
- **Electrical trade fairs** (light + building, installation-technology fairs) — meet brand product managers there.
- **Installer communities** (electrician forums, smart-home installer associations, KNX/Matter installer groups) for the own-brand pilot of 50 installers.

**Scale:** brand ODM contracts; electrical wholesale listing.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | **Thermal kill test** (10 A, 8 h, sealed 60 mm box); talk to 10 brands; LOI from one |
| Q2 | EVT 30 units; Matter firmware on Silicon Labs SDK; pre-scan EMC; safety pre-assessment at a lab |
| Q3 | DVT; full EN 60669-2-1 + EMC + RED; Matter certification |
| Q4 | 1,000–5,000 units for the brand partner; installer pilot |

**Team:** 1 power-electronics/mains engineer (critical — someone who has done EN 60669/60730 products before), 1 embedded engineer (Silicon Labs Matter SDK), a project lead/founder with brand-sales experience. Use a certification consultant.

**Funding to the first 1,000 certified units (estimates):** NRE €100k (hardware €40k, Matter firmware €40k, tooling €20k) + safety/EMC/RED €35k + Matter/CSA €20k+ + 1,000 units landed ~€15k + 9 months team €90k ≈ **€260k+**. With a brand partner paying €80–120k NRE/certification, the gap drops to ~€150k. Route: **ODM/NRE deal first**, then an angel. Don't crowdfund a mains insert.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: heat** in a sealed 60 mm box at 10 A for hours (relay contact + supply losses) | Latching relay, tiny supply, copper pours; thermal kill test before tooling |
| **Technical:** RF through a metal box / near metal screws | IPEX antenna placed on the front side; test in metal and plastic boxes |
| **Regulatory:** EN 60669-2-1 + EMC + RED + Matter = high fixed cost | Brand pays NRE; reuse the module's RED report; one design, many brands |
| **Market:** big brands entering in 2026 | Go white-label for second-tier brands; speed and certification package are the product |
| **Installation:** many countries require an electrician; neutral needed | Market to installers; publish wiring diagrams; no-neutral version is a different (harder) product |
| **Tuya variant:** cloud dependency, GDPR/data residency (where Tuya processes EU users' data, which entity is the processor), app lock-in for the brand | Default to the Tuya-free Matter build; if Tuya, DPA + data-location check + disclose on the box; Matter local control must work without the cloud |
| **Supply:** single module source | MG24 is available from several module makers; keep the footprint flexible |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF HM-MT2401C (IPEX) | https://www.gongbans.com/db/hoperf-hm-mt2401c.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401C) | Matter-over-Thread radio + MCU (EFR32MG24) with IPEX antenna | PCB layout, datasheet | MIT (HopeRF GitHub repo) |
| HopeRF HM-MT2401 EVB kit | https://www.gongbans.com/db/hoperf-hm-mt2401-evb-kit.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401%20EVB%20Kit) | Reference schematic for the module, development board | Schematic | MIT (HopeRF GitHub repo) |
| Hi-Link HLK-10LSxx 10 W ultra-small AC-DC | https://www.gongbans.com/db/hilink-10lsxx.html | Isolated mains supply for the prototype (oversized for production) | **Datasheet public, files via maker** | Commercial module; check its safety approvals for your use |
| Tuya TS24-U Thread module (optional variant) | https://www.gongbans.com/db/tuya-ts24-u.html | Same MG24 chip in Tuya's footprint, for brands that want Tuya's app tools | **Datasheet public, files via maker** | Tuya platform terms + cloud dependency apply |

### Block diagram
```
 L ──┬─[fuse]─[varistor]─[isolated AC-DC]──> 3.3 V ──> [HM-MT2401C MG24] ~~Thread~~> [border router] -> Matter controllers
     │                                                      |  ^
     └──[latching relay 10 A]──> L-out (lamp)   <-- drive --+  |-- [zero-cross detect]
 N ──────────────────────────────────────────────────────────  |-- [switch input sense (isolated/safe)]
                                                               |-- [current sense (optional metering)]
                                  [IPEX antenna on the front side of the insert]
```
**Engineering gap:** the mains design (creepage/clearance, isolation, thermal, relay drive, zero-cross timing, surge), the switch-input sensing circuit, and Matter firmware (On/Off Light, optional Electrical Measurement clusters) on the Silicon Labs SDK. The radio is the easy part.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HM-MT2401C | €3.50–4.50 | MG24 modules from several makers; ask HopeRF for the volume price |
| AC-DC supply (prototype HLK-10LSxx; production ~1–2 W) | €1.50–2.50 | Size for heat, not for headroom |
| Latching relay 10–16 A | €1.50 | Pick one with a high inrush rating (LED drivers) |
| Zero-cross + input sensing + MOSFET drivers | €0.60 | |
| Fuse, varistor, terminals | €0.90 | Terminals: installers judge you on these |
| PCB (FR-4, thick copper) | €0.60 | |
| V-0 enclosure | €1.20 | Tooling ~€8–12k |

### Firmware/software starting point
- **Silicon Labs Simplicity SDK / Gecko SDK** with the Matter extension (Silicon Labs' Matter GitHub repos; search "SiliconLabs matter").
- **Project CHIP / connectedhomeip** (github.com/project-chip/connectedhomeip) — the open-source Matter SDK.
- **OpenThread** (github.com/openthread/openthread).
- HopeRF's GitHub folder for the module's datasheet and layout; Matter example apps start from Silicon Labs' "lighting-app" sample.
- **Tuya variant:** Tuya's developer platform docs for the TS24 series (requires a Tuya developer account).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Thermal kill test:** breadboard relay + supply in a sealed 60 mm box, 10 A resistive for 8 h; terminal temperature rise within the limits you'll test to (check EN 60669-2-1 values with your lab). Plus: 5 brand calls, 1 LOI or paid feasibility |
| 3–5 | Works-like | EVB + relay board; commissions into 2 Matter ecosystems via QR code; switch input works (toggle and push); recovers state after power loss |
| 6–8 | Looks-like + EVT | Insert-size PCB in V-0 housing; 30 units; RF range test in metal and plastic boxes; thermal re-test |
| 9–10 | DVT + pre-compliance | Safety pre-assessment (creepage, glow-wire, temperature rise, endurance cycles), EMC pre-scan incl. surge/burst, Matter test-harness pass |
| 11–12 | Pilot batch | 50 units installed by 10 electricians; 0 safety incidents; commissioning <3 min average |

### Certification checklist (EU)
- **LVD / safety:** EN 60669-1 + **EN 60669-2-1** (electronic switches) — temperature rise, endurance, glow-wire, creepage/clearance. Biggest cost and schedule item. Est. **€15–25k**.
- **EMC:** EN 55014-1/-2 or EN 55015 as applicable, EN 61000-3-2/-3-3, surge/burst immunity. Est. **€5–8k**.
- **RED:** EN 300 328 (2.4 GHz), EN 301 489-1/-17, EN 62311 — reuse module reports where accepted. Est. **€5–8k**.
- **RED delegated act / EN 18031-1:** applies (internet-connected via border router). Self-assessment ~€3–6k.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Matter's built-in device attestation + OTA help, but you still need SBOM, vulnerability handling and a support period statement.
- **Matter certification** (CSA membership + authorised test lab + device attestation certificates). Check current fees.
- **RoHS, REACH, WEEE**, packaging registration.
- **GDPR:** low for local Matter control. **Tuya variant:** cloud processing of usage data — DPA, data-location check, privacy notice.
- National installation rules: in several EU countries only electricians may install fixed-wiring devices — say so in the IFU.
- **Total estimate: €40–60k + Matter/CSA costs.**

### Validation toolkit
- **Kill question:** Can the insert stay below its temperature limit in a sealed 60 mm box at 10 A for 8 hours? If not at a sane size, kill it before tooling. Commercial kill question: will one brand sign an NRE/LOI?
- **Cheapest experiment (~€300 + time):** relay, supply and MG24 dev board in a sealed flush box with thermocouples and a 2.3 kW resistive load; log 8 hours.
- **5-question interview (brand product manager):** 1) Do you have a Matter-over-Thread insert on your roadmap? When? 2) What stops you building it in-house? 3) Which certifications do you require from a supplier? 4) What volume would your first order be, and what price per unit? 5) Would you co-fund certification for exclusivity in your region?
- **Landing page headline (installer version):** "Keep the switch. Add Matter." Bullets: "Fits behind any European switch in a 60 mm box (neutral required)." / "Matter over Thread: works with all major smart-home apps, no account needed." / "Latching relay, 10 A, zero-cross switching for LED loads."
- **Pass threshold:** one signed brand LOI or paid feasibility study (≥€10k), or 50 installers pre-ordering 10 units each.

### First production checklist
- **Samples:** 3 relay suppliers tested for inrush/endurance; supply module samples temperature-mapped.
- **Golden sample:** the exact unit that passed the safety test — freeze BOM; any relay or supply change = re-test.
- **DFM review:** creepage/clearance on the PCB, slots, conformal coating decision, terminal torque, potting (no — heat).
- **MOQ talk:** relay MOQ, module MOQ, V-0 resin colour.
- **QC/AQL:** AQL II 0.65 for safety-critical; 100% hi-pot test, 100% relay function, 100% Matter commissioning test with unique attestation certificates and QR labels.
- **Packaging:** wiring diagram, Matter QR code on device and box, installer leaflet in the main EU languages.
- **Incoterms:** FOB Shenzhen; check that safety-critical parts are sourced exactly as tested (no silent substitutions — write it in the contract).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and Hi-Link (海凌科) and Tuya Smart (涂鸦智能)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector)](/db/hoperf-hm-mt2401c.html) (Matter-over-Thread module (IPEX version, antenna routed out of the metal-free side)); [HopeRF HM-MT2401 Matter-over-Thread EVB kit](/db/hoperf-hm-mt2401-evb-kit.html) (Thread module reference schematic). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS)](/db/hilink-10lsxx.html) (ultra-small isolated AC-DC supply (needs neutral)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Tuya Smart (涂鸦智能)** (涂鸦智能模组部门, developer.tuya.com) — platform + module maker; 151 boards in the catalogue; files via Tuya Smart public module documentation · https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber. Directory entry: WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side. Boards used here: [Tuya TS24-U Thread module](/db/tuya-ts24-u.html) (alternative Thread module in Tuya's 20×16 mm footprint if a white-label brand wants Tuya tooling). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and Hi-Link (海凌科) and Tuya Smart (涂鸦智能) websites)

```email
Subject: Sample order and volume pricing — HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module — for a Thread Switch Insert

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Thread Switch Insert: A relay insert that fits behind the existing European wall switch in a 60 mm flush box and turns any dumb light into a Matter-over-Thread light — keep the switch you like, gain automations. The design is built around your HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module.

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module.
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
主题：样品订购及批量报价 — HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module — 用于Thread Switch Insert

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Thread Switch Insert：A relay insert that fits behind the existing European wall switch in a 60 mm flush box and turns any dumb light into a Matter-over-Thread light — keep the switch you like, gain automations。产品设计基于贵司的HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module。
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
Subject: PCBA quote from open design files — Thread Switch Insert, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Thread Switch Insert: A relay insert that fits behind the existing European wall switch in a 60 mm flush box and turns any dumb light into a Matter-over-Thread light — keep the switch you like, gain automations. The design starts from published open-hardware files (HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Thread Switch Insert，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Thread Switch Insert：A relay insert that fits behind the existing European wall switch in a 60 mm flush box and turns any dumb light into a Matter-over-Thread light — keep the switch you like, gain automations。设计基于已公开的开源硬件文件（HopeRF HM-MT2401C Matter-over-Thread module (IPEX antenna connector), HopeRF HM-MT2401 Matter-over-Thread EVB kit, HLK-10LSxx 10W ultra-small AC-DC isolated power module (10W-LS), Tuya TS24-U Thread module；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order the HM-MT2401 EVB kit, a few HM-MT2401C modules, an HLK-10LS supply and three latching-relay samples; build the thermal test box.
2. List 30 European switch/lighting brands without a Matter-over-Thread insert; book 5 calls.
3. Get one quote from an accredited lab for EN 60669-2-1 + EMC and check current CSA membership/Matter certification costs; put both in your funding plan.

Want help sourcing or building this? Talk to us via www.gongbans.com.
