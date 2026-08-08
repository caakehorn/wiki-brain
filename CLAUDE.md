# Personal Wiki — second brain

A custom wiki system that aims to be as exhaustive and detailed as possible about its creator, Dan Frank: biography, history, cognitive traits, ideology, tendencies, and every other datapoint that points back to the real person. It fills knowledge gaps as they are found and updates as time passes.

**This file governs process — the operations and how to run them.** Read it with the rest of the governing set. When any two disagree, the "wins on" column decides.

| File | Governs | Wins on |
|---|---|---|
| `STRATEGY.md` | what we're doing and why; the core loop | intent |
| **CLAUDE.md** (this file) | the operations | process |
| `EXTRACTION_SPEC.md` | how deep to mine a source before writing | depth |
| `STYLE_GUIDE.md` | page format and the substance standard | format |
| `CONNECTIONS_SPEC.md` | typed edges and their claims | edges |
| `SYNTHESIS_SPEC.md` | altitude — how conclusions stack | climbing |

`BACKLOG.md` = standing work. `LLM_HANDOFF.md` = the exact resume point.

## Start and end every session here

**At the start of every session, read `LLM_HANDOFF.md`** to understand current state, recent changes and immediate priorities. **When you end, update it** — what you accomplished and the exact focus for the next model. This is what makes the work continuous across sessions and models.

## The three things that matter most

1. **Depth is the binding constraint.** There are 438 pages; there are not enough *details on them*. A pattern can only be found among details that were written down, and synthesis reasons from `wiki/`, not `raw/` — so anything dropped at extraction is a connection nobody can ever make. Read sources to exhaustion, write long, keep the mundane. `EXTRACTION_SPEC.md`.
2. **Findings get written back.** A conclusion that spans several pages is written into *each* of them as a typed edge whose claim states the finding — not left on one page for the others to rediscover. This is `STRATEGY.md`'s core loop, step 5, and the step most often done partially.
3. **Never clear a stale warning by bumping a date.** Re-read the premise that moved, decide whether the conclusion survives, record the decision. This is the one move that corrupts the system quietly.

## Architecture — plain files, one direction of flow

```
inbox/  →  raw/  →  wiki/          exports/ (generated, disposable)
typed &     immutable   compiled
uploaded    source      knowledge
```

- **`inbox/`** — staging. Material arrives via `bin/capture` or by being dropped in. On ingest, MOVE the file to the right `raw/` subdirectory, then synthesize. Never leave a file in both.
- **`raw/`** — immutable source archive, organized `raw/<domain>/<collection>/`. Never modify or delete anything here except when filing from `inbox/`. **`raw/self/context-core/CONTEXT_CORE_EXPANDED.md` is the primary authoritative source for facts about Dan** — curated, internally cross-checked, explicit about its own gaps. Check it first on any self/mind/timeline topic; treat other sources as supplementary or corrective to it unless they carry a specific dated correction it lacks. Source tiers and per-source traps: `EXTRACTION_SPEC.md`.
- **`wiki/`** — the compiled product: accumulated understanding, not a cache of `raw/`. Domains: `self`, `timeline`, `people`, `mind`, `work`, `interests`, `health`, `places`, `legal`. Add a domain only when several pages clearly don't fit an existing one. `wiki/**/archive/` holds pinned oversized artifacts (`status: archived`) — exempt from budgets, never updated.
- **`exports/`** — output of `bin/export-corpus`; never hand-edit, gitignored.
- **Meta files** (root): `index.md` master navigation · `log.md` append-only operation log · `queue.md` pending-ingest ledger · `connection-queue.md` mined edge backlog · `synthesis-queue.md` mined climb backlog · `BACKLOG.md` standing work.

Git is the history mechanism. Commit after every ingest with `<op>: <short description>`. Never commit secrets or `exports/`.

## Why this is a second brain, not a RAG

A retrieval system keeps the sources and re-derives every answer on demand; it never learns, and yesterday's reasoning is thrown away. This is the opposite. You read a source **once, to exhaustion**, reason out what it *means*, and write that understanding into `wiki/`. From then on you reason **from** the wiki. Knowledge compounds: today's synthesized conclusion is tomorrow's premise.

This has a hard consequence — the wiki is **not** a disposable cache of `raw/`. Two kinds of content live here:

- **Derived** content — message counts, discographies reconstructed from slugs, anything mechanical — is safely regenerable.
- **Earned** content — a thesis, a psychological read, a conclusion cross-referenced from many sources — is the product of reasoning done once. `raw/` does not contain it literally, and re-running the pipeline may not reproduce it. This is the actual point of the system.

So **never regenerate an earned page from scratch — revise it.** When new raw contradicts it, flag and correct; do not bulldoze and re-derive from zero. Pages declare which kind they are with `knowledge: earned | derived | mixed`.

The one sanctioned exception is a deliberate wipe-and-rewrite the operator has asked for, which has its own protocol — see the `wiki-rewrite` skill below.

## The operations

### INGEST — one source per pass, never parallel

**If you are given a general or unspecified instruction to "ingest," "do the Phase B ingest," "keep going on the wiki," or any open-ended synthesis task — read `INGEST_RUNBOOK.md` first and follow it exactly.** That file is the reproduction-grade instruction for the cross-corpus synthesis pass. Do not improvise the ingest workflow.

Parallel "swarm" ingests destroyed v1 (fragment prose, duplicate entities, wrong statuses). Ingest ONE inbox item per pass, fully:

1. Move it from `inbox/` to the right `raw/<domain>/<collection>/`.
2. **Read it to exhaustion** — not until it answers your question. `EXTRACTION_SPEC.md`.
3. Put quantified data (dates, counts) into tables on the target pages; re-derive every number rather than copying it forward.
4. Write or update every relevant page — typically the domain summary plus every person, event and concept the source touches.
5. Update the domain index and `index.md` if pages were added.
6. Update `queue.md`; append to `log.md`: `## [YYYY-MM-DD] ingest | <domain> | <source>`.
7. Run the three gates; commit.

Large exports (social media dumps, message CSVs) may take multiple passes; track progress in `queue.md` rather than half-finishing silently.

Captured notes may carry `targets: [wiki/...paths]` — a targeted note is a correction or expansion of those specific pages: apply it there first, then file the note into `raw/`. Humans also edit pages directly in the app; those appear in `log.md` as `edit | <domain> | human edit via app` — treat them as authoritative content but normalize formatting and frontmatter on the next pass.

### QUERY

Start at `index.md`, follow domain indexes, answer with citations to wiki pages. Reason **from** the wiki first; re-open `raw/` only when the wiki is silent on the question or a source is newer than the page that used it — otherwise you are re-doing settled work. If the synthesis is new and durable, save it as a page: that is how the brain grows.

### CLIMB — the operation that raises altitude

The only operation that runs on `wiki/` rather than `raw/`. Where INGEST adds ground, CLIMB builds above it. **Full protocol in `SYNTHESIS_SPEC.md` — follow it exactly.** The short form:

1. `bin/wiki-climb candidates` maintains `synthesis-queue.md`. Take the top cluster, or one you have reason to prefer.
2. Read the member pages **in full** — you are reasoning from them.
3. Find the governing rule, **or reject the cluster in the queue with a line of reasoning.** A cluster that resists synthesis is knowledge too. Never write a page whose thesis is "these things are related."
4. Write it: `page_type: synthesis`, `knowledge: earned`, `synthesizes:` listing every member, thesis in the first two sentences, the controls that carry it, at least one prediction, and Gaps.
5. Wire it both ways. **Every member page gets the finding written back into it** — an `instantiates` edge whose claim states what this page turned out to be evidence *of*, plus a prose sentence wherever it is load-bearing. A synthesis whose members do not carry it back is half-built.
6. All three gates at 0 errors; log `climb | <domain> | <page>`; commit.

Climb when a cluster has survived two or more ingests, or immediately when an ingest makes you think "this is the third time I've seen this shape." Do not climb to raise a number: three thin pages stacked make one thin page.

### REWRITE — wipe and re-derive an existing page

When the operator asks to rewrite, wipe, redo, re-research or overhaul a page that already exists, **invoke the `wiki-rewrite` skill (`.claude/skills/wiki-rewrite/`) and follow it exactly.** INGEST governs new sources arriving; that skill governs an existing page being re-derived, and it carries the parts this pass gets wrong: snapshotting earned content before the wipe, ranking primary against AI-secondary sources, verifying derived numbers with `bin/mine-messages`, resolving identity through two independent contact exports, and working the staleness cascade without bumping a date.

### LINT (periodic)

Sweep for: broken links, orphan pages, contradictions between pages, claims superseded by newer raw data, entities mentioned 3+ times with no page, and **stale premises** (`bin/wiki-climb check`). Fix mechanically what you can; queue the rest in `BACKLOG.md`. A stale page is never fixed mechanically — re-read what changed in the premise before touching the dependent.

## Tools (`bin/` — pure Python stdlib, no dependencies, no APIs)

| Tool | Purpose |
|---|---|
| `bin/capture` | human-facing input: interactive typing/pasting, one-shot facts, file upload (`-f`), `status` |
| `bin/mine-messages` | corpus mining over the full iMessage dump: `stats`, `grep`, `timeline`, `battery`, `entities`. **Use this instead of grep** — three properties of the dump make naive grep silently wrong |
| `bin/wiki-lint` | frontmatter, links, orphans, sizes. Must be 0 errors before commit |
| `bin/wiki-connect` | `check` (typed-edge lint), `audit` (graph health), `candidates` (writes `connection-queue.md`) |
| `bin/wiki-climb` | `check` (validates `synthesizes:`, reports stale premises), `audit` (tier distribution), `candidates` (writes `synthesis-queue.md`) |
| `bin/wiki-digest` | regenerates `DIGEST.md`, `RECENT.md`, `OPEN.md` — committed, safe to rerun any time |
| `bin/llm-publish` | builds `llm/`, the public LLM access point — **generated but COMMITTED**; rerun after any content pass |
| `bin/export-corpus` | concatenates the wiki into one markdown file for LLM ingestion, with a token estimate |
| `bin/wiki-search`, `bin/wiki-status`, `bin/wiki-tui` | search, status, terminal browser |
| `bin/ingest-pack` / `bin/ingest-apply` | the any-LLM paste-box route (`INGEST_PROTOCOL.md`) |

## Before every commit

```bash
bin/wiki-lint && bin/wiki-connect check && bin/wiki-climb check   # all at 0 errors
bin/wiki-digest && bin/llm-publish                                 # after any content pass
```

Then append to `log.md` as **findings, not activity** — what was wrong, what the evidence was, what changed — and update `LLM_HANDOFF.md`.

Size warnings from `bin/wiki-lint` are **advisory**. They mean "check navigation," never "shorten." Never trim earned content to clear one.
