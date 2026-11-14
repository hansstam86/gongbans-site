# Quiet Guardian — Founder Start Pack

> Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of Europeans over 75 live alone; their children call at 19:00 and worry the other 23 hours. The products on offer are a pendant the parent won't wear, a camera the parent won't accept, or a care-grade lamp at ~€97–116/month in NL (Nobi + platform) that is aimed at care organisations, not families.
- **Customer:** Adult children aged 45–65 in NL/DE/UK/Nordics (they pay, €149 once plus an optional €4.99/month), the parent (must consent and must not notice it), and home-care organisations as a second channel.
- **Product:** Three battery sensor nodes — thermal presence in the living room (detects a person sitting still, which PIR can't), a reed switch on the front door, a reed switch on the fridge — plus a plug-in hub. The hub learns the week's rhythm and the family gets one message a day: "all normal". Alerts only when the pattern breaks (no movement by 10:00, door open at 03:00, fridge not opened in 36 h). Wellness positioning only.
- **Why now:** Thread/Zigbee-class radios on €2 silicon with one-year coin-cell life, a thermal-presence sensor as a €10 module, and a demographic cliff that home care cannot staff. Europe has no €149, no-fee, privacy-first kit from a brand the children trust.
- **The ask:** ~€140k to the first 1,000 kits; hardware is trivial, the money goes into the pattern software, the family UX and the trust (DPIA, consent flow, support).

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Put a mock-up in 5 real homes for 3 weeks: do the children still open the daily 'all normal' message in week 3?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Adult children (45–65) of parents living alone in NL/DE/UK/Nordics; home-care organisations.

**The problem as the pack states it:** Millions of Europeans over 75 live alone; their children call at 19:00 and worry the other 23 hours. The products on offer are a pendant the parent won't wear, a camera the parent won't accept, or a care-grade lamp at ~€97–116/month in NL (Nobi + platform) that is aimed at care organisations, not families.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **r/AgingParents** · https://www.reddit.com/r/AgingParents/ — adult children caring for parents: the buyer for most elderly-care devices.
- **r/dementia** · https://www.reddit.com/r/dementia/ — families living with dementia.
- **Alzheimer's Society Dementia Support Forum (UK, formerly Talking Point)** · https://forum.alzheimers.org.uk/ — families and carers of people with dementia.
- **Carers UK forum** · https://www.carersuk.org/forum/ — family carers in the UK.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€149 + optional €4.99/month, the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how adult children of parents living alone in NL/DE/UK/Nordics deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know today that your parent got up this morning, and what did you do the last time you could not reach them?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp. On a scale of one to ten, how likely would you be to buy that at €149 + optional €4.99/month, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Quiet Guardian: would you pay €149 + optional €4.99/month for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Quiet Guardian: Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €149 + optional €4.99/month, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

The need is reassurance, not surveillance. The failure mode of every incumbent is the parent's dignity: pendants are "for old people", cameras are intrusive, and an app with 40 sensor graphs makes the child anxious rather than calm. The design brief is "one green dot a day" — and the hard part is the false-alarm rate: three false alerts and the family turns it off.

- **Who pays:** the daughter or son (statistically more often the daughter), 45–65, has a smartphone and a Zigbee lightbulb at home. Price anchor: "less than one month of the care-lamp subscription". Secondary payers: home-care organisations (NL: thuiszorg with 'leefstijlmonitoring' budgets; DE: Pflegekassen fund some digital aids under §40 SGB XI — a long road; UK: councils' technology-enabled-care budgets).
- **Who uses:** the parent, passively; must give informed consent; must be able to switch it off visibly.
- **Who installs:** the child, on a Sunday visit, in 15 minutes, with stickers.

### Market size (estimates — check)

- **TAM:** EU-27 + UK people aged 75+ living alone ≈ 15–17M (Eurostat single-person households by age — verify). At one kit per household (€149) → **€2.3B** theoretical; recurring at €4.99/month for 30% → €300M/year.
- **SAM:** NL/DE/UK/Nordic households where a child lives >30 min away and uses a smartphone ≈ 40% → 3M households → **€450M**.
- **SOM (3 years):** 30–50k kits → **€4.5–7.5M** + subscription. Year 1: 1,000–3,000 via D2C.

Sources used: Dutch press on Nobi pricing (€39/month lamp + €19 platform; ~€97–116/month per home), UK Age Co home monitor (price not public), Zorgring's Sensara manual (care-organisation deployed, pricing per client). Demographics: Eurostat — verify.

### Competition (2 searches)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing — the 19:00 phone call, the neighbour with a key | €0 | Works until it doesn't; the anxiety is the cost |
| Personal alarm pendant / fall-detection watch (many brands) | €30–150 + €15–40/month | Parent must wear it and press it; many don't |
| Care-lamp with fall detection (Nobi, Nobita) | ~€97–116/month in NL; ~$2,499 or $119/month in the US (older figure) | Excellent for care homes; priced and sold for institutions; camera-class optics in the ceiling |
| Lifestyle monitoring via care organisations (Sensara and peers in NL; TEC services in the UK) | Per client via the care provider | Only reachable through a care contract; not something a daughter can buy on Saturday |
| DIY: Zigbee sensors + Home Assistant + automations | €60 + evenings | The engineer's child does this; nobody else |
| Smart-home motion sensors with "activity" notifications (Aqara, Ring) | €20–60 | Ecosystem apps, no pattern learning, alert spam |

**Wedge:** a consumer-priced, no-subscription-required kit that a child installs in 15 minutes, says "all normal" once a day, and promises in writing: no camera, no microphone, no data sold, parent can unplug it.

### Product & value proposition

- **Nodes (3):** thermal presence (TMOS-class, detects a stationary person in a room, 6–8 m), door reed (magnet on the frame), fridge reed. Each: 802.15.4 radio (Thread), CR123A or 2× AA, one year of life, stick-on.
- **Hub:** plug-in (EU plug) with WiFi + 802.15.4, learns the pattern locally for the first 14 days, then raises alerts; cloud only relays notifications (end-to-end encrypted summaries) — the pattern lives on the hub.
- **Family app/web:** daily "all normal" at a chosen time; alert with a call button; shared with siblings; a "visible off switch" in the parent's hallway.
- **Positioning:** peace of mind, daily rhythm; never "fall detection", "medical alert" or "safety device" — see the regulatory section.
- **Pricing (estimates):** kit €149 (hub + 3 nodes); optional Plus €4.99/month (multi-sibling, longer history, phone-call escalation); extra node €29; care-organisation bundle €99 + €3/month at 100+.

### Unit economics (estimates, EUR per kit)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (3 nodes: ESP32-H2-class radio €1.8 ×3, TMOS presence sensor €8, reed + magnet €0.6 ×2, battery holders + cells €1.2 ×3, PCBs €0.6 ×3; hub: ESP32-C6-class €2.5, EU plug PSU module €2.5, PCB + passives €2.5) | 27 | 22 |
| PCBA assembly + test (4 boards, radio range test) | 6.5 | 4.5 |
| Enclosures (3 node shells + hub, 4 small tools ~€22k) | 6.0 | 2.8 |
| Packaging (gift-grade box — the child buys this for a parent), stickers, guide | 3.5 | 2.5 |
| Freight + duty to EU (lithium primary cells → DG surcharge if CR123A; AA alkaline avoids it) | 3.0 | 1.5 |
| Certification amortised (€45k: RED + EN 18031-1/-2, EMC, safety, Thread) | 45.0 | 9.0 |
| **Landed cost** | **91** | **42.3** |
| D2C net price (€149 incl. 21% VAT → €123) less €8 fulfilment | 115 | 115 |
| **Gross margin D2C** | **€24 (21%)** | **€73 (63%)** |
| Subscription €4.99/month at 30% attach, ~€0.40/month cost | +€16/year/kit | +€16/year/kit |

Hardware margin at 1k is thin; the first 1,000 kits are a software-and-trust investment. Use AA alkaline, not CR123A, for node power: cheaper, no DG, and the parent can buy them at the supermarket.

### Go-to-market

**First 100 customers:** 5 real homes for the kill question, then 100 kits to the people already asking — the "caring for ageing parents" Facebook groups and forums in NL and DE, the mantelzorg (informal carer) organisations' newsletters, two podcasts for the sandwich generation, and a GP-practice waiting-room flyer in one town. Price €149, explicit "no subscription needed".

**Scale:** D2C (search: "ouders alleen thuis sensor", "Eltern allein zuhause Sicherheit ohne Kamera"), pharmacies and home-care shops (thuiszorgwinkels, Sanitätshäuser), informal-carer insurance benefits (some Dutch insurers reimburse mantelzorg aids — check), home-care organisations as a B2B2C channel with the €99 bundle, and UK councils' TEC frameworks later.

### 12-month plan

- **Q1:** kill question (5 homes, 3 weeks, mock-up from dev kits), pattern model v1 (rule-based: wake window, door events, fridge gaps), consent flow and DPIA drafted with a privacy lawyer.
- **Q2:** own node + hub PCBs, Thread stack stable, 50 EVT kits in 50 homes for 8 weeks; false-alert rate measured; family UX iterated weekly.
- **Q3:** DVT, certification (RED, EN 18031-1/-2, EMC, safety, Thread certification optional), pilot batch 200, pharmacy/home-care-shop pilot in one region.
- **Q4:** production 1,000, D2C launch with the "no camera, no subscription required" promise, care-organisation pilot.

**Team:** founder (product, trust, content), 1 embedded engineer (ESP-IDF, Thread/802.15.4, low power), 1 full-stack/mobile developer (hub logic, app, notifications), part-time data scientist for the pattern model (rules first, ML later), a geriatric-care advisor (part-time), privacy lawyer (contract). Customer support from day one — this product gets phone calls.

**Funding to 1,000 units (estimate):** NRE €32k (PCBs €6k, tooling €22k, ID €4k) + certification €45k + 9 months salaries (3 people, lean) €95k + legal/DPIA €8k + 1,000 kits at €46 landed €46k = **€226k**, less first-year revenue (~€85k) → **€140k** net. Route: a health/ageing innovation grant (EIT Health, national ageing-in-place programmes, Dutch ZonMw-type calls), an angel with a care background, pre-orders from the carer communities. Not a bootstrap product: the software and support burn before the hardware sells.

### Top risks

- **Market — false alarms kill trust.** Mitigation: rule-based model with conservative thresholds, 14-day learning period with no alerts, "all normal" daily so silence is never ambiguous, measure false-alert rate in 50 homes before launch (target <1 per month per home).
- **Regulatory — medical-device line.** "Fall detection", "emergency", "health monitoring" claims push you into MDR. Mitigation: wellness/reassurance wording only, lawyer-reviewed; if you ever add fall detection, state that MDR applies and plan for it.
- **Regulatory — GDPR.** Behavioural data about a specific, often vulnerable person: DPIA mandatory; consent of the monitored person (and a capacity question for dementia — your advisor's job); data minimisation (pattern on the hub, summaries only in the cloud); parent-visible off switch.
- **Technical — thermal presence in a room with a radiator, a pet or sunlight.** Mitigation: TMOS-class sensors handle stationary people better than PIR but still need placement rules; combine with door/fridge events; pets in the interview script.
- **Supply — presence sensor single-vendor.** Mitigation: qualify a mmWave alternative module for the same footprint; buy 3k sensors with production.
- **Support cost.** Mitigation: installation video, chat support, a "test my sensors" button; budget 0.5 FTE support per 2,000 homes.

## 4. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| M5Stack Unit TMOS PIR (U185) | https://www.gongbans.com/db/m5stack-unit-tmos-pir.html | Thermal presence that detects stationary people (plain PIR cannot) — the living-room node's sensor | enclosure/structure files only; electronics not published | Off-the-shelf; use as bought; design the production node around the sensor IC |
| Seeed Grove-Magnetic Switch | https://www.gongbans.com/db/seeed-grove-magnetic-switch.html | Door/fridge reed-switch reference | schematic | Seeed open-hardware terms; check |
| Espressif esp32-h2-devkitm-1 | https://www.gongbans.com/db/espressif-esp32-h2-devkitm-1.html | Thread/Zigbee sensor-node radio and low-power reference | reference design files from Espressif (per catalogue) | Espressif reference-design terms; check |
| Espressif esp32-c6-devkitc-1 | https://www.gongbans.com/db/espressif-esp32-c6-devkitc-1.html | Hub with WiFi + 802.15.4 (Thread border router) | reference design files from Espressif (per catalogue) | Espressif reference-design terms; check |

### Block diagram

```
[Living-room node: TMOS presence + ESP32-H2, 2xAA] ~~Thread~~> |
[Door node: reed + ESP32-H2, 2xAA] ~~~~~~~~~~~~~~~~~~~~~~~~~~~> | [Hub: ESP32-C6, EU plug] --WiFi--> cloud relay (summaries only) --> family app
[Fridge node: reed + ESP32-H2, 2xAA] ~~~~~~~~~~~~~~~~~~~~~~~~~> |   pattern model runs here; visible off switch
Daily: "all normal" at 10:00. Alerts: no presence by X, door at night, fridge gap > 36 h, hub offline.
```

**Engineering gap:** one-year battery life on Thread with a thermal sensor (duty cycling, sleepy end device), a border router on the hub that non-engineers never see, the pattern model with a measured false-alert rate, the consent/DPIA flow built into onboarding, and a gift-grade unboxing that a 50-year-old installs in 15 minutes.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| ESP32-H2-MINI module ×3 (Thread/Zigbee, BLE) | €1.8 each | Multi-distributor; H2 is single-vendor silicon but mainstream |
| TMOS thermal presence sensor (STHS34PF80-class) | €8 | Single-vendor; qualify a mmWave alternative |
| Reed switch + magnet ×2 | €0.6 each | Commodity |
| 2× AA holder ×3 + alkaline cells | €1.2 each | No DG, supermarket replaceable |
| ESP32-C6-MINI (hub) | €2.5 | Multi-distributor |
| EU plug-in PSU module 5 V/1 A, CE | €2.5 | Buy certified module |
| Node PCBs ×3, hub PCB | €3 total | |
| Node shells ×3 + hub shell (4 tools) | €2.8 at 5k | Tooling €22k; white/beige, 3M adhesive |

### Firmware/software starting point

- ESP-IDF with Espressif's OpenThread port (esp-openthread, border-router example on C6; sleepy end device examples on H2).
- Matter is optional — a closed Thread network of your own nodes is simpler and avoids commissioning UX; add Matter later if families ask for Home Assistant integration.
- Hub logic: start rule-based in C or MicroPython on the hub; cloud relay with any push service; app as a PWA to avoid app-store delays.
- Home Assistant for the 5-home mock-up (any Zigbee/Thread sensors + automations) — the fastest way to run the kill question.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | Mock-up (dev kits or off-the-shelf Zigbee sensors + a mini-PC) in 5 real homes for 3 weeks; a daily "all normal" message by hand/script. Do the children still open the message in week 3 (≥4 of 5)? Do the parents accept it (≥4 of 5)? Below that: stop or change the UX. |
| 3–5 | Works-like | 3 node types on ESP32-H2 dev boards + C6 hub, Thread network stable for 2 weeks, measured node current → projected ≥12 months on 2× AA; rule-based model v1 running; false alerts logged. |
| 6–8 | Looks-like + EVT | Own PCBs, SLA shells, 50 kits in 50 homes for 8 weeks; false-alert rate <1/home/month; install time <15 min for 8/10 families; EMC pre-scan. |
| 9–10 | DVT + pre-compliance | PCB v2, tooled samples, RED/EMC/safety pre-tests, EN 18031-1/-2 checklist, DPIA + consent flow signed off by the lawyer, support playbook. |
| 11–12 | Pilot batch | 200 kits from a CM, golden sample, gift packaging, 100 sold at €149 to the carer communities, NPS from children ≥50. |

### Certification checklist (EU)

- **CE / RED:** 802.15.4 + BLE + WiFi → EN 300 328, EN 301 489-1/-17, EN 62311; safety EN 62368-1 (plug-in hub is the mains part — use a certified PSU module and still test the assembly).
- **RED delegated act — EN 18031-1 (network), -2 (personal data):** applies in full. Encryption, secure onboarding, no default credentials, update mechanism.
- **CRA:** reporting since September 2026, full December 2027; this is a product people trust with a parent — SBOM, disclosure policy, 5-year updates in writing.
- **GDPR:** DPIA mandatory (systematic monitoring of a vulnerable person's behaviour); explicit consent of the monitored person; capacity questions documented; data minimisation; right to switch off; EU hosting.
- **Not a medical device** as long as claims are wellness/reassurance. The moment you say "fall detection" or "emergency", MDR Class I/IIa applies — say so in your roadmap.
- **Battery regulation:** alkaline AA → producer registration still applies if you ship cells; no UN 38.3.
- **RoHS, REACH, WEEE**, packaging registration; Thread Group membership/certification only if you use the logo.
- **Estimated test costs:** RED (3 radios, 4 products — test the family) €15–20k, EMC/safety €6k, EN 18031-1/-2 €18–22k, DPIA/legal €6–8k. Budget **€45k** + legal.

### Validation toolkit

- **Kill question:** in 5 real homes over 3 weeks, do the children still open the daily "all normal" message in week 3 — and do the parents accept the sensors? **Cheapest experiment:** off-the-shelf Zigbee door/motion sensors and a mini-PC with Home Assistant per home (~€120 each), a scripted daily WhatsApp-style message sent by you. Cost ≈ €600 and 5 Sunday installs.
- **5-question interview (adult child):** 1) When did you last worry about your parent and what did you do? 2) What has your parent refused so far — pendant, camera, app — and why? 3) Who else in the family would want the daily message? 4) If the device said "unusual: no movement since 09:00", what would you do first? 5) €149 once, optional €4.99/month — what would make you buy today, and what would make your parent say no?
- **Landing page:** headline "Your parent lives alone. You get one message a day: all normal." Bullets: "Three stick-on sensors, no camera, no microphone, no wearable"; "Learns their rhythm; alerts only when the day looks different"; "€149, installed by you in 15 minutes — no subscription required".
- **Pass threshold:** 4/5 homes pass the 3-week test; then 100 pre-orders at €149 within 4 weeks of the waitlist opening.

### First production checklist

- Samples: 5 mock-ups, 50 EVT, 200 pilot; keep 3 kits per revision.
- Golden sample: node current profile, Thread range test in a typical flat, hub onboarding time, signed.
- DFM review: battery door usability for a 50-year-old's fingers, adhesive pad area, sensor window (thermal) material, hub plug orientation in EU sockets.
- MOQ talk: PCBA 500 per board type; TMOS sensor 1k; tooling at 1k shots; packaging 1k.
- QC/AQL: level II, AQL 1.0/2.5; 100% radio join test; 100% presence-sensor function on a jig; 100% hub power-on.
- Packaging: gift box, pre-paired nodes, stickers, a printed consent card for the parent.
- Incoterms: FOB Shenzhen; alkaline cells inside — declare, no DG.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (M5Stack and Seeed Studio and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit TMOS PIR (U185)](/db/m5stack-unit-tmos-pir.html) (thermal presence that detects stationary people (plain PIR cannot)). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Seeed Studio** (矽递科技(深圳)有限公司, seeedstudio.com) — community / maker brand; 183 boards in the catalogue; files via Seeed Studio wiki catalog · https://github.com/Seeed-Studio/wiki-documents. Directory entry: IoT module + open hardware OEM: XIAO ESP32S3; Grove modules; LoRa gateway; Jetson carrier; OEM PCBA. Boards used here: [Seeed Grove-Magnetic Switch](/db/seeed-grove-magnetic-switch.html) (door/fridge reed switch). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-h2-devkitm-1](/db/espressif-esp32-h2-devkitm-1.html) (Thread/Zigbee sensor nodes); [Espressif esp32-c6-devkitc-1](/db/espressif-esp32-c6-devkitc-1.html) (hub with WiFi + 802.15.4). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

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

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack and Seeed Studio and Espressif websites)

```email
Subject: Sample order and volume pricing — M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1 — for a Quiet Guardian

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Quiet Guardian: Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp. The design is built around your M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1.

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1.
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
主题：样品订购及批量报价 — M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1 — 用于Quiet Guardian

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Quiet Guardian：Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp。产品设计基于贵司的M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1。
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
Subject: PCBA quote from open design files — Quiet Guardian, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Quiet Guardian: Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp. The design starts from published open-hardware files (M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Quiet Guardian，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Quiet Guardian：Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp。设计基于已公开的开源硬件文件（M5Stack Unit TMOS PIR (U185), Seeed Grove-Magnetic Switch, Espressif esp32-h2-devkitm-1, Espressif esp32-c6-devkitc-1；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Buy 5 sets of off-the-shelf Zigbee door/motion sensors and 5 mini-PCs; recruit 5 families from your own network and install the mock-ups this weekend with the consent card.
2. Order the TMOS PIR unit, two ESP32-H2 dev kits and a C6 dev kit; measure the sleepy-end-device current and the thermal sensor's response to a seated person at 5 m.
3. Book an hour with a privacy lawyer about consent for a monitored parent with and without capacity; draft the one-page DPIA outline before the call.

Want help sourcing or building this? Talk to us via www.gongbans.com.
