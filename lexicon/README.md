# lexicon/ — words caught before they are understood

The portal has a box for words. Somebody types a word, a piece of slang or a
phrase into it, and the word lands here as a file — one file per word, parked,
with no analysis attached to it.

This exists because the alternative loses things. A word noticed in passing has
a short half-life: by the time there is a session with the time to work out what
it means, where it came from and whether it is his or borrowed, the word itself
is gone. `sage/` solved the same problem for questions — catch it at the moment
somebody has it, park it, answer it properly later — and this is that mechanism
pointed at vocabulary.

**Nothing analyses a word automatically.** There is no model behind the box. The
word is parked, `bin/wiki-work` lists it as an obligation, and a session works
out what it is and folds the finding into
[`wiki/interests/language/vocabulary-lexicon.md`](../wiki/interests/language/vocabulary-lexicon.md),
which is the page this whole queue drains into.

## Why these files are not in `raw/`

Same reason `sage/questions/` is not: `raw/` is immutable and these files
mutate. A word arrives `pending` and becomes `analyzed` (or `rejected`), and the
reading is written into the same file so the word and what was made of it can
never be separated.

## The file

One file per word, `lexicon/words/<id>.md`, where the id is
`<YYYY-MM-DD>_<HHMMSS>_<slug>` — sortable, unique per second, readable. Exactly
the `sage/questions/` convention, because two programs parse both and there is
no reason for them to differ.

```markdown
---
id: 2026-08-27_143022_choomed
added: 2026-08-27T14:30:22Z
word: choomed
kind: slang
status: pending
analyzed:
targets: []
---

## Note

Whatever context was typed alongside the word. Often empty — the box does not
require it, because requiring it is how a capture box stops being used.

## Reading

Written when a session analyses it. Empty until then.
```

### The fields

| Field | What it holds |
|---|---|
| `id` | `<date>_<time>_<slug>`, matching the filename |
| `added` | ISO timestamp, from the browser that typed it |
| `word` | the word, slang or phrase, verbatim |
| `kind` | `word` · `slang` · `phrase` · `insult` · `praise` — a rough bucket, not a taxonomy |
| `status` | `pending` · `analyzed` · `rejected` |
| `analyzed` | date the reading was written |
| `targets` | every `wiki/` page the reading was written into |

`kind` is deliberately coarse. It is a sorting hint for whoever drains the
queue, not a claim about the word, and a session is free to disagree with it in
the reading.

## Analysing one — the operation

This is an INGEST in miniature and follows the same discipline. The short form:

1. **Read the word as given.** The note may be empty, wrong, or a joke. The word
   is the datum.
2. **Check the corpus before deciding what it is.** `bin/mine-messages grep` and
   `bin/text-metrics` over the message record answer the only question that
   distinguishes a real finding from an impression: *does he actually use this,
   and since when?* A word he likes and never says is a different fact from a
   word he says four hundred times, and the vocabulary-lexicon page already
   carries that distinction as its central caveat — it records words **selected
   as pleasing**, not words observed.
3. **Write the reading into the file** under `## Reading`, with the counts.
4. **Fold it into `wiki/interests/language/vocabulary-lexicon.md`** — into the
   argument, not appended as a list item. If it belongs somewhere else as well
   (`wiki/mind/profile/linguistic-profile.md` for a register finding, a person
   page if the word is traceable to one channel), write it there too and add
   both to `targets:`.
5. `status: analyzed`, `analyzed: <date>`, then the gates and a `lexicon |`
   line in `log.md`.

A word that turns out to be nothing — borrowed wholesale, used once, not his —
gets `status: rejected` and one line saying so. **That is a real outcome and it
is kept, not deleted.** A word checked and found empty and a word nobody has
looked at yet must not look the same from outside, which is the same rule
`sage/` applies to a declined question.

## What drains here

Everything lands in one page:
[`wiki/interests/language/vocabulary-lexicon.md`](../wiki/interests/language/vocabulary-lexicon.md).
That page already holds two curated batches and their readings, and it carries
the standing caveat this queue is the cure for — that its contents were
*selected*, never *measured*. A word caught in the wild and then checked against
the message record is the first kind of entry it can hold that does not need
that caveat.
