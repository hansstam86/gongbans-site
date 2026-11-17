# Rain-Barrel Gauge & Pump Controller — Founder Start Pack

> A lid sensor for rain barrels and 1,000-litre IBC tanks that shows how many litres you have and runs the garden pump only when the barrel has water and the soil needs it — sold as a garden-centre own-brand product with a white-label app.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Gardeners collect rainwater but don't know how much is left, run pumps dry (and burn them out), and water on a timer even after it rained. Summer droughts and local tap-water watering restrictions make the barrel matter more every year.
- **Customer:** Garden centres and DIY chains that want an app-connected own-brand line (they pay), and gardeners/allotment holders in DE, NL, BE, FR (they use). Direct-to-consumer as the proving ground.
- **Product:** A UV-proof lid unit with a 24 GHz level radar (no contact with the water, ±3 mm per module spec) and a Wi-Fi/BLE module, plus a switched 12 V output for a low-voltage submersible pump. Litres per tank shape, dry-run protection, schedules that skip after rain, optional soil probe.
- **Why now:** Rainwater harvesting is booming with summer droughts; retailers want connected garden products fast, and a white-label IoT app platform (Tuya) shortens app development from months to weeks — with a cloud dependency you must disclose.
- **The ask:** ~€95k to first 1,000 units; bring a garden-centre buyer in before Christmas buying rounds for spring and let their order fund the tooling.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will a garden-centre buyer list it for spring at €69 — and accept that app features stop working if the Tuya cloud account ends? Pitch before Christmas buying rounds.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Gardeners and allotment holders in DE/NL/BE/FR facing summer watering bans; garden-centre own brands.

**The problem as the pack states it:** Gardeners collect rainwater but don't know how much is left, run pumps dry (and burn them out), and water on a timer even after it rained. Summer droughts and local tap-water watering restrictions make the barrel matter more every year.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/gardening** · https://www.reddit.com/r/gardening/ — home gardeners.
- **r/UKGardening** · https://www.reddit.com/r/UKGardening/ — UK gardeners and allotment holders; hosepipe bans come up every summer.
- **The National Allotment Society (UK)** · https://thenas.org.uk/ — UK allotment federation (formerly NSALG); member associations run the sites.
- **Bundesverband der Kleingartenvereine Deutschlands (DE)** · https://kleingarten-bund.de/ — German allotment federation; the regional and local Kleingartenvereine are the way in.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€59–79 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how gardeners and allotment holders in DE/NL/BE/FR facing summer watering bans deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know how much water is left in your barrels or tank, and what did you do last summer when there was a watering ban or the barrel ran dry?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A lid sensor for rain barrels and 1,000-litre IBC tanks that shows how much water you have and runs the garden pump only when the barrel has water and the soil needs it — set up in a white-label app. On a scale of one to ten, how likely would you be to buy that at €59–79 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Rain-Barrel Gauge & Pump Controller: would you pay €59–79 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Rain-Barrel Gauge & Pump Controller: A lid sensor for rain barrels and 1,000-litre IBC tanks that shows how much water you have and runs the garden pump only when the barrel has water and the soil needs it — set up in a white-label app. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €59–79 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

A 300-litre barrel is 3–4 evenings of watering for a small garden. People find out it's empty when the pump sucks air. Cheap submersible pumps die of dry-running; mid-range barrel pumps have a float switch that jams in leaves. Nobody knows the actual litres, and nobody's timer knows it rained last night.

- **Who pays (scale):** garden-centre chains and DIY retailers' garden category buyers — they need a connected product for the "climate garden" shelf and prefer own-brand margin. They buy in autumn/winter for spring.
- **Who pays (launch):** keen gardeners and allotment holders (Kleingärtner in DE: ~900k plots per the national federation — check), people with 1,000 L IBC tanks on allotments and small farms, eco-gardening households.
- **Who uses:** the gardener, via the app or the lid's own LED level bar if they never open the app.

### Market size (estimates — check)

- **TAM:** DE+NL+BE+FR+AT households with a garden ≈ 40M (rough); assume 30% have at least one rain barrel → 12M barrels. One unit at €69 → **~€830M** theoretical.
- **SAM:** households that also pump from the barrel (barrel pump, IBC with pump) and buy garden tech: assume 10% → 1.2M; at €69 → **~€83M**.
- **SOM (3 years):** one or two retailer own-brand programmes at 5–10k units/season plus 3k D2C → **~15–25k units**, €0.6–1.2M revenue (mostly at wholesale prices). Year 1: 1,000–3,000.

### Competition (1 search + category knowledge)

| Alternative | What it is | Why we can still win |
|---|---|---|
| Do nothing / dipstick / float gauge on the barrel | €5–15 mechanical level indicator | No pump logic, no rain skip, no remote reading |
| Barrel pumps with built-in timer/float switch (big garden brands) | Pump + basic automation | Float jams; no litres, no weather/soil logic; tied to one pump |
| 433 MHz tank level meters (generic, e.g. models used with Homey) | Ultrasonic level + indoor display | Needs 30–40 cm clearance; no pump control; hub for remote |
| DIY ESP32 + ultrasonic/float switches in Home Assistant | Cheap, flexible | Enthusiasts only; ultrasonic fogs in humid barrels |
| Smart irrigation controllers (tap-based Wi-Fi valves) | Schedules on mains water | Tap water, not rainwater; no barrel level |
| Australian tank monitors (e.g. Kingspan SENSiT) | Level + app | Built for large tanks; not sold for EU garden barrels |

**Wedge:** the only lid-mounted product (that we found) that combines contact-free litres with pump control for a normal rain barrel — and it can carry the retailer's brand.

### Product & value proposition

- **Lid unit:** IP65 housing, UV-stabilised ASA, mounts on the lid of a 200–500 L barrel or the top of an IBC (adapter for the IBC cap). Radar looks down through a radome; keep ≥15 cm above max water level (module minimum range 0.15 m).
- **Level:** litres from a tank-shape table (barrel diameters, IBC 1,000 L, custom cylinder/rectangle). LED bar on the unit (5 segments) so it's useful without the app.
- **Pump control:** 12 V DC output up to 5 A for a low-voltage submersible pump; cut-off at minimum level (dry-run protection); schedules; skip if the barrel filled by >X litres in the last 24 h (= it rained) — the barrel itself is your rain gauge. Optional capacitive soil probe.
- **Power:** certified 12 V adaptor (sold in the box) — keeps everything at the barrel SELV. A 230 V pump version via a certified smart plug, not via our own relay.
- **App:** white-label (retailer brand) on the Tuya platform at launch; local fallback: lid LED + a button for "water now".
- **Bundles:** lid unit alone €69; with a 12 V barrel pump €109.

**Pricing (estimates):** D2C **€79** (brand launch); retailer own-brand wholesale **€32–36** FOB/DDP for a €69 shelf price; allotment association 10-pack €590.

### Unit economics (estimates, EUR per lid unit incl. 12 V adaptor, no pump)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (HLK-LD2413 level radar ~€6.0, Tuya CBU module €2.0, 12 V/5 A MOSFET switch + current sense €0.8, buck regulator €0.6, PCB/passives/connectors €1.5, cable glands €0.6) | 11.5 | 9.6 |
| Certified 12 V/2 A adaptor (outdoor-rated cable) | 3.5 | 3.0 |
| PCBA assembly + test | 2.0 | 1.4 |
| Enclosure (UV-stable ASA, radome, IBC adapter) | 3.5 | 2.4 |
| Packaging + leaflet | 2.0 | 1.5 |
| Freight + duty to EU | 1.8 | 1.0 |
| Tuya licence/cloud fee per device (estimate — get the quote) | 1.0 | 0.8 |
| Certification amortised (€16k) | 16.0 | 3.2 |
| **Landed cost** | **41.3** | **22.9** |
| D2C at €79 incl. VAT → €66.4 net, less €7 fulfilment | 59.4 | 59.4 |
| **Gross margin D2C** | **€18.1 (30%)** | **€36.5 (61%)** |
| Retailer own-brand wholesale at €34 | -€7.3 | €11.1 (33%) |

Blunt: own-brand only makes sense at 5k+ per season, and the retailer should pay for the tooling (or pre-pay 30%). The radar is the cost driver — if it quotes above €7, look at a cheaper level-radar module before you look at anything else.

### Go-to-market

**First 100 customers:**
- Allotment associations (Kleingartenvereine): offer one association a 10-unit pilot at cost in March; they talk to each other at every federation meeting.
- Gardening communities: mein-schoener-garten forum, r/gardening and r/Kleingarten-type subs, gardening YouTubers who review barrel pumps (send units, not money).
- Permaculture/rainwater groups and the rainwater-harvesting trade association newsletters (fbr in DE — check).
- D2C landing page with pre-orders in January–March (the buying window).

**Then scale:** two meetings that matter — the garden category buyer at a DIY/garden chain (autumn, for next spring) and an online garden retailer. Trade fair: spoga+gafa (Cologne, garden trade fair — check dates). Then NL/BE garden centres, FR jardineries.

### 12-month plan (anchored on the garden season)

- **Q1 (Jan–Mar):** 10 prototypes on barrels at friends/allotments; buyer pitch with the kill question; D2C pre-orders; lab quotes.
- **Q2 (Apr–Jun):** pilot season: 50 units on allotments; rev A; measure litres accuracy, rain-skip logic, condensation on the radome.
- **Q3 (Jul–Sep):** rev B, certification, tooling; spoga+gafa with a retailer-ready sample; close a spring own-brand order.
- **Q4 (Oct–Dec):** 1,000 D2C units + retailer order production (ship to EU warehouse by February).

**Team:** founder (retail sales), embedded engineer (part-time; Tuya SDK on BK7231N), mechanical designer (contract; outdoor enclosure, UV, radome), app configurator (Tuya white-label is configuration, not code — 2–4 weeks part-time), Shenzhen partner.

**Funding to first 1,000 units (estimate):** landed hardware excl. cert (1,000 × €25.3) €25k + tooling €14k + certification €16k + Tuya app/platform setup €3k + prototypes/pilot €5k + 6 months part-time team €35k + marketing/trade fair €8k = **≈€106k**. Offsets: D2C pre-orders (300 × €59 early-bird) €18k, retailer tooling contribution/pre-payment €10–20k. Net need **≈€70–80k**. Route: pre-orders + retailer pre-payment; climate-adaptation / water-saving grants for SMEs (search national and regional programmes); angel from the garden trade if a chain signs.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** condensation/droplets on the radome, foam, leaves floating; narrow barrels give side reflections | Radome angle + hydrophobic coating; median filtering; test 200 L narrow barrels and IBCs early; module spec ±12° beam — check in practice |
| **Technical:** BK7231N/Tuya SDK learning curve | Tuya's module SDK + their reference apps; budget 4 weeks |
| **Platform dependency (Tuya cloud):** app features (remote level, schedules from the phone, push) depend on Tuya's cloud; if the retailer's Tuya account ends or Tuya changes terms, the app stops working | Keep core functions local: dry-run protection, schedules stored on device, LED level bar, "water now" button. Contract with Tuya with defined service terms. Disclose it on the box ("app requires cloud service") |
| **Tuya-free alternative** | Same PCB footprint with an ESP32-C3 module + ESPHome/Matter-over-Wi-Fi for a "local/Home Assistant" SKU. Community firmware for BK7231N exists (search OpenBeken / LibreTiny) but don't ship a product on reflashed modules — you lose Tuya's certifications and support |
| **GDPR / data residency:** Tuya hosts EU users in its EU region (verify the data centre location and the DPA in your contract); data includes location (garden) and usage patterns | Data-processing agreement with Tuya, privacy notice naming the processor, minimise data (no precise GPS — use postcode for weather) |
| **Market:** retailer wants €25 wholesale | Walk away below €30; push bundle with pump; sell D2C |
| **Regulatory:** pump switching | Only 12 V SELV pumps from our unit; mains pumps via a certified smart plug |
| **Supply:** Hi-Link level radar and Tuya module single-source | Qualify a second level sensor (ultrasonic fallback SKU) and the ESP32 footprint |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2413 24 GHz liquid-level radar | https://www.gongbans.com/db/hilink-ld2413.html | Non-contact level: 0.15–10 m, ±3 mm, ±12°, 3.3 V, 23 mA @ 160 ms, UART, 44×36 mm | Datasheet public, files via maker (no open schematic) | Buy as module |
| Tuya CBU Wi-Fi + BLE module (BK7231N) | https://www.gongbans.com/db/tuya-cbu.html | Wi-Fi/BLE + white-label app via Tuya's platform; ADC, SPI, PWM | Datasheet public, files via maker (no open schematic) | Tuya platform terms apply; per-device licence |
| Seeed Grove-Relay | https://www.gongbans.com/db/seeed-grove-relay.html | Reference for the pump switching stage (prototype); replace with a MOSFET for 12 V DC in the product | schematic | Seeed wiki resources — check licence |

### Block diagram

```
12 V certified adaptor ─► protection ─┬─► buck 3.3 V ─► Tuya CBU (BK7231N) ⇄ Wi-Fi ⇄ Tuya cloud ⇄ white-label app
                                      │                    │ UART          │ GPIO/ADC
                                      │                LD2413 radar     LED bar, button, soil probe (opt.)
                                      └─► MOSFET + current sense ─► 12 V submersible pump
Local logic on module: litres = f(distance, tank shape); pump only if litres > min; skip if barrel rose > X L in 24 h
```

**Engineering gap:** level → litres with real tank shapes; radome and mounting that don't collect water; dry-run detection that also uses pump current (a pump drawing low current = sucking air); local-first behaviour when Wi-Fi/cloud is down.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| HLK-LD2413 | €5–7 | Single source; ask Hi-Link for 1k/5k pricing and lead time |
| Tuya CBU module | €1.8–2.2 | Bought with Tuya licence; MOQ via Tuya |
| Logic-level MOSFET 30 V/10 A + shunt | €0.5 | |
| Buck 12→3.3 V | €0.6 | |
| Soil probe (capacitive, optional) | €1.5 | Separate SKU |
| UV-stable ASA housing + radome | €3.5 | Tooling ~€10–12k |
| 12 V/2 A outdoor-cable adaptor (CE/GS) | €3.5 | Buy certified, don't design |

### Firmware/software starting point

- **Tuya IoT Development Platform**: create the product, pick the "TuyaOS" module SDK for BK7231N, define data points (level %, litres, pump state, schedules), configure the white-label app ("OEM app"). Confirm current pricing and terms before committing.
- **Tuya-free SKU:** ESP32-C3 + **ESPHome** (UART component for the radar; a small custom parser for the LD2413 protocol) → Home Assistant; or Matter over Wi-Fi via ESP-IDF's esp-matter.
- Weather skip without weather APIs: use the barrel's own rise as a rain gauge — no third-party data needed.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — buyer meeting(s) with a mock-up and price; 15 gardener interviews; 2 dev-kit units on real barrels | One buyer agrees to evaluate for spring at ≥€30 wholesale and accepts the cloud disclosure; ≥8/15 gardeners would pay €69+ |
| 3–5 | **Works-like** — 10 units on barrels/IBCs (allotments), Tuya data points, pump control with dry-run cut-off | Level within ±1 cm over 2 weeks incl. rain; zero dry-runs; rain skip works |
| 6–8 | **Looks-like + EVT** — rev A PCB, printed UV housing, 25 units; app branded | IP65 spray test pass (internal); radome stays readable in fog/rain; buyer reviews the branded app |
| 9–10 | **DVT + pre-compliance** — rev B, RED/EMC pre-scan, UV/thermal cycling (−10 to +60 °C), EN 18031 gap check | No pre-scan fails; enclosure survives 200 h UV test without cracking |
| 11–12 | **Pilot batch** — 50 units to allotment associations + buyer's test stores | ≥90% still installed after 4 weeks; retailer purchase order or LOI for the season |

### Certification checklist (EU)

- **CE — RED:** EN 300 440 (24 GHz radar module — note the LD2413 operates 23–27 GHz per the brochure; confirm the band used in EU mode is within an allowed SRD/level-probing allocation — level-probing radar has its own harmonised standard, EN 302 729, for LPR; ask the lab which applies), EN 300 328 (Wi-Fi/BLE), EN 301 489-1/-3/-17, EN 62368-1 (12 V SELV product + certified adaptor), EN 62311.
- **EN 18031-1 (RED delegated act cybersecurity):** yes — internet-connected via Wi-Fi. EN 18031-2 if personal data is processed (it is: account, location by postcode). Tuya supplies module-level documentation; your product still needs its own assessment.
- **CRA:** product with digital elements; security updates (Tuya OTA), SBOM, vulnerability contact by Dec 2027; remote data processing (Tuya cloud) is part of the product under CRA — your supplier contract must cover it.
- **IP65** (EN 60529), UV/outdoor durability (no CE requirement, but retailers will ask).
- **RoHS, REACH, WEEE**, packaging registration. Ecodesign external power supply rules for the adaptor (buy one that already complies).
- **GDPR:** account data, usage patterns; DPA with Tuya; privacy notice; EU data residency confirmed in writing.
- No battery regulation (mains adaptor) unless you add a backup cell. No toy directive. No MDR.
- **Estimated test costs:** €13–18k.

### Validation toolkit

- **Kill question:** Will a garden-centre buyer list it for spring at €69 — and accept that app features stop working if the Tuya cloud account ends? Pitch before Christmas buying rounds. **Cheapest experiment:** a working dev-kit unit on a barrel, a 1-page sell sheet with the retailer's logo, and 3 buyer meetings.
- **Interview script (5) — gardeners:**
  1. How do you water now — tap, barrel, both? How big is your barrel/tank?
  2. How do you know how much water is left? Ever run a pump dry?
  3. Do you water on a schedule? What happens when it rained?
  4. Would you use an app for the garden, or should the device just work?
  5. €69 for level + automatic pump control: yes/no? With a pump for €109?
- **Landing page:** Headline: "Know how many litres you have. Water only when it makes sense." Bullets: "Contact-free radar: litres on the lid and in the app." / "Never runs your pump dry." / "Skips watering when your barrel says it rained."
- **Pre-order pass:** one retailer LOI/PO ≥2,000 units for spring at ≥€30, **or** ≥250 D2C pre-orders at €59 in the Jan–Mar window.

### First production checklist

- **Samples:** 5 PCBAs from two assemblers; golden sample with level accuracy measured at 0.2/0.5/1.0 m on water.
- **DFM review:** radome thickness/angle (radar transparency of ASA at 24 GHz — test), gasket, cable glands, UV stabiliser in the resin spec, IBC adapter.
- **MOQ talk:** Tuya modules come with licence MOQ; radar modules 1k; enclosure tooling sized for 20k shots/season.
- **QC/AQL:** ISO 2859-1 level II, AQL 0.65/2.5; 100% functional test (radar reads a fixed target at 50 cm ±1 cm, pump output switched under load, Wi-Fi pairing test), IP spray test on sample basis.
- **Packaging:** retailer-branded box option, outdoor-safe instructions, tank-shape quick setup sheet.
- **Incoterms:** FOB for D2C; retailers often want DDP to their EU DC with seasonal delivery windows — price it in, and agree what happens with unsold stock (no returns!).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and Tuya Smart (涂鸦智能) and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2413 24 GHz liquid-level detection radar module](/db/hilink-ld2413.html) (24 GHz low-power level radar (no contact with the water)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Tuya Smart (涂鸦智能)** (涂鸦智能模组部门, developer.tuya.com) — platform + module maker; 151 boards in the catalogue; files via Tuya Smart public module documentation · https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber. Directory entry: WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side. Boards used here: [Tuya CBU Wi-Fi + Bluetooth LE module](/db/tuya-cbu.html) (Wi-Fi module with white-label app). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Relay](/db/seeed-grove-relay.html) (pump relay reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and Tuya Smart (涂鸦智能) and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay — for a Rain-Barrel Gauge & Pump Controller

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Rain-Barrel Gauge & Pump Controller: A lid sensor for rain barrels and 1,000-litre IBC tanks that shows how much water you have and runs the garden pump only when the barrel has water and the soil needs it — set up in a white-label app. The design is built around your HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay.
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
主题：样品订购及批量报价 — HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay — 用于Rain-Barrel Gauge & Pump Controller

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Rain-Barrel Gauge & Pump Controller：A lid sensor for rain barrels and 1,000-litre IBC tanks that shows how much water you have and runs the garden pump only when the barrel has water and the soil needs it — set up in a white-label app。产品设计基于贵司的HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay。
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
Subject: PCBA quote from open design files — Rain-Barrel Gauge & Pump Controller, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Rain-Barrel Gauge & Pump Controller: A lid sensor for rain barrels and 1,000-litre IBC tanks that shows how much water you have and runs the garden pump only when the barrel has water and the soil needs it — set up in a white-label app. The design starts from published open-hardware files (HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Rain-Barrel Gauge & Pump Controller，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Rain-Barrel Gauge & Pump Controller：A lid sensor for rain barrels and 1,000-litre IBC tanks that shows how much water you have and runs the garden pump only when the barrel has water and the soil needs it — set up in a white-label app。设计基于已公开的开源硬件文件（HLK-LD2413 24 GHz liquid-level detection radar module, Tuya CBU Wi-Fi + Bluetooth LE module, Seeed Grove-Relay；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order 2× HLK-LD2413 and a Tuya CBU dev board; mount one on a real barrel with a 12 V pump and log level for a week (it's November — a water butt in the garage works).
2. Ask Tuya for written terms: per-device licence, OEM app cost, EU data residency, and what happens to devices if the account is closed. That letter is half your pitch to a buyer.
3. Find the garden category buyer at two chains and one online garden retailer; request a 20-minute slot in December/January.

Want help sourcing or building this? Talk to us via www.gongbans.com.
