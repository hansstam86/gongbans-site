# Touchless Switch Module — Founder Start Pack

> A 25 × 25 mm wave-to-activate gesture/proximity module, built from a fully open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Small European manufacturers of soap dispensers, bathroom furniture, lamps and kitchen fittings want "touch-free" on the box, but have no optical-sensor engineer, and the €1 Alibaba IR switches false-trigger, fail EMC and come with no documentation.
- **Customer:** EU OEMs and their contract manufacturers (they pay, they design in); the end user waves a hand.
- **Product:** A documented module with a defined connector, relay or MOSFET output, false-trigger filtering, an EMC pre-test report and a design-in guide. No radio.
- **Why now:** Hygiene expectations stuck after 2020; the catalogue holds a complete gesture reference (schematic, PCB, Gerber, BOM) so the sensor front-end is a copy job, not a research project.
- **The ask:** ~€45k (estimate) to 1,000 modules, five sampled OEMs and one 1,000-piece order. Bootstrap plus OEM NRE fees; no outside money needed if the first OEM pays for samples.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 5 European OEMs request samples and does one place a 1,000-piece order within 3 months?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** European makers of soap and sanitiser dispensers, bathroom furniture, lamps and kitchen fittings; contract manufacturers.

**The problem as the pack states it:** Small European manufacturers of soap dispensers, bathroom furniture, lamps and kitchen fittings want "touch-free" on the box, but have no optical-sensor engineer, and the €1 Alibaba IR switches false-trigger, fail EMC and come with no documentation.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **Hackaday / hackaday.io** · https://hackaday.io/ — maker audience; visibility more than buyers.
- **r/esp32** · https://www.reddit.com/r/esp32/ — ESP32 builders; good for early technical feedback, less for buyers.
- **EEVblog forum** · https://www.eevblog.com/forum/ — electronics engineers and serious hobbyists; test-equipment and soldering opinions.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€9–15 per module (1k volume), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how European makers of soap and sanitiser dispensers, bathroom furniture, lamps and kitchen fittings deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last product where you added a touchless or gesture control: who supplied the module, what did it cost, and what was wrong with it?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A wave-to-activate gesture module, based on a full open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves. On a scale of one to ten, how likely would you be to buy that at €9–15 per module (1k volume), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Touchless Switch Module: would you pay €9–15 per module (1k volume) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Touchless Switch Module: A wave-to-activate gesture module, based on a full open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €9–15 per module (1k volume), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Buyer: the product manager or lead engineer at a **European OEM with 10–200 employees** making dispensers (soap, sanitiser, paper), bathroom mirrors and cabinets, kitchen lighting (under-cabinet), waste bins, drinking-water taps and small appliances. Their contract manufacturers (often in Poland, Portugal, Italy, Turkey) are the second buyer. They need a part number they can put on a BOM, a datasheet in English, and someone who answers when the sensor false-triggers under a fluorescent tube.

The user is whoever waves a hand. They never know your name. This is a **component business**: low glamour, repeatable, margin comes from volume and from NRE fees for variants.

### Market size (estimates)
- Factory-direct IR hand-wave switches list at **US$2.6–4.8** on sourcing platforms, and retail in Europe at **£9–12 / $12–58** depending on brand ([Global Sources listing](https://www.globalsources.com/product/light-sensor-switch_1194614365f.htm), [UK retail example](https://www.simplelighting.co.uk/products/white-hand-wave-sensor-switch-12-24vdc-5cm-range), [US retail example](https://marvellighting.com/product-detail-page/hand-wave-motion-sensor-switch-by-alloy-led)). That tells you the price band and that the market is real.
- **TAM (estimate):** EU + UK consumption of touchless sensor switches for dispensers, furniture lighting and small appliances — assume 15 M units/yr at ~€3 average → **~€45 M/yr**.
- **SAM (estimate):** OEMs that want a documented, EU-supported module rather than a bulk Alibaba part — maybe 15% of volume → ~2 M units → **~€7 M/yr**.
- **SOM (3-year, estimate):** 5% of SAM → 100k units/yr at €9 → **~€0.9 M/yr**. Small, but a 40%-margin component line with repeat orders is a fine first business and a door-opener for bigger design-in work.

### Competition
| Alternative | Notes | Weakness we attack |
|---|---|---|
| Bulk IR switch modules from Chinese catalogue suppliers (US$0.3–5, MOQ 200+) | The default for cost-driven OEMs | No EMC report, no false-trigger spec, part changes without notice, zero support |
| Branded furniture-lighting sensor switches (German/Italian furniture-hardware brands, €5–25 trade) | Sold as finished switch, not as design-in module | Fixed form factor and connector, premium price, not for dispensers |
| Integrated proximity sensor ICs (VCNL-class, APDS-class) | What a competent OEM would use | Needs optical design, firmware, EMC work — exactly what small OEMs lack |
| Capacitive touch | Cheap, reliable | Not touchless; doesn't work through thick fronts or with gloves |
| mmWave / ToF modules | Overkill, €4–10 | Price, power, over-sensitivity |
| Do nothing (mechanical switch or pedal) | Free | "Touch-free" sells; pedals break |

**Wedge:** *documentation and support as the product*. Datasheet with real trigger distance vs. surface reflectance, an EMC pre-test report the OEM can hand to its test lab, a design-in guide (window material, aperture, mounting), and a variant programme (relay, MOSFET, logic output; 5 V/12 V/24 V) for a small NRE fee.

### Product & value proposition
- **Module A (proximity):** VCNL4020-class IR proximity sensor + small MCU, 5–24 V input, open-drain or 3 A MOSFET output, trigger distance adjustable 2–20 cm, latching/momentary/timed modes via solder jumper or a one-wire config. 25 × 25 mm, 2.0 mm pitch connector.
- **Module B (gesture):** same footprint, adds left/right swipe (for dimming lamps, cycling modes) using the open gesture reference as the starting point.
- **Module C (relay):** mains-rated relay daughterboard, for lamps and dispensers with AC loads (safety work doubles here — do it only if an OEM pays NRE).

Pricing (estimates, B2B only): **€9–15/module at 1k**, €6–8 at 10k; sample kit (5 modules + eval board + design guide) €149; variant NRE €3–8k. No B2C.

### Unit economics (estimates, Module A, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| Electronics BOM (proximity sensor, MCU, MOSFET, LDO, passives, connector, PCB) | €3.60 | €2.90 |
| Assembly & test (SMT, flash, optical functional test) | €0.90 | €0.55 |
| Enclosure (none — bare module; optional IR-pass window sold separately) | €0.00 | €0.00 |
| Packaging (tray + ESD bag, 50/tray) | €0.12 | €0.08 |
| Freight + duty to EU | €0.30 | €0.15 |
| Certification amortised (EMC pre-test + RoHS/REACH docs ~€6k) | €6.00 | €1.20 |
| **Landed cost** | **€10.92** | **€4.88** |
| Sell price | €12.00 | €9.00 |
| Channel margin (direct) | €0 | €0 (10% if via distributor) |
| **Gross margin** | **€1.08 (9%)** | **€4.12 (46%)** |

The first 1,000 units pay for the EMC report; that is normal for a component. Charge the sample kits and NRE so the first thousand aren't your money.

### Go-to-market
**First 100 customers (really: first 20 design-ins, 5 of them serious):**
1. Make a list of 100 EU OEMs: dispenser makers (DE, IT, NL, DK), bathroom-furniture and mirror makers (DE, PL, IT), kitchen-lighting brands, drinking-water tap and bin makers. Trade fairs: ISH Frankfurt (bathroom), interzum Cologne (furniture components), Light + Building, Interclean Amsterdam (hygiene). Walk the halls with a working demo on a soap dispenser.
2. Contract manufacturers and EMS in Poland/Portugal/Hungary serving these OEMs — they recommend parts.
3. A listing on a European electronics distributor's marketplace once you have a datasheet and a part number.

**Scale channels:** distributors (catalogue + long-tail), furniture-hardware wholesalers, a "touchless inside" co-branding sticker for OEMs who want the marketing.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Copy the open gesture pack into a 25 × 25 mm module; 50 hand-built samples; EMC pre-scan; datasheet v0.9. Kill question: 5 OEM sample requests, 1 PO within 3 months. |
| Q2 | Production v1 (1k), full EMC report, relay/MOSFET variants, design-in guide, eval board. Walk interzum/ISH. |
| Q3 | First OEM in production; second 2k batch; distributor listing. |
| Q4 | 5k batch; gesture variant B; first NRE-funded custom. |

**Team:** 1 hardware/firmware engineer (full-time), 1 founder for OEM sales and documentation (full-time), test-lab and layout bought in. Two people. Keep it that way for a year.

**Funding to first 1,000 units (estimates):** PCB spins and samples €6k, EMC pre-test + RoHS/REACH documentation €6k, eval boards and sample kits €4k, first 1k modules €4.5k landed, two trade fairs €8k, 9 months lean overhead €25k ≈ **€53k**; minus sample-kit and NRE income (~€10k) ≈ **€45k**. Bootstrap. If an OEM pays €5k NRE for a variant in month 3, you are funded.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** false triggers from sunlight, fluorescent flicker, shiny surfaces, steam | Modulated IR, ambient-light cancellation in the sensor, firmware hysteresis, configurable distance; publish the limits honestly in the datasheet |
| **Technical:** OEM front panels block IR | Design-in guide with window material list; sell a tested IR-pass window |
| **Market:** OEMs copy the module and go direct to a Chinese supplier after a year | Expected. Keep adding variants and support; margin is in the first two years of each design-in; move upmarket (gesture, relay, UL/CE packs) |
| **Regulatory:** the OEM's end product fails EMC with your module installed | Your pre-test report plus a hand-holding clause: you attend their EMC test for a day fee |
| **Supply:** the sensor IC is single-source | Qualify a second sensor family on the same footprint from day one; keep 6 months of ICs in stock |
| **Licence:** the open reference pack's licence | Read it. If restrictive, use it as a *reference* and redraw the schematic with your own layout — that is what you'd do anyway |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Gesture Recognition (VCNL4020 + LPC824) | https://www.gongbans.com/db/gesture-vcnl4020-lpc824.html | Full open design pack of exactly this function (hand-cream dispenser reference) | bom, gerber, pcb, schematic | Curated ATU kit, hosted files; verify redistribution terms before selling a derivative |
| Proximity Sensor (VCNL4020) | https://www.gongbans.com/db/proximity-sensor-vcnl4020.html | Simpler proximity-only variant, 1–200 mm | none listed | Documentation only; use for application reference |
| M5Stack Unit Gesture (U127) | https://www.gongbans.com/db/m5stack-unit-gesture.html | Richer gesture sensing for the premium variant; quick prototype | enclosure/structure only | Buy the unit; don't copy electronics |
| Seeed Grove IR Distance Interrupter v1.2 | https://www.gongbans.com/db/seeed-grove-ir-distance-interrupter-v1-2.html | Lowest-cost IR interrupter alternative for a €0.50 BOM version | schematic | Seeed wiki resources; check licence per file |

### Block diagram
```
 5-24 V in --> [LDO 3.3 V] --> [small MCU (LPC8xx/CH32V/STM32G0-class)]
                                    |  I2C
                             [IR proximity/gesture sensor] (IR LED + photodiode)
                                    |
                     [output stage: open-drain | 3 A MOSFET | relay board]
                     [config: solder jumpers / 1-wire]  [status LED]
```
**Engineering gap:** the open pack gives you the sensor front-end and MCU. Missing: a 5–24 V tolerant input and output stage, EMC hardening (ESD on the connector, ferrites, layout), production firmware with configurable modes and robust false-trigger filtering, the IR window spec, and the documentation set. Two to three engineer-months.

### Starter BOM (estimates per module at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| IR proximity sensor with ambient-light cancellation (VCNL4020-class) | €1.20 | **Sole-source per part number**; qualify a second family |
| Small ARM/RISC-V MCU (LPC824-class or CH32V003/STM32G0) | €0.60 | Choose on availability; the open pack uses LPC824 |
| 3 A N-MOSFET + gate drive | €0.25 | |
| LDO 3.3 V, 24 V-tolerant | €0.20 | |
| ESD/TVS, ferrite, passives | €0.35 | EMC insurance, don't skip |
| Connector 2.0 mm 4-pin | €0.15 | Pick a connector OEMs already stock |
| PCB 2-layer 25 × 25 mm | €0.35 | |
| Optional IR-pass window (sold separately) | €0.40 | Polycarbonate, 850 nm pass |

### Firmware/software starting point
- The gesture pack's firmware targets LPC824; NXP's MCUXpresso SDK exists for LPC8xx. If you switch MCU, the proximity-sensor logic is a few hundred lines — rewrite it.
- Vendor drivers for VCNL-class sensors exist as Arduino libraries (search "VCNL4020 Arduino library").
- No cloud, no app, no radio. The deliverable is a datasheet, not a repo.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Breadboard from Unit Gesture + a MOSFET on a bought soap dispenser and an under-cabinet lamp; video; sample requests from **5 OEMs** via fair/LinkedIn/distributor contacts. Kill question clock starts: 1 PO of 1,000 within 3 months |
| 3–5 | Works-like | 25 × 25 mm PCB v1 from the open pack; false-trigger test bench (sunlight lamp, fluorescent, steam, white/black/mirror targets) passes your published spec; 50 samples shipped |
| 6–8 | Looks-like + EVT | v2 with connector, output options, ESD; EMC pre-scan (EN 55032 radiated/conducted, EN 55035 ESD/EFT/surge) clean; datasheet v1.0; design-in guide |
| 9–10 | DVT + pre-compliance | 200 units from the EMS; RoHS/REACH declarations collected; full EMC report from an accredited lab; 1,000-hour burn-in on 20 units |
| 11–12 | Pilot batch | 1,000 modules produced; first OEM pilot (50 dispensers) in the field for 4 weeks with <1% false-trigger complaints |

### Certification checklist (EU)
- **CE via EMC Directive**: EN 55032 / EN 55035 (or EN IEC 61000-6-1/-3). No RED (no radio). The module alone is a component; the OEM certifies the end product — but your EMC report is your sales tool. Est. €3–5k pre-test + €4–6k full report.
- **LVD** only applies to the relay variant if the module itself carries >50 V AC — keep mains on a separate, separately-certified relay board or buy a certified relay module.
- **RoHS** (collect supplier declarations), **REACH** SVHC check, **WEEE**: as a component supplier you usually aren't the producer-of-record; confirm per country.
- **EN 18031 / RED cybersecurity:** not applicable (no radio, no internet). **CRA:** applies to "products with digital elements" — a module with firmware counts. Reporting obligations from 11 Sept 2026, full application 11 Dec 2027. Keep a vulnerability contact and an SBOM; low burden for a device with no connectivity, but document it.
- **Battery regulation:** none. **GDPR:** none. **Toy directive:** none unless an OEM puts it in a toy — state that it is not evaluated for toys.
- Photobiological safety of the IR LED (EN 62471): usually exempt-class at these powers; get a one-page assessment (~€800).
- **Total certification budget estimate: €8–12k.**

### Validation toolkit
- **Kill question:** Do 5 European OEMs request samples and does one place a 1,000-piece order within 3 months?
- **Cheapest experiment (~€400):** retrofit two bought products (soap dispenser, under-cabinet lamp) with Unit Gesture + MOSFET; a one-page datasheet PDF; 30 targeted messages to OEM engineers. Count sample requests.
- **5-question interview (OEM product/engineering lead):** 1) Do you sell or plan a touch-free product, and what sensor is in it today? 2) What went wrong with it (false triggers, supplier changes, EMC)? 3) What voltage, output and connector would make it a drop-in for you? 4) What documentation does your EMC lab or your buyer ask for? 5) At €9–12 at 1k pieces, who signs the PO and what's the annual volume?
- **Landing page:** headline "Touch-free, designed in by Friday." Bullets: "25 × 25 mm module, 5–24 V, relay or MOSFET output." / "EMC pre-test report and design-in guide included." / "Built on an open reference design — no black box, no surprise part changes."
- **Pass threshold:** 5 sample kits sold at €149 **and** one written PO/LOI for 1,000 pieces within 12 weeks.

### First production checklist
- Samples: 5 golden samples with measured trigger-distance curves attached.
- DFM with the EMS: panelisation of 25 × 25 mm boards, test-point access, programming/test jig quote.
- MOQ talk: sensor IC reels (typically 2.5k–5k per reel) — buy a reel; EMS MOQ 500–1,000.
- QC: AQL II 1.0 major for a component; 100% functional optical test on the jig; log serials.
- Packaging: ESD trays of 50, moisture-barrier bag, humidity indicator; label with part number, rev, date code.
- Incoterms: EXW/FOB from the EMS; if the EMS is in the EU (plenty in PL/HU can do this cheaply), no duty question at all — consider that seriously for a no-radio board.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (WPI ATU (distributor kits) and M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **WPI ATU (distributor kits)** (WPI Group, wpigroup.com) — distributor; 16 boards in the catalogue; files via WPI ATU solution pages (WPG hot channel / tech-highlights / press releases) · https://wpig.wpgholdings.com/tech-highlights/zhcn. Directory entry: Smartphone reference design (MediaTek): MediaTek smartphone + tablet gongban; 1000+ reference designs; billions of devices. The kit files are hosted here; WPI's application unit published them for its distribution customers. Boards used here: [Gesture Recognition (VCNL4020 + LPC824)](/db/gesture-vcnl4020-lpc824.html) (full open design pack: gesture recognition (hand-cream dispenser example)); [Proximity Sensor](/db/proximity-sensor-vcnl4020.html) (proximity-only simpler variant). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Gesture (U127)](/db/m5stack-unit-gesture.html) (richer gesture-sensor reference for the premium variant). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-IR Distance Interrupter v1.2](/db/seeed-grove-ir-distance-interrupter-v1-2.html) (low-cost IR interrupter alternative). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the WPI ATU (distributor kits) and M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2 — for a Touchless Switch Module

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Touchless Switch Module: A wave-to-activate gesture module, based on a full open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves. The design is built around your Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2.

Could you please send:
1. Price and lead time for [10] sample units of each: Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2.
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
主题：样品订购及批量报价 — Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2 — 用于Touchless Switch Module

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Touchless Switch Module：A wave-to-activate gesture module, based on a full open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves。产品设计基于贵司的Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2。

请提供以下信息：
1. 各[10]片样品的单价和交期：Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2。
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
Subject: PCBA quote from open design files — Touchless Switch Module, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Touchless Switch Module: A wave-to-activate gesture module, based on a full open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves. The design starts from published open-hardware files (Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Touchless Switch Module，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Touchless Switch Module：A wave-to-activate gesture module, based on a full open design pack, that dispenser, lamp and furniture makers drop into their products to add touch-free operation without engineering it themselves。设计基于已公开的开源硬件文件（Gesture Recognition (VCNL4020 + LPC824), Proximity Sensor, M5Stack Unit Gesture (U127), Seeed Grove-IR Distance Interrupter v1.2；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Download the gesture pack (schematic, PCB, Gerber, BOM), read its licence, and order 10 bare boards and parts from the BOM.
2. Buy a soap dispenser and an under-cabinet lamp; retrofit both with Unit Gesture + MOSFET and film a 30-second demo.
3. Build the 100-OEM list (dispensers, bathroom furniture, kitchen lighting, bins, taps) with the engineering contact for each, and book interzum or ISH tickets.

Want help sourcing or building this? Talk to us via www.gongbans.com.
