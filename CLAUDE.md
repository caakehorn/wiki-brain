# Personal Wiki — second brain

This repository is a custom built wiki system which aims to be as exhaustive and detailed as possible  
in detailing everything about its creator, Dan Frank. 

It seeks to define and provide complete context for his life - biography, history, cognitive traits, ideology, tendencies and all other datapoints which point back to the real world individual. 

As an ongoing project, this wiki strives to gradually fill in any and all knowledge gaps about Dan, as well as continuously update with realtime information as time passes.  
## Why this is a second brain, not a RAG

A retrieval system keeps the sources and re-derives every answer from them on
demand; it never learns, and yesterday's reasoning is thrown away. This wiki is
the opposite. You read a source **once**, reason out what it *means*, and write
that understanding into `wiki/`. From then on you reason **from** the wiki, not
from `raw/`. Knowledge compounds: today's synthesized conclusion is tomorrow's
premise, and the wiki grows to reflect what has actually been read and
understood — a record of a shared journey through the data, not an index of it.

This has a hard consequence: the wiki is **not** a disposable cache of `raw/`.
Two kinds of content live here.

- **Derived** content — message counts, discographies reconstructed from
  slugs, anything mechanical — is safely regenerable from `raw/`.
- **Earned** content — a thesis, a psychological read, a conclusion cross-
  referenced from many sources ("the gaslighting outweighed the affair") — is
  the product of reasoning done once. `raw/` does not contain it literally, and
  re-running the pipeline may not reproduce it. This is the actual point of the
  system.

So **never regenerate an earned page from scratch — revise it.** Trust the
synthesis already on disk and build on it; when new raw contradicts it, apply
the contradiction/revision rules (flag and correct), you do not bulldoze it and
re-derive from zero. Pages may declare which kind they are with an optional
`knowledge: earned | derived | mixed` frontmatter field (see STYLE_GUIDE.md).

### The wiki is an input to itself (adopted 2026-07-26)

Reading raw once and writing it down is only the first half. The second half
is that **finished pages are premises**: a page may reason from other pages
rather than from `raw/`, declare that with `synthesizes:`, and become in turn
a premise for something above it. Ground pages carry entities and events;
junction pages carry the pattern across three or more of them; doctrine
carries the rule across junctions. That ladder is the product. A repository
of accurate ground pages with nothing above them is an archive, not a brain.

Two obligations come with it, both mechanical:

- **Premises that move make dependents stale.** If a page declares
  `synthesizes: [A]` and A is modified later, `bin/wiki-climb check` flags
  it. Clearing the flag means re-reading what changed and deciding whether
  the conclusion survives — revise, or record the falsification. Bumping
  `date_modified` to silence it is the one prohibited move in the system.
- **Conclusions must be falsifiable, and their failures are kept.** Pages
  state what they predict; when the corpus settles a prediction the
  resolution goes *on the page*, wrong ones included. This is the mechanism
  by which the wiki generates knowledge that exists in no source: a rule,
  broken by a case it did not anticipate, comes back wider.

Governing document: **`SYNTHESIS_SPEC.md`** (repo root), mandatory reading
alongside this file, `STYLE_GUIDE.md` and `CONNECTIONS_SPEC.md`.

## Connections & Strategy (adopted 2026-07-17)
**`CONNECTIONS_SPEC.md`, `SYNTHESIS_SPEC.md` and `STRATEGY.md` (repo root)
are mandatory reading** alongside this file. Connections between pages are TYPED EDGES with argued
claims (`connections:` frontmatter); bare `related:` lists and `## Related`
footers are deprecated and being retired page-by-page. When you touch any
page, write or refresh its `connections:` block per the spec, add inverse
edges on target pages, and run `bin/wiki-connect check` and `bin/wiki-climb check` next to
`bin/wiki-lint` before committing. `bin/wiki-connect candidates` maintains
`connection-queue.md`, the mined backlog of evidenced-but-unmade
connections; `bin/wiki-climb candidates` maintains `synthesis-queue.md`, the
backlog of clusters with no page above them.

## LLM Handoff & Coordination
**CRITICAL:** At the start of every session or turn, you MUST read `LLM_HANDOFF.md` in the root directory to understand the current project state, recent changes, and immediate priorities. When you end your session, you MUST update `LLM_HANDOFF.md` by logging what you accomplished and setting the focus for the next model. This ensures seamless continuity across different models and sessions.

## Architecture — plain files, one direction of flow

```
inbox/  →  raw/  →  wiki/          exports/ (generated, disposable)
typed &     immutable   compiled
uploaded    source      knowledge
```

- **inbox/** — staging. The human adds material here via `bin/capture` (typed
  facts/stories or copied files) or by dropping files in manually. On ingest,
  MOVE the file to the right `raw/` subdirectory, then synthesize. Never leave
  a file in both inbox/ and raw/.
- **raw/** — immutable source archive, organized `raw/<domain>/<collection>/`.
  Never modify or delete anything here except when filing from inbox/.
  **`raw/self/context-core/CONTEXT_CORE_EXPANDED.md` is the primary
  authoritative source for facts about Dan** — biography, timeline,
  psychology, relationships, ideology. It is curated and internally
  cross-checked (flags its own gaps and unresolved items explicitly,
  e.g. "do not speculate"), unlike the bulk chat/dossier exports, which
  are raw and sometimes self-contradictory. When starting work on any
  self/mind/timeline topic, check this file first before searching the
  wider raw/ corpus — its wiki counterpart is [[wiki/self/context-core]].
  Treat other raw sources as supplementary or corrective to it, not
  co-equal, unless they carry a specific dated correction it lacks.
- **wiki/** — the compiled product: accumulated understanding, not a cache of
  raw/ (see the second-brain principle above — earned pages are not
  regenerable). You own every byte. Domains: `self` (identity, core facts,
  digital footprint), `timeline`
  (periods & events), `people` (+ `people/contacts/` quarantine: auto-generated
  stubs, never linked from prose), `mind` (beliefs, ideology, psychology,
  values), `work`, `interests` (music production, favorites, taste),
  `health`, `places`, `legal` (disputes, property matters). Add a domain only
  when several pages clearly don't fit an existing one. `wiki/**/archive/`
  holds pinned oversized artifacts (status `archived`) — exempt from budgets,
  never updated.
- **exports/** — output of `bin/export-corpus`; never hand-edit, gitignored.
- **Meta files** (root): `index.md` master navigation, `log.md` append-only
  operation log, `queue.md` pending-ingest ledger, `connection-queue.md`
  mined edge backlog, `synthesis-queue.md` mined climb backlog.

Git is the history mechanism. Commit after every ingest with message
`<op>: <short description>`. Never commit secrets or exports/.

## Tools (bin/ — pure Python stdlib, no dependencies, no APIs)

- `bin/capture` — human-facing input: interactive typing/pasting, one-shot
  facts, file upload (`-f`), and `status` (inbox listing).
- `bin/wiki-climb` — altitude engine: `check` (validates `synthesizes:` and
  reports stale premises), `audit` (tier distribution, domains with no
  junction above them, load-bearing pages), `candidates` (writes
  `synthesis-queue.md`). See SYNTHESIS_SPEC.md.
- `bin/export-corpus` — concatenates the wiki (optionally raw/ and inbox/)
  into a single markdown file for LLM ingestion, with a token estimate.
- `bin/llm-publish` — builds `llm/`, the public LLM access point served by
  GitHub Pages: `llm/index.txt` (the one URL to hand any model — plain-text
  instructions + per-page URL manifest), `llm/corpus.txt` (whole wiki, one
  file), `llm/manifest.json`, and `llm/pages/**.txt` (one plain-text file
  per page; .txt bypasses Jekyll). Unlike exports/, **`llm/` is
  generated-but-COMMITTED** — rerun `bin/llm-publish` after any content
  pass and commit the diff so the published copy tracks the wiki.
  Entry point: `https://caakehorn.github.io/wiki-brain/llm/index.txt`.

## The operations

### INGEST — one source per pass, never parallel
**If you are given a general or unspecified instruction to "ingest," "do the
Phase B ingest," "keep going on the wiki," or any open-ended synthesis task —
READ `INGEST_RUNBOOK.md` (repo root) FIRST and follow it exactly.** That
file is the complete, reproduction-grade instruction for the cross-corpus
synthesis pass: environment facts, governance files to read, the per-pass
protocol, the frontmatter spec, the gotchas from prior sessions (including the
"verify derived numbers against raw — the operator will catch unverified
figures" rule), what's already done, and what remains. Do not improvise the
ingest workflow; the runbook IS the standing instruction.
Captured notes may carry `targets: [wiki/...paths]` in frontmatter (created by
typing `@page` in the app's Capture tab). A targeted note is a correction or
expansion of those specific pages: apply it there first (honoring the
contradiction/revision rules), then file the note into raw/ as usual.
Humans can also edit pages directly in the app; those edits appear in log.md
as `edit | <domain> | human edit via app` — treat them as authoritative
content but normalize formatting/frontmatter on the next pass over that page.
Parallel "swarm" ingests destroyed v1 (fragment prose, duplicate entities,
wrong statuses). Ingest ONE inbox item per pass, fully:
1. Move it from inbox/ to the right `raw/<domain>/<collection>/`.
2. Read it completely.
3. Put quantified data (dates, counts) into tables on the target pages.
4. Write or update the relevant wiki pages — typically the domain summary
   plus every person/event/concept the source touches.
5. Update the domain index and `index.md` if pages were added.
6. Update queue.md; append to log.md: `## [YYYY-MM-DD] ingest | <domain> | <source>`.
7. Commit.

Large exports (social media dumps, message CSVs) may take multiple passes;
track progress in queue.md rather than half-finishing silently.

### QUERY
Start at index.md, follow domain indexes, answer with citations to wiki
pages. Reason **from** the wiki first; only re-open `raw/` when the wiki is
silent on the question or a source is newer than the page that used it —
otherwise you are re-doing settled work. If the synthesis is new and durable,
save it as a page: that is how the brain grows, and it is what keeps the next
answer from re-deriving this one.

### CLIMB — the operation that raises altitude
The only operation that runs on `wiki/` rather than `raw/`. Where INGEST adds
ground, CLIMB builds above it: find a cluster of three or more pages spanning
two or more domains that share a shape and have nothing above them, find the
one rule true of all of them and false of the corpus generally, and write the
page that states it. **Full protocol in `SYNTHESIS_SPEC.md` — follow it
exactly; do not improvise a synthesis pass.** The short form:

1. `bin/wiki-climb candidates` maintains `synthesis-queue.md`, the mined
   backlog of unclimbed clusters. Take the top one, or one you have reason
   to prefer.
2. Read the member pages **in full** — you are reasoning from them.
3. Find the governing rule, **or reject the cluster in the queue with a line
   of reasoning.** A cluster that resists synthesis is knowledge too. Never
   write a page whose thesis is "these things are related."
4. Write it: `page_type: synthesis`, `knowledge: earned`, `synthesizes:`
   listing every member, thesis in the first two sentences, the rule stated
   plainly, the controls that carry it, at least one prediction, and Gaps.
5. Wire it with typed edges both ways per CONNECTIONS_SPEC.md.
6. All three gates at 0 errors; log `climb | <domain> | <page>`; commit.

Climb when a cluster has survived two or more ingests, or immediately when an
ingest makes you think "this is the third time I've seen this shape." Do not
climb to raise a number: three thin pages stacked make one thin page.

### LINT (periodic)
Sweep for: broken links, orphan pages, contradictions between pages, claims
superseded by newer raw data, entities mentioned 3+ times with no page,
pages over budget, and **stale premises** (`bin/wiki-climb check` — pages
whose `synthesizes:` inputs were modified after them). Fix mechanically what
you can; queue the rest. A stale page is never fixed mechanically: re-read
what changed in the premise before touching the dependent.

### IMPERATIVES, GENERALLY
Articles must be robust, exhaustive and thoroughly linked. They should be seen as very unique nodes and shouldn't follow more structure than what is listed in teh style guide


## Frontmatter (every wiki page — metadata only, no prose)

```yaml
---
domain: self | timeline | people | mind | work | interests | health | places | legal
page_type: entity | event | concept | period | summary | synthesis | profile | report | chat | note | index
status: active | stable | stub | closed | archived
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
sources: []    # real raw/ paths that exist on disk — bin/wiki-lint checks this
related: []    # wiki page paths
---
```

`active` = live situation · `stable` = accurate, settled · `stub` =
placeholder · `closed` = formally ended · `archived` = pinned artifact in an
archive/ dir, never update. Default for finished pages: stable, NOT archived.
**`closed` means a thing has formally ended, not that the page feels
finished** — the July 2026 reopening of `annie-ulmer.md`, marked closed six
weeks earlier, is the standing cautionary example. Run `bin/wiki-lint`,
`bin/wiki-connect check` and `bin/wiki-climb check` before committing any
ingest or climb.

## Writing rules (v1 failed by ignoring these)

**`STYLE_GUIDE.md` in the root is the binding page-format spec** (frontmatter
fields incl. optional title/aliases/tags/importance/changelog, LLM Quick
Brief convention, capture bracket-instruction handling). The rules below are
the short form; read the style guide before writing pages.

1. **Complete sentences.** No dossier shorthand or fragment chains. Every
   page must read as prose to a human opening it cold.
2. **Tables hold numbers, prose holds meaning.** Never repeat a table in prose.
3. **Paraphrase, don't transplant.** Verbatim source text stays in raw/;
   pages cite it. Quotes of one sentence or less allowed when the wording
   itself is the evidence.
4. **Page budget ~8 KB is a navigation heuristic, not a cap** (settled
   2026-07-18; STYLE_GUIDE substance rule 4 governs). The operator's
   standing preference is LONGER, denser entries. Lint size warnings are
   advisory on hub/junction/exemplar pages — never trim earned content
   to satisfy them; split only when navigation genuinely improves.
5. **Indexes are navigation only** — links plus one-line summaries. No
   session history or agent chatter anywhere in wiki/; that goes in log.md.
6. **One page per entity.** Before creating a people/ page, grep for the
   person under all known names and handles. Merge, never fork.
7. **Contradictions are flagged, not overwritten.** Inline
   `> **CONTRADICTION:**` blockquote; revisions get `> **REVISED [date]:**`.
8. **Dates are absolute.** Convert "last summer" to a year at ingest time,
   flagging uncertainty: `(~2019?)`.
