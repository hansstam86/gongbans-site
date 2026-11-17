# Farmyard Help Button (LoRa, no SIM) — Founder Start Pack

> A rugged help pendant with 1–2 km line-of-sight range for older people working alone in large gardens, orchards, farmyards and allotments, where DECT and Wi-Fi alarm pendants don't reach.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Older people in rural areas keep working outdoors: the orchard, the vegetable plot, the sheep in the back field, the woodpile. Home social-alarm pendants work within ~50–100 m of the base. Mobile-phone SOS needs a charged phone in a pocket and coverage. When something happens 400 m from the house, nobody hears.
- **Customer:** The family (often adult children) and the older person themselves on small farms, smallholdings, rural homes with big plots, and allotment associations. B2B: care organisations in rural regions and farm-safety programmes.
- **Product:** A set: an IP67 pendant (button + optional "fell and stayed still" alert) and an indoor base with a loud sounder and a relay output to an existing home alarm or phone dialler. The pendant talks to the base directly over sub-GHz LoRa: no SIM, no network, no subscription. Messages are acknowledged; the pendant vibrates when help is notified.
- **Why now:** LoRa SoC modules with the MCU built in (HopeRF HM-6601W) make a tiny long-range pendant feasible. Rural ageing populations and farm-safety campaigns keep pushing lone working as a risk. Subscription fatigue makes "buy once, no SIM" attractive.
- **The ask:** About €120k (estimate) to reach 1,000 sets. Route: pre-orders through farm and rural shows, a rural-development/innovation grant, then a farm-safety or rural-care partner.

**Positioning: a safety alert, not a medical device and not a replacement for professional social-alarm services.**

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does a pendant reach the house through a barn wall and 600 m of orchard in 95% of 200 test presses? Measure in 5 real farms first.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Rural older adults and their families, small farms, allotment associations, care organisations in rural regions.

**The problem as the pack states it:** Older people in rural areas keep working outdoors: the orchard, the vegetable plot, the sheep in the back field, the woodpile. Home social-alarm pendants work within ~50–100 m of the base. Mobile-phone SOS needs a charged phone in a pocket and coverage. When something happens 400 m from the house, nobody hears.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/AgingParents** · https://www.reddit.com/r/AgingParents/ — adult children caring for parents: the buyer for most elderly-care devices.
- **Carers UK forum** · https://www.carersuk.org/forum/ — family carers in the UK.
- **The Farming Forum (UK)** · https://thefarmingforum.co.uk/ — UK farmers; machinery, arable, livestock, farm diversification.
- **Landtreff (DE)** · https://www.landtreff.de/ — German farmers' forum.
- **Farm Safety Foundation / Yellow Wellies (UK)** · https://yellowwellies.org/ — UK farm-safety charity; lone working on farms is one of its topics.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€99–129 set (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how rural older adults and their families, small farms, allotment associations, care organisations in rural regions deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. When your parent is working alone out in the garden, orchard or yard, how would anyone know if something happened, and what have you tried that did not reach that far?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A rugged help pendant with 1–2 km line-of-sight range for older people working alone in large gardens, orchards, farmyards and allotments — where DECT and Wi-Fi alarm pendants don't reach. On a scale of one to ten, how likely would you be to buy that at €99–129 set (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Farmyard Help Button (LoRa, no SIM): would you pay €99–129 set (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Farmyard Help Button (LoRa, no SIM): A rugged help pendant with 1–2 km line-of-sight range for older people working alone in large gardens, orchards, farmyards and allotments — where DECT and Wi-Fi alarm pendants don't reach. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €99–129 set (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Start with **small farms and smallholdings run by people aged 65+** in IE, UK, FR, NL, DE and AT. Farming has one of the oldest workforces in Europe, many of them work alone, and many farm injuries happen to older workers.

Second: **rural homes with large gardens/orchards** (the "my dad is 82 and still cuts the hedges" buyer).

Third: **allotment associations** (the association buys 2–3 sets for the site and members carry them).

The buyer is usually the adult child or the spouse. The user must find the pendant comfortable and not stigmatising, so make it look like a tool, not a care product.

### Market size (estimates)
- EU farm holders aged 65+: roughly 3 M (Eurostat farm structure data shows a large share of holders over 65; check the latest figure). Add rural 70+ homeowners with large plots: estimate another 3–5 M.
- **TAM:** ~7 M × €119 ≈ **€830 M**.
- **SAM:** IE, UK, FR, NL, DE, AT, Nordics, reachable through farm shows/merchants and with families who'd pay, ~15% → **€125 M**.
- **SOM (3 years):** 1% of SAM → ~10,000 sets → **~€1.2 M**. Realistically plan for 3–5k sets.

### Competition
| Alternative | Price (listings, estimate) | Weakness we attack |
|---|---|---|
| Home social-alarm pendants (DECT/proprietary, with monitoring centre) | €0–40/month | Range ends at the garden fence; monitoring centre calls the house phone |
| LoRaWAN panic buttons (e.g. MOKO LW004-PB ~$59–65, Tektelic SafeAlert ~$80; see [Robotshop](https://robotshop.com/products/lorawan-sensors-gateway-lorawan-emergency-button)) | €55–75 + gateway + network server | Need a LoRaWAN gateway, network server and integration, so B2B lone-worker products, not a family kit |
| Cheap 433 MHz SOS/caregiver pagers | €15–25 | ~150 m range claims, no acknowledgement, toy-grade |
| Smartwatch / phone SOS | €250–450 or €0 (own phone) | Needs a charged device on the body and mobile coverage; the phone is in the kitchen |
| PMR446 walkie-talkies | €30–60 a pair | Needs someone listening all day and a free hand to talk |
| Do nothing | Free | Lie in the field until someone comes looking |

**Wedge:** a pre-paired set that works out of the box at 1 km+, gives the wearer acknowledgement feedback ("help notified" vibration), has a year-plus battery and no SIM or subscription, and integrates with what's already in the house (a relay into the existing alarm/dialler).

### Product & value proposition
- **Pendant:** HopeRF HM-6601W LoRa SoC (Cortex-M4 + radio on one module, up to +22 dBm, sleep 1.3 µA per HopeRF), one big button with a recessed second button for "cancel", a vibration motor, LED, accelerometer for the optional "tilt-and-still" alert, IP67, lanyard + belt clip.
- **Battery:** the LoRa transmit current (~108 mA at +22 dBm per the datasheet) is too much for a plain CR2032. Use a 1/2 AA Li-SOCl2 or a CR2477 plus a supercap/buffer, target ≥1 year with a daily check-in. Lower TX power when the base is close.
- **Base:** LoRa receiver (SX1262 class; M5Stack Cap LoRa-1262 for the works-like), a loud sounder (>85 dB), a flashing light, a dry-contact relay output to an existing home alarm, social-alarm base input or auto-dialler, and a mains adapter with a backup battery.
- **Protocol:** point-to-point, acknowledged, with retries and frequency/timing diversity; daily pendant heartbeat ("pendant battery OK / pendant not seen for 24 h").
- **Optional (v2):** base with LTE-M to send SMS directly, as a paid add-on.

**Pricing (estimates):** €119 set RRP (pendant + base), €49 extra pendant, €29 range-extender/repeater for the barn. B2B (care organisations, allotment associations): €95/set at 20+.

### Unit economics (estimates per set, ex-VAT)
| Item | 1k sets | 5k sets |
|---|---|---|
| Pendant BOM (HM-6601W, accelerometer, vibration motor, battery + buffer, antenna, PCB) | €11.50 | €9.00 |
| Base BOM (SX1262 module/MCU, sounder, relay, LED, backup cell, PCB) | €9.50 | €7.50 |
| Mains adapter (certified) | €2.20 | €1.80 |
| Assembly & test (RF range/TX power test, pairing) | €3.50 | €2.40 |
| Enclosures (IP67 pendant + base) | €5.50 | €3.20 |
| Packaging (box, lanyard, clip, manual) | €1.80 | €1.30 |
| Freight + duty to EU | €1.60 | €1.10 |
| Certification amortised (~€22k: RED 868 MHz, EMC, LVD via certified adapter, IP67, battery docs) | €22.00 | €4.40 |
| **Landed cost** | **€57.60** | **€30.70** |
| Net price after channel (direct €99 ex-VAT / merchant €65) | €99 | €65 |
| **Gross margin** | **€41.40 (42%)** | **€34.30 (53%)** |

### Go-to-market
**First 100 customers:**
- **Farm and ploughing shows** (big rural crowds in IE, UK, FR): a range demo is the whole pitch. Set up the base on the stand and have a volunteer press the pendant from the far end of the showground.
- **Farm-safety organisations and campaigns:** national farm-safety charities and agricultural advisory services run lone-worker campaigns. Offer a pilot for their older-farmer programme.
- **Rural women's and farm-family associations, and allotment associations** (one association = 20–200 members).
- **Agricultural merchants' counters** with a demo set.

**Scale channels:** agri-merchant chains, rural care organisations (add it to their home care package), farm-insurer prevention programmes, garden-machinery dealers (bundle with ride-on mowers and chainsaws).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Range kill test on 5 farms; works-like sets; interview 30 families |
| Q2 | Custom pendant + base PCBs, IP67 enclosure; EVT 30 sets on farms for 8 weeks |
| Q3 | DVT; RED + IP67 testing; pilot 200 sets via one farm-safety programme |
| Q4 | 1,000 sets; merchant listing; repeater and LTE-M base variant designed |

**Team:** 1 RF/embedded engineer (LoRa link, low-power pendant), 1 firmware/hardware generalist (base, relay, sounder), the founder on rural sales, ideally with a farming background. Buy in mechanical design (IP67 pendant).

**Funding to the first 1,000 sets (estimates):** NRE €45k (two PCBs €12k, IP67 pendant + base tooling €20k, firmware €13k) + certification €22k + 1,000 sets landed ~€36k + 9 months lean costs €50k ≈ **€153k**. Subtract show pre-orders (200 × €109 ≈ €22k) and a rural innovation grant share (~€15–25k) → **~€110–120k**. Route: pre-orders + grant + an angel from agri-supply or rural care.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** range through barn walls, hedges, hills and a body (pendant on the chest, user lying face down) | Kill test in week 1–3 on 5 real farms; base antenna high (window or outside mount); repeater option; acknowledged messages with retries |
| **Technical:** battery life with high TX power | Adaptive TX power based on the last link RSSI; daily heartbeat only; low-battery warning 4 weeks ahead |
| **Regulatory:** 868 MHz duty-cycle and power limits | Check the band choice with a lab: ERC Rec 70-03 has a dedicated social-alarm band (869.20–869.25 MHz, low power) and the 869.40–869.65 MHz band allows higher power at 10% duty cycle. An alarm press is rare, so the duty cycle is fine; test it |
| **Market/safety:** people trust it as a life-saver, and a missed alarm is catastrophic | Honest claims ("extends range; not a guaranteed emergency service"); heartbeat + "pendant not seen" alerts; recommend combining with existing social alarms; product-liability insurance from day one |
| **Market:** families choose a smartwatch | Sell range, a no-charging battery, ruggedness and "no phone needed" |
| **Supply:** HM-6601W single-source | Footprint-compatible LoRa SoC modules from other makers exist (the STM32WL-based ones); keep the firmware on a portable radio abstraction |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF HM-6601W LoRa SoC module | https://www.gongbans.com/db/hoperf-hm-6601w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/HM-6601W) | Pendant brain + radio in one: Cortex-M4 48 MHz, +22 dBm, −138 dBm sensitivity, sleep 1.3 µA, 868 MHz variant | Datasheet/user guide (no schematic/PCB in the folder) | MIT (HopeRF repo) for the published files |
| M5Stack Cap LoRa-1262 (U214) | https://www.gongbans.com/db/m5stack-cap-lora-1262.html | Ready LoRa (SX1262) receiver for the works-like base | Enclosure/structure only (no main-board electronics) | Buy for prototyping |
| Seeed Grove-Buzzer | https://www.gongbans.com/db/seeed-grove-buzzer.html | Sounder driver reference (scale up to an >85 dB piezo siren) | schematic | Seeed wiki resources; check the licence |

### Block diagram
```
PENDANT (IP67)                                                   BASE (indoors, mains + backup cell)
[HELP button] [cancel (recessed)]                                [SX1262 LoRa RX/TX] <- antenna, high mount
[accelerometer: tilt-and-still]  -> [HM-6601W LoRa SoC] ~~868 MHz, acked, retries~~> [MCU] -> [sounder >85 dB] [flash light]
[vibration motor: "help notified"] <-                                               -> [relay out -> home alarm / auto-dialler]
[Li-SOCl2 1/2 AA + buffer cap]                                                      -> [optional LTE-M SMS module (v2)]
                                                                                    -> ["pendant not seen 24 h" warning]
```
**Engineering gap:** the radios exist. What's missing: an ultra-low-power pendant design with a pulse-current buffer, an IP67 pendant that's comfortable and has a big button that can't be pressed by accident, the acknowledged point-to-point protocol with pairing and heartbeats, the tilt-and-still algorithm (keep it conservative), the base's relay/dialler integration, and a lot of range testing.

### Starter BOM (estimates per set at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HM-6601W (868 MHz variant) | €4.50–6.00 | **Sole-source (HopeRF)**; confirm the 868 variant's availability and MOQ |
| 3-axis accelerometer | €0.50 | Low-power wake-on-motion |
| Vibration motor + LED + buttons | €0.90 | |
| Li-SOCl2 1/2 AA + supercap/hybrid layer capacitor | €2.80 | Pulse-current capable; DG shipping |
| Pendant antenna (helical/PCB) | €0.40 | Body detuning: tune with a phantom |
| Base: SX1262 module + MCU | €5.50 | Or a second HM-6601W as the base radio + MCU |
| Base: piezo siren >85 dB, relay, LED, backup cell | €3.50 | |
| Mains adapter (certified, 5 V) | €2.20 | Buy with existing CE reports |
| PCBs, passives | €2.00 | |

### Firmware/software starting point
- HopeRF HM-6601W datasheet/user guide from the GitHub folder; ask HopeRF for its SDK and example projects.
- RadioLib (github.com/jgromes/RadioLib) supports SX126x on the base side for fast prototyping on ESP32.
- Point-to-point protocol: keep it simple (packet with pendant ID, counter, event type, CRC + an AES-CMAC so a neighbour's device can't fake alarms), ack within 200 ms, 3–5 retries on different timing.
- The M5Stack examples for the Cap LoRa-1262 get the base working on day one.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | Works-like pendant (HM-6601W eval or any SX126x board in a pouch) + base; **kill question: 200 presses at 5 real farms (barn wall + 600 m orchard), ≥95% delivered with ack**; 30 family interviews |
| 3–5 | Works-like | Battery-powered pendant prototype; current profile measured, ≥12-month battery model; heartbeat + "not seen" logic; relay output tested with 2 common auto-diallers |
| 6–8 | Looks-like + EVT | Custom pendant PCB in a soft-tooled IP67 housing; base enclosure; 30 sets on farms for 8 weeks; drop test 1.5 m on concrete; glove-press test |
| 9–10 | DVT + pre-compliance | RED pre-scan (EN 300 220, duty cycle, power), EMC; IP67 immersion; battery transport docs; tilt-and-still false-alert rate < 1/month |
| 11–12 | Pilot batch | 50 sets sold through one show/programme; return rate < 5%; at least 3 real-world "help" uses documented (with consent) |

### Certification checklist (EU)
- **CE under RED:** EN 300 220-1/-2 (868 MHz SRD, including the band-specific power and duty-cycle limits; choose the band with your lab), EN 301 489-1/-3 (EMC), EN 62368-1 (base safety; use a certified mains adapter), EN 62479 (exposure, low power). Est. **€8–14k**.
- **Social-alarm standards:** the EN 50134 series covers social-alarm systems. It's not mandatory for this product, but follow its principles (acknowledgement, supervision) and don't claim conformity unless tested.
- **RED delegated act (EN 18031):** not applicable while the base has no internet connection. The LTE-M v2 base would bring EN 18031-1 (and -2 if it handles personal data, such as phone numbers).
- **CRA:** still a product with digital elements: secure pairing, update path (at least via USB on the base), vulnerability contact; reporting from 11 Sept 2026, full from 11 Dec 2027.
- **Battery Regulation (EU) 2023/1542:** portable batteries (pendant primary cell, base backup), labelling, removability by the user, take-back. Lithium shipping (UN 3091/3481) paperwork.
- **IP67** (EN 60529) for the pendant; **RoHS, REACH, WEEE**, packaging registration.
- **Not a medical device:** a safety alert with no health monitoring or diagnosis. Keep "fall detection" wording out of the marketing (use "tilt-and-still alert"), or the MDR/claims questions start.
- **GDPR:** minimal (no cloud). The v2 SMS base stores contacts' phone numbers, so add a short privacy notice.
- **Total certification budget estimate: €12–22k.**

### Validation toolkit
- **Kill question:** Does a pendant reach the house through a barn wall and 600 m of orchard in 95% of 200 test presses? Measure on 5 real farms first.
- **Cheapest experiment (~€300):** two off-the-shelf SX126x dev boards with a simple acked ping, one in a pocket-sized box on a lanyard and one in the farmhouse window; walk the farm and press 200 times while logging RSSI and acks. Then show the result at a farmer meeting with a price card.
- **5-question interview (adult child / older farmer):** 1) Where on the property do you (or your parent) work alone, and how far is that from the house? 2) What happens today if something goes wrong out there? 3) Have you tried a home alarm pendant, phone or watch, and why didn't it work outside? 4) Who should hear the alarm: the house, a neighbour, your phone? 5) €119 once, no SIM, no subscription: would you buy it today?
- **Landing page headline:** "Help, all the way to the far field." Bullets: "1 km+ range, no SIM, no subscription, no mobile signal needed." / "Press once: the house siren sounds and you feel it vibrate when help is notified." / "Rugged, waterproof, a battery that lasts a year."
- **Pass threshold:** ≥95% delivery in the range test **and** 50 set pre-orders (€25 deposit) from one show or one farm-safety programme.

### First production checklist
- **Samples:** golden pendant + base with TX power, frequency error and sensitivity measured; range reference test on a fixed test site.
- **DFM review:** pendant button feel (with gloves), gasket and ultrasonic welding vs screws, antenna clearance from the battery, base siren acoustics.
- **MOQ talk:** HM-6601W (868 variant), Li-SOCl2 cells (DG shipping; consider an EU source), enclosure colours (high-vis orange?).
- **QC/AQL:** AQL II 0.65 (critical: alarm path) / 1.0 / 2.5; 100% TX power and frequency check, 100% pairing + ack test, 100% siren dB check, 5% IP67 dunk per lot.
- **Packaging:** set box with both units pre-paired, lanyard, belt clip, base window mount, clear "what this is / isn't" card.
- **Incoterms:** FOB Shenzhen; ship pendants without cells if DG costs bite and insert EU-sourced cells at a local fulfilment partner.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (HopeRF (华普微) and M5Stack and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU)](/db/hoperf-hm-6601w.html) (LoRa SoC module in the pendant (radio + Cortex-M4, runs the app)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Cap LoRa-1262 (U214)](/db/m5stack-cap-lora-1262.html) (LoRa receiver for the indoor base station). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Buzzer](/db/seeed-grove-buzzer.html) (base-station sounder reference). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and M5Stack and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer — for a Farmyard Help Button (LoRa, no SIM)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Farmyard Help Button (LoRa, no SIM): A rugged help pendant with 1–2 km line-of-sight range for older people working alone in large gardens, orchards, farmyards and allotments — where DECT and Wi-Fi alarm pendants don't reach. The design is built around your HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer.

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer.
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
主题：样品订购及批量报价 — HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer — 用于Farmyard Help Button (LoRa, no SIM)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Farmyard Help Button (LoRa, no SIM)：A rugged help pendant with 1–2 km line-of-sight range for older people working alone in large gardens, orchards, farmyards and allotments — where DECT and Wi-Fi alarm pendants don't reach。产品设计基于贵司的HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer。
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
Subject: PCBA quote from open design files — Farmyard Help Button (LoRa, no SIM), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Farmyard Help Button (LoRa, no SIM): A rugged help pendant with 1–2 km line-of-sight range for older people working alone in large gardens, orchards, farmyards and allotments — where DECT and Wi-Fi alarm pendants don't reach. The design starts from published open-hardware files (HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Farmyard Help Button (LoRa, no SIM)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Farmyard Help Button (LoRa, no SIM)：A rugged help pendant with 1–2 km line-of-sight range for older people working alone in large gardens, orchards, farmyards and allotments — where DECT and Wi-Fi alarm pendants don't reach。设计基于已公开的开源硬件文件（HopeRF HM-6601W LoRa SoC module (radio + Cortex-M4 MCU), M5Stack Cap LoRa-1262 (U214), Seeed Grove-Buzzer；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order two SX126x dev boards (or the HopeRF HM-6601W samples), flash a simple acked ping, and run the 200-press range walk on one farm.
2. Ask a test lab which 868 MHz sub-band and power level they recommend for an alarm pendant, with duty-cycle maths for 1 press/day + heartbeats.
3. Contact one farm-safety organisation and one allotment association, use the interview script, and ask for a 10-set pilot.

Want help sourcing or building this? Talk to us via www.gongbans.com.
