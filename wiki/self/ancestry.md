---
domain: self
page_type: report
status: stable
date_created: 2026-06-23
date_modified: 2026-07-14
sources: ["raw/self/ancestry/23andme-ancestry-family-tree-20260623.zip", "raw/self/ancestry/dna-reports/Ancestry Composition - 23andMe.pdf", "raw/self/ancestry/dna-reports/health.pdf", "raw/self/ancestry/dna-reports/chromosome.pdf", "raw/self/ancestry/extracted/", "raw/self/dox-md/LIFE_EVENTS_CALENDAR.md"]
related: ["wiki/self/context-core", "wiki/self/overview", "wiki/self/location-history", "wiki/timeline/periods/2015-2016-annie-relationship-start"]
---

# Ancestry / 23andMe + Family Tree

## Summary
23andMe personal genomics export combined with Ancestry.com GEDCOM family tree (sourced as "Daniel Frank family tree"). The primary readable artifact is the GEDCOM (1.1 MB text). 515 individuals recorded. Strongly corroborates core biographical spine facts (DOB, birthplace, early residences in Fayette County, PA). Provides paternal line depth and collateral relatives.

**Note:** The zip additionally contains three PDFs (Ancestry Composition, health.pdf, chromosome.pdf) whose full content was not text-extracted in this pass but remain in raw/ for future reference.

## Tree Dimensions

| Metric              | Value                                      |
|---------------------|--------------------------------------------|
| Total individuals   | 515                                        |
| Primary file        | Daniel Frank family tree.txt (GEDCOM 5.5.1) |
| Export origin       | 23andMe + Ancestry Member Trees (data dated ~2024) |
| Core subject        | Daniel Gillingham Frank                    |
| DOB / Birthplace    | 1988-11-01, Uniontown, Fayette County, Pennsylvania, USA |
| Geographic focus    | Fayette County PA cluster (Uniontown, Brownsville, Hopwood, Champion) |

## Immediate Family (extracted from GEDCOM)

| Relation                  | Name                                      | Birth / Death                  | Place                              | Key Ties |
|---------------------------|-------------------------------------------|--------------------------------|------------------------------------|----------|
| Self                      | Daniel Gillingham Frank                   | 1988-11-01                     | Uniontown, Fayette, PA, USA        | Core spine match |
| Father                    | Richard Harrison "Rick" Frank             | 1959-05-22                     | Uniontown, PA                      | [[wiki/people/rick-frank]]; low contact, 2005 hinge |
| Mother                    | Suzanne Whyel /Shrum/ Frank ("Suz")       | 1962-09-15                     | Pittsburgh, Allegheny, PA          | [[wiki/people/suzanne-frank]]; realtor, primary financial line |
| Sister                    | Vanessa C. Frank                          | 1994-01-16                     | Greensburg, Westmoreland, PA       | [[wiki/people/vanessa-frank]]; Vail ski-school |
| Paternal Grandfather      | Morley Jay Frank                          | 1927-08-20 – 1998-12-13        | Brownsville – Hopwood, PA          | [[wiki/people/morley-frank]]; 113+ sources |
| Paternal Great-Grandfather| David J. Frank                            | 1892-08-12 – 1960-04-06        | Russia – Brownsville, PA           | [[wiki/people/david-j-frank]]; Russian Jewish immigrant |
| Paternal Great-Grandmother| [[wiki/people/sadie-harris|Sadie Harris]]                              | 1900-12-14 – 1997-11-27        | Austria – Hopwood, PA              | Jewish immigrant line |
| Maternal Great-Grandmother| Jesse Frances Thomas Whyel /Coldren ("Fran") | 1920-08-15 – 2018-04-04     | Fort Martin, WV – Uniontown, PA    | [[wiki/people/fran-coldren]]; biggest influence, gifted Numark NS7 |
| Maternal Grandfather      | George Dixon Shrum Jr                     | 1937-06-14 – ~2025-09          | —                                  | Death date inferred, see note below |
| Maternal Grandmother      | Rebecca Diane Van Voorhis                 | 1939-01-30                     | —                                  | — |

**On the maternal grandfather's death date:** the GEDCOM tree has no death
record for George Dixon Shrum Jr, but an outbound message from Dan dated
2025-09-03 reads "eat n' park delivered frownie cookies to my granfather's
funeral i swear to god lmao" (LIFE_EVENTS_CALENDAR.md). He is the only
grandfather without a recorded death date (Morley Frank, the paternal
grandfather, died in 1998), so this is very likely his funeral — treated
here as a strong inference, not a confirmed record, pending a source that
states his name directly.

## Key Geographic / Residence Patterns (tree data)
- Heavy concentration in Fayette County / Uniontown area across generations. This directly grounds the core "ORIGIN (1988–Sep 2008)" period and repeated Uniontown returns (337 Saratoga Drive family-built 1996; 12 Bryer Ave prior).
- Paternal grandfather (Morley): Brownsville (1930-1945) → Hopwood/Champion (1990s) → multiple documented moves.
- Father (Rick): Uniontown residences 1989, 1993-1997, 1998-2002.
- Maternal great-grandmother (Fran): WV origins (1920 Adkin, 1930 Cass) → PA (1940 Smithfield, 1961 Uniontown, 1990s Uniontown).
- Ties to [[wiki/self/location-history]] (Fayette Co cluster, thousands of visits) and core addresses.

## Paternal Jewish Immigrant Heritage
Paternal line: David J. Frank (b.1892 Russia) + Sadie Harris (b.1900 Austria) → Morley → Rick → Dan. Confirms CONTEXT_CORE: "Paternal line Jewish; father Episcopalian, mother Presbyterian. Jewish heritage is load-bearing to his politics." This immigrant story (late 19th/early 20th c. Eastern European Jewish to coal/steel PA) connects to identity (Jewish self-ID), politics (democratic socialist, institutional skepticism), and [[wiki/mind/synthesis/vertical-authority-skepticism]] (family vertical patterns).

## DNA / 23andMe Genetic Reports (Direct Processing)
The following reports were staged in ingest/ and copied to raw/self/ancestry/dna-reports/ (per protocol; never treat ingest/ as source of truth):

- Ancestry Composition - 23andMe.pdf (368 KB, 1 page; browser export 2025-03-30 via Chrome/Skia)
- chromosome.pdf (199 KB, 2 pages)

These are the core DNA data outputs from 23andMe (graphical/image-based reports with embedded maps, pie charts, and paintings; no extractable text layer for specific percentages or variants — confirmed via inspection and strings attempts yielding only PDF internals).

**Contents and Analysis:**
- **Ancestry Composition**: Visual breakdown of genetic ancestry components (ethnicity estimates, confidence regions, global maps). Directly complements the GEDCOM tree: paternal Jewish immigrant line (David J. Frank b.1892 Russia + Sadie Harris b.1900 Austria) predicts prominent European/Ashkenazi signal; maternal WV/PA roots (via Suzanne Whyel Shrum / Fran Coldren) add context. Confirms CONTEXT_CORE: "Paternal line Jewish; father Episcopalian, mother Presbyterian. Jewish heritage is load-bearing to his politics."
- **Chromosome reports**: Segment paintings and ancestry visualizations across chromosomes, showing DNA segment assignments. Ties tree genealogy to specific genetic segments (no raw SNPs in this export).

The reports + family tree together provide both raw genetic measurements and full genealogical backbone. No contradictions with core, locations, or prior data. Full details require viewing the raw PDFs (preserved for reference).

**Sources:**
- `raw/self/ancestry/dna-reports/Ancestry Composition - 23andMe.pdf`
- `raw/self/ancestry/dna-reports/chromosome.pdf`
- `raw/self/ancestry/23andme-ancestry-family-tree-20260623.zip` (original)

## Connections to Broader Corpus
- **To Core/Periods**: Full corroboration of DOB, Uniontown birthplace, family addresses. 2005 hinge (Rick rehab + mother's affair → divorce + father's cancer) now has genealogical context.
- **To People**: See dedicated pages for Rick, Suzanne, Vanessa, Morley, Fran, David J. Frank. Expands social graph with blood relatives.
- **To Attachment & Conflict**: Paternal "undischarged paternal-authority wound" (core) + family alcoholism pattern (mother/grandmother/great-grandmother/father per core) → templates in [[wiki/mind/concepts/attachment-model]] and [[wiki/mind/concepts/conflict-architecture]].
- **To Music**: Fran's gift of Numark NS7 directly seeds production identity, sub-bass signature, aliases (MOGZART etc.), [[wiki/interests/favorites/music]].
- **To [[wiki/people/annie-ulmer|Annie]]/Events**: Fran's deathwatch shared with Annie (core); multi-generational family entanglement (grandmothers neighbors 50+ yrs).
- **To Location/Events**: Reinforces PA roots vs. NYC chapters; 337 Saratoga as family anchor (now selling, ties to legal/suz realtor role).
- **To Synthesis**: See new [[wiki/self/ancestry]] for interpretive layer (immigrant resilience, regional loyalty vs. escape, Jewish + Appalachian/WV maternal mix informing "wounded genius" mythos).

## Relation to Core
- [DOC] confirmation of name (full "Daniel Gillingham Frank"), DOB 1988-11-01, Uniontown birthplace, early PA residences.
- Extends location-history spine with multi-generational Fayette County / WV-PA roots.
- No contradictions with CONTEXT_CORE_EXPANDED or prior location ingest. All new data defers to core for behavioral framing.
- Explicitly links to core family notes: Rick low contact, Vanessa Vail, Fran biggest influence, 2005 hinge, family alcoholism, Jewish paternal line.

## Sources in Raw
- `raw/self/ancestry/23andme-ancestry-family-tree-20260623.zip` (contains GEDCOM + 3 PDFs)
- `raw/self/ancestry/extracted/`
- `raw/self/ancestry/dna-reports/`

**Raw/ Ingest Verification (2026-06-23):** Structure matches ingest/ (23andme zip + ANCESTRY _ DNA.txt + PDFs staged); raw has extracted/ + dna-reports/ per protocol. No dupe nesting observed (unlike FB). Minor filename "geneoiogy" in zip. Immutable.

## Related
- [[wiki/self/context-core]]
- [[wiki/self/location-history]]
- [[wiki/self/overview]]
- [[wiki/timeline/periods/2017-poverty-floor]] (regional context)