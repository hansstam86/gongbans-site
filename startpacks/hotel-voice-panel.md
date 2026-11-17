# Hotel Room Voice Panel (offline) — Founder Start Pack

> A bedside panel guests can talk to ("lights off", "warmer", "do not disturb", "wake me at seven"). Speech is recognised on the device, nothing is recorded, and a big physical button does everything too.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Guests now expect voice control at home, but hotels can't put cloud smart speakers in rooms: guests complain about microphones that "listen", the accounts are a hassle, and data-protection officers say no. Meanwhile guests fight with five unlabelled light switches at midnight, and guests with low vision or limited mobility can't reach or read the controls.
- **Customer:** Boutique and design hotels (20–150 rooms), holiday parks and serviced apartments, and **accessible rooms** in any hotel. The owner or operations manager pays; the guest uses it; the DPO and the electrician have a veto.
- **Product:** A bedside or wall panel with an **offline** fixed-command voice engine (EN/DE/NL/FR — verify chip language support) plus large physical buttons. It controls room relays (lights, curtains), sends setpoints to the thermostat, sets a wake-up alarm, and switches "do not disturb". A hardware mute switch physically cuts the microphone, with an LED that shows it.
- **Why now:** Wi-Fi modules with a built-in offline voice-recognition chip cost a few euros, so the voice path no longer needs a cloud. Hotels are retrofitting rooms with LED lighting and smart thermostats anyway. Accessibility is a growing booking and compliance factor.
- **The ask:** About €180–220k (estimate) to the first 1,000 panels, funded by pilot hotels (paid pilots), a hospitality-tech angel and a dealer/integrator partnership.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does the voice path stay offline in practice and will a hotel's DPO sign off the Tuya cloud dependency for the dashboard? If either fails, ship only the M5Stack/offline variant.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Boutique hotels, holiday parks, accessible hotel rooms (guests with low vision or limited mobility).

**The problem as the pack states it:** Guests now expect voice control at home, but hotels can't put cloud smart speakers in rooms: guests complain about microphones that "listen", the accounts are a hassle, and data-protection officers say no. Meanwhile guests fight with five unlabelled light switches at midnight, and guests with low vision or limited mobility can't reach or read the controls.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **HOTREC** · https://www.hotrec.eu/ — European umbrella of national hotel and restaurant associations.
- **DEHOGA (DE)** · https://www.dehoga-bundesverband.de/ — German hotel and restaurant association.
- **UKHospitality** · https://www.ukhospitality.org.uk/ — UK hospitality trade body.
- **RNIB (UK)** · https://www.rnib.org.uk/ — blind and partially sighted people; RNIB Connect community.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€129–169 per room (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how boutique hotels, holiday parks, accessible hotel rooms deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. What do guests struggle with in your rooms (lights, heating, the TV, wake-up calls), and what do they ask the front desk for that a switch could have done?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A bedside panel guests can talk to — 'lights off', 'warmer', 'do not disturb', 'wake me at seven' — recognised on the device, nothing recorded, with a big physical button for everything too. On a scale of one to ten, how likely would you be to buy that at €129–169 per room (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Hotel Room Voice Panel (offline): would you pay €129–169 per room (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Hotel Room Voice Panel (offline): A bedside panel guests can talk to — 'lights off', 'warmer', 'do not disturb', 'wake me at seven' — recognised on the device, nothing recorded, with a big physical button for everything too. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €129–169 per room (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Start with **independent boutique hotels and small groups (3–10 properties)** in DACH/Benelux: they decide fast, compete on experience and often have no expensive guest-room management system (GRMS). Second: **holiday parks** (many identical units, central maintenance). Third: **accessible rooms** across hotel chains — a smaller number per hotel, but a clear need and a strong story.

Avoid large chains with a central GRMS in year 1: long procurement, IT-security reviews, integration demands.

### Market size (estimates)
- Europe has roughly 200k hotels and ~6–7 M hotel rooms (order of magnitude; check the latest industry data). Assume 25% are boutique/independent or holiday-park units that renovate on 7–10-year cycles.
- **TAM:** ~1.6 M rooms × €149 ≈ **€240 M** hardware, plus set-up and support.
- **SAM:** DACH/Benelux/Nordics independents + holiday parks, ~25% → **~€60 M**.
- **SOM (3 years):** 0.5–1% of SAM → **3–6k rooms → €0.5–1 M** hardware + installation/support revenue.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Cloud voice assistants for hospitality (big-tech programmes) | €50–100/room + platform fee | Cloud microphones in rooms, guest privacy concerns, programme changes outside your control |
| Guest-room management systems from building-automation vendors (KNX/BACnet-based panels) | €300–1,000+/room installed | Expensive, need renovation-level wiring; voice rarely included |
| In-room tablets / TV-based room control | €150–400/room | Not usable in the dark or for low-vision guests; theft/cleaning issues |
| Labelled switches + bedside master switch | €20–80/room | Cheap and robust (honestly: the real competitor) but no voice, no wake-up, no accessibility gain |
| Do nothing | Free | Guest frustration, reviews mentioning "couldn't find the light switch" |

**Wedge:** **offline voice + big buttons, no cloud microphone, retrofit-friendly**. The DPO can sign it off because no audio leaves the panel.

### Product & value proposition
- **Two variants:**
  - **Tuya variant:** Tuya T3-V-PRO module — Wi-Fi 6 2.4 GHz + BLE 5.4, Tuya T3 MCU plus a Chipintelli CI1302 offline voice-recognition chip, mic in and speaker out (per Tuya's public datasheet). Voice is recognised **on the device**. Remote functions (property dashboard, central config, OTA) run through **Tuya's cloud and B2B tools**.
  - **Offline/Tuya-free variant:** M5Stack Unit ASR (offline speech-recognition unit) for prototyping, with your own MCU, and control via local relays, a local gateway or a hotel network. No third-party cloud at all; central management via a small on-premise server or your own EU-hosted service.
- **Tuya cloud dependency, explained honestly:** on the Tuya variant the **voice path stays offline**, but the dashboard and remote control functions need the Tuya cloud. That means the hotel (as controller) signs a data-processing agreement covering Tuya, checks where data is processed, and documents it. Room-control data (lights on/off, DND, wake-up times, temperature) can reveal guest presence and habits, which is personal data under GDPR. If the DPO refuses: ship the Tuya-free variant.
- **Outputs:** 2–4 relay channels (or commands to existing room controllers), thermostat setpoint via its local interface (Modbus/0–10 V/Matter, depending on the installed thermostat), DND/MUR (make-up room) indicator at the door (wired or wireless).
- **Power:** Hi-Link HLK-10Mxx isolated AC-DC (10 W, 85–265 VAC, 3000 VAC isolation) for wall/bedside installation.
- **UX:** big tactile buttons with Braille/tactile markers; a voice "help" command lists what you can say; audio confirmation; night-light; hardware mute.

**Pricing (estimates):** €149 per room (panel), installation via the hotel's electrician or a partner (€50–100/room), optional dashboard €1/room/month. Accessible-room pack (panel + door indicator + vibrating alarm option) €249.

### Unit economics (estimates per panel, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (T3-V-PRO or ASR + MCU, mic array (2 mics), speaker + amp, relays, buttons, LEDs, AC-DC module, PCB) | €26.00 | €20.00 |
| Assembly & test (voice test in a quiet booth, relay test, hi-pot) | €3.50 | €2.40 |
| Enclosure (wall/bedside, hotel-grade finish, wipeable) | €6.00 | €4.00 |
| Packaging (bulk, 10 per carton) | €0.80 | €0.50 |
| Freight + duty to EU | €1.20 | €0.80 |
| Certification amortised (~€30k) | €30.00 | €6.00 |
| **Landed cost** | **€67.50** | **€33.70** |
| Net revenue (direct €149; via integrator €110) | €149 | €110 |
| **Gross margin** | **€81.50 (55%)** | **€76.30 (69%)** |

### Go-to-market
**First 100 customers (≈ 5–10 hotels):**
- **One paid pilot hotel per segment:** a boutique hotel, a holiday park, an accessible-room project. Install 10–20 panels each; collect guest feedback and DPO sign-off letters.
- **Hospitality trade fairs and hotel-renovation fairs**; hotel-tech communities and boutique-hotel associations.
- **Electrical installers who specialise in hotels**: they are in every renovation and recommend what they can install easily.
- **Accessibility organisations** and accessible-travel platforms: a listing as "accessible room technology" is valuable marketing for hotels.

**Scale:** hotel-renovation integrators, furniture/headboard makers (panel built into the headboard!), holiday-park groups.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: voice accuracy offline in DE/EN/NL/FR in a real hotel room (AC + TV noise); DPO review of both variants with 2 hotels |
| Q2 | Works-like panels in 1 pilot hotel (20 rooms); guest survey; installation guide |
| Q3 | EVT/DVT; LVD/EMC/RED testing; holiday-park pilot; accessibility pilot |
| Q4 | 1,000 panels; 1 integrator partner; headboard-maker partnership |

**Team:** founder with hospitality sales background, 1 embedded engineer (voice chip tuning, relays, mains), 1 part-time installer/field engineer, part-time software for the dashboard (if Tuya-free).

**Funding to the first 1,000 panels (estimates):** NRE €70k (hardware €25k, voice-command packs + firmware €25k, enclosure tooling €20k) + certification €30k + 1,000 panels landed ~€35k + pilot installs €15k + 9 months lean costs €60k ≈ **€210k**. Minus paid pilots (50 rooms × €200 ≈ €10k) and hospitality/accessibility innovation grants where available → **~€150–190k** from founders/angel.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** offline ASR accuracy with accents, AC noise, TV on, across 4 languages | Kill test in a real room; fixed short commands; wake word + button fallback; language support verified with the chip vendor |
| **Technical:** integration with existing thermostats and room controllers varies hotel by hotel | Start with relays + a few common thermostat interfaces; survey each hotel before quoting |
| **Privacy/GDPR (Tuya variant):** cloud dependency for dashboard; data residency; DPA chain | Offer Tuya-free variant; for Tuya: DPA, data-location check, minimal data (no audio ever), guest notice in the room |
| **Trust:** "is it listening?" | Hardware mute switch that physically cuts the mic, visible LED, card on the nightstand explaining "no recording, nothing leaves this panel" — and make sure firmware audit backs it up |
| **Regulatory:** mains installation in rooms | Electrician installation; LVD testing; low-voltage variant powered from the existing room controller where possible |
| **Market:** hotels think "nice-to-have" | Sell to accessible rooms + boutique "wow" first; measure review mentions and complaints |
| **Supply:** Tuya module sole source; voice-chip vendor language packs | Keep the M5Stack/own-MCU variant alive; ask for long-term availability letters |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Tuya T3-V-PRO Wi-Fi + BLE module | https://www.gongbans.com/db/tuya-t3-v-pro.html | Wi-Fi 6/BLE + offline voice chip (CI1302), mic/speaker pins | **Datasheet public, files via maker** (no open schematic/PCB) | Tuya platform terms; cloud dependency for remote features |
| M5Stack Unit ASR (U194) | https://www.gongbans.com/db/m5stack-unit-asr.html | Offline ASR unit for the Tuya-free prototype | Enclosure/structure files only — main-board electronics not published | Prototype; production design via the chip vendor |
| Hi-Link HLK-10Mxx 10 W isolated AC-DC | https://www.gongbans.com/db/hilink-10mxx.html | Mains supply for wall/bedside install | **Datasheet public, files via maker** | Commercial module; check its safety approvals |

### Block diagram
```
                [2 mics] -> [offline voice chip (CI1302 in T3-V-PRO, or ASR unit)] --> recognised command ID (no audio stored)
                                         |
[big buttons + tactile marks] ---> [MCU / T3] --GPIO--> [relays: lights, curtains]
       [hardware mute: cuts mic power] ->  |--RS485/0-10V/local--> [thermostat]
                                           |--> [door DND/MUR indicator]
                                           |--> [speaker: confirmation, wake-up alarm]
                                           ~~Wi-Fi~~> Tuya cloud dashboard (Tuya variant)  |  local server / own EU cloud (Tuya-free)
                [230 VAC] -> [HLK-10Mxx] -> 5 V / 3.3 V
```
**Engineering gap:** command packs per language (and testing them), the mic front-end (placement, noise), relay/mains design, thermostat integration options, the hotel dashboard (or on-premise server) and a robust installation concept. The voice chip and modules are off the shelf.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Tuya T3-V-PRO (or ASR chip + own MCU) | €5–8 | **Sole-source per variant**; verify language packs |
| 2 MEMS mics + speaker + class-D amp | €2.50 | Mic placement matters more than mic price |
| 2–4 relays (10 A) + drivers | €3.00 | |
| Buttons (large, tactile), LEDs, night-light | €2.50 | |
| HLK-10Mxx | €3.00 | Or a smaller supply if the load allows |
| PCB, terminals, fuse, varistor | €3.00 | |
| Enclosure | €6.00 | Tooling ~€15k |

### Firmware/software starting point
- **Tuya variant:** Tuya developer platform documentation for the T3 series and the voice-module SDK (Tuya developer account needed); custom command words are configured via the vendor's tools — confirm the process for EN/DE/NL/FR.
- **Offline voice chip:** Chipintelli provides tooling for custom wake words/commands; search "Chipintelli CI1302 SDK" and ask the module vendor for the language-pack process.
- **Tuya-free control plane:** search "Home Assistant" (open source) as an on-premise server for pilots, or a small MQTT broker (search "Eclipse Mosquitto").
- **Thermostats:** depends on site — Modbus RTU libraries (search "libmodbus"), or Matter where installed.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill test:** dev-kit panel in a real hotel room; 20 speakers (4 languages) × 10 commands with AC + TV running: ≥90% correct, ≤1 false wake per night. Packet capture confirms **no audio leaves the device**. 2 hotel DPOs give written feedback on Tuya vs Tuya-free |
| 3–5 | Works-like | Relays + thermostat + DND + wake-up working in 3 rooms; guest-mode reset at checkout |
| 6–8 | Looks-like + EVT | Hotel-grade enclosure, 20 panels in a pilot hotel; housekeeping can clean it; tactile/Braille marks reviewed by low-vision testers |
| 9–10 | DVT + pre-compliance | LVD/EMC/RED pre-scan, EN 18031 gap analysis (Tuya variant), firmware audit of the "no audio" claim |
| 11–12 | Pilot batch | 50 panels in 2–3 hotels; ≥70% of guests used voice at least once; no privacy complaints; hotel buys or extends |

### Certification checklist (EU)
- **LVD:** EN 62368-1 (mains-powered audio/IT equipment), plus relay switching of room circuits — check EN 60669-2-1 if it acts as an electronic switch in fixed installation. Est. **€8–15k**.
- **EMC:** EN 55032/55035 or EN 55014, EN 61000-3-2/-3-3. **RED:** EN 300 328, EN 301 489-1/-17, EN 62311. Est. **€8–12k**.
- **RED delegated act (EN 18031-1/-2):** Wi-Fi + microphone → internet-connected and processes personal data; mandatory since 1 Aug 2025. Est. €5–10k.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: secure updates (Tuya OTA or your own), SBOM, vulnerability handling.
- **GDPR:** hotel = controller. No audio stored or transmitted (prove it); room events = personal data; DPA with Tuya on the Tuya variant; data location; retention (clear at checkout); guest information card.
- **Accessibility:** tactile markings; consider EN 301 549 for any guest-facing app/web; accessible-room standards vary by country.
- **RoHS, REACH, WEEE**, packaging registration.
- **Total estimate: €25–40k.**

### Validation toolkit
- **Kill question:** Does the voice path stay offline in practice, and will a hotel's DPO sign off the Tuya cloud dependency for the dashboard? If either fails, ship only the offline variant.
- **Cheapest experiment (~€600):** T3-V-PRO and ASR dev units with a relay board and a lamp in a borrowed hotel room for one day; 20 staff/guests test commands; Wi-Fi packet capture during testing.
- **5-question interview (hotel owner/ops):** 1) What do guests complain about in rooms (lights, temperature, noise)? 2) Have you considered voice control? What stopped you? 3) Who must approve a device with a microphone (DPO, owner, brand)? 4) What room control exists today (switches, GRMS, thermostats)? 5) At €149 per room + installation, would you pilot 10 rooms this season?
- **Landing page headline:** "Voice control for hotel rooms — without a cloud microphone." Bullets: "Guests say 'lights off' or 'wake me at seven'. Speech is recognised inside the panel; nothing is recorded." / "Big buttons for everything, hardware mute, tactile markings for accessible rooms." / "Retrofits into existing rooms in under an hour."
- **Pass threshold:** 2 paid pilots (≥10 rooms each) + one DPO approval letter.

### First production checklist
- **Samples:** module samples with the production command packs; mic samples tested in the final enclosure.
- **Golden sample:** with command-pack version, mic gain settings, enclosure finish approved by a pilot hotel.
- **DFM review:** acoustic ports (mic + speaker), cleanability (no gaps for dust), button feel, mains creepage/clearance, mounting to standard wall boxes.
- **MOQ talk:** Tuya module MOQ, custom command-pack fee (if any), enclosure colours (hotels want options — limit to 2).
- **QC/AQL:** AQL II 1.0/2.5; 100% voice test (recorded command playback in a test box), 100% relay and hi-pot test, mute-switch test (mic must be dead).
- **Packaging:** bulk cartons per floor, labels with room numbers optional, installer guide, guest card.
- **Incoterms:** FOB Shenzhen; DAP to the integrator for project deliveries.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Tuya Smart (涂鸦智能) and M5Stack and Hi-Link (海凌科)).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Tuya Smart (涂鸦智能)** (涂鸦智能模组部门, developer.tuya.com) — platform + module maker; 151 boards in the catalogue; files via Tuya Smart public module documentation · https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber. Directory entry: WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. Listed from Tuya's public developer documentation; Tuya is not affiliated with GONGBANS. Tuya modules can also be ordered through the Tuya developer platform, which covers the app and cloud side. Boards used here: [Tuya T3-V-PRO Wi-Fi + Bluetooth LE module](/db/tuya-t3-v-pro.html) (Wi-Fi 6 module with offline voice-recognition chip). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit ASR (U194)](/db/m5stack-unit-asr.html) (alternative offline ASR unit for a non-Tuya variant). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package)](/db/hilink-10mxx.html) (isolated AC-DC supply for a wall/bedside install). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Matter / Tuya smart-home modules and app platform)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Tuya Smart (涂鸦智能) and M5Stack and Hi-Link (海凌科) websites)

```email
Subject: Sample order and volume pricing — Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package) — for a Hotel Room Voice Panel (offline)

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Hotel Room Voice Panel (offline): A bedside panel guests can talk to — 'lights off', 'warmer', 'do not disturb', 'wake me at seven' — recognised on the device, nothing recorded, with a big physical button for everything too. The design is built around your Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package).

Could you please send:
1. Price and lead time for [10] sample units of each: Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package).
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
主题：样品订购及批量报价 — Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package) — 用于Hotel Room Voice Panel (offline)

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hotel Room Voice Panel (offline)：A bedside panel guests can talk to — 'lights off', 'warmer', 'do not disturb', 'wake me at seven' — recognised on the device, nothing recorded, with a big physical button for everything too。产品设计基于贵司的Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package)。

请提供以下信息：
1. 各[10]片样品的单价和交期：Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package)。
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
Subject: PCBA quote from open design files — Hotel Room Voice Panel (offline), [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Hotel Room Voice Panel (offline): A bedside panel guests can talk to — 'lights off', 'warmer', 'do not disturb', 'wake me at seven' — recognised on the device, nothing recorded, with a big physical button for everything too. The design starts from published open-hardware files (Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Hotel Room Voice Panel (offline)，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Hotel Room Voice Panel (offline)：A bedside panel guests can talk to — 'lights off', 'warmer', 'do not disturb', 'wake me at seven' — recognised on the device, nothing recorded, with a big physical button for everything too。设计基于已公开的开源硬件文件（Tuya T3-V-PRO Wi-Fi + Bluetooth LE module, M5Stack Unit ASR (U194), HLK-10Mxx 10W AC-DC isolated power module, incl. 10W-B, 10W-C and 10W-T (5W package)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order a T3-V-PRO sample and an M5Stack Unit ASR; ask both vendors which languages and how many custom commands are supported.
2. Ask two boutique hotels for one room for a day of testing and a 20-minute chat with their DPO.
3. Write the one-page data-flow sheet (voice offline; what goes to the cloud on the Tuya variant; what goes nowhere on the Tuya-free variant).

Want help sourcing or building this? Talk to us via www.gongbans.com.
