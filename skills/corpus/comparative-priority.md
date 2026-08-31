---
status: active
scope: corpus
triggers:
  - a claim that ranks two people against each other
  - writing or revising a page that names two partners in the same finding
  - message volume, thread concurrency or response latency compared across contacts
  - Dan said different things to two people and the difference is being interpreted
  - a synthesis about attachment, primacy, substitution or which bond mattered more
sources:
  - CLAUDE.md — "the four things that matter most", comparative claims about people
  - SYNTHESIS_SPEC.md — the constitution pass
  - operator directive, 2026-08-31
validated: 2026-08-31
supersedes: []
---

# A ranking is a claim, and it needs its own evidence

## Instruction

When a page is about to say that one person mattered more to Dan than another —
was primary, was chosen, outranked, was the real one — that sentence is a claim
in its own right and carries its own evidentiary burden. It is not a summary of
the measurements sitting next to it.

These inferences are invalid on their own. Each is a real finding about
something else:

| Observation | Does **not** establish | Is evidence of |
|---|---|---|
| He said different or contradictory things to each | a hierarchy | compartmentalization, conflict avoidance, impression management, uncertainty, a changed mind, different questions answered, or a lie — the record has to say which |
| One thread carries more messages | greater significance | where attention went in those hours |
| One relationship ran longer | current priority | duration |
| One thread carries the crisis | relational primacy | which channel the crisis was in |
| Both threads run in the same hours | that one is the cover for the other | concurrency, and nothing more |

What a comparative claim actually requires, in order:

1. **The claim, stated narrowly** — who, ranked on what dimension, over what window.
2. **Evidence appropriate to that dimension.** Volume evidences volume. A claim
   about significance needs something that measures significance.
3. **Temporal scope**, attached to the claim rather than left implied. A ranking
   true in one window is not a standing fact about a person.
4. **The competing explanations, named and dismissed on the record** — because
   for every observation in the table above there are several, and picking one
   silently is where the ranking gets manufactured.

If any of the four is missing, write the measurement and stop. A recorded
observation with the conclusion explicitly deferred is a complete and correct
outcome, and `wiki/people/annie-ulmer.md` does exactly this at the August 18–19
overlap: the hour table, then *"recorded here as evidence… not a conclusion
drawn on this person page."*

## Why

A ranking manufactured this way is unusually durable, because it arrives
wearing the evidence for something else. The numbers under it are real and
check out; only the arrow from them to the conclusion is invented, and no
later gate can see an invented arrow. It then becomes a premise, and the pages
that reason from it inherit a hierarchy nobody ever established.

It is also the failure most likely to be committed by a session trying to be
rigorous, because the observations really are findings. The discipline is not
to distrust the measurement — it is to notice that the measurement and the
ranking are two claims and only one of them has been evidenced.

**The correction is also a trap.** In August 2026 a draft fixed a version of
this on `ally-lubin` and `contact-gini` by replacing *"408 messages to Annie
and 552 to Ally"* with *"more messages to Ally than to Annie, by a three-figure
margin"* — deleting the exact counts while keeping the comparison. That is
backwards. The counts were the evidence and were never the problem; the
unevidenced arrow was. Remove the conclusion, keep the record. A corrected page
should end up with **more** checkable fact on it, not less.

## Validation

The page states its comparative claim with the dimension, the window and the
evidence for that dimension, and names at least one competing explanation it
ruled out. Every quantity the argument rested on is still on the page and still
exact. A reader can disagree with the conclusion without having to go back to
`raw/` to find out what the numbers were.

## Known limits

This does not forbid comparison, and it does not install a reverse default: a
ranking is not made safer by pointing the other way. Some comparative claims are
well evidenced and belong on the page — a cohabiting eleven-year relationship
and a correspondent never met in person differ in ways the record states
directly, and `page_type: synthesis` exists to carry exactly that kind of
conclusion once it has been earned. The rule is about the arrow, not the claim.
