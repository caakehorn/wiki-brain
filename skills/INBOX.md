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
