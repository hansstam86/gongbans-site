# Isolated Bench Power Module — Founder Start Pack

> A breadboard-friendly module that gives analog and audio projects isolated ±12 V, ±5 V and 3.3 V from a USB-C port, plus an isolated USB-UART — so you stop blowing up laptops, scopes and USB ports through ground loops.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Makers, students and repair-café volunteers power op-amp and audio circuits from 9 V batteries or a cheap non-isolated breadboard supply, then plug in a scope and a laptop and create a ground loop. Result: hum, noise, a dead USB port, or worse. Proper isolated dual rails mean a bench supply most hobbyists don't own.
- **Customer:** Electronics hobbyists (audio DIY, synth DIY, analog), engineering students and their labs, repair cafés, test engineers who need a quick isolated rail. Electronics retailers and maker shops sell it.
- **Product:** A breadboard-straddling module: USB-C in → three isolated DC-DC stages (±12 V, ±5 V, 3.3 V), each with a current limit and an LED; jumper rail selector; plus an isolated USB-UART on the same board. Clear isolation-barrier silkscreen and a "what isolation does and doesn't protect" card in the box.
- **Why now:** Isolated regulated dual-output DC-DC modules now cost a few euros, high-CMTI digital isolators are cheap, and an open isolated-USB design already exists to learn from. Synth DIY and audio DIY communities keep growing.
- **The ask:** ~€45k to first 1,000 units (no radio, no tooling — this is a PCB with a box). Kill question: will one distributor order 500?

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Will electronics retailers/maker shops list it next to their breadboard PSUs at €39? One distributor order of 500 is the pass line.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Makers, electronics students, audio DIY community, repair cafés, test engineers.

**The problem as the pack states it:** Makers, students and repair-café volunteers power op-amp and audio circuits from 9 V batteries or a cheap non-isolated breadboard supply, then plug in a scope and a laptop and create a ground loop. Result: hum, noise, a dead USB port, or worse. Proper isolated dual rails mean a bench supply most hobbyists don't own.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **diyAudio forum** · https://www.diyaudio.com/community/ — audio DIY builders; power supplies and ground loops are core topics.
- **EEVblog forum** · https://www.eevblog.com/forum/ — electronics engineers and serious hobbyists; test-equipment and soldering opinions.
- **r/AskElectronics** · https://www.reddit.com/r/AskElectronics/ — electronics hobbyists and students.
- **Repair Café International** · https://www.repaircafe.org/ — network of volunteer repair cafés; the local café is the way in.
- **mikrocontroller.net (DE)** · https://www.mikrocontroller.net/ — German-speaking electronics engineers and students.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€35–49 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how makers, electronics students, audio DIY community, repair cafés, test engineers deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last time a ground loop, a noisy supply or a mains-adjacent circuit got in the way of a measurement or a repair: what did you use, and what went wrong?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A breadboard-friendly module that gives analog and audio projects isolated ±12 V, ±5 V and 3.3 V from USB-C, plus an isolated USB-UART — the safe way to probe mains-adjacent or ground-loop-prone circuits. On a scale of one to ten, how likely would you be to buy that at €35–49 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Isolated Bench Power Module: would you pay €35–49 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Isolated Bench Power Module: A breadboard-friendly module that gives analog and audio projects isolated ±12 V, ±5 V and 3.3 V from USB-C, plus an isolated USB-UART — the safe way to probe mains-adjacent or ground-loop-prone circuits. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €35–49 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

Isolation is the thing every beginner learns about the expensive way. The ADuM3160-style USB isolators sold to makers isolate data but supply little power. Breadboard PSUs give 5 V/3.3 V, not ±12 V, and are not isolated. Bench supplies with two floating channels start at €60–150 and don't fit on a breadboard.

- **Who pays:** hobbyists (D2C and via electronics web shops), university/vocational labs (bulk, 20–50 at a time), repair cafés (small budgets, grants), electronics retailers and maker distributors (wholesale).
- **Who uses:** same people; students in lab sessions.
- **Who influences:** YouTube electronics educators, synth-DIY forums, lab instructors who write the parts list.

### Market size (estimates — check)

- **TAM:** EU electronics hobbyists and students actively building circuits ≈ 2–3M people (rough, based on maker-community sizes — no hard source). If 10% buy one isolated supply in 3 years at €45 → **~€10–13M**.
- **SAM:** analog/audio/synth DIY + engineering labs + repair cafés ≈ 400k people/places; 10% → 40k units → **~€1.8M**.
- **SOM (3 years):** **5–8k units** through 3–5 distributors and D2C → €0.2–0.35M revenue. A good product line for a small maker brand; not a company on its own. Pair it with more modules later.

### Competition (1 search + category knowledge)

| Alternative | What it is | Why we can still win |
|---|---|---|
| Do nothing / 9 V batteries for ±9 V | Isolated by nature | Run flat, sag, not ±12 V, no current limit |
| MB102-style breadboard PSU (€2–5) | 5 V/3.3 V from USB/barrel jack | Not isolated, no negative rail |
| ADuM3160-based USB isolator modules (various maker brands) | Isolated USB data, limited isolated power | Data-only or ~100 mA; no ±rails |
| Bench PSU with two floating channels | Real tool | €60–300; not on the breadboard; students don't have one at home |
| DIY: buy isolated DC-DC modules and wire them | Cheapest | Noise, no current limit, no protection, an evening of debugging |
| Eurorack-style ±12 V supplies | For synth cases | Mains-powered, not isolated from your laptop ground in the way you need on the bench |

**Wedge:** the only (that we found) breadboard module with isolated ±12/±5/3.3 V **and** isolated UART from one USB-C — plus honest documentation of what isolation means.

### Product & value proposition

- **Rails:** ±12 V @ ~±80 mA (2 W module), ±5 V @ ~±100 mA (1 W module), 3.3 V @ ~200 mA (1 W module + LDO). Each output post-filtered (LC + low-noise LDO) — the isolated converters switch at hundreds of kHz; audio people will measure the noise and post it.
- **Protection:** per-rail resettable fuse or eFuse, LED per rail (on / overcurrent), reverse-polarity safe headers.
- **Isolated USB-UART:** USB-C → USB-UART bridge → 2-channel digital isolator → 3.3 V/5 V selectable UART header; isolated side powered by its own small converter.
- **Isolation rating — honest:** the DC-DC modules are rated 1,500 VDC isolation (functional), the isolator chip 5 kVrms. The system is **functional isolation for ground-loop breaking and low-voltage protection — not safety isolation for working on live mains.** Print it on the board and the card.
- **Form factor:** straddles a standard breadboard; screw terminals as an option; clear silkscreen barrier line; acrylic bottom plate.

**Pricing (estimates):** **€49** retail (the idea brief said €35–49; see unit economics — €39 doesn't survive a distributor). Lab 10-pack €399. Bare PCB + BOM kit for solderers €24.

### Unit economics (estimates, EUR per unit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (IA0512S-2W ~€3.0, IA0505S-1W ~€2.5, 2× B0505S-1W ~€1.6, CMT8121 isolator ~€0.7, USB-UART bridge €0.4, LDOs + LC filters €1.2, eFuses/polyfuses + LEDs €1.0, USB-C + headers + jumpers €0.9, 2-layer PCB with isolation slot €0.8) | 12.1 | 10.3 |
| PCBA assembly + test (incl. hipot sample test) | 1.8 | 1.2 |
| Acrylic base plate + standoffs | 0.5 | 0.4 |
| Packaging + isolation card | 1.0 | 0.7 |
| Freight + duty to EU | 0.5 | 0.3 |
| Certification/testing amortised (€8k) | 8.0 | 1.6 |
| **Landed cost** | **23.9** | **14.5** |
| D2C at €49 incl. VAT → €41.2 net, less €4 fulfilment | 37.2 | 37.2 |
| **Gross margin D2C** | **€13.3 (36%)** | **€22.7 (61%)** |
| Distributor at €49 retail (pays ~60% of net) → €24.7 | €0.8 (3%) | €10.2 (41%) |
| Distributor at €39 retail → €19.7 | -€4.2 | €5.2 (26%) |

Blunt: at €39 retail the kill-question distributor deal is a loss at 1k and thin at 5k. Price at €49, or take cost out (the 2 W ±12 V module is the lever; a single wider-input dual-output module with post-regulation for ±5 V is another).

### Go-to-market

**First 100 customers:**
- Synth-DIY and audio-DIY communities: modwiggler and diyAudio forums, the Lines community, r/synthdiy, r/diyaudio. Post noise measurements (scope screenshots of each rail) — that's the marketing.
- Two electronics YouTubers who do analog/repair content: send units, no paid placement.
- Repair cafés: offer 20 units at cost to a repair-café network in exchange for feedback and a mention.
- Pre-launch on a hardware crowdfunding marketplace (e.g. Crowd Supply, Tindie for the first batch) — check their fees.

**Then scale:** EU electronics web shops and maker distributors (DE, NL, UK, Nordics), university lab purchasing (one lab instructor → 30 units/year), bundle with analog course kits.

### 12-month plan

- **Q1:** prototype on dev modules; noise and isolation measurements; 3 distributor conversations with a sample; community post with data.
- **Q2:** rev A, 50-unit beta to forum members and repair cafés; EMC pre-scan.
- **Q3:** rev B, EMC test, 1,000-unit run; crowdfunding/marketplace launch; first distributor orders.
- **Q4:** lab 10-packs; second product in the line (e.g. isolated USB-C PD power-only module, isolated I²C/SPI probe).

**Team:** one hardware engineer-founder (this is a one-person product to start), part-time help for shop/fulfilment, a Shenzhen PCBA partner.

**Funding to first 1,000 units (estimate):** landed hardware excl. cert (1,000 × €15.9) €16k + test fixtures €2k + EMC/safety testing €8k + prototypes/beta €3k + 4 months founder runway part-time €12k + marketing/samples €3k = **≈€44k**. Offsets: crowdfunding/marketplace pre-orders (300 × €45 = €13.5k), distributor pre-order (500 × €24.7 = €12k, if it happens). Net need **≈€20k**. Route: bootstrap + pre-orders. No outside money needed.

### Top risks

| Risk | Mitigation |
|---|---|
| **Technical:** switching noise from isolated converters on audio rails | LC + low-noise LDO post-regulation; publish measurements; optional "quiet mode" with lower current |
| **Technical:** unregulated B-series module output varies with load | Regulate after it (LDO) — it's the 3.3 V and UART side only |
| **Safety/claims:** someone uses it on live mains believing it's a safety isolator | Board, card and listing say "not for live mains work"; no "safety isolation" wording; consider an explicit warning label |
| **Market:** clones within months | Speed and community; open the design (if the licences you reuse allow) and win on documentation and support |
| **Licence:** the OSHWHub isolated-USB reference has its own licence | Read it before copying anything; if it's share-alike, your derivative must be too |
| **Supply:** Hi-Link DC-DC modules single source | Pin-compatible SIP isolated converters exist from several Chinese and EU makers — keep the footprint standard |

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) | https://www.gongbans.com/db/hilink-ia-s-1wr3-series.html | Isolated **regulated** dual (±) outputs, 1–2 W, 1,500 VDC isolation, SIP 27×8.5×11 mm, short-circuit protected | Datasheet public, files via maker (no open schematic) | Buy as module |
| Hi-Link B_S series (B0505S-1WR3 etc.) | https://www.gongbans.com/db/hilink-b-s-1wr3-series.html | Isolated **unregulated** single output 0.5–3 W, 1,500 VDC, SIP — for 3.3 V rail and the UART side | Datasheet public, files via maker (no open schematic) | Buy as module |
| HopeRF CMT812X dual-channel digital isolator | https://www.gongbans.com/db/hoperf-cmt812x.html | Isolated UART TX/RX; 5 kVrms, 150 Mbps, CMTI 200 kV/µs, SOIC-8 | pcb, schematic (datasheet marked preliminary) | MIT — github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Isolator/SCH_PCB/CMT812X |
| OSHWHub isolated USB converter (ADuM3160-based) | https://www.gongbans.com/db/oshwhub-project-xuyxglld.html | Reference for isolation layout, overcurrent protection and silkscreen ideas | pcb, schematic | Community project — check its licence on OSHWHub before reuse |

### Block diagram

```
USB-C (5 V, CC resistors) ─► input filter + eFuse
   │                │                 │                     │
   ▼                ▼                 ▼                     ▼
IA0512S-2W      IA0505S-1W        B0505S-1W            USB-UART bridge (host side)
±12 V iso        ±5 V iso          5 V iso → LDO 3.3 V        │ TX/RX
   │ LC+LDO         │ LC+LDO          │                  CMT8121 isolator
   ▼                ▼                 ▼                        │
rail jumpers + per-rail fuse + LED ─► breadboard pins      B0505S-1W powers iso side ─► UART header (3.3/5 V)
════════════════ isolation barrier (slot in PCB, silkscreened) ═══════════════
```

**Engineering gap:** layout of the isolation barrier (creepage across the slot; the modules set the limit at 1,500 VDC), noise performance, inrush when all converters start on a weak USB port (soft-start/sequence), and good documentation.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| IA0512S-2WR3 | €2.5–3.5 | Check output ripple spec; pin-compatible alternatives exist |
| IA0505S-1WR3 | €2–2.5 | |
| B0505S-1WR3 ×2 | €0.7–0.9 each | Unregulated — post-regulate |
| CMT8121 | €0.5–0.8 | Preliminary datasheet → confirm production status |
| USB-UART bridge (CH340/CP2102-class) | €0.3–1.0 | Driver support on all OSes |
| Low-noise LDOs ±, LC filters | €1.2 | The audio-quality lever |
| eFuses/polyfuses, LEDs | €1.0 | |
| USB-C receptacle, headers, jumpers | €0.9 | |

### Firmware/software starting point

- No firmware on the module (keep it that way for v1 — fewer CRA obligations). The USB-UART bridge uses the vendor's standard driver.
- Documentation is the software: a website page with the isolation explainer, rail specs, noise plots, KiCad files (if you open-source it), and example circuits (op-amp, audio preamp, RS-485 transceiver on the isolated UART).
- KiCad for the design; search for existing KiCad footprints of the SIP modules.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — sample on perfboard; show to 3 distributors/maker shops; forum post asking for beta testers | One distributor says yes to 500 at the price that works (≥€24 to you); ≥50 beta sign-ups |
| 3–5 | **Works-like** — rev 0 PCB, measure rails (ripple, load regulation, cross-regulation), hipot test at 1,500 VDC | Ripple <5 mV p-p on ±12 V after filtering (target — set your own); passes 1,500 VDC for 1 min |
| 6–8 | **Looks-like + EVT** — rev A with silkscreen, acrylic base, packaging, card; 50 beta units | Beta testers report no ground-loop issues; no failures in 2 weeks |
| 9–10 | **DVT + pre-compliance** — rev B, EMC pre-scan (conducted/radiated emissions are the risk with 4 switchers), thermal test | Passes pre-scan with margin; max case temperature OK at full load |
| 11–12 | **Pilot batch** — 200 units: marketplace launch + distributor sample batch | <1% returns; distributor confirms the 500 order |

### Certification checklist (EU)

- **CE — EMC Directive 2014/30/EU:** EN 55032 (emissions) and EN 55035 (immunity). Four switching converters → emissions are the real risk. Est. €3–5k.
- **LVD:** not in scope (all voltages <75 V DC). Product safety is covered by the **General Product Safety Regulation (EU) 2023/988** — do a risk assessment; EN 62368-1 as a voluntary reference (est. €1–2k for a review).
- **RED:** not applicable (no radio).
- **EN 18031:** not applicable (no radio).
- **CRA:** the USB-UART bridge gives a data connection to a computer, so the module may count as a product with digital elements — likely the default (non-critical) category. Confirm; if in scope, SBOM and vulnerability contact by Dec 2027 (small effort for fixed-function chips).
- **RoHS, REACH, WEEE** (it's EEE), packaging registration.
- No batteries, no GDPR, no toy directive (state "not a toy, 14+" if sold to students), no MDR.
- **Estimated test costs:** €5–8k.

### Validation toolkit

- **Kill question:** Will electronics retailers/maker shops list it next to their breadboard PSUs — one distributor order of 500 is the pass line (at a price that leaves you ≥€24 per unit). **Cheapest experiment:** perfboard sample + a one-page datasheet with measured rails, sent to 5 distributors' product managers; ask for a listing decision.
- **Interview script (5) — makers/lab instructors:**
  1. What do you power analog/audio circuits from today?
  2. Have you ever had a ground-loop problem (hum, dead port)? What did you do?
  3. Which rails do you actually need, at what current?
  4. Would you trust a module's noise spec — what would you need to see?
  5. €49 for this — buy, wait, or build your own? What would make it a must-have?
- **Landing page:** Headline: "Isolated ±12 V, ±5 V and 3.3 V on your breadboard — from one USB-C." Bullets: "Break ground loops before they break your laptop." / "Per-rail current limit and LED; isolated UART built in." / "Measured noise, published. Honest about what isolation can't do."
- **Pre-order pass:** 1 distributor PO for 500, **or** ≥300 marketplace pre-orders in 30 days.

### First production checklist

- **Samples:** 10 PCBAs; golden sample with rail measurements (ripple, regulation, isolation) printed on a test report.
- **DFM review:** isolation slot routing, creepage on the panel and around mouse bites, SIP module coplanarity for wave/selective soldering (THT modules on an SMT board — decide hand-solder vs selective solder).
- **MOQ talk:** Hi-Link modules (ask for 1k pricing and lead time), isolator via distributor, PCB panelisation.
- **QC/AQL:** ISO 2859-1 level II, AQL 0.65/2.5; 100% rail test with electronic load (voltage at 50% load per rail, overcurrent trip check), sample hipot test (1,500 VDC, 1 min) per lot.
- **Packaging:** small box, ESD bag, isolation card (multilingual), jumper set.
- **Incoterms:** FOB Shenzhen or DAP via express for 1k (small volume, small boxes).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and HopeRF (华普微)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) 1-2 W fixed-input isolated regulated dual-output DC-DC converter](/db/hilink-ia-s-1wr3-series.html) (isolated regulated dual-output DC-DC (±rails)); [Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP](/db/hilink-b-s-1wr3-series.html) (isolated single-output DC-DC for 5/3.3 V). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT812X dual-channel digital isolator](/db/hoperf-cmt812x.html) (dual-channel digital isolator for the UART (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [【开源】【彩色丝印】隔离USB转换器](/db/oshwhub-project-xuyxglld.html) (open isolated USB converter design for reference).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) websites)

```email
Subject: Sample order and volume pricing — Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) 1-2 W fixed-input isolated regulated dual-output DC-DC converter, Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT812X dual-channel digital isolator — for a Isolated Bench Power Module

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Isolated Bench Power Module: A breadboard-friendly module that gives analog and audio projects isolated ±12 V, ±5 V and 3.3 V from USB-C, plus an isolated USB-UART — the safe way to probe mains-adjacent or ground-loop-prone circuits. The design is built around your Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) 1-2 W fixed-input isolated regulated dual-output DC-DC converter, Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT812X dual-channel digital isolator.

Could you please send:
1. Price and lead time for [10] sample units of each: Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) 1-2 W fixed-input isolated regulated dual-output DC-DC converter, Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT812X dual-channel digital isolator.
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
主题：样品订购及批量报价 — Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) 1-2 W fixed-input isolated regulated dual-output DC-DC converter, Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT812X dual-channel digital isolator — 用于Isolated Bench Power Module

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Isolated Bench Power Module：A breadboard-friendly module that gives analog and audio projects isolated ±12 V, ±5 V and 3.3 V from USB-C, plus an isolated USB-UART — the safe way to probe mains-adjacent or ground-loop-prone circuits。产品设计基于贵司的Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) 1-2 W fixed-input isolated regulated dual-output DC-DC converter, Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT812X dual-channel digital isolator。

请提供以下信息：
1. 各[10]片样品的单价和交期：Hi-Link IA_S-1WR3/2WR3 series (IA0505S-1WR3 etc.) 1-2 W fixed-input isolated regulated dual-output DC-DC converter, Hi-Link B_S series (B0505S-1WR3 etc.) 0.5-3 W fixed-input isolated DC-DC converter, SIP, HopeRF CMT812X dual-channel digital isolator。
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
Subject: PCBA quote from open design files — Isolated Bench Power Module, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Isolated Bench Power Module: A breadboard-friendly module that gives analog and audio projects isolated ±12 V, ±5 V and 3.3 V from USB-C, plus an isolated USB-UART — the safe way to probe mains-adjacent or ground-loop-prone circuits. The design starts from published open-hardware files (【开源】【彩色丝印】隔离USB转换器; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Isolated Bench Power Module，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Isolated Bench Power Module：A breadboard-friendly module that gives analog and audio projects isolated ±12 V, ±5 V and 3.3 V from USB-C, plus an isolated USB-UART — the safe way to probe mains-adjacent or ground-loop-prone circuits。设计基于已公开的开源硬件文件（【开源】【彩色丝印】隔离USB转换器；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order IA0512S, IA0505S, B0505S modules and CMT8121 samples; build a perfboard version and measure ripple on each rail with a scope.
2. Read the OSHWHub isolated-USB project's licence and the HopeRF CMT812X reference schematic/PCB (MIT) — decide what you reuse.
3. Email 5 distributor product managers a one-page datasheet draft and ask one question: "Would you list this at €49 retail, and what quantity would you start with?"

Want help sourcing or building this? Talk to us via www.gongbans.com.
