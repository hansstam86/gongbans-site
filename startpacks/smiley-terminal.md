# Smiley Terminal, No Subscription — Founder Start Pack

> A four-button customer-feedback terminal (very happy → very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** The incumbent smiley terminals are sold as SaaS: resellers quote roughly $35–100 per terminal per month. A pharmacy or a municipal service desk wants to measure satisfaction, not sign a three-year subscription for four buttons and a radio.
- **Customer:** Facility managers and quality managers of supermarkets, pharmacies, public offices (Bürgerämter, gemeentehuizen), hospital facility teams, airport cleaning contractors, gyms. They pay from an opex-light capex budget. Users are the public — zero training.
- **Product:** A floor-stand or counter terminal with four big backlit buttons, 2-year battery, LoRaWAN (EU868) or WiFi uplink, anti-spam debounce, and an open dashboard (self-host or €0 hosted basic) with CSV export. €249–349 one-off (estimate).
- **Why now:** Public bodies are required or pushed to measure service quality and hate subscriptions; LoRaWAN coverage is now good in NL/DE/BE/FR public and private networks; the hardware is trivially cheap.
- **The ask:** ~€75k to a certified first 1,000 units; the B2B deposits should fund most of it.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 5 facility managers buy 4 terminals each at €299 instead of renewing their subscription?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Supermarkets, pharmacies, public offices, hospitals' facility teams, airports' cleaning contractors in the EU.

**The problem as the pack states it:** The incumbent smiley terminals are sold as SaaS: resellers quote roughly $35–100 per terminal per month. A pharmacy or a municipal service desk wants to measure satisfaction, not sign a three-year subscription for four buttons and a radio.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **IFMA** · https://www.ifma.org/ — facility managers; local chapters across Europe.
- **GEFMA** · https://www.gefma.de/ — German facility-management association.
- **r/PropertyManagement** · https://www.reddit.com/r/PropertyManagement/ — property and facility managers.
- **r/smallbusiness** · https://www.reddit.com/r/smallbusiness/ — shop and café owners.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€249–349 one-off, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how supermarkets, pharmacies, public offices, hospitals' facility teams, airports' cleaning contractors in the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you find out today whether the people using this building are satisfied with cleaning or service, and what did that cost you last year?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A four-button customer-feedback terminal (very happy to very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee. On a scale of one to ten, how likely would you be to buy that at €249–349 one-off, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Smiley Terminal, No Subscription: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Smiley Terminal, No Subscription: A four-button customer-feedback terminal (very happy to very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee. Before we spend money on tooling I want to find out whether this solves a real problem for supermarkets, pharmacies, public offices, hospitals' facility teams, airports' cleaning contractors in the EU.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €249–349 one-off per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

## 4. Start kit

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

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Dual Button (U025)](/db/m5stack-unit-dual-button.html) (big button reference); [M5Stack Stamp C6LoRa (S012)](/db/m5stack-stamp-c6lora.html) (open ESP32-C6 + LoRa core for the LoRaWAN variant); [M5Stack Unit LoRaWAN-EU868 (U184-EU868)](/db/m5stack-unit-lorawan-eu868.html) (EU868 LoRaWAN module). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Dual-Button](/db/seeed-grove-dual-button.html) (alternative button reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button — for a Smiley Terminal, No Subscription

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Smiley Terminal, No Subscription: A four-button customer-feedback terminal (very happy to very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee. The design is built around your M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button.
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
主题：样品订购及批量报价 — M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button — 用于Smiley Terminal, No Subscription

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Smiley Terminal, No Subscription：A four-button customer-feedback terminal (very happy to very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee。产品设计基于贵司的M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button。
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
Subject: PCBA quote from open design files — Smiley Terminal, No Subscription, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Smiley Terminal, No Subscription: A four-button customer-feedback terminal (very happy to very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee. The design starts from published open-hardware files (M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Smiley Terminal, No Subscription，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Smiley Terminal, No Subscription：A four-button customer-feedback terminal (very happy to very unhappy) that posts results over LoRaWAN or WiFi to a simple dashboard you own — buy once, no per-terminal monthly fee。设计基于已公开的开源硬件文件（M5Stack Unit Dual Button (U025), M5Stack Stamp C6LoRa (S012), M5Stack Unit LoRaWAN-EU868 (U184-EU868), Seeed Grove-Dual-Button；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Write the one-page offer (€299, no subscription, 60-day refund) and call 10 facility/quality managers; aim for 3 pilot LOIs.
2. Order Stamp C6LoRa ×2, Unit LoRaWAN-EU868 ×2, Unit Dual Button ×4, a Grove Dual Button; register a free The Things Stack application and get one press uplinking.
3. Ask two EU labs for RED quotes (EN 300 220 + EMC + safety) on "battery LoRaWAN feedback terminal with pre-certified module" and ask explicitly whether EN 18031-2 applies with zero personal data.

Want help sourcing or building this? Talk to us via www.gongbans.com.
