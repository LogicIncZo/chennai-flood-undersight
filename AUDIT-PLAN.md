# AUDIT-PLAN.md — RTFF & SDSS technical + economic audit

**Subject:** Real-Time Flood Forecasting & Spatial Decision Support System (RTFF & SDSS)
for the Chennai basin — the ₹107.2-crore system behind chennaifloodmonitor.tn.gov.in.
Promoted by TNSMART/TN-DSS (Water Resources Dept), World Bank PDGF funds via TNUIFSL,
consultants JBA/SECON, oversight IIT Madras.

**Stance:** riders'-advocate oversight — evidence over opinion, systems not persons,
responsible disclosure by default. Every figure traced to a capture in
`UngalSoththu/data/chennai-floods/cfm-dss-2026-09-29/` or a dated public source.

**Ground rules:** passive observation of public endpoints (GET/POST the front-end itself
uses; no auth bypass, no load tests, no scraping of personal data). Security findings →
CERT-In disclosure pack before publication. RTIs via rtionline.gov.in (TN has no state RTI
portal). India-vantage checks via the ocitwo node. Monsoon = audit season.

---

## Track A — Technology / digital-layer audit

### A1. Availability & posture
- Hosting & stack census: IPs, CDN/WAF, server headers, TLS config (cert, HSTS, CAA),
  geohorr (GeoServer) vs IIS front-end split. *In hand:* session fingerprints + anti-CSRF
  cookie + 403 behavioral wall already documented.
- **Standing uptime probe** on 6 endpoints (dashboard, 3 AJAX APIs, geohorr WFS,
  bulletin PDF host) from inside + outside India. Output: public uptime like the
  bank-domains tracker.
- Verify the April-2026 DNS cutover (old DSS → CFM) left no public exposure of legacy
  hosts.

### A2. API surface & data infrastructure
- Publish the **endpoint census** (~60 dashboard AJAX + WFS/WMS/CSW/WMTS) as a documented
  API reference — the state itself has none.
- Session model analysis: what breaks API access (fingerprint, cookie, CSRF), stability
  across months, fair-use thresholds.
- The open-by-accident question: is GeoServer access *intended*? Evidence: robots, docs,
  site maps, any auth on staging vs prod.
- Endpoint reliability ledger: `GetYearlydataforriver` 500s, `aws_new` layer error,
  `giswardmesh` empty — file as defect list with dates.

### A3. Sensor-network integrity (the maintenance audit)
- **Station freshness ledger**: from registries × transactions, compute last-seen per
  station (328 ARG + 663 SRG + 273 AWLR). Monthly diff → "dead gauge watch".
- Data-quality flagging: negative rain, impossible temps, unit-suspect series (the
  ORR-bridge class), duplicate IDs.
- RTI lane: AMC vendor + `amcvalidtill` fields (already in hand) → is maintenance paid
  and delivered? Which zones lag?

### A4. Model & forecast layer
- Model run registry (ECMWF/NCEP-GFS/NCMRWF det+ens): actual run cadence vs claimed
  cadence across seasons; ensemble percentiles' provenance (incl. post-Michaung
  recalibration layers).
- **The static-layer problem**: ward depth matrix dated 2021-08-11 — is the "street
  inundation forecast" a live model or a scenario lookup? Evidence so far says lookup.
  RTI for the model configuration + validation reports.
- **No forecast retention** = no verifiable skill. Fix proposal: require published
  forecast archive (we'll maintain our own mirror meanwhile).

### A5. Alerting chain (the consumer-facing layer)
- Alert lifecycle: `GetPublishAlert` (empty in Sept 2026), bulletin issuance cadence,
  TN-Alert app integration, WhatsApp/SMS claims vs evidence.
- Alert-equity finding: alerts live in one app + image PDFs; no API/RSS/cell-broadcast
  API. Deliverable: gap note + "what a public alert feed should look like" spec.
- TN-Alert APK review (client-side-vuln-scout): permissions, trackers, data flows —
  same treatment as Chennai One.

### A6. Web quality & accessibility
- Image-only PDFs (no text layer), alt-text, i18n (Tamil), dashboard JS quality,
  visitor-counter integrity (50,566 across resets?).
- Defect register with severity; feed the "open-data compliance" recommendation list.

### A7. Privacy & citizen data
- Crowdsourced flood reports: retention, username/phone exposure (we scrubbed ours),
  consent language in the citizen app.
- No privacy policy on the portal — documented gap; DPIA-style note.

### A8. Open-data compliance & recommendations
- Compare against: National Data Sharing policy, TN e-governance data policy, OGC
  service norms. Output: **recommendation register** (license, docs, API, archive,
  forecast retention, alert feed) sized for an op-ed + RTI follow-through.

---

## Track B — Economic angle & debt monitoring

### B1. Capex ledger (where the ₹107.2 crore went)
- Sanction order (RTI to WRD/TNUIFSL), World Bank PDGF tranche mapping, contract splits:
  JBA (modelling), SECON (survey/sensors), IIT-M (R&D oversight), control-room ops.
- Cross-check: CAG TN audits, PIB/TN press notes, TN budget docs (demand no. for WRD),
  procurement portal notices (like the Chennai One trail).

### B2. O&M & vendor debt register (the fiscal-debt book)
- Harvest `agencyname_amc` / `amcvalidtill` / `isamc` from all station registries →
  vendor-by-station map + expiry calendar (we hold the raw data already).
- Annual O&M spend RTI (AMC payments, comms/sim leases, control-room staffing, pump
  rentals during activations).
- Quarterly **RTFF-DSS ledger** post: capex vs O&M vs coverage delivered (stations
  alive), in the RegTrac/LobbyWatch register style.

### B3. Technical-debt register (what the system owes itself)
| Debt item | Evidence in hand | Cost if unpaid |
| --- | --- | --- |
| Stale stations (Nungambakkam frozen May-2025; SRG pull stalls 2026-02) | transaction tables | blind spots exactly where data matters |
| Static 2021 ward-depth layer as "forecast" | B5.0 + ward layer dates | false confidence ward-by-ward |
| No forecast archive | API census | unverifiable ₹107.2-cr performance |
| No API docs/license | portal | zero reuse, one-vendor lock-in |
| Image-only PDFs | bulletins repo | no machine-readable alerts |
| Dead predecessor site | Dec-2023 mirror | institutional memory loss |
Each entry: owner (WRD/TNSMART/TNUIFSL), ageing, escalation path (RTI → CAG → press).

### B4. Cost-effectiveness frame
- Cost per km² (₹107.2 cr ÷ 4,974 km² ≈ ₹2.16 lakh/km²), per ward (₹53.6 lakh), per
  activation day; compare with Mumbai's CFLOWS and global urban FFWS benchmarks.
- Counterfactual per-rupee: ₹107.2 cr = how many desilting km, pump stations, or gauge
  networks at unit rates from TN budget docs — the fare-hike-test applied to data
  infrastructure: *what service quality justifies this line item?*

### B5. Cadence
- **Monthly**: uptime + station-freshness diff (automated probes).
- **Quarterly**: RTFF-DSS ledger (money + tech debt).
- **Every NEM activation**: forecast scorecard within 7 days of the event.
- **Annually**: full re-census + dataset re-mirror (the Dec-2023 lesson).

---

## Deliverables
1. API reference + uptime page (this repo / GitHub Pages).
2. Station-freshness + AMC-expiry dashboard (DuckDB + static site).
3. Forecast scorecards (NEM 2026 first edition).
4. The RTFF-DSS Ledger (quarterly money + debt register).
5. CERT-In pack (if security findings warrant) + recommendation register as op-ed/RTI
   annexes.

**Status:** data layer complete (2026-09-29 release). Track A1/A2 evidence captured;
B2 raw material in hand. Next concrete step: A3 freshness ledger + B2 AMC calendar from
already-pulled data.
