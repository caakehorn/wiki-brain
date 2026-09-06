---
status: active
scope: corpus
triggers:
  - writing, revising or verifying any dated claim on a wiki page
  - a page that hedges a date (`~2019?`, "early 2017", "sometime in")
  - an event known only from a retelling, a dossier or an operator answer
  - deciding what a source is worth against another source on the same day
  - reaching for `bin/mine-messages grep` to check whether something happened
sources:
  - bin/wiki-corroborate — the module docstring, and `coverage`
  - CLAUDE.md — CORROBORATE, and rule 3 of "the five things that matter most"
  - EXTRACTION_SPEC.md — move 10, and the source tiers
  - wiki/timeline/events/fran-death-vigil.md — the worked case
validated: 2026-09-06
supersedes: []
---

# Read the window, not the wiki, and read it before you write the date

## Instruction

1. **Before writing any dated claim, run `bin/wiki-corroborate window <date>`.**
   Not when you doubt the date — always, when the date falls inside coverage.
   It takes about two seconds and you cannot tell from inside a claim whether
   the record has something to add.
2. **Read the whole window. Do not grep it.** Nobody texts the name of the event
   they are living through. A search for "fall", "grandmother" or "keno" over
   the keno morning returns nothing; reading the hours returns the whole day in
   four threads.
3. **Widen `--days` before concluding anything is absent.** An event at midnight
   lands on two dates, and a page that says "the morning of the 26th" may be
   describing something that started on the 25th.
4. **The messages outrank the source you are working from** on any date, time,
   sequence or who-was-present. Where they disagree, correct the page and say so
   in a `> **CORROBORATED [YYYY-MM-DD]:**` block with the old claim visible.
5. **Check `coverage` before you take a null result seriously.** 2012–2014 hold
   nothing; 2022 holds four rows. A claim outside coverage is unexamined, not
   unsupported, and `record` refuses to let `absent` stand in for `uncovered`.
6. **Record what came back, including nothing.** `--outcome absent` is a real
   result: it distinguishes a page nobody has checked from a page the corpus
   cannot help, and those look identical from outside.

## Why

**Almost every page in this wiki was written from something other than the
contemporaneous record.** A dossier, a later retelling, a memory of a video, an
operator answer. All of them are testimony *about* a day. A message is a
fragment *of* it, written at the time by the people involved, with no audience
and no thesis — which is exactly what makes it good evidence and exactly why
nobody thinks to check it.

The worked case is the keno morning. Three pages dated Fran Coldren's first long
floor-fall as **"~late 2017?"**. The record dates it to the minute — Dan to his
mother, *"Should I️ tell u she fell trying to walk out"*, **00:06 on
2017-11-26** — and then contradicts the retelling in four places:

| The pages said | The record says |
|---|---|
| Dan woke to a "bump" at 8:00 AM and found her | He reported the fall at 00:06 and was awake through the night |
| Suz arrived "around 10:00 AM" | *"I'll be over in 10"* at **12:41**; *"On way back"* at 13:41 |
| Fran still down at 2:00 PM, lifted at 4:00 PM | *"she's up and walking around now"* to Ellen Ulmer at **13:21** |
| An all-night **video-keno** marathon | The word "keno" appears **nowhere** in ±2 days |

None of that was reachable by search. All of it was one window away, for years.

**The failure has no symptom.** A page with a wrong date reads exactly like a
page with a right one. Nothing goes red, nothing enters `WORK.md`, and every
synthesis that reasons over the sequence inherits the error silently. This is
the same shape as the source-mention debt in `corpus/source-mention-debt.md` —
and worse, because a date is load-bearing for every page downstream of it.

## Validation

`bin/wiki-corroborate check` gates in `bin/wiki-check` and fails a commit that
writes a **new** dated claim inside coverage with no record covering it. It
reads the working diff, not the tree, so it fires on the pass that creates the
debt rather than on 378 pages of inherited debt. There is no skip flag.

`bin/wiki-corroborate scan <page> --hedged` lists a page's own admitted
uncertainties; `queue` orders the wiki by them.

## Known limits

**Coverage is real and uneven.** 2012–2014 and 2022 are empty; 2011 has one row.
Nothing about a claim in those years can be settled here in either direction.

**79% of the master CSV's Sent rows carry no handle**, so a window can show what
Dan wrote without showing who he wrote it to. The dox dump is the corpus with
reliable direction and counterparty; where the two disagree about *who*, prefer
it and say so.

**A window is not the whole of a day.** These are three exports of overlapping
records and none is a superset — the tool reads all three and dedupes, and it is
still an archive somebody made on a particular afternoon, not the world.

**It cannot corroborate what nobody texted about.** Silence in a window is
evidence that the thing was not discussed by text, which is a much weaker claim
than the thing not happening, and the difference matters most for exactly the
events people do not put in writing.
