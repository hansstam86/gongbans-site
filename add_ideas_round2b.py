#!/usr/bin/env python3
"""
add_ideas_round2b.py — the last three ideas of the November 2026 replacement round (two LIKELY
as-is, one UNCERTAIN with the researcher's fix), bringing the round to 16. Reuses the generator
and templates from add_ideas_round2.py. One-off; safe to re-run (skips slugs already present).
"""

import json

import add_ideas_round2 as r2
from add_ideas_round2 import CERT_BATT, CERT_STD, NEXT_STD, PROD_STD, board, econ_table, open_note

IDEAS, PACKSPEC, MARKETSPEC = [], {}, {}


def add(i, p, m):
    IDEAS.append(i); PACKSPEC[i["slug"]] = p; MARKETSPEC[i["slug"]] = m


# A ---------------------------------------------------------------------------
bf = [board("m5stack-unit-dlight", "ambient-light unit for the first prototype node"),
      board("seeed-grove-digital-light-sensor", "open digital light-sensor reference circuit"),
      board("m5stack-unit-light", "simple light sensor, second source"),
      board("m5stack-stamp-c6lora", "open ESP32-C6 + LoRa core for the node"),
      board("m5stack-unit-lorawan-eu868", "EU868 LoRaWAN module for the prototype run")]
note, share = open_note(bf)
add({"slug": "emergency-light-logger", "title": "Emergency Light Test Logger", "category": "LoRaWAN & building IoT",
     "pitch": "A stick-on light-sensor node per emergency luminaire that records over LoRaWAN whether the lamp lit during the monthly function test and stayed lit through the annual duration test, producing the test log for older luminaires that have no self-test; evidence of the test, not the test itself.",
     "audience": "Facility managers of schools, housing blocks, offices and halls with older emergency lighting; electrical contractors who perform and log the tests; housing associations.",
     "why_now": "EN 50172 / DIN VDE 0108 require periodic, logged emergency-lighting tests, self-test systems (IEC 62034) only come with new installations, and the building stock is full of old luminaires whose test log is a clipboard walked round by an electrician.",
     "built_from": bf,
     "whats_new": "A coin-cell node with a light sensor and a LoRaWAN core, stuck to each luminaire; it timestamps when the lamp lit and for how long during the test the electrician triggers as before, the server assembles the test log per building; whether inspectors accept it as compliance evidence is an open question the pack states, not settles.",
     "effort_weeks_est": "8–10", "bom_eur_est": "8–14", "price_eur_est": "49–79",
     "certification": "RED (EN 300 220) via module, EMC, RoHS, WEEE, CRA; Battery Regulation for the coin cell; the node is a logging accessory, not emergency-lighting equipment under EN 60598-2-22.",
     "kill_question": "Do 3 facility managers or 2 electrical contractors install a paid pilot of 50 nodes at €59, run one quarterly cycle, and does at least one inspector or insurer accept the generated log alongside the manual record? Pass = 3 pilots and 1 written acceptance in 12 weeks.",
     "open_files_share": share, "scores": {"demand": 4, "buildability": 5, "margin": 4, "speed": 4},
     "tags": ["building", "lorawan", "b2b", "compliance", "safety"], "open_boards_note": note, "score_total": 17},
    {"problem": "Emergency lighting must be tested and the tests logged; in older buildings an electrician walks round with a clipboard, and the self-test systems that would automate it are sold with new luminaires, not for the thousands already on the ceiling.",
     "customer": "Facility managers and housing associations with older buildings, and the electrical contractors who perform the tests for them; the facility or maintenance budget pays, the contractor installs and reads the log.",
     "product": "A coin-cell light-sensor node stuck to each luminaire, reporting over LoRaWAN whether and how long the lamp lit during the function and duration tests, and a server that assembles the per-building test log; sold as evidence that supports the mandatory record.",
     "ask": "~€35–45k to certification and a first 2,000 nodes (estimate); three pilots cover a fifth.",
     "problem_long": "EN 50172 and DIN VDE 0108 (and their national equivalents) require a monthly function test and an annual duration test of every emergency luminaire, with a log. Self-test systems under IEC 62034 do this automatically, but only in new installations (Zumtobel, Legrand, Eaton and others sell them with the luminaires). For the older stock the test is manual and the log is paper. One thing this pack states plainly and does not resolve: a light sensor reading \"it lit for 61 minutes\" is evidence that light was emitted during a test, not the standard's duration test itself, which concerns the battery-backed runtime of the luminaire; whether an inspector or insurer accepts the generated log as compliance evidence is a genuinely open question, and the kill question asks it.",
     "who_pays": "**Who pays, B2B:** the facility manager or housing association; electrical contractors buy for their customers and resell the service. **Who uses:** the contractor on test day and the facility manager when the inspector comes.",
     "market": "- **TAM:** emergency luminaires in EU non-residential and multi-family buildings without self-test: estimate 50–100M. Theoretical €3B+ at €59.\n- **SAM:** buildings managed by professional facility managers with a LoRaWAN or willing to add a gateway: estimate 5M luminaires → €300M.\n- **SOM (3 yrs):** 100,000–200,000 nodes; year-1: 5,000–10,000 across three pilots and two contractors.",
     "searches": 3,
     "competition": [("Self-test / DALI emergency systems (Zumtobel, Legrand, Eaton; IEC 62034)", "Automatic testing built into new luminaires", "Retrofit on old luminaires without replacing them; we complement new-build systems"),
                     ("Inspection and maintenance software subscriptions", "Digital clipboards for the contractor", "We add the sensor evidence; can feed their logs"),
                     ("Replacing luminaires with self-test models", "€100–300 per luminaire installed (estimate)", "A fraction of that per point"),
                     ("The clipboard", "Free", "No evidence, no timestamps, no duration record")],
     "wedge": "sensor evidence for the mandatory test log on the luminaires nobody will replace, at a tenth of a replacement, with the limits of that evidence stated.",
     "product_long": "- Node: light sensor facing the luminaire, coin cell for two years (estimate), LoRaWAN uplink of light-on / light-off timestamps; adhesive and magnetic mounts; tamper flag.\n- Test flow unchanged: the electrician triggers the function or duration test as today; the nodes record who lit and for how long; the server builds the per-building log with exceptions (did not light, lit under 60/180 minutes).\n- Export in the format the contractor's log already uses; API; no per-node licence.\n- Clear statement in manual and log: supports the record; the duration test's battery criterion remains the luminaire's own; acceptance by inspectors to be confirmed locally.",
     "econ": econ_table("8–14", "49–79", 1.5, 2.0, 1.0, 1.0, 8, "contractor channel, ~€8", 8.0, vat=19),
     "econ_note": "Lesson: a node is cheap; the gateway and the server are per building and should be priced as a kit; volume comes in hundreds per building.",
     "gtm": "**First 100 customers:**\n\n1. Three facility managers with old stock and an upcoming inspection, each a 50-node paid pilot.\n2. Two electrical contractors who test for many buildings and resell the service.\n3. A housing association as the multi-building reference.\n\n**Scale channels:** electrical contractors, facility-management associations (GEFMA, IFMA), LoRaWAN integrators, insurers' loss-prevention teams.",
     "q1": "Kill-question conversations incl. an inspector; works-like node on Stamp C6LoRa + DLight; log format from one contractor.",
     "q2": "Custom node PCB; EVT 100 nodes in two buildings; one quarterly cycle logged.",
     "q3": "DVT; certification; 5,000 nodes; pilots shipped; inspector feedback documented.",
     "q4": "Contractor channel; 20,000 nodes; insurer conversation.",
     "team": "one embedded engineer, one backend developer, one founder with facility-management or electrical-contracting background.",
     "funding": "NRE €12k + certification €8k + first 2,000 nodes landed ~€24k ≈ €44k; minus pilots ~€9k ≈ €35k.",
     "risks": [("Inspectors do not accept the sensor log as evidence", "State the limit up front; sell as support to the manual record; get one written acceptance in the pilot before scaling"),
               ("Light sensor reads ambient light instead of the luminaire", "Mounting guidance, shielded sensor, baseline reading per node"),
               ("Buildings have no LoRaWAN", "Gateway in the kit; Cat-M gateway option"),
               ("Coin-cell life", "Report only on events; two-year estimate validated in EVT")],
     "boards_note": "The Seeed light sensor publishes its schematic; the M5Stack light units are the prototype path; the Stamp C6LoRa (open PCB and schematic) is the node core.",
     "diagram": "  LUMINAIRE: [light sensor facing the lamp] -> [ESP32-C6 + LoRa node, coin cell] -> LoRaWAN gateway (building)\n  TEST DAY: electrician triggers test as today -> nodes report lit / not lit / duration\n  SERVER: per-building test log, exceptions, export to the contractor's record  (evidence, not the duration test itself)",
     "bom": [("Light sensor", "1.0", ""), ("ESP32-C6 + LoRa module", "5.0", ""), ("Coin cell + holder", "1.0", ""), ("Enclosure + adhesive/magnet", "2.0", ""), ("PCB, passives", "1.5", "")],
     "firmware": "- ESP-IDF; light threshold with per-node baseline; event-based uplinks (lit, off, duration); deep sleep; LoRaWAN class A.\n- Server: building and luminaire register, test sessions, exception rules, export in the contractor's log format; API.",
     "weeks": ["Interviews incl. an inspector and two contractors; pilot proposals", "Prototype node", "Baseline and threshold logic", "Mounting tests on luminaire types", "Node PCB v1", "Server and log format",
               "EVT 100 nodes in two buildings", "One test cycle logged", "Inspector review of the log", "DVT", "Pre-compliance", "Certification; pilot roll-out"],
     "cert": CERT_BATT + "\n- Not emergency-lighting equipment: the node does not alter the luminaire; say so in the manual.",
     "cheapest": "Twenty prototype nodes in one building for one monthly function test, the log shown to the contractor and, if possible, the inspector; ask whether they would pay €59 per point.",
     "interview": "1) How do you test and log emergency lighting today, and how long does a round take? 2) What did the last inspection say about the log? 3) Who pays for the testing and what does it cost per year? 4) Would an automated log of 'lit / duration' help, and who would need to accept it? 5) At €59 per luminaire, how many buildings?",
     "landing": "headline \"The emergency-lighting test log, from a €59 sticker.\" Bullets: works on the luminaires you have; function and duration tests recorded; your contractor's format; evidence for the record, not a replacement for the test. Button: request a pilot (B2B).",
     "pass": "3 pilots and one written acceptance by an inspector or insurer within 12 weeks.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "EN 50172 / DIN VDE 0108 genuinely require periodic tested-and-logged emergency-lighting checks, and self-test systems (Zumtobel, Legrand and others under IEC 62034) only cover new installations, which confirms the older-luminaire gap.",
     "risk": "A light-sensor \"it lit\" reading is not the standard's duration test (which concerns battery-backed runtime); whether inspectors accept this log as compliance evidence is a genuinely open question, stated in the pack and asked in the kill question.",
     "rows": [["Eaton emergency-lighting inspection and maintenance guide", "Periodic function and duration tests with a log", "Compliance pull confirmed"], ["DIN VDE 0108 test-log guidance (Whitecroft)", "Log requirements", "Same"], ["Fagerhult self-test / EN 62034 explainer", "Self-test systems for new luminaires", "Gap for older stock confirmed"]]})

# B ---------------------------------------------------------------------------
bf = [board("m5stack-unit-uhf-rfid", "UHF RFID reader unit: the wand's front end"),
      board("m5stack-core2", "touch-screen controller for the prototype wand"),
      board("m5stack-cardputer", "keyboard handheld alternative for the list"),
      board("m5stack-unit-buzzer", "missing-tool alert"),
      board("m5stack-stickc-plus", "compact handheld core for a second prototype")]
note, share = open_note(bf)
add({"slug": "tool-check-wand", "title": "Tool Check Wand", "category": "Industrial & installer tools",
     "pitch": "A handheld UHF RFID wand that inventories a van's or a workshop's tagged tools in ten seconds and says what is missing before the van drives off, with a local list and no subscription; on-metal tag reliability to be proven in the field before any claim.",
     "audience": "Trades companies with 3–30 vans (electricians, plumbers, HVAC, builders), workshop managers, tool-hire counters; the owner pays after the second lost or stolen tool.",
     "why_now": "Van tool theft is large and documented (UK police data: 44,514 incidents in 2023, about £98m stolen), the existing answers are either locked to one tool brand (Milwaukee One-Key) or enterprise-priced (Hilti ON!Track subscription, Zebra readers at $900–1,900+), and the catalogue has a UHF reader unit.",
     "built_from": bf,
     "whats_new": "A wand with a UHF reader and antenna tuned for a van, a local tool list per van and per technician, a ten-second sweep that lists what is missing, a buzzer, and an optional end-of-day check-in; tags are standard UHF where possible and on-metal tags where needed; no cloud account.",
     "effort_weeks_est": "10–12", "bom_eur_est": "40–60", "price_eur_est": "199–249",
     "certification": "RED (UHF RFID reader EN 302 208, BLE), EMC, EN 62368-1, RoHS, WEEE, CRA; Battery Regulation / UN 38.3 for the cell.",
     "kill_question": "Do 10 trades companies tag one van each with 50 tags, achieve a reliable sweep (95%+ of tagged tools read in three sweeps, measured), and buy the wand at €229 after a two-week trial? Pass = 10 purchases and the read-rate met on real vans.",
     "open_files_share": share, "scores": {"demand": 3, "buildability": 4, "margin": 4, "speed": 4},
     "tags": ["industrial", "installer", "b2b", "rfid", "tools"], "open_boards_note": note, "score_total": 15},
    {"problem": "A technician drives off without the €600 drill and finds out at the next job, or the van is opened overnight and nobody knows what was in it; the trades company has no inventory of what is in which van, and the tools that offer tracking only track their own brand.",
     "customer": "Small and mid-sized trades companies with a few to a few dozen vans, workshop managers in facilities and manufacturing, tool-hire counters; the owner or operations lead pays.",
     "product": "A battery wand with a UHF reader: one sweep of the van or the shelf reads every tagged tool and lists what is missing against that van's list; buzzer, local app, end-of-day check-in, tags for every brand; no subscription. Read reliability on metal tools is measured in the pilot before any claim.",
     "ask": "~€55–70k to certification and a first 500 wands plus tags (estimate); ten trial purchases cover a tenth.",
     "problem_long": "The pain is documented: UK police figures put van tool theft at 44,514 incidents in 2023 and about £98m stolen, and every tradesperson has a story. Milwaukee One-Key tracks cheaply but only Milwaukee tools; Hilti ON!Track is a managed service at roughly $120 a month; enterprise UHF readers such as the Zebra RFD40 cost $900–1,900+ before software. Between them is the small trades company with mixed brands and no budget line. The technical risk is equally real: UHF tags on metal tools need on-metal tags, which cost more than standard labels and still read unevenly in a packed van; this pack treats read reliability as the first thing to measure, not something to assume.",
     "who_pays": "**Who pays, B2B:** the company owner or operations lead, usually after a loss; insurers may discount for inventory evidence (unverified). **Who uses:** the technician at the end of the day and the storeman at the counter; a sweep must take seconds or it will not happen.",
     "market": "- **TAM:** trades and service vans in DE/UK/NL/FR: estimate 5–8M; workshops and hire counters on top. Theoretical €1B+ at €229 plus tags.\n- **SAM:** companies with 3–30 vans and a recent loss: estimate 300,000 companies → €70M for wands plus tag revenue.\n- **SOM (3 yrs):** 15,000–30,000 wands and millions of tags; year-1: 500–1,000 wands through trade suppliers and insurers.",
     "searches": 3,
     "competition": [("Milwaukee One-Key", "Cheap tags and app, locked to Milwaukee tools", "Any brand, any tool; local list"),
                     ("Hilti ON!Track", "Managed asset tracking, about $120 a month (research, Nov 2026)", "No subscription; sized for a 5-van company"),
                     ("Zebra RFD40 and enterprise UHF readers", "$900–1,900+ per reader plus software", "A quarter of the price, with the van list built in"),
                     ("ToolWatch and asset-management software", "Software subscriptions with barcode or RFID", "Hardware first, no subscription; export to their software if wanted"),
                     ("A photo of the van and memory", "Free", "The ten-second sweep is the product")],
     "wedge": "a brand-agnostic ten-second van inventory at a quarter of enterprise reader prices and no subscription, if and only if the on-metal read rate holds in a real van.",
     "product_long": "- Wand: UHF reader (EU 865–868 MHz) with a directional antenna, BLE to the phone or an on-wand screen, buzzer, 8-hour battery; sweep mode and single-tag mode.\n- Lists: per van, per technician, per job kit; missing-tool list after a sweep; check-in at end of day; export CSV; optional sync to the company's existing software.\n- Tags: standard UHF labels for cases and plastic tools, on-metal tags for drills and metal tools, priced separately and honestly; a tagging guide per tool type.\n- Read-rate test built into the app: the pilot measures it on each van and the company sees the number before buying more.",
     "econ": econ_table("40–60", "199–249", 6.0, 10.0, 4.0, 4.0, 12, "trade suppliers and direct, ~€30", 30.0),
     "econ_note": "Lesson: the wand margin is modest; tags are the volume line (on-metal tags cost multiples of labels, so price them per type). Do not promise read rates before the pilot numbers.",
     "gtm": "**First 100 customers:**\n\n1. Ten trades companies, one van each, two-week trials with the read-rate measured.\n2. One trade supplier (electrical or plumbing wholesaler) as the shelf.\n3. One insurer's loss-prevention team as the referrer.\n\n**Scale channels:** trade wholesalers, van-fitting companies, insurers, hire counters.",
     "q1": "Kill-question trials; works-like wand on Core2 + UHF unit; read-rate tests on three real vans with standard and on-metal tags.",
     "q2": "Custom wand board and antenna; EVT 20 in ten companies; tagging guide.",
     "q3": "DVT; certification (UHF reader); 300 wands; trade-supplier listing.",
     "q4": "Insurer channel; 1,000 wands; sync integrations.",
     "team": "one RF/embedded engineer, one app developer, one founder from the trades or trade supply.",
     "funding": "NRE €25k (antenna and wand mechanics) + certification €12k + first 500 wands and tags landed ~€35k ≈ €72k; minus trial purchases ~€2k ≈ €70k.",
     "risks": [("UHF read rate on metal tools in a packed van", "Measure first; on-metal tags; antenna design; sweep technique in the guide; do not claim until measured"),
               ("Tag cost undermines 'tag everything'", "Tag only the valuable tools; price tags per type; say so"),
               ("Milwaukee or Hilti move down-market", "Brand-agnostic and no-subscription remain the wedge"),
               ("Technicians skip the sweep", "Ten-second target; end-of-day reminder; the missing list is the reward")],
     "boards_note": "All M5Stack products with published module files; the UHF-RFID unit is the reader front end for prototyping, the production wand needs its own antenna design.",
     "diagram": "  [UHF reader + directional antenna] -> [ESP32 core, 8 h cell] -> BLE -> phone app (lists per van / technician)\n           sweep 10 s -> read tags -> compare with the van list -> missing tools -> [buzzer] [screen]\n  tags: standard labels (cases, plastic) | on-metal tags (drills, metal tools)  read rate measured per van",
     "bom": [("UHF RFID reader module", "18.0", ""), ("Directional antenna", "6.0", "custom"), ("ESP32-S3 module + BLE", "3.0", ""), ("Li-ion cell + charger + USB-C", "5.0", ""), ("Wand enclosure + trigger + buzzer", "12.0", ""), ("PCB, screen option, passives", "6.0", "")],
     "firmware": "- ESP-IDF; reader driver (EPC Gen2), inventory rounds with session management, RSSI filtering; BLE to the app; local lists in flash.\n- App: vans, technicians, kits, sweep results, read-rate test, CSV export, optional sync.",
     "weeks": ["Interviews with ten companies; trial design", "Prototype wand", "Read-rate tests on three vans (standard vs on-metal tags)", "Antenna design", "Wand board v1", "App v0 with lists and sweep",
               "EVT 20 in ten companies", "Read-rate review; tagging guide", "Enclosure tooling decision", "DVT", "Pre-compliance (UHF)", "Certification; supplier listing"],
     "cert": CERT_BATT + "\n- UHF RFID reader: EN 302 208 radio testing; power limits for EU 865–868 MHz; antenna is part of the certified design.",
     "cheapest": "One prototype wand and 50 tags on one friendly company's van for two weeks; publish the read rate; ask ten companies whether they would buy at €229 given that number.",
     "interview": "1) What did you last lose or have stolen from a van, and what did it cost? 2) How do you know what is in each van today? 3) Have you tried One-Key, ON!Track or anything else; what stopped you? 4) What brands are your tools? 5) At €229 per wand plus tags, how many vans?",
     "landing": "headline \"Know what left the van before it leaves.\" Bullets: ten-second sweep; any brand; no subscription; read rate measured in your van first. Button: request a two-week trial (B2B).",
     "pass": "10 purchases after trials with the read-rate target met on real vans.",
     "production": PROD_STD + "\n- RF: antenna tuning per batch; read-rate test fixture on the line.",
     "next": NEXT_STD},
    {"verdict": "LIKELY",
     "summary": "Van tool theft is a confirmed, large pain point (UK police data: 44,514 incidents in 2023, about £98m stolen). A genuine gap exists between Milwaukee One-Key (cheap but locked to Milwaukee tools) and Hilti ON!Track / Zebra RFD40 (enterprise: readers $900–1,900+, ON!Track about $120 a month).",
     "risk": "UHF tags on metal tools are a real, unresolved reliability risk; on-metal tags cost more than standard tags, which could undercut the \"tag everything cheaply\" pitch. Needs real-world testing before claiming it works; the pack measures it first.",
     "rows": [["Direct Line / Fleetnews tool-theft data", "44,514 incidents, ~£98m stolen (UK, 2023)", "The pain is large and documented"], ["Hilti ON!Track (pricing discussion)", "Managed service, ~$120/month", "Enterprise incumbent with subscription"], ["Milwaukee One-Key (tag pricing)", "Cheap tags, Milwaukee tools only", "Brand-locked incumbent"], ["Zebra RFD40 (pricing)", "$900–1,900+ per reader", "Enterprise incumbent, 4× the target"]]})

# C (fix: paging intercom, not cueing; mic-interference unverified) ------------
bf = [board("m5stack-unit-mic", "microphone unit for the stage talk station"),
      board("m5stack-unit-mini-pdm", "digital microphone alternative"),
      board("seeed-grove-speaker-plus", "open amplified speaker reference circuit"),
      board("m5stack-atoms3-lite", "ESP32-S3 core for stations and speakers"),
      board("m5stack-unit-button", "push-to-page button")]
note, share = open_note(bf)
add({"slug": "backstage-relay", "title": "Backstage Relay", "category": "Audio",
     "pitch": "A paging and show-relay set for small venues and school theatres: one stage microphone station, three battery speakers for dressing rooms and the green room, and a push-to-page button for the stage manager, over WiFi or ESP-NOW; for announcements and listening in, not for calling cues, which stay with the cue lights.",
     "audience": "Amateur theatres, school and university stages, churches with performances, small event venues; the same buyers as the cue-light set, which this pairs with.",
     "why_now": "Technical-theatre forums (ControlBooth among them) carry active threads from ultra-low-budget groups asking for exactly this and ready to build it, while professional show-relay and paging systems run into the thousands; WiFi audio over catalogue parts is cheap, as long as it is sold for what it does.",
     "built_from": bf,
     "whats_new": "A stage station with a microphone and a page button, battery speakers that play the stage feed quietly and switch to a page announcement at full volume, a simple pairing, and a clear positioning: half-second-class latency is fine for 'five minutes to places' and listening to the show, and useless for split-second cues, which the cue-light set handles; 2.4 GHz coexistence with wireless microphones is tested on site, not assumed.",
     "effort_weeks_est": "10", "bom_eur_est": "60–90", "price_eur_est": "299–399",
     "certification": "RED via pre-certified ESP32 module (2.4 GHz), EMC, EN 62368-1, RoHS, WEEE, CRA; Battery Regulation / UN 38.3 for the speaker cells.",
     "kill_question": "Do 10 amateur groups or schools pre-order at €349 after a video demo that states the latency and the 'paging, not cueing' scope, and do 5 of them already own or pre-order the cue-light set? Pass = 10 deposits, 5 paired, in 6 weeks.",
     "open_files_share": share, "scores": {"demand": 3, "buildability": 5, "margin": 4, "speed": 5},
     "tags": ["events", "audio", "education", "b2b", "wifi"], "open_boards_note": note, "score_total": 17},
    {"problem": "In a small venue the dressing rooms cannot hear the show and the stage manager cannot call 'five minutes to places' without running; the professional show-relay and paging systems that solve it are installed products priced for theatres with a technical budget.",
     "customer": "Amateur dramatic societies, school and university stages, churches with performances, small event venues; the society or the drama department pays, often together with the cue-light set.",
     "product": "A stage microphone station with a page button and three battery speakers that play the stage feed quietly and switch to announcements at full volume, over WiFi or ESP-NOW, pairing in a minute; positioned for paging and listening in, with the latency stated, never for calling cues.",
     "ask": "~€45–60k to certification and a first 500 sets (estimate); pre-orders paired with the cue-light set cover a third.",
     "problem_long": "ControlBooth and similar forums show the demand: groups with no budget asking how to get the show into the dressing rooms and announcements back out, and ready to build it. The research also found the failure to avoid: a venue reported that WiFi and ESP-NOW-style paging was \"virtually useless for cueing\" because of latency. That is right, and it is why this product is not a cueing system: paging and show relay tolerate a half second; cues do not and stay with the cue-light set. A second open point stays open: 2.4 GHz coexistence with the venue's wireless microphones was not resolved by the research or a clean comparison, so the pack calls for an on-site test and does not assume it is fine.",
     "who_pays": "**Who pays:** the society or school (small budgets, equipment grants); bundled with the cue-light set the buyer is the same stage manager. **Who uses:** actors in the dressing rooms (listen), the stage manager (page), front of house (page).",
     "market": "- **TAM:** amateur theatre groups, schools with a stage and small venues across DE/UK/NL/AT/CH: tens of thousands. Theoretical €10–20M.\n- **SAM:** groups that already own some technical kit and stage two or more productions a year: estimate 10,000 → €3.5M.\n- **SOM (3 yrs):** 1,500–2,500 sets, half of them with the cue-light set; year-1: 300–500.",
     "searches": 3,
     "competition": [("Clear-Com / Tecpro show relay and paging", "Installed professional systems, thousands of euros", "A tenth of the price, portable, battery"),
                     ("Williams AV and assistive-listening transmitters", "Professional audio distribution", "Different purpose and price class"),
                     ("Baby monitors and walkie-talkies", "Cheap improvisations found on the forums", "Multi-room, page button, proper speakers, pairs with the cue lights"),
                     ("DIY builds on ControlBooth and similar", "Groups building their own", "Demand signal; we ship the box and state the limits")],
     "wedge": "a boxed, honest paging and show-relay set at a tenth of professional prices, sold alongside the cue lights so each does the job it can do.",
     "product_long": "- Stage station: microphone (switchable stage pickup), page button, level control, USB-C power; optional front-of-house station.\n- Speakers: battery (one show per charge, estimate), quiet show-relay level with page override at full volume, wall hook and stand; three in the set, up to eight.\n- Link: WiFi (venue network) or ESP-NOW point-to-multipoint; latency stated on the box (target under 300 ms; measured value published); not for cues.\n- Coexistence: a built-in channel scan and a printed on-site test procedure for venues with wireless microphones; recommendation to test before the first show.",
     "econ": econ_table("60–90", "299–399", 7.0, 14.0, 5.0, 5.0, 10, "direct + theatre suppliers, ~€28 per set", 28.0),
     "econ_note": "Lesson: four enclosures and three cells per set; bundle with the cue-light set to share the sales effort and the shipping box.",
     "gtm": "**First 100 customers:**\n\n1. Ten groups from one federation, half of them existing cue-light pre-orderers, after a video demo that shows the latency honestly.\n2. Drama departments through their teachers' association.\n3. Small venues and churches via AV hire companies.\n\n**Scale channels:** theatre suppliers, federation festivals, the cue-light customer list.",
     "q1": "Kill-question pre-orders; works-like set on AtomS3 + MIC + Speaker-Plus; latency measured and published; coexistence test with a borrowed wireless-mic rack.",
     "q2": "Custom boards (station, speaker); enclosures; EVT 10 sets with two groups.",
     "q3": "DVT; certification; 200 sets; bundle with cue lights.",
     "q4": "Supplier listing; 500 sets; eight-speaker option.",
     "team": "one embedded engineer with audio experience, one founder from the theatre world (shared with the cue-light pack); enclosure design bought in.",
     "funding": "NRE €22k + certification €10k + first 500 sets landed ~€45k ≈ €77k; minus pre-orders ~€20k ≈ €57k.",
     "risks": [("Buyers expect it to call cues", "Say 'paging and show relay, not cues' everywhere; bundle with the cue lights; publish the latency"),
               ("2.4 GHz interference with wireless microphones", "On-site test procedure; channel scan; do not claim coexistence until tested in real venues"),
               ("Audio quality and dropouts over WiFi", "Codec and buffer choice; ESP-NOW mode; EVT in steel-framed halls"),
               ("Battery life for a long show", "One show per charge target; USB-C power option for fixed speakers")],
     "boards_note": "The Seeed speaker board publishes its schematic; the M5Stack microphone and core units are the prototype path; two PCBs (station, speaker).",
     "diagram": "  STAGE STATION: [mic] [page button] -> [ESP32-S3] -> WiFi / ESP-NOW -> SPEAKERS 1..8: [ESP32-S3] -> [amp + speaker] [cell]\n                                            quiet show relay  |  page = full volume     latency stated; not for cues\n  pair with: cue-light set (standby / go)",
     "bom": [("Microphone + preamp", "4.0", ""), ("ESP32-S3 modules ×4", "10.0", ""), ("Amplifier + speaker ×3", "18.0", ""), ("Li-ion cells + chargers ×3", "12.0", ""), ("Enclosures ×4", "16.0", ""), ("PCBs, buttons, USB-C, passives", "10.0", "")],
     "firmware": "- ESP-IDF; I2S capture, low-bit-rate codec, multicast over WiFi or ESP-NOW with jitter buffer; page override; channel scan; latency measurement mode.\n- Pairing by button; no app required; optional web page for levels.",
     "weeks": ["Pre-orders with an honest demo video; interviews", "Prototype set", "Latency and dropout measurements", "Coexistence test with wireless mics", "Two PCBs v1", "Enclosures",
               "EVT 10 sets in two venues", "Show feedback", "Tooling decision", "DVT", "Pre-compliance", "Certification; bundle fulfilment"],
     "cert": CERT_BATT,
     "cheapest": "A three-speaker prototype in one group's dressing rooms for one production, latency and interference noted; ask ten groups whether they would buy at €349 knowing it does not call cues.",
     "interview": "1) How do your dressing rooms hear the show and the calls today? 2) What have you improvised and what failed? 3) Do you use wireless microphones; how many channels? 4) Who pays for kit and when? 5) At €349 for a station and three speakers, paging only, would you order?",
     "landing": "headline \"Five minutes to places, heard in every dressing room.\" Bullets: show relay and paging; three battery speakers; pairs with the cue lights; not for cues; €349. Button: refundable €50 deposit.",
     "pass": "10 deposits, 5 of them paired with the cue-light set, in 6 weeks.",
     "production": PROD_STD, "next": NEXT_STD},
    {"verdict": "UNCERTAIN",
     "summary": "Real DIY community interest is confirmed (ControlBooth forum threads, including ultra-low-budget groups open to DIY), but a venue reported in a forum thread that WiFi / ESP-NOW-style paging was \"virtually useless for cueing\" because of latency, a documented failure.",
     "risk": "Repositioned before building as a paging and show-relay intercom for non-time-critical communication, paired with the cue-light set rather than replacing it; 2.4 GHz interference with wireless microphones stays unverified and needs on-site testing.",
     "correction": {"title": "Built with the research fix applied (November 2026)",
                    "text": "The research found a venue reporting WiFi-style paging as useless for cueing because of latency. This pack therefore sells the set as a paging and show-relay intercom for announcements and listening in, states the latency, and leaves split-second cues to the cue-light set it pairs with. Coexistence of 2.4 GHz audio with wireless microphones was not resolved by the research and is treated as an on-site test, not an assumption. As researched November 2026 by web search; verify before relying on it."},
     "rows": [["ControlBooth forum threads", "Low-budget groups asking for and building show relay / paging", "Demand signal"], ["Venue report on WiFi / ESP-NOW paging latency", "\"Virtually useless for cueing\"", "Scope fixed: paging, not cues"], ["Clear-Com / Tecpro show relay", "Professional installed systems, thousands of euros", "Incumbent at a multiple of the target"]]})


def main():
    ideas = json.loads(r2.IDEAS_PATH.read_text(encoding="utf-8"))
    market = json.loads(r2.MARKET.read_text(encoding="utf-8"))
    have = {i["slug"] for i in ideas["ideas"]}
    added = 0
    for i in IDEAS:
        if i["slug"] in have:
            continue
        ideas["ideas"].append(i)
        (r2.PACKS / f"{i['slug']}.md").write_text(r2.pack_md(i, PACKSPEC[i["slug"]]), encoding="utf-8")
        market["ideas"][i["slug"]] = MARKETSPEC[i["slug"]]
        added += 1
    for r in ideas.get("rounds", []):
        if r.get("date") == "2026-11-14" and "Round 2" in r.get("note", ""):
            r["slugs"] = sorted(set(r["slugs"]) | {i["slug"] for i in IDEAS})
            r["note"] = "Round 2: 16 ideas added after an external market check of 19 candidates (12 as-is, 4 with the researcher's fix applied; 3 dropped)."
    r2.IDEAS_PATH.write_text(json.dumps(ideas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    r2.MARKET.write_text(json.dumps(market, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"added {added} ideas; total {len(ideas['ideas'])}")


if __name__ == "__main__":
    main()
