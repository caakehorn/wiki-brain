# Ingest Protocol (LLM-agnostic)

This protocol lets ANY large language model perform a wiki ingestion — no
Claude Code, no API keys, no subscription. It is the durability layer: as
long as some chat LLM exists with a paste box, the wiki can grow.

## The loop

1. `bin/capture status` — see what's in the inbox.
2. `bin/ingest-pack <inbox-file>` — writes `exports/ingest-prompt.md`
   containing the protocol, the source item, and the current content of
   every page it targets.
3. Paste that file's contents into any capable LLM chat.
4. Save the model's entire response to a file (e.g. `response.md`).
5. `bin/ingest-apply response.md` — validates and applies it: writes pages,
   moves the inbox item to raw/, appends log.md, runs bin/wiki-lint.
6. Review with `git diff`, then commit (the apply step prints a suggested
   message), or `bin/ingest-apply response.md --commit` to do both.

Nothing is applied blindly: ingest-apply refuses paths outside wiki/,
refuses to touch raw/ except the single inbox→raw move, and runs the
linter. Git remains the undo button for everything.

## Response format (what the LLM must produce)

The prompt pack instructs the model to answer ONLY with these blocks:

```
===FILE: wiki/people/example.md===
<complete new file content, frontmatter included>
===END===

===MOVE: inbox/<item> -> raw/<domain>/<collection>/<item>===

===LOG: ingest | <domain> | <one-line description>===

===COMMIT: ingest: <short description>===
```

Any number of FILE blocks; exactly one MOVE, LOG, and COMMIT. Everything
else in the response is ignored, so the model may think out loud first.

## The factstory route (hand-typed captures)

Facts and stories typed by hand in `leviathan/factstory.html` arrive as a
self-contained **INGEST BRIEF** markdown file rather than through `inbox/`,
because the person doing the typing is usually not at a terminal. The brief
carries its own copy of the rules so a model with nothing but a paste box can
still ingest correctly.

**`FACTSTORY_BRIEF_TEMPLATE.md` (repo root) is the source of truth for that
brief.** The generator in the other repository is regenerated from it; when the
template changes, the generator must change in lockstep or offline ingests will
drift away from in-repo ones. Its own revision history is at the top of the
file.

## Quality bar

Four rules bind here as much as anywhere, and both the prompt pack and the
factstory brief state all four:

- **Every data point gets an entry.** Coverage is the goal; a thin stub beats an
  omission. The exception is `wiki/people/contacts/`, which stays quarantine.
- **Findings get written back.** If the pass produces a conclusion spanning
  several pages, that conclusion is written into each of them as a typed edge
  whose claim states the finding — not left on one page for the others to
  rediscover.
- **A capture is testimony, not fact** (added 2026-08-02). Hand-typed memories
  are the only place some events exist, and the dates attached to them are the
  least reliable part. Check every date, age and count against the corpus before
  writing prose; when they disagree, table the evidence and say which governs
  rather than silently picking one. The standing example is the brief-#4 batch,
  which dated the Fran sequence to 2017 against seven independent records
  putting it in 2018.
- **Follow every proper noun into `raw/`** (added 2026-08-02). The capture is
  the prompt, not the boundary. The same batch's highest-value output — two
  named gaps closed and a corrected family tree — came from chasing one hostile
  aside about a grandmother into the genealogy export, and none of it was in the
  capture.

The pack embeds STYLE_GUIDE.md and the ingest rules from CLAUDE.md
(one source per pass, complete-sentence prose, tables for numbers,
~8 KB budget, one page per entity, contradictions flagged not overwritten,
absolute dates, `targets:` frontmatter applied first, `[BRACKET]` lines
executed as operator instructions). The model is told to output full-file
replacements — never diffs — so apply stays dumb and safe.
