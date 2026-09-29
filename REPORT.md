# The Flood Machine and Its Shadow Data
## A public audit of Chennai's ₹107.2-crore Real-Time Flood Forecasting & Spatial Decision Support System

**CashlessConsumer / UngalSoththu desk** · Report draft v0.1 (for iteration) · 2026-09-29
**Companion data release:** four Hugging Face datasets (links in §3) + the 2026-12 rescue archive `chennai-rain-gauges`
**Evidence grades used:** **A** = artifact captured in our archive (reproducible command in appendix) · **B** = captured + corroborated by dated press · **C** = press-reported only, not independently verified · **D** = inference from evidence (reasoning stated)

---

## Executive summary

1. Tamil Nadu operates India's first fully operational urban flood-forecasting decision-support system for Chennai — the RTFF & SDSS, sanctioned at ₹107.2 crore, covering 4,974 km² across five districts, promoted via TNSMART/TN-DSS with World Bank PDGF funding through TNUIFSL and IIT Madras oversight. It has been fully operational since October 2025. **[C]**
2. The system's public-facing output is seven image-only PDF bulletins and a dashboard. It has no published data license, no API documentation, no public alert API, and no archive of its own forecasts — so its central promise (street-level, 72-hour-ahead flood intelligence) **cannot be independently verified by the public it protects.** **[A/B]**
3. Behind that wall, the system's own GeoServer — unadvertised, unlicensed, undocumented — serves **344 data layers** including 1.7 million sensor readings, 2005/2015 flood footprints, ward-level depth tables, and station registries embedding vendor maintenance contracts. We mirrored the readable 343 layers and published them openly. **[A]**
4. The mirror already surfaces accountability-relevant facts the portal itself does not surface: of 38 rain stations on its flagship dashboard, only 22 reported fresh data on census day; the city's historic reference gauges (Nungambakkam, Meenambakkam-ISRO, Madhavaram) have been frozen at **2025-05-10** for over sixteen months; the ward-level depth "forecast" layer is a **static scenario dated 2021-08-11**; and the machine-readable ARG feed was last bulk-updated in **January 2022** even as the dashboard reads 2026 data through a separate pipeline. **[A]**
5. We propose a lawful, attribution-first mirror posture grounded in the fact that **raw government telemetry is not copyrightable**, that NDSAP 2012 makes openness the default for exactly this class of data, and that research/reporting use is statutorily fair-dealing (§52, Copyright Act 1957). **[D — legal analysis]**

---

## 1. Why Chennai, why now

Chennai's flood risk is not a scenario exercise. The city drowned in December 2015; Cyclone Michaung delivered a verified **639 mm in 24 hours** at a single GCC zone gauge (Zone 12, Meenambakkam 6A gate) on 2023-12-04 in our own rescued archive; and in early December 2025 the remnant of Cyclone Ditwah dropped a reported **56 cm over three days on Ennore**, forced Red Hills shutters open for the sixth time that season, and produced the system's own highest citizen flood-severity report (level 6 of 6, at the Puzhal surplus outflow, 2025-12-04). **[A for our gauges and reports; B for press figures]**

The state's structural answer, sanctioned after 2015 and operational only in October 2025, is the RTFF & SDSS: five weather models fused with rain-gauge, river, lake and sea data into street-level inundation forecasts for vulnerable neighbourhoods (Pulianthope, Nungambakkam, Mambalam, Saidapet, Velachery, Meenambakkam, Mudichur), disseminated through a dashboard, press bulletins and the TN-Alert app. **[C]**

A forecasting system is only as accountable as its record. This report is the first outside look at that record.

## 2. What the system publishes — and what it doesn't

| Dimension | Published | Missing |
| --- | --- | --- |
| Forecasts | 7 bulletins (Oct 2025 activation), image-only PDF | Forecast archive; any forecast-vs-observed comparison |
| Sensor data | Dashboard cards (current day) | Bulk download, history, API docs |
| Alerts | `GetPublishAlert` feed (0 rows on 2026-09-29) | Public API, RSS, SMS spec |
| GIS | Portal map tiles | — (the GeoServer is open, but unadvertised) |
| Legal | Nothing | License, terms of use, privacy policy |
| Economics | ₹107.2 cr press figure | Sanction order, contract splits, O&M spend, validation reports |

The pattern is consistent: **display without documentation, delivery without durable record.**

## 3. The release: what we mirrored

On 2026-09-29 we enumerated the system's GeoServer capabilities (**344 layers; 343 anonymously readable** — census: `docs/wfs_census_2026-09-29.csv`), pulled every readable layer, pulled all transaction tables in full, and mirrored the dashboard API payloads. Released:

| Dataset | Contents | Size |
| --- | --- | --- |
| [`chennai-flood-monitor-transactions`](https://huggingface.co/datasets/CashlessConsumer/chennai-flood-monitor-transactions) | SRG rain 662,904 rows (1976→2026-02); AWS/ARG rain+met 669,147 (2018→2022-01 bulk); AWLR water levels 385,950 (2021-09→2026-08); 33 station registries incl. AMC vendor fields, PII-scrubbed | 37 MB |
| [`chennaidss-gis-layers`](https://huggingface.co/datasets/CashlessConsumer/chennaidss-gis-layers) | 181 GeoParquet layers: wards, drainage, waterways, tanks, bathymetry, forecast ensembles, crowdsourced reports (submitter identities stripped) | 40 MB |
| [`chennai-flood-history`](https://huggingface.co/datasets/CashlessConsumer/chennai-flood-history) | NRSC 2015 flood extent (4,001 polygons), IRS 2005 (235), GCC hotspots 2015 + NEM-2020, ward depth min/max, flood warnings | 2.3 MB |
| [`chennai-flood-bulletins`](https://huggingface.co/datasets/CashlessConsumer/chennai-flood-bulletins) | All 7 operational bulletins of the Oct 2025 run — the system's complete public record to date | 92 MB |

Plus the predecessor rescue: [`chennai-rain-gauges`](https://huggingface.co/datasets/CashlessConsumer/chennai-rain-gauges) — 34,050 GCC zone-gauge readings (2020-11→2023-12) including the full Michaung event, from the dead `chennaifloodsdss.in` portal.

## 4. Findings

**F1 — The data is open by accident, not by policy. [A→D]**
343 of 344 layers answer anonymous WFS requests. None of it is linked, licensed, or documented anywhere on the portal. The state has, in effect, published a world-class urban flood dataset and forgotten to notice. This is the release's enabling condition — and its fragility: no license means no assurance it stays open.

**F2 — The flagship rain gauges are dark on the public dashboard. [A]**
Dashboard station table, 2026-09-29: 38 stations listed, 22 fresh. Nungambakkam, Meenambakkam-ISRO, Madhavaram-AMFU and Ennore Port frozen at **2025-05-10**; RIMC Lab at **2024-10-21**. Chennai's historic IMD reference gauge (Nungambakkam) — the yardstick for every flood comparison since 2015 — has no current public reading on the system built to provide exactly that.

**F3 — Two pipelines, one visible. [A]**
The machine-readable ARG transaction table tops out at 2022-01-31 (bulk 2018–2021), while the dashboard API returns 2026-09 readings through a different pipeline. The "open" layer and the "operational" layer are not the same data path — so even a diligent citizen reading the open feed gets a four-year-stale city.

**F4 — The ward "forecast" is a 2021 scenario. [A]**
`ward_waterdepth_minmax`: 200 wards, every depth stamped **2021-08-11**. Street-level inundation, as exposed to the public record, is a static lookup from five monsoons ago — not a live model output. (The live street-flood output exists, but only as bulletin PDF maps during activations.)

**F5 — No forecast archive means no verifiable skill. [A→D]**
The model-run registry shows activations (Oct–Dec 2024; 2025-10-18→2025-12-02) and ensembles, but the system retains no published forecast-vs-observed record. After ₹107.2 crore, the question "how good is it?" has no public answer. Our mirror now holds the observed side; the forecast side must be captured going forward, activation by activation.

**F6 — Alerts exist, barely, and only inward. [A]**
The alert feed has returned an empty set on every check. Alerting happens through press bulletins and (claimed) the TN-Alert app during activations. There is no public API, RSS, or machine feed — alert equity depends on having the right app installed and open.

**F7 — The mirror holds data-quality anomalies the portal never surfaces. [A]**
Air-temperature readings of **−6.2 °C** at Madhavaram and **−18 °C** at Kattupakkam; a bridge sensor reading 26.476 "m" against a Cooum cross-section of ~7 m (unit-suspect); station names like `dc`; empty promoted layers (`getDailyRainfallValue`: 0 rows; `giswardmesh`: 0; `aws_new`: server error). Each is small; together they describe absent QA.

**F8 — The Dec-2025 flood is corroborated across three independent layers of the system's own data. [B]**
Citizen level-6 report (Puzhal surplus outflow, 2025-12-04 03:00Z) + bridge danger-level peaks same day (Aminjikarai 7.705 m at 15:30; Manali 2.501 m) + 168 crowd reports in Nov 2025 — consistent with The Hindu's Ennore/Red-Hills coverage of the same week. The system worked as a recorder during its last real test. Whether it worked as a forecaster is exactly what F5 says cannot be checked.

**F9 — The predecessor died and took its data with it. [A]**
`chennaifloodsdss.in` is NXDOMAIN (last Wayback capture 2025-08-31). Only the Dec-2023 rescue exists. Without mirrors, institutional memory evaporates at every URL change — which is why this release is annual-recurring by design.

**F10 — The economics are unaudited by design. [C→D]**
₹107.2 crore sanctioned (≈ ₹2.16 lakh/km² of the 4,974 km² covered; ≈ ₹53.6 lakh per ward). World Bank PDGF via TNUIFSL, consultants JBA/SECON, IIT-M oversight — all press/official-briefing level. No sanction order, contract split, O&M budget, or validation report is public. The station registries we mirror carry AMC vendor names and expiry dates — the thread an RTI pulls.

## 5. Licensing: is investigating public data of the city lawful?

Yes — and it needs less "exemption" than commonly assumed. Raw government telemetry (rain, levels, coordinates, geometries) is **not copyrightable**: the Copyright Act, 1957 protects original expression, not facts, and machine-emitted measurements involve no authorial selection. *Eastern Book Co v. D.B. Modak* requires skill-and-judgment-plus-creativity for compilation rights; an exhaustive, mechanical, documented mirror has none to infringe. Where copyright does vest in the Government (bulletin graphics, §17), our use — research, review, reporting of current affairs, mirror-with-attribution — is statutory fair dealing (§52(1)(a)(i)–(iii)). Policy points the same way: **NDSAP 2012 makes non-sensitive government data open by default** behind a negative list; a state flood-DSS's telemetry is the paradigm NDSAP case. The US-hosted mirror inherits the same logic (*Feist*; §107 factors). We therefore claim: no rights over the facts; CC BY 4.0 on our arrangements; attribution everywhere; notice-and-takedown without argument. Full analysis: `docs/LEGAL-NOTE.md`. **[D — legal analysis, not legal advice]**

## 6. Recommendations

**To TNSDMA / WRD / TNUIFSL** (none requires new money; all are policy):
1. Publish a data license (CC BY 4.0 suffices) and an API reference — the census we mirror is the draft.
2. Archive every bulletin and every model run; publish forecast-vs-observed after each activation.
3. Fix or retire the frozen flagship gauges; publish a station-freshness status layer.
4. Open the alert feed (API/RSS/SMS spec) — alerts in one app is alert inequity.
5. Adopt NDSAP formally for CFM-DSS: openness as default, negative list published.

**To researchers, journalists, civic technologists:** use the mirror. Score the next activation's bulletins against our gauges. Watch the AMC calendar. Demand the sanction order. The data now exists for all of it.

## 7. Method & reproducibility

Single-day census + full pulls on 2026-09-29: GeoServer `GetCapabilities` parse → per-layer WFS `GetFeature` (GeoJSON) with pagination → transaction tables pulled whole (`count` ≥ table size, verified `numberMatched == numberReturned`) → dashboard AJAX endpoints replayed with the front-end's own headers via a scripted browser session → PII scrub (officer/SIM/mobile columns; crowd submitter identities) → Parquet/GeoParquet conversion (DuckDB spatial + GeoPandas) → Hugging Face. Every figure in this report traces to a file in `UngalSoththu/data/chennai-floods/cfm-dss-2026-09-29/`. Census script committed (`docs/` of the release archive). No authentication was bypassed; only endpoints the portal's own front-end calls, called the way it calls them.

## 8. Limitations

Point-in-time capture (2026-09-29); activations since Oct 2025 may have changed server state. Press figures (rainfall totals, system cost, launch facts) are corroborated but not independently re-measured. The legal analysis is our own research posture, not legal advice. Five layers failed at source during pull and are excluded (logged). Claims are graded by evidence in the appendix.

## Appendix A — Claim-evidence ledger (key claims)

| # | Claim | Grade | Evidence |
| --- | --- | --- | --- |
| 1 | 344 layers, 343 readable anonymously | A | census CSV, 2026-09-29 |
| 2 | SRG 662,904 rows, 1976→2026-02 | A | `srg_full` count + min/max date |
| 3 | AWS/ARG 669,147 rows, bulk 2018→2022-01 | A | per-year DuckDB group-by |
| 4 | AWLR 385,950 rows, 2021-09→2026-08-16 | A | min/max date |
| 5 | 22/38 dashboard stations fresh on census day | A | API pull, 2026-09-29 |
| 6 | Nungambakkam/Meenambakkam-ISRO/Madhavaram frozen 2025-05-10 | A | station `date_time` fields |
| 7 | Ward depth layer static, dated 2021-08-11 | A | layer property inspection |
| 8 | ARG WFS bulk ends Jan 2022 | A | year group-by (2022: 3 rows) |
| 9 | Alert feed empty; 7 bulletins total | A | API pulls |
| 10 | ₹107.2 cr / 4,974 km² / 5 models / Oct 2025 launch | C | The Hindu 2025-10-22; Business Standard |
| 11 | Ennore 56 cm/3 days; Red Hills shutters 6th time (Dec 2025) | B | The Hindu 2025-12-03 vs our sensor/crowd layers |
| 12 | Michaung 639 mm/24 h at Zone-12 gauge | A | rescued archive peak query |
| 13 | 95% SWD works done before NEM 2026 | C | Live Chennai, Sep 2026 |
| 14 | "Open by accident" characterization | D | synthesis of 1, 9, absence of license/docs |

## Appendix B — Reproduction

Scripts and step-by-step in the release archive README (`UngalSoththu/data/chennai-floods/cfm-dss-2026-09-29/`); census: `docs/wfs_census_2026-09-29.csv`; layer diff: `docs/layer_diff_vs_2023archive.json`. Verify any count with a one-line DuckDB query against the Parquet files on Hugging Face.

## Sources

- The Hindu, "Chennai gets India's first real-time flood forecast system", 2025-10-22 — https://www.thehindu.com/news/cities/chennai/chennai-gets-indias-first-real-time-flood-forecast-system/article70186744.ece
- The Hindu, "After pounding north Tamil Nadu, remnant of Cyclone Ditwah drifts inland", 2025-12-03 — https://www.thehindu.com/news/cities/chennai/after-pounding-north-tamil-nadu-remnant-of-cyclone-ditwah-drifts-inland-city-to-get-light-rain-today/article70353989.ece
- Business Standard, "How urban flood warning systems work", 2026 — https://www.business-standard.com/india-news/how-urban-flood-warning-systems-work-mumbai-chennai-show-the-way-126070900246_1.html
- Live Chennai, "Chennai Monsoon Preparedness: 95% of Storm Water Drain Works Completed", Sep 2026 — https://www.livechennai.com/detailnews.asp?newsid=83291
- The Week, "Floods in Tamil Nadu from October–December... CM Vijay told", 2026-09-23 — https://www.theweek.in/news/india/2026/09/23/tamil-nadu-floods-from-october-december-extreme-heatwaves-2027-cm-vijay.html
- New Indian Express, "Not just drought, TN may also face flood and heatwave due to El Nino", 2026-09-23 — https://www.newindianexpress.com/states/tamil-nadu/2026/Sep/23/not-just-drought-tn-may-also-face-flood-and-heatwave-due-to-el-nino-says-panel
- Eastern Book Co v. D.B. Modak, (2014) 1 SCC 257 · Feist v. Rural Telephone Service, 499 US 340 (1991) · Copyright Act, 1957 §§13, 17, 52 · NDSAP 2012
- Primary archive: `UngalSoththu/data/chennai-floods/cfm-dss-2026-09-29/` (this workspace) · census + diff in `docs/`
