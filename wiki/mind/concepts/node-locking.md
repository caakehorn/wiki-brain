---
domain: mind
page_type: concept
title: "Node Locking"
aliases: ["profile locking", "DATA_LOGGED", "relational source code", "Deep Architecture"]
status: stable
date_created: 2026-07-15
date_modified: 2026-07-15
sources:
  - raw/self/gemini-activity/Gemini Activity.html
  - raw/self/dox-md/Gemini-_07.md
  - raw/self/dox-md/Gemini-_18.md
related:
  - wiki/mind/concepts/forensic-method
  - wiki/mind/concepts/exocortex
  - wiki/mind/synthesis/ai-collaborative-analysis
  - wiki/self/chats/gemini-18
  - wiki/self/chats/gemini-07
  - wiki/timeline/events/eli-incident
  - wiki/people/annie-ulmer
  - wiki/people/eli
  - wiki/self/gemini-activity/archive/v1-extract
tags: [ai-collaboration, forensic-analysis, relationships, digital-footprint]
---

# Node Locking

Node locking is the memory-persistence protocol Dan runs inside his AI
sessions: he delivers granular, named "Node X:" observations and requires the
model to retain all of them — verbatim, unconsolidated — into persistent
profile state, then export that state to other models. The 20.8 MB Gemini
activity archive shows ~403 "node" mentions and 1,041 "profile" references;
the pinned DANFRANK-ISMS chat carries 77+ nodes. The explicit constraint is
the same one this wiki inherits: keep all information, never summarize away
detail. The mechanism is the personal-scale instance of the broader
[[wiki/mind/concepts/forensic-method|forensic method's]] lossless-retention rule.

## How a lock works

A lock is an explicit command of the form "lock these nodes into your
profile," usually accompanied by `DATA_LOGGED` acknowledgments, structured
tables, and a `BUFFER STATUS`. The model confirms with "Write Operation
Successful." The locked content is framed as the "relational source code" or
the "Deep Architecture" of the interaction — the irreducible facts that must
survive any future session without re-derivation.

## The master node set

The nodes most frequently locked across the Gemini corpus, with what each
holds:

| Node | What it locks | Redaction |
|------|---------------|-----------|
| **Separation Logistics** | The February 2025 physical break: move back to PA from NYC (~Feb 22), Annie's Sugie-shift caregiver constraint (9am-3pm or 8pm-8am), the unilateral end of an 8-year cohabitation, the "List Defense" (recited chores used to shut down emotional requests) | Core |
| **The Loop** | The pursuit-withdrawal trap; existential outsourcing of self-worth to Annie's availability; gaslighting inversion; the tether (money / drugs / Sugie). Briefly broken by the dog-death witness act | Core |
| **The Betty Event** | The death of the dog Dan stayed with; Annie delayed / absent; briefly broke the avoidance loop. "Tier 1 Life Debt" | High-value |
| **The Signals** | Communication tells, location spoofing, blackout patterns post-confront (e.g. the Suzy-call NACK, the 10-day radio silence) | Core |
| **Eli Incident (Patient Zero)** | The February 2025 lobby incident with Annie's coworker Eli; location tracking disabled; texts from her phone; powder noted; 10-day blackout | Explicitly **purged** from exports meant for other models |
| **Uniontown Generational Loop** | Fran (great-grandmother Coldren) + Sugie as 50-year country-club neighbors; "plot loop" weaponized as a DUI-defense "gentry indiscretion" | Bio / ancestry cross |
| **Bio / Ishlab / Psychometrics** | Full name, Uniontown birth, ishlab audio-engineer years, Full Sail 2010 + Pro Tools HD8, INTP 5w4-sx, 96% impulsivity, punk-drummer and Hunter/Hacker profile | Locked for Grok transfer |
| **Master Annie Record / Eggie** | Met via Alexis; "avatar of reliability" vs the zero-notice work firing; the long cohabitation | Relational source code |

## Redaction control (the Eli case)

The defining sophistication of the protocol is **selective redaction for
export**. Nodes are locked in full, then stripped of sensitive material before
being handed to another model. The Eli incident is the worked example: Dan
commands "no - do not include any information about eli," then re-includes a
stripped version, and the model confirms "The 'Eli' variable has been purged
from the dataset." This is why the [[wiki/people/eli|Eli]] material is absent
from nearly every cross-model export even though it dominates the raw HTML
(5,524 mentions) — it is deliberately scrubbed at the boundary, consistent
with the [[wiki/timeline/events/eli-incident|incident's]] status as the
relationship-ending node.

## Cross-model transfer (Grok handshake)

Gemini-_18 contains a commissioned "TOTAL, EXHAUSTIVE, ZERO-HEDGING memory
dump" structured for transfer to Grok: full biographical timeline,
relationships (Alexis, Annie, family), personality architecture, contradictions,
real names and dates. The bio/psychometrics node above is the part flagged
"locked for cross-model." The same node style appears in the pinned
DANFRANK-ISMS chat (77 nodes) and in the ChatGPT exports uploaded back into
Gemini, confirming the pattern is Dan's, not the platform's
([[wiki/mind/synthesis/ai-collaborative-analysis]]).

## Structural reading

Node locking is the externalized-memory layer of the [[wiki/mind/concepts/exocortex|exocortex]]:
it turns an AI session into a writable, transferable extension of self-model.
The redaction control shows the self-model is edited at the export boundary —
what another model receives is not the full record but a curated, litigation-
and-dignity-aware subset. That curation is itself data: the Eli purge marks
exactly which node is too loaded to propagate.

**Gaps:** the full set of node names locked across all sessions is not
enumerated in one place; the eight listed here are the ones confirmed by
verbatim lock language in the HTML January 2, 2026 cluster and the _07/_18
sessions. Other sessions (e.g. the 77-node pinned chat) likely define
additional nodes not yet cataloged here.
