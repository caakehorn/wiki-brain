# `data/intake/` — the intake ledger

An append-only event log of substances, supplements and consumables tracked as
**discrete units**: a finite object enters the record, every known disposition
of it is recorded against it, and at closure the ledger reconciles what is
known, preserves what is unknown, and computes only what the evidence supports.

Written by `/ledger` in [`caakehorn/home`](https://github.com/caakehorn/home).
Read here by `bin/wiki-intake`.

## Why this is not in `raw/`

`raw/` is an archive of sources that arrived from somewhere else — an export, a
scan, a capture of something already said. This is neither. It is a **primary
instrument**: a measurement taken at the moment the thing happened, by the
person it happened to, in a format designed before the first reading rather than
reverse-engineered after the fact.

That distinction matters for how it should be used. Everything else this
repository reasons from about substance use is recollection, and the wiki is
honest about it — `wiki/health/cocaine.md` states a dosage arc of
"1 g → 3.5–7 g → 0.5–1 g" reconstructed across twenty years from messages and
memory. That is the best the corpus could do. This is the instrument that
measures it instead, and a page that cites this log is making a different and
much stronger kind of claim than one that cites a remembered range.

It is also mutable in a way `raw/` is not — new events append to the current
month's file forever — so filing it under an immutable archive would be a lie
about what the directory contains.

## The files

```
data/intake/
  events-YYYY-MM.jsonl   the log, sharded by the month an event was LOGGED
  units.json             a derived snapshot; regenerated, never hand-edited
  README.md              this
```

Sharding is on `loggedAt`, not `occurredAt`, for three reasons in order of how
much they matter: GitHub's contents API caps a read at a megabyte and has no
append, so an unsharded log eventually stops being readable by the thing that
writes it; a closed month is then never rewritten, so the only file two devices
can collide on is the current one; and a month of a life reads well in a
`git log`.

`units.json` is derived from the log and carries no wall clock — its "as of" is
`throughEvent`, the id of the last event it was built from — so two devices
produce identical bytes from identical logs and it is rewritten only when a unit
actually changed.

## The event shape

One JSON object per line. Flat, no nesting beyond `patch` and `source`, every
enum a literal string, every instant an ISO 8601 string **carrying its offset**.

```json
{"id":"evt_01K…","type":"intake_logged","loggedAt":"2026-08-29T15:17:22-04:00",
 "unit":"unit_01K…","occurredAt":"2026-08-29T15:17:22-04:00",
 "measurement":"measured","quantity":0.18,"uom":"g",
 "source":{"app":"home","tool":"intake-ledger","v":1}}
```

The offset is not decoration. Time-of-day is one of the few things this dataset
answers well, and `03:40-04:00` and `07:40Z` are the same instant but not the
same fact about a night. Keeping the offset means the local hour is recoverable
by reading two characters, with no timezone database anywhere in the stack.

| `type` | what it records |
|---|---|
| `unit_opened` | a finite object enters the record: substance, quantity, uom, when received |
| `intake_logged` | one consumption event against one unit |
| `intake_corrected` | an earlier event's figure was wrong; carries the new value and a **required** reason |
| `intake_voided` | an earlier event did not happen; required reason |
| `unit_adjusted` | material left the unit without being taken — spilled, discarded, given away |
| `unit_amended` | the unit's own particulars were wrong |
| `unit_closed` | how it ended, and what was done with anything unaccounted for |
| `unit_reopened` | closed by mistake, or material turned up |

**Nothing is ever updated in place and nothing is ever deleted.** A mistyped dose
is followed by a correction carrying the old value; a double-tap by a void. Both
require a reason, because a correction with no reason is indistinguishable from
a revision, and the difference between those two is the entire value of the log.

Ids are ULID-shaped: 10 characters of millisecond timestamp, 16 of randomness.
Sortable by creation, and unique without coordination — which is the property
that matters, because it makes merging two copies of the log a set union by id.
Two devices can both be offline, both append, and converge later with nothing
lost.

## The three measurement classes

This is the design, not a detail.

| `measurement` | means | contributes to |
|---|---|---|
| `measured` | it came off a scale | every statistic |
| `estimated` | a number somebody produced by looking; carries `confidence` | quantity totals, kept separable |
| `unquantified` | a real event with no number — `descriptor: "one line"` | event counts, intervals, time-of-day. **No sum, ever.** |

An `unquantified` event carries no `quantity` field at all, and the writer
enforces it: an empty quantity box becomes `unquantified` with whatever words
were used, never `measured: 0`, which would drag every mean down with a number
nobody measured.

Dropping those events would make the record cleaner and false. Keeping them
lets a report say the honest thing:

> Unit #001 had 14 consumption events over 31 hours. Eight were measured,
> accounting for 2.1 g. Six were logged without a figure.

## The refusals

Any program reading this log must hold these, or it is producing plausible
numbers rather than true ones. `bin/wiki-intake` and `src/ledger/project.ts`
implement them independently, and `tests/test_wiki_intake.py` and
`scripts/check-ledger.mjs` pin them over the same worked fixture on both sides.

1. **A remainder is a bound.** `initial − quantified − spilled` is an *upper*
   bound on what is left whenever any event was logged without a figure, because
   those events took an unknown positive amount. Print `≤`, or do not print it.

2. **A mean dose is over quantified events.** Never the unit's initial quantity
   over the count of all events. A 3.5 g unit with seven logged events did not
   average 0.5 g unless the log accounts for all 3.5 g, and it usually does not.
   Carry the denominator next to the figure.

3. **Closing does not assume consumption.** When the log does not reach the whole
   unit, the closer picks what happened to the difference, and the four answers
   stay different facts downstream — a last dose nobody logged becomes a real
   low-confidence estimated dose in the statistics; attributing it to the
   unquantified events derives a mean for *those alone*, labelled derived; a
   discrepancy derives nothing; lost or transferred never reaches a dose
   statistic.

4. **An overdrawn unit is a finding, not an error.** When the log accounts for
   more than the unit ever held, a dose was double-logged or the initial weight
   was wrong. `bin/wiki-intake check` fails on it rather than clamping it to
   zero.

5. **Quantities convert only within a dimension.** Mass to mass, volume to
   volume; a tablet is not a capsule and neither is a gram. A dose logged in a
   unit that will not reduce to the unit's own is counted as an event, named as
   unconvertible, and kept out of every sum.

## Reading it

```
bin/wiki-intake check                validate the log; runs in bin/wiki-check
bin/wiki-intake units                every unit with its honest tally
bin/wiki-intake report <unit|name>   one unit, start to finish  (--events)
bin/wiki-intake stats                across units, by substance
bin/wiki-intake timeline --from 2026-08-01 --to 2026-08-31
```

`timeline` exists to be joined against anything else in this repository that
carries a date — the message record via `bin/mine-messages`, the turn-level
style measurements in `bin/text-metrics`, the events on
`wiki/timeline/master-timeline.md`. That join is the point of putting this here
rather than leaving it in an app: a question like *what changed in his sleep,
his messaging and his intake across August 2026* becomes answerable from
timestamped evidence instead of from "I think I was probably doing more around
then?".

## Writing it into the wiki

Nothing here writes to `wiki/` automatically, and nothing should. This is
evidence, and the standing rule for anything drawn from it is the one in
`SYNTHESIS_SPEC.md`: a pattern found in this log is a fact about this log until
it has been read against the person. A page citing it cites specific units and
specific dates the way it would cite any other source, and states what the log
could not account for — which is on every report for exactly that reason.
