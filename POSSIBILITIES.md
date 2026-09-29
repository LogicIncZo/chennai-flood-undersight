# POSSIBILITIES.md — why this data matters, what it can build

## Why it's important

**1. It is the only public record of how Chennai's ₹107.2-crore flood system actually
performs.** The RTFF & SDSS was bought to forecast street flooding ward-by-ward. It
publishes no data downloads, no API, no forecast archive, no post-event verification. Its
bulletins are image PDFs. Without this mirror, "did the system warn us?" is unanswerable
by anyone outside the control room. With it, every future activation can be scored:
forecast vs observed rain vs actual flood reports.

**2. Chennai has learned the cost of data vanishing before.** The predecessor DSS site
died after Michaung; only our Dec-2023 mirror keeps its 287 layers usable. Rain-gauge
records for the 2015 flood (the 1,045 mm NEM) are effectively lost to the public. This
release makes 669K+ hourly weather records, 663K rain records and 386K water-level records
permanent and citable.

**3. It converts an invisible sensor network into a monitorable public asset.** The
registries tell us where sensors *should* be; the transaction tables tell us which ones
*are* reporting. The difference — 328 ARG stations claimed, fewer answering — is the
maintenance gap, in data. Registry AMC fields even name the maintenance vendors and
contract expiry dates: a maintenance-debt register waiting to be published.

**4. Flood history becomes mappable at ward scale.** 2005 + 2015 extents, GCC hotspots
(2015, NEM-2020), the 2021 ward depth matrix and today's ward boundaries can be stacked
with census population — exposure maps that infrastructure debates currently run without.

## What can be built with it

**Accountability journalism & audit**
- **NEM forecast scorecards**: each activation, score B2/B4/B5 bulletins against gauge
  rain and crowd reports. The audit plan's crown deliverable.
- **Stale-gauge tracker**: monthly "which of 328 ARG stations stopped reporting" ledger.
- **AMC expiry calendar**: vendor contracts lapsing, renewal RTIs queued 90 days ahead.
- **₹107.2-crore ledger**: sanction → consultants → vendors → O&M, from the World Bank
  PDGF disclosures + TNUIFSL RTIs, tracked like the Chennai One tender trail.

**Research & engineering**
- **Urban rainfall baselines**: 669K records 2019–2026 across 328 gauges — diurnal
  patterns, rain-shadow effects, Michaung/Ditwah event composites, urban heat-island ×
  rainfall studies.
- **Hydrology & drainage modeling**: real cross-sections, bathymetry, tank capacities
  (1,081 Mcft Poondi-class storage series) + 6,724 water bodies — open inputs for
  independent flood models to challenge the official one.
- **Forecast-benchmark dataset**: NCMRWF/ECMWF/GFS ensemble surfaces paired with observed
  gauges = the only urban flood-forecast verification set of its kind in India.

**Civic & consumer tech**
- **Ward flood-exposure lookup**: "does my ward flood?" from 2005/2015/2020 extents +
  depth matrix + crowd reports.
- **Open nowcasting baselines**: simple persistence/rank statistics from the gauge network
  to contextualize whatever the ₹107.2-crore system claims.
- **Alert-equity gap map**: alerts exist on a government app and as image PDFs — none as
  an API. Documenting the gap is step one to demanding one.

**Data infrastructure**
- **Continuity**: snapshot per monsoon (the Dec-2023 lesson), so no flood system's data
  dies with its website again.
- **Standing census diff**: 344 layers today, 58 more since 2023 — every new layer is a
  new public capability; every removed one is a question for the control room.

## The one-sentence case

A city that spends ₹107.2 crore on forecasting floods but publishes no verifiable
forecast record is asking its citizens to take the forecast on faith — this release turns
faith into something we can check, monsoon after monsoon.
