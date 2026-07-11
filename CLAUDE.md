# Personal Wiki — second brain

This repository is a lifelong personal wiki for Dan Frank: complete biographical
history, psychological and ideological profile, relationships, and everything
else about his personhood that can be stored as text. The human drops sources
in; the agent (you) compiles knowledge out. You are the maintenance agent.

A prior version of this project lives at `~/wiki project` (marked failed).
Its raw archive, compiled pages, and pending inbox were migrated here on
2026-07-11 — treat that directory as read-only reference; nothing new
should be filed there.

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
- **wiki/** — the compiled product, all regenerable from raw/. You own every
  byte. Domains: `self` (identity, core facts, digital footprint), `timeline`
  (periods & events), `people` (+ `people/contacts/` quarantine: auto-generated
  stubs, never linked from prose), `mind` (beliefs, ideology, psychology,
  values), `work`, `interests` (music production, favorites, taste),
  `health`, `places`, `legal` (disputes, property matters). Add a domain only
  when several pages clearly don't fit an existing one. `wiki/**/archive/`
  holds pinned oversized artifacts (status `archived`) — exempt from budgets,
  never updated.
- **exports/** — output of `bin/export-corpus`; never hand-edit, gitignored.
- **Meta files** (root): `index.md` master navigation, `log.md` append-only
  operation log, `queue.md` pending-ingest ledger.

Git is the history mechanism. Commit after every ingest with message
`<op>: <short description>`. Never commit secrets or exports/.

## Tools (bin/ — pure Python stdlib, no dependencies, no APIs)

- `bin/capture` — human-facing input: interactive typing/pasting, one-shot
  facts, file upload (`-f`), and `status` (inbox listing).
- `bin/export-corpus` — concatenates the wiki (optionally raw/ and inbox/)
  into a single markdown file for LLM ingestion, with a token estimate.

## The operations

### INGEST — one source per pass, never parallel
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
pages. If the synthesis is new and durable, save it as a page.

### LINT (periodic)
Sweep for: broken links, orphan pages, contradictions between pages, claims
superseded by newer raw data, entities mentioned 3+ times with no page,
pages over budget. Fix mechanically what you can; queue the rest.

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
Run `bin/wiki-lint` before committing any ingest.

## Writing rules (v1 failed by ignoring these)

1. **Complete sentences.** No dossier shorthand or fragment chains. Every
   page must read as prose to a human opening it cold.
2. **Tables hold numbers, prose holds meaning.** Never repeat a table in prose.
3. **Paraphrase, don't transplant.** Verbatim source text stays in raw/;
   pages cite it. Quotes of one sentence or less allowed when the wording
   itself is the evidence.
4. **Page budget ~8 KB.** Bigger means it is two pages.
5. **Indexes are navigation only** — links plus one-line summaries. No
   session history or agent chatter anywhere in wiki/; that goes in log.md.
6. **One page per entity.** Before creating a people/ page, grep for the
   person under all known names and handles. Merge, never fork.
7. **Contradictions are flagged, not overwritten.** Inline
   `> **CONTRADICTION:**` blockquote; revisions get `> **REVISED [date]:**`.
8. **Dates are absolute.** Convert "last summer" to a year at ingest time,
   flagging uncertainty: `(~2019?)`.
