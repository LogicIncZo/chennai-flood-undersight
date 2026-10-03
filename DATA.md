# DATA.md — what the data is

**Extracted:** 2026-09-29 (single-day census + full pulls) from
`chennaifloodmonitor.tn.gov.in` — the Chennai Flood Monitor (CFM-DSS), the public face of
the **RTFF & SDSS** (Real-Time Flood Forecasting & Spatial Decision Support System),
promoted by TNSMART/TN-DSS, funded via World Bank PDGF through TNUIFSL (₹107.2 crore),
consultants JBA/SECON, academic oversight IIT Madras.

**Access method:** the portal's front-end reads its data from an unadvertised GeoServer
endpoint (`/geohorr/ChennaiDSS/ows`) plus ~60 dashboard AJAX endpoints. We enumerated the
GeoServer capabilities (344 layers), fetched all readable layers and transaction tables,
and mirrored the dashboard API payloads. Read-only, anonymous, same requests a browser
loads. The predecessor system (`chennaifloodsdss.in`) died after we mirrored it in Dec 2023
— these mirrors are the continuity layer.

## Datasets (Hugging Face)

### 1. [`chennai-flood-monitor-transactions`](https://huggingface.co/datasets/CashlessConsumer/chennai-flood-monitor-transactions) (~37 MB)
Full sensor time series, GeoParquet:
- `transactions/srg_full.geojson` — **662,904** self-recording rain-gauge records,
  2021-05 → 2026-02 (full pull stalls post-Feb 2026 while AWS/ARG continue — itself a
  finding). 663 station IDs like `Adyar-01`.
- `transactions/aws_arg_full.geojson` — **669,147** AWS/ARG records (rainfall, temp, RH,
  wind, pressure), 2019-05 → 2026-09-29 (live to extraction day). Includes flagship
  stations (Nungambakkam, Meenambakkam) — with the real-world gaps (see quirks).
- `transactions/awlr_full.geojson` — **385,950** automatic water-level records, ~273
  sensors on rivers/canals/tanks, through Apr 2026.
- `stations/` — 33 registry layers: ARG 328 (incl. IITM 61 + proposed 87), AWLR 121
  existing + 139 basin-proposed, SRG 63 GCC + 53 PWD, AWS 39 + 13 proposed, 5 gate
  sensors, agro, tidal, groundwater. Registries carry **AMC vendor + validity fields** —
  the seed of the maintenance-debt register.

### 2. [`chennaidss-gis-layers`](https://huggingface.co/datasets/CashlessConsumer/chennaidss-gis-layers) (~40 MB)
181 GeoParquet layers (of 344 enumerated; 199 attempted, 5 server-failures preserved as
logs): administrative units (200 GCC wards + basin districts), full drainage network
(rivers, streams, major drain layers), 6,724 water bodies, bathymetry contours, LULC/soil,
model surfaces (ECMWF/NCEP/NCMRWF ensembles incl. post-Michaung recalibrations),
sub-basins, contours.

### 3. [`chennai-flood-history`](https://huggingface.co/datasets/CashlessConsumer/chennai-flood-history) (~2.3 MB)
- NRSC 2015 flood extent (4,001 features), IRS 2005 extent (235).
- GCC flood hotspots: 2015 (327), NEM 2020 (53).
- `ward_waterdepth_minmax` — 200 wards × depth min/max, **dated 2021-08-11** (static
  pre-launch scenario layer — a headline audit finding).
- `floodwarnings` (4), 173 crowdsourced flood reports (Nov–Dec 2025; usernames scrubbed).

### 4. [`chennai-flood-bulletins`](https://huggingface.co/datasets/CashlessConsumer/chennai-flood-bulletins) (~92 MB)
The system's only published outputs — 7 image PDFs from its first operational window:
B1.0 Observed Rainfall, B2.0 Rainfall Forecast (3 model variants), B3.0 Lake Water Level,
B4.0 River Water Level, B5.0 **Street Flood Inundation Forecast** (Ward-level depth map,
ECMWF Ensemble P75). Issued 22–28 Oct 2025 (pre-Ditwah activation, model runs Oct 18 →
Dec 2 2025).

### 5. [`chennai-rain-gauges`](https://huggingface.co/datasets/CashlessConsumer/chennai-rain-gauges) (predecessor archive)
Dec-2023 mirror of the dead `chennaifloodsdss.in`: 287 GIS layers + daily rainfall CSVs +
bulletins. Baseline for the 58-layer diff.

## Quirk ledger (read before trusting any field)

- `aws_arg_full`: negative rainfall values (−6.2) and impossible temps (−6.2 °C) appear —
  uncalibrated sensors ship raw.
- Nungambakkam-class stations frozen in the time series since 2025-05 — "flagship" ≠
  "working".
- The GeoServer CORS filter stack triples `Access-Control-Allow-Origin` (`*`, origin
  echo, `*`) with `Access-Control-Allow-Credentials: true` — per the fetch spec,
  browsers must reject that, so *any* third-party browser app calling the API dies
  with "Failed to fetch" while curl works from anywhere (incl. abroad). The atlas
  ships a read-only relay (`cashlessconsumer.zo.space/api/cfm-wfs`) as fallback.
  Net effect: the portal is only consumable same-origin — a quiet interoperability
  moat, whether intended or not.
- SRG and AWLR transaction endpoints stall for recent months (server-side) — full
  history only through Feb/Apr 2026 at pull time.
- 1 of 344 layers (`aws_new`) errors; `giswardmesh` is empty; a few registry rows carry
  placeholder names ("dc").
- `GetYearlydataforriver` (historical river levels 2019–2026) is intermittently broken
  server-side (500s) — the one gap we could not close on extraction day.

## Provenance & license posture

Everything is as-served by the government system, unmodified (crowdsourced personal
handles scrubbed). The portal publishes no license, no metadata, no API docs — we publish
as-received with provenance. Local working copy + extraction scripts:
`UngalSoththu/data/chennai-floods/cfm-dss-2026-09-29/`.
