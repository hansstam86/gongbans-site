# Shop-Window e-Paper Signs — Founder Start Pack

> Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and "back in 10 minutes" from a phone — no wiring, no cloud subscription.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Small shops print and tape paper every day: today's bread prices, holiday hours, "back at 14:00", allergens. Electronic shelf labels exist, but they are sold to chains as enterprise systems (Vusion, Hanshow, SoluM) with gateways, integrations and per-label economics that make no sense for 20 labels; battery e-paper signage (Visionect Place & Play at $349/$899) comes with a subscription.
- **Customer:** Independent retailers, bakeries, butchers, pharmacies, cafés, market stalls, small chains (3–30 shops) across the EU. The owner pays and uses.
- **Product:** A5-size (7.5") and shelf-edge (2.9–4.2") e-paper signs with ESP32, BLE provisioning, WiFi or phone-direct sync, months on a charge (timer-wake), a sunlight-readable window mount, and a phone app with templates (prices, hours, allergens, promo) and scheduled changes. €99–149 per A5 sign, €39–59 shelf-edge (estimate). No subscription.
- **Why now:** E-paper panels and ESP32 are cheap; an open community (OpenEPaperLink) has shown that ESL hardware is commodity; the small-shop segment is unserved because nobody sells it as a buy-once consumer-grade product.
- **The ask:** ~€70k to a certified first 1,000 signs; a 20-shop doorstep test answers the kill question for the price of a train ticket.

## 2. Business plan

### Problem & customer

The baker changes prices twice a week and hours every holiday; the pharmacy posts the emergency rota; the café writes "cash only today" on a napkin. Each change is a printer, tape and a walk to the window. The buyer wants the change to come from a phone, in the back room, in 20 seconds — and to buy the sign like a lamp, not sign a SaaS contract.

- **Who pays:** the shop owner or the small chain's operations manager; sometimes the shopping-street association or a city "digital high street" programme.
- **Who uses:** the same owner and staff; the customer in the street reads it.
- **Why they haven't:** chains' ESL vendors do not sell to them; consumer e-paper gadgets are not weather- or sun-ready and have no templates.

### Market size (estimates — check)

- **TAM (EU independent retail/food/service outlets):** ~3.5–4M. At 2 signs each at €99 → **€700M+**.
- **SAM (outlets in NL/DE/BE/AT/CH/DK that already run a phone-based POS or social media, i.e. digital-ready; plus small chains):** ~800k → **€150M**.
- **SOM (3 yrs):** 1% of SAM → **8k outlets, 16–20k signs**. Year 1: 1,000–2,000 signs.

### Competition (2 searches)

| Alternative | What it is | Why we still win |
|---|---|---|
| Paper + printer + tape; chalkboard | Free, daily labour | The 20-second phone update; the window looks professional |
| Enterprise ESL (Vusion/SES-imagotag, Hanshow, SoluM) | $6–25 per label (Vusion FAQ) but sold as systems with gateways, integration and projects | Not sold to a bakery; no window-size signs; needs IT |
| Visionect Place & Play 6"/13" ($349/$899 + subscription) | Battery e-paper signage with cloud | Subscription-based; 2–3× our price |
| Samsung 32" colour e-paper ($1,350) | Poster-sized, 500-day static retention | Different league; not a shelf or window sign |
| Waveshare NFC/USB e-paper tags ($40–45) | Bare panels you update by phone tapping | No templates, no scheduling, no mount, no weather readiness |
| OpenEPaperLink DIY (repurposed ESL tags + ESP32 AP) | Open community for hobbyists | Our customer will not flash tags; great firmware inspiration (check licence) |
| Small LCD/LED digital signage on mains | Bright but wired, power-hungry | No wiring is the point |

**Wedge:** buy-once, phone-first, window-ready e-paper with templates for small shops — and a price point under the "I'll just ask my nephew" threshold.

### Product & value proposition

- A5 sign: 7.5" 800×480 mono or 7.3" colour (Spectra-class, slower refresh — fine for signs), ESP32-C3/S3, 18650 or 2,500 mAh pouch, RTC timer-wake (Stamp Timer Power-style) for scheduled updates, suction-cup/adhesive window mount with anti-glare front; indoor-only rating at launch (behind glass).
- Shelf-edge sign: 2.9"/4.2" mono, coin-cell or AAA, rail clip.
- App: templates (price list, hours, allergens, promo, "back at…"), schedule changes, multi-sign groups, PNG upload; sync via BLE directly or via WiFi; optional free cloud relay for remote changes (no fee for up to 10 signs; a €2/sign/year "Pro" only for chains).
- **Pricing (estimates):** €119 A5 mono, €149 A5 colour, €49 shelf-edge, 5-pack shelf-edge €199, starter kit (1 A5 + 3 shelf) €229.

### Unit economics (estimates, EUR per unit; A5 mono)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (7.5" mono panel €18–22, ESP32-C3 €2.3, e-paper driver €1.5, RTC/timer power circuit €1, charger + cell €4, PCB €1.2) | 29.0 | 25.0 |
| PCBA + test | 2.8 | 1.9 |
| Enclosure (ABS/PC frame, anti-glare front, suction/adhesive mount) | 5.0 | 3.5 |
| Packaging + USB-C cable + mount kit | 2.5 | 1.8 |
| Freight + duty to EU | 2.5 | 1.2 |
| Certification amortised (€18k incl. battery) | 18.0 | 3.6 |
| **Landed cost** | **59.8** | **37.0** |
| Net price D2C (€119 incl. 21% VAT → €98.3) less €8 fulfilment | 90.3 | 90.3 |
| **Gross margin D2C** | **€30.5 (34%)** | **€53 (59%)** |
| Via POS dealers/wholesale at 35% off (€64 net) | €4 (6%) | €27 (42%) |

Dealers only after 5k. The panel is the BOM; two vendors, locked part numbers.

### Go-to-market

**First 100 customers:** one shopping street — walk it with a working sign and a phone, doorstep demo, €119 on the spot with a 30-day return. Then the local shopkeepers' association (winkeliersvereniging / Gewerbeverein) newsletter. Bakeries first (they change prices most). Instagram reels of the "back in 10 minutes" update.

**Then scale:** POS/cash-register dealers (they visit every shop), bakery and butcher trade suppliers and fairs (e.g. the big bakery fairs in DE/NL — search), city "smart high street" programmes, small-chain operations managers, Amazon Business, pharmacy wholesalers.

### 12-month plan

- **Q1:** 10 hand-built signs (PaperS3 + mount + phone web app), one street, 20-shop test; kill decision.
- **Q2:** own PCB (7.5" + timer-wake + 18650), frame and window mount, 50-unit EVT in 20 shops; shelf-edge prototype on PaperMono.
- **Q3:** certification incl. battery; 1,000 A5 production; app v1 on iOS/Android (or PWA).
- **Q4:** shelf-edge SKU, dealer programme, colour SKU EVT.

**Team:** firmware engineer (full), app developer (full for 4 months, then half), industrial designer (contract) for frame and mount, founder on street sales and dealers. Shenzhen partner for panels, PCBA and frames.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €42k + tooling (frame, mount) €10k + certification €18k + 50 pilot units €5k + 6 months team €55k + marketing €5k = **≈€135k**; pre-sales at the doorstep (400 × €119 = €39k ex VAT) and a street-association bulk order reduce the external need to **≈€70–80k**. Route: doorstep pre-sales + bootstrap; city/regional retail-digitalisation grants (many EU cities fund "digital high street" — search your region); angel if a POS dealer chain signs.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** shops love the idea and don't buy ("I'll think about it") | Sell on the doorstep with the unit in hand; 30-day return; the kill question is 20 sales, not 20 compliments |
| **Technical:** sun and heat behind a window (e-paper ghosting, battery heat), condensation | Indoor-behind-glass rating; thermal test at 50 °C; anti-UV front film; colour panels have temperature limits — check |
| **Technical:** battery life claims | Timer-wake only on scheduled updates; measure and publish |
| **Regulatory:** Li-ion → UN 38.3, Battery Regulation; RED cyber on a BLE/WiFi sign | 18650 holder; self-assess EN 18031; no personal data |
| **Supply:** e-paper panels, especially colour, allocation and price | Two vendors; mono first; buy panels at EVT |

## 3. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack PaperS3 (C139) | https://www.gongbans.com/db/m5stack-papers3.html | ESP32-S3 e-paper device for the A5 pilot signs | enclosure/structure only | Finished device for pilots |
| M5Stack PaperColor (C151) | https://www.gongbans.com/db/m5stack-papercolor.html | Colour e-paper for promo-sign pilots | enclosure/structure only | Same |
| M5Stack PaperMono (C153) | https://www.gongbans.com/db/m5stack-papermono.html | Small shelf-edge variant pilot | enclosure/structure only | Same |
| M5Stack Stamp Timer Power2 (S021) | https://www.gongbans.com/db/m5stack-stamp-timer-power2.html | RTC-timed wake / power gating for months of battery life — open Altium PCB to copy the timer-power circuit | pcb (Altium) | M5_Hardware repo — check licence |

Catalogue honesty: panel sizes, resolutions and battery capacities of the Paper devices are not in the catalogue — verify on M5 docs. Stamp Timer Power2 lists PCB only, no schematic row entry — derive from the PCB and M5 docs.

### Block diagram

```
18650 ──► charger/protection ──► RTC timer-power gate (Stamp Timer Power2-style) ──► ESP32-C3/S3
     ESP32 ──SPI──► e-paper driver/boost ──► 7.5" panel (A5 sign) | 2.9"/4.2" (shelf-edge)
     ESP32 ──BLE──► phone app (direct provisioning + image push)
     ESP32 ──WiFi──► optional relay server (remote updates, schedules) 
Frame: anti-glare front, suction/adhesive window mount or shelf clip; USB-C charge port
```

**Engineering gap:** the app (templates, scheduling, groups), image rendering/dithering for e-paper, timer-wake power design, and the window mount that survives summer behind glass.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| 7.5" 800×480 mono e-paper (A5) | €18–22 | **Price-volatile; few makers**; colour 7.3" €30–40 |
| ESP32-C3 (mono) / S3 (colour, PSRAM for dithering) | €2.3–3.5 | |
| E-paper driver + boost | €1.5 | |
| RTC (e.g. low-power RTC with alarm) + load switch | €1 | Copy topology from Stamp Timer Power2 |
| Charger + protection + 18650 holder + cell | €4 | Cell with UN 38.3 report |
| PCB 2-layer | €1.2 | |
| Frame + anti-glare front + mount | €5 | Tooling €8–10k |
| Shelf-edge: 2.9" panel €4, ESP32-C3, 2×AAA | €9 total BOM | Separate SKU later |

### Firmware/software starting point

- **ESP-IDF**/Arduino-ESP32 with **GxEPD2** for panels; **M5Unified/M5GFX** for Paper-device pilots.
- **OpenEPaperLink** (open ESL ecosystem) — study its image push and tag protocol; check its licence before reuse.
- BLE provisioning: Espressif **ESP BLE Prov** component; image transfer over BLE/WiFi — write your own simple protocol.
- App: **Flutter** or a PWA with Web Bluetooth (Android/desktop only — iOS needs a native app or WiFi path); templates rendered in the app, dithered to 1-bit/colour.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — 3 PaperS3 signs in printed frames with a PWA pushing a price template; walk one street; doorstep demos | ≥20 shops buy at €119 (or pay a €30 deposit) on one street |
| 3–5 | **Works-like** — 10 signs live in shops, schedule feature, battery logging | ≥9/10 shops still updating weekly after 3 weeks; battery ≥8 weeks at 2 updates/day |
| 6–8 | **Looks-like + EVT** — own PCB rev A (7.5", timer-wake, 18650), frame, window mount; 30 units; heat test behind glass | Rev A works; 50 °C soak without ghosting; mount holds 30 days |
| 9–10 | **DVT + pre-compliance** — rev B, EMC pre-scan, battery safety review, EN 18031 checklist, app beta on iOS/Android | No fails; checklist complete; app store beta approved |
| 11–12 | **Pilot batch** — 50 units with packaging to 30 shops, 2 POS dealers | ≤2 failures; ≥60% of pilot shops buy a second sign; one dealer signs |

### Certification checklist (EU)

- **CE — RED:** EN 300 328 (BLE/WiFi via module), **EN 301 489-1/-17**, **EN 62368-1** incl. charging: €7–10k.
- **EN 18031-1** (connected): self-assess; no personal data (no 18031-2 unless the app sends shop data via your cloud — ask): €2–3k.
- **CRA:** SBOM, signed OTA, disclosure contact.
- **Battery:** **UN 38.3** (cell report), **EU Battery Regulation** (registration, labelling, removable by 2027 — 18650 holder), shipping paperwork.
- **RoHS, WEEE (B2B/consumer), REACH, packaging.**
- **GDPR:** none on the device; app account minimal.
- **Total estimate:** €14–18k.

### Validation toolkit

- **Kill question:** Do 20 shops in one shopping street buy at least one sign at €119 after a doorstep demo? Cheapest experiment: 3 PaperS3 signs, one Saturday, a card reader.
- **Interview script (5):** 1) What did you change in your window or on your shelves this week, and how long did it take? 2) Who makes the change — you, staff, head office? 3) Where would a sign hang; does the sun hit it? 4) Phone app, WhatsApp-style, or a web page — what would you actually use? 5) €119 per A5 sign, €49 per shelf label, no subscription — buy today, or what is missing?
- **Landing page:** Headline: "Change your shop sign from your phone. Buy once, no subscription." Bullets: "Prices, hours, 'back at 14:00' — updated in 20 seconds." / "Battery e-paper: no wiring, months per charge." / "Templates for bakeries, pharmacies, cafés and market stalls."
- **Pre-order pass:** ≥20 paid units on one street in one weekend (deposits count).

### First production checklist

- Samples: panels from two vendors tested for ghosting at 5 °C and 45 °C; 5 PCBAs; **golden sample** framed sign with reference image.
- DFM: panel flex-cable strain relief, front film lamination, mount adhesive choice, USB-C seal.
- MOQ: panels 500–1,000; PCBA 500; frames 1k shots (negotiate 500).
- QC/AQL: Z1.4 II, AQL 1.0/2.5; 100% test: full-screen pattern, BLE provisioning, charge test, timer-wake.
- Packaging: mount kit and quick-start card; battery labelling; EU DoC + WEEE.
- Incoterms: FOB Shenzhen sea; lithium cells → DG paperwork; pilot by air DAP.

## 4. Next steps (this week)

1. Build 3 signs: PaperS3 in a printed A5 frame with a suction mount; a PWA with one "price list" and one "back at…" template pushed over WiFi.
2. Pick one shopping street with 40+ independents; plan Saturday doorstep demos with a card reader and a €30-deposit option.
3. Ask two labs for RED/safety quotes on "battery BLE/WiFi e-paper sign with 18650" and get the cell vendor's UN 38.3 report.

Want help sourcing or building this? Talk to us via www.gongbans.com.
