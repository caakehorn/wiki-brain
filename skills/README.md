# Agent Skills

This directory is the persistent memory for **how to work on wiki-brain**.

The rest of the repository records what the system knows. `skills/` records what agents and LLMs have learned about **changing the system without repeatedly rediscovering the same operational knowledge**.

A skill is not a personality prompt and not a generic coding guideline. It is a reusable, evidence-backed instruction produced by work on this repository.

## Core rule

> When an agent learns something that would make the next agent materially better at touching this codebase, it writes that learning back here.

This is a feedback loop:

```text
work → observation → candidate instruction → validation → skill → reuse → revision
```

No model is the permanent owner. Claude, Codex, ChatGPT, Cursor, local agents, scripts, and future tools all read and improve the same corpus.

## Two layers, one subsystem

The prose layer answers *what should an agent do here?* and a person reads it.
It cannot answer the other question, which is the one that actually blocks
cross-model work: **what does each model actually have?** A Claude Code session
arrives with skills, MCP servers, plugin tools and subagents a Codex session
does not have, and neither can see the other's. So there is a second layer, and
it is a database rather than prose because its writers are machines running in
parallel.

```text
skills/
├── README.md          # this contract
├── INDEX.md           # active skills and routing
├── PROTOCOL.md        # how to create, test, revise, and retire skills
├── INBOX.md           # unvalidated observations and candidate lessons
├── CHANGELOG.md       # append-only history of promotions/revisions/retirements
├── <domain>/
│   └── <skill>.md     # one reusable skill per file
└── registry/          # THE DATABASE — what each model has, pushed by the model
    ├── README.md      # the manifest format and the one rule with teeth
    ├── events.jsonl   # append-only; the record
    ├── registry.json  # a projection of the log; regenerable
    └── manifests/     # worked examples of the half a scan cannot see
```

`bin/wiki-skills` writes the database; `wiki/meta/skills.md` is its public face,
generated and served on the portal like any other page. Full instruction:
`skills/agents/registry-push.md`.

## Mandatory session behavior

Before making a non-trivial code or repository change:

1. Read `skills/INDEX.md`.
2. Load every skill whose trigger matches the task.
3. Push what you have into the database, and read what the others have:

   ```bash
   bin/wiki-skills push --scan --agent <your-id> --vendor <v> --surface <s>
   bin/wiki-skills push -f skills/registry/manifests/<your-id>.json
   bin/wiki-skills page
   ```

   The scan covers this repository. The manifest covers your own skills, MCP
   servers, plugin tools, subagents and harness — nothing in the working tree
   records those, so if you do not declare them nobody else will know you had
   them. The push is idempotent; recording nothing is a success. **Environment
   variable names only, never a value: this repository is public.**

After completing work:

1. Ask whether the session exposed a repeatable failure mode, hidden invariant, useful command sequence, or model-specific trap.
2. If yes, add it to `skills/INBOX.md` or revise an existing skill.
3. Promote only validated instructions according to `skills/PROTOCOL.md`.
4. Record promotions, revisions, and retirements in `skills/CHANGELOG.md`.

## What belongs here

- repo-specific commands that are easy to get subtly wrong
- invariants discovered while debugging
- workflow sequences that prevent recurring failures
- tool/agent differences that matter in this repository
- reliable validation procedures
- lessons extracted from failed PRs, merge conflicts, broken builds, or silent regressions

## What does not belong here

- generic programming advice
- temporary session state (use `LLM_HANDOFF.md`)
- standing work (use `BACKLOG.md` / `bin/wiki-work`)
- source facts about Dan or the wiki corpus
- one-off prompts with no reusable operational content

## Governing relationship

`CLAUDE.md` governs repository operations. Existing specs govern their named domains. Skills are subordinate to those documents: they operationalize knowledge; they do not silently override policy.

When a skill conflicts with a governing document, the governing document wins and the conflict itself should be recorded for repair.
