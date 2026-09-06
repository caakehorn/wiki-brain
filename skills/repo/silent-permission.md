---
status: active
scope: repo
triggers:
  - writing or changing a guard that refuses, blocks, redacts or withholds
  - a safety check that reads a frontmatter field to decide whether a rule applies
  - reviewing an enforcement point for any operator directive held as code
  - a check whose failure mode is allowing rather than blocking
sources:
  - bin/wiki-crosslink — under_moratorium(), and the nine pages it missed
  - bin/wiki-plain — MORATORIUM, and the `annie_metadata_24h.csv` boundary hole
  - tests/test_wiki_crosslink.py — LinkPlacement, the refusals that remain
  - tests/test_wiki_plain.py — TestLaneRefusal, the refusal that remains
validated: 2026-09-04
revised: 2026-09-06
supersedes: []
---

# A guard that fails open leaves no trace, so it has to be tested against the corpus it guards

## Instruction

1. **Ask what the guard reads, then ask how often that field is absent.** A
   check keyed on `title:` looks total and is not: **288 of 497 pages here carry
   no `title:` field at all.** Resolve the subject the way the rest of the file
   already resolves it — in this repository that means `title_of()`, which falls
   back to `infobox.name` and then to the slug.
2. **Write the test in both directions.** A test that only asserts the refusal
   is satisfied by a guard that refuses everything, which is its own failure —
   `bin/wiki-crosslink`'s guard is deliberately narrower than `bin/wiki-plain`'s
   because porting the wider rule across would withhold 197 of 497 pages for no
   safety gained. Assert what it refuses **and** what it must not.
3. **Pin the real pages, not only synthetic ones.** The synthetic cases pass
   against a guard that has never met the corpus. The regression that closed the
   second hole below named all nine exposed pages by slug, so it could not
   reopen quietly.
4. **Check every enforcement point, not the one you are in.** The same directive
   is enforced in two files here and both shipped with a hole of this shape.
   Finding one is a reason to go and read the other.
5. **A guard's blind spot is found by measuring, not by reading it.** Both holes
   were found by accident — one by hand-checking a translation, one because a
   frontmatter sweep touched a page and nothing fired. Neither was found by
   looking at the code, and the code looked correct both times.

## Why

**Every other check in this repository fails closed.** `bin/wiki-lint` goes red,
`bin/wiki-plain check` blocks a commit, `bin/wiki-climb check` prints a warning
somebody eventually reads. A guard that refuses is the opposite: when it is
wrong it **permits**, and permission produces no output, no exit code and no
warning. The only evidence is the thing it should have stopped, happening
normally.

Two instances, both on the Annie moratorium — **an operator directive that has
since been lifted (2026-09-06), which changes nothing about the lesson**: the
evidence is what a fail-open guard costs, not which rule it was enforcing. Two
different tools, neither found deliberately:

| Tool | What it read | What it missed |
|---|---|---|
| `bin/wiki-plain` | `\bannie\b` | `_` is a word character, so the trailing boundary fails against `annie_metadata_24h.csv` — the filename that material is cited by throughout. A page carrying it twice read as ELIGIBLE FOR TRANSLATION. |
| `bin/wiki-crosslink` | `scalar(fm, "title")` + aliases | 288 pages have no `title:`. **Nine pages were invisible**, including `wiki/timeline/annie-record`, `wiki/people/ellen-ulmer` and `wiki/timeline/events/shelbie-annie-threesome-april-2019` — pages squarely about her, which `scan` would have accepted as subjects and offered as targets to write edges onto. |

The second one is worse than it looks, because `bin/wiki-crosslink`'s whole
output is a worklist. A candidate list that includes her page is an instruction
to write about her, in the column nobody was checking: the guard was enforced on
the page being scanned and not on the pages being *offered*, which is the same
defect from a third angle and was fixed the same day.

**The measurement that would have found either one takes a minute.** For the
second: `288 of 497 pages have no title:` is one loop over the corpus, and it
makes the hole obvious the moment anybody asks what the guard reads.

**Both guards are gone now and the live examples of the shape are elsewhere** —
`bin/wiki-crosslink`'s `--apply` refusals (a wikilink written inside somebody's
quoted words leaves no trace either), `bin/wiki-plain`'s lane refusal, and any
exemption list in a gate, which is a fail-open guard wearing a different hat.

## Validation

`python3 -m unittest tests.test_wiki_crosslink.LinkPlacement` — the surviving
refusals of this shape, pinned against the real corpus.
`tests.test_wiki_plain.TestLaneRefusal` pins the other. The two moratorium
regressions this skill was written from were removed on 2026-09-06 with the
directive; `TheMoratoriumIsLifted` in each file now pins the *absence* of the
guard, which is the same discipline pointed the other way.

Broader check, for a guard anywhere in this repository: count how many pages
lack the field the guard reads. If the answer is not zero, the guard has a blind
spot the size of that number.

## Known limits

**This says nothing about whether the rule is right, only whether it runs.** The
narrowness of `bin/wiki-crosslink`'s threshold against `bin/wiki-plain`'s is a
judgment about what the directive actually forbids, measured at 197 pages, and
no test can settle it — only the operator can.

**It does not generalise to checks that fail closed.** A gate that goes red when
it is wrong announces itself and does not need this treatment; the cost of a
false positive there is an annoyed session, not a silent breach.
