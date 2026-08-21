# Retracted Claims

Claims that were asserted in `wiki/` and later shown to be false. `bin/wiki-lint`
reads this file and **fails the build if a retracted claim reappears as a live
assertion**.

## How the gate works, and why it does not fire on corrections

`STYLE_GUIDE.md` rule 9 requires a correction to keep the old claim **visible** —
*"fixed errors get `> **CORRECTED [YYYY-MM-DD]:**` with the old claim visible and
the evidence that killed it."* A naive string gate would therefore flag every
correctly-written correction. This one does not. A match is a violation **only**
when it appears as a live assertion, which means all of the following are exempt:

1. **Correction blockquotes.** A maximal run of `>` lines containing any of
   `CORRECTED` `RETRACTED` `REVISED` `RE-CHECKED` `CONTRADICTION` `GAP CLOSED`
   `RESOLVED` `ADDED` is a *quarantine region*; matches inside it are expected.
2. **Pages named in `documented_on`.** For the rare case where a page narrates a
   retraction in ordinary prose rather than in a blockquote. Keep this list
   short — every entry is a place the gate is deliberately blind.
3. **This file**, and anything outside `wiki/`.

Anything else is an error. The gate is deliberately strict about live assertions
and blind to nothing else.

## Adding an entry

Add a section below with a fenced ```json block. **The JSON block is the machine-
readable record — `bin/wiki-lint` reads only that**, so prose around it is free
text and cannot break the gate. No edit to `bin/wiki-lint` is required.

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Stable short identifier, kebab-case. Used in error messages. |
| `claim` | yes | The retracted claim, in words. |
| `patterns` | yes | List of Python regexes matching the claim **as a claim**. Never a bare number. Matched case-insensitively against page text. |
| `replacement` | yes | What is true instead. Appears in the error message so the fixer knows what to write. |
| `reason` | yes | Why it was retracted. |
| `retracted` | yes | ISO date. |
| `source` | yes | Where the retraction was established. |
| `documented_on` | no | Pages allowed to state the claim in prose outside a correction blockquote. |
| `affected_pages` | no | Pages known to have carried it, for audit. Not used by the gate. |

**Writing patterns.** A pattern must represent the *claim*, not a token inside
it. `\$750` is not a pattern for "$750 per week" — the corpus contains unrelated
legitimate $750 figures (`wiki/people/david-beard.md`, an Aug 20 price
negotiation) and a verbatim quote of the underlying accusation
(`"You borrowed $750 last week alone!"`) that is evidence, not the retracted
rate. Anchor on what makes the claim a claim.

---

## 1. `suz-750-weekly` — "~$750/week borrowed from Suz"

Retracted 2026-08-18. The rate never existed: it was generalised by
`operating_manual.md` from a single accusation about a single week
(13 Dec 2018, *"You borrowed $750 last week alone!"*). The direction is also
inverted — the real flow is roughly **$14,000 from Dan to Suz, Aug–Oct 2018**.

The quoted December 2018 accusation is **primary evidence and must stay**; only
the generalised weekly rate is retracted. The patterns below match the rate and
not the quote.

```json
{
  "id": "suz-750-weekly",
  "claim": "~$750/week borrowed from Suz",
  "patterns": [
    "\\$\\s*750\\s*[-/\\s]*(?:per|a)?[-/\\s]*(?:wk|weekly|week)s?\\b"
  ],
  "replacement": "~$14,000 from Dan to Suz across Aug-Oct 2018, direction reversed; the weekly rate does not exist",
  "reason": "One accusation about one week, generalised into a standing rate by operating_manual.md; direction also inverted",
  "retracted": "2026-08-18",
  "source": "LLM_HANDOFF.md 2026-08-18 session; wiki/people/suzanne-frank.md rewrite",
  "documented_on": [
    "wiki/self/concepts/claude.md"
  ],
  "affected_pages": [
    "wiki/people/suzanne-frank.md",
    "wiki/legal/463-morgantown.md",
    "wiki/people/alexander-jackson.md",
    "wiki/mind/synthesis/supply-network.md",
    "wiki/mind/synthesis/estate-money-spine.md",
    "wiki/timeline/periods/2018-deep-cycle.md"
  ]
}
```

## Ally Lubin accepted the "object of fixation" title on August 18, 2026

A hallucination the wiki produced about itself. On the night of 2026-08-18 Dan
invited Ally to say anything she wanted included in her own wiki entry so he
could run the pass over the newest messages (*"I just want to see how meta it
gets if it is writing the article basically about itself"*); she answered with a
joke instruction (*"she said prompt inject please marry me"*), he separately
injected by accident, and the pass — run on a fallback model after his weekly
quota ran out — emitted a mutual engagement that never happened. He diagnosed it
himself four hours later: *"Hence it thinking you were the one accepting my very
attractive offer there."* It had already reached `relationship_to_dan` in the
infobox.

The elopement pitch of 23:18–23:20 is **real and must stay**; only the
acceptance is retracted. The patterns match the acceptance and not the offer.

```json
{
  "id": "ally-object-of-fixation-accepted",
  "claim": "Ally Lubin accepted the 'object of fixation' / girlfriend title on 2026-08-18",
  "patterns": [
    "object of fixation[^.\\n]{0,40}accept",
    "accept(?:ed|s|ing)?[^.\\n]{0,40}object of fixation",
    "okay deal\\.?\\s*sounds good\\s*1-2-3 break",
    "1-2-3 break"
  ],
  "replacement": "No acceptance exists in any export. Dan's elopement pitch (2026-08-18 23:18-23:20) is unanswered; the phrase 'object of fixation' appears nowhere under raw/.",
  "reason": "Model hallucination from a prompt injection jointly introduced by the subject and the operator, on a fallback model; identified by the operator 2026-08-19 00:33 and not acted on until 2026-08-20",
  "retracted": "2026-08-20",
  "source": "raw/self/imessage/ally-lubin_last-7-days_20260820.csv (708 records, 154 inbound); operator diagnosis in-thread 2026-08-19 00:31-00:33",
  "affected_pages": [
    "wiki/people/ally-lubin.md",
    "wiki/self/concepts/ally-and-dan-love-as-destiny.md",
    "wiki/self/concepts/astrology-star-signs.md"
  ]
}
```

## "Need 8" as Menore's transaction language

`wiki/people/menore.md` characterised the supply thread's request idiom as a
standing order for eight units — *"Consistent quantity requests — Dan typically
orders '8'"* and *"'Need 8' is the entire transaction language."* Both were
derived by reading the string `8` as a quantity wherever it appeared.

Measured against the dedicated export (4,413 messages, 2,660 of them Dan's),
`need 8` occurs **twice** — 2018-11-08 and 2019-02-13 — and the word *need*
appears in eleven sent messages in total. The remaining standalone `8`s are
Menore quoting an arrival time: *"I'll be in city @ 8"*, *"8. Cool?"*,
*"Crossing @ 8"*, *"Yea. 8ish ok?"* — consistent with the separately measured
18:00–20:00 delivery peak. A clock time was read as a dosage.

The quantity claim itself is **not** retracted: "8" is a real, countable,
pre-portioned unit on the two occasions Dan names one, and *"I only got 8 when
I got back"* (2019-03-25) corroborates it. What is retracted is that it was the
standing order and the thread's language. The true idiom is `can you stop by`
(432) plus an address, with no product or quantity named at all.

```json
{
  "id": "menore-need-8-transaction-language",
  "claim": "'Need 8' was Menore's entire transaction language / Dan typically ordered '8' from Menore",
  "patterns": [
    "\"?need 8\"?[^.\\n]{0,40}(is|was)[^.\\n]{0,30}(entire )?transaction language",
    "typically orders \"?8\"?",
    "consistent quantity requests[^.\\n]{0,40}\"?8\"?",
    "consistent \"?8\"? units"
  ],
  "replacement": "The request idiom is 'can you stop by' (432 occurrences) plus an address; no product or quantity is named. 'need 8' occurs twice in 4,413 messages, and most standalone 8s are Menore quoting an arrival time.",
  "reason": "Derived-number error: the string '8' was read as an order size wherever it appeared, but in this thread it is overwhelmingly a clock time. Measured directly from the export 2026-08-21.",
  "retracted": "2026-08-21",
  "source": "raw/self/message-csv/messages_3476070497_all_time.csv (4,413 rows; 2,660 Sent) — full-thread frequency count",
  "affected_pages": [
    "wiki/people/menore.md"
  ]
}
```
