# CROSSLINK_CAMPAIGN.md — running the whole wiki through the source-mention pass

The CROSSLINK operation (`CLAUDE.md`) was written on 2026-09-04 against one
corpus and nineteen pages. This file is the plan for running it across the
**whole** repository, and it exists because that is not one session's work and
must survive being handed between models.

**Read `CLAUDE.md`'s CROSSLINK operation first.** This file is sequencing and
tooling; that one is the method, and nothing here overrides it.

---

## The situation, measured 2026-09-04

| | |
|---|---|
| wiki pages | **497** |
| typed edges | 2,666 |
| pages with **zero** typed edges | **106** (38 people, 29 interests, 18 self) |
| one-way edges owing an inverse | **77** |
| pages stating a **checkable limit about themselves** | **157** |
| substantial `raw/` corpora cited by pages | **8** |
| corpora `bin/wiki-crosslink` can read | **1** |
| pages that cite the twitter archive | **42** |
| pages the twitter archive **actually names** (`coverage`) | **20** |
| pages carrying no `aliases:` at all — the index's blind spot | **389** |
| pages with no unambiguous name at all (bare first names) | **99** (44 people) |
| cost of a scan / of `coverage` over the whole wiki | 0.38s per page / **1.7s** |

**Rows three to five are the whole problem.** Scanning is free — the entire
wiki triages in under two seconds. Reading is not. And until Phase 0 the tool
pointed the reading in the wrong direction, while the index could not see 389
of the pages it was supposed to be finding.

---

## Four findings from Phase 0, two of which corrected this file's own estimates

### 1. `scan` read only corpora a page already cites, which was backwards — fixed

`scan_page` took the page's own `sources:` and kept the ones it had a reader
for, so a page was checked against the corpora it was **already built from**.
Every finding in the pilot came from the opposite move.

`scan --against <corpus>` now exists. But the first run of it returned *the
same candidate list for every page*, because a date range is not a scope: a
person's page spanning 2009–2025 matches every entity in seventeen years.
Against mode now first finds the rows that **name the page itself**, and looks
only inside those — "in what this corpus says about X, what else does it
name?", which is the question the obligation is actually about.

A page whose names never appear returns *"the corpus is silent on it"* in
milliseconds. That is a real negative and it is most of the answers.

### 2. The value is concentrated and the concentration is measurable

157 pages make a checkable claim about their own limits — "the complete
record", "everything known arrives through", "no ledger entries at all and
remains description". Every pilot finding landed on such a page, and four
falsified the claim outright.

`scan` now ranks candidates by the **target's** self-limit score, and
`--queue` orders the whole wiki by it. Before this, scanning the concert
record put Katie Fletcher (7 self-limit claims) below 82 SLOPPP mentions.

### 3. **Correction — "184 pages unlocked" was wrong. It is 20.**

This file first estimated the `--against` unlock at 184 pages, from date-range
overlap with the twitter archive. Overlap is not mention. Running
`coverage` across all 497 pages: **20 are actually named by the archive**,
eight of which do not cite it. The rest overlap in time and the corpus says
nothing about them.

**The twitter archive is close to exhausted**, which the pilot's yield already
hinted at. That is good news for sequencing — it means the corpus is done, not
that the campaign is small — but this file said otherwise and the number was
never checked before it was written down.

### 4. **The real bottleneck is `aliases:`, and it is missing on 389 pages**

Matching is exact-phrase on a page's title, and a title is almost never how a
thing is written in a source.

`wiki/interests/opie-and-anthony` is the worked case. The archive names it
**61 times** — `o&a` 8, `opie` 25, `cumia` 10, `@OpieRadio` 18 — and the exact
string *"opie and anthony"* appears **zero** times. `coverage` therefore
reports the corpus silent on it, which is a false negative produced entirely
by missing frontmatter.

**395 of 497 pages carry no aliases at all.** Every corpus reader built from
here on inherits this blindness, so populating `aliases:` is worth more than
any further work on the matcher, and it must come before the readers rather
than after. `bin/wiki-crosslink entities --missing` is the list, ranked so
that multi-word titles — the ones sources abbreviate — come first.

### The false-positive rate, unchanged and still the reason to triage

Of roughly 240 pilot candidates, about 29 were high-confidence and ~20
actionable — **under 10%**. Single-token names ("Rick" → Rick Santorum, "Tom"
→ Tom Cruise, "slim" → slim jims) were near-100% noise. High confidence is now
the default and `--low` opts in.

## Phase 0 — the instrument — **DONE 2026-09-04**

- `scan --against <corpus>`, scoped by the page's own names rather than by its
  date range. The date-range requirement was dropped once the name filter made
  it redundant; it was blocking 246 pages for nothing.
- High confidence by default, `--low` to opt in.
- Candidates ranked by the target's self-limit score; `--queue` orders the wiki.
- `coverage` — which readable corpora actually name a page. 1.7s for all 497,
  and it is the triage step: run it before scanning, because most page/corpus
  pairs are silent.
- `entities --missing` — the 389-page alias gap.
- **The moratorium is a refusal, not a warning**, and deliberately narrower
  than `bin/wiki-plain`'s: scoped to her own pages by title and alias, because
  porting that tool's body-mention threshold across would refuse 197 of 497
  pages — `interests/golf`, `self/tattoos`, `music/aliases/sloppp` — for no
  safety gained. The rest of the directive constrains what a session *writes*,
  and `scan` prints that reminder on any page naming her.
- **A parsing bug fixed that predated all of this.** `aliases: ["Lex",
  "@alexisarmel"]` kept the quotes on every entry after the first, so every
  quoted `@handle` was silently demoted to a low-confidence single token. It
  cost 83 of 84 matching rows on one page.

**Two items deferred with reasons, not dropped.** `crosslink report` (a derived
campaign page) and `crosslink audit` (the fabrication referee — every dated
quote in a claim must appear verbatim in the corpus it cites) are both still
right. Neither is the blocker: the audit matters once there is volume to
police, and there is not yet; and a campaign page that reports on a campaign
which cannot see 389 of its own pages would mostly report the blindness.
**Aliases first.**

## Phase 0.5 — populate `aliases:` — **the new first content task**

389 pages, none of which the index can find under any name but their exact
title. This is the cheapest work in the campaign and it gates everything after
it. Worked by `entities --missing`, multi-word titles first, and it is ordinary
page editing rather than a new operation.

The test for an alias is not "what could this be called" but **"what does the
record actually call it"** — `o&a` and `@OpieRadio` are aliases because they
appear in the corpus; "the Opie and Anthony Show" is not, because nothing
writes that.

## Phase 1 — drain the 77 one-way edges

No searching required to find them; `bin/wiki-crosslink reciprocal` prints the
list. Each still needs reading to write a claim that carries the finding rather
than pointing at it. This is the cheapest real value in the repository and it
is already computed.

## Phase 2 — corpus readers, in citation order (after 0.5, not before)

Each reader inherits its corpus's known traps. **A reader written without them
produces confident wrong candidates**, which is worse than no reader.

| Order | Corpus | Pages citing | The traps it must carry |
|---|---|---|---|
| 1 | `message-csv/MASTER_MESSAGES_DB_DUMP.csv` + `dox-scan/all_imessages_complete_dump.txt` | **106 + 93** | the three properties in `bin/mine-messages`' docstring; two forms of one corpus, so dedupe or double-count |
| 2 | `concerts/table.csv` | 48 | already joined once by hand; rows 6/16/17/24 still open |
| 3 | `favorites/FAVS MASTERLIST.csv` | 40 | 43 artist pages downstream |
| 4 | `gemini-activity/Gemini Activity.html` | 28 | 21.8 MB of HTML; T2 source, `skills/corpus/source-chain.md` governs |
| 5 | `facebook/facebook-ihatedanfrank/` | 20 | a directory of HTML, not a file |

**The message dump is first by a distance** — 199 page-citations, and
`wiki/interests/music/overview` carries absence claims derived from it that
have never been checked either way.

## Phase 3 — the passes, worked by value

1. The **157 self-limiting pages**, densest first (13 hit three or more
   categories; `wiki/timeline/master-timeline` hits five).
2. The **106 zero-edge pages** — 38 of them people. These are not islands
   because nothing connects to them; they are islands because nobody ran this.
3. Everything else, opportunistically, when a session is in the neighbourhood.

**Never as a sweep.** One page per pass, fully, exactly as INGEST works.

---

## The honest limit: this cannot be handed to a cheap unattended agent

`plain/` has a free lane because `bin/wiki-plain audit` is arithmetic — a
number in the twin that appears nowhere in the page is a fabrication, and a
grade level is a measurement. The tool has the last word and the model cannot
argue with it.

**Crosslinking does not decompose that way.** Its two failure modes are:

- **Fabrication** — a quote or date that is not in the corpus. *Mechanically
  catchable*, and Phase 0.5 above is the check.
- **Judgment** — writing an edge from a false-positive match, or promoting a
  mention to a relationship. A tweet naming Diplo is a music-consumption
  datapoint, not a Diplo relationship. This failure produces **plausible,
  well-formed, correctly-cited prose**, and no arithmetic over two files
  detects it.

The second is the whole job. So the referee bounds the damage; it cannot
replace the reader, and this campaign has no free lane. Anyone proposing one
should be asked what would catch a confidently-written edge about the wrong
Rick.

## What this costs, plainly

The pilot was 19 pages against 1 corpus: ~35 edges, 6 real findings, four
falsified self-claims, one long session.

Revised after Phase 0, and the shape changed more than the total:

| | |
|---|---|
| Phase 0.5, aliases on 389 pages | 3–5 sessions — mechanical, batchable, gates everything |
| Phase 1, the 77 one-way edges | 2–3 sessions |
| Phase 2, four corpus readers | 1 session each, plus the message dump's traps |
| Phase 3, the passes | the long tail |

**Still fifteen to twenty-five sessions**, but the front of it is now cheap
mechanical work rather than reading, which was not true when this file was
first written. Worth saying up front so a session producing four edges and one
finding is understood as on pace rather than as a bad day.

**And the twitter corpus is nearly done** — 20 pages named, most already
worked. A session looking for volume should go to Phase 0.5, not back to the
archive.

## Logging

`connect | <domain> | <source> → <N pages>` per `CLAUDE.md`. The campaign page
is derived from those commits, which is why the prefix is load-bearing here and
not merely a convention.
