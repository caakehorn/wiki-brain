# STRATEGY — what this repository is doing and why (read me if you read nothing else)

Any model — including one less capable than the models that designed this system — should be able to open this repository cold and continue the work correctly by reading this file. It states the strategy in plain language. Read it alongside `CLAUDE.md` (process), `STYLE_GUIDE.md` (page format), `CONNECTIONS_SPEC.md` (connection format), and `SYNTHESIS_SPEC.md` (altitude — how conclusions stack on conclusions).

## The purpose

This wiki is a second brain about one person, Dan Frank. Its job is to collect, store, and synthesize as much data as possible about his life, mind, history, ideology, environment, and relationship to reality — every story, every friend, every place, every perspective, every development, every thought. Every data point gets an entry.

Each entry carries two things: everything known about it as of ingestion, and everything later produced by using it in analysis alongside the rest of the corpus. A wiki entry is never just a record — it's a live node that accumulates conclusions drawn from reading it against everything else.

Beyond archiving, the wiki is an analytical instrument in its own right: it exists to **mine one life for hidden connections** — linkages between people, events, money, substances, music, work, and psychology that no single source states, but that the corpus proves when read across itself. A fact filed is worth little. A connection argued is the product.

## The core loop

The system runs on one repeating cycle:

**Story → Entry → Analysis → Synthesized finding → Saved back to every entry it touches → Repeat.**

1. A memory, fact, or document is captured once and filed immutably into `raw/`.
2. It's read from `raw/` exactly once, and that understanding is written into a durable `wiki/` page — this is a ground-floor entry.
3. Once enough ground entries exist, they're read *across* each other — not one at a time — looking for a pattern that no single entry states but that several together prove.
4. That pattern becomes its own finding: a synthesis, stated as a falsifiable claim, not a vague observation.
5. The finding is written back into **every ground entry it draws from**, via a typed connection with an argued claim — so the insight doesn't have to be re-derived the next time someone lands on that entry.
6. The finding itself becomes a premise for the *next* round: junctions can be read across each other to find doctrine, the same way ground entries were read across each other to find junctions.

This is **amortized insight**. Analysis is expensive to do well, so it's done once, saved at every point it's relevant, and each future pass starts from a higher floor instead of re-deriving what's already known. Nothing above this line is optional flavor text — it's the actual mechanism the rest of the spec files exist to support.

## Why altitude matters

The product isn't flat. Every conclusion written today is a **premise** available tomorrow:

- **Ground pages** carry entities and events read out of `raw/`.
- **Junction pages** carry the pattern found across three or more ground pages, spanning two or more domains.
- **Doctrine pages** carry the rule found across junctions.

Each layer declares its `synthesizes:` list, naming exactly what it was built from, so the dependency chain is visible, checkable, and stays current when something below it changes. The loop is meant to run forever: ingest raises the floor, CLIMB raises the ceiling, and the new ceiling becomes the floor for the next climb. A repository of accurate ground pages with nothing built on top of them is an archive. **The altitude is the brain.**

## The pipeline in one paragraph

Material enters `inbox/`, is filed immutably into `raw/`, and is read ONCE — the understanding extracted from it is written into `wiki/` as prose pages. From then on, reasoning happens FROM the wiki, returning to `raw/` only when the wiki is silent or a claim needs primary verification. Pages are either `derived` (mechanically regenerable from raw — counts, discographies) or `earned` (conclusions produced by reasoning — NOT regenerable, must be revised, never rewritten from scratch). `raw/self/context-core/CONTEXT_CORE_EXPANDED.md` is the single most authoritative raw source.

## Why connections are typed

The graph audit of 2026-07-17 found the wiki full of links that said nothing: "Related: tom" records that two pages touch, not how. That's an index, not a brain. Every connection is now a **typed edge with a claim** — a relationship type from a fixed vocabulary plus one argued sentence:

```yaml
connections:
  - page: wiki/people/tom
    type: supplies
    claim: "Tom is the physical supply line whose spring-2026 delivery failures are the proximate trigger of the friendship's rupture."
```

The claim is the knowledge. It survives being read cold, it can be grepped, and chains of typed edges compose into arguments (X causes Y, Y evidences Z). Full vocabulary and rules live in `CONNECTIONS_SPEC.md`. Bare `related:` lists and `## Related` footers are deprecated and being removed.

## The junction-page mechanism — and the operation that runs it

When three or more pages across two or more domains show the same pattern, that pattern earns its own synthesis page. Each member carries an `instantiates` edge into it; the new page declares `synthesizes:` listing its members. This is how N scattered observations become one reusable premise — the compounding mechanism, and the highest-value work in the repository. A discovered cross-domain pattern is worth more than any ten routine link fixes.

The operation is called **CLIMB**, alongside INGEST, QUERY, and LINT. `bin/wiki-climb candidates` mines the backlog into `synthesis-queue.md`; `bin/wiki-climb audit` shows which domains are all ground and no junction; `bin/wiki-climb check` reports **stale** pages — ones whose premises changed after they were written. Protocol in `SYNTHESIS_SPEC.md`. Two rules matter more than the rest:

- **A cluster you cannot state a falsifiable rule about gets rejected in the queue, with reasoning.** A considered non-synthesis is knowledge. A page whose thesis is "these things are related" is worse than no page.
- **When a conclusion is falsified, the failure stays on the page.** The block/unblock loop predicted the June 2026 severance would hold, and was wrong 52 days later because it scored dependency as material and missed a shared dog. The correction made the rule wider and truer — and that wider rule exists in no raw source anywhere. That is what this system is for.

## The substance standard in one paragraph

The first paragraph of every page must answer the stranger's question (for a person: who is this to Dan, what is the current state, what is the defining thing; for an event: what happened and what changed). Order by consequence, not chronology. State load-bearing conclusions plainly. Name gaps explicitly. Tables hold numbers; prose holds meaning. Exemplar pages — imitate their shape — are `wiki/people/annie-ulmer.md`, `wiki/people/suzanne-frank.md`, `wiki/timeline/events/eli-incident.md`. A page that is tidy but leads with corpus statistics instead of the story is a failed page.

## If you are a limited model, or unsure: the four unbreakable rules

1. **Never write an untyped link.** Every connection gets a `type` from the CONNECTIONS_SPEC vocabulary and a `claim` sentence. If you cannot write the claim, do not make the connection — record the rejection in `connection-queue.md` with one line of reasoning.
2. **Never state a fact without a raw source that exists on disk.** Verify numbers and quotes against `raw/` before writing them; flag dossier-only material as such. Never guess identities — grep all known names and handles first. Known trap: the `direction` column in `MASTER_MESSAGES_DB_DUMP.csv` is unreliable; reconstruct the speaker from content.
3. **Leave the site as you found it, plus your work.** Run `bin/wiki-lint`, `bin/wiki-connect check`, and `bin/wiki-climb check` before committing; commit before ending the session; append to `log.md`; update `LLM_HANDOFF.md` with what you did and the exact resume point.
4. **Never clear a stale warning by bumping the date.** If `wiki-climb check` says a page's premise moved, read what changed and decide whether the conclusion survives. Silencing it is the one move that corrupts the system quietly, because everything built above the page keeps compounding on a premise nobody re-checked.

Follow these four and you cannot corrupt the system, even if you understand nothing else here.

## Running on lesser models (the post-2026-07-18 operating reality)

The most capable model that will ever work on this repository finished its last session on 2026-07-18. Everything after this line is executed by less capable models, and the work has been shaped for that.

**Safe to execute mechanically (do these freely):**
- Clearing `bin/wiki-climb check` staleness warnings *properly* — read the changed premise, add one line saying the conclusion was re-checked and holds, then bump the date. If it doesn't hold, that's a REVISED block and a real pass, not a mechanical one.
- The `related:` → `connections:` retrofit backlog (per the protocol in `CONNECTIONS_SPEC.md`, one page per pass) and `connection-queue.md` top-down.
- The standing verdicts in `LONG_TAIL_TRIAGE.md` — decisions are made; execute, don't re-litigate.
- The storytime-mining workflow (`INGEST_RUNBOOK.md` §11) — with operator approval at step 3.
- `bin/llm-publish` regeneration after every content pass; queue.md and inbox hygiene; knowledge-tagging pages you already touch.

**Do NOT attempt without strong evidence in hand:**
- Rewriting or re-deriving any `knowledge: earned` page (junction pages, the synthesis stack, the fallout verdict). Revise with REVISED/CONTRADICTION blocks only, and only when raw evidence forces it.
- Changing a verdict or a verified number. The 2026-07-18 primary-count pass (`dan-annie-fallout-verdict.md`) is the worked example of the required discipline: base-rate controls, direction checks, exact-row citations. If you can't run that discipline, flag and queue instead.
- Guessing identities. Grep every name and handle; when in doubt, add to `contact-review.md` and move on.

**The model of the product** — what a finished piece of work looks like — is the junction-page trio (`supply-network`, `estate-money-spine`, `block-unblock-loop`): verified members, typed edges with argued claims, inverse edges on every member, one governing rule stated plainly, gaps named. Imitate their shape.

## Current campaign

Two run in parallel.

**Breadth (the retrofit):** converting the legacy graph to typed connections, page by page, in the priority order given in `CONNECTIONS_SPEC.md` (islanded pages → synthesis pages → `connection-queue.md` top-down → remaining `related:` holders), deepening body copy from raw in the same pass. `bin/wiki-connect audit` shows live progress.

**Height (the climb):** as of 2026-07-26 only 3.6% of pages sit above ground level, and four domains — `self`, `timeline`, `work`, `places` — have three or more pages and nothing above any of them. That is the structural gap now. Work `synthesis-queue.md` top-down, one climb per pass, per `SYNTHESIS_SPEC.md`. `bin/wiki-climb audit` shows live progress.

See `LLM_HANDOFF.md` for the exact resume point.
