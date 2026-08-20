# MECHANICAL AUDIT REPORT

Generated: 2026-08-20
Auditor: Free Agent (Yashuwa)
Scope: Phases 0A-0L of the Wiki-Brain mechanical audit

## Executive Summary

The wiki has **476 pages** across **9 domains**. The graph is quantitatively healthy (3,323 prose edges) but semantically under-connected: **996 bare `related:` entries** remain untyped, **36 pages are islanded**, and the LLM manifest is **11 pages stale**.

## Priority Matrix

### P0 — Can silently corrupt or misrepresent knowledge

| Finding | Fix | Who |
|---|---|---|
| LLM manifest stale (465 pages vs 476 actual) | Regenerate after every content pass | Free |
| Retracted "$750/week" figure still on 10 pages | grep gate + manual correction | Free (audit) + Claude (correction) |
| Phantom sources (10 files, 5 cited) | Flag citations, never substitute | Free |

### P1 — Materially harms retrieval or provenance

| Finding | Fix | Who |
|---|---|---|
| 996 bare `related:` entries | Convert to typed connections with claims | Claude |
| 68 pages with `## Related` footers | Convert or delete | Claude |
| 36 islanded pages | Wire into graph with typed edges | Claude |
| 30 pages `status: archived` outside `archive/` | Re-status or move to archive/ | Free (identify) + Claude (decide) |
| 215 pages with `date_modified` before 2026-08-01 | Review for currency | Claude |

### P2 — Significant quality improvement

| Finding | Fix | Who |
|---|---|---|
| 2,229 never-cited raw files | Source-mining campaigns | Claude |
| 2169 large never-cited raw files | Prioritize for extraction | Claude |
| 788 entity candidates (3+ mentions, no page) | Create pages or resolve | Claude |

### P3 — Cosmetic / Low value

| Finding | Fix | Who |
|---|---|---|
| Domain pairs with 0 edges (interests <-> legal) | Cross-domain connections | Claude |
| 24 disconnected domain pairs | Build cross-domain tissue | Claude |

## Phase 0 Audit Reports Produced

| Section | Report | Status |
|---|---|---|
| A | corpus-inventory.json + .md | Complete |
| B | generated-drift.md | Complete |
| C | duplicate-frontmatter.md | Complete |
| D | archive-status-audit.md | Complete |
| E | phantom-sources.md | Complete |
| F | retraction-candidates.md | Complete |
| G | connection-retrofit.md | Complete |
| H | synthesis-audit.md | Complete |
| I | source-coverage.md | Complete |
| J | entity-candidates.md | Complete |
| K | islands.md | Complete |
| L | temporal-audit.md | Complete |
| M | llm-feed-audit.md | Complete |

## Free-Agent Safe Work (Phase 1)

Per Section 24 of the plan:

1. Add duplicate YAML key lint to `bin/wiki-lint`
2. Add generated-feed CI freshness check
3. Add retracted-string gate to `bin/wiki-lint`
4. Add master-timeline generation to required precommit
5. Fix stale root counts/index metadata
6. Fix obvious stale documentation
7. Add phantom-source detection

## Claude-Required Work (Phase 2+)

Per Section 28-38 of the plan:

1. Gchat exhaustive extraction (highest ROI)
2. iMessage per-contact CSV sweep
3. 240 connection retrofit (graph candidates)
4. OPEN.md contradiction resolution
5. High-centrality synthesis review
6. People significance audit
7. Interest lifecycle audit
8. Turning-point synthesis
9. Relationship architecture synthesis
10. Current-state page creation

## Do-Not-Touch-Yet

- Agent architecture review (Phase 5) — wait until content work stabilizes
- Vector DB / RAG (Phase 5) — not yet
- MCP server (Phase 5) — not yet
- Fancy search UI (Phase 5) — not yet
