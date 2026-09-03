# Architectural review — the Wiki Brain Rebuild Proposal

**Reviewing:** *Wiki Brain Rebuild Proposal — From an Accumulated Repository to an
Agent-Native Knowledge Operating System*, GPT-5.6 Luna
**Reviewer:** Claude (Opus 5), acting as Gate 1 per the proposal's §27
**Date:** 2026-09-03
**Repository state reviewed:** `main` @ `8228cc5`, 497 pages, 991,632 words

The proposal asked for a hostile review rather than a rubber stamp. This is that.
It is organised as the proposal requested: findings first, then the ten questions
of §28 answered directly.

---

## Verdict in one line

**Do not rebuild. The binding constraint is not architecture — it is that
nothing runs the gates the architecture already has.** Six of the proposal's
features already exist and work; one diagnosis is correct and has a cheap fix
that does not require a new repository; and the migration as specified would
destroy the only content in this corpus that cannot be regenerated.

---

## 1. The decisive finding

**`main` is red on five of eight gates right now, and has been since
2026-09-02.**

```
FAILED  bin/wiki-lint       FAILED  bin/wiki-connect check
FAILED  bin/wiki-climb      FAILED  bin/wiki-plain check
FAILED  bin/wiki-freshness
wiki-check: 5 gate(s) red in 6.1s
```

Every one of those five failures traces to a single file — 
`wiki/synthesis/twitter-2024-cognitive-state.md`, added by PR #247 (`c15b6ed`),
merged 2026-09-02:

| Gate | What it said |
|---|---|
| `wiki-lint` | invalid `status: draft`; invalid `domain: synthesis`; invalid `page_type: analysis`; 5 undeclared tags |
| `wiki-connect` | 2 typed edges missing a type or a claim |
| `wiki-climb` | **"sources a wiki page (`wiki/self/twitter/2024.md`) — wiki belongs in `synthesizes:`"** |
| `wiki-plain` | generated campaign page behind the tree |
| `wiki-freshness` | page never published to `llm/` |

Read the `wiki-climb` line again. **That is the proposal's central thesis —
§2's "the system does not sharply distinguish SOURCE from EVIDENCE from
SYNTHESIS" — detected, named, and located by the existing tooling, in 6.1
seconds.** The distinction the proposal says the architecture lacks is
mechanically enforced by a gate that has been in the tree for weeks.

It gets sharper. On the same day, the same author promoted
`skills/corpus/source-chain.md` (`validated: 2026-09-02`), whose instruction #1
reads:

> *"Start from the raw or first-party evidence where available; treat derived
> wiki pages as reasoning surfaces, not stronger evidence merely because they
> are cleaner."*

The rule was written, the gate that enforces it fired, and the violating page
merged anyway — because:

**There is no CI check on pull requests.** Three workflows exist
(`deploy-site.yml`, `notify-portal.yml`, `sage-drain.yml`). None has a
`pull_request:` trigger. None runs `bin/wiki-check`. The only mention of the
gates in `.github/` is inside `sage-drain.yml`'s *prompt text*, telling an agent
to please run them.

So the causal chain for the corpus's most recent quality failure is:

```
rule existed  →  gate existed  →  gate detected it  →  nobody ran the gate  →  merged
```

**No part of that chain is fixed by a new architecture.** A `pull_request:`
trigger running the command that already exists would have blocked it. That is
roughly fifteen lines of YAML against a proposal for a seven-phase migration of
a million words.

---

## 2. Six of the proposed features already exist

The proposal reads as though it were written against a description of the
repository rather than the repository. Measured:

| § | Proposed as new | Actually in the tree |
|---|---|---|
| 10 | Provenance graph | `sources:` on 485 pages; `synthesizes:` on 79; `EXTRACTION_SPEC.md` source tiers; `bin/source-index` |
| 11 | Contradiction management | 53 pages carry `> **CONTRADICTION:**` blocks; `RETRACTED.md` is a **machine-readable, gated** ledger of 5 falsified claims that fails the build if one reappears as a live assertion |
| 13 | Entity + relationship graph | **2,465 typed edges across 385 pages**, each carrying a prose `claim` stating what the edge asserts — richer than the subject/predicate/object triples §13 proposes |
| 15 | Derived-surface dependency graph | `bin/wiki-climb check` **is** that graph. It produced 95 stale-premise warnings on this run, each naming the dependent, the premise, and the number of days it moved |
| 16 | Skill evolution lifecycle | `skills/` with `PROTOCOL.md` (lifecycle), `CHANGELOG.md` (gated — a skill absent from it fails), `INBOX.md` (unvalidated candidates), and `bin/wiki-lessons route` |
| 18 | Agent self-registration | `skills/registry/` — append-only JSONL, 70 events, 56 capabilities, 2 models, public face at `wiki/meta/skills.md`, gated by `bin/wiki-skills check` |

Feature 12 (multi-dimensional confidence) partially exists as
`knowledge: earned|derived|mixed`, `status:`, and the `EXTRACTION_SPEC.md`
source tiers. Feature 9 (activity logs) was added on 2026-09-02 as
`AGENT_ACTIVITY_LOG.md` — see §4 below.

Rebuilding these is not a migration to a better architecture. It is
reimplementing working, tested machinery — 17,598 lines of dependency-free
Python with 4,180 lines of tests across 10 test files — in order to obtain
properties it already has.

---

## 3. The one diagnosis that is correct

**§19.2, "giant universal agent prompts," is right, and it is the only claim in
the proposal that survives contact with the repository.** Measured:

| Mandatory at session start per `CLAUDE.md` | Words |
|---|---|
| `CLAUDE.md` | 10,283 |
| `LLM_HANDOFF.md` — *"read at the start of every session"* | **58,873** |
| plus the governing set it points to (STRATEGY, EXTRACTION, STYLE, CONNECTIONS, SYNTHESIS, INGEST_RUNBOOK, AGENT_ACCESS) | 17,984 |

That is roughly **87,000 words — on the order of 115,000 tokens — consumed
before any work begins.** `LLM_HANDOFF.md` alone is 419 KB, six times
`CLAUDE.md`, and it is an append-only narrative that has never been rotated.

This is a real defect with real cost, and it is getting worse monotonically.
**It does not require a new repository.** It requires:

1. Rotating `LLM_HANDOFF.md` — keep the last two sessions live, move the rest to
   `handoff/archive/`. The historical record is already in `log.md` and git.
2. Splitting `CLAUDE.md` into a ~1,500-word bootstrap and per-operation files
   loaded on demand — which is exactly what `bin/wiki-lessons route "<task>"`
   already does for `skills/`. The pattern is proven here; it just has not been
   applied to the governing set.

That is a week of work inside the current repo, and it delivers the whole of
§5's "First Contact 2.0" benefit without the bootstrap protocol.

---

## 4. The proposal reproduces the defect it diagnoses

`AGENT_ACTIVITY_LOG.md` was merged on 2026-09-02 (PR #249) implementing §9. It
opens with an operating rule in bold — *"Every PR created for work in this
repository MUST include an Agent Activity Log entry"* — and closes with
**"No entry = incomplete agent workflow."**

```
$ grep -rl 'AGENT_ACTIVITY_LOG' bin/ tests/ .github/
NOTHING reads it — no gate, no test, no CI
```

It is a hand-maintained markdown file, containing two entries, enforced by
nothing. PR #250 merged after it without one.

`CLAUDE.md` names this exact pattern as the repository's core failure mode:

> *"a corpus of instructions that relies on somebody remembering to look is one
> that a session can skip without the skip being visible."*

The proposal's §7 (task contracts), §8 (exit gates), §9 (activity logs) and §17
(handoffs) are, as specified, four more of these — conventions with no
enforcement surface named. **A rebuild that carries this habit forward produces
the same repository with a different directory layout in eighteen months.**
The habit is the problem. It is correctable in place, and correcting it in place
is the only way to know it has been corrected.

---

## 5. Migration risks the proposal underestimates

### 5.1 "Move the information, not the prose" is incoherent for earned content

Phase 2 says: *"Move the information, not the prose. No improvements. No
interpretation."* This is coherent for derived content and destructive for
earned content, and `CLAUDE.md` already says why:

> *"**Earned** content — a thesis, a psychological read, a conclusion
> cross-referenced from many sources — is the product of reasoning done once.
> `raw/` does not contain it literally, and re-running the pipeline may not
> reproduce it."*

| `knowledge:` | Pages | Words |
|---|---|---|
| earned | 80 | **324,950** |
| mixed | 160 | — |
| derived | 44 | — |

**For 80 pages and ~325,000 words, the prose *is* the information.** A
psychological read does not decompose into `subject / predicate / object`
without ceasing to be the thing that was valuable. The proposal's own §20 says
"existing analytical work" must be preserved — but Phase 2 and Phase 5
("regenerate synthesis from the migrated substrate") are the mechanism by which
it would be lost. Those two sections contradict each other and the proposal does
not notice.

`CLAUDE.md`'s standing rule is *"never regenerate an earned page from scratch —
revise it."* Phase 5 is that prohibition applied to the entire corpus at once.

### 5.2 The migration would be performed by the agents that caused the drift

The proposal treats migration as a mechanical transformation. It is not — it is
497 pages of judgment calls, executed by LLMs. The agent population available to
do it is the one that, last week, merged five red gates while holding the
correct rule in an adjacent file. **A full-corpus rewrite is the single
highest-variance operation this repository could undergo, proposed as the
remedy for insufficiently disciplined writing.**

### 5.3 The machinery-to-data ratio is worse than assumed

This repo already contains three structured, event-sourced,
generated-view layers — the exact pattern §3 proposes. Their cost:

| Layer | Tool LOC | Events held |
|---|---|---|
| `intake/` | 2,363 | 20 |
| `testimony/` | 1,384 | 24 |
| `skills/registry/` | 1,383 | 70 |

That is **50–120 lines of maintained Python per event held.** These are the
best evidence available for what the proposal's substrate would cost, and they
argue against it: decomposing 991,632 words into claim-level records produces
tens of thousands of objects, and nothing in the proposal explains who writes or
maintains the tooling at that scale. The three existing layers took months to
build for 114 events combined.

### 5.4 The standing safety directive is not mentioned once

**This is the most serious omission in the document.**

`CLAUDE.md` carries a standing operator directive — the Annie moratorium, a
**safety directive about a living person believed to be in danger** — which
outranks every other priority in the repository. It is not a convention. It is
enforced as code in three tools (`bin/wiki-plain`, `bin/wiki-skills`,
`bin/wiki-testimony`), as a compiled pattern and an integer threshold
(`MORATORIUM`, `INCIDENTAL`), and pinned by `tests/test_wiki_plain.py`. It
**refuses** rather than warns.

The proposal — which proposes new tools, a new schema, a new publication layer
and a full re-derivation of every page — does not mention it. Under the proposed
migration, every one of those enforcement points would have to be re-implemented
and re-tested in the new stack **before a single page moved**, and a Phase 5
"regenerate synthesis from the migrated substrate" pass is precisely the
operation the directive forbids: *new writing about her, rebuilt, and published.*

This alone is disqualifying for the migration as specified. It is not an
engineering oversight; it is a safety-relevant one, and it is the clearest
available evidence that the proposal was written against an idea of the
repository rather than its contents.

### 5.5 Also unmentioned: 685 MB of `raw/`, sealed pages, and the portal contract

- `raw/` is 3,366 files and 685 MB, declared immutable. The proposal's `brain/sources/` implies a reorganisation of it; `CLAUDE.md` forbids one.
- `wiki.locks.json` in the portal repo names pages shipped as **ciphertext**. Any new publication layer must reimplement that seal or it publishes what the seal exists to keep shut.
- The portal (`caakehorn/home`) reads `wiki/**` and `sage/questions/**` and nothing else, deletes and rebuilds its snapshot on a schedule, and derives page history from **this repository's git log** at `fetch-depth: 0`. A new directory layout silently breaks a live public site and every page's revision history. The proposal's §4 layout has no `wiki/` at all.

---

## 6. What is actually worth taking from the proposal

Three things, all buildable inside the current repo in weeks:

1. **§8, evidence-based exit gates — as CI, not as a concept.** A
   `pull_request:` workflow running `bin/wiki-check --check-only` and
   `python3 -m unittest discover -s tests`, set as a required check. This is the
   single highest-value change available to this repository today and it closes
   the failure documented in §1 above.
2. **§11, contradictions as first-class objects — as an upgrade, not a rebuild.**
   The 53 `CONTRADICTION` blockquotes are a convention; `RETRACTED.md` is a
   gated, machine-readable ledger. Promote the former to the shape of the
   latter: `CONTRADICTIONS.md` with JSON blocks, a gate that fails when a page
   asserts one side of an open contradiction as settled. Small, high value, and
   it lands the §2 thesis mechanically.
3. **§19.2, the instruction diet.** Rotate `LLM_HANDOFF.md`; split `CLAUDE.md`
   into bootstrap + routed operations, using the `bin/wiki-lessons route`
   pattern already proven here.

---

## 7. Answers to §28

**A. Should Wiki Brain be rebuilt?**
**NO** — conditional on the enforcement work below being done first. Revisit in
90 days with data. If, after CI gates are required and the instruction surface
is cut, the corpus still degrades at the same rate, the architectural argument
becomes real and I will say so. It is not established today, because the control
condition — a system whose gates actually run — has never been tried.

**B. Is the separation of knowledge / synthesis / agent operations correct?**
**YES as a principle, REVISE as a plan.** The separation is right and it is
mostly already implemented: `raw/` → `wiki/` (with `knowledge:` declaring which
is which) → `skills/` + `bin/`. What is missing is not the boundary but its
enforcement, and `bin/wiki-climb check` shows the enforcement is achievable
within the current layout — it caught the violation.

**C. Is structured knowledge preferable to Markdown-first storage?**
**CONDITIONAL, and mostly NO here.** Structure is correct for anything
countable — intake, testimony, registry, typed edges — and all four are already
structured. It is wrong for ~325,000 words of earned analytical prose, where the
prose is the artifact. The right architecture is the current one: structured
where the data is atomic, prose where the reasoning is. The proposal's error is
treating this as one question with one answer.

**D. Which features belong in v1?**
CI exit gates (§8, as YAML). Contradiction ledger (§11, as a gate). Instruction
diet (§19.2). Nothing else.

**E. Which features should explicitly NOT be built?**
§4 (new directory layout — breaks the portal, `raw/` immutability, and every
page's public revision history). §5 (First Contact bootstrap — solve the context
problem with a diet, not a protocol). §6 (capability registry — exists). §7
(task contracts — a convention with no enforcement surface; make CI the
contract). §10, §13, §15, §16, §18 (all exist). §9 as currently built — either
gate `AGENT_ACTIVITY_LOG.md` or delete it; an ungated MUST is worse than
nothing because it reads like a control.

**F. What migration risks are underestimated?**
The five in §5 above, in order of severity: the standing safety directive
(unmentioned, mechanically enforced, and a Phase 5 re-derivation violates it);
the irreducibility of 325k words of earned prose; the migration being executed
by the agent population that produced the drift; the machinery-to-data ratio
measured from this repo's own three structured layers; and the live portal
contract, the sealed pages, and 685 MB of immutable `raw/`.

**G. What architectural principles are missing?**
Two. **(i) A rule is only real if something fails when it is broken.** This
repository has more correct rules than any comparable corpus and almost no
enforcement of them; the ratio, not the count, is the problem. **(ii) Prefer the
cheapest intervention that would have prevented the last actual failure.**
Applied to PR #247, that is a CI trigger — which is also the test the proposal
itself never runs against any of its 19 features.

**H. What would I design differently?**
I would not design. I would wire `bin/wiki-check --check-only` into a required
PR check, fix the five red gates, rotate the handoff file, and promote
contradictions to a gated ledger. Then measure for a quarter. The proposal's
best instinct — §21's "the migration is itself the best test of the
architecture" — is right, and the cheaper version of that test is: make the
existing architecture's own gates binding and see what still breaks.

**I. What must be true before migration begins?**
Four things, none of which is true today. (1) `main` green for 30 consecutive
days under required CI. (2) The Annie moratorium re-implemented and test-pinned
in any new tool, verified before a single page moves. (3) A written, operator-
approved answer to what happens to 80 earned pages that says something other
than "regenerate." (4) A fidelity harness that can prove a round-trip on a
20-page slice — including edges, contradictions, gaps, and seal status — before
page 21 is touched.

**J. What would make me refuse to sign off?**
Any of: a migration plan that re-derives earned pages rather than carrying their
prose across verbatim; any new tool touching `plain/` or any publication surface
before the moratorium is re-encoded and tested in it; a schema change landing
before `caakehorn/home`'s sync and history derivation are updated to match; or
the migration starting while `main` is red — which is the current state, and is
the condition under which this proposal was written.

---

## 8. Recommendation

**Continue on the current system. Spend the next two weeks on enforcement, not
architecture.**

In priority order:

1. Fix the five red gates on `main` (one page; delete or repair
   `wiki/synthesis/twitter-2024-cognitive-state.md` and re-run the generators).
2. Add `.github/workflows/gates.yml` — `pull_request:` → `bin/wiki-check
   --check-only` + `unittest discover` — and set it as a required check.
3. Gate or delete `AGENT_ACTIVITY_LOG.md`.
4. Rotate `LLM_HANDOFF.md` to the last two sessions.
5. Split `CLAUDE.md` into bootstrap + routed operations.
6. Promote contradictions to a gated ledger alongside `RETRACTED.md`.
7. Re-measure in 90 days.

The proposal's closing line is *"if the new brain can't faithfully ingest the
old one without losing provenance, contradictions, or source distinctions, we've
learned exactly what the new architecture is missing."* That test is available
today, for free, and the current architecture has already run it: it caught a
lost source distinction in 6.1 seconds and named the file. The finding is not
that the architecture is inadequate. **The finding is that nobody was listening
to it.**

Build the listener first.
