# Modbus Pocket Analyser — Founder Start Pack

> A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop on the boiler-room floor.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Commissioning and fault-finding Modbus RTU devices (heat pumps, PV inverters, energy meters, BMS controllers) means a laptop, a USB-RS485 dongle, a driver that doesn't install, and a spreadsheet of register maps. Handheld protocol analysers that do this exist at ~£1,700–2,000 ([Lineeye LE-3500XR](https://thedebugstore.com/products/lineeye-le-3500xr-v2-e-multi-protocol-serial-analyser-uk)).
- **Customer:** HVAC and solar service technicians, building-automation integrators, maintenance departments across the EU — the installed base of heat pumps alone is ~25–28 M units ([EHPA](https://ehpa.org/news-and-resources/press-releases/heat-pump-sales-14-times-greater-in-lead-countries/)). The company pays; the technician carries it.
- **Product:** A €199–279 pocket tool: isolated RS485, keyboard + screen, auto-baud and ID scan, register profiles for the top 50 devices, SD logging, BLE link to a phone for reports.
- **Why now:** The Modbus installed base in homes exploded with heat pumps and PV; the catalogue has a keyboard handheld (Cardputer), an isolated RS485 unit, and an open rechargeable Bluetooth-to-RS485 test box to build from.
- **The ask:** ~€75k (estimate) to 1,000 units. Route: pre-orders from installer communities + bootstrap; a distributor's prepayment or a wholesaler listing replaces an angel.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> After one day shadowing three technicians, do they say they would carry it instead of the laptop — and pay €249?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** HVAC and solar service technicians, building-automation integrators, maintenance departments.

**The problem as the pack states it:** Commissioning and fault-finding Modbus RTU devices (heat pumps, PV inverters, energy meters, BMS controllers) means a laptop, a USB-RS485 dongle, a driver that doesn't install, and a spreadsheet of register maps. Handheld protocol analysers that do this exist at ~£1,700–2,000 ([Lineeye LE-3500XR](https://thedebugstore.com/products/lineeye-le-3500xr-v2-e-multi-protocol-serial-analyser-uk)).

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **PLCtalk forum** · https://www.plctalk.net/ — industrial automation technicians and integrators.
- **r/PLC** · https://www.reddit.com/r/PLC/ — industrial automation engineers and integrators.
- **Control.com forum** · https://control.com/ — process-control and instrumentation engineers.
- **r/HVAC** · https://www.reddit.com/r/HVAC/ — HVAC technicians (mostly US); installer mindset.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€199–279, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how HVAC and solar service technicians, building-automation integrators, maintenance departments deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about your last Modbus commissioning problem: what tool did you use to find it, and how long did it take?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop needed. On a scale of one to ten, how likely would you be to buy that at €199–279, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Modbus Pocket Analyser: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Modbus Pocket Analyser: A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop needed. Before we spend money on tooling I want to find out whether this solves a real problem for HVAC and solar service technicians, building-automation integrators, maintenance departments.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €199–279 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

Two questions, no pitch: how do you handle this today, and what would make you say no to the above? Twenty minutes on a call this week, or a reply here, both help.
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

## 4. Start kit

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

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Cardputer (K132)](/db/m5stack-cardputer.html) (keyboard + screen + ESP32-S3 handheld for the prototype); [M5Stack Unit RS485-ISO (U094)](/db/m5stack-unit-rs485-iso.html) (isolated RS485 front-end); [M5Stack Station-485 (K123)](/db/m5stack-station-485.html) (multi-port RS485 station reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [充电式蓝牙转485通讯测试盒](/db/oshwhub-lan-ya-xu-ni-chuan-kou-diao-shi-qi-copy.html) (open rechargeable Bluetooth-to-RS485 test box).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack Cardputer (K132), M5Stack Unit RS485-ISO (U094), M5Stack Station-485 (K123) — for a Modbus Pocket Analyser

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Modbus Pocket Analyser: A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop needed. The design is built around your M5Stack Cardputer (K132), M5Stack Unit RS485-ISO (U094), M5Stack Station-485 (K123).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Cardputer (K132), M5Stack Unit RS485-ISO (U094), M5Stack Station-485 (K123).
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
主题：样品订购及批量报价 — M5Stack Cardputer (K132), M5Stack Unit RS485-ISO (U094), M5Stack Station-485 (K123) — 用于Modbus Pocket Analyser

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Modbus Pocket Analyser：A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop needed。产品设计基于贵司的M5Stack Cardputer (K132), M5Stack Unit RS485-ISO (U094), M5Stack Station-485 (K123)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Cardputer (K132), M5Stack Unit RS485-ISO (U094), M5Stack Station-485 (K123)。
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
Subject: PCBA quote from open design files — Modbus Pocket Analyser, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Modbus Pocket Analyser: A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop needed. The design starts from published open-hardware files (充电式蓝牙转485通讯测试盒; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Modbus Pocket Analyser，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Modbus Pocket Analyser：A handheld with keyboard and screen that plugs into any RS485 bus, auto-detects baud rate and slave IDs, decodes registers of common heat pumps, inverters and meters and logs to SD — no laptop needed。设计基于已公开的开源硬件文件（充电式蓝牙转485通讯测试盒；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Buy a Cardputer and a Unit RS485-ISO; flash a sniff + scan proof-of-concept against any Modbus device you can reach (a cheap energy meter works).
2. Line up three technicians (HVAC, PV, BMS) for shadow days in the next three weeks; write the observation sheet.
3. Collect the public Modbus register PDFs of the 10 most common heat-pump and inverter brands in your market and draft the profile format.

Want help sourcing or building this? Talk to us via www.gongbans.com.
