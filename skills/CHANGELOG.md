# Skill Changelog

Append-only. Every promotion, revision, deprecation and retirement, with its date
and its reason. `PROTOCOL.md` §6 forbids silently changing what a skill means, so
a skill that is not named here has entered the corpus with no account of why it
should be believed — and `bin/wiki-skills check` fails on exactly that.

## 2026-08-30 — the subsystem is wired in

The section shipped earlier today as seven markdown files describing a system
that did not exist: `CLAUDE.md` never mentioned `skills/`, so its "mandatory
session behavior" was mandatory nowhere, nothing validated the corpus, and
nothing surfaced what it was holding. This pass makes it real.

**Tooling and routing**

- Added `bin/wiki-skills` — `check` (the gate), `scan` (regenerates
  `INDEX.md`), `route` (runs the routing algorithm rather than describing it),
  `list`, `status`, `next`, `new`.
- `INDEX.md` is now **generated** from the skill files. It previously carried a
  `Status` column duplicating each file's `status:` frontmatter — two sources of
  truth for one fact, which is the defect `WORK.md` exists to not have.
- `bin/wiki-skills check` joined the gate chain in `bin/wiki-check`, and
  unvalidated inbox candidates now surface as obligations in `bin/wiki-work`.
- `CLAUDE.md` routes at the section: the governing set, the architecture map,
  the LEARN operation, the tools table and the pre-commit block.

**Promoted to `active`** — each traceable to a dated incident already in this
repository's record:

- `repo/derived-surfaces.md` — write to the source, never to the surface it
  generates. Two December 2015 read passes were written into the portal's
  derived snapshot; one was deleted by the rebuild cron 39 minutes after merging
  (`log.md`, 2026-08-17). The mirror failure is drift: the 2026-08-20 audit
  found `llm/manifest.json` eleven pages behind `wiki/`.
- `repo/stale-premise.md` — never clear a staleness warning by bumping the date.
  Named in `CLAUDE.md` as the one move that corrupts the system quietly;
  promoted because it is mechanically implied by `bin/wiki-climb check` and
  `bin/wiki-plain check` (PROTOCOL §3, third clause).
- `corpus/message-mining.md` — use `bin/mine-messages` over grep, and
  `bin/text-metrics` for anything about length or cadence. Both tools carry the
  reasoning in their own docstrings: three properties of the dump make naive
  grep quietly wrong, and message-level counts hide the turn-level effect
  entirely (3.05x in 2026 against 1.23x in 2015–19).
- `repo/publication-surface.md` — `.gitignore` is not a privacy control; it
  governs `git add` and never touched the contents API the portal writes
  through. From the intake ledger's two failed arrangements and the operator's
  2026-08-30 decision.

**Recorded, unchanged in substance**

- `repo/session-loop.md` and `repo/change-safety.md` — promoted `active` on
  2026-08-30 with the section itself; named here because the gate requires it
  and their arrival was never recorded.
