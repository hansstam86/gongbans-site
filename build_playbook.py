#!/usr/bin/env python3
"""
build_playbook.py — /playbook.html, the zero-experience founder playbook shared by all 50 ideas.

Written as Markdown in PLAYBOOK below and rendered with the start-pack renderer so it looks like the
packs. Covers what every start pack has in common: the kill question, ordering samples, the first
quote, choosing a manufacturer, EU certification (CE) and FCC, import/customs, logistics and
fulfilment, a landed-cost worksheet, the outreach e-mails and a glossary.

Rule of the site applies: no invented prices or claims. Where a number is unavoidable it is a
public rule (a VAT rate, a directive number) or explicitly an estimate to check.

Run from the repo root:  python3 build_playbook.py       (build_ideas.py calls build())
"""

import re
from pathlib import Path

from build_detail_pages import FOOTER, e, head, nav
from build_startpacks import md_to_html

ROOT = Path(__file__).parent
OUT = ROOT / "playbook.html"
UPDATED = "November 2026"

PLAYBOOK = r"""
## 0. Read this first

You have shipped software. You have never had a product made. This page is the part of every start pack that is the same for all fifty ideas: the order of operations, the words people will use, the documents you will need, and the mistakes that cost software founders their first production run. Read it once end to end, then come back to the section you are in.

Three rules carry through everything below:

- **A gongban is a starting point, not a product.** The catalogue boards give you working electronics with published files. Your product is the board plus an enclosure, a power path, firmware, a box and a stack of certificates. Each of those is a project.
- **Every number on this site is an estimate** until a supplier writes it in a quote. BOM costs, MOQs, lead times and certification fees in the packs are there so you can plan; the quote replaces them.
- **Check the licence before anything commercial.** Boards tagged `check-licence` come from community projects; some licences forbid commercial use or require you to publish your changes. Read the licence on the board's page, and ask when it is unclear.

Where the people are: every start pack has a **Who to contact** section (section 4) that names the companies on file in gongban.db for that idea. This page tells you what to do with them.

## 1. Week zero: the kill question

Every idea on this site carries a *kill question*: one measurable test that, if it fails, tells you to stop before you spend money on hardware. It is the hardware equivalent of a landing-page test, and it comes first because hardware mistakes are slow and expensive to undo.

How to run one in a week:

1. **Build the fake product.** A landing page with a rendered image or a cardboard mock-up photographed well, the price from the pack, and a button that takes a refundable deposit or a signed letter of intent. No code, no boards.
2. **Put it in front of the exact customer named in the pack.** The forum, the trade association, the ten facility managers, the WhatsApp group of installers. Not your friends.
3. **Count.** The pack states the pass mark (a conversion rate, a number of deposits, a number of yes-answers). Hit it or don't.
4. **Talk to ten who said no.** Their reasons are your spec changes or your reason to pick another idea.

If it passes, keep the deposits list: those people are your first beta units and your first reviews. If it fails, you have lost a week and learned what a hardware company would have taken a year to learn.

## 2. Order the sample boards

The start kit (section 3 of each pack) lists catalogue boards to copy from. Before you design anything, buy them and make the product work on your desk with the real modules, even if it is held together with tape.

- **Where.** The board's page in the [catalogue](/boards.html) links to the publisher's own files. The publisher (M5Stack, Seeed Studio, Espressif and the others named in section 4 of the pack) sells the physical boards through its own shop and through the usual distributors. Three of each board is a good number: one to use, one to break, one to compare against.
- **Open-hardware boards** (OSHWHub projects) have no shop behind them. You order the bare PCB and parts from a prototype fab using the published Gerber and BOM files, or you pick the nearest commercial module that does the same job. The pack usually names one.
- **Chinese marketplaces.** Many gongban kits exist as finished boards on 1688 and Taobao, the physical kit market the catalogue records as a source. Buying there needs a Chinese address and payment method or a purchasing agent; for a first prototype the publisher's international shop is faster and the parts are traceable.
- **What arrives.** Boards, sometimes a cable, rarely documentation. The documentation is on the board's page. Expect one to three weeks including customs for a small parcel into the EU. <span class="est">estimate</span>
- **Import of samples.** Low-value parcels still carry import VAT in the EU; the courier collects it on delivery with a handling fee. Keep every invoice: these are development costs and you will need the HS codes later.

Milestone: the product does its one job on your desk with the sample boards. Software founders call this the proof of concept. Hardware people call it the *looks-like / works-like* prototype, usually two separate objects at this stage.

## 3. From prototype to production, in hardware words

The vocabulary matters because your suppliers will use it, and it maps badly onto software releases.

| Stage | What it is | Software analogy | Typical quantity |
|---|---|---|---|
| **POC / breadboard** | Sample boards wired together, your firmware, no enclosure | Spike / prototype branch | 1–3 |
| **EVT** (engineering validation) | Your own PCB for the first time, hand-built or small-batch assembled, tested against the spec | Alpha | 5–20 |
| **DVT** (design validation) | Near-final design in the real enclosure; this is the build you send to the test lab for certification | Beta | 20–100 |
| **PVT** (production validation) | Built on the factory's production line with the production tooling and test fixtures; proves the line, not the design | Release candidate | 100–500 |
| **MP** (mass production) | The real run | GA release | the order |

Quantities are the usual ranges, not rules. <span class="est">estimate</span> Each stage ends with a review; a design change after DVT means re-testing, and a change after PVT means re-tooling. "Just one more fix" is how a hardware company misses Christmas.

Two more words you will hear in the first week:

- **DFM** (design for manufacturing): the factory's review of your files for things that are hard or expensive to build. Ask for it before you pay for anything; good houses do it free or for a small fee.
- **NRE** (non-recurring engineering): one-off costs such as tooling for the enclosure, SMT stencils, test fixtures and programming jigs. A quote without NRE is incomplete.

## 4. Find the manufacturer

There are three kinds of company behind every idea on this site, and the first e-mail to each is different. Section 4 of the pack tells you which exist on file for your idea.

**The board publisher** (M5Stack, Seeed Studio, Espressif, SIMCom, WPI's application unit). They designed the board and sell it. What they are good for: sample units, volume pricing of the module as-is, sometimes a customised variant (your connector, your enclosure, firmware pre-loaded). What to send them: template A from the pack. What they are not: your contract manufacturer for the whole product.

**The solution house / ODM** (the directory entries). Shenzhen companies that already make products in your category from their own reference designs. What they are good for: taking your spec and delivering a finished, certified product, often faster and cheaper than you designing it, in exchange for less control and a design you do not own. What to send them: a spec sheet and target quantities; ask what they already have that is close. The directory entries in the packs are **category matches**, companies on file in gongban.db that make this kind of thing; none of them has seen the idea.

**The PCBA / EMS house** (Kingbrother and Foxlink are on file; there are thousands). They build *your* design from *your* files: PCB fabrication, component sourcing, SMT assembly, test, often box build. What they are good for: everything from EVT onwards once you have your own design. What to send them: template B from the pack, with the files.

How to vet any of them before money moves, in order of cost:

1. **Website and company registration.** The Chinese company name (公司名) on the pack page is what you search in the national registry; a trading company and a factory can have the same English name.
2. **A video call, camera on, from the factory floor.** Ask to see the SMT line and the test stations. A solution house or trading company will show you an office; that is fine as long as you know which one you are talking to.
3. **A paid sample run first.** Ten to fifty units of your design, paid in full, before any production order. You learn their communication, their quality and their invoice all at once. <span class="est">estimate</span>
4. **Payment terms.** Thirty percent deposit, seventy percent before shipment is the common first-order structure; pay the balance only after you or a third-party inspector has seen the finished goods. <span class="est">estimate</span>
5. **Third-party inspection** for the first production run: an inspector visits the factory before shipment and reports against your checklist. This costs a few hundred euros per visit and is the cheapest insurance in hardware. <span class="est">estimate</span>
6. **Ask who else they build for** and whether you can call one customer. A good house will say yes.

Red flags, from twenty years of this: a quote that comes back within an hour with no questions; a unit price far below the others with no explanation; refusing a video call; asking for the full amount up front; "no problem" to every technical question; a different company name on the invoice than on the website.

## 5. The first quote, and how to read it {#quote}

Your e-mail (templates in section 4 of the pack) asks for samples, volume pricing, NRE, lead time, certification documents and terms. A real quote answers all six. Read it like this:

- **Unit price at each quantity break.** Note the currency and whether it includes components, packaging and testing. A PCBA quote often excludes a few "customer-supplied" parts: ask.
- **MOQ** (minimum order quantity). This is negotiable for a first order, especially if you pay a higher unit price. The MOQ of the *components* matters as much as the factory's: one chip only sold on a reel of 3,000 sets your real minimum.
- **NRE and tooling**, itemised. Stencil, fixtures, programming jig; enclosure tooling if they do box build (an injection mould for a simple plastic enclosure runs into the thousands of euros and takes weeks; a 3D-printed or sheet-metal enclosure has almost none). <span class="est">estimate</span>
- **Lead time** from "files approved and deposit received" to "ready to ship", and the component lead time separately. Long-lead parts (some radio modules, displays, connectors) decide your schedule more than the assembly does.
- **Incoterm.** EXW (you collect at their door), FOB Shenzhen (they deliver to the ship or plane; you pay the rest), DDP your city (they deliver duty paid to you). For a first order DDP by courier is the simplest and worth its premium; see section 7.
- **Validity.** Quotes expire, usually in 30 days, because component prices move. <span class="est">estimate</span>

Get three quotes. The spread between them teaches you what is expensive in your design.

## 6. Certification: CE for Europe, FCC for the US

The single most important thing a software founder gets wrong: **CE is not a test you pass; it is a declaration you sign.** You, the person putting the product on the EU market, declare that it meets every applicable directive and you hold a *technical file* that proves it. Test labs produce reports that go into the file; a *notified body* is only required for some radio cases. The CE mark itself you print on the label.

Which directives apply to the ideas on this site (the pack's certification line names the ones for each idea):

| Directive / regulation | Applies when | What goes in the technical file |
|---|---|---|
| **RED** 2014/53/EU (radio) | Anything with WiFi, Bluetooth, LoRa, cellular, Thread, NFC | Radio test report (EN 300 220, EN 300 328, EN 301 908 …), EMC (EN 301 489), safety, and since 2025 the **EN 18031** cybersecurity series for internet-connected devices |
| **EMC** 2014/30/EU | Everything electronic without radio (RED covers EMC when there is radio) | Emissions and immunity reports (EN 55032 / EN 55035 or the product standard) |
| **LVD** 2014/35/EU | Mains-powered equipment (50–1000 V AC) | Safety report, typically **EN 62368-1**; a USB-powered device with a certified external PSU largely sidesteps this |
| **RoHS** 2011/65/EU | Everything | Supplier declarations for every part; the factory provides most of them |
| **REACH** | Everything | Substance declarations; same route as RoHS |
| **WEEE** 2012/19/EU | Everything | Not a test: you register as a producer in each country you sell in (Germany: stiftung ear), pay a scheme, and put the crossed-out bin on the label |
| **Battery Regulation** 2023/1542 | Anything with a battery | Battery documentation, labelling, removability rules, UN 38.3 transport test for lithium cells |
| **CRA** (Cyber Resilience Act) 2024/2847 | Anything with a digital connection; reporting duties from 2026, full application 2027 | Vulnerability handling process, security updates for the support period, documentation |
| **GPSR** 2023/988 | Consumer products | A responsible person in the EU on the label, a risk assessment, traceability |

Three ways to make this cheaper, all used in the packs:

- **Use a pre-certified radio module.** A WiFi or LoRa module that already carries RED test reports (ask the publisher; the e-mail template does) lets the lab test your product as a host, not as a new radio. This is why the packs favour modules over bare chips.
- **Power from USB or a certified external supply.** No mains inside the enclosure means no LVD testing of your own board.
- **No battery, no microphone, no camera** unless the idea needs them. Each one adds a regulation.

What a test lab costs depends on the radio count and the product; a connected product with a pre-certified module and USB power is at the low end, a battery-powered multi-radio device at the high end. Get a quote from two accredited labs (there are many in Shenzhen and in every EU country) with your DVT units; budget it in the plan as the pack does, and treat the pack's figure as an estimate. <span class="est">estimate</span> Test with the DVT build, in the real enclosure, with the production firmware. A failed EMC test is usually fixed with a few components and a re-spin, so leave time for one.

**United States: FCC.** Intentional radiators (anything that transmits) need FCC authorisation: a *certification* through a Telecommunication Certification Body and an FCC ID on the label, or, if you use a module with its own *modular approval*, mostly the module's FCC ID plus your host testing. Unintentional radiators (digital devices without radio) need a Supplier's Declaration of Conformity under Part 15. Different reports, same labs. Add **UKCA** for Great Britain if you sell there; it mirrors CE with its own marking.

Documents you will need to produce for all of this, so start them at EVT: a product spec, block diagram and schematics, the BOM with manufacturer part numbers, the risk assessment, the user manual with the safety and disposal text, the label artwork, and the Declaration of Conformity. The factory will not write these for you.

## 7. Import and customs {#customs}

Your goods are in Shenzhen; your customers are in Europe. Between them is a set of paperwork that is boring and entirely predictable once you have done it once.

- **EORI number.** Your business's EU customs identifier; apply once with your national customs authority, free, takes days. You cannot import commercially without it.
- **HS / TARIC code.** Every product has a tariff classification. Most of the ideas on this site fall in chapter 85 (electrical machinery) or chapter 90 (measuring instruments); the exact ten-digit TARIC code decides the duty rate and is yours to declare correctly. Look it up in the EU TARIC database, then confirm it with your customs broker; your supplier's suggestion is a starting point, not an answer.
- **Duty.** Under the Information Technology Agreement most computing and telecoms electronics enter the EU at 0% duty, but sensors, instruments, lamps, toys and kits can carry a few percent. The TARIC code tells you. <span class="est">estimate: check your code</span>
- **Import VAT.** Charged on the customs value plus duty plus freight, at your country's standard rate (Germany 19%, Netherlands 21%, as of writing; check yours). If you are VAT-registered you reclaim it in your return, so it is a cash-flow cost, not a real one.
- **Who clears it.** A customs broker or the courier's brokerage does the declaration from your commercial invoice and packing list; for a first order the courier's DDP service bundles all of this. For sea freight you appoint a forwarder who handles it.
- **Paperwork from the factory:** commercial invoice (with HS codes, Incoterm, your EORI), packing list, and for lithium batteries the UN 38.3 test summary and the dangerous-goods declaration.
- **Product compliance at the border.** Customs can and does check for the CE mark, the EU responsible-person address (GPSR) and WEEE registration. Ship compliant goods or do not ship.
- **Selling to consumers across the EU:** the **IOSS** scheme lets you charge destination-country VAT at checkout for low-value consignments shipped from outside the EU; if you stock in the EU (section 8) ordinary VAT rules apply.

## 8. Logistics and fulfilment {#logistics}

- **Samples and small batches: courier (DHL / FedEx / UPS).** Three to seven days, door to door, DDP available. Priced by weight and volume; fine up to a few cartons. <span class="est">estimate</span>
- **Air freight.** A pallet or more, airport to airport plus handling; one to two weeks with clearance. Faster than sea, cheaper than courier per kilo above a certain size.
- **Sea freight.** LCL (you share a container) or FCL (your own). Thirty to forty-five days Shenzhen to Rotterdam or Hamburg plus clearance, and the cheapest per unit by far. Plan it: a product that ships by sea needs a six-week buffer in the launch plan. <span class="est">estimate</span>
- **Lithium batteries** travel under dangerous-goods rules: fewer carriers, more paperwork, sometimes sea only. Design decision, not a shipping decision.
- **Packaging** is part of the product and part of the freight cost. Ask the factory for the master-carton dimensions and weight in the quote; a box that fits 24 units instead of 20 pays for itself.
- **Where the stock lives.** Options, in order of effort: your garage; a 3PL (third-party logistics warehouse) in the EU that stores, picks and ships from your web shop orders; Amazon FBA; a distributor who buys the pallet. B2B ideas on this site usually ship from a 3PL or directly from the factory to the customer; consumer ideas usually need the 3PL or FBA.
- **Returns and spares.** Reserve a few percent of the first run for replacements and reviewers, and decide before launch who opens the returned units. <span class="est">estimate</span>

## 9. The landed-cost worksheet {#landed-cost}

The pack's unit economics use an estimated BOM. Replace it with this once you have a quote. "Landed cost" is what one unit costs sitting on your shelf in Europe, before you spend anything on selling it.

```
  Factory unit price (PCBA + box build, at your quantity)        ______
+ NRE and tooling ÷ units in this run                            ______
+ Freight ÷ units (courier / air / sea, incl. insurance)         ______
+ Duty  = (unit price + freight share) × duty rate for your code ______
+ Customs brokerage and handling ÷ units                         ______
+ Certification and lab fees ÷ units over the first year         ______
+ Compliance fees ÷ units (WEEE scheme, battery scheme, GPSR rep) ______
+ Yield loss: units built that fail test or arrive damaged, %    ______
= LANDED COST PER UNIT                                           ______

  Import VAT is paid on (unit price + freight + duty) and reclaimed if you are
  VAT-registered: track it as cash flow, not as cost.
```

Rules of thumb that hold for the ideas here, every one of them an estimate until your quote says otherwise: landed cost lands well above the bare BOM once NRE, freight and certification are spread over a first run of a few hundred units; retail price is a multiple of landed cost, not of BOM; and the first run is never the cheap one. The packs' unit-economics tables assume exactly this, which is why their first-year margins look thin.

## 10. The outreach e-mails {#emails}

Every start pack carries two e-mails in section 4, pre-filled with that idea's boards and pitch, each in English and Chinese:

- **A. To a board publisher**: samples, volume pricing, customisation, radio test reports, payment terms.
- **B. To a PCBA / EMS house**: fabrication and assembly quote from the open files, NRE, lead time, QC, box build, Incoterms.

How to use them: fill the brackets, attach nothing on the first mail except a link to your files if you have them, send to the sales or "contact us" address on the company's own website, and send both language versions in the same message. Expect replies in one to three working days, often on WeChat or WhatsApp after the first exchange; keep the commercial terms in e-mail. A reply that answers all the numbered points is a company worth a video call.

## 11. Glossary

<dl class="glossary">
<dt>Gongban (公板)</dt><dd>A reference design, usually from a chip house or solution house, that many products are built on with little change. The catalogue on this site lists them.</dd>
<dt>BOM</dt><dd>Bill of materials: every part on the board with its manufacturer part number and quantity. The PCBA house quotes from it.</dd>
<dt>PCBA / SMT</dt><dd>Printed-circuit-board assembly; surface-mount technology, the machine process that places the components.</dd>
<dt>Gerber / pick-and-place</dt><dd>The file formats a fab needs: the copper layers and drill (Gerber), and where each part goes (pick-and-place / centroid file).</dd>
<dt>MOQ</dt><dd>Minimum order quantity, of the finished unit and of each component.</dd>
<dt>NRE</dt><dd>Non-recurring engineering: one-off costs such as tooling, stencils, fixtures.</dd>
<dt>DFM</dt><dd>Design-for-manufacturing review by the factory.</dd>
<dt>EVT / DVT / PVT / MP</dt><dd>Engineering, design and production validation builds, then mass production. See section 3.</dd>
<dt>ODM / OEM</dt><dd>ODM: they design and build, you brand it. OEM: they build your design. Shenzhen uses both words loosely; ask what is meant.</dd>
<dt>Incoterms (EXW, FOB, DDP)</dt><dd>Who pays and who is responsible for the goods at each step of the journey. See section 5.</dd>
<dt>HS / TARIC code</dt><dd>The customs classification that sets duty. See section 7.</dd>
<dt>EORI</dt><dd>Your EU customs identifier.</dd>
<dt>CE / DoC / technical file</dt><dd>The EU conformity mark, the Declaration of Conformity you sign, and the evidence folder behind it. See section 6.</dd>
<dt>RED / EMC / LVD / RoHS / WEEE / CRA</dt><dd>The EU directives and regulations most likely to apply. See section 6.</dd>
<dt>FCC ID / modular approval</dt><dd>US radio authorisation; a module with modular approval carries its own FCC ID.</dd>
<dt>UN 38.3</dt><dd>The transport safety test every lithium battery needs before it may fly or sail.</dd>
<dt>3PL</dt><dd>Third-party logistics warehouse that stores and ships your stock.</dd>
<dt>Kill question</dt><dd>The one measurable test in each idea that tells you to stop. See section 1.</dd>
</dl>
"""

SECTION_LABELS = {"0": "Read this first", "1": "Week zero · kill question", "2": "Samples", "3": "Prototype → production",
                  "4": "The manufacturer", "5": "The first quote", "6": "Certification · CE / FCC", "7": "Import & customs",
                  "8": "Logistics & fulfilment", "9": "Landed-cost worksheet", "10": "Outreach e-mails", "11": "Glossary"}
ANCHORS = {"5": "quote", "7": "customs", "8": "logistics", "9": "landed-cost", "10": "emails", "4": "manufacturer"}


def render():
    md = PLAYBOOK
    # inline raw HTML blocks (the glossary <dl>) must pass through untouched: pull them out, render, put back
    raw = {}
    def stash(m):
        key = f"\x00RAW{len(raw)}\x00"
        raw[key] = m.group(0)
        return key
    md = re.sub(r"<dl class=\"glossary\">.*?</dl>", stash, md, flags=re.S)
    md = re.sub(r"\s*\{#[a-z-]+\}\s*$", "", md, flags=re.M)      # heading anchors handled below
    html = md_to_html(md)
    for key, val in raw.items():
        html = html.replace(f"<p>{key}</p>", val).replace(key, val)
    # <span class="est"> was escaped by the renderer; restore it
    html = html.replace("&lt;span class=&quot;est&quot;&gt;", '<span class="est">').replace("&lt;span class=\"est\"&gt;", '<span class="est">').replace("&lt;/span&gt;", "</span>")
    # wrap each <h2> block in a section with the site's label style and stable ids
    parts = re.split(r"(?=<h2 )", html)
    out = []
    for p in parts:
        m = re.match(r'<h2 id="[^"]*">(\d+)\.\s*(.*?)</h2>', p)
        if not m:
            out.append(p); continue
        num, title = m.group(1), m.group(2)
        sid = f"s{num}"
        alias = f' <span id="{ANCHORS[num]}"></span>' if num in ANCHORS else ""
        out.append(f'<section class="dsection pack-section" id="{sid}"><div class="dsection-label">{num} · {e(SECTION_LABELS[num])}</div>'
                   f'<h2>{title}{alias}</h2>{p[m.end():]}</section>')
    body = "\n".join(out)
    toc = "".join(f'<a href="#s{k}">{k} · {e(v.split(" · ")[0])}</a>' for k, v in SECTION_LABELS.items())
    desc = ("The zero-experience founder playbook for the 50 gongban ideas: the kill question, ordering samples, EVT/DVT/PVT, "
            "finding and vetting a Shenzhen manufacturer, CE and FCC certification, EU import and customs, logistics, a landed-cost worksheet and the outreach e-mails.")
    return f'''{head("Zero-experience founder playbook — from gongban idea to shipped product · GONGBANS", desc, "playbook.html")}
<body>
{nav("ideas")}

<div class="page-header">
  <div class="page-header-inner">
    <div class="crumbs"><a href="/ideas.html">Ideas</a><span class="sep">/</span><span>Playbook</span></div>
    <div class="header-id">FOUNDER PLAYBOOK · SHARED BY ALL 50 IDEAS · UPDATED {e(UPDATED.upper())}</div>
    <h1>Never built hardware? <em>Start here.</em></h1>
    <p class="sub">What every start pack has in common, for founders who have shipped software and never had a product made: the order of operations, the words, the paperwork, and who to e-mail in Shenzhen.</p>
  </div>
</div>

<main class="detail startpack playbook">
  <div class="idea-disclaimer"><strong>General guidance, not advice.</strong> This page explains the process shared by the 50 ideas. Directive numbers and VAT rates are public rules as of {e(UPDATED)}; every cost, quantity and duration is a rough estimate marked as such, to be replaced by your own quotes. Not legal, tax or investment advice. The companies named in each pack's "Who to contact" section come from gongban.db and are not verified suppliers for any specific idea.</div>
  <nav class="pb-toc" aria-label="Sections">{toc}</nav>

  <article class="pack-body">
{body}
  </article>

  <section class="dsection" id="help">
    <div class="dsection-label">Where next</div>
    <div class="hans-note">
      <div class="hans-note-label">Pick an idea, run its kill question</div>
      <p>The <a href="/ideas.html">50 ideas</a> each have a founder start pack with the boards, the plan, the people on file and the two e-mails. If you take one on and want a second pair of eyes on the sourcing, <a href="https://hansstam.eu">talk to Hans via hansstam.eu</a>.</p>
    </div>
  </section>

  <p class="catalogue-note">Playbook written for the GONGBANS founder start packs, {e(UPDATED)}. Board facts come from the <a href="/boards.html">catalogue</a>; company facts from gongban.db; everything else here is general guidance with estimates marked. <a href="/ideas.html#startpacks">All start packs →</a></p>
</main>

{FOOTER}
</body>
</html>
'''


def build():
    OUT.write_text(render(), encoding="utf-8")
    print("playbook.html: written")


if __name__ == "__main__":
    build()
