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


### 2026-09-02 — A claim of absence needs a deliberately over-broad pattern first — **PROMOTED to `corpus/vocabulary-drift.md`, 2026-09-02**

- **Observed during:** mining the @danfrank twitter archive for the production identity's public arc
- **Surface:** `bin/mine-tweets timeline`, `bin/mine-messages grep`, `bin/text-metrics` — any instrument used to establish that something is *not* in a corpus
- **Observation:** a narrow pattern (`soundcloud|ableton|mixtape|sloppp|mogzart|gripnotic|…`) returned zero hits for 2017 through 2025 and I was one step from writing "eleven years of public silence" onto `wiki/interests/music/overview`. Re-running with a deliberately over-broad vocabulary (adding `remix|mix|dj|producer|track|beat|studio|bass|edm|mastering`) returned hits in 2017, 2022 and 2024 — every one a false positive on reading (a double **bass** at a concert, "**beat** to death with a lead pipe", the "don**bas**" region, Biden "**beat** him", "**track** record"). The zero survived, but the *boundary moved*: the real last post is 7 March 2016, not somewhere in 2016, and the run is ten years rather than eleven. A narrow pattern that returns zero cannot distinguish "he never said it" from "he never said it *that way*", and it fails silently in the direction that makes the finding look stronger.
- **Candidate invariant:** a positive claim is supported by the hits you found; a negative claim is only as good as the hits you would have found. The two need opposite search strategies, and the absence claim needs the expensive one.
- **Candidate instruction:** before writing that something is absent from a corpus, re-run with a pattern wide enough to produce false positives, and **read every hit individually**. If the broad pattern returns nothing at all, the pattern is probably still too narrow. State the window's coverage alongside the zero — here the 2017–2025 window is spreadsheet-complete, which is what makes its zero a real zero rather than a retrieval gap, and the 2010–2012 counts are live-scrape floors where the same zero would have meant nothing.
- **Second instance, same day, and it generalises the rule:** mining the politics arc a few hours later, a pattern built from 2012–2024 political vocabulary (`trump|biden|obama|democrat|…`) returned **0.0% for 2026**. 2026 is not apolitical — it contains "EVERYBODY🙏HATES🙏ISRAEL🙏", a read on Curtis Sliwa's "antizionist credentials and… the new Tucker lane of nat con populism", and "It's Irish Zionism". None of those words were in the pattern. The corrected figure is **23.1%**. I was one edit from publishing "the politics sicko went silent in 2026", which is false and would have been the most quotable claim in the pass.
- **The stronger rule this implies:** the first instance looked like *a pattern too narrow*. This one is not narrowness — it is **drift**. A vocabulary changes across a seventeen-year corpus, and a keyword list built from the middle of that span reports the ends as empty. The failure is worst precisely where the corpus is most interesting: a year whose subject matter is *new* is the year a fixed pattern is least able to see. Any per-year table over a long corpus is exposed to this, not just absence claims.
- **Validation:** reproducible in both directions — `bin/mine-tweets timeline '<narrow>'` vs `'<broad>'` disagree about 2017/2022/2024 for music, and about 2026 for politics. Two instances now, and both PROTOCOL §3 tests pass. **Still not promoted, deliberately:** both occurrences are the same author, in the same session, on the same corpus, which is not the independent confirmation §3 is asking for. Promote when it catches someone else, or a different corpus — `bin/mine-messages` over the 196,399-message dump is the obvious next place, and `wiki/interests/music/overview` already carries several absence claims drawn from it that were never checked this way.
- **Third instance, and the one that promoted it:** the politics table built from the second instance was **published** on `wiki/mind/synthesis/2020-left-turn` claiming "two steps, not one" — a 2017 engagement step and a 2013–2016 off period. Both were withdrawn the same day: with era-appropriate vocabulary 2016 is 9.3% not 4.0% (so the "step" vanishes) and 2013 is 7.8% not 1.4%. A defect that reached a synthesis page is different evidence from a near-miss, and it is what moved this out of the inbox.
- **Status:** promoted → `skills/corpus/vocabulary-drift.md` (see `CHANGELOG.md`, 2026-09-02)

### 2026-09-02 — A self-entered profile field is testimony; the timestamp beside it is a record

- **Observed during:** dating the 2010 Brooklyn move against `wiki/self/facebook`
- **Surface:** `raw/self/facebook/facebook-ihatedanfrank/`; applies to any export that renders user-entered fields and system-generated ones into one table — Facebook, LinkedIn, dating profiles, `contacts.csv`
- **Observation:** `wiki/self/facebook` said "every field cross-checks against context-core" and was the wiki's strongest [DOC] anchor for the biographical spine. One field does not cross-check. `places lived: Brooklyn NYC from Jan 3, 2010` is wrong by eight weeks — the tweet archive has Dan in Florida through 28 February, posting "moving to brooklyn in 9 days" on the 20th. **The same export is right two rows up:** `work history` starts ishlab in March 2010, and `dan@ishlab.com` first appears in a tweet on 24 March. The export contradicts itself, and the split is not random — it is between what Facebook *recorded* (a relationship timestamp, a job entry, a birthday) and what Dan *typed into a form* at an unknown later date. Both render as plain rows in the same table with no visual difference, and `wiki/timeline/periods/2010s` had carried the January 3 date as one of two live candidates for six weeks because of it.
- **Candidate invariant:** provenance inside a single export is not uniform. A field's reliability tracks whether a machine or a person put the value there, and an export flattens that distinction away.
- **Candidate instruction:** before citing a profile export for a date, ask whether that specific field was generated or entered. `relationship … since November 28, 2015` can anchor a period page; `places lived: from Jan 3, 2010` cannot, and should be cited as testimony with the same weight as a memory. Where a self-entered field disagrees with a timestamped source, hold the contradiction on both pages rather than resolving by seniority — the export is still the better source for most of what it contains.
- **Validation:** promote after a second entered-vs-generated split is found in another export. `contacts.csv` and the dating-profile material are the named candidates; neither has been read for this distinction.
- **Status:** inbox

### 2026-09-02 — A transcribed source is not a mined source, and the tree makes it look finished

- **Observed during:** starting the tweet-mining pass
- **Surface:** any large export filed to `raw/` and rendered as `wiki/` pages — `wiki/self/twitter/`, `wiki/self/facebook/`, `wiki/self/youtube-watch-history`, the message corpora
- **Observation:** the twitter archive arrived as 2,525 originals in `raw/` plus eighteen dated yearly pages under `wiki/self/twitter/`, all `knowledge: derived`, all gates green, `queue.md` updated, hub written. Everything about it read as a completed ingest. But `grep -rln 'raw/self/twitter' wiki/ | grep -v '^wiki/self/twitter'` returned pages that mostly cited the *old 2019–2026 sample file*, not the archive — and the archive turned out to close a gap `wiki/timeline/periods/2010s` had declared in its own text, falsify the governing thesis of `wiki/self/tattoos`, and fill a window `wiki/self/location-history` recorded as "N/A". None of that is visible from the twitter tree, because a transcription page is complete *as a transcription* and no gate asks whether anything reasoned from it.
- **Candidate invariant:** rendering a source into `wiki/` satisfies every mechanical check while leaving step 4 of the INGEST operation ("write or update every relevant page") entirely undone, and the result is indistinguishable from a finished ingest by inspection of the tree.
- **Candidate instruction:** after filing a large source, run `grep -rln '<raw path>' wiki/ --include=*.md | grep -v '^<its own tree>'`. A count near zero means the source has been transcribed and not mined, whatever the queue says. Then read the target domains' **stated gaps** first — `wiki/timeline/periods/2010s` named the exact question the archive answered, in its own Gaps section, and that was the highest-value thing in the corpus.
- **Validation:** promote after this is run against a second transcribed source. `wiki/self/youtube-watch-history` and `wiki/self/facebook/posts` are the named candidates and have not been checked.
- **Status:** inbox
