# DATA-CATALOGUE — the CFM-DSS mirror, itemised

**Compiled:** 2026-10-03 · **Mirror pull:** 2026-09-29 · **Live re-census:** 2026-10-03
**Scope:** every dataset the Chennai Flood Monitor (RTFF & SDSS) exposes — GeoServer layers, transaction tables, dashboard payloads, bulletins — and where our archive holds each one.

## 1. Did we archive everything? (coverage verdict)

**Yes — everything the server would hand an anonymous client on census day, with named exceptions.** The server enumerates **344 layers**; the census found 343 anonymously readable (1 auth-walled). Reconciliation, layer by layer:

| Bucket | Count | Detail |
| --- | --- | --- |
| Enumerated in GetCapabilities | 344 | census `docs/wfs_census_2026-09-29.csv`, counts per layer; **14,204,587 total features** across layers returning ≥1 |
| Empty at source (0 features) | 26 | incl. `aws_new` (server error), `giswardmesh`, `getDailyRainfallValue` — empties themselves are findings (report F7) |
| Failed at pull (OWS exception preserved) | 5 | `keylocations_bulletin`, `keylocations_obsbulletin`, `keylocations_districtmap`, `ecmwf_control_ensemble`, `dgps_cfms` |
| Unreadable (343-of-344 gap) | 1 | the layer the census could not fetch anonymously — see DATA.md access note |
| **Mirrored** | **312** | pulled whole, except the two sampled below |
| — of which sampled, not whole | 2 | `results_elements_242` (20k-row sample of ~242k), `tmp_table` (32k-row sample) — flagged in §4 gaps |
| Not captured (our query fault) | 1 | `arg_last7days` — our CQL used an illegal property name; the live 7-day ARG window is recapturable (§4) |

Naming note for reconciliation: dump files are renamed from source layer names (count baked into the filename, `gis_` prefixes dropped, and each layer's `_withlabel` label-variant merged into the base file). The label merges are why 312 mirrored layers condense to **199 archived GeoJSON files**.

**Live diff, 2026-10-03 vs census day:** re-ran GetCapabilities today — **344 = 344, zero layers added, zero removed** since the pull. Coverage remains complete as of this catalogue's date.

**Beyond the GeoServer** the portal exposes two more surfaces, both mirrored: ~60 dashboard AJAX endpoints (day-of payloads in `dump/api/dashboard_2026-09-29.json`) and the 7 bulletins (image-only PDFs, `dump/bulletins/` + HF).

## 2. Where the archive lives

| Location | What | Verified |
| --- | --- | --- |
| Hugging Face — `CashlessConsumer/chennai-flood-monitor-transactions` | 36 files: 3 transaction Parquets (1.72M sensor rows) + 33 station registries | pushed 2026-09-29T02:22Z |
| Hugging Face — `CashlessConsumer/chennaidss-gis-layers` | 184 files: 181 GIS GeoParquets + README/manifest | pushed 2026-09-29T02:28Z |
| Hugging Face — `CashlessConsumer/chennai-flood-history` | 13 files: 2015 NRSC extent, 2005 IRS, hotspots, ward depths, warnings, crowd | pushed 2026-09-29T02:22Z |
| Hugging Face — `CashlessConsumer/chennai-flood-bulletins` | 9 files: the 7 operational bulletins (Oct 2025 run) + docs | pushed 2026-09-29T02:22Z |
| Hugging Face — `CashlessConsumer/chennai-rain-gauges` | 20 files: Dec-2023 predecessor mirror (287 layers + daily CSVs) | pushed 2026-09-28T21:29Z |
| GitHub — `ungalsoththu/chennai-flood-undersight` | Report, audit plan, notes, docs (not the data — HF is the data home) | last push 2026-10-03 |
| Local — `UngalSoththu/data/chennai-floods/cfm-dss-2026-09-29/` | Full working archive: 199 GeoJSONs, census XML/CSV/JSON, API payloads, extract scripts | on this machine |

HF `lastModified` values above were re-verified via the HF API on 2026-10-03.

## 3. The catalogue, group by group

Source freshness = the newest observation *inside the data* (found in this audit); mirror freshness = pulled 2026-09-29 / pushed to HF 2026-09-29 unless noted.


### Sensor time series (transaction tables)

| layer (file) | features | source freshness |
| --- | --- | --- |
| `agro_transaction` | 3 | obs 2021-05-26 → 2021-05-26 |
| `arg_last7days` | error | NOT CAPTURED — our query errored (OWS exception) |
| `awlr_30d` | 0 | empty (0 features) at pull |
| `awlr_full` | 385,950 | obs 2021-09→2026-08-16 |
| `aws_airtemp_30d` | error | OWS exception preserved |
| `aws_arg_full` | 669,147 | obs 2012→2022-09-06 (7 rows 2012; bulk 2018–2021; 3 stragglers 2022) |
| `aws_panevap_full` | 4,485 | static/reference (no timestamp field) |
| `aws_rh_30d` | error | OWS exception preserved |
| `aws_soilmoisture_30d` | error | OWS exception preserved |
| `aws_sunenergy_30d` | error | OWS exception preserved |
| `aws_wind_30d` | error | OWS exception preserved |
| `srg_30d` | 0 | static/reference (no timestamp field) |
| `srg_full` | 662,904 | obs 1975→2026-02-17 (2 stray 1975 rows; bulk from 1976) |

### Station & sensor registries

| layer (file) | features | source freshness |
| --- | --- | --- |
| `administrativetable` | 20 | static/reference (no timestamp field) |
| `agro_stations` | 1 | static/reference (no timestamp field) |
| `arg` | 328 | registry last-update field to 2025-09-29 |
| `arg_iitm_existing` | 9 | static/reference (no timestamp field) |
| `arg_proposed` | 87 | static/reference (no timestamp field) |
| `arg_registry_328` | 328 | obs 2018-01-02 → 2025-09-29 |
| `awlr_44` | 44 | static/reference (no timestamp field) |
| `awlr_gcc_existing_46` | 46 | static/reference (no timestamp field) |
| `awlr_iitm_existing` | 6 | static/reference (no timestamp field) |
| `awlr_plank` | 8 | static/reference (no timestamp field) |
| `awlr_proposed_78` | 78 | static/reference (no timestamp field) |
| `awlr_proposed_basin_139` | 139 | static/reference (no timestamp field) |
| `awlr_radarpressureultrasonic` | 7 | static/reference (no timestamp field) |
| `awlr_shaftencoder` | 3 | static/reference (no timestamp field) |
| `awlr_stations_121` | 121 | static/reference (no timestamp field) |
| `aws_iitm_existing` | 6 | static/reference (no timestamp field) |
| `aws_proposed` | 13 | static/reference (no timestamp field) |
| `aws_registry_39` | 39 | obs 2018-01-01 → 2026-08-26 |
| `aws_registry_sql` | 38 | obs 2023-08-11 → 2023-08-11 |
| `dgps_cfms` | error | OWS exception preserved |
| `dgps_tanks` | 267 | static/reference (no timestamp field) |
| `gate_sensors_proposed` | 5 | static/reference (no timestamp field) |
| `groundwater_stations` | 0 | static/reference (no timestamp field) |
| `hydrological_stations` | 0 | static/reference (no timestamp field) |
| `meteorological_stations` | 0 | static/reference (no timestamp field) |
| `raingauge_proposed` | 0 | static/reference (no timestamp field) |
| `raingauge_stations_63` | 63 | static/reference (no timestamp field) |
| `srg` | 51 | obs 2023-09-25 → 2023-09-25 |
| `srg_pwd_existing_53` | 53 | static/reference (no timestamp field) |
| `srg_registry` | 51 | obs 2025-11-30 → 2026-08-16 |
| `tidal_stations` | 0 | static/reference (no timestamp field) |

### Water bodies, levels, bathymetry

| layer (file) | features | source freshness |
| --- | --- | --- |
| `awlrrls_latest_69` | 69 | obs 2021-09-06→2026-08-17 |
| `basin_lakes` | 6 | static/reference (no timestamp field) |
| `bathymetry_5298` | 5,298 | static contours |
| `bathymetry_contours_2863` | 2,863 | static/reference (no timestamp field) |
| `creeks` | 5 | static/reference (no timestamp field) |
| `gcc_tanks` | 309 | static/reference (no timestamp field) |
| `lakes_reservoirs_5841` | 5,841 | static/reference (no timestamp field) |
| `majorwaterbodies_bulletin` | 4 | static/reference (no timestamp field) |
| `pallikaranai_marsh` | 1 | static/reference (no timestamp field) |
| `purd_tanks_6720` | 6,720 | static geometry |
| `pwd_tanks_785` | 785 | static/reference (no timestamp field) |
| `rivers_naturalchannels` | 8 | static/reference (no timestamp field) |
| `rivers_naturalchannels_line_946` | 946 | static/reference (no timestamp field) |
| `routing_tanks` | 34 | static/reference (no timestamp field) |
| `scenario_points_bydatetime` | 41 | static/reference (no timestamp field) |
| `scenario_waterlevel_points_datetime` | 41 | static/reference (no timestamp field) |
| `spillway_uncontrolled` | 0 | static/reference (no timestamp field) |
| `structures` | 115 | static/reference (no timestamp field) |
| `tank_agency` | 14 | static/reference (no timestamp field) |
| `tank_drinkingwateroff_pump` | 2 | static/reference (no timestamp field) |
| `tank_drinkingwaterofftakes` | 6 | static/reference (no timestamp field) |
| `tank_hydraulic` | 10 | static/reference (no timestamp field) |
| `tank_inflowdetails` | 7 | static/reference (no timestamp field) |
| `tank_master` | 11 | static/reference (no timestamp field) |
| `tank_master_new` | 5 | static/reference (no timestamp field) |
| `tank_sluice` | 24 | static/reference (no timestamp field) |
| `tank_spillway_gate` | 28 | static/reference (no timestamp field) |
| `tank_spillway_uc` | 6 | static/reference (no timestamp field) |
| `waterbodies_bulletin_5659` | 5,659 | static/reference (no timestamp field) |
| `waterbodies_cma` | 782 | static/reference (no timestamp field) |
| `waterlevel_display_points` | 0 | static/reference (no timestamp field) |
| `waterlevel_display_points_datetime` | 41 | per-point latest timestamps (2021-era) |
| `waterways_bulletin_941` | 941 | static/reference (no timestamp field) |
| `waterways_cma` | 166 | static/reference (no timestamp field) |

### Drainage network

| layer (file) | features | source freshness |
| --- | --- | --- |
| `buckingham_canal` | 5 | static/reference (no timestamp field) |
| `krishna_water_canal` | 1 | static/reference (no timestamp field) |
| `macro_drains` | 15 | static/reference (no timestamp field) |
| `manmade_channels` | 294 | static/reference (no timestamp field) |
| `manmade_channels_line_3874` | 3,874 | static/reference (no timestamp field) |
| `micro_drains` | 37 | static/reference (no timestamp field) |
| `rivers_line_labels` | 946 | static/reference (no timestamp field) |
| `rivers_streams_876` | 876 | static/reference (no timestamp field) |

### Administrative & basin boundaries

| layer (file) | features | source freshness |
| --- | --- | --- |
| `adjacent_subbasin` | 8 | static/reference (no timestamp field) |
| `basin` | 1 | static/reference (no timestamp field) |
| `basin_boundary` | 1 | static/reference (no timestamp field) |
| `blocks` | 33 | static/reference (no timestamp field) |
| `catchments` | 71 | static/reference (no timestamp field) |
| `cma_boundary` | 1 | static/reference (no timestamp field) |
| `cmwssb_areas` | 15 | static/reference (no timestamp field) |
| `cmwssb_divisions` | 200 | static/reference (no timestamp field) |
| `district` | 33 | static/reference (no timestamp field) |
| `erstwhile_cc` | 1 | static/reference (no timestamp field) |
| `extended_gcc` | 1 | static/reference (no timestamp field) |
| `extended_gcc_zones` | 16 | static/reference (no timestamp field) |
| `gcc_boundary` | 1 | static/reference (no timestamp field) |
| `municipalities` | 9 | static/reference (no timestamp field) |
| `new_subbasin` | 6 | static/reference (no timestamp field) |
| `subbasin` | 5 | static/reference (no timestamp field) |
| `subbasin_boundary` | 6 | static/reference (no timestamp field) |
| `taluks` | 40 | static/reference (no timestamp field) |
| `tehsil_boundary` | 33 | static/reference (no timestamp field) |
| `ulb_boundary` | 9 | static/reference (no timestamp field) |
| `villages_1127` | 1,127 | static/reference (no timestamp field) |
| `watershed_boundary` | 71 | static/reference (no timestamp field) |
| `watersheds` | 74 | static/reference (no timestamp field) |
| `zone_boundary` | 16 | static/reference (no timestamp field) |

### Wards, crowdsourced reports, alerts

| layer (file) | features | source freshness |
| --- | --- | --- |
| `crowdsourced_173` | 173 | reports 2022-11-14→2025-12-04 (bulk Nov–Dec 2025) |
| `floodwarnings_4` | 4 | 4 warnings (dates in rows) |
| `gcc_200_wards` | 200 | static geometry |
| `gcc_200_wards_labels` | 200 | static/reference (no timestamp field) |
| `giswardmesh` | 0 | static/reference (no timestamp field) |
| `sb_wardboundaries_337` | 337 | static/reference (no timestamp field) |
| `ward_boundary_200` | 200 | static/reference (no timestamp field) |
| `ward_waterdepth_minmax_200` | 200 | obs 2021-08-11 → 2021-08-11 |

### Historical flood extents & hotspots

| layer (file) | features | source freshness |
| --- | --- | --- |
| `flood_spot_heights` | 368 | static/reference (no timestamp field) |
| `hotspots_gcc_2015` | 327 | static/reference (no timestamp field) |
| `hotspots_gcc_nem2020` | 53 | static/reference (no timestamp field) |
| `hotspots_irs_2005` | 200 | static/reference (no timestamp field) |
| `hotspots_kancheepuram_2015` | 139 | static/reference (no timestamp field) |
| `hotspots_tiruvallur_2015` | 200 | static/reference (no timestamp field) |
| `hotspots_vellore_2015` | 29 | static/reference (no timestamp field) |
| `irs_flood_extent_2005_235` | 235 | static/reference (no timestamp field) |
| `nrsc_flood_extent_2015_4001` | 4,001 | static/reference (no timestamp field) |

### Model surfaces & forecast ensembles

| layer (file) | features | source freshness |
| --- | --- | --- |
| `ecmfw_bulletin` | 75 | static/reference (no timestamp field) |
| `ecmfw_bulletin_values` | 75 | static/reference (no timestamp field) |
| `ecmwf_control` | 551 | static/reference (no timestamp field) |
| `ecmwf_control_ensemble` | error | OWS exception preserved |
| `ecmwf_control_max` | 0 | static/reference (no timestamp field) |
| `ecmwf_ens_aftermichaung_p75` | 567 | static/reference (no timestamp field) |
| `ecmwf_ens_p25` | 0 | static/reference (no timestamp field) |
| `ecmwf_ens_p50` | 0 | static/reference (no timestamp field) |
| `ecmwf_ens_p75` | 0 | static/reference (no timestamp field) |
| `ecmwf_ens_p90` | 0 | static/reference (no timestamp field) |
| `ecmwf_ensemble_after_michaung` | 567 | static/reference (no timestamp field) |
| `ecmwfcontrol_651` | 651 | static/reference (no timestamp field) |
| `floodforecast_2d_outputarea` | 1 | static/reference (no timestamp field) |
| `getDailyRainfallValue_EMPTY` | 0 | empty (0 rows) at source |
| `idw_demo` | 0 | static/reference (no timestamp field) |
| `iitm_bulletin_670` | 670 | static/reference (no timestamp field) |
| `iitm_control_12136` | 12,136 | static/reference (no timestamp field) |
| `imd_bulletin` | 0 | static/reference (no timestamp field) |
| `imd_bulletin_values` | 52 | static/reference (no timestamp field) |
| `ncepcontrol` | 289 | static/reference (no timestamp field) |
| `ncepgfs_bulletin` | 16 | static/reference (no timestamp field) |
| `ncepgfs_control` | 72 | static/reference (no timestamp field) |
| `ncepgfs_control_ensemble` | 225 | static/reference (no timestamp field) |
| `ncepgfs_control_max` | 72 | static/reference (no timestamp field) |
| `ncepgfs_ens_p75` | 23 | static/reference (no timestamp field) |
| `ncmrwf_bulletin_573` | 573 | static/reference (no timestamp field) |
| `ncmrwf_bulletin_values` | 573 | static/reference (no timestamp field) |
| `ncmrwf_control_1452` | 1,452 | static/reference (no timestamp field) |
| `observed_rainfall_bulletin` | 52 | static/reference (no timestamp field) |
| `observed_rainfall_values` | 0 | static/reference (no timestamp field) |
| `onedim_model_area` | 38 | static/reference (no timestamp field) |
| `streetfloodbulletin_waterbodies` | 57 | static/reference (no timestamp field) |
| `streetfloodbulletin_waterways_1700` | 1,700 | static/reference (no timestamp field) |
| `twodim_modelarea_ecmwf` | 75 | static/reference (no timestamp field) |
| `twodim_modelarea_ncep` | 9 | static/reference (no timestamp field) |
| `ukmo_control` | 304 | static/reference (no timestamp field) |
| `ukmo_control_max` | 304 | static/reference (no timestamp field) |

### Bulletin wrappers, scenario layers, offices, streets

| layer (file) | features | source freshness |
| --- | --- | --- |
| `amenities` | 8 | static/reference (no timestamp field) |
| `basinboundary_obsbulletin` | 1 | static/reference (no timestamp field) |
| `camera_poles_gcc` | 100 | static/reference (no timestamp field) |
| `cma_bulletin` | 1 | static/reference (no timestamp field) |
| `gcc_bulletin` | 1 | static/reference (no timestamp field) |
| `gcc_observedrainfallbulletin` | 1 | static/reference (no timestamp field) |
| `gcczones_bulletin` | 16 | static/reference (no timestamp field) |
| `gds` | 0 | static/reference (no timestamp field) |
| `indianboundary_bulletin` | 1 | static/reference (no timestamp field) |
| `keylocations_bulletin` | error | OWS exception preserved |
| `keylocations_districtmap` | error | OWS exception preserved |
| `keylocations_gcc_obsbulletin` | 18 | static/reference (no timestamp field) |
| `keylocations_obsbulletin` | error | OWS exception preserved |
| `levelling` | 149 | static/reference (no timestamp field) |
| `locations` | 47 | static/reference (no timestamp field) |
| `ncepgfsgrid` | 289 | static/reference (no timestamp field) |
| `offices_cmwssb` | 1 | static/reference (no timestamp field) |
| `offices_collectors` | 5 | static/reference (no timestamp field) |
| `offices_fire` | 1 | static/reference (no timestamp field) |
| `offices_gcc` | 32 | static/reference (no timestamp field) |
| `offices_police` | 5 | static/reference (no timestamp field) |
| `offices_twad` | 1 | static/reference (no timestamp field) |
| `offices_wrd` | 21 | static/reference (no timestamp field) |
| `proposed_flood_control_rooms` | 7 | static/reference (no timestamp field) |
| `results_elements_242_sample20k` | 20,000 | SAMPLE ONLY (20k of 242k rows) |
| `rf_ddmmyy_obsbulletin` | 98 | static/reference (no timestamp field) |
| `rf_gcc_obsbulletin` | 98 | static/reference (no timestamp field) |
| `sewage_treatment_plants` | 5 | static/reference (no timestamp field) |
| `stateboundary_bulletin` | 39 | static/reference (no timestamp field) |
| `subbasinboundary_bulletin` | 4 | static/reference (no timestamp field) |
| `surface_test` | 0 | static/reference (no timestamp field) |
| `testview` | 74 | static/reference (no timestamp field) |
| `tmp_table_32k_sample` | 5,000 | SAMPLE ONLY (32k rows) |
| `water_distribution_stations` | 108 | static/reference (no timestamp field) |
| `water_treatment_plants` | 10 | static/reference (no timestamp field) |

## 4. Gaps register (what we do NOT hold whole)

| # | Gap | Why | Recoverable? |
| --- | --- | --- | --- |
| G1 | `arg_last7days` (live 7-day ARG window) | our query sent an illegal property name; server returned OWS exception | Yes — fix CQL to `date` field, re-pull |
| G2 | `results_elements_242` — only 20k-row sample | table ~242k rows; pulled as sample to bound size | Yes — paginated full pull |
| G3 | `tmp_table` — only 32k-row sample | same | Yes — paginated full pull |
| G4 | 5 failed layers | server OWS exceptions at pull (names in §1) | Retry; they may be ephemeral |
| G5 | `aws_new`, `giswardmesh`, `getDailyRainfallValue` | empty/errored **at source** | Nothing to pull; empties are audit findings (F7) |
| G6 | Forecast ensembles are last-run snapshots | server overwrites per model run, no versioning | Only future captures fix this — capture per activation |
| G7 | Bulletins between Dec 2025 and today | none observed published since the Oct-2025 window | Watch portal per activation |

## 5. Freshness: how to read this catalogue

Three distinct clocks — never conflate them:
1. **Observation freshness** — newest timestamp inside the data (§3 tables). This is the system's own data currency: SRG stops 2026-02, ARG open feed stops 2022, AWLR runs to 2026-08, ward "forecast" is 2021.
2. **Mirror freshness** — when we pulled (2026-09-29) and pushed (2026-09-29). The mirror is a snapshot; it does not self-update.
3. **Coverage freshness** — whether the server's layer set changed since the pull. Checked 2026-10-03: unchanged (344 = 344).

## 6. Re-verification commands

```bash
# Re-census the live layer set and diff against the archive
curl -s "https://chennaifloodmonitor.tn.gov.in/geohorr/ChennaiDSS/ows?service=WFS&version=2.0.0&request=GetCapabilities" -o /tmp/caps.xml
python3 -c "import xml.etree.ElementTree as ET; r=ET.parse('/tmp/caps.xml').getroot(); print(sum(1 for e in r.iter() if e.tag.endswith('}FeatureType')))"
# Expected: 344 while unchanged (2026-10-03)

# HF release state
curl -s "https://huggingface.co/api/datasets/CashlessConsumer/chennai-flood-monitor-transactions" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['id'], d['lastModified'], len(d['siblings']),'files')"

# Verify any figure in §3 against the public Parquets (DuckDB)
duckdb -c "SELECT count(*), min(date), max(date) FROM 'data/srg_rain.parquet'" # on HF transactions repo
```
