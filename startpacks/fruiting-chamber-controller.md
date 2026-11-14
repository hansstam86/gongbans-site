# Fruiting-Chamber Controller — Founder Start Pack

> One box that holds a mushroom fruiting chamber at 85–95% humidity and under 1,000 ppm CO2 by driving a fogger and a fan — plug-and-play, European plugs, no US-only app.
>
> *Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.*

## 1. Summary

- **Problem:** Gourmet mushrooms (oyster, lion's mane, shiitake) fruit well only at 85–95% RH with fresh air. Hobby and micro-farm growers hack together a humidity plug, a timer fan and a US-import controller whose sensor is rated to 85% RH — exactly where mushrooms start.
- **Customer:** Home and urban mushroom growers and micro-farms in DE/NL/FR/UK; grow-shop retailers and grow-kit sellers as channel. The grower pays €139–199; the kit seller bundles it.
- **Product:** 12/24 V DC controller with a sealed NDIR CO2 + T/RH sensor pod on a cable, outputs for an ultrasonic fogger and a fan, fungi-tuned hysteresis, EU PSU, optional WiFi logging.
- **Why now:** The gourmet-mushroom wave is real (grow-kit market estimates US$0.4–1.2 B globally in 2025, Europe ~28%); incumbents are US-centric and not built for saturated humidity; every part exists in the catalogue.
- **The ask:** ~€45k to the first 1,000 units; pre-orders from grower communities fund half.

## 2. Business plan

### Problem & customer
A fruiting chamber (a tub, a tent, a converted fridge, or a 10 m² room in a micro-farm) needs three things controlled: humidity (fogger/humidifier on-off), CO2 (fresh-air exchange fan), and sometimes temperature. The hobby solution is an Inkbird humidity controller (€50–85) that switches a mains humidifier and a timer-driven fan, with no CO2 sensing — so growers either over-ventilate (dry pins) or under-ventilate (long stems, small caps). The US controller brands offer good apps but their T/RH probes are rated to 85% RH, no CO2 at the hobby price, US plugs on grey imports, and no EU support.

Who pays: the grower (B2C, €139–199 — the price of two grow kits); micro-farms (B2B, 2–10 units per farm); grow-kit and spawn shops who want a controller to upsell.

### Market size (estimates — check them)
- **TAM:** Grow-kit market estimates for 2025 range US$0.4–1.2 B globally with Europe ~28% → **€100–300 M/year** of kit spend in Europe; controllers are an accessory to maybe 5% of serious growers. Plus ~2,000–4,000 micro-farms/urban farms in Europe (estimate).
- **SAM:** Growers who build a chamber (not just open a kit on the kitchen counter): say 150,000 households in DE/NL/FR/UK + 2,000 micro-farms; replacement/upgrade cycle 3 years → ~50,000 controller sales/year × €150 ≈ **€7.5 M/year**.
- **SOM (year 2):** 4,000 units ≈ **€560k revenue**.

### Competition (3 searches)
| Alternative | Price (EU, est.) | Weakness |
|---|---|---|
| Inkbird IHC-200 humidity controller + timer fan ("DIY standard") | €50–85 | Humidity only, mains switching in a wet place, no CO2 |
| AC Infinity Controller 69 Pro | €98–139 | No CO2 at that price, probe rated 35–85% RH, US-centric app and support |
| Home Assistant / Arduino DIY with an SCD41 | €40 in parts + weekends | Only for tinkerers |
| Commercial farm controllers | €1,000+ | Overkill for a tent |
| Do nothing — mist by hand twice a day | €0 | Pins dry out, no consistency |

**Wedge:** real NDIR CO2 + a sensor pod built to live at 95% RH, DC-only outputs (safe in a wet tent), EU plugs and support, fungi presets. The 85% RH probe rating of the incumbents is the headline.

### Product & value proposition
- **Controller box:** ESP32-C3, 2 PWM/switched 12/24 V outputs (fogger, fan) + 1 spare (light/heater), 2-line OLED + knob, RJ11 sensor cable.
- **Sensor pod:** SCD41 (NDIR CO2 + T/RH) in a hydrophobic-membrane housing with a tiny heater pulse to shed condensation; replaceable.
- **Logic:** humidity hysteresis (e.g. 88–92%), CO2 ceiling with fan duty, "fresh-air flush" schedule, species presets (oyster, lion's mane, shiitake), manual override.
- **Optional WiFi:** logging to a simple web page/MQTT; works fully offline.
- **Pricing:** controller + pod **€139 incl. VAT** (B2C); bundle with 12 V fogger disc driver + 120 mm fan + EU PSU **€199**; micro-farm pack (3 controllers) €349 ex-VAT; replacement pod €39.

### Unit economics (estimates, controller + pod)
| Item | 1,000 units | 5,000 units |
|---|---|---|
| Electronics BOM (SCD41 €12, ESP32-C3 €2, drivers, OLED, PSU-less) | €27 | €22 |
| Assembly & test (incl. CO2 check in ambient air) | €5 | €3.50 |
| Enclosures (controller box + sealed pod with membrane) | €5 | €3.20 |
| Packaging, cables, EU PSU 24 V 2 A (certified) | €7.50 | €5.50 |
| Freight + duty to EU | €2.50 | €1.30 |
| Certification amortised (€15k) | €15 | €3 |
| **Landed cost** | **€62** | **€38.50** |
| Sell price ex-VAT (from €139 incl. 19% VAT) | €117 | €117 |
| Via grow shop (40% of €139 → net €70 ex-VAT) | — | €70 |
| **Gross margin direct** | **47%** | **67%** |
| **Gross margin via grow shop** | 11% | 45% |

Lesson: at 1k units sell direct only; the grow-shop channel works from 5k. The bundle (€199) carries better margin because fogger/fan/PSU are cheap.

### Go-to-market
**First 100 customers:** the three biggest German and Dutch mushroom-growing Facebook groups and the big English-language mushroom forums/subreddits; two YouTube growers for a review unit; grow-kit sellers' newsletters (give them an affiliate cut); one micro-farm as a pilot with photos of yield before/after.

**Scale:** grow shops (hydroponics retailers already stock the US brands), grow-kit sellers bundling the controller, Amazon.de/.nl/.fr, a "chamber in a box" partner (tent + fogger + controller).

### 12-month plan
- **Q1:** Breadboard with the Grove SCD41 + C3 devkit on a real tub, pre-order post in the groups. Gate: 60 deposits at €139 in two weeks.
- **Q2:** Own PCB, pod with membrane, 3 months of humidity-chamber testing (drift!), RED/EMC tests, first 300 units.
- **Q3:** 1,000 units, bundle SKU, first 10 grow shops, Amazon.
- **Q4:** Micro-farm pack, WiFi logging, second sensor variant (temperature/heater output).

**Team:** one firmware/hardware engineer (full-time for 6 months), one grower-marketer part-time (community, content), founder on ops. The enclosure/pod needs a mechanical freelancer for 4 weeks.

**Funding to 1,000 units (estimate):** NRE €20k (PCB, pod tooling €8k, test chamber) + certification €15k + 1,000 × €47 production = €47k → **~€82k**; 60 deposits + a 300-unit pre-order round covers ~€40k → cash need **~€45k**. Bootstrap/pre-orders; no investor needed.

### Top risks
- **Technical — sensor at saturation:** SCD41 drifts and condensation kills readings. Mitigation: membrane housing, periodic heater pulse, automatic self-calibration disabled and a weekly fresh-air calibration routine, replaceable pod at €39.
- **Market — hobby niche, incumbents could ship an EU version:** they already sell in Europe; mitigation is the 95% RH pod and CO2, and the community relationship.
- **Regulatory:** RED + EN 18031 if WiFi; EMC; EN 62368-1 at low voltage only (the PSU carries its own CE); CRA for the connected version. Mitigation: ship v1 offline-capable; WiFi as a firmware option after EN 18031.
- **Supply:** SCD41 is a sole-source part with 8–16 week lead times at times. Mitigation: order 2,000 early; design the pod footprint to accept the cheaper SCD40 too.

## 3. Start kit

### Boards to start from
| Board | Contributes | Files (catalogue) | Licence note |
|---|---|---|---|
| [seeed-grove-co2-temperature-humidity-sensor-scd41](https://www.gongbans.com/db/seeed-grove-co2-temperature-humidity-sensor-scd41.html) | True NDIR CO2 + T/RH; the sensor pod reference circuit | schematic | Seeed wiki — check licence |
| [seeed-grove-water-atomization](https://www.gongbans.com/db/seeed-grove-water-atomization.html) | Ultrasonic fogger disc driver reference | schematic | Seeed wiki — check licence |
| [m5stack-unit-fan](https://www.gongbans.com/db/m5stack-unit-fan.html) | 12 V fan drive for prototypes | enclosure/structure only | Module |
| [espressif-esp32-c3-devkitm-1](https://www.gongbans.com/db/espressif-esp32-c3-devkitm-1.html) | Controller MCU reference design | schematic | Espressif reference files — permissive, check the download terms |

### Block diagram and engineering gap
```
[Sensor pod: SCD41 + membrane + heater] --I2C/RJ11--> ESP32-C3
ESP32-C3 --> [MOSFET out 1: fogger disc driver 24 V]  
         --> [MOSFET out 2: 120 mm fan, PWM]
         --> [MOSFET out 3: spare (light/heater)]
         --> [OLED + knob]      --WiFi optional--> web page / MQTT
[24 V 2 A EU PSU, certified] --> box; nothing above 24 V inside
```
Gap: the pod (condensation survival), fungi control logic and presets, DC-only power architecture, and a box that survives a wet tent (IP54 for the controller, pod IP67 with a breathable membrane).

### Starter BOM (per unit, estimates)
| Part | Est. cost | Note |
|---|---|---|
| SCD41 CO2/T/RH | €12 | Sole source, long lead — order early; footprint-compatible SCD40 as fallback |
| ESP32-C3 module (certified) | €2.00 | — |
| 3× N-MOSFET outputs + protection | €1.50 | — |
| OLED 0.96" + encoder knob | €2.20 | — |
| PCB + assembly | €4.50 | — |
| Pod housing + PTFE membrane + heater resistor | €3.00 | Membrane is a specialist part; 2 suppliers |
| Controller box, IP54, cable glands | €3.00 | Off-the-shelf box first |
| 24 V 2 A EU PSU (certified) | €4.50 | Buy certified; don't design mains |
| Fogger disc + driver, 120 mm fan (bundle) | €9.00 | Bundle only |

### Firmware/software starting point
- ESPHome (exists; supports SCD4x, PWM outputs, climate/hysteresis components) is a legitimate v1 firmware and gives Home Assistant users a free integration. Move to ESP-IDF when you need custom pod heater logic.
- Mycodo (exists; open-source environmental regulation for Raspberry Pi) is worth reading for grower control logic.
- Web page: a static page served from the ESP32 — no app.

### 12-week build plan
- **Week 1–2 — validate.** Grove SCD41 + C3 devkit + Unit Fan + a fogger on a 60 L tub of oyster mushrooms; post the €139 pre-order in three groups. *Exit:* 60 deposits in two weeks; the breadboard holds 88–92% RH and <1,000 ppm for a week.
- **Week 3–5 — works-like.** Own PCB, 3 outputs, OLED menu, pod v1 with membrane. *Exit:* 5 units running on 5 community testers' chambers.
- **Week 6–8 — looks-like + EVT.** Box and pod housings printed in the final geometry, presets tuned from tester data. *Exit:* 2 weeks without a sensor fault at 95% RH.
- **Week 9–10 — DVT + pre-compliance.** Pod tool, EMC pre-scan, PSU and cable qualification. *Exit:* pre-scan pass; pod drift <5% RH over 30 days.
- **Week 11–12 — pilot batch.** 50 units to depositors, logs collected. *Exit:* <5% support tickets, yield feedback positive.

### Certification checklist (EU)
- **RED** if WiFi enabled: EN 300 328, EN 301 489-1/-17, EN 62368-1 (SELV only). **EMC-only route** (EN 55032/55035) if you ship the no-WiFi SKU first. Est. **€8–15k**.
- **EN 18031** (RED delegated act) if the WiFi version talks to the internet; **CRA** — reporting obligations from Sept 2026, full in Dec 2027: SBOM, update path, vulnerability handling.
- **RoHS, WEEE, REACH**; the PSU must carry its own CE and be from a reputable supplier.
- No battery, no camera, no personal data (unless you add accounts — don't).
- Not a toy, not a medical device. Don't claim food-safety outcomes.

### Validation toolkit
- **Kill question:** 60 paid deposits at €139 within two weeks from three grower communities? **Cheapest experiment:** €250 — breadboard, a photo of it holding 90% RH, a pre-order page.
- **5-question interview:** (1) What's your chamber and how do you control humidity today? (2) What went wrong in your last flush — dry pins, long stems, contamination? (3) Do you know your CO2 level? Would you pay to? (4) €139 for the controller or €199 with fogger and fan — which? (5) Where did you buy your last grow gear?
- **Landing-page headline:** "The first fruiting-chamber controller built for 95% humidity." Bullets: Real NDIR CO2 + a sensor pod that doesn't drown · 24 V only — nothing mains in your wet tent · EU plug, EU support, works offline.
- **Pre-order pass:** 60 deposits of €30 (or 30 full pre-payments) in 14 days.

### First production checklist
Sensor samples from the distributor (not grey market — fakes exist), golden sample with logged 7-day RH/CO2 trace, DFM on the pod (membrane welding, strain relief), MOQ 500 with a 2,000 forecast, QC/AQL Level II + 100% functional test in ambient CO2, drop/humidity packaging test, FOB Shenzhen, EU importer on the label, PSU batch certificates filed.

## 4. Next steps (this week)
1. Order the Grove SCD41, C3 devkit, Unit Fan, a 24 V fogger disc and a 60 L tub; start an oyster block.
2. Draft the pre-order post and page (€139, ships in 16 weeks) and get admin permission in three grower groups.
3. Email the SCD41 distributor for 2,000-piece lead time and price; ask a lab for a RED-vs-EMC quote.

Want help sourcing or building this? Talk to us via www.gongbans.com.
