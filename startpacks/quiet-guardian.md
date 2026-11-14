# Quiet Guardian — Founder Start Pack

> Three stick-on sensors (presence, front door, kitchen) that learn an elderly parent's daily rhythm and quietly tell the family when the pattern breaks — no camera, no wearable, no €2,500 lamp.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Millions of Europeans over 75 live alone; their children call at 19:00 and worry the other 23 hours. The products on offer are a pendant the parent won't wear, a camera the parent won't accept, or a care-grade lamp at ~€97–116/month in NL (Nobi + platform) that is aimed at care organisations, not families.
- **Customer:** Adult children aged 45–65 in NL/DE/UK/Nordics (they pay, €149 once plus an optional €4.99/month), the parent (must consent and must not notice it), and home-care organisations as a second channel.
- **Product:** Three battery sensor nodes — thermal presence in the living room (detects a person sitting still, which PIR can't), a reed switch on the front door, a reed switch on the fridge — plus a plug-in hub. The hub learns the week's rhythm and the family gets one message a day: "all normal". Alerts only when the pattern breaks (no movement by 10:00, door open at 03:00, fridge not opened in 36 h). Wellness positioning only.
- **Why now:** Thread/Zigbee-class radios on €2 silicon with one-year coin-cell life, a thermal-presence sensor as a €10 module, and a demographic cliff that home care cannot staff. Europe has no €149, no-fee, privacy-first kit from a brand the children trust.
- **The ask:** ~€140k to the first 1,000 kits; hardware is trivial, the money goes into the pattern software, the family UX and the trust (DPIA, consent flow, support).

## 2. Business plan

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

## 3. Start kit

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

## 4. Next steps (this week)

1. Buy 5 sets of off-the-shelf Zigbee door/motion sensors and 5 mini-PCs; recruit 5 families from your own network and install the mock-ups this weekend with the consent card.
2. Order the TMOS PIR unit, two ESP32-H2 dev kits and a C6 dev kit; measure the sleepy-end-device current and the thermal sensor's response to a seated person at 5 m.
3. Book an hour with a privacy lawyer about consent for a monitored parent with and without capacity; draft the one-page DPIA outline before the call.

Want help sourcing or building this? Talk to us via www.gongbans.com.
