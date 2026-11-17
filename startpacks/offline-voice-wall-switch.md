# Offline Voice Wall Switch — Founder Start Pack

> A wall switch you can talk to ("lights on", "dim to half", "kitchen off"), with all speech recognised on the device, no audio ever leaving the room, and Matter to talk to the rest of the house.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Many households in DE, NL and AT want voice control but refuse to put a cloud microphone in the kitchen or bedroom. The cloud speakers they reject are also the only easy way to get voice. Separately, people with full hands (cooking, workshop, carrying a child) want lights without touching a switch.
- **Customer:** Privacy-minded homeowners and renovators; holiday-home owners (guests, no accounts); electricians and smart-home installers doing renovations. The homeowner pays, the electrician installs and recommends.
- **Product:** A wall switch in a standard European 60 mm flush box with: a relay for the local light circuit, a physical rocker/button, an **offline** fixed-vocabulary voice engine (~30 commands per language; DE/NL/EN first — the language support of the ASR chip must be verified), a wake word, and a **hardware mute switch** that physically disconnects the microphone. A Matter-over-Thread radio controls other Matter lights, plugs and scenes in the house.
- **Why now:** Offline keyword ASR modules cost a few euros. Matter lets one switch drive lights of any brand. The EU AI Act and GDPR debates have made "no cloud microphone" a selling point. Open-source local-voice ecosystems show demand among enthusiasts; mainstream buyers want it in a switch that just works.
- **The ask:** About €250–300k (estimate) to the first 1,000 certified units. The fixed costs (mains safety, EMC, RED, Matter) come before the first sale. Funding route: an electrical-installation brand partner or a smart-home angel + pre-orders.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does the offline ASR reach >90% command accuracy in a real kitchen with a dishwasher running, in Dutch and German? Test 20 speakers before anything else.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Privacy-minded households in DE/NL/AT who refuse cloud speakers; holiday-home owners; people whose hands are full (kitchens, workshops).

**The problem as the pack states it:** Many households in DE, NL and AT want voice control but refuse to put a cloud microphone in the kitchen or bedroom. The cloud speakers they reject are also the only easy way to get voice. Separately, people with full hands (cooking, workshop, carrying a child) want lights without touching a switch.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **r/smarthome** · https://www.reddit.com/r/smarthome/ — less technical smart-home buyers.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€69–99 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how privacy-minded households in DE/NL/AT who refuse cloud speakers deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you switch and dim lights today when your hands are full, and what made you decide against a cloud voice speaker, if you did?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A wall switch you can talk to — 'lights on', 'dim to half', 'kitchen off' — with all speech recognised on the device, no audio ever leaving the room, and Matter to talk to the rest of the house. On a scale of one to ten, how likely would you be to buy that at €69–99 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Offline Voice Wall Switch: would you pay €69–99 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Offline Voice Wall Switch: A wall switch you can talk to — 'lights on', 'dim to half', 'kitchen off' — with all speech recognised on the device, no audio ever leaving the room, and Matter to talk to the rest of the house. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €69–99 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Primary: **privacy-aware homeowners in DE/NL/AT who are renovating** (kitchen and bathroom renovations are the moment a switch gets replaced). They pay; an electrician installs. Secondary: **holiday-home owners** — guests can control lights by voice without any app or account, and the owner doesn't worry about microphones. Third, B2B: **switch-range brands** that want a voice insert/cover for their range (white label).

### Market size (estimates)
- DE + NL + AT households: ~53 M. Assume 2% put at least one voice switch in over 5 years, 2 switches each → **~2.1 M units → TAM ~€170 M** at €79.
- **SAM:** reachable via installers + online in DE/NL/AT, ~25% → **~€40 M**.
- **SOM (3 years):** 2% of SAM → **~10k units → ~€800k**. Real upside only with a switch-brand partnership.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Cloud smart speakers + smart bulbs/switches | €30–100 + bulbs | Cloud microphone, accounts, privacy — exactly what this segment refuses |
| Open-source local voice satellites (e.g. Home Assistant's voice hardware and DIY ESP32 satellites) | €50–80 + a home server | Needs a server and tinkering; not a wall switch an electrician installs |
| Smart switches / panels with built-in cloud voice assistants | €100–250 | Cloud voice again; big panels |
| Matter/Zigbee wall switches without voice | €30–70 | No voice |
| Do nothing: elbow the switch | Free | Fine for many people — be honest about it |

**Wedge:** **the only thing on the wall is the switch — and it never sends audio anywhere.** Offline voice + a normal switch + Matter, installed by an electrician like any other switch.

### Product & value proposition
- **Voice:** offline ASR chip, fixed commands, wake word. Prototype with the M5Stack Unit ASR; production with the ASR chip/module directly on your PCB (ask the vendor). Command set example: "Licht an/aus", "dimmen auf Hälfte", "Küche aus", "alles aus", "Szene Abend".
- **Radio:** HopeRF HM-MT2401 (EFR32MG24, Matter over Thread / BLE 5.3, 1,536 KB flash, 256 KB RAM) as main MCU: local relay control + Matter client (bindings) to other devices + Matter server so the switch itself appears in any Matter app.
- **Power:** Hi-Link HLK-5LSxx 5 W ultra-small isolated supply (26.4 × 17.5 × 10 mm, 3000 VAC isolation) — needs neutral in the box.
- **Switching:** latching relay for the local circuit (low heat), zero-cross switching; dimming version later (trailing-edge dimmers in a wall box are a separate, harder product).
- **Privacy design:** hardware mute (slide switch) that cuts mic power; mic-active LED wired to the mic power rail (cannot be faked by firmware); no audio path to the radio at all (the ASR chip outputs only command IDs over UART). This lets you make — and prove — the claim.

**Pricing (estimates):** €79 RRP (one-gang, relay + voice + Matter); €69 voice "remote" version (battery or no relay, controls other devices only); installer price ~€55.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (ASR chip/module, mic, small speaker for confirmation, HM-MT2401, HLK-5LS supply, latching relay, zero-cross, mute switch, PCB) | €16.50 | €13.00 |
| Assembly & test (voice test box, relay, hi-pot) | €2.20 | €1.50 |
| Enclosure: insert + rocker + frame (V-0) | €3.50 | €2.40 |
| Packaging | €1.00 | €0.70 |
| Freight + duty to EU | €0.60 | €0.40 |
| Certification amortised (safety + EMC + RED ~€40k, Matter/CSA ~€20k) | €60.00 | €12.00 |
| **Landed cost** | **€83.80** | **€30.00** |
| Net revenue (direct €66 ex-VAT; installer/wholesale €46) | €66 | €46 |
| **Gross margin** | **−€17.80 (loss)** | **€16.00 (35%)** |

At 1k units you lose money because of fixed certification costs. Plan for 5k+ in year 1–2, or let a brand partner pay certification as NRE.

### Go-to-market
**First 100 customers:**
- **Privacy-tech communities** in DE/NL (data-protection associations' events, privacy blogs, local-first/self-hosting forums, Mastodon) — the claim must survive their scrutiny, so publish the firmware architecture and a third-party audit summary.
- **Kitchen and bathroom renovation installers** in one region: give 10 installers demo units and a margin.
- **Holiday-home owners' associations and rental-platform host communities** — "voice for guests, no microphones in the cloud".
- **Crowdfunding** with a strong privacy story (but deliver only after certification; don't ship uncertified mains products).

**Scale:** electrical wholesale; white-label insert for a switch-range brand; smart-home retailers.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: offline ASR accuracy in a real kitchen (dishwasher, extractor hood) in NL and DE, 20 speakers; thermal check in a sealed box |
| Q2 | Works-like with relay + Matter; 10 homes; privacy architecture review by an external security person |
| Q3 | EVT/DVT; safety (EN 60669-2-1), EMC, RED, Matter certification |
| Q4 | 1,000–5,000 units; installer channel in one country; brand talks |

**Team:** 1 mains/power engineer (experienced with EN 60669), 1 embedded engineer (Matter on Silicon Labs + ASR integration), founder on marketing/installer channel. Certification consultant.

**Funding to the first 1,000 certified units (estimates):** NRE €90k (hardware €35k, firmware/Matter/ASR packs €40k, tooling €15k) + certification €40k + Matter/CSA €20k + 1,000 units landed ~€24k + 9 months lean costs €70k ≈ **€245k**. Minus crowdfunding/pre-orders (600 × €69 ≈ €40k) → **~€200k**. Route: angel + pre-orders; or brand NRE.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** ASR accuracy in noisy kitchens; Dutch and German support of the chip | Kill test first; short command set; mic placement at the top of the frame; language support confirmed with the vendor in writing |
| **Technical:** mic and speaker inside a wall switch — acoustics through a small grille | Acoustic design early (week 3–5), not as an afterthought |
| **Technical:** heat in the box (supply + relay) | Latching relay; 5 W supply is already oversized — measure; thermal test sealed |
| **Trust/claims:** "no audio leaves the device" must be literally true | Hardware architecture with no audio path to the radio; external audit; publish it |
| **Regulatory:** mains + radio + Matter certification costs | Brand partner or volume; reuse module reports |
| **Market:** niche; many people are fine with cloud speakers or no voice | Target privacy communities + holiday homes; keep a non-voice SKU sharing the same platform |
| **Supply:** ASR chip vendor dependency, language packs | Second ASR option qualified; keep ASR on a daughterboard footprint |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit ASR (U194) | https://www.gongbans.com/db/m5stack-unit-asr.html | Offline speech recognition (fixed command set) for the works-like prototype | Enclosure/structure files only — main-board electronics not published | Prototype; production design with the ASR chip vendor |
| HopeRF HM-MT2401 Matter-over-Thread module | https://www.gongbans.com/db/hoperf-hm-mt2401.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Matter/HM-MT2401) | Matter over Thread + main MCU (EFR32MG24) | PCB footprint/library, datasheet | MIT (HopeRF GitHub repo) |
| Hi-Link HLK-5LSxx 5 W ultra-small AC-DC | https://www.gongbans.com/db/hilink-5lsxx.html | Isolated mains supply that fits a wall box | **Datasheet public, files via maker** | Commercial module; check its safety approvals |

### Block diagram
```
 L/N ─[fuse]─[varistor]─[HLK-5LS]──> 3.3 V
                                       |
 [MEMS mic] -[mute switch cuts power]-> [offline ASR chip] --UART: command ID only--> [HM-MT2401 (MG24)]
       [mic-active LED on mic power rail]                                             |   |   |
                                                       [rocker/button] -------------->+   |   +~~Thread/Matter~~> other lights, plugs, scenes
                                                       [small speaker: "kitchen off"] <---+
 L ──[latching relay]──> L-out (local light) <-------------- drive ------------------------+
```
**Engineering gap:** acoustics in a switch frame, ASR command packs per language, the hardware mute and the "no audio path" architecture, the mains design (creepage, heat, relay), and Matter firmware (On/Off Light server + On/Off client bindings).

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Offline ASR chip/module | €2.50–4.00 | **Vendor-dependent language packs**; confirm DE/NL |
| MEMS mic + small speaker + amp | €1.80 | |
| HM-MT2401 | €3.50–4.50 | MG24 modules available from several makers |
| HLK-5LSxx | €2.00 | |
| Latching relay + zero-cross + drivers | €2.00 | |
| Mute slide switch + LEDs | €0.40 | |
| PCB, terminals, fuse, varistor | €1.50 | |
| Insert + rocker + frame | €3.50 | Tooling ~€12–18k; frame compatibility with common EU ranges is a sales argument |

### Firmware/software starting point
- **Matter:** Silicon Labs Matter extension for MG24; **connectedhomeip** (github.com/project-chip/connectedhomeip) — combine the "lighting-app" (local relay) and "light-switch-app" (bindings to other devices) examples.
- **OpenThread** (github.com/openthread/openthread).
- **ASR:** vendor tools for custom command words (ask M5Stack which chip the Unit ASR uses and get the chip vendor's SDK); search "offline voice recognition module custom command" for the chip vendor's documentation.
- **Reference for privacy claims:** document the data path; an external reviewer from the privacy/self-hosting community is worth more than marketing.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill test:** ASR unit in a real kitchen with dishwasher + extractor hood running; 20 speakers (10 DE, 10 NL) × 10 commands: >90% correct, <1 false trigger per day. Plus 200 waitlist sign-ups from privacy communities |
| 3–5 | Works-like | ASR + MG24 + relay on a bench in a wall box; local light + 2 Matter lights controlled; acoustic test through a grille prototype |
| 6–8 | Looks-like + EVT | Insert + frame; 30 units; 10 homes; thermal test sealed 8 h at rated load |
| 9–10 | DVT + pre-compliance | Safety pre-assessment (EN 60669-2-1), EMC/RED pre-scan, Matter test harness, external privacy review |
| 11–12 | Pilot batch | 50 units installed by 5 electricians; accuracy ≥90% in homes; no audio-related findings in the review |

### Certification checklist (EU)
- **LVD / safety:** EN 60669-1 + EN 60669-2-1 (electronic switch in fixed installation): temperature rise, endurance, creepage/clearance, glow-wire. Est. **€15–25k**.
- **EMC:** EN 55014-1/-2 / EN 55015 as applicable, EN 61000-3-2/-3-3, surge/burst. Est. **€5–8k**.
- **RED:** EN 300 328, EN 301 489-1/-17, EN 62311 (reuse module reports). Est. **€5–8k**.
- **RED delegated act (EN 18031-1/-2):** internet-connected via Thread border router; microphone → personal-data aspects. Self-assessment €3–6k.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: secure updates (Matter OTA), SBOM, vulnerability handling, support period.
- **Matter certification** (CSA membership, test lab, device attestation).
- **GDPR:** if no audio or transcripts leave the device and no cloud account exists, data processing is minimal. Still: publish a privacy statement and keep the "no audio" claim exact (also relevant under consumer-protection law — misleading claims).
- **RoHS, REACH, WEEE**, packaging registration.
- **Total estimate: €40–60k + Matter/CSA costs.**

### Validation toolkit
- **Kill question:** Does the offline ASR reach >90% command accuracy in a real kitchen with a dishwasher running, in Dutch and German? Test 20 speakers before anything else.
- **Cheapest experiment (~€150):** M5Stack Unit ASR + an ESP32/MG24 dev board + a relay and a lamp; record accuracy in 5 kitchens.
- **5-question interview:** 1) Do you use voice control today? Why or why not? 2) Where in the house would you use voice for lights (kitchen, bathroom, bedroom)? 3) What would convince you that a microphone in the wall never sends audio anywhere? 4) Are you renovating in the next 12 months, and who installs your switches? 5) At €79 per switch, how many rooms would you equip?
- **Landing page headline:** "Voice control for your lights — the microphone never leaves the room." Bullets: "Speech is recognised inside the switch. No cloud, no account, no recordings." / "Hardware mute switch with a light you can trust." / "Works with Matter lights of any brand, and as a normal switch."
- **Pass threshold:** 300 waitlist sign-ups + 100 paid €20 deposits in 8 weeks, or one switch brand paying for a feasibility study.

### First production checklist
- **Samples:** ASR chips from production lot with final command packs; mic + grille acoustic check per lot.
- **Golden sample:** the unit that passed safety and the privacy review; freeze BOM (any change in supply/relay = re-test).
- **DFM review:** acoustic port sealing (dust, cleaning), creepage on the PCB, terminal design, frame clips for common EU switch ranges.
- **MOQ talk:** ASR chip MOQ and command-pack fees, MG24 module, frame colours (white + 1 colour only at start).
- **QC/AQL:** AQL II 0.65 safety; 100% hi-pot, relay, voice playback test (recorded commands in a test box), mute-switch test (mic dead), Matter commissioning with unique certificates.
- **Packaging:** wiring diagram, Matter QR on device + box, command list card per language, privacy leaflet.
- **Incoterms:** FOB Shenzhen; make sure safety-critical parts are sourced exactly as certified (written in the supply contract).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and HopeRF (华普微) and Hi-Link (海凌科)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit ASR (U194)](/db/m5stack-unit-asr.html) (offline speech-recognition unit (fixed command set)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder)](/db/hoperf-hm-mt2401.html) (Matter-over-Thread module to control lights/scenes). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)](/db/hilink-5lsxx.html) (5 W ultra-small isolated AC-DC supply for the wall box). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and HopeRF (华普微) and Hi-Link (海凌科) websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS) — for a Offline Voice Wall Switch

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Offline Voice Wall Switch: A wall switch you can talk to — 'lights on', 'dim to half', 'kitchen off' — with all speech recognised on the device, no audio ever leaving the room, and Matter to talk to the rest of the house. The design is built around your M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS).
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
主题：样品订购及批量报价 — M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS) — 用于Offline Voice Wall Switch

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Offline Voice Wall Switch：A wall switch you can talk to — 'lights on', 'dim to half', 'kitchen off' — with all speech recognised on the device, no audio ever leaving the room, and Matter to talk to the rest of the house。产品设计基于贵司的M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)。
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
Subject: PCBA quote from open design files — Offline Voice Wall Switch, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Offline Voice Wall Switch: A wall switch you can talk to — 'lights on', 'dim to half', 'kitchen off' — with all speech recognised on the device, no audio ever leaving the room, and Matter to talk to the rest of the house. The design starts from published open-hardware files (M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Offline Voice Wall Switch，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Offline Voice Wall Switch：A wall switch you can talk to — 'lights on', 'dim to half', 'kitchen off' — with all speech recognised on the device, no audio ever leaving the room, and Matter to talk to the rest of the house。设计基于已公开的开源硬件文件（M5Stack Unit ASR (U194), HopeRF HM-MT2401 Matter-over-Thread module (PCB antenna + antenna holder), HLK-5LSxx 5W ultra-small AC-DC isolated power module (5W-LS)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order an M5Stack Unit ASR and an HM-MT2401 module; ask M5Stack/the chip vendor which languages and how many custom commands are supported.
2. Run the 5-kitchen accuracy test with family and friends (DE and NL speakers).
3. Post the concept with the hardware privacy architecture in one privacy/self-hosting community and count sign-ups.

Want help sourcing or building this? Talk to us via www.gongbans.com.
