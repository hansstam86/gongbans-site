# Club Scoreboard — Founder Start Pack

> A bright 64×32 LED-matrix scoreboard with a wireless handheld controller for amateur football, handball, volleyball and school sports — at a fifth of the price of sports-hall boards.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Hall scoreboards from Favero, Stramatel or Mobatime list at €1,050–3,200+ ex VAT before the console, radio option and installation; most small clubs and school gyms still flip cardboard numbers or use a €149 tabletop toy nobody can read from the stands.
- **Customer:** Amateur sports clubs (volunteers with a small grant), school gyms, municipal sports halls, youth tournaments across Europe. The treasurer pays; the volunteer at the table uses it.
- **Product:** A 64×32 P3/P4 RGB LED-matrix panel (about 38×19 cm at P6 for halls — choose pitch per range) in an aluminium frame with wall/tripod mount, an external PSU, and a handheld ESP-NOW remote with sport templates (score, period, fouls, shot clock), horn, and a phone spectator view. €349–499 (estimate).
- **Why now:** Open P3 matrix driver boards and HUB75 ESP32 libraries make the hard part a download; clubs spend grant money in small chunks; the existing boards have not changed in a decade.
- **The ask:** ~€70k to a certified first 1,000; pre-orders from one or two regional federations can carry a big share.

## 2. Business plan

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

## 3. Start kit

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

## 4. Next steps (this week)

1. Order the open matrix driver PCB from the OSHWHub project (JLC one-click) or breadboard an ESP32-S3 with a HUB75 cable, buy one P6 64×32 panel and an AtomS3-Lite; get a score counting with two buttons.
2. Find the next regional youth handball or volleyball tournament in 4–6 weeks and ask the organiser for a table; prepare a €50 deposit page.
3. Email two EU labs for an EMC/RED quote on "LED matrix scoreboard with ESP32 and external certified PSU" and ask what reduces LED PWM emissions in their experience.

Want help sourcing or building this? Talk to us via www.gongbans.com.
