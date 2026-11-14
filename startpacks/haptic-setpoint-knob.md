# HaptiKnob — Haptic Setpoint Knob — Founder Start Pack

> A wall-mounted motorised knob with a round screen that feels like a thermostat — detents, end-stops, resistance — and controls your heat pump, lights or speakers through your local home-automation hub.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Smart homes replaced the thermostat dial with a phone app and a wall of touchscreens. Visitors, kids and partners hate it; the heat-pump maker's own controller is worse. The open-source haptic knob proved people want a physical dial that *feels* like the thing it controls — but it is a desk toy you build yourself.
- **Customer:** Home-automation households in DE/NL/AT/Nordics running a local hub (Home Assistant, Homey, KNX, Loxone), heat-pump owners stuck with a bad UI, and the installers who fit premium smart homes and need a wall control that looks finished.
- **Product:** A 60 mm wall-box knob: BLDC motor + magnetic encoder + round LCD, USB-C or 24 V powered, with haptic profiles per entity (thermostat: fine detents 0.5 °C with soft end-stops; dimmer: smooth with a bump at 100%; volume: coarse clicks). Talks MQTT and Matter to the hub. €149–179 haptic; €79 non-haptic dial SKU on the same firmware (estimates).
- **Why now:** Two open designs exist with schematics and PCB; Chinese brands ship touchscreen dials (Aqara Touchscreen Dial V1 at €80–165) but with vibration only and locked ecosystems; nobody sells a finished *haptic* wall product in Europe with a proper EU box mount.
- **The ask:** ~€140k to first 1,000 haptic units; crowdfund/pre-order driven, with a small angel or founder cheque for tooling and certification.

## 2. Business plan

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

## 3. Start kit

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

## 4. Next steps (this week)

1. Order the parts for one open-design haptic knob (ESP32-S3 board, gimbal motor, encoder, round LCD, driver) and the M5Stack Dial; build the demo unit.
2. Write the three haptic-profile demos (thermostat / dimmer / volume) and film the 30-second video; set up the €149 waitlist page.
3. Call two smart-home installers and ask the five questions — especially whether 24 V in the box or USB-C is acceptable.

Want help sourcing or building this? Talk to us via www.gongbans.com.
