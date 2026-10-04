# ChennaiFloodUndersight — the ELI10 walkthrough

**Draft v0.1 · 2026-10-03 · for your own understanding — iterate freely, then we publish the polished version**
Companion to `file REPORT.md` (the formal audit), `file MEDIA-CLAIMS.md`, `file DATA-CATALOGUE.md`, `file AUDIT-PLAN.md`. Every number here traces to those files.

---

## 1. The whole project in one paragraph

Chennai spent **₹107.2 crore** of public money — most of it World Bank loan money — on a "flood forecasting brain" that promises to tell you *which street will flood, three days early*. It went fully live in **October 2025**. What the public gets from it: **seven PDF files and a dashboard with dead gauges**. What we did: walked through the side door the system accidentally left open, copied **everything** (344 data layers, 1.7 million sensor readings), published it openly, and have been checking its homework ever since. This document explains every piece of that, in plain language.

---

## 2. The thing we're watching: what is RTFF & SDSS?

Think of Chennai's flood problem first. The city sits where rivers (Adyar, Cooum, Kosasthalaiyar), lakes, storm drains and the sea all meet. When the northeast monsoon misbehaves — like 2015, or Cyclone Michaung in 2023 (639 mm in one day at one gauge), or the December 2025 Ditwah aftermath (56 cm in three days on Ennore) — water comes from everywhere at once.

After 2015, the state decided to build a brain that would see all of it coming:

| What | Detail |
| --- | --- |
| Name | Real-Time Flood Forecasting & Spatial Decision Support System — **RTFF & SDSS** |
| Public face | "Chennai Flood Monitor" website, `chennaifloodmonitor.tn.gov.in` |
| Cost | **₹107.2 crore** (\~US$12.8M) |
| Coverage | **4,974 km²**, 5 districts (Chennai, Tiruvallur, Kancheepuram, Chengalpattu, Ranipet) |
| Senses | Rain gauges, weather stations, water-level recorders, gate sensors on lakes |
| Brains | 5 weather models fused with river/lake/drain/sea data → street-level flood predictions |
| Promise | Warnings **3 days ahead**, street by street, for places like Pulianthope, Velachery, Mambalam |
| Built by | Consultant JV **SECON (India) + JBA (UK)**, supervised by **IIT Madras** |
| Ran by | TNUIFSL (a state fund-manager company) on behalf of three government bodies |
| Live since | **October 2025** (pilot during the 2021 monsoon; "fully operational" Oct 2025) |

## The pitch is genuinely good. A city that floods every few years should absolutely have an early-warning brain. **We are not against the system. We are against not being able to check it.** உங்கள் சொத்து — this is public property; the public gets to see the report card.

## 2A. The history: how this machine came to be (1996 → today)

The flood brain didn't appear in 2025. It has a thirty-year backstory in three threads — the money, the science, and the website — and each thread explains something odd about the present.

**The money thread: a thirty-year pipe.** In 1996, Tamil Nadu set up the Tamil Nadu Urban Development Fund (TNUDF) — a public-private trust, part-government part-banks (ICICI, HDFC, IL&FS) — as the funnel for World Bank urban money. The Bank lent in waves: TNUDP I (late 1990s, which created TNUDF), TNUDP II, and TNUDP III (approved 2006, **$300 million**). Alongside the TNUDF loan stream, the Bank's projects created little "grant fund" side-pockets (Grant Fund I, II, III) for consultancies and studies. In **April 2015** — eight months before the Great Flood — the government consolidated those side-pockets into the **PDGF**, the grant shop from §6. So when the flood came and the state wanted to buy a forecasting brain, the pipe already existed: World Bank loan → TNUDF-era grant funds → PDGF → consultancies. The project was simply slotted into thirty years of plumbing.

**The disaster thread: December 2015.** The flood drowned the city (the government's final count: **421 deaths** between 28 Oct and 31 Dec 2015). After 2015, the state sanctioned RTFF & SDSS under the PDGF — the government's own portal says it plainly: sanctioned "to manage the frequent extreme floods occurrences in Chennai", funded by the World Bank. Early scope: **four river basins (Adyar, Cooum, Kosasthalaiyar, Kovalam), \~4,073 km²**, with an Araniar-basin expansion debated as early as March 2019 (pending "contract-rate variations with the World Bank"). The consultant JV (SECON of Bangalore + JBA of the UK) and IIT Madras as technical supervisor come from this phase.

**The science thread: IIT-M was doing the research long before the ribbon-cutting.** A rough sequence:

- IIT-M civil engineering (Prof. Balaji Narasimhan's group and colleagues) built Chennai flood models and a **4-km-resolution weather model with 7 ensemble members**, made for this basin.
- **Nov 2021, Cyclone Nivar:** IIT-M researchers (with IIT Bombay, Anna University, NCCR) went *out into the storm* to collect real flood data for calibrating the pilot.
- **2021–2024:** \~2,000 Chennai residents logged flood depths through an IIT-M citizen-science portal — data that fed model validation and now feeds RTFF & SDSS.
- **June 2021:** the state formalised an Advisory Committee for Flood Management (IIT-M, IIT-B, NRSC, Anna University, NDMA-linked experts).
- **July 2024:** the system's own scientific paper appears in *Current Science* (vol. 127) — "Setting up and operationalization of the RTFF–SDSS for Chennai" — documenting that it was **piloted in NEM 2021 and operationalized for NEM 2022 and 2023**.

So the academic side is real and laudable — real models, real fieldwork, real citizen data. The research existed; the *public accountability layer* never did.

**The website thread: one brain, three faces, two mirrors.** The system's first public face was `chennaifloodsdss.in` — footer: "Developed and Maintained by SECON & JBA" — live by the 2021 pilot. That's the site we mirror-backed in **Dec 2023** (34,050 gauge readings, incl. the full Michaung storm). In 2025 the state moved the system to a new government domain, `chennaifloodmonitor.tn.gov.in` ("Chennai Flood Monitor"), and the old site simply **died** — last archived copy Aug 2025, now an unresolvable address. Same system, same AboutUs text (typo included), new URL, no redirect, no notice. This is exactly the pattern F9 flags: institutional memory evaporates at every URL change — which is why we re-mirror every year.

**The cost thread, and the creep nobody mentions.** When the press reported the system as newly real in **Nov 2022, the project cost was ₹71 crore**. By the Oct 2025 launch coverage it was **₹107.2 crore**. That's **+51% in three years** — sensors added, scope grown to \~4,974 km² — and there is no public paper trail for the increase. Not an accusation; an accounting gap. It's the same gap F10 flags, now with two datapoints.

**The compressed timeline:**

| Year | What happened |
| --- | --- |
| 1996 | TNUDF created (World-Bank-aided public-private trust) — the pipe is born |
| 2006 | TNUDP III approved — $300M; Grant Fund side-pockets created |
| Apr 2015 | PDGF created at TNUIFSL (merging TNUDP-III/KfW/JBIC grant funds) |
| Dec 2015 | The Great Flood — 421 official deaths; RTFF & SDSS conceived after this |
| 2016–18 | Project sanctioned under PDGF; SECON–JBA JV + IIT-M supervision; 4 basins, \~4,073 km² |
| Mar 2019 | First press on scope/expansion (Araniar basin debate) |
| Feb 2021 | Ward-by-ward basemap surveys (sheets marked "restricted publication") |
| Jun 2021 | Advisory Committee for Flood Management formed |
| Nov 2021 | **Pilot during NEM 2021** — IIT-M collects data inside Cyclone Nivar; old site live |
| Nov 2022 | "Becomes a reality" — reported cost **₹71 crore**; operationalized NEM 2022 |
| 2023 | Operationalized NEM 2023; Dec: **our first mirror** of the old site |
| Jul 2024 | *Current Science* paper documents the build |
| Aug 2025 | Old site dies (last archive 2025-08-31) |
| Oct 2025 | New portal + "fully operational"; cost now **₹107.2 crore**; 7 bulletins issued |
| Dec 2025 | Ditwah flood — great recorder, unverifiable forecaster |
| Sep–Oct 2026 | Our census + open-data release + audits; IFMC announced with the same street-level 3-day promise |

One-paragraph takeaway: **the research was excellent, the money pipe was old, the websites were disposable, and the accountability was never built.** That last clause is the whole project.

---

---

## 3. How we got in (the lawful part, explained)

**The front door:** the public website. It gives you a dashboard and seven image-only PDF "bulletins". No raw data, no license, no API documentation.

**The side door:** like almost all map-based government sites, the pretty dashboard is just a skin over a standard map-data server (a "GeoServer"). The website itself asks this server for data hundreds of times a second. We asked the server the **same questions the website asks**, with no password, no bypassing, nothing hidden. It answered — **343 of its 344 layers**.

Analogy: the government built a museum, locked the front gate, and left the delivery entrance wide open. We didn't pick any lock. We walked in the open delivery door and photographed every exhibit.

What we did **not** do: no logins bypassed, no scraping of personal data (we scrubbed officer names, SIM numbers, citizen usernames), no writes to their systems. Read-only, same as a browser.

---

## 4. What we took home (the mirror)

We copied all of it on **29 Sept 2026** and published it openly. Five public boxes:

1. `chennai-flood-monitor-transactions` — the heartbeat data. 662,904 rain-gauge readings (back to 1976), 669,147 weather-station readings, 385,950 water-level readings (2021→Aug 2026), plus 33 "who owns which sensor" registers.
2. `chennaidss-gis-layers` — 181 map layers: wards, drains, rivers, 6,724 lakes and tanks, land use, the model's own working files.
3. `chennai-flood-history` — the memory: 2015 flood maps (4,001 polygons), 2005 flood maps, flood hotspots, the ward-depth table.
4. `chennai-flood-bulletins` — all 7 official bulletins. The system's *complete* public output to date.
5. `chennai-rain-gauges` — the predecessor system's data (34,050 readings incl. the full Michaung flood), rescued before that website died in 2025.

Why publish? Two reasons. First, **public data deserves a public home**. Second — and this is the part to remember — *the predecessor system's data would be gone forever if we hadn't copied it in 2023.* The website is now literally unreachable. Mirroring is how public memory survives URL changes.

---

## 5. The ten findings (the heart of it)

Each finding is numbered in the formal report. Here's each one, plainly:

**F1 — The data is open by accident, not on purpose.**
Nobody at the government decided to publish 343 open layers. It just… leaked through the website's plumbing. That's how we got in — and also why it's fragile. Tomorrow someone "fixes" the leak and 12 years of data goes dark again. No license, no promise it stays.

**F2 — The famous gauges are dead on the public dashboard.**
On the day we looked: 38 rain stations shown, only **22 reporting fresh data**. The others, including **Nungambakkam** — THE reference rain gauge of Chennai, the one every flood story since 2015 is measured against — were **frozen at 10 May 2025**. Sixteen months of nothing. Analogy: your speedometer shows 60 km/h because it froze there last year.

**F3 — There are two pipes, and the open one is stale.**
The feed any citizen or researcher can read programmatically stops in **January 2022** (with 3 stragglers). The dashboard shows 2026 numbers through a *different* pipe. So even a diligent person reading the "open" data gets a **four-year-old city**.

**F4 — The "ward-level forecast" is a photo, not a camera.**
The public map layer of "how deep will water get in your ward" carries the date **11 Aug 2021**. Every ward. It is a snapshot from five monsoons ago. The real forecasts exist — but only as PDF pictures during storms, not as data.

**F5 — There is no report card. The ₹107 crore question.**
A forecasting system should keep every forecast it ever made, so anyone can ask: "on 3 Dec 2025, what did it say Velachery's flood depth would be? What actually happened?" This system publishes **no forecast archive**. So "how good is it?" — the entire reason it was bought — has **no public answer**. This is the single most important finding.

**F6 — The alarm bell barely rings.**
The system has an alerts feed. It has returned **zero alerts, every time we've checked**. Real warnings go out via press notes and one government app. If you don't have that app open at the right moment, the system has no other way to reach you. Alerts-in-one-app = alert inequity.

**F7 — The sensors need a doctor.**
Our copy shows temperature readings of **−6.2 °C** in Madhavaram and **−18 °C** in Kattupakkam (Chennai has never recorded below \~13 °C), a bridge sensor reading "26 m" on a 7-m-deep river, and stations named `dc`. Small things. Together: nobody is checking the checking machine.

**F8 — But it worked as a tape recorder in December 2025.**
During the Ditwah floods, the system *recorded* reality well: citizen distress reports (level 6 of 6 at Puzhal), bridge sensors peaking exactly when The Hindu reported the Ennore disaster. Three independent data streams agree. **But a recorder is not a forecaster.** Whether it *predicted* anything before the water came — F5 says nobody can check.

**F9 — The previous system died and took its data with it.**
`chennaifloodsdss.in` — the pre-2025 flood portal — is now a dead web address. If we hadn't copied its data in Dec 2023, Michaung's records would be gone. Lesson institutionalised: **we re-mirror every year**, and this project is built to repeat.

**F10 — Nobody has ever audited the money.**
₹107.2 crore ÷ 4,974 km² = **₹2.16 lakh per km²**, or **₹53.6 lakh per ward**. No sanction order public, no contract values public, no O&M budget public. The station registers we copied *do* name maintenance vendors and contract end-dates — that's the thread an RTI pulls.

---

## 6. The money story (who actually paid, and on what terms)

The website says "funded by the World Bank". Here's what actually happens, layer by layer:

1. **The World Bank lends money — but only to countries, never to states or cities.** So it lends to the Government of India, which passes it to Tamil Nadu. Tamil Nadu carries the debt in foreign currency, for **decades**. Recent TN loans run **20–32 years** (the current $300M urban program: 32-year maturity, 7-year grace).
2. **Tamil Nadu runs a "grant shop"** called the Project Development Grant Fund (PDGF) — a pot of money managed by TNUIFSL that hands out grants for studies and consultancies. Its corpus comes from those same foreign-loan budget lines. So loan money walks in one door and comes out the other wearing a "grant" costume.
3. **The flood system was bought through that grant shop.** Which means: at the project level nobody "owes" anything, but one layer up, every rupee is sovereign debt with a 32-year tail.

The kicker numbers: in 2023-24 PDGF received **₹35.23 crore** and paid out **₹52.64 crore** — for *everything*. The flood system cost **₹107.2 crore** — roughly **two years of the entire fund's output**. It is almost certainly the biggest thing this grant fund has ever bought. And the World Bank's *current* program is still paying for this system's aftercare (its 2024 procurement plans list "handholding supervision" and satellite-survey work for exactly this project).

The sharpest point: the Bank's new program pays out **only against independently verified results**. Verification could have been free — written into the payment terms. Instead, the one thing consumers need (proof the forecasts work) is the one thing that was never made verifiable.

---

## 7. The hype vs. the record (what the media says)

We logged **every news mention** of the system's success (`file MEDIA-CLAIMS.md`, 27 entries). Three patterns:

1. **Every claim is in future tense.** "Can save lives", "will minimise damage", "is expected to reduce loss". Twenty-seven references. **Zero** that point to a checked, dated outcome. The future tense is where success claims go to avoid verification.
2. **During the actual flood — silence.** In Dec 2025, when Ditwah's remnants actually flooded Chennai, every news credit went to the weather office, the water commission, collectors, and the city corporation's separate alarm system. **Not one article** credited the ₹107-crore forecasting system with a single warning that reached anyone.
3. **The promise got re-announced in 2026.** In Oct 2026 the state unveiled a new "Integrated Flood Management Centre" — which, the papers reported, "will predict street-level flooding three days before it happens". That is *exactly* what the 2025 launch promised. Same promise, new name, one year after "fully operational". Either an upgrade or a rebrand — and nothing public tells us which.

Also fun: the government's own website misspells its funding scheme's name ("Project Development **Grand** Fund"). Small, but it's the same sloppiness fingerprint as the frozen gauges and the PDF-only bulletins.

---

## 8. The data health check (the catalogue)

`file DATA-CATALOGUE.md` answers: *did we get everything, and how fresh is each piece?*

- **Coverage:** 344 layers existed; 26 were empty at the source; 5 broke; 1 was unreachable; **312 are in our archive** (310 whole, 2 as samples, flagged). Re-checked the server on 3 Oct 2026: still exactly 344 layers, nothing added or removed. Nothing has slipped past us.
- **Freshness has three clocks, and people always confuse them:**
  1. *Observation freshness* — how new is the data inside the system? (Answer: mixed. Water levels to Aug 2026; rain gauges stopped Feb 2026; the map "forecast" stopped in 2021.)
  2. *Mirror freshness* — when did WE copy it? (29 Sept 2026.)
  3. *Coverage freshness* — has anything new appeared since? (Checked 3 Oct: no.)
- **Known gaps, honestly listed:** the live 7-day rain window (our query errored — recapturable), two big tables sampled rather than full, the 5 broken layers. Each gap has a "how to recover it" note.

---

## 9. "Is what you did even legal?" (yes, and here's the short version)

- **Facts aren't copyrightable.** Rainfall numbers, water levels, coordinates — machines emit them; there's no creative author to own. (Indian and US law agree on this.)
- **Government policy says this data should be open anyway.** India's 2012 open-data policy (NDSAP) makes non-sensitive government data open *by default*. A flood-warning system's telemetry is the textbook case.
- **The PDF bulletins** do have copyright (government's), but quoting and reporting on them for the public is explicitly protected "fair dealing" under §52 of the Copyright Act.
- **Our posture:** we claim no rights over the facts; we put CC BY 4.0 on our own arrangements; everything is attributed; and if the government objects to any specific file, we take it down without a fight. We're a mirror, not a rival.

---

## 10. The ongoing audit (what happens next)

This isn't a one-time exposé — it's a monitoring beat, like a beat reporter covers a beat:

- **Monthly:** automatic probes — are the gauges alive? Is the alert feed still empty?
- **Every storm (activation):** a **forecast scorecard within 7 days** — what did the system say, what actually happened, published as data. This is how F5 gets answered going forward, activation by activation.
- **Quarterly:** the "RTFF-DSS Ledger" — money vs. maintenance vs. stations actually alive.
- **Yearly:** full re-mirror (the Dec-2023 lesson).
- **Two watches:** the AMC maintenance-contract calendar (who maintains what until when — our copied registers hold the expiry dates), and the new IFMC (is it the same promise re-sold, or a real upgrade?).
- **RTI queue:** the sanction order, the SECON–JBA contract value, the PDGF spending statements that name this project.

**The five asks** (all policy, none need new money): publish a data license; archive every forecast; fix or retire the dead gauges; open the alert feed beyond one app; adopt the open-data policy formally.

---

## 11. Open questions (things we genuinely don't know yet)

1. Was the Dec-2025 silence (§7.2) because the system *didn't* forecast, or because nobody told the media it did? Unknowable until forecasts are archived — or an RTI lands.
2. Is the 2026 IFMC the RTFF's successor, its expansion, or its rebrand?
3. What did the SECON–JBA contract actually cost, and how is the ₹107.2 crore split between software, sensors, and surveys?
4. Who maintains the sensors after the current AMC contracts expire — and is anyone paying for it?
5. Will NEM 2026 produce the first ever public forecast scorecard?

---

*Draft for internal iteration — not published, not committed to the repo yet. Once you've marked it up, the public version ships as a themed page (masthead mode, per `file DESIGN.md` tokens) linked from the project hub.*