# 433 MHz Legacy-to-Matter Bridge — Founder Start Pack

> A plug-in bridge that listens to and replays the 433 MHz signals of old remote sockets, doorbells, awnings and window sensors, so the radio gadgets a house already has show up in Matter. No rip-and-replace.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** European homes are full of cheap 433 MHz gear bought at DIY stores and discounters over 15 years: remote-controlled sockets, doorbells, awning and blind remotes, window contacts, weather stations. They work fine, but they're invisible to Apple Home, Google Home, Alexa, SmartThings and Home Assistant. People either live with three remotes in a drawer or throw working devices away.
- **Customer:** Households (DE, NL, AT, BE, FR, the Nordics) with a few of these devices who just bought a Matter-capable hub or speaker; home-automation hobbyists who want something cleaner than a hacked bridge. The person who sets up the home tech pays and uses it.
- **Product:** A small USB- or plug-powered bridge: a HopeRF CMT2300A sub-GHz transceiver (OOK/FSK, 433.92 MHz) plus an ESP32-C6 running a Matter Bridge over Wi-Fi (Thread-ready). Learn mode decodes common fixed-code protocols, and every learned device appears in Matter as an on/off plug, contact sensor or button. Local only, no cloud.
- **Why now:** Matter's bridge device type lets one box expose non-Matter devices as native accessories in every major ecosystem. Matter-capable hubs/speakers are now in many homes, and people want the old stuff to join in. Open HopeRF reference designs and Espressif's Matter SDK make this a firmware project, not a radio-research project.
- **The ask:** About €150k (estimate) to reach 1,000 units, including Matter certification. Route: crowdfunding pre-orders in DACH/NL home-automation communities, then distribution through electronics/smart-home retailers.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> What share of 433 MHz gear in a random sample of 30 homes is fixed-code and decodable? If under 60%, the 'works with what you have' promise fails.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Households with drawers of 433 MHz remote sockets and sensors (very common in DE/NL DIY stores); home-automation hobbyists.

**The problem as the pack states it:** European homes are full of cheap 433 MHz gear bought at DIY stores and discounters over 15 years: remote-controlled sockets, doorbells, awning and blind remotes, window contacts, weather stations. They work fine, but they're invisible to Apple Home, Google Home, Alexa, SmartThings and Home Assistant. People either live with three remotes in a drawer or throw working devices away.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/homeassistant** · https://www.reddit.com/r/homeassistant/ — the largest home-automation community; very receptive to new sensors and ESP32 devices.
- **Home Assistant Community forum** · https://community.home-assistant.io/ — where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers.
- **Tweakers forum (NL)** · https://gathering.tweakers.net/ — Dutch tech forum with active energy, domotica and smart-meter sections.
- **r/RTLSDR** · https://www.reddit.com/r/RTLSDR/ — software-defined-radio hobbyists; 433 MHz decoding with rtl_433 is common.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€39–55 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how households with drawers of 433 MHz remote sockets and sensors deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. Which old radio-controlled sockets, doorbells or awnings do you still have in the house, and what have you tried to get them into your home automation?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Plug-in bridge that listens to and replays the 433 MHz signals of old remote sockets, doorbells, awnings and window sensors so the house's existing cheap radio gadgets appear in Matter — no rip-and-replace. On a scale of one to ten, how likely would you be to buy that at €39–55 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: 433 MHz Legacy-to-Matter Bridge: would you pay €39–55 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a 433 MHz Legacy-to-Matter Bridge: Plug-in bridge that listens to and replays the 433 MHz signals of old remote sockets, doorbells, awnings and window sensors so the house's existing cheap radio gadgets appear in Matter — no rip-and-replace. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €39–55 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The core customer is the **"accidental smart-home owner"**: they have a smart speaker or a Matter hub and a handful of 433 MHz remote sockets (Christmas lights, a floor lamp, the aquarium pump), an awning remote and a doorbell. They don't want to buy €20 Matter plugs to replace sockets that work. They want "make what I have work" for under €50.

Second: **home-automation hobbyists** who already use DIY RF bridges with custom firmware and want a supported, Matter-native box they can recommend to their parents.

Positioning matters: this is a convenience product for **your own** fixed-code devices. It's deliberately not a security tool: rolling-code signals (garage doors, car keys, alarm systems) are detected and refused.

### Market size (estimates)
- Households in DE/NL/AT/BE/FR/Nordics with 433 MHz gear: assume 25% of ~100 M households → 25 M; of those, households with a Matter-capable controller and a reason to connect: ~10% → **~2.5 M**.
- **TAM:** 2.5 M × €45 ≈ **€110 M**.
- **SAM:** reachable through German/Dutch/English online channels and DIY/electronics retail, ~30% → **€34 M**.
- **SOM (3 years):** 2% of SAM → ~15,000 units → **~€680k**. Upside: retail listing at a DIY chain.

### Competition
| Alternative | Price (listings, estimate) | Weakness we attack |
|---|---|---|
| Wi-Fi 433 MHz bridges from smart-home brands (e.g. Sonoff RF Bridge R2, €11–25 at EU retailers) | €11–25 | Vendor app + cloud; Matter/HA only via community firmware hacks; limited protocol support |
| DIY gateways with open firmware (RFLink, ESP32 + receiver + custom firmware; RTL-SDR + rtl_433 + Home Assistant) | €20–60 + time | Works for hobbyists only; no Matter; no support |
| Premium multi-radio hubs with 433 MHz built in (e.g. Homey Pro class) | €300–400 | Great but expensive; a whole new platform |
| Replace every device with Matter plugs/sensors | €15–30 per device | Waste; awnings/blinds/doorbells aren't simple swaps |
| Do nothing (keep the remotes) | Free | Three remotes in a drawer, no automation |

**Wedge:** **Matter-native** (shows up in Apple/Google/Amazon/SmartThings/Home Assistant without hacks), **local-only**, a guided learn mode with a protocol library (point the remote, press, done), and €45. Plus a principled "no rolling codes, no code-grabbing" design that retailers and app stores won't object to.

### Product & value proposition
- **Radio:** HopeRF CMT2300A transceiver (127–1020 MHz, OOK/(G)FSK, up to +20 dBm, −121 dBm sensitivity at 2 kbps, per HopeRF), matched for 433.92 MHz; v2 adds an 868 MHz variant for the many 868 MHz home systems in DACH (check protocol openness first).
- **Host:** ESP32-C6 (Wi-Fi 6 + 802.15.4 Thread + BLE for Matter commissioning) running Espressif's Matter SDK with the bridge device type.
- **Learn mode:** the user presses "add device" in a small local web page or by pressing the bridge button. Pressing the original remote makes the bridge decode the protocol (EV1527/PT2262-class and other common fixed-code encoders) and propose the device type (socket = on/off, doorbell = button, window sensor = contact), which then appears in Matter.
- **Transmit:** sends the learned on/off frames for sockets, awnings and blinds. **Limitation, stated honestly:** most 433 MHz sockets don't report state, so the bridge assumes the state (and resyncs when someone uses the original remote, because the bridge hears that too).
- **Safety by design:** rolling-code/encrypted frames are classified and refused; no "capture any signal and replay" UI; transmit only on learned fixed codes; a TX duty-cycle limiter.

**Pricing (estimates):** €45 RRP (€39 early bird); 2-pack €79; a v2 dual-band (433 + 868) at €59. Retail channel at 35–40% off.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (ESP32-C6 module, CMT2300A + 433 matching/SAW, antenna, button, LED, USB-C, PCB) | €10.50 | €8.00 |
| Assembly & test (RF TX power/frequency + RX sensitivity, Matter DAC provisioning) | €2.20 | €1.50 |
| Enclosure (small plug/USB stick, 2-part) | €1.80 | €0.90 |
| Packaging (retail box with Matter QR code label) | €1.20 | €0.80 |
| Freight + duty to EU | €0.60 | €0.40 |
| Certification amortised (~€40k: RED 433 + Wi-Fi/BLE/802.15.4, EMC, EN 18031-1/-2, Matter certification + CSA membership share) | €40.00 | €8.00 |
| Matter device attestation certificates (per unit, estimate) | €0.20 | €0.10 |
| **Landed cost** | **€56.50** | **€19.70** |
| Net price after channel (1k: direct €38 ex-VAT / 5k: retail €23) | €38 | €23 |
| **Gross margin** | **−€18.50 (loss)** | **€3.30 (14%)** (direct sales at 5k: €18.30, 48%) |

**Read this table carefully:** at 1k units Matter certification makes each unit loss-making. Options: (a) sell the first 1,000 direct at €45–49 and accept the first batch as a certification investment; (b) launch v1 **without Matter certification** as a Home Assistant/ESPHome-native product (certification ~€12k instead of ~€40k), and certify Matter at 5k units; (c) use a white-label Matter-certified platform to share the costs. Most founders should pick (b).

### Go-to-market
**First 100 customers:**
- **German and Dutch home-automation forums and communities** (Home Assistant, ioBroker, openHAB, Homey). Post a "my 2009 remote sockets in Apple Home" video.
- **Tech YouTubers in DACH/NL** reviewing smart-home gear (send units, no paid placement at first).
- **Crowdfunding** (also the kill test), pitched at "make your old stuff smart".
- **Repair and sustainability communities:** "don't throw away working devices" fits the right-to-repair/anti-waste mood.

**Scale channels:** smart-home online shops, electronics retailers, DIY store chains (they sold the original 433 MHz sockets, so they can sell the bridge next to them), and bundling with 433 MHz socket sets as "Matter-ready".

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: decode survey of 30 homes; works-like bridge on the ESP32-C6 devkit + CMT-RF_EB; Matter bridge example running with 3 real sockets |
| Q2 | Custom PCB; protocol library v1 (top 10 fixed-code families); crowdfunding launch; EVT 50 units |
| Q3 | DVT; RED + EN 18031 testing; ship 500 to backers (Home Assistant/ESPHome-native, Matter beta via test certs) |
| Q4 | 1,000 units; decide Matter certification based on volume; retailer listing; 868 MHz research |

**Team:** 1 firmware engineer with ESP-IDF/Matter experience (essential), 1 RF/embedded engineer (part-time: CMT2300A front end, decoders), the founder on community/marketing and retail.

**Funding to the first 1,000 units (estimates):** NRE €45k (PCB/RF €10k, small enclosure tooling €6k, firmware Matter + decoders €29k) + certification €12k (path b) to €40k (with Matter) + 1,000 units landed ~€17k + 9 months lean costs €50k ≈ **€124–152k**. Subtract crowdfunding (600 × €39 ≈ €23k) → **~€100–130k**. Route: crowdfunding + founder savings or a small angel; no VC needed for v1.

### Top risks
| Risk | Mitigation |
|---|---|
| **Market: not enough decodable fixed-code gear in real homes** | The kill question: decode survey of 30 homes before building the product |
| **Technical:** assumed state for sockets; collisions with other 433 MHz traffic; range through walls | State the limitation; resync on hearing the original remote; repeat frames (as the remotes do); test TX range to 3 rooms |
| **Technical:** Matter bridge complexity (endpoints, commissioning, ecosystem quirks) | Start from Espressif's Matter bridge examples; test with 4 ecosystems weekly; recruit beta testers per ecosystem |
| **Regulatory:** "code-grabbing" perception; misuse | Rolling-code frames refused by design; transmit only learned fixed codes; no generic replay UI; document it in the DoC and the marketing |
| **Regulatory:** 433 MHz SRD limits (power, duty cycle) | Comply with ERC Rec 70-03 / EN 300 220 limits for 433.05–434.79 MHz; TX duty-cycle limiter in firmware |
| **Cost:** Matter certification and CSA membership | Path (b): launch HA/ESPHome-native, certify Matter when volume justifies it |
| **Supply:** CMT2300A single source | Footprint/firmware abstraction for an alternative OOK transceiver; 6-month chip stock |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| HopeRF CMT2300A transceiver | https://www.gongbans.com/db/hoperf-cmt2300a.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2300A) | 433.92 MHz OOK/FSK receive + transmit; +20 dBm max, −121 dBm, packet handler | schematic, PCB, demo code, datasheet | MIT (HopeRF repo) |
| HopeRF CMT-RF_EB evaluation board | https://www.gongbans.com/db/hoperf-cmt-rf-eb.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/Tools_Kit) | STM32 base + CMT23xx demo projects, RFPDK tool, app notes for 1527/1920 encoder pairs (the classic fixed-code remotes) | schematic, firmware | MIT |
| Espressif ESP32-C6-DevKitC-1 | https://www.gongbans.com/db/espressif-esp32-c6-devkitc-1.html | Matter host: Wi-Fi 6, Thread (802.15.4), BLE for commissioning | Reference design files (per catalogue) | Espressif docs CC BY-SA 4.0 / Apache-2.0; production on a pre-certified module |

### Block diagram
```
[433 MHz remote sockets, doorbells, awnings, window contacts]
          ~~ 433.92 MHz OOK ~~
               |
[antenna] -> [433 SAW / matching] -> [CMT2300A TX/RX] --SPI + DATA(GPIO)--> [ESP32-C6]
                                                                               |-- Matter Bridge (Wi-Fi; Thread-ready) --> [Apple/Google/Amazon/SmartThings/Home Assistant]
                                                                               |-- learn-mode web page / button + LED
[USB-C 5 V] -> [3.3 V LDO]                                                     `-- protocol library + "refuse rolling codes" classifier
```
**Engineering gap:** the radio reference design and the Matter SDK exist. What's missing: robust OOK decoding of real-world remotes (timing tolerance, noise), the protocol library and device-type mapping, the Matter bridge endpoint management (add/remove/rename learned devices), assumed-state handling, the rolling-code classifier, and a learn-mode UX non-technical people get through.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| ESP32-C6 module (pre-certified, 4–8 MB flash for Matter) | €2.80 | Matter needs flash; pick ≥4 MB |
| CMT2300A + crystal | €0.90 | **Sole-source (HopeRF)** |
| 433.92 MHz SAW filter + matching + RF switch | €0.90 | |
| Antenna (PCB or small wire) | €0.20 | |
| USB-C, LDO, button, LED, passives | €1.20 | |
| PCB 4-layer small | €0.80 | |
| Enclosure (plug-in stick) | €1.80 | Tooling ~€5–7k |

### Firmware/software starting point
- **Matter:** Espressif's esp-matter SDK (github.com/espressif/esp-matter) includes bridge examples; ESP-IDF for everything else.
- **Radio:** HopeRF CMT2300A demo code and the RFPDK register configurator (GitHub folders above).
- **Protocol references:** rtl_433 (github.com/merbanan/rtl_433) and RFLink document many 433 MHz protocols. Both are GPL, so use them as a reference or open-source your firmware accordingly. Search "rc-switch Arduino" for the classic fixed-code encoder timings.
- **Path (b) without Matter certification:** ship ESPHome-compatible firmware or a native Home Assistant integration first; keep Matter in beta.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** in a sample of 30 homes, what share of 433 MHz gear is fixed-code and decodable? Use a works-like receiver (ESP32 + CMT2300A demo board) at friends' homes and log every remote. Pass: ≥60% decodable |
| 3–5 | Works-like | ESP32-C6 + CMT-RF_EB running the esp-matter bridge example with 3 learned sockets, 1 doorbell, 1 window contact; controlled from 2 ecosystems; rolling-code classifier refusing 5 test garage remotes |
| 6–8 | Looks-like + EVT | Custom PCB in the plug enclosure; 50 EVT units to beta testers; learn-mode success ≥80% without help |
| 9–10 | DVT + pre-compliance | RED pre-scan (EN 300 220 at 433 MHz, EN 300 328 for 2.4 GHz), EMC; EN 18031-1/-2 gap analysis; signed OTA |
| 11–12 | Pilot batch | 50 sold units; support tickets/unit < 0.3; protocol library ≥10 families; Matter certification decision with real volume data |

### Certification checklist (EU)
- **CE under RED:** 433.05–434.79 MHz SRD (EN 300 220-1/-2, power and duty cycle per ERC Rec 70-03), 2.4 GHz Wi-Fi/BLE/802.15.4 (EN 300 328), EMC (EN 301 489-1/-3/-17), safety EN 62368-1 (USB powered; plug variant needs mains testing), exposure EN 62311/62479. Est. **€8–12k** (more for a mains plug variant).
- **RED delegated act cybersecurity: EN 18031-1 and EN 18031-2** (internet-connected home device; processes personal data such as presence via door contacts). Mandatory since 1 Aug 2025. Matter's security model helps (device attestation, PASE/CASE), but you still need the assessment. Est. **€8–15k**.
- **Matter certification (optional for v1):** CSA membership + an authorised test lab + product certification. Budget **€15–30k** in the first year (check current CSA fee schedules).
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027. Signed OTA, SBOM, vulnerability disclosure, a defined support period. Matter users expect updates.
- **RoHS, REACH, WEEE**, packaging registration.
- **GDPR:** local-only design keeps you out of most of it; if you ever add a cloud, door-contact events are personal data.
- **Product-safety messaging:** it must not be marketed for controlling safety-relevant equipment (heaters left on, alarm systems).
- **Total certification budget estimate: €16–27k without Matter certification; €31–57k with.**

### Validation toolkit
- **Kill question:** What share of 433 MHz gear in a random sample of 30 homes is fixed-code and decodable? If it's under 60%, the "works with what you have" promise fails.
- **Cheapest experiment (~€150):** an ESP32 + CMT2300A (or any OOK receiver) logging decoded frames on a laptop, carried to 30 homes (friends, a home-automation meetup "bring your remotes" night). Record brand, device type and decodable yes/no.
- **5-question interview (home owner):** 1) Which remote-controlled things do you have at home, and how old are they? 2) Do you use a smart speaker or hub, and which one? 3) What would you automate first if the old stuff worked with it? 4) Would you rather replace the devices or bridge them, and at what price? 5) €45 for a plug-in bridge: buy now?
- **Landing page headline:** "Your old remote sockets, now in Apple Home, Google and Alexa." Bullets: "Learns your 433 MHz sockets, doorbells, awnings and window sensors in seconds." / "Works locally through Matter. No cloud, no new app." / "Don't throw away things that work."
- **Pass threshold:** ≥60% decodable in the survey **and** 500 crowdfunding backers (or 300 deposits) in 6 weeks.

### First production checklist
- **Samples:** golden sample with TX power/frequency and RX sensitivity measured; Matter test certificate chain (or production DAC provisioning plan) verified.
- **DFM review:** antenna clearance in the small enclosure, USB-C strength, LED light pipe.
- **MOQ talk:** ESP32-C6 modules (flash size variant), CMT2300A reels, SAW filters (lead time).
- **QC/AQL:** AQL II 1.0/2.5; 100% RF test (TX + RX on a known 433 MHz frame), 100% Wi-Fi + commissioning test, 100% unique Matter onboarding QR label check against the provisioned device.
- **Packaging:** box with the Matter QR code (and a duplicate sticker for the manual), a "what works / what doesn't (rolling codes)" card.
- **Incoterms:** FOB Shenzhen; small air shipments for the crowdfunding batch, sea for retail.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (HopeRF (华普微) and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver](/db/hoperf-cmt2300a.html) (sub-GHz OOK/FSK transceiver (open schematic + PCB)); [HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003)](/db/hoperf-cmt-rf-eb.html) (evaluation base board with STM32 demo code for the CMT23xx radios). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c6-devkitc-1](/db/espressif-esp32-c6-devkitc-1.html) (Matter host (Wi-Fi 6 / Thread) running the bridge). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Tuya Smart** (涂鸦智能股份有限公司) · tuya.com — IoT platform + module solution house: WiFi/BT/Zigbee/BLE Mesh modules; 500+ product smart-home gongbans; global OEM APP. *(Smart-home modules and app platform)*
- **Tuya Smart Module** (涂鸦智能模组部门) · developer.tuya.com — WiFi/BT/Zigbee smart home modules: CBU / WBR3 / BT3L modules; Alexa/Google certified; volume IoT OEM. *(Smart-home modules and app platform)*
- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the HopeRF (华普微) and Espressif websites)

```email
Subject: Sample order and volume pricing — HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1 — for a 433 MHz Legacy-to-Matter Bridge

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a 433 MHz Legacy-to-Matter Bridge: Plug-in bridge that listens to and replays the 433 MHz signals of old remote sockets, doorbells, awnings and window sensors so the house's existing cheap radio gadgets appear in Matter — no rip-and-replace. The design is built around your HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1.

Could you please send:
1. Price and lead time for [10] sample units of each: HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1.
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
主题：样品订购及批量报价 — HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1 — 用于433 MHz Legacy-to-Matter Bridge

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款433 MHz Legacy-to-Matter Bridge：Plug-in bridge that listens to and replays the 433 MHz signals of old remote sockets, doorbells, awnings and window sensors so the house's existing cheap radio gadgets appear in Matter — no rip-and-replace。产品设计基于贵司的HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1。
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
Subject: PCBA quote from open design files — 433 MHz Legacy-to-Matter Bridge, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a 433 MHz Legacy-to-Matter Bridge: Plug-in bridge that listens to and replays the 433 MHz signals of old remote sockets, doorbells, awnings and window sensors so the house's existing cheap radio gadgets appear in Matter — no rip-and-replace. The design starts from published open-hardware files (HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — 433 MHz Legacy-to-Matter Bridge，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款433 MHz Legacy-to-Matter Bridge：Plug-in bridge that listens to and replays the 433 MHz signals of old remote sockets, doorbells, awnings and window sensors so the house's existing cheap radio gadgets appear in Matter — no rip-and-replace。设计基于已公开的开源硬件文件（HopeRF CMT2300A Ultra-low-power OOK/(G)FSK/(G)MSK transceiver, HopeRF CMT-RF_EB sub-GHz evaluation board (rev002/rev003), Espressif esp32-c6-devkitc-1；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order the HopeRF CMT-RF_EB kit (or CMT2300A samples) and an ESP32-C6-DevKitC-1; build and run the esp-matter bridge example with a dummy endpoint.
2. Run the 30-home decode survey: start with a "bring your remotes" evening at a local home-automation meetup.
3. Price both certification paths (HA/ESPHome-native first vs Matter-certified from day one) with a test lab and decide before the PCB.

Want help sourcing or building this? Talk to us via www.gongbans.com.
