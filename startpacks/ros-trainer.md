# ROS Trainer Robot — Founder Start Pack

> A ready-built ROS navigation robot on an open RK3566 board — lidar-ready, camera-ready — sold as a classroom platform for vocational schools and applied universities teaching mobile robotics.

Concept from the GONGBANS inventor. Not validated. All numbers are estimates — check them. Check every board's licence before commercial use.

## 1. Summary

- **Problem:** Industry wants ROS 2 skills; schools teach them on a TurtleBot 4 (€1,300–2,500 per robot at retail) or a Chinese kit with Chinese documentation. A class of 20 needs 5–10 robots; most programmes have two and a simulator.
- **Customer:** Vocational schools (Berufsschulen, ROCs, lycées pro), applied universities (Hochschulen, hogescholen), robotics bootcamps and corporate training in DE/NL/FR/Nordics. The teacher specifies; the school or an education distributor pays.
- **Product:** A fully assembled ROS 2 differential-drive robot on an open RK3566 SBC with a 2D lidar, a depth or RGB camera, a swappable sensor deck, charging dock, an English ROS 2 image and a 12-week curriculum (SLAM, navigation, perception). €899–1,299 per robot (estimates); class set of 5 with dock and curriculum licence.
- **Why now:** An open ROS trolley design on the Taishan Pi RK3566 board already exists with schematics and PCB; ROS 2 LTS releases are stable enough for a school year; and the alternatives are either premium-priced or undocumented in European languages.
- **The ask:** ~€140k to the first 300 robots (60 class sets). This is a €1,000 product — 1,000 units would be €250k+ of inventory, so the first-year goal is 300; the funding math below is for 300, with 1,000-unit costs shown for reference.

## 2. Validate demand first

<!-- validate-demand:start -->
**Do this before anything else in this pack: before the business plan, before you order a sample board, and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; 15–20 conversations are cheap.

### The gate: this idea's kill question

> Do 3 schools buy a 5-robot class set at €999 each for the coming semester?

You pass this section when you can answer that question with evidence you collected yourself, not a guess: a measured conversion on a fake-door landing page for the consumer side and, for the business side, at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order. Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.

### Who you are looking for

**The audience named in the idea:** Vocational schools, applied universities, robotics bootcamps and corporate training in DE/NL/FR/Nordics.

**The problem as the pack states it:** Industry wants ROS 2 skills; schools teach them on a TurtleBot 4 (€1,300–2,500 per robot at retail) or a Chinese kit with Chinese documentation. A class of 20 needs 5–10 robots; most programmes have two and a simulator.

Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.

### Where to find them

Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.

- **ROS Discourse** · https://discourse.ros.org/ — the official ROS community; education category.
- **r/ROS** · https://www.reddit.com/r/ROS/ — ROS users and teachers.
- **r/robotics** · https://www.reddit.com/r/robotics/ — robotics hobbyists, students, educators.

Beyond the named ones, the same four methods work for every idea on this site:

- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.
- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.
- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.
- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.

### The plan: 15–20 conversations, then a fake door

1. **15–20 real conversations** (ten buyers from the business side and ten from the consumer side), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.
2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price (€899–1,299, the pack's estimate), and one button. Two buttons: a refundable deposit or waitlist for consumers, "request a pilot" for businesses.
3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.
4. **Count** against the kill question. Then decide: go, change the idea, or stop.

### Interview script (fifteen minutes, problem first)

Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.

```email
Thanks for the time. I am looking into how vocational schools, applied universities, robotics bootcamps and corporate training in DE/NL/FR/Nordics deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.

1. What robot do your students run ROS on today, how long does one group take to get it working, and what breaks?
2. What do you do about it today, and what does that cost you in money or time per month?
3. What have you already tried or bought, and why did you stop using it?
4. If this went away tomorrow, what would change for you? (If the answer is "not much", you have your answer.)
5. [Only now describe it in one sentence:] A ready-built ROS navigation robot on an open RK3566 board — lidar-ready, camera-ready — sold as a classroom platform for vocational schools and applied universities teaching mobile robotics. On a scale of one to ten, how likely would you be to buy that at €899–1,299, and what would make it a ten?
6. Who else should I talk to about this? (Ask for two names.)

Close: "If I build this, can I come back to you with a prototype?" A yes with a calendar date is worth more than any compliment.
```

### Pre-order / pilot message (forum post or direct message)

```email
Subject: ROS Trainer Robot: would you pay €899–1,299 for this? Looking for 20 people to tell me I am wrong

I am [your name], [your background]. I am considering building a ROS Trainer Robot: A ready-built ROS navigation robot on an open RK3566 board — lidar-ready, camera-ready — sold as a classroom platform for vocational schools and applied universities teaching mobile robotics. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.

If you would want one at €899–1,299, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.

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

Teachers of mechatronics, automation and applied CS have the same shopping list: a robot that boots into ROS 2, drives, maps a room, navigates, sees — and that a student can break and the teacher can fix on Monday. Then: a curriculum that fits a semester, a charging dock so 10 robots are ready at 08:00, and spares from Europe in a week. TurtleBot 4 ticks the first box at a price that limits the class to two robots and a queue; the Chinese kits tick the price box and fail the documentation and spares boxes.

- **Who pays:** the school's equipment budget (often via a distributor with a framework contract), the Hochschule's lab budget, the bootcamp's capex, the company's training department.
- **Who uses:** 16–24-year-olds in groups of 2–3 per robot, 2–4 hours a week, for a semester. Robustness and resettability are the spec.
- **Who specifies:** the teacher — win them with a loaner and the curriculum.

### Market size (estimates — check)

- **TAM:** EU vocational schools with mechatronics/automation ≈ 6,000; applied universities with robotics ≈ 1,200 departments; bootcamps/corporate ≈ 500. At 6 robots per site over a 5-year cycle: ~46k robots → **€46M** per cycle; curriculum/support recurring €150/robot/year.
- **SAM:** DE/NL/FR/AT/CH/Nordics, programmes that already teach ROS or plan to ≈ 35% → **€16M**.
- **SOM (3 years):** 1,200–1,800 robots → **€1.2–1.8M**. Year 1: 300.

Sources used: TurtleBot 4 Lite ~$1,340–1,465, Standard ~$2,200 at US retailers (RobotShop, reach.dog); Clearpath's TurtleBot 4 courseware claims; a buyer review complaining about documentation. School counts: national statistics estimates — verify.

### Competition (1 search)

| Alternative | Price (est.) | Why we still win |
|---|---|---|
| Do nothing — Gazebo/Isaac simulation only | €0 | Students never touch hardware; employers notice |
| TurtleBot 4 Lite / Standard (Clearpath, iRobot Create 3 base) | €1,300 / €2,200+ | The reference; Create 3 base dependency, price limits class size; documentation complaints exist |
| TurtleBot 3 Burger/Waffle (ROBOTIS) | €700–1,600 | Ageing, small, Raspberry Pi + OpenCR; still common |
| Chinese ROS kits (Yahboom ROSMASTER, Hiwonder) | €400–1,200 | Good value, Jetson/RPi based; documentation and spares are the weak point for European classrooms |
| AgileX LIMO and other pro-education platforms | €2,500–4,000 | Excellent, out of a vocational-school budget |
| DIY: open designs + student labour | €300 + a semester | Great for one capstone team; useless for 10 identical robots |

**Wedge:** ten identical, dock-charged, English-documented ROS 2 robots for the price of four TurtleBot 4s, with a semester curriculum and EU spares — built on an open board the school can also study.

### Product & value proposition

- Base: differential drive with encoders, 300 mm chassis, 3 kg payload deck, bumper, 12 V Li-ion pack (removable), auto-dock charging contacts.
- Compute: open RK3566 SBC (Taishan Pi-class, 2–4 GB), Ubuntu + ROS 2 LTS image, WiFi/BLE via a certified module, HDMI/USB for the classroom.
- Sensors: 2D lidar (360°, 8–12 m), RGB camera (depth camera as an option), IMU, wheel odometry; swappable deck for student add-ons (ultrasonic, line sensors, a small arm).
- Classroom: fleet WiFi config, one-button factory reset, a "teacher mode" to lock parameters, dock for 5 robots, spares kit (wheels, bumpers, cables) in the box.
- Curriculum: 12 weeks — ROS 2 basics, teleop, SLAM, Nav2, perception, a final challenge; teacher slides, grading rubrics, CC-BY-SA so schools can adapt.
- **Pricing (estimates):** Base robot (lidar + RGB) €899; Pro (depth camera, bigger battery) €1,299; class set of 5 Base + dock + curriculum €4,999; spares kit €99; support/curriculum updates €150/robot/year optional.

### Unit economics (estimates, EUR per Base robot)

| Item | 1k | 5k |
|---|---|---|
| Electronics BOM (RK3566 SBC €45, 2D lidar €55, RGB camera €12, motor controller + IMU board €15, 2× encoder motors €24, 12 V Li-ion 5 Ah pack €28, WiFi module + PSU + cables €15) | 194 | 165 |
| Mechanics (aluminium chassis plates, wheels, caster, deck posts, bumper) | 38 | 28 |
| Assembly + test (full robot: drive, lidar, camera, dock) | 22 | 15 |
| Enclosure/covers (sheet metal + 2 moulded covers ~€18k tooling) | 9 | 5 |
| Packaging (robot + dock-ready box, foam) | 7 | 5 |
| Freight + duty to EU (Li-ion DG; sea for volume) | 16 | 9 |
| Certification amortised (€40k: RED, EMC, safety, UN 38.3, EN 18031) | 40 | 8 |
| **Landed cost** | **326** | **235** |
| Education net €899 ex VAT (direct), less €25 fulfilment/support | 874 | 874 |
| **Gross margin direct** | **€548 (63%)** | **€639 (73%)** |
| Distributor net €680 ex VAT | €354 (52%) | €445 (65%) |

At 300 units the certification amortisation is €133/robot; still fine at a €899 price. The lidar and the SBC are the lead-time items.

### Go-to-market

**First 100 customers (robots, i.e. ~20 schools):** three schools buying a 5-robot class set at €999/robot for the coming semester (the kill question). Reach teachers via the national mechatronics teacher associations, the ROS 2 education mailing lists and Discord, applied-university robotics labs you can visit, and the regional VET innovation centres. Offer: a loaner robot for 4 weeks + the curriculum PDF; buy a class set and the loaner is free.

**Scale:** education distributors with school framework contracts (DE/NL/FR), university procurement portals, ROS community visibility (publish the ROS 2 packages and the curriculum openly), robotics competitions (sponsor a vocational-school league with your robot as the standard platform), corporate training providers.

### 12-month plan

- **Q1:** kill question (3 class sets ordered), works-like robot from the open trolley design + Taishan Pi + lidar, ROS 2 image, curriculum weeks 1–4 written and tested with one class.
- **Q2:** own chassis and motor-controller board, dock, 15 EVT robots (3 class sets) in schools for a term; pre-compliance; spares list.
- **Q3:** DVT, certification (RED, EMC, safety, UN 38.3, EN 18031), pilot batch 50, first distributor, curriculum complete.
- **Q4:** production 150–250, Pro SKU, competition league pilot, FR/Nordic distributors.

**Team:** founder (education sales, robotics credibility), 1 robotics engineer (ROS 2, Nav2, Linux images), 1 mechanical/electrical engineer (chassis, motor control, dock, battery), a teacher as paid curriculum co-author, a fulfilment partner holding spares in the EU.

**Funding to the first 300 robots (estimate):** NRE €45k (chassis + covers tooling €18k, motor-controller PCB €8k, dock €6k, image/curriculum €13k) + certification €40k + 9 months salaries €85k + 300 robots at ~€360 landed (small-batch cost) €108k = **€278k**, less revenue from 150 robots sold in-year (~€135k) → **€140k** net. Route: 3 class-set pre-orders (deposits €15k), an EdTech/VET innovation grant (Erasmus+ partnerships, national digital-education funds), and an angel or regional fund ticket. For reference: 1,000 robots would need ~€330k of inventory alone — don't.

### Top risks

- **Market — procurement cycles.** Schools buy once a year, often via tender above thresholds. Mitigation: class-set price below the threshold where possible, distributor frameworks, loaner programme timed to budget season (spring for the autumn semester).
- **Technical — Linux image rot.** ROS 2 and kernel updates break classes. Mitigation: pin an LTS, ship a factory-reset image on the eMMC, release once a year in summer.
- **Technical — lidar and SBC lead times and EOL.** Mitigation: qualify two lidars with the same mount; the open SBC is a plus (you can have it made) but the RK3566 supply is Rockchip's call — buy for a year.
- **Regulatory — Li-ion:** UN 38.3, Battery Regulation (removable pack is right), DG shipping. **Machinery Regulation** — a desktop education robot is generally outside, but a 3 kg robot driving in a classroom deserves an honest risk assessment (bumper, speed limit 0.5 m/s, e-stop). Check with the test lab.
- **Support — schools call.** Mitigation: spares kit in every class set, a teacher forum, 48-hour spares shipping from the EU; budget 0.3 FTE support per 300 robots.
- **Competition — Clearpath lowers price or Chinese kits add English docs.** Mitigation: curriculum + community + spares, not hardware alone.

## 4. Start kit

### Boards to start from

| Board | Link | What it contributes | Files (catalogue) | Licence note |
|---|---|---|---|---|
| 泰山派ROS小车 (OSHWHub) | https://www.gongbans.com/db/oshwhub-taishan-pie-ros-trolley.html | Open ROS navigation robot built on the Taishan Pi — low-cost, for robot programming and algorithm study; your works-like base | schematic, pcb | OSHWHub project licence — check before commercial derivation |
| 立创·泰山派开发板 (OSHWHub) | https://www.gongbans.com/db/oshwhub-li-chuang-tai-shan-pai-kai-fa-ban.html | Open RK3566 SBC (Taishan Pi) — the compute, with schematics you can teach from | schematic, pcb | OSHWHub project licence — check |
| M5Stack RoverC-Pro (K036-B) | https://www.gongbans.com/db/m5stack-roverc-pro.html | Small omni-wheel base for an entry/desk kit (pre-ROS, micro-ROS experiments) | enclosure/structure files only; electronics not published | Off-the-shelf |
| Sparkbot_45coll版本 (OSHWHub) | https://www.gongbans.com/db/oshwhub-sparkbot-45coll.html | Line-following and wireless-charging references (derived from an open Espressif design) | schematic, pcb | OSHWHub project licence — check |

### Block diagram

```
[2D lidar] --USB/UART--> |
[RGB/depth camera] -USB-> | [RK3566 SBC: Ubuntu + ROS 2, WiFi module] --UART/USB--> [motor-controller MCU: 2x encoder motors, IMU, bumper, battery gauge]
[HDMI/USB classroom I/O]  |      |-- WiFi --> classroom network / teacher laptop
[12 V Li-ion removable pack] --> [power board: 5 V/3 A SBC, 12 V motors, dock contacts, e-stop]
Swappable sensor deck (I2C/UART/GPIO header) on top.
```

**Engineering gap:** a robust motor-controller/power board (the open trolley's electronics are a starting point, not a classroom product), auto-dock charging, a battery pack with gauge and protection, mechanical robustness (students), the fleet-ready Linux image with factory reset, and the curriculum.

### Starter BOM (estimates)

| Part | Est. unit cost | Notes |
|---|---|---|
| RK3566 SBC (Taishan Pi-class, 2–4 GB, eMMC) | €45 | Open design; RK3566 supply via Rockchip distributors; 8–12 wk |
| 2D 360° lidar (8–12 m, UART) | €55 | 2–3 vendors; qualify two with the same mount |
| RGB camera (USB UVC) / depth camera option | €12 / €80 | Multi-source |
| Encoder DC gearmotors ×2 | €24 | Multi-source |
| Motor-controller MCU board (ESP32-S3 or STM32, IMU, drivers) | €15 | Your design |
| 12 V 5 Ah Li-ion pack with BMS, removable | €28 | Certified pack vendor; UN 38.3 report |
| WiFi/BLE module, certified | €5 | |
| Chassis plates, wheels, caster, posts, bumper | €28 at 5k | CNC/laser at 1k |
| Dock (contacts, 12 V charger) | €25 per robot share | Class-set item |

### Firmware/software starting point

- ROS 2 (current LTS) with Nav2 and slam_toolbox — the standard navigation stack; ros2_control for the base.
- micro-ROS for the motor-controller MCU (ESP32/STM32 supported).
- Rockchip Linux/Ubuntu images for the RK3566 — search the Taishan Pi community resources and the open trolley's repository for the existing ROS image before building your own.
- TurtleBot 4 and TurtleBot 3 open-source packages and courseware as structural references for the curriculum (licences vary — check).
- Gazebo (new Gazebo, formerly Ignition) model of your robot for the simulation weeks.

### 12-week build plan

| Weeks | Gate | Exit criteria |
|---|---|---|
| 1–2 | Validate | 3 schools order a 5-robot class set at €999/robot for the coming semester (deposits). Fewer than 2: stop or pivot to a bootcamp/corporate buyer. Meanwhile: the open trolley + Taishan Pi + a lidar maps your office with slam_toolbox. |
| 3–5 | Works-like | Nav2 navigation between two waypoints in a classroom-sized room, camera stream in RViz, 2-hour battery, factory-reset image; curriculum weeks 1–4 taught to one class. |
| 6–8 | Looks-like + EVT | Own motor/power board, chassis v1, dock v1, 15 robots in 3 schools for 6 weeks; failures logged; pre-compliance EMC with motors. |
| 9–10 | DVT + pre-compliance | Board v2, chassis v2, RED/EMC/safety pre-tests, UN 38.3 report from the pack vendor, risk assessment (speed limit, bumper, e-stop), EN 18031 checklist. |
| 11–12 | Pilot batch | 50 robots + 10 docks from a CM, golden sample, spares kits, curriculum v1 complete, teacher forum live. |

### Certification checklist (EU)

- **CE / RED:** WiFi/BLE → EN 300 328, EN 301 489-1/-17, EN 62311; safety EN 62368-1 (battery, charger, dock contacts); EMC with motors is the hard test.
- **RED delegated act — EN 18031-1:** applies (WiFi). Classroom networks: no default passwords, per-robot credentials, signed images.
- **CRA:** reporting since September 2026, full December 2027; an SBC running Ubuntu needs an update story — yearly image releases, security patches policy.
- **Battery Regulation (2023/1542) + UN 38.3:** removable pack, labelling, producer registration, DG shipping (Class 9).
- **Machinery Regulation 2023/1230:** likely not applicable to a desktop/classroom education robot, but document the risk assessment (moving robot, pinch points, speed limit, e-stop) — ask the lab.
- **Toy Safety Directive:** not applicable (not for children under 14; state the age in the manual).
- **RoHS, REACH, WEEE**, packaging registration.
- **GDPR:** camera on a robot in a classroom — no recording by default, a visible LED when streaming, a note for schools.
- **Estimated test costs:** RED €10k, EMC with motors €7k, safety €6k, UN 38.3 (pack vendor's report, verify) €0–4k, EN 18031 €12–15k, documentation €2k. Budget **€40k**.

### Validation toolkit

- **Kill question:** do 3 schools buy a 5-robot class set at €999 each for the coming semester? **Cheapest experiment:** one works-like robot (open trolley + Taishan Pi + lidar ≈ €350), a 4-week loaner tour of 6 schools, the curriculum outline as a PDF, and a class-set quote. Cost ≈ €600 and six visits.
- **5-question interview (teacher):** 1) What do you teach mobile robotics on today and how many students share one robot? 2) What broke last semester and how long was the robot out? 3) Which ROS 2 topics must the course cover for your employers' needs? 4) Who approves a €5,000 class-set purchase and when is the budget window? 5) If spares arrived in 48 hours and the curriculum came with slides and rubrics, what would still stop you?
- **Landing page:** headline "Ten ROS 2 robots for the price of four. Built for classrooms, documented in English." Bullets: "Boots into ROS 2 with SLAM and Nav2 running — lidar and camera included"; "Dock-charged, student-proof, spares shipped from Europe in 48 h"; "12-week curriculum with slides, labs and rubrics — €899 per robot".
- **Pass threshold:** 3 class sets (15 robots) ordered with deposits before you tool anything; 60 robots committed by the end of the first semester.

### First production checklist

- Samples: 1 works-like, 15 EVT, 50 pilot; keep 2 per revision.
- Golden sample: drive straightness, lidar map quality, dock success rate (20/20), battery runtime, image hash — signed.
- DFM review: chassis stacking tolerances, motor mounts, cable routing for student access, dock contact alignment, battery latch robustness.
- MOQ talk: SBC 300 (then 1k), lidar 300, motors 500, packs 300 (certified vendor), tooling at 1k shots for covers.
- QC/AQL: level II, AQL 1.0/2.5; 100% drive + lidar + camera + dock test; 100% image verification.
- Packaging: DG-compliant carton for the pack (or ship packs separately), foam cradle, spares kit, quick-start.
- Incoterms: FOB Shenzhen with a DG forwarder; consider assembling in the EU for the first 50 to learn the product.

## 5. Who to contact

<!-- who-to-contact:start -->
**On file: 1 board publisher (M5Stack).** Only useful once section 2 (validate demand) has passed. Everything below comes from gongban.db, the directory behind this site. It names the companies that publish the boards this idea is built from, the manufacturers on file, and directory entries in the same product category. None of it is a verified supplier relationship for this specific idea: nobody has quoted it yet. Company websites only; no personal contacts are published.

### Board publishers (direct)

- **M5Stack** — community / maker brand; 274 boards in the catalogue; files via M5Stack M5_Hardware repo · https://github.com/m5stack/M5_Hardware. Boards used here: [M5Stack RoverC-Pro (K036-B)](/db/m5stack-roverc-pro.html) (small omni-wheel base for the entry kit). What to ask for: sample units of the SKUs above, unit pricing at 100 / 500 / 1,000, whether a customised variant is possible (and its NRE and MOQ), and the module's radio test reports if any.

### Open-hardware boards without a company behind them

- **OSHWHub community designs** — community projects on OSHWHub 立创开源硬件平台 (JLC open hardware platform) · https://oshwhub.com . The author is an individual, not a supplier, and author handles are not published here. Fabricate from the files through a PCBA house (below) and check each project's licence first. Boards used here: [泰山派ROS小车](/db/oshwhub-taishan-pie-ros-trolley.html) (open ROS navigation robot built on the Taishan Pi); [立创·泰山派开发板](/db/oshwhub-li-chuang-tai-shan-pai-kai-fa-ban.html) (open RK3566 SBC (Taishan Pi)); [Sparkbot_45coll版本--无线充电、红外巡线](/db/oshwhub-sparkbot-45coll.html) (line-following and wireless-charging references).

### Manufacturing (PCBA / EMS) on file

- **Kingbrother / King Brother Technology** · https://global.kingbrother.com/ — PCB fab + EMS; see the [Kingbrother SOM page](/boards-kingbrother.html) on this site.
- **Foxlink (SZ)** (正崴精密工业(深圳)有限公司) · foxconn.com — PCBA + cable assembly EMS: Cable assembly; PCBA; connector; OEM for major electronics brands.

### Also in the directory (category match, not idea-specific)

Companies in the gongban.db solution-house directory whose product category overlaps this idea. They were matched on the idea's tags, not on this design; none has seen it.

- **Forlinx Embedded** (飞凌嵌入式技术有限公司) · forlinx.com — ARM core board / SOM OEM: i.MX8M / RK3568 / AM62x SOM; carrier board; Linux BSP; OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **Toradex (SZ)** (深圳图睿达科技有限公司) · toradex.com — Industrial SOM / embedded Linux OEM: Apalis / Colibri SOM; carrier board; Yocto Linux; long-term supply. *(Edge-AI / SOM boards and Linux BSPs)*
- **iWave Systems (SZ)** (爱微电子(深圳)有限公司) · no website on file — ARM SOM / carrier board ODM: RK3568/i.MX8 SOM; carrier board; embedded Linux OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*
- **Kangshida (Conradtech)** (深圳市康士达科技有限公司) · cstipc.com — Industrial PC / AI edge computing OEM: Industrial PC board; AI edge card; computer vision; OEM/ODM. *(Edge-AI / SOM boards and Linux BSPs)*

### MOQ and landed cost

gongban.db holds no MOQ, unit-price or tariff data for these companies, so none is shown. Get the numbers from the quote (the e-mail below asks for them) and run them through the [landed-cost worksheet in the playbook](/playbook.html#landed-cost). The starter BOM in the start kit section is an estimate, not a quote.

### Outreach e-mail, ready to send

Fill in the [brackets], keep it short, and send it to the sales or "contact us" address on the company's own website. The Chinese version is the same letter; sending both in one mail is normal. How to read the reply: [playbook → the first quote](/playbook.html#quote).

**A. To a board publisher — samples and volume price** (send to the sales / "contact us" address on the M5Stack website)

```email
Subject: Sample order and volume pricing — M5Stack RoverC-Pro (K036-B) — for a ROS Trainer Robot

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are developing a ROS Trainer Robot: A ready-built ROS navigation robot on an open RK3566 board — lidar-ready, camera-ready — sold as a classroom platform for vocational schools and applied universities teaching mobile robotics. The design is built around your M5Stack RoverC-Pro (K036-B).

Could you please send:
1. Price and lead time for [10] sample units of each: M5Stack RoverC-Pro (K036-B).
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
主题：样品订购及批量报价 — M5Stack RoverC-Pro (K036-B) — 用于ROS Trainer Robot

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款ROS Trainer Robot：A ready-built ROS navigation robot on an open RK3566 board — lidar-ready, camera-ready — sold as a classroom platform for vocational schools and applied universities teaching mobile robotics。产品设计基于贵司的M5Stack RoverC-Pro (K036-B)。

请提供以下信息：
1. 各[10]片样品的单价和交期：M5Stack RoverC-Pro (K036-B)。
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
Subject: PCBA quote from open design files — ROS Trainer Robot, [50] prototypes + [500] production units

Hello [company] sales team,

I am [your name], founder of [your company] in [country]. We are building a ROS Trainer Robot: A ready-built ROS navigation robot on an open RK3566 board — lidar-ready, camera-ready — sold as a classroom platform for vocational schools and applied universities teaching mobile robotics. The design starts from published open-hardware files (泰山派ROS小车, 立创·泰山派开发板, Sparkbot_45coll版本--无线充电、红外巡线; schematic, PCB and BOM available) with our own modifications.

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
主题：基于开源设计文件的PCBA报价 — ROS Trainer Robot，[50]台样机 + [500]台量产

[公司]销售团队，您好：

我是[姓名]，[国家][公司]的创始人。我们正在开发一款ROS Trainer Robot：A ready-built ROS navigation robot on an open RK3566 board — lidar-ready, camera-ready — sold as a classroom platform for vocational schools and applied universities teaching mobile robotics。设计基于已公开的开源硬件文件（泰山派ROS小车, 立创·泰山派开发板, Sparkbot_45coll版本--无线充电、红外巡线；含原理图、PCB和BOM），并做了我们自己的修改。

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

1. Order the Taishan Pi board and the parts list from the open ROS trolley project plus a 2D lidar; get slam_toolbox mapping a room on it.
2. Write the 12-week curriculum outline (one page) and the class-set quote; email 10 mechatronics teachers and offer a 4-week loaner.
3. Ask a test lab for a 30-minute pre-assessment on Machinery Regulation applicability and the EMC plan for a motorised WiFi robot.

Want help sourcing or building this? Talk to us via www.gongbans.com.
