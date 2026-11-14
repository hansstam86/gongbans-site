# HaptiKnob — Haptic Setpoint Knob — Founder Start Pack

> A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Smart homes replaced the thermostat dial with a phone app and a wall of touchscreens. Visitors, kids and partners hate it; the heat-pump maker's own controller is worse. The open-source haptic knob proved people want a physical dial that *feels* like the thing it controls — but it is a desk toy you build yourself.
- **Customer:** Home-automation households in DE/NL/AT/Nordics running a local hub (Home Assistant, Homey, KNX, Loxone), heat-pump owners stuck with a bad UI, and the installers who fit premium smart homes and need a wall control that looks finished.
- **Product:** A 60 mm wall-box knob: BLDC motor + magnetic encoder + round LCD, USB-C or 24 V powered, with haptic profiles per entity (thermostat: fine detents 0.5 °C with soft end-stops; dimmer: smooth with a bump at 100%; volume: coarse clicks). Talks MQTT and Matter to the hub. €149–179 haptic; €79 non-haptic dial SKU on the same firmware (estimates).
- **Why now:** Two open designs exist with schematics and PCB; Chinese brands ship touchscreen dials (Aqara Touchscreen Dial V1 at €80–165) but with vibration only and locked ecosystems; nobody sells a finished *haptic* wall product in Europe with a proper EU box mount.
- **The ask:** ~€140k to first 1,000 haptic units; crowdfund/pre-order driven, with a small angel or founder cheque for tooling and certification.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** The concept is validated by patents and one shipping product, the Aqara Touchscreen Dial V1, which is locked to Aqara's ecosystem; no cross-platform "works with any hub" haptic dial was found, matching the pitch's gap. **Main risk:** Aqara, well funded, could extend its dial to more hubs faster than a newcomer establishes the category. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Post a 30-second haptic-thermostat demo video to home-automation communities with a €149 waitlist. 500 sign-ups in 2 weeks = go.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a fake-door landing page that the million-plus European home-automation households and heat-pump owners who dislike the manufacturer's UI actually visited, with a measured conversion to a waitlist or refundable deposit, plus the interview notes behind it. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** The million-plus European home-automation households and heat-pump owners who dislike the manufacturer's UI; installers of premium smart homes.

**The problem as the pack states it:** Smart homes replaced the thermostat dial with a phone app and a wall of touchscreens. Visitors, kids and partners hate it; the heat-pump maker's own controller is worse. The open-source haptic knob proved people want a physical dial that *feels* like the thing it controls — but it is a desk toy you build yourself.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **r/esp32** · https://www.reddit.com/r/esp32/ — ESP32 builders; good for early technical feedback, less for buyers.
- **Hackaday / hackaday.io** · https://hackaday.io/ — maker audience; visibility more than buyers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (twenty people from the audience line), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79 (dial) / 149–179 (haptic), the pack's estimate), and one button. For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how the million-plus European home-automation households and heat-pump owners who dislike the manufacturer's UI deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. What do you adjust most often in your home automation, and how annoying is doing it from a phone?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub. On a scale of one to ten, how likely would you be to buy that at €79 (dial) / 149–179 (haptic), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: HaptiKnob — Haptic Setpoint Knob: would you pay €79 (dial) / 149–179 (haptic) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a HaptiKnob — Haptic Setpoint Knob: A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79 (dial) / 149–179 (haptic), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

The "setpoint" problem is universal: heating, lighting scenes, blinds, volume. Apps are fine for schedules and terrible for the five-second interaction at the wall. Touch dials exist but lack the one thing that makes a dial satisfying — resistance and detents that change with the function. The motorised-knob hobby projects nailed the feel; what they lack is a wall mount, a quiet motor, a sane power input and a box with a CE mark.

- **Who pays, B2C:** the household's "home-automation person" — they already spent €1–3k on a local hub, dozens of Zigbee devices and a Nabu-Casa-style subscription. Price sensitivity is low if the feel is right.
- **Who pays, B2B:** installers of premium smart homes (KNX/Loxone country: DE, AT, CH, NL) who want a wall control with real feedback for clients who refuse touchscreens. They buy 5–20 per project at trade price.
- **Who uses:** everyone in the house, including the person who refused the app. That is the pitch.

### Market size (estimates — check)

- **TAM:** Home Assistant alone reports well over a million active installs (public analytics, opt-in, so undercounted); add Homey, openHAB, KNX/Loxone homes → ≈3M European homes with a local hub. One knob at €150 = **€450M** theoretical; realistically 2–3 knobs per enthusiast home over time.
- **SAM:** enthusiast homes that already buy wall-mounted controls (NSPanel-class devices, Zigbee dimmer knobs) ≈ 15% → 450k homes → **€70M**; installer channel for premium homes adds **€20–30M**.
- **SOM (3 years):** 15–25k units → **€2–3.5M**. Year 1: 1,000–2,500 (crowdfunding wave plus one installer distributor).

Sources used: Home Assistant public analytics (verify the current number), Aqara Touchscreen Dial V1 retail listings (galaxus.at/.fr, aio.lv), Home Assistant community posts on open-source ESP32-S3 knob controllers.

### Competition (1 search)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing / phone app / voice | €0 | The whole complaint is the app |
| Aqara Touchscreen Dial V1 (DS-K01D) | €80–165 | Vibration only, Aqara ecosystem, not exposed to third-party hubs per retailers — no real haptics, no open API |
| MOES/Tuya Zigbee knob, Philips Hue Tap Dial, IKEA dial | €15–60 | Cheap, works, but a plastic encoder with no screen and no feel |
| NSPanel / Sonoff touch panels | €60–120 | Touch, not a dial; needs flashing to be local |
| Open-source SmartKnob builds / dev kits from small shops | €150–300 + your weekends | The feel is there; no wall mount, no CE, motor whine, bring your own power |
| KNX/Loxone room controllers | €200–600 | Installer-grade, no haptics, closed bus |

**Wedge:** the only finished wall product with true motorised haptics, local-first (MQTT + Matter), EU 60 mm box mount, from a brand the hub communities trust because the firmware is open.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Aqara Touchscreen Dial V1 | Shipping haptic dial, Aqara ecosystem only | Concept proven, gap is cross-platform |
| Haptic smart-home patent (USPTO) | Patent | Prior art to check before launch |
| Immersion Home Smart Panel concept | Concept page | Interest from haptics vendors |

**Verdict as researched: LIKELY.** Main risk: Aqara, well funded, could extend its dial to more hubs faster than a newcomer establishes the category.
<!-- market-competitors:end -->

### Product & value proposition

- Round LCD 1.28" (240×240) behind a machined or moulded knob; BLDC gimbal motor + magnetic encoder; ESP32-S3 (WiFi + BLE; Matter over WiFi) — the Super Dial design is already S3-based.
- Haptic profiles are entities: the hub pushes "thermostat 15–28 °C, 0.5 °C detents, soft stop" and the knob renders it. Press = confirm/next entity. A ring LED shows state when the screen sleeps.
- Power: USB-C PD (5 V/3 A) or 24 V DC from the KNX/Loxone-style power supplies installers already run; never mains inside the knob (keeps you out of mains-LVD territory and the box small).
- Mount: EU 60 mm flush box with claws, plus a surface adapter and a desk stand.
- **Pricing (estimates):** HaptiKnob €169 B2C (€149 early-bird); Dial (non-haptic, same firmware, M5Stack-Dial-class hardware) €79; installer trade price €115 haptic in 10+.

### Unit economics (estimates, EUR per unit; haptic SKU)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-S3 module €3, BLDC gimbal motor €7–9, magnetic encoder €1.5, motor driver €2.5, 1.28" round LCD €6, USB-C PD + 24 V buck €2.5, PCB + passives €4) | 31 | 26 |
| PCBA assembly + test (motor calibration + encoder zero on a jig) | 5.0 | 3.4 |
| Enclosure (knob cap, body, mount ring, claws — 4 tools ~€25k) | 9.5 | 4.2 |
| Packaging + USB-C cable + mount kit | 3.0 | 2.2 |
| Freight + duty to EU | 2.8 | 1.3 |
| Certification amortised (€45k: RED + EN 18031 + EMC with motor PWM + safety) | 45.0 | 9.0 |
| **Landed cost** | **96.3** | **46.1** |
| D2C net price (€169 incl. 19% VAT → €142) less €10 fulfilment | 132 | 132 |
| **Gross margin D2C** | **€36 (27%)** | **€86 (65%)** |
| Installer/distributor net €115 ex VAT | €19 (16%) | €69 (60%) |

At 1k the haptic SKU is thin — the motor and the four enclosure tools eat it. Crowdfund 1,500+ before tooling, or launch the Dial SKU first to amortise firmware and certification.

### Go-to-market

**First 100 customers:** a 30-second video of the knob switching from "thermostat detents" to "dimmer smooth" to "volume clicks" posted in the Home Assistant community forum, r/homeassistant, the Homey community, and two German smart-home YouTube channels that review NSPanel-class devices. Waitlist at €149. Hand-build the first 100 from the open designs (desk-stand version) for the loudest backers — they become the installers' reference.

**Scale:** a Kickstarter/Crowd Supply-style campaign for the wall version; then the smart-home e-tailers in DE/NL (the ones selling Shelly, Aqara, Sonoff), the Home Assistant-compatible hardware stores, and two KNX/Loxone installer distributors with a 24 V variant and a KNX-IP bridge note.

### 12-month plan

- **Q1:** video + waitlist (kill question), build 5 units from the open Super Dial / smartknob designs, measure motor noise and heat; pick the motor; define the MQTT and Matter entity model.
- **Q2:** own PCB (S3 + driver + PD), SLA enclosure, 60 mm mount, 30 beta units to community members; pre-compliance EMC (motor PWM is the risk).
- **Q3:** tooling, DVT, RED + EN 18031 + EMC/safety certification, crowdfunding campaign with the certified-design promise.
- **Q4:** pilot 200, production 1,000, Dial SKU launch, first installer distributor.

**Team:** founder (product/community), 1 firmware engineer (ESP-IDF, FOC motor control, LVGL), 0.5 ME (knob feel is a mechanical problem as much as electrical), contract ID for the cap and mount, part-time Matter/Home Assistant integration developer.

**Funding to 1,000 units (estimate):** NRE €45k (PCB + firmware €15k, tooling €25k, ID €5k) + certification €45k + 9 months lean salaries €60k + 1,000 units at €51 landed €51k = **€200k**, less €120k from 800 pre-orders at €149 → **€80k** gap: founder cheque or one angel. Bootstrap variant: ship the Dial SKU (no motor, €15k certification) first to fund the haptic tooling.

### Top risks

- **Technical — motor whine, heat and cogging in a sealed wall box.** The open designs are desk toys: fans of airflow, no wall. Mitigation: gimbal motor with higher pole count, FOC at >20 kHz PWM, duty-cycle the hold torque, aluminium motor cup as heat sink; measure early (week 3).
- **Technical — EMC.** A BLDC driver next to a WiFi antenna in a metal-ish box. Mitigation: pre-scan at week 8, filtered motor leads, careful antenna placement.
- **Market — "cool demo, no purchase".** Mitigation: the kill question is the waitlist, not the applause. Dial SKU at €79 as a fallback product.
- **Regulatory — Matter certification** is a separate CSA process (membership + test). Mitigation: launch MQTT + Home Assistant native first; Matter in v1.1.
- **Supply — gimbal motors are a cottage industry.** Mitigation: qualify two motors with the same mount pattern; order 1.5k with the tooling.

## 4. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| [已验证]smartknob-original (OSHWHub) | https://www.gongbans.com/db/oshwhub-smartknob-original.html | Verified open clone of the haptic knob: BLDC + magnetic encoder + round LCD. Your feel reference. | schematic, pcb | OSHWHub project licence; the upstream project is open-source — check both before commercial derivation |
| Super Dial 电机旋钮屏—esp32s3—v2 (OSHWHub) | https://www.gongbans.com/db/oshwhub-a2fff3c71f5d4de2b899c64b152d3da5.html | ESP32-S3 motor-knob with screen, v2 — closer to your production architecture | schematic, pcb | OSHWHub project licence — check |
| M5Stack Dial (K130) | https://www.gongbans.com/db/m5stack-dial.html | Non-haptic Dial SKU hardware for prototypes; same firmware | enclosure/structure files only; electronics not published | Off-the-shelf; use as bought |
| M5Stack Unit BLDC Driver (U181) | https://www.gongbans.com/db/m5stack-unit-bldc-driver.html | Motor-driver reference for bench tests if you re-spin | enclosure/structure files only | Off-the-shelf module |

### Block diagram

```
[Knob cap] -- shaft -- [BLDC gimbal motor] <--3-phase-- [FOC driver] <-- [ESP32-S3]
                        [magnetic encoder] --SPI/ABI--------------------^   |  |
[1.28" round LCD] <--SPI--------------------------------------------------+  |
[Ring LED] <--------------------------------------------------------------+  |
[USB-C PD 5V/3A]  or  [24V DC in] --> buck 5V/3.3V --------------------------+
WiFi/BLE --> MQTT (hub) / Matter over WiFi
```

**Engineering gap:** wall-grade motor acoustics and thermal design; a 60 mm box mount that survives installers; EU power input (24 V) and USB-C PD negotiation; an entity model for haptic profiles pushed from the hub; Matter commissioning; and an EMC-clean motor drive next to the radio.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| ESP32-S3-WROOM-1 (8 MB flash, PSRAM) | €3 | Multi-source distributors |
| Gimbal BLDC motor (e.g. 2804/2805-class, hollow shaft optional) | €7–9 | Cottage suppliers; qualify two |
| Magnetic encoder (MT6701/AS5600-class) + diametric magnet | €1.5 | Multi-source |
| 3-phase gate driver / integrated FOC driver (TMC6300-class) | €2.5 | Check lead time; second source via discrete driver |
| 1.28" 240×240 round IPS LCD (GC9A01-class) | €6 | Many Shenzhen panel houses |
| USB-C PD sink controller + 24 V buck | €2.5 | |
| 4-layer PCB, round 50 mm | €1.8 | |
| Knob cap (aluminium or PC), body, mount ring, claws | €4.2 at 5k | Tooling €25k; cap finish drives perceived value |

### Firmware/software starting point

- The upstream open-source SmartKnob firmware (ESP32, SimpleFOC-based haptics, LVGL UI) — search GitHub for "smartknob"; it is the de-facto reference.
- SimpleFOC (Arduino/ESP-IDF FOC library) for motor control.
- LVGL for the round UI; ESP-IDF for production.
- ESPHome (many knob builds use its Home Assistant integration) and Home Assistant MQTT discovery for the entity model.
- Matter: Espressif's ESP-Matter SDK (connectedhomeip-based) — budget real time for it.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | 30-second haptic-thermostat demo video (hand-built from the open design) posted to 4 communities with a €149 waitlist. ≥500 sign-ups in 2 weeks = go; <200 = stop or pivot to the Dial SKU only. |
| 3–5 | Works-like | 5 units on own-assembled open PCBs; three haptic profiles switchable from Home Assistant via MQTT; motor noise measured at 30 cm (target <30 dBA idle, <40 dBA while turning); surface temp <45 °C after 1 h of hold torque. |
| 6–8 | Looks-like + EVT | Own PCB v1 (S3 + driver + PD + 24 V), SLA cap/body/mount in a real 60 mm box, 30 beta units to community members; EMC pre-scan with the motor running. |
| 9–10 | DVT + pre-compliance | PCB v2 with EMC fixes, tooled-part samples, RED pre-test, EN 18031 checklist (secure boot, signed OTA, no default passwords), battery-free safety review (EN 62368-1). |
| 11–12 | Pilot batch | 50 units from a CM with motor calibration jig; golden sample; crowdfunding page live with certified-design date; beta NPS ≥50. |

### Certification checklist (EU)

- **CE / RED:** EN 300 328 (WiFi/BLE), EN 301 489-1/-17 (EMC), EN 62311 (RF exposure), EN 62368-1 (safety — 24 V/USB-C, no mains). Motor PWM makes EN 301 489 the hard one.
- **RED delegated act — EN 18031-1/-2 (and -3 if you ever add payment, you won't):** applies, it is internet-connected. Self-declaration is possible if you meet the harmonised standard fully; otherwise notified body.
- **CRA:** reporting duties in force since September 2026; full obligations December 2027. Signed firmware, SBOM, disclosure policy, 5-year update commitment.
- **RoHS, REACH, WEEE** registration per country; packaging registration (DE LUCID).
- **Battery regulation:** not applicable (no battery) — keep it that way.
- **Matter certification** (CSA membership + ATL testing) if you claim the Matter logo — separate budget €15–25k; skip for v1.
- **GDPR:** no personal data on device; the hub does the rest. State it.
- **Estimated test costs:** RED radio + EMC €12–18k (module pre-certification helps the radio part, not the EMC with motor), safety €4k, EN 18031 €15–25k, documentation €3k. Budget **€45k**.

### Validation toolkit

- **Kill question:** does the demo video convert to ≥500 waitlist sign-ups at a stated €149 within 2 weeks? **Cheapest experiment:** build one knob from the open smartknob design (~€120 in parts), film it switching haptic profiles while a Home Assistant dashboard follows, post, count. Under €300 and 10 days.
- **5-question interview (hub owner / installer):** 1) Which setpoint do you touch most often, and how? 2) What do the other people in your home do when they want it warmer? 3) Have you bought a wall control before — which, and why did it disappoint? 4) Would you accept a USB-C cable to the wall, or does it have to be in the box? 5) At €149, what would stop you ordering today?
- **Landing page:** headline "The thermostat dial your smart home forgot." Bullets: "Real motorised haptics — detents and stops change with what you control"; "Local first: MQTT and Matter, works with your hub, no cloud"; "Fits a standard 60 mm wall box, USB-C or 24 V".
- **Pass threshold:** 500 waitlist in 2 weeks, then 300 paid pre-orders at €149 (€30 deposit) in the first campaign week.

### First production checklist

- Samples: 5 works-like, 30 beta, 50 pilot; keep motor serials — feel varies per motor batch.
- Golden sample: haptic-profile test on a jig (torque ripple, detent count), noise and temp numbers signed.
- DFM review: knob-to-motor coupling tolerance, encoder-magnet gap (±0.2 mm), claw mount strength, cap finish (anodising scratches).
- MOQ talk: motor 1k, LCD 1k, PCBA 500, tooling at 1k shots minimum.
- QC/AQL: level II, AQL 1.0/2.5; 100% motor calibration + encoder zero + WiFi test; 5% noise check.
- Packaging: retail box with a window (people buy the feel — show the knob), mount kit, QR to the hub guide.
- Incoterms: FOB Shenzhen; no batteries so no DG paperwork.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Dial (K130)](/db/m5stack-dial.html) (non-haptic cheaper SKU running the same firmware); [M5Stack Unit BLDC Driver (U181)](/db/m5stack-unit-bldc-driver.html) (motor-driver reference if you re-spin). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [[已验证]smartknob-original](/db/oshwhub-smartknob-original.html) (verified open clone: BLDC + magnetic encoder + round LCD); [Super Dial 电机旋钮屏—esp32s3—v2](/db/oshwhub-a2fff3c71f5d4de2b899c64b152d3da5.html) ('Super Dial' ESP32-S3 motor-knob v2, open).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Dial (K130), M5Stack Unit BLDC Driver (U181) — for a HaptiKnob — Haptic Setpoint Knob

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a HaptiKnob — Haptic Setpoint Knob: A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub. The design is built around your M5Stack Dial (K130), M5Stack Unit BLDC Driver (U181).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Dial (K130), M5Stack Unit BLDC Driver (U181).
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
主题：样品订购及批量报价 — M5Stack Dial (K130), M5Stack Unit BLDC Driver (U181) — 用于HaptiKnob — Haptic Setpoint Knob

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款HaptiKnob — Haptic Setpoint Knob：A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub。产品设计基于贵司的M5Stack Dial (K130), M5Stack Unit BLDC Driver (U181)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Dial (K130), M5Stack Unit BLDC Driver (U181)。
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
Subject: PCBA quote from open design files — HaptiKnob — Haptic Setpoint Knob, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a HaptiKnob — Haptic Setpoint Knob: A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub. The design starts from published open-hardware files ([已验证]smartknob-original, Super Dial 电机旋钮屏—esp32s3—v2; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — HaptiKnob — Haptic Setpoint Knob，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款HaptiKnob — Haptic Setpoint Knob：A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub。设计基于已公开的开源硬件文件（[已验证]smartknob-original, Super Dial 电机旋钮屏—esp32s3—v2；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order the parts for one open-design haptic knob (ESP32-S3 board, gimbal motor, encoder, round LCD, driver) and the M5Stack Dial; build the demo unit.
2. Write the three haptic-profile demos (thermostat / dimmer / volume) and film the 30-second video; set up the €149 waitlist page.
3. Call two smart-home installers and ask the five questions — especially whether 24 V in the box or USB-C is acceptable.

Want help sourcing or building this? Talk to us via www.gongbans.com.
