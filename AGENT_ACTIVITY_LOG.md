# Agent Activity Log

A persistent, append-only ledger of substantive work performed by LLMs and agents in `wiki-brain`.

## Operating rule

Every PR created for work in this repository MUST include an **Agent Activity Log** entry before the PR is considered ready for merge. The entry is written by the model/agent that performed the work and should describe what it actually did, not merely restate the PR title.

The canonical ledger lives in this file. Each PR also carries the relevant entry in its PR body or a top-level PR comment so the local review trail and the repository-wide history stay linked.

### Required workflow

1. Agent receives a task.
2. Agent inspects the relevant wiki/repository state and identifies the work actually performed.
3. Agent makes changes on a branch.
4. Before opening or finalizing the PR, the agent appends one entry to this file on that branch.
5. Agent opens the PR with a copy of the entry, or posts the entry as a top-level PR comment if the PR already exists.
6. If the PR changes materially after review, append a follow-up entry rather than silently rewriting history.
7. On merge, the PR's entry becomes part of the permanent running ledger on `main`.

**No entry = incomplete agent workflow.**

## Entry contract

Each entry must contain:

- **Timestamp:** when the work was performed (local ISO-8601 time when available)
- **PR:** PR number, or `pending` until assigned
- **Agent/model:** the model or agent identity as reported by the executing system; do not guess
- **Task:** the user's requested objective
- **Work performed:** concrete actions taken (inspection, search, extraction, analysis, edits, tests, verification)
- **Files / areas touched:** paths or repository areas actually changed or inspected when useful
- **Reasoning summary:** brief explanation of important decisions, constraints, or rejected approaches
- **Validation:** what was checked, and what was not checked
- **Result:** what changed and the current status
- **Open questions / follow-up:** unresolved items, risks, or `None`

Do **not** fabricate tool calls, tests, confidence, sources, file reads, or results. The log is a provenance record, not a performance review.

## Standard entry template

```markdown
## YYYY-MM-DD HH:MM:SS ±HH:MM — PR #<number|pending>

- **Agent/model:** <reported identity>
- **Task:** <objective>
- **Work performed:** <concrete sequence of actions>
- **Files / areas touched:** <paths / areas>
- **Reasoning summary:** <important decisions and why>
- **Validation:** <checks run; explicitly name anything not verified>
- **Result:** <what changed / status>
- **Open questions / follow-up:** <None or specific items>
```

## Log entries

## 2026-09-02 20:00:00 -04:00 — PR #pending

- **Agent/model:** GPT-5.6 Luna
- **Task:** Create a new wiki-brain system in which every new PR includes a model-authored description of the work performed in a running activity log.
- **Work performed:** Inspected the repository root and the existing agent-access documentation; identified the repository's agent workflow documentation as the appropriate enforcement surface; created this append-only ledger and defined the required PR/agent procedure and entry schema.
- **Files / areas touched:** `AGENT_ACTIVITY_LOG.md`; planned follow-up integration in `AGENT_ACCESS.md`.
- **Reasoning summary:** The log needs to be both repository-persistent and PR-visible. A PR comment alone would fragment history; a file alone would hide the entry from PR review. The system therefore makes the ledger canonical while requiring the same entry to accompany each PR. Follow-up entries preserve provenance when work changes after the initial entry.
- **Validation:** Confirmed the repository contains existing LLM/agent access documentation and that the new branch was created from `main`. No automated tests are applicable to this documentation-only change.
- **Result:** Established the canonical append-only activity ledger and a concrete contract for future model/agent work.
- **Open questions / follow-up:** Add the same requirement to the primary agent instructions so future agents encounter it before creating PRs.

## 2026-09-03 14:00:00 +00:00 — PR #pending

- **Agent/model:** Claude Code, configured model `claude-opus-5` (serving model may differ; not asserted)
- **Task:** Continue the tweet mining for data and insight; add a narrative section at the top of each year's Twitter activity page; remove the quick-link box from the yearly Twitter pages only.
- **Work performed:** Read `LLM_HANDOFF.md` and ran `bin/wiki-work check` and `bin/wiki-lessons route` at session start. Read all 2,741 originals in `raw/self/twitter/archive.jsonl` in date order, 2008–2026, year by year rather than by keyword. Computed per-month row counts, distinct-days-per-month and mean position-in-month by source to characterise the retrieval bias. Wrote a `## Narrative` section on all nineteen yearly pages (~12,000 words); rewrote eleven `## Gaps` sections with per-month figures; replaced the vestigial single month heading above each transcript with `## Transcript`; added `toc: false` to all nineteen. Patched `app.py` and `bin/build-site` to honour that key. Moved `wiki/synthesis/twitter-2024-cognitive-state.md` to `wiki/mind/synthesis/`, rebuilt its frontmatter, indexed and de-orphaned it. Wrote findings back to `wiki/self/twitter`, `wiki/mind/synthesis/2020-left-turn`, `wiki/mind/synthesis/vertical-authority-skepticism`, `wiki/mind/synthesis/millennial-digital-witness` and `wiki/interests/opie-and-anthony` as prose plus typed edges. Added a `forecast` claim class and a `post` channel to `bin/wiki-testimony`; recorded and adjudicated ten dated public forecasts. Re-translated three Reader's Digest twins that went stale. Updated the master-index count and `wiki/mind/index.md`. Appended two observations to `skills/INBOX.md`, an entry to `log.md` and a session entry to `LLM_HANDOFF.md`.
- **Files / areas touched:** `wiki/self/twitter.md`, `wiki/self/twitter/*.md` (19), `wiki/mind/synthesis/{twitter-2024-cognitive-state,2020-left-turn,vertical-authority-skepticism,millennial-digital-witness}.md`, `wiki/interests/opie-and-anthony.md`, `wiki/mind/index.md`, `index.md`, `plain/mind/synthesis/*.md` (3), `bin/wiki-testimony`, `bin/build-site`, `app.py`, `testimony/events.jsonl`, `skills/INBOX.md`, `log.md`, `LLM_HANDOFF.md`, plus regenerated artifacts.
- **Reasoning summary:** The yearly pages warned "in progress — 10-result search cap", which reads as a thin sample; measuring position-in-month showed it is a selection bias (0.838 / 0.681 against 0.500 uniform, versus 0.492 for the operator spreadsheet), so the correct statement is that pre-2014 counts measure queries rather than behaviour. Two red gates on `main` were both the same misfiled page; moving it rather than patching its frontmatter in place was chosen because `wiki/synthesis/` is not a declared domain and the file escaped no lint rule — lint had been red on it too. `forecast` was added as a claim class rather than folded into `existence` or `other_state` because the tool's own design comment cuts classes by kind of proposition and a forecast fails differently from a memory claim. Two claims first written were corrected after checking against existing pages: the caddying and the restaurant work are already documented (`wiki/work/nemacolin-caddying`, `wiki/work/au-zaatar`), and the 2016 gig-tweet contradiction had already been resolved on `wiki/interests/music/overview`; both were rewritten to cite those pages rather than assert novelty. 2015 and 2016 carry a strand not narrated under the standing directive in `CLAUDE.md`, stated on the pages rather than passed over.
- **Validation:** `bin/wiki-check` clean (lint, connect, climb, plain check + audit, freshness, intake, testimony, lessons, skills, history, work scan). `python3 -m unittest discover -s tests` — 367 tests, all pass; the master-index drift test caught the moved page and the count was corrected. `bin/build-tweet-year <year> --check` clean on all nineteen. The `toc: false` guard was executed against real page frontmatter using `app.py`'s own `parseFM` under node: suppressed on `wiki/self/twitter/2013.md`, not suppressed on `wiki/self/twitter.md`. **Not verified:** the public portal. `bin/build-site` no longer renders pages — it emits redirects to `caakehorn/home` — so its `toc` change is inert today, and the box the operator sees is rendered by that repository, which this session could not access.
- **Result:** Nineteen yearly narratives, eleven rewritten Gaps sections, five pages carrying new findings, ten new adjudicated testimony records, two red gates cleared, one misfiled page relocated. All gates green.
- **Open questions / follow-up:** (1) `caakehorn/home` needs one line to honour `toc: false`; `add_repo` was denied for that repository. (2) The 94 stale premises in `WORK.md` are untouched and this pass added more by revising three syntheses. (3) `bin/wiki-work check` does not report `bin/wiki-lint`'s state — deliberate, undocumented in its output, recorded in `skills/INBOX.md` rather than fixed. (4) Leads found and not written up are listed in `LLM_HANDOFF.md`.
