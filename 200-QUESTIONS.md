# 200 Questions — a Chennai-ite asks about the flood-forecasting machine

**Companion to** `file REPORT.md` · `file ELI10.md` · `file DATA-CATALOGUE.md` · `file MEDIA-CLAIMS.md` · Compiled 2026-10-03.

**The premise:** ₹107.2 crore of public money bought a machine that promises to tell you which street will flood, three days early. You own it. Here are the 200 questions you have a right to ask — with the best answer we have today. **Status legend:** ✅ answered from verified evidence (pointers to our reports/data) · 🟡 partial · ❌ unknown — RTI target or standing watch.

---

## A. The system in plain terms

**Q1. What exactly is this ₹107-crore thing I keep hearing about?**
✅ RTFF & SDSS — a sensor network + weather models + maps fused into a dashboard that promises street-level flood forecasts 72 hours ahead. REPORT §1–2.

**Q2. Who runs it day to day?**
✅ The Hydro-Modelling Control Room at the State EOC (Ezhilagam) under the Commissionerate of Revenue Administration / TNDRRA; consultant SECON–JBA runs modelling during activations; Flood Monitoring Centres sit in district collectorates. CFM AboutUs.

**Q3. Where is it physically?**
✅ HMCR at SEOC Ezhilagam; FMCs at GCC, Kancheepuram, Tiruvallur, Chengalpattu, Ranipet collectorates; a disaster-recovery centre proposed at WRD Chepauk. CFM AboutUs.

**Q4. When did it start?**
✅ Conceived after the 2015 flood; piloted NEM 2021; "operationalized" NEM 2022 and 2023 (Current Science, Jul 2024); declared "fully operational" Oct 2025.

**Q5. Is it really India's first?**
🟡 Billed "first fully operational comprehensive urban FF-DSS" in launch coverage (graded B/C in our ledger). Mumbai's CFLOWS predates it in research; "first" depends on definitions nobody has fixed.

**Q6. Does it predict floods or just record them?**
✅ Design says predict (72-hour street-level). Evidence says it *records* well (F8) and predicting is publicly unverifiable (F5). Both halves verified in our mirror.

**Q7. Which areas does it cover?**
✅ 4,974 km² across Chennai, Tiruvallur, Kancheepuram, Chengalpattu, Ranipet — the Adyar, Cooum, Kosasthalaiyar and Kovalam basins.

**Q8. Is my district inside?**
✅ If you're in those five districts, yes on paper. Exact per-ward sensor coverage: check the station registries in our `chennai-flood-monitor-transactions` dataset.

**Q9. Who built it?**
✅ SECON Private Ltd (Bangalore) + JBA Consulting (UK) as a JV; IIT Madras provided technical supervision; TNUIFSL managed the money.

**Q10. Chennai flooded in 2005, 2015, 2021, 2023 — why did the brain only arrive in 2025?**
✅ The 2015 flood created the political mandate and the World Bank money pipe; the build took ~5 years; press calls it "operational" only from Oct 2025. History: ELI10 §2A.

---

## B. Money: sanction, cost and the creep

**Q11. How much did it cost, finally?**
✅ ₹107.2 crore — press figure at launch (ledger row 10, graded C).

**Q12. Was that always the price?**
✅ No. Nov 2022 press reported **₹71 crore**; Oct 2025 launch reported ₹107.2 crore — **+51% in three years**, no public revision order (ledger row 22).

**Q13. Where can I read the sanction order?**
❌ Not published anywhere we can find. **RTI target #1:** WRD / CRA / Finance Dept for the G.O. sanctioning RTFF & SDSS under PDGF.

**Q14. Is it grant money or loan money?**
✅ Both, layered: World Bank *loan* to GoI→GoTN, repackaged as PDGF *grant* for consultancies (REPORT §5).

**Q15. Who repays the World Bank?**
✅ GoTN, via GoI, in hard currency — FX risk on the state budget, 20–32-year maturities observed in the TN portfolio.

**Q16. How does ₹107.2 cr split between software, sensors, surveys, IIT-M?**
❌ No public split. **RTI target:** SECON–JBA contract schedules + PDGF utilisation certificates.

**Q17. What is PDGF in one line?**
✅ The government's own "grant shop" at TNUIFSL — a non-lapsable technical-assistance fund fed by World Bank/KfW/JICA/ADB project lines, operational 1 Apr 2015.

**Q18. How big is PDGF next to this one project?**
✅ PDGF disbursed ₹52.64 cr in 2023-24 — *across all assignments*. RTFF & SDSS cost ~2 years of the entire fund's output.

**Q19. Is the World Bank still paying for it?**
✅ Yes — TNCRUDP (P179189) procurement plans (Dec 2023, Dec 2024) list RTFF "handholding supervision" ($0.10M) and satellite DEM/DSM work ($0.36M).

**Q20. Was there competitive bidding for the consultant?**
🟡 TNUIFSL uses QCBS/direct-selection routes; the actual RTFF award method and bids are not public. **RTI target:** TNUIFSL tender file.

**Q21. What's the annual operations budget?**
❌ Never published. No O&M line exists publicly — a headline gap (F10).

**Q22. What does it cost per km², per ward?**
✅ ₹2.16 lakh/km²; ₹53.6 lakh per ward. Whether that's good value depends on verification — which doesn't exist (F5).

**Q23. Is the money spent, or still flowing?**
🟡 Build-phase money spent (₹107.2 cr claim); aftercare money still flowing via TNCRUDP IPF-TA assignments.

**Q24. Who can audit this spend?**
✅ CAG can, on its own initiative or on demand; no CAG report on this line is public. **Ask:** include RTFF & SDSS in a performance audit.

---

## C. The World Bank and the terms of lending

**Q25. Does the World Bank lend to Chennai directly?**
✅ No — IBRD lends only to sovereign governments. Chennai's system is financed through GoI→GoTN chains.

**Q26. What interest rate did Tamil Nadu pay?**
🟡 IBRD pricing is benchmark-plus-spread with fees; the specific rate for the PDGF-feeding projects isn't published at this layer. Loan agreements (public at WB) carry it.

**Q27. How long does repayment take?**
✅ Observed TN instruments: 32-yr maturity/7-yr grace (TNCRUDP 2023), 23-yr/6.5-yr (SHORE 2025), 20-yr/3.5-yr (housing DPLs). Your flood brain sits on decades of sovereign debt.

**Q28. What is "Program-for-Results"?**
✅ A WB instrument that disburses only against independently verified program results — verification is a payment condition.

**Q29. Does the current program verify forecast accuracy as a result?**
❌ Nothing public shows RTFF performance indicators in the TNCRUDP results framework. **RTI/watch:** the PforR DLR schedule and ISRs.

**Q30. Can citizens read the loan agreement?**
✅ World Bank loan agreements and DLR schedules are published on its website — a no-RTI ask once signed.

**Q31. Has the Bank funded TN flood/urban work before?**
✅ Yes — TNUDP I–III (1990s–2006, incl. $300M TNUDP III), TN & Puducherry Coastal DRR ($236M, 2013), TNSUDP ($400M IBRD, 2015), now TNCRUDP ($300M, 2023).

**Q32. What is the Inspection Panel?**
✅ The World Bank's independent accountability mechanism — affected people can request investigation of WB-financed projects.

**Q33. What else has PDGF bought over the years?**
🟡 Annual utilisation statements exist at TNUIFSL (₹35–122 cr/yr inflows); itemised assignment lists are patchy. **RTI target:** PDGF statements naming RTFF & SDSS.

**Q34. Is the "grant" framing misleading?**
✅ At the project level, no one repays — but one layer up it is sovereign debt. The costume matters for disclosure: grants skip the investment-project disclosure stack (REPORT §5.4.3).

---

## D. Contracts, consultants and vendors

**Q35. Who is SECON?**
✅ A Bangalore survey/water-resources engineering firm; project consultant (planning, setup, commissioning) and web-DSS developer.

**Q36. Who is JBA?**
✅ JBA Consulting (UK) — a flood-risk consultancy whose parent sells flood models to the re/insurance industry.

**Q37. What did the SECON–JBA contract cost?**
❌ Not public. **RTI target #2:** the JV's contract value and payment schedule.

**Q38. Are there other vendors?**
✅ Yes — station registries we mirrored carry AMC (maintenance) vendor-name fields; the hardware sensor vendors are also in the registry stack.

**Q39. What is IIT-M's contract?**
🟡 "Technical supervision" per official text; the value and terms of IIT-M's engagement are not public.

**Q40. When do the maintenance contracts expire?**
🟡 66 stations carry `isamc=true` flags, but expiry dates are populated for only ~6 — the O&M calendar is unknown even to its own registry (F10).

**Q41. What happens when an AMC lapses?**
❌ No published plan. **Watch:** our AMC-expiry calendar (AUDIT-PLAN B2).

**Q42. Were the tenders published?**
🟡 TN e-procurement notices and WB procurement plans exist in fragments; no consolidated public list of RTFF contracts.

**Q43. Were conflict-of-interest checks done?**
❌ Nothing public.

**Q44. Who owns the system's software IP?**
❌ RTI target: contract IP clauses.

**Q45. Is the same JV involved in the new IFMC?**
❌ Not stated in Oct 2026 coverage. **Watch:** IFMC procurement trail.

---

## E. The sensor network

**Q46. How many sensors are there?**
✅ Registries we mirror: 328 ARG (incl. IIT-M 61 + 87 proposed), 121 AWLR existing + 139 basin-proposed, 63+53 SRG (GCC+PWD), 39+13 AWS, 5 gate sensors, plus tidal, agro, groundwater stations.

**Q47. Are they all working?**
✅ On census day: 22 of 38 dashboard stations fresh — 16 stale (F2).

**Q48. What about Nungambakkam, THE Chennai rain gauge?**
✅ Frozen at **10 May 2025** — 16+ months of nothing on the system built to show exactly that (F2).

**Q49. Who checks the sensors' health?**
❌ No public QA process; our mirror shows impossible values that nobody flagged (F7).

**Q50. What's a gate sensor for?**
✅ It reads lake/shutter positions — input to reservoir-release decisions (LoGS).

**Q51. What's an AWLR?**
✅ Automatic Water Level Recorder — telemetry on rivers, canals, tanks.

**Q52. Are sensor locations public?**
✅ Yes — coordinates are in the registry layers (our mirror publishes them as maps).

**Q53. Are there sensors near me?**
🟡 Likely, if you're in the 5 districts — verify against the ARG/AWLR registry maps in our GIS release.

**Q54. Why did a sensor read −18 °C in Chennai?**
✅ Data-quality failure at Kattupakkam (F7) — and nobody at the system flagged it. That's the point of F7.

**Q55. Who physically fixes a dead gauge?**
❌ Per-station maintenance responsibility is not published (AMC fields sparse).

**Q56. Is there a public sensor-status page?**
❌ No — recommendation #3 asks for exactly that.

**Q57. How old is this network?**
🟡 Rain records reach back to 1976 (SRG archive); the modern telemetry network is largely a 2018–2021 install.

**Q58. Did the 639 mm in one day at Michaung really happen?**
✅ Yes — it's in our rescued predecessor archive: 639 mm/24 h at the Zone-12 (Meenambakkam 6A) gauge, 2023-12-04 (ledger row 12, grade A).

**Q59. Can I watch live sensor data right now?**
🟡 The dashboard shows day-cards only; the machine-readable open feed is stale (F3). Our mirror is point-in-time.

**Q60. Do all districts have equal sensor density?**
❌ No published density analysis. Compute it yourself from our registries — that's what they're for.

---

## F. Open data and public access

**Q61. Is the system's data "open data"?**
✅ Accidentally, yes (F1) — 343 of 344 GeoServer layers answer anonymous queries; but with no license, no docs, no promise it stays.

**Q62. Can I download bulk data from the government?**
🟡 No bulk facility exists. Bulk is available from **our** Hugging Face mirrors.

**Q63. What license governs the government's data?**
❌ None published. Our release carries CC BY 4.0 on our arrangements; we claim no rights over the facts.

**Q64. Is there an API?**
🟡 An undocumented GeoServer + ~60 AJAX endpoints exist; the only "API reference" is our census (REPORT §3).

**Q65. Did you hack the system?**
✅ No. Read-only requests, identical to what the public website's own browser session issues. No logins, no bypassing.

**Q66. Is what you did legal?**
✅ Raw telemetry isn't copyrightable; NDSAP 2012 makes this class of data open by default; §52 fair dealing covers research/reporting (REPORT §6, ELI10 §9).

**Q67. Where do I get your data?**
✅ Hugging Face: `CashlessConsumer/chennai-flood-monitor-transactions`, `chennaidss-gis-layers`, `chennai-flood-history`, `chennai-flood-bulletins`, `chennai-rain-gauges`.

**Q68. What formats?**
✅ Parquet/GeoParquet — one-line DuckDB queries; GeoJSON source dumps also on disk.

**Q69. Is personal data in your release?**
✅ Scrubbed: officer names, SIM/mobile columns, citizen usernames removed (DATA-CATALOGUE §1, gis-layers README).

**Q70. Could the government switch the leak off?**
🟡 Yes — and that's F1's warning. Our annual re-mirror and the public release are the hedge.

**Q71. Why does open data matter for a flood?**
✅ Because independent verification, third-party apps, journalism, and research all need it. A warning you can't independently check is a rumour with a logo.

**Q72. What's a GeoServer?**
✅ Standard open-source map-data server software; the pretty website is a skin over it.

**Q73. What are the 344 layers, in groups?**
✅ DATA-CATALOGUE §3: transactions (13), station registries (31), water (34), drainage (8), boundaries (24), wards/crowd/alerts (8), flood history (9), forecast surfaces (37), misc bulletin wrappers (35).

**Q74. Has anything changed since you mirrored?**
✅ Re-census 2026-10-03: still exactly 344 layers, zero added/removed (DATA-CATALOGUE §1).

---

## G. The forecasts themselves

**Q75. Does it really give 3-day street-level warnings?**
🟡 The design says so and the Oct-2025 bulletins (image PDFs) show street-flood maps for the activation window. Publicly verifiable, continuously? No (F4/F5).

**Q76. How far ahead does it look?**
✅ 72 hours — five weather models fused with real-time sensor data.

**Q77. Which weather models does it fuse?**
✅ ECMWF, NCEP-GFS, UKMet, IMD-GFS and NCMRWF ensembles (AboutUs).

**Q78. What's an "ensemble"?**
✅ The same model run many ways (P25…P95 percentiles) — a range, not a single number.

**Q79. Are the forecasts saved anywhere?**
❌ **No archive exists.** The single most damning gap (F5). Forecast side must be captured activation-by-activation going forward.

**Q80. So how accurate is it?**
❌ No public forecast-vs-observed record exists — the ₹107-crore question with no public answer (F5).

**Q81. Which areas get street-level forecasts?**
✅ Named vulnerable zones: Pulianthope, Nungambakkam, Mambalam, Saidapet, Velachery, Meenambakkam, Mudichur.

**Q82. What about my ward specifically?**
🟡 The only public ward-depth layer is **static, stamped 11 Aug 2021** (F4) — a five-monsoon-old scenario, not a live forecast.

**Q83. What is LoGS?**
✅ Lake & Reservoir Operation Guidance System — advises WRD on shutter releases to reduce peaks while saving drinking water.

**Q84. Does it model storm-water drains?**
✅ The SWD network is a model input (GIS layer in our mirror). But drains must physically work — a model can't desilt.

**Q85. Can I see an actual sample forecast?**
✅ Yes — all 7 bulletins are on Hugging Face (`chennai-flood-bulletins`), incl. B5.0 Street Flood Inundation (ECMWF P75).

**Q86. Why are bulletins image-only PDFs?**
❌ Never explained; it makes machine verification impossible. Recommendation: publish data, not pictures.

**Q87. Did the IIT-M research model actually get used?**
🟡 Citizen Matters reports IIT-M's 4-km, 7-ensemble model is integrated and daily forecasts go to GCC/WRD; independent accuracy checks don't exist publicly.

**Q88. Is there a floodplain map I can use?**
✅ 2D model areas, bathymetry, contours are in our GIS mirror — the model's own working surfaces.

---

## H. Alerts and warning delivery

**Q89. How would I personally get warned?**
✅ Three routes today: press bulletins during activations, the TN-Alert mobile app, and TNSMART for departments. No SMS/RSS/API spec is public.

**Q90. Is there an SMS blast?**
❌ No public spec or evidence.

**Q91. Does TN-Alert cost me anything?**
🟡 App is free; the data cost is yours — a small but real equity point.

**Q92. Does the public alert feed work?**
✅ It has returned **zero rows on every check** (F6).

**Q93. What's "alert equity"?**
✅ If the only channel is one app you must have installed and open, the poorest, least-connected, most flood-exposed residents are the least served.

**Q94. Will I actually get a warning three days early?**
❌ Unverifiable — and during Ditwah (Dec 2025) not one media reference credited this system with any warning reaching anyone (MEDIA-CLAIMS pattern 2).

**Q95. Do school closures come from this system?**
🟡 No — collectors act on IMD alerts; RTFF wasn't visibly in that chain in Dec 2025.

**Q96. Do elderly/disabled residents get targeted alerts?**
❌ No evidence of any differentiated-alert design.

**Q97. Are alerts in Tamil?**
🟡 TN-Alert is claimed multilingual; the bulletins are English-only PDFs.

**Q98. Who decides when to issue an alert?**
🟡 HMCR feeds CRA/departments via TNSMART; the SOP and sign-off chain are not public.

**Q99. Can I subscribe to alerts myself?**
❌ No public subscription mechanism exists.

---

## I. How it did in real storms

**Q100. Did it work in the Dec 2025 Ditwah flood?**
✅ As a *recorder*: yes — citizen level-6 report at Puzhal, bridge sensors peaking (Aminjikarai 7.705 m, Manali 2.501 m), all consistent with press (F8). As a *forecaster*: unverifiable (F5).

**Q101. And Michaung (Dec 2023)?**
🟡 System was in pilot/operational transition; our predecessor mirror holds the full 639 mm event; no public forecast scorecard exists.

**Q102. NEM 2022?**
🟡 "Operationalized" per the Current Science paper; no public evaluation was ever published.

**Q103. What about 2015?**
✅ The system didn't exist; the flood maps (NRSC, 4,001 polygons) that justify it are in our mirror.

**Q104. Is it working in NEM 2026 right now?**
✅ Our probes run monthly; a forecast scorecard within 7 days of every activation is the standing protocol (ELI10 §10).

**Q105. Why has no scorecard ever been published?**
❌ No archive culture exists inside the system — F5. Scorecards need the forecast side; the system throws it away.

**Q106. Did warnings reach Velachery in Dec 2025?**
❌ Unknowable from any public record. **RTI target:** activation logs + dissemination records.

**Q107. What about Red Hills (Puzhal) shutters?**
✅ Opened for the sixth time that season in early Dec 2025; the system's sensors recorded the levels (REPORT §1, F8).

**Q108. Did any forecast demonstrably save a life?**
✅ Answer: **zero verified references** across 27 media entries (MEDIA-CLAIMS pattern 1). Not proof of failure — proof of no evidence.

**Q109. Was Ennore's 56 cm in 3 days forecast?**
❌ No archive to check against. This question is exactly why F5 matters.

**Q110. How fresh is the water-level data during storms?**
🟡 AWLR runs near-live (to Aug 2026 in our pull); ARG open feed is stale to 2022 (F3) — the picture is per-sensor-type.

**Q111. Who got the credit in the press during Ditwah?**
✅ IMD/RMC, CWC, district collectors, GCC's separate ICCC/EWS — not RTFF (MEDIA-CLAIMS entries 17–18).

**Q112. What did the control room actually do during Ditwah?**
❌ No public log. **RTI target:** HMCR activation log, Dec 2025.

**Q113. Could I have compared forecast vs rainfall myself last December?**
❌ No — no forecast archive. From NEM 2026 onward, our scorecards will make that possible.

**Q114. Has the system ever been wrong in public?**
🟡 No public record of any forecast — so also no record of any miss. Silence isn't accuracy.

**Q115. What's the first storm where a public scorecard is possible?**
✅ NEM 2026 — if activations occur, we publish within 7 days.

---

## J. Maintenance and operations

**Q116. Who staffs the control room?**
🟡 CRA/TNDRRA officers + SECON-JBA (handholding); actual staffing rosters are not public.

**Q117. What is this "handholding phase"?**
✅ WB-funded supervisory consultancy for the RTFF project ($0.10M line in TNCRUDP plans) — aftercare bought from the Bank, years after "operational".

**Q118. Is the system dependent on consultants forever?**
🟡 The structure suggests yes (consultant-run activations + AMCs + handholding); no public exit/capacity-transfer plan exists.

**Q119. What's an AMC?**
✅ Annual Maintenance Contract — the vendor keeps sensors/software alive; expiry dates live in the registries we mirrored.

**Q120. How many stations have an active AMC?**
🟡 66 flagged `isamc=true`; expiry populated for only ~6 — calendar unknown (F10).

**Q121. What does maintenance cost per year?**
❌ RTI target: AMC payment records (TNUIFSL/WRD).

**Q122. Who pays when the PDGF grant ends?**
❌ Unresolved — likely TNCRUDP, but no public commitment. The "operating money unresolved at both ends" point (REPORT §5.5).

**Q123. Is there a backup data centre?**
✅ A Nearline Disaster Recovery Centre at WRD Chepauk is described on the portal.

**Q124. Is there a public operations manual?**
❌ No SOP published — recommendation-grade gap.

**Q125. What happens during a power/network failure in a cyclone?**
❌ No public redundancy/continuity spec.

---

## K. Governance and oversight

**Q126. If it fails, who is answerable?**
🟡 CRA overall supervision per official structure; no published SLA, no named accountable officer.

**Q127. What is TNDRRA?**
✅ TN Disaster Risk Reduction Agency under the Commissionerate of Revenue Administration — the HMCR's home.

**Q128. Does the elected council or MLAs oversee it?**
❌ No visible elected oversight anywhere in the public record.

**Q129. What is the Advisory Committee?**
✅ Expert committee (IIT-M, IIT-B, NRSC, Anna University, NDMA-linked) formed 21 Jun 2021; its minutes are not public.

**Q130. Is there a citizens' representative on it?**
❌ None in any published membership list we've seen.

**Q131. Has CAG looked at it?**
❌ No public audit of this line exists. **Ask** for a performance audit.

**Q132. Is it under RTI?**
✅ Yes — CRA, WRD, TNUIFSL and GCC are public authorities; our §5.6 lists the targets.

**Q133. Whose budget line does it sit under?**
🟡 WRD/PDGF/TNUIFSL mix; the exact ledger split is not public.

**Q134. What happens when the government changes?**
🟡 Unknown — but the 2026 IFMC announcement suggests institutional memory survives via re-announcements, not via records.

**Q135. Is there any legislative committee on urban flooding?**
❌ Not in our sweep. (One for Assembly-watch.)

---

## L. The old website and institutional memory

**Q136. Was there an earlier website?**
✅ `chennaifloodsdss.in` — same system, first web face, live by the 2021 pilot, footer "Developed and Maintained by SECON & JBA".

**Q137. Why did it die?**
🟡 Quiet migration to the gov domain in 2025; domain now NXDOMAIN; no redirect, no notice, no archive notice (F9).

**Q138. Where did its data go?**
✅ Officially: nowhere. Practically: into our Dec-2023 mirror — 34,050 gauge readings incl. the full Michaung event.

**Q139. Can I still see the old site?**
✅ Partially via Wayback Machine (last capture 2025-08-31) and fully in our mirrors.

**Q140. Is the new site better?**
🟡 Same data pattern, new domain; the bulletin set grew from 0 to 7 — otherwise the gaps carry over.

**Q141. What else could vanish like this?**
🟡 Everything on it — which is why the project re-mirrors annually by design (ELI10 §4).

**Q142. Could this happen to the new site too?**
✅ Yes. F9 is a pattern, not an event.

---

## M. The 2026 IFMC (Integrated Flood Management Centre)

**Q143. What is the IFMC?**
✅ A new centre announced Oct 2026 (Revenue & DM secretary, at NIOT forum) promising street-level flood prediction three days ahead — focused on Chennai first.

**Q144. Is it new money?**
❌ No cost stated in coverage. **Watch:** IFMC sanction/trail.

**Q145. Is IFMC the same as RTFF & SDSS?**
🟡 The promise is verbatim RTFF's 2025 promise; the relationship (successor/expansion/rebrand) is publicly undefined.

**Q146. Was the earlier promise ever finished before the new one launched?**
✅ That is precisely the accountability question — one year after "fully operational", the same capability is being re-promised (MEDIA-CLAIMS pattern 3).

**Q147. Should residents welcome or resist IFMC?**
✅ Neither — demand the paper trail: what it adds, what it costs, and whether RTFF's gaps (F2–F7) are being fixed, not re-branded.

**Q148. Will you track it?**
✅ Yes — standing IFMC watch (ELI10 §10).

---

## N. Equity: who actually gets warned

**Q149. Do richer areas get better warnings?**
🟡 The seven named street-forecast zones span income levels; no equity analysis of alert delivery exists anywhere.

**Q150. What about Ennore / north Chennai?**
✅ Ennore's Dec 2025 disaster was *recorded* well by the system's own layers (56 cm/3 days, level-6 report) — but warning *delivery* there is undocumented.

**Q151. Peripheral flood hotspots like Mudichur?**
🟡 Named in the street-forecast list; actual alert reach unknown.

**Q152. Do resettlement-colony residents get alerts?**
❌ No evidence of targeted design.

**Q153. Is warning info available in Tamil?**
🟡 Partial — app claims multilingual; the substantive bulletins are English PDFs.

**Q154. Do tenants get warned the same as owners?**
❌ No differentiated mechanism exists.

**Q155. Are informal settlements inside the model?**
🟡 Wards are; informal layouts are likely under-represented in cadastral layers — a research question we can test with the GIS mirror.

**Q156. Do I need a smartphone to be warned?**
🟡 Effectively yes for TN-Alert — that's the digital-divide problem (alert equity, Q96–Q97).

**Q157. Is there a phone hotline for flood help?**
✅ GCC's 1913 complaint line (flood); a *forecasting* hotline does not exist.

**Q158. Has anyone studied who received Dec-2025 warnings?**
❌ Nobody — no delivery data is public. **RTI target.**

---

## O. Comparisons and benchmarks

**Q159. How does this compare with Mumbai's CFLOWS?**
🟡 CFLOWS (IIT-B for MCGM) is the usual benchmark; a cost-and-capability comparison is queued in our audit plan (B4) — no rigorous public comparison exists yet.

**Q160. Kolkata?**
🟡 Kolkata's early-warning system (KEWS) exists with published alerts; comparative audit pending.

**Q161. Bengaluru?**
🟡 Fragmented civic alerting; no comparable integrated DSS — part of why "first in India" claims go unchallenged.

**Q162. What does global good practice look like?**
✅ Japan/UK/Netherlands: published forecast archives, open APIs, post-event verification reports as routine.

**Q163. Is ₹107 crore good value?**
🟡 Unanswerable until verification exists — that's the honest budget position, not a slogan.

**Q164. What else could ₹107 crore have bought?**
✅ Counterfactual framing queued (AUDIT-PLAN B4): desilted kilometres at unit rates, pump stations, gauge networks. The "fare-hike test" applied to data infrastructure.

**Q165. How many flood-forecast stations does all of India have?**
✅ CWC runs ~360 flood-forecast stations nationally (2026 preparedness conference figure) — Chennai's urban system is a different beast; comparisons need care.

---

## P. "What about MY street?" — practical questions

**Q166. Can I check whether my street will flood?**
🟡 Only via image-PDF maps during an activation, or the static 2021 ward-depth layer. No live street query exists for the public.

**Q167. Where's my ward's data?**
✅ All 200 wards are in our GIS mirror (`gcc_200_wards`, ward depth min/max — noting the 2021 stamp).

**Q168. How do I read a bulletin?**
🟡 They're image PDFs; an explainer is on our list for the public page.

**Q169. My area flooded but no alert came. What do I do?**
✅ Document (photos+timestamp), complain on GCC 1913, and send us the record — evidence is how the scorecard gets built.

**Q170. Can I report flooding to the system?**
✅ The system has a crowdsourced-report layer (we mirrored 173 reports, identities stripped); GCC 1913 and IIT-M's citizen portal also collect reports.

**Q171. Do citizen reports actually reach the model?**
🟡 The crowd layer feeds the dashboard; whether it enters forecasts isn't documented.

**Q172. How deep was the water on my street in 2015?**
🟡 NRSC's 2015 extent (4,001 polygons) gives area-level depth bands — street-level granularity doesn't exist publicly.

**Q173. Are my lake's levels public?**
✅ Poondi, Chembarambakkam, Red Hills, Cholavaram storage are on the dashboard and in our mirror.

**Q174. Can I build my own flood app on this data?**
✅ Yes — that's what our HF datasets are for. (The government's own open feed is stale — F3 — so build on the mirror, and demand they fix theirs.)

**Q175. Who do I complain to about a dead gauge?**
✅ Start with GCC ward works + an RTI to CRA/WRD citing the station ID from our registries; the formal ask is a public station-status layer.

**Q176. What should I actually do this monsoon?**
✅ Follow IMD/RMC and collector advisories as primary; treat RTFF bulletins as one input; keep evidence (photos, dates); check our site for the scorecard after each activation.

---

## Q. The accountability toolkit

**Q177. What RTI should I file first?**
✅ One line: *"Certified copy of the sanction order(s) for RTFF & SDSS Chennai under PDGF, with cost and revisions."* To PIO, WRD / CRA / Finance Dept. (REPORT §5.6 list.)

**Q178. Which authority's PIO handles this?**
🟡 Three: WRD (basin/works), CRA/TNDRRA (control room), TNUIFSL (fund management) — and GCC for ward-level SWD.

**Q179. What if the RTI is refused?**
✅ First appeal to the departmental FAO, second appeal to the TN Information Commission. Refusals on "third-party information" are contestable for sanction orders.

**Q180. Can the CAG audit it?**
✅ Yes — citizens can request inclusion of RTFF & SDSS in a TN performance audit; cite F10's gaps.

**Q181. Is there a World Bank grievance route?**
✅ The Inspection Panel (and GRS) accept complaints from affected people on WB-financed operations; TNCRUDP is the current operation to cite.

**Q182. Can I see procurement documents?**
🟡 WB-side plans are public (P179189); TNUIFSL tender files need RTI; award values have never been published.

**Q183. Have MLAs/MPs asked questions about it?**
❌ We haven't swept TN Assembly Q&A yet — queued watch.

**Q184. Has any journalist investigated it?**
✅ Launch coverage is universal; accountability coverage is effectively our project — MEDIA-CLAIMS documents the gap.

**Q185. How do I use your evidence in a petition or story?**
✅ REPORT (evidence-graded claims + ledger), MEDIA-CLAIMS (hype vs record), DATA-CATALOGUE (provenance) are built to be citable, with sources.

**Q186. Can resident welfare associations file jointly?**
✅ Any citizen may file; RWAs can bundle RTIs (sanction order + AMC payments + activation logs are three clean, unjoinable asks).

**Q187. What's the single highest-leverage ask?**
✅ **Publish the forecast archive.** Every other question becomes answerable once forecasts are kept and comparable to observations (F5).

**Q188. How do I track whether things improve?**
✅ Project hub + the quarterly RTFF-DSS Ledger; monthly probes; per-activation scorecards (ELI10 §10).

---

## R. Privacy and surveillance

**Q189. Does the system track me personally?**
✅ The sensor telemetry is environmental, not personal; the crowdsourced layer did carry usernames — we stripped them before publishing.

**Q190. Are CCTV feeds part of it?**
🟡 GCC's ICCC (separate system) integrates CCTV; RTFF's AboutUs describes CCTV-equipped control rooms — camera governance is a different audit.

**Q191. Does TN-Alert collect my location?**
❌ Unknown — the app has no published privacy policy we could find. A fair question to put to TNSDMA.

**Q192. Are citizen flood reports public?**
✅ Yes — 173 reports (Nov–Dec 2025) are in our mirror, scrubbed of identities.

**Q193. Should I worry about my name in flood reports?**
✅ In our release, no (scrubbed). In the government's original system, retention policy is unpublished — ask.

---

## S. The basin: drains, lakes, wetlands

**Q194. Why not just fix drains instead of buying forecasts?**
✅ Both/and. GCC's FY2026-27 climate budget is ₹1,341 crore for 240+ km of SWD; forecasting without working drains is a thermometer for a broken pipe. The desk supports both, verified.

**Q195. Are encroachments the real problem?**
🟡 Partially — hydrology vs ecology debates (Pallikaranai, wetland loss) are real; a forecasting model cannot de-encroach. It can, however, expose where build-overs worsen inundation — if its data were open.

**Q196. Does the model include the storm-drain network?**
✅ SWD layers are model inputs (in our GIS mirror); drain *maintenance* status is not modelled — it's a GCC works question.

**Q197. Who desilts, and when?**
🟡 GCC pre-monsoon works, claimed 95% complete before NEM 2026 (press, graded C); independent verification is absent.

**Q198. What about Pallikaranai and the wetlands?**
✅ The marsh is a mapped layer in our mirror; NGT-driven protection orders are recent news — the flood model and the ecology fight are two fronts of the same basin story.

**Q199. The Kosasthalaiyar floods north Chennai differently than the Adyar floods the south. Does the forecast know that?**
🟡 The model covers both basins separately, but their public outputs arrive in the same PDF — basin-level separation that a Manali resident and a Velachery resident both need is achievable from existing layers if they were published as data.

**Q200. After everything we've read: what is the single question I should ask my MLA?**
✅ "Where is the archive of this system's forecasts, and when will it be public?" — every other number in this document flows from that one answer. உங்கள் சொத்து.
