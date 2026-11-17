# Refill-Station Level Radar — Founder Start Pack

> A clip-on radar for the bulk dispensers and canisters in zero-waste and refill shops. It shows how full each container is and tells the owner what to reorder, measuring through the lid without touching the liquid.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Refill and zero-waste shops run on thin margins and dozens of bulk containers: detergents, soaps, oils, vinegar, plus gravity bins of nuts and grains. Nobody knows what's running low until a customer stands at an empty tap. Stock checks are manual, done at closing time, and reorders are guesswork.
- **Customer:** Independent refill/zero-waste shops (20–80 dispensers), organic stores with refill corners, and the operators of detergent/soap refill points in supermarkets (brands and service companies that restock them). The shop owner or the refill-point operator pays.
- **Product:** One measurement point per container: a Hi-Link LD8001B 79 GHz liquid-level radar (±5 mm accuracy, up to 15 m, per datasheet) clipped above or on the lid, or a load-cell unit (M5Stack Weight-I2C class) under gravity bins for dry goods. An ESP32-C3 hub per shelf collects readings over Wi-Fi. Dashboard: fill % per container, days-to-empty, reorder list per supplier.
- **Why now:** The EU Packaging and Packaging Waste Regulation (PPWR) pushes refill and reuse, so refill points are spreading from niche shops into supermarkets and drugstores. Compact 79 GHz radar modules now measure liquid level without contact, which matters for food and chemicals.
- **The ask:** About €90–120k (estimate) to the first 1,000 measurement points. Realistically, it needs one refill-point operator or supermarket pilot as anchor customer, because independent shops can't afford €80 × 40 points.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Does the radar read reliably through the HDPE/glass lids actually used in refill shops? Test 10 container types; if more than 3 need a lid hole, rethink.

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Refill and zero-waste shops, organic stores, bulk detergent/soap refill points in supermarkets.

**The problem as the pack states it:** Refill and zero-waste shops run on thin margins and dozens of bulk containers: detergents, soaps, oils, vinegar, plus gravity bins of nuts and grains. Nobody knows what's running low until a customer stands at an empty tap. Stock checks are manual, done at closing time, and reorders are guesswork.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **Unverpackt e.V. (DE)** · https://www.unverpackt-verband.de/ — German association of package-free and refill shops.
- **r/ZeroWaste** · https://www.reddit.com/r/ZeroWaste/ — zero-waste shoppers and some shop owners.
- **EuroCommerce** · https://www.eurocommerce.eu/ — European retail and wholesale federation.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€79–99 per point (estimate), the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how refill and zero-waste shops, organic stores, bulk detergent/soap refill points in supermarkets deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. How do you know today which of your refill containers are running low, how often do you check, and when did a product last run out before the delivery came?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A clip-on radar for the bulk dispensers and canisters in zero-waste and refill shops that shows how full each container is and tells the owner what to reorder — through the lid, no contact with the liquid. On a scale of one to ten, how likely would you be to buy that at €79–99 per point (estimate), and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: Refill-Station Level Radar: would you pay €79–99 per point (estimate) for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a Refill-Station Level Radar: A clip-on radar for the bulk dispensers and canisters in zero-waste and refill shops that shows how full each container is and tells the owner what to reorder — through the lid, no contact with the liquid. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €79–99 per point (estimate), the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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
Be honest about who can pay. An independent refill shop with 40 containers would spend €3,000+ on per-point radar. Most of those shops are 1–2-person businesses that don't have it. And their **checkout scale/POS already records what was sold per product**, so "delivered minus sold" gives a rough stock level for free if the POS is set up properly.

**The better first customer is the operator of refill stations in larger retail:** a detergent or personal-care brand (or service company) running refill machines in 50–500 supermarket or drugstore locations. They send staff or drivers to restock, and an empty station is lost sales across a whole network of stores. For them, remote fill levels plan routes and restocking. Second: **organic supermarket chains with refill corners** (10–30 dispensers per store, many stores, central purchasing). Third: independent shops, with a cheap "top 10 containers" kit.

### Market size (estimates)
- Refill/bulk points in EU retail: assume ~15,000 independent refill/organic shops with bulk sections (avg 30 points) + ~20,000 supermarket/drugstore refill stations (avg 6 points) by 2028, as PPWR reuse targets kick in → **~570,000 measurement points**.
- **TAM:** 570,000 × €89 ≈ **€51 M**, plus software (€1/point/month ≈ €7 M/yr).
- **SAM:** DE, FR, NL, BE, AT, Nordics, liquid points first (radar fits liquids best): ~35% → **~200,000 points ≈ €18 M**.
- **SOM (3 years):** 1 refill-point operator (3,000 points) + 2 organic chains (2,000 points) + 100 independent shops (1,000 points) → **~6,000 points ≈ €0.5 M hardware + ~€70k/yr software**.

### Competition
| Alternative | Cost (estimate) | Weakness we attack |
|---|---|---|
| Weight-based refill dispensers (e.g. shop-fitting makers' liquid dispensers with built-in weight sensors that track fill level) | Part of a new dispenser system, high per point | Requires replacing the dispensers |
| Generic LoRaWAN fill-level sensors (e.g. Milesight WS201, time-of-flight, battery, refill alerts) | ~$55–91 per sensor (retail listings) + LoRaWAN gateway | ToF optical reads into the container, so needs a line of sight to the surface (lid hole, transparent path); not made for food/chemical refill shops; no reorder logic |
| POS-based stock (delivered − sold, from the checkout scale) | Already paid for | Works only if every delivery and every sale is entered correctly; drift and spillage; no real level |
| Manual stock check at closing | Staff time | Late, error-prone, no forecast |
| Do nothing | Free | Empty taps, lost sales, rush orders |

**Wedge:** **contactless through the lid** (no hole, no contact with food or detergent, no hygiene question), retrofit onto existing dispensers, plus a reorder list grouped by supplier. For the refill-point operator: multi-store view and restock planning.

### Product & value proposition
- **Liquid point:** LD8001B 79 GHz FMCW radar (79–81 GHz, 3.3 V, ~135 mA average / 600 mA peak, 200 ms response, UART, 35.3 × 35.3 mm, ±50° H / ±40° V beam per Hi-Link). Mounted in a small clip or adhesive housing on the lid, pointing down. Powered over a shelf bus (current draw rules out coin cells; it's a wired or USB product, or duty-cycled with a sizeable battery, to be measured).
- **Dry-goods point:** load cell + HX711-class amplifier under gravity bins (M5Stack Weight-I2C as the prototype unit), because radar on a cone of nuts is noisy.
- **Shelf hub:** ESP32-C3 reads up to ~16 points over RS-485 or a simple daisy-chained UART/I²C bus, sends to the cloud over Wi-Fi.
- **Software:** container set-up (shape/volume table per container type, product, supplier), fill %, days-to-empty from sales speed, reorder list per supplier, low-level alerts. Multi-store view and restock planning for operators.
- **Later:** shelf-edge e-ink price tag showing price/kg and "refilled today".

**Honest physics:** 79 GHz radar passes through thin HDPE and PP lids reasonably well, less well through thick glass, not at all through metal lids. Its beam is wide (±40–50°), so in narrow tall containers the walls cause reflections. That's why the kill question is "does it read through real lids in real containers".

**Pricing (estimates):** €89 per liquid point, €59 per weight point, shelf hub €49; software €1/point/month (operators with many stores) or free for single shops up to 10 points. Shop starter kit: hub + 8 points €590.

### Unit economics (estimates per liquid point, ex-VAT)
| Item | 1k points | 5k points |
|---|---|---|
| BOM (LD8001B radar, MCU/bus interface, connector, PCB, share of hub) | €24.00 | €19.00 |
| Assembly & test (radar distance test against a reference target) | €2.50 | €1.80 |
| Enclosure (radar-transparent clip housing) | €1.80 | €1.00 |
| Packaging | €0.70 | €0.50 |
| Freight + duty to EU | €0.80 | €0.50 |
| Certification amortised (~€25k: RED 79 GHz + 2.4 GHz hub, EMC, EN 18031) | €25.00 | €5.00 |
| **Landed cost** | **€54.80** | **€27.80** |
| Net price ex-VAT: direct to shops €75 (from €89) / operator volume price €60 | €75 / €60 | €75 / €55 |
| **Gross margin** | **€20 (27%) direct / €5 (9%) operator** | **€47 (63%) / €27 (49%)** |

Read it: 1k points barely pays for certification. You need the anchor operator's volume (several thousand points) and the software fee. Confirm the LD8001B unit price at volume early: 79 GHz modules cost more than 24 GHz ones, and that one line decides the business.

### Go-to-market
**First 100 customers (points, then sites):**
- **Refill-point operators:** detergent and personal-care brands running refill machines in retail, and the service companies restocking them. Two conversations decide the business.
- **Organic supermarket chains** with refill sections: category/operations managers, not store staff.
- **Zero-waste shop networks and associations** (national unpackaged-shop associations exist in several countries) for the independent-shop kit and for feedback.
- **Shop-fitting companies** that install bulk dispensers: they can pre-fit the sensors.

**Scale channels:** shop fitters and dispenser makers (OEM), retail-tech resellers, POS/inventory software integrations (sync levels into the shop's stock system).

### 12-month plan
| Quarter | Milestones |
|---|---|
| Q1 | Kill question: lid test on 10 container types; interviews with 2 refill-point operators + 2 organic chains + 10 shops; one pilot site |
| Q2 | Shelf bus + hub PCB, clip housing; dashboard v1 with reorder list; 40-point pilot in 2 shops + 1 operator's 5 stations |
| Q3 | DVT; RED (79 GHz) + EMC + EN 18031 testing; weight-point variant; POS integration #1 |
| Q4 | 1,000 points; operator contract (if pilot passes); e-ink tag prototype |

**Team:** founder (retail/operator sales), 1 embedded engineer (radar signal handling, bus, firmware), 1 web developer (dashboard, forecasting, integrations), part-time industrial designer (clip housings for common dispensers).

**Funding to the first 1,000 points (estimates):** NRE €50k (electronics + hub €15k, firmware €12k, dashboard €15k, housings €8k) + certification €25k + 1,000 points landed ex-cert ~€30k + hubs (70 × €20) €1.4k + 9 months lean costs €30k ≈ **€136k**; minus pilot fees/pre-orders (~€20k) → **~€115k**. Route: paid operator pilot, sustainability/circular-economy innovation grants (PPWR-related programmes are appearing in several member states), a small angel.

### Top risks
| Risk | Mitigation |
|---|---|
| **Technical: radar through lids, wall reflections in narrow containers, foam on detergents** | Kill-question test on 10 real container types first; per-container calibration table; filtering; if >3 of 10 need a lid hole, rethink |
| **Market: shops can't afford per-point sensors; POS already "knows" stock** | Anchor on operators/chains; independent kit only for the top 10 fast-movers; combine POS sales with sensor truth |
| **Cost: 79 GHz module price** | Get Hi-Link volume quotes before committing; consider a cheaper ToF variant for transparent containers |
| **Regulatory: 79 GHz level radar standards** | Check whether the use counts as level-probing radar in open air (EN 302 729) or in closed tanks (EN 302 372) with a test lab early |
| **Power: 135 mA average rules out small batteries** | Wired shelf bus as default; battery variant only with heavy duty-cycling, measured |
| **Supply: LD8001B sole source** | Radar abstraction layer; keep a ToF/weight fallback per container type |

## 4. Start kit

### Boards to start from
| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| Hi-Link HLK-LD8001B 79 GHz liquid-level radar | https://www.gongbans.com/db/hilink-ld8001b.html | Contactless level: 79–81 GHz FMCW, ±5 mm, 15 m range, 200 ms response, UART, 35.3×35.3 mm (per Hi-Link) | Datasheet public; schematics/files via maker (contact Hi-Link) | Commercial module, no open design files |
| M5Stack Unit Weight-I2C (U180) | https://www.gongbans.com/db/m5stack-unit-weight-i2c.html | Load-cell interface for dry-goods gravity bins (prototype) | Enclosure/structure files only (main-board electronics not published) | Dev unit; production uses your own load-cell amplifier design |
| Espressif ESP32-C3-DevKitM-1 | https://www.gongbans.com/db/espressif-esp32-c3-devkitm-1.html | Shelf hub: Wi-Fi + BLE controller | Schematic | Espressif reference designs free to use; ship on a pre-certified module |

### Block diagram
```
[container lid] <- clip housing: [LD8001B 79 GHz radar] --UART--> [point MCU]--+
[gravity bin]   <- [load cell] --> [HX711-class amp] --> [point MCU]-----------+--RS-485 / shelf bus (power + data)
                                                                               |
                                                    [Shelf hub: ESP32-C3] <----+
                                                         |~~ Wi-Fi ~~> [cloud: fill %, days-to-empty, reorder list, fleet view]
                                                         `-- 24 V/12 V shelf PSU
```
**Engineering gap:** radar signal processing for small containers (first-echo picking, wall/lid reflection rejection, foam), container shape → volume tables, a cheap robust shelf bus with power, calibration UX, forecasting from consumption rates, reorder lists per supplier, POS integration.

### Starter BOM (estimates at 1k points)
| Part | Est. cost | Notes |
|---|---|---|
| HLK-LD8001B radar module | €15–20 | **Biggest cost line; sole source (Hi-Link); get volume quote** |
| Point MCU (small Cortex-M0 or ESP32-C3 if wireless) | €0.80–2.00 | Wired bus keeps it cheap |
| RS-485 transceiver + connectors | €1.20 | |
| PCB + passives | €1.00 | |
| Clip housing | €1.80 | Radar-transparent plastic, uniform thickness |
| Load cell + amplifier (weight point) | €4–6 | Separate SKU |
| Hub: ESP32-C3 module, PSU, enclosure | €8–10 per hub | One per shelf |

### Firmware/software starting point
- **Radar:** Hi-Link's LD8001B UART protocol from the datasheet/user manual; ask Hi-Link for their configuration tool (their download centre lists tools for many radars).
- **Hub:** ESP-IDF (Modbus RTU over RS-485 is a simple, well-supported choice: search "esp-modbus").
- **Weight:** HX711-class libraries are widespread (search "HX711 ESP-IDF"); M5Stack's Weight-I2C examples for the prototype.
- **Backend:** any EU-hosted stack; simple linear consumption forecast is enough for v1.

### 12-week build plan
| Weeks | Phase | Exit criteria |
|---|---|---|
| 1–2 | Validate | **Kill question:** LD8001B on 10 real container types (HDPE, PP, glass, with/without lid). Pass: ≤3 of 10 need a lid hole, ±1 cm repeatability. Plus 2 operator/chain interviews with a pilot "yes" |
| 3–5 | Works-like | 8 radar points + ESP32-C3 hub on a test shelf; fill % within ±3% of volume on 4 container shapes, incl. foaming detergent |
| 6–8 | Looks-like + EVT | Point PCB + clip housing, shelf bus; 40 points in 2 shops / operator stations for 4 weeks; reorder list used by staff |
| 9–10 | DVT + pre-compliance | RED pre-scan at 79 GHz with a lab that has the gear (few do; book early), EMC, EN 18031 gap analysis |
| 11–12 | Pilot batch | 50–100 points live; zero "empty tap" events at pilot sites; operator quote request for all their stores |

### Certification checklist (EU)
- **CE under RED:** 79 GHz radar (level-probing radar standards: EN 302 729 for LPR / EN 302 372 for TLPR in closed tanks; confirm which applies with a test lab; 79 GHz test capability is limited and pricey), 2.4 GHz Wi-Fi/BLE in the hub (EN 300 328, reuse module reports), EMC EN 301 489-1/-3, safety EN 62368-1 (low-voltage supply), RF exposure. Est. **€12–18k**.
- **RED delegated act cybersecurity EN 18031-1** for the internet-connected hub (business inventory data; -2 only if personal data). Est. **€5–8k**.
- **CRA:** reporting from 11 Sept 2026, full from 11 Dec 2027: OTA, SBOM, vulnerability handling, support period.
- **RoHS, REACH, WEEE, packaging registration.**
- **Food contact:** none if mounted on/above the lid; if a housing could touch food (dry-goods bins), use food-contact-compliant materials (EU 1935/2004, 10/2011 for plastics).
- **GDPR:** essentially none (container levels); staff log-ins only.
- **Not applicable:** LVD (low-voltage shelf bus), battery regulation (unless you add a battery variant).
- **Total estimate: €17–26k.**

### Validation toolkit
- **Kill question:** Does the radar read reliably through the HDPE/glass lids actually used in refill shops? Test 10 container types; if more than 3 need a lid hole, rethink.
- **Second kill question:** Will a refill-point operator or chain pay €60–89 per point, given that POS data gives a rough stock level for free?
- **Cheapest experiment (~€150):** one LD8001B + a USB-serial adapter + a laptop, taken to 2 refill shops for an afternoon. Measure 10 containers, compare to a ruler.
- **5-question interview (shop owner / operator):**
  1. How do you know today what's running low? How long does it take?
  2. How often did a container run empty last month? What did that cost?
  3. Does your POS tell you stock per product, and do you trust it?
  4. Who orders from which supplier, and how often?
  5. €89 per container, or €590 for your top 8: worth it? What would make it worth it?
- **Landing-page headline:** "Never an empty tap again."
  - Sees through the lid how full every dispenser is. No contact with the product.
  - Days-to-empty and a reorder list per supplier.
  - Clips onto the containers you already have.
- **Pass threshold:** lid test passes **and** one operator/chain signs a paid pilot (≥40 points) or 10 shops pre-order the starter kit.

### First production checklist
- **Samples:** radar modules from the production lot tested on a reference container; clip housings tested on the top 5 dispenser types.
- **Golden sample:** point + hub with calibration table, measured distance error at 3 fill levels, firmware version.
- **DFM review:** radar window thickness (uniform, no metallic paint or label in front), clip strength on wet/slippery lids, cleanability, bus connector robustness.
- **MOQ talk:** LD8001B (price breaks at volume are the key negotiation), housings, RS-485 cables.
- **QC/AQL:** AQL II 1.0/2.5; 100% distance test against a reference reflector at 2 distances; 100% bus communication test.
- **Packaging:** points in multi-packs, hub, cables, container set-up card (QR → shape table).
- **Incoterms:** FCA Shenzhen; small air batches for pilots.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 3 board publishers (Hi-Link (海凌科) and M5Stack and Espressif).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **Hi-Link (海凌科)** (深圳市海凌科电子有限公司, hlktech.com) — module maker; 155 boards in the catalogue; files via Hi-Link (Shenzhen Hi-Link Electronic) product catalogue · https://www.hlktech.com. Directory entry: WiFi / BLE / radar sensor / power module maker: WiFi & router modules (MT7688/MT7628/WiFi6); BLE modules; 5.8/10/24/60/79 GHz mmWave radar sensors; AC-DC & DC-DC power modules; face / fingerprint recognition modules. Datasheets are public on hlktech.com (download centre); anything beyond the public datasheets has to be asked from Hi-Link directly. Boards used here: [HLK-LD8001B 79 GHz liquid-level detection radar module](/db/hilink-ld8001b.html) (79 GHz liquid-level radar module). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack Unit Weight-I2C (U180)](/db/m5stack-unit-weight-i2c.html) (load-cell option for dry goods (nuts, grains) in gravity bins). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.
- **Espressif** — chip house; 48 boards in the catalogue; files via Espressif esp-dev-kits (GitHub) · https://github.com/espressif/esp-dev-kits. Boards used here: [Espressif esp32-c3-devkitm-1](/db/espressif-esp32-c3-devkitm-1.html) (Wi-Fi controller and dashboard). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **AI-Thinker** (安信可科技(深圳)有限公司) · ai-thinker.com — ESP8266 / ESP32 module OEM: ESP-01; ESP32-CAM; A9 GSM modules; massive community. *(ESP32 / ESP8266 modules)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the Hi-Link (海凌科) and M5Stack and Espressif websites)

```email
Subject: Sample order and volume pricing — HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1 — for a Refill-Station Level Radar

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a Refill-Station Level Radar: A clip-on radar for the bulk dispensers and canisters in zero-waste and refill shops that shows how full each container is and tells the owner what to reorder — through the lid, no contact with the liquid. The design is built around your HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1.

Could you please send:
1. Price and lead time for [10] sample units of each: HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1.
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
主题：样品订购及批量报价 — HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1 — 用于Refill-Station Level Radar

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Refill-Station Level Radar：A clip-on radar for the bulk dispensers and canisters in zero-waste and refill shops that shows how full each container is and tells the owner what to reorder — through the lid, no contact with the liquid。产品设计基于贵司的HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1。

请提供以下信息：
1. 各[10]片样品的单价和交期：HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1。
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
Subject: PCBA quote from open design files — Refill-Station Level Radar, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a Refill-Station Level Radar: A clip-on radar for the bulk dispensers and canisters in zero-waste and refill shops that shows how full each container is and tells the owner what to reorder — through the lid, no contact with the liquid. The design starts from published open-hardware files (HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — Refill-Station Level Radar，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款Refill-Station Level Radar：A clip-on radar for the bulk dispensers and canisters in zero-waste and refill shops that shows how full each container is and tells the owner what to reorder — through the lid, no contact with the liquid。设计基于已公开的开源硬件文件（HLK-LD8001B 79 GHz liquid-level detection radar module, M5Stack Unit Weight-I2C (U180), Espressif esp32-c3-devkitm-1；含原理图、PCB和BOM），并做了我们自己的修改。

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
1. Order 3 LD8001B modules and a USB-UART adapter; run the 10-container lid test in a real refill shop.
2. Ask Hi-Link for volume pricing at 1k/5k/20k on the LD8001B and the 79 GHz level-radar certification reports they have.
3. Book 2 calls with refill-point operators (brands running refill machines in retail) and 2 with organic chains; ask the POS question.

Want help sourcing or building this? Talk to us via www.gongbans.com.
