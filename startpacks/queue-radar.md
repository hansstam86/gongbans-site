# Queue Radar — Founder Start Pack

> A sensor above the counter that sees how many people are waiting and lights a "second till please" lamp in the back office — radar, so there's no camera pointing at customers.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** In bakeries, pharmacies, post-office counters and small supermarkets, staff in the back (baking, stocking, picking prescriptions) don't see the queue building. Customers walk out after a minute. Owners can't afford an extra person "just in case".
- **Customer:** Owners/branch managers of small counter-service businesses in the EU (they pay); staff (use the lamp). Chains with 10–100 branches are the scale customer.
- **Product:** A wall/ceiling sensor with a 24 GHz multi-target tracking radar aimed at the queue zone, and a lamp/buzzer unit in the back office over Wi-Fi. Thresholds per daypart ("≥3 waiting for >30 s → lamp"), optional daily "longest wait / busiest hour" e-mail. No images, no IDs.
- **Why now:** Staff is the biggest cost in small retail and hard to find; camera-based queue analytics trigger GDPR signage questions and, in Germany, works-council co-determination. Multi-target radar modules now track several people for a few euros.
- **The ask:** ~€90k to first 1,000 sets; kill question: does the count stay accurate in a busy bakery with prams and kids? — 3 shops, 1 week each.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does the count stay within ±1 person for queues up to 8 in a busy bakery with prams and kids? 3 shops, 1 week each.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Bakeries, pharmacies, post-office counters, small supermarkets and town halls in the EU.

**The problem as the pack states it:** In bakeries, pharmacies, post-office counters and small supermarkets, staff in the back (baking, stocking, picking prescriptions) don't see the queue building. Customers walk out after a minute. Owners can't afford an extra person "just in case".

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/smallbusiness** · https://www.reddit.com/r/smallbusiness/ — shop and café owners.
- **r/pharmacy** · https://www.reddit.com/r/pharmacy/ — pharmacists and pharmacy staff.
- **HDE, Handelsverband Deutschland** · https://einzelhandel.de/ — German retail association; regional associations reach the shops.
- **EuroCommerce** · https://www.eurocommerce.eu/ — European retail and wholesale federation.
- **Zentralverband des Deutschen Bäckerhandwerks (DE)** · https://www.baeckerhandwerk.de/ — German bakers' trade federation; the local Bäckerinnung is the way in.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€99–149 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how bakeries, pharmacies, post-office counters, small supermarkets and town halls in the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you notice today that the queue at the till is getting too long, and what happened the last time nobody did?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A sensor above the till that counts how many people are waiting and lights a 'second till please' lamp in the back office — radar, so there's no camera pointing at customers. On a scale of one to ten, how likely would you be to buy that at €99–149 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Queue Radar: would you pay €99–149 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Queue Radar: A sensor above the till that counts how many people are waiting and lights a 'second till please' lamp in the back office — radar, so there's no camera pointing at customers. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €99–149 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

The classic bakery: two staff, one at the counter, one in the back. At 07:40 the queue goes from 1 to 6 in two minutes. The person in the back finds out when the counter person shouts — or doesn't. Walk-outs aren't measured, so the loss is invisible. Pharmacies: one pharmacist at the counter, one picking orders; same story.

- **Who pays:** independent bakery/pharmacy owners (single site, €100–150 spend is an owner decision); branch-network operators (bakery chains, pharmacy groups, convenience chains) — they want the daily report across branches.
- **Who uses:** staff in the back (lamp/buzzer), the branch manager (thresholds, report).
- **Who influences:** POS/till dealers and shopfitters who visit these shops anyway.

### Market size (estimates — check)

- **TAM:** DE alone has roughly 9–10k craft-bakery businesses with tens of thousands of shops, ~17k pharmacies, plus post/parcel counters, butchers, small supermarkets. DE+AT+NL+BE: assume **~200k** counter-service sites. One set at €129 → **~€26M** hardware (+ optional report service €4/month → ~€10M/yr if all took it — they won't).
- **SAM:** sites with peaky queues and back-office staff: assume 35% → 70k → **~€9M** hardware.
- **SOM (3 years):** 3% of SAM via 2–3 chains + independents → **~2,000–2,500 sets**, ~€0.3M hardware + €50–80k/yr service. Bigger only if a POS vendor or chain rolls it out.

### Competition (1 search + category knowledge)

| Alternative | What it is | Why we can still win |
|---|---|---|
| Do nothing / counter staff shouts | Free | Walk-outs, stressed staff |
| Counter bell/call button | Staff presses a button | Staff is busy serving — they don't press it |
| Camera-based queue analytics | Ceiling camera + AI counts per queue | Privacy compliance depends on configuration, signage and retention; works-council issues in DE; pricier |
| Overhead people counters with queue alerts (e.g. V-Count-type 3D/thermal sensors) | Professional retail analytics, zone alerts | Built for larger stores and analytics budgets; ceiling height 2.2–7 m; subscription |
| Ticket/queue management systems | Take-a-number + display | Different shop format (town halls, pharmacies sometimes) — heavy |

**Wedge:** no camera, €129, plug-in install in 15 minutes, a lamp in the back. Not an analytics platform — a staffing trigger.

### Product & value proposition

- **Sensor:** wall-mounted at ~2.0–2.4 m behind/above the counter facing the customer area (the module is specified for horizontal wall mounting, 8 m range, ±60° H/±30° V), mains via a 5 W isolated supply or USB-C adaptor. Software zones: "queue zone" polygon, "staff side" excluded.
- **Honest limit — read this:** the HLK-LD2454 tracks **up to three targets**. That's enough for the decision that matters ("≥3 people waiting → call the second till"), but not to count a queue of 8. For long queues: add a second sensor covering the tail of the queue (zone 2 occupied = queue ≥ 4–6), or evaluate a multi-target module with more tracks. Don't sell "counts your queue to 8" until you've proven it.
- **Logic:** occupancy per zone + dwell time; thresholds per daypart (morning rush vs afternoon); hysteresis so the lamp doesn't flicker.
- **Back-office unit:** 5×5 LED matrix or LED bar + buzzer, shows the number (1/2/3+) and colour; ESP-NOW or Wi-Fi from the sensor; mute button.
- **Report (optional, €4/month):** daily e-mail: busiest 30 minutes, longest estimated wait, number of "second till" calls. Aggregates only.
- **No images, no IDs, no Bluetooth/Wi-Fi sniffing.**

**Pricing (estimates):** set (sensor + back-office lamp) **€129 ex VAT**; extra tail sensor €79; report €4/month per site. Chains (20+ sites): €109 per set.

### Unit economics (estimates, EUR per set: sensor + lamp)

| Item | 1k | 5k |
|---|---|---|
| Sensor BOM (HLK-LD2454 ~€5, ESP32-C3 module €2.2, HLK-5M05 5 W AC-DC €2.2, PCB/passives/connectors €1.5) | 10.9 | 9.3 |
| Lamp BOM (ESP32-C3 module €2.2, 25 addressable LEDs €1.0, buzzer €0.3, PCB €0.6, certified USB-C adaptor €2.5) | 6.6 | 5.7 |
| PCBA assembly + test (both) | 2.5 | 1.8 |
| Enclosures (sensor with radome + bracket, lamp) | 4.5 | 3.2 |
| Packaging + install guide | 1.8 | 1.3 |
| Freight + duty to EU | 1.5 | 0.8 |
| Certification amortised (€16k) | 16.0 | 3.2 |
| **Landed cost** | **43.8** | **25.3** |
| Direct at €129 ex VAT, less €8 fulfilment | 121.0 | 121.0 |
| **Gross margin direct** | **€77.2 (64%)** | **€95.7 (79%)** |
| Via POS dealer/shopfitter (keeps ~35%) → €83.9 | €40.1 (48%) | €58.6 (70%) |

Margins are fine. The hard cost is selling to thousands of small shops one by one — which is why chains and POS dealers matter.

### Go-to-market

**First 100 customers:**
- Three bakeries for the kill-question test (free week, then €99 if they keep it).
- A regional bakers' guild (Bäckerinnung) meeting or newsletter; the bakery trade press; local pharmacy owner groups.
- Two POS/till dealers who service bakeries: they see the problem every visit; give them a demo set and a 30% margin.
- Walk-in sales: 20 bakeries in one city at 07:30 with a tablet showing the radar live view. Bluntly the fastest way to learn.

**Then scale:** bakery chains and pharmacy groups (head-office pilot in 5 branches → rollout), POS vendors (bundle/integration), shopfitters for new branches, NL/AT/BE.

### 12-month plan

- **Q1:** dev-board prototypes; the kill-question test in 3 shops; 15 owner interviews; works-council/GDPR one-pager reviewed.
- **Q2:** rev A sensor + lamp, 20 paid pilots, threshold tuning, daily report MVP.
- **Q3:** rev B, certification, 1,000-set run; POS-dealer channel; first chain pilot.
- **Q4:** tail-sensor SKU, chain rollout, second country.

**Team:** founder (sales — walk-in and chains), embedded engineer (part-time; radar tracking + zones), web developer (part-time; config page + report), Shenzhen partner. Data-protection advisor (a few hours) for the works-council/GDPR pack.

**Funding to first 1,000 sets (estimate):** landed hardware excl. cert (1,000 × €27.8) €28k + tooling €12k + certification €16k + prototypes/pilots €5k + 6 months part-time team €35k + sales/demo kits €6k = **≈€102k**. Offsets: pilot conversions (20 × €99) €2k, chain pilot pre-payment €5–15k. Net need **≈€85–95k**. Route: bootstrap + chain pre-payment; retail-innovation/digitalisation grants for SMEs that shops can use to buy it (e.g. state digital-bonus programmes — check current ones); a small angel round from the bakery/POS trade.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** module tracks max 3 targets; prams, kids, people standing close merge into one target | Sell a threshold ("≥3 waiting"), not a count; zone 2 tail sensor; test with prams and kids (the kill question); clear spec sheet |
| **Technical:** glass counters, metal shelving and fridges cause multipath/ghost targets | Mounting guide, zone masking, ghost filtering on dwell/track behaviour; per-site calibration mode |
| **Market:** owners love it in week 1, ignore the lamp in week 6 | Buzzer + lamp; daily report showing "calls answered within 60 s"; daypart thresholds |
| **Regulatory / works council (DE):** a technical device that could monitor staff performance triggers co-determination (BetrVG §87(1)6) even without cameras | Exclude the staff side by design (zones), no per-employee data, written device description for works councils; offer a template agreement |
| **GDPR:** radar positions without identity are likely not personal data, but tracking + timestamps in a small shop could be argued | Process on device, keep only aggregates, no raw tracks stored; customer notice at the door is good practice; DPIA template for chains |
| **Supply:** Hi-Link radar single source (no open files) | Second multi-target module footprint in rev B; buy a year's stock at EVT |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HLK-LD2454 24 GHz multi-target positioning/tracking radar | https://www.gongbans.com/db/hilink-ld2454.html | Tracks up to 3 targets, 8 m, ±60° H/±30° V, 0.72 m resolution, 5 V/50 mA, UART, horizontal wall mount, 34×15 mm | Datasheet public, files via maker (no open schematic) | Buy as module |
| M5Stack Atom-Matrix (C008-B) | https://www.gongbans.com/db/m5stack-atom-matrix.html | ESP32 + 5×5 LED matrix: instant back-office lamp for prototypes and pilots | enclosure/structure only — main-board electronics not published | Prototype/pilot; design your own lamp board for volume |
| HLK-5Mxx 5 W AC-DC | https://www.gongbans.com/db/hilink-5mxx.html | Isolated 230 V → 5 V/1 A for the sensor, 3,000 VAC isolation, CE/RoHS per brochure | Datasheet public, files via maker (no open schematic) | Buy as module; product still needs LVD/EMC tests |

### Block diagram

```
SENSOR (wall, 2.0–2.4 m, facing customers)                BACK OFFICE
230 V ─► HLK-5M05 ─► 5 V ─┬─► LD2454 (≤3 tracks, x/y)      ┌──────────────────────────┐
                          └─► ESP32-C3 ◄─UART──┘           │ ESP32-C3 + LED matrix/bar │
                               zones: queue / tail / staff  │ buzzer + mute             │
                               occupancy + dwell + daypart  │ shows 1 / 2 / 3+ waiting  │
                               thresholds ─── ESP-NOW/Wi-Fi ─► └──────────────────────────┘
                               (opt.) aggregates ─► Wi-Fi ─► daily report e-mail (EU-hosted)
```

**Engineering gap:** zone configuration that a shop owner can do (phone web page with a live dot view), ghost/merge handling, multi-sensor fusion for the tail zone, and a no-cloud default with an optional report.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| HLK-LD2454 | €4–6 | Single source; ask Hi-Link for 1k pricing/lead time |
| ESP32-C3 module ×2 | €2.2 each | Pre-certified |
| HLK-5M05 | €2.0–2.4 | Or a certified USB-C adaptor if mains outlet is near |
| Addressable LEDs ×25, buzzer | €1.3 | |
| Radome-friendly sensor housing + tilt bracket | €2.5 | No metallic paint on the front |
| Lamp housing + certified USB-C adaptor | €4.5 | |

### Firmware/software starting point

- **ESPHome** has an `ld2450` component for Hi-Link's multi-target module; **check whether the LD2454 protocol is supported** — if not, write a UART parser from Hi-Link's protocol document (the frames are simple HEX, per the brochure).
- **ESP-IDF** for production: ESP-NOW for sensor→lamp; a small web server on the sensor for zone setup (live dot view in the browser).
- Report: minimal EU-hosted backend (a few hundred lines) or plain SMTP from the device; aggregates only.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — kill-question test: dev-board sensor + Atom-Matrix lamp in 3 shops for 1 week each, with a manual tally (staff clicker) as reference; 15 owner interviews | "≥3 waiting" decision correct ≥90% of 5-min intervals incl. prams/kids; ≥2/3 shops want to keep it |
| 3–5 | **Works-like** — zone setup page, dayparts, tail-sensor fusion test in one shop | Owner configures zones in <10 min; lamp calls answered faster (measure) |
| 6–8 | **Looks-like + EVT** — rev A sensor + lamp, housings, 20 sets in paid pilots | <1 false call per hour in quiet periods; no missed rush |
| 9–10 | **DVT + pre-compliance** — rev B, RED/EMC/LVD pre-scan, EN 18031 checklist, works-council pack + DPIA template | No pre-scan fails; works-council pack reviewed by a data-protection advisor |
| 11–12 | **Pilot batch** — 50 sets: one chain (5–10 branches) + independents | ≥80% of sites still using lamp after 4 weeks; chain LOI for rollout |

### Certification checklist (EU)

- **CE — RED:** EN 300 440 (24 GHz SRD), EN 300 328 (Wi-Fi/BLE/ESP-NOW), EN 301 489-1/-3/-17, EN 62368-1 (mains sensor unit), EN 62311/EN 62479. Module reports help.
- **LVD:** via EN 62368-1 on the sensor with the integrated AC-DC module (or avoid with a certified external adaptor).
- **EN 18031-1:** internet-connected (Wi-Fi, report) → yes; -2 if the report counts as personal data processing (be conservative). Est. €2–4k.
- **CRA:** product with digital elements; OTA, SBOM, vulnerability contact by Dec 2027.
- **RoHS, REACH, WEEE** (B2B EEE still needs WEEE registration), packaging registration.
- **GDPR:** no images, no identifiers, aggregates only. Still: DPIA template for chains, a customer notice at the door as good practice, staff information. In DE: works-council co-determination for devices suitable to monitor employees — provide the device description and keep staff zones excluded.
- No battery, no MDR, no toy directive.
- **Estimated test costs:** €12–16k.

### Validation toolkit

- **Kill question:** Does the count stay within ±1 person for queues up to 8 in a busy bakery with prams and kids? Given the module tracks max 3 targets, reframe the test honestly: is the "≥3 waiting → call the second till" decision right ≥90% of the time, and does a second (tail) sensor detect longer queues? 3 shops, 1 week each. **Cheapest experiment:** two dev-board sensors, an Atom-Matrix lamp, and a staff clicker for ground truth. Cost < €200 in hardware.
- **Interview script (5) — owners/branch managers:**
  1. When does the queue build, and who notices first?
  2. How many customers walk out in a rush, do you think? How would you know?
  3. What do you do today — bell, shout, a second person on standby?
  4. Would a camera be acceptable to you, your staff and customers? Why/why not?
  5. €129 for a sensor and a lamp in the back — would you buy one today? For all branches?
- **Landing page:** Headline: "Know when to open the second till — before customers walk out." Bullets: "A lamp in the back lights up when the queue builds." / "Radar, not a camera: no images, no faces, nothing stored." / "Fits above the counter in 15 minutes."
- **Pre-order pass:** 2 of 3 test shops pay €99 to keep it, **plus** one chain agrees to a paid 5-branch pilot.

### First production checklist

- **Samples:** 10 sets; golden sample with documented detection performance at 2, 4 and 6 m with 1–3 people.
- **DFM review:** radome (thickness, material, no metal paint), bracket tilt range, cable management at the counter, lamp housing.
- **MOQ talk:** radar modules 500–1k, ESP32-C3 modules (reel), power modules 1k.
- **QC/AQL:** ISO 2859-1 level II, AQL 0.65/2.5; 100% functional test (radar sees a moving target in a test booth, ESP-NOW pairing to its lamp, LED/buzzer check), hipot on sensor units.
- **Packaging:** sensor + lamp pre-paired, install guide with mounting-height diagram, works-council/GDPR leaflet in the box (DE).
- **Incoterms:** FOB Shenzhen; DDP quotes for chains.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2454 24 GHz multi-target positioning and tracking radar module](/db/hilink-ld2454.html) (multi-target positioning radar for the queue zone); [HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C](/db/hilink-5mxx.html) (5 W isolated AC-DC supply). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Atom-Matrix (C008-B)](/db/m5stack-atom-matrix.html) (ESP32 controller with LED matrix as staff signal). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B) — for a Queue Radar

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Queue Radar: A sensor above the till that counts how many people are waiting and lights a 'second till please' lamp in the back office — radar, so there's no camera pointing at customers. The design is built around your HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B).
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
主题：样品订购及批量报价 — HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B) — 用于Queue Radar

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Queue Radar：A sensor above the till that counts how many people are waiting and lights a 'second till please' lamp in the back office — radar, so there's no camera pointing at customers。产品设计基于贵司的HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B)。
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
Subject: PCBA quote from open design files — Queue Radar, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Queue Radar: A sensor above the till that counts how many people are waiting and lights a 'second till please' lamp in the back office — radar, so there's no camera pointing at customers. The design starts from published open-hardware files (HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Queue Radar，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Queue Radar：A sensor above the till that counts how many people are waiting and lights a 'second till please' lamp in the back office — radar, so there's no camera pointing at customers。设计基于已公开的开源硬件文件（HLK-LD2454 24 GHz multi-target positioning and tracking radar module, HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack Atom-Matrix (C008-B)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order 2× HLK-LD2454 (plus an LD2450-class module for comparison), 2× ESP32-C3 dev boards and an M5Stack Atom-Matrix; get raw tracks on a laptop and walk three people through the zone.
2. Ask three bakeries near you for a one-week test in January; offer them the lamp for free if they let you sit in the corner for one morning rush.
3. Write the one-page "what it sees and what it doesn't" for owners, staff and works councils — you'll need it in every sales conversation.

Want help sourcing or building this? Talk to us via www.gongbans.com.
