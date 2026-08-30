# Skill Changelog

## 2026-08-30

- Created the canonical `skills/` subsystem for persistent, cross-model operational learning.
- Added routing (`INDEX.md`), lifecycle rules (`PROTOCOL.md`), candidate capture (`INBOX.md`), and initial repository skills.
- Added the registry: `skills/registry/`, an append-only cross-model database of
  what each model actually has — skills, MCP servers, plugin tools, subagents,
  harnesses and this repository's own commands. Written by `bin/wiki-skills`,
  rendered public at `wiki/meta/skills.md`, gated in `bin/wiki-check`. This
  makes the third mandatory session step in `README.md` a real operation rather
  than an intention; it had named a "running directory" that did not exist.
- Promoted `agents/registry-push.md` to active — the instruction for a model
  told to update the skills in the wiki. Seeded with 51 capabilities from one
  model; the diff view is worth nothing until a second model pushes.
