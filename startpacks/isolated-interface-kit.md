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

## 2. Business plan

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

## 3. Start kit

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

## 4. Next steps (this week)
1. Order 10 each of the four open boards from the fab and five aluminium project cases; write the pymodbus scan script tonight.
2. Call the regional heating or solar trade association and get 10 minutes at the next meeting.
3. Check all four OSHWHub licences; list which chips in each are single-source.

Want help sourcing or building this? Talk to us via www.gongbans.com.
