# Legal note — what rights apply to this data, and what are we claiming?

**Status:** analysis for research posture, not legal advice. Written 2026-09-29.
**Question posed:** is there an exemption for investigating what is ostensibly
public-domain data of the city — data owned by the people?

## Short answer

We don't even need the exemption for the bulk of this release. **Facts are not
copyrightable in India.** Rainfall numbers, water levels, gauge coordinates, station
names, ward geometries, flood extents — these are facts and government-generated
records, not creative expression. The Copyright Act, 1957 protects original
*expression*; it does not protect the facts themselves. Our mirror of those facts,
in our own file formats, with our own provenance documentation, is a new compilation
of unprotectable data. What remains copyrightable (the bulletin maps' visual design,
the portal's code) we have not reproduced except as attributed quotations of official
publications — squarely inside fair dealing for research and reporting.

## The three layers

| Layer | Example | Status |
| --- | --- | --- |
| Facts / data itself | 662,904 SRG readings; ward polygons; gauge coordinates | No copyright in facts; govt-generated records, publicly served, no license or terms asserted at source |
| Our arrangement | Parquet conversion, census, cards, this repo | Ours. Released CC BY 4.0 |
| Government creative works | Bulletin PDF maps/graphics; portal code | Copyright likely vests in the Government (§17, works under its direction); we link/mirror bulletins as attributed official publications and use them for research/reporting — fair dealing territory (§52) |

## The statutes and cases

- **Copyright Act, 1957, §13** — copyright subsists only in *original* works.
  Facts and data are not "works". Compilations get protection only for the
  author's own selection/arrangement that meets the originality bar.
- **Eastern Book Co v. D.B. Modak** (2014) 1 SCC 257 — India's compilation
  standard is "skill and judgment" **plus** a modicum of creativity; sweat of the
  brow alone is insufficient (moving past *Macmillan v. K&J Cooper*, AIR 1924 PC 75,
  which had allowed thin compilation rights). Raw gauge telemetry — machine-emitted
  numbers with no creative selection — sits below any originality bar.
- **§17** — where a work is made under the direction or control of the Government,
  the Government is the first owner. That covers the bulletin graphics. It does
  **not** create copyright in measurements the instruments produce.
- **§52(1)(a)(i)–(iii)** — fair dealing for private or personal use including
  research; criticism or review; reporting of current events and affairs. Our use
  (research + journalism + mirror-with-attribution) is the textbook triple.
- **§52(1)(q)–(r)** — reproduction/publication of matter published in an Official
  Gazette and of public committee/court reports. The bulletins are not gazettes,
  but the principle — official public documents circulate — supports the posture.
- **NDSAP, 2012** (National Data Sharing and Accessibility Policy) — GoI policy
  default: non-sensitive government datasets *should be shared openly* behind a
  negative list, with govt data treated as a public resource. A state flood-DSS's
  sensor telemetry is the poster child of what NDSAP intends to be open. TN's own
  e-governance data policies echo this. So the honest framing is stronger than an
  "exemption for investigation": **openness is the stated default; closure is what
  would need justification.**

## Jurisdictional overlap

The mirror is served from Hugging Face (US). Under US law, facts are likewise
unprotectable (*Feist v. Rural Telephone*, 499 US 340 (1991)), and 17 USC §107
fair-use factors (purpose: nonprofit research/journalism; nature: factual;
amount: verifiable data; market effect: none — the state sells nothing here)
all point the same way.

## What we are and are not claiming

- We claim **no rights over the underlying facts** — they belong to no one and
  everyone. "Owned by the people" is constitutionally apt for taxpayer-funded
  instrumentation, even if copyright law reaches the same place via "no one".
- Our additions (formats, documentation, verification) are **CC BY 4.0**.
- We provide **attribution** to TNSMART/TN-DSS/WRD on every artifact and commit
  to **notice-and-takedown**: if the data controller objects to any specific
  artifact, we take it down first and argue after.
- We do **not** reproduce the portal's code or bulletin graphics beyond what
  quotation and the bulletins dataset (published official documents, needed as
  the system's only public record) require.

## Remaining risk, honestly stated

A court could hold that the *compilation* of the transaction tables required
protected skill/judgment. Against that: the selection was exhaustive (all rows,
no editorial filtering), mechanical, and documented — the anti-originality facts.
The political risk is the real one: an embarrassed agency asking a host to pull
data. The mitigation is the posture above: attribution, takedown-first, public
interest documentation, and the NDSAP default doing the heavy lifting.
