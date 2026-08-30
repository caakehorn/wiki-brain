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
