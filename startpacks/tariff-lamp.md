# Tariff Lamp — Founder Start Pack

> A small lamp that glows green, amber or red with your actual hourly electricity price (and solar surplus), so the household runs the dishwasher when power is cheap — no app, no dashboard.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Over a million Dutch households and a fast-growing German cohort are on dynamic (hourly) electricity contracts, but nobody in the family opens the tariff app. Behaviour change needs a glanceable object, not a dashboard.
- **Customer:** Dutch and German households on dynamic tariffs (Tibber, Zonneplan, ANWB Energie, aWATTar, Octopus, Rabot, Ostrom and the like). Second buyer: the energy retailer itself, as a branded onboarding gift that reduces churn and improves load-shifting.
- **Product:** A USB-C powered frosted lamp with an ESP32-class WiFi module and eight RGB LEDs. It fetches day-ahead prices itself (public market data, optional retailer account link), shows price now and the trend for the next hours, and has a solar-surplus mode. Local MQTT mode for Home Assistant people. Target retail €49–69 (estimate).
- **Why now:** Dynamic tariffs are mass-market in NL and every German supplier must offer one since January 2025; dynamic grid fees arrive in 2026. Searches (ours and this one) found only web-page "Strompreis-Ampel" pages — no physical price lamp on the shelf.
- **The ask:** ~€45–60k to get through certification and a first 1,000 units (math in §3), ideally half of it from pre-orders and a retailer co-branding deal.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** No standalone competing product was found (Tibber Pulse's light shows connection status, not price), while several independent DIY builds do exactly this, and dynamic tariffs are a real, growing NL/DE category (Tibber, EDF FreePhase, Nord Pool-indexed contracts). **Main risk:** Technical users can DIY it with a cheap smart bulb and Home Assistant; the product has to beat "just buy a smart plug" on simplicity. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 100 people on dynamic-tariff forums pre-order at €59 from a landing page with a render? Pass = >3% conversion to a refundable deposit.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a fake-door landing page that Dutch and German households on dynamic electricity contracts actually visited, with a measured conversion to a waitlist or refundable deposit, plus the interview notes behind it. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Dutch and German households on dynamic electricity contracts; home-automation enthusiasts; energy retailers as a branded giveaway.

**The problem as the pack states it:** Over a million Dutch households and a fast-growing German cohort are on dynamic (hourly) electricity contracts, but nobody in the family opens the tariff app. Behaviour change needs a glanceable object, not a dashboard.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.
- **Photovoltaikforum (DE)** · https://www.photovoltaikforum.com/ — German PV, battery, heat-pump and dynamic-tariff owners.
- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **OpenEnergyMonitor community** · https://community.openenergymonitor.org/ — open energy-monitoring builders; heat-pump monitoring is a major topic.
- **r/Octopus_Energy** · https://www.reddit.com/r/Octopus_Energy/ — UK customers on time-of-use tariffs.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (twenty people from the audience line), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€49–69, the pack's estimate), and one button. For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how Dutch and German households on dynamic electricity contracts deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. When was the last time you actually changed when you ran the dishwasher or charged the car because of the hourly price, and how did you know the price at that moment?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A small lamp that glows green, amber or red with your actual hourly electricity price (and solar surplus) so the household runs the dishwasher when power is cheap — no app, no dashboard. On a scale of one to ten, how likely would you be to buy that at €49–69, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Tariff Lamp: would you pay €49–69 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Tariff Lamp: A small lamp that glows green, amber or red with your actual hourly electricity price (and solar surplus) so the household runs the dishwasher when power is cheap — no app, no dashboard. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €49–69, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

The dynamic-tariff household saves money only if it shifts load. Shifting load requires knowing the price at the moment you reach for the dishwasher button. Apps are good at history and bad at the moment. The person who signed the contract is rarely the person loading the washing machine. A lamp in the kitchen solves exactly that: everyone sees it, nobody needs a login.

- **Who uses it:** the whole household, including kids and the partner who did not pick the tariff.
- **Who pays (B2C):** the tariff-picker: tech-leaning, 30–55, owns a P1-port reader or a Home Assistant box, NL/DE/AT/BE, follows Tweakers or Photovoltaikforum.
- **Who pays (B2B):** energy retailers and energy cooperatives wanting an onboarding gift that lowers churn, and installers of PV/heat pumps who want a visible "your system is thinking" object. Here the buyer is marketing, the user is the household, the price pressure is heavy (€25–35 per unit at 2–5k volumes, estimate) but the volume is real.

### Market size (estimates — check)

- **TAM (EU households on hourly/dynamic tariffs, 2026):** NL >1.1M (ACM/Bright.nl via round-1 notes), DE a low single-digit percentage of ~41M households, say 1–2M, plus Nordics (where spot contracts are the norm, several million) and AT/BE. Call it **6–8M households**. At €59 that is a €350–470M theoretical device TAM — meaningless as a number except that the pool is deep.
- **SAM (reachable: NL + DE + AT + BE, online, home-automation-curious):** about 10–15% of the dynamic cohort actively tries to shift load → **300–500k households**. ~€20–30M.
- **SOM (3 years):** 1–2% of SAM → **5–10k units direct** plus one retailer deal of 2–5k units. Year-1 realistic: 1,000–2,500 units.

Sources used for the tariff numbers: ACM/Bright.nl (NL >1.1M dynamic contracts), Verbraucherzentrale and vattenfall.de for the German legal obligation. The device-level numbers are my gut.

### Competition (3 searches)

| Alternative | What it is | Why we still win |
|---|---|---|
| Do nothing / the app | Tibber, Zonneplan, aWATTar apps show hourly prices | Nobody opens it at the right moment; no family visibility |
| Web "Strompreis-Ampel" pages (energiemarie.de etc.) | Browser page with a traffic light | Not a physical object; proves the metaphor people want |
| DIY: ESP32 + WLED/ESPHome + Home Assistant automation | Forums are full of these builds | Needs HA, a weekend and a soldering iron; our customer wants a box |
| Smart bulb + HA automation (Hue/IKEA colour bulb) | Colour follows price via automation | Same DIY dependency; a bulb has no "trend" display and no standalone fetch |
| Retailer hardware (Tibber Pulse, HomeWizard P1) | Meter readers, not price indicators | Complementary — our solar-surplus mode can read their local API |

**Wedge:** the only standalone, zero-setup physical price indicator. Works out of the box with public day-ahead data; no account needed for the basic mode.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Tibber Pulse (meter reader with status light) | Light indicates connection status only, not price | Confirms the gap: no retailer hardware shows the price itself |
| Home Assistant forum thread "Preparing for a Dynamic Energy Contract with Color Awareness" | DIY colour-by-price build | Demand signal: people build this themselves |
| GitHub gist for Amber (Australia) price light | DIY build on another market's dynamic tariff | Same need re-invented elsewhere |
| Aqara forum "traffic light" post | DIY price traffic light | Same |
| Homey community thread asking for exactly this | User asked for a price lamp and was told to build it | Unmet demand stated by a user |
| Dynamic tariff providers: Tibber, EDF FreePhase, Nord Pool-indexed contracts | The category the lamp depends on | Real and growing in NL/DE |

**Verdict as researched: LIKELY.** Main risk: Technical users can DIY it with a cheap smart bulb and Home Assistant; the product has to beat "just buy a smart plug" on simplicity.
<!-- market-competitors:end -->

### Product & value proposition

- Frosted diffuser, ~90 mm diameter, USB-C, 8 addressable RGB LEDs arranged as a clock-like ring: colour = price band now, ring segments = the next 8 hours. One capacitive touch: hold to show "cheapest 2-hour window today" as a sweep.
- Setup via captive portal in 2 minutes: country/bidding zone, tariff type (plain spot or retailer formula with tax and margin). Optional: link retailer account, link P1/inverter for surplus mode.
- Local MQTT/Home Assistant discovery for the enthusiasts. Signed OTA.
- **Pricing (estimates):** B2C €59 (launch €49 for pre-orders). B2B co-branded €29–35 at 2k+ with the retailer's logo on the base. Gift bundle of two for €99.

### Unit economics (estimates, EUR per unit)

| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (ESP32-C3/C5-class module €2.5, 8 RGB LEDs €1.2, USB-C + LDO + passives €1.3, PCB €0.8) | 5.8 | 4.6 |
| PCBA assembly + test | 2.2 | 1.4 |
| Enclosure (diffuser + base, injection moulded; tooling amortised separately) | 3.5 | 2.4 |
| Packaging + USB cable + leaflet | 2.0 | 1.5 |
| Freight + duty to EU (air at 1k, sea at 5k; ~0% duty on lamps/electronics varies — check HS code) | 2.5 | 1.2 |
| Certification amortised (€14k at 1k; same €14k at 5k) | 14.0 | 2.8 |
| **Landed cost** | **30.0** | **13.9** |
| Channel: direct D2C (payment + returns + shipping subsidy ~€8) | 8.0 | 8.0 |
| Net price received (D2C €59 incl. 21% VAT → €48.8 ex VAT) | 48.8 | 48.8 |
| **Gross margin D2C** | **€10.8 (22%)** | **€26.9 (55%)** |
| Retail channel (40% margin, you receive ~€29 ex VAT) | negative at 1k | €15 (52% on €29) |

Lesson: at 1k units you are paying for certification, not making money. Retail only makes sense after 5k. Tooling for the diffuser (~€6–9k for two parts, estimate) is on top; use a 3D-printed/urethane-cast run for the first 200.

### Go-to-market

**First 100 customers:** Tweakers Energie forum, r/tibber, r/Zonneplan, Home Assistant NL/DE Discord, Photovoltaikforum.com, the Dutch "Slimme meter" Facebook groups, akkudoktor forum (DE). One good video of the lamp changing colour at 14:00 when solar peaks. Refundable €10 deposit.

**Then scale:** (1) retailer co-branding — pitch two Dutch and two German dynamic-tariff retailers an onboarding gift pilot of 500 units; (2) HomeWizard/Tibber-adjacent marketplaces and Tweakers Pricewatch listing; (3) Amazon.de/.nl once the margin tolerates 15% fees; (4) PV installers as an upsell with an inverter.

### 12-month plan

- **Q1:** kill-question experiment (landing page + deposits). Works-like prototype on Stamp-C5/C3 devkit. Decide at week 6. Request lab quotes.
- **Q2:** own PCB (one spin), diffuser design, 50-unit pilot with 3D-printed housings to depositors. Firmware hardened (signed OTA, EN 18031 checklist). Pre-compliance scan.
- **Q3:** tooling, RED/EMC/safety testing, EN 18031 self-assessment, declaration of conformity. 1,000-unit run. Ship pre-orders.
- **Q4:** retailer pilot (500 co-branded), Amazon listing, second colour/size SKU, surplus mode via P1 readers.

**Team:** one firmware/cloud engineer (full-time), one hardware/industrial designer (half-time), one founder doing sales, community and ops. A sourcing partner in Shenzhen for PCBA + enclosure.

**Funding to first 1,000 units (estimate):** PCBA + enclosure + packaging landed €16k (1,000 × €16 excl. cert) + tooling €8k + certification €14k + pilot run & samples €4k + 6 months of two half-salaries/contractors €40k + marketing €5k = **≈€87k**. Pre-orders (500 × €49 = €24.5k) plus a retailer pilot deposit can cover a third. Route: bootstrap + pre-orders; a regional energy-transition grant (NL: RVO/MIT; DE: regional digital bonus) for the firmware; angel only if the retailer deal lands and you need working capital for 5k.

### Top risks

| Risk | Mitigation |
|---|---|
| **Market:** "the app is enough" | The deposit experiment answers this for €500 before any PCB |
| **Technical:** price data source changes or costs money (ENTSO-E API keys, retailer formulas differ by supplier) | Run a tiny proxy you control; device never talks to third parties directly; ship a tax/margin editor |
| **Regulatory:** EN 18031 and CRA on a €59 gadget | Keep it simple: no cloud account, signed OTA, no open ports; self-declare under EN 18031-1 where no restrictions apply |
| **Supply:** addressable LED colour binning, module EOL | Spec LEDs with CCT/bin tolerance; design for two module footprints (C3 and C5-class) |
| **Commercial:** retailers copy it as a giveaway | Be first and be their supplier; margin is in B2B volume, not patents |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Stamp-C5 (S016) | https://www.gongbans.com/db/m5stack-stamp-c5.html | WiFi MCU core; open Altium pcb+schematic to copy the module footprint, antenna keep-out and USB path | pcb, schematic (Altium) | M5_Hardware repo — check the repo licence before copying into a commercial design |
| Espressif esp32-c3-devkitm-1 | https://www.gongbans.com/db/espressif-esp32-c3-devkitm-1.html | Lower-cost WiFi MCU alternative; official reference schematic for power/USB/strapping | schematic | Espressif reference design terms — check |
| Seeed Grove-Chainable RGB LED | https://www.gongbans.com/db/seeed-grove-chainable-rgb-led.html | RGB light-engine reference circuit (chainable LED driver) | schematic | Seeed wiki resources — check licence (often CC) |
| OSHWHub 多用途RGB灯控制板-402304A | https://www.gongbans.com/db/oshwhub-rgb-deng-kong-zhi-qi-402304a.html | Open RGB-strip driver (5 V/12 V strips, button, IR, Tuya app) — the driver and power topology for a diffuser lamp | schematic, pcb (EasyEDA) | OSHWHub project licence shown on the project page — check; it uses a Tuya module, which you will replace |

Catalogue honesty: the chip field is empty for the Stamp-C5 row; the "C5" name suggests an ESP32-C5-class part but verify on the M5 docs.

### Block diagram

```
USB-C 5V ──► 3.3V LDO ──► ESP32-C3/C5 module (WiFi, flash)
                │                 │ GPIO (data)
                │                 ▼
                └──► 8× addressable RGB LEDs (ring) ──► frosted diffuser
                                  │
                      touch pad (hold = cheapest window)
WiFi ──► your proxy (day-ahead prices, retailer formula, OTA) ──► device
Optional local: MQTT to Home Assistant / P1 reader for solar-surplus mode
```

**Engineering gap:** almost none in electronics. The work is firmware (price fetch, formula editor, captive portal, signed OTA, EN 18031 hygiene), the proxy service, and a diffuser that looks like furniture, not a gadget. Thermal: 8 LEDs at full white in a closed diffuser — keep total LED power under ~1.5 W.

### Starter BOM (estimates)

| Part | Est. unit cost @1k | Notes |
|---|---|---|
| ESP32-C3-MINI-1 or C5-class module (pre-certified) | €2.2–3.0 | Two footprints on PCB; module RED pre-cert is what keeps RED cheap |
| 8× WS2812B/SK6812-class RGB LEDs (5050) | €1.0–1.4 | Bin by colour; test for amber consistency |
| USB-C receptacle + ESD + 5 V→3.3 V LDO | €0.9 | USB-C 5.1k CC resistors for proper 5 V |
| Capacitive touch pad (PCB copper) | €0 | Firmware only |
| 2-layer PCB ~60 mm round | €0.8 | |
| Diffuser + base (PC/PMMA frosted, ABS base) | €2.5–4 | Tooling €6–9k, or cast/3D-print first 200 |
| USB-A to C cable 1 m | €0.7 | |
| Box + leaflet | €1.2 | |

No long-lead or sole-source parts if you avoid exotic LEDs. The ESP module is the only item with occasional 8–12 week lead; buy 1,200 early.

### Firmware/software starting point

- **ESP-IDF** or **ESPHome** (ESPHome gives you captive portal, OTA, MQTT/HA discovery and light control for free; good for the pilot; for the product move to ESP-IDF for signed OTA/secure boot control).
- **WLED** / **FastLED** for LED effects if you go Arduino-style.
- Price data: **ENTSO-E Transparency Platform API** (day-ahead prices by bidding zone; free token). Retailer APIs (Tibber GraphQL exists; others — search).
- Solar surplus: **HomeWizard P1 local API** and Tibber Pulse — search current docs.
- Backend proxy: anything small (a Cloudflare Worker or a €5 VPS) caching day-ahead once per day.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — landing page NL/DE, render, €10 refundable deposit; devkit + Grove RGB + IKEA frosted lamp video | ≥3% visitor→deposit and ≥100 deposits; otherwise stop |
| 3–5 | **Works-like** — Stamp-C5 devkit, 8-LED ring, ESPHome build fetching ENTSO-E via proxy; 10 units at depositors' homes | 10/10 units run 14 days without reset; users report they "looked at it" daily |
| 6–8 | **Looks-like + EVT** — own PCB rev A (both module footprints), printed diffuser, 30 units; thermal and WiFi range checks | Rev A passes functional test; LED power <1.5 W; WiFi −70 dBm at 10 m through a wall |
| 9–10 | **DVT + pre-compliance** — rev B if needed; pre-scan radiated emissions at a local lab (€1–2k); EN 18031 self-assessment checklist; signed OTA working | No emissions fails >3 dB margin; OTA rollback demonstrated; test report drafts ready |
| 11–12 | **Pilot batch** — 50 units with cast/printed housings, full packaging, to depositors; collect NPS and returns | ≤2 field failures of 50; ≥8/10 would recommend; MOQ + tooling quotes signed |

### Certification checklist (EU)

- **CE — RED** (WiFi): EN 300 328 covered by the pre-certified module; still need **EN 301 489-1/-17** (EMC) and **EN 62368-1** (safety; low-voltage USB device so light testing) on the final product: €6–10k (estimate).
- **RED delegated act cybersecurity — EN 18031-1** (internet-connected): applies since 1 Aug 2025. Self-assessment possible if no restricted clauses apply (keep no default passwords, signed updates). Budget €2–4k for a consultant review, more if a notified body is needed.
- **CRA:** reporting obligations live since Sept 2026, full obligations Dec 2027 — ship an SBOM, a vulnerability contact and a 5-year update plan.
- **RoHS** (declaration + supplier CoCs), **WEEE** registration per country sold (NL, DE — Stiftung EAR costs €, budget €1–2k/yr), **REACH** SVHC declaration, **Packaging** registration (DE LUCID).
- No battery, no mic, no camera → no Battery Regulation, GDPR only if account linking (keep tokens on-device; state it).
- **Total estimate:** €12–16k first year.

### Validation toolkit

- **Kill question:** Will 100 people on dynamic-tariff forums pre-order at €59 from a landing page with a render? Pass = >3% conversion to a refundable deposit. Cheapest experiment: €200 ads + a weekend, as above.
- **Interview script (5):** 1) Which tariff, since when, and what do you actually shift? 2) Where in your home would a price lamp sit, and who else would see it? 3) What did you try before (app, HA automation, bulb)? Why did it stop working? 4) Price now vs trend for next hours vs cheapest window — which one would make you act? 5) €49, €59 or €79 — at which price do you stop, and would you want it as a gift from your retailer?
- **Landing page:** Headline: "Your electricity price, as a colour in your kitchen." Bullets: "Green = run it now. Red = wait." / "Works in 2 minutes with any dynamic tariff — no account needed." / "Solar surplus mode: free power glows bright green."
- **Pre-order pass:** ≥100 deposits of €10 within 30 days at ≥3% conversion.

### First production checklist

- 3 PCBA samples from two assemblers; **golden sample** signed with the factory (LED colour reference photos under defined light).
- **DFM review** of diffuser draft angles, light leakage at the base seam, USB-C alignment.
- **MOQ talk:** PCBA 500 / 1,000; enclosure moulder MOQ usually 1,000 shots — negotiate 500 with a higher unit price.
- **QC/AQL:** ANSI/ASQ Z1.4 level II, AQL 1.0 major / 2.5 minor; 100% functional test with a fixture that checks all 8 LEDs in R, G, B and WiFi join.
- **Packaging:** drop test ISTA 1A; include EU DoC URL and WEEE symbol.
- **Incoterms:** FOB Shenzhen for sea; DAP for the first air shipment so you learn the duty line (HS 9405 vs 8517 — your customs broker decides, and it changes duty).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and Espressif and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Stamp-C5 (S016)](/db/m5stack-stamp-c5.html) (WiFi MCU core (open PCB + schematic)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c3-devkitm-1](/db/espressif-esp32-c3-devkitm-1.html) (lower-cost WiFi MCU alternative). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Chainable RGB LED](/db/seeed-grove-chainable-rgb-led.html) (RGB light-engine reference circuit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [【训练营】多用途RGB灯控制板-402304A](/db/oshwhub-rgb-deng-kong-zhi-qi-402304a.html) (open RGB-strip driver board for the diffuser lamp).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Linkage Technology** (深圳市联控智能科技有限公司) · linkage-tech.com — Smart meter / energy IoT solution house: Smart energy meter; sub-metering IoT; NB-IoT / LoRa; OEM/ODM. *(Smart-metering / energy IoT)*
- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Espressif and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Stamp-C5 (S016), Espressif esp32-c3-devkitm-1, Seeed Grove-Chainable RGB LED — for a Tariff Lamp

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Tariff Lamp: A small lamp that glows green, amber or red with your actual hourly electricity price (and solar surplus) so the household runs the dishwasher when power is cheap — no app, no dashboard. The design is built around your M5Stack Stamp-C5 (S016), Espressif esp32-c3-devkitm-1, Seeed Grove-Chainable RGB LED.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Stamp-C5 (S016), Espressif esp32-c3-devkitm-1, Seeed Grove-Chainable RGB LED.
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
主题：样品订购及批量报价 — M5Stack Stamp-C5 (S016), Espressif esp32-c3-devkitm-1, Seeed Grove-Chainable RGB LED — 用于Tariff Lamp

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tariff Lamp：A small lamp that glows green, amber or red with your actual hourly electricity price (and solar surplus) so the household runs the dishwasher when power is cheap — no app, no dashboard。产品设计基于贵司的M5Stack Stamp-C5 (S016), Espressif esp32-c3-devkitm-1, Seeed Grove-Chainable RGB LED。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Stamp-C5 (S016), Espressif esp32-c3-devkitm-1, Seeed Grove-Chainable RGB LED。
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
Subject: PCBA quote from open design files — Tariff Lamp, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Tariff Lamp: A small lamp that glows green, amber or red with your actual hourly electricity price (and solar surplus) so the household runs the dishwasher when power is cheap — no app, no dashboard. The design starts from published open-hardware files (【训练营】多用途RGB灯控制板-402304A; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Tariff Lamp，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Tariff Lamp：A small lamp that glows green, amber or red with your actual hourly electricity price (and solar surplus) so the household runs the dishwasher when power is cheap — no app, no dashboard。设计基于已公开的开源硬件文件（【训练营】多用途RGB灯控制板-402304A；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Build the landing page (NL + DE) with a render and €10 deposit; post in Tweakers Energie, r/tibber, HA NL Discord; spend €200 on ads.
2. Order a Stamp-C5 and a C3 devkit, a Grove chainable RGB LED and an IKEA frosted lamp; get the ENTSO-E token and have prices glowing by Friday.
3. Ask two EU labs for a RED/EMC/safety quote on "USB-powered WiFi lamp with pre-certified module" and confirm whether EN 18031-1 self-declaration applies to your feature set.

Want help sourcing or building this? Talk to us via www.gongbans.com.
