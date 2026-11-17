# Powerline Outbuilding Energy Monitor — Founder Start Pack

> A DIN-rail meter for the garden house, sauna, workshop or stable that measures the circuit's energy and reports over the mains wiring itself, where Wi-Fi doesn't reach, to an app.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

**Two hard truths before you start:**
1. **The PLC module's band.** The Tuya S130N-ISI in the catalogue uses **IEEE 1901.1 / the Chinese grid PLC standard (SGCC Q/GDW 11612) over 0–12 MHz**. That is not the European CENELEC narrowband (3–148.5 kHz, EN 50065) world. Signals in the low-MHz range on mains wiring fall under EU in-home PLC emission rules (EN 50561-1 territory) and overlap HF radio bands, which radio amateurs actively complain about. Check with an EMC lab **in week 1** whether a 1901.1 device can pass EU conducted-emission requirements. If not, switch to a CENELEC-band PLC modem or sub-GHz radio.
2. **This is not a billing meter.** Allotment associations or holiday parks that *bill* members/guests for electricity need an approved (MID) meter. This product is for information. Say so.

## 1. Summary

- **Problem:** Outbuildings with electric heaters, saunas, pumps, kilns, compressors and EV chargers are energy blind spots. Wi-Fi rarely reaches them, so smart meters/plugs don't work there. Owners find out about the sauna left on or the frost heater running all winter only from the annual bill.
- **Customer:** Homeowners with outbuildings (DE, NL, Nordics, AT), small farms and stables, holiday-park operators (information per cabin), allotment associations (information, not billing). The owner pays and uses it.
- **Product:** A DIN-rail module in the outbuilding's sub-panel with a clamp-on current transformer, measuring kWh and peak power. It talks over the existing mains cable to a plug-in head unit in the house, which connects to the home network and an app. Alerts for "sauna left on", "frost heater running in April", and monthly cost at the user's own tariff.
- **Why now:** Energy prices made "where does my power go?" mainstream; heat pumps, saunas and garden offices added big loads in outbuildings; PLC chips are cheap; the cable to the outbuilding is already there.
- **The ask:** About €180–230k (estimate) to the first 1,000 pairs, via electrician pre-orders, an energy-efficiency grant, and one angel. Much less if you use existing certified modules instead of designing PLC coupling yourself.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does the PLC link survive through a residual-current device and 50 m of garden cable in 10 houses? And will buyers accept the Tuya-cloud dependency for the app?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Homeowners with outbuildings, small farms, allotment associations with shared power, holiday-park operators.

**The problem as the pack states it:** Outbuildings with electric heaters, saunas, pumps, kilns, compressors and EV chargers are energy blind spots. Wi-Fi rarely reaches them, so smart meters/plugs don't work there. Owners find out about the sauna left on or the frost heater running all winter only from the annual bill.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.
- **Photovoltaikforum (DE)** · https://www.photovoltaikforum.com/ — German PV, battery, heat-pump and dynamic-tariff owners.
- **Bundesverband der Kleingartenvereine Deutschlands (DE)** · https://kleingarten-bund.de/ — German allotment federation; the regional and local Kleingartenvereine are the way in.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€89–129 pair (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how homeowners with outbuildings, small farms, allotment associations with shared power, holiday-park operators deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know what your garden house, sauna, workshop or stable uses in electricity today, and how is the power for it shared or billed?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A DIN-rail meter for the garden house, sauna, workshop or stable that measures the circuit's energy and reports over the mains wiring itself — where Wi-Fi doesn't reach — to an app. On a scale of one to ten, how likely would you be to buy that at €89–129 pair (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Powerline Outbuilding Energy Monitor: would you pay €89–129 pair (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Powerline Outbuilding Energy Monitor: A DIN-rail meter for the garden house, sauna, workshop or stable that measures the circuit's energy and reports over the mains wiring itself — where Wi-Fi doesn't reach — to an app. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €89–129 pair (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Primary: **homeowners with a powered outbuilding** (garden office, sauna, workshop) in DE/NL/Nordics/AT, typically on a sub-panel fed by an underground cable 10–60 m long. They pay; an electrician installs (DIN-rail = fixed installation; in most countries that means an electrician). Secondary: **stables and small farms** (pumps, heaters, water-trough heaters). Third: **holiday parks** — consumption per cabin for operational decisions (not billing).

### Market size (estimates)
- DE + NL + AT + Nordics: ~25 M owner-occupied houses; assume 10% have a powered outbuilding with meaningful loads → **~2.5 M**. Plus small farms/stables.
- **TAM:** 2.5 M × €109 ≈ **€270 M**.
- **SAM:** owners who care about energy and would pay an electrician to install (~10%) → **~€27 M**.
- **SOM (3 years):** 2% of SAM → **~5k pairs → ~€550k**. Niche; better as one product in an energy-monitoring range, or white-labelled by an energy company.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Wi-Fi DIN-rail energy meter (e.g. [Shelly Pro EM-50 at ~€78](https://www.smartech.ee/en/products/muu/shelly-pro-em-50-energy-meter-wifilan-5)) + a HomePlug powerline adapter pair to bring the network to the outbuilding | €78 + €60–120 adapters | Works — this is the real competitor. But: two products, a powerline adapter sitting on a socket in the shed, Ethernet/Wi-Fi bridging config |
| Meter in the main panel measuring the outbuilding feeder | €50–80 | Best solution if the feeder leaves the main panel and there's space — no PLC needed at all |
| Wi-Fi meter + Wi-Fi mesh/outdoor access point | €80 + €80–150 | Extra network gear; garden Wi-Fi often unreliable |
| Smart plugs on individual devices | €15–25 each | Doesn't work for hard-wired saunas, heaters, pumps |
| Home-energy monitors with CT clamps on the main supply | €50–150 | See the whole house, not the outbuilding |
| Do nothing: read the annual bill | Free | — |

**Wedge (narrow, be honest):** **one-box install, no network gear in the outbuilding, outbuilding-specific alerts** (sauna, frost heater, pump short-cycling). If the electrician can put the CT on the feeder in the main panel, the customer doesn't need you — target installations where that isn't possible (sub-panel fed from a separate meter or long cable, no space in the main panel, or the shed has its own sub-circuits to watch).

### Product & value proposition
- **Outbuilding unit (DIN-rail, 1–2 modules wide):** CT clamp input (Seeed Grove-Electricity Sensor as a sensing reference; production: proper metering IC + CT), voltage sense, metering-grade energy calculation, PLC modem (Tuya S130N-ISI in the original concept — see the band warning), isolated supply (Hi-Link HLK-PMxx 3 W, 85–265 VAC, with EMC circuit variant).
- **Head unit (plug-in, in the house):** PLC coordinator + Wi-Fi to the app.
- **The Tuya cloud dependency:** with Tuya modules and Tuya's app/white-label tools, data goes through Tuya's cloud; no internet = no app (the meter still counts locally). The S130N-ISI is a **station** module: you also need a matching coordinator in the head unit — check that Tuya supplies one and whether it works outside China's grid-PLC ecosystem.
- **Tuya-free alternative (recommended to evaluate first):**
  - (a) **CENELEC-band narrowband PLC** (band C/B for consumer use, EN 50065) modem in both units + a local hub/app (Home Assistant integration, MQTT) or your own EU cloud; or
  - (b) **868 MHz sub-GHz radio** instead of PLC — often reaches 30–100 m to a garden building and avoids the coupling and emission issues entirely. Ask: is PLC actually needed?
- **App:** kWh per day/month, peak power, cost at your tariff, alerts (load on longer than X h, load during "away", unusual night consumption), export.

**Pricing (estimates):** €109 pair (outbuilding unit + head unit) RRP; €69 extra outbuilding unit; installer price €80/pair. No subscription in the Tuya-free local version; optional €1/month cloud history.

### Unit economics (estimates per pair, ex-VAT)
| Item | 1k pairs | 5k pairs |
|---|---|---|
| BOM outbuilding unit (PLC modem + coupling transformer/caps, metering IC, CT clamp, HLK-PM supply, MCU, terminals, PCB) | €17.00 | €13.50 |
| BOM head unit (PLC modem + coupling, Wi-Fi MCU, supply, plug housing parts) | €11.00 | €8.50 |
| Assembly & test (2 units, hi-pot, metering calibration, PLC link test) | €4.50 | €3.00 |
| Enclosures (DIN-rail V-0 + plug-in housing with mains pins) | €4.50 | €3.00 |
| Packaging | €1.50 | €1.00 |
| Freight + duty to EU | €1.20 | €0.80 |
| Certification amortised (~€40k: LVD for both, EMC incl. PLC emissions, RED for Wi-Fi) | €40.00 | €8.00 |
| **Landed cost** | **€79.70** | **€37.80** |
| Net revenue (direct €92 ex-VAT; installer/wholesale €67) | €92 | €67 |
| **Gross margin** | **€12.30 (13%)** | **€29.20 (44%)** |

The plug-in head unit with mains pins is a whole second mains product — it doubles your safety testing. Option: put the head unit on a DIN rail in the main panel too (electrician installs both) — simpler certification, and it's the same install visit.

### Go-to-market
**First 100 customers:**
- **Electricians who install saunas, garden offices and outbuilding sub-panels**: they're on site with the panel open. Give 20 installers a demo kit and margin.
- **Sauna, garden-office and tiny-house builders**: bundle the monitor as an option at the point of sale.
- **Energy-saving communities** (home-energy forums, smart-meter/home-automation communities, energy-advice associations).
- **Horse/stable associations** (frost heaters for water, lights, pumps).

**Scale:** electrical wholesale; white-label for an energy retailer or a sauna brand; holiday-park operators.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | **Band/EMC check** of the PLC choice with a lab; kill test: PLC link in 10 houses through RCD + 50 m cable; Tuya vs Tuya-free decision |
| Q2 | Works-like pairs in 20 houses; app/alerts; installer feedback |
| Q3 | EVT/DVT; LVD/EMC (incl. conducted emissions)/RED testing |
| Q4 | 1,000 pairs; 50 installers; one sauna/garden-office brand bundle |

**Team:** 1 power/metering engineer (mains + PLC coupling + EMC — rare skills, hire or contract someone who has done PLC before), 1 embedded/app developer, founder on installer channel.

**Funding to the first 1,000 pairs (estimates):** NRE €80k (hardware 2 units €40k, firmware/app €30k, tooling €10k) + certification €40k + 1,000 pairs landed ~€40k + 9 months lean costs €60k ≈ **€220k**. Minus installer pre-orders (300 pairs × €80 ≈ €24k) and an energy-efficiency/SME innovation grant (€30–60k where available) → **~€140–170k**. If you switch to sub-GHz radio instead of PLC, NRE and certification risk drop noticeably.

### Top risks
| Risk | Mitigation |
|---|---|
| **Regulatory/EMC: 0–12 MHz PLC emissions on EU mains** (and interference complaints) | Lab check in week 1; if negative, CENELEC-band modem or 868 MHz radio |
| **Technical:** PLC through RCDs, different phases, long garden cable, noisy loads (heat-pump inverters, LED drivers) | Kill test in 10 real houses; phase coupler advice; fallback radio |
| **Tuya dependency:** cloud required for app; GDPR/data residency (consumption profiles reveal presence/habits = personal data); coordinator availability for EU use | Tuya-free design path; if Tuya: DPA, data-location check, disclose on the box |
| **Market:** a Wi-Fi meter + powerline adapter is "good enough"; or the CT goes in the main panel | Target only installs where that doesn't work; sell through sauna/garden-office builders |
| **Regulatory:** customers using it for billing | "Not for billing" label; offer MID-meter guidance |
| **Supply:** PLC modem ecosystem (Chinese-standard parts may not suit EU) | Pick a modem with EU deployments; keep metering front-end separate |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Tuya S130N-ISI PLC module | https://www.gongbans.com/db/tuya-s130n-isi.html | PLC station modem (IEEE 1901.1, 0–12 MHz, Cortex-M4 + DSP, UART/SPI/I2C) — needs external mains coupling | **Datasheet public, files via maker** (no open schematic/PCB) | Tuya platform terms; check EU suitability of the band |
| Seeed Grove-Electricity Sensor | https://www.gongbans.com/db/seeed-grove-electricity-sensor.html | CT current-sensing reference | Schematic | Check Seeed's licence for the wiki design files |
| Hi-Link HLK-PMxx 3 W isolated AC-DC | https://www.gongbans.com/db/hilink-pmxx.html | Small isolated supply (EMC-circuit variant listed) | **Datasheet public, files via maker** | Commercial module; check its safety approvals |

### Block diagram
```
 OUTBUILDING SUB-PANEL (DIN rail)                                         HOUSE
 [CT clamp on feeder] -> [metering IC] -> [MCU] -> [PLC modem] -[coupling]-> ═══ mains cable (10-60 m, via RCD) ═══ -[coupling]-> [PLC coordinator] -> [Wi-Fi MCU] -> app (Tuya cloud | local hub/own EU cloud)
 [voltage sense] ------^                   |
 [HLK-PM 3 W supply]                [local kWh store, LEDs]
 Alternative path: replace both PLC blocks with 868 MHz radios (no coupling, no conducted-emission issue).
```
**Engineering gap:** mains coupling circuits and EMC filtering for PLC (the specialist part), metering calibration, the head unit, the alert logic, and — critically — a decision on PLC band vs radio.

### Starter BOM (estimates at 1k, per pair)
| Part | Est. cost | Notes |
|---|---|---|
| 2× PLC modem (S130N-ISI + coordinator, or CENELEC modem) | €8–12 | **Check coordinator availability and EU band suitability first** |
| PLC coupling (transformer, capacitors, protection) ×2 | €3.00 | X-capacitors and surge protection — safety-critical |
| Metering IC + CT clamp | €4.50 | Split-core CT for retrofit |
| MCU + Wi-Fi MCU (head unit) | €3.50 | |
| 2× isolated supply (HLK-PMxx) | €3.00 | |
| PCBs, terminals, fuses, varistors | €3.00 | |
| Enclosures (DIN + plug-in/DIN) | €4.50 | Tooling ~€10–15k |

### Firmware/software starting point
- **Tuya route:** Tuya developer platform docs for the PLC series (module + coordinator), Tuya MCU-SDK for your metering MCU.
- **Tuya-free route:** search "Home Assistant MQTT energy" for a local integration (Home Assistant's energy dashboard is a natural home for this data); a small MQTT broker (search "Eclipse Mosquitto"); for 868 MHz, search "RadioLib" (a widely used Arduino radio library).
- **Metering:** use the metering-IC vendor's application notes for calibration.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Two kill tests:** (1) EMC lab opinion on the PLC band (go/no-go for S130N); (2) dev-kit PLC (or radio) link between a house socket and an outbuilding socket in 10 houses: ≥99% of messages delivered, through the RCD, over the real cable. Plus 10 installer interviews |
| 3–5 | Works-like | Metering ±2% vs a reference meter at 100 W–3.5 kW; alerts working; 10 houses |
| 6–8 | Looks-like + EVT | DIN enclosure + head unit; 30 pairs; installers fit them in <20 min |
| 9–10 | DVT + pre-compliance | Safety pre-assessment (EN 62368-1 / IEC 61010-1 for the measuring unit as appropriate), conducted-emission pre-scan of the PLC signal, RED for Wi-Fi |
| 11–12 | Pilot batch | 50 pairs via 10 installers; 0 safety issues; ≥1 alert per house acted on in the first month |

### Certification checklist (EU)
- **LVD / safety:** DIN-rail measuring unit — IEC/EN 61010-1 (measurement equipment) or EN 62368-1, depending on classification; plug-in head unit with mains pins has its own requirements. Est. **€12–20k** for both.
- **EMC:** EN 61000-6-1/-6-3 (or product-specific), plus **PLC-specific conducted emissions**: EN 50065-1 for CENELEC 3–148.5 kHz devices; EN 50561-1 for in-home PLC in the 1.6/2–30 MHz range. A 0–12 MHz modem straddles these — get a lab opinion. Est. **€8–15k**.
- **RED:** Wi-Fi in the head unit: EN 300 328, EN 301 489-1/-17, EN 62311. Est. €5–8k.
- **RED delegated act (EN 18031-1/-2):** head unit is internet-connected; consumption data is personal data. Self-assessment €3–6k.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: updates, SBOM, vulnerability handling (both units have firmware).
- **Metrology:** not a MID billing meter — label "for information only, not for billing".
- **RoHS, REACH, WEEE**, packaging registration.
- **GDPR:** consumption profiles reveal presence/habits → personal data. Tuya route: DPA + data location; local route: minimal.
- **Total estimate: €30–50k.**

### Validation toolkit
- **Kill question:** Does the PLC link survive through a residual-current device and 50 m of garden cable in 10 houses — and is its band legal in the EU? And will buyers accept the Tuya-cloud dependency for the app?
- **Cheapest experiment (~€300):** a pair of off-the-shelf powerline adapters + a pair of 868 MHz dev boards in 10 friends' gardens to see which link type works; meanwhile ask an EMC lab for an opinion on the S130N band.
- **5-question interview (owner/installer):** 1) What's in your outbuilding that uses power, and how is it fed? 2) Do you know what it costs per year? 3) Have you had a "left on" incident (sauna, heater)? 4) Is there Wi-Fi out there, and have you tried to fix that? 5) At €109 plus installation, would you buy it — and would your electrician install it on the next visit?
- **Landing page headline:** "See what your garden house really costs — no Wi-Fi needed out there." Bullets: "Measures your outbuilding's power right in its fuse box." / "Talks over the existing cable — no extra network gear." / "Alerts when the sauna or frost heater is left on."
- **Pass threshold:** 20 installers each committing to 5 pairs, or 100 paid €20 deposits in 6 weeks.

### First production checklist
- **Samples:** PLC modems/coupling transformers from the production supplier; metering IC calibration samples.
- **Golden sample:** the safety-tested unit; freeze BOM (coupling parts are safety-critical).
- **DFM review:** creepage/clearance, X-capacitor ratings, DIN-clip strength, terminal torque, CT connector.
- **MOQ talk:** modem MOQ, coupling transformer (often custom), CT clamps.
- **QC/AQL:** AQL II 0.65 safety; 100% hi-pot, 100% metering calibration at 2 loads, 100% PLC link test pairing the two units.
- **Packaging:** pre-paired units in one box, wiring diagram, "not for billing" notice, QR onboarding.
- **Incoterms:** FOB Shenzhen; DIN enclosures may be sourced as standard parts in the EU.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Tuya Smart (涂鸦智能) and Seeed Studio and Hi-Link (海凌科)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Tuya Smart (涂鸦智能)** (涂鸦智能模组部门, developer.tuya.com) — platform + module maker; 151 boards in the catalogue; files via Tuya Smart public module documentation · https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber. Directory entry: WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side. Boards used here: [Tuya S130N-ISI PLC module](/db/tuya-s130n-isi.html) (powerline-carrier (PLC) communication module, station role). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Electricity Sensor](/db/seeed-grove-electricity-sensor.html) (current-transformer sensing reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)](/db/hilink-pmxx.html) (3 W isolated AC-DC supply). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Tuya Smart (涂鸦智能) and Seeed Studio and Hi-Link (海凌科) websites)

```email
Subject: Sample order and volume pricing — Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit) — for a Powerline Outbuilding Energy Monitor

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Powerline Outbuilding Energy Monitor: A DIN-rail meter for the garden house, sauna, workshop or stable that measures the circuit's energy and reports over the mains wiring itself — where Wi-Fi doesn't reach — to an app. The design is built around your Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit).

Could you please send:
1. Price and lead time for [10] sample units of each: Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit).
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
主题：样品订购及批量报价 — Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit) — 用于Powerline Outbuilding Energy Monitor

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Powerline Outbuilding Energy Monitor：A DIN-rail meter for the garden house, sauna, workshop or stable that measures the circuit's energy and reports over the mains wiring itself — where Wi-Fi doesn't reach — to an app。产品设计基于贵司的Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)。
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
Subject: PCBA quote from open design files — Powerline Outbuilding Energy Monitor, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Powerline Outbuilding Energy Monitor: A DIN-rail meter for the garden house, sauna, workshop or stable that measures the circuit's energy and reports over the mains wiring itself — where Wi-Fi doesn't reach — to an app. The design starts from published open-hardware files (Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Powerline Outbuilding Energy Monitor，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Powerline Outbuilding Energy Monitor：A DIN-rail meter for the garden house, sauna, workshop or stable that measures the circuit's energy and reports over the mains wiring itself — where Wi-Fi doesn't reach — to an app。设计基于已公开的开源硬件文件（Tuya S130N-ISI PLC module, Seeed Grove-Electricity Sensor, HLK-PM01/PM03/PM12 etc. 3W AC-DC isolated power module, incl. 3W-B and 3W-C (with EMC circuit)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Send the S130N-ISI datasheet to an EMC lab and ask for a written opinion on EU conducted-emission limits for a 0–12 MHz PLC device; ask Tuya whether a matching coordinator is available for EU projects.
2. Run the 10-garden link test with off-the-shelf powerline adapters and 868 MHz dev boards side by side.
3. Interview 10 electricians who install saunas or garden offices about how outbuildings are fed and what they'd install.

Want help sourcing or building this? Talk to us via www.gongbans.com.
