# Style Guide — Personal Wiki

The binding rules for every page in `wiki/`. CLAUDE.md holds the operating
process (ingest/query/lint); this file holds the page format. When the two
disagree, this file wins on formatting, CLAUDE.md wins on process.
`bin/wiki-lint` mechanically enforces the vocabularies below — run it before
every commit.

## Frontmatter

Required fields, in this order:

```yaml
---
domain: self | timeline | people | mind | work | interests | health | places | legal
page_type: entity | event | concept | period | summary | synthesis | profile | report | chat | note | index
status: active | stable | stub | closed | archived
date_created: YYYY-MM-DD
date_modified: YYYY-MM-DD
sources: []    # real raw/ paths that exist on disk
related: []    # wiki page paths (no .md extension needed)
---
```

Optional fields (adopted 2026-07-11 — use when they add value, never
invent new ones):

```yaml
title: "Human Title"        # when the filename isn't the natural title
aliases: ["nickname", ...]  # alternate names/handles for search & dedupe
tags: [topic, topic]        # cross-domain topical hooks
importance: critical | high | normal   # triage for LLM context budgets
knowledge: earned | derived | mixed    # is this regenerable from raw/?
changelog:                  # only on critical pages; newest first
  - date: YYYY-MM-DD
    note: "one line"
infobox:                    # Wikipedia-style right-hand box; rendered only if present
  name: "Display Name"      # header of the box
  # any of: born, born_date, status, type, aliases, occupation, known_for,
  # relationship, partner, parents, location, duration, outcome, discovered,
  # closed, diagnosis, medication, ideology, affiliation, period, notes
  # values may contain [[wikilinks]]; they render as real links
image: self                 # optional: override the auto illustration
                             # (domain/type default). Name of assets/img/<name>.svg
                             # (no real photographs are used anywhere in the wiki)
---

**`knowledge`** marks what kind of understanding a page holds, so a future
agent knows whether re-deriving it from `raw/` would lose anything (see
CLAUDE.md, "Why this is a second brain, not a RAG"):

- `derived` — mechanical compilation (counts, catalogs, timelines built from
  slugs). Safely regenerable from `raw/`.
- `earned` — a conclusion reasoned to once, not present literally in `raw/` (a
  thesis, a psychological read, a cross-referenced judgment). **Revise these,
  never regenerate them from scratch.** `page_type: synthesis` and most
  `concept` pages are earned.
- `mixed` — both (most people/event pages: derived tables carrying an earned
  read). Treat the earned prose as earned.

The field is optional; an absent value means `mixed`. `bin/wiki-lint` rejects
any other value.

**`tags`** — controlled vocabulary, applied wiki-wide 2026-07-14. Reuse
these rather than inventing new ones; if a page genuinely needs a tag
outside this list, add the tag to this list too so it stays a closed set.
2-5 tags per page, most-relevant first.

```
relationships, trauma-bond, infidelity, attachment, family,
addiction-recovery, mental-health, physical-health, grief,
legal, dui, financial-stress, housing, career,
music-production, personality-profile, ideology, politics,
forensic-analysis, ai-collaboration, digital-footprint,
uniontown-era, nyc-era, pets
```

There is **no** `author-stub` / `artist-stub` / other invented page_type: a
stub is `page_type: entity` (or the appropriate type) with `status: stub`.

## Status vocabulary

`active` = live situation, expect updates · `stable` = accurate, settled ·
`stub` = placeholder awaiting real content · `closed` = formally ended ·
`archived` = pinned artifact in an `archive/` dir, never updated, exempt
from budgets. Default for a finished page is `stable`, not `archived`.

## Substance rules (these outrank everything below)

A page is not good because it is tidy; it is good because it tells you what
matters. The failure mode of this wiki's early drafts was **inventory
masquerading as insight**: message counts and source citations up top,
while the actual story — who this person is to Dan, what actually happened,
why it mattered — was buried or missing.

**The first paragraph test.** After the title, the first paragraph must
answer, in plain language, the question a stranger would ask:

- **Person:** Who is this to Dan, what is the current state of the
  relationship, and what one thing defines it? (Corpus statistics come
  LAST, never first.)
- **Event:** What happened, when, who was involved, and what changed
  because of it?
- **Period:** What years, what defined daily life then, and how did it
  begin and end?
- **Concept/synthesis:** State the thesis in one or two sentences, then
  prove it. Not "this page collects material about X."

**Consequence over chronology.** Order sections by importance, not by the
order sources were ingested. If the Eli incident is why the Annie
relationship ended, it appears on page one of annie.md, not as row 14 of a
timeline table.

**Say the load-bearing thing plainly.** If the sources support "she
gaslit him for months and the gaslighting hurt more than the affair,"
write that sentence. Do not scatter it across evidence fragments and hope
the reader assembles it. Attribute contested claims to their source; flag
genuine contradictions; but do not hedge documented conclusions into mush.

**Gaps are content.** If something important is unknown (why the 2021–22
corpus goes near-silent, where he'll live after the house sells), say so
in a **Gaps** line rather than silently omitting the topic.

**Exemplars:** `wiki/people/annie.md`, `wiki/people/suz.md`, and
`wiki/timeline/events/eli-incident.md` show the standard. Before rewriting
any page, read the exemplar of the same page_type and match its shape:
lead paragraph that answers the stranger's question, consequence-ordered
sections, tables holding only numbers, a Gaps section naming the unknowns.

## Prose rules

1. **Complete sentences.** No dossier shorthand, no fragment chains. A page
   must read as prose to a human opening it cold.
2. **Tables hold numbers, prose holds meaning.** Never narrate a table's
   contents in the surrounding text.
3. **Primary-source voice belongs on the page.** Verbatim first-person
   material from a subject (their own accounts, essays, correspondence)
   is an exception to the old "quote ≤1 sentence / keep verbatim in raw/"
   rule: when the subject's own wording carries the meaning, it goes on the
   page as a block quote, not paraphrased away. Other sourced verbatim
   still prefers raw/ with short citation, but a subject's own voice is
   primary-source evidence and may be quoted at length.
4. **Page budget is a soft floor, not a hard ceiling.** Articles should be
   as long as the subject earns. Short, choppy pages are a failure mode;
   prefer dense, narrative, fully-developed prose. Split only when a single
   page would become unwieldy for navigation — not to hit an arbitrary size.
5. **No agent chatter anywhere.** No session notes, ingest logs, "/tmp/"
   paths, model names, or "this pass did X" — that history lives in log.md
   and the git log only.
6. **One page per entity.** Grep for every known name/handle/alias before
   creating a people page. Merge, never fork.
7. **Contradictions are flagged, not overwritten:** inline
   `> **CONTRADICTION:** ...` blockquote. Corrections get
   `> **REVISED [YYYY-MM-DD]:** ...`.
8. **Dates are absolute.** Convert relative time at write time; flag
   uncertainty as `(~2019?)`.

## LLM Quick Brief

Pages marked `importance: critical` should open (after the intro paragraph)
with an `## LLM Quick Brief` section: one dense paragraph written for
direct context injection — who/what this page covers and the load-bearing
facts, self-contained, with wikilinks. Keep it under 200 words. Do not add
briefs to ordinary pages.

## Linking

- Wikilinks use full repo-relative paths without extension:
  `[[wiki/people/annie]]`. Directory links (`[[wiki/people/contacts/]]`)
  are allowed when the directory exists.
- Every non-index page must be reachable from its domain index (the lint
  orphan check enforces this).
- `wiki/people/contacts/` is quarantine: auto-generated stubs, never linked
  from prose. Promote a contact to a real page (move it out of contacts/)
  once it's mentioned 3+ times in prose or the user asks.

## Capture-note handling (ingest)

Captured notes may carry `targets: [wiki/...]` (from @-mentions) — apply
the note to those pages first. Square-bracket lines like
`[RENAME PAGE TO x]` are **operator instructions to the ingesting model**,
not content: execute them (honoring all rules above, e.g. link updates on
rename), and do not copy the bracket text into any page. The note still
gets the full synthesis treatment and is filed into raw/ afterward.
