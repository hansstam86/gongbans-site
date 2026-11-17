# Shed & Allotment Guard — Founder Start Pack

> A battery radar alarm for garden sheds, allotment huts, boat sheds and storage containers. It detects an intruder and sends an alert over LoRa up to kilometres away. No camera, no SIM, no subscription.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Sheds and allotment huts get broken into for tools, garden machinery, cordless-tool batteries and outboard motors. They have no mains power, no Wi-Fi, often no reliable mobile signal, and a camera on a shared plot starts a fight with the neighbours (and a GDPR problem). Local sirens scare nobody at 3 a.m. on an empty allotment.
- **Customer:** Allotment and garden-plot holders and their associations; homeowners with sheds far from the house; marinas and boat-shed owners; small farms; container-storage operators. Individuals pay for their own nodes; associations pay for a shared gateway.
- **Product:** A battery node with a 24 GHz long-range presence radar (Hi-Link LD2410D, range adjustable to ~10 m, sees still people per datasheet) and a HopeRF RFM95 LoRa radio, sending an encrypted alert to an indoor base unit at home (LoRa receiver, M5Stack Cap LoRa-1262-class for the prototype) or to an association's shared gateway. Arm/disarm by key fob, optional siren, radar zones that ignore the path outside the door.
- **Why now:** Tool and battery theft from sheds has grown with expensive cordless tools and e-garden machinery. LoRa reaches 1–5 km in open terrain without any subscription, and 24 GHz radar is cheap enough to replace false-alarm-prone PIRs.
- **The ask:** About €90–110k (estimate) to the first 1,000 nodes. Route: crowdfunding/pre-orders in allotment and gardening communities plus association bulk orders. No VC needed.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Can the radar ignore cats, swaying plants and rain on a tin roof? Run 10 sheds for 4 weeks; more than one false alarm a week is a kill.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Allotment associations, garden owners, marinas, small farms, container-storage operators.

**The problem as the pack states it:** Sheds and allotment huts get broken into for tools, garden machinery, cordless-tool batteries and outboard motors. They have no mains power, no Wi-Fi, often no reliable mobile signal, and a camera on a shared plot starts a fight with the neighbours (and a GDPR problem). Local sirens scare nobody at 3 a.m. on an empty allotment.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **The National Allotment Society (UK)** · https://thenas.org.uk/ — UK allotment federation (formerly NSALG); member associations run the sites.
- **Bundesverband der Kleingartenvereine Deutschlands (DE)** · https://kleingarten-bund.de/ — German allotment federation; the regional and local Kleingartenvereine are the way in.
- **r/UKGardening** · https://www.reddit.com/r/UKGardening/ — UK gardeners and allotment holders; hosepipe bans come up every summer.
- **The Things Network forum** · https://www.thethingsnetwork.org/forum/ — LoRaWAN builders, operators and the companies that deploy them.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79 node / 129 starter set (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how allotment associations, garden owners, marinas, small farms, container-storage operators deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Tell me about the last break-in at your shed, allotment or boat: when did you find out, what was taken, and what have you tried since?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A battery radar alarm for garden sheds, allotment huts, boat sheds and storage containers that detects an intruder and sends an alert over LoRa up to kilometres away — no camera, no SIM, no subscription. On a scale of one to ten, how likely would you be to buy that at €79 node / 129 starter set (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Shed & Allotment Guard: would you pay €79 node / 129 starter set (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Shed & Allotment Guard: A battery radar alarm for garden sheds, allotment huts, boat sheds and storage containers that detects an intruder and sends an alert over LoRa up to kilometres away — no camera, no SIM, no subscription. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79 node / 129 starter set (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Allotment gardening is huge in parts of Europe: Germany alone has on the order of 900,000 allotment plots in associations, Poland a similar order of magnitude, plus large numbers in the UK, the Netherlands, Austria and Scandinavia (association figures; check). Most plots have a hut with tools inside. Burglary waves hit whole sites at once, and associations get asked "what can we do?" at every meeting.

**Two buyers:**
1. **The individual plot holder or homeowner** (€79 node + €129 starter set): the base unit sits in their kitchen, up to a few km away.
2. **The association / site manager:** one shared gateway at the clubhouse or a member's house near the site, alerts going to the plot holder and optionally the site's "night contact". The association buys the gateway and negotiates a bulk price for members.

Also: **marinas and boat-shed rows** (outboard motor theft), **container storage** (the operator monitors many containers), small farms.

### Market size (estimates)
- Allotment plots + detached sheds/huts far from the house in DE, PL, NL, AT, UK, Nordics: assume ~3 M plots + ~5 M qualifying private sheds/outbuildings = **8 M potential sites**, of which maybe 5% care enough to buy an alarm in 5 years → **400,000 sites**.
- **TAM:** 400,000 × €129 ≈ **€52 M** + association gateways.
- **SAM:** DE, AT, NL, UK online + garden-retail reach: ~50% → **€26 M**.
- **SOM (3 years):** 2% of SAM → **~4,000 starter sets + 2,000 extra nodes ≈ €0.67 M**. A good small business if association bulk orders work.

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| Battery PIR sirens (local alarm only) | €15–40 | Nobody hears them on an empty site; PIR false alarms from heat and animals |
| GSM/4G shed alarms (SMS/call on alarm) | €60–150 + SIM | SIM cost and expiry; weak mobile signal in sheds; battery hungry |
| Wi-Fi/4G cameras | €50–200 + often subscription | No Wi-Fi on allotments; filming neighbours' plots = GDPR and conflict; power |
| DIY LoRa alarms (maker projects with LoRa boards, shared-key alerts) | €30–60 + time | Works for makers, no enclosure, no support, battery life unknown |
| LoRaWAN door/motion sensors on public networks | €40–80 + network | Public LoRaWAN coverage is patchy on allotment sites; needs set-up skills |
| Do nothing (padlocks, empty sheds) | Free | Keeps losing tools |

**Wedge:** **no SIM, no Wi-Fi, no camera, no subscription**; alerts reach your kitchen kilometres away; radar that ignores the cat; and an **association mode** where one gateway covers a whole site.

### Product & value proposition
- **Node:** LD2410D radar (24 GHz FMCW, motion/micro-motion/presence, range adjustable to ~10 m, ±60°; avg 50 mA, 100 mA for the Bluetooth D-B version, per Hi-Link) + low-power MCU + RFM95 LoRa (EU868) + battery + optional piezo siren. IP54+ enclosure.
- **The battery problem, honestly:** 50 mA continuous radar draw empties a 10 Ah pack in about 8 days. "Months on a battery" only works with a **low-power wake trigger** (a µA-level PIR or a door/vibration contact) that switches the radar on to confirm a person-sized target, or with a **small solar panel** (2–3 W) + Li-ion/LiFePO4 pack. Design for both: PIR/contact wake + radar confirm = fewer false alarms *and* long battery life. Measure it in EVT; the radar's real duty cycle decides the product.
- **Base unit (home):** LoRa receiver + loud buzzer + LED + Wi-Fi for an optional phone push. Works without Wi-Fi as a pure "it beeps in your kitchen" device.
- **Association gateway:** LoRa receiver at the clubhouse, forwards alerts by Wi-Fi/LTE to plot holders' phones (push/SMS gateway), shows a site map of armed nodes.
- **Key fob:** arm/disarm, rolling-code encrypted. Auto-arm schedule optional.
- **Radar zones:** set the detection distance so the path outside the door is ignored (LD2410D range gates).

**Pricing (estimates):** €79 node, €129 starter set (node + base unit + fob), €39 extra fob ×2, solar kit €29; association gateway €249 (+ member nodes at €69 in bulk).

### Unit economics (estimates per starter set, ex-VAT)
| Item | 1k sets | 5k sets |
|---|---|---|
| BOM node (LD2410D, MCU, RFM95, PIR wake sensor, battery pack, siren, PCB) | €17.00 | €13.50 |
| BOM base unit (RFM95 or SX1262 module, ESP32-C3, buzzer, LED, USB-C) + fob | €11.00 | €8.50 |
| Assembly & test (RF link per pair, radar functional, current consumption in sleep) | €3.00 | €2.20 |
| Enclosures (IP54 node, base, fob) | €4.00 | €2.50 |
| Packaging | €1.50 | €1.00 |
| Freight + duty to EU (battery shipping adds cost) | €1.80 | €1.20 |
| Certification amortised (~€25k: RED 24 GHz + 868 MHz + 2.4 GHz, EMC, EN 18031, battery transport UN 38.3 if Li-ion) | €25.00 | €5.00 |
| **Landed cost** | **€63.30** | **€33.90** |
| Net price ex-VAT: direct €108 (from €129) / via garden/DIY retail ~€70 | €108 / €70 | €108 / €70 |
| **Gross margin** | **€45 (41%) direct / €7 (10%) retail** | **€74 (69%) / €36 (52%)** |

Sell direct and through associations for the first 1,000; retail only once volume brings the cost down.

### Go-to-market
**First 100 customers:**
- **Allotment associations** in one city: present at the annual meeting after a break-in wave (they happen every winter), offer a site pilot: 1 gateway + 10 nodes at cost.
- **Allotment and gardening forums, Facebook groups and magazines** (DE "Kleingarten" community is very active; UK allotment forums; NL "volkstuin" networks).
- **Marinas:** harbour masters are a single point of contact for 50–300 boat owners.
- **Crowdfunding** in DE/UK as the kill test and launch.

**Scale channels:** national allotment federations (member-benefit deals), garden centres, DIY chains, marina chandlers, container-storage operators (B2B multi-node).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question: 10 sheds × 4 weeks with works-like nodes (false-alarm count, battery drain); association interviews; crowdfunding page draft |
| Q2 | Custom node + base PCB, IP54 enclosure, PIR-wake + radar-confirm firmware; crowdfunding launch (spring, when people return to their plots) |
| Q3 | DVT; RED/EMC/EN 18031 + UN 38.3; association gateway; ship backers before autumn (break-in season) |
| Q4 | 1,000 sets; 5 association sites live; garden-retail conversations |

**Team:** founder (community sales, associations), 1 embedded engineer (low-power design, LoRa protocol, radar tuning), part-time industrial designer (IP54 enclosures), part-time support/community person in season.

**Funding to the first 1,000 sets (estimates):** NRE €40k (electronics €12k, firmware €15k, enclosures + tooling €10k, app/gateway €3k) + certification €25k + 1,000 sets landed ex-cert ~€38k + 9 months lean costs €25k ≈ **€128k**; minus crowdfunding (600 × €99 early bird ≈ €59k gross, ~€50k net) → **~€80–90k** from savings/angel. Route: crowdfunding + association pre-orders; possibly local crime-prevention or community grants for association pilots.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: false alarms (cats, foxes, swaying plants, rain on a tin roof, wind-shaken shed)** | Inside-the-shed mounting (no plants), radar range gates, PIR/contact + radar double confirmation, 4-week 10-shed test: more than one false alarm a week = kill |
| **Technical: battery life with a 50 mA radar** | Wake-trigger architecture + solar option; publish measured battery life, not a datasheet guess |
| **Technical: LoRa range from inside metal containers/sheds** | External antenna option; association gateway near the site; range test in EVT |
| **Legal: "alarm system" expectations** | State clearly: an alert device, **not** a certified intruder-alarm system (EN 50131); no insurance claims |
| **Security: jamming or replay** | Encrypted, counter-based frames; supervision heartbeat (node silent = alert) |
| **Market: seasonal, price-sensitive buyers** | Launch in spring, ship before autumn; association bulk pricing |
| **Supply: LD2410D sole source; Li-ion shipping** | Radar abstraction; primary-lithium battery option (simpler transport and lower fire risk in a shed) |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD2410D / LD2410D-B long-range presence radar | https://www.gongbans.com/db/hilink-ld2410d.html | Motion/micro-motion/presence to ~10 m (adjustable), ±60°, UART + GPIO, 3.3/5 V, avg 50/100 mA (per Hi-Link) | Datasheet public; schematics/files via maker (contact Hi-Link) | Commercial module, no open design files |
| HopeRF RFM95/96/98(W) LoRa module | https://www.gongbans.com/db/hoperf-rfm95-96-98w.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/LoRa/RFM95_96_98%28W%29) | Node radio: LoRa EU868, +20 dBm max, −144 dBm, 200 nA register retention, SPI | PCB footprint, demo code, datasheet, 3D model, CE/FCC reports | MIT (HopeRF repo) |
| M5Stack Cap LoRa-1262 (U214) | https://www.gongbans.com/db/m5stack-cap-lora-1262.html | Base-unit LoRa receiver for the prototype (SX1262-class) | Enclosure/structure files only (main-board electronics not published) | Dev unit; production base is your own PCB |

### Block diagram
```
SHED NODE (battery / solar)
[PIR or door/vibration contact, µA] --wake--> [low-power MCU] --enable--> [LD2410D radar] --UART--> confirm person-sized target
                                                   |--SPI--> [RFM95 LoRa] ~~ encrypted alert + 6-h heartbeat ~~+
                                                   `--> [piezo siren (optional)]                              |
                                                                                                              v
HOME BASE:  [LoRa receiver] -> [ESP32-C3] -> buzzer + LED (+ optional Wi-Fi push)      or
ASSOCIATION GATEWAY: [LoRa receiver] -> [Wi-Fi/LTE] -> push/SMS to plot holder, site map
[key fob: LoRa or sub-GHz, rolling counter] ~~ arm / disarm ~~> node
```
**Engineering gap:** the low-power wake/confirm state machine and real battery budget, radar range-gate tuning inside small sheds, an encrypted point-to-point protocol with supervision (missing heartbeat = alert), the multi-node association gateway, pairing UX for non-technical gardeners, and an IP54 enclosure that's radar-transparent.

### Starter BOM (estimates at 1k sets)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD2410D radar | €2.50–3.50 | Sole source (Hi-Link) |
| RFM95W × 2 (node + base) or SX1262 module at base | €7.00 | Multiple SX127x/SX126x sources |
| Low-power MCU (Cortex-M0+/M4 with deep sleep in µA range) | €1.00 | Not an ESP32 on the node: sleep current matters |
| PIR sensor (low-power digital) | €1.20 | Wake trigger |
| Battery: 2× primary lithium D or 18650 Li-ion pack | €4–7 | Li-ion needs UN 38.3 + protection; primary simpler |
| Piezo siren 95 dB | €1.00 | Optional |
| Base: ESP32-C3 module, buzzer, LED, USB-C | €4.00 | |
| Fob (MCU + radio, coin cell) | €3.00 | |

### Firmware/software starting point
- **LoRa:** RadioLib (supports SX127x/RFM95 and SX126x; point-to-point and LoRaWAN), HopeRF demo code from the GitHub folder.
- **Radar:** Hi-Link LD2410D serial protocol and BLE configuration (D-B variant; search Hi-Link's download centre for their app/tool); ESPHome has community LD2410 support for quick bench tests (search "ESPHome ld2410").
- **Mesh/community alternative for a quick prototype:** Meshtastic (open-source LoRa mesh firmware) can carry simple alert messages; good for a feasibility test, not for the product.
- **Encryption:** AES-128 with a frame counter (your MCU vendor's crypto library or mbedTLS on the base).

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question set-up:** 10 sheds (allotments + gardens + 1 boat shed) recruited; works-like nodes from devkits; baseline association interviews (5) |
| 3–5 | Works-like | Devkit nodes in 10 sheds for 4 weeks; log every trigger. Pass: ≤1 false alarm per shed per week, 100% of staged walk-ins detected, LoRa alert received at ≥1.5 km in town |
| 6–8 | Looks-like + EVT | Custom low-power PCB, IP54 enclosure, PIR-wake + radar-confirm; measured average current → projected battery life ≥4 months (or solar break-even) |
| 9–10 | DVT + pre-compliance | RED pre-scan (24 GHz, 868 MHz), EMC, EN 18031 gap analysis, IP54 test, cold test (−10 °C), UN 38.3 if Li-ion |
| 11–12 | Pilot batch | 50 sets: 1 association site with gateway + individual buyers; returns <5%; association asks for a member price |

### Certification checklist (EU)
- **CE under RED:** 24 GHz radar (EN 300 440), 868 MHz SRD (EN 300 220-1/-2; respect duty cycle, e.g. use the 869.4–869.65 MHz sub-band with 10% duty and up to 500 mW ERP for alarm-type traffic, per ERC Rec 70-03; check current rules), 2.4 GHz in the base (EN 300 328), EMC (EN 301 489-1/-3/-17), safety EN 62368-1, RF exposure. Est. **€10–14k**.
- **RED delegated act cybersecurity EN 18031-1** for the internet-connected base/gateway (and -2 if it processes personal data such as plot holders' contact details). Est. **€5–8k**.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: update path (local for nodes), SBOM, vulnerability handling.
- **Battery Regulation (EU) 2023/1542:** labelling, removability, collection; **UN 38.3** transport test for Li-ion; primary lithium avoids some hassle.
- **RoHS, REACH, WEEE, packaging registration.**
- **Not EN 50131:** state on the box and in the manual that it's an alert device, not a certified intruder-alarm system, and not an insurance-grade alarm.
- **GDPR:** radar doesn't identify anyone; the association gateway stores member contacts and alert times (personal data) → simple privacy notice and DPA for associations.
- **Total estimate: €17–25k.**

### Validation toolkit
- **Kill question:** Can the radar ignore cats, swaying plants and rain on a tin roof? Run 10 sheds for 4 weeks; more than one false alarm a week is a kill.
- **Cheapest experiment (~€250):** 10 radar + LoRa devkit nodes in 10 sheds with power banks, one receiver logging every trigger with a timestamp, plus a weekly "was that you?" check with the owners.
- **5-question interview (plot holder / association chair):**
  1. Has your hut (or your site) been broken into? What was taken, and what did it cost?
  2. What have you tried: padlocks, sirens, cameras? What went wrong?
  3. Is there power, Wi-Fi or mobile signal at your hut?
  4. Would you rather have the alert in your kitchen, on your phone, or with a site contact?
  5. €129 for a set, no subscription: would you buy it today? Would your association co-fund a gateway?
- **Landing-page headline:** "Know when someone's in your shed. From your kitchen."
  - Radar alarm that ignores cats and plants. No camera.
  - Alerts over long-range radio: no SIM, no Wi-Fi, no subscription.
  - One gateway can cover a whole allotment site.
- **Pass threshold:** false-alarm test passes **and** ≥300 crowdfunding backers or 3 associations ordering a site pilot within 6 weeks.

### First production checklist
- **Samples:** sleep current of 20 production nodes (the battery promise lives here), radar lot test, LoRa output power and frequency.
- **Golden sample:** node + base + fob paired, measured sleep current, detection test at 2/4/6 m, firmware version.
- **DFM review:** IP54 gasket and cable glands, radar-transparent front (uniform wall, no metallic finish), battery door usable with gloves, condensation venting.
- **MOQ talk:** LD2410D, RFM95, enclosures (tooling for 3 parts ~€10–15k; start with a stock IP enclosure + custom front), batteries (supplier with UN 38.3 reports).
- **QC/AQL:** AQL II 1.0/2.5; 100% RF pairing test, 100% sleep-current test, 100% radar trigger test; batch IP test sampling.
- **Packaging:** pre-paired set, mounting kit, "not a certified alarm" notice, quick-start card with LoRa range tips.
- **Incoterms:** FCA Shenzhen; batteries complicate air freight, so plan sea/rail or ship batteries separately from an EU source.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and HopeRF (华普微) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth)](/db/hilink-ld2410d.html) (long-range 24 GHz presence radar). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module](/db/hoperf-rfm95-96-98w.html) (LoRa transceiver (point-to-point or LoRaWAN)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Cap LoRa-1262 (U214)](/db/m5stack-cap-lora-1262.html) (LoRa receiver for the indoor base unit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and HopeRF (华普微) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214) — for a Shed & Allotment Guard

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Shed & Allotment Guard: A battery radar alarm for garden sheds, allotment huts, boat sheds and storage containers that detects an intruder and sends an alert over LoRa up to kilometres away — no camera, no SIM, no subscription. The design is built around your HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214).
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
主题：样品订购及批量报价 — HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214) — 用于Shed & Allotment Guard

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Shed & Allotment Guard：A battery radar alarm for garden sheds, allotment huts, boat sheds and storage containers that detects an intruder and sends an alert over LoRa up to kilometres away — no camera, no SIM, no subscription。产品设计基于贵司的HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214)。
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
Subject: PCBA quote from open design files — Shed & Allotment Guard, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Shed & Allotment Guard: A battery radar alarm for garden sheds, allotment huts, boat sheds and storage containers that detects an intruder and sends an alert over LoRa up to kilometres away — no camera, no SIM, no subscription. The design starts from published open-hardware files (HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Shed & Allotment Guard，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Shed & Allotment Guard：A battery radar alarm for garden sheds, allotment huts, boat sheds and storage containers that detects an intruder and sends an alert over LoRa up to kilometres away — no camera, no SIM, no subscription。设计基于已公开的开源硬件文件（HLK-LD2410D/LD2410D-B 24 GHz long-range human-presence radar module (D-B with Bluetooth), HopeRF RFM95 / 96 / 98(W) Low-power long-range LoRa transceiver module, M5Stack Cap LoRa-1262 (U214)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 10 LD2410D modules, 12 RFM95W and 2 LoRa receivers; build 2 nodes and measure real current draw with the radar on and off.
2. Recruit 10 sheds for the 4-week false-alarm test (your own allotment association, a marina, friends' gardens).
3. Ask 3 allotment association chairs whether a site-gateway pilot could be decided at their next meeting, and what it would need to cost.

Want help sourcing or building this? Talk to us via www.gongbans.com.
