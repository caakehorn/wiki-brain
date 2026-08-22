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
| `WORK.md` | what is outstanding, and in what order | sequence |

`BACKLOG.md` = standing work. `LLM_HANDOFF.md` = the exact resume point.

## Start and end every session here

**At the start of every session, read `LLM_HANDOFF.md`** to understand current state, recent changes and immediate priorities. **When you end, update it** — what you accomplished and the exact focus for the next model. This is what makes the work continuous across sessions and models.

**Then run `bin/wiki-work`.** It is the one list, it is mandatory, and it is not optional reading. Outstanding work used to live in six files and two frontmatter flags, every one of which relied on somebody remembering to look; a session that read four of the six was indistinguishable from one that read all six. This aggregates them and separates the two kinds:

- **Obligations** — a red gate, a question parked by the portal, an answer staged on a page, a synthesis whose premise moved under it, a portal edit nobody normalised. Somebody or something is waiting on each one. There are usually a handful. A failing gate sits above all of them because it blocks every commit; on 2026-08-21 `bin/wiki-connect check` sat red on `main` with 70 errors after a portal save deleted 56 typed-edge claims, and nothing surfaced it, because nothing had to.
- **Standing work** — the ingest queue, the mined edge and cluster candidates, the backlog. Hundreds of entries, worked top-down by choice rather than drained, each in the file built for it.

**The order is fixed, and step 4 is the one that gets skipped:**

1. read `LLM_HANDOFF.md` and `operator-log.md`
2. run `bin/wiki-work` — see what is outstanding *before* you start
3. **do what the operator actually asked for**, in full
4. **then come back and drain the obligations, from the top**
5. anything still outstanding goes into `LLM_HANDOFF.md` with a reason — never silently

That order is deliberate in both directions: the operator's request never waits behind the queue, and the queue never waits on somebody noticing it.

**Nothing in `WORK.md` can be ticked off.** Every row is a live condition recomputed on each run — there is no ledger, no checkbox and no `done` command, because a list that can be marked complete independently of the thing it describes is a list that can lie, and the first lie it would tell is that a question somebody is waiting on has been answered. An item leaves the list when what it points at changes. Record what you did in `log.md`, as always.

`operator-log.md` and `bin/wiki-gaps pending` still exist and are still worth opening: the log is the durable half — append-only, survives `clear`, and records what was *already* integrated so a session can tell a fresh answer from an old one without reading git history. `bin/wiki-work` will not let you miss that there is one; the log tells you its history.

## The three things that matter most

1. **Depth is the binding constraint.** There are 438 pages; there are not enough *details on them*. A pattern can only be found among details that were written down, and synthesis reasons from `wiki/`, not `raw/` — so anything dropped at extraction is a connection nobody can ever make. Read sources to exhaustion, write long, keep the mundane. `EXTRACTION_SPEC.md`.
2. **Findings get written back.** A conclusion that spans several pages is written into *each* of them as a typed edge whose claim states the finding — not left on one page for the others to rediscover. This is `STRATEGY.md`'s core loop, step 5, and the step most often done partially.
3. **Never clear a stale warning by bumping a date.** Re-read the premise that moved, decide whether the conclusion survives, record the decision. This is the one move that corrupts the system quietly.

## Architecture — plain files, one direction of flow

```
inbox/  →  raw/  →  wiki/  →  caakehorn/home public/wiki/   exports/ (generated,
typed &     immutable   compiled    derived snapshot, never edited            disposable)
uploaded    source      knowledge                    │
              ▲                                      │  a question is asked
              │                                      ▼
              └────────────── sage/questions/ ◄──────┘
               the answer is filed        parked until a session answers it
               to raw/ and staged
               onto every page it cites
```

One loop closes here that no other operation closes: a question comes *in* from
outside the repository, and the work of answering it goes back into `raw/` and
`wiki/` as new material. The corpus is bigger after a question than before it.

- **`inbox/`** — staging. Material arrives via `bin/capture` or by being dropped in. On ingest, MOVE the file to the right `raw/` subdirectory, then synthesize. Never leave a file in both.
- **`raw/`** — immutable source archive, organized `raw/<domain>/<collection>/`. Never modify or delete anything here except when filing from `inbox/`. **`raw/self/context-core/CONTEXT_CORE_EXPANDED.md` is the primary authoritative source for facts about Dan** — curated, internally cross-checked, explicit about its own gaps. Check it first on any self/mind/timeline topic; treat other sources as supplementary or corrective to it unless they carry a specific dated correction it lacks. Source tiers and per-source traps: `EXTRACTION_SPEC.md`.
- **`wiki/`** — the compiled product: accumulated understanding, not a cache of `raw/`. Domains: `self`, `timeline`, `people`, `mind`, `work`, `interests`, `health`, `places`, `legal`. Add a domain only when several pages clearly don't fit an existing one. `wiki/**/archive/` holds pinned oversized artifacts (`status: archived`) — exempt from budgets, never updated.
- **`sage/`** — questions put to the wiki **from outside it**. The portal has a question box; anyone through the door can ask something about Dan and the question lands in `sage/questions/` as a file. Nothing answers it automatically — there is no model behind the box and no workflow that calls one. It is parked, `bin/wiki-work` lists it at priority 1, and a session answers it properly. Not in `raw/` because these files mutate (`pending` → `answered`); the immutable artifact is the capture written to `raw/self/sage/` at answer time. See `sage/README.md` and the ANSWER operation below.
- **`exports/`** — output of `bin/export-corpus`; never hand-edit, gitignored.
- **The portal** — [`caakehorn/home`](https://github.com/caakehorn/home) renders this wiki, and its `public/wiki/**` is a **derived snapshot of `wiki/`, not a second copy of it.** A workflow there re-runs the derivation against this repo on dispatch *and hourly*, deleting the directory and rebuilding it, so **anything written into `public/wiki/` is destroyed within the hour** — including a change that merged. If a session finds itself editing a page as JSON, it is in the wrong repository: pages are `wiki/**.md`, here. This is not a style preference; two December 2015 read passes were written into the snapshot and one was reverted 39 minutes after merging (restored 2026-08-17). **The dispatch that wakes it is `.github/workflows/notify-portal.yml`, here** — it fires `wiki-updated` at the portal on every push to `main` touching `wiki/**` or `sage/questions/**`, which are the only two paths the portal's `sync-wiki.mjs` reads. It needs `PORTAL_DISPATCH_TOKEN` in this repository's secrets and **ships inert without it**, falling back to the portal's hourly cron; if a merged answer is not live within a minute or two, check that secret first.
- **Meta files** (root): `index.md` master navigation · `log.md` append-only operation log · `operator-log.md` append-only ledger of operator additions (written by `bin/wiki-gaps`, never by hand) · **`WORK.md` the one outstanding-work list (written by `bin/wiki-work`, never by hand)** · `queue.md` pending-ingest ledger · `connection-queue.md` mined edge backlog · `synthesis-queue.md` mined climb backlog · `BACKLOG.md` standing work.

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

### ANSWER — a question put to the wiki from outside it

QUERY is somebody in this repository asking the wiki something. ANSWER is somebody *outside* it doing so — through the portal's question box, which parks the question in `sage/questions/` and promises them an answer. `bin/wiki-work` lists it at priority 1 for exactly that reason: it is the only obligation in this repository where the person waiting cannot see whether anything is happening.

Read `sage/README.md` for the file format. The protocol:

1. **Read the question as asked**, not as you would have preferred it asked. It may be hostile, badly framed, or about something the corpus cannot settle. Answer the question that was typed.
2. **Retrieve properly.** Reason from `wiki/` first, then go to `raw/` for the proofs — `bin/mine-messages` over the message record rather than grep, and the per-contact CSVs where the question is about one relationship. A question about future behaviour is a question about the documented pattern; find the pattern's instances and its counterexamples both.
3. **Cite every claim, and quote directly.** This is the standard the whole operation stands on. A sentence about what Dan does cites the page that establishes it; a sentence about what he *did* quotes the record with its date. An answer without proofs is an opinion with a citation style, and it is worth less than nothing here — it looks like evidence.
4. **Say where the record cuts the other way.** Every answer states its own strongest counter-evidence and what would falsify it. The corpus contains things that do not flatter its subject, and an answering system that routes around them is one nobody should believe on anything. Where the corpus genuinely cannot settle the question, that is the answer, and it is a real one.
5. **Never quote a sealed page.** `wiki.locks.json` in the portal repo names pages that ship as ciphertext precisely so the site cannot read them out. An answer that quotes one publishes through the back door what the seal exists to keep shut.

Then the five writes, none of them optional:

1. The answer into `sage/questions/<id>.md` — `status: answered`, `answered:`, `capture:` and every path in `cites:`. This is what the portal renders.
2. The immutable capture to `raw/self/sage/<id>.md`: question, answer, sources. `sage/` mutates; `raw/` is the record.
3. **The findings staged onto every page the answer cites**, under `## Sage findings — pending ingest` with a `sage_pending: YYYY-MM-DD` flag — the same shape as `bin/wiki-gaps`'s block and a **deliberately different key**. An operator answer is T0 first-person testimony; this is synthesis *about* the corpus, and the two must never be mistaken for each other on a page. As with a staged gap answer, do not bump `date_modified`: the page has not been corrected yet, and bumping it would clear the staleness warnings on every page that reasons from this one.
4. `log.md`: `## [YYYY-MM-DD] answer | <domain> | <the question, short>` — as findings, not activity.
5. `bin/wiki-work scan`, three gates at 0 errors, commit.

An answer that produced no finding worth staging stages nothing, and says so in the answer. That is a legitimate outcome — it means the wiki already knew — and it is still an answer.

A question that is abusive, is about somebody other than Dan, or cannot be answered from the corpus gets `status: declined` and a reason in the Answer section. Declined in the open, never deleted: the portal renders it, so a question nobody wants to answer is visible as one.

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

### CLOSE — integrate an answer the operator has already given

Every other operation starts from a source. This one starts from the operator having sat down and answered something a page admitted it did not know. `bin/wiki-gaps` stages those answers; **applying them is not optional and is not low-priority work.** An answer sitting in a staging block is the wiki holding knowledge it has not absorbed — strictly worse than not having it, because `OPEN.md` now reads as if the question were still open somewhere and the answer is invisible to every page that needed it.

`bin/wiki-gaps pending` lists them; `OPEN.md` carries the same list under **Answered, awaiting ingest**. For each page:

1. **Read the whole page first**, then the staged blocks under `## Operator answers — pending ingest`. Each block carries the gap as the page stated it, the operator's answer verbatim, and the `raw/` path the answer was filed to.
2. Treat the answer as **T0 first-person testimony, not as proof.** It is the strongest source class the corpus has and it is still one source. Where it can be checked against `raw/` — `bin/mine-messages`, an export, a contacts file — check it, and say on the page which parts were corroborated and which rest on testimony alone. Where it *contradicts* something the page derived from a primary source, that is a `> **CONTRADICTION:**` to hold, not a disagreement to settle by seniority.
3. **Rewrite the page around the answer** — integrate it where it belongs in the existing argument. Do not leave the staged block in place as the answer's permanent home; that is the changelog rot STYLE_GUIDE rule 6 forbids.
4. Record the result inline as a `> **GAP CLOSED [YYYY-MM-DD]:**` blockquote with the original gap visible (STYLE_GUIDE rule 9), and cite the `raw/` capture in `sources:`.
5. **Cascade.** A gap is rarely local: every page that reasoned from the unknown, cited the gap, or carries a typed edge into this one gets the correction written back. This is the step most often skipped, and skipping it is what leaves a corrected page contradicting three uncorrected ones.
6. Bump `date_modified` **now** — the page has actually moved, which it had not when the answer was merely staged.
7. `bin/wiki-gaps clear <page>` to delete the staging section and the `pending_ingest:` flag. Clearing means integrated, never discarded: the answer is permanent in `raw/`.
8. Three gates at 0 errors; log `close | <domain> | <page> — <what the answer changed>`; commit.

If an answer turns out to be **wrong** against a primary source, that is a finding worth more than the answer was — write it up, keep both claims visible, and clear the flag anyway. A staged answer that was never acted on and a staged answer that was checked and rejected must not look the same from outside.

### LINT (periodic)

Sweep for: broken links, orphan pages, contradictions between pages, claims superseded by newer raw data, entities mentioned 3+ times with no page, and **stale premises** (`bin/wiki-climb check`). Fix mechanically what you can; queue the rest in `BACKLOG.md`. A stale page is never fixed mechanically — re-read what changed in the premise before touching the dependent.

**Invoke the `wiki-housekeeping` skill (`.claude/skills/wiki-housekeeping/`) and follow it** whenever the operator asks to tidy, sweep, lint, audit or do housekeeping, and at the end of a session that moved the repo a lot. It carries the part this paragraph cannot: which warnings are requests to look rather than defects (the size warnings are, and trimming to clear one destroys earned content), how to work a stale premise without bumping a date, and how to drain obligations without mistaking a cleared flag for an integrated answer. The mechanical half is `bin/wiki-check`; the skill is the half that needs a reader.

## Tools (`bin/` — pure Python stdlib, no dependencies, no APIs)

| Tool | Purpose |
|---|---|
| `bin/capture` | human-facing input: interactive typing/pasting, one-shot facts, file upload (`-f`), `status` |
| `bin/mine-messages` | corpus mining over the full iMessage dump: `stats`, `grep`, `timeline`, `battery`, `entities`. **Use this instead of grep** — three properties of the dump make naive grep silently wrong |
| `bin/wiki-check` | **the whole mechanical chain in one command** — regenerates, runs the three gates plus freshness, rescans `WORK.md`, in the one order that is correct. `--check-only` gates without writing (CI, review); `--quiet` for hooks. Exits 1 on any red gate. The judgment half is the `wiki-housekeeping` skill |
| `bin/wiki-lint` | frontmatter, links, orphans, sizes, duplicate frontmatter keys, retracted claims (`RETRACTED.md`), empty cited sources, **unresolved merge markers, assistant citation artifacts, malformed frontmatter blocks and master-index count drift**. Must be 0 errors before commit |
| `bin/wiki-freshness` | is the generated corpus (`llm/`) in sync with `wiki/`? Exact set difference against `llm/manifest.json`; never writes. Exit 1 on drift |
| `bin/wiki-connect` | `check` (typed-edge lint), `audit` (graph health), `candidates` (writes `connection-queue.md`) |
| `bin/wiki-climb` | `check` (validates `synthesizes:`, reports stale premises), `audit` (tier distribution), `candidates` (writes `synthesis-queue.md`) |
| `bin/wiki-digest` | regenerates `DIGEST.md`, `RECENT.md`, `OPEN.md` — committed, safe to rerun any time |
| `bin/llm-publish` | builds `llm/`, the public LLM access point — **generated but COMMITTED**; rerun after any content pass |
| `bin/export-corpus` | concatenates the wiki into one markdown file for LLM ingestion, with a token estimate |
| `bin/wiki-search`, `bin/wiki-status`, `bin/wiki-tui` | search, status, terminal browser |
| `bin/ingest-pack` / `bin/ingest-apply` | the any-LLM paste-box route (`INGEST_PROTOCOL.md`) |
| `bin/wiki-work` | **the one outstanding-work list, and a required session step.** Aggregates every source of outstanding work — parked `sage/` questions, staged answers, stale premises, unnormalised portal edits, and the four standing queues — and separates obligations from campaign work. `scan` regenerates `WORK.md`; `next` names the top item and the operation that clears it; `check` prints the gate banner and always exits 0. No `done` command, by design |
| `bin/wiki-gaps` | operator-facing: answer an open gap, or volunteer a fact the page never asked for, and stage it for the next pass. `pages [filter]` lists **every** page so any of them can take a manual addition; `list` lists only those with open items; `pending` lists what is waiting; `clear` closes the loop and marks `operator-log.md`. Reads gaps, open leads, corrections queues and "what's missing" sections alike |

## Before every commit

```bash
bin/wiki-check              # regenerate, gate, scan — the whole chain, ~4s, red exits 1
bin/wiki-check --check-only # gate without writing anything (CI, or reviewing a branch)
```

`bin/wiki-check` runs what used to be four hand-copied lines, **and it runs them
in the order that is actually correct**, which the four lines were not:
generators first, then gates, then the scan. `bin/wiki-lint` checks master-index
count drift, so running it before `bin/wiki-digest` inspects numbers that are
about to change; and `bin/wiki-freshness` exists to confirm the generators ran,
so running it before them asks a question whose answer is guaranteed stale. In
`--check-only` mode nothing is written and `wiki-freshness` becomes the real
gate rather than a formality — it is what catches a content pass committed
without regenerating, which is how the LLM manifest got eleven pages behind on
2026-08-20. The individual tools still work exactly as before:

```bash
bin/wiki-lint && bin/wiki-connect check && bin/wiki-climb check   # all at 0 errors
bin/wiki-digest && bin/llm-publish                                 # after any content pass
bin/wiki-freshness                                                 # confirms the two above actually ran
bin/wiki-work scan                                                 # WORK.md back in step with the repo
```

`bin/wiki-lint` ends every run with what `bin/wiki-work check` found. That banner
is **advisory and never changes the exit code** — a question parked on Tuesday
must not block Thursday's typo fix, because a gate that blocks unrelated work is a
gate that gets an escape hatch, and an escape hatch is how a mandatory step stops
being one. Read it anyway; it is the reminder that step 4 above is still waiting.

`bin/wiki-freshness` exists because the generated corpus is committed and drifts
silently when a pass forgets to regenerate — the 2026-08-20 audit found the LLM
manifest eleven pages behind. It compares the manifest's own page list against
`wiki/` and names every page that is missing, orphaned or changed. It never
writes; you fix drift by running the generators yourself.

**Retracted claims.** `RETRACTED.md` is a machine-readable ledger of claims shown
to be false; `bin/wiki-lint` fails if one reappears as a live assertion.
Correction blockquotes are exempt by design — STYLE_GUIDE rule 9 requires the old
claim to stay visible where it is corrected — so documenting a retraction never
trips the gate. Add a claim by appending a JSON block to that file; no tool edit
is needed. Patterns must model the *claim*, never a bare number.

**Tests.** `python3 -m unittest discover -s tests` covers the lint gates and the
freshness check.

Then append to `log.md` as **findings, not activity** — what was wrong, what the evidence was, what changed — and update `LLM_HANDOFF.md`.

Size warnings from `bin/wiki-lint` are **advisory**. They mean "check navigation," never "shorten." Never trim earned content to clear one.
