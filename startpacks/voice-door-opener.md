# Offline Voice Door Opener — Founder Start Pack

> A small box that lets a wheelchair user open their powered front door, gate or garage-style door by saying a personal command, recognised offline. It triggers the door drive's existing push-button input or its fixed-code 433/868 MHz receiver.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Powered door operators are installed in many homes under home-adaptation schemes, but the user still has to find and press a remote or reach a wall button. For people with limited arm strength or hand function, that last step is the barrier. The voice options that exist today run through cloud assistants: they fail when the internet is down, need an account and a smartphone, and send audio to a cloud.
- **Customer:** Wheelchair users and people with limited arm/hand function (the users); **housing-adaptation contractors, door-operator installers and occupational therapists** (who specify and install); municipal and insurer home-adaptation schemes and the users themselves (who pay).
- **Product:** A wall- or wheelchair-mountable box with an offline speech-recognition unit (M5Stack Unit ASR class), a two-step command (wake word + personal phrase), LED and voice feedback, and two outputs: a dry-contact relay wired to the door drive's push-button input (universal), and a HopeRF CMT2119B sub-GHz transmitter for drives with fixed-code 433/868 MHz receivers. No cloud, no app required.
- **Why now:** Offline speech-recognition modules are now cheap and good enough for a few fixed commands. Home-adaptation budgets exist (for example, German long-term-care insurance funds home-adaptation measures), and installers want simple add-ons they can fit in an hour.
- **The ask:** About €80–110k (estimate) to the first 1,000 units, plus a clear regulatory decision up front (see MDR below). Route: installer partners + grants for accessibility innovation; small angel.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do housing-adaptation contractors in 2 municipalities agree to offer it as an add-on, and does recognition work for users with dysarthric speech? Test both early.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Wheelchair users and people with limited arm strength, housing adaptation contractors, municipal home-adaptation schemes.

**The problem as the pack states it:** Powered door operators are installed in many homes under home-adaptation schemes, but the user still has to find and press a remote or reach a wall button. For people with limited arm strength or hand function, that last step is the barrier. The voice options that exist today run through cloud assistants: they fail when the internet is down, need an account and a smartphone, and send audio to a cloud.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/wheelchairs** · https://www.reddit.com/r/wheelchairs/ — wheelchair users; ask, do not pitch.
- **r/disability** · https://www.reddit.com/r/disability/ — disabled users and carers.
- **r/OccupationalTherapy** · https://www.reddit.com/r/OccupationalTherapy/ — occupational therapists, the people who recommend assistive devices.
- **AbilityNet (UK)** · https://abilitynet.org.uk/ — assistive technology charity.
- **DVE, Deutscher Verband Ergotherapie (DE)** · https://www.dve.info/ — German occupational-therapy association.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149–199 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how wheelchair users and people with limited arm strength, housing adaptation contractors, municipal home-adaptation schemes deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you get through your front door or gate today when you come home, and what happens on the days when your hands or arms are not up to it?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A small box that lets a wheelchair user open their powered front door, gate or garage-style door by saying a personal command — recognised offline — by triggering the door drive's existing input or fixed-code 433 MHz receiver. On a scale of one to ten, how likely would you be to buy that at €149–199 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Offline Voice Door Opener: would you pay €149–199 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Offline Voice Door Opener: A small box that lets a wheelchair user open their powered front door, gate or garage-style door by saying a personal command — recognised offline — by triggering the door drive's existing input or fixed-code 433 MHz receiver. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149–199 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
The user is clear: someone who can speak reliably but can't comfortably press a button at the right moment, approaching their own front door, garage or garden gate. The **buyer is often not the user**: the installer quotes it as part of a door-operator job, the occupational therapist recommends it, and a care insurer, municipality or the user's own budget pays.

So sell to **installers of powered door operators and housing-adaptation contractors** first. They already visit the home, wire the operator, and can connect a dry contact in 20 minutes. One installer does 50–200 accessible door jobs a year.

### Market size (estimates)
- People using wheelchairs in the EU: commonly estimated at roughly 1% of the population → **~4.5 M**. Assume 10% live in homes with a powered door/gate operator or will get one via adaptation in 5 years → **450,000**; add people with limited hand function (MS, ALS, high spinal cord injury, rheumatoid arthritis, stroke) using powered doors → say **600,000 potential users**.
- **TAM:** 600,000 × €179 ≈ **€107 M** (one-off).
- **SAM:** DE, NL, BE, AT, Nordics (strong home-adaptation funding) + UK: ~35% → **~€37 M**.
- **SOM (3 years):** 1.5% of SAM via 30–50 installer partners → **~3,000 units ≈ €0.55 M**. Small, worthwhile, and it opens the door (sorry) to a broader offline voice-control product for accessible homes.

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| Cloud voice assistant + smart relay wired to the door controller (a common DIY/installer workaround) | €30–150 | Internet + cloud account + phone needed; audio goes to the cloud; fails offline; opens on anyone's voice |
| Residential door-opener systems with voice options (a few US-centric products for quadriplegic users) | €1,000s installed | Expensive, region-specific, voice path often via cloud assistants |
| Environmental control units (ECUs) for severely disabled users (switch scanning, infrared, voice; often sold as assistive/medical devices) | €1,000–5,000 | Overkill for one door; prescription process |
| Wheelchair-armrest remote button / large-button remotes | €20–100 | Still needs reliable hand function |
| Proximity transponder (door opens when tag is near) | €200–600 | Opens for whoever holds the tag; can open unintentionally when passing |
| Do nothing / carer opens the door | Free | Independence |

**Wedge:** **offline** (works with no internet, no account, no phone), **personal two-step command** (fewer accidental openings than "open door"), installs on the existing drive's button input in minutes, and an installer price that fits inside an adaptation quote.

### Product & value proposition
- **Recognition:** offline ASR unit (M5Stack Unit ASR class, a fixed-command speech module) recognising a wake word + one of a few command phrases. **Key limitation:** off-the-shelf offline command modules recognise *predefined* phrases, typically tuned for typical speech. Users with dysarthric (slurred) speech may get poor accuracy. A personal, user-trained model may need a different engine (e.g. Espressif's ESP-SR on an ESP32-S3, or a small on-device keyword-spotting model trained on the user's own recordings). Test this in weeks 1–2; it decides the product.
- **Outputs:** (1) relay dry contact (Seeed Grove-Relay as the prototype reference) wired in parallel with the door drive's push-button input, the universal and safest method; (2) CMT2119B sub-GHz transmitter (127–1020 MHz, up to +20 dBm, OOK/FSK, per HopeRF) to replay **fixed-code** remote frames for drives that only have a radio receiver. Rolling-code receivers (most modern garage and gate drives) can't be triggered by a cloned code; for those, use the drive's wired input or an extra receiver input.
- **Feedback:** LED ring + short voice/beep confirmation ("opening"), error tone on rejected commands.
- **Security:** voice is not authentication. Optional spoken PIN phrase; command only accepted within N metres (mic sensitivity); lockout after repeated failures; "night lock" schedule. Disclose clearly: anyone who knows the phrase and sounds close enough may open the door.
- **Power:** mains adapter (USB-C) for the wall version; a wheelchair-mounted version runs from the chair's USB port or a small battery.

**Pricing (estimates):** €179 RRP; installer price €125; installation 30–60 min (installer's line item).

### MDR: decide this before anything else
Under the EU Medical Device Regulation (2017/745), a product intended for the **"alleviation of, or compensation for, a disability"** can be a medical device. Marketing this as "a door opener for wheelchair users" may make it one (likely Class I, self-declared, but with technical documentation, risk management, a person responsible for regulatory compliance, post-market surveillance and EUDAMED registration).

Two clean options:
1. **General-purpose product:** "offline voice control for powered doors and gates", designed accessibly, marketed to everyone (hands full with shopping, elderly users, convenience). No medical/disability-compensation intended purpose in the labelling, instructions or marketing. Cheaper and faster, but you can't make disability claims, and some funding schemes may want a medical device.
2. **Class I medical device:** intended purpose explicitly for people with disabilities. More work (budget €15–30k for documentation, consultant support and processes), but it can unlock listings in assistive-device catalogues and insurer reimbursement in some countries.

**Recommendation:** start with option 1 to validate the product and recognition quality; move to option 2 once you see installers and insurers asking for it. Get a one-hour MDR consultant opinion on your exact wording either way. This pack makes **no medical claims**.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (offline ASR module, MCU, CMT2119B + matching, relay, mic, speaker, LED ring, USB-C PSU, PCB) | €21.00 | €16.50 |
| Assembly & test (recognition test with recorded phrases, relay, RF output) | €2.50 | €1.80 |
| Enclosure (wall box + optional wheelchair clamp) | €2.50 | €1.50 |
| Packaging + installer manual | €1.20 | €0.80 |
| Freight + duty to EU | €1.00 | €0.70 |
| Certification amortised (~€18k: RED sub-GHz, EMC, safety, EN 18031 not needed if not internet-connected) | €18.00 | €3.60 |
| **Landed cost** | **€46.20** | **€24.90** |
| Net price ex-VAT: installer €105 (from €125 incl. VAT) / direct €150 | €105 / €150 | €105 / €150 |
| **Gross margin** | **€59 (56%) installer / €104 (69%) direct** | **€80 (76%) / €125 (83%)** |

If you go the MDR Class I route, add ~€15–30k one-off and ongoing QMS/vigilance costs (≈ €10–20/unit at 1k).

### Go-to-market
**First 100 customers:**
- **Door-operator installers and accessibility contractors** in one region: demo kit, installer price, 3 free units for their next jobs.
- **Occupational therapists and home-adaptation advisers** (municipal and charity advice centres): they decide what gets recommended.
- **Disability user communities and peer networks** (spinal-cord-injury associations, MS societies, wheelchair-user forums): co-design and beta testers, not just customers. Pay testers for their time.
- **Accessibility trade fairs** (rehab and care fairs in DE/NL/Nordics).

**Scale channels:** door-operator manufacturers (bundle as an accessory), assistive-tech dealers, insurer/municipal approved-product lists (may require the MDR route).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill questions: recognition test with 15 users incl. 5 with dysarthric speech; 2 installer/contractor partners in 2 municipalities agree to offer it; MDR opinion |
| Q2 | Works-like with relay + RF on 3 real door drives; engine decision (fixed-command module vs user-trained KWS); EVT 20 units with paid beta users |
| Q3 | DVT; RED/EMC/safety testing; installer manual; first 100 units through partners |
| Q4 | 500–1,000 units; door-operator maker accessory talks; MDR Class I decision based on funding-route demand |

**Team:** founder (installer channel + user community), 1 embedded/audio engineer (speech engine, RF, low-noise mic design), part-time accessibility/OT adviser (paid), part-time regulatory consultant (MDR question).

**Funding to the first 1,000 units (estimates):** NRE €40k (electronics €10k, speech engine work €15k, RF/relay + installer kit €5k, enclosure €10k) + certification €18k + 1,000 units landed ex-cert ~€28k + user-testing budget €5k + 9 months lean costs €25k ≈ **€116k**; minus installer pre-orders (~€15k) → **~€100k**. Route: accessibility/social-innovation grants and foundations (many fund assistive tech pilots), installer pre-orders, a small angel. If MDR route: +€15–30k.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: recognition for dysarthric or quiet speech; noise outdoors** | Test early with real users; user-trained engine option; directional mic; push-to-talk alternative (sip/puff or big button input) as fallback |
| **Safety: unintended opening (TV, other people, mis-recognition)** | Two-step command, optional PIN phrase, confidence threshold, night lock, event log on the device |
| **Safety: door/gate movement hazards** | The box only replaces a push button; the operator's safety sensors and its EN 16005 / EN 12453 compliance stay with the door; installer checklist |
| **Security: voice is not authentication; RF replay of fixed codes** | Disclose; recommend wired input; fixed-code RF only where the drive already uses fixed codes (it's already insecure, don't make it worse) |
| **Regulatory: MDR classification** | Decide intended purpose deliberately; consultant review of all marketing text |
| **Market: small, slow funding processes** | Installer channel; general-purpose positioning widens the market |
| **Supply: ASR module from one maker** | Keep the audio front end generic; ESP32-S3 + ESP-SR as second engine |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit ASR (U194) | https://www.gongbans.com/db/m5stack-unit-asr.html | Offline speech-recognition unit for the works-like prototype | Enclosure/structure files only (main-board electronics not published) | Dev unit; check the ASR module's command-word customisation process and licence with the maker |
| HopeRF CMT2119B high-power sub-GHz transmitter | https://www.gongbans.com/db/hoperf-cmt2119b.html · [GitHub folder](https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio/tree/main/Sub-1GHz/CMT2119B) | 433/868 MHz OOK/FSK transmit (127–1020 MHz, up to +20 dBm, 64-byte FIFO, packet handler, per HopeRF) to trigger fixed-code door receivers | Schematic, PCB layout, datasheet | MIT (HopeRF repo); datasheet marked preliminary |
| Seeed Grove-Relay | https://www.gongbans.com/db/seeed-grove-relay.html | Dry-contact relay reference for the door drive's push-button input | Schematic | Seeed open hardware licence; check before copying |

### Block diagram
```
[MEMS mic(s)] --> [offline ASR module  OR  ESP32-S3 + on-device KWS]
                         | wake word -> personal phrase (+ optional PIN phrase), confidence threshold
                         v
                    [MCU: command logic, lockout, night lock, event log]
                         |--> [relay, dry contact] ---- wired in parallel ----> [door drive push-button input]
                         |--> [CMT2119B 433/868 MHz TX] ~~ fixed-code frame ~~> [door drive radio receiver]
                         `--> [LED ring + speaker: "opening" / error tone]
[USB-C 5 V adapter or wheelchair USB]
```
**Engineering gap:** choosing and tuning the speech engine for real users (including atypical speech), the two-step command logic with false-accept/false-reject trade-off, the RF learn-and-replay function for fixed-code remotes (learn from the user's existing remote with a receiver; the CMT2119B only transmits), a robust installer wiring kit, and the accessibility of set-up itself (set-up by the installer or carer, not requiring fine motor skills).

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| Offline ASR module (fixed-command class) or ESP32-S3 module (8 MB PSRAM for ESP-SR) | €3–5 | Engine decision in weeks 1–2 |
| MEMS microphones ×2 + front-end | €1.20 | Two mics help with noise |
| CMT2119B + crystal + matching + SAW | €1.50 | Sole source (HopeRF) |
| Sub-GHz receiver for code learning (e.g. a CMT22xx receiver) | €1.00 | Only needed for RF learn |
| Relay (low-voltage dry contact) + terminals | €1.20 | |
| Small speaker + amp, LED ring | €2.50 | |
| MCU (if ASR module needs a host), PCB, passives | €2.50 | |
| USB-C 5 V adapter | €2.50 | Pre-certified adapter |

### Firmware/software starting point
- **Offline speech:** Espressif ESP-SR (WakeNet + MultiNet, on ESP32-S3; check supported languages for German/Dutch/Nordic commands); the ASR unit maker's command-word configuration process for the M5Stack Unit ASR (search M5Stack docs for "Unit ASR"). For user-trained keyword spotting, search "TinyML keyword spotting ESP32" and the open-source tooling around it.
- **RF:** HopeRF CMT2119B demo/layout files in the GitHub folder; HopeRF's RFPDK register tool (search HopeRF's site); fixed-code timings: search "EV1527 PT2262 timing" (and see rtl_433 as a GPL-licensed protocol reference).
- **No cloud, no app** in v1. Set-up via buttons + voice prompts; optional BLE set-up app later.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill questions:** (a) recognition test with 15 paid testers, 5 with dysarthric speech, at a real door with background noise. Pass: ≥95% correct acceptance for typical speech, ≥85% for atypical speech with the chosen engine, ≤1 false acceptance per 24 h of TV/household audio. (b) 2 installers/contractors in 2 municipalities agree to offer it |
| 3–5 | Works-like | Devkit box on 3 real door drives (1 wired input, 1 fixed-code radio, 1 gate); end-to-end open in <1.5 s after the phrase |
| 6–8 | Looks-like + EVT | Custom PCB + wall enclosure + wheelchair clamp; 15 EVT units with beta users at home for 3 weeks; diary of every failure |
| 9–10 | DVT + pre-compliance | RED pre-scan (EN 300 220 at 433/868 MHz), EMC, safety; installer manual tested by an installer who wasn't involved; MDR intended-purpose wording frozen |
| 11–12 | Pilot batch | 30–50 units installed through 2 installer partners; user satisfaction ≥8/10; no unintended openings reported |

### Certification checklist (EU)
- **CE under RED:** sub-GHz SRD transmitter (EN 300 220-1/-2; 433.05–434.79 MHz or 868 MHz sub-bands with power/duty-cycle limits per ERC Rec 70-03), EMC (EN 301 489-1/-3), safety EN 62368-1, RF exposure. Est. **€6–10k**.
- **RED delegated act cybersecurity (EN 18031):** applies to internet-connected radio equipment; an offline device with no internet connection is likely out of scope; if you add Wi-Fi/app later, EN 18031-1 (and -2 for personal data) applies. Confirm with your test lab.
- **CRA:** applies to products with digital elements; even offline, plan for vulnerability handling and firmware updates (reporting from 11 Sept 2026, full from 11 Dec 2027).
- **MDR (2017/745):** see the MDR section above. If the intended purpose is compensation for a disability, it's a medical device (likely Class I): technical documentation, risk management (EN ISO 14971), usability engineering (EN 62366-1), PRRC, EUDAMED, post-market surveillance. Budget **€15–30k** if chosen. Otherwise: no medical or disability-compensation claims anywhere.
- **Door safety:** the door operator keeps its own conformity (EN 16005 for powered pedestrian doors, EN 12453 for gates/garage doors, Machinery rules). Your box replaces a push button; the installer must not bypass safety devices.
- **RoHS, REACH, WEEE, packaging registration.**
- **GDPR:** audio is processed locally and not stored; keep it that way and say so. If you log events, keep them on the device.
- **Total estimate: €8–12k (general-purpose route); €23–42k (with MDR Class I).**

### Validation toolkit
- **Kill question:** Do housing-adaptation contractors in 2 municipalities agree to offer it as an add-on, and does recognition work for users with dysarthric speech? Test both early.
- **Cheapest experiment (~€150 + tester fees):** an ESP32-S3 devkit running ESP-SR and an M5Stack Unit ASR side by side, a relay on a test door operator (or a lamp as stand-in), 15 testers each saying the commands 50 times in a noisy room. Measure accept/reject rates per engine.
- **5-question interview (user):**
  1. How do you open your front door/garage/gate today? What's hardest about it?
  2. When has the current way failed you (cold hands, bags, rain, remote out of reach)?
  3. Would you trust a voice command to open your door? What would make you not trust it?
  4. Do you use voice assistants today? Do they understand you reliably?
  5. Who would pay for this in your situation: you, your insurer/municipality, the installer's quote?
- **Interview (installer/contractor):** how many powered doors per year; how do users trigger them; would you fit a voice add-on; what price in your quote; what proof do funders need?
- **Landing-page headline:** "Open your door with your voice. No internet needed."
  - Your own command phrase, recognised on the device. Nothing goes to the cloud.
  - Works with the door or gate drive you already have.
  - Installed by your door installer in under an hour.
- **Pass threshold:** recognition targets met with at least one engine **and** 2 installer partners place a paid order for 10 units each.

### First production checklist
- **Samples:** recognition test on 20 production units with a recorded phrase set (mic tolerance matters); RF output and frequency test.
- **Golden sample:** unit with recorded acceptance rates, relay and RF function, firmware/model version.
- **DFM review:** mic port sealing and placement away from the speaker, relay terminals accessible for installers, enclosure for outdoor-adjacent mounting (IP rating if near the door outside), wheelchair clamp strength.
- **MOQ talk:** ASR module/ESP32-S3, CMT2119B, microphones (matched sensitivity), enclosure tooling.
- **QC/AQL:** AQL II 1.0/2.5; 100% recognition test with a reference recording in a quiet box, 100% relay and RF test.
- **Packaging:** box, wall mount + wheelchair clamp, installer wiring guide (wired input first), user card with the command set-up steps in large print.
- **Incoterms:** FCA Shenzhen; small air batches for the pilot.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and HopeRF (华普微) and Seeed Studio).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit ASR (U194)](/db/m5stack-unit-asr.html) (offline speech-recognition unit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **HopeRF (华普微)** (深圳市华普微电子股份有限公司, hoperf.com) — chip house; 122 boards in the catalogue; files via HopeRF Product Portfolio (GitHub, MIT) · https://github.com/HOPE-MICROELECTRONICS/Product_Portfolio. Directory entry: RF chip house + module maker: Sub-GHz transmitter/receiver/transceiver ICs (CMT2xxx) and RFM modules; LoRa modules (RFM9x, RFM6601); BLE SoCs + modules; Matter-over-Thread / Wi-Fi modules; digital isolators. HopeRF publishes datasheets and, for some products, schematic and PCB files in its public GitHub portfolio (MIT licence). Boards used here: [HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter](/db/hoperf-cmt2119b.html) (high-power (G)FSK/OOK transmitter to trigger 433/868 MHz door receivers (open schematic + PCB)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Relay](/db/seeed-grove-relay.html) (dry-contact output to the door drive's push-button input). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and HopeRF (华普微) and Seeed Studio websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay — for a Offline Voice Door Opener

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Offline Voice Door Opener: A small box that lets a wheelchair user open their powered front door, gate or garage-style door by saying a personal command — recognised offline — by triggering the door drive's existing input or fixed-code 433 MHz receiver. The design is built around your M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay.
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
主题：样品订购及批量报价 — M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay — 用于Offline Voice Door Opener

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Offline Voice Door Opener：A small box that lets a wheelchair user open their powered front door, gate or garage-style door by saying a personal command — recognised offline — by triggering the door drive's existing input or fixed-code 433 MHz receiver。产品设计基于贵司的M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay。
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
Subject: PCBA quote from open design files — Offline Voice Door Opener, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Offline Voice Door Opener: A small box that lets a wheelchair user open their powered front door, gate or garage-style door by saying a personal command — recognised offline — by triggering the door drive's existing input or fixed-code 433 MHz receiver. The design starts from published open-hardware files (M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Offline Voice Door Opener，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Offline Voice Door Opener：A small box that lets a wheelchair user open their powered front door, gate or garage-style door by saying a personal command — recognised offline — by triggering the door drive's existing input or fixed-code 433 MHz receiver。设计基于已公开的开源硬件文件（M5Stack Unit ASR (U194), HopeRF CMT2119B High-power (G)FSK/OOK/(G)MSK transmitter, Seeed Grove-Relay；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order an M5Stack Unit ASR, an ESP32-S3 devkit (for ESP-SR) and a relay; get "wake word + open" switching a lamp on the bench.
2. Contact a spinal-cord-injury or MS association to recruit 15 paid testers (5 with dysarthric speech) for the recognition test.
3. Book a one-hour MDR consultant call to decide the intended purpose wording before writing any marketing text.

Want help sourcing or building this? Talk to us via www.gongbans.com.
