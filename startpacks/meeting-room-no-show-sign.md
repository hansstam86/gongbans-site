# Meeting-Room No-Show Sign — Founder Start Pack

> An e-paper sign by the meeting-room door that shows the booking. If nobody turns up within 10 minutes, a radar inside notices the empty room and releases it automatically.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Ghost bookings. People book a room "just in case", don't show up, and the room sits empty while others wander the floor looking for space. Vendor surveys put pre-policy no-show rates at 30–45% of bookings (vendor data, treat as indicative). Panels with a "check in" button exist, but people forget to tap, and then a meeting that's actually happening gets released.
- **Customer:** Facility managers and workplace teams at offices with 10–100 bookable rooms (DACH, Benelux, Nordics), co-working operators, universities. The facility/workplace budget pays; employees and students use it.
- **Product:** Two parts per room. Outside: a battery e-paper sign (ESP32-S3 + e-paper, PaperS3-class) showing now/next booking. Inside: a small ceiling or wall unit with a 24 GHz presence radar (Hi-Link LD2412) and an ESP32-C6, which confirms "people are in the room". No check-in tap, no camera, no microphone. If the room is booked and stays empty for 10 minutes, the booking is released in the calendar.
- **Why now:** Hybrid work means rooms are booked more speculatively than ever, and offices are shrinking floor space, so every empty booked room hurts. Cheap 24 GHz radar now detects people sitting still (which PIR misses), and calendar APIs from the common office suites make integration a software job.
- **The ask:** About €120–150k (estimate) to the first 1,000 rooms, funded by 3–5 paid pilots plus a small angel round. B2B, sold per room with an optional software fee.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will an office with 20 rooms pay €229/room when cheaper non-sensing signs exist? Measure released hours in a 4-week pilot; need >15% more usable room time.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Offices with room-booking systems, co-working spaces, universities.

**The problem as the pack states it:** Ghost bookings. People book a room "just in case", don't show up, and the room sits empty while others wander the floor looking for space. Vendor surveys put pre-policy no-show rates at 30–45% of bookings (vendor data, treat as indicative). Panels with a "check in" button exist, but people forget to tap, and then a meeting that's actually happening gets released.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/sysadmin** · https://www.reddit.com/r/sysadmin/ — the IT people who approve or block a calendar integration.
- **r/msp** · https://www.reddit.com/r/msp/ — managed-service providers: the reseller channel for office devices.
- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€199–249 per room (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how offices with room-booking systems, co-working spaces, universities deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How often are your meeting rooms booked but empty, how do you know, and what have you tried to stop it?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] An e-paper sign by the meeting-room door that shows the booking — and if nobody turns up within 10 minutes, radar notices the empty room and releases it automatically. On a scale of one to ten, how likely would you be to buy that at €199–249 per room (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Meeting-Room No-Show Sign: would you pay €199–249 per room (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Meeting-Room No-Show Sign: An e-paper sign by the meeting-room door that shows the booking — and if nobody turns up within 10 minutes, radar notices the empty room and releases it automatically. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €199–249 per room (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The pain is felt by two people. The **employee** who can't find a room. The **facility or workplace manager** who's told "we need more meeting rooms" while their occupancy data says rooms are booked 70% and used 40%. The manager pays, out of the workplace/facility budget, typically as a per-room line item.

Best first segment: **mid-size offices (200–1,500 staff) in DACH/Benelux/Nordics that already use a cloud calendar for room resources but have no sensors.** They have the problem, a calendar API to plug into, and no €400-per-room integrator project in their budget. Second segment: **co-working operators**, who sell room hours, so a released ghost booking is directly resellable. Third: **universities** (seminar and study rooms booked by students), slower to buy but huge in room count.

Who doesn't buy: offices with 3 meeting rooms (no pain), and enterprises that already standardised on a large workplace platform with its own sensors.

### Market size (estimates)
- Offices in EU-27 + UK + CH + NO with ≥10 bookable rooms: assume ~150,000 sites × average 20 rooms → **~3 M bookable rooms**.
- **TAM:** 3 M rooms × €229 hardware ≈ **€690 M** one-off, plus optional software €3/room/month (≈ €108 M/yr if all paid).
- **SAM:** DACH + Benelux + Nordics, sites on the main cloud calendars, no existing sensor system: ~25% → **~750k rooms ≈ €170 M**.
- **SOM (3 years):** 1% of SAM → **~7,500 rooms ≈ €1.7 M hardware + ~€270k/yr software**. That's a small, profitable company, not a unicorn, and the honest goal.

### Competition
| Alternative | Typical cost (estimate) | Weakness we attack |
|---|---|---|
| Room-booking panels (tablet-class door displays from workplace-software vendors) with tap check-in | €300–800 per room + software subscription | Need mains/PoE at the door; people forget to tap; no presence truth |
| Panel + separate occupancy sensor from the same vendor (e.g. room-booking platforms that sell a sensor add-on for auto-release) | €500–1,000+ per room + subscription | Price; integrator project; locked to one platform |
| Workplace analytics sensors (ceiling people counters) | €150–400 per sensor + analytics subscription | Built for analytics reports, not for releasing bookings at the door |
| Calendar-only auto-release (release if not accepted/checked-in in the app) | Free / included | Releases rooms that are in use; nobody trusts it, so it gets switched off |
| Do nothing / "booking etiquette" emails | Free | Doesn't work. Never has |

**Wedge:** battery-powered on both sides (no electrician, no PoE run, install in 10 minutes per room with adhesive or two screws), **presence radar instead of a tap**, privacy story that works councils accept (no camera, no microphone, no person identification), and a price under €250 per room. Sold as a small add-on to the calendar an office already has, not a platform migration.

### Product & value proposition
- **Door sign (outside):** ~4.7" e-paper on ESP32-S3 (PaperS3-class), shows room name, current/next booking (title optional, can be hidden for privacy), status colour bar via e-paper icons, "released: room free" message. Wakes every few minutes or on a push from the gateway. Target: 6–12 months on a battery (estimate; depends on refresh rate).
- **Room unit (inside):** LD2412 24 GHz radar (presence range 0.75–9 m adjustable, ±60°, per Hi-Link) + ESP32-C6 (Wi-Fi 6, Thread, BLE). Mains USB or battery (radar draws ~90 mA average per the datasheet, so battery needs aggressive duty cycling; the default is a USB-C power version and a battery version for rooms without a socket near the ceiling).
- **Cloud/bridge service:** connects to the office calendar resource mailboxes, applies the rule (booked + no presence for N minutes → release, notify organiser), logs room utilisation per hour. No personal data from the radar; calendar data is processed under a DPA.
- **Utilisation report:** per room, booked vs used hours, ghost booking rate, "rooms you could convert". This report is what the facility manager forwards to the CFO.

**Pricing (estimates):**
- €229 per room (sign + sensor), volume €199 above 20 rooms.
- Software: €3/room/month (calendar sync, release, report), or €0 with a self-hosted bridge for IT teams that want it on-premise.
- Pilot pack: 5 rooms + 3 months software for €990, credited against an order.

### Unit economics (estimates per room set, ex-VAT)
| Item | 1k rooms | 5k rooms |
|---|---|---|
| BOM (e-paper + ESP32-S3 sign, LD2412 + ESP32-C6 room unit, batteries, PCBs) | €45.00 | €36.00 |
| Assembly & test (2 units, radar functional test, e-paper check) | €4.00 | €3.00 |
| Enclosures (2 small, injection moulded after 1k; 3D-printed/urethane-cast before) | €5.00 | €3.00 |
| Packaging (one box per room, mounting kit) | €1.50 | €1.00 |
| Freight + duty to EU | €1.50 | €1.00 |
| Certification amortised (~€30k: RED 24 GHz + 2.4 GHz, EMC, safety, EN 18031) | €30.00 | €6.00 |
| **Landed cost** | **€87.00** | **€50.00** |
| Net price: direct (€229) / via reseller (~€160 after 30%) | €229 / €160 | €199 / €140 |
| **Gross margin (hardware only)** | **€142 (62%) direct / €73 (46%) reseller** | **€149 (75%) / €90 (64%)** |

Software (€3/room/month) runs at ~85% gross margin once hosted; at 1,000 rooms that's ~€36k/yr recurring, which pays for support.

### Go-to-market
**First 100 customers (rooms, then sites):**
- **Your own network and local tech/co-working scene:** co-working operators decide fast and feel the money. Offer the 5-room pilot pack.
- **Facility-management communities:** national FM associations and their events, LinkedIn groups for workplace/facility managers, FM trade fairs in DACH and the Netherlands. Bring the utilisation report, not the hardware.
- **IT admins of mid-size companies:** a self-hosted bridge on GitHub is a strong door-opener; IT teams like products they can audit.
- **Universities:** one faculty building as a pilot through the facility department; students talk.

**Scale channels:** AV and workplace integrators (they install room systems and want a cheap sensing add-on), office furniture dealers who do fit-outs, and resellers of the large calendar suites. Later: white-label the room unit to a room-booking software company that has no hardware.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill-question pilot: 10 rooms at 2 offices with a works-like radar + logger (no sign yet), measure ghost-booking rate and released hours; calendar integration with one major suite |
| Q2 | Custom PCBs for sign and room unit; 50-room EVT at 4 sites; utilisation report v1; works-council/privacy pack |
| Q3 | DVT, RED/EMC/EN 18031 testing; second calendar suite; first integrator partner; 200 rooms sold |
| Q4 | 1,000 rooms produced and installed; software subscription live; reseller programme |

**Team:** founder (sales + workplace domain), 1 embedded engineer (ESP-IDF, radar tuning, low power), 1 backend developer (calendar APIs, Microsoft/Google-class OAuth, DPA-grade hosting in the EU), part-time industrial designer. Support can be the founders until ~2,000 rooms.

**Funding to the first 1,000 rooms (estimates):**
- NRE: electronics 2 boards €15k, firmware €20k, backend + calendar integrations €30k, enclosure design + soft tooling €12k → **€77k**
- Certification **€30k**
- 1,000 room sets landed (ex-cert) ~€57 → **€57k**
- Lean running costs 9 months (part-time team stipends, hosting, travel to pilots) **€45k**
- Total ≈ **€209k**; minus pilot and pre-order revenue (say 300 rooms prepaid at €199 ≈ €60k) → **~€150k** to raise.
- Route: paid pilots + an angel or two from the proptech/workplace scene; regional innovation vouchers can cover part of the firmware/backend work. No VC needed until there's a reseller channel working.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: false "empty" (people sitting very still, partitions, glass walls)** | Radar tuned per room size; 10-min confirmation; organiser gets a "still using the room? tap to keep" notice before release; log every release for tuning |
| **Technical: radar battery life** | Default to USB-C power for the room unit; battery version only with radar duty cycling, measured in EVT |
| **Market: cheaper non-sensing signs exist** | Sell the released hours (report), not the sign; offer a sensor-only version for offices that already have panels |
| **Market: big platforms bundle sensors** | Stay platform-agnostic and cheap; integrator/white-label channel |
| **Regulatory/privacy: works council (BetrVG §87 in DE) sees "employee monitoring"** | Room-level presence only, no person tracking, no per-person data; ready-made works-agreement template and DPIA; aggregated reports only |
| **Security: calendar access tokens** | EU hosting, least-privilege API scopes (room resources only), EN 18031 + pentest; self-hosted option |
| **Supply: LD2412 single source (Hi-Link)** | Abstract the radar interface (UART protocol layer); qualify a second 24 GHz presence module in DVT |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD2412 24 GHz presence radar (BLE) | https://www.gongbans.com/db/hilink-ld2412.html | Room-presence truth incl. still people; 0.75–9 m adjustable, ±60°, UART + GPIO, BLE set-up, avg 90 mA (per datasheet) | Datasheet public; schematics/files via maker (contact Hi-Link) | Commercial module; buy from Hi-Link or distributors; no open design files |
| M5Stack PaperS3 (C139) | https://www.gongbans.com/db/m5stack-papers3.html | Works-like door sign: ESP32-S3 + e-paper in one unit | Enclosure/structure files only (main-board electronics not published) | Use as dev platform; your production board is your own design |
| Espressif ESP32-C6-DevKitC-1 | https://www.gongbans.com/db/espressif-esp32-c6-devkitc-1.html | Room-unit controller: Wi-Fi 6, Thread, BLE | Reference design files from Espressif (per catalogue) | Espressif reference designs are free to use; ship on a pre-certified module |

### Block diagram
```
INSIDE ROOM                                   OUTSIDE DOOR
[LD2412 radar] --UART--> [ESP32-C6] ~~Wi-Fi~~>  [ESP32-S3 + e-paper sign]
   presence/still         room unit     \        now/next, "released", battery
                                         \
                                          v
                               [Bridge service, EU-hosted or on-prem]
                                 |-- calendar API (room resources)
                                 |-- release rule: booked & empty > N min
                                 `-- utilisation report per room
```
**Engineering gap:** the boards give you radar, radio and display. Missing: radar tuning for meeting rooms (still people at a table, glass walls), the release logic with organiser override, calendar integrations with proper OAuth and resource scopes, low-power e-paper refresh scheduling, provisioning (pair sign + room unit + calendar room in under 5 minutes), and the utilisation report.

### Starter BOM (estimates at 1k sets)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD2412 radar module | €3.50 | Sole source (Hi-Link); check MOQ and lead time |
| ESP32-C6 module (room unit) | €2.50 | Pre-certified module |
| ESP32-S3 module (sign) | €3.00 | PSRAM variant for e-paper buffers |
| 4.2–4.7" e-paper panel | €12–18 | **Long lead / allocation risk**; lock a panel supplier early |
| Batteries (Li-ion pouch or 2× AA lithium for sign) | €3–5 | Li-ion triggers battery regulation duties (see certification) |
| PCBs + passives, USB-C, buttons (2 boards) | €5.00 | |
| Mounting kit (adhesive, screws) | €1.00 | |
| Enclosures (2) | €5.00 | Soft tooling at 1k |

### Firmware/software starting point
- **ESP-IDF** (Espressif) for both units; Espressif's e-paper examples and M5Stack's PaperS3 libraries (search the M5Stack GitHub for "PaperS3").
- **Radar:** Hi-Link publishes the LD24xx serial protocol in the datasheet/user manual; community drivers exist for ESPHome for the LD2410/LD2450 family (search "ESPHome ld2410"). For the LD2412 specifically, search, and expect to write your own parser from the protocol doc.
- **Calendar:** the common office suites' REST APIs for room/resource calendars (search the vendors' developer docs for "room resource calendar API"). Use least-privilege app permissions scoped to room mailboxes.
- **Prototype shortcut:** Home Assistant + ESPHome on the devkits can fake the whole loop in a week before you write the bridge.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question pilot:** 10 rooms at 2 offices, radar logger only, compare to calendar. Pass: ghost bookings ≥20% of booked hours, and the facility manager says they'd pay €229/room to release them |
| 3–5 | Works-like | Devkits: LD2412 + ESP32-C6 in the room, PaperS3 at the door, bridge releasing test bookings in one calendar suite. Pass: correct presence on 95% of 15-minute intervals across 3 room sizes |
| 6–8 | Looks-like + EVT | Custom PCBs, printed enclosures; 30 sets in 2 offices; install time < 10 min/room; sign battery projection ≥ 6 months |
| 9–10 | DVT + pre-compliance | RED pre-scan (24 GHz radar + 2.4 GHz), EMC, EN 18031 gap analysis; works-council pack reviewed by one real works council; false-release rate < 1 per room per month |
| 11–12 | Pilot batch | 50 sets sold at 3+ sites; utilisation report accepted by a facility manager as "worth paying for"; reorder intent from 1 site |

### Certification checklist (EU)
- **CE under RED (2014/53/EU):** 24 GHz radar (EN 300 440 short-range devices; check the current version and the 24.05–24.25 GHz conditions), 2.4 GHz Wi-Fi/BLE/Thread (EN 300 328), EMC (EN 301 489-1/-3/-17), safety EN 62368-1, RF exposure EN 62311/62479. Est. **€10–15k** for two devices.
- **RED delegated act cybersecurity (EN 18031-1, and -2 because it handles calendar data)**, mandatory since 1 Aug 2025. Est. **€8–12k**.
- **CRA:** reporting obligations from 11 Sept 2026, full application 11 Dec 2027. Plan: signed OTA, SBOM, vulnerability disclosure policy, defined support period (≥5 years for B2B buyers).
- **RoHS, REACH (SVHC declaration), WEEE** registration in each country you sell to (B2B WEEE in DE via stiftung ear), packaging registration.
- **Battery Regulation (EU) 2023/1542** if Li-ion: labelling, collection, due diligence thresholds; easier with replaceable primary lithium AA for the sign.
- **GDPR:** radar gives room-level presence, no identification, but in an office context presence can be linked to whoever booked the room. Do a DPIA, offer a DPA, EU hosting, data minimisation (store aggregates, not raw timelines). In Germany, involve the works council (co-determination on technical monitoring systems).
- **Not applicable:** LVD (low voltage, USB-powered), toy, medical.
- **Total estimate: €20–30k.**

### Validation toolkit
- **Kill question:** Will an office with 20 rooms pay €229/room when cheaper non-sensing signs exist? Measure released hours in a 4-week pilot; you need >15% more usable room time.
- **Cheapest experiment (~€300):** 10 radar devkits + ESP32 loggers taped to the ceilings of 10 rooms for 4 weeks, compared offline to the room calendars. No sign, no release. Just the report: "Your rooms were booked 68% and used 41%."
- **5-question interview (facility/workplace manager):**
  1. How do you know today whether booked rooms are actually used?
  2. What happens when someone can't find a room? Who complains, and to whom?
  3. Have you tried check-in or auto-release before? Why did it stick or not?
  4. Who has to agree to sensors in rooms (IT, works council, DPO)? How long does that take?
  5. If we showed you 20% more usable room hours, what budget line pays €229 per room?
- **Landing-page headline:** "Booked but empty? The room frees itself."
  - Sees if anyone is in the room, without cameras or microphones.
  - Battery sign at the door, installed in 10 minutes. No cabling.
  - Works with the calendar you already use, and shows the hours you got back.
- **Pass threshold:** 3 paid pilots (5-room pack at €990) within 6 weeks of outreach, and one site committing to ≥20 rooms after its pilot.

### First production checklist
- **Samples:** 3 radar module samples per batch tested in a standard room (still person at 3 m, 5 m, 7 m); e-paper panels from the production lot.
- **Golden sample:** sign + room unit with firmware version, radar sensitivity settings and battery measurement recorded; kept at the factory and with you.
- **DFM review:** radar keep-out area in front of the antenna (no metal, uniform plastic thickness), e-paper flex cable strain relief, battery door, adhesive mounting strength.
- **MOQ talk:** e-paper panels (often the MOQ driver), LD2412 reels, ESP modules. Ask for buffer stock agreements on the panel.
- **QC/AQL:** AQL II 1.0 (major) / 2.5 (minor); 100% functional test: radar detects a reference target, Wi-Fi joins, e-paper full refresh, battery current in sleep below spec.
- **Packaging:** one box per room (sign + unit + mounting kit + QR code linking the pair), privacy notice card for the room ("This room uses a presence sensor. No camera, no microphone.").
- **Incoterms:** FOB/FCA Shenzhen; air freight for pilot batches, sea or rail for 1k+; check DDP quotes for small batches.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and M5Stack and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2412 24 GHz human-presence radar module with Bluetooth](/db/hilink-ld2412.html) (24 GHz presence radar with Bluetooth set-up). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (e-paper display with ESP32-S3). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c6-devkitc-1](/db/espressif-esp32-c6-devkitc-1.html) (Wi-Fi 6 / Thread controller reference for the in-room unit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **iDisc Technology** (深圳市艾迪思科技有限公司) · no website on file — E-ink display module / e-reader OEM: E-ink display module; e-reader gongban; retail price tag; OEM/ODM. *(E-ink display modules)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and M5Stack and Espressif websites)

```email
Subject: Sample order and volume pricing — HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1 — for a Meeting-Room No-Show Sign

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Meeting-Room No-Show Sign: An e-paper sign by the meeting-room door that shows the booking — and if nobody turns up within 10 minutes, radar notices the empty room and releases it automatically. The design is built around your HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1.
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
主题：样品订购及批量报价 — HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1 — 用于Meeting-Room No-Show Sign

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Meeting-Room No-Show Sign：An e-paper sign by the meeting-room door that shows the booking — and if nobody turns up within 10 minutes, radar notices the empty room and releases it automatically。产品设计基于贵司的HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1。
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
Subject: PCBA quote from open design files — Meeting-Room No-Show Sign, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Meeting-Room No-Show Sign: An e-paper sign by the meeting-room door that shows the booking — and if nobody turns up within 10 minutes, radar notices the empty room and releases it automatically. The design starts from published open-hardware files (HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Meeting-Room No-Show Sign，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Meeting-Room No-Show Sign：An e-paper sign by the meeting-room door that shows the booking — and if nobody turns up within 10 minutes, radar notices the empty room and releases it automatically。设计基于已公开的开源硬件文件（HLK-LD2412 24 GHz human-presence radar module with Bluetooth, M5Stack PaperS3 (C139), Espressif esp32-c6-devkitc-1；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 10 LD2412 modules, 10 ESP32-C6 devkits and 2 PaperS3 units; flash a simple presence logger.
2. Line up 2 offices (one co-working operator, one mid-size company) for the 4-week ghost-booking measurement; send the works-council one-pager up front.
3. Build the utilisation report mock-up from fake data and show it to 5 facility managers; ask the €229 question at the end.

Want help sourcing or building this? Talk to us via www.gongbans.com.
