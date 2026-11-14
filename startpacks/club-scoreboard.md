# Club Scoreboard — Founder Start Pack

> A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports — at a fifth of the price of sports-hall boards.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Hall scoreboards from Favero, Stramatel or Mobatime list at €1,050–3,200+ ex VAT before the console, radio option and installation; most small clubs and school gyms still flip cardboard numbers or use a €149 tabletop toy nobody can read from the stands.
- **Customer:** Amateur sports clubs (volunteers with a small grant), school gyms, municipal sports halls, youth tournaments across Europe. The treasurer pays; the volunteer at the table uses it.
- **Product:** A 64×32 P3/P4 RGB LED-matrix panel (about 38×19 cm at P6 for halls — choose pitch per range) in an aluminium frame with wall/tripod mount, an external PSU, and a handheld ESP-NOW remote with sport templates (score, period, fouls, shot clock), horn, and a phone spectator view. €349–499 (estimate).
- **Why now:** Open P3 matrix driver boards and HUB75 ESP32 libraries make the hard part a download; clubs spend grant money in small chunks; the existing boards have not changed in a decade.
- **The ask:** ~€70k to a certified first 1,000; pre-orders from one or two regional federations can carry a big share.

<!-- market-check:start -->
> **External market check (November 2026): LIKELY.** Full-size varsity boards run about $5,000–5,700 (Anthem Sports, School Health / Sportable); mid-tier portable wireless units about $2,089 (First Team FT810W); Daktronics is quote-only. Demand evidence: a Silicon Chip article calls pro boards generally out of reach for amateur and school teams, an Electro-Tech-Online thread shows a club rejecting pre-built units as too costly and asking how to DIY one, and a Make Magazine piece covers a parent building one for the same reason. **Main risk:** All demand evidence is anecdotal; nobody has quantified what clubs will pay. Also: at €399 the board is roughly a fifth of the mid-tier and a twelfth of the full-size price, so the pitch's "a fifth of the price" should name which tier it compares to. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 10 clubs from one regional federation pre-order at €399 after a demo at a tournament weekend?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Amateur sports clubs, school gyms, municipal sports halls across Europe.

**The problem as the pack states it:** Hall scoreboards from Favero, Stramatel or Mobatime list at €1,050–3,200+ ex VAT before the console, radio option and installation; most small clubs and school gyms still flip cardboard numbers or use a €149 tabletop toy nobody can read from the stands.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **DOSB (DE)** · https://www.dosb.de/ — German sports confederation; the regional Landessportbund reaches the clubs.
- **r/trackandfield** · https://www.reddit.com/r/trackandfield/ — athletes and coaches.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€349–499, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how amateur sports clubs, school gyms, municipal sports halls across Europe deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Walk me through how the score is shown at your home games today, and what happened the last time it went wrong.
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports, at a fifth of the price of sports-hall boards. On a scale of one to ten, how likely would you be to buy that at €349–499, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Club Scoreboard: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Club Scoreboard: A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports, at a fifth of the price of sports-hall boards. Before we spend money on tooling I want to find out whether this solves a real problem for amateur sports clubs, school gyms, municipal sports halls across Europe.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €349–499 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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

A hall scoreboard is a capital item few small clubs can justify. Favero's FC50 lists at €1,050 ex VAT for a 15 cm-digit board plus console; the FS-130 at €3,180 ex VAT; Mobatime and Stramatel do not even publish prices. Municipal halls have one board, fixed, often broken, controlled from a wired console in a locked cupboard. Meanwhile the tournament on pitch 3 of the youth cup runs on paper.

- **Who pays:** the club treasurer or youth coordinator (grant money, sponsor money, fundraising); school/municipal sports departments (small direct procurement); tournament organisers (rental).
- **Who uses:** a parent volunteer at the table, in a loud hall, with no training. Three buttons must do 90% of the job.
- **Who watches:** players and spectators 10–40 m away — brightness and digit height are the spec, not pixel art.

### Market size (estimates — check)

- **TAM (EU amateur sports clubs):** Germany alone has ~86k sports clubs (DOSB); the EU has well over 700k. Say 300k play indoor/field team sports with scores. At 1.5 boards each at €399 → **€180M**, replacement every 8–10 years.
- **SAM (clubs and schools in DACH, Benelux, Nordics, FR that buy online and have a grant line):** ~80k venues → **€30–40M**.
- **SOM (3 yrs):** 2–3% of SAM → **2,000–3,000 boards**. Year 1: 500–1,000.

### Competition (2 searches)

| Alternative | Price | Why we still win |
|---|---|---|
| Favero FC50 / FS-130, Stramatel 452 series, Mobatime 8T220 | €1,050–3,180+ ex VAT board, console and radio extra | A fifth of the price, remote included, portable |
| €10–150 tabletop LED scoreboards (Fruugo/Amazon import) | Cheap | Unreadable from 15 m, flimsy, no sport logic, no horn |
| Manual flip boards (VICTOR Zähltafel ~€55) | Cheap | Not visible, no clock, no horn |
| Phone/tablet apps + TV in the hall | Free-ish | Someone must bring a TV and cables; sunlight washes it out outdoors |
| DIY: HUB75 panel + ESP32 + open library | €80 of parts | No remote, no housing, no PSU safety, no CE — clubs will not build it |

**Wedge:** a complete, CE-marked, portable kit at the price of a tabletop toy times three, with sport templates and a remote that any parent can use.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Full-size varsity boards (Anthem Sports, School Health / Sportable) | About $5,000–5,700 | €399 is roughly a twelfth of this |
| First Team FT810W portable wireless | About $2,089 | €399 is roughly a fifth of this; the pitch's comparison tier |
| Daktronics | Quote-only | No public price found |
| Silicon Chip article on DIY scoreboards | Pro boards "generally out of reach for amateur and school teams" | Demand signal, anecdotal |
| Electro-Tech-Online forum thread | Club rejected pre-built units as too costly, asked how to DIY | Demand signal, anecdotal |
| Make Magazine piece | Parent built one after finding commercial units too expensive | Demand signal, anecdotal |

**Verdict as researched: LIKELY.** Main risk: All demand evidence is anecdotal; nobody has quantified what clubs will pay. Also: at €399 the board is roughly a fifth of the mid-tier and a twelfth of the full-size price, so the pitch's "a fifth of the price" should name which tier it compares to.
<!-- market-competitors:end -->

### Product & value proposition

- Panel: one 64×32 RGB module (P6 ≈ 384×192 mm for halls up to ~40 m; P4/P3 for smaller rooms), 1,500–4,000 nit outdoor-type panels for field use as a premium SKU. Aluminium frame, polycarbonate front, IP54 optional.
- Controller: ESP32-S3 in the panel; handheld remote with 8 buttons and a small screen, ESP-NOW link 50 m (no WiFi needed in the hall), USB-C rechargeable (or 3×AA to avoid battery regulation hassle — pick AA).
- Templates: football, handball, volleyball (sets), basketball (shot clock via add-on 4-digit display), floorball, hockey, school generic. Horn via a 100 dB buzzer or an external speaker jack.
- Spectator view: panel broadcasts a tiny web page over its own WiFi AP or ESP-NOW to a second phone.
- **Pricing (estimates):** €399 hall kit (panel + remote + PSU + wall mount), €499 outdoor-bright kit, €149 shot-clock add-on, €59 tripod. Tournament rental partners at 35% off.

### Unit economics (estimates, EUR per unit; hall kit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (64×32 P6 panel €22, ESP32-S3 driver board (open matrixled-derived) €6, remote: ESP32-C3 + buttons + OLED €9, buzzer €2, 5 V 8 A PSU (certified, EU plug) €9, cables €2) | 50.0 | 42.0 |
| PCBA (driver + remote) + test | 5.0 | 3.4 |
| Enclosure (aluminium profile frame, PC front, back plate, remote ABS case) | 22.0 | 16.0 |
| Packaging (panel-sized box, foam) | 6.0 | 4.5 |
| Freight + duty to EU (sea; bulky) | 10.0 | 6.0 |
| Certification amortised (€18k) | 18.0 | 3.6 |
| **Landed cost** | **111** | **75.5** |
| Net price direct (€399 incl. 19% VAT → €335) less €18 shipping | 317 | 317 |
| **Gross margin direct** | **€206 (65%)** | **€242 (76%)** |
| Via sports retailer (40% margin: €201 net) | €90 (45%) | €126 (63%) |

The LED panel is a commodity (dozens of Shenzhen makers); the certified PSU is where you must not save money.

### Go-to-market

**First 100 customers:** demo at one regional youth tournament weekend per sport (handball and volleyball first — indoor, loud, point-heavy), a stand with two boards running, pre-order at €399 with €50 deposit. Regional federations' newsletters (e.g. a Landesverband) and coach Facebook groups. Three clubs you know get boards at cost in exchange for videos.

**Then scale:** federations (bulk deals for member clubs), school sports suppliers and catalogues (Sport-Thieme-type catalogues — search), municipal sports departments, tournament rental companies, Amazon.de/.nl, and a Kickstarter-style pre-order in the second year for the outdoor SKU.

### 12-month plan

- **Q1:** works-like on the open matrix driver + AtomS3-Lite remote; demo at two tournaments; deposits.
- **Q2:** own driver PCB (rev A from the open EasyEDA project), remote PCB, frame design; 30-unit EVT; sport templates finished with coaches.
- **Q3:** certification (EMC on PWM LEDs is the hard one), 500–1,000 production, ship pre-orders before the autumn indoor season.
- **Q4:** shot-clock add-on, outdoor SKU, federation deals, rental partners.

**Team:** embedded engineer (full), mechanical/industrial designer (half), founder who has coached and knows the federations, a part-time UX person for the remote. Shenzhen partner for panels, frame extrusion, PSU sourcing.

**Funding to first 1,000 (estimate):** landed hardware excl. cert €93k + tooling (remote case, frame corners) €10k + certification €18k + demo units/events €6k + 6 months team €45k + marketing €6k = **≈€178k** gross; with 400 pre-orders × €399 (€160k, ~€134k ex VAT) you need **≈€50–70k** external. Route: pre-orders at tournaments + bootstrap; sports-innovation grants (national sport federations and lottery funds often have equipment-innovation lines — search); angel if a federation signs for 300+.

### Top risks

| Risk | Mitigation |
|---|---|
| **Regulatory/technical:** EMC — a HUB75 panel with fast PWM radiates; the first scan may fail | Shielded frame, ferrites on panel cables, lower PWM clock, pre-scan early (week 9); budget a second scan |
| **Market:** clubs buy once per decade and only when grant money appears | Sell at the moment of grant decisions (autumn), via federations; offer rental |
| **Technical:** readability outdoors; 64×32 is low resolution for text-heavy sports | Start indoor; big digits only; outdoor SKU with high-brightness panels later |
| **Supply:** panel vendors change LED bins and connector pinouts between batches | Lock a vendor and a part number; incoming inspection on every batch |
| **Safety:** mains PSU in a kids' environment | External certified PSU (EN 62368-1 / EN 61558), low-voltage only inside the board; strain relief |

Not a toy: it is sports equipment for adults to operate; avoid marketing it to children to stay clear of the toy directive.

## 4. Start kit

### Boards to start from

| Board | Link | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| OSHWHub MATRIX LED 64*32 P3 driver board | https://www.gongbans.com/db/oshwhub-matrixled.html | Open 64×32 P3 full-colour matrix driver — PCB and schematic in EasyEDA; the base for your driver | schematic, pcb | OSHWHub project licence on the project page — check (community projects vary) |
| M5Stack AtomS3-Lite (C124) | https://www.gongbans.com/db/m5stack-atoms3-lite.html | ESP32-S3 controller for the handheld remote prototype | enclosure/structure only | Module for prototypes; design own remote PCB |
| Seeed Grove-4-Digit Display | https://www.gongbans.com/db/seeed-grove-4-digit-display.html | Simple 4-digit display for the shot-clock add-on | schematic | Seeed wiki — check |
| M5Stack Unit Buzzer (U132) | https://www.gongbans.com/db/m5stack-unit-buzzer.html | Horn/buzzer output reference for the pilot | enclosure/structure only | Module for prototypes |

Catalogue honesty: the OSHWHub row lists no chip; read the schematic to see which MCU drives the HUB75 bus and whether it is ESP32-based before assuming library compatibility.

### Block diagram

```
Mains ──► certified external 5 V 8–10 A PSU ──► panel + driver board
   Driver (ESP32-S3) ──HUB75──► 64×32 RGB LED panel
   ESP32-S3 ──ESP-NOW (2.4 GHz)──► Handheld remote (ESP32-C3, 8 buttons, small OLED, 3×AA)
   ESP32-S3 ──GPIO──► horn driver (buzzer / speaker jack)
   ESP32-S3 ──WiFi AP──► spectator phone web view (optional)
Add-on: 4-digit shot-clock display on a cable (Grove-style) 
```

**Engineering gap:** EMC of the LED bus, a frame that is light but rigid, remote UX (templates, undo), horn loudness in a hall (buzzer vs small amplifier), and pairing without WiFi.

### Starter BOM (estimates)

| Part | Est. @1k | Notes |
|---|---|---|
| 64×32 RGB LED module, P6 (indoor, ~1,000 nit) | €18–25 | Commodity; lock the vendor/part |
| Driver PCB: ESP32-S3-WROOM, level shifters, HUB75 header | €6 | Based on the open project; S3 for PSRAM/DMA headroom |
| Remote: ESP32-C3 module, 8 tact/arcade buttons, 0.96" OLED, AA holder | €9 | |
| Certified 5 V 8–10 A desktop PSU with EU cord | €8–11 | **Do not use an unbranded supply** — safety cert is yours otherwise |
| 100 dB piezo horn or 3 W speaker + Class-D amp | €2–4 | |
| Aluminium profile frame, PC front, steel back | €18–22 | EU extrusion possible for small runs |
| Wall mount + tripod adapter (3/8") | €3 | |
| Box + foam | €5–6 | |

### Firmware/software starting point

- **ESP32-HUB75-MatrixPanel-DMA** (mrfaptastic) — the standard Arduino/ESP-IDF library for HUB75 panels on ESP32/S3; **PxMatrix** older alternative. Fonts via Adafruit GFX.
- **ESP-NOW** (Espressif) for the remote link; **ESP-IDF** or Arduino-ESP32.
- Remote UI: **LVGL** is overkill for an OLED — use u8g2.
- Spectator view: tiny web server in ESP-IDF or ESPAsyncWebServer with a single HTML page.
- Sport rule templates: write them with coaches; nothing to download.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | **Validate** — one board from the open driver + a bought P6 panel + AtomS3-Lite remote in a printed case; show at one tournament; deposits | ≥10 clubs deposit €50 at €399; volunteers operate it without help |
| 3–5 | **Works-like** — 5 units with handball + volleyball + football templates, ESP-NOW range test in a hall | 50 m range through a hall; zero missed button presses in 3 full matches |
| 6–8 | **Looks-like + EVT** — rev A driver + remote PCBs, aluminium frame, 30 units; horn loudness; brightness measurement | ≥90 dB at 1 m; readable from 30 m; frame survives 1 m drop in box |
| 9–10 | **DVT + pre-compliance** — EMC pre-scan (radiated, with PWM at max), ESD on buttons, PSU verification; EN 18031 check (WiFi AP mode counts as internet-capable? ask the lab) | Emissions pass with margin or a fix plan; test plan signed |
| 11–12 | **Pilot batch** — 50 units to depositor clubs before season start; feedback loop on templates | ≤2 failures; ≥8/10 clubs would recommend; federation LOI |

### Certification checklist (EU)

- **CE — RED** (ESP-NOW/WiFi 2.4 GHz): EN 300 328 via module pre-cert; **EN 301 489-1/-17**; **EN 62368-1** for the board (low voltage, external PSU must carry its own certificate — ask for the CB report). The LED PWM EMC is the budget eater: €9–14k incl. one re-test.
- **EN 18031:** if the board exposes a WiFi AP or connects to the internet (firmware updates), assume in scope; keep it offline-first and self-assess: €2–3k.
- **CRA:** SBOM, USB-C local firmware update, disclosure contact.
- **RoHS, WEEE (consumer category — register in each country), REACH, packaging.**
- **Battery Regulation:** AA in the remote → producer registration; if Li-ion, UN 38.3 + removable design.
- **GDPR:** none. **Toy directive:** not applicable if marketed as sports equipment for club use.
- **Total estimate:** €14–20k.

### Validation toolkit

- **Kill question:** Do 10 clubs from one regional federation pre-order at €399 after a demo at a tournament weekend? Cheapest experiment: one hand-built board, one weekend, a deposit QR code.
- **Interview script (5):** 1) What do you use today to show the score, and who operates it? 2) When did you last buy equipment over €300, and where did the money come from? 3) Which sports and age groups play in your hall; what must the board show for each? 4) How far away are the spectators and does sunlight hit the hall? 5) €349, €399 or €499 — where do you stop, and would you rent for tournaments instead?
- **Landing page:** Headline: "A real scoreboard for clubs that run on volunteers." Bullets: "Readable from 30 metres, with horn and shot clock." / "Wireless remote any parent can use — no cables, no app." / "€399 complete. Hall boards cost five times more."
- **Pre-order pass:** ≥10 club deposits of €50 within 4 weeks of the first demo.

### First production checklist

- Samples: 3 panels from two vendors tested side by side (brightness, colour, dead pixels); 3 driver PCBAs; **golden sample** full kit.
- DFM: frame assembly time (<10 min), cable routing, PC front glare, remote button feel.
- MOQ: panels 100+; frame extrusion 500; remote case 1k shots (negotiate 500); PSU from stock.
- QC/AQL: Z1.4 II, AQL 1.0/2.5; 100% test: full-colour sweep, dead-pixel check, remote pairing, horn.
- Packaging: ISTA 1A; panel-face protection; EU DoC + WEEE marks; PSU certificate copy on file.
- Incoterms: FOB Shenzhen sea; pilot batch by air DAP; HS code for LED display assembly vs scoreboard — ask the broker.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack AtomS3-Lite (C124)](/db/m5stack-atoms3-lite.html) (ESP32-S3 controller for the handheld remote); [M5Stack Unit Buzzer (U132)](/db/m5stack-unit-buzzer.html) (horn/buzzer output reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-4-Digit Display](/db/seeed-grove-4-digit-display.html) (simple 4-digit display for the shot-clock add-on). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [MATRIX LED 64*32 P3 全彩显示屏驱动板](/db/oshwhub-matrixled.html) (open 64×32 P3 full-colour LED-matrix driver board).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Topway (Tuo Pu)** (深圳市拓普威科技有限公司) · topwaytech.com — Commercial display / digital signage solution: Commercial LCD display; Android signage player; meeting room controller; OEM. *(Commercial displays / signage)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack AtomS3-Lite (C124), M5Stack Unit Buzzer (U132), Seeed Grove-4-Digit Display — for a Club Scoreboard

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Club Scoreboard: A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports, at a fifth of the price of sports-hall boards. The design is built around your M5Stack AtomS3-Lite (C124), M5Stack Unit Buzzer (U132), Seeed Grove-4-Digit Display.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack AtomS3-Lite (C124), M5Stack Unit Buzzer (U132), Seeed Grove-4-Digit Display.
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
主题：样品订购及批量报价 — M5Stack AtomS3-Lite (C124), M5Stack Unit Buzzer (U132), Seeed Grove-4-Digit Display — 用于Club Scoreboard

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Club Scoreboard：A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports, at a fifth of the price of sports-hall boards。产品设计基于贵司的M5Stack AtomS3-Lite (C124), M5Stack Unit Buzzer (U132), Seeed Grove-4-Digit Display。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack AtomS3-Lite (C124), M5Stack Unit Buzzer (U132), Seeed Grove-4-Digit Display。
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
Subject: PCBA quote from open design files — Club Scoreboard, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Club Scoreboard: A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports, at a fifth of the price of sports-hall boards. The design starts from published open-hardware files (MATRIX LED 64*32 P3 全彩显示屏驱动板; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Club Scoreboard，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Club Scoreboard：A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports, at a fifth of the price of sports-hall boards。设计基于已公开的开源硬件文件（MATRIX LED 64*32 P3 全彩显示屏驱动板；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order the open matrix driver PCB from the OSHWHub project (JLC one-click) or breadboard an ESP32-S3 with a HUB75 cable, buy one P6 64×32 panel and an AtomS3-Lite; get a score counting with two buttons.
2. Find the next regional youth handball or volleyball tournament in 4–6 weeks and ask the organiser for a table; prepare a €50 deposit page.
3. Email two EU labs for an EMC/RED quote on "LED matrix scoreboard with ESP32 and external certified PSU" and ask what reduces LED PWM emissions in their experience.

Want help sourcing or building this? Talk to us via www.gongbans.com.
