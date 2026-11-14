# Modbus Pocket Analyser — Founder Start Pack

> A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop on the boiler-room floor.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Commissioning and fault-finding Modbus RTU devices (heat pumps, PV inverters, energy meters, BMS controllers) means a laptop, a USB-RS485 dongle, a driver that doesn't install, and a spreadsheet of register maps. Handheld protocol analysers that do this exist at ~£1,700–2,000 ([Lineeye LE-3500XR](https://thedebugstore.com/products/lineeye-le-3500xr-v2-e-multi-protocol-serial-analyser-uk)).
- **Customer:** HVAC and solar service technicians, building-automation integrators, maintenance departments across the EU — the installed base of heat pumps alone is ~25–28 M units ([EHPA](https://ehpa.org/news-and-resources/press-releases/heat-pump-sales-14-times-greater-in-lead-countries/)). The company pays; the technician carries it.
- **Product:** A €199–279 pocket tool: isolated RS485, keyboard + screen, auto-baud and ID scan, register profiles for the top 50 devices, SD logging, BLE link to a phone for reports.
- **Why now:** The Modbus installed base in homes exploded with heat pumps and PV; the catalogue has a keyboard handheld (Cardputer), an isolated RS485 unit, and an open rechargeable Bluetooth-to-RS485 test box to build from.
- **The ask:** ~€75k (estimate) to 1,000 units. Route: pre-orders from installer communities + bootstrap; a distributor's prepayment or a wholesaler listing replaces an angel.

## 2. Business plan

### Problem & customer
The user is a service technician who does 4–6 site visits a day. The buyer is the service manager of a 5–50-technician HVAC/solar company, or the technician himself if self-employed. Building-automation integrators (BACnet/Modbus gateways, meters) are the second group; maintenance teams in industry and property management the third. Pain is concrete: 20–40 minutes per visit lost to laptop faff; "no fault found" visits because the register map was wrong; no log to show the manufacturer when claiming warranty.

### Market size (estimates)
- Heat-pump installed base ~25–28 M in Europe (EHPA, 2024–2025), PV systems ~tens of millions, plus meters and BMS. Technicians: assume **~400k field technicians in EU + UK** touching Modbus devices (estimate from installer counts; no published figure).
- **TAM:** 400k × €249 ≈ **€100 M** (one per technician).
- **SAM:** technicians at companies that already pay for tools in this class (clamp meters, refrigerant analysers) and who hit Modbus weekly — 25% → 100k → **€25 M**.
- **SOM (3 years):** 4% → 4,000 units → **€1 M**, plus profile-pack and accessory sales.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Handheld multi-protocol serial analysers (~£1,670–2,000; [Lineeye](https://thedebugstore.com/products/lineeye-le-3500xr-v2-e-multi-protocol-serial-analyser-uk)) | Lab-grade, decodes everything | Price; no device profiles; built for engineers, not installers |
| Laptop + USB-RS485 + free poll software (Modbus poll/scan tools exist as Windows utilities) | The status quo | Laptop on the floor, drivers, no register maps, no log of the visit |
| Manufacturer service tools/apps (per brand) | Free with the brand | One brand each; technicians carry 5 brands |
| Phone + BLE-RS485 dongle apps | €40–80 dongle | Phone UI, no isolation, no keyboard, dies in the cold |
| Bench protocol analysers / PC software (~€100–300) | Good decoding | Not a handheld |
| "Do nothing" (guess, call the hotline) | Free | Lost hours, repeat visits |

**Wedge:** price (1/7 of a lab analyser), **profiles** (plug in, pick "heat pump brand X", see COP, flow temp, error code in plain language), auto-baud/ID scan, isolation that survives wiring mistakes, and a visit log on SD that the office can attach to the job. Source on tool landscape: [RS485 analysers for industrial automation](https://industrialmonitordirect.com/blogs/knowledgebase/rs485-protocol-analyzers-and-testers-for-industrial-automation).

### Product & value proposition
Hardware: Cardputer-class handheld (ESP32-S3, 1.14" screen, QWERTY keyboard), isolated RS485 front-end with surge protection and A/B swap detection, bus-activity LEDs, line-voltage check (A/B/idle), microSD, BLE/WiFi, 1,200 mAh Li-ion, rubber boot, 2-pin + screw terminal + RJ45 pigtail adapters. Firmware: passive sniff mode (decode traffic, CRC error counter), master mode (auto-baud 1200–115200, parity sweep, ID scan 1–247), register read/write with profile decoding, profile packs updatable from SD or phone, visit log (CSV + annotated), screenshot to SD. Phone app: profile updates, report export (PDF), OTA.

Pricing (estimates): **€249 B2C/direct** (rubber boot, adapters, 32 GB SD), €279 with pro profile pack, €199 launch pre-order. B2B wholesale at 30% off to electrical/HVAC wholesalers. Profile packs: free for the top 50, €49/year "all brands + updates" optional.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32-S3 module, 1.14" LCD, keyboard switches/dome sheet, isolated RS485 transceiver + isolated DC-DC, TVS, SD slot, Li-ion 1,200 mAh, charger, PCB) | €34.00 | €27.50 |
| Assembly & test (SMT, keyboard assembly, RS485 loopback + isolation test) | €6.00 | €4.20 |
| Enclosure (2-shell PC, keycaps/dome sheet, rubber boot, tooling amortised) | €7.50 | €4.60 |
| Packaging (box, adapters, pigtail, SD) | €4.20 | €3.10 |
| Freight + duty to EU | €2.80 | €1.60 |
| Certification amortised (~€32k: RED, EMC, 62368-1, UN 38.3, EN 18031) | €32.00 | €6.40 |
| **Landed cost** | **€86.50** | **€47.40** |
| Sell price (direct €249 / wholesale €174) | €249 | €174 |
| **Gross margin** | **€162.50 (65%)** | **€126.60 (73% at wholesale)** |

A proper tool margin. The risk isn't margin; it's building enough credible profiles.

### Go-to-market
**First 100 customers:** shadow 3 technicians for a day each (kill question), then installer communities: heat-pump and PV installer forums and Facebook/WhatsApp groups (DE, NL, UK, FR are active), trade-school instructors, the service managers of 10 regional HVAC/solar companies; trade fairs (ISH, Intersolar, Chillventa, national installer days). Ten review units to YouTube installer channels.

**Scale channels:** electrical and HVAC wholesalers (they own the technician's van stock), heat-pump and inverter manufacturers' service networks (co-branded profile packs), tool distributors.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Works-like on Cardputer + RS485-ISO unit; sniff + scan + 10 profiles; 3 shadow days; 50 pre-orders. |
| Q2 | Custom PCB (own isolated front-end, better battery), tooled case with boot; 50 profiles; EVT 50; pre-compliance. |
| Q3 | DVT, certification, 300-unit pilot to pre-order customers; phone app beta; wholesaler talk. |
| Q4 | 1,000 units; profile-pack subscription; 2 manufacturer co-brands. |

**Team:** 1 embedded engineer (ESP32-S3, RS485, Modbus — full-time), 1 firmware/app developer (UI, profiles, app — full-time from Q2), founder with HVAC/solar network for profiles and sales; mechanical and compliance bought in. Profiles need a technician adviser paid per profile (€200 each is cheap).

**Funding to first 1,000 units (estimates):** NRE €50k (PCB spins €10k, tooling €18k, keyboard tooling €6k, app €10k, profiles €6k) + certification €32k + 1,000 units landed ~€55k + 9 months lean overhead €70k ≈ **€207k**; minus pre-orders (300 × €199 ≈ €60k) and pilot sales (~€70k) ≈ **~€75k**. Bootstrap + pre-orders; a wholesaler prepayment for 500 units would close the gap without equity.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** real buses are ugly (wrong termination, mixed baud, 24 V on the wrong pin) | Isolated front-end with ±60 V tolerance, TVS, polarity auto-detect, line-voltage display; test on 20 real installations before EVT |
| **Technical:** profiles are wrong or outdated | Community-contributed profiles with versioning; manufacturer co-validation; "raw register" mode always available |
| **Market:** technicians don't buy tools themselves; managers don't see the pain | Sell the visit log to managers (fewer repeat visits); sell the time saved to the technician; demo at wholesalers' counters |
| **Regulatory:** BLE/WiFi → RED + EN 18031; CRA | Pre-certified module; keep WiFi for OTA only; budget EN 18031 from day one |
| **Supply:** keyboards are custom and fiddly; LCD models change | Use a dome-sheet + silicone keypad design you own; second-source the LCD by panel size |
| **Licence:** the open RS485 test box is an OSHWHub project | Read the licence; use as reference for the front-end and redraw your own board |

## 3. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Cardputer (K132) | https://www.gongbans.com/db/m5stack-cardputer.html | Keyboard + screen + ESP32-S3 handheld: the works-like prototype in one buy | enclosure/structure only | Buy; electronics not published — your own PCB later |
| M5Stack Unit RS485-ISO (U094) | https://www.gongbans.com/db/m5stack-unit-rs485-iso.html | Isolated RS485 front-end for the prototype | enclosure/structure only | Buy |
| Rechargeable Bluetooth-to-RS485 test box (OSHWHub) | https://www.gongbans.com/db/oshwhub-lan-ya-xu-ni-chuan-kou-diao-shi-qi-copy.html | Open schematic + PCB of a battery BLE-RS485 tester: reference for the front-end and power | schematic, pcb (EasyEDA) | **OSHWHub licence varies — read it; redraw your own board** |
| M5Stack Station-485 (K123) | https://www.gongbans.com/db/m5stack-station-485.html | Multi-port RS485 station reference for a bench/desk variant | enclosure/structure only | Buy |

### Block diagram
```
RS485 bus (A/B/GND) -> [TVS, PTC] -> [isolated RS485 transceiver] -> [isolated DC-DC] -> [ESP32-S3]
                        [line-voltage ADC via isolation]                                    |-> [1.14" LCD] [QWERTY keypad] [LEDs]
                                                                                             |-> [microSD log] [BLE/WiFi -> phone app]
                                                                                             |-> [Li-ion 1,200 mAh, USB-C charge]
```
**Engineering gap:** the Cardputer gives you the form factor; the RS485-ISO unit gives isolation. Missing: a robust front-end (surge, polarity, line check), auto-baud/ID scan logic, the profile system and its content (the real moat), a ruggedised case with a sealed keypad, and the app. Content and firmware dominate.

### Starter BOM (estimates per unit at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 module (N16R8-class, PSRAM for UI) | €3.20 | Pre-certified |
| 1.14"–1.9" IPS LCD, SPI | €3.50 | Second-source by size |
| Keypad: dome sheet + silicone keys + PCB pads | €4.50 | **Custom tooling €5–8k**; the fiddly part |
| Isolated RS485 transceiver (integrated isolation) | €3.80 | Two vendors make pin-compatible parts |
| Isolated DC-DC 5 V 1 W | €1.50 | |
| TVS/PTC/polarity detect, line-voltage ADC path | €1.20 | |
| microSD slot + 32 GB card | €3.20 | |
| Li-ion 1,200 mAh + PCM + charger | €3.30 | UN 38.3 from cell vendor |
| PCB 4-layer, passives, USB-C | €4.00 | |
| Case 2-shell + rubber boot + screw-terminal adapter + RJ45 pigtail | €7.50 | **Tooling €12–18k** |

### Firmware/software starting point
- Cardputer: M5Stack's M5Cardputer Arduino library exists; the community firmware "M5Launcher" and various Cardputer apps on GitHub show the UI patterns.
- Modbus: libmodbus (C, exists) or the Arduino "ModbusMaster"/"eModbus" libraries for ESP32 (search). Sniffing requires your own UART frame-timing code (3.5-char gaps) — a few hundred lines.
- Profiles: define a JSON/YAML register-map format; seed it from public register documentation of heat-pump, inverter and meter manufacturers (many publish Modbus maps as PDFs). Home Assistant's community Modbus integrations are a useful public reference for which registers matter (search "Home Assistant modbus heat pump").
- App: BLE file transfer + PDF export; or start with SD card + a web page.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Cardputer + RS485-ISO sniffing and scanning a real heat pump and a meter; **3 shadow days with technicians: do they say they'd carry it instead of the laptop — and pay €249?** |
| 3–5 | Works-like | Auto-baud + ID scan reliable on 10 real devices; 10 profiles decode live values; SD visit log; 8 h battery |
| 6–8 | Looks-like + EVT | Own PCB with isolated front-end; printed case with boot; 30 units to technicians; surge test (±2 kV) and polarity-reversal survive; EMC pre-scan |
| 9–10 | DVT + pre-compliance | 50 profiles validated by technicians; RED/EMC pre-compliance; EN 18031 self-assessment; drop test 1.5 m; −10 °C operation |
| 11–12 | Pilot batch | 50 units to pre-order customers; ≥ 80% still in daily use after 4 weeks; profile bug rate measured and fixed via OTA |

### Certification checklist (EU)
- **CE under RED:** EN 300 328, EN 301 489-1/-17, EN 62311; **EN IEC 62368-1** (battery, user-accessible terminals; the RS485 port should be rated and isolated — document the isolation voltage); **EN 18031-1** (internet-connected via WiFi/app, mandatory since 1 Aug 2025; -2 only if personal data). Est. €6–9k RED/EMC, €3–5k safety, €10–18k EN 18031.
- EMC for a measurement instrument: consider EN IEC 61326-1 (industrial immunity) alongside EN 55032/55035 — buyers ask.
- **RoHS, REACH, WEEE; Battery Regulation (EU) 2023/1542 + UN 38.3**; design the cell as technician-replaceable.
- **CRA:** reporting from 11 Sept 2026, full 11 Dec 2027: signed firmware, OTA, SBOM, vulnerability contact; profile packs are "software" too.
- **GDPR:** visit logs may contain site addresses and customer names → personal data in the app; privacy notice, local-first storage.
- **Not a safety or metrology instrument**; the line-voltage check is indicative; say so. No toy, no medical.
- **Total certification budget estimate: €25–35k.**

### Validation toolkit
- **Kill question:** After one day shadowing three technicians, do they say they would carry it instead of the laptop — and pay €249?
- **Cheapest experiment (~€250):** a Cardputer + RS485-ISO unit with a 3-day firmware (sniff, scan, 3 profiles); three shadow days; a Stripe pre-order link at €199 shown at the end of each day.
- **5-question interview (technician / service manager):** 1) Walk me through the last Modbus problem you had on site — what did you use, how long did it take? 2) Which five device brands do you touch most? 3) What does your current laptop setup cost you per visit in minutes? 4) Would a pocket tool with those brands' registers decoded replace the laptop for 80% of visits? 5) €249 — your money or the company's, and who signs?
- **Landing page:** headline "Modbus in your pocket. Leave the laptop in the van." Bullets: "Auto-detects baud and slave IDs; isolated RS485 that survives wiring mistakes." / "Decodes heat pumps, inverters and meters in plain language — 50 profiles included." / "Logs every visit to SD; report to your phone. €249."
- **Pass threshold:** 3 of 3 technicians say yes, and 50 pre-orders at €199 in 6 weeks.

### First production checklist
- Samples: 5 golden samples with isolation test certificates and keypad feel signed off (keypads are what people complain about).
- DFM: keypad stack-up, SD slot accessibility, boot fit, terminal strain relief; test jig with a Modbus simulator.
- MOQ talk: LCD 1k; keypad 1k; case 1k; cells 1k; isolated transceiver reel 1k.
- QC: AQL II 2.5/4.0; 100% functional test incl. RS485 loopback at 3 baud rates and a 500 V isolation check; 100% keypad test; 2% drop sample.
- Packaging: tool box with foam, adapters, printed quick card; lithium labels.
- Incoterms: FOB Shenzhen; air for the first 300, sea after.

## 4. Next steps (this week)
1. Buy a Cardputer and a Unit RS485-ISO; flash a sniff + scan proof-of-concept against any Modbus device you can reach (a cheap energy meter works).
2. Line up three technicians (HVAC, PV, BMS) for shadow days in the next three weeks; write the observation sheet.
3. Collect the public Modbus register PDFs of the 10 most common heat-pump and inverter brands in your market and draft the profile format.

Want help sourcing or building this? Talk to us via www.gongbans.com.
