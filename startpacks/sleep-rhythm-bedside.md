# Sleep Rhythm Bedside Radar — Founder Start Pack

> A bedside e-paper clock with a 60 GHz radar that shows last night's in-bed time, restlessness and breathing-rhythm trend: contactless, no wearable, no camera, nothing uploaded unless you choose.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

**Read this first:** this is a **wellness product**, not a medical device. It shows trends against the user's own baseline. It does not diagnose, monitor a disease, detect apnoea or measure heart conditions. The moment you claim any of that, the EU Medical Device Regulation (MDR 2017/745) applies and this plan stops being valid. See the certification section.

## 1. Summary

- **Problem:** Many people want to understand their sleep but won't wear a ring, watch or band to bed. They forget to charge it, it's uncomfortable, or (for older relatives) they won't wear it at all. Phone apps on the mattress are unreliable. Cameras in the bedroom are a no-go.
- **Customer:** Wellness-minded adults 40+ in DACH and the Nordics who have tried and dropped a wearable; adult children buying for an older parent who lives alone (they want a "did Mum sleep normally?" trend, not a medical alarm).
- **Product:** An e-paper bedside clock with a 60 GHz radar pointing at the upper body. In the morning it shows: time in bed, number of out-of-bed episodes, calm vs restless share and a breathing-rate band compared with the user's own 14-day baseline. No glowing screen at night. Data stays on the device by default; optional export or app.
- **Why now:** 60 GHz FMCW modules that report respiration and presence are now cheap off-the-shelf parts. E-paper ESP32 boards are mass-market. Privacy worries around cameras and cloud microphones make "radar, local, no camera" a selling point.
- **The ask:** About €200–250k (estimate) to the first 1,000 units. Fund it with a crowdfunding pre-order campaign plus one angel from consumer health/wellness retail.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does the module's breathing-rate trend agree with a reference chest belt within ±2 breaths/min for 20 sleepers, through a duvet? If not, the product is a fancy clock.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** People who won't wear a sleep tracker, older relatives, wellness-minded consumers in DACH/Nordics.

**The problem as the pack states it:** Many people want to understand their sleep but won't wear a ring, watch or band to bed. They forget to charge it, it's uncomfortable, or (for older relatives) they won't wear it at all. Phone apps on the mattress are unreliable. Cameras in the bedroom are a no-go.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/sleep** · https://www.reddit.com/r/sleep/ — people who sleep badly and talk about it.
- **r/AgingParents** · https://www.reddit.com/r/AgingParents/ — adult children caring for parents: the buyer for most elderly-care devices.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€119–159 (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how people who won't wear a sleep tracker, older relatives, wellness-minded consumers in DACH/Nordics deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you keep track of how you (or a relative) sleep today, and what made you stop using the last tracker or app you tried?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A bedside e-paper clock with a 60 GHz radar that shows last night's in-bed time, restlessness and breathing-rhythm trend — contactless, no wearable, no camera, nothing uploaded unless you choose. On a scale of one to ten, how likely would you be to buy that at €119–159 (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Sleep Rhythm Bedside Radar: would you pay €119–159 (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Sleep Rhythm Bedside Radar: A bedside e-paper clock with a 60 GHz radar that shows last night's in-bed time, restlessness and breathing-rhythm trend — contactless, no wearable, no camera, nothing uploaded unless you choose. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €119–159 (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Segment 1: **"wearable drop-outs"** — 40–65, own a smartwatch or had one, stopped wearing it at night. They buy for themselves, through Amazon, electronics retail and crowdfunding.

Segment 2: **adult children of independent older parents** in DE/AT/CH/NL/Nordics. The child pays, the parent uses it. The parent must accept it, which is easier for "a nice clock" than for a "monitor". This segment wants an optional, opt-in weekly summary on the child's phone. That is personal data about a third person: consent and design matter (see risks).

Do **not** sell to care homes or clinics in version 1: that pulls you straight into MDR and care-documentation requirements.

### Market size (estimates)
- Adults in DACH + Nordics + Benelux: ~110 M. Assume 15% are interested in sleep tracking and 20% of those reject wearables → ~3.3 M people.
- **TAM:** 3.3 M × €139 ≈ **€460 M**.
- **SAM:** reachable via online + consumer-electronics retail in DE/AT/CH/NL in 3 years, ~20% → **~€90 M**.
- **SOM (3 years):** 0.5% of SAM, ~3,300 units/year by year 3 → **~€450k/year**. Getting retail shelf space would multiply that; without it, expect low thousands per year.

### Competition
| Alternative | Price (estimate) | Weakness we attack |
|---|---|---|
| Under-mattress sleep pads (e.g. Withings Sleep Analyzer, listed at [~€150 on the Withings EU store](https://www.withings.com/en-eu/products/sleep), €119–150 at retail) | €119–150 | Under the mattress, needs Wi-Fi + app/cloud account; some models carry medical claims in some markets, which raises expectations |
| Smart rings / watches with sleep tracking | €200–450 + subscription | Must be worn and charged — exactly what this segment rejects |
| Smart displays with radar sleep sensing (big-tech attempts) | €80–120 | Glowing screen, cloud account, features come and go with software policy |
| Phone apps on the bedside table / mattress | Free–€5/month | Unreliable, phone in bed, battery |
| Do nothing | Free | The "how did I sleep?" question stays a feeling |

**Wedge:** contactless, nothing to wear or charge, **no light at night (e-paper)**, **no cloud account required**, and honest trend views instead of pseudo-clinical "scores".

### Product & value proposition
- **Radar:** Hi-Link HLK-LD6002, 58–62 GHz FMCW. The datasheet lists respiration 9–48 bpm, heart rate 60–150 bpm, chest range 0.4–1.5 m, ±60°, single person, 3.3 V at up to 600 mA, UART. We use **presence, motion and respiration trend only** in v1. Heart rate stays off the display (too close to a medical claim, and accuracy through a duvet is unproven).
- **Display + brain:** M5Stack PaperS3 (ESP32-S3 + e-paper) for the works-like prototype; production = your own ESP32-S3 + e-paper PCB.
- **Power:** mains via an isolated Hi-Link 5 W module (HLK-5Mxx) inside the base, or simpler and safer: an external certified USB-C adapter. The radar's up-to-600 mA peak rules out battery-only operation.
- **Features:** morning summary on e-paper; 7-day and 30-day trend; "compare to last week"; out-of-bed count; a gentle sunrise alarm is a nice extra. Optional: local export (USB/CSV) or an app over BLE. Optional opt-in weekly summary to a family member.
- **Design rule:** no "sleep score". Show facts (hours, episodes, rate band) against the user's own baseline.

**Pricing (estimates):** €139 RRP; €119 crowdfunding early bird; two-pack for "you + your parent" €249. No subscription. Optional family-summary service €2/month if it needs a server.

### Unit economics (estimates per unit, ex-VAT)
| Item | 1k units | 5k units |
|---|---|---|
| BOM (LD6002 radar, ESP32-S3, 4.7" e-paper, PCB, passives, light sensor, buzzer) | €30.00 | €23.00 |
| Power (certified USB-C adapter + cable) | €3.50 | €2.60 |
| Assembly & test (radar functional test on a breathing-phantom jig) | €3.50 | €2.40 |
| Enclosure (radar-transparent front, no metal paint) | €5.00 | €3.20 |
| Packaging (retail box) | €2.00 | €1.40 |
| Freight + duty to EU | €1.80 | €1.20 |
| Certification amortised (~€30k) | €30.00 | €6.00 |
| **Landed cost** | **€75.80** | **€39.80** |
| Net revenue (direct €117 ex-VAT; retail ~€70 after 40% margin) | €117 | €70 |
| **Gross margin** | **€41.20 (35%)** | **€30.20 (43%)** |

At 1k units, certification eats the margin. Sell direct first; retail only once volume pays for it.

### Go-to-market
**First 100 customers:**
- **Sleep and quantified-self communities** (Reddit sleep subforums, German-language QS meetups, Nordic wellness blogs): post the honest validation data (radar vs a chest-belt reference), not marketing.
- **Crowdfunding campaign** with a working prototype video. Target the "I stopped wearing my watch" story.
- **Adult-children angle:** parenting/elder-care newsletters and forums in DACH; content on "how to know your parent is OK without spying".
- **Design press:** e-paper + no-glow is a photogenic, design-blog-friendly story.

**Scale:** consumer-electronics retail (online first), design/lifestyle shops, pharmacy-adjacent wellness retail only with very careful claims.

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill test: LD6002 vs reference chest belt on 20 sleepers through a duvet; landing page + waitlist |
| Q2 | Custom PCB + enclosure; EVT 30 units in homes; MDR-safe wording reviewed by a regulatory consultant |
| Q3 | DVT, RED/EMC/safety testing; crowdfunding campaign (target 500 backers) |
| Q4 | Production of 1,000 units; ship backers; first retail conversation |

**Team:** 1 embedded/signal engineer (radar data, baselining, firmware), 1 industrial designer (part-time), founder on marketing/community; regulatory consultant on call (MDR boundary + GDPR), ~10 days.

**Funding to the first 1,000 units (estimates):** NRE €70k (PCB + firmware €40k, enclosure tooling €20k, app €10k) + certification €30k + regulatory/GDPR advice €10k + 1,000 units landed ~€46k + 9 months lean costs €60k ≈ **€215k**. Crowdfunding 500 × €119 ≈ €60k (minus ~10% fees) → **~€160k** from founders/angel. Consumer hardware with thin early margins: be careful with grants (most innovation grants exclude "consumer gadgets"; check health-tech-adjacent schemes only if the claims stay wellness).

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical:** breathing trend through a duvet, with a partner in bed, a pet, a fan | Kill test first; single-person mode with distance gating (radar range 0.4–1.5 m); detect "two people" and show "data unclear" rather than wrong data |
| **Technical:** module accuracy claims (90% per datasheet) are vendor numbers | Own reference testing; show bands, not exact numbers |
| **Regulatory: MDR creep.** One sentence like "detects sleep apnoea" or "monitors heart health" makes it a medical device | Written intended-use statement; marketing and app copy reviewed; no heart-rate display; no alarms about breathing |
| **Privacy/GDPR:** breathing and sleep data are health-adjacent (possibly special-category data under GDPR Art. 9); family-summary shares data about a third person | Local-first by default; explicit consent by the sleeper (not the buyer); clear on-device "sharing on/off" indicator; EU hosting; DPIA for the family feature |
| **Market:** "nice clock, meh data" | Honest trend design; return policy; long-term reviews |
| **Supply:** sole-source radar module | Qualify a second 60 GHz vital-sign module from another maker in Q3 |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD6002 60 GHz respiration/heart-rate radar | https://www.gongbans.com/db/hilink-ld6002.html | The sensor: presence, motion, respiration via UART | **Datasheet public, files via maker** (no open schematic/PCB) | Commercial module; get the UART protocol + RED report from Hi-Link |
| M5Stack PaperS3 (C139) | https://www.gongbans.com/db/m5stack-papers3.html | ESP32-S3 + e-paper for the works-like prototype | Enclosure/structure files only — main-board electronics not published | Prototype only; design your own production PCB |
| Hi-Link HLK-5Mxx 5 W isolated AC-DC | https://www.gongbans.com/db/hilink-5mxx.html | Option for an internal mains supply | **Datasheet public, files via maker** | Internal mains = more safety testing; external USB-C adapter is the simpler route |

### Block diagram
```
[LD6002 60 GHz radar] --UART--> [ESP32-S3] --SPI--> [e-paper 4.7"]
                                    |  \--I2C--> [light sensor] (wake the display politely)
                                    |  \--GPIO-> [buzzer / sunrise LED (optional)]
                                    |  \--BLE (optional)--> [phone app / export]
                  [USB-C 5 V certified adapter] -> [3.3 V regulator, sized for 600 mA radar peaks]
```
**Engineering gap:** the signal work. Turning raw presence/respiration frames into robust night summaries (in-bed detection, restlessness, baseline, "data unclear" logic) is 60% of the project. The rest: radome design (radar-transparent front, angle towards the chest), power stage for radar peaks, a low-power e-paper UI.

### Starter BOM (estimates at 1k)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD6002 | €12–16 | **Sole-source**; ask Hi-Link for the volume price, firmware freeze and lifecycle |
| ESP32-S3 module (8 MB flash/PSRAM) | €3.00 | Many sources |
| 4.7" e-paper panel | €8–10 | Check panel lifecycle; e-paper supply is concentrated |
| PCB, regulator, passives, light sensor, buzzer | €3.50 | Size the regulator for radar peaks |
| USB-C adapter (CE certified) + cable | €3.50 | Buy certified; don't design your own |
| Enclosure + radome | €5.00 | Tooling ~€15–20k |

### Firmware/software starting point
- **ESP32-S3:** ESP-IDF (Espressif, github.com/espressif/esp-idf) or Arduino-ESP32.
- **E-paper on PaperS3:** M5Stack's own libraries for the PaperS3 (search "M5Stack PaperS3 library"); for production with a generic panel, search "GxEPD2" (Arduino e-paper library).
- **Radar:** Hi-Link's UART protocol document and PC configuration tool come from the maker; Home Assistant community integrations exist for several Hi-Link radars — search for the LD6002 specifically before assuming.
- **Data:** keep the night summary on the device (flash ring buffer), export via BLE/USB.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill test:** LD6002 breathing-rate trend vs a reference chest belt within ±2 breaths/min for 20 sleepers through a duvet (median over 5-minute windows). Landing page live; 300 waitlist sign-ups |
| 3–5 | Works-like | PaperS3 + LD6002 on 10 bedside tables for 2 weeks; morning summary readable; "two people / pet" cases flagged as unclear, not wrong |
| 6–8 | Looks-like + EVT | Custom PCB + enclosure; 30 units; radome angle fixed; users rate the summary "useful" ≥4/5 |
| 9–10 | DVT + pre-compliance | RED pre-scan at 60 GHz (needs a lab with mm-wave equipment), EMC, safety; intended-use and copy review by a regulatory consultant |
| 11–12 | Pilot batch | 50 paid units; return rate <10%; no medical-claim wording anywhere (checklist signed) |

### Certification checklist (EU)
- **MDR boundary (most important):** intended use = "wellness information about sleep habits and restfulness for personal use". Not for diagnosis, prevention, monitoring, treatment or alleviation of disease (MDR Art. 2(1)). Banned words in copy, app and IFU: apnoea, diagnose, monitor (in the clinical sense), heart, arrhythmia, alarm for breathing stops, "clinically validated". Have a regulatory consultant sign off. If you ever want medical claims: that is a different company plan (class IIa or higher, notified body, clinical evaluation, QMS to ISO 13485 — easily €300k+ and 18+ months).
- **CE under RED:** 60 GHz short-range device — confirm the harmonised standard the module was tested to (e.g. EN 305 550 / EN 303 883-type standards for SRD radar; confirm with the lab). BLE: EN 300 328. EMC: EN 301 489-1/-3/-17. Safety: EN 62368-1. Exposure: EN 62311/62479. Est. **€15–25k** (60 GHz testing is not cheap and not every lab does it).
- **RED delegated act (EN 18031-1/-2):** applies if it connects to the internet (app/cloud); EN 18031-2 is relevant because of personal data. Local-only BLE export reduces scope, not to zero.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: secure update, SBOM, vulnerability handling, security by default.
- **GDPR:** sleep/breathing data may count as health data. Local-first, consent from the sleeper, DPIA for any family-sharing feature, EU hosting.
- **RoHS, REACH, WEEE**, packaging registration. No battery → no Battery Regulation scope (unless you add a backup cell).
- **Total certification + regulatory advice estimate: €25–40k.**

### Validation toolkit
- **Kill question:** Does the module's breathing-rate trend agree with a reference chest belt within ±2 breaths/min for 20 sleepers, through a duvet? If not, the product is a fancy clock.
- **Cheapest experiment (~€400):** 2 LD6002 samples + an ESP32 logging to SD + a consumer chest-strap breathing belt (or a borrowed research belt) for 20 nights across volunteers.
- **5-question interview:** 1) Have you tracked your sleep before? What made you stop? 2) What do you actually want to know in the morning? 3) Would you put a radar sensor next to your bed if nothing leaves the device? 4) (Adult children) What would tell you your parent had a normal night, and would they agree to it? 5) At €139 with no subscription, would you buy it now, or what would have to be true?
- **Landing page headline:** "Understand your sleep — without wearing anything." Bullets: "A calm e-paper clock that never glows at night." / "Shows time in bed, restlessness and breathing rhythm compared with your own normal." / "No camera. No microphone. Your data stays on the device."
- **Pass threshold:** 300 waitlist sign-ups and 60 paid €20 deposits in 6 weeks, plus a passed kill test.

### First production checklist
- **Samples:** 5 LD6002 from 2 lots — check lot-to-lot behaviour; e-paper panels from the production supplier.
- **Golden sample:** with radar firmware version, radome material/thickness and the test-jig results recorded.
- **DFM review:** radome (thin, low-loss plastic, no metallic paint or texture in front of the antenna); thermal (radar heat near e-paper); cable strain relief.
- **MOQ talk:** radar module MOQ and lead time; e-paper panel MOQ; enclosure colour MOQ.
- **QC/AQL:** AQL II 1.0/2.5; 100% radar functional test with a moving-plate "breathing phantom" jig; 100% display test; burn-in 4 h.
- **Packaging:** retail box, quick-start with the intended-use statement and privacy summary on paper (no medical words).
- **Incoterms:** FOB Shenzhen, sea freight for volume; adapter shipped in the box (check plug types per country).

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 2 board publishers (Hi-Link (海凌科) and M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R)](/db/hilink-ld6002.html) (60 GHz respiration / heart-rate radar module (2T2R)); [HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C](/db/hilink-5mxx.html) (5 W isolated AC-DC module). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack PaperS3 (C139)](/db/m5stack-papers3.html) (e-paper display + ESP32-S3 for the morning summary). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **iDisc Technology** (深圳市艾迪思科技有限公司) · no website on file — E-ink display module / e-reader OEM: E-ink display module; e-reader gongban; retail price tag; OEM/ODM. *(E-ink display modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and M5Stack websites)

```email
Subject: Sample order and volume pricing — HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139) — for a Sleep Rhythm Bedside Radar

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Sleep Rhythm Bedside Radar: A bedside e-paper clock with a 60 GHz radar that shows last night's in-bed time, restlessness and breathing-rhythm trend — contactless, no wearable, no camera, nothing uploaded unless you choose. The design is built around your HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139).

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139).
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
主题：样品订购及批量报价 — HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139) — 用于Sleep Rhythm Bedside Radar

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sleep Rhythm Bedside Radar：A bedside e-paper clock with a 60 GHz radar that shows last night's in-bed time, restlessness and breathing-rhythm trend — contactless, no wearable, no camera, nothing uploaded unless you choose。产品设计基于贵司的HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139)。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139)。
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
Subject: PCBA quote from open design files — Sleep Rhythm Bedside Radar, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Sleep Rhythm Bedside Radar: A bedside e-paper clock with a 60 GHz radar that shows last night's in-bed time, restlessness and breathing-rhythm trend — contactless, no wearable, no camera, nothing uploaded unless you choose. The design starts from published open-hardware files (HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139); schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Sleep Rhythm Bedside Radar，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Sleep Rhythm Bedside Radar：A bedside e-paper clock with a 60 GHz radar that shows last night's in-bed time, restlessness and breathing-rhythm trend — contactless, no wearable, no camera, nothing uploaded unless you choose。设计基于已公开的开源硬件文件（HLK-LD6002 60 GHz respiration and heart-rate radar module (2T2R), HLK-5Mxx 5W AC-DC isolated power module, incl. 5W-B and 5W-C, M5Stack PaperS3 (C139)；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 2 LD6002 samples and an M5Stack PaperS3; ask Hi-Link for the UART protocol, the RED test report and the volume price.
2. Recruit 10 volunteers (20 nights) and buy or borrow a reference breathing belt for the kill test.
3. Write the one-paragraph intended-use statement now and use it to filter every line of marketing copy.

Want help sourcing or building this? Talk to us via www.gongbans.com.
