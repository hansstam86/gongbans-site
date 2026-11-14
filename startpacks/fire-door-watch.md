# Fire-Door Watch — Founder Start Pack

> A LoRaWAN sensor that reports when a fire door is wedged open, for how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Propped-open fire doors are the most common finding in fire inspections. Facility teams walk rounds with a clipboard, find the wedge, remove it, and the door is open again an hour later. There is no record, so the inspector's report becomes a dispute.
- **Customer:** Facility managers of hospitals, schools, universities, offices and housing blocks; fire-safety consultants and facility-services contractors who run the rounds. They pay from a compliance budget; the people who use it are the same team plus the inspector who reads the report.
- **Product:** A battery LoRaWAN door sensor with open-duration thresholds, optional presence detection (to separate "someone walking through" from "wedged open"), 5-year battery, adhesive/screw mount, and a per-building weekly compliance report. €59–79 per door plus a small platform fee (estimate). Explicitly **not** an EN 54 fire-safety device: monitoring only.
- **Why now:** LoRaWAN door sensors cost €16–78 but ship as generic "open/closed" with no compliance logic or report; building regulations and insurers demand evidence of checks; LoRaWAN reaches stairwells and basements that WiFi never will.
- **The ask:** ~€70k to a certified first 1,000 doors; paid pilots with three building owners should fund most of it.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 facility managers deploy 50 doors each in a paid pilot at €69 per door?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Facility managers of hospitals, schools, offices and housing blocks; fire-safety consultants in the EU.

**The problem as the pack states it:** Propped-open fire doors are the most common finding in fire inspections. Facility teams walk rounds with a clipboard, find the wedge, remove it, and the door is open again an hour later. There is no record, so the inspector's report becomes a dispute.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.
- **FPA, Fire Protection Association (UK)** · https://www.thefpa.co.uk/ — fire-safety professionals.
- **r/PropertyManagement** · https://www.reddit.com/r/PropertyManagement/ — property and facility managers.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€59–79 per door + platform, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how facility managers of hospitals, schools, offices and housing blocks deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know right now which fire doors in your building are propped open, and what did your last inspection report say about them?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A LoRaWAN sensor that reports when a fire door is wedged open, how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds. On a scale of one to ten, how likely would you be to buy that at €59–79 per door + platform, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Fire-Door Watch: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Fire-Door Watch: A LoRaWAN sensor that reports when a fire door is wedged open, how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds. Before we spend money on tooling I want to find out whether this solves a real problem for facility managers of hospitals, schools, offices and housing blocks.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €59–79 per door + platform per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

A fire door only works if it is closed. Everyone knows the wedge, the fire extinguisher jammed under the door, the chair. What the facility manager lacks is not awareness but evidence and prioritisation: which of 300 doors are habitually open, when, and whether the self-closer is broken. Generic LoRaWAN contact sensors (Dragino LDS02 ~€16–40, Milesight WS301 ~€52–78) give a raw open/closed stream. Turning that into "door 2.14 was open 3 h 42 min on Tuesday, nobody present, closer likely faulty — 4th week in a row" is the product.

- **Who pays:** the building owner's facility/compliance manager (hospital technical department, school district, university estates, housing association), or the facility-services contractor who sells compliance to them.
- **Who uses:** the same team (weekly report, alerts), plus the external inspector or fire-safety officer who gets a PDF.
- **Who is affected:** nobody needs training; the device is invisible on the door frame.

### Market size (estimates — check)

- **TAM (EU):** fire doors in non-residential buildings — a hospital has hundreds, a school dozens. Rough estimate: 50–100M fire doors in EU non-residential stock. At €69 → **€3–7B** theoretical hardware, nonsense as a target but it says the pool is unlimited.
- **SAM (buildings with a professional facility team and a LoRaWAN-friendly structure: hospitals, universities, large offices, social housing in DACH/Benelux/Nordics/UK):** ~2–4M "problem doors" (those actually found propped) → **€150–300M** hardware plus platform.
- **SOM (3 yrs):** 0.5% of SAM → **10–20k doors**. Year 1: 1,000–2,000 doors across 5–10 buildings.

### Competition (2 searches)

| Alternative | What it is | Why we still win |
|---|---|---|
| Clipboard rounds / do nothing | The status quo; the inspector finding is the "cost" | Continuous evidence, and the data finds the broken closers |
| Generic LoRaWAN contact sensors (Dragino LDS02 €16–40, Milesight WS301 €52–78, Netvox R311A) + an integrator's dashboard | Open/closed events | No duration logic, no presence, no compliance report; integrator builds it per project at €€€ |
| Door-sensor platforms (Connect IoT, Connect ONE, Zenner "monitoring of doors and windows") | Multi-sensor building platforms with logs | Horizontal, priced for whole-building deployments; we are a vertical, per-door, report-first product |
| Hold-open devices with alarm (magnetic hold-opens wired to the fire alarm) | Legitimate hold-open with release | Expensive, needs electrician; we monitor doors that must simply stay shut |
| Fire-alarm system door monitoring (EN 54 ecosystems) | Certified, wired | Costly retrofit; we are the cheap layer for everything the alarm system does not watch |

**Wedge:** vertical compliance product: the report, the thresholds and the "faulty closer" inference, priced per door, deployable by the facility team themselves in an afternoon.

### Product & value proposition

- Two-part reed/magnet sensor on frame and door leaf; main unit ~80×30×20 mm, 2× AA lithium or 1× AA Li-SOCl2 for 5 years (estimate at 15-minute heartbeats plus event uplinks).
- Open-duration thresholds (e.g. >2 min = propped), presence optional via a TMOS-type IR sensor to classify "traffic" vs "propped-nobody-there" — also catches a broken self-closer (door never closes fully: separate "ajar" magnet position).
- Weekly PDF per building, live alerts to the team, inspector export, API.
- **Pricing (estimates):** €69 per sensor (€59 at 500+), platform €0.50/door/month (or €6/door/year prepaid), gateway (off-the-shelf, resold) €249 if the building has no LoRaWAN coverage. Pilot pack: 50 doors + gateway + 12 months platform = €3,990.

### Unit economics (estimates, EUR per unit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C6+LoRa core or pre-cert LoRaWAN module €6–8, reed switch + magnet €0.8, optional TMOS IR presence €3 (SKU option), battery holder €0.5, antenna €0.8, PCB €0.7) | 11.5 (base) | 9.5 |
| PCBA + test | 2.0 | 1.3 |
| Enclosure (ABS two-part, adhesive pad, screws) | 2.0 | 1.3 |
| Packaging (10-pack boxes, batteries included) | 1.5 | 1.0 |
| Battery (AA lithium) | 1.8 | 1.5 |
| Freight + duty to EU | 1.2 | 0.6 |
| Certification amortised (€14k) | 14.0 | 2.8 |
| **Landed cost** | **34.0** | **18.0** |
| Net price direct B2B (€69 ex VAT, pallet-shipped) | 69 | 69 |
| **Gross margin direct** | **€35 (51%)** | **€51 (74%)** |
| Via facility-services reseller at 30% off (€48 net) | €14 (29%) | €30 (62%) |

Platform revenue (€6/door/year) is what makes the reseller channel fine: at 10k doors it is €60k/year recurring with near-zero marginal cost.

### Go-to-market

**First 100 customers (first 1,000 doors):** three buildings — one hospital technical department, one university estates team, one housing association with stairwell issues. Pilot pack at €3,990 with a 90-day refund. Find them via fire-safety consultants (Brandschutzbeauftragte in DE; brandveiligheidsadviseurs in NL) who already write the inspection reports and would love a data appendix.

**Then scale:** fire-safety consultancies and facility-services companies as resellers; LoRaWAN operator marketplaces; insurers (property insurers' loss-prevention teams); hospital procurement groups; the UK (where fire-door inspection regimes are strict — but note UKCA rules).

### 12-month plan

- **Q1:** 20 pilot nodes from Stamp C6LoRa + Grove magnetic switch + LoRaWAN Unit in printed boxes on real doors; dashboard MVP with weekly PDF.
- **Q2:** own PCB rev A, enclosure, 100-node EVT across two buildings; presence SKU trial.
- **Q3:** certification; 1,000-node production; reseller agreements with two consultancies.
- **Q4:** insurer pilot, gateway bundle, inspector export format agreed with one authority.

**Team:** embedded/LoRaWAN engineer (full), web/backend developer (half), founder with facility-management network, fire-safety consultant (advisory days). Shenzhen partner for PCBA and enclosure.

**Funding to first 1,000 doors (estimate):** landed hardware excl. cert €20k + tooling €6k + certification €14k + pilots/gateways €6k + 6 months team €45k + sales/travel €5k = **≈€96k**; three pilot packs (€12k) plus prepaid first orders (say 600 doors × €59 = €35k) reduce the external need to **≈€45–55k**. Route: paid pilots + bootstrap; building-safety/digitalisation grants (regional); angel only if an insurer or hospital group signs a frame agreement.

### Top risks

| Risk | Mitigation |
|---|---|
| **Regulatory:** being mistaken for a fire-safety device (EN 54) | Clear labelling "monitoring aid, not a fire-safety component"; no claims about life safety; legal review of marketing text |
| **Market:** procurement wants a whole-building platform | Partner with existing LoRaWAN building platforms via API; stay the best door-compliance app |
| **Technical:** LoRaWAN coverage in stairwells/basements | Pilot includes a coverage survey; bundle an indoor gateway; adaptive data rate |
| **Technical:** magnet alignment on heavy steel doors, false "ajar" | Wide-gap reed, metal spacer in the kit, calibration at install via button |
| **Supply:** LoRa module allocation | Two approved modules (own C6+SX126x path and a pre-certified module) |

GDPR: presence detection is binary and not identifying; keep it that way and document it.

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Seeed Grove-Magnetic Switch | https://www.gongbans.com/db/seeed-grove-magnetic-switch.html | Door reed-switch reference circuit | schematic | Seeed wiki — check |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | ESP32-C6 + LoRa core, open Altium PCB + schematic — the node core | pcb, schematic | M5_Hardware repo — check licence |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | EU868 LoRaWAN uplink module for pilots | enclosure/structure only | Module; production via C6LoRa path or a pre-certified module |
| M5Stack Unit TMOS PIR (U185) | https://www.gongbans.com/db/m5stack-unit-tmos-pir.html | Presence detection (stationary human presence) next to the door — optional SKU | enclosure/structure only | Module for pilots; source the TMOS sensor directly for production |

Catalogue honesty: chip fields are empty for these M5 rows; the LoRa transceiver and the TMOS sensor part numbers must be read from M5 docs/schematics.

### Block diagram

```
AA lithium ──► LDO 3.3V ──► ESP32-C6 (deep sleep; RTC wake)
     reed switch (frame/leaf) ──► GPIO interrupt (open/close timestamps)
     optional TMOS IR presence ──► I²C/interrupt (presence while open)
     ESP32-C6 ──► LoRa EU868 ──► LoRaWAN network (public or own gateway) ──► backend
Backend: per-door state machine → thresholds → alerts; weekly PDF per building; inspector export
```

**Engineering gap:** power budget for 5 years (event-driven uplinks plus a 15-minute heartbeat), the state machine (traffic vs propped vs ajar vs faulty closer), magnet mechanics on steel doors, and a report inspectors accept.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-C6 module + SX1262-class LoRa, or pre-certified LoRaWAN module | €6–8 | Module route halves RED test scope |
| Wide-gap reed switch + magnet (two magnet positions for "ajar") | €0.8 | |
| TMOS-type IR presence sensor (optional SKU) | €3 | **Few sources**; verify part from M5 docs |
| AA Li-FeS2 or Li-SOCl2 cell + holder | €2.3 | Li-SOCl2 for 5 years; check transport rules |
| 868 MHz antenna (PCB/helical) | €0.8 | |
| PCB 2-layer | €0.7 | |
| ABS enclosure + magnet housing + adhesive + screws | €2.0 | Tooling €6–8k |

### Firmware/software starting point

- **ESP-IDF** on ESP32-C6; LoRaWAN via **RadioLib** or Semtech **LoRaMac-node**; pilot with the M5 Unit over its documented command interface.
- Network: **The Things Stack** or **ChirpStack**; payload decoder published.
- Backend: Node-RED for the pilot; a small Python/Go service with Postgres for production; PDF via WeasyPrint/ReportLab (exist).
- Dashboard: Grafana for the pilot; a simple web app for the product.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 calls to facility managers/fire consultants; 3 pilot LOIs; 5 pilot nodes (Stamp C6LoRa + Grove magnetic + LoRaWAN Unit) on real doors | ≥3 managers commit to a paid 50-door pilot at €69/door; nodes uplink reliably from a stairwell |
| 3–5 | **Works-like** — 20 nodes in one building, state machine, weekly PDF | ≥95% event capture vs manual log over 2 weeks; first "faulty closer" caught |
| 6–8 | **Looks-like + EVT** — rev A PCB, enclosure, magnet kit, 100 units; sleep current profile | Average current supports ≥5 years (estimate ≤15 µA sleep, <20 uplinks/day) |
| 9–10 | **DVT + pre-compliance** — rev B, EN 300 220 + EMC pre-scan, EN 18031 checklist, drop test | Radio within limits with margin; checklist complete; adhesive holds 30 days on painted steel |
| 11–12 | **Pilot batch** — 150 nodes across 3 buildings, gateway bundles, training sheet | ≤2% failures; 2 of 3 pilots convert to 300+ doors; a consultant signs as reseller |

### Certification checklist (EU)

- **CE — RED:** EN 300 220-2 (LoRa), EN 301 489-1/-3, EN 62368-1 (battery device): €8–12k; a pre-certified module reduces radio tests.
- **EN 18031:** internet-connected via LoRaWAN → assume in scope; self-assessment (no personal data, no payments) €2–3k.
- **CRA:** SBOM, update path (FUOTA or local), disclosure contact.
- **RoHS, WEEE (B2B), REACH, packaging.**
- **Battery Regulation:** lithium primary cells → producer registration, labelling; design for removal.
- **GDPR:** presence is binary and unidentified; document it; building owner is the controller.
- **Not EN 54 / Construction Products Regulation:** do not claim fire-safety function; put it in writing.
- **Total estimate:** €12–16k.

### Validation toolkit

- **Kill question:** Do 3 facility managers deploy 50 doors each in a paid pilot at €69 per door? Cheapest experiment: a one-page pilot offer plus five hand-built nodes in your own building to show live data on a call.
- **Interview script (5):** 1) How many fire doors do you have and how do you check them today? 2) What did the last inspection report say about doors, and what did it cost you? 3) Which doors are chronically propped, and why (workflow, heat, deliveries)? 4) Who would receive an alert, and what would they do in the next 10 minutes? 5) €69 per door plus €6/year — yes, no, or "only if it integrates with X"?
- **Landing page:** Headline: "Every fire door, every hour, on record." Bullets: "Know which doors are wedged open — and for how long." / "Finds broken self-closers before the inspector does." / "Battery LoRaWAN sensor, installed by your own team in minutes."
- **Pre-order pass:** 3 paid pilots (≥150 doors) signed within 6 weeks.

### First production checklist

- Samples: 5 PCBAs from two assemblers; **golden sample** with magnet kit; reed gap tested on a steel door jig.
- DFM: enclosure snap vs screws, battery contact spring, adhesive area, antenna clearance from steel.
- MOQ: PCBA 500; enclosure 1k shots (negotiate 500); batteries from EU stock to avoid shipping lithium.
- QC/AQL: Z1.4 II, AQL 1.0/2.5; 100% test: reed trigger, LoRa join on a bench gateway, current draw in sleep.
- Packaging: 10-packs; lithium battery marking if shipped installed; EU DoC + WEEE marks.
- Incoterms: FOB Shenzhen sea for nodes; batteries sourced in EU; pilot by air DAP.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Seeed Studio and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Magnetic Switch](/db/seeed-grove-magnetic-switch.html) (door reed-switch reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN uplink); [M5Stack Unit TMOS PIR (U185)](/db/m5stack-unit-tmos-pir.html) (optional presence detection next to the door). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.
- **ManThink** · https://www.manthink.cn/ — open-source LoRaWAN gateway (direct supplier submission): [ManThink GD6 open-source LoRaWAN gateway](/db/manthink-gd6-lorawan-gateway.html). Supplier reference price (Nov 2026, GD61 indoor, 8 channels): basic Ethernet/Wi-Fi US$50; 4G+PoE US$70; global 4G+PoE US$87; power kit +US$5. MOQ and lead time on request.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **RAK Wireless** (深圳锐凌无线技术有限公司) · rakwireless.com — LoRaWAN gateway / module OEM: RAK2245 / RAK4630 LoRaWAN; Helium compatible; CE/FCC; OEM. *(LoRaWAN gateways / modules)*
- **Dragino Technology** (创联技术(深圳)有限公司) · dragino.com — LoRaWAN gateway / sensor OEM: LG308 LoRa gateway; LHT65 temp/humidity sensor; open-source firmware OEM. *(LoRaWAN gateways / modules)*

### MOQ and landed cost

Apart from the ManThink reference price above, gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Seeed Studio and M5Stack websites)

```email
Subject: Sample order and volume pricing — Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185) — for a Fire-Door Watch

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Fire-Door Watch: A LoRaWAN sensor that reports when a fire door is wedged open, how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds. The design is built around your Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185).

Could you please send:
1. Price and lead time for [10] sample units of each: Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185).
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
主题：样品订购及批量报价 — Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185) — 用于Fire-Door Watch

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fire-Door Watch：A LoRaWAN sensor that reports when a fire door is wedged open, how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds。产品设计基于贵司的Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185)。
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
Subject: PCBA quote from open design files — Fire-Door Watch, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Fire-Door Watch: A LoRaWAN sensor that reports when a fire door is wedged open, how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds. The design starts from published open-hardware files (Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Fire-Door Watch，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Fire-Door Watch：A LoRaWAN sensor that reports when a fire door is wedged open, how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds。设计基于已公开的开源硬件文件（Seeed Grove-Magnetic Switch, M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), M5Stack Unit TMOS PIR (U185)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Draft the pilot offer (50 doors + gateway + 12 months platform = €3,990, 90-day refund) and call five facility managers and three fire-safety consultants.
2. Order Stamp C6LoRa ×5, Unit LoRaWAN-EU868 ×5, Grove Magnetic Switch ×5, Unit TMOS PIR ×2; register on The Things Stack; put a node on the nearest fire door and record a week.
3. Write the one-paragraph legal positioning ("monitoring aid, not an EN 54 component") and have a fire-safety consultant and a lawyer read it.

Want help sourcing or building this? Talk to us via www.gongbans.com.
