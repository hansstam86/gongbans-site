# Isolated Field-Tech Interface Kit — Founder Start Pack

> A rugged pocket set of galvanically isolated USB-to-RS485/RS232/TTL adapters and a 4-port RS485 fan-out, so service technicians can talk to heat pumps, inverters and PLCs without frying a laptop.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Every heat pump, inverter, battery and BMS controller now has a Modbus/RS485 service port. Technicians plug in €5 unisolated dongles, get ground loops, kill USB ports and occasionally a laptop, and still don't know which wire is A and which is B.
- **Customer:** HVAC, solar/storage and building-automation service technicians; industrial maintenance teams; distributors of installer tools. The firm pays €119 per kit; the tech uses it daily.
- **Product:** metal-cased isolated 3-in-1 (RS485/RS232/TTL) adapter with labelled screw terminals, a 4-port isolated RS485 fan-out for bench and commissioning, a cable set for the common service connectors, and a free Modbus scanner that finds baud rate and slave ID in one click.
- **Why now:** ~28 M heat pumps and tens of millions of inverters installed in Europe need servicing; all four source boards are fully open; no radio, no battery — a pilot can be on sale in weeks.
- **The ask:** ~€30k to the first 1,000 kits; bootstrap with trade-association pre-orders.

<!-- market-check:start -->
> **External market check (November 2026): WEAK.** Isolated USB-to-RS485/RS232/TTL adapters are a mature commodity category at $16–180; Waveshare's $16–24 multibus converter covers the exact use case. No evidence that technicians discuss "frying a laptop" as a live pain point. **Main risk:** This is a packaging and bundling play on commodity hardware, not a product gap. *As researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast. Competitors and sources found: see [the market check in the competition table](#external-market-check).*
<!-- market-check:end -->

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 20 installers from one regional trade association pre-order at €119 after a 2-minute demo?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: a signed letter of intent, a paid pilot, or a dated purchase order for the first units. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** HVAC, solar and building-automation service technicians; industrial maintenance teams; distributors of installer tools.

**The problem as the pack states it:** Every heat pump, inverter, battery and BMS controller now has a Modbus/RS485 service port. Technicians plug in €5 unisolated dongles, get ground loops, kill USB ports and occasionally a laptop, and still don't know which wire is A and which is B.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/PLC** · https://www.reddit.com/r/PLC/ — industrial automation engineers and integrators.
- **PLCtalk forum** · https://www.plctalk.net/ — industrial automation technicians and integrators.
- **r/embedded** · https://www.reddit.com/r/embedded/ — embedded engineers.
- **EEVblog forum** · https://www.eevblog.com/forum/ — electronics engineers and serious hobbyists; test-equipment and soldering opinions.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten budget-holders and ten users), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€99–149, the pack's estimate), and one button. For a business buyer the button is "request a pilot" that leads to a short form and a letter of intent.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how HVAC, solar and building-automation service technicians deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last time a serial link to a machine damaged a laptop or a port, or behaved strangely on site.
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A rugged pocket set of galvanically isolated USB-to-RS485/RS232/TTL adapters and a 4-port RS485 fan-out, so service technicians can talk to heat pumps, inverters and PLCs without frying a laptop. On a scale of one to ten, how likely would you be to buy that at €99–149, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Isolated Field-Tech Interface Kit: looking for 3 pilot sites before we build it

I am [your name], [your background]. We are considering building a Isolated Field-Tech Interface Kit: A rugged pocket set of galvanically isolated USB-to-RS485/RS232/TTL adapters and a 4-port RS485 fan-out, so service technicians can talk to heat pumps, inverters and PLCs without frying a laptop. Before we spend money on tooling I want to find out whether this solves a real problem for HVAC, solar and building-automation service technicians.

If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay €99–149 per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.

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
The pro-grade isolated adapters exist (Moxa UPort 1150I ~€192 ex-VAT; StarTech isolated ~US$150–180) but they are IT products: DB9 connectors, no screw terminals, no cable for the inverter's RJ45 service port, no help finding the Modbus parameters. The cheap end (Waveshare isolated ~€14–30; no-name unisolated €5) works on the bench and fails in the field: no protection against 48 V on the bus, no over-current on the USB side, and drivers that fight with Windows. Between the two sits the technician, who wants one labelled box in the van that just works with the three devices he sees most.

Who pays: the service company (tool budget per van is €2–5k a year); the solar installer's commissioning team; the building-automation integrator. Who uses: the technician, often on a ladder, in the rain, with gloves. Distributors of installer tools are the channel — they already sell clamp meters and pipe cutters.

### Market size (estimates — check them)
- **TAM:** ~48,000 SHK firms in Germany, ~20,000 solar/storage installers in DE, similar again in FR/NL/UK/IT/ES; plus building-automation integrators and industrial maintenance → ~250,000 firms in Europe, average 2 kits → **~€60 M** at €119.
- **SAM:** firms that do heat-pump/inverter service with Modbus tools today — ~20% → **~€12 M**, replacement every 4 years.
- **SOM (3 years):** 12,000 kits ≈ **€1.2 M revenue**. Boring, profitable, and a foot in the door for other installer tools.

### Competition (2 searches)
| Alternative | Price (est.) | Weakness |
|---|---|---|
| €5 unisolated USB-RS485 dongle ("do nothing") | €5 | Ground loops, dead USB ports, bad drivers |
| Waveshare isolated USB-RS485 (various) | €14–30 | Bench part: no screw-terminal labels, no cable set, mixed quality |
| Moxa UPort 1150I | ~€192 ex-VAT | IT product, DB9, no field cables, no scanner |
| StarTech/Sealevel isolated | US$115–180 | Same |
| Manufacturer service dongles (per brand) | €100–300 | One brand only, locked software |

**Wedge:** field-first packaging (metal, labelled A/B/GND, screw terminals, cable set for the common service ports), a 4-port fan-out for commissioning several devices at once, and a free scanner app that finds the device. Price between the cheap and the IT-grade.

<!-- market-competitors:start -->
#### External market check

Competitors, demand signals and price comparables found by web search in November 2026. Sources are named as found and not linked; as researched November 2026 by web search; verify before relying on it. Verdicts are a reading of the evidence found, not a forecast.

| Who / source | What it is | What it tells us |
|---|---|---|
| Waveshare Multibus Converter | About $16–24 | Commodity incumbent covering the same buses |
| DFRobot isolated USB-RS485 | About $17 | Commodity incumbent |
| StarTech ICUSB422IS | About €180 | Premium end of the same category |

**Verdict as researched: WEAK.** Main risk: This is a packaging and bundling play on commodity hardware, not a product gap.
<!-- market-competitors:end -->

### Product & value proposition
- **Adapter:** isolated USB-C to RS485/RS232/TTL (switch-selected), 2.5 kV isolation, bus TVS + PTC, USB-side over-current (from the open isolated-USB design), A/B/GND screw terminals and a DB9, activity LEDs, aluminium case, 120 Ω termination switch.
- **Fan-out:** USB to 4× isolated RS485 (CH344Q design), DC output terminal for powering a device under test, metal case.
- **Cables:** RJ45-to-bare, RJ12, 2-pin and 3-pin pluggable terminal leads, 2 m each; a laminated pinout card for the common heat-pump and inverter service ports.
- **Software:** Modbus scanner (baud/parity/ID sweep, register dump, CSV), Windows/macOS/Linux, offline, free.
- **Pricing:** **Kit €119 incl. VAT** (€100 ex-VAT): adapter + cables + case; **Pro kit €179** adds the 4-port fan-out; adapter alone €69; trade distributor price €72/€110 ex-VAT.

### Unit economics (estimates, per standard kit)
| Item | 1,000 kits | 5,000 kits |
|---|---|---|
| Electronics BOM (USB bridge, digital isolator, isolated DC-DC, transceivers, TVS, PCB) | €11 | €8.50 |
| Assembly & test (loopback at 3 interfaces, isolation hipot sample) | €3 | €2 |
| Aluminium case + end plates + switch caps | €4.50 | €3 |
| Cable set (4 leads) + pinout card | €4 | €2.80 |
| Packaging (semi-hard case) | €3 | €2 |
| Freight + duty to EU | €1.50 | €0.80 |
| Certification amortised (€5k EMC) | €5 | €1 |
| **Landed cost** | **€32** | **€20.10** |
| Sell price ex-VAT direct | €100 | €100 |
| Via tool distributor (net €72) | €72 | €72 |
| **Gross margin direct** | **68%** | **80%** |
| **Gross margin via distributor** | 56% | 72% |

### Go-to-market
**First 100 customers:** one regional heating trade association meeting with a 2-minute demo ("plug in, click scan, it finds the heat pump"); the solar-installer forums and groups; the building-automation integrator forums; a YouTube short per common inverter brand showing the service-port pinout and the scan; a loaner kit to 10 technicians with a request for the cables they're missing.

**Scale:** installer-tool distributors and wholesaler catalogues (the clamp-meter aisle), heat-pump and inverter manufacturers' training academies (they want installers to stop frying their controllers), Amazon Business, industrial MRO catalogues.

### 12-month plan
- **Q1:** Build 20 kits from the open boards in off-the-shelf aluminium cases, scanner app v1, 20 pre-orders at €119 from one association. Gate: 20 installers pre-order after a 2-minute demo.
- **Q2:** Own merged PCB (3-in-1 + protection), case tooling (extrusion is cheap), EMC test, 300 kits, cable set finalised from technician feedback.
- **Q3:** 1,000 kits, first two distributors, Pro kit with fan-out.
- **Q4:** Manufacturer academy partnerships, FR/NL localisation of the pinout card, 3,000 kits.

**Team:** one electronics engineer part-time (the designs exist; merge and harden), one software developer part-time (scanner app), founder on sales and sourcing. No full-timers until 3,000 kits.

**Funding to 1,000 kits (estimate):** NRE €10k (merged PCB, case extrusion die €2k, app) + certification €5k + 1,000 × €27 production = €27k → **~€42k**; 100 pre-orders cover €10k → cash need **~€30k**. Bootstrap; this one should never need outside money.

### Top risks
- **Technical — drivers:** CH34x drivers are built into recent Windows/macOS/Linux kernels; the CH344 (4-port) may need a driver on some systems. Mitigation: ship a signed driver bundle and a "no driver" FTDI/CP210x variant if support tickets pile up.
- **Technical — isolation claims:** if you print "2.5 kV isolated" you need to test it. Mitigation: hipot test on a sample per batch; use a digital isolator and isolated DC-DC with datasheets that back the number.
- **Market — "I have a €5 dongle":** Mitigation: the laptop-death story sells itself; demo the scanner, not the isolation.
- **Regulatory:** EMC (EN 55032/55035) + no LVD (≤5 V USB; the bus is SELV). **CRA** for the scanner software and the adapter firmware — keep an SBOM. No radio, no battery, no personal data.
- **Supply:** the digital isolator in the open isolated-USB design (ADuM-class) is a single-vendor part with occasional allocation; Mitigation: qualify a second-source isolator footprint on the merged PCB.
- **Licence:** all four boards are OSHWHub — check each licence; if NC, re-draw the schematic yourself (these are datasheet reference circuits).

## 4. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [oshwhub-ge-li-xing-usb-zhuan-485-232-ttl-san-ge-yi](https://www.gongbans.com/db/oshwhub-ge-li-xing-usb-zhuan-485-232-ttl-san-ge-yi.html) | Isolated USB to RS485/RS232/TTL three-in-one: the core adapter | schematic, pcb | OSHWHub — check licence |
| [oshwhub-ch344q-usb-ji-xian-qi](https://www.gongbans.com/db/oshwhub-ch344q-usb-ji-xian-qi.html) | USB to 4× RS485 (CH344Q) with DC terminal output: the fan-out | schematic, pcb | OSHWHub — check licence |
| [oshwhub-project-xuyxglld](https://www.gongbans.com/db/oshwhub-project-xuyxglld.html) | Isolated USB converter (ADuM3160) with over-current protection: the USB-side protection block | schematic, pcb | OSHWHub — check licence |
| [oshwhub-lckfb-ch340x-usb-to-ttl-type-c](https://www.gongbans.com/db/oshwhub-lckfb-ch340x-usb-to-ttl-type-c.html) | Protected USB-C to TTL (ESD/TVS/fuse, 3.3 V LDO, 5 V-tolerant IO): the TTL leg | schematic, pcb | OSHWHub — check licence |

### Block diagram and engineering gap
```
USB-C --> [USB isolator + over-current (ADuM3160 design)] --> [USB-UART bridge (CH340X-class)]
      --> [isolated DC-DC] --> [RS485 transceiver | RS232 transceiver | 3.3/5 V TTL] --> switch --> screw terminals + DB9
      TVS + PTC on every bus pin; 120 ohm termination switch; LEDs TX/RX/PWR
Fan-out: USB-C --> [CH344Q 4x UART] --> 4x isolated RS485 --> 4x terminals; DC out terminal
```
Gap: merge the three designs into one PCB with one isolation barrier, decide the switch scheme (mechanical vs. firmware), harden against 48 V on the bus, design the case/labels, and write the scanner app. Low risk.

### Starter BOM (per adapter, estimates)
| Part | Est. cost | Note |
|---|---|---|
| USB-UART bridge (CH340X per open design; or FTDI/CP210x variant) | €0.80–2.50 | Driverless variant costs more |
| USB digital isolator (ADuM3160 per open design) | €3.50 | Single vendor — qualify a second footprint |
| Isolated DC-DC 5 V/5 V 1 W | €1.50 | Two sources |
| RS485 + RS232 transceivers, TVS, PTC | €1.80 | — |
| PCB + assembly | €3.00 | — |
| Aluminium extrusion case + CNC end plates | €4.50 | Extrusion die €1–2k |
| Screw terminals, DB9, switches, LEDs | €1.50 | — |
| Cable set + pinout card | €4.00 | — |
| CH344Q + 4× isolated RS485 (fan-out) | €12 BOM | Pro kit only |

### Firmware/software starting point
- No device firmware beyond the bridge chips. Scanner app: build on **pymodbus** (exists) or the C **libmodbus** (exists); for CLI testing **mbpoll** (exists); for a GUI reference look at **QModMaster** (exists). Ship a single-binary app for Windows/macOS/Linux.
- Keep a public register-map library for common heat pumps/inverters only where the manufacturer documents are public — don't reverse-engineer and publish protected maps.

### 12-week build plan
- **Week 1–2 — validate.** Order the four open boards from the fab (10 each), put the 3-in-1 in an off-the-shelf alu case with labels; scanner v0 (pymodbus script). Demo to 20 installers at one association meeting. *Exit:* 20 pre-orders at €119.
- **Week 3–5 — works-like.** Merged PCB v1 with protection, switch scheme, LEDs; scanner app v1 with GUI; 10 kits to 10 technicians. *Exit:* 10 techs talk to a real heat pump and an inverter without help.
- **Week 6–8 — looks-like + EVT.** Case extrusion, end plates, cable set, pinout card, semi-hard case. *Exit:* techs rate the cable set "complete" for their top 3 devices.
- **Week 9–10 — DVT + pre-compliance.** EMC pre-scan (isolated DC-DC is the noise source), hipot test, surge on the bus pins. *Exit:* pass; 2.5 kV hipot on 5 samples.
- **Week 11–12 — pilot batch.** 100 kits, golden sample, first distributor meeting. *Exit:* 100 paid, <3% support tickets, one distributor quote.

### Certification checklist (EU)
- **EMC:** EN 55032/EN 55035 (class B); self-declaration. **LVD:** not applicable (USB-powered, SELV). Est. **€3–5k**.
- **RoHS, WEEE, REACH** (cable PVC, case anodising).
- **No radio** → no RED/EN 18031. **CRA:** adapter has no updatable firmware (good), but the scanner app is software you place on the market — SBOM, vulnerability contact, update mechanism; low effort.
- **No battery, no GDPR, no toy, no medical.**
- Isolation claim: have the lab (or your own tester) do a dielectric test to back the datasheet number you print.

### Validation toolkit
- **Kill question:** do 20 installers from one regional association pre-order at €119 after a 2-minute demo? **Cheapest experiment:** €300 — 3 open boards in cases, one laptop, one meeting.
- **5-question interview:** (1) What do you plug into a heat pump or inverter service port today? (2) Ever lost a USB port or laptop to it? (3) Which three devices do you connect to most, and which connectors? (4) What takes longest: wiring, drivers, or finding baud/ID? (5) €119 for the kit from the wholesaler — would you order two for the vans?
- **Landing-page headline:** "Talk to any heat pump or inverter. Keep your laptop." Bullets: Isolated RS485/RS232/TTL in one metal box, screw terminals labelled A/B/GND · Cable set for the common service ports · Free scanner finds baud, parity and ID in one click.
- **Pre-order pass:** 20 pre-orders at one meeting, or 60 online in 4 weeks.

### First production checklist
Chip samples from authorised distributors (the USB bridge market is full of clones), golden sample with hipot and loopback report, DFM on the extrusion (slot tolerance for the PCB), MOQ 500 with a 2,000 forecast, QC/AQL Level II + 100% loopback on 3 interfaces + hipot sample per lot, cable pull test, FOB Shenzhen air for 500, EU importer + WEEE number on the case label.

## 5. Who to contact

<!-- who-to-contact:start -->
**No verified company contact on file yet for this idea.** Every board it is built from is a community design on OSHWHub, where the author is an individual, not a supplier. Nothing has been invented to fill the gap: once section 2 (validate demand) has passed, use the manufacturing houses and the directory entries below, follow the [zero-experience founder playbook](/playbook.html), and treat the first quote you get as the real data. Company websites only; no personal contacts are published.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [隔离型USB转485,232,TTL三合一](/db/oshwhub-ge-li-xing-usb-zhuan-485-232-ttl-san-ge-yi.html) (isolated USB to RS485/RS232/TTL three-in-one); [USB转4路485-CH344Q](/db/oshwhub-ch344q-usb-ji-xian-qi.html) (USB to 4× RS485 for testing several devices at once); [【开源】【彩色丝印】隔离USB转换器](/db/oshwhub-project-xuyxglld.html) (isolated USB converter with over-current protection); [LCKFB-CH340X-USB-TO-TTL-TYPE-C](/db/oshwhub-lckfb-ch340x-usb-to-ttl-type-c.html) (protected USB-C to TTL tool).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Xinhua Control (XHC)** (深圳市欣华宸科技有限公司) · xhciot.com — Industrial edge gateway / RTU OEM: Industrial edge gateway; RTU; RS485/Modbus; 4G/LoRa. *(Industrial RS485 / Modbus gateways)*
- **Kongtai Technology** (深圳市控泰科技有限公司) · kongtai.net — SCADA / PLC / edge computing OEM: PLC; HMI; SCADA; edge gateway. *(Industrial RS485 / Modbus gateways)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**B. To a PCBA / EMS house — quote from the open design files** (send to Kingbrother, Foxlink or any assembler you vet; see the [playbook](/playbook.html#manufacturer))

```email
Subject: PCBA quote from open design files — Isolated Field-Tech Interface Kit, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Isolated Field-Tech Interface Kit: A rugged pocket set of galvanically isolated USB-to-RS485/RS232/TTL adapters and a 4-port RS485 fan-out, so service technicians can talk to heat pumps, inverters and PLCs without frying a laptop. The design starts from published open-hardware files (隔离型USB转485,232,TTL三合一, USB转4路485-CH344Q, 【开源】【彩色丝印】隔离USB转换器, LCKFB-CH340X-USB-TO-TTL-TYPE-C; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Isolated Field-Tech Interface Kit，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Isolated Field-Tech Interface Kit：A rugged pocket set of galvanically isolated USB-to-RS485/RS232/TTL adapters and a 4-port RS485 fan-out, so service technicians can talk to heat pumps, inverters and PLCs without frying a laptop。设计基于已公开的开源硬件文件（隔离型USB转485,232,TTL三合一, USB转4路485-CH344Q, 【开源】【彩色丝印】隔离USB转换器, LCKFB-CH340X-USB-TO-TTL-TYPE-C；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 10 each of the four open boards from the fab and five aluminium project cases; write the pymodbus scan script tonight.
2. Call the regional heating or solar trade association and get 10 minutes at the next meeting.
3. Check all four OSHWHub licences; list which chips in each are single-source.

Want help sourcing or building this? Talk to us via www.gongbans.com.
