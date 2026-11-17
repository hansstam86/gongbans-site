# Presence-Led Infrared Heating Controller — Founder Start Pack

> A controller for infrared heating panels in churches, workshops, studios and bathrooms that heats only the zones where people actually are. Long-range radar sees people sitting still, so the heat doesn't cut out mid-service.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Big, rarely used spaces (churches, community halls, workshops, studios) are ruinous to heat with air heating at today's energy prices. Infrared panels heat people and surfaces, not the air, so they're the right tool, but they only pay off if they're on where people are and off where they aren't. The PIR sensors used today miss people who sit still, so the heat cuts out during the sermon, the yoga class or the choir rehearsal, and people go back to leaving everything on.
- **Customer:** Two buyers. (1) **Infrared-panel makers and their installers** who want a smart controller to bundle (OEM). (2) **Churches, parish and community halls, workshops and yoga studios** buying a retrofit kit. The building owner or parish/association board pays; visitors and staff benefit.
- **Product:** One controller per heating zone: a 24 GHz long-range presence radar (Hi-Link LD2410D, up to ~10 m, detects micro-motion and stationary people per datasheet), a Tuya WBR3 Wi-Fi + BLE module for app control and schedules, and panel switching (solid-state relay for small loads, contactor for larger ones). Pre-heat by schedule, presence hold, max-on safety timer, kWh estimate per zone. Works offline on a local schedule if Wi-Fi drops.
- **Why now:** Energy prices made heating the biggest line item for many churches and halls; congregations are shrinking but buildings aren't. Infrared panels are being installed in large numbers, and 24 GHz presence radar is now cheap enough for a per-zone controller.
- **The ask:** About €100–130k (estimate) to the first 1,000 zone controllers, ideally financed by an OEM pilot order from a panel maker plus pre-orders from church/hall networks.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will an infrared-panel maker bundle it, or 5 churches/halls buy a 3-zone kit at €399? Ask both before building.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Churches and community halls, workshops, yoga studios; infrared-panel makers wanting a smart controller.

**The problem as the pack states it:** Big, rarely used spaces (churches, community halls, workshops, studios) are ruinous to heat with air heating at today's energy prices. Infrared panels heat people and surfaces, not the air, so they're the right tool, but they only pay off if they're on where people are and off where they aren't. The PIR sensors used today miss people who sit still, so the heat cuts out during the sermon, the yoga class or the choir rehearsal, and people go back to leaving everything on.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **HaustechnikDialog (DE)** · https://www.haustechnikdialog.de/ — German heating installers and owners; hydronic balancing, heat pumps, legionella.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€99–149 per zone (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how churches and community halls, workshops, yoga studios deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about heating your hall, church or workshop last winter: who switches it on, when, and how often was it heating an empty room or cutting out with people still there?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A controller for infrared heating panels in churches, workshops, studios and bathrooms that heats only the zones where people actually are — long-range radar sees seated, still people, so the heat doesn't cut out mid-service. On a scale of one to ten, how likely would you be to buy that at €99–149 per zone (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Presence-Led Infrared Heating Controller: would you pay €99–149 per zone (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Presence-Led Infrared Heating Controller: A controller for infrared heating panels in churches, workshops, studios and bathrooms that heats only the zones where people actually are — long-range radar sees seated, still people, so the heat doesn't cut out mid-service. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €99–149 per zone (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
**The OEM route is the one that scales.** An infrared-panel maker sells panels by the dozen to installers; a "presence-smart" controller that works with their panels is a differentiator and a margin item for them. Also: EU ecodesign rules for electric local space heaters (Regulation (EU) 2015/1188) credit certain control functions, including presence detection, in the seasonal efficiency calculation. Check the details, but it's a reason panel makers care about controls.

**The direct route proves the product.** Churches and halls are the most extreme case: high ceilings, 2–6 occupied hours a week, people sitting very still for an hour. If the controller works there, it works in a workshop. The board, parish council or building committee decides; often a volunteer handles the building.

Who doesn't buy: homes with central heating (different product), and big buildings with a building-management system (they buy KNX/BACnet presence detectors through an integrator).

### Market size (estimates)
- Churches and chapels in the EU + UK + CH + NO: on the order of 100,000+ buildings in regular use (estimate; national church statistics vary). Add community/village halls, studios and workshops: assume ~400,000 candidate buildings, ~10% using or moving to infrared panels in the next 5 years → **40,000 buildings × 4 zones = 160,000 zones**.
- **TAM:** 160,000 zones × €129 ≈ **€21 M** direct retrofit, plus OEM volume (panel makers ship far more panels than that into homes and bathrooms; an OEM controller at €40–60 into, say, 500,000 panel installations a year would be **€20–30 M/yr**).
- **SAM:** DACH, Benelux, UK, Nordics (where infrared panels are common): ~50% → **~€10 M direct + OEM share**.
- **SOM (3 years):** 5,000 direct zones (€0.6 M) + 1–2 OEM partners at ~10,000 units/yr (€0.5 M/yr). Realistic but you need the OEM deal.

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| Panel makers' own controllers with presence (e.g. Herschel InfraSense, which lists presence detection and app control for its Halo emitters) | Bundled with that brand's panels | Locked to one brand; check which features ship today vs "future" |
| Zoned smart-heating systems used in churches (e.g. Genius Hub, with app zones and occupancy detection; UK church case studies exist) | Hub + per-zone devices, several hundred € per site and up | Built around wet radiators and room sensors; PIR-type occupancy |
| PIR heater controllers (patio/quartz heater controllers like Infresco P) | €100–250 | PIR misses people sitting still; designed for outdoor lamps |
| KNX/BMS presence detectors + actuators (e.g. ABB, Theben) via an integrator | €300–800 per zone installed | Integrator project; overkill for a parish hall |
| Timers / smart plugs | €15–50 | No presence; heat runs for empty halls or cuts out mid-service |
| Do nothing (heat everything, or don't heat and lose users) | €€€ or cold | The status quo the board wants to fix |

**Wedge:** **radar presence that sees still people**, brand-agnostic panel switching, zone pre-heat by schedule (the hall is warm when the choir arrives, not 20 minutes later), and a per-zone kWh estimate the treasurer can read. €399 for a 3-zone kit beats any integrator quote.

### Product & value proposition
- **Zone controller:** LD2410D radar (24 GHz FMCW, motion/micro-motion/presence, range adjustable to ~10 m, ±60°, per Hi-Link), Tuya WBR3 (Wi-Fi 4 + BLE 5.4, Realtek W701-class SoC, per Tuya's datasheet) or a Tuya-free module (see below), relay/SSR output, temperature sensor, local button + LED.
- **Switching:** small loads (one panel up to ~1 kW) via an on-board SSR or relay; anything bigger via a contactor fitted by an electrician. The Seeed Grove SSR V2 is the starting reference for the SSR drive circuit only.
- **Logic:** weekly schedule with pre-heat; presence hold (keeps heating while anyone is detected, with a configurable delay); presence-only mode for workshops; **max-on safety timer** (e.g. 4 h) and frost protection; open-door/window detection via a fast temperature drop (optional).
- **Offline first:** schedules and presence logic run locally on the controller. App, remote changes and reports need the cloud (see Tuya below).
- **Reporting:** on-time × panel wattage (entered at set-up) = kWh estimate per zone; monthly summary.

**Pricing (estimates):** €129 per zone controller (retail), 3-zone church/hall kit €399, OEM price €40–60 per unit at 5k+/yr (white-label, with the panel maker's app branding via Tuya's white-label app if they want it).

### Tuya: the cloud question (read this before choosing)
- **What Tuya gives you:** a certified Wi-Fi + BLE module, a ready-made white-label phone app, cloud, OTA and voice-assistant integrations in weeks rather than months. That's why the OEM route is fast: a panel maker can have "their" app without an app team.
- **What it costs you:** **remote control, schedules from the phone and reports depend on Tuya's cloud.** If Tuya changes terms, prices or shuts a region, your product's app features go with it. Tuya also charges licence/cloud fees per device (get the current terms in writing).
- **Data residency and GDPR:** presence data in a church or workshop can reveal when specific people are present (the sexton, the one person in the workshop). Choose Tuya's European data-centre region, sign a DPA, document the data flows, and minimise: send zone states and kWh, not raw presence timelines. Disclose it.
- **Tuya-free alternative:** the same hardware with an **ESP32-C3/C6 module** and your own firmware: local web UI, Home Assistant/ESPHome and/or Matter (Matter has thermostat and occupancy device types). More engineering, no per-device cloud fee, no third-party dependency. Many churches and municipal buyers prefer it. **Recommendation:** design the PCB with one module footprint and two SKUs (Tuya for OEM partners, Tuya-free for direct/public buyers), or pick the Tuya-free path first if you have the firmware skills.
- **Hard rule either way:** the controller must keep heating safely and on schedule with no internet at all.

### Unit economics (estimates per zone controller, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (LD2410D, WBR3 or ESP32-C3 module, SSR/relay, temp sensor, isolated AC-DC, terminals, PCB) | €19.00 | €15.00 |
| Assembly & test (radar functional, relay switching under load, Wi-Fi provisioning) | €2.50 | €1.80 |
| Enclosure (wall/ceiling, radar-transparent front) | €2.50 | €1.50 |
| Packaging + install guide | €1.00 | €0.70 |
| Freight + duty to EU | €1.00 | €0.70 |
| Certification amortised (~€25k: LVD/EN 60730, EMC, RED, EN 18031) | €25.00 | €5.00 |
| Tuya licence/cloud fee (Tuya SKU, estimate, check current terms) | €1.00 | €0.80 |
| **Landed cost** | **€52.00** | **€25.50** |
| Net price ex-VAT: direct €108 (from €129) / OEM €50 | €108 / — | €108 / €50 |
| **Gross margin** | **€56 (52%) direct** | **€82 (76%) direct / €24.50 (49%) OEM** |

At 1k units certification eats the margin; OEM only makes sense at volume, which is the point of signing a panel maker.

### Go-to-market
**First 100 customers:**
- **Church networks:** diocesan/regional church building departments and their energy advisers (many run "heat the people, not the building" programmes); church building fairs and newsletters.
- **Infrared-panel installers:** they're asked "can it sense people?" weekly. Offer them a kit price and a demo case.
- **Village/community-hall associations** and yoga/pilates studio networks.
- **Two infrared-panel makers** for the OEM conversation (go with a working demo and the ecodesign angle).

**Scale channels:** OEM bundling with panel makers, electrical wholesalers, the church building departments' preferred-supplier lists, and municipal community-building programmes.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question: OEM conversations with 3 panel makers + 5 church/hall pilot sign-ups; works-like controller on devkits in 2 buildings during the heating season |
| Q2 | Custom PCB (dual module footprint), EN 60730-style safety design; EVT 30 units in 5 buildings; Tuya white-label app or own local UI |
| Q3 | DVT; LVD/EMC/RED/EN 18031 testing; OEM pilot order (200 units) if a panel maker commits |
| Q4 | 1,000 units before the heating season; installer programme; case studies with measured kWh savings |

**Team:** founder (OEM + church/hall sales), 1 embedded engineer (radar, mains switching, safety logic), part-time power-electronics/safety engineer (EN 60730 design review), part-time app/firmware integrator (Tuya or ESPHome/Matter).

**Funding to the first 1,000 units (estimates):** NRE €50k (electronics + safety design €18k, firmware €20k, app/white-label €5k, enclosure €7k) + certification €25k + 1,000 units landed ex-cert ~€27k + 9 months lean costs €30k ≈ **€132k**; minus pre-orders/OEM pilot deposit (say €25k) → **~€105k**. Route: OEM pilot order with a deposit, church/hall pre-orders, regional energy-efficiency innovation grants; angel if the OEM deal needs stock financing.

### Top risks
| Risk | Mitigation |
|---|---|
| **Safety: mains switching of heaters, fire risk if a panel stays on** | Max-on timer and over-temperature cut-off in hardware, not just firmware; relay/SSR derating; EN 60730 design; contactor for big loads, electrician installs |
| **Technical: radar in tall rooms (6–15 m ceilings) and big pews** | Wall-mount at 2–3 m aimed at the seating zone; one controller per zone; site-survey guide; test in 3 real churches before tooling |
| **Technical: radar false presence from moving panels' air/heat, curtains, fans** | Zone tuning via BLE set-up (LD2410D-B variant); presence hold logic with confirmation |
| **Cloud dependency (Tuya)** | Local-first logic; Tuya-free SKU; contract terms on data region and service continuity |
| **GDPR / data residency** | EU region, DPA, data minimisation, disclosure notice for buildings |
| **Market: panel makers build their own** | Move fast with one OEM; offer white-label so they don't have to |
| **Supply: LD2410D and Tuya module sole-source** | Radar protocol abstraction; dual module footprint (Tuya / ESP32) |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD2410D / LD2410D-B long-range presence radar | https://www.gongbans.com/db/hilink-ld2410d.html | 24 GHz presence incl. micro-motion; range adjustable ~10 m; ±60°; UART + GPIO; D-B adds BLE for set-up | Datasheet public; schematics/files via maker (contact Hi-Link) | Commercial module, no open design files |
| Tuya WBR3 Wi-Fi + BLE module | https://www.gongbans.com/db/tuya-wbr3.html | Certified Wi-Fi 4 + BLE 5.4 module (W701-VA2-CG, 2 MB flash, 16 pins, 16×24 mm per Tuya) with Tuya app/cloud | Datasheet public (Tuya developer docs); design files via maker | Requires a Tuya developer account and Tuya's commercial terms; app features depend on Tuya cloud |
| Seeed Grove-Solid State Relay V2 | https://www.gongbans.com/db/seeed-grove-solid-state-relay-v2.html | Reference for the SSR drive circuit (small loads); bigger loads via contactor | Schematic | Seeed open hardware licence; check the licence file before copying |

### Block diagram
```
[LD2410D radar] --UART--> [Wi-Fi/BLE module: Tuya WBR3  OR  ESP32-C3/C6 (Tuya-free)]
[temp sensor]  --I2C-->            |  local schedule + presence logic + max-on timer
[button/LED]                       |
                                   |--GPIO--> [SSR / relay driver] --> [IR panel ≤1 kW] or --> [contactor coil] --> [IR panels, zone]
                                   |--[hardware over-temp / watchdog cut-off]
[230 V] -> [isolated AC-DC 5 W] -> 3.3/5 V
                                   `~~ Wi-Fi ~~> [Tuya cloud + white-label app]  OR  [local web UI / Home Assistant / Matter]
```
**Engineering gap:** heater-safe switching design (derating, thermal design of the SSR, hardware cut-off independent of firmware), radar tuning for tall rooms and still audiences, schedule + pre-heat + presence logic that runs fully offline, the Tuya data-point model (or ESPHome/Matter endpoints), and an installer-friendly set-up flow.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD2410D(-B) radar | €2.50–3.50 | Sole source (Hi-Link) |
| Tuya WBR3 module (or ESP32-C3 module) | €2.00–2.50 | Tuya SKU needs Tuya account + licence; ESP32 SKU needs own firmware |
| SSR (zero-cross, 2–5 A) + heatsink, or 16 A relay | €3.00–5.00 | Derate heavily; heaters run for hours |
| Isolated AC-DC 3–5 W (e.g. Hi-Link 5 W class) | €2.00 | Choose a module with CE/safety reports |
| Temperature sensor + thermal fuse/over-temp cut-off | €1.00 | Hardware safety independent of MCU |
| Terminals, fuse, varistor, PCB, button, LED | €3.00 | |
| Enclosure (radar-transparent front) | €2.50 | ABS/PC; no metallic paint in front of the radar |

### Firmware/software starting point
- **Tuya SKU:** Tuya's device SDK and the developer platform (search Tuya developer docs for "TuyaOS" and "WBR3"); define data points (zone on/off, mode, schedule, presence, kWh).
- **Tuya-free SKU:** ESP-IDF or ESPHome on ESP32-C3/C6; ESPHome has community support for the LD2410 radar family (search "ESPHome ld2410"), and a "climate" component for thermostat logic; or Espressif's esp-matter SDK for a Matter thermostat.
- **Radar:** Hi-Link's serial protocol from the LD2410D user manual; Hi-Link's BLE configuration tool for the D-B variant (search Hi-Link's download centre).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** pitch to 3 panel makers + 5 churches/halls with a slide and a 2-minute radar demo video. Pass: one panel maker agrees to a 20-unit pilot or 5 buildings commit to a €399 kit pre-order |
| 3–5 | Works-like | LD2410D + ESP32/WBR3 devkit + SSR driving one real panel; presence held for a seated person at 6 m for 60 min with zero drop-outs; offline schedule works with Wi-Fi off |
| 6–8 | Looks-like + EVT | Custom PCB with safety cut-off, enclosure; 20 controllers in 4 buildings for 4 weeks; heating hours down vs prior weeks with no "cold mid-service" complaints |
| 9–10 | DVT + pre-compliance | EN 60730/LVD pre-assessment (temperature rise of SSR/terminals at full load for 8 h), EMC conducted/radiated pre-scan, RED pre-scan, EN 18031 gap analysis |
| 11–12 | Pilot batch | 50 units installed; measured kWh savings in at least 3 buildings; OEM pilot order or 30 kit orders |

### Certification checklist (EU)
- **LVD (2014/35/EU) / safety:** mains switching of heaters → EN 60730-1 (+ EN 60730-2-9 for temperature-sensing controls) for the controller; creepage/clearance, glow-wire, temperature rise. As a radio device it's under RED, which covers the LVD safety objectives. Est. **€6–10k**.
- **EMC:** EN 301 489-1/-3/-17 (radio), plus emissions of the switching stage (zero-cross SSR helps); EN 55014 class. Est. **€4–6k**.
- **CE under RED:** 24 GHz radar (EN 300 440), 2.4 GHz Wi-Fi/BLE (EN 300 328; reuse the module's reports), RF exposure. Est. **€5–8k**.
- **RED delegated act cybersecurity EN 18031-1 and -2** (internet-connected; presence data is personal data). Est. **€6–10k**. With Tuya: get Tuya's security documentation for your technical file.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: OTA updates, SBOM, vulnerability handling, support period. With Tuya, document who is responsible for which component.
- **Ecodesign (EU) 2015/1188** for local space heaters: applies to the heater; as an OEM supplier, give panel makers the control-function documentation they need.
- **RoHS, REACH, WEEE, packaging registration.**
- **GDPR:** presence data in non-domestic buildings; EU data region, DPA with Tuya (or self-host), disclosure notice, minimisation.
- **Total estimate: €21–34k.**

### Validation toolkit
- **Kill question:** Will an infrared-panel maker bundle it, or 5 churches/halls buy a 3-zone kit at €399? Ask both before building.
- **Cheapest experiment (~€100):** an LD2410D + ESP32 devkit logging presence in one church service and one yoga class. Overlay with when a PIR would have timed out. The chart ("PIR would have switched off the heat 4 times during the service") is your pitch.
- **5-question interview (church building committee / hall manager):**
  1. What did heating cost last winter, and how many hours a week is the building actually used?
  2. How is the heating switched today? Who comes early to turn it on?
  3. Have you tried timers or motion sensors? What went wrong?
  4. Who decides on a €400 purchase, and what proof do they need?
  5. Would you be OK with the app relying on a Chinese IoT cloud, or do you need local-only?
- **Interview (panel maker):** which controllers do installers ask for; what do you bundle today; what does an app cost you; does presence control help your ecodesign numbers; what price per unit at what volume?
- **Landing-page headline:** "Heat the people, not the empty church."
  - Radar sees people sitting still: no more cold mid-service.
  - Pre-heats before the service, switches off when the last person leaves.
  - Works offline. Shows kWh per zone.
- **Pass threshold:** one panel maker signs a pilot (20+ units, paid) **or** 5 buildings pre-order kits within 6 weeks.

### First production checklist
- **Samples:** SSR/relay temperature rise at full rated load for 8 h; radar samples from the production lot tested at 6 m seated.
- **Golden sample:** controller with measured thermal profile, cut-off test, radar sensitivity settings, module firmware version (Tuya PID/firmware key or own build hash).
- **DFM review:** creepage/clearance on the PCB, terminal torque, heat-sinking, radar window, wall/ceiling mount.
- **MOQ talk:** radar modules, Tuya module (Tuya may require registered product IDs and licence quantities), SSRs.
- **QC/AQL:** AQL II 0.65 for safety (hi-pot 100%, earth continuity if applicable, relay/SSR function under load), 1.0/2.5 cosmetic; 100% radar functional and Wi-Fi provisioning test.
- **Packaging:** controller, mounting kit, installer guide (wiring, contactor sizing, zone placement), privacy notice for the building.
- **Incoterms:** FCA Shenzhen; ship by September for the heating season.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and Tuya Smart (涂鸦智能) and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth)](/db/hilink-ld2410d.html) (long-range 24 GHz presence radar). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Tuya Smart (涂鸦智能)** (涂鸦智能模组部门, developer.tuya.com) — platform + module maker; 151 boards in the catalogue; files via Tuya Smart public module documentation · https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber. Directory entry: WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side. Boards used here: [Tuya WBR3 Wi-Fi + Bluetooth LE module](/db/tuya-wbr3.html) (Wi-Fi + BLE module for the app and schedules). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Solid State Relay V2](/db/seeed-grove-solid-state-relay-v2.html) (panel switching reference (via contactor for larger loads)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and Tuya Smart (涂鸦智能) and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2 — for a Presence-Led Infrared Heating Controller

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Presence-Led Infrared Heating Controller: A controller for infrared heating panels in churches, workshops, studios and bathrooms that heats only the zones where people actually are — long-range radar sees seated, still people, so the heat doesn't cut out mid-service. The design is built around your HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2.
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
主题：样品订购及批量报价 — HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2 — 用于Presence-Led Infrared Heating Controller

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Presence-Led Infrared Heating Controller：A controller for infrared heating panels in churches, workshops, studios and bathrooms that heats only the zones where people actually are — long-range radar sees seated, still people, so the heat doesn't cut out mid-service。产品设计基于贵司的HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2。
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
Subject: PCBA quote from open design files — Presence-Led Infrared Heating Controller, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Presence-Led Infrared Heating Controller: A controller for infrared heating panels in churches, workshops, studios and bathrooms that heats only the zones where people actually are — long-range radar sees seated, still people, so the heat doesn't cut out mid-service. The design starts from published open-hardware files (HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Presence-Led Infrared Heating Controller，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Presence-Led Infrared Heating Controller：A controller for infrared heating panels in churches, workshops, studios and bathrooms that heats only the zones where people actually are — long-range radar sees seated, still people, so the heat doesn't cut out mid-service。设计基于已公开的开源硬件文件（HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), Tuya WBR3 Wi-Fi + Bluetooth LE module, Seeed Grove-Solid State Relay V2；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Book calls with 3 infrared-panel makers and 2 regional church building departments; send the "PIR vs radar" one-pager first.
2. Order 3 LD2410D-B modules, an ESP32-C3 devkit and a WBR3 sample; log presence during one real service or class.
3. Decide Tuya vs Tuya-free for the first SKU: list per-device Tuya fees and data-region terms vs the extra firmware weeks.

Want help sourcing or building this? Talk to us via www.gongbans.com.
