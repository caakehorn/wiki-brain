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
