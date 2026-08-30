# `intake/` — the intake ledger

A finite object enters the record. Every known disposition of that object is
recorded after it. At closure the system reconciles what is known, preserves
what is unknown, and computes only what the evidence actually supports.

That sentence is the whole design. Everything below is how it is enforced.

Run it with `bin/intake`, from the local app at **Special:Intake**, or from
**`/ledger`** in [`caakehorn/home`](https://github.com/caakehorn/home) — the
portal, which is the one interface that is in your pocket.

## Why a unit and not a dose

A dose diary records *"I did X at 8:30"* and can answer almost nothing
afterwards, because the number it holds has no denominator. This tracks the
**unit** — a finite quantity that entered the record at a known time — and then
records every known disposition of that unit until it is gone.

```
UNIT RECEIVED  ──▶  UNIT RECORD          substance · initial quantity · unit ·
                    (finite, dated)      received_at · source · status
                          │
                          │  each intake event consumes some of it
                          ▼
                    INTAKE EVENT         occurred_at · quantity? · measurement
                    (repeatable)         type · descriptor · note
                          │
                          ▼
                    CLOSURE              how it ended, and what happened to
                    (reconciled)         anything unaccounted for
                          │
                          ▼
                    UNIT REPORT          duration · counts · mean/median/min/max
                    (computed)           · intervals · peak window · phases
```

Only with a denominator can the ledger reach the questions worth asking: how
long 3.5 g actually lasts, whether the first dose runs larger than the rest,
whether consumption accelerates toward depletion, how often a unit is gone
inside a day. A list of doses cannot answer any of them.

## Three kinds of event, because precision is not always available

| kind | what it holds | counts toward |
|---|---|---|
| `measured` | `0.18 g` on a scale | everything |
| `estimated` | `~0.2 g` with a confidence | everything, flagged |
| `unquantified` | `"one line"`, `"two hits"` | event counts, timing, clustering — **never** a quantity statistic |

The third is the one that matters. A system that only accepts grams loses the
behavioural record — the count, the timing, the clustering — every time the
scale is not to hand, and it loses it *silently*. Here the event is still real:

> Unit #1 had 13 consumption events over 40 hours. Ten were quantitatively
> measured, accounting for 2.45 g. Three were logged without a reliable
> quantity.

That is more honest than inventing precision, and it is strictly more data than
refusing the event. **Every quantity figure this tool prints carries the share of
events it was computed from**, so a mean over 10 of 13 events never gets to look
like a mean over 13.

## The arithmetic is deliberately incomplete

Open 3.5 g, log ten events totalling 2.7 g, close the unit — this tool will
**not** tell you the average dose was 0.35 g. It does not know what happened to
the other 0.8 g, and inventing a distribution for it produces a number that
looks like evidence and is not.

So closing a unit asks two questions. *How did it end* — consumed, discarded,
transferred, unknown. And, if quantity is unaccounted for, *what was that
quantity* — a final intake, a measurement discrepancy, a spill, a transfer.
`bin/intake close` refuses to proceed without an answer:

```
$ bin/intake close 1 --disposition consumed
intake: 1.05 g is unaccounted for — say what happened to it:
        --resolution final_intake|discrepancy|lost|transferred|other
```

Answer `final_intake` and the remainder is written as one **estimated,
low-confidence** intake event, and the report says so wherever it shows up:

```
COVERAGE
  1.05 g of the quantified total is a single remainder written off at close,
  not a watched dose.
```

Reconciliation is a recorded decision with a timestamp, never a silent
subtraction.

## Event-sourced, in plain files

`events.jsonl` is the **source of truth**: append-only, one JSON object per
line, never rewritten. `units.json` is a **projection** — regenerated from the
log on every write, and safe to delete (`bin/intake rebuild` returns it
identical). `substances.json` is reference data: the select box, and the one
file here meant to be edited by hand.

Nothing is ever edited in place. A mistyped `0.5 g` becomes an
`event_corrected` record naming the original, the correction and the reason:

```json
{"type":"intake_logged","id":"intake_evt_01M…","data":{"quantity":0.5,"unit":"g"}}
{"type":"event_corrected","data":{"target":"intake_evt_01M…",
  "fields":{"quantity":0.05},"reason":"decimal entry error"}}
```

The ledger shows `0.05 g`. The log remembers both, and that a correction was
needed two minutes later is itself evidence about how the logging happens.

**JSONL rather than SQLite**, which the first sketch called for. This repository
is plain files under git and that is not incidental to it: a JSONL line diffs,
greps, survives every tool here, and shows up in `git log` as the history it
already is. `sqlite3` is stdlib and would have worked — it would just have been
the only unreadable file in the corpus.

## ⚠ The data is in git, and that depends on this repository being private

It did not used to be. `intake/events.jsonl`, `intake/units.json` and
`raw/health/intake/` were in `.gitignore` because this repository was public and
a consumption record is not something to publish by accident — the tool tracked,
the record not. That cost was real: the ledger's history was outside git, a
fresh clone started empty, and a session working from a clone could not read it.

**The repository is private now, so those three lines are gone** and the ledger
keeps its history the way everything else here does. That is the step the
previous version of this section named as the fix.

### The interlock, because `.gitignore` was never the guard it looked like

Worth being precise about, because it is easy to get wrong twice. `.gitignore`
only governs `git add`. It has no effect whatsoever on GitHub's contents API —
which is exactly how `/ledger` in the portal writes here, from a browser, with
no working tree involved. An ignored path is committed by that API without
complaint.

So while those lines were in place they were protecting the CLI and the local
app and doing nothing at all for the portal. The actual guard is in the portal:
**it reads this repository's visibility before its first push of a session and
refuses to sync while it is public**, naming the reason. That check does not
care what `.gitignore` says, and it is what makes the ordering safe — flip the
repository back to public and the portal stops writing rather than quietly
publishing a night's events.

If you ever do make it public again, put the three lines back *and* expect the
portal to stop syncing. Both are correct.

## Why it lives in wiki-brain

Because this is the anti-unreliable-narrator layer. The wiki reasons from what
was written down, and prose recollection of consumption is the least reliable
testimony a person gives about themselves.

> *"I barely used anything that weekend."*

The ledger does not argue. It says: `Aug 14–16 — 37 logged intake events across
4 units`, with timestamps. It is a first-party dated dataset that can be set
against a page's narrative the way `bin/text-metrics` is set against a page's
assertions about how he writes, and it is meant to be cited in exactly that way.

**It is not a wiki page and does not become one automatically.** A finding drawn
from the ledger goes onto a page through the normal operations, cited to a unit
id and a date range, with the coverage figure attached. The ledger is evidence;
the page is the claim.

## The commands

```
bin/intake                          active units, recent events, what to do next
bin/intake substances               the select box — list it
bin/intake substance add "Kratom" --category other --unit g

bin/intake new cocaine 3.5g --at "2026-08-29 13:42" --source "…"
bin/intake log 1 .18g                       measured
bin/intake log 1 .2g --estimated            estimated, medium confidence
bin/intake log 1 --descriptor "one line"    unquantified, still an event
bin/intake log 1 180mg                      converts within the unit's family
bin/intake adjust 1 .3g --kind spill --note "knocked off the table"

bin/intake correct <event> --quantity .05g --reason "decimal entry error"
bin/intake void <event> --reason "logged against the wrong unit"

bin/intake close 1 --disposition consumed --resolution discrepancy
bin/intake reopen 1 --reason "closed it by mistake"

bin/intake report 1                 the unit report, plus every event
bin/intake stats --substance cocaine --since 2026-01-01
bin/intake units --all
bin/intake rebuild                  units.json from the log
bin/intake check                    the gate — runs inside bin/wiki-check
bin/intake export                   the whole ledger as one JSON document
```

Units convert inside a family and never across one: milligrams are grams,
millilitres are not, and `2 tab` is never `2 g`. A cross-family log is an error,
not a coercion.

## What the unit report computes

Duration · event counts by measurement type · quantified total split into
measured and estimated · remaining · mean, median, smallest, largest dose ·
dose variability (CV) · mean and median interval · rate of consumption · peak
usage window · first dose against the later mean · a time-of-day histogram · and
the **phases** — first 25% / middle 50% / final 25% of the unit *by quantity
consumed*, with a velocity comparison between the ends.

Phases are cut by quantity rather than by elapsed time on purpose: the question
they answer is whether consumption accelerates toward depletion, which is about
how fast the material went, not how the clock ran. Unquantified events carry no
quantity, so they are placed by falling inside a phase's time span and counted
separately — they never move a boundary.

`bin/intake stats` runs the same reasoning across every unit ever opened: unit
size and duration distributions, how often a unit is gone inside 24 hours, dose
distribution and variability per substance, month-by-month drift in mean dose,
and the time-of-day profile of every event in the ledger.
