# STRATEGY — what this repository is doing and why (read me if you read nothing else)

This file exists so that any model — including one less capable than the
models that designed this system — can open this repository cold and continue
the work correctly. It states the top-down strategy in plain language. It is
mandatory reading alongside `CLAUDE.md` (process), `STYLE_GUIDE.md` (page
format), and `CONNECTIONS_SPEC.md` (connection format).

## The purpose

This wiki is a second brain about one person, Dan Frank. Its purpose is not
storage. Its purpose is to **mine the elements of one life for hidden
connections** — linkages between people, events, money, substances, music,
work, and psychology that no single source states, but that the corpus,
read across itself, proves. A fact filed is worth little; a connection
argued is the product. The wiki compounds: every synthesized conclusion
written today becomes a premise available tomorrow, so the system gets
smarter with use instead of re-deriving everything from raw sources.

## The pipeline in one paragraph

Material enters `inbox/`, is filed immutably into `raw/`, and is read ONCE —
the understanding extracted from it is written into `wiki/` as prose pages.
From then on, reasoning happens FROM the wiki, returning to `raw/` only when
the wiki is silent or a claim needs primary verification. Pages are either
`derived` (mechanically regenerable from raw — counts, discographies) or
`earned` (conclusions produced by reasoning — these are NOT regenerable and
must be revised, never rewritten from scratch). `raw/self/context-core/
CONTEXT_CORE_EXPANDED.md` is the single most authoritative raw source.

## Why connections are typed

The graph audit of 2026-07-17 found the wiki full of links that said nothing:
"Related: tom" records that two pages touch, not how. That is an index, not
a brain. So every connection is now a **typed edge with a claim** — a
relationship type from a fixed vocabulary plus one argued sentence:

```yaml
connections:
  - page: wiki/people/tom
    type: supplies
    claim: "Tom is the physical supply line whose spring-2026 delivery failures are the proximate trigger of the friendship's rupture."
```

The claim is the knowledge. It survives being read cold, it can be grepped,
and chains of typed edges compose into arguments (X causes Y, Y evidences
Z). The full vocabulary and rules are in `CONNECTIONS_SPEC.md`. Bare
`related:` lists and `## Related` footers are deprecated and being removed.

## The junction-page mechanism

When three or more pages across two or more domains show the same pattern,
that pattern gets its own synthesis page, and each member page carries an
`instantiates` edge into it. This is how N scattered observations become one
reusable premise — it is the compounding mechanism and the highest-value
work in the repository. A discovered cross-domain pattern is worth more than
any ten routine link fixes.

## The substance standard in one paragraph

The first paragraph of every page must answer the stranger's question (for a
person: who is this to Dan, what is the current state, what is the defining
thing; for an event: what happened and what changed). Order by consequence,
not chronology. State load-bearing conclusions plainly. Name gaps
explicitly. Tables hold numbers; prose holds meaning. The exemplar pages —
imitate their shape — are `wiki/people/annie-ulmer.md`,
`wiki/people/suzanne-frank.md`, `wiki/timeline/events/eli-incident.md`.
A page that is tidy but leads with corpus statistics instead of the story
is a failed page.

## If you are a limited model, or unsure: the three unbreakable rules

1. **Never write an untyped link.** Every connection you add gets a `type`
   from the CONNECTIONS_SPEC vocabulary and a `claim` sentence. If you
   cannot write the claim, do not make the connection — record the rejection
   in `connection-queue.md` with one line of reasoning.
2. **Never state a fact without a raw source that exists on disk.** Verify
   numbers and quotes against `raw/` before writing them; flag
   dossier-only material as such. Never guess identities — grep all known
   names and handles first. Known trap: the `direction` column in
   `MASTER_MESSAGES_DB_DUMP.csv` is unreliable; reconstruct the speaker
   from content.
3. **Leave the site as you found it, plus your work.** Run
   `bin/wiki-lint` and `bin/wiki-connect check` before committing; commit
   before ending the session; append to `log.md`; update `LLM_HANDOFF.md`
   with what you did and the exact resume point.

Follow these three and you cannot corrupt the system, even if you understand
nothing else here.

## Current campaign

The retrofit: converting the legacy graph to typed connections, page by
page, in the priority order given in `CONNECTIONS_SPEC.md` (islanded pages →
synthesis pages → `connection-queue.md` top-down → remaining `related:`
holders), deepening body copy from raw in the same pass. `bin/wiki-connect
audit` shows live progress. See `LLM_HANDOFF.md` for the exact resume point.
