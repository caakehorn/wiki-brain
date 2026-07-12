# LLM Model Coordination & Handoff Log

**Purpose:** This file acts as a centralized brain and handoff document for different AI models working on the Wiki Rewrite Project. Because this project is being handled across multiple sessions and potentially different models, this file ensures continuity, tracks recent file changes, and dictates the immediate next steps.

---

## 🛑 INSTRUCTIONS FOR INCOMING MODELS
1. **Read this file first** to understand the current state of the project.
2. **Check `task.md`** in the root directory for the granular task checklist.
3. **Check `STYLE_GUIDE.md`** (or `CLAUDE.md`) for the strict formatting and prose rules.
4. **When you finish your session**, update the **Session Log** below with a brief, clear summary of what files you modified and what your last action was. Update the **Current Focus** section so the next model knows exactly where to pick up.

---

## 🎯 Current Project Status
- **Phase 1 (Core Spine):** Complete (`context-core.md`, `overview.md`, `index.md`).
- **Phase 2 (Concepts):** Complete. All concepts rewritten to prose and stabilized.
- **Contact Stubs Issue:** Resolved. 97 stubs cross-referenced against `contacts.csv`; 73 renamed; collisions merged. 2 more (danielle-onesi, alexi-armel) merged into primary pages 2026-07-11. ~22 unidentified `contact-xxxxxx` stubs remain (await user identification).
- **STYLE_GUIDE.md now EXISTS** (repo root) — it is the binding page-format spec. The extended frontmatter that earlier sessions introduced (title/aliases/tags/importance/changelog + LLM Quick Brief) is now official; invented page_types like `author-stub` are banned (use `status: stub`). `bin/wiki-lint` must pass (0 errors) before every commit.
- **Phase 3 (Synthesis):** 5 of 12 done (forensic-methodology, attachment-trauma-bond, totality-themes, ai-collaborative-analysis, political-psyops).

## 🚀 Current Focus & Next Steps
**Continue Phase 3 (Mind / Synthesis)** — 7 files remain, see `task.md`. Then Phase 4 (People primary cast).

Standing rules learned this cycle:
- Commit your work before ending a session — do not leave the tree dirty.
- Never write exports/corpus files into the repo root (exports/ is gitignored).
- Process inbox capture notes (especially `targets:` corrections and `[BRACKET]` operator instructions) BEFORE rewriting the pages they touch — see STYLE_GUIDE.md "Capture-note handling."
- Renames must update every inbound link (`grep -r` before and after) and merge any matching `contacts/` stub.

---

## 📝 Session Log (Newest First)

### [2026-07-11] - Session: Coordination Stabilization + Phase 3 Continuation
* **Model:** Claude Fable 5 (Claude Code)
* **Summary:**
  - Audited the multi-model workflow; verdict: output good, coordination drifting. Fixes:
  - Committed prior session's uncommitted Phase 3 work (3 synthesis rewrites + task.md).
  - Untracked `corpus_2026-07-11.md` (1MB export accidentally committed to root); gitignored `corpus_*.md`.
  - **Wrote `STYLE_GUIDE.md`** — codifies extended frontmatter, LLM Quick Brief, capture bracket-instructions; CLAUDE.md now points to it. Fixed 8 invalid page_types (`author-stub`/`artist-stub` → `entity`+`stub`); lint back to 0 errors.
  - Added the two missing oversized pages to task.md Phase 3.
  - **Ingested both capture corrections:** `danielle.md`→`danielle-onesi.md` (full name, "Dee", merged 44-msg contact stub) and `lex.md`→`alexis-armel.md` (aliases, merged 41-msg inbound-only stub, first-mention Alexis links added in 12 pages). All inbound links rewritten; notes filed to `raw/people/captures/`.
  - **Phase 3:** rewrote `ai-collaborative-analysis.md` (21KB→7.6KB, worst v1 chatter in wiki) and `political-psyops.md` (11KB→6.9KB, triplicated J6 sections deduped).
  - App renderer now supports `[[path|label]]` pipe links.
* **Handoff Note:** Tree clean, lint 0 errors / 16 warnings (all size-budget). Next: remaining 7 Phase 3 synthesis files, then Phase 4. Inbox holds 3 items (saratoga-drive story, ANCESTRY_DNA.txt, takeout manifest) awaiting regular ingestion.

### [2026-07-11] - Session: Contact Stubs & Phase 2 Completion
* **Model:** Gemini 3.1 Pro (High) / Antigravity
* **Summary:** 
  - Wrote a python script (`bin/contact-rename.py`) to cross-reference 97 `contact-xxxxxx.md` stubs against `contacts.csv`. Successfully renamed 73 stubs to proper names. 
  - Identified two collisions from the rename: `vanessa-frank.md` and `annie-ulmer.md`. Merged their high-volume iMessage corpus data into the canonical `wiki/people/vanessa-frank.md` and `wiki/people/annie.md` pages, then deleted the redundant contact stubs.
  - Completed the remaining Phase 2 concept rewrites: `conflict-architecture.md`, `dans-law.md`, `forensic-analysis.md`, `cato.md`, and `phenomenology-lens.md`. Converted fragments to prose, formatted tables, and set status to `stable`.
  - Checked off Phase 2 in `task.md`.
  - Committed all changes to git.
* **Handoff Note:** The repository is in a clean state. Ready to tackle Phase 3 or Phase 4.

### [2026-07-11] - Session: Phase 1 & 2 Kickoff (Previous Session)
* **Summary:** 
  - Upgraded frontmatter and added LLM briefs to `wiki/self/index.md` and `wiki/self/overview.md`.
  - Fixed status in `wiki/self/context-core.md`.
  - Full style-guide rewrite for `wiki/people/annie.md`.
  - Prose rewrites for `wiki/mind/concepts/abyssal-architect.md`, `attachment-model.md`, and `contact-gini.md`.
  - Fixed `.git/index.lock` issue and committed changes.
