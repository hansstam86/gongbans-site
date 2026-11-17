#!/usr/bin/env python3
"""
build_validate.py — "Validate demand first" for every founder start pack.

    startpacks/<slug>.md    section "## 2. Validate demand first" inserted/refreshed between the
                            <!-- validate-demand:start --> … <!-- validate-demand:end --> markers,
                            directly after the Summary and BEFORE the business plan, start kit and
                            the sourcing section. Existing sections are renumbered once:
                            Business plan 2→3, Start kit 3→4, Who to contact 4→5, Next steps 5→6.

The section is idea-specific, built from data/ideas.json (audience, kill_question, pitch, price,
tags) and the pack's own Problem bullet, plus two hand-curated tables below:

    PROBE      one problem-first opening question per idea for the customer interview
    WHERE      which communities / associations to look for that idea's audience in

Accuracy rule for WHERE: only communities the author is confident exist and are relevant (checked
against what we know as of November 2026). Anything less certain is expressed as "search for … in
your market" rather than a name that may be wrong or dead. Every pack repeats that caveat.

Run from the repo root:  python3 build_validate.py      (build_ideas.py calls patch_packs() after
build_contacts.patch_packs() and before the packs are rendered)
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
IDEAS_JSON = ROOT / "data" / "ideas.json"
PACK_DIR = ROOT / "startpacks"

START = "<!-- validate-demand:start -->"
END = "<!-- validate-demand:end -->"
CONVERSATIONS = "15–20"

# ---------------------------------------------------------------------------
# communities (id → label, url, what it is). Keep to ones that exist and are active.
# ---------------------------------------------------------------------------
C = {
    # reddit
    "r_homeassistant": ("r/homeassistant", "https://www.reddit.com/r/homeassistant/", "the largest home-automation community; very receptive to new sensors and ESP32 devices"),
    "r_smarthome": ("r/smarthome", "https://www.reddit.com/r/smarthome/", "less technical smart-home buyers"),
    "r_esp32": ("r/esp32", "https://www.reddit.com/r/esp32/", "ESP32 builders; good for early technical feedback, less for buyers"),
    "r_heatpumps": ("r/heatpumps", "https://www.reddit.com/r/heatpumps/", "heat-pump owners and installers, EU and US"),
    "r_solar": ("r/solar", "https://www.reddit.com/r/solar/", "PV owners"),
    "r_hvac": ("r/HVAC", "https://www.reddit.com/r/HVAC/", "HVAC technicians (mostly US); installer mindset"),
    "r_electricians": ("r/electricians", "https://www.reddit.com/r/electricians/", "working electricians"),
    "r_plumbing": ("r/Plumbing", "https://www.reddit.com/r/Plumbing/", "plumbers and heating engineers"),
    "r_plc": ("r/PLC", "https://www.reddit.com/r/PLC/", "industrial automation engineers and integrators"),
    "r_embedded": ("r/embedded", "https://www.reddit.com/r/embedded/", "embedded engineers"),
    "r_askelectronics": ("r/AskElectronics", "https://www.reddit.com/r/AskElectronics/", "electronics hobbyists and students"),
    "r_scienceteachers": ("r/ScienceTeachers", "https://www.reddit.com/r/ScienceTeachers/", "secondary-school science teachers"),
    "r_teachers": ("r/Teachers", "https://www.reddit.com/r/Teachers/", "teachers in general; use for the budget-holder question"),
    "r_woodworking": ("r/woodworking", "https://www.reddit.com/r/woodworking/", "hobby and small-shop woodworkers"),
    "r_mushroomgrowers": ("r/MushroomGrowers", "https://www.reddit.com/r/MushroomGrowers/", "hobby and small-farm mushroom growers"),
    "r_mycology": ("r/mycology", "https://www.reddit.com/r/mycology/", "mycology hobbyists"),
    "r_beekeeping": ("r/Beekeeping", "https://www.reddit.com/r/Beekeeping/", "beekeepers"),
    "r_entomology": ("r/Entomology", "https://www.reddit.com/r/Entomology/", "insect scientists and enthusiasts"),
    "r_farming": ("r/farming", "https://www.reddit.com/r/farming/", "working farmers"),
    "r_homesteading": ("r/homestead", "https://www.reddit.com/r/homestead/", "smallholders"),
    "r_pestcontrol": ("r/pestcontrol", "https://www.reddit.com/r/pestcontrol/", "pest-control technicians and owners"),
    "r_propertymanagement": ("r/PropertyManagement", "https://www.reddit.com/r/PropertyManagement/", "property and facility managers"),
    "r_landlord": ("r/Landlord", "https://www.reddit.com/r/Landlord/", "small landlords"),
    "r_homeimprovement": ("r/HomeImprovement", "https://www.reddit.com/r/HomeImprovement/", "homeowners with damp, mould and air problems"),
    "r_smallbusiness": ("r/smallbusiness", "https://www.reddit.com/r/smallbusiness/", "shop and café owners"),
    "r_restaurateur": ("r/restaurateur", "https://www.reddit.com/r/restaurateur/", "restaurant owners"),
    "r_kitchenconfidential": ("r/KitchenConfidential", "https://www.reddit.com/r/KitchenConfidential/", "chefs and kitchen staff; the people who do the fridge log"),
    "r_reptiles": ("r/reptiles", "https://www.reddit.com/r/reptiles/", "reptile keepers"),
    "r_beardeddragons": ("r/BeardedDragons", "https://www.reddit.com/r/BeardedDragons/", "the single largest UVB-dependent pet community"),
    "r_leopardgeckos": ("r/leopardgeckos", "https://www.reddit.com/r/leopardgeckos/", "gecko keepers"),
    "r_blind": ("r/Blind", "https://www.reddit.com/r/Blind/", "blind and low-vision users; ask, do not pitch"),
    "r_deaf": ("r/deaf", "https://www.reddit.com/r/deaf/", "Deaf community; read the rules on hearing-person posts first"),
    "r_hardofhearing": ("r/hardofhearing", "https://www.reddit.com/r/hardofhearing/", "hard-of-hearing adults, many late-deafened"),
    "r_disability": ("r/disability", "https://www.reddit.com/r/disability/", "disabled users and carers"),
    "r_agingparents": ("r/AgingParents", "https://www.reddit.com/r/AgingParents/", "adult children caring for parents: the buyer for most elderly-care devices"),
    "r_caregiversupport": ("r/CaregiverSupport", "https://www.reddit.com/r/CaregiverSupport/", "family carers"),
    "r_dementia": ("r/dementia", "https://www.reddit.com/r/dementia/", "families living with dementia"),
    "r_museumpros": ("r/MuseumPros", "https://www.reddit.com/r/MuseumPros/", "museum staff"),
    "r_ros": ("r/ROS", "https://www.reddit.com/r/ROS/", "ROS users and teachers"),
    "r_robotics": ("r/robotics", "https://www.reddit.com/r/robotics/", "robotics hobbyists, students, educators"),
    "r_controltheory": ("r/ControlTheory", "https://www.reddit.com/r/ControlTheory/", "control engineers and students"),
    "r_18650": ("r/18650masterrace", "https://www.reddit.com/r/18650masterrace/", "cell harvesters and pack builders"),
    "r_batteries": ("r/batteries", "https://www.reddit.com/r/batteries/", "battery hobbyists"),
    "r_ebikes": ("r/ebikes", "https://www.reddit.com/r/ebikes/", "e-bike owners who rebuild packs"),
    "r_synthesizers": ("r/synthesizers", "https://www.reddit.com/r/synthesizers/", "synth and MIDI musicians"),
    "r_wearethemusicmakers": ("r/WeAreTheMusicMakers", "https://www.reddit.com/r/WeAreTheMusicMakers/", "musicians and music teachers"),
    "r_ergomech": ("r/ErgoMechKeyboards", "https://www.reddit.com/r/ErgoMechKeyboards/", "ergonomic and one-handed keyboard users and builders"),
    "r_videography": ("r/videography", "https://www.reddit.com/r/videography/", "working videographers"),
    "r_cinematography": ("r/cinematography", "https://www.reddit.com/r/cinematography/", "camera crews"),
    "r_amateurradio": ("r/amateurradio", "https://www.reddit.com/r/amateurradio/", "radio hobbyists who also teach and mentor"),
    "r_trackandfield": ("r/trackandfield", "https://www.reddit.com/r/trackandfield/", "athletes and coaches"),
    "r_octopus": ("r/Octopus_Energy", "https://www.reddit.com/r/Octopus_Energy/", "UK customers on time-of-use tariffs"),
    "r_transit": ("r/transit", "https://www.reddit.com/r/transit/", "public-transport enthusiasts"),
    "r_astronomy": ("r/Astronomy", "https://www.reddit.com/r/Astronomy/", "amateur astronomers; light pollution is a constant topic"),
    "darksky": ("DarkSky International", "https://darksky.org/", "the certification body and its European chapters; municipalities and parks come through here"),
    "vds": ("VdS, Vereinigung der Sternfreunde (DE)", "https://www.vds-astro.de/", "German amateur-astronomy federation with a light-pollution working group"),
    "r_eceprofessionals": ("r/ECEProfessionals", "https://www.reddit.com/r/ECEProfessionals/", "early-childhood educators; noise and stress come up often"),
    "r_techtheatre": ("r/techtheatre", "https://www.reddit.com/r/techtheatre/", "stage managers and technicians, many in schools and amateur theatre"),
    "blueroom": ("The Blue Room (UK)", "https://www.blue-room.org.uk/", "UK technical-theatre forum; DIY cue-light threads live here"),
    "r_sysadmin": ("r/sysadmin", "https://www.reddit.com/r/sysadmin/", "the IT people who approve or block a calendar integration"),
    "r_msp": ("r/msp", "https://www.reddit.com/r/msp/", "managed-service providers: the reseller channel for office devices"),
    "controlbooth": ("ControlBooth", "https://www.controlbooth.com/", "technical-theatre forum; the show-relay and paging threads live here"),
    "r_pottery": ("r/Pottery", "https://www.reddit.com/r/Pottery/", "hobby potters, many with a home kiln"),
    "digitalfire": ("Digitalfire", "https://digitalfire.com/", "ceramics reference and community; the source on controller safety and insurance"),
    "r_arborists": ("r/arborists", "https://www.reddit.com/r/arborists/", "tree-care professionals, including municipal crews"),
    # forums and communities
    "ha_forum": ("Home Assistant Community forum", "https://community.home-assistant.io/", "where new devices get adopted or ignored; also the Home Assistant and ESPHome Discord servers"),
    "tweakers": ("Tweakers forum (NL)", "https://gathering.tweakers.net/", "Dutch tech forum with active energy, domotica and smart-meter sections"),
    "pvforum": ("Photovoltaikforum (DE)", "https://www.photovoltaikforum.com/", "German PV, battery, heat-pump and dynamic-tariff owners"),
    "haustechnik": ("HaustechnikDialog (DE)", "https://www.haustechnikdialog.de/", "German heating installers and owners; hydronic balancing, heat pumps, legionella"),
    "oem": ("OpenEnergyMonitor community", "https://community.openenergymonitor.org/", "open energy-monitoring builders; heat-pump monitoring is a major topic"),
    "ttn": ("The Things Network forum", "https://www.thethingsnetwork.org/forum/", "LoRaWAN builders, operators and the companies that deploy them"),
    "hackaday": ("Hackaday / hackaday.io", "https://hackaday.io/", "maker audience; visibility more than buyers"),
    "eevblog": ("EEVblog forum", "https://www.eevblog.com/forum/", "electronics engineers and serious hobbyists; test-equipment and soldering opinions"),
    "mikrocontroller": ("mikrocontroller.net (DE)", "https://www.mikrocontroller.net/", "German-speaking electronics engineers and students"),
    "plctalk": ("PLCtalk forum", "https://www.plctalk.net/", "industrial automation technicians and integrators"),
    "controlcom": ("Control.com forum", "https://control.com/", "process-control and instrumentation engineers"),
    "shroomery": ("Shroomery", "https://www.shroomery.org/forums/", "long-running mushroom-cultivation forum"),
    "farmingforum": ("The Farming Forum (UK)", "https://thefarmingforum.co.uk/", "UK farmers; machinery, arable, livestock, farm diversification"),
    "landtreff": ("Landtreff (DE)", "https://www.landtreff.de/", "German farmers' forum"),
    "endless": ("Endless Sphere forum", "https://endless-sphere.com/", "e-bike and battery-pack builders"),
    "diysolar": ("DIY Solar Power forum", "https://diysolarforum.com/", "home battery and second-life cell builders"),
    "geekhack": ("geekhack", "https://geekhack.org/", "custom keyboard builders and group buys"),
    "ros_discourse": ("ROS Discourse", "https://discourse.ros.org/", "the official ROS community; education category"),
    "reptileforums": ("Reptile Forums (UK)", "https://www.reptileforums.co.uk/", "UK reptile keepers"),
    "applevis": ("AppleVis", "https://www.applevis.com/", "blind and low-vision technology users; the most tech-literate part of the audience"),
    "ukworkshop": ("UKworkshop", "https://www.ukworkshop.co.uk/", "UK woodworkers and small shops"),
    "festool": ("Festool Owners Group", "https://www.festoolownersgroup.com/", "dust-extraction-conscious woodworkers"),
    "inat": ("iNaturalist forum", "https://forum.inaturalist.org/", "citizen scientists and ecologists"),
    "lines": ("lines (llllllll.co)", "https://llllllll.co/", "experimental-music and instrument-builder community"),
    "alz_forum": ("Alzheimer's Society Dementia Support Forum (UK, formerly Talking Point)", "https://forum.alzheimers.org.uk/", "families and carers of people with dementia"),
    "carersuk": ("Carers UK forum", "https://www.carersuk.org/forum/", "family carers in the UK"),
    "tes": ("Tes Community (UK)", "https://community.tes.com/", "UK teachers' forum"),
    # associations and trade bodies
    "dsv": ("DSV, Deutscher Schädlingsbekämpfer-Verband", "https://www.dsvonline.de/", "German pest-control association; regional meetings"),
    "bpca": ("BPCA, British Pest Control Association", "https://bpca.org.uk/", "UK pest-control trade body; PestEx trade show"),
    "npma": ("NPMA, National Pest Management Association", "https://npmapestworld.org/", "US pest-control association"),
    "ifma": ("IFMA", "https://www.ifma.org/", "facility managers; local chapters across Europe"),
    "gefma": ("GEFMA", "https://www.gefma.de/", "German facility-management association"),
    "zvshk": ("ZVSHK", "https://www.zvshk.de/", "German plumbing/heating installer federation; the local Innung is the way in"),
    "aapt": ("AAPT", "https://www.aapt.org/", "American Association of Physics Teachers"),
    "iop": ("IOP, Institute of Physics (UK)", "https://www.iop.org/", "UK physics teacher network and conferences"),
    "mnu": ("MNU (DE)", "https://www.mnu.de/", "German association of maths and science teachers; regional conferences"),
    "farmretail": ("Farm Retail Association (UK)", "https://farmretail.co.uk/", "farm shops and farmers' markets"),
    "nemo": ("NEMO, Network of European Museum Organisations", "https://www.ne-mo.org/", "European museum associations"),
    "mcn": ("MCN, Museum Computer Network", "https://mcn.edu/", "museum technology staff"),
    "ukhospitality": ("UKHospitality", "https://www.ukhospitality.org.uk/", "UK hospitality trade body"),
    "dehoga": ("DEHOGA (DE)", "https://www.dehoga-bundesverband.de/", "German hotel and restaurant association"),
    "dght": ("DGHT (DE)", "https://www.dght.de/", "German herpetological society; regional groups of reptile keepers"),
    "rnib": ("RNIB (UK)", "https://www.rnib.org.uk/", "blind and partially sighted people; RNIB Connect community"),
    "dbsv": ("DBSV (DE)", "https://www.dbsv.org/", "German federation of the blind and visually impaired"),
    "hlaa": ("HLAA, Hearing Loss Association of America", "https://www.hearingloss.org/", "hard-of-hearing adults; local chapters"),
    "drake": ("Drake Music (UK)", "https://www.drakemusic.org/", "accessible music technology charity"),
    "ohmi": ("OHMI Trust (UK)", "https://www.ohmi.org.uk/", "one-handed musical instruments; runs a competition for exactly this"),
    "abilitynet": ("AbilityNet (UK)", "https://abilitynet.org.uk/", "assistive technology charity"),
    "vow": ("Verbund Offener Werkstätten (DE)", "https://www.offene-werkstaetten.org/", "German network of open workshops and makerspaces"),
    "hackerspaces": ("hackerspaces.org wiki", "https://wiki.hackerspaces.org/", "directory of makerspaces worldwide; e-mail the ones near you"),
    "fpa": ("FPA, Fire Protection Association (UK)", "https://www.thefpa.co.uk/", "fire-safety professionals"),
    "dosb": ("DOSB (DE)", "https://www.dosb.de/", "German sports confederation; the regional Landessportbund reaches the clubs"),
    # added 2026-11-17 for the round-2 ideas (non-Reddit URLs checked with GET 200 on 17 Nov 2026)
    "r_dogs": ("r/dogs", "https://www.reddit.com/r/dogs/", "dog owners; health and behaviour questions"),
    "r_cats": ("r/cats", "https://www.reddit.com/r/cats/", "cat owners"),
    "r_dogtraining": ("r/Dogtraining", "https://www.reddit.com/r/Dogtraining/", "owners and trainers; separation problems are a constant topic"),
    "r_airbnbhosts": ("r/AirBnBHosts", "https://www.reddit.com/r/AirBnBHosts/", "short-stay hosts; party and noise complaints come up often"),
    "airbnb_community": ("Airbnb Community Center", "https://communitycenter.airbnb.com/", "Airbnb's own host forum, with country and language boards"),
    "r_gardening": ("r/gardening", "https://www.reddit.com/r/gardening/", "home gardeners"),
    "r_ukgardening": ("r/UKGardening", "https://www.reddit.com/r/UKGardening/", "UK gardeners and allotment holders; hosepipe bans come up every summer"),
    "nas": ("The National Allotment Society (UK)", "https://thenas.org.uk/", "UK allotment federation (formerly NSALG); member associations run the sites"),
    "bdg": ("Bundesverband der Kleingartenvereine Deutschlands (DE)", "https://kleingarten-bund.de/", "German allotment federation; the regional and local Kleingartenvereine are the way in"),
    "dib": ("Deutscher Imkerbund (DE)", "https://deutscherimkerbund.de/", "German beekeepers' federation; local Imkervereine meet monthly"),
    "bbka": ("BBKA, British Beekeepers Association", "https://www.bbka.org.uk/", "UK beekeepers; local associations and the spring convention"),
    "csa": ("Connectivity Standards Alliance", "https://csa-iot.org/", "the body behind Matter and Zigbee; member companies, certification and training"),
    "r_homekit": ("r/HomeKit", "https://www.reddit.com/r/HomeKit/", "Apple Home users; Matter and Thread devices are a main topic"),
    "r_esphome": ("r/Esphome", "https://www.reddit.com/r/Esphome/", "ESPHome builders; mmWave presence sensors are a frequent topic"),
    "r_rtlsdr": ("r/RTLSDR", "https://www.reddit.com/r/RTLSDR/", "software-defined-radio hobbyists; 433 MHz decoding with rtl_433 is common"),
    "r_flipperzero": ("r/flipperzero", "https://www.reddit.com/r/flipperzero/", "owners of the Flipper Zero, the people already poking at sub-GHz remotes"),
    "repaircafe": ("Repair Café International", "https://www.repaircafe.org/", "network of volunteer repair cafés; the local café is the way in"),
    "diyaudio": ("diyAudio forum", "https://www.diyaudio.com/community/", "audio DIY builders; power supplies and ground loops are core topics"),
    "csta": ("CSTA, Computer Science Teachers Association", "https://csteachers.org/", "computing teachers (mostly US) with chapters"),
    "cas": ("Computing at School (UK)", "https://www.computingatschool.org.uk/", "UK computing teachers' community and local hubs"),
    "alz_europe": ("Alzheimer Europe", "https://www.alzheimer-europe.org/", "umbrella of the national Alzheimer associations; find your country's member there"),
    "dalzg": ("Deutsche Alzheimer Gesellschaft (DE)", "https://www.deutsche-alzheimer.de/", "German Alzheimer association; regional groups and carer support"),
    "age_platform": ("AGE Platform Europe", "https://www.age-platform.eu/", "EU network of organisations of and for older people"),
    "tsa": ("TSA, TEC Services Association (UK)", "https://www.tsa-voice.org.uk/", "UK trade body for technology-enabled care (telecare); the buyers in councils and housing providers"),
    "r_wheelchairs": ("r/wheelchairs", "https://www.reddit.com/r/wheelchairs/", "wheelchair users; ask, do not pitch"),
    "r_ot": ("r/OccupationalTherapy", "https://www.reddit.com/r/OccupationalTherapy/", "occupational therapists, the people who recommend assistive devices"),
    "rcot": ("RCOT, Royal College of Occupational Therapists (UK)", "https://www.rcot.co.uk/", "UK occupational therapists"),
    "dve": ("DVE, Deutscher Verband Ergotherapie (DE)", "https://www.dve.info/", "German occupational-therapy association"),
    "aaate": ("AAATE", "https://aaate.net/", "European association for assistive technology; researchers, therapists and makers"),
    "euroblind": ("European Blind Union", "https://www.euroblind.org/", "umbrella of the national organisations of the blind; find your country's member there"),
    "thecircuit": ("The Circuit (UK)", "https://www.thecircuit.uk/", "the UK national defibrillator network; the people who register and look after public AEDs"),
    "resus_uk": ("Resuscitation Council UK", "https://www.resus.org.uk/", "UK resuscitation guidance body"),
    "erc": ("European Resuscitation Council", "https://www.erc.edu/", "European resuscitation guidelines; national councils are members"),
    "grc": ("German Resuscitation Council (GRC, DE)", "https://www.grc-org.de/", "German resuscitation council"),
    "efci": ("EFCI", "https://www.efci.eu/", "European federation of cleaning and facility-services companies"),
    "biv": ("Die Gebäudedienstleister (BIV, DE)", "https://www.die-gebaeudedienstleister.de/", "German building-cleaning trade federation"),
    "hde": ("HDE, Handelsverband Deutschland", "https://einzelhandel.de/", "German retail association; regional associations reach the shops"),
    "eurocommerce": ("EuroCommerce", "https://www.eurocommerce.eu/", "European retail and wholesale federation"),
    "r_zerowaste": ("r/ZeroWaste", "https://www.reddit.com/r/ZeroWaste/", "zero-waste shoppers and some shop owners"),
    "unverpackt": ("Unverpackt e.V. (DE)", "https://www.unverpackt-verband.de/", "German association of package-free and refill shops"),
    "r_breadit": ("r/Breadit", "https://www.reddit.com/r/Breadit/", "bread bakers, home and professional"),
    "baecker": ("Zentralverband des Deutschen Bäckerhandwerks (DE)", "https://www.baeckerhandwerk.de/", "German bakers' trade federation; the local Bäckerinnung is the way in"),
    "r_pharmacy": ("r/pharmacy", "https://www.reddit.com/r/pharmacy/", "pharmacists and pharmacy staff"),
    "djv": ("DJV, Deutscher Jagdverband (DE)", "https://www.jagdverband.de/", "German hunters' association; wild-boar damage on crops is a standing topic"),
    "face": ("FACE", "https://www.face.eu/", "European federation of hunting associations"),
    "r_equestrian": ("r/Equestrian", "https://www.reddit.com/r/Equestrian/", "horse owners and yard managers"),
    "yellowwellies": ("Farm Safety Foundation / Yellow Wellies (UK)", "https://yellowwellies.org/", "UK farm-safety charity; lone working on farms is one of its topics"),
    "r_septic": ("r/septic", "https://www.reddit.com/r/septic/", "homeowners and installers with septic tanks and pump pits"),
    "gdw": ("GdW (DE)", "https://www.gdw.de/", "German federation of housing companies and cooperatives"),
    "aedes": ("Aedes (NL)", "https://aedes.nl/", "Dutch federation of housing associations (woningcorporaties)"),
    "euroheat": ("Euroheat & Power", "https://www.euroheat.org/", "European district-heating association"),
    "agfw": ("AGFW (DE)", "https://www.agfw.de/", "German district-heating association; metering is one of its working groups"),
    "hotrec": ("HOTREC", "https://www.hotrec.eu/", "European umbrella of national hotel and restaurant associations"),
    "fediaf": ("FEDIAF, European Pet Food", "https://europeanpetfood.org/", "European pet-food industry federation; its members are the brands"),
    "interzoo": ("Interzoo (Nuremberg)", "https://www.interzoo.com/", "the main European pet-industry trade fair; exhibitor list = buyer list"),
    "r_sleep": ("r/sleep", "https://www.reddit.com/r/sleep/", "people who sleep badly and talk about it"),
}

# where to look, per idea
WHERE = {
    "tariff-lamp": ["tweakers", "pvforum", "r_homeassistant", "oem", "r_octopus"],
    "mould-risk-monitor": ["r_homeimprovement", "haustechnik", "tweakers", "r_landlord", "r_propertymanagement"],
    "smiley-terminal": ["ifma", "gefma", "r_propertymanagement", "r_smallbusiness"],
    "club-scoreboard": ["dosb", "r_trackandfield"],
    "fire-door-watch": ["ifma", "gefma", "fpa", "r_propertymanagement"],
    "hallway-transit-board": ["r_homeassistant", "tweakers", "r_transit", "ha_forum"],
    "meter-eye": ["r_homeassistant", "ha_forum", "pvforum", "tweakers"],
    "sg-ready-price-switch": ["haustechnik", "pvforum", "r_heatpumps", "oem", "tweakers"],
    "shop-window-epaper-signs": ["r_smallbusiness"],
    "loop-logger-4-20ma": ["plctalk", "controlcom", "r_plc", "ttn"],
    "balance-kit": ["haustechnik", "zvshk", "r_hvac", "r_heatpumps"],
    "build-a-radio-kit": ["r_scienceteachers", "r_amateurradio", "mnu", "tes"],
    "classroom-geiger-kit": ["r_scienceteachers", "aapt", "iop", "mnu", "tes"],
    "fruiting-chamber-controller": ["r_mushroomgrowers", "shroomery", "r_mycology"],
    "half-keyboard": ["r_ergomech", "geekhack", "r_disability", "abilitynet"],
    "hay-spear": ["farmingforum", "landtreff", "r_farming", "r_homesteading"],
    "isolated-interface-kit": ["r_plc", "plctalk", "r_embedded", "eevblog"],
    "nfc-voice-labels": ["r_blind", "applevis", "rnib", "dbsv", "r_agingparents"],
    "one-knob-radio": ["r_agingparents", "r_dementia", "alz_forum", "r_caregiversupport"],
    "accessible-midi-instrument": ["drake", "ohmi", "r_synthesizers", "r_wearethemusicmakers", "lines"],
    "sip-coaster": ["r_agingparents", "r_caregiversupport", "carersuk"],
    "touchless-switch-module": ["hackaday", "r_esp32", "eevblog"],
    "trap-check": ["dsv", "bpca", "npma", "r_pestcontrol"],
    "uvb-lamp-checker": ["r_beardeddragons", "r_reptiles", "r_leopardgeckos", "reptileforums", "dght"],
    "bedroom-audit-box": ["r_homeimprovement", "r_landlord", "tweakers"],
    "club-timing-gates": ["r_trackandfield", "dosb", "r_scienceteachers"],
    "haccp-fridge-logger": ["r_kitchenconfidential", "r_restaurateur", "dehoga", "ukhospitality"],
    "modbus-pocket-analyser": ["plctalk", "r_plc", "controlcom", "r_hvac"],
    "trail-talker": ["r_museumpros", "nemo"],
    "workshop-dust-sentinel": ["r_woodworking", "ukworkshop", "festool", "vow", "hackerspaces"],
    "cell-grader": ["r_18650", "diysolar", "endless", "r_batteries"],
    "control-theory-balance-kit": ["r_controltheory", "r_robotics", "aapt", "mnu"],
    "farm-shop-self-checkout": ["farmretail", "farmingforum", "r_smallbusiness"],
    "frost-sentinel": ["farmingforum", "landtreff", "r_farming", "ttn"],
    "heat-pump-cop-lite": ["oem", "r_heatpumps", "haustechnik", "pvforum", "tweakers"],
    "pack-rebuilder-spot-welder": ["r_18650", "endless", "r_ebikes", "diysolar"],
    "school-scope": ["r_scienceteachers", "aapt", "iop", "mnu", "tes"],
    "sound-to-light-alert": ["r_deaf", "r_hardofhearing", "hlaa", "r_homeassistant"],
    "switchboard-hotspot-watch": ["r_electricians", "ifma", "gefma", "ttn"],
    "vibration-health-sticker": ["plctalk", "r_plc", "ttn", "ifma"],
    "footfall-counter": ["r_smallbusiness"],
    "haptic-setpoint-knob": ["r_homeassistant", "ha_forum", "r_esp32", "hackaday"],
    "trinkwasser-logger": ["gefma", "haustechnik", "zvshk", "r_propertymanagement", "ttn"],
    "makerspace-soldering-station": ["vow", "hackerspaces", "eevblog", "mikrocontroller", "r_askelectronics"],
    "motion-control-slider": ["r_videography", "r_cinematography"],
    "new-flat-air-check": ["r_homeimprovement", "tweakers", "r_landlord"],
    "quiet-guardian": ["r_agingparents", "r_dementia", "alz_forum", "carersuk"],
    "ros-trainer": ["ros_discourse", "r_ros", "r_robotics"],
    "offline-ai-docent": ["r_museumpros", "mcn", "nemo"],
    "pollinator-counter": ["r_beekeeping", "r_entomology", "inat"],
    "dark-sky-meter": ["r_astronomy", "vds", "darksky", "inat"],
    "classroom-noise-light": ["r_eceprofessionals", "r_teachers", "tes", "gefma"],
    "cue-light-system": ["r_techtheatre", "blueroom", "hackaday"],
    "village-stop-display": ["r_transit", "ttn"],
    "oil-tank-eye": ["r_homeassistant", "ha_forum", "haustechnik", "pvforum", "tweakers"],
    "room-door-sign": ["r_sysadmin", "r_msp", "r_homeassistant", "ha_forum"],
    "kiln-mind": ["r_pottery", "digitalfire"],
    "vitrine-log": ["r_museumpros", "nemo", "mcn"],
    "tree-thirst-sensor": ["r_arborists", "ttn", "ifma"],
    "machine-access-box": ["vow", "hackerspaces", "hackaday"],
    "hall-heat-scheduler": ["dosb", "haustechnik", "zvshk"],
    "shared-laundry-notifier": ["r_propertymanagement", "r_homeassistant", "ha_forum", "gefma"],
    "stream-level-gauge": ["ttn", "r_homeassistant"],
    "emergency-light-logger": ["ifma", "gefma", "r_electricians", "fpa"],
    "tool-check-wand": ["r_electricians", "r_plumbing", "r_hvac"],
    "backstage-relay": ["controlbooth", "r_techtheatre", "blueroom"],
    # round 2 (gongban-inventor, 17 Nov 2026)
    "basement-flood-sentinel": ["r_homeimprovement", "haustechnik", "r_homeassistant", "tweakers", "nemo"],
    "night-path-light": ["r_agingparents", "r_caregiversupport", "carersuk", "age_platform"],
    "rain-barrel-irrigator": ["r_gardening", "r_ukgardening", "nas", "bdg", "r_homeassistant"],
    "aed-cabinet-monitor": ["thecircuit", "resus_uk", "erc", "grc", "dosb"],
    "clubhouse-last-out-check": ["dosb"],
    "isolated-bench-power-module": ["diyaudio", "eevblog", "r_askelectronics", "repaircafe", "mikrocontroller"],
    "pet-bowl-drink-watch": ["r_cats", "r_dogs"],
    "pump-station-alarm-relay": ["r_septic", "r_plumbing", "zvshk", "haustechnik"],
    "queue-radar": ["r_smallbusiness", "r_pharmacy", "hde", "eurocommerce", "baecker"],
    "radar-physics-kit": ["r_scienceteachers", "aapt", "iop", "mnu", "tes"],
    "washroom-visit-counter": ["efci", "biv", "ifma", "gefma", "ttn"],
    "mmwave-radar-carrier": ["r_homeassistant", "ha_forum", "r_esphome", "r_esp32", "hackaday"],
    "desk-occupancy-puck": ["ifma", "gefma", "r_sysadmin"],
    "industrial-esp32-carrier": ["plctalk", "r_plc", "r_esp32", "ha_forum", "eevblog"],
    "isolated-can-ble-sniffer": ["diysolar", "pvforum", "r_solar", "r_hvac", "plctalk"],
    "trough-level-radar": ["farmingforum", "landtreff", "r_farming", "r_equestrian", "ttn"],
    "matter-ac-ir-bridge": ["r_heatpumps", "r_homeassistant", "ha_forum", "tweakers", "r_homekit"],
    "matter-lab-kit": ["csa", "r_embedded", "mikrocontroller"],
    "matter-presence-puck": ["r_homeassistant", "ha_forum", "r_homekit", "r_smarthome", "tweakers"],
    "night-door-prompt": ["r_dementia", "alz_forum", "dalzg", "alz_europe", "r_caregiversupport"],
    "phone-booth-controller": ["ifma", "gefma"],
    "sub-ghz-remote-analyser": ["r_rtlsdr", "r_flipperzero", "r_homeassistant", "repaircafe", "r_amateurradio"],
    "legacy-433-matter-bridge": ["r_homeassistant", "ha_forum", "tweakers", "r_rtlsdr"],
    "bathroom-fall-alert": ["r_agingparents", "r_caregiversupport", "carersuk", "tsa", "age_platform"],
    "dog-alone-time-logger": ["r_dogs", "r_dogtraining"],
    "farmyard-help-button": ["r_agingparents", "carersuk", "farmingforum", "landtreff", "yellowwellies"],
    "fire-tank-level": ["fpa", "ifma", "gefma", "ttn"],
    "fitting-room-free-light": ["hde", "eurocommerce"],
    "heat-meter-lorawan-reader": ["ttn", "gdw", "aedes", "euroheat", "agfw"],
    "lora-class-network": ["ttn", "r_scienceteachers", "mnu", "iop", "r_amateurradio"],
    "meeting-room-no-show-sign": ["r_sysadmin", "r_msp", "ifma", "gefma"],
    "voice-door-opener": ["r_wheelchairs", "r_disability", "r_ot", "abilitynet", "dve"],
    "pitch-floodlight-remote": ["dosb"],
    "presence-infrared-heating": ["haustechnik", "r_homeassistant"],
    "proofing-cabinet-controller": ["r_breadit", "baecker", "r_restaurateur", "r_kitchenconfidential"],
    "party-noise-guard": ["r_airbnbhosts", "airbnb_community"],
    "refill-station-level": ["unverpackt", "r_zerowaste", "eurocommerce"],
    "room-ready-radar": ["hotrec", "dehoga", "ukhospitality"],
    "shed-guard-radar": ["nas", "bdg", "r_ukgardening", "ttn"],
    "hive-scale-lora": ["r_beekeeping", "dib", "bbka", "ttn"],
    "heat-pump-modbus-matter": ["r_heatpumps", "ha_forum", "oem", "haustechnik", "pvforum"],
    "sleep-rhythm-bedside": ["r_sleep", "r_agingparents"],
    "thread-switch-insert": ["r_homeassistant", "ha_forum", "r_electricians", "tweakers", "r_homekit"],
    "air-gesture-remote": ["r_ot", "rcot", "dve", "aaate", "r_disability"],
    "eu-brand-pet-feeder-camera": ["fediaf", "interzoo", "r_cats"],
    "field-edge-wildlife-alarm": ["djv", "face", "landtreff", "farmingforum", "r_farming"],
    "hotel-voice-panel": ["hotrec", "dehoga", "ukhospitality", "rnib"],
    "offline-voice-wall-switch": ["r_homeassistant", "ha_forum", "r_smarthome", "tweakers"],
    "powerline-outbuilding-meter": ["r_homeassistant", "ha_forum", "tweakers", "pvforum", "bdg"],
    "channel-sounding-wayfinding": ["euroblind", "rnib", "dbsv", "r_blind", "applevis", "nemo"],
}

# one problem-first opening question per idea (never mentions the product)
PROBE = {
    "tariff-lamp": "When was the last time you actually changed when you ran the dishwasher or charged the car because of the hourly price, and how did you know the price at that moment?",
    "mould-risk-monitor": "Tell me about the last mould or damp problem in one of your flats: how did it start, who noticed, and how was the blame settled?",
    "smiley-terminal": "How do you find out today whether the people using this building are satisfied with cleaning or service, and what did that cost you last year?",
    "club-scoreboard": "Walk me through how the score is shown at your home games today, and what happened the last time it went wrong.",
    "fire-door-watch": "How do you know right now which fire doors in your building are propped open, and what did your last inspection report say about them?",
    "hallway-transit-board": "Tell me about this morning: how did you decide when to leave for the tram or train, and how often do you miss one?",
    "meter-eye": "How do you read your gas, water or electricity meter today, and what do you do with the number?",
    "sg-ready-price-switch": "Does your heat pump react to electricity prices or solar surplus today, and if not, what have you tried?",
    "shop-window-epaper-signs": "How did you last change the prices or the promotion in your shop window, and how long did it take?",
    "loop-logger-4-20ma": "Tell me about a 4–20 mA sensor on site that nobody logs today: why is it not connected, and what would you do with the data?",
    "balance-kit": "Walk me through your last hydronic balancing job: how long it took, what you measured, and how you proved it was done.",
    "build-a-radio-kit": "What did your students build last year with their own hands, how did you pay for the kits, and what went wrong?",
    "classroom-geiger-kit": "How do you teach radioactivity today, what equipment do you have for it, and when did you last use it?",
    "fruiting-chamber-controller": "Tell me about your last failed flush: what do you think went wrong with humidity, CO2 or temperature, and how would you have known earlier?",
    "half-keyboard": "How do you type today, what have you tried, and what made you abandon the last thing you tried?",
    "hay-spear": "Have you ever had a bale heat up on you? How do you check your stack today, and how often?",
    "isolated-interface-kit": "Tell me about the last time a serial link to a machine damaged a laptop or a port, or behaved strangely on site.",
    "nfc-voice-labels": "How do you tell your tins, medication or frozen meals apart today, and what happens when the labelling fails?",
    "one-knob-radio": "How does your parent listen to music or the radio today, and when did it last stop working for them?",
    "accessible-midi-instrument": "Tell me about the last lesson or session where an instrument did not fit the player: what did you use instead?",
    "sip-coaster": "How do you know today whether your parent or resident drank enough, and what happened the last time they did not?",
    "touchless-switch-module": "Tell me about the last product where you added a touchless or gesture control: who supplied the module, what did it cost, and what was wrong with it?",
    "trap-check": "How many trap and bait points does a technician check on a normal day, and how many of those visits find nothing?",
    "uvb-lamp-checker": "How do you decide when to replace your UVB bulb, and have you ever had an animal get sick that you later linked to the lamp?",
    "bedroom-audit-box": "Tell me about the last time you slept badly in a rental or hotel room: what did you suspect, and could you prove it?",
    "club-timing-gates": "How do you time sprints or laps at training today, and what do you do with the times afterwards?",
    "haccp-fridge-logger": "Walk me through your fridge temperature log: who writes it, when, and what happened at your last inspection?",
    "modbus-pocket-analyser": "Tell me about your last Modbus commissioning problem: what tool did you use to find it, and how long did it take?",
    "trail-talker": "How do visitors get information along your trail or site today, and what is broken, vandalised or out of date right now?",
    "workshop-dust-sentinel": "How do you know whether your dust extraction is actually working at the machine you are using, and when did you last check?",
    "cell-grader": "Tell me about your last batch of harvested cells: how did you grade them, how long did it take, and how many did you throw away later?",
    "control-theory-balance-kit": "How do you teach feedback control today: what do students touch with their hands, and what does that lab cost you?",
    "farm-shop-self-checkout": "What happens in your shop when nobody is at the till, and how much do you think you lose or miss because of it?",
    "frost-sentinel": "Tell me about your last frost night: how did you find out it was happening, and what did you lose?",
    "heat-pump-cop-lite": "Do you know what your heat pump's real efficiency was last month, and what have you tried to find out?",
    "pack-rebuilder-spot-welder": "Walk me through the last pack you rebuilt: what did you weld with, and what went wrong?",
    "school-scope": "What do your students use to look at a signal today, how many of those do you have working, and who repairs them?",
    "sound-to-light-alert": "How do you notice the doorbell, a smoke alarm or a crying child at night today, and what have you tried that did not work?",
    "switchboard-hotspot-watch": "When did you last have an overheating connection in a distribution board, how was it found, and what did it cost?",
    "vibration-health-sticker": "Tell me about the last motor or pump that failed unexpectedly: what did it cost you, and what had anyone measured on it before?",
    "footfall-counter": "How do you know how many people came into the shop yesterday, and what would you change if you knew the number per hour?",
    "haptic-setpoint-knob": "What do you adjust most often in your home automation, and how annoying is doing it from a phone?",
    "trinkwasser-logger": "How do you document hot-water temperatures for legionella compliance today, and what did it cost last year in time or fines?",
    "makerspace-soldering-station": "Tell me about the soldering stations in your space: how many are broken right now, and what killed them?",
    "motion-control-slider": "Tell me about the last shot where you wanted repeatable camera movement: what did you use, what did it cost, and why did you not buy a slider?",
    "new-flat-air-check": "When you last moved into a flat or renovated, what did you worry about in the air, and what did you do about it?",
    "quiet-guardian": "How do you know today that your parent got up this morning, and what did you do the last time you could not reach them?",
    "ros-trainer": "What robot do your students run ROS on today, how long does one group take to get it working, and what breaks?",
    "offline-ai-docent": "How do visitors ask questions in your galleries today, and what do you know about the questions they do not ask the staff?",
    "dark-sky-meter": "How did you last measure the sky at your observing site or in your municipality, with what, and who asked for the number?",
    "classroom-noise-light": "How loud does it get in your rooms on a bad day, how do you know, and what did you do about it last time?",
    "cue-light-system": "Walk me through how cues were called at your last show and what went wrong.",
    "village-stop-display": "Which of your stops have any passenger information today, what did it cost per stop, and do your operators broadcast live positions?",
    "oil-tank-eye": "How do you check your tank today, how often, and when did you last run low unexpectedly?",
    "room-door-sign": "How do people find a free room in your office today, and what happened the last time two groups wanted the same one?",
    "kiln-mind": "Tell me about your kiln: how do you set a firing, how do you know it is done, and what was your last ruined firing?",
    "vitrine-log": "What did the last lender ask you for about the climate, and how did you produce it?",
    "tree-thirst-sensor": "How does your crew decide which young trees get watered this week, and how many did you lose last summer?",
    "machine-access-box": "How do you control who uses the dangerous machines today, and what happened the last time someone untrained used one?",
    "hall-heat-scheduler": "Who sets the hall heating, when was it last changed, and what did heating cost you last winter?",
    "shared-laundry-notifier": "How do residents find out whether a machine is free, and what do they complain about to you?",
    "stream-level-gauge": "Tell me about the last time the stream flooded: how did you find out, and how early could you have known?",
    "emergency-light-logger": "How do you test and log the emergency lighting today, how long does a round take, and what did the last inspection say about the log?",
    "tool-check-wand": "Tell me about the last tool that went missing from a van: when did you notice, what did it cost, and how do you know what is in each van today?",
    "backstage-relay": "How do the dressing rooms hear the show and the calls today, and what have you improvised that failed?",
    "pollinator-counter": "How do you count pollinators or insects on your site today, who does it, and what do you do with the counts?",
    # round 2 (gongban-inventor, 17 Nov 2026). Radar/wellness ideas: ask about the situation, never a diagnosis.
    "basement-flood-sentinel": "Tell me about the last time water got into your cellar or boiler room: how did you find out, how long had it been there, and what did it cost?",
    "night-path-light": "When your parent gets up at night to go to the bathroom, how do they find their way, and has anything happened on that route in the dark?",
    "rain-barrel-irrigator": "How do you know how much water is left in your barrels or tank, and what did you do last summer when there was a watering ban or the barrel ran dry?",
    "aed-cabinet-monitor": "Who checks your defibrillator cabinet, how often, and what did they find the last time something was wrong with it?",
    "clubhouse-last-out-check": "Tell me about the last time the clubhouse was left with a door open, lights on or the heating running overnight: who found out, when, and what did it cost the club?",
    "isolated-bench-power-module": "Tell me about the last time a ground loop, a noisy supply or a mains-adjacent circuit got in the way of a measurement or a repair: what did you use, and what went wrong?",
    "pet-bowl-drink-watch": "How do you know today how much your cat or dog drinks, and has a change in drinking ever been the first thing you or your vet noticed?",
    "pump-station-alarm-relay": "Tell me about the last pump-pit callout where the high-level alarm went unnoticed: where was the alarm, why did nobody hear it, and what did the cleanup cost?",
    "queue-radar": "How do you notice today that the queue at the till is getting too long, and what happened the last time nobody did?",
    "radar-physics-kit": "How do you teach waves and the Doppler effect today, what do students measure with their own hands, and what equipment would you replace if you could?",
    "washroom-visit-counter": "How do you decide today when a washroom gets cleaned, and what happened the last time it was cleaned too late or for nothing?",
    "mmwave-radar-carrier": "Tell me about the last presence or radar sensor you wired up: which module, how long did it take to get working, and what was the fiddliest part?",
    "desk-occupancy-puck": "How do you know today how many of your booked desks are actually used, and what decision did you last make without that number?",
    "industrial-esp32-carrier": "Tell me about the last ESP32 or microcontroller project you put into a control cabinet: what did you build around it for power, isolation and RS-485, and what failed?",
    "isolated-can-ble-sniffer": "When did you last need to see what was on the CAN bus of a battery, inverter or heat pump on site, what did you connect with, and what went wrong?",
    "trough-level-radar": "How do you check the water troughs in your far fields today, how often do you drive out for it, and when did you last find one empty or overflowing?",
    "matter-ac-ir-bridge": "How do you control your air-conditioner or air-to-air heat pump today, and how often is it running in an empty room?",
    "matter-lab-kit": "What hardware do your students build connected-device projects on today, how close does it get to a real product, and what do employers say is missing?",
    "matter-presence-puck": "Tell me about the last time your lights or automations switched off while someone was still in the room: what sensor was it, and what did you try to fix it?",
    "night-door-prompt": "Tell me about the nights: has your relative tried to go out at night, how did you find out, and what do you do now so you can sleep?",
    "phone-booth-controller": "What do people complain about in your phone booths or pods, and how do you know how often they are actually used?",
    "sub-ghz-remote-analyser": "Tell me about the last 433 or 868 MHz remote, doorbell or sensor you had to figure out: what did you use to see what it was sending, and how long did it take?",
    "legacy-433-matter-bridge": "Which old radio-controlled sockets, doorbells or awnings do you still have in the house, and what have you tried to get them into your home automation?",
    "bathroom-fall-alert": "Your parent lives alone: what happens today if they slip in the bathroom and cannot get up, and have you tried anything (a pendant, a call routine) that did not stick?",
    "dog-alone-time-logger": "What do you know about what your dog does while you are out, how did you find out, and what have you tried to find out more?",
    "farmyard-help-button": "When your parent is working alone out in the garden, orchard or yard, how would anyone know if something happened, and what have you tried that did not reach that far?",
    "fire-tank-level": "How do you check the level of your fire-water tank today, who climbs up to do it, and what did the last inspection say?",
    "fitting-room-free-light": "How do your staff know which fitting rooms are free and how long people wait, and what happens on a busy Saturday?",
    "heat-meter-lorawan-reader": "How are the heat and water meters in your buildings read today, what does a reading round cost per flat, and what goes wrong with it?",
    "lora-class-network": "What have your students built that communicates beyond the classroom, and what do you use today to teach radio, range and antennas?",
    "meeting-room-no-show-sign": "How often are your meeting rooms booked but empty, how do you know, and what have you tried to stop it?",
    "voice-door-opener": "How do you get through your front door or gate today when you come home, and what happens on the days when your hands or arms are not up to it?",
    "pitch-floodlight-remote": "Who switches the pitch floodlights on and off today, how, and when were they last left burning all night?",
    "presence-infrared-heating": "Tell me about heating your hall, church or workshop last winter: who switches it on, when, and how often was it heating an empty room or cutting out with people still there?",
    "proofing-cabinet-controller": "Tell me about your last ruined batch in the proofer or retarder: what went wrong with temperature, humidity or timing, and how would you have known earlier?",
    "party-noise-guard": "Tell me about the last noise complaint or party in one of your rentals: how did you find out, how late, and what did it cost you?",
    "refill-station-level": "How do you know today which of your refill containers are running low, how often do you check, and when did a product last run out before the delivery came?",
    "room-ready-radar": "How does housekeeping know today whether a guest is in the room, and how many knocks on occupied rooms or wasted trips happen in a normal day?",
    "shed-guard-radar": "Tell me about the last break-in at your shed, allotment or boat: when did you find out, what was taken, and what have you tried since?",
    "hive-scale-lora": "How do you know today what is happening inside a hive without opening it, and when did you last lose a colony or a swarm you wish you had seen coming?",
    "heat-pump-modbus-matter": "How does your heat pump talk to the rest of your home automation today, and what have you tried to get local control without the maker's cloud?",
    "sleep-rhythm-bedside": "How do you keep track of how you (or a relative) sleep today, and what made you stop using the last tracker or app you tried?",
    "thread-switch-insert": "Tell me about the last light you wanted to automate: why did or didn't you replace the switch, and what put you off the smart switches you looked at?",
    "air-gesture-remote": "Tell me about the people you work with who cannot use a normal remote or a voice assistant: what do they use today to control the TV, lights or a call button, and where does it fail?",
    "eu-brand-pet-feeder-camera": "Has your brand looked at selling a connected feeder or other device, and what stopped you or went wrong when you tried?",
    "field-edge-wildlife-alarm": "Tell me about the last night wild boar or deer got into a field: when did you find out, what did it cost, and what have you tried to keep them out?",
    "hotel-voice-panel": "What do guests struggle with in your rooms (lights, heating, the TV, wake-up calls), and what do they ask the front desk for that a switch could have done?",
    "offline-voice-wall-switch": "How do you switch and dim lights today when your hands are full, and what made you decide against a cloud voice speaker, if you did?",
    "powerline-outbuilding-meter": "How do you know what your garden house, sauna, workshop or stable uses in electricity today, and how is the power for it shared or billed?",
    "channel-sounding-wayfinding": "Tell me about the last time you had to find a specific door, lift or accessible toilet in a public building you did not know: what did you rely on, and where did it fail?",
}


KEEP_CAP = {"Dutch", "German", "German,", "EU", "European", "HVAC", "HVAC,", "Deaf"}


def short_audience(idea):
    """First clause of the audience line, without parentheticals, lower-cased unless it starts with a proper noun."""
    a = idea["audience"].split(";")[0]
    a = re.sub(r"\s*\([^)]*\)", "", a).strip().rstrip(".")
    first = a.split()[0]
    return a if first in KEEP_CAP or first.isupper() else a[0].lower() + a[1:]


def segment(idea):
    tags = set(idea["tags"])
    if "b2b" in tags and "consumer" not in tags:
        return "b2b"
    if "consumer" in tags and "b2b" not in tags:
        return "consumer"
    return "mixed"


def problem_bullet(md):
    m = re.search(r"^- \*\*Problem:\*\*\s*(.+)$", md, re.M)
    return m.group(1).strip() if m else ""


def price(idea):
    p = idea["price_eur_est"]
    return f"€{p}" if not str(p).startswith("€") else str(p)


def section_md(idea, md):
    seg = segment(idea)
    title, pitch = idea["title"], idea["pitch"].rstrip(".")
    kq = idea["kill_question"]
    aud = idea["audience"].rstrip(".")
    prob = problem_bullet(md)
    where = WHERE.get(idea["slug"], [])
    L = []
    L.append(f"**Do this before anything else in this pack: before the business plan, before you order a sample board, "
             f"and long before you e-mail a factory (section 5).** The classic first-time mistake is to source and build first "
             f"and find out later that nobody wanted it. Hardware mistakes are slow and expensive to undo; {CONVERSATIONS} conversations are cheap.")
    L.append("")
    corr = idea.get("market_correction")
    if corr:
        L.append(f"> **{corr['title']}.** {corr['text']}")
        L.append("")
    L.append("### The gate: this idea's kill question")
    L.append("")
    L.append(f"> {kq}")
    L.append("")
    if idea.get("kill_question_original"):
        L.append(f"*Revised after the external market check; the original question was: \"{idea['kill_question_original']}\"*")
        L.append("")
    if seg == "b2b":
        evidence = ("written answers from at least ten decision-makers who hold the budget, at least three of whom put something on paper: "
                    "a signed letter of intent, a paid pilot, or a dated purchase order for the first units")
    elif seg == "consumer":
        evidence = (f"a fake-door landing page that {short_audience(idea)} actually visited, with a measured conversion to a waitlist "
                    "or refundable deposit, plus the interview notes behind it")
    else:
        evidence = ("a measured conversion on a fake-door landing page for the consumer side and, for the business side, "
                    "at least three decision-makers who put something on paper: a letter of intent, a paid pilot or a purchase order")
    L.append(f"You pass this section when you can answer that question with evidence you collected yourself, not a guess: {evidence}. "
             f"Until then: no factory e-mail, no sample order, no firmware, no logo. If the answer is no, you have lost a few weeks and saved the rest.")
    L.append("")
    L.append("### Who you are looking for")
    L.append("")
    L.append(f"**The audience named in the idea:** {aud}.")
    if prob:
        L.append("")
        L.append(f"**The problem as the pack states it:** {prob}")
    L.append("")
    L.append("Talk to the people who have the problem *and* the people who pay; in B2B they are often not the same person, and the one who pays decides.")
    L.append("")
    L.append("### Where to find them")
    L.append("")
    if where:
        L.append("Communities and associations where this audience actually talks, as far as we know them in November 2026. Confirm each is still active and read its rules on self-promotion before posting; most allow a genuine question about a problem and ban a pitch.")
        L.append("")
        for cid in where:
            name, url, what = C[cid]
            L.append(f"- **{name}** · {url} — {what}.")
        L.append("")
    else:
        L.append("No community we are confident about is on file for this exact audience, so do not take a guess from a list: the methods below find them in a day.")
        L.append("")
    L.append("Beyond the named ones, the same four methods work for every idea on this site:")
    L.append("")
    L.append(f"- **Search for communities around the problem, not the product:** forums, Facebook groups, Discord servers and newsletters in your own country for the terms in the audience line above. Many of the best groups are national and in the local language; a Dutch or German group beats a global English one for an EU launch.")
    L.append("- **Trade associations and their regional meetings** for the B2B audiences: one meeting puts twenty buyers in a room, and the association newsletter will often run a short survey for a member.")
    L.append("- **LinkedIn:** search people by the job titles in the audience line, message ten a day with one question (not a pitch), and ask for twenty minutes. Expect one in five to say yes.")
    L.append("- **Your deposit list from the kill question** and anyone who replied to the fake door: those are the first interviews, not the last.")
    L.append("")
    L.append(f"### The plan: {CONVERSATIONS} conversations, then a fake door")
    L.append("")
    n = "ten budget-holders and ten users" if seg == "b2b" else ("twenty people from the audience line" if seg == "consumer" else "ten buyers from the business side and ten from the consumer side")
    L.append(f"1. **{CONVERSATIONS} real conversations** ({n}), fifteen minutes each, using the script below. Before writing a line of code or ordering a board. Write up each one the same day: the problem in their words, what they do today, what it costs them, what they said when you named the price.")
    L.append(f"2. **A fake door.** One page: the pitch as the headline, a rendered image or a photo of a cardboard mock-up, the price ({price(idea)}, the pack's estimate), and one button. "
             + ("For a business buyer the button is \"request a pilot\" that leads to a short form and a letter of intent." if seg == "b2b" else
                "For a consumer the button takes a refundable deposit or a waitlist e-mail; a deposit is worth ten e-mails." if seg == "consumer" else
                "Two buttons: a refundable deposit or waitlist for consumers, \"request a pilot\" for businesses."))
    L.append("3. **Send it** to everyone you interviewed and post it, with the problem question first, in the communities above. Run it for two to four weeks.")
    L.append("4. **Count** against the kill question. Then decide: go, change the idea, or stop.")
    L.append("")
    L.append("### Interview script (fifteen minutes, problem first)")
    L.append("")
    L.append("Ask, then be quiet. Do not describe the product until question 5; if you pitch first you will only hear politeness.")
    L.append("")
    L.append("```email")
    L.append(f"Thanks for the time. I am looking into how {short_audience(idea)} deal with [the problem in their words]; I have not built anything yet and I am trying to find out whether it is worth building.")
    L.append("")
    L.append(f"1. {PROBE.get(idea['slug'], 'Tell me about the last time this problem came up for you.')}")
    L.append("2. What do you do about it today, and what does that cost you in money or time per month?")
    L.append("3. What have you already tried or bought, and why did you stop using it?")
    L.append("4. If this went away tomorrow, what would change for you? (If the answer is \"not much\", you have your answer.)")
    L.append(f"5. [Only now describe it in one sentence:] {pitch}. On a scale of one to ten, how likely would you be to buy that at {price(idea)}, and what would make it a ten?")
    L.append("6. Who else should I talk to about this? (Ask for two names.)")
    L.append("")
    L.append("Close: \"If I build this, can I come back to you with a prototype?\" A yes with a calendar date is worth more than any compliment.")
    L.append("```")
    L.append("")
    L.append("### Pre-order / pilot message (forum post or direct message)")
    L.append("")
    L.append("```email")
    if seg == "b2b":
        L.append(f"Subject: {title}: looking for 3 pilot sites before we build it")
        L.append("")
        L.append(f"I am [your name], [your background]. We are considering building a {title}: {pitch}. Before we spend money on tooling I want to find out whether this solves a real problem for {short_audience(idea)}.")
        L.append("")
        L.append(f"If it would, I am looking for three pilot customers willing to sign a short letter of intent now and pay {price(idea)} per unit for the first batch, delivered in [month]. The LOI is non-binding on the price; it tells me the problem is real.")
        L.append("")
        L.append("Two questions, no pitch: how do you handle this today, and what would make you say no to the above? Twenty minutes on a call this week, or a reply here, both help.")
    else:
        L.append(f"Subject: {title}: would you pay {price(idea)} for this? Looking for 20 people to tell me I am wrong")
        L.append("")
        L.append(f"I am [your name], [your background]. I am considering building a {title}: {pitch}. Before I order a single part I want to know whether this is a real problem for people like you or only in my head.")
        L.append("")
        L.append(f"If you would want one at {price(idea)}, the page at [link] takes a fully refundable €[10–20] deposit (or a waitlist e-mail if you prefer); if twenty people do that, I build it, if not, everyone gets their money back and I have learned something.")
        L.append("")
        L.append("Either way, two questions: how do you deal with this today, and what would make you say no? Honest answers are worth more to me than deposits.")
    L.append("```")
    L.append("")
    L.append("### Reading the signal")
    L.append("")
    L.append("| Real signal | False positive |")
    L.append("|---|---|")
    L.append("| A refundable deposit, a signed LOI, a paid pilot, a calendar invite for the prototype | \"Sounds cool\", \"I would totally buy that\", likes and upvotes |")
    L.append("| They describe the problem unprompted and in detail, with numbers | They agree with your description of the problem |")
    L.append("| They have already paid for a workaround (a product, a service, their own time) | They have never tried anything and are not bothered |")
    L.append("| Landing-page conversion to deposit or form above the pack's pass mark, from cold traffic | Conversion from friends, family and your own network |")
    L.append("| A named budget and a named decision-maker (B2B) | An enthusiastic user who cannot buy |")
    L.append("")
    L.append("### Go / no-go")
    L.append("")
    L.append(f"- **Go to section 3 (business plan) and section 4 (start kit)** when the kill question above is met by your own numbers, you have {CONVERSATIONS} written-up conversations, and at least one real signal from the left column per segment you plan to sell to. Only then does section 5 (Who to contact) apply.")
    L.append("- **Change the idea** when the problem is real but the price, the buyer or the form factor in the pitch is wrong: the interviews will tell you which. Rewrite the pitch and run the fake door again; this is normal and costs a week.")
    L.append("- **Stop** when the kill question fails on honest numbers, or when nobody you talked to has paid for a workaround. Pick another idea on this site; the boards in the start kit are not wasted, only unused.")
    L.append("")
    L.append("The full worksheet, with how to define the segment and run the fake door, is in the [playbook → validate demand](/playbook.html#validate).")
    return "\n".join(L) + "\n"


def patch_md(md, section, slug):
    block = f"{START}\n{section}{END}"
    if START in md and END in md:
        return md[:md.index(START)] + block + md[md.index(END) + len(END):]
    # one-time renumbering, highest first so nothing collides
    for old, new in (("## 5. Next steps", "## 6. Next steps"), ("## 4. Who to contact", "## 5. Who to contact"),
                     ("## 3. Start kit", "## 4. Start kit"), ("## 2. Business plan", "## 3. Business plan")):
        md = re.sub("^" + re.escape(old), new, md, count=1, flags=re.M)
    if slug == "tariff-lamp":
        md = md.replace("(math in §2)", "(math in §3)")
    m = re.search(r"^## 3\. Business plan", md, re.M)
    if not m:
        raise SystemExit(f"{slug}: no Business plan section to insert before")
    return md[:m.start()] + "## 2. Validate demand first\n\n" + block + "\n\n" + md[m.start():]


def patch_packs():
    # every packed idea (round 1 and 2) MUST have a WHERE and a PROBE entry, so the market check can't silently be missing.
    # WHERE may be an empty list on purpose (= generic search guidance only), but the key has to be there.
    ideas = [i for i in json.loads(IDEAS_JSON.read_text(encoding="utf-8"))["ideas"] if (PACK_DIR / f"{i['slug']}.md").exists()]
    missing_where = [i["slug"] for i in ideas if i["slug"] not in WHERE]
    missing_probe = [i["slug"] for i in ideas if i["slug"] not in PROBE]
    assert not missing_where, f"no WHERE entry (communities) for: {missing_where}"
    assert not missing_probe, f"no interview probe for: {missing_probe}"
    # round-2 probes must be questions (some round-1 probes are "Walk me through …" prompts; left as published)
    bad_probe = [i["slug"] for i in ideas if i.get("round") == 2 and not PROBE[i["slug"]].rstrip().endswith("?")]
    assert not bad_probe, f"probe does not end with '?': {bad_probe}"
    unpacked = sorted(set(WHERE) - {i["slug"] for i in ideas})
    generic = [i["slug"] for i in ideas if not WHERE[i["slug"]]]
    for slug, ids in WHERE.items():
        for cid in ids:
            assert cid in C, f"{slug}: unknown community id {cid}"
    n = 0
    for idea in ideas:
        path = PACK_DIR / f"{idea['slug']}.md"
        if not path.exists():
            continue
        md = path.read_text(encoding="utf-8")
        new = patch_md(md, section_md(idea, md), idea["slug"])
        if new != md:
            path.write_text(new, encoding="utf-8")
        n += 1
    # fixed pack order, checked on every pack
    order = ["1. Summary", "2. Validate demand first", "3. Business plan", "4. Start kit", "5. Who to contact", "6. Next steps"]
    for idea in ideas:
        heads = re.findall(r"^## (\d+\. .+?)\s*$", (PACK_DIR / f"{idea['slug']}.md").read_text(encoding="utf-8"), re.M)
        got = [h.split(" (")[0] for h in heads]
        assert len(got) == 6 and all(g.startswith(o) for g, o in zip(got, order)), f"{idea['slug']}: section order {got}"
    print(f"startpacks/: 'Validate demand first' in {n} packs as section 2; {len(ideas) - len(generic)} with named communities, "
          f"{len(generic)} with generic search guidance only{(' (' + ', '.join(generic) + ')') if generic else ''}"
          f"{('; WHERE entries without a pack: ' + ', '.join(unpacked)) if unpacked else ''}")


if __name__ == "__main__":
    patch_packs()
