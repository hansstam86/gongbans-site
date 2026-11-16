#!/usr/bin/env python3
"""
build_guides.py: short platform guides under /guides/, linked from the issuer cards on issuers.html
(ISSUER_GUIDES in build_detail_pages.py) and from the credit box of that issuer's board pages.

Currently: /guides/build-with-tuya.html (added 2026-11-16 with the Tuya module import).
Generic guidance in Hans's voice; no company names other than the platform itself, no prices.
Called by build_detail_pages.py main(); can also be run on its own:  python3 build_guides.py
"""

from pathlib import Path

from build_detail_pages import FOOTER, e, head, nav
from build_startpacks import md_to_html

ROOT = Path(__file__).parent
OUT_DIR = ROOT / "guides"
UPDATED = "November 2026"

TUYA = r"""
A Tuya module is a small radio board (Wi-Fi, Bluetooth, Zigbee, Thread, Sub-G or cellular) that comes with Tuya's firmware on it and a place in Tuya's cloud. You solder it onto your PCB, set up your product on Tuya's developer platform, and your device shows up in Tuya's Smart Life app, or in a white-label app with your logo. No backend team, no app team. That is the pitch, and for the right product it is a good one.

## When it fits

- You want a connected consumer product on the shelf fast: plugs, lights, sensors, heaters, pet feeders, small appliances.
- The product is the hardware, not the software. You are fine with "the app" being an off-the-shelf app with your brand on it.
- You want voice assistants and the usual smart-home integrations without negotiating each one yourself.
- Your factory already knows Tuya. Most Shenzhen smart-home factories do, and that alone saves you weeks.

## When it does not

- **You want your own cloud, your own firmware, your own data.** On the standard path the device runs Tuya's firmware and talks to Tuya's cloud. You can go deeper with TuyaOS and the SDKs, but you are building on their platform, not yours.
- **Your customers ask where the data lives.** Tuya runs regional data centres. The GDPR questions are still yours: who is controller, who is processor, which data processing agreement. Sort it before launch, not when the first big buyer asks.
- **You think the module makes you compliant.** It doesn't. Under the EU Cyber Resilience Act and EN 18031 (the cybersecurity standard under the Radio Equipment Directive) you, the maker, carry the duty: security updates, vulnerability handling, the technical file. A certified module helps with your radio tests. It does not sign your declaration of conformity.
- **You plan to raise money on "our platform".** Investors will ask what you own. On a Tuya product the honest answer is the brand, the hardware and the customer.

## How to start

1. **Buy a dev kit.** Tuya sells demo boards for its main module families. Play with one for a weekend before you design anything.
2. **Create the product on the Tuya developer platform** (platform.tuya.com). Pick the category, define the functions, and choose: no-code (the module runs everything) or MCU mode (your own microcontroller talks to the module over a serial link).
3. **Pick the module.** Match radio, size, pins and antenna to your enclosure. Every Tuya module in our catalogue links to its official datasheet.
4. **Certification.** Check which radio certificates the module already has, then plan your own CE (RED), EN 18031 and, for the US, FCC. Plan time for it. It is never the quick part.

Then build a small batch, put it in real homes, and only then order volume.
"""


def page_tuya():
    body = md_to_html(TUYA.strip(), "tuya")
    desc = ("Build it with Tuya: what a Tuya module is, when it fits a connected consumer product, when it does not "
            "(own cloud, data residency, CRA and EN 18031 duties), and how to start: dev kit, Tuya platform, module, certification.")
    return f'''{head("Build it with Tuya: when a Tuya module fits, and when it doesn't · GONGBANS", desc, "guides/build-with-tuya.html")}
<body>
{nav("issuers")}

<div class="page-header">
  <div class="page-header-inner">
    <div class="crumbs"><a href="/issuers.html">Who makes them</a><span class="sep">/</span><a href="/boards.html#issuer=Tuya">Tuya</a><span class="sep">/</span><span>Guide</span></div>
    <div class="header-id">GUIDE · TUYA MODULES · UPDATED {e(UPDATED.upper())}</div>
    <h1>Build it with <em>Tuya</em></h1>
    <p class="sub">The fastest way to put a connected consumer product on the market, and the trade-offs that come with it.</p>
  </div>
</div>

<main class="detail startpack playbook">
  <div class="idea-disclaimer"><strong>General guidance, not advice.</strong> Listed from Tuya's public documentation; Tuya is not affiliated with GONGBANS unless stated. Check Tuya's own documentation and current terms before you decide. Not legal advice.</div>

  <article class="pack-body">
{body}
  </article>

  <section class="dsection" id="modules">
    <div class="dsection-label">Next</div>
    <div class="hans-note">
      <div class="hans-note-label">Pick a module</div>
      <p>All <a href="/boards.html#issuer=Tuya">Tuya modules in the catalogue</a>, each with its chip, radio, size and a link to Tuya's official datasheet. Never had a product made? Read <a href="/start.html">Start here</a> and the <a href="/playbook.html">founder playbook</a> first.</p>
    </div>
  </section>

  <section class="dsection" id="credit">
    <div class="dsection-label">Credit</div>
    <h2>Content credit</h2>
    <p>Credit: Tuya Smart (tuya.com). Listed from Tuya's public documentation; Tuya is not affiliated with GONGBANS unless stated.</p>
    <p><a href="https://www.tuya.com" target="_blank" rel="noopener">tuya.com ↗</a> · <a href="https://developer.tuya.com/en/docs/iot/network-module-overview?id=Ka4z12ojepber" target="_blank" rel="noopener">Tuya network modules ↗</a></p>
  </section>
</main>

{FOOTER}
</body>
</html>
'''


def build():
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "build-with-tuya.html").write_text(page_tuya(), encoding="utf-8")
    print("guides/build-with-tuya.html: written")


if __name__ == "__main__":
    build()
