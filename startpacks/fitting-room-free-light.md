# Fitting-Room Free Light — Founder Start Pack

> A radar above each fitting room that shows a green/red light outside and tells staff how long cubicles are busy. Cameras in fitting rooms are illegal, and a drawn curtain tells you nothing.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Fitting rooms are where fashion sales are decided, and they're a black box. Customers queue in front of curtains that hide empty cubicles, staff don't know someone has been waiting 10 minutes for another size, and head office has no idea how often cubicles are used. Cameras are out (and illegal in most of Europe), and RFID-mirror systems cost a fortune.
- **Customer:** Regional fashion chains, outdoor/sports retailers and department stores in the EU. The retail operations manager buys; store staff and shoppers use it.
- **Product:** One small 24 GHz presence-radar node per cubicle (it sees a still person through the curtain, no image) drives a green/red light above the door and reports over a sub-GHz radio to a staff display/tablet. That gives "cubicle 4 busy 12 min → offer help" prompts and a weekly utilisation report. Retrofit in an evening.
- **Why now:** Presence radar that detects people standing still costs a few euros, so you're no longer stuck with PIR sensors that turn the light green while someone stands still in their underwear. Store staffing is thin, and every converted fitting-room visit counts.
- **The ask:** About €110k (estimate) to reach 1,000 cubicles (~120 stores). Route: one paid pilot with a regional chain, an angel from retail tech, and customer-funded rollouts after that.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will one regional fashion chain pilot 2 stores and show that staff respond faster (more items sold per visitor)? Need the retailer's own number, not ours.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Fashion retailers, outdoor/sports shops, department stores in the EU.

**The problem as the pack states it:** Fitting rooms are where fashion sales are decided, and they're a black box. Customers queue in front of curtains that hide empty cubicles, staff don't know someone has been waiting 10 minutes for another size, and head office has no idea how often cubicles are used. Cameras are out (and illegal in most of Europe), and RFID-mirror systems cost a fortune.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **HDE, Handelsverband Deutschland** · https://einzelhandel.de/ — German retail association; regional associations reach the shops.
- **EuroCommerce** · https://www.eurocommerce.eu/ — European retail and wholesale federation.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€69–99 per cubicle (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how fashion retailers, outdoor/sports shops, department stores in the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do your staff know which fitting rooms are free and how long people wait, and what happens on a busy Saturday?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A radar above each fitting room that shows a green/red light outside and tells staff how long cubicles are busy — because cameras in fitting rooms are illegal and curtains don't tell you anything. On a scale of one to ten, how likely would you be to buy that at €69–99 per cubicle (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Fitting-Room Free Light: would you pay €69–99 per cubicle (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Fitting-Room Free Light: A radar above each fitting room that shows a green/red light outside and tells staff how long cubicles are busy — because cameras in fitting rooms are illegal and curtains don't tell you anything. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €69–99 per cubicle (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Target: **regional and national fashion and sports chains with 20–200 stores** in DE, NL, BE, AT, the Nordics, PL and FR. They're big enough to care about conversion, but too small for the enterprise RFID/smart-mirror platforms.

- **Who pays:** the head of retail operations or store experience. Budget comes from the store-ops or loss-prevention line.
- **Who uses:** store staff (the prompt), shoppers (the light), area managers (the report).
- **Why they buy:** more items sold per fitting-room visit, shorter queues on Saturdays, and fewer "abandoned" garments, all without privacy trouble.

### Market size (estimates)
- EU clothing/footwear/sports stores with fitting rooms: roughly 300k+ stores (estimate; check Eurostat retail statistics), averaging 4–8 cubicles → ~1.5–2 M cubicles.
- **TAM:** 1.8 M cubicles × €85 ≈ **€150 M** hardware + a software subscription (€2/cubicle/month ≈ €43 M/year).
- **SAM:** chain stores (not single independents) in the target countries, ~30% → **€45 M** hardware.
- **SOM (3 years):** 2% of SAM → ~10,000 cubicles (~1,500 stores) → **~€850k** hardware + €240k/year software.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Occupancy indicator kits with PIR/door contact (e.g. SECO-LARM RM-R100 series, per [SDM coverage](https://sdmmag.com/articles/96657-seco-larm-occupancy-monitor-reduces-crowding)) | €80–200 per room | PIR misses still people (shows "free" while someone changes); door contacts don't work with curtains; no data |
| Fitting-room service/call-button platforms (e.g. Alert Technologies Smart Button, per [Retail TouchPoints](https://retailtouchpoints.com/features/solution-spotlight/solution-spotlight-alert-technologies-smart-button-streamlines-fitting-room-service)) | Project pricing | Built for US big-box; integration-heavy |
| Enterprise RFID/smart-mirror fitting-room software (e.g. Johnson Controls Fitting Room 360) | Large-chain projects | Requires item-level RFID and an enterprise rollout |
| Cameras / people counters at the fitting-room entrance | €300–1,500 | Counts entries, not cubicles; cameras near fitting rooms are a legal minefield |
| Do nothing (staff peek, "is anyone in there?") | Free | Embarrassing, slow, no data |

**Wedge:** radar presence that sees still people through curtains with **zero image data**, battery or 12 V nodes that retrofit without electricians, a light shoppers understand, and a weekly report the area manager reads. Priced per cubicle so a pilot of 2 stores is a small purchase order.

### Product & value proposition
- **Cubicle node:** Hi-Link LD2410B 24 GHz presence radar (presence and micro-motion, adjustable range including the 0.2–1.6 m mode, GPIO + UART per the brochure) mounted on the ceiling pointing down into the cubicle; a HopeRF CMT2300A sub-GHz transceiver (868 MHz) to talk to the store hub; an RGB LED light above the cubicle door (Grove Chainable RGB LED as the reference). Power: 12 V from a shared supply (the LD2410B draws ~74–80 mA on average, which is too much for a long battery life), or a long-life battery pack with radar duty-cycling as the "no-wiring" option. Test both.
- **Store hub:** sub-GHz receiver + Wi-Fi/Ethernet, driving a staff tablet/screen (or a smartwatch/wearable push via the store's existing devices): "Cubicle 4 busy 12 min → offer help", "3 people waiting, 2 cubicles free".
- **Cloud/report:** utilisation per cubicle/hour, average dwell time, peak hours, "help offered within X min" (if staff tap acknowledge). Weekly email to the area manager.
- **Privacy:** no images, no IDs, no Bluetooth/Wi-Fi sniffing of phones. Sign it at the entrance anyway ("radar occupancy sensor, no camera").

**Pricing (estimates):** €85 per cubicle node + €249 store hub; software €2/cubicle/month (reports, alerts, multi-store dashboard). A typical 6-cubicle store: €759 hardware + €144/year. Installation by the retailer's shop-fitter or our partner.

### Unit economics (estimates per cubicle node, ex-VAT)
| Item | 1k nodes | 5k nodes |
|---|---|---|
| BOM (LD2410B, CMT2300A + matching, MCU, RGB LED light bar, 12 V input/regulator, PCB) | €12.50 | €9.50 |
| Assembly & test | €2.00 | €1.40 |
| Enclosure (ceiling node + door light bar) | €3.50 | €2.00 |
| Packaging (bulk store kit) | €0.70 | €0.50 |
| Freight + duty to EU | €0.80 | €0.50 |
| Certification amortised (~€25k across node + hub: RED 24 GHz + 868 MHz + Wi-Fi, EMC, EN 18031 for the hub) | €25.00 | €5.00 |
| **Landed cost** | **€44.50** | **€18.90** |
| Net price (direct to chains) | €85 | €75 |
| **Gross margin (hardware)** | **€40.50 (48%)** | **€56.10 (75%)** |

Store hub: BOM ~€30, sold at €249. Software is nearly pure margin once the dashboard exists.

### Go-to-market
**First 100 customers (cubicles):**
- **One regional fashion chain** with 20–60 stores: a 2-store pilot (~12 cubicles) for 8 weeks with the retailer's own conversion data (items sold per fitting-room visit, POS data). The retailer's number is the only number that counts.
- **Outdoor and sports retailers** (busy weekends, expensive items, customers who try many sizes).
- **Shop-fitting companies** (they renovate fitting rooms and want a "smart fitting room" upsell).
- **Retail trade fairs** (EuroShop-type) and retail-innovation newsletters.

**Scale channels:** shop-fitters, retail-tech integrators (POS, workforce apps: push the alerts into the staff app the store already uses), and department-store groups.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: works-like nodes in 2 stores of one chain; baseline conversion data from the retailer |
| Q2 | Custom node + hub PCBs, light bar; dashboard v1; pilot results presented to the retailer's board |
| Q3 | DVT, RED/EMC/EN 18031 testing; rollout to the pilot chain (20–50 stores) |
| Q4 | 1,000 cubicles; 2 more chains; shop-fitter partnership; staff-app integration |

**Team:** 1 embedded/RF engineer (radar tuning, sub-GHz network), 1 full-stack developer (hub, dashboard, reports, integrations), the founder on retail sales (a retail-operations background is ideal). Use an installer partner for rollouts.

**Funding to the first 1,000 cubicles (estimates):** NRE €45k (two PCBs €12k, enclosures €10k, firmware €8k, dashboard/integration €15k) + certification €25k + 1,000 nodes + 150 hubs landed ~€25k + €5k + 9 months lean costs €60k ≈ **€160k**. Subtract the pilot fee + first rollout (~€50k, B2B pays 50% upfront) → **~€110k**. Route: angel from retail tech + customer prepayments. A retail-innovation grant is unlikely, so don't count on it.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: radar sees through thin walls into the next cubicle** (24 GHz passes through curtains and thin partitions) | Mount on the ceiling pointing down, use the short-range mode (0.2–1.6 m), tune gates per cubicle; measure cross-talk in week 3. Kill criterion: >2% wrong status |
| **Technical:** power (radar average ~74–80 mA makes battery nodes short-lived) | 12 V wiring as default (one supply per row of cubicles); battery variant only with radar duty-cycling and a proven ≥1-year life |
| **Labour law: staff performance monitoring** | Response-time metrics can be seen as monitoring employees. In Germany the works council has co-determination rights over technical systems that can monitor staff (BetrVG §87); other countries have similar rules. Offer a "store-level only" report mode (no per-employee data), and give the retailer a works-council information pack |
| **Privacy perception** | Visible signage, a one-page privacy explanation, no images/IDs; GDPR impact is low but explain it |
| **Market:** retailer doesn't share conversion data | Make data sharing a pilot condition; also measure queue length and dwell time yourself |
| **Supply:** radar and sub-GHz chips single-sourced | LD2410B has many clones/peers (24 GHz presence modules are a commodity); CMT2300A footprint alternatives exist |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD2410B/LD2410C 24 GHz presence radar | https://www.gongbans.com/db/hilink-ld2410b.html | Still-person presence through the curtain, adjustable range incl. 0.2–1.6 m mode, GPIO + UART | **Datasheet public, files via maker** (no open schematic/PCB) | Commercial module |
| HopeRF CMT2300A sub-GHz transceiver | https://www.gongbans.com/db/hoperf-cmt2300a.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2300A) | 868 MHz link cubicle → hub; up to +20 dBm, 8.5 mA RX, packet handler | schematic, PCB, demo code, datasheet | MIT (HopeRF repo) |
| HopeRF CMT-RF_EB evaluation board | https://www.gongbans.com/db/hoperf-cmt-rf-eb.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/Tools_Kit) | STM32 base board + CMT2300A demo code and the RFPDK config tool | schematic, firmware | MIT |
| Seeed Grove-Chainable RGB LED | https://www.gongbans.com/db/seeed-grove-chainable-rgb-led.html | Reference for the green/red light driver | schematic | Seeed wiki resources; check the licence |

3 of 4 boards publish schematics; the radar is a bought module.

### Block diagram
```
PER CUBICLE (ceiling)                                         STORE HUB (back office)
[LD2410B radar, pointing down] --GPIO/UART--> [MCU]           [CMT2300A RX/TX] -> [MCU/ESP32] -> [Wi-Fi/Ethernet] ~~> [cloud: reports]
                                               |  \                                    |
[12 V row supply] -> [regulator]   [CMT2300A 868 MHz] ~~>        [staff tablet / screen / staff-app push]
                                               |
                         [RGB light bar above the curtain: green / red / blue "help requested"]
```
**Engineering gap:** the sensing and radio parts exist. What's missing: per-cubicle radar tuning (gates and sensitivity so neighbours don't bleed through), a robust star network (acknowledged messages, 30–60 nodes per store), the hub, the staff-alert UX, the dashboard/report, and install mechanics for every type of cubicle.

### Starter BOM (estimates per node at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD2410B | €2.50–3.50 | Commodity class; several peer modules exist |
| CMT2300A + crystal + matching | €1.50 | HopeRF; schematic reference in the GitHub folder |
| MCU (small Cortex-M0+) | €0.70 | Or run on an ESP32-C3 if Wi-Fi per node is acceptable (it isn't for 60 nodes) |
| RGB LED light bar + light pipe | €2.50 | Visible from the queue |
| 12 V input, regulator, connector | €1.20 | |
| PCB + passives | €1.50 | |
| Ceiling enclosure + light-bar housing | €3.50 | Tooling ~€6–10k |
| Hub: ESP32 + CMT2300A + Ethernet option + enclosure + PSU | ~€30 | Per store |

### Firmware/software starting point
- **Radar:** LD2410 serial protocol doc from Hi-Link (gate sensitivity, distance gates); ESPHome has an LD2410 component (search "ESPHome LD2410") for fast tuning experiments.
- **Radio:** HopeRF CMT2300A demo code + RFPDK (in the GitHub folders above) for register settings.
- **Hub:** ESP-IDF; MQTT to your backend; a simple local web page for the staff view as a fallback.
- **Dashboard:** any time-series DB + web app; email reports. Integrations later via webhooks.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Pilot agreement with one regional chain (2 stores), including access to their POS conversion data; works-like nodes (LD2410B + ESP32 + LED) in 2 cubicles of a friendly store |
| 3–5 | Works-like | 12 cubicles in 2 stores running on works-like nodes + hub; status correct ≥98% (spot checks); cross-talk between cubicles ≤2%; staff alert working on a tablet |
| 6–8 | Looks-like + EVT | Custom node + hub PCBs, light bar, ceiling enclosure; 30 EVT nodes; install time ≤15 min/cubicle; 4-week pilot data |
| 9–10 | DVT + pre-compliance | RED pre-scan (24 GHz + 868 MHz + Wi-Fi hub), EMC; EN 18031 gap analysis on the hub; works-council info pack; report v1 |
| 11–12 | Pilot batch | **Kill question answered:** the retailer's own number shows faster staff response and more items sold per fitting-room visit (any measurable lift); 50 nodes paid; rollout decision |

### Certification checklist (EU)
- **CE under RED:** 24 GHz radar (module's standard per Hi-Link, e.g. EN 300 440; confirm), 868 MHz EN 300 220-1/-2 (duty cycle for status messages), hub Wi-Fi EN 300 328, EMC EN 301 489-1/-3/-17, safety EN 62368-1 (12 V SELV; buy a certified 12 V supply), exposure EN 62479. Est. **€10–16k**.
- **RED delegated act (EN 18031-1):** the store hub is internet-connected, so it's mandatory (since 1 Aug 2025). The cubicle nodes aren't directly internet-connected; document that. EN 18031-2 only if personal data is processed (avoid per-employee data). Est. **€6–12k**.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Signed hub OTA, node update path, SBOM, vulnerability contact.
- **GDPR:** occupancy without identity is low-risk, but the retailer is the controller for any staff-response data. Provide a processing agreement and a store-level-only mode. Signage at fitting rooms.
- **Labour law:** works-council/employee-representative consultation where staff metrics are used (DE: BetrVG §87; similar elsewhere). Not a certification, but it blocks rollouts if ignored.
- **RoHS, REACH, WEEE** (B2B WEEE registration), packaging registration.
- **Fire safety of ceiling-mounted devices:** use flame-retardant plastics (UL94 V-0) for shop-fitting acceptance.
- **Total certification budget estimate: €18–30k.**

### Validation toolkit
- **Kill question:** Will one regional fashion chain pilot 2 stores and show that staff respond faster (more items sold per visitor)? It has to be the retailer's own number, not ours.
- **Cheapest experiment (~€600):** 6 works-like nodes (LD2410B + ESP32 + LED strip) taped above the cubicles of one friendly store for 2 weeks, with the staff view on a cheap tablet. Compare the store manager's tally of "customer asked for help / was offered help" before and after.
- **5-question interview (retail ops manager):** 1) Do you measure fitting-room conversion today, and how? 2) What happens on a busy Saturday at the fitting rooms? 3) What did you try (call buttons, attendants, RFID)? 4) What would a pilot need to prove for a rollout decision, and whose data counts? 5) €85 per cubicle + €2/month: who signs the PO, and how long does it take?
- **Landing page headline:** "Know which fitting rooms are free, and who's waiting for help." Bullets: "A green/red light above every cubicle; radar sees through the curtain, no camera." / "Staff get a nudge when someone has been in a cubicle for 10 minutes." / "Weekly report: utilisation, dwell time, peak hours per store."
- **Pass threshold:** one chain signs a paid 2-store pilot (€2–3k) and agrees to share its POS conversion data.

### First production checklist
- **Samples:** golden node + hub with the radar configuration (gate settings) recorded; firmware frozen with the module maker.
- **DFM review:** ceiling mount for different ceilings (grid, plaster, open), light-bar visibility, cable management for 12 V rows.
- **MOQ talk:** radar modules (cheap, but check lot-to-lot consistency), LED light-bar diffuser colours, enclosure colour to match shop fittings (white/black).
- **QC/AQL:** AQL II 1.0/2.5; 100% radar presence test at 1 m, 100% radio link test with a reference hub, 100% LED colour check.
- **Packaging:** store kits (6/8/10 cubicles + hub) with installation sheet and signage stickers.
- **Incoterms:** FOB Shenzhen; B2B shipments consolidated per rollout wave; spares at 5%.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and HopeRF (华普微) and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410B/LD2410C 24 GHz human-presence radar module](/db/hilink-ld2410b.html) (24 GHz presence radar per cubicle). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver](/db/hoperf-cmt2300a.html) (sub-GHz link from each cubicle to the staff display (open schematic + PCB)); [HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003)](/db/hoperf-cmt-rf-eb.html) (radio reference board and demo code). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Chainable RGB LED](/db/seeed-grove-chainable-rgb-led.html) (free/busy light reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED — for a Fitting-Room Free Light

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Fitting-Room Free Light: A radar above each fitting room that shows a green/red light outside and tells staff how long cubicles are busy — because cameras in fitting rooms are illegal and curtains don't tell you anything. The design is built around your HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED.
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
主题：样品订购及批量报价 — HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED — 用于Fitting-Room Free Light

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fitting-Room Free Light：A radar above each fitting room that shows a green/red light outside and tells staff how long cubicles are busy — because cameras in fitting rooms are illegal and curtains don't tell you anything。产品设计基于贵司的HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED。
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
Subject: PCBA quote from open design files — Fitting-Room Free Light, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Fitting-Room Free Light: A radar above each fitting room that shows a green/red light outside and tells staff how long cubicles are busy — because cameras in fitting rooms are illegal and curtains don't tell you anything. The design starts from published open-hardware files (HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Fitting-Room Free Light，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fitting-Room Free Light：A radar above each fitting room that shows a green/red light outside and tells staff how long cubicles are busy — because cameras in fitting rooms are illegal and curtains don't tell you anything。设计基于已公开的开源硬件文件（HLK-LD2410B/LD2410C 24 GHz human-presence radar module, HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Seeed Grove-Chainable RGB LED；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 6× LD2410B, 6× ESP32 boards and an LED strip; test cross-talk between two cubicles made from cardboard and a curtain.
2. Interview 5 retail operations managers at regional chains (LinkedIn or trade-association events) with the script, and ask each one for the pilot-success metric.
3. Draft a one-page works-council/privacy info sheet: what's measured, what isn't, store-level only.

Want help sourcing or building this? Talk to us via www.gongbans.com.
