---
domain: self
page_type: concept
title: "The Wiki-Brain"
aliases: ["wiki-brain", "the wiki", "second brain", "the repository"]
status: active
knowledge: earned
date_created: 2026-08-19
date_modified: 2026-08-19
importance: critical
tags: [ai-collaboration, digital-footprint, personality-profile]
sources:
  - "STRATEGY.md"
  - "CLAUDE.md"
  - "STYLE_GUIDE.md"
  - "CONNECTIONS_SPEC.md"
  - "EXTRACTION_SPEC.md"
  - "SYNTHESIS_SPEC.md"
  - "LLM_HANDOFF.md"
connections:
  - page: wiki/self/dan-frank
    type: instantiates
    claim: "The wiki-brain is the externalized model of Dan Frank's mind — every person, event, and connection mapped as his brain has registered them."
  - page: wiki/mind/synthesis/block-unblock-loop
    type: instance-of
    claim: "The block-unblock-loop is one of the wiki's highest-altitude findings — a pattern discovered across multiple relationships that no single source states."
  - page: wiki/people/annie-ulmer
    type: evidences
    claim: "The Annie page is the wiki's most-read case study, the one that tests whether the system can model a single relationship across 17 years of primary sources."
  - page: wiki/self/message-corpora/source-coverage-index
    type: component-of
    claim: "The source-coverage-index is the wiki's instrument panel — it tracks what the corpus can and cannot see, and flags the silent failures."
---

# The Wiki-Brain

The wiki-brain is a second brain about one person, Dan Frank. It is a custom-built knowledge repository that collects, stores, and synthesizes every available datum about his life, mind, history, ideology, environment, and relationship to reality — every story, every friend, every place, every perspective, every development, every thought. Its job is not to archive but to **mine one life for hidden connections**: linkages between people, events, money, substances, music, work, and psychology that no single source states, but that the corpus proves when read across itself.

It is built on plain files, one direction of flow: `inbox/` → `raw/` → `wiki/` → `caakehorn/home` public/wiki/. Material arrives via capture or drop, is filed immutably into `raw/`, is read to exhaustion, and the understanding extracted is written into `wiki/` as prose pages. From then on, reasoning happens FROM the wiki, returning to `raw/` only when the wiki is silent or a claim needs primary verification. The portal (`caakehorn/home`) renders the wiki as a static site, but its `public/wiki/` is a derived snapshot regenerated hourly — anything written there is destroyed within the hour. Pages are `wiki/**.md`, never JSON.

## The core loop

The system runs on one repeating cycle: **Story → Entry → Analysis → Synthesized finding → Saved back to every entry it touches → Repeat.**

1. A memory, fact, or document is captured once and filed immutably into `raw/`.
2. It's read from `raw/` **to exhaustion**, and that understanding is written into a `wiki/` page — a ground-floor entry.
3. Once enough ground entries exist, they're read *across* each other — not one at a time — looking for a pattern that no single entry states but that several together prove.
4. That pattern becomes its own finding: a synthesis, stated as a falsifiable claim, not a vague observation.
5. The finding is written back into **every ground entry it draws from**, via a typed connection with an argued claim — so the insight doesn't have to be re-derived the next time someone lands on that entry.
6. The finding itself becomes a premise for the *next* round: junctions can be read across each other to find doctrine, the same way ground entries were read across each other to find junctions.

This is **amortized insight**. Analysis is expensive to do well, so it's done once, saved at every point it's relevant, and each future pass starts from a higher floor instead of re-deriving what's already known.

## The altitude ladder

The product isn't flat. Every conclusion written today is a **premise** available tomorrow:

- **T0** — Immutable source: `raw/` files.
- **T1** — Ground page: one entity, event, period, or place, read out of `raw/`.
- **T2** — Junction page: one pattern found across 3+ ground pages, spanning 2+ domains.
- **T3** — Doctrine: one rule found across 2+ junctions, domain-general.

Each layer declares its `synthesizes:` list, naming exactly what it was built from, so the dependency chain is visible, checkable, and stays current when something below it changes. The loop is meant to run forever: ingest raises the floor, CLIMB raises the ceiling, and the new ceiling becomes the floor for the next climb. A repository of accurate ground pages with nothing built on top of them is an archive. **The altitude is the brain.**

## The sources

The wiki draws from a finite, immutable archive of primary and AI-secondary sources:

**Primary** — records of what happened. Message dumps and per-thread exports; the GEDCOM; `contacts.csv` and the Facebook address book; Goodreads, YouTube, Twitter and Facebook takeouts; the Gchat archive; photographs and documents.

**AI-secondary** — a model reasoning about the corpus. The Gemini and ChatGPT sessions under `dox-md/`, `THE_DAN_FRANK_BOOTLOADER.md`, `THE_DAN_FRANK_MANUAL.md`, `CATO_*`, `DANSYNTH.txt`, the profile dumps. Dan's own words inside a session are primary testimony; the model's factual assertions are not evidence.

**The spine** — `raw/self/context-core/CONTEXT_CORE_EXPANDED.md` sits above both tiers: curated, internally cross-checked, explicit about its own gaps. It is the single most authoritative raw source for facts about Dan.

The corpus is 217,573 messages across 503 handles, 106,629 sent / 110,944 received. It is 9.6x duplicated — a feature, not a bug: the Rick correction and the `sic semper` inversion were each found by one export contradicting another. Consolidating would destroy the only error-detection the corpus has.

## Dan's role

Dan Frank is the architect, the operator, and the subject. He built the system, he governs its operations, and he is the person it models. He answers gaps directly, corrects the wiki's errors, and supplies the raw material — but the wiki is not a monument to him. It is a map of his own mind, and the people in it appear only as his brain has registered them. The distinction matters: the wiki is about the mapper, not the mapped.

## What it's building towards

The wiki-brain is building towards a comprehensive model of one mind — not a static archive but a living system that compounds insight over time. Its current campaigns run in parallel:

**Depth (extraction).** The binding constraint. Sources already marked ingested routinely turn out to hold three times what the first pass took, and the leftovers are not marginal — they are the findings that reorganize pages.

**Height (the climb).** Four domains — `self`, `timeline`, `work`, `places` — have three or more pages and nothing above any of them. The climb turns N scattered observations into one reusable premise.

**Breadth (the retrofit).** Converting the legacy graph to typed connections, page by page, deepening body copy from raw in the same pass.

## The typed edges system

Every connection between pages is a **typed edge with a one-sentence argued claim**, stored in frontmatter and (for load-bearing edges) argued in prose. "Related: tom" records that two pages touch, not how. "Tom `supplies` the neurochemical stack whose delivery failures are the proximate trigger of the friendship's rupture" is knowledge — it survives being read cold, it is greppable, and chains of typed edges compose into queryable arguments.

The vocabulary is fixed: `causes`/`caused-by`, `evidences`/`evidenced-by`, `instantiates`/`instance-of`, `precedes`/`follows`, `supplies`/`supplied-by`, `component-of`/`contains`, `contradicts`, `parallels`, `mirrors`, `co-occurs`. Choosing `co-occurs` when the raw would support `causes` is a substance failure; choosing `causes` when the raw only supports `co-occurs` is a provenance failure. The type IS the analytical commitment.

## The governing documents

The wiki is governed by six documents, in the order a new reader should meet them:

| File | Governs | Wins on |
|---|---|---|
| **STRATEGY.md** | what we are doing and why | intent |
| **CLAUDE.md** | the operations | process |
| **EXTRACTION_SPEC.md** | how deep to go into a source | depth |
| **STYLE_GUIDE.md** | page format and the substance standard | format |
| **CONNECTIONS_SPEC.md** | typed edges and their claims | edges |
| **SYNTHESIS_SPEC.md** | altitude — how conclusions stack | climbing |

`BACKLOG.md` holds the standing work; `LLM_HANDOFF.md` holds the exact resume point.

## The five unbreakable rules

1. **Never write an untyped link.** Every connection gets a `type` and a `claim`.
2. **Never state a fact without a raw source that exists on disk.** Verify numbers and quotes against `raw/` before writing them.
3. **Never stop at what you came for.** A source is read when it is exhausted, not when it has answered your question.
4. **Never clear a stale warning by bumping the date.** If `wiki-climb check` says a page's premise moved, read what changed and decide whether the conclusion survives, then record that decision on the page.
5. **Leave the site as you found it, plus your work.** Run `bin/wiki-lint`, `bin/wiki-connect check`, and `bin/wiki-climb check` before committing.

## What a finished piece of work looks like

For synthesis pages: verified members, typed edges with argued claims, inverse edges on every member, one governing rule stated plainly, gaps named. For ground pages: every claim re-derived from raw, corrections flagged rather than silently applied, and the mundane kept.

Two things are worth more than volume of output. **Negative results** — "checked X, it is not there" — are cheap falsifiers and belong on pages. And **corrections of the wiki's own errors**, with the old claim left visible, are the most valuable artifact the repository produces, because they are where the model of Dan actually improves.

## Prediction

The wiki-brain will continue to compound insight as long as the core loop runs. Its failure mode is not error but **stale premises** — conclusions built on pages that have since moved, with nobody re-checking whether the conclusion survives. The staleness cascade is the system's immune response: it flags what needs re-reading. The prohibited move is silencing that alarm by bumping a date.

**What would falsify this:** a synthesis page whose thesis is "these things are related" rather than a falsifiable rule. A ground page that leads with corpus statistics instead of the story. A correction applied silently, with the old claim deleted. A source declared ingested when it was only skimmed.

The wiki-brain is not a finished product. It is a process — one that gets more valuable the longer it runs, because every finding written back is a finding that never has to be re-derived.
