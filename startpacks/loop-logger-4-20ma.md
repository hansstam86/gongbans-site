# 4–20 mA Loop Logger (LoRaWAN) — Founder Start Pack

> A DIN-rail or field box that reads any legacy 4–20 mA sensor (level, pressure, flow) and sends it over LoRaWAN — turning thirty-year-old instrumentation into IoT without touching the control loop.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of 4–20 mA transmitters hang on tanks, pipes and pumps across Europe, wired to a local gauge or a PLC that nobody can reach remotely. Replacing them with "smart" sensors costs thousands per point; the operator just wants the value on a dashboard and an alarm on the phone.
- **Customer:** Small water utilities and water boards, greenhouses, breweries, food plants, biogas and small process plants, and above all the **system integrators** who serve them. Integrators buy; plant operators use.
- **Product:** A two-channel 4–20 mA (and 0–10 V) to LoRaWAN node in a DIN-rail housing (24 V powered, can power the loop) and an IP65 field version (5-year battery or loop-powered pass-through), on-node threshold alarms, a standard payload codec, and a no-nonsense configuration tool. €149–199 (estimate).
- **Why now:** LoRaWAN coverage (public and private) is mature; competitors exist (Milesight UC300 at ~€125 net EU868 with 2× 4–20 mA plus lots more; Dragino PS-LB ~€56–94; Sentinum AION420; Enless; Radio Bridge) — so this is a crowded but fragmented market where a sharper, cheaper, integrator-friendly node with a loop-powered trick still wins deals.
- **The ask:** ~€60k to a certified first 1,000 nodes; integrator pilot orders carry most of it.

## 2. Business plan

### Problem & customer

Retrofit beats replacement when budgets are tight. The transmitter already works; it just talks 4–20 mA to a thing on the wall. The retrofit node sits in series (loop pass-through, so the existing PLC keeps reading) or reads a spare transmitter. The integrator wants: a node that installs in 10 minutes, a decoder that drops into their network server, and a datasheet that answers the water board's questions (isolation, IP rating, battery life, alarm behaviour).

- **Who pays:** system integrators (10–100 nodes per project) and directly small utilities/greenhouses with an in-house technician.
- **Who uses:** plant operators (dashboard/alarm), maintenance (battery/replace).
- **What they compare:** Milesight UC300 (feature-rich, DC-powered, €125 net), Dragino PS-LB (cheap, battery), Sentinum AION420 (loop-through, DE-made, premium), Enless TX 4/20 mA (5-year battery).

### Market size (estimates — check)

- **TAM:** installed 4–20 mA transmitters in the EU — no public figure found; analyst-style guesses run into tens of millions of loops. Take **20M** as a working number; 10% worth connecting → 2M points → at €169 **€340M** hardware, plus services.
- **SAM (small/mid operators and integrators in DACH/Benelux/Nordics/FR/IT where LoRaWAN is strong; water, agri, food, biogas):** ~300–500k points → **€50–85M**.
- **SOM (3 yrs):** 1% → **3–5k nodes**. Year 1: 800–1,500 via 5–10 integrators.

### Competition (2 searches)

| Alternative | Price (listings, approx.) | Why we still win |
|---|---|---|
| Milesight UC300 (EU868) | ~€125 net; 2× 4–20 mA, 2× 0–10 V, PT100, RS-485, relays | Over-featured and DC-only; our field SKU is battery/loop-powered and IP65; our DIN SKU is simpler and cheaper to configure |
| Dragino PS-LB / CS01-LB | ~€56–94 / ~€150 | Hobby-grade enclosures and docs; integrators want a datasheet, isolation and support in EU time zones |
| Sentinum AION420 (loop-through, mioty/LoRaWAN) | premium (quote) | We undercut with the same loop-through trick |
| Enless TX 4/20 mA, Radio Bridge 4–20 mA, Netvox | €100–200 | Fragmented; none owns the integrator relationship with an open codec + config tool |
| Replace the transmitter with a native LoRaWAN sensor | €300–1,500 per point | Retrofit is 5× cheaper and keeps the loop |
| Do nothing (manual rounds, local gauge) | Free | Alarm on phone pays for itself at the first overflow |

**Wedge:** loop-powered pass-through + 2 channels + on-node alarms + integrator tooling (codec, batch config, white-label label) at €149–199, from an EU company with a real datasheet.

### Product & value proposition

- **DIN SKU:** 2× 4–20 mA (16-bit, isolated), 2× 0–10 V, 24 V in, can source 24 V loop power for 2 transmitters, 1 digital input (pulse/flow), LoRaWAN EU868 (SMA antenna), USB-C config.
- **Field SKU:** IP65 polycarbonate box, 1–2 channels, loop pass-through (steals <2 V from the loop, with battery backup) or 5-year battery with transmitter power pulsing (warm-up timing configurable), cable glands.
- On-node: sampling interval, thresholds with hysteresis, rate-of-change alarms, immediate uplink on alarm, daily heartbeat with battery and loop status.
- Tooling: NFC/USB config app, CSV batch provisioning, published codec for TTN/ChirpStack/Actility/Loriot, Modbus-to-LoRaWAN later.
- **Pricing (estimates):** DIN €149, field battery €179, field loop-powered €199; integrator tiers −20/−30%; 10-pack pilot €1,490.

### Unit economics (estimates, EUR per unit; DIN SKU)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C6+LoRa core or pre-cert LoRaWAN module €7, 16-bit ADC + precision shunts + isolation €5, 24 V in + loop-power boost €3, protection/TVS €1, terminals €2.5, SMA + antenna €2, PCB €1.5) | 22.0 | 18.5 |
| PCBA + calibration test | 4.0 | 2.6 |
| Enclosure (DIN 3–4 TE housing; field: IP65 box + glands) | 4.0 (DIN) | 3.0 |
| Packaging + label + quick guide | 1.5 | 1.1 |
| Freight + duty to EU | 1.5 | 0.8 |
| Certification amortised (€18k incl. industrial EMC) | 18.0 | 3.6 |
| **Landed cost** | **51.0** | **29.6** |
| Net price integrator (−25%: €112 ex VAT) | 112 | 112 |
| **Gross margin integrator** | **€61 (54%)** | **€82 (74%)** |
| Direct (€149 ex VAT) | €98 (66%) | €119 (80%) |

The precision front end (ADC, shunts, isolation) is where you must not save; the LoRa module is the lead-time risk.

### Go-to-market

**First 100 customers (first 1,000 nodes):** five integrators — one water (a small water board's contractor), one greenhouse automation firm, one brewery/food automation shop, one biogas service company, one LoRaWAN network operator's partner. 10-unit pilot packs at €1,490. Find them in The Things Industries partner list, LoRa Alliance member list, regional automation associations, Hannover Messe/SPS/Aquatech visitor lists (search).

**Then scale:** distributors of IoT hardware in the EU (the usual LoRaWAN webshops that already list Milesight/Dragino — get listed), network operators' marketplaces, instrumentation distributors (they sell the transmitters — add the node), OEM/white-label for pump and tank makers.

### 12-month plan

- **Q1:** works-like on Stamp C6LoRa + Unit AIN4-20mA in a DIN base; codec; 5 integrator pilots (hand-built).
- **Q2:** own PCB (precision front end, isolation, loop power), DIN housing; 50-unit EVT; field IP65 prototype.
- **Q3:** certification (RED + industrial EMC), 1,000 DIN production; config tool v1.
- **Q4:** field SKU production; distributor listings; white-label talk with one tank/pump OEM.

**Team:** embedded engineer with analogue skills (full), firmware/LoRaWAN (half), founder with integrator network, technical writer (contract — the datasheet sells). Shenzhen partner for PCBA with calibration fixture and housings.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €33k + calibration fixture/tooling €8k + certification €18k + pilots €5k + 6 months team €45k + fairs/marketing €8k = **≈€117k**; five pilot packs (€7.5k) and integrator pre-orders (500 × €112 = €56k) bring the external need to **≈€50–60k**. Route: integrator pre-orders + bootstrap; regional industrial-IoT/water-innovation grants; angel optional.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** crowded; Milesight/Dragino are cheap and everywhere | Win on loop-powered pass-through, datasheet quality, EU support, integrator tooling; do not try to beat Dragino on price alone |
| **Technical:** loop-powered pass-through must not disturb the control loop (voltage burden, startup transient) | Design for <2 V burden, soft-start, pass-through even when the node is dead (fail-safe short); test on real PLC inputs |
| **Technical:** accuracy and drift (claim 0.1% FS) | 16-bit ADC, precision shunt, factory calibration with stored coefficients |
| **Regulatory:** industrial EMC (EN 61326 class) and surge on long cables | Isolation, TVS, pre-scan early; budget a re-test |
| **Supply:** LoRa module allocation | Two approved module paths |

## 3. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit AIN4-20mA (U162) | https://www.gongbans.com/db/m5stack-unit-ain4-20ma.html | 4–20 mA input reference for the pilot | enclosure/structure only | Module for prototypes; own precision front end for production |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | ESP32-C6 + LoRa core with open Altium PCB and schematic — the node core | pcb, schematic | M5_Hardware repo — check licence |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | EU868 LoRaWAN stack module for pilots | enclosure/structure only | Module; production via C6LoRa path or a pre-certified module |
| M5Stack Base DIN (M132) | https://www.gongbans.com/db/m5stack-base-din.html | DIN-rail mounting reference | enclosure/structure only | Mechanical reference |

Catalogue honesty: the AIN4-20mA Unit's ADC resolution and isolation are not in the catalogue — check M5 docs; it is a pilot part, not your front end.

### Block diagram

```
24 V DC in (DIN) | loop pass-through / battery (field) ──► power stage (+ loop-power boost 24 V)
     2× 4–20 mA ──► precision shunt ──► isolated 16-bit ADC ──► ESP32-C6
     2× 0–10 V, 1× digital/pulse input ──► ESP32-C6
     ESP32-C6 ──► LoRa EU868 (SMA) ──► LoRaWAN NS (TTN/ChirpStack/Actility/Loriot) ──► integrator dashboard
     USB-C / NFC config ; on-node thresholds, hysteresis, heartbeat
```

**Engineering gap:** the analogue front end (accuracy, isolation, surge), loop-powered pass-through that fails safe, battery/transmitter warm-up timing, and the integrator tooling (codec, batch config).

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-C6 module + SX1262-class LoRa or pre-certified LoRaWAN module | €7 | **Lead-time item**; two paths |
| 16-bit ADC (ADS1115/ADS1120-class) + 0.1% shunts | €3 | |
| Isolation (digital isolator or isolated DC/DC) | €2.5 | For the DIN SKU; field SKU single-channel may skip |
| 24 V input + loop-power boost (24 V, 50 mA) | €3 | |
| TVS/surge protection, PTC | €1 | Long cables = surges |
| Pluggable screw terminals | €2.5 | |
| SMA connector + 868 MHz antenna | €2 | |
| DIN 3–4 TE housing / IP65 PC box + glands | €4 / €9 | Standard parts |
| Field battery: Li-SOCl2 D cell | €6 | Transport rules apply |

### Firmware/software starting point

- **ESP-IDF** on ESP32-C6; LoRaWAN via **RadioLib** or Semtech **LoRaMac-node**; pilot with the M5 LoRaWAN Unit.
- Network: **The Things Stack**, **ChirpStack**; codecs in JavaScript per the LoRa Alliance payload codec API; **Cayenne LPP** optional.
- Config tool: a desktop/web app over USB serial (Web Serial) — simple; NFC later.
- Dashboard for pilots: Node-RED + InfluxDB + Grafana.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 integrator calls; 3 pilot LOIs; 3 pilot nodes (Stamp C6LoRa + Unit AIN4-20mA + LoRaWAN Unit in a DIN base) on a pressure transmitter | ≥5 integrators commit to a 10-unit pilot at €1,490 within 6 weeks |
| 3–5 | **Works-like** — 15 pilot nodes at 3 sites, codec, alarms | Readings within 1% of the PLC value; alarms arrive <2 min; uptime >99% |
| 6–8 | **Looks-like + EVT** — rev A PCB (precision front end, isolation, loop power), DIN housing, 30 units; calibration fixture | Accuracy ≤0.2% FS after calibration; loop burden <2 V; fail-safe pass-through verified |
| 9–10 | **DVT + pre-compliance** — rev B, EN 300 220 + industrial EMC pre-scan (surge, ESD, RF immunity), EN 18031 checklist, datasheet v1 | No fails or a fix plan; datasheet reviewed by 2 integrators |
| 11–12 | **Pilot batch** — 50 units to 5 integrators, config tool beta | ≤2 failures; 3 of 5 integrators place a 50+ order; field SKU EVT started |

### Certification checklist (EU)

- **CE — RED:** EN 300 220-2, EN 301 489-1/-3, safety via **EN 62368-1** or **EN 61010-1** depending on classification (industrial measuring equipment — ask the lab): €9–13k.
- **Industrial EMC:** EN 61326-1 (immunity/emissions for measurement equipment) is what integrators and water boards ask for: +€4–6k.
- **EN 18031-1** (internet-connected via LoRaWAN): self-assess: €2–3k.
- **CRA:** SBOM, local update over USB, disclosure contact; 10-year support plan.
- **RoHS, WEEE (B2B), REACH, packaging.**
- **Battery Regulation** for the field SKU (Li-SOCl2 primary): registration, labelling, removability; transport paperwork.
- **GDPR:** none.
- **ATEX:** not covered — say explicitly "not for hazardous areas".
- **Total estimate:** €16–22k (both SKUs €22–28k).

### Validation toolkit

- **Kill question:** Do 5 system integrators each order a 10-unit pilot at €169 within 6 weeks? Cheapest experiment: a datasheet PDF, a codec on GitHub, and three hand-built nodes you can demo on a call.
- **Interview script (5):** 1) Which 4–20 mA points do your customers want remote, and why haven't they done it? 2) Which LoRaWAN nodes do you use today and what annoys you about them? 3) Loop-powered pass-through vs battery vs 24 V — which do you actually need? 4) What must the datasheet say for a water board to approve it (isolation, IP, accuracy, battery)? 5) €112 net for the DIN node, €149 field — margin OK, and would you white-label?
- **Landing page:** Headline: "Your old 4–20 mA sensors, on LoRaWAN, in ten minutes." Bullets: "Two channels, loop-powered or 24 V, keeps your PLC reading." / "On-node alarms, 5-year battery, IP65 field box." / "Open codec for TTN, ChirpStack, Actility, Loriot."
- **Pre-order pass:** ≥5 integrators × 10-unit pilot packs within 6 weeks.

### First production checklist

- Samples: 5 PCBAs with calibration fixture from the assembler; **golden sample** with calibration certificate.
- DFM: terminal torque, isolation gaps, antenna connector strain, gland sealing on the field SKU.
- MOQ: PCBA 500; DIN housings 500; IP65 boxes 300; LoRa modules reel.
- QC/AQL: Z1.4 II, AQL 0.65 major / 2.5 minor; 100% calibration at 4, 12, 20 mA, LoRa join, loop-power check.
- Packaging: quick guide with wiring diagrams; EU DoC + WEEE; batteries shipped separately for the field SKU.
- Incoterms: FOB Shenzhen sea; pilots by air DAP.

## 4. Next steps (this week)

1. Write the two-page datasheet (specs you intend to hit, honestly marked "target") and the JavaScript codec; put both on a landing page.
2. Order Stamp C6LoRa ×3, Unit AIN4-20mA ×3, Unit LoRaWAN-EU868 ×3, Base DIN ×3; wire one to a pressure transmitter and uplink to The Things Stack.
3. Call 10 integrators from the LoRaWAN partner lists with the pilot-pack offer; aim for 3 LOIs.

Want help sourcing or building this? Talk to us via www.gongbans.com.
