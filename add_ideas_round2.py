#!/usr/bin/env python3
"""
add_ideas_round2.py — the November 2026 replacement round: 13 ideas that passed the external
market check (10 as-is, 3 with the researcher's fix applied), replacing 16 withdrawn ones.

Writes:  data/ideas.json          (+13 records in the inventor's shape)
         startpacks/<slug>.md     (one founder start pack each, in the original 4-section layout;
                                   build_ideas.py then inserts Validate demand / Who to contact /
                                   market check and renumbers, exactly as for the first 50)
         data/market-check.json   (+13 entries from the research)

Every number is an estimate and labelled so. Competitor prices are the researcher's findings
(November 2026, web search), repeated as given. Boards are real catalogue entries; names and
open-file kinds are read from data/catalog.json, never typed.

One-off; kept for the record. Safe to re-run (skips slugs already present).
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
IDEAS_PATH = ROOT / "data" / "ideas.json"
MARKET = ROOT / "data" / "market-check.json"
CATALOG = ROOT / "data" / "catalog.json"
PACKS = ROOT / "startpacks"

cat = {g["slug"]: g for g in json.loads(CATALOG.read_text(encoding="utf-8"))["gongbans"]}
OPEN_KINDS = {"schematic", "pcb", "gerber", "bom"}


def board(slug, role):
    g = cat[slug]
    kinds = sorted(set(g.get("kinds") or []) & OPEN_KINDS)
    return {"board_slug": slug, "role": role, "board_name": g["name"], "issuer": g["issuer"], "open_files": ",".join(kinds)}


def open_note(bf):
    n = sum(1 for b in bf if b["open_files"])
    return f"{n} of {len(bf)} boards publish schematic/PCB files", ("all open" if n == len(bf) else "mostly open")


def mid(rng):
    a, b = [float(x.replace(",", "")) for x in rng.split("–")]
    return (a + b) / 2


def econ_table(bom_rng, price_rng, assembly, enclosure, packaging, freight, cert_k, channel_note, channel_cost, vat=19):
    bom = mid(bom_rng)
    price = mid(price_rng)
    rows = []
    for units, f_bom, f_asm, f_enc, f_pk, f_fr in ((1000, 1.0, 1.0, 1.0, 1.0, 1.0), (5000, 0.8, 0.65, 0.7, 0.75, 0.5)):
        b, a, e2, p, fr = bom * f_bom, assembly * f_asm, enclosure * f_enc, packaging * f_pk, freight * f_fr
        c = cert_k * 1000 / units
        landed = b + a + e2 + p + fr + c
        net = price / (1 + vat / 100)
        margin = net - channel_cost - landed
        rows.append((units, b, a, e2, p, fr, c, landed, net, margin))
    r1, r5 = rows
    L = ["| Item | 1k units | 5k units |", "|---|---|---|",
         f"| Electronics BOM (estimate, mid of €{bom_rng}) | {r1[1]:.1f} | {r5[1]:.1f} |",
         f"| PCBA assembly + test | {r1[2]:.1f} | {r5[2]:.1f} |",
         f"| Enclosure / mechanics (tooling amortised separately) | {r1[3]:.1f} | {r5[3]:.1f} |",
         f"| Packaging, cable, leaflet | {r1[4]:.1f} | {r5[4]:.1f} |",
         f"| Freight + duty to EU (air at 1k, sea at 5k; check the HS code) | {r1[5]:.1f} | {r5[5]:.1f} |",
         f"| Certification amortised (€{cert_k:.0f}k, estimate) | {r1[6]:.1f} | {r5[6]:.1f} |",
         f"| **Landed cost** | **{r1[7]:.1f}** | **{r5[7]:.1f}** |",
         f"| Channel cost ({channel_note}) | {channel_cost:.1f} | {channel_cost:.1f} |",
         f"| Net price received (€{price:.0f} incl. {vat}% VAT → €{r1[8]:.1f} ex VAT) | {r1[8]:.1f} | {r5[8]:.1f} |",
         f"| **Gross margin per unit** | **€{r1[9]:.1f} ({100 * r1[9] / r1[8]:.0f}%)** | **€{r5[9]:.1f} ({100 * r5[9] / r5[8]:.0f}%)** |"]
    return "\n".join(L)


def table(header, rows):
    return "\n".join(["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + ["| " + " | ".join(r) + " |" for r in rows])


def pack_md(i, p):
    bf = i["built_from"]
    boards = "\n".join(f"- [{b['board_name']}](https://www.gongbans.com/db/{b['board_slug']}.html) — {b['role']}"
                       + (f" (open files: {b['open_files']})" if b["open_files"] else " (design files published for the module; electronics not open)") for b in bf)
    comp = table(["Alternative", "What it is / price found", "Why we still win"], p["competition"])
    risks = table(["Risk", "Mitigation"], p["risks"])
    plan = table(["Quarter", "Milestones"], [("Q1", p["q1"]), ("Q2", p["q2"]), ("Q3", p["q3"]), ("Q4", p["q4"])])
    bom = table(["Part", "Est. € (1k)", "Note"], p["bom"])
    weeks = "\n".join(f"{n}. {w}" for n, w in enumerate(p["weeks"], 1))
    return f"""# {i['title']} — Founder Start Pack

> {i['pitch']}

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** {p['problem']}
- **Customer:** {p['customer']}
- **Product:** {p['product']} Target price {('€' + i['price_eur_est'])} (estimate).
- **Why now:** {i['why_now']}
- **The ask:** {p['ask']}

## 2. Business plan

### Problem & customer

{p['problem_long']}

{p['who_pays']}

### Market size (estimates — check)

{p['market']}

### Competition ({p['searches']} searches, incl. the November 2026 external market check)

{comp}

**Wedge:** {p['wedge']}

### Product & value proposition

{p['product_long']}

### Unit economics (estimates, EUR per unit)

{p['econ']}

{p['econ_note']}

### Go-to-market

{p['gtm']}

### 12-month plan

{plan}

**Team:** {p['team']}

**Funding to first production (estimates):** {p['funding']}

### Top risks

{risks}

## 3. Start kit

### Boards to start from

{boards}

{p['boards_note']}

### Block diagram

```
{p['diagram']}
```

### Starter BOM (estimates)

{bom}

### Firmware/software starting point

{p['firmware']}

### 12-week build plan

{weeks}

### Certification checklist (EU)

{p['cert']}

### Validation toolkit

- **Kill question:** {i['kill_question']}
- **Cheapest experiment:** {p['cheapest']}
- **5-question interview:** {p['interview']}
- **Landing page:** {p['landing']}
- **Pass threshold:** {p['pass']}

### First production checklist

{p['production']}

## 4. Next steps (this week)

{p['next']}
"""


# ---------------------------------------------------------------------------
# the 13 ideas
# ---------------------------------------------------------------------------

IDEAS = []
PACKSPEC = {}
MARKETSPEC = {}

CERT_STD = ("- **RED** via the module's own radio reports (EN 300 328 / EN 300 220 as applicable, EN 301 489 EMC), **EN 18031** cybersecurity for the connected variant, **EN 62368-1** safety (USB-powered, no mains inside), **RoHS/REACH**, **WEEE** registration per country, **CRA** vulnerability-handling process.\n"
            "- Test with the DVT build in the real enclosure; budget a re-spin for EMC.\n"
            "- Lab cost: a few thousand euros for a USB-powered device with a pre-certified module, more with battery or multiple radios (estimate; get two quotes).")
CERT_BATT = CERT_STD + "\n- **Battery Regulation (EU) 2023/1542** and **UN 38.3** for the lithium cell; user-replaceable or documented removal."
CERT_MAINS = ("- Everything in the standard list (RED if radio, EMC, RoHS/REACH, WEEE, CRA) **plus LVD / EN 62368-1 or EN 60730-1 for a mains-connected control device**; the switched load goes through an installer-fitted contactor or SSR rated for it, never through the box's own relay above its rating.\n"
              "- Installer-fitted product: write the installation manual for an electrician, not a consumer; label the box accordingly.\n"
              "- Budget the lab at the high end (estimate; get two quotes) and allow one re-spin.")
PROD_STD = ("- 10 golden samples measured and photographed; one per enclosure colour.\n"
            "- DFM review with the PCBA house: test pads, programming jig, serial/MAC provisioning, who holds the signing keys (you).\n"
            "- MOQ talk: module, enclosure, packaging; get the next price break in writing.\n"
            "- QC: AQL II 2.5/4.0; 100% functional test incl. radio; burn-in sample.\n"
            "- Packaging and label: CE, WEEE bin, responsible-person address, model/serial; manual with safety and disposal text.\n"
            "- Incoterm and shipping: DDP by courier for the first run; forwarder quote for the second.")
NEXT_STD = ("1. Run section 2 (validate demand): book the first ten conversations and put the fake door up before touching a board.\n"
            "2. Order the sample boards in the start kit (three of each) and build the works-like prototype on the desk.\n"
            "3. Send e-mail A to the board publisher and e-mail B to one PCBA house (section on who to contact) to learn the real numbers behind the estimates above.")


def add(i, p, m):
    IDEAS.append(i); PACKSPEC[i["slug"]] = p; MARKETSPEC[i["slug"]] = m


# 1 ---------------------------------------------------------------------------
bf = [board("seeed-grove-digital-light-sensor", "TSL2561 digital light sensor: the measuring front end"),
      board("m5stack-unit-dlight", "alternative ambient-light unit for a quick first prototype"),
      board("dfrobot-sen0097", "BH1750 light sensor, second-source option"),
      board("m5stack-atoms3-lite", "ESP32-S3 core with display-less button for the handheld"),
      board("m5stack-stamp-c6lora", "LoRaWAN variant for a fixed monitoring post"),
      board("m5stack-unit-rtc", "timestamped logging without network")]
note, share = open_note(bf)
add({"slug": "dark-sky-meter", "title": "Dark-Sky Meter", "category": "Air & environment",
     "pitch": "A pocket sky-quality meter (mag/arcsec²) with logging and optional LoRaWAN upload, for astronomy clubs and municipalities measuring light pollution, at a third of the price of the meters they use today.",
     "audience": "Astronomy clubs and societies; municipalities and nature parks pursuing DarkSky certification or complying with light-pollution rules (France's 2018 decree, Slovenia, Croatia); ecologists studying light at night.",
     "why_now": "Light-pollution rules and DarkSky certifications now ask for measured sky brightness, the two meters everyone uses (Unihedron SQM-L, TESS-W) cost €200–290, and the sensor inside them is a €3 part the catalogue carries on three boards.",
     "built_from": bf,
     "whats_new": "A calibrated light front end behind a narrow lens, firmware that integrates long enough for dark skies, a mag/arcsec² readout, SD/phone logging and a LoRaWAN post variant; a transfer calibration against a reference meter per unit.",
     "effort_weeks_est": "8–10", "bom_eur_est": "12–18", "price_eur_est": "79–99",
     "certification": "RED (BLE / LoRa variant) via pre-certified module, EMC, EN 62368-1, RoHS, WEEE, CRA; battery → Battery Regulation / UN 38.3 for the handheld.",
     "kill_question": "Do 10 astronomy clubs or 3 municipal dark-sky projects pre-order at €89 after a side-by-side reading against a Unihedron SQM-L? Pass = 10 deposits or 3 purchase orders in 6 weeks.",
     "open_files_share": share, "scores": {"demand": 3, "buildability": 4, "margin": 4, "speed": 4},
     "tags": ["environment", "sensors", "b2b", "education", "lorawan"], "open_boards_note": note, "score_total": 15},
    {"problem": "Measuring sky brightness is the entry ticket to every dark-sky programme and to enforcing new lighting rules, and the only instruments in use are two small-volume meters at €200–290 each; a club or a municipality that wants ten measurement points does not buy ten.",
     "customer": "Astronomy clubs (hundreds across DE/FR/UK/NL), municipalities and nature parks applying for DarkSky certification or reporting under national light-pollution rules, ecologists and university departments. The club treasurer or the municipal environment officer pays.",
     "product": "A handheld meter with a narrow-field light sensor, a mag/arcsec² readout, logging to SD and phone, and a fixed LoRaWAN post variant for continuous monitoring; each unit ships with a transfer calibration against a reference meter.",
     "ask": "~€40–55k to certification and a first 1,000 units (estimate), ideally a third from club pre-orders and one municipal pilot.",
     "problem_long": "Sky-quality meters read the brightness of the night sky in magnitudes per square arcsecond; DarkSky International's certifications, France's 2018 lighting decree and the Slovenian and Croatian laws all lean on such measurements. The two meters in actual use, Unihedron's SQM-L and the open TESS-W, cost €200–290, which is why most clubs own one and most municipalities own none. Continuous monitoring, the thing that shows whether a lighting change worked, is rarer still.",
     "who_pays": "**Who pays, B2B/B2G (primary):** municipalities and parks with a dark-sky project (a certification needs a baseline and a yearly re-measurement across many points), universities and ecological consultancies. **Who pays, B2C:** amateur astronomers and clubs buying one or several. The user is often a volunteer with a clipboard at 1 a.m.; the device must be one-button.",
     "market": "- **TAM:** amateur astronomy clubs in the EU (estimate: 3,000–5,000) plus ~200 dark-sky places and candidate municipalities worldwide; one to ten meters each. Theoretical €5–10M.\n- **SAM:** clubs and municipalities in DE/FR/UK/NL/AT/CH active in light-pollution work: estimate 1,500 organisations, 3 meters each → €400k.\n- **SOM (3 yrs):** 2,000–4,000 units across clubs, a dozen municipal networks and the LoRaWAN post variant. Year-1: 500–1,000 units.",
     "searches": 3,
     "competition": [("Unihedron SQM-L", "The reference handheld; $198–290 (research, Nov 2026)", "Same sensor class at a third of the price; logging and phone export built in"),
                     ("TESS-W (Stars4All)", "Finished open-hardware photometer, about €275 assembled; fixed station with WiFi", "A finished product already exists, so the wedge is price and the handheld form, not novelty"),
                     ("Smartphone apps (Dark Sky Meter, Loss of the Night)", "Camera-based estimates", "Not accepted as a measurement by certification bodies"),
                     ("DIY TSL2591 / TSL2561 builds", "Forum and GitHub projects", "Need a case, a lens, a calibration and a battery; our customer wants to buy that")],
     "wedge": "price and one-button simplicity against a single-vendor legacy meter, with the calibration certificate that makes a club or a council trust the number. Not novelty: TESS-W already proves the open approach.",
     "product_long": "- Narrow-field (about 20°) sensor behind a lens; readout in mag/arcsec², with Bortle class shown for non-experts.\n- Long integration at dark sites (10–30 s) with a clear \"measuring\" indicator; result logged with time and, if the phone is connected, position.\n- Transfer calibration per unit against a reference SQM-L, certificate in the box; yearly re-calibration service as a small recurring line.\n- Post variant: same sensor in an IP65 tube with a Stamp C6LoRa, solar-charged, reporting every 10 minutes over LoRaWAN or TTN.\n- Open data format; CSV export; no account needed.",
     "econ": econ_table("12–18", "79–99", 2.5, 4.0, 2.0, 2.0, 10, "direct + club resellers, ~€7 per unit", 7.0),
     "econ_note": "Lesson: the first thousand pays for certification and the calibration jig; margin appears at the second run. The calibration service is the recurring line that makes the business more than a one-off gadget.",
     "gtm": "**First 100 customers:**\n\n1. Ten astronomy clubs met through their national federation newsletters (VdS in Germany, SAF in France, FAS in the UK), each buying one meter and running a side-by-side with their SQM-L.\n2. Two municipal dark-sky candidates found via DarkSky International's European chapters, buying a ten-point network.\n3. University ecology departments studying artificial light at night.\n\n**Scale channels:** astronomy retailers (Teleskop-Service, Astroshop), the DarkSky community, environmental consultancies.",
     "q1": "Kill-question conversations; works-like prototype on the Digital Light Sensor + AtomS3; calibration method agreed with one club that owns an SQM-L.",
     "q2": "Custom PCB with the lens barrel; EVT 20; pre-compliance; post variant on Stamp C6LoRa.",
     "q3": "DVT; certification; 300-unit run; club pre-orders shipped; first municipal network installed.",
     "q4": "1,000 units; retailer listing; calibration service live.",
     "team": "one embedded engineer (optics and calibration experience helps), one founder for clubs and councils; mechanical design and the lens barrel bought in.",
     "funding": "NRE €18k (PCB spins, lens tooling, calibration rig) + certification €8–10k + first 1,000 units landed ~€25k ≈ €50–55k; minus pre-orders ~€15k ≈ €35–40k.",
     "risks": [("Sensitivity at very dark skies (above 21 mag/arcsec²) needs long integration and a low-noise sensor", "Characterise the TSL2561 and TSL2591 early; state the measuring range on the box; the post variant integrates longer"),
               ("Clubs trust the SQM-L and nothing else", "Side-by-side data published per unit; calibration certificate; invite a federation to test"),
               ("Municipal sales cycles are slow", "Sell to clubs first; councils follow the club's data"),
               ("TESS-W is open and good", "Compete on the handheld form, price and the service; do not pretend it does not exist")],
     "boards_note": "The Seeed Grove Digital Light Sensor publishes its schematic; the M5Stack DLight unit and the DFRobot board are second sources for the same job. The Stamp C6LoRa (open PCB + schematic) is the core of the post variant.",
     "diagram": "  [lens + baffle] -> [TSL2561 / BH1750 light sensor]\n                           |  I2C\n  [button] -> [ESP32-S3 AtomS3 core] -> [OLED / phone BLE]\n                           |\n                  [RTC] [microSD] [Li-ion + USB-C charge]\n  post variant: [sensor] -> [Stamp C6LoRa] -> LoRaWAN / TTN,  [solar + cell]",
     "bom": [("TSL2561 / BH1750 sensor board", "2.0", "or TSL2591 for more dark-sky range"), ("ESP32-S3 module", "2.5", "pre-certified"), ("Lens + baffle tube", "2.0", "stock plastic lens; tolerance matters"),
             ("Li-ion cell + charger + USB-C", "3.0", "handheld variant"), ("RTC + microSD", "1.5", ""), ("Enclosure", "3.5", "injection moulded at volume; printed for EVT"), ("PCB + passives", "1.5", "")],
     "firmware": "- ESP-IDF or Arduino; integration-time control, dark-current subtraction, conversion to mag/arcsec² with per-unit calibration constants stored in NVS.\n- BLE to a small web app (Web Bluetooth) for logging and export; no account.\n- Post variant: LoRaWAN uplink every 10 minutes, Cayenne LPP, TTN decoder published.",
     "weeks": ["Interviews and fake door live", "Sensor characterisation against an SQM-L at a dark site", "Prototype on AtomS3 + Grove sensor", "Lens barrel and baffle design", "Custom PCB v1", "Calibration rig and procedure",
               "EVT 20 built", "Field test with two clubs", "Enclosure tooling decision", "DVT build in enclosure", "Pre-compliance EMC/radio", "Certification submission; pre-order shipping plan"],
     "cert": CERT_BATT,
     "cheapest": "Borrow a club's SQM-L, build one prototype, publish 30 nights of side-by-side readings; ask ten clubs whether that data would make them buy at €89.",
     "interview": "1) How many measurements did you take last year and with what? 2) What did they cost you, including the meter? 3) Who asks you for the numbers (council, certification, your own records)? 4) What would make you distrust a cheaper meter? 5) At €89 with a calibration certificate, how many would you buy?",
     "landing": "headline \"Measure your sky. €89, calibrated, logs to your phone.\" Bullets: side-by-side with SQM-L; Bortle class and mag/arcsec²; LoRaWAN post for councils. Button: refundable €20 deposit.",
     "pass": "10 club deposits or 3 municipal purchase orders within 6 weeks.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "Unihedron SQM-L ($198–290) and TESS-W (about €275 assembled) confirm a real 2.5–3× price gap. TESS-W is already a finished open-hardware product at a similar price to the SQM-L, so the wedge is price and simplicity, not novelty.",
     "risk": "A finished open product exists; the handheld form, the calibration certificate and the price must carry the pitch.",
     "rows": [["Unihedron SQM-L", "$198–290 handheld", "Legacy reference meter, 2.5–3× the target"], ["TESS-W (Stars4All)", "About €275 assembled, open hardware, fixed station", "Finished open product already exists"], ["France 2018 light-pollution decree (overview)", "Regulation requiring lighting controls and measurements", "Institutional pull"]]})

# 2 ---------------------------------------------------------------------------
bf = [board("m5stack-unit-mic", "microphone unit for the sound front end"),
      board("m5stack-unit-mini-pdm", "digital PDM microphone alternative"),
      board("seeed-grove-analog-microphone", "open analogue microphone reference circuit"),
      board("dfrobot-dfr0034", "analogue sound sensor, second source"),
      board("seeed-grove-chainable-rgb-led", "RGB light-engine reference circuit for the traffic light"),
      board("m5stack-atoms3-lite", "ESP32-S3 core")]
note, share = open_note(bf)
add({"slug": "classroom-noise-light", "title": "Noise Light", "category": "Education & STEM",
     "pitch": "A wall traffic light that shows classroom or kindergarten noise level live and logs daily exposure for the teacher, with no subscription and no app required.",
     "audience": "Kindergartens and primary schools (teacher hearing-protection guidance from the German Unfallkassen), libraries, open-plan offices; kindergarten operators (Träger) as the buyer.",
     "why_now": "Noise in kindergartens is a recognised occupational hazard (DGUV / Unfallkassen guidance), the institutional product costs over €1,200, and lending programmes exist precisely because nobody can afford to buy one per room.",
     "built_from": bf,
     "whats_new": "A wall unit with a big three-colour light, A-weighted level estimation on an ESP32, a daily exposure log on an e-paper or small OLED, optional WiFi export; set-up by two buttons, no app.",
     "effort_weeks_est": "8", "bom_eur_est": "18–28", "price_eur_est": "99–149",
     "certification": "RED via module (WiFi variant), EMC, EN 62368-1 (USB power), RoHS, WEEE, CRA; no battery in the wall unit.",
     "kill_question": "Do 10 kindergartens of one Träger buy at €119 after a two-week trial unit, knowing that their Unfallkasse lends similar lights for free? Pass = 10 orders or one Träger-wide framework order.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 5},
     "tags": ["education", "sensors", "b2b", "wifi", "building"], "open_boards_note": note, "score_total": 18},
    {"problem": "Kindergarten and classroom noise regularly reaches levels that damage teachers' hearing and children's concentration; staff know it but have no live feedback, and the institutional noise lights cost €1,200–3,500 each.",
     "customer": "Kindergarten operators (municipal, church and private Träger running 5–200 sites), primary schools, libraries and open-plan offices. The Träger's facility or health-and-safety lead pays; the teacher uses it.",
     "product": "A wall-mounted traffic light with a microphone, a live colour (green / amber / red with adjustable thresholds), a daily exposure log readable on the device and exportable over WiFi, powered by USB-C.",
     "ask": "~€35–45k to certification and a first 1,000 units (estimate); one Träger framework order covers half.",
     "problem_long": "German accident insurers (Unfallkassen, DGUV) treat kindergarten noise as an occupational hazard and publish guidance on it; they even lend noise lights to sites for a few weeks because the purchase price is prohibitive. A traffic light children can see changes behaviour in the room within minutes; the exposure log gives the teacher an argument for acoustic measures. Today both come in a €1,230–3,500 institutional device or in a web app on a laptop nobody has in the room.",
     "who_pays": "**Who pays, B2B (primary):** kindergarten Träger and school boards buying for many rooms; libraries and offices as a second segment. **Who uses:** the teacher, who must be able to set thresholds with two buttons. **Free alternative to beat:** the Unfallkasse lending programme (a few weeks per site, then it is gone).",
     "market": "- **TAM:** ~60,000 kindergartens in Germany alone, ~300,000 rooms; plus schools, libraries, offices across the EU. Theoretical €40–60M in DE.\n- **SAM:** Träger with more than ten sites and a health-and-safety lead: estimate 15,000 rooms addressable per year → €1.5–2M.\n- **SOM (3 yrs):** 5–10 Träger framework orders plus retail: 6,000–10,000 units. Year-1: 1,000–2,000.",
     "searches": 3,
     "competition": [("SoundEar 3 (and SoundEar II)", "Institutional noise light; €1,230–3,500 (research, Nov 2026)", "A tenth of the price for the same visible function; logging included"),
                     ("DGUV / Unfallkassen lending programmes", "Free noise lights on loan for a few weeks", "Free beats cheap for a trial; we are the thing to buy after the loan proves it"),
                     ("Bouncy Balls and similar web apps", "Laptop microphone + browser", "Needs a laptop in the room; no log; no visibility for small children"),
                     ("DIY ESP32 noise lights", "Maker projects", "No case, no calibration, no one to sell to a Träger")],
     "wedge": "a tenth of the institutional price with the exposure log, sold to the Träger after the free loan has shown the effect.",
     "product_long": "- 150 mm three-colour light, visible from the back of the room; thresholds set by two buttons (default 70/80 dB(A) for kindergartens).\n- Indicative A-weighted level from the MEMS microphone; a calibration tone procedure in the manual; clearly labelled \"not a class-2 sound-level meter\".\n- Daily exposure log (minutes in amber and red) on a small e-paper or OLED; CSV export over WiFi; no cloud account.\n- Optional quiet-time mode (light off, log on) for nap time.",
     "econ": econ_table("18–28", "99–149", 2.5, 6.0, 2.5, 2.5, 8, "direct to Träger and education resellers, ~€10", 10.0),
     "econ_note": "Lesson: a Träger order of 50–200 units is the unit of sale; price the framework order, not the single light. Retail through education suppliers works at the second run.",
     "gtm": "**First 100 customers:**\n\n1. Three Träger approached through their health-and-safety leads with a two-week trial unit per site.\n2. The Unfallkassen that run lending programmes, asked to list the product as the thing to buy afterwards.\n3. Libraries and co-working spaces via direct outreach.\n\n**Scale channels:** education suppliers (Betzold, Wehrfritz), DGUV publications, Träger associations.",
     "q1": "Kill-question conversations with three Träger; works-like prototype on the Unit MIC + AtomS3 + chainable RGB LEDs; threshold defaults agreed with a teacher.",
     "q2": "Custom PCB; enclosure; EVT 20 in ten rooms; pre-compliance.",
     "q3": "DVT; certification; 500 units; first Träger framework order shipped.",
     "q4": "Education-supplier listing; 2,000 units; Unfallkasse conversation.",
     "team": "one embedded engineer, one founder selling to Träger; industrial design bought in.",
     "funding": "NRE €15k + certification €8k + first 1,000 units landed ~€30k ≈ €53k; minus a framework pre-order ~€25k ≈ €30k.",
     "risks": [("The free loan programme is enough for some sites", "Position as the purchase after the loan; sell the log and the permanence"),
               ("Indicative dB is challenged by a facility manager", "Say so on the box; offer a calibration tone; never claim class-2"),
               ("Träger procurement wants three quotes", "Have the education-supplier listing ready; price per room"),
               ("Light becomes a toy for the children", "Threshold and hysteresis design; nap mode")],
     "boards_note": "The Seeed microphone and RGB LED boards publish schematics; the M5Stack units are the quickest prototype path. One PCB spin combines microphone, LED driver and ESP32 module.",
     "diagram": "  [MEMS mic] -> [ESP32-S3: A-weighting, 1 s Leq] -> [3-colour LED array 150 mm]\n                      |                                    |\n               [2 buttons: thresholds]              [small e-paper/OLED: today's log]\n                      |\n               [USB-C 5 V]   optional WiFi export (CSV)",
     "bom": [("MEMS microphone (PDM or analogue)", "1.5", ""), ("ESP32-S3 module", "2.5", "pre-certified"), ("LED array + driver (three colours, 150 mm)", "5.0", ""), ("Small e-paper or OLED", "4.0", ""), ("Enclosure + wall mount", "6.0", "two-part moulded; printed for EVT"), ("PCB, USB-C, passives", "2.5", "")],
     "firmware": "- ESP-IDF; I2S microphone, A-weighting filter, 1-second Leq, hysteresis on colour changes; log per day in flash.\n- Local web page over WiFi (optional) for CSV export; no cloud.\n- Calibration-tone routine with a phone app or a reference meter in the manual.",
     "weeks": ["Interviews with Träger; fake door", "Prototype on Unit MIC + AtomS3 + RGB", "A-weighting and thresholds tested in one kindergarten", "Enclosure and light design", "Custom PCB v1", "Daily log and export",
               "EVT 20 in ten rooms", "Teacher feedback round", "Enclosure tooling decision", "DVT in enclosure", "Pre-compliance", "Certification submission; framework order paperwork"],
     "cert": CERT_STD,
     "cheapest": "Three prototypes in three rooms of one kindergarten for two weeks; ask the Träger's safety lead whether they would buy 20 at €119.",
     "interview": "1) How loud does it get in your rooms and how do you know? 2) Have you borrowed a noise light from the Unfallkasse; what happened when it went back? 3) Who decides on purchases like this and what budget line? 4) What would the log need to show to be useful to you? 5) At €119 per room, how many rooms?",
     "landing": "headline \"The noise light your Träger can afford.\" Bullets: see the noise, log the day, €119 instead of €1,200+. Button: request a trial unit (B2B form).",
     "pass": "10 orders or one Träger framework order within 8 weeks of the trials.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY (STRONG)",
     "summary": "SoundEar 3 sells at €1,230–3,500 to institutions, a far larger gap than assumed. German DGUV / Unfallkassen already recognise kindergarten noise as a hazard and run free noise-light lending programmes.",
     "risk": "The free lending programmes are a competing alternative for the trial phase; the product must be the purchase after the loan.",
     "rows": [["SoundEar 3", "€1,230–3,500 institutional noise light", "Incumbent, 10× the target"], ["DGUV / Unfallkassen Lärmampel lending programmes", "Free loan of noise lights to kindergartens", "Competing free alternative; also confirms the hazard is recognised"], ["DIY ESP32 noise-light projects", "Maker builds", "Demand signal, no finished product"]]})

# 3 ---------------------------------------------------------------------------
bf = [board("m5stack-atoms3-lite", "ESP32-S3 core for master and outstations (ESP-NOW)"),
      board("m5stack-unit-bytebutton", "RGB-lit button bar for the master"),
      board("m5stack-unit-button", "single big button for an outstation"),
      board("m5stack-unit-buzzer", "acknowledge beep"),
      board("seeed-grove-chainable-rgb-led", "open RGB indicator circuit for the outstation lamp")]
note, share = open_note(bf)
add({"slug": "cue-light-system", "title": "Cue Lights for Small Stages", "category": "Audio",
     "pitch": "A wireless standby/go cue-light set (master plus four battery outstations with big lit buttons) for school theatres, amateur dramatics, churches and small event crews, 30–55% cheaper than the entry-level professional systems.",
     "audience": "Amateur theatre federations (BDAT in Germany, Little Theatre Guild in the UK), school and university theatres, churches with productions, small AV hire companies.",
     "why_now": "Amateur and school stages run cues by whisper and WhatsApp; the professional cue-light systems start around $485 and go to $985 (research, Nov 2026); ESP-NOW and lit buttons make a reliable set buildable from catalogue parts.",
     "built_from": bf,
     "whats_new": "A stage-manager master with four channels and four battery outstations; standby (flashing) and go (solid) with acknowledge; ESP-NOW with retries and a link-health light; no WiFi network, no app.",
     "effort_weeks_est": "10", "bom_eur_est": "60–90", "price_eur_est": "349–449",
     "certification": "RED via pre-certified ESP32 module (2.4 GHz), EMC, EN 62368-1, RoHS, WEEE, CRA; Battery Regulation / UN 38.3 for the outstation cells.",
     "kill_question": "Do 10 amateur groups from one federation pre-order the five-piece set at €399 after a video demo? Pass = 10 deposits in 6 weeks.",
     "open_files_share": share, "scores": {"demand": 3, "buildability": 5, "margin": 4, "speed": 5},
     "tags": ["events", "education", "b2b", "consumer", "wifi"], "open_boards_note": note, "score_total": 17},
    {"problem": "Small stages have no cue lights: the stage manager whispers, waves or texts, and missed cues follow. Professional sets exist but cost $485–985 and are sized for venues with a budget line for them.",
     "customer": "Amateur dramatic societies (thousands in DE/UK/NL), school and university theatres, churches staging productions, small AV and event-hire companies. The society treasurer, the school drama department or the hire company pays.",
     "product": "A stage-manager master with four lit channel buttons and four battery outstations with a big lit button and a buzzer; standby flashes, go is solid, the operator acknowledges; ESP-NOW link with retries and a link-health light; charges over USB-C.",
     "ask": "~€45–60k to certification and a first 500 sets (estimate); federation pre-orders cover a third.",
     "problem_long": "Cue lights are the standard way a stage manager tells lighting, sound, fly and stage crew when to stand by and when to go. Professional venues wire them in; everyone below that improvises. The professional portable systems (DSan PerfectCue and CueLight, $485–985) are good but priced for professionals; amateur groups, schools and churches, which stage most of the productions in Europe by number, run without.",
     "who_pays": "**Who pays:** the society or school (B2B-ish, small budgets, grant-funded equipment purchases), the AV hire company (buys several sets, rents them). **Who uses:** volunteers, so set-up must be nothing: switch on, pair, go.",
     "market": "- **TAM:** amateur theatre groups in DE (~2,500 in BDAT), UK (~2,500 affiliated), NL/AT/CH, plus schools with a stage (tens of thousands) and churches. Theoretical €10–20M.\n- **SAM:** groups that stage two or more productions a year and own some kit: estimate 10,000 → €4M.\n- **SOM (3 yrs):** 2,000–3,000 sets; year-1: 400–600, mostly through two federations and one hire company.",
     "searches": 3,
     "competition": [("DSan PerfectCue / CueLight", "Professional portable cue lights; $485–985 (research, Nov 2026)", "30–55% cheaper with the same standby/go/acknowledge logic; sized and priced for amateurs"),
                     ("Interspace Industries and wired venue systems", "Installed systems, quote-based", "Different market; we are portable and battery"),
                     ("WhatsApp, headsets, hand signals", "Free", "Missed cues; headsets cost more than our set"),
                     ("DIY cue-light projects (Blue Room forum, Hackaday)", "Arduino / ESP32 builds", "Demand signal; nobody ships a boxed set")],
     "wedge": "a boxed, charged, paired-out-of-the-box set at €399 for the people who today whisper; the gap against the entry-level professional set is 30–55%, not a multiple, so the simplicity matters as much as the price.",
     "product_long": "- Master: four channels, lit buttons (amber standby, green go), per-channel acknowledge indication, link-health light, USB-C charged.\n- Outstation: one big lit button, buzzer (switchable), belt clip and magnet, 20-hour battery (estimate).\n- Radio: ESP-NOW on 2.4 GHz with acknowledgements and retries; channel scan at start; range tested across a 30 m hall with walls.\n- Expand to eight outstations; no app, no WiFi needed; firmware update over USB.",
     "econ": econ_table("60–90", "349–449", 8.0, 14.0, 6.0, 5.0, 10, "direct + theatre suppliers, ~€30 per set", 30.0),
     "econ_note": "Lesson: a five-piece set carries five enclosures and five batteries; the margin lives in the second run and in extra outstations sold separately.",
     "gtm": "**First 100 customers:**\n\n1. Ten groups from one federation after a video demo and a loaner set at a festival weekend.\n2. One AV hire company buying five sets.\n3. Drama departments via their teachers' association.\n\n**Scale channels:** theatre suppliers (Thomann, Stage Depot), federation newsletters and festivals, school equipment catalogues.",
     "q1": "Kill-question conversations; works-like set on five AtomS3 + ByteButton/Button units; range test in a hall.",
     "q2": "Custom PCBs (master, outstation); enclosures; EVT 10 sets with two groups.",
     "q3": "DVT; certification; 200 sets; federation pre-orders shipped.",
     "q4": "Supplier listing; 500 sets; eight-channel master.",
     "team": "one embedded engineer, one founder from the theatre world; enclosure design bought in.",
     "funding": "NRE €22k (two PCBs, two enclosures) + certification €10k + first 500 sets landed ~€45k ≈ €77k; minus pre-orders ~€20k ≈ €57k.",
     "risks": [("Gap against DSan is smaller than hoped", "Compete on the amateur-sized package and simplicity; do not overclaim the price gap"),
               ("Radio reliability in a steel-framed hall", "Acknowledged protocol, retries, link-health light, channel scan; test early"),
               ("Battery and enclosure cost of five pieces", "Shared enclosure for master and outstation; one battery type"),
               ("Volunteers lose outstations", "Sell singles; magnet and clip; bright colour")],
     "boards_note": "The AtomS3 Lite and the button units are M5Stack products with published module files; the Seeed RGB board gives the open indicator circuit. Two PCBs: master and outstation.",
     "diagram": "  MASTER: [4 lit buttons] -> [ESP32-S3] -> ESP-NOW ->  OUTSTATION 1..8: [ESP32-S3] -> [big lit button] [buzzer]\n           [link light]       [USB-C + cell]                            [USB-C + cell] [clip/magnet]\n  standby = flashing amber, go = solid green, ack = button press echoed to master",
     "bom": [("ESP32-S3 modules ×5", "12.5", ""), ("Lit buttons (master 4 + outstations 4)", "10.0", ""), ("Li-ion cells + chargers ×5", "12.0", ""), ("Buzzers ×4", "2.0", ""), ("Enclosures ×5", "14.0", "one shared design"), ("PCBs, USB-C, passives", "8.0", ""), ("Case / pouch for the set", "6.0", "")],
     "firmware": "- ESP-IDF, ESP-NOW with application-level acks and sequence numbers; channel selection at power-up; pairing by holding buttons.\n- State machine per channel: idle / standby / go / acknowledged; buzzer patterns.\n- Battery gauge and low-battery flash; USB firmware update.",
     "weeks": ["Interviews; fake door with a demo video", "Prototype five units", "Protocol: acks, retries, range test", "Button and lamp design", "Two PCBs v1", "Enclosure design",
               "EVT 10 sets", "Two productions run with it", "Tooling decision", "DVT sets", "Pre-compliance", "Certification; pre-order shipping"],
     "cert": CERT_BATT,
     "cheapest": "Film a 60-second demo of the five-unit prototype in a real tech rehearsal; post it in two federation groups with a €399 pre-order link.",
     "interview": "1) How do you call cues today and what went wrong last show? 2) Have you priced cue lights; which and why not? 3) Who signs off equipment purchases and from what budget? 4) How many positions need a light? 5) At €399 for master plus four, would you order for the next production?",
     "landing": "headline \"Standby. Go. No whispering.\" Bullets: five pieces, charged, paired; works through walls; €399. Button: refundable €50 deposit.",
     "pass": "10 deposits from one federation in 6 weeks.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY (CONTESTED)",
     "summary": "The real incumbent, DSan PerfectCue / CueLight, sells at $485–985, not the £1.5–4k first assumed; the gap holds at 30–55% cheaper but is smaller than first thought. Blue Room forum threads and a Hackaday cue-light project show DIY demand.",
     "risk": "A smaller price gap than assumed: the package and simplicity for amateur groups must carry the pitch alongside price.",
     "rows": [["DSan PerfectCue / CueLight", "$485–985 portable cue lights", "Incumbent; the target is 30–55% below it"], ["Blue Room forum DIY threads", "Technicians building their own", "Demand signal"], ["Hackaday cue-light project", "Maker build", "Demand signal, no boxed product"]]})

# 4 (fix: scheduled + live where available) ---------------------------------
bf = [board("m5stack-papers3", "ESP32-S3 e-paper device for the prototype sign"),
      board("m5stack-papercolor", "colour e-paper variant for line colours"),
      board("simcom-a7670x-hw-design", "Cat-1/Cat-M cellular module hardware design for the backhaul"),
      board("m5stack-unit-catm", "Cat-M unit for the prototype"),
      board("dfrobot-dfr0535", "solar power manager for the off-grid post"),
      board("m5stack-stamp-c6lora", "LoRaWAN backhaul where a town network exists")]
note, share = open_note(bf)
add({"slug": "village-stop-display", "title": "Village Stop Display", "category": "Displays",
     "pitch": "A solar e-paper departure sign for rural bus stops and dial-a-ride that shows the timetable always and live departures where the operator broadcasts them, at a fraction of the price of transit-agency displays.",
     "audience": "Landkreise and regional transport associations whose operators already publish GTFS-Realtime (for example VBN and other open-data regions), small municipalities, rural bus operators; B2G procurement.",
     "why_now": "Rural stops have paper timetables and no information at all when a bus is late; agency displays cost €2,000–5,000 with service contracts; e-paper, Cat-M and solar make a €800 sign possible, and open GTFS data is spreading region by region.",
     "built_from": bf,
     "whats_new": "An A4-class e-paper sign in an IP65 housing with a solar panel, a Cat-M or LoRaWAN modem, firmware that always shows the scheduled departures from GTFS and overlays live times only where GTFS-Realtime for that stop actually exists, and says which it is showing.",
     "effort_weeks_est": "14", "bom_eur_est": "120–180", "price_eur_est": "599–899",
     "certification": "RED (cellular module pre-certified; LoRa variant EN 300 220), EMC, EN 62368-1, RoHS, WEEE, CRA; Battery Regulation for the solar buffer cell; IP65 and vandal-resistance by design, not certification.",
     "kill_question": "Do 2 Landkreise or transport associations whose operators already publish GTFS-Realtime sign a paid 10-stop pilot at €799 per sign within 8 weeks? Pass = 2 signed pilots; a region without GTFS-RT at its stops does not count.",
     "open_files_share": share, "scores": {"demand": 3, "buildability": 4, "margin": 4, "speed": 3},
     "tags": ["displays", "e-paper", "b2b", "cellular", "solar", "public"], "open_boards_note": note, "score_total": 14},
    {"problem": "Outside cities, a bus stop is a pole and a laminated sheet; when the bus is late nobody knows, and the agency displays that could tell them cost €2,000–5,000 each plus a service contract, so rural stops never get one.",
     "customer": "Landkreise and regional transport associations (B2G) in regions whose operators publish GTFS and GTFS-Realtime; municipalities that co-fund stop furniture; dial-a-ride and community bus operators. The transport association's passenger-information budget pays.",
     "product": "An A4-class e-paper sign in an IP65 housing with solar panel and buffer cell, Cat-M (or LoRaWAN where a town network exists), showing the scheduled departures from GTFS at all times and live times where GTFS-Realtime exists for that stop, with the source stated on screen.",
     "ask": "~€90–120k to certification and a first 200 signs (estimate); two paid pilots cover a third.",
     "problem_long": "Research for this pack confirmed the catch: live departure data needs on-board equipment in the vehicle, and rural or small-contractor fleets often lack it, so a sign that promises \"live\" everywhere lies in exactly the places that need it most. The product is therefore scoped: timetable always, live where the operator broadcasts it, and the sign says which. Even the scheduled-only mode replaces a laminated sheet that is often out of date, and the live overlay arrives as operators equip their fleets (regions such as VBN already publish GTFS-Realtime as open data).",
     "who_pays": "**Who pays, B2G (primary):** transport associations and Landkreise from passenger-information and stop-furniture budgets, often with regional or EU funding for rural mobility. **Who uses:** passengers, including older people without a smartphone, which is the political argument for the sign.",
     "market": "- **TAM:** ~300,000 bus stops in Germany, the large majority without any display; similar density in AT/CH/NL/FR. Theoretical €200M+ at €800.\n- **SAM:** stops in regions with open GTFS feeds and a rural-mobility programme: estimate 30,000 stops → €25M.\n- **SOM (3 yrs):** 1,500–3,000 signs across 10–20 regions. Year-1: 100–200 signs in two pilots and two follow-on orders.",
     "searches": 4,
     "competition": [("Papercast, Luminator, ConnectPoint", "Agency-grade e-paper and LED stop displays, €2,000–5,000 per sign plus service (quote-based)", "A third to a fifth of the price, no service contract, open data in"),
                     ("Paper timetable", "Free, out of date", "We show the same timetable, always current, plus live where it exists"),
                     ("Municipal pilot displays (Meisenheim, Ludwigsburg examples)", "Individual municipalities already trial e-paper stop displays", "Demand signal and a procurement precedent"),
                     ("DIY e-paper transit boards (the hallway-board family)", "Hobby builds", "Proof of the display idea; not an outdoor product")],
     "wedge": "price and honesty: a quarter of the agency display, no service contract, and a sign that says \"scheduled\" or \"live\" so the passenger can trust it.",
     "product_long": "- 7.5–13.3 inch e-paper, readable in sunlight, backlight for night, in a vandal-resistant IP65 housing on a standard pole clamp.\n- Solar panel and buffer cell sized for a northern winter at ten refreshes an hour (estimate; validate in December).\n- Cat-M modem with an operator SIM or the region's IoT SIM; LoRaWAN variant where a town network exists.\n- Firmware: GTFS static for the stop, GTFS-Realtime overlay when the feed carries that stop's trips, a \"scheduled / live\" label, disruption text, QR to the operator's app.\n- Fleet dashboard for the association: battery, last refresh, uptime; open API; no per-sign licence.",
     "econ": econ_table("120–180", "599–899", 15.0, 60.0, 8.0, 12.0, 15, "direct B2G, tender support and installation partner, ~€60", 60.0),
     "econ_note": "Lesson: the housing and the pole mount cost as much as the electronics; design one housing for two display sizes. Procurement support time is the hidden cost; price it into the pilot.",
     "gtm": "**First 100 customers:**\n\n1. Two transport associations with open GTFS-Realtime, found through their open-data portals, offered a paid ten-stop pilot.\n2. Municipalities that already trialled e-paper stop displays, offered the cheaper second generation.\n3. Dial-a-ride and community-bus operators that need a sign at a handful of stops.\n\n**Scale channels:** regional mobility programmes and funding calls, stop-furniture suppliers, the association's own roll-out plans.",
     "q1": "Kill-question conversations with four associations; works-like sign on PaperS3 + Unit CatM reading one region's GTFS and GTFS-RT; December solar test.",
     "q2": "Custom board, housing, pole mount; EVT 5 signs at real stops with one association.",
     "q3": "DVT; certification; 50 signs; first paid pilot shipped and installed.",
     "q4": "Second pilot; fleet dashboard; 200 signs; funding-call partnerships.",
     "team": "one embedded engineer, one backend developer (GTFS, dashboard), one founder for B2G sales; housing design and installation partner bought in.",
     "funding": "NRE €40k (board, housing tooling, mount) + certification €15k + first 200 signs landed ~€50k ≈ €105k; minus two pilots ~€16k ≈ €90k.",
     "risks": [("Regions without GTFS-Realtime at their stops", "Scope to regions that publish it; scheduled-only mode is honest and still useful; say which mode on screen"),
               ("Winter solar budget", "Measure in December before DVT; larger panel or mains option"),
               ("Vandalism and weather", "Polycarbonate window, tamper alert, replaceable front; warranty terms"),
               ("Procurement cycles of 6–18 months", "Paid pilots under tender thresholds first; partner with a stop-furniture supplier")],
     "boards_note": "The PaperS3 and PaperColor give the display path; the SIMCom A7672X hardware design is the openly mirrored reference for the cellular section; the DFRobot solar power manager covers the off-grid power path for prototypes.",
     "diagram": "  [solar panel] -> [solar power manager + LiFePO4 cell] -> [ESP32-S3]\n                                                            |  SPI\n  [Cat-M modem (A767x)] <-- GTFS / GTFS-RT every 6 min --> [e-paper 7.5–13.3\"]\n  [temp sensor] [tamper switch]        label on screen: SCHEDULED | LIVE",
     "bom": [("E-paper 7.5–13.3 inch + driver", "45.0", "size per stop"), ("ESP32-S3 module", "3.0", ""), ("Cat-M modem + antenna + SIM holder", "15.0", ""), ("Solar panel 10–20 W + power manager", "20.0", ""), ("LiFePO4 cell", "12.0", ""), ("IP65 housing + pole clamp + polycarbonate window", "60.0", "two display sizes, one housing family"), ("PCB, sensors, passives", "8.0", "")],
     "firmware": "- ESP-IDF; GTFS static parsed server-side per stop and pushed as a compact schedule; GTFS-RT polled server-side and pushed only when the stop's trips are in the feed.\n- Partial e-paper refresh; deep sleep between refreshes; battery and temperature telemetry.\n- Server: small open-source service per region (GTFS ingest, per-stop API, fleet dashboard); no per-sign licence.",
     "weeks": ["Interviews with associations; fake door for B2G", "Prototype on PaperS3 + CatM with one region's GTFS", "GTFS-RT overlay and the scheduled/live label", "Solar budget measurement", "Custom board v1", "Housing and mount design",
               "EVT 5 at real stops", "Association feedback; dashboard v0", "Housing tooling decision", "DVT signs", "Pre-compliance", "Certification; pilot contract"],
     "cert": CERT_BATT,
     "cheapest": "One PaperS3 in a weatherproof box at one rural stop for a month with the association's blessing, showing scheduled times; count the passengers who ask for it to stay.",
     "interview": "1) Which of your stops have any display today and what did it cost per stop? 2) Does your GTFS-Realtime feed cover rural lines; which operators are equipped? 3) Who decides on stop furniture and from which budget? 4) What would a sign need to do for you to put ten on poles? 5) At €799 per sign without a service contract, how many stops in a pilot?",
     "landing": "headline \"A departure sign every stop can afford.\" Bullets: timetable always, live where your buses report, solar, €799, no service contract. Button: request a pilot (B2G form).",
     "pass": "2 signed ten-stop pilots in regions with GTFS-RT within 8 weeks.",
     "production": PROD_STD + "\n- Outdoor: IP65 ingress test on samples, UV-stable window, salt-spray on the clamp if coastal.",
     "next": NEXT_STD},
    {"verdict": "UNCERTAIN",
     "summary": "A real technical blocker: live GTFS-Realtime requires on-board vehicle equipment that rural and small-contractor bus fleets often lack (confirmed in a Südtirol example), so buses without it show only scheduled times, in exactly the rural markets targeted. Municipal e-paper stop displays (Meisenheim, Ludwigsburg) and regional GTFS-RT open data (VBN) exist.",
     "risk": "The pitch was reworked before building: scheduled always, live where available, with the source labelled on screen; scope sales to regions that already publish GTFS-RT.",
     "correction": {"title": "Built with the research fix applied (November 2026)",
                    "text": "The research found that live departure data needs on-board equipment many rural fleets lack, so a sign promising live times everywhere would fail in its own target market. This pack is therefore scoped to \"scheduled always, live where the operator broadcasts it\", the sign labels which it shows, and the kill question only counts regions that already publish GTFS-Realtime for their stops. As researched November 2026 by web search; verify before relying on it."},
     "rows": [["Südtirol real-time caveat", "Buses without on-board equipment do not report live positions", "The 'live' promise cannot hold everywhere; pitch reworked"], ["Meisenheim, Ludwigsburg municipal display examples", "Municipalities trialling e-paper stop displays", "Demand and procurement precedent"], ["VBN GTFS-Realtime open data", "Regional live feed published openly", "Target regions exist"], ["Papercast, Luminator, ConnectPoint", "Agency displays, quote-based €2–5k", "Incumbents at a multiple of the target"]]})

# 5 ---------------------------------------------------------------------------
bf = [board("m5stack-unit-ultrasonic-i2c", "ultrasonic distance unit for the tank lid"),
      board("m5stack-unit-tof", "time-of-flight alternative for small tanks"),
      board("seeed-grove-ultrasonic-ranger", "open ultrasonic ranger reference circuit"),
      board("m5stack-atoms3-lite", "ESP32-S3 WiFi core"),
      board("m5stack-stamp-c6lora", "LoRa variant for tanks out of WiFi range"),
      board("m5stack-unit-oled", "local display at the tank or in the hallway")]
note, share = open_note(bf)
add({"slug": "oil-tank-eye", "title": "Tank Eye", "category": "Energy & solar",
     "pitch": "A heating-oil (or pellet, or rainwater) tank level sensor with a local display and WiFi or LoRa, no app account and no subscription.",
     "audience": "The roughly five million oil-heated homes in DE/AT/CH, holiday-home owners, small heating-oil dealers as a channel; Home Assistant users as the first buyers.",
     "why_now": "The two known connected tank sensors bill a subscription on top of the device, oil prices made households watch their tank, and the ESPHome community has built this sensor hundreds of times without anyone boxing it.",
     "built_from": bf,
     "whats_new": "A lid-mounted ultrasonic or ToF sensor with a tank-shape wizard (cylinder, cuboid, battery of tanks), a local display puck, WiFi with a local web page and MQTT, optional LoRa for the barn tank, consumption trend and a low-level alert by e-mail; no account.",
     "effort_weeks_est": "8", "bom_eur_est": "14–20", "price_eur_est": "79–99",
     "certification": "RED via module, EMC, EN 62368-1, RoHS, WEEE, CRA; explosion-safety (ATEX) status of a sensor in a heating-oil tank headspace must be verified before launch, not assumed.",
     "kill_question": "100 members of a German heating forum offered it at €89 with \"no account, no subscription\": 30 refundable deposits in 3 weeks.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 5},
     "tags": ["energy", "smart-home", "consumer", "wifi", "sensors"], "open_boards_note": note, "score_total": 18},
    {"problem": "Millions of households heat with oil and read the tank with a dipstick or a float gauge in the cellar; the connected sensors on the market charge a monthly fee for a number that changes once a day.",
     "customer": "Oil-heated households in DE/AT/CH (and pellet-store and rainwater-cistern owners with the same problem), holiday-home owners who want to know from afar, heating-oil dealers who would like to know when to call. The homeowner pays; Home Assistant users buy first.",
     "product": "A sensor that screws into a spare lid opening, a small display puck for the hallway, a local web page and MQTT, consumption trend and low-level alerts by e-mail, LoRa option for tanks out of WiFi range; no account, no fee.",
     "ask": "~€35–45k to certification and a first 1,000 units (estimate); forum pre-orders cover a third.",
     "problem_long": "Oilfox (device plus a yearly subscription) and Boilerjuice Connected (£75 plus £4.99 a month) have shown that people pay to see their tank from the phone, and that they resent the fee. On the Home Assistant and ESPHome forums the same device is built again and again from an ESP32 and an ultrasonic or ToF sensor; the threads are long because the tank-shape maths and the mounting are fiddly. A boxed version with a tank wizard is the missing product.",
     "who_pays": "**Who pays:** the homeowner (B2C) and the holiday-home owner; heating-oil dealers as a channel that may subsidise the device for the order signal. **Who uses:** everyone in the house, via the hallway puck.",
     "market": "- **TAM:** ~5M oil-heated homes in DE plus AT/CH, plus pellet stores and cisterns. Theoretical €400M+.\n- **SAM:** households that already own a smart-home device or buy from an online heating-oil dealer: estimate 1M → €90M.\n- **SOM (3 yrs):** 20,000–40,000 units; year-1: 2,000–4,000 through forums, Home Assistant channels and one dealer partnership.",
     "searches": 3,
     "competition": [("Oilfox", "Connected tank sensor; device plus subscription (about £6 a month, research Nov 2026)", "No fee, no account; local data"),
                     ("Boilerjuice Connected (UK)", "£75 + £4.99 a month", "Same"),
                     ("Watchman Sonic Advanced", "Ultrasonic sender + receiver, no app", "We add the trend, the alert and MQTT at a similar price"),
                     ("Tecson and similar ultrasonic gauges", "€150–250, wired display", "Half the price with WiFi"),
                     ("ESPHome / Home Assistant DIY builds (simon42, rogerfrost and many threads)", "Free if you have a weekend", "The customer wants the box and the tank wizard")],
     "wedge": "the DIY device everyone builds, boxed, with a tank-shape wizard and no subscription.",
     "product_long": "- Sensor head for the standard 2-inch (G2) lid opening and a universal flange; ultrasonic for large tanks, ToF for small ones; sealed against vapour.\n- Tank wizard: cylinder, cuboid, battery of tanks, custom table; litres and days-to-empty.\n- Hallway puck with an OLED showing litres and trend; WiFi local page; MQTT; e-mail alert at a set level; no cloud.\n- LoRa variant for the barn or the garden cistern.\n- Pellet-store and rainwater modes are the same device with a different wizard.",
     "econ": econ_table("14–20", "79–99", 2.5, 4.5, 2.0, 2.0, 9, "direct and dealer channel, ~€8", 8.0),
     "econ_note": "Lesson: the sensor head and the puck are two small enclosures; keep the puck optional to hit €79 for the Home Assistant crowd.",
     "gtm": "**First 100 customers:**\n\n1. Pre-orders from two German heating forums and the Home Assistant community.\n2. One online heating-oil dealer offering it to customers.\n3. Holiday-home owners via vacation-rental forums.\n\n**Scale channels:** heating-oil dealers (they want the order signal), smart-home retailers, heating installers.",
     "q1": "Kill-question pre-orders; works-like prototype on Unit Ultrasonic + AtomS3 on a real tank; tank wizard.",
     "q2": "Custom PCB and sensor head; EVT 30 in forum members' cellars; ATEX question answered with a notified body or a test house.",
     "q3": "DVT; certification; 500 units; pre-orders shipped.",
     "q4": "Dealer partnership; LoRa variant; 2,000 units.",
     "team": "one embedded engineer, one founder; mechanical design of the sensor head bought in.",
     "funding": "NRE €15k + certification and the ATEX assessment €10–14k + first 1,000 units landed ~€22k ≈ €50k; minus pre-orders ~€12k ≈ €38k.",
     "risks": [("Explosion-safety rules for a sensor in a tank headspace", "Verify before launch: heating oil's flash point is above 55 °C, but confirm whether any ATEX zoning applies to the lid opening; design for intrinsically low energy either way; do not claim it is fine until a test house says so"),
               ("Vapour fouls the sensor", "Sealed head; ToF behind a window; field test over a winter"),
               ("Oilfox cuts its fee", "Our wedge is also local data and the puck; stay cheaper"),
               ("Tank-shape maths wrong", "Wizard with a dipstick calibration step")],
     "boards_note": "The Seeed ultrasonic ranger publishes its schematic; the M5Stack units and the AtomS3 give the fastest prototype; the Stamp C6LoRa (open files) is the LoRa variant's core.",
     "diagram": "  TANK LID: [ultrasonic / ToF sensor, sealed] -> [ESP32-S3] -> WiFi -> local page, MQTT, e-mail alert\n                                                   |  LoRa variant: [Stamp C6LoRa] -> gateway in the house\n  HALLWAY: [OLED puck: litres, trend, days left]",
     "bom": [("Ultrasonic or ToF sensor", "3.0", "ToF for small tanks"), ("ESP32-S3 module", "2.5", ""), ("Sensor head enclosure + G2 thread + seal", "4.5", ""), ("Hallway puck: OLED + ESP32-C3 + enclosure", "6.0", "optional"), ("PCB, USB-C, passives", "2.0", "")],
     "firmware": "- ESPHome-compatible firmware (the community can keep using its own) plus a stock firmware with the wizard and the local page.\n- Median filtering, temperature compensation, tank geometry tables; MQTT discovery for Home Assistant.\n- E-mail alert through the user's own SMTP or a free relay; no cloud of ours.",
     "weeks": ["Forum pre-orders live", "Prototype on a real tank", "Tank wizard and filtering", "Sensor head design", "ATEX question to a test house", "Custom PCB v1",
               "EVT 30 in volunteers' cellars", "Winter fouling check", "Puck design", "DVT", "Pre-compliance", "Certification; shipping plan"],
     "cert": CERT_STD + "\n- **Explosion safety:** obtain a written assessment for the sensor position in a heating-oil tank before sale; if zoning applies, the design changes (intrinsically safe) or the product is scoped to pellet and water tanks first.",
     "cheapest": "Post the prototype and a 60-second video in two heating forums with a €89 pre-order link and \"no account, no subscription\" in the title.",
     "interview": "1) How do you check your tank today and how often? 2) Have you looked at Oilfox or similar; what stopped you? 3) What would you do with a daily consumption number? 4) Where is the tank: WiFi reach, lid openings free? 5) At €89 once, would you order?",
     "landing": "headline \"See your tank. No app account, no monthly fee.\" Bullets: fits a spare lid opening; litres and days left in the hallway; works with Home Assistant. Button: refundable €20 deposit.",
     "pass": "30 deposits from 100 forum members within 3 weeks.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "Oilfox is confirmed subscription-based (about £6 a month) and Boilerjuice Connected costs £75 plus £4.99 a month, a real no-subscription wedge; the ESPHome / Home Assistant DIY precedent is strong and active (simon42, rogerfrost and multiple build threads).",
     "risk": "Explosion-safety (ATEX) requirements for a sensor in an oil-tank headspace are unverified; a compliance check is needed before launch and the pack does not claim it is fine.",
     "rows": [["Oilfox", "Device + subscription (~£6/month)", "Incumbent with the fee"], ["Boilerjuice Connected", "£75 + £4.99/month", "Incumbent with the fee"], ["Watchman Sonic Advanced", "Ultrasonic sender + receiver", "Incumbent without app"], ["simon42 / rogerfrost ESPHome builds and Home Assistant threads", "DIY tank sensors", "Strong demand signal, no boxed product"]]})

# 6 ---------------------------------------------------------------------------
bf = [board("m5stack-papers3", "ESP32-S3 e-paper device for the sign"),
      board("m5stack-coreink", "small e-paper variant for narrow door frames"),
      board("m5stack-papercolor", "colour variant for status colours")]
note, share = open_note(bf)
add({"slug": "room-door-sign", "title": "Door Sign, No Subscription", "category": "Displays",
     "pitch": "An e-paper meeting-room sign that reads any CalDAV, Google or Microsoft 365 calendar directly, runs for months on a charge, and never bills per room.",
     "audience": "SMEs, co-working spaces, schools, churches and community centres that book rooms; IT resellers and managed-service providers as the channel.",
     "why_now": "Room signs from Joan and Evoko bill per device per month or cost up to several thousand euros; the e-paper plus calendar build is one of the most repeated Home Assistant and ESPHome projects; the devices in the catalogue already have the display, battery and radio.",
     "built_from": bf,
     "whats_new": "Firmware that talks to CalDAV, Google Calendar and Microsoft Graph directly from the device or through a small self-hosted bridge, a one-time setup page, book-now and end-early buttons, 2–4 months on a charge, a magnetic or glass mount; no per-room fee.",
     "effort_weeks_est": "10", "bom_eur_est": "35–55", "price_eur_est": "149–199",
     "certification": "RED via module, EMC, EN 62368-1, RoHS, WEEE, CRA; Battery Regulation / UN 38.3 for the cell.",
     "kill_question": "Do 10 co-working spaces or SMEs pre-order 3 signs each at €169 from a landing page within 30 days? Pass = 10 orders of 3 or more.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 5},
     "tags": ["displays", "e-paper", "b2b", "office", "wifi"], "open_boards_note": note, "score_total": 18},
    {"problem": "Every office with more than two meeting rooms wants a sign on the door that shows whether the room is free and lets you grab it, and the products that do it bill a subscription per room or cost as much as a laptop.",
     "customer": "SMEs with 3–30 rooms, co-working operators, schools and universities, churches and community centres with bookable halls; IT resellers and managed-service providers who install for them. Office management or IT pays.",
     "product": "A 4.7–7.5 inch e-paper sign with a battery that lasts months, reading the room's calendar from CalDAV, Google or Microsoft 365, showing free/busy and the next bookings, with book-now and end-early buttons; mounts on glass or wall; no per-room fee ever.",
     "ask": "~€45–60k to certification and a first 1,000 units (estimate); pre-orders of 3+ cover a third.",
     "problem_long": "Joan charges per device per month; Evoko's Naso costs $800–3,600 plus licensing; both work well and both are the reason small organisations use paper on the door. The DIY world has solved the display side many times over (ESPHome-ePaper-Calendar and its relatives). What stops those builds becoming products is not hardware but the calendar plumbing: Microsoft 365 and Google app consent, the IT security review, and tenant admin approvals. That is the real work in this pack, and the real sales bottleneck.",
     "who_pays": "**Who pays, B2B:** office management or IT; resellers and MSPs buy ten at a time for their customers. **Who uses:** everyone walking past the door; the sign must be readable at three metres and obvious without a manual.",
     "market": "- **TAM:** meeting rooms in EU organisations with 10–500 staff: estimate 5–8M rooms. Theoretical €1B at €169.\n- **SAM:** rooms in organisations already on Microsoft 365 or Google Workspace with an IT contact who installs things: estimate 1M rooms → €170M.\n- **SOM (3 yrs):** 15,000–30,000 signs through direct sales and 20–50 resellers; year-1: 1,500–3,000.",
     "searches": 3,
     "competition": [("Joan", "E-paper room sign; about €5–20 per device per month (research, Nov 2026)", "No subscription; comparable hardware"),
                     ("Evoko Naso (Biamp)", "$800–3,600 per device plus licensing", "A tenth of the price"),
                     ("Meetio, Robin, tablets on the wall", "Subscription software on an iPad or Android panel", "No tablet, no mains cable, no fee"),
                     ("ESPHome-ePaper-Calendar and similar DIY", "Free if you can run Home Assistant and register an app", "We do the calendar plumbing and the IT paperwork once, for everyone")],
     "wedge": "no per-room fee, months of battery, and the calendar integrations already approved and documented for IT, which is what the DIY builds cannot offer an office.",
     "product_long": "- 4.7-inch (PaperS3) and 7.5-inch sizes; status colour band (PaperColor variant) or LED edge for free/busy visible down the corridor.\n- Calendar: CalDAV direct; Google and Microsoft 365 through a small self-hosted or hosted bridge with a published app registration and security documentation; per-room service accounts.\n- Book-now (15/30/60 min) and end-early buttons; check-in to release no-shows (optional).\n- 2–4 months per charge at 5-minute refreshes (estimate); USB-C; glass mount with VHB, wall plate with screws.\n- Fleet page: battery, last sync, firmware; open API; no per-room licence.",
     "econ": econ_table("35–55", "149–199", 4.0, 8.0, 3.0, 3.0, 10, "direct and reseller margin, ~€20", 20.0),
     "econ_note": "Lesson: the e-paper panel is half the BOM; the 7.5-inch version needs a higher price. The reseller margin is the cost of scaling without a sales team.",
     "gtm": "**First 100 customers:**\n\n1. Ten co-working spaces and SMEs from a landing page and direct outreach, each buying three signs.\n2. Two MSPs that install them for their customers.\n3. One school or university testing the CalDAV path.\n\n**Scale channels:** MSPs and IT resellers, office-furniture dealers, Microsoft and Google marketplace listings once the app registrations are verified.",
     "q1": "Kill-question pre-orders; works-like sign on PaperS3 with CalDAV; Microsoft and Google app registrations started (the long pole).",
     "q2": "Bridge service; verified app publisher status; EVT 20 signs in three offices; security documentation written.",
     "q3": "DVT; certification; 500 signs; reseller programme.",
     "q4": "7.5-inch size; 2,000 signs; marketplace listings.",
     "team": "one embedded engineer, one backend developer who has done OAuth app verification before, one founder selling to offices and MSPs.",
     "funding": "NRE €18k + app verification, security review and pen-test €12k + certification €8k + first 1,000 signs landed ~€45k ≈ €83k; minus pre-orders ~€25k ≈ €58k.",
     "risks": [("Microsoft 365 / Google app consent and IT security review stall sales", "Start verification in month one; publish a security whitepaper; offer the CalDAV and self-hosted bridge path for strict IT"),
               ("Battery life claims", "Measure at 5-minute refresh over a month before claiming; show the number on the fleet page"),
               ("Joan drops its price", "Our wedge is also the no-licence model; keep the hardware margin healthy"),
               ("Glass mounting failures", "VHB spec and a wall plate; replacement mounts in the box")],
     "boards_note": "All three are M5Stack e-paper devices with published module files (electronics not open); the first product can ship on a customised PaperS3 before a custom board exists.",
     "diagram": "  [calendar: CalDAV | Google | Microsoft 365] -> [bridge service (self-hosted or hosted)] -> WiFi -> [ESP32-S3 + e-paper 4.7\"/7.5\"]\n                                                                                              |\n                                                   [buttons: book 15/30/60, end early]   [battery 2–4 months, USB-C]",
     "bom": [("E-paper 4.7 inch + driver (7.5 inch: +€15)", "18.0", ""), ("ESP32-S3 module", "2.5", ""), ("Li-ion cell 2,000–3,000 mAh + charger", "5.0", ""), ("Enclosure + glass/wall mount", "8.0", ""), ("Buttons, LED edge, PCB, USB-C", "4.0", ""), ("Packaging", "2.0", "")],
     "firmware": "- ESP-IDF; deep sleep; partial refresh; HTTPS to the bridge; buttons wake the device.\n- Bridge: small open-source service (CalDAV client, Google Calendar API, Microsoft Graph) with per-room tokens; self-host or our hosting at cost; fleet page.\n- App registrations: verified publisher on both platforms; documented scopes (calendar read/write for the room resource only).",
     "weeks": ["Pre-orders live; interviews with office managers and two MSPs", "Prototype on PaperS3 + CalDAV", "Bridge v0 with Google and Microsoft sandbox tenants", "App registrations and verification submitted", "Enclosure and mount design", "Custom board or customised PaperS3 decision",
               "EVT 20 in three offices", "Battery measurement month", "Security documentation", "DVT", "Pre-compliance", "Certification; reseller kit"],
     "cert": CERT_BATT,
     "cheapest": "Three PaperS3 signs with CalDAV on three doors of one co-working space for a month; ask the operator whether they would buy ten at €169.",
     "interview": "1) How do people find a free room today and what goes wrong? 2) Have you priced Joan or Evoko; what stopped you? 3) Who would approve a calendar integration in your IT; what would they ask for? 4) How many rooms and doors? 5) At €169 per sign with no fee, how many?",
     "landing": "headline \"The room sign without the subscription.\" Bullets: months on a charge; Microsoft 365, Google, CalDAV; book from the door; €169. Button: pre-order 3 (refundable deposit).",
     "pass": "10 orders of 3 or more within 30 days.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "Joan (about €5–20 per device per month) and Evoko Naso ($800–3,600 plus licensing) are confirmed subscription-attached, a real wedge; the DIY precedent is confirmed (ESPHome-ePaper-Calendar and relatives).",
     "risk": "The risk is the sales cycle, not the market: Microsoft 365 / Google app consent and IT security review will be the real bottleneck.",
     "rows": [["Joan", "E-paper room sign, ~€5–20/device/month", "Incumbent with subscription"], ["Evoko Naso (Biamp)", "$800–3,600 + licensing", "Incumbent at a multiple of the target"], ["ESPHome-ePaper-Calendar", "DIY e-paper calendar sign", "Demand signal, no boxed product"]]})

# 7 (fix: hobbyist potters only) ----------------------------------------------
bf = [board("m5stack-unit-kmeter-iso", "isolated K-type thermocouple input for the kiln probe"),
      board("m5stack-stamplc", "DIN-rail PLC-style controller core"),
      board("m5stack-stamplc-ac", "mains-powered StamPLC variant"),
      board("seeed-grove-solid-state-relay-v2", "pilot-signal SSR reference; the kiln load goes through an external contactor"),
      board("m5stack-unit-buzzer", "end-of-firing and fault alarm")]
note, share = open_note(bf)
add({"slug": "kiln-mind", "title": "Kiln Mind", "category": "Maker tools",
     "pitch": "A retrofit controller and logger for the home potter's small electric kiln: ramp-and-hold programmes, a phone notification when the firing is done, and a log of every firing, for individual hobbyists, not schools or studios.",
     "audience": "Individual hobbyist potters with a small electric kiln at home (DE/UK/NL/Nordics), kiln repair technicians as installers; explicitly not schools, colleges or commercial studios, where insurance terms rule out non-listed controllers.",
     "why_now": "Hobby kilns are booming with the ceramics revival, the replacement controllers cost $388–699 and are sold through dealers, the catalogue has an isolated thermocouple input and a DIN controller ready, and the research confirmed the insurance problem that keeps this a hobbyist product.",
     "built_from": bf,
     "whats_new": "A controller box with an isolated thermocouple input, programme editor on the phone over local WiFi, cone-table presets, a pilot output to the kiln's existing contactor fitted by a technician, over-temperature and stuck-relay watchdogs, and a log of every firing; sold with an installer note and a clear statement that it is not a listed controller for institutions.",
     "effort_weeks_est": "14", "bom_eur_est": "45–70", "price_eur_est": "249–349",
     "certification": "LVD / EN 60730-1 class for a mains-connected temperature controller, EMC, RED (WiFi), RoHS, WEEE, CRA; installer-fitted; the kiln contactor and wiring stay the installer's responsibility.",
     "kill_question": "Do 10 individual hobbyist potters (not schools or studios) buy at €299 after seeing one logged firing on a kiln like theirs, and does a kiln repair technician agree to fit it? Pass = 10 orders and 1 installer in 8 weeks.",
     "open_files_share": share, "scores": {"demand": 3, "buildability": 4, "margin": 4, "speed": 3},
     "tags": ["maker", "consumer", "wifi", "heating", "tools"], "open_boards_note": note, "score_total": 14},
    {"problem": "Home potters firing a small electric kiln either babysit a manual kiln-sitter or pay $388–699 for a replacement controller sold through dealers; the ones who want a log and a phone notification have to build it.",
     "customer": "Individual hobbyist potters with a kiln at home. Not schools, colleges or commercial studios: research found that non-listed controllers are implicated in insurance disputes, so institutions must buy a listed controller, and this pack says so.",
     "product": "A retrofit controller box with an isolated thermocouple input, phone programme editor over local WiFi, cone presets, a pilot output to the kiln's existing contactor fitted by a technician, watchdogs, a buzzer and a firing log; sold with an installer note and a clear scope statement.",
     "ask": "~€55–70k to certification and a first 500 units (estimate); the certification line is the big one.",
     "problem_long": "A kiln firing is a ten-hour ramp-and-hold profile; getting it right decides the result, and knowing it has finished decides whether you sleep. Replacement controllers from Skutt and Bartlett cost $388–699 and are sold and fitted through dealers; the DIY alternatives on forums work but are explicitly not listed for safety, and the Digitalfire community notes that such controllers are implicated in fire-insurance disputes. That settles the market: a safety-certified, installer-fitted controller for the individual hobbyist, scoped away from institutions whose insurers require listed equipment.",
     "who_pays": "**Who pays:** the hobbyist potter (B2C), typically after the second kiln or the first ruined glaze firing; the kiln repair technician who fits it is the channel. **Who does not:** schools and studios, by design, until a listed version exists.",
     "market": "- **TAM:** hobby electric kilns in private hands in the EU: estimate 150,000–300,000. Theoretical €50–90M.\n- **SAM:** owners of manual or ageing controllers who follow pottery communities online: estimate 50,000 → €15M.\n- **SOM (3 yrs):** 3,000–5,000 units through communities and technicians; year-1: 400–600.",
     "searches": 3,
     "competition": [("Skutt KilnMaster (KMT) kit", "$579–650 (research, Nov 2026)", "Half the price, with the log and the notification"),
                     ("Bartlett Genesis 2.0", "$388–699 replacement controller", "Similar to lower price; local WiFi and log included"),
                     ("Nabertherm and kiln-maker controllers", "Bundled with new kilns, quote-based", "Different purchase moment"),
                     ("DIY PID / Arduino kiln controllers", "Forum builds, not listed", "We are certified and installer-fitted; same price class as the parts plus a weekend")],
     "wedge": "a certified, installer-fitted controller with the log and the phone notification, at or below the replacement-controller price, sold honestly to hobbyists only.",
     "product_long": "- Isolated K-type (and S-type option) input; 0–1,300 °C; cone tables; ramp/hold editor on a phone over local WiFi; no cloud.\n- Pilot output (SSR or relay) to the kiln's existing contactor; the controller never carries the element current.\n- Watchdogs: over-temperature, thermocouple break, stuck-relay detection (temperature rising with output off), maximum firing time; mains-independent buzzer.\n- Firing log with the full curve, exportable; notification by e-mail or local push when done or faulted.\n- Installer note and a scope statement in the box: for private hobby kilns; institutions require a listed controller.",
     "econ": econ_table("45–70", "249–349", 6.0, 10.0, 3.0, 4.0, 18, "direct and technician channel, ~€25", 25.0),
     "econ_note": "Lesson: certification dominates the first run (a mains-connected temperature controller is tested to a demanding standard); at 1k units the product barely breaks even, at 5k it works. Do not launch without the certification quote in hand.",
     "gtm": "**First 100 customers:**\n\n1. Ten hobbyists from pottery communities who send a video of their kiln and their last firing problem.\n2. Two kiln repair technicians who fit it and recommend it.\n3. Pottery supply shops' hobby customers.\n\n**Scale channels:** kiln technicians, pottery supply shops, ceramics communities and courses.",
     "q1": "Kill-question conversations; works-like controller on KMeter-ISO + StamPLC driving a contactor on a technician's bench kiln; certification quotes from two labs.",
     "q2": "Custom board; enclosure; EVT 10 with hobbyists and a technician; watchdog tests.",
     "q3": "DVT; certification (the long pole); 200 units.",
     "q4": "Technician network; 500 units; S-type input option.",
     "team": "one embedded engineer with functional-safety instincts, one founder from the ceramics world; a technician partner.",
     "funding": "NRE €20k + certification €15–20k + first 500 units landed ~€30k ≈ €70k; minus pre-orders ~€10k ≈ €60k.",
     "risks": [("Insurance and liability if a kiln is damaged", "Scope to hobbyists; installer-fitted; watchdogs; written scope statement; product liability insurance priced in"),
               ("Certification cost and time for a mains temperature controller", "Quote before building; design to the standard from day one"),
               ("Hobbyists happy with a kiln-sitter", "Sell the log and the notification; target owners who ruined a firing"),
               ("Technicians prefer dealer controllers", "Margin for the installer; simple fitting")],
     "boards_note": "The KMeter-ISO is the isolated thermocouple front end; the StamPLC family provides the DIN-rail controller; the Seeed SSR board (open schematic) is the pilot-output reference. The kiln contactor is bought and fitted by the technician.",
     "diagram": "  [K-type thermocouple] -> [KMeter-ISO, isolated] -> [StamPLC controller] -> pilot -> [kiln's own contactor] -> elements\n                                                        |  watchdogs: over-temp, TC break, stuck relay, max time\n  [phone, local WiFi: programmes, log]          [buzzer, mains-independent]",
     "bom": [("Isolated thermocouple input (MAX31855-class + isolation)", "6.0", ""), ("ESP32-S3 controller board (StamPLC-class)", "12.0", ""), ("SSR / relay pilot output", "4.0", "contactor external"), ("Power supply (mains to 5 V, certified module)", "6.0", ""), ("Enclosure, DIN clips, terminals", "12.0", ""), ("Buzzer, display, PCB, passives", "8.0", "")],
     "firmware": "- ESP-IDF; PID with ramp/hold scheduler; cone tables; watchdogs in a separate task with hardware output disable.\n- Local web app for programmes and logs; MQTT optional; e-mail / local push when done.\n- Logging of every firing to flash with export.",
     "weeks": ["Interviews with hobbyists and a technician; fake door", "Prototype on bench kiln", "Watchdog design and tests", "Certification quotes and standard study", "Custom board v1", "Enclosure",
               "EVT 10 with hobbyists", "Firing logs reviewed", "Design freeze for the lab", "DVT", "Pre-compliance and safety tests", "Certification submission"],
     "cert": CERT_MAINS,
     "cheapest": "Fit the prototype to one technician's bench kiln, log three firings, and show the log to ten hobbyists with a €299 price; ask who orders.",
     "interview": "1) Tell me about your kiln and your last ruined firing. 2) How do you know when it is done today? 3) Have you priced a replacement controller; what stopped you? 4) Who services your kiln? 5) At €299 fitted by your technician, would you order?",
     "landing": "headline \"Your kiln, programmed from the sofa, logged forever. For home potters.\" Bullets: fitted by your kiln technician; watchdogs; €299; not for schools or studios (listed controllers required). Button: refundable €30 deposit.",
     "pass": "10 hobbyist orders and one technician agreement within 8 weeks.",
     "production": PROD_STD + "\n- Safety: 100% hi-pot and functional watchdog test on the line; installer note in every box.",
     "next": NEXT_STD},
    {"verdict": "UNCERTAIN",
     "summary": "The price gap is real (Skutt KMT kit $579–650, Bartlett Genesis 2.0 $388–699 against the €249–349 target), but an independent source (the Digitalfire community) confirms DIY kiln controllers are not CSA/UL listed and are implicated in fire-insurance disputes, a real threat to institutional sales regardless of price.",
     "risk": "Scoped before building to individual hobbyist potters only; schools and studios are excluded in the pack text until a listed version exists.",
     "correction": {"title": "Built with the research fix applied (November 2026)",
                    "text": "The research found that non-listed kiln controllers are implicated in fire-insurance disputes, which rules out schools, colleges and commercial studios as buyers regardless of price. This pack is therefore scoped to individual hobbyist potters, sold installer-fitted and certified as a mains temperature controller, with the scope stated on the landing page and in the box. As researched November 2026 by web search; verify before relying on it."},
     "rows": [["Skutt KilnMaster (KMT) kit", "$579–650", "Incumbent, about double the target"], ["Bartlett Genesis 2.0", "$388–699", "Incumbent, similar to higher price"], ["Digitalfire community on DIY controllers", "Not CSA/UL listed; implicated in insurance disputes", "Rules out institutional buyers; scope fixed"]]})

# 8 ---------------------------------------------------------------------------
bf = [board("seeed-grove-temperatureandhumidity-sensor-hdc1000", "HDC1000 temperature/humidity reference circuit"),
      board("seeed-grove-temptureandhumidity-sensor-high-accuracy-andmini-v1-0", "high-accuracy T/RH alternative"),
      board("m5stack-unit-env-pro", "BME688-class environmental unit for the prototype"),
      board("seeed-grove-uv-sensor", "UV sensor reference circuit"),
      board("m5stack-unit-dlight", "lux measurement"),
      board("m5stack-stamp-c6lora", "open ESP32-C6 + LoRa core for the logger"),
      board("m5stack-unit-lorawan-eu868", "EU868 LoRaWAN module for the prototype run")]
note, share = open_note(bf)
add({"slug": "vitrine-log", "title": "Vitrine Log", "category": "LoRaWAN & building IoT",
     "pitch": "A showcase and archive climate logger (temperature, humidity, lux, UV) over LoRaWAN or BLE that produces the loan-ready PDF report lenders ask for, at a third of institutional logger prices.",
     "audience": "Regional and university museums, archives, instrument and art collections, churches holding artworks; conservators and registrars; the museum's collections budget pays.",
     "why_now": "Loan agreements routinely require continuous climate records (the UK Government Indemnity Scheme is the citable case, currently under review), institutional loggers cost £487–617 each plus software, and the sensors are catalogue parts.",
     "built_from": bf,
     "whats_new": "A small logger with calibrated T/RH, lux and UV sensors, two years on a cell, LoRaWAN or BLE readout, and a report generator that outputs the per-object climate PDF a lender's registrar expects (ranges, excursions, graphs) with no per-logger software licence.",
     "effort_weeks_est": "10", "bom_eur_est": "25–40", "price_eur_est": "149–199",
     "certification": "RED (LoRa EN 300 220 / BLE) via module, EMC, EN 62368-1, RoHS, WEEE, CRA; Battery Regulation for the lithium cell.",
     "kill_question": "Do 3 regional museums buy 10 loggers each at €169 after one loan cycle with the PDF report? Pass = 3 orders in 10 weeks.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 4},
     "tags": ["building", "lorawan", "b2b", "sensors", "compliance", "museum"], "open_boards_note": note, "score_total": 17},
    {"problem": "Museums must prove the climate around borrowed and owned objects, lenders ask for continuous records as a loan condition, and the institutional loggers that produce them cost £487–617 each plus annual software, so small museums log with a pen or borrow a logger for the loan.",
     "customer": "Regional, municipal and university museums, archives, historic houses, instrument collections and churches that lend or borrow objects; conservators and registrars specify, the collections budget pays.",
     "product": "A palm-sized logger (T, RH, lux, UV) with two years on a cell, LoRaWAN or BLE readout, calibration certificate, and a report tool that produces the per-object climate PDF a lender's registrar expects; no per-logger licence.",
     "ask": "~€45–60k to certification and a first 1,000 loggers (estimate); three museum orders cover a third.",
     "problem_long": "The UK Government Indemnity Scheme (National Heritage Act 1980) genuinely requires relative humidity, temperature and light monitoring for the loan period; the specific environmental-conditions rule has been reported under active review (suspended through at least March 2023 with its status unclear), so verify the current requirement before leaning on it as a hard mandate. Lender loan policies (the Walters Art Museum's is a public example) ask for the same records regardless. The incumbent loggers (Testo 160 THL at about £487–617, Hanwell, ELTEK) are good and institutional; small museums own two and need twenty.",
     "who_pays": "**Who pays, B2B/B2G:** the museum's collections or facilities budget; a loan can also carry the cost into the exhibition budget. **Who uses:** the registrar and conservator; the report must look like what they already send.",
     "market": "- **TAM:** ~20,000 museums in Europe plus archives and historic houses; 10–50 loggers each in the professional tier. Theoretical €50–100M.\n- **SAM:** museums that lend and borrow and lack a monitoring system: estimate 5,000 institutions × 15 loggers → €13M.\n- **SOM (3 yrs):** 8,000–15,000 loggers; year-1: 1,000–1,500 across 50–100 museums.",
     "searches": 3,
     "competition": [("Testo 160 THL", "Institutional T/RH/lux/UV logger; about £487–617 (research, Nov 2026)", "A third of the price with the same four quantities and the report"),
                     ("Hanwell, ELTEK, Meaco", "Museum monitoring systems with receivers and annual software", "No per-logger licence; LoRaWAN uses the building's own gateway"),
                     ("Blue Maestro and consumer BLE loggers", "Cheap T/RH only, phone app", "No lux/UV, no calibration, no loan report"),
                     ("Pen and paper / borrowed logger for the loan", "Free", "The report generator is the product")],
     "wedge": "the loan report at a third of the institutional price, four quantities in one logger, no software licence.",
     "product_long": "- T/RH (±0.2 °C / ±2% RH class), lux and UV sensors; calibrated per unit with a certificate; two-year cell (estimate at 10-minute logging).\n- LoRaWAN (museum gateway or TTN) or BLE readout by phone for museums without a network; local server or hosted at cost.\n- Report generator: per object or case, date range, set-point bands, excursions, graphs, PDF matching the registrar's expectations; CSV export.\n- Discreet case in white or black, magnet and museum-putty mounts, no blinking lights in the vitrine.",
     "econ": econ_table("25–40", "149–199", 3.5, 5.0, 2.5, 3.0, 10, "direct to museums and conservation suppliers, ~€15", 15.0),
     "econ_note": "Lesson: the calibration step is a real production cost (a chamber and an hour per batch); price it in and sell the yearly re-calibration as a service.",
     "gtm": "**First 100 customers:**\n\n1. Three regional museums with upcoming loans, offered ten loggers and the report for one loan cycle.\n2. Conservators' associations and museum federations (NEMO members, national museum associations) for newsletters and conferences.\n3. Conservation suppliers as resellers.\n\n**Scale channels:** museum federations, conservation suppliers, LoRaWAN integrators working with municipalities.",
     "q1": "Kill-question conversations with registrars; works-like logger on Stamp C6LoRa + HDC1000 + UV + DLight; report generator v0 with one museum's loan template.",
     "q2": "Custom PCB; calibration procedure; EVT 30 in three museums; BLE variant.",
     "q3": "DVT; certification; 500 loggers; first three orders shipped with reports.",
     "q4": "Conservation-supplier listing; 1,500 loggers; re-calibration service.",
     "team": "one embedded engineer, one developer for the report tool, one founder who speaks to registrars; calibration set-up bought in.",
     "funding": "NRE €16k + calibration rig €6k + certification €9k + first 1,000 loggers landed ~€35k ≈ €66k; minus museum pre-orders ~€15k ≈ €50k.",
     "risks": [("The GIS environmental rule is under review", "Do not sell on the mandate; sell on lenders' loan conditions, which exist regardless; verify the current GIS text before quoting it"),
               ("Sensor drift over two years", "Calibration certificate; re-calibration service; sensor choice"),
               ("Museums have no LoRaWAN", "BLE readout by phone; gateway bundle with a municipal network"),
               ("Report format rejected by a lender", "Build it with two registrars; keep it editable")],
     "boards_note": "The Seeed sensor boards publish schematics; the Stamp C6LoRa (open PCB and schematic) is the core; the M5Stack units are the quickest prototype path for lux and the environmental sensor.",
     "diagram": "  [T/RH sensor] [lux sensor] [UV sensor] -> [ESP32-C6 + LoRa (Stamp C6LoRa)] -> LoRaWAN gateway / TTN  or  BLE -> phone\n                                                   |  [cell, 2 years]  [microSD backup]\n  SERVER: per-object records -> report generator -> loan PDF, CSV",
     "bom": [("T/RH sensor (HDC1000 / SHT4x class)", "2.5", ""), ("Lux + UV sensors", "3.0", ""), ("ESP32-C6 + LoRa module", "6.0", ""), ("Lithium cell (AA-class, 2 years)", "3.0", ""), ("Enclosure, mounts", "5.0", ""), ("PCB, microSD, passives", "4.0", ""), ("Calibration (labour share)", "4.0", "")],
     "firmware": "- ESP-IDF; 10-minute logging to flash and uplink; LoRaWAN class A; BLE advertising with last values and a connect-to-download mode.\n- Server: open-source ingest, per-object assignment, excursion rules, PDF generation; hosted at cost or self-hosted.\n- Calibration constants per unit in NVS; certificate PDF generated at production.",
     "weeks": ["Interviews with registrars; fake door", "Prototype logger", "Report generator v0 from a real loan template", "Calibration procedure", "Custom PCB v1", "Enclosure",
               "EVT 30 in three museums", "One loan cycle with reports", "BLE variant", "DVT", "Pre-compliance", "Certification; order fulfilment"],
     "cert": CERT_BATT,
     "cheapest": "Five prototypes in one museum's vitrines for a loan period, the report delivered to the lender; ask the registrar whether they would buy ten at €169.",
     "interview": "1) What do lenders ask you for and how do you produce it today? 2) How many loggers do you own and what did they cost with software? 3) Who decides and from which budget? 4) What would make a conservator distrust a cheaper logger? 5) At €169 with a calibration certificate and the report, how many?",
     "landing": "headline \"The loan report, from a €169 logger.\" Bullets: temperature, humidity, lux, UV; two years on a cell; LoRaWAN or phone; PDF your lender accepts. Button: request a trial set (B2B).",
     "pass": "3 orders of 10 within 10 weeks.",
     "production": PROD_STD + "\n- Calibration batch record per unit; certificate in the box.",
     "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "The UK Government Indemnity Scheme (National Heritage Act 1980) genuinely requires RH, temperature and light monitoring for loan periods, a citable requirement, and Testo 160 THL (about £487–617) confirms a 2–3× price gap. The specific GIS environmental-conditions rule is reported under active review (suspended through at least March 2023, status unclear).",
     "risk": "Verify current GIS requirements before leaning on them as a hard mandate; lenders' own loan conditions carry the demand regardless.",
     "rows": [["UK Government Indemnity Scheme (ICOM UK on the GIS review)", "Climate monitoring required for loans; environmental rule under review", "Compliance pull, but verify current status"], ["Walters Art Museum loan policy", "Lender requires climate records", "Demand regardless of GIS"], ["Testo 160 THL", "About £487–617", "Incumbent, 2–3× the target"]]})

# 9 ---------------------------------------------------------------------------
bf = [board("m5stack-unit-earth", "soil moisture unit for the first prototype"),
      board("m5stack-unit-watering", "capacitive soil moisture + pump reference"),
      board("dfrobot-sen0114", "soil moisture sensor, second source"),
      board("m5stack-stamp-c6lora", "open ESP32-C6 + LoRa core"),
      board("seeed-grove-temperatureandhumidity-sensor-hdc1000", "soil / air temperature reference circuit")]
note, share = open_note(bf)
add({"slug": "tree-thirst-sensor", "title": "Tree Thirst Sensor", "category": "Agri",
     "pitch": "A LoRaWAN soil-moisture and temperature stake for municipal young-tree watering, publishing to the city's own LoRaWAN or TTN with no platform fee.",
     "audience": "Municipal green-space departments with climate-adaptation budgets (Vienna, Ludwigsburg, Jena and Pforzheim already run such programmes), tree-care contractors, housing associations with green space.",
     "why_now": "Cities already run funded tree-sensor programmes, the watering of young trees in dry summers is a line item every green department fights over, and the commercial sensors come with a platform fee the municipal IT would rather avoid.",
     "built_from": bf,
     "whats_new": "A 60 cm stake with two capacitive moisture probes (30 and 60 cm), soil temperature, a sealed head with a Stamp C6LoRa and a lithium cell for five years, a soil-type calibration wizard, and open decoders for TTN and the city's LoRaWAN; a simple map and a watering list, no per-sensor fee.",
     "effort_weeks_est": "8", "bom_eur_est": "15–25", "price_eur_est": "69–99",
     "certification": "RED (EN 300 220) via module, EMC, RoHS, WEEE, CRA; Battery Regulation / UN 38.3 for the cell; IP67 head by design.",
     "kill_question": "Do 3 cities' green departments order a 50-sensor paid pilot at €89 within one budget cycle? Pass = 3 purchase orders in 12 weeks.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 4},
     "tags": ["agri", "lorawan", "b2b", "sensors", "outdoor", "public"], "open_boards_note": note, "score_total": 17},
    {"problem": "Young city trees die in dry summers because watering rounds are scheduled, not measured; the departments that have tried sensors pay for a platform per sensor per year, and the ones that have not, water by guesswork.",
     "customer": "Municipal green-space departments (Grünflächenämter), their watering contractors, and housing associations; the department's climate-adaptation or tree-maintenance budget pays, often with regional funding.",
     "product": "A stake with moisture at two depths and soil temperature, a sealed LoRaWAN head with a five-year cell, a soil-type wizard, open decoders for TTN and city networks, and a map plus a watering list, with no per-sensor platform fee.",
     "ask": "~€35–45k to certification and a first 1,000 stakes (estimate); three municipal pilots cover half.",
     "problem_long": "Vienna's \"Internet of Trees\", Ludwigsburg, Jena and Pforzheim show the demand is live, funded and municipal: sensors in the root zone tell the watering crew which trees need the tanker today. The commercial sensors (Treesense, FloraPulse and others) do not publish prices, so the cost advantage must be confirmed with a quote; what they share is a platform fee, and municipal IT departments that run their own LoRaWAN would rather see the data in their own system.",
     "who_pays": "**Who pays, B2G:** the green-space department, sometimes the city's smart-city or climate programme; watering contractors buy when the city asks for measured watering. **Who uses:** the watering crew (a list of trees to water today) and the arborist (trends per tree).",
     "market": "- **TAM:** young street trees in EU cities (planted within the last five years): estimate 10–20M; one sensor per 5–20 trees in a monitored scheme. Theoretical €100M+.\n- **SAM:** cities with a LoRaWAN network and a tree-watering programme: estimate 300 cities × 300 sensors → €8M.\n- **SOM (3 yrs):** 20,000–40,000 stakes; year-1: 1,500–3,000 across three pilots and their follow-ons.",
     "searches": 3,
     "competition": [("Treesense", "Tree sensors with platform (whitepaper found; no public pricing)", "No platform fee; open decoders; get a quote before claiming cheaper"),
                     ("FloraPulse, Agvolution, Plantcare", "Agricultural and tree sensors, quote-based", "Same"),
                     ("City programmes (Vienna Internet of Trees, Ludwigsburg, Jena, Pforzheim)", "Already deployed sensor schemes", "Demand proof and reference customers to learn from"),
                     ("TTN community tree sensors", "Volunteer-built stakes", "The open precedent; we add a product, a cell life and a calibration")],
     "wedge": "no platform fee and open data into the city's own LoRaWAN, with a stake designed for a five-year life in a tree pit.",
     "product_long": "- Two capacitive probes (30 and 60 cm) and a temperature sensor in a glass-fibre stake; sealed head with the LoRa core and an AA-class lithium cell for five years (estimate at hourly uplinks).\n- Soil-type wizard (sandy, loam, clay, substrate) from a one-off reference reading; drift compensation.\n- Open decoders for TTN and the common city LoRaWAN servers; a small map with a \"water today\" list; CSV and API; no per-sensor fee.\n- Installer kit: pilot drill, depth guide, tree-ID tag.",
     "econ": econ_table("15–25", "69–99", 3.0, 6.0, 2.0, 2.5, 8, "direct B2G and contractor channel, ~€10", 10.0),
     "econ_note": "Lesson: the stake and the sealed head are the cost, not the electronics; design for a five-year life or the city buys twice.",
     "gtm": "**First 100 customers:**\n\n1. Three green departments found through the cities' smart-city teams and existing programmes, each with a 50-stake paid pilot.\n2. Two watering contractors who want to prove measured watering.\n3. Housing associations with new plantings.\n\n**Scale channels:** municipal associations and climate-adaptation programmes, LoRaWAN integrators, tree nurseries that supply the trees.",
     "q1": "Kill-question conversations with three departments; works-like stake on Stamp C6LoRa + Unit Earth; soil calibration method.",
     "q2": "Custom board and stake; EVT 50 in one city over a summer; map and watering list v0.",
     "q3": "DVT; certification; 1,000 stakes; two pilots shipped.",
     "q4": "Follow-on orders; contractor channel; 3,000 stakes.",
     "team": "one embedded engineer, one developer for decoders and the map, one founder who speaks to municipalities; stake mechanics bought in.",
     "funding": "NRE €14k + certification €8k + first 1,000 stakes landed ~€25k ≈ €47k; minus pilots ~€13k ≈ €34k.",
     "risks": [("Cheap capacitive probes drift and corrode", "Coated probes, drift compensation, field test over a summer; reference reading at install"),
               ("Cities already have a vendor", "No fee and open data are the switch argument; integrate with their network, not against it"),
               ("Procurement cycles", "Pilots under tender thresholds; regional funding calls"),
               ("Vandalism / mowers", "Flush stake head, bright tag, replaceable head")],
     "boards_note": "The Stamp C6LoRa publishes PCB and schematic; the M5Stack and DFRobot moisture boards give three probe options for the prototype; the Seeed sensor board is the open temperature reference.",
     "diagram": "  TREE PIT: [capacitive probe 30 cm] [capacitive probe 60 cm] [soil temp] -> [ESP32-C6 + LoRa head, sealed] -> city LoRaWAN / TTN\n                                                                    [AA lithium cell, 5 years]\n  SERVER: open decoder -> map + 'water today' list -> watering crew",
     "bom": [("Capacitive probes ×2 (coated)", "4.0", ""), ("Temperature sensor", "1.0", ""), ("ESP32-C6 + LoRa module", "6.0", ""), ("Lithium AA-class cell", "2.5", ""), ("Stake + sealed head + tag", "6.0", ""), ("PCB, passives", "2.5", "")],
     "firmware": "- ESP-IDF; hourly uplink, daily temperature profile; soil-type model; LoRaWAN class A with ADR.\n- Decoders published for TTN, ChirpStack and the common municipal servers; map and list as a small open-source app.",
     "weeks": ["Interviews with green departments; pilot proposal", "Prototype stake", "Soil calibration experiments", "Stake mechanics", "Custom board v1", "Decoders and map v0",
               "EVT 50 in one city", "Summer drift review", "Head sealing test", "DVT", "Pre-compliance", "Certification; pilot deliveries"],
     "cert": CERT_BATT,
     "cheapest": "Ten prototype stakes in one city's new plantings for a summer, the watering list sent to the crew weekly; ask the department whether they would buy 50 at €89.",
     "interview": "1) How do you decide which trees get watered this week? 2) Have you trialled sensors; what did the platform cost? 3) Who signs a €5k pilot and from which budget line? 4) Which LoRaWAN do you have? 5) At €89 per stake with no fee, how many trees?",
     "landing": "headline \"Water the trees that are thirsty.\" Bullets: two depths, five years, your LoRaWAN, no platform fee, €89. Button: request a pilot (B2G).",
     "pass": "3 purchase orders of 50 within 12 weeks.",
     "production": PROD_STD + "\n- Outdoor: IP67 immersion test on heads; probe coating inspection.",
     "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "Already-funded municipal programmes exist (Vienna \"Internet of Trees\", Ludwigsburg, Jena, Pforzheim): live demand, not hypothetical. Treesense and FloraPulse exist as competitors but do not publish pricing.",
     "risk": "Get a real competitor quote before claiming to be cheaper.",
     "rows": [["Vienna Internet of Trees; Ludwigsburg, Jena, Pforzheim programmes", "Municipal tree-sensor deployments", "Funded demand exists"], ["Treesense (whitepaper)", "Tree sensors + platform, no public price", "Incumbent; quote needed"], ["FloraPulse", "Plant water-status sensors, no public price", "Incumbent; quote needed"]]})

# 10 --------------------------------------------------------------------------
bf = [board("m5stack-unit-rfid2", "13.56 MHz RFID reader for member cards"),
      board("m5stack-unit-nfc", "NFC reader alternative"),
      board("m5stack-unit-fingerprint2", "fingerprint option for spaces without cards"),
      board("m5stack-unit-relay", "single relay for the machine enable"),
      board("m5stack-unit-2relay", "two-channel relay for enable + indicator"),
      board("m5stack-core2", "touch-screen controller for the prototype"),
      board("m5stack-atoms3-lite", "compact core for the production box"),
      board("m5stack-unit-buzzer", "feedback beep")]
note, share = open_note(bf)
add({"slug": "machine-access-box", "title": "Machine Access Box", "category": "Maker tools",
     "pitch": "An RFID or fingerprint interlock for workshop machines that checks the user's training level, logs usage and enables power, with no subscription.",
     "audience": "Makerspaces and open workshops (Verbund Offener Werkstätten, FabLabs), school and university workshops, repair cafés; the space's board or the workshop manager pays.",
     "why_now": "FabAccess is being rolled out across ten workshops with public funding, which proves the sector wants machine access control; the commercial option bills per machine, and the catalogue has readers, relays and cores ready.",
     "built_from": bf,
     "whats_new": "A DIN or wall box per machine with a reader, a relay that enables the machine's control circuit, an LED ring and buzzer, a local server (or FabAccess compatibility) holding members and training levels, usage logs and maintenance counters; no per-machine fee.",
     "effort_weeks_est": "10", "bom_eur_est": "30–45", "price_eur_est": "149–199",
     "certification": "RED (WiFi, 13.56 MHz reader) via modules, EMC, EN 62368-1 (low-voltage control circuit only), RoHS, WEEE, CRA; not a safety-rated interlock: it enables the control circuit, it does not replace the machine's e-stop.",
     "kill_question": "Do 10 makerspaces from one network pre-order 3 boxes each at €169? Pass = 10 orders of 3 in 8 weeks.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 5},
     "tags": ["maker", "b2b", "education", "nfc", "wifi"], "open_boards_note": note, "score_total": 18},
    {"problem": "Open workshops need to know that the person starting the laser cutter has been trained on it, and to log who used what; today that is a sticker, a key cabinet or a per-machine software subscription.",
     "customer": "Makerspaces and open workshops, school and university workshops, repair cafés and tool libraries. The space's board, the workshop manager or the university's lab budget pays; the volunteer instructor sets training levels.",
     "product": "A box per machine with a card or fingerprint reader, a relay that enables the machine's control circuit, an LED ring and buzzer, a local members-and-training server (FabAccess-compatible) with usage logs and maintenance counters; no per-machine fee.",
     "ask": "~€40–55k to certification and a first 1,000 boxes (estimate); network pre-orders cover a third.",
     "problem_long": "Machine access control is the recurring project of every makerspace: FabAccess (offene-werkstaetten.org, a FOSDEM talk, a publicly funded ten-workshop roll-out in 2023–24) shows the sector organising around it; commercial Fabman bills per bridge (pricing unverified; get a quote before claiming a cost advantage). What spaces lack is the box: a finished, certified, pretty unit per machine that a volunteer can install in an hour and that talks to the open server.",
     "who_pays": "**Who pays, B2B:** the space (membership fees, grants) or the institution; a space buys 5–30 boxes at once. **Who uses:** every member, so the reader must work with the cards they already have (Mifare, DESFire, student cards).",
     "market": "- **TAM:** ~2,000 makerspaces and FabLabs in Europe plus school and university workshops; 10–30 machines each. Theoretical €10–20M.\n- **SAM:** spaces with paid membership or institutional backing: estimate 1,200 × 12 machines → €2.4M.\n- **SOM (3 yrs):** 6,000–10,000 boxes; year-1: 1,000–1,500 through two networks and a university.",
     "searches": 3,
     "competition": [("Fabman", "Per-machine bridge with a subscription (pricing unverified)", "No per-machine fee; open server; get the quote before claiming"),
                     ("FabAccess (open source, funded roll-out)", "Open access-control software with DIY hardware", "We are the finished box that runs it; compatibility, not competition"),
                     ("MakeACS, MakerCard and similar", "Smaller access-control projects and products", "Finished hardware and support"),
                     ("Key cabinets and stickers", "Free", "No log, no training check, no maintenance counter")],
     "wedge": "the finished box for the open server the sector is already adopting: certified, installer-simple, no per-machine fee.",
     "product_long": "- Reader: 13.56 MHz (Mifare/DESFire/student cards) or fingerprint; LED ring (red/green/amber), buzzer; relay output for the machine's control circuit (24 V / low-voltage enable), never the motor current.\n- Modes: enable while card present, enable for a session, two-person rule for dangerous machines, instructor override.\n- Server: local (Raspberry Pi class or the space's server), FabAccess-compatible API, members and training levels, usage log, maintenance counters, CSV; no cloud of ours.\n- Install: DIN or wall box, 12–24 V in, two terminals out, one-hour fit by a volunteer with the machine's manual.",
     "econ": econ_table("30–45", "149–199", 4.0, 7.0, 2.5, 3.0, 9, "direct to spaces and networks, ~€15", 15.0),
     "econ_note": "Lesson: a space buys a dozen at a time; discount the dozen, not the single box. Fingerprint readers raise the BOM; keep them optional.",
     "gtm": "**First 100 customers:**\n\n1. Ten spaces from one network (Verbund Offener Werkstätten, a FabLab network) pre-ordering three boxes each.\n2. One university workshop as the institutional reference.\n3. Repair cafés and tool libraries for the cheapest variant.\n\n**Scale channels:** the networks' meetings and mailing lists, FabAccess's community, university procurement frameworks.",
     "q1": "Kill-question pre-orders; works-like box on Core2 + RFID2 + Relay with FabAccess; three spaces test.",
     "q2": "Custom PCB; enclosure; EVT 30 in three spaces; fingerprint variant.",
     "q3": "DVT; certification; 500 boxes; network pre-orders shipped.",
     "q4": "University framework; 1,500 boxes; maintenance-counter features.",
     "team": "one embedded engineer, one backend developer close to the FabAccess community, one founder from a makerspace.",
     "funding": "NRE €14k + certification €8k + first 1,000 boxes landed ~€35k ≈ €57k; minus pre-orders ~€15k ≈ €42k.",
     "risks": [("Spaces expect a safety interlock", "State clearly: control-circuit enable, not a safety function; e-stop stays; installation guide"),
               ("Fabman turns out cheaper than assumed", "Get the quote; compete on openness and no fee"),
               ("Card diversity", "Reader supports the common standards; UID-based enrolment; fingerprint option"),
               ("Volunteer installations go wrong", "Two terminals, clear manual, photos per machine type")],
     "boards_note": "All M5Stack units with published module files; the first boxes can ship on AtomS3 + units in a custom enclosure before a single PCB exists.",
     "diagram": "  [member card / fingerprint] -> [reader] -> [ESP32 core: check training level] -> [relay] -> machine control circuit (enable)\n                                                   |                                  [LED ring, buzzer]\n                                            WiFi -> [local server: members, levels, logs, maintenance counters]  (FabAccess-compatible)",
     "bom": [("13.56 MHz reader module", "4.0", ""), ("ESP32-S3 module", "2.5", ""), ("Relay (control circuit rating)", "2.0", ""), ("LED ring + buzzer", "2.5", ""), ("Enclosure (DIN/wall) + terminals", "8.0", ""), ("PCB, 12–24 V input, passives", "4.0", ""), ("Fingerprint module (option)", "+12.0", "optional")],
     "firmware": "- ESP-IDF; reader driver; offline cache of allowed UIDs per machine; session logic; relay watchdog; LED/buzzer feedback.\n- Server: FabAccess-compatible API or FabAccess itself; admin UI for training levels; logs; CSV.",
     "weeks": ["Pre-orders live; interviews with three space managers", "Prototype box", "FabAccess integration", "Enclosure", "Custom PCB v1", "Fingerprint option",
               "EVT 30 in three spaces", "Installer manual with photos", "Tooling decision", "DVT", "Pre-compliance", "Certification; shipping"],
     "cert": CERT_STD,
     "cheapest": "Three prototype boxes on three machines of one makerspace for a month; ask the board whether they would buy twelve at €169.",
     "interview": "1) How do you control who uses the laser cutter today? 2) Have you looked at Fabman or built your own; what happened? 3) Who pays for equipment and how much per year? 4) What cards do your members carry? 5) At €169 per machine with no fee, how many machines?",
     "landing": "headline \"Only trained hands start the machine.\" Bullets: your cards, your server, usage log, €169 per machine, no fee. Button: pre-order 3 (refundable deposit).",
     "pass": "10 orders of 3 within 8 weeks.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "FabAccess is confirmed real and actively funded (a ten-workshop roll-out in 2023–24), a strong sector-wide demand signal. Fabman is a real incumbent but its pricing is unverified.",
     "risk": "Get a Fabman quote before claiming a cost advantage.",
     "rows": [["FabAccess (offene-werkstaetten.org, FOSDEM talk)", "Open access-control project, funded ten-workshop roll-out", "Sector demand; compatibility target"], ["Fabman", "Per-machine bridge + subscription, pricing unverified", "Incumbent; quote needed"], ["MakeACS", "Access-control project", "Precedent"]]})

# 11 (fix: no compliance claim) ------------------------------------------------
bf = [board("m5stack-stamplc-ac", "mains-powered DIN controller core"),
      board("m5stack-stamplc", "DIN-rail PLC-style controller"),
      board("m5stack-unit-pir", "presence detection in the hall"),
      board("m5stack-unit-tmos-pir", "thermal presence that sees a still person"),
      board("seeed-grove-solid-state-relay-v2", "open SSR reference for the boiler enable signal"),
      board("m5stack-unit-env-iii", "hall temperature and humidity"),
      board("m5stack-unit-rtc", "schedule keeping without network")]
note, share = open_note(bf)
add({"slug": "hall-heat-scheduler", "title": "Hall Heat Scheduler", "category": "Energy & solar",
     "pitch": "A DIN-rail box that heats sports halls, church halls and clubhouses only when the booking calendar and a presence sensor say so, locally, with no cloud, cutting the hours a hall is heated for nobody.",
     "audience": "Sports clubs, parishes and municipal hall managers who pay the heating bill; electricians and heating installers who fit it. Sold on cost savings, not on compliance.",
     "why_now": "Clubs manually fight heated empty halls (German sports-federation guidance describes exactly this), energy prices made the bill visible, and the building-automation rules that exist are sized for far bigger buildings, so nothing forces a solution and nobody sells a small one.",
     "built_from": bf,
     "whats_new": "A DIN box that reads the hall's booking calendar (CalDAV, Google, the club's booking tool), a presence sensor, a temperature sensor and a schedule, and drives the boiler enable or zone valve with pre-heat logic; a local web page and a monthly report of heating hours saved; no cloud.",
     "effort_weeks_est": "12", "bom_eur_est": "60–90", "price_eur_est": "299–399",
     "certification": "LVD / EN 60730-1 class for a mains-connected control device, EMC, RED (WiFi), RoHS, WEEE, CRA; installer-fitted; the boiler interface stays within the boiler maker's enable contact spec.",
     "kill_question": "Do 5 clubs or parishes install a paid pilot at €349 and measure heating hours saved for one month? Pass = 5 pilots and a measured saving in at least 3.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 4, "margin": 4, "speed": 4},
     "tags": ["energy", "heating", "b2b", "din-rail", "building"], "open_boards_note": note, "score_total": 16},
    {"problem": "Halls are heated on a weekly timer set years ago: the Tuesday training that moved, the cancelled Saturday tournament and the empty Monday all get heated, and the club pays. Nobody sells a small controller that reads the booking calendar.",
     "customer": "Sports clubs (the treasurer and the hall warden), parishes with a parish hall, municipalities running community halls, with electricians and heating installers as the fitters. The heating bill payer pays; the saving is the argument.",
     "product": "A DIN-rail box that reads the booking calendar and a presence sensor, keeps a frost guard, pre-heats before bookings and drops the set-point when the hall is empty, drives the boiler enable or a zone valve, and reports heating hours saved on a local page; no cloud.",
     "ask": "~€55–70k to certification and a first 500 units (estimate); five paid pilots cover a quarter.",
     "problem_long": "German sports-federation guidance (DFB) confirms that clubs manually fight this exact problem: someone remembers to turn the heating down, or does not. The underlying pain is cost, not compliance: the research found that the EU's building-automation requirements (EPBD thresholds at 70–290 kW) are sized for buildings far bigger than a parish or sports hall, so this pack does not claim a mandate and does not need one; a hall heated 30 fewer hours a month pays for the box in a season (estimate; verify with the pilot).",
     "who_pays": "**Who pays:** the club or parish (B2B with small budgets and energy-saving grants), the municipality for its halls. **Who installs:** an electrician or heating installer, who also becomes the channel. **Who uses:** the hall warden, via a local page and the booking calendar they already keep.",
     "market": "- **TAM:** ~90,000 sports clubs in Germany, tens of thousands of parish and community halls across DE/NL/UK/AT/CH. Theoretical €50M+ at €349.\n- **SAM:** halls with a gas or oil boiler and a digital booking calendar: estimate 40,000 → €14M.\n- **SOM (3 yrs):** 4,000–8,000 units through installers and federations; year-1: 300–500.",
     "searches": 3,
     "competition": [("Building-management systems (Siemens, Honeywell and integrators)", "Quote-based, €5k and up, sized for large buildings", "A tenth of the price, sized for one hall"),
                     ("Smart thermostats (tado°, Netatmo)", "Consumer, cloud, schedule-based", "Calendar-driven and presence-aware; no cloud account for a club"),
                     ("Church-heating specialists", "Installed systems, quote-based", "Retrofit box on the existing boiler"),
                     ("The weekly timer and the warden's memory", "Free", "That is the cost we remove")],
     "wedge": "the booking calendar as the heating schedule, in a box an installer fits in an afternoon, sold on the saving it measures itself.",
     "product_long": "- Inputs: booking calendar (CalDAV, Google, common club booking tools via ICS), presence (PIR / thermal), hall temperature, outside temperature from the net or a sensor.\n- Logic: pre-heat time learned per hall, set-back when empty, frost guard, manual boost button for the unplanned use, holiday mode.\n- Outputs: boiler enable contact or zone valve through an SSR / relay rated for the signal, never the burner mains; optional second zone.\n- Reporting: local page with heating hours by week, estimated saving; CSV; no cloud.",
     "econ": econ_table("60–90", "299–399", 6.0, 10.0, 3.0, 4.0, 15, "installer channel margin, ~€40", 40.0),
     "econ_note": "Lesson: certification for a mains-connected controller is the big first-run item; the installer's margin is what makes the channel work. Price the second zone as an add-on.",
     "gtm": "**First 100 customers:**\n\n1. Five clubs or parishes in one region, each a paid pilot with a one-month measurement.\n2. Two heating installers who fit the pilots and quote it afterwards.\n3. A regional sports federation newsletter once the savings are measured.\n\n**Scale channels:** heating installers and electricians, sports federations (Landessportbünde), church administrations, municipal energy advisers.",
     "q1": "Kill-question conversations; works-like controller on StamPLC + PIR + ENV-III reading one club's calendar; pilot contracts.",
     "q2": "Custom board; enclosure; EVT 5 pilots installed by one installer; saving measured.",
     "q3": "DVT; certification; 200 units; installer kit.",
     "q4": "Federation channel; 500 units; second-zone option.",
     "team": "one embedded engineer, one developer for calendar integrations, one founder who knows clubs and installers.",
     "funding": "NRE €20k + certification €15k + first 500 units landed ~€40k ≈ €75k; minus pilots ~€9k ≈ €66k.",
     "risks": [("Savings smaller than hoped", "Measure in the pilot before scaling; pick halls with the worst timers first"),
               ("Boiler interfaces vary", "Support the standard enable contact and a zone valve; installer decides; document the common boilers"),
               ("Clubs do not keep a digital calendar", "ICS from any tool; a simple built-in weekly schedule with exceptions as fallback"),
               ("Installer-fitted product with certification cost", "Quote the lab first; design to the standard")],
     "boards_note": "The StamPLC family is the DIN controller; the Seeed SSR board publishes its schematic as the enable-output reference; the M5Stack presence and environment units are the sensors for the prototype.",
     "diagram": "  [booking calendar: CalDAV / ICS]  [PIR / thermal presence]  [hall temp]  [outside temp]\n                 \\                 |                  /             /\n                  -> [StamPLC controller: pre-heat, set-back, frost guard] -> [SSR] -> boiler enable / zone valve\n                                   |  local page: heating hours, saving        [boost button in the hall]",
     "bom": [("ESP32-S3 DIN controller board (StamPLC-class)", "14.0", ""), ("PIR / thermal presence unit", "6.0", ""), ("T/RH sensor", "2.0", ""), ("SSR / relay for the enable signal", "4.0", ""), ("Certified mains PSU module", "7.0", ""), ("DIN enclosure, terminals, boost button", "14.0", ""), ("PCB, RTC, passives", "6.0", "")],
     "firmware": "- ESP-IDF; ICS/CalDAV parsing locally; schedule engine with learned pre-heat; presence hold-off; frost guard independent of network.\n- Local web page; CSV; MQTT optional; no cloud.\n- Safe states on power loss and network loss (timer fallback).",
     "weeks": ["Interviews with clubs and installers; pilot proposals", "Prototype on StamPLC", "Calendar engine and pre-heat learning", "Enclosure and terminals", "Custom board v1", "Certification quotes and standard study",
               "EVT 5 pilots installed", "One month of measurement", "Installer manual", "DVT", "Pre-compliance and safety tests", "Certification submission"],
     "cert": CERT_MAINS,
     "cheapest": "One prototype in one club hall for a month, logging boiler hours against the previous month's timer; show the number to five clubs with a €349 price.",
     "interview": "1) Who sets the hall heating and when did they last change it? 2) What did heating cost last winter? 3) Do you keep bookings in a calendar; which? 4) Who would fit something on the boiler? 5) If it saved 30 hours a month, would you pay €349 plus fitting?",
     "landing": "headline \"Heat the hall when the calendar says so.\" Bullets: reads your bookings; knows when the hall is empty; shows the hours saved; €349 fitted by your installer. Button: request a pilot (B2B).",
     "pass": "5 paid pilots and a measured saving in at least 3 within 10 weeks.",
     "production": PROD_STD + "\n- Safety: 100% hi-pot and relay test; installer note in every box.",
     "next": NEXT_STD},
    {"verdict": "UNCERTAIN",
     "summary": "The compliance angle does not hold: EU EPBD building-automation thresholds (70–290 kW) are sized for buildings much bigger than a typical sports or parish hall. German sports-federation guidance (DFB) confirms clubs manually fight this exact problem today, so the pain is real, but cost-driven, not compliance-driven.",
     "risk": "Pitch reworked before building: sold on measured heating savings and the B2B buyer only; no mandate is claimed.",
     "correction": {"title": "Built with the research fix applied (November 2026)",
                    "text": "The research found that the EU building-automation requirements (EPBD, 70–290 kW thresholds) do not apply to halls this size, so this pack claims no compliance pull. It is sold on the heating hours it measurably saves, to the club or parish that pays the bill, with the installer as the channel; the kill question requires a measured saving. As researched November 2026 by web search; verify before relying on it."},
     "rows": [["EU EPBD building-automation thresholds (70–290 kW)", "Apply to large buildings only", "No compliance pull for halls; claim dropped"], ["DFB (German football federation) guidance on hall heating", "Clubs manually manage heating of empty halls", "The pain is real and cost-driven"]]})

# 14 --------------------------------------------------------------------------
bf = [board("m5stack-unit-ac-measure", "AC power measurement per machine"),
      board("dfrobot-sen0098", "AC current sensor alternative"),
      board("m5stack-unit-accel", "vibration-based detection where the plug is not accessible"),
      board("m5stack-papers3", "e-paper status board at the laundry-room door"),
      board("m5stack-coreink", "small e-paper variant"),
      board("m5stack-stamp-c6lora", "LoRa link from basement laundry rooms"),
      board("m5stack-atoms3-lite", "ESP32-S3 sensor node core")]
note, share = open_note(bf)
add({"slug": "shared-laundry-notifier", "title": "Laundry Room Notifier", "category": "Smart home",
     "pitch": "Clip-on current or vibration sensors per machine and an e-paper status board at the laundry-room door, with optional push to residents, so nobody carries a basket down to a busy room; no subscription.",
     "audience": "Housing associations, student-housing operators and housing co-ops in CH/DE/Nordics where shared laundry rooms are standard; facility managers buy, residents use.",
     "why_now": "Washer-done detection is one of the most repeated Home Assistant projects, shared laundry rooms are a daily friction for millions of residents, and the professional booking systems are expensive and tied to card infrastructure.",
     "built_from": bf,
     "whats_new": "Sensor nodes that read a machine's power draw or vibration and classify running / finished / free, a door-side e-paper board listing every machine, an optional resident web page or push, and a LoRa link for basements; installed without touching the machines' electrics; no per-room fee.",
     "effort_weeks_est": "10", "bom_eur_est": "50–80", "price_eur_est": "249–349",
     "certification": "RED via modules, EMC, EN 62368-1 (clip-on current sensor, no mains contact; plug-through variant needs the socket's own certification), RoHS, WEEE, CRA; Battery Regulation for battery nodes.",
     "kill_question": "Do 3 housing associations or student-housing operators install a paid pilot in 5 laundry rooms at €299 per room, and do residents say in week 3 that they check the board before carrying the basket? Pass = 3 pilots and a majority yes.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 4},
     "tags": ["smart-home", "building", "b2b", "e-paper", "lorawan", "housing"], "open_boards_note": note, "score_total": 17},
    {"problem": "Residents of blocks with a shared laundry room carry the basket down to find every machine running, and operators field the complaints; the booking systems that solve it are expensive card infrastructures sold with the machines.",
     "customer": "Housing associations, student-housing operators and co-ops with shared laundry rooms (the norm in Switzerland, common in Germany and the Nordics); the facility or property manager pays per room, residents use the board and the page.",
     "product": "Clip-on sensor nodes per machine (power draw, or vibration where the plug is unreachable), an e-paper board at the laundry-room door showing each machine's state and expected finish, an optional resident page or push, a LoRa link for basements; no per-room fee.",
     "ask": "~€45–55k to certification and a first 300 rooms (estimate); three pilots cover a fifth.",
     "problem_long": "The Home Assistant forums carry multiple long threads and GitHub projects for detecting a washer's cycle from its power draw or vibration; the pattern is proven at home. In a shared room the same information is worth more and nobody provides it except full booking systems (Miele and Electrolux Professional, Aptus, the Swiss card systems), whose prices were not found publicly and must be verified. The open question the demand interviews must settle: do operators want detection layered on an existing booking or card system, or do they consider the problem solved by it?",
     "who_pays": "**Who pays, B2B:** the operator, per room, from the facility budget or the laundry-room income. **Who uses:** residents, who must get the answer without an app (the board) and may get it on the phone (the page).",
     "market": "- **TAM:** shared laundry rooms in CH (most apartment blocks), DE and the Nordics (student housing, co-ops): estimate 500,000+ rooms. Theoretical €150M at €299.\n- **SAM:** rooms run by professional operators with more than 20 units: estimate 150,000 → €45M.\n- **SOM (3 yrs):** 5,000–10,000 rooms; year-1: 300–500 through three operators.",
     "searches": 3,
     "competition": [("Miele / Electrolux Professional booking systems", "Card or app booking tied to the machines; pricing not public", "Retrofit on any machine, no card infrastructure; verify their pricing before claiming a gap"),
                     ("Aptus and Swiss Waschkarten systems", "Access and booking systems, pricing not public", "Same; we may layer on top of them"),
                     ("Smart plugs + Home Assistant (washer/dryer notify blueprints, GitHub washer-notifier)", "DIY at home", "Proven detection; we make it a product for a shared room"),
                     ("A whiteboard on the door", "Free", "Nobody updates it")],
     "wedge": "retrofit detection on any machine with a door-side board residents trust, sold per room without a fee; it layers on existing booking systems rather than replacing them.",
     "product_long": "- Sensor node: clip-on current transformer on the machine's cable or a plug-through power meter where allowed; vibration node (accelerometer, magnet-mounted) for machines with inaccessible plugs; cycle classification (running, final spin, finished, idle).\n- Door board: e-paper listing machines, state, expected finish, last updated; battery or USB.\n- Resident page: QR on the board, no login; optional push via the operator's existing app or e-mail.\n- Link: WiFi where it reaches, LoRa node-to-board for basements; operator dashboard with utilisation per machine (helps plan machine counts).",
     "econ": econ_table("50–80", "249–349", 6.0, 10.0, 4.0, 4.0, 9, "direct to operators and facility-service channel, ~€25", 25.0),
     "econ_note": "Lesson: a room is four nodes and a board; the utilisation data for the operator is the upsell that pays for support.",
     "gtm": "**First 100 customers:**\n\n1. Three operators (one Swiss housing association, one student-housing operator, one co-op) with five-room paid pilots.\n2. Facility-service companies that run laundry rooms for operators.\n3. Co-ops via their federations.\n\n**Scale channels:** housing-association federations, facility-service firms, laundry-machine dealers for retrofit.",
     "q1": "Kill-question conversations with operators (including the layering question); works-like nodes on Unit AC Measure + AtomS3 and a PaperS3 board in one room.",
     "q2": "Custom node PCB; vibration node; EVT in 5 rooms; resident feedback.",
     "q3": "DVT; certification; 150 rooms; three pilots shipped.",
     "q4": "Operator dashboard; 500 rooms; dealer channel.",
     "team": "one embedded engineer, one developer for the board and page, one founder selling to operators.",
     "funding": "NRE €16k + certification €9k + first 300 rooms landed ~€30k ≈ €55k; minus pilots ~€9k ≈ €46k.",
     "risks": [("Operators see the problem as solved by booking systems", "Ask it in the first ten interviews; position as a layer; target rooms without booking first"),
               ("Cycle detection errors (false 'finished')", "Classifier tuned per machine type; final-spin detection; expected-finish shown as estimate"),
               ("Residents ignore the board", "Place at eye level by the door; QR page; week-3 question in the kill question"),
               ("Electrical rules for clip-on and plug-through sensors", "Clip-on CT needs no mains contact; plug-through only with a certified socket module")],
     "boards_note": "The M5Stack measurement, e-paper and core units carry published module files; the DFRobot current sensor is the second source; the Stamp C6LoRa (open files) is the basement link.",
     "diagram": "  per machine: [clip-on CT or plug-through meter | accelerometer] -> [ESP32 node] -> WiFi / LoRa\n                                                                                  |\n  door: [e-paper board: W1 running 23 min | W2 free | D1 finished]  <- [bridge] -> resident page (QR), operator dashboard",
     "bom": [("Current transformer + ADC or plug-through meter module (×4)", "16.0", "per room"), ("ESP32 nodes ×4", "10.0", ""), ("Accelerometer option", "+3.0", ""), ("E-paper board + ESP32 + enclosure", "22.0", ""), ("Node enclosures, cables", "8.0", ""), ("LoRa bridge option", "+8.0", "basement rooms")],
     "firmware": "- ESP-IDF; power/vibration sampling, cycle state machine per machine type; LoRa or WiFi uplink; board renders states and estimates.\n- Small server: states, resident page, operator dashboard, utilisation CSV; self-hosted or hosted at cost.",
     "weeks": ["Interviews with operators (layering question first); pilot proposals", "Prototype nodes and board in one room", "Cycle classifier", "Node PCB v1", "Vibration node", "Board enclosure",
               "EVT in 5 rooms", "Resident survey in week 3", "Dashboard v0", "DVT", "Pre-compliance", "Certification; pilot roll-out"],
     "cert": CERT_BATT,
     "cheapest": "Four smart-plug sensors and a PaperS3 board in one laundry room for three weeks; ask residents at the door whether they checked it, and the operator whether they would pay €299 per room.",
     "interview": "1) How do residents find out whether a machine is free today, and what do they complain about? 2) Do you run a booking or card system; what did it cost and does it tell people when a cycle ends? 3) Who approves a per-room purchase? 4) Where are the rooms (basement, WiFi)? 5) At €299 per room with no fee, how many rooms?",
     "landing": "headline \"Know before you carry the basket.\" Bullets: works with your machines; board at the door; page on the phone; €299 per room, no fee. Button: request a pilot (B2B).",
     "pass": "3 pilots and a resident majority saying they check the board by week 3.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "A confirmed, active Home Assistant DIY pattern (multiple forum threads and GitHub projects for washer/dryer notification): real demand. No public pricing was found for Miele, Electrolux or Waschkarten systems, so the competitive gap must be verified.",
     "risk": "Ask in the demand interviews whether housing associations want detection layered on existing booking or card systems or consider the problem solved; verify incumbent pricing before claiming a gap.",
     "rows": [["Home Assistant forum threads (laundry sensors; washer/dryer notify blueprint)", "DIY detection at home", "Proven pattern, demand signal"], ["GitHub washer-notifier project", "DIY project", "Same"], ["Miele / Electrolux Professional, Aptus, Waschkarten systems", "Booking systems, pricing not public", "Incumbents; gap unverified"]]})

# 15 --------------------------------------------------------------------------
bf = [board("m5stack-unit-ultrasonic-i2c", "ultrasonic distance to the water surface"),
      board("seeed-grove-ultrasonic-ranger", "open ultrasonic ranger reference circuit"),
      board("m5stack-stamp-c6lora", "open ESP32-C6 + LoRa core"),
      board("m5stack-unit-lorawan-eu868", "EU868 LoRaWAN module for the prototype"),
      board("m5stack-unit-catm", "Cat-M fallback where no LoRaWAN exists"),
      board("dfrobot-dfr0535", "solar power manager for the post")]
note, share = open_note(bf)
add({"slug": "stream-level-gauge", "title": "Stream Level Gauge", "category": "LoRaWAN & building IoT",
     "pitch": "A solar ultrasonic water-level sensor for bridges and culverts that reports over LoRaWAN or Cat-M to a public dashboard, giving small municipalities an advisory early warning on the streams nobody gauges; advisory, not an official gauge.",
     "audience": "Municipalities, water boards and volunteer fire brigades in flood-prone regions (post-2021 budgets in DE/BE/NL; EU Floods Directive planning), TTN communities that already build such sensors.",
     "why_now": "Hennef installed a community-built level sensor on a public bridge feeding its smart-city map, and Bergisch Gladbach gauges the Strunde the same way: municipalities take these sensors up when they exist; the official gauges cost thousands and are placed only on larger rivers.",
     "built_from": bf,
     "whats_new": "An IP67 post or bridge-rail mount with a downward ultrasonic sensor, a Stamp C6LoRa, solar panel and cell, firmware with temperature compensation, surface-noise filtering and rate-of-rise alerts, a public dashboard and alert rules for the fire brigade; labelled advisory on every screen.",
     "effort_weeks_est": "12", "bom_eur_est": "80–130", "price_eur_est": "399–599",
     "certification": "RED (EN 300 220 / cellular module), EMC, EN 62368-1, RoHS, WEEE, CRA; Battery Regulation for the cell; IP67 by design; no claim to be a measuring instrument under metrology law.",
     "kill_question": "Do 3 municipalities or one water board sign a paid 10-gauge advisory pilot at €499 within one budget cycle, with the advisory status accepted in writing? Pass = 3 signed pilots (or 1 water board) in 12 weeks.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 4, "margin": 4, "speed": 3},
     "tags": ["lorawan", "b2b", "outdoor", "solar", "public", "safety"], "open_boards_note": note, "score_total": 15},
    {"problem": "The official gauge network covers the big rivers; the stream that floods the village underpass has no gauge, and the official instruments that could watch it cost €2,000–6,000 each, so the fire brigade finds out from a phone call.",
     "customer": "Municipalities (civil protection and public works), water boards, volunteer fire brigades, and the TTN communities already building sensors with them; the municipality's flood-protection or smart-city budget pays.",
     "product": "An IP67 ultrasonic level sensor on a bridge rail or post, solar-powered, reporting every 10 minutes (every minute when rising fast) over LoRaWAN or Cat-M to a public dashboard with alert rules; advisory status stated on every screen and in the contract.",
     "ask": "~€60–80k to certification and a first 300 gauges (estimate); three pilots cover a fifth.",
     "problem_long": "The precedent is strong and institutional: TTN Rhein-Sieg's sensor in Hennef was installed by the city on a public bridge and feeds its public smart-city map; TTN Bergisch Gladbach gauges the Strunde. Official instruments (OTT ecoLog and similar) are excellent and priced for the state gauge network. The liability point must be plain: this is an advisory sensor for local awareness and early mobilisation, not an official gauge and not a substitute for the state warning service; the pack, the dashboard and the contract say so.",
     "who_pays": "**Who pays, B2G:** the municipality or water board; sometimes the fire brigade's association or a regional flood-protection programme. **Who uses:** the fire brigade's duty officer (alerts), public works (trends), residents (the public map).",
     "market": "- **TAM:** small streams with flood history in DE/BE/NL/AT/CH: estimate 50,000 sites worth gauging; theoretical €25M at €499.\n- **SAM:** municipalities with a flood-protection budget and a LoRaWAN or willingness to use Cat-M: estimate 3,000 municipalities × 5 gauges → €7.5M.\n- **SOM (3 yrs):** 2,000–4,000 gauges; year-1: 150–300 across three pilots and a water board.",
     "searches": 3,
     "competition": [("OTT ecoLog and official gauge loggers (SEBA, Hydro-Met)", "€2,000–6,000 class instruments for the state network (research, Nov 2026)", "A tenth of the price for advisory use; we do not compete for official gauges"),
                     ("TTN community sensors (Hennef / Rhein-Sieg, Bergisch Gladbach Strunde)", "Volunteer-built, city-installed", "The precedent; we add a product, a warranty and the dashboard"),
                     ("State warning services (Hochwasserzentralen)", "Official, river-scale", "We are upstream of them, on streams they do not cover; link to them, never replace"),
                     ("Phone calls and a resident who looks out of the window", "Free", "The alert at 3 a.m. is the product")],
     "wedge": "an advisory gauge at a tenth of the official price, building on the sensor municipalities already accepted from their TTN communities, with alerts the fire brigade can act on.",
     "product_long": "- Downward ultrasonic sensor (0.3–6 m), temperature-compensated, surface-noise filtering; mounting kit for bridge rails and posts; IP67.\n- Solar panel and cell for a northern winter at 10-minute uplinks, 1-minute when rising fast (estimate; validate in December).\n- LoRaWAN (city or TTN) or Cat-M; store-and-forward on link loss.\n- Dashboard: public map and graph, alert rules (level, rate of rise), SMS/e-mail/app to the duty officer; \"advisory sensor, not an official gauge\" on every screen; API for the city's systems.",
     "econ": econ_table("80–130", "399–599", 10.0, 35.0, 6.0, 8.0, 12, "direct B2G and integrator channel, ~€45", 45.0),
     "econ_note": "Lesson: the mount and the housing are half the cost; one housing for rail and post. Dashboard hosting at cost; the alert rules are what the brigade pays attention to.",
     "gtm": "**First 100 customers:**\n\n1. Three municipalities with recent flood damage, approached with their TTN community and their fire brigade.\n2. One water board for a catchment of ten streams.\n3. Regional flood-protection programmes that fund municipal sensors.\n\n**Scale channels:** municipal associations, TTN communities, LoRaWAN integrators, fire-brigade associations.",
     "q1": "Kill-question conversations with municipalities and one water board; works-like gauge on Stamp C6LoRa + Unit Ultrasonic at one stream; advisory wording agreed with a municipal lawyer.",
     "q2": "Custom board; housing and mounts; EVT 10 at real sites over a wet season; dashboard v0.",
     "q3": "DVT; certification; 100 gauges; pilots shipped.",
     "q4": "Water-board catchment; 300 gauges; alert integrations.",
     "team": "one embedded engineer, one backend developer, one founder who speaks to municipalities and fire brigades; housing design bought in.",
     "funding": "NRE €24k + certification €10k + first 300 gauges landed ~€40k ≈ €74k; minus pilots ~€15k ≈ €60k.",
     "risks": [("Liability if a flood is not warned", "Advisory status in contract, dashboard and manual; no safety claim; the brigade's own procedures stay; insurance priced in"),
               ("Accuracy in wind, foam, ice", "Filtering, mounting guidance, temperature compensation; rate-of-rise is the robust signal"),
               ("Winter power budget", "Measure in December; larger panel or mains where available"),
               ("Permits to mount on bridges", "Municipality owns the bridge in the pilot; mounting kit for rails without drilling")],
     "boards_note": "The Stamp C6LoRa publishes PCB and schematic; the Seeed ranger publishes its schematic; the M5Stack units and the DFRobot solar manager are the quickest prototype path.",
     "diagram": "  BRIDGE RAIL: [ultrasonic sensor, downward] -> [ESP32-C6 + LoRa / Cat-M] -> LoRaWAN / cellular -> dashboard\n               [solar panel + cell]  [temp sensor]   every 10 min; 1 min when rising fast\n  DASHBOARD: public map + graph; alert rules -> fire brigade duty officer;  'advisory, not an official gauge'",
     "bom": [("Ultrasonic sensor, outdoor grade", "18.0", ""), ("ESP32-C6 + LoRa module (or + Cat-M)", "8.0", "+15 for Cat-M"), ("Solar panel 5–10 W + power manager", "15.0", ""), ("LiFePO4 cell", "10.0", ""), ("IP67 housing + rail/post mount", "35.0", ""), ("PCB, temp sensor, passives", "6.0", "")],
     "firmware": "- ESP-IDF; median and outlier filtering, temperature compensation, adaptive uplink rate on rate of rise; store-and-forward.\n- Dashboard: open-source ingest, public map, alert engine (level, rate), SMS/e-mail; API; advisory label hard-coded.",
     "weeks": ["Interviews with municipalities, brigade, water board; advisory wording", "Prototype at one stream", "Filtering and rate-of-rise logic", "Housing and mount", "Custom board v1", "Dashboard v0 and alerts",
               "EVT 10 over a wet season", "Brigade feedback", "Winter power check", "DVT", "Pre-compliance", "Certification; pilot deliveries"],
     "cert": CERT_BATT + "\n- Not a measuring instrument under metrology law and not a safety device: say so in the manual, the contract and on the dashboard.",
     "cheapest": "One prototype on the bridge of the stream that last flooded, data on a public page for a season; ask the municipality and the brigade whether they would buy ten at €499 as advisory sensors.",
     "interview": "1) Tell me about the last flood on a stream without a gauge: how did you find out? 2) What do official gauges cost you and where are they? 3) Who decides on civil-protection purchases and what is the budget? 4) Would an advisory sensor fit your procedures, and what wording would your lawyer want? 5) At €499 per gauge, how many streams?",
     "landing": "headline \"Watch the stream before it reaches the village.\" Bullets: solar, LoRaWAN or cellular, public map, alerts to the brigade; advisory sensor, not an official gauge; €499. Button: request a pilot (B2G).",
     "pass": "3 signed advisory pilots (or one water board) within 12 weeks.",
     "production": PROD_STD + "\n- Outdoor: IP67 immersion test; mount load test; label with the advisory statement.",
     "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "Strong confirmed precedent: a community-built sensor in Hennef was installed by the city on a public bridge and feeds a public smart-city map, real institutional pickup; TTN Bergisch Gladbach gauges the Strunde the same way. OTT ecoLog represents the official instrument class.",
     "risk": "Liability: positioned as advisory, not an official gauge, given the flood-safety stakes; the pack says so in contract, manual and dashboard.",
     "rows": [["TTN Rhein-Sieg Hennef sensor", "Community sensor installed by the city on a public bridge, public map", "Institutional pickup confirmed"], ["TTN Bergisch Gladbach Strunde sensor", "Community stream gauge", "Precedent"], ["OTT ecoLog", "Official gauge logger class", "Incumbent for official gauges, €2–6k class"]]})

# ---------------------------------------------------------------------------

def main():
    ideas = json.loads(IDEAS_PATH.read_text(encoding="utf-8"))
    market = json.loads(MARKET.read_text(encoding="utf-8"))
    have = {i["slug"] for i in ideas["ideas"]}
    added = 0
    for i in IDEAS:
        if i["slug"] in have:
            continue
        ideas["ideas"].append(i)
        (PACKS / f"{i['slug']}.md").write_text(pack_md(i, PACKSPEC[i["slug"]]), encoding="utf-8")
        market["ideas"][i["slug"]] = MARKETSPEC[i["slug"]]
        added += 1
    ideas.setdefault("rounds", []).append({"date": "2026-11-14", "note": "Round 2: 13 ideas added after an external market check of 16 candidates (10 as-is, 3 with the researcher's fix applied; 3 dropped).", "slugs": [i["slug"] for i in IDEAS]})
    IDEAS_PATH.write_text(json.dumps(ideas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    MARKET.write_text(json.dumps(market, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"added {added} ideas; total {len(ideas['ideas'])}")


if __name__ == "__main__":
    main()
