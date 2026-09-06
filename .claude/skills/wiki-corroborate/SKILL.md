---
name: wiki-corroborate
description: >
  Cross-reference what a wiki page says against the 282,050 first-party messages
  in raw/ — dating an event, filling out what a page did not have, and catching
  where a retelling has drifted from the contemporaneous record. Use whenever
  the operator asks to cross-reference, corroborate, verify, date, date-check,
  pin down, or "check the texts" for anything; whenever a page hedges a date
  (`~2019?`, "early 2017", "sometime in"); whenever an event is known only from
  a dossier, a video or a memory; before writing any dated claim during an
  ingest; and when asked what the message record says about a day, a person or
  an event. Also reach for it when a page states a limit about its own evidence
  ("only known through later narration", "the complete record"). This is NOT
  keyword mining over the corpus — that is bin/mine-messages — and it is not the
  entity-mention debt, which is bin/wiki-crosslink.
---

# CORROBORATE — the message record, joined to the page

`CLAUDE.md`'s CORROBORATE operation is the protocol and this is how to run it.
`bin/wiki-corroborate` is the instrument; read its module docstring once.

## 0. Non-negotiables

**Repository.** Work in `~/wiki-brain`. Pages are `wiki/**.md`. Never edit
`caakehorn/home` — its `public/wiki/**` is a build artifact and your change dies
within minutes.

**Never modify `raw/`.** The archive is immutable. This operation reads it.

**Never work on `main`.** Branch first.

**The messages outrank the page.** On any date, time, sequence or
who-was-present, the contemporaneous record wins and the page says so.

## 1. Know what a null result is worth, before you take one

```bash
bin/wiki-corroborate coverage
```

2015–2026, unevenly: **2012–2014 hold nothing, 2022 holds four rows, 2011 holds
one.** A claim dated outside coverage cannot be checked here in either
direction. `record` refuses `--outcome absent` for one — that is `uncovered`,
and collapsing the two publishes the archive's silence as the world's.

## 2. Pick the target

The operator named one, or:

```bash
bin/wiki-corroborate scan <page> --hedged   # what this page admits it doesn't know
bin/wiki-corroborate queue 25               # the whole wiki, worst first
bin/wiki-corroborate status <page>          # has anything been checked here before?
```

**Hedged dates first.** A page writing "~late 2017?" is telling you where to
point the instrument, and the corpus can usually settle it in one window.

## 3. Read the window — the whole thing

```bash
bin/wiki-corroborate window 2017-11-26 --days 1 --limit 0
bin/wiki-corroborate window 2017-11-26 --days 1 --handle 7243228715   # one thread
```

**Do not grep it.** Nobody texts the name of the event they are living through.
The keno morning contains the word "keno" zero times; it is dated by a mother's
*"Is she back in bed?"* and a girlfriend's *"I think I got a total of 1 whole
hour of sleep"*.

**Widen `--days` before concluding anything.** An event at midnight lands on two
dates. Start at ±1; go to ±3 when the page's own date is vague.

**Use the thread summary the tool prints.** It names every counterparty in the
window with a count — that is your map of who was in the day, and it routinely
includes people the page never mentions.

## 4. Read for four things, in this order

1. **Does the date hold?** The highest-value question, because a wrong date
   corrupts every sequence the page participates in, silently.
2. **What did the page not have?** The hours. The other threads. Who else was
   told, and what they were told — the end of the keno morning is recorded on
   the girlfriend's *mother's* thread, not on anyone's the page cites.
3. **What does it contradict?** A retelling that has drifted is a finding, not
   an embarrassment. Write it up.
4. **Who else is named?** That is `bin/wiki-crosslink`'s debt arriving through a
   different door. Pay it while you are here.

## 5. Write the pages first, record second

The ledger records that a check happened. **The finding goes on the pages**, and
this is the step that makes the work compound:

- A corrected or narrowed date gets a `> **CORROBORATED [YYYY-MM-DD]:**` block
  with the old claim visible and the rows that moved it, quoted with timestamps
  (`STYLE_GUIDE.md` rule 9).
- New material goes in the prose where it belongs, at the page's own altitude.
- A claim the record contradicts gets `> **CONTRADICTION:**` and stays visible.
- **Cascade.** Every page that carries the same date or reasons from it gets the
  correction. This is the step most often skipped, and skipping it leaves one
  corrected page contradicting three uncorrected ones.
- Where the window named a person, place or work with a page, write the typed
  edge — with the timestamp in the claim.

Then:

```bash
bin/wiki-corroborate record \
  --page wiki/timeline/events/fran-death-vigil \
  --page wiki/people/suzanne-frank \
  --claim "the keno morning — Fran's first long floor-fall" \
  --date 2017-11-26 --days 1 --outcome refined \
  --row "2017-11-26 00:06 Sent +17243228715" \
  --was "~late 2017?" --now "the night of 2017-11-25 into 2017-11-26" \
  --because "the thread dates the fall to 00:06 and the recovery to 13:21"
```

Every cited row is verified against the archive before the ledger will take it,
so a citation cannot be invented. **`--outcome absent` is a real result** and the
honest one when the window holds nothing.

## 6. Close out

```bash
bin/wiki-check          # regenerates the ledger page and runs every gate
```

`log.md`: `## [YYYY-MM-DD] corroborate | <domain> | <claim> — <what moved>`.
Then `LLM_HANDOFF.md` if the pass moved the repo.

## What this operation is not

- **Not `bin/mine-messages`.** That answers "does this string appear, and how
  often". This answers "what happened that day". Reach for that one for a
  vocabulary or volume question, this one for anything dated.
- **Not `bin/wiki-crosslink`.** That asks what a source said about *other*
  pages. This asks what the *message record* says about *this* one. The two
  queues do not overlap, and a window pays some of that debt as a side effect.
- **Not a verification ritual.** If you find yourself recording `absent` for
  every date on a page without reading anything, stop: the value is in the
  reading, and a ledger full of unread `absent`s is worse than an empty one.
