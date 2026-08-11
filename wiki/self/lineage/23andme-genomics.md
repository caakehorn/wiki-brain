---
domain: self
page_type: report
status: active
date_created: 2026-07-25
date_modified: 2026-08-11
sources: ["raw/self/ancestry/dna-reports/Ancestry Composition - 23andMe.pdf", "raw/self/ancestry/dna-reports/chromosome.pdf", "raw/self/ancestry/dna-reports/health.pdf", "raw/self/ancestry/extracted/health-report-extracted-layout.txt"]
tags: [family, physical-health]
connections:
  - page: wiki/mind/synthesis/ancestral-dialectic
    type: evidences
    claim: "The Ashkenazi signal and the sub-regional European mapping are the biological half of the dialectic, corroborating from DNA what the paper trail already showed."
  - page: wiki/health/chemical-architecture
    type: contextualizes
    claim: "The 95th-percentile Neanderthal variant load is offered as background to the chemical architecture rather than a cause of it — the PheWAS links to mood, nicotine and chronotype are population-level associations, not a finding about Dan."
---

# 23andMe Genomics

Genomic profile exported from 23andMe provides a biological cross-reference to the documentary family tree, highlighting a significant Neanderthal variant load alongside the expected Ashkenazi and sub-regional European signals. The `Ancestry Composition - 23andMe.pdf` and `chromosome.pdf` visual exports are image-based without an extractable text layer (percentages below are read off the page images). `health.pdf` — a separate 23andMe "Reports Summary" export, uploaded independently by the operator 2026-08-11 as a "Huge find" and confirmed byte-identical to the copy already on file — **does** carry a text layer, but a two-column condition/result layout that a naive extraction badly mis-pairs; `pdftotext -layout` preserves the correct pairing and is the source for the two sections below (full extraction: `raw/self/ancestry/extracted/health-report-extracted-layout.txt`).

## Ancestry Composition

Exact percentages, previously flagged as an extraction gap, now resolved from `health.pdf`'s Ancestry Reports section (Updated: October 25, 2024):

| Region | % |
|---|---|
| **European** | 99.7% |
| — Northwestern European | 78.3% |
| —— British & Irish | 55.8% |
| —— French & German | 22.2% |
| —— Broadly Northwestern European | 0.3% |
| — Ashkenazi Jewish | 21.4% |
| **Sub-Saharan African** | 0.2% |
| — West African (Ghanaian, Liberian & Sierra Leonean) | 0.2% |
| **Unassigned** | 0.1% |

**Maternal Haplogroup: R0. Paternal Haplogroup: R-Z93.**

The paternal Jewish immigrant line ([[wiki/people/david-j-frank]], b. 1892
Russia; [[wiki/people/sadie-harris]], b. 1900 Austria) reliably predicts the
21.4% Ashkenazi signal, exactly matching what
[[wiki/mind/synthesis/ancestral-dialectic]] already treats as the paternal
"hypervigilance" line's biological substrate. The 78.3% Northwestern
European (British & Irish 55.8%, French & German 22.2%) maps onto the
maternal Fayette County / Appalachian network the same page treats as the
"numbness" line — the two figures are within a few points of the
theoretically-expected 50/50 split for a single-generation paternal/
maternal divide, once the Ashkenazi and non-Ashkenazi European totals are
compared (21.4% vs. 78.3%, i.e. the paternal signal is diluted below 50%
because Rick's own maternal side, per the GEDCOM, was not exclusively
Ashkenazi either).

**A genuinely new, previously undocumented data point: a 0.2% Sub-Saharan
African (Ghanaian, Liberian & Sierra Leonean) trace signal**, filed under
23andMe's "Additional Ancestry Regions... that reflect mixed ancestry or
more recent migration." At this magnitude (23andMe's own trace-region
threshold), this is exactly the kind of low-confidence signal that can
reflect distant reference-panel noise as easily as a real ancestor several
generations back — it is recorded here as a documented fact of the report,
not folded into [[wiki/mind/synthesis/ancestral-dialectic]]'s two-line
frame, which concerns dominant heritage strands (Ashkenazi vs. British/
German-Appalachian) rather than trace admixture. No paper-trail record in
[[wiki/self/lineage/family-tree]] currently explains it; flagged as a gap
rather than a finding.

## Chromosome Painting

Derived from chromosome.pdf (199 KB, 2 pages), this segment visualizes ancestry assignments across all chromosomes. It provides a granular look at the distribution of different ethnic markers, though no raw SNPs are available in this specific export.

## Neanderthal Ancestry
Dan's Neanderthal percentage places him in the 95th percentile of 23andMe customers ("More Neanderthal variants than 95% of customers" — health.pdf's exact wording, confirming the figure previously read off the visual export). While PheWAS studies have linked some Neanderthal-introgressed variants to mood disorders, nicotine addiction, and chronotype, there is no direct causal link established here. Instead, this genetic data point functions as a symbolic reinforcement of an outsider identity.

## Health Predisposition and Carrier Status

Of 14+ Health Predisposition reports and 46+ Carrier Status reports, only
two returned anything other than "Variants not detected":

- **Hereditary Thrombophilia — slightly increased risk.** A predisposition
  toward blood clotting (elevated risk of deep vein thrombosis / pulmonary
  embolism). No other corpus material currently documents a clotting event
  or diagnosis; filed here as a standing health datapoint, not a finding
  about anything that has happened.
- **Tyrosinemia Type I — variant detected (carrier status).** A recessive
  metabolic disorder; carrier status alone has no expected health effect
  for Dan himself, but is relevant to any future family-planning context —
  it only matters if a partner is also a carrier.
- **Age-Related Macular Degeneration** — "variant detected, not likely at
  increased risk" (a variant present but not the risk-conferring
  combination).
- Every other tested condition — including Alzheimer's, Parkinson's,
  BRCA1/2, Celiac, Hemochromatosis, G6PD deficiency, and the full 45-entry
  remainder of the Carrier Status list (Cystic Fibrosis, Tay-Sachs, Sickle
  Cell, Canavan, Gaucher Type 1, and so on) — returned "Variants not
  detected" or, for BRCA1/2, "Complete tasks to view result" (never
  completed).

## Wellness and Traits (selected)

Lower-signal but on the record: **unlikely to flush from alcohol**;
**likely to consume less caffeine**; **less likely to be a deep sleeper**;
**predisposed to weigh about average**; **muscle composition common in
elite power athletes**; **lactose tolerant**; **likely to wake up around
8:34am**; typical trait predictions for eye/hair color, earwax, bitter
taste, and the rest of the standard 37-trait panel. None of this
contradicts or extends anything else on file; recorded for completeness
per the corpus's "keep the mundane" standard rather than because any of it
is individually load-bearing.

## Gaps
- The Sub-Saharan African 0.2% trace signal has no corroborating paper-trail source and is unexplained.
- Chromosome-painting PDF still has no raw SNP/CSV export attached — visual only.
- Whether the Hereditary Thrombophilia finding has ever been discussed with a physician or shown up in any documented medical event is unrecorded.
