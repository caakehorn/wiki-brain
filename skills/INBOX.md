# Skill Inbox

Unvalidated observations and candidate instructions. This is deliberately append-oriented: do not promote a lesson by deleting the evidence that produced it.

## Entry template

### YYYY-MM-DD — short title

- **Observed during:** task / PR / incident
- **Surface:** files, commands, or subsystem
- **Observation:** what actually happened
- **Candidate invariant:** what appears to remain true
- **Candidate instruction:** what a future agent should do
- **Validation:** evidence needed before promotion
- **Status:** inbox | provisional

---

## Seed candidates

### 2026-08-30 — Persistent cross-agent learning loop

- **Observed during:** creation of the `skills/` section
- **Surface:** all non-trivial repository work
- **Observation:** repository instructions and handoffs preserve process and current state, but reusable lessons can otherwise remain trapped in individual model sessions.
- **Candidate invariant:** durable operational knowledge needs a canonical repository location independent of the LLM or agent that discovered it.
- **Candidate instruction:** capture reusable lessons in `skills/`, route future agents through `skills/INDEX.md`, and promote only validated instructions.
- **Validation:** multiple future agents can discover, follow, revise, and reuse the same skill without relying on the original conversation.
- **Status:** provisional

### 2026-08-30 — A generator's own output is not the published object

- **Observed during:** writing `tests/test_wiki_skills.py` for the skills database
- **Surface:** `bin/wiki-skills check`; applies to every generator here that gates its own output — `bin/wiki-digest`, `bin/llm-publish`, `bin/wiki-plain`
- **Observation:** the gate applied the standing-directive check to the page it had just *rendered*, not to the file on disk. The two are identical only when the drift check above it passed. A hand-edited page that named a person under the directive would have been reported as "the page is behind the database" — a true statement, and not the one that mattered. The check passed for the right reason only by accident of ordering.
- **Candidate invariant:** a check on generated output must run against **the artifact that ships**, not against a fresh render of it. The render proves what the tool *would* publish; only the file proves what is published.
- **Candidate instruction:** where a gate asserts a property of a generated file, assert it on the file's own bytes as well as on the render, and make the test assert the error *message* rather than the exit code — a test that only checks `!= 0` passes when a different error fires first, and will keep passing after the property stops being checked at all.
- **Validation:** `tests/test_wiki_skills.py::TestMoratorium::test_the_gate_catches_a_hand_edit_that_names_her` fails if either check is removed. Generalises `repo/change-safety.md` ("validate behavior, not merely successful commands") from HTTP 200 to a second case; promote after it catches a second instance in another generator.
- **Status:** provisional

### 2026-08-31 — A secret's absence must fail whatever the secret was for

- **Observed during:** diagnosing "the wiki takes up to an hour to reach the site", reported as the site being generally unreliable
- **Surface:** `.github/workflows/notify-portal.yml` here; `.github/workflows/deploy.yml` in `caakehorn/home`; the same shape is claimed for `ANTHROPIC_API_KEY` in `sage-drain.yml` by notify-portal's own header, unverified
- **Observation:** `notify-portal.yml` guarded its dispatch with `if [ -z "$TOKEN" ]; then echo notice; exit 0; fi`, deliberately, with a written rationale: a workflow that fails red over a secret nobody set is one people learn to ignore. `PORTAL_DISPATCH_TOKEN` then stopped being present on 2026-08-28 and the job reported **success eighteen consecutive times while sending nothing**, including runs where its own `What moved` step had counted a changed page. Confirming it needed the *receiving* repository's Actions log — `caakehorn/home` recorded no `repository_dispatch` for three days — because on this side there was no signal at all. The reported symptom was not "a workflow is broken" but "the whole site feels janky", which is what a silent hour of latency looks like from outside.
- **Candidate invariant:** the test is not whether a secret is set, it is **whether the job still accomplishes what its name claims without it**. `notify-portal` exists only to send the dispatch, so a missing token means the job did not happen and must be red. `scripts/wiki-locks.mjs` in the portal is the correct counter-example and should not be "fixed" to match: it requires `WIKI_LOCK_PASSPHRASE` only when `wiki.locks.json` actually seals a page, and no-ops cleanly when it seals none — the secret is conditional there, so its absence is genuinely not a failure.
- **Candidate instruction:** when adding a secret-guarded step, ask what the job still does without the secret. If the answer is "nothing it is named for", exit non-zero and name the secret, the permission it needs and the repository it belongs in. Reserve the quiet-skip branch for work that is genuinely optional, and where it is used, make the run *say which path it took* — a skipped step and a broken step are indistinguishable in the Actions UI. Never let the fallback's existence (here, an hourly cron) justify silence: a backstop that has quietly become the only mechanism is the thing most worth being told about.
- **Validation:** promote after this catches a second live instance. The candidates are already named above — `deploy.yml`'s gate-verifier step was skipped on every run this repository has ever made with nothing on the run to say so, and its adjacent comment asserted a consequence ("the site deploys with the door unconfigured") that was simply untrue and had never been checked; `sage-drain.yml` is claimed to share the shape and has not been read. Both were touched on 2026-08-31 but neither has yet *failed* in a way this rule predicted.
- **Status:** inbox

### 2026-08-31 — A tie-break that is arbitrary is a tie-break that will be wrong

- **Observed during:** filing the intake ledger's first portal export
- **Surface:** `bin/intake` `merge_lines`; the same shape is claimed for `skills/registry/events.jsonl`, which is also an append-only JSONL log merged as a set union across devices — unverified
- **Observation:** `merge_lines` sorted merged events by `(timestamp, id)`. Three of the four units in the first real export were opened, logged and closed in a single tap, which writes three events carrying the same timestamp *to the second*; the id is a ULID whose low half is random, so the tie-break ordered a causal burst arbitrarily. The merged log stated that a unit had been closed before it was opened, and `bin/intake check` rejected it. Nothing about the failure said "ordering" — the four errors read as events against unknown units, because a `unit_created` sorted after its own `intake_logged` means the unit does not exist yet at that line.
- **Candidate invariant:** where a total order is imposed on records that carry a causal relationship, the sort key must encode that relationship above any value chosen for uniqueness. A random tie-break is not neutral: it is a uniform draw over the orderings, most of which are wrong, and second-resolution timestamps make ties the normal case rather than the rare one.
- **Candidate instruction:** when sorting an event log for merge, rank by what each event *does* to the entity (created → mutated → closed) before falling back to the id, and keep the id in the key so concurrent devices still converge to identical bytes. Test with a burst whose ids deliberately sort against causal order — a fixture whose ids happen to agree with it passes either way and proves nothing.
- **Validation:** `tests/test_intake.py::TestMerge` — four cases, including a scrambled burst and an end-to-end merge that must survive `check`. Promote after this catches a second instance; `skills/registry/` is the named candidate, and `bin/wiki-skills` should be read for the same tie-break before it acquires two pushers in the same second.
- **Status:** inbox

### 2026-08-31 — A write path that skips the tool skips everything the tool also did

- **Observed during:** the same pass
- **Surface:** `bin/intake` `close_unit` vs. the portal and ボスの部屋 write paths; the same shape applies to any repository interface writing through GitHub's contents API rather than through `bin/`
- **Observation:** `bin/intake close` does two things — it appends the `unit_closed` event *and* files the unit's immutable report to `raw/health/intake/`. The portal and ボスの部屋 write events straight to `intake/events.jsonl` through the contents API, so they perform the first and not the second. Every one of the four units in the first export was closed and had no archive entry at all, and nothing anywhere reported a problem: `bin/intake check` validates the log against the projection, and the capture is in neither. `intake/README.md` describes the four interfaces as "four interfaces over one code path", which is true of the arithmetic and not of the side effects.
- **Candidate invariant:** when a second interface writes the same data store directly, it inherits the store's format and none of the writing function's side effects — and the side effects are exactly what no consistency check covers, because they live outside the data being checked.
- **Candidate instruction:** for each side effect a CLI write performs beyond the append, either give it a backfill command (`bin/intake capture`) or make the gate assert it. And where an artifact's value rests on *when* it was produced, a backfilled copy must say it was backfilled — the archive here carried "generated once at close, never revised", which would have been false on every file the backfill wrote.
- **Validation:** `tests/test_intake.py::TestBackfilledCaptures` pins the provenance line in both directions. Promote after a second interface-side-effect gap is found; the gate does not yet assert that a closed unit has a capture, which would be the stronger fix and is deliberately not done here — every unit closed before `bin/intake capture` existed would fail it retroactively, which is a red gate for history rather than for a defect.
- **Status:** inbox

