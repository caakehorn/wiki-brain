# The testimony veracity ledger

**What Dan says about his own life is the corpus's most valuable source class
and its least verifiable one.** `CLAUDE.md`'s CLOSE operation already says the
right thing about it: an operator answer is **T0 first-person testimony, not
proof**, and where it can be checked against `raw/`, it must be.

The wiki has been doing that for months. What it has never done is **keep the
results**. Each check lands as a blockquote on one page — `GAP CLOSED`,
`CONTRADICTION`, `CORROBORATION ATTEMPTED` — and then it is over. Page 41 has
no idea that the same person's date claims came back eight weeks early on page
12, so the next answer is weighed exactly as credulously as the first.

This is the missing half of CLOSE: the place the result of the check is
recorded, so that scattered adjudications become one instrument pointed at the
next unproven thing he says.

---

## Two numbers, because one would be a lie

A single "trust score" collapses two independent facts, and the collapse is why
most credibility scores are useless:

| | what it measures | what it is for |
|---|---|---|
| **Veracity** | how often he turns out to be right, weighted by how specific and load-bearing the claim was | how much to believe him |
| **Calibration** | whether his own stated confidence tracks that accuracy | whether to believe his *confidence* |

Only the second one makes an **unproven** claim assessable. You cannot check
the unproven claim — that is what unproven means — so all you have is the class
it belongs to and the confidence it arrived with. A person right 70% of the
time who says *"I think, not sure"* on exactly the wrong 30% is fully reliable;
you just read the hedge. A person right 90% of the time who says *"definitely"*
about all of it is more accurate and **less usable**.

## The scoring, in full

```
weight  = specificity (1 vague / 2 definite / 3 exact)  x  1.5 if load-bearing
value   = confirmed 1.0 · partial 0.5 · self_contradicted 0.25 · refuted 0.0
points  = weight x (2 x value - 1)
score   = 50 + 50 x (sum points / sum weight)      →  0..100
```

A confirmed claim earns its full weight, a refuted one loses it, a partial is a
wash. That is the plain reading of *"given or lose points."*

**`unfalsifiable` scores zero and never negative.** Checked, and the corpus
cannot settle it. Punishing him for the archive's gaps would make the number a
measure of the corpus rather than of the man, and would make honest recording
of a hard claim costly — which is the fastest way to end up with a ledger
holding only easy claims.

**Unadjudicated claims are excluded from every statistic.** They are the queue,
not the record. `bin/wiki-testimony status` lists them, and each one is a claim
the wiki is currently carrying on his word alone.

Calibration is a **Brier skill score against a coin flip**, plus the observed
gap between what each confidence band says it is worth and what it turned out
to be worth.

## The stratification is the product

"Dan is 74% reliable" is not usable by anything. The findings that are usable
look like: *date claims about events more than ten years back come back early
94% of the time, by a median of eight weeks* — because that is a correction you
can actually apply to the next date he gives.

So three columns carry the analysis, and `bin/wiki-testimony taxonomy` prints
every value of each:

- **Claim class** — the *what*. Cut by kind of proposition (`date`, `quantity`,
  `identity`, `self_state`, `enumeration`…) rather than by subject matter,
  because the error profile follows the proposition: a date is misremembered
  the same way whether it is about a job or a funeral.
- **Failure mode** — the *how*. `compression`, `displacement`, `conflation`,
  `transposition`, `inversion`, `omission`, `overreach`, `rounding`,
  `confabulation`, `stale`. Required on every claim that did not come back
  clean; `check` fails without it, because an unexplained miss teaches the
  ledger nothing.
- **Slant** — which way the error ran **relative to his own interest**:
  `flattering`, `condemning`, `neutral`. Also required, `neutral` included, so
  that the absence of self-serving error is evidence rather than an untested
  assumption. This is the column that separates a memory limit from a bias.

Plus **direction** (`early`/`late`/`over`/`under`/`inward`/`outward`) — the
subtractable half. Knowing he is wrong about dates is nearly useless; knowing
he is *early* is a bias you can correct for.

## Small samples are named as such, always

This ledger holds tens of adjudications, not thousands. So:

- every rate carries its `n`;
- class rates are **shrunk** toward the global rate with a pseudocount of 3;
- a **Wilson interval** is printed rather than a bare percentage;
- a class below `MIN_N = 5` is **refused as a prior** — `assess` falls back to
  the global figure and says that it did;
- any bucket below `MIN_BUCKET = 3` prints its count and withholds the
  interpretation.

This is the discipline `bin/intake` applies to a mean over 10 of 13 events, for
the same reason: a figure that cannot state its own denominator gets believed
as though it had one.

## Files

| file | what it is |
|---|---|
| `events.jsonl` | **the source of truth** — append-only, one JSON object per line, never rewritten |
| `testimonies.json` | a projection, regenerated on every write, safe to delete |
| `SUMMARY.md` | the analysis surface, so nothing has to parse JSONL |
| `wiki/meta/testimony-veracity.md` | the public face, generated; a hand-edit fails `check` |

An adjudication that turns out to be wrong is **superseded, never edited** —
`adjudicate --revise --reason`. The ledger shows the current verdict and the
log remembers that it changed. That matters more here than anywhere else in
this repository: a veracity record that can be quietly rewritten is worth less
than no veracity record at all.

## The standing directive left a hole, and the page still declares it

From 2026-08-23 to 2026-09-06 `record` refused any claim naming one living
person and `check` failed if one reached the log, under a standing operator
directive. **That directive was lifted on 2026-09-06** and the refusal is gone.

**What it cost is still in the numbers.** At least one cleanly adjudicated
confirmation went unrecorded — an April 2019 sequence the operator supplied and
a direction-reliable dump then corroborated to the minute. It can be entered
now, and until it and anything like it are, the score is drawn from what that
fortnight permitted. The generated page says so in its own words; a rate drawn
from a filtered record that does not announce the filter is a worse object than
no rate.

## What the seed set is, and is not

The ledger opened on 2026-09-02 with **11 records reconstructed from
adjudications the wiki had already made** and left scattered across pages.
Every one cites the page or `raw/` capture it came from, and every adjudication
cites what settled it.

Two honest limits on that seed, which apply to it and not to records made from
here on:

1. **The `confidence` values are inferred.** Nobody recorded how confident he
   was at the time, so each was read from how the page reports the assertion.
   Records made going forward should capture it at the moment of assertion.
2. **Adjudicated claims are not a random sample of claims.** A claim gets
   checked when somebody had a reason to check it, and the reasons correlate
   with the claim being surprising, load-bearing, or already doubted. Expect
   the settled set to over-represent both the spectacular confirmations and the
   spectacular failures.

## Using it

```bash
bin/wiki-testimony                      # the standing state and the queue
bin/wiki-testimony taxonomy             # every class, mode, direction, tier
bin/wiki-testimony score                # the two numbers, global and by class
bin/wiki-testimony profile              # what and how the errors run
bin/wiki-testimony assess --class date --confidence certain
bin/wiki-testimony list --pending       # claims carried on his word alone
bin/wiki-testimony show t002
```

Recording a claim, and settling it later:

```bash
bin/wiki-testimony record \
  --claim "The sale closed in summer 2019 for $250,000" \
  --class date --class quantity --confidence confident \
  --channel capture --specificity 3 --load-bearing \
  --about 2019-07 --source raw/places/captures/2026-08-27_022401_gap-117-belmont-circle.md \
  --page wiki/places/117-belmont-circle \
  --note "what would settle it: a Fayette County deed search"

bin/wiki-testimony adjudicate t005 --outcome refuted \
  --tier primary_document --evidence "Deed recorded 2019-09-14, $232,000" \
  --failure magnitude --direction over --magnitude "\$18,000" --slant neutral
```

## Where it fits in the operations

**Every CLOSE should end here.** `CLAUDE.md`'s CLOSE step 2 says to check the
operator's answer against `raw/` where it can be checked, and to say on the
page which parts were corroborated and which rest on testimony alone. That
sentence describes an adjudication. Record it, so the next session inherits it:

```bash
bin/wiki-gaps clear <page>          # the answer is integrated
bin/wiki-testimony record ...       # and the claim is now on the record
```

An answer that could not be checked is still recorded — as `unfalsifiable`,
scoring zero, naming what would settle it. That is the row that tells a later
session a document is worth chasing.
