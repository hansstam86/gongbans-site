# Shop-Window e-Paper Signs — Founder Start Pack

> Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and "back in 10 minutes" from a phone — no wiring, no cloud subscription.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Small shops print and tape paper every day: today's bread prices, holiday hours, "back at 14:00", allergens. Electronic shelf labels exist, but they are sold to chains as enterprise systems (Vusion, Hanshow, SoluM) with gateways, integrations and per-label economics that make no sense for 20 labels; battery e-paper signage (Visionect Place & Play at $349/$899) comes with a subscription.
- **Customer:** Independent retailers, bakeries, butchers, pharmacies, cafés, market stalls, small chains (3–30 shops) across the EU. The owner pays and uses.
- **Product:** A5-size (7.5") and shelf-edge (2.9–4.2") e-paper signs with ESP32, BLE provisioning, WiFi or phone-direct sync, months on a charge (timer-wake), a sunlight-readable window mount, and a phone app with templates (prices, hours, allergens, promo) and scheduled changes. €99–149 per A5 sign, €39–59 shelf-edge (estimate). No subscription.
- **Why now:** E-paper panels and ESP32 are cheap; an open community (OpenEPaperLink) has shown that ESL hardware is commodity; the small-shop segment is unserved because nobody sells it as a buy-once consumer-grade product.
- **The ask:** ~€70k to a certified first 1,000 signs; a 20-shop doorstep test answers the kill question for the price of a train ticket.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Enterprise ESL vendors (Pricer, Hanshow) target chains with thousands of SKUs; independent-grocer sources (DUMAC, RetailWire) name upfront cost as the top objection because independents cannot spread it like chains. A Shopify Community thread confirms no plug-and-play, no-subscription ESL kit exists today. Bare e-paper hardware costs about $47–113; enterprise gateways (not needed here) add $300–400, which makes a €119 finished no-gateway unit plausible on margin. **Main risk:** Nothing confirms an underserved category at scale, only that the big players do not serve it; independents may keep using a €2 chalk sign. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 20 shops in one shopping street buy at least one sign at €119 after a doorstep demo?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Independent retailers, bakeries, pharmacies, market stalls and small chains in the EU.

**The problem as the pack states it:** Small shops print and tape paper every day: today's bread prices, holiday hours, "back at 14:00", allergens. Electronic shelf labels exist, but they are sold to chains as enterprise systems (Vusion, Hanshow, SoluM) with gateways, integrations and per-label economics that make no sense for 20 labels; battery e-paper signage (Visionect Place & Play at $349/$899) comes with a subscription.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/smallbusiness** · https://www.reddit.com/r/smallbusiness/ — shop and café owners.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€99–149 per sign, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how independent retailers, bakeries, pharmacies, market stalls and small chains in the EU deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How did you last change the prices or the promotion in your shop window, and how long did it take?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and 'back in 10 minutes' from a phone — no wiring, no cloud subscription. On a scale of one to ten, how likely would you be to buy that at €99–149 per sign, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Shop-Window e-Paper Signs: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Shop-Window e-Paper Signs: Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and 'back in 10 minutes' from a phone — no wiring, no cloud subscription. Before we spend money on tooling I want to find out whether this solves a real problem for independent retailers, bakeries, pharmacies, market stalls and small chains in the EU.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €99–149 per sign per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Pricer, Hanshow | Enterprise ESL for chains with 5,000+ SKUs | Do not serve independents |
| DUMAC, RetailWire (independent-grocer sources) | Upfront cost is the top objection to ESL | Confirms the price-sensitivity of the target |
| Shopify Community thread | No plug-and-play, no-subscription ESL kit exists | Confirms the gap |
| Bare e-paper hardware ($47–113); enterprise gateways ($300–400) | Component and system price points | Supports the €119 no-gateway unit on margin |

**Verdict as researched: LIKELY.** Main risk: Nothing confirms an underserved category at scale, only that the big players do not serve it; independents may keep using a €2 chalk sign.
<!-- market-competitors:end -->

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

## 4. Start kit

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

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (ESP32-S3 e-paper device for the A5-size sign); [M5Stack PaperColor (C151)](/db/m5stack-papercolor.html) (colour e-paper for promotional signs); [M5Stack PaperMono (C153)](/db/m5stack-papermono.html) (small shelf-edge variant); [M5Stack Stamp Timer Power2 (S021)](/db/m5stack-stamp-timer-power2.html) (RTC-timed wake for months of battery life). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **iDisc Technology** (深圳市艾迪思科技有限公司) · no website on file — E-ink display module / e-reader OEM: E-ink display module; e-reader gongban; retail price tag; OEM/ODM. *(E-ink display modules)*
- **GREPOW** (深圳格瑞普电池有限公司) · grepow.com — High-rate Li-Po / NiMH battery OEM: High-drain Li-Po; shaped/custom battery; NiMH; UAV battery. *(Custom Li-Po / NiMH batteries)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021) — for a Shop-Window e-Paper Signs

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Shop-Window e-Paper Signs: Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and 'back in 10 minutes' from a phone — no wiring, no cloud subscription. The design is built around your M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021).
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
主题：样品订购及批量报价 — M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021) — 用于Shop-Window e-Paper Signs

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Shop-Window e-Paper Signs：Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and 'back in 10 minutes' from a phone — no wiring, no cloud subscription。产品设计基于贵司的M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021)。
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
Subject: PCBA quote from open design files — Shop-Window e-Paper Signs, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Shop-Window e-Paper Signs: Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and 'back in 10 minutes' from a phone — no wiring, no cloud subscription. The design starts from published open-hardware files (M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Shop-Window e-Paper Signs，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Shop-Window e-Paper Signs：Battery-powered e-paper signs for shop windows and shelves that update prices, opening hours and 'back in 10 minutes' from a phone — no wiring, no cloud subscription。设计基于已公开的开源硬件文件（M5Stack PaperS3 (C139), M5Stack PaperColor (C151), M5Stack PaperMono (C153), M5Stack Stamp Timer Power2 (S021)；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Build 3 signs: PaperS3 in a printed A5 frame with a suction mount; a PWA with one "price list" and one "back at…" template pushed over WiFi.
2. Pick one shopping street with 40+ independents; plan Saturday doorstep demos with a card reader and a €30-deposit option.
3. Ask two labs for RED/safety quotes on "battery BLE/WiFi e-paper sign with 18650" and get the cell vendor's UN 38.3 report.

Want help sourcing or building this? Talk to us via www.gongbans.com.
