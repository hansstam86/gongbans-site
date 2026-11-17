# Quiet-Hours Guard for Rentals — Founder Start Pack

> A host-owned sensor for short-stay apartments that measures noise level and roughly how many people are present, without recording audio or images. It warns the guests first and the host second, before the neighbours complain.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** One loud night costs a short-stay host far more than a cleaning fee: neighbour complaints, building-association fights, platform penalties and, in cities like Amsterdam, Barcelona, Lisbon, Paris and Berlin, fines or a lost permit. Hosts find out the next morning.
- **Customer:** Professional short-stay hosts and management companies with 5–200 units in strict EU cities. They pay. Guests are "users" only in the sense that they see the warning light.
- **Product:** A small mains-powered box: on-device dB(A) metering from a PDM microphone (level only, audio never stored or sent), a 24 GHz multi-target radar (Hi-Link LD2452) for a rough "how many people are moving in this room" signal, and an LTE-M uplink that doesn't depend on the guest Wi-Fi. Escalation: an in-room light and short voice/beep nudge to the guests first, then a message to the host.
- **Why now:** Cities are tightening short-stay rules and revoking permits over nuisance; platforms push hosts towards noise monitoring and have banned indoor cameras. The incumbents are subscription-first (around €10–15 per unit per month) and infer occupancy from Wi-Fi devices rather than people.
- **The ask:** About €130–160k (estimate) to the first 1,000 units. Route: pre-orders from management companies + a small angel round. Revenue: €149 device + an optional €4/month plan (or no plan, with local alerts only).

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will 30 hosts pay €149 + monthly when incumbent noise monitors exist? Differentiator must be people-count + no-subscription option; test with a host forum survey and 10 pre-orders.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Short-stay hosts and management companies in Amsterdam, Barcelona, Lisbon, Berlin, Paris where nuisance rules and permits are strict.

**The problem as the pack states it:** One loud night costs a short-stay host far more than a cleaning fee: neighbour complaints, building-association fights, platform penalties and, in cities like Amsterdam, Barcelona, Lisbon, Paris and Berlin, fines or a lost permit. Hosts find out the next morning.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/AirBnBHosts** · https://www.reddit.com/r/AirBnBHosts/ — short-stay hosts; party and noise complaints come up often.
- **Airbnb Community Center** · https://communitycenter.airbnb.com/ — Airbnb's own host forum, with country and language boards.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149 + €4/month (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how short-stay hosts and management companies in Amsterdam, Barcelona, Lisbon, Berlin, Paris where nuisance rules and permits are strict deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last noise complaint or party in one of your rentals: how did you find out, how late, and what did it cost you?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A host-owned sensor for short-stay apartments that measures noise level and how many people are present — without recording audio or images — and warns guests first, the host second, before neighbours complain. On a scale of one to ten, how likely would you be to buy that at €149 + €4/month (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Quiet-Hours Guard for Rentals: would you pay €149 + €4/month (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Quiet-Hours Guard for Rentals: A host-owned sensor for short-stay apartments that measures noise level and how many people are present — without recording audio or images — and warns guests first, the host second, before neighbours complain. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149 + €4/month (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Hosts don't want to spy on guests. They want **early warning** and a **record that they acted**, because that's what a city inspector, a building association or a platform asks for after a complaint. The guest-first escalation matters: most groups turn it down when a light goes amber; a host call at 01:00 is the second step, not the first.

**Who pays:** management companies (10–200 units) first. They buy in batches, handle installation during cleaning turnovers, and have a nuisance-compliance problem with their city. **Then:** individual pro hosts with 2–10 units, through host communities.

**Who doesn't buy:** hosts renting a room in their own home (they're there), and the big hotel-like operators (they have night staff).

### Market size (estimates)
- Short-stay listings in the EU are in the low millions; assume ~1.5 M entire-home listings in cities with active nuisance enforcement (estimate, check current platform/Eurostat short-stay data).
- **TAM:** 1.5 M × (€149 + 3 years × €48) ≈ **€440 M** over a 3-year device life.
- **SAM:** professionally managed units in NL, ES, PT, FR, DE, IT big cities, ~30% → **~450k units ≈ €130 M**.
- **SOM (3 years):** 1.5% of SAM → **~7,000 units ≈ €1 M device revenue + ~€330k/yr recurring.**

### Competition
| Alternative | Price (published/listings, estimate) | Weakness we attack |
|---|---|---|
| Minut (Swedish, sensor + platform) | Subscription per unit, roughly $10/unit/month for add-on plans or ~£120/yr core plan per property (published, varies by market) | Subscription-heavy; occupancy estimate is not a people count |
| NoiseAware | Starter ~$15/month per property; outdoor sensor $99 one-time (published, US-centric) | US focus, no EU pricing published; relies on Wi-Fi |
| Roomonitor, Alertify and similar | Device + monthly | Similar model; Wi-Fi-dependent |
| Building/smart-home sound sensors (DIY with a sound meter + home automation) | €30–100 + time | Not practical across 20 units; no audit trail |
| Do nothing; deal with complaints | Free until the fine | Permit risk, bad reviews from neighbours, platform penalties |

**Wedge:** (1) **people count from radar**, not "number of phones on Wi-Fi" (guests can turn Wi-Fi off; radar doesn't care), (2) **LTE-M uplink** so the guest can't "unplug the router" to blind it (but see power: unplugging the box itself still needs a tamper alert), (3) **no-subscription option** with local nudges and an SMS to the host, (4) a ready-made **disclosure kit** (listing text, sticker, house rules) for GDPR and platform policies.

**Honest limitation:** the LD2452 tracks up to **three** targets per sensor (per Hi-Link's datasheet), within ~6 m. So the "people count" saturates at 3+ per room. That's still a useful party signal ("3+ people moving in the living room at 01:30 with 78 dB(A)") but it isn't a headcount. A second sensor in the large room or a combined dB + motion-density heuristic gets you further. Don't market "counts guests".

### Product & value proposition
- **Noise:** on-device A-weighted level (Leq over 1 min, peak, and "time above threshold"), using a PDM MEMS mic. Firmware never stores or transmits samples: only levels leave the chip. Publish the firmware audit or the relevant source to prove it.
- **Occupancy:** LD2452 in the main living area, wall-mounted horizontally (as the datasheet specifies), gives 0–3+ moving targets.
- **Escalation:** quiet-hours schedule per unit (e.g. 22:00–07:00), thresholds per building. Step 1: in-room amber light + a short chime. Step 2 after 10 min: host alert (app push / SMS / webhook into the property-management system). Step 3: log entry "host contacted guest at 01:12" for the record.
- **Connectivity:** LTE-M (Cat-M) so it works without guest Wi-Fi; a Wi-Fi-only SKU for cheaper deployments.
- **Tamper:** "device offline/unplugged" alert; mains-powered with a small backup capacitor or cell to send the last-gasp message.

**Pricing (estimates):** €149 device (LTE-M), €119 Wi-Fi only. Plans: €0 (local nudge + SMS to host, limited), €4/unit/month (dashboard, PMS integration, history export for authorities). Management-company bundle: 10 units for €1,290.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (MCU/Wi-Fi module, PDM mic, LD2452, LTE-M module + SIM holder, LED ring, buzzer, AC-DC, PCB) | €36.00 | €29.00 |
| Assembly & test (radar + mic level calibration with a reference source, LTE-M attach test) | €3.50 | €2.50 |
| Enclosure (wall-mount, light-pipe ring) | €2.50 | €1.50 |
| Packaging + disclosure sticker kit | €1.50 | €1.00 |
| Freight + duty to EU | €1.20 | €0.80 |
| Certification amortised (~€35k: RED incl. cellular, EMC, LVD for mains, EN 18031) | €35.00 | €7.00 |
| **Landed cost** | **€79.70** | **€41.80** |
| Net price ex-VAT: direct ~€125 (from €149 incl. VAT) / via reseller or PMS partner ~€90 | €125 / €90 | €125 / €90 |
| **Gross margin (device)** | **€45 (36%) direct / €10 (11%) reseller** | **€83 (67%) / €48 (54%)** |

Recurring: cellular data at ~€0.50–1/unit/month (IoT SIM, estimate) means the €4 plan nets ~€3; the free plan costs you ~€0.50–1/month per unit forever. **Fix that before launch:** either include 24 months of connectivity in the device price and charge after, or make the free tier Wi-Fi-only. At 1k units the device margin is thin through resellers: sell direct for the first batch.

### Go-to-market
**First 100 customers:**
- **Host associations and short-stay management meetups** in Amsterdam, Barcelona, Lisbon, Berlin, Paris. Management companies show up there.
- **Host forums and Facebook/LinkedIn groups** for professional short-stay hosts: run the kill-question survey there.
- **Property-management system (PMS) marketplaces:** an integration listing is a sales channel in itself.
- **Building associations / owner associations** with nuisance problems: they can recommend (or require) it for units rented short-stay.

**Scale channels:** PMS and channel-manager partners, insurers that cover short-stay damage (discount for monitored units), city "good host" programmes.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Host survey + 10 pre-orders (kill question); works-like box on devkits in 5 friendly units; legal check on in-dwelling monitoring in 3 target countries |
| Q2 | Custom PCB with LTE-M; firmware with level-only audio pipeline; dashboard v1; EVT 50 units with 2 management companies |
| Q3 | DVT, RED/EMC/LVD/EN 18031 testing; PMS integration #1; launch at a host event |
| Q4 | 1,000 units shipped; paid plan live; insurer/PMS partnership conversation |

**Team:** founder (sales into host/management companies), 1 embedded engineer (audio DSP for dB(A), radar, LTE-M), 1 full-stack developer (dashboard, alerts, PMS integration), part-time privacy/legal adviser.

**Funding to the first 1,000 units (estimates):** NRE €70k (electronics €15k, firmware €25k, dashboard/alerts €20k, enclosure + soft tooling €10k) + certification €35k + 1,000 units landed ex-cert ~€45k + connectivity year 1 ~€8k + 9 months lean costs €40k ≈ **€198k**; minus pre-orders (~300 units × €125 ≈ €37k) → **~€160k**. Route: management-company pre-orders, then an angel from the proptech/hospitality space.

### Top risks
| Risk | Mitigation |
|---|---|
| **Market: incumbents are established and platform-endorsed** | Don't fight on features; fight on "people, not phones", LTE-M and the no-subscription option. Validate with 10 pre-orders before building |
| **Legal/privacy: monitoring inside a dwelling** | Level-only audio, no images; mandatory disclosure in the listing and on the device; DPIA template; legal check per country (DE is strictest); never market as surveillance |
| **Technical: dB(A) accuracy** | Calibrate each unit against a reference source at end of line; specify "indicative, not a class-1/2 sound level meter" |
| **Technical: radar count saturates at 3 targets** | Communicate honestly; optional second sensor; use motion density + noise over time |
| **Platform policy changes** | Track platform host policies for noise monitors; disclosure kit updated |
| **Recurring cost of the free plan (cellular)** | Wi-Fi-only free tier or a time-limited bundled data plan |
| **Supply: LD2452 single source** | Abstract the radar protocol layer; qualify an alternative multi-target radar module |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit Mini PDM (U089) | https://www.gongbans.com/db/m5stack-unit-mini-pdm.html | PDM MEMS microphone for dB level metering in the works-like prototype | Enclosure/structure files only (main-board electronics not published) | Dev unit; production uses your own mic layout |
| Hi-Link HLK-LD2452 multi-target radar | https://www.gongbans.com/db/hilink-ld2452.html | Tracks up to 3 targets, 6 m, ±60° H / ±30° V, UART, 5 V avg 126 mA (per datasheet) | Datasheet public; schematics/files via maker (contact Hi-Link) | Commercial module, no open design files |
| M5Stack Unit CatM (U128) | https://www.gongbans.com/db/m5stack-unit-catm.html | LTE-M uplink independent of guest Wi-Fi, for prototyping | Enclosure/structure files only | Dev unit; production uses a pre-certified LTE-M module |

### Block diagram
```
[PDM mic] --PDM--> [MCU (ESP32-class)] -- dB(A) Leq/peak only, no samples leave the chip
[LD2452 radar] --UART-->     |
                             |-- amber LED ring + chime (guest nudge)
                             |-- LTE-M module --> [cloud: alerts, dashboard, PMS webhook]
                             `-- Wi-Fi (optional SKU)
[mains] -> [isolated AC-DC] -> [5 V / 3.3 V] + last-gasp capacitor for the "unplugged" alert
```
**Engineering gap:** A-weighting filter and Leq computation on the MCU (with a provable "no audio leaves" pipeline), radar mounting and zone tuning for living rooms, escalation logic and quiet-hours schedules, LTE-M power and provisioning, tamper/offline detection, the host dashboard and PMS integration.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-S3 or -C3 module | €2.50 | Enough DSP for A-weighting at 16 kHz |
| PDM MEMS microphone | €0.60 | Pick one with a published sensitivity tolerance |
| HLK-LD2452 radar | €7–9 | Sole source (Hi-Link); confirm price and MOQ |
| LTE-M module (pre-certified) + SIM holder/eSIM | €9–12 | **Long-lead risk**; cellular operator certification can take weeks |
| IoT SIM (per unit, first year) | €6–10 | Recurring |
| Isolated AC-DC 5 W | €2.50 | Or USB-C wall adapter version (avoids LVD on the device) |
| LED ring, buzzer, button, passives, PCB | €3.00 | |

### Firmware/software starting point
- **ESP-IDF** with the I2S/PDM driver; A-weighting filters are standard IIR biquads (search "A-weighting IIR biquad coefficients 16 kHz").
- **Radar:** Hi-Link's LD2452 serial protocol from the datasheet; ESPHome has community components for related Hi-Link radars (search "ESPHome LD2450") that show the frame format style.
- **Cellular:** the LTE-M module vendor's AT command set; M5Stack's Unit CatM examples for the prototype (search the M5Stack docs).
- **Backend:** any EU-hosted stack; alerts via SMS gateway and push; webhooks for PMS systems.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** host-forum survey (≥80 answers) + 10 pre-orders/deposits from hosts or management companies. Pass: ≥10 deposits and ≥40% of surveyed pros rate "people count without cameras" as a top-2 reason |
| 3–5 | Works-like | Devkits in 5 real units: dB(A) within ±2 dB of a reference meter; radar 0/1/2/3+ classification correct ≥85% of 5-min windows; host alert end-to-end over LTE-M |
| 6–8 | Looks-like + EVT | Custom PCB, wall-mount enclosure, LED ring; 30 units at 2 management companies; guest nudge resolves ≥60% of events without host contact |
| 9–10 | DVT + pre-compliance | RED pre-scan (24 GHz, LTE-M, 2.4 GHz), EMC, safety; EN 18031 gap analysis; privacy review of the audio pipeline |
| 11–12 | Pilot batch | 50 units deployed; < 1 false host alert per unit per month; 2 management companies ask for a quote for all units |

### Certification checklist (EU)
- **CE under RED:** 24 GHz radar (EN 300 440), LTE-M (EN 301 908-1/-13; use a pre-certified module to reuse its reports), 2.4 GHz (EN 300 328), EMC (EN 301 489 series), safety EN 62368-1, RF exposure. Mains-powered device: the safety assessment covers LVD-type risks; a USB-adapter version simplifies this. Est. **€15–22k**.
- **RED delegated act cybersecurity: EN 18031-1, -2 (processes personal data: noise level + presence inside a home) and -3 if any payment features (no).** Est. **€8–12k**.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: signed OTA, SBOM, vulnerability handling, support period.
- **RoHS, REACH, WEEE, packaging registration.**
- **GDPR (big one):** noise levels and presence in a rented dwelling are personal data about guests. Legal basis = the host's legitimate interest, with transparency: disclosure in the listing, in the house rules and on the device. DPIA template for management companies. Data minimisation: store levels/counts, delete raw timelines after e.g. 30 days. Check national rules on monitoring inside dwellings (and ePrivacy if anything touches communications).
- **Platform policies:** check each short-stay platform's current rules on noise monitors (typically allowed if disclosed, decibel-only; cameras inside banned).
- **Total estimate: €25–35k.**

### Validation toolkit
- **Kill question:** Will 30 hosts pay €149 + monthly when incumbent noise monitors exist? The differentiator must be people count + a no-subscription option; test with a host forum survey and 10 pre-orders.
- **Cheapest experiment (~€0–200):** a landing page with the €149 offer and a €20 refundable deposit, posted in 5 host communities, plus 10 calls with management companies. No hardware needed yet.
- **5-question interview (host / management company):**
  1. How many nuisance complaints did your units get last year, and what did each one cost you?
  2. What do you use today to know about a party before the neighbours call? What's wrong with it?
  3. How do you disclose monitoring to guests today? Ever had a guest complain about it?
  4. Would you pay more for "how many people are there" versus "how loud"? How much more?
  5. Device €149 with no subscription, or €49 + €10/month: which, and for how many units?
- **Landing-page headline:** "Know about the party before the neighbours do."
  - Measures noise and people. Never records sound or images.
  - Warns the guests first, then you, over its own mobile link.
  - No subscription needed. Disclosure kit included.
- **Pass threshold:** ≥10 paid deposits (≥3 from management companies) within 4 weeks, or one management company signing a 50-unit letter of intent.

### First production checklist
- **Samples:** mic sensitivity spread across 20 samples (decides whether per-unit calibration is needed); radar modules from the production lot.
- **Golden sample:** calibrated dB reading at 94 dB(A) reference, radar target test, LTE-M attach; firmware hash recorded.
- **DFM review:** mic port acoustic path (sealing gasket, no cavity resonance), radar window material and thickness, LED light-pipe, mains creepage distances if AC-DC inside.
- **MOQ talk:** LTE-M module (operator variants), radar module, LED ring parts.
- **QC/AQL:** AQL II 1.0/2.5; 100%: mic level at reference tone ±1 dB, radar detects a reference target, LTE-M registers, LED/buzzer check, firmware audio pipeline locked (debug ports disabled).
- **Packaging:** device, mounting kit, disclosure sticker for the door and the device, listing-text card with QR code to the privacy notice.
- **Incoterms:** FCA Shenzhen; air for the pilot; consider DDP for the first batch so customs (radio + cellular) isn't your problem.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Hi-Link (海凌科)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Mini PDM (U089)](/db/m5stack-unit-mini-pdm.html) (PDM microphone used only for dB level, no audio stored); [M5Stack Unit CatM (U128)](/db/m5stack-unit-catm.html) (Cat-M uplink independent of the guest Wi-Fi). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2452 24 GHz multi-target positioning and tracking radar module](/db/hilink-ld2452.html) (multi-target radar for a rough people count). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Hi-Link (海凌科) websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module — for a Quiet-Hours Guard for Rentals

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Quiet-Hours Guard for Rentals: A host-owned sensor for short-stay apartments that measures noise level and how many people are present — without recording audio or images — and warns guests first, the host second, before neighbours complain. The design is built around your M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module.
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
主题：样品订购及批量报价 — M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module — 用于Quiet-Hours Guard for Rentals

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Quiet-Hours Guard for Rentals：A host-owned sensor for short-stay apartments that measures noise level and how many people are present — without recording audio or images — and warns guests first, the host second, before neighbours complain。产品设计基于贵司的M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module。
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
Subject: PCBA quote from open design files — Quiet-Hours Guard for Rentals, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Quiet-Hours Guard for Rentals: A host-owned sensor for short-stay apartments that measures noise level and how many people are present — without recording audio or images — and warns guests first, the host second, before neighbours complain. The design starts from published open-hardware files (M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Quiet-Hours Guard for Rentals，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Quiet-Hours Guard for Rentals：A host-owned sensor for short-stay apartments that measures noise level and how many people are present — without recording audio or images — and warns guests first, the host second, before neighbours complain。设计基于已公开的开源硬件文件（M5Stack Unit Mini PDM (U089), M5Stack Unit CatM (U128), HLK-LD2452 24 GHz multi-target positioning and tracking radar module；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Put up the landing page with a €20 refundable deposit and post it in 5 host communities and 2 management-company networks.
2. Order 5 LD2452 modules, 5 PDM mic units and an LTE-M dev unit; get a dB(A) reading within ±2 dB of a cheap reference meter on the bench.
3. Ask a privacy lawyer for a one-hour check on "level-only noise + radar presence in a short-stay rental" in DE, NL and ES; turn the answer into the disclosure kit.

Want help sourcing or building this? Talk to us via www.gongbans.com.
