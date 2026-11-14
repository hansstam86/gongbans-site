# Smiley Terminal, No Subscription — Founder Start Pack

> A four-button customer-feedback terminal (very happy → very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The incumbent smiley terminals are sold as SaaS: resellers quote roughly $35–100 per terminal per month. A pharmacy or a municipal service desk wants to measure satisfaction, not sign a three-year subscription for four buttons and a radio.
- **Customer:** Facility managers and quality managers of supermarkets, pharmacies, public offices (Bürgerämter, gemeentehuizen), hospital facility teams, airport cleaning contractors, gyms. They pay from an opex-light capex budget. Users are the public — zero training.
- **Product:** A floor-stand or counter terminal with four big backlit buttons, 2-year battery, LoRaWAN (EU868) or WiFi uplink, anti-spam debounce, and an open dashboard (self-host or €0 hosted basic) with CSV export. €249–349 one-off (estimate).
- **Why now:** Public bodies are required or pushed to measure service quality and hate subscriptions; LoRaWAN coverage is now good in NL/DE/BE/FR public and private networks; the hardware is trivially cheap.
- **The ask:** ~€75k to a certified first 1,000 units; the B2B deposits should fund most of it.

## 2. Business plan

### Problem & customer

Four buttons are not a technology problem. They are a business-model problem. HappyOrNot (FI), FeedbackNow (CH, now Forrester), Ombea (SE), Qwesteo (FR) sell terminals bundled with analytics subscriptions; HappyOrNot itself quotes custom pricing, resellers mention $69–100/month per kiosk. For a chain with 300 stores this is fine. For a pharmacy with one counter, a municipal office with four desks or a cleaning contractor with 40 washrooms it is absurd — so they do nothing, or they print a QR code nobody scans.

- **Who pays:** the facility/quality manager with a small capex budget; procurement in municipalities (under-threshold direct purchases of a few thousand euro are easy — that is a feature).
- **Who uses:** the public, pressing one button on the way out. The product must survive kids, mops and being kicked.
- **Who looks at the data:** the manager, weekly, in a simple chart; the cleaning contractor who wants to prove SLA compliance to the client.

### Market size (estimates — check)

- **TAM (EU):** ~1M+ physical service points where feedback is worth measuring (grocery ~150k stores, pharmacies ~160k, public service desks tens of thousands, hospitals/clinics, gyms, airport washrooms). At 1.5 terminals each and €299 → **€400M+** one-off, plus replacement cycles.
- **SAM (small/mid operators who refuse subscriptions, DACH + Benelux + Nordics first):** ~150–250k sites → **€50–75M**.
- **SOM (3 yrs):** 1% of SAM → **1,500–2,500 sites, 3–5k terminals**. Year 1: 500–1,000 terminals.

### Competition (2 searches)

| Alternative | Model | Why we still win |
|---|---|---|
| HappyOrNot Smiley Terminal | SaaS, quote-only; reseller figures $69–100/month per kiosk | We are capex, ~1 year of their fee buys our terminal forever |
| FeedbackNow (Forrester) Smiley Box | Enterprise SaaS | Same |
| Ombea ExpressPod | "from $35/month billed annually" | Same; our dashboard is open and exportable |
| Qwesteo (e-ink + 4 buttons) | SaaS | Same |
| QR code to a web survey / do nothing | Free | Response rates collapse; no in-the-moment signal |
| DIY: four Grove buttons + ESP32 + Google Sheets | A weekend for a maker | Nobody in facility management does this; no stand, no battery life, no spam filter |

**Wedge:** buy-once hardware with open data. Secondary wedge: LoRaWAN — the terminal works in the washroom in the basement without store WiFi or IT approval.

### Product & value proposition

- Four 60 mm backlit buttons (green-dark green-amber-red smileys), silicone keycaps, tamper screws, steel/aluminium floor stand or counter mount, 4× D-cell or an 18650 pack for 2 years (LoRaWAN) — WiFi SKU on USB-C/PoE.
- Debounce + anti-spam: minimum gap between presses, burst detection, optional "why?" second-level buttons (four reasons).
- Dashboard: self-hosted docker (free) or our hosted basic (free for up to 5 terminals, then €1/terminal/month optional — this is the only recurring money and it is optional). CSV export, weekly email, API.
- **Pricing (estimates):** €299 LoRaWAN terminal incl. stand, €249 WiFi counter unit, €49 "why?" extension, €990 for a 4-pack. Resellers (facility services, IoT integrators) at 30% off.

### Unit economics (estimates, EUR per unit; LoRaWAN floor model)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (ESP32-C6+LoRa core €6, 4 big switches + caps €6, LED backlight €1.5, battery holder/pack €4, PCB €1.5, antenna €1) | 20.0 | 16.5 |
| PCBA + test | 3.5 | 2.4 |
| Enclosure + stand (sheet metal/aluminium stand €14, ABS head €5) | 19.0 | 14.0 |
| Packaging (bulky — double-wall box, foam) | 5.0 | 3.8 |
| Freight + duty to EU (volume-heavy: stand) | 9.0 | 5.5 |
| Certification amortised (€15k) | 15.0 | 3.0 |
| **Landed cost** | **71.5** | **45.2** |
| Net price (€299 ex VAT direct B2B) less €15 shipping/handling | 284 | 284 |
| **Gross margin direct** | **€212 (75%)** | **€239 (84%)** |
| Via reseller at 30% off (€209 net) | €123 (59%) | €149 (71%) |

This is a margin business; the risk is demand, not cost. Ship the stand flat-packed to kill freight.

### Go-to-market

**First 100 customers:** five facility managers you can reach — one pharmacy chain regional manager, one municipality (Bürgeramt / gemeente service desk), one hospital facility team, one cleaning contractor, one gym chain. Offer a 4-terminal pilot at €999 with full refund in 60 days. LinkedIn posts in Dutch and German aimed at "Facility Manager", "Qualitätsmanagement", "Kundenzufriedenheit".

**Then scale:** facility-services companies and cleaning contractors as resellers (they sell SLA proof to their clients), LoRaWAN network operators' partner marketplaces (The Things Industries partner list, KPN Things, Swisscom LPN, Netzikon/other DE operators — search), municipal procurement portals (under-threshold), pharmacy wholesaler catalogues, trade fairs (Facility Management fair Frankfurt, Vakbeurs Facilitair NL).

### 12-month plan

- **Q1:** 10 pilot terminals from M5Stack modules + printed head + bought stand; dashboard MVP; five pilot customers.
- **Q2:** own PCB (rev A), designed head + flat-pack stand, 50-unit EVT; LoRaWAN join/coverage tests in basements.
- **Q3:** certification, 500–1,000 production run, reseller agreements with two facility-services companies.
- **Q4:** WiFi/PoE counter SKU, "why?" extension, hosted dashboard tier, first trade fair.

**Team:** one embedded engineer (full), one web developer (half, dashboard), one founder on B2B sales, a mechanical designer (contract) for head and stand. Shenzhen partner for PCBA, metal stand and ABS head.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €57k + tooling (head mould, stand jigs) €14k + certification €15k + pilots €5k + 6 months team €50k + fairs/marketing €8k = **≈€149k** gross; pilots and pre-paid orders (say 300 terminals × €299 = €90k) cut the external need to **≈€60–75k**. Route: B2B deposits + bootstrap; an EU LoRaWAN operator co-marketing budget if you get one; angel if a national chain signs.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** buyers actually like the subscription analytics (benchmarks, alerts) | Hosted basic dashboard is free; sell optional analytics later, not required |
| **Market:** incumbents drop prices or offer a capex option | Stay cheaper on TCO and own the "open data" story; move fast |
| **Technical:** vandalism, liquid ingress, button lifespan (millions of presses) | Industrial-grade switches rated >1M cycles; IP54 head; replaceable keycaps |
| **Regulatory:** RED for LoRaWAN; CRA for a connected device | Pre-certified LoRaWAN module; EN 18031 self-assessment — no personal data on device |
| **Supply:** stand metalwork quality and freight damage | Flat-pack design, drop tests, local powder-coating option for the EU |

No personal data is collected — say so loudly; it is a procurement advantage in the public sector.

## 3. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit Dual Button (U025) | https://www.gongbans.com/db/m5stack-unit-dual-button.html | Big-button reference for the pilot | enclosure/structure only | Module for prototype only |
| Seeed Grove-Dual-Button | https://www.gongbans.com/db/seeed-grove-dual-button.html | Open button circuit (debounce/pull-up) to copy | schematic | Seeed wiki — check licence |
| M5Stack Stamp C6LoRa (S012) | https://www.gongbans.com/db/m5stack-stamp-c6lora.html | ESP32-C6 + LoRa core with open Altium PCB and schematic — the heart of the LoRaWAN SKU | pcb, schematic | M5_Hardware repo — check licence |
| M5Stack Unit LoRaWAN-EU868 (U184-EU868) | https://www.gongbans.com/db/m5stack-unit-lorawan-eu868.html | Ready EU868 LoRaWAN stack module for pilots (AT-command style per M5 docs — verify) | enclosure/structure only | Module; for production either the Stamp C6LoRa path or a pre-certified LoRaWAN module |

Catalogue honesty: the Stamp C6LoRa row has no chip field; "C6" and "LoRa" are from the name; the LoRa transceiver part is not stated — read the open schematic.

### Block diagram

```
Battery (4×D or 18650 pack) ──► LDO 3.3V
   ESP32-C6 (Stamp C6LoRa path) ──► LoRa radio (EU868) ──► public/private LoRaWAN ──► your dashboard
        │ GPIO ×4 (interrupt wake)          [WiFi SKU: ESP32-C6 WiFi ──► local network]
   4× big switches + backlight LEDs
   debounce + anti-spam counters in RAM; hourly uplink of counts; immediate uplink on first press
```

**Engineering gap:** power design for 2 years (uplink counts hourly, deep sleep between), a stand that survives a shopping centre, and the dashboard. LoRaWAN joining and coverage in basements is a field test, not an engineering problem.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| ESP32-C6 module + SX126x-class LoRa transceiver (or pre-certified LoRaWAN module) | €6–9 | Pre-certified module shortens RED testing |
| 4× 60 mm arcade-style switches rated >1M cycles | €5–7 | Many sources; check feel and click noise |
| Backlight LEDs + drivers | €1.5 | |
| 4× D-cell holder or 2×18650 pack with protection | €3–5 | Li-ion adds UN 38.3; alkaline D is simpler |
| 868 MHz antenna (PCB or whip inside head) | €1 | |
| PCB 2-layer | €1.5 | |
| ABS head (tooling €8–10k) | €5 | |
| Steel/aluminium stand, powder coat, flat-pack | €12–16 | Heaviest cost item; consider EU-made stand for small volumes |

### Firmware/software starting point

- **ESP-IDF** on ESP32-C6; LoRaWAN stack: **RadioLib** (has LoRaWAN support) or Semtech **LoRaMac-node**; **Basicmac** as older alternative.
- Payload codec: **Cayenne LPP** or your own 4-byte counts; publish the decoder for TTN/ChirpStack.
- Network: **The Things Stack** (community or paid), **ChirpStack** for private.
- Dashboard: Node-RED + InfluxDB + Grafana for the pilot; a small Django/Rails app for the product. Pilot WiFi units: **ESPHome** with four binary sensors is a one-afternoon job.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 10 calls to facility/quality managers; 3 pilot LOIs; two M5 pilot terminals (Unit Dual Buttons ×2 + LoRaWAN Unit + printed head on a bought music stand) | ≥5 managers say they would buy 4 at €299; 2 deployed and uplinking |
| 3–5 | **Works-like** — 10 pilot terminals in 5 sites, dashboard MVP with CSV | ≥500 presses recorded; spam filter tuned; uptime >98% |
| 6–8 | **Looks-like + EVT** — rev A PCB (Stamp C6LoRa-derived), designed head, flat-pack stand prototype; 30 units; battery current profile | Average current supports ≥24 months on D-cells (estimate ≤60 µA sleep, hourly uplink) |
| 9–10 | **DVT + pre-compliance** — rev B, EN 300 220 pre-scan, EMC pre-scan, EN 18031 checklist, drop/kick tests on stand | No radio fails; stand survives 10 kicks and a 1 m tip-over; test plan signed |
| 11–12 | **Pilot batch** — 50 units to pilot customers and 2 resellers, full packaging | ≤2 failures; 3 of 5 pilot customers convert to paid; reseller signs |

### Certification checklist (EU)

- **CE — RED:** LoRaWAN EN 300 220-2 (module pre-cert helps but the final product with its antenna is assessed), EN 301 489-1/-3 (EMC), EN 62368-1 (battery, safety): €8–12k. WiFi SKU: EN 300 328 + EN 301 489-17.
- **EN 18031** (RED cyber): applies to internet-connected radio equipment — LoRaWAN terminals talk to the internet via the network; assume yes, self-assess (no personal data → 18031-2 may not apply; ask the lab): €2–4k.
- **CRA:** SBOM, update capability (LoRaWAN FUOTA is painful — plan for USB-C local update), vulnerability disclosure.
- **RoHS, WEEE (B2B category), REACH, packaging.**
- **Battery Regulation:** D-cells placed on the market → producer registration; Li-ion pack → UN 38.3, removable design.
- **GDPR:** none (no personal data) — document that this is by design.
- **Total estimate:** €13–18k.

### Validation toolkit

- **Kill question:** Do 5 facility managers buy 4 terminals each at €299 instead of renewing their subscription (or instead of doing nothing)? Cheapest experiment: a one-page PDF offer + 10 calls; ask for a €200 deposit per site.
- **Interview script (5):** 1) How do you measure service satisfaction today, and what does it cost per year? 2) Who reads the results, how often, and what did you change because of them? 3) What happened last time a vendor asked you to sign a subscription? 4) Where would the terminal stand, and what has been vandalised there? 5) Would you buy at €299 one-off, and do you need a dashboard, or is a weekly CSV email enough?
- **Landing page:** Headline: "Four buttons. One price. Your data." Bullets: "€299 once — no monthly fee per terminal, ever." / "Works without WiFi: LoRaWAN reaches the basement washroom." / "Open dashboard and CSV export — your results stay yours."
- **Pre-order pass:** ≥5 sites with ≥€200 deposits (≥20 terminals) within 6 weeks.

### First production checklist

- Samples: 3 PCBAs from two assemblers; 2 stands from two metal shops; **golden sample** head + stand with colour chips.
- DFM: keycap retention, tamper screws, cable path in the stand, flat-pack hardware kit.
- MOQ: PCBA 300–500; head mould 1k shots (negotiate 500); stand 200.
- QC/AQL: Z1.4 II, AQL 1.0/2.5; 100% test: each button 10 presses, backlight, LoRaWAN join on a test gateway.
- Packaging: ISTA 1A drop; stand edge protection; EU DoC and WEEE marks.
- Incoterms: FOB Shenzhen by sea (stands are volume); first 50 by air DAP to learn duty lines (HS for the terminal vs the stand).

## 4. Next steps (this week)

1. Write the one-page offer (€299, no subscription, 60-day refund) and call 10 facility/quality managers; aim for 3 pilot LOIs.
2. Order Stamp C6LoRa ×2, Unit LoRaWAN-EU868 ×2, Unit Dual Button ×4, a Grove Dual Button; register a free The Things Stack application and get one press uplinking.
3. Ask two EU labs for RED quotes (EN 300 220 + EMC + safety) on "battery LoRaWAN feedback terminal with pre-certified module" and ask explicitly whether EN 18031-2 applies with zero personal data.

Want help sourcing or building this? Talk to us via www.gongbans.com.
