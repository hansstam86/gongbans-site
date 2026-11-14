# Fire-Door Watch — Founder Start Pack

> A LoRaWAN sensor that reports when a fire door is wedged open, for how long, and whether anyone is nearby — the compliance log facility managers currently collect on clipboard rounds.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Propped-open fire doors are the most common finding in fire inspections. Facility teams walk rounds with a clipboard, find the wedge, remove it, and the door is open again an hour later. There is no record, so the inspector's report becomes a dispute.
- **Customer:** Facility managers of hospitals, schools, universities, offices and housing blocks; fire-safety consultants and facility-services contractors who run the rounds. They pay from a compliance budget; the people who use it are the same team plus the inspector who reads the report.
- **Product:** A battery LoRaWAN door sensor with open-duration thresholds, optional presence detection (to separate "someone walking through" from "wedged open"), 5-year battery, adhesive/screw mount, and a per-building weekly compliance report. €59–79 per door plus a small platform fee (estimate). Explicitly **not** an EN 54 fire-safety device: monitoring only.
- **Why now:** LoRaWAN door sensors cost €16–78 but ship as generic "open/closed" with no compliance logic or report; building regulations and insurers demand evidence of checks; LoRaWAN reaches stairwells and basements that WiFi never will.
- **The ask:** ~€70k to a certified first 1,000 doors; paid pilots with three building owners should fund most of it.

## 2. Business plan

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

## 3. Start kit

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

## 4. Next steps (this week)

1. Draft the pilot offer (50 doors + gateway + 12 months platform = €3,990, 90-day refund) and call five facility managers and three fire-safety consultants.
2. Order Stamp C6LoRa ×5, Unit LoRaWAN-EU868 ×5, Grove Magnetic Switch ×5, Unit TMOS PIR ×2; register on The Things Stack; put a node on the nearest fire door and record a week.
3. Write the one-paragraph legal positioning ("monitoring aid, not an EN 54 component") and have a fire-safety consultant and a lawyer read it.

Want help sourcing or building this? Talk to us via www.gongbans.com.
