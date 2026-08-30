# Skill Index

Read this before non-trivial repository work. Load skills by trigger, not by curiosity.

| Skill | Trigger | Status |
|---|---|---|
| `repo/session-loop.md` | Any multi-step code/repository task | active |
| `repo/change-safety.md` | Editing commands, workflows, build logic, or repository-wide behavior | active |
| `agents/registry-push.md` | Told to update the skills in the wiki; a skill, MCP server, hook or subagent changed; a model working here for the first time | active |

The machine-readable half of this index is `skills/registry/` — every skill,
command, MCP server, subagent and harness any model has declared, with who
declared it and when. Read it before assuming a capability is absent:

```bash
bin/wiki-skills list --kind command    # the bin/ tools, with their own summaries
bin/wiki-skills diff <you> <them>      # what another model has that you lack
```

## Routing algorithm

1. Identify the files, commands, workflows, and subsystems the task can affect.
2. Load every skill whose trigger intersects that surface.
3. Prefer the narrowest applicable skill first.
4. If no skill applies but the work teaches a reusable lesson, create an INBOX candidate after validation.
5. Do not treat absence from this index as permission to invent repository conventions.

## Status meanings

- **active** — validated and expected to be followed
- **provisional** — useful but not yet sufficiently validated
- **deprecated** — retained for history; do not use for new work
- **retired** — known wrong, obsolete, or superseded
