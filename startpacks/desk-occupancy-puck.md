# Desk Occupancy Puck (Thread) — Founder Start Pack

> A battery puck under each hot desk that tells the booking system whether the desk is actually used — radar sees a person sitting still, there is no camera, and nothing identifies who sat there.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Hybrid work left offices 40–60% empty on most days, yet companies still pay for every desk. Booking systems say a desk is "booked", not "used": no-shows block desks and the real-estate team decides on floor space with bad data. PIR under-desk sensors miss people sitting still; cameras are a non-starter with works councils.
- **Customer:** Corporate real-estate and facility teams (they pay), flexible-office operators, universities with study desks. Employees just sit down; the puck must be invisible to them.
- **Product:** A 2-year battery puck with a low-power 24 GHz presence radar and a Thread radio. It reports occupied/free every minute to a border router, aggregates into floor reports, and offers an API to booking tools for auto-release of no-shows. Counts and states only, never identities.
- **Why now:** Companies are cutting floor space based on data. Works councils (Betriebsrat, OR, CSE) block anything that can track individuals. Low-power radar (~100 µA average per catalogue) and Thread make an anonymous battery sensor practical.
- **The ask:** ~€110k to certification and a 1,000-desk rollout, ideally against a signed works-council approval and one paying anchor customer.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will a works council approve it in writing for one 200-desk pilot? That signed approval is the sales asset — try to get it before building 200.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Corporate real-estate and facility teams, flexible-office operators, universities with study desks.

**The problem as the pack states it:** Hybrid work left offices 40–60% empty on most days, yet companies still pay for every desk. Booking systems say a desk is "booked", not "used": no-shows block desks and the real-estate team decides on floor space with bad data. PIR under-desk sensors miss people sitting still; cameras are a non-starter with works councils.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.
- **r/sysadmin** · https://www.reddit.com/r/sysadmin/ — the IT people who approve or block a calendar integration.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€59–79 per desk + software (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how corporate real-estate and facility teams, flexible-office operators, universities with study desks deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know today how many of your booked desks are actually used, and what decision did you last make without that number?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A battery puck under each hot desk that tells the booking system whether the desk is actually used — radar sees a person sitting still, there's no camera, and nothing identifies who sat there. On a scale of one to ten, how likely would you be to buy that at €59–79 per desk + software (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Desk Occupancy Puck (Thread): would you pay €59–79 per desk + software (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Desk Occupancy Puck (Thread): A battery puck under each hot desk that tells the booking system whether the desk is actually used — radar sees a person sitting still, there's no camera, and nothing identifies who sat there. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €59–79 per desk + software (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

The real-estate manager of a 2,000-desk company has a lease decision worth millions and wants to know: how many desks are actually used, when, and where. Badge data tells who entered the building, not where they sat. Booking data lies (no-shows, people sitting at unbooked desks).

- **Who pays:** corporate real estate (CRE) or facility management, from a workplace-strategy budget. Flex-office operators pay to prove utilisation to their own landlords and to optimise layouts.
- **Who uses:** CRE analysts (dashboards), the booking system (API), employees (indirectly — fewer blocked desks).
- **Who can kill it:** the works council and the DPO. In Germany, co-determination applies to technical devices that are *suitable* to monitor employees' behaviour or performance (§87(1) No. 6 BetrVG) — suitability, not intent. Your design has to make individual tracking impossible, and you need that confirmed in writing.

### Market size (estimates — check)

- **TAM:** EU + UK office desks in companies >250 employees: ~30–40M desks (estimate). At €65 per puck = **€2–2.6B** theoretical.
- **SAM:** companies with hybrid policies, desk sharing and an active workplace-analytics programme: ~10% → **3–4M desks**, €200–260M hardware plus €1–3/desk/month software.
- **SOM (3 yrs):** 10–20 enterprise or flex-operator customers at 500–3,000 desks → **15–30k pucks**. Realistic if you win one reference with a works-council-approved deployment.

### Competition (2 searches)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / booking data + badge data | Free, already there | No-shows and unbooked use make it wrong by 20–40% |
| Under-desk PIR/thermal sensors (Milesight VS340-type ~£60, Elsys, IAconnects, Pressac, Disruptive Technologies) | Mature, LoRaWAN or proprietary | PIR misses still people; LoRaWAN needs gateways; several are "heat" sensors that caused privacy panics in the press |
| Ceiling sensors (Density Waffle-type at ~$2.50/desk/month software, Butlr thermal, PointGrab) | One sensor covers several desks | Expensive install, ceiling access, platform lock-in |
| Desk-booking tools with check-in apps (manual "check in" button) | Software only | Employees forget; check-in rates collapse after a month |
| Cameras | Accurate | Works councils say no; end of discussion |

**Wedge:** still-person radar (catches the motionless person that PIR misses) + Thread (no proprietary gateway; border routers are cheap) + a ready-made works-council/DPIA package. The approval document is part of the product.

### Product & value proposition

- **Hardware:** 60 mm puck stuck under the desk top or monitor arm, LD2410S low-power radar looking at the chair zone, HM-MT2401 (EFR32MG24) running Thread. 2× AA or a CR123A-class primary cell; target 2 years at 1-minute reporting (to be proven).
- **Privacy by design:** no unique person signal leaves the puck; only desk ID + occupied/free + timestamp. No micro-motion or breathing data exported. Sensitivity zone limited to the chair.
- **Software:** border router (pilot: M5 Gateway H2 or any Thread BR) → small edge/cloud service → dashboard + API (REST/webhook) into booking tools; auto-release of no-show bookings after X minutes.
- **Pricing (estimates):** puck €59–79 one-off; software €1.50–2.50/desk/month; or hardware-as-a-service €3.50/desk/month on a 36-month contract. Pilot: 200 desks for 3 months, €6–9k.

### Unit economics (estimates, EUR per puck)

| Item | 1k | 5k |
|---|---|---|
| LD2410S radar | 3.5 | 2.7 |
| HM-MT2401 Thread module | 4.5 | 3.5 |
| Battery holder + 2× AA (or primary cell) | 1.2 | 1.0 |
| Power path, LED, button, passives | 0.8 | 0.6 |
| PCB | 0.6 | 0.4 |
| Assembly + test (radar response, Thread join) | 2.0 | 1.2 |
| Enclosure + mounting pad/bracket | 2.2 | 1.4 |
| Packaging (bulk, 20 per box) | 0.6 | 0.4 |
| Freight + duty | 1.0 | 0.6 |
| Certification amortised (€18k) | 18.0 | 3.6 |
| **Landed cost** | **34.4** | **15.4** |
| Net price direct (€65) | 65 | 65 |
| Integrator/booking-vendor margin if indirect (30%) | −19.5 | −19.5 |
| **Gross margin direct** | **€30.6 (47%)** | **€49.6 (76%)** |
| **Gross margin via partner** | **€11** | **€30** |

Software at €2/desk/month over 36 months = €72 per desk. That's where the business is; the puck is the door-opener.

### Go-to-market

**First 100 customers (desks → first 1,000 desks):** one company with an active Betriebsrat/OR that *wants* to do a real-estate study. Approach via CoreNet Global chapters, workplace-strategy consultants (they run occupancy studies and need sensors), and flex-office operators (fewer works-council issues, faster decisions). Offer a 200-desk, 3-month study with a report.

**Then scale:** desk-booking software vendors as distribution partners (you become their sensor SKU), workplace consultants who run 6-week occupancy studies (rental model — pucks go from study to study), facility-service companies.

### 12-month plan

- **Q1:** prototype on HM-MT2401 EVB + LD2410S; works-council/DPIA package drafted with a labour lawyer; approach 3 pilot candidates (kill question).
- **Q2:** own PCB rev A, battery profiling, border-router integration, dashboard v0; 200-desk pilot with signed works-council agreement.
- **Q3:** pilot report; certification; first 1,000 units; one booking-software integration.
- **Q4:** second customer, consultant rental programme, Matter occupancy profile as optional (home-market spin-off reuses the same hardware).

**Team:** founder on enterprise sales (workplace/CRE background helps), embedded engineer (Thread/EFR32, full-time), backend/dashboard dev (part-time), privacy/labour-law advisor (a few days), Shenzhen partner for PCBA.

**Funding to first 1,000 pucks (estimate):** hardware landed excl. cert €16k + tooling €8k + certification €18k + prototypes/pilot €6k + 7 months team €55k + legal/DPIA €5k + sales €5k = **≈€113k**. Pilot fees (€6–9k) + first customer pre-payment for 1,000 desks (hardware €65k on order) cover most. Route: customer-funded rollout + angel or a proptech-focused pre-seed.

### Top risks

| Risk | Mitigation |
|---|---|
| **Regulatory/HR:** works council refuses | Approval package first; data minimisation by design (no person-level data possible); offer aggregated-only mode (floor-level %) |
| **Technical:** battery life — radar at ~100 µA average plus Thread polling | Sleepy end device, report on change + 15-min heartbeat; measure in week 6; fall back to USB-powered from monitor if needed |
| **Technical:** false "occupied" from a chair moving, a fan, the neighbour desk | Narrow detection gates; per-desk calibration on install; validate against manual audit (target ≥95% agreement) |
| **Market:** CRE buys studies, not permanent sensors | Rental model for 6–12 week studies; permanent install as upsell |
| **Supply:** LD2410S single source, contact-only design files | Firmware abstraction; second radar candidate qualified by DVT |
| **Ecosystem:** Thread border routers in offices are not standard IT | Ship your own BR in the pilot pack; IT-friendly docs (VLAN, outbound only) |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2410S low-power presence radar | https://www.gongbans.com/db/hilink-ld2410s.html | Still + moving person detection at ~100 µA average, GPIO + UART | Datasheet public, design files via maker (no open schematics) | Buy as module |
| HopeRF HM-MT2401 Matter-over-Thread module | https://www.gongbans.com/db/hoperf-hm-mt2401.html | EFR32MG24 Thread radio + your application firmware | PCB library — HopeRF MIT GitHub folder: https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401 | MIT licence for repo content |
| M5Stack Unit Gateway H2 (U195) | https://www.gongbans.com/db/m5stack-unit-gateway-h2.html | Thread/Zigbee gateway unit for pilot border-router setups | Enclosure/structure files only — main-board electronics not published | Prototyping/pilot only |

Also useful: the HM-MT2401 EVB kit (https://www.gongbans.com/db/hoperf-hm-mt2401-evb-kit.html, open schematic) as the reference for your base board.

### Block diagram

```
2×AA ──► power path ──► HM-MT2401 (EFR32MG24, Thread sleepy end device)
                             │ UART + GPIO (wake on presence change)
                       LD2410S radar, gates limited to chair zone
                             │
            Thread mesh ──► border router (pilot: Gateway H2 + host)
                             │
               occupancy service ──► dashboard + API ──► desk-booking tool (auto-release)
```

**Engineering gap:** power budget (radar + Thread sleep), the chair-zone tuning, install UX (desk ID pairing via QR in under 30 s per desk), and the privacy documentation.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| LD2410S | €3–4 | **Single source**; check sleep/wake behaviour per firmware version |
| HM-MT2401 | €4–5 | EFR32MG24 is Silicon Labs; module supply via HopeRF |
| 2× AA + holder | €1.2 | Or CR123A; avoid Li-ion (Battery Reg., shipping) |
| LDO/buck with low Iq | €0.4 | |
| Install button + LED | €0.3 | |
| Enclosure + VHB pad | €2 | Radar window toward the chair |
| QR label with desk-ID | €0.05 | |

### Firmware/software starting point

- **Silicon Labs Simplicity SDK** + **OpenThread** for the EFR32MG24 (HM-MT2401). Start from the sleepy end device examples.
- **OpenThread Border Router (ot-br-posix)** on a Linux host, or the ESP Thread BR on ESP32 (Espressif's esp-thread-br exists) for the pilot.
- Radar: LD2410S protocol from the Hi-Link datasheet; ESPHome's `ld2410` component is a useful reference for LD2410-family framing (verify S-variant differences).
- Backend: any time-series store + small API; desk-booking integrations — search which vendors your pilot uses and whether they accept occupancy webhooks.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — works-council/DPIA one-pager drafted; 8 interviews with CRE managers; 1 pilot candidate | Pilot candidate agrees to put the one-pager to its works council |
| 3–5 | **Works-like** — EVB + LD2410S on 10 desks, data to a dashboard | ≥95% agreement with a manual audit (every 15 min, 2 days); still-person detection proven |
| 6–8 | **Looks-like + EVT** — rev A PCB, enclosure, battery current profile, QR install flow; 30 pucks | Projected battery life ≥18 months; install <30 s/desk |
| 9–10 | **DVT + pre-compliance** — pre-scan (24 GHz + 2.4 GHz), EN 18031 gap analysis, security review (Thread credentials, OTA) | No pre-scan fails; written works-council approval for 200 desks |
| 11–12 | **Pilot batch** — 200 pucks deployed, auto-release live | Customer report: real utilisation vs booked; no-show release working; LOI for full floor/building |

### Certification checklist (EU)

- **CE — RED:** EN 300 440 (24 GHz radar), EN 300 328 (2.4 GHz Thread/802.15.4), EN 301 489-1/-3/-17, EN 62368-1, EN 62311/62479. Estimate €8–12k.
- **EN 18031-1/-2** (RED delegated act, since Aug 2025): the puck communicates via the border router to an internet service → in scope. -2 applies because the system processes data that could relate to persons. Budget €3–5k.
- **CRA:** reporting from 11 Sep 2026, full from 11 Dec 2027: SBOM, OTA updates, vulnerability handling, defined support period (enterprise customers will ask for 5+ years).
- **Matter certification:** not needed for the B2B Thread product unless you sell a Matter SKU; then CSA membership + test lab fees (estimate €10–20k all-in — check the current CSA fee schedule).
- **RoHS, REACH, WEEE**, packaging EPR. **Battery Regulation** for supplied AA cells (labelling, take-back).
- **GDPR + works council:** DPIA template, data-flow diagram, retention policy, statement that data cannot be linked to persons (no booking-ID join in raw data unless the customer explicitly configures auto-release — then document it). In DE: Betriebsvereinbarung template.
- **Total estimate:** €14–20k (without Matter cert).

### Validation toolkit

- **Kill question:** Will a works council approve it in writing for one 200-desk pilot? That signed approval is the sales asset — get it before building 200. Cheapest experiment: a 2-page privacy description + a demo puck shown to one works council via a friendly CRE manager.
- **Interview script (5):**
  1. How do you measure desk utilisation today, and how wrong do you think the numbers are?
  2. What decision would better data change in the next 12 months (lease, floor consolidation, layout)?
  3. Have you tried sensors before? What did the works council or employees say?
  4. Who would sign the budget, and is it a study (weeks) or a permanent tool?
  5. At €65 per desk + €2/month, how many desks would you start with?
- **Landing page:** Headline: "Know which desks are really used — without watching anyone." Bullets: "Radar detects a person sitting still; no cameras, no names." / "Releases no-show bookings automatically." / "Works-council and DPIA package included."
- **Pass:** one signed works-council approval + a paid 200-desk pilot, or 3 CRE teams requesting paid pilots within 8 weeks.

### First production checklist

- Samples: radar modules from 2 lots; verify low-power mode current on each.
- Golden sample: battery current profile logged 7 days; detection map documented.
- DFM: enclosure with radar window, tool-less mounting, battery door that cleaners can't knock off.
- MOQ talk: modules per tray; negotiate split delivery against the rollout schedule.
- QC/AQL: 100% Thread join + radar test; sleep-current check on a sample per lot (AQL 0.65 on current).
- Packaging: bulk 20/box, QR stickers pre-printed with desk-ID series.
- Incoterms: FOB Shenzhen; ship batteries separately or as "contained in equipment" with correct paperwork.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410S 24 GHz low-power human-presence radar module](/db/hilink-ld2410s.html) (low-power 24 GHz presence radar). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder)](/db/hoperf-hm-mt2401.html) (Thread module (mesh to a border router)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Gateway H2 (U195)](/db/m5stack-unit-gateway-h2.html) (Thread/Zigbee gateway unit for pilots). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195) — for a Desk Occupancy Puck (Thread)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Desk Occupancy Puck (Thread): A battery puck under each hot desk that tells the booking system whether the desk is actually used — radar sees a person sitting still, there's no camera, and nothing identifies who sat there. The design is built around your HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195).
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
主题：样品订购及批量报价 — HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195) — 用于Desk Occupancy Puck (Thread)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Desk Occupancy Puck (Thread)：A battery puck under each hot desk that tells the booking system whether the desk is actually used — radar sees a person sitting still, there's no camera, and nothing identifies who sat there。产品设计基于贵司的HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195)。
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
Subject: PCBA quote from open design files — Desk Occupancy Puck (Thread), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Desk Occupancy Puck (Thread): A battery puck under each hot desk that tells the booking system whether the desk is actually used — radar sees a person sitting still, there's no camera, and nothing identifies who sat there. The design starts from published open-hardware files (HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Desk Occupancy Puck (Thread)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Desk Occupancy Puck (Thread)：A battery puck under each hot desk that tells the booking system whether the desk is actually used — radar sees a person sitting still, there's no camera, and nothing identifies who sat there。设计基于已公开的开源硬件文件（HLK-LD2410S 24 GHz low-power human-presence radar module, HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), M5Stack Unit Gateway H2 (U195)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Write the 2-page privacy and works-council description now — before any hardware. Ask a labour-law contact to red-line it.
2. Order an HM-MT2401 EVB kit and 3 LD2410S; get occupancy from one desk into a Thread network.
3. Message 10 CRE / workplace managers on LinkedIn asking one question: "Would your works council approve an anonymous desk sensor if the data could never identify a person?"

Want help sourcing or building this? Talk to us via www.gongbans.com.
