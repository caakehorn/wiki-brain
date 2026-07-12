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

## Quality bar

The pack embeds STYLE_GUIDE.md and the ingest rules from CLAUDE.md
(one source per pass, complete-sentence prose, tables for numbers,
~8 KB budget, one page per entity, contradictions flagged not overwritten,
absolute dates, `targets:` frontmatter applied first, `[BRACKET]` lines
executed as operator instructions). The model is told to output full-file
replacements — never diffs — so apply stays dumb and safe.
