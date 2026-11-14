# Hay Spear — Founder Start Pack

> A one-metre temperature spear with LoRaWAN that lives inside the hay or straw stack and warns the farmer before self-heating turns into a barn fire.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Hay and straw stored too wet heat up by microbial action; above ~50–60 °C the stack can ignite. Farmers probe by hand for a week after harvest, then stop. Barns, machinery and animals burn every summer; insurers in the alpine countries already expect temperature monitoring of self-igniting stores.
- **Customer:** Livestock and arable farms with hay/straw storage in DE/AT/CH/NL/FR; agricultural insurers and farm-supply dealers as channels. The farmer pays €169 per spear (or the insurer co-funds); the farmer and the family use the alarm.
- **Product:** stainless 1 m spear with 3 sensing depths, IP67 head, EU868 LoRaWAN, 5-year primary cell, threshold and rate-of-rise alarms by app/SMS; farmyard gateway bundle for farms without coverage.
- **Why now:** Open ESP32-C6 + LoRa core exists with PCB and schematic; LoRaWAN modules are cheap; the one established wireless system is a 10-probe starter kit with a reader and a subscription at a four-figure price.
- **The ask:** ~€70k to the first 1,000 spears; pre-orders at fairs plus one insurer partnership.

## 2. Business plan

### Problem & customer
Self-heating is slow, invisible and well understood: moisture >18–20% at baling, microbial growth, 40 °C in days, 60 °C in two weeks, and from ~70 °C a real fire risk. Prevention is boring: measure every day for 6–8 weeks after storing. Nobody does — so the stack gets probed when it smells. Insurers' loss-prevention departments know this (self-ignition is ~9–10% of farm fires by number in the sources found; no central statistic exists in Germany) and the Austrian rules quoted by the chambers of agriculture require temperature monitoring of self-igniting materials.

Who pays: the farmer (a €169 spear is cheap against a €200k barn), or the insurer as a loss-prevention subsidy (they already pay for lightning protection and fire extinguishers). Who uses: whoever has the phone — the alarm must work by SMS/app with no IT skills.

### Market size (estimates — check them)
- **TAM:** farms with hay/straw storage: DE ~130,000 livestock farms, AT ~90,000, CH ~45,000, NL ~30,000, FR ~200,000 → ~500,000 farms; average 3 spears + gateway for half of them → **~€300 M** one-off hardware potential.
- **SAM:** alpine/dairy regions with loose-hay stacks and bale barns, reached through 4–6 farm dealers and 2–3 insurers: ~80,000 farms × 3 spears × €169 ≈ **€40 M**, replacement every 5 years.
- **SOM (3 years):** 8,000 spears + 1,500 gateways ≈ **€1.8 M revenue**.

### Competition (3 searches)
| Alternative | Price (est.) | Weakness |
|---|---|---|
| Hand probe thermometer (1–2 m, analogue or digital) | €60–250 | Manual, stops after a week |
| Quanturi Haytech (40 cm probes, 433/868 radio, reader with 2G/Ethernet, premium service) | ~£600–1,200 for 10 probes + reader + 1 yr service | Starter-kit sizing, subscription, short probe; strong in big operations |
| Consumer Bluetooth logger in a PVC pipe (DIY) | €15 | Range of 10 m, no alarm away from the barn |
| Industrial stack-monitoring lances (IP67, 1.8 m) | several hundred € each | Wired, installer product |
| Do nothing — sniff and hope | €0 | Barn fires |

**Wedge:** a 1 m spear with three depths (the core heats first), LoRaWAN that reaches across the yard and into public networks, buy-once pricing (no subscription for alarms), and insurer co-funding.

### Product & value proposition
- **Spear:** 1,000 mm × 20 mm stainless tube, pointed, three digital temperature sensors at 30/60/90 cm, PA66 head with IP67 seal and a loop for pulling out, LED + button.
- **Radio:** EU868 LoRaWAN class A; joins public networks (TTN or operator) or the farm's own gateway; 15-minute uplinks, immediate alarm uplink on rate-of-rise.
- **Power:** primary lithium (Li-SOCl2 C-cell), target 5 years.
- **Service:** free app and SMS alarms (bundled SMS budget); optional €2/month per farm for history and reports after year 1 — optional, not required for alarms.
- **Pricing:** **€169 incl. VAT per spear** (€142 ex-VAT); 3-spear pack + gateway **€599**; insurer/dealer price €119 ex-VAT at 50+.

### Unit economics (estimates, per spear)
| Item | 1,000 units | 5,000 units |
|---|---|---|
| Electronics BOM (ESP32-C6 + LoRa module €8, 3 sensors €3, PCB, antenna, cell €4) | €24 | €19 |
| Assembly & test (incl. LoRa join test, sensor check in a water bath) | €6 | €4 |
| Spear tube + tip + head enclosure + seal | €16 | €11 |
| Packaging, manual, QR card | €2.50 | €1.60 |
| Freight + duty to EU (1 m long — ship by sea; air is painful) | €4 | €2.20 |
| Certification amortised (€25k) | €25 | €5 |
| **Landed cost** | **€77.50** | **€42.80** |
| Sell price direct ex-VAT | €142 | €142 |
| Via dealer/insurer (net €119) | €119 | €119 |
| **Gross margin direct** | **45%** | **70%** |
| **Gross margin via dealer** | 35% | 64% |

Gateway bundle: an off-the-shelf indoor LoRaWAN gateway lands at ~€90–120; sell in the €599 pack. SMS/app running cost ~€1/spear/year.

### Go-to-market
**First 100 customers:** one agricultural fair per country (the big autumn machinery fairs) with a demo stack and a pre-order form at €169; chambers of agriculture loss-prevention advisers; one insurer's prevention department (they publish hay-fire warnings every June — give them a product to point at); farm Facebook groups and the dairy-farmer forums; contractors who bale for many farms.

**Scale:** farm-supply dealer chains (the shops where the farmer buys fence wire), insurer co-funding programmes, chambers' subsidised prevention lists, LoRaWAN network operators in rural areas (they need devices), FR/PL distributors.

### 12-month plan
- **Q1:** 10 prototype spears from the Stamp C6LoRa + sensors in a tube, in two real hay stacks; pre-order list at one fair or chamber event. Gate: 20 farmers pre-order at €169 and one insurer agrees to promote.
- **Q2:** Own PCB in the head, IP67 head tool, RED tests, app + SMS alarms, 300 spears for the June–August hay season.
- **Q3:** Field data from season 1, dealer listings, gateway bundle, 1,000 spears for straw season.
- **Q4:** Insurer programme, FR/PL distributor talks, silage/grain variant (same spear, different firmware).

**Team:** one embedded engineer (LoRaWAN + low power; full-time 6 months), one mechanical/sourcing person for the spear (part-time), one farm-side salesperson (part-time, ex-advisory), a backend/app contractor.

**Funding to 1,000 spears (estimate):** NRE €30k (PCB, head tool €10k, app/backend, test rig) + certification €25k + 1,000 × €52 production = €52k → **~€107k**; fair pre-orders and an insurer pilot order cover ~€35k → cash need **~€70k**. Route: pre-orders + an agri-innovation grant (rural development programmes fund fire prevention) + possibly an insurer-backed pilot. Angel money only for the multi-country push.

### Top risks
- **Technical — radio inside a hay stack:** hay is wet and absorbs 868 MHz; the antenna must be in the head, outside the stack, and the head must stay up. Mitigation: head design with the antenna on top; a repeater/gateway bundle; test in a real stack early.
- **Technical — 5-year battery:** achievable with class A, 15-minute uplinks and deep sleep on the C6, but only if you measure it. Mitigation: current profiling in week 3, derate to 3 years in marketing until proven.
- **Market — seasonality:** you sell in May–August. Mitigation: straw and silage extend the season; stock for season 1 must be ready by May.
- **Regulatory:** RED (EN 300 220), EN 301 489, EN 62368-1, IP67, **EN 18031** (it connects to the internet via LoRaWAN — assume yes), CRA, lithium-metal cell transport (UN 38.3, labels) and Battery Regulation. Mitigation: pre-certified LoRa module with a RED file; cells from a supplier with transport docs.
- **Supply:** the stainless tube and tip are simple; the IP67 head is tooled. Mitigation: first 300 with a machined/printed head.

## 3. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [m5stack-stamp-c6lora](https://www.gongbans.com/db/m5stack-stamp-c6lora.html) | Open ESP32-C6 + LoRa core: the head electronics reference (Altium sources) | pcb, schematic | M5Stack hardware repo — check licence |
| [m5stack-unit-lorawan-eu868](https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html) | EU868 LoRaWAN module for the first prototypes | enclosure/structure only | Module |
| [m5stack-unit-kmeter-iso](https://www.gongbans.com/db/m5stack-unit-kmeter-iso.html) | Isolated thermocouple input for a high-temperature "fire-service" probe variant | enclosure/structure only | Module |
| [seeed-grove-temperature-and-humidity-sensor-pro](https://www.gongbans.com/db/seeed-grove-temperature-and-humidity-sensor-pro.html) | Ambient T/RH reference at the stack surface (for drying-rate logic) | schematic | Seeed wiki — check |

### Block diagram and engineering gap
```
[Spear tube 1 m] : sensor @30cm — sensor @60cm — sensor @90cm  (1-wire or I2C digital temp)
        |
[IP67 head] : ESP32-C6 (C6LoRa-derived) + LoRa EU868 + antenna on top + Li-SOCl2 cell + LED/button
        |--LoRaWAN--> public network or farm gateway --> backend --> app + SMS
Optional: surface T/RH node for ambient
```
Gap: mechanical spear and head (sealing, pull-out force, sensor wiring down a tube), antenna placement, deep-sleep power budget, LoRaWAN provisioning (keys, QR join), alarm logic (absolute + rate-of-rise), and a backend that sends SMS reliably.

### Starter BOM (per spear, estimates)
| Part | Est. cost | Note |
|---|---|---|
| ESP32-C6 module (certified) | €2.50 | — |
| LoRa transceiver module, EU868, pre-certified | €5.50 | Pick one with a RED test report |
| 3× digital temperature sensors on a flex/wire harness | €3.00 | Commodity |
| Li-SOCl2 C-cell (8.5 Ah) + holder | €4.50 | UN 38.3 docs required; lithium-metal shipping rules |
| PCB + assembly | €4.00 | — |
| Antenna (868 MHz, in head) | €1.00 | — |
| Stainless tube 20 × 1,000 mm + welded tip | €9.00 | EU or CN; long item — sea freight |
| IP67 PA66 head + seal + pull loop | €6.00 | Tooled; machined for pilot |
| Packaging (long box) | €2.50 | — |

### Firmware/software starting point
- **RadioLib** (exists; LoRaWAN support on ESP32) or Semtech's **LoRaMac-node** (exists) for the device; ESP-IDF deep sleep.
- Network: **The Things Stack / TTN** (public) and **ChirpStack** (self-hosted, exists) for the farm gateway bundle.
- Backend: anything that takes MQTT from the network server and sends SMS via a gateway API; keep it boring.

### 12-week build plan
- **Week 1–2 — validate.** Stamp C6LoRa + Unit LoRaWAN-EU868 + 3 sensors in a 1 m electrical conduit, pushed into a real stack; log to TTN. Pre-order form at a chamber event or fair. *Exit:* uplinks from inside a stack at 200 m; 20 pre-orders at €169; one insurer prevention person says "send me the flyer".
- **Week 3–5 — works-like.** Own head PCB, power profile measured (target <40 µA sleep), rate-of-rise alarm, SMS path. *Exit:* 5 spears in 5 stacks reporting for 3 weeks; projected battery ≥3 years.
- **Week 6–8 — looks-like + EVT.** Stainless spear, machined head, IP67 test in a bucket, app v1. *Exit:* 10 farmers use the app without a call; no water ingress.
- **Week 9–10 — DVT + pre-compliance.** Head tool, RED pre-scan (EN 300 220 limits, spurious), EN 18031 gap review. *Exit:* pre-scan pass, security checklist done.
- **Week 11–12 — pilot batch.** 50 spears + 10 gateways to pre-order farms before the hay season. *Exit:* 50 paid, <5% faults, alarms proven on at least one warm stack.

### Certification checklist (EU)
- **RED:** EN 300 220-2 (SRD 868 MHz), EN 301 489-1/-3, EN 62368-1; **EN 18031-1** (and -2/-3 if you store personal data or take payments — you store phone numbers, so plan -2) because the device connects to the internet via LoRaWAN; est. **€15–25k** total, less with a pre-certified module.
- **CRA:** reporting from Sept 2026, full obligations Dec 2027 — SBOM, secure update (LoRaWAN FUOTA or "return for update" — decide), vulnerability disclosure page.
- **RoHS, WEEE, REACH**; **IP67** test (IEC 60529) at the lab, €1–2k.
- **Battery Regulation:** applies to all batteries; primary lithium-metal: UN 38.3, transport labels, removability information. Not Li-ion, so no charging-safety work.
- **GDPR:** phone numbers for SMS alarms — privacy notice, EU hosting, deletion on request.
- No toy, no medical.

### Validation toolkit
- **Kill question:** do 20 farmers at one fair pre-order at €169, and does one insurer agree to promote it? **Cheapest experiment:** €500 — two conduit prototypes, a demo bale with a heater inside, a pre-order form, a stand at a chamber event.
- **5-question interview:** (1) How do you check your hay now and for how long after storing? (2) Have you or a neighbour had a hot stack? What happened? (3) Who in the family would get the alarm, and by SMS or app? (4) €169 per spear, €599 for three with a gateway — which, and would an insurer discount change it? (5) Where do you buy farm gear — dealer, online, co-op?
- **Landing-page headline:** "Your hay tells you before it burns." Bullets: 1 m spear, 3 depths, alarm to your phone · 5-year battery, no subscription for alarms · Works across the yard with LoRaWAN — gateway included if you need it.
- **Pre-order pass:** 20 paid pre-orders (€50 deposit) at one event, or 60 online in 6 weeks, plus one insurer letter.

### First production checklist
Tube/tip samples (pull and bend test), head samples sealed and dunked, golden sample with join keys printed on a QR label, DFM on the harness routing in the tube, MOQ 300 with a 2,000 forecast and a May delivery date written in the contract, QC/AQL Level II + 100% join test and sensor bath test, long-box drop test, sea freight FOB, lithium-metal transport paperwork, EU importer label, battery labelling per Battery Regulation.

## 4. Next steps (this week)
1. Order Stamp C6LoRa, Unit LoRaWAN-EU868, six digital temperature sensors and a 1 m conduit; register on TTN; find a farmer with a stack to push it into.
2. Call the chamber of agriculture's fire-prevention adviser and one insurer's loss-prevention department; ask for their hay-fire numbers and whether they'd co-fund.
3. Ask a LoRa module vendor for a module with an EN 300 220 report, and a lab for a RED + EN 18031 quote.

Want help sourcing or building this? Talk to us via www.gongbans.com.
