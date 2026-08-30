# Skill Protocol

## 1. Capture the observation

A candidate skill starts as a concrete observation, not an instruction.

Good:
- "Pages returned 200 while serving the wrong artifact; HTTP success was not a valid deployment check."
- "A portal save deleted typed-edge claims without surfacing the loss in the ordinary workflow."

Bad:
- "Always be careful."
- "Use best practices."

Put the observation in `INBOX.md` with enough context to reproduce the reasoning.

## 2. Extract the invariant

Turn the observation into the smallest rule that prevents recurrence.

```text
failure → mechanism → invariant → instruction → validation
```

The instruction must name:
- **trigger** — when it applies
- **action** — what to do
- **reason** — what failure it prevents
- **validation** — how to know it worked

## 3. Validate before promotion

Promote a candidate to `active` only when at least one is true:

- it has prevented or explained the same class of failure more than once;
- a direct test, check, or reproducible command validates it;
- it is mechanically implied by existing repository behavior or a governing spec.

Otherwise keep it provisional or in the inbox.

## 4. Skill file format

```markdown
---
status: active
scope: repo
triggers:
  - description of applicable work
sources:
  - file/path/or/incident
validated: YYYY-MM-DD
supersedes: []
---

# Skill name

## Instruction

Imperative, specific steps.

## Why

The failure mode or invariant.

## Validation

Exact command, test, inspection, or observable condition.

## Known limits

Where the rule does not apply.
```

## 5. Model and agent portability

Skills must describe outcomes and repository actions, not depend on one vendor's hidden behavior.

Model-specific material is allowed only when it genuinely matters. Put it under a clearly labeled `## Adapter notes` section, for example:

- Claude: use `CLAUDE.md` as the governing entrypoint.
- Codex: map the same skill to its repository instruction mechanism.
- Cursor/other agent: read the canonical file directly when no native rule loader exists.

The canonical skill remains in this repository. Adapters are copies or pointers, never competing sources of truth.

## 6. Revision and retirement

Never overwrite history by silently changing what a skill means.

- revise when the invariant survives but the instruction improves;
- deprecate when a better skill replaces it;
- retire when evidence shows it is wrong or obsolete.

Record every state transition in `CHANGELOG.md` with the date and reason.

## 7. End-of-task reflection

Before closing substantial work, run this mental diff:

> What did this agent have to discover that the next agent should not have to rediscover?

If the answer is concrete and reusable, capture it.
