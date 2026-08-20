# Semantic Remediation Record — 2026-08-20

**Auditor:** Free Agent (Yashuwa)
**Scope:** Resolve provenance and link errors from PR #155

---

## Current State (Before → After)

| Metric | Before | After |
|---|---|---|
| wiki-lint errors | 30 | 28 |
| wiki-lint warnings | 23 | 20 |
| wiki-climb errors | 9 | 0 |
| LLM manifest pages | 465 | 476 |
| DIGEST pages | 470 | 476 |

---

## Queue A — Retracted String Errors

### A-1: wiki/legal/463-morgantown.md — $750/week, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** All mentions are inside `CORRECTED [2026-08-18]` blockquotes that explicitly state the figure is wrong. The page is correctly documenting the retraction.
- **Reason:** The wiki-lint validator is flagging the retracted string even though it's inside a correction block. This is a validator limitation — the string is preserved intentionally as part of the correction record.

### A-2: wiki/mind/synthesis/estate-money-spine.md — $750/week, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** All mentions are inside CORRECTED blockquotes or explicitly marked as **retracted**.

### A-3: wiki/mind/synthesis/supply-network.md — $750/week, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** All mentions are inside CORRECTED blockquotes.

### A-4: wiki/mind/synthesis/totality-themes.md — $750/week, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** Mentions are in the context of documenting the correction.

### A-5: wiki/people/alexander-jackson.md — $750/week, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** Mention is in the context of documenting the correction to Suz's finances.

### A-6: wiki/people/ally-lubin.md — $750/week
- **Status:** FIXED
- **Evidence:** The mention was in active prose (not a correction block). Changed to `~$14,000 from Dan to her (Aug–Oct 2018)` and added a CORRECTED block.

### A-7: wiki/people/david-beard.md — $750
- **Status:** VERIFIED_VALID
- **Evidence:** The `$750` here refers to a price negotiation for a product, NOT the Suz borrowing figure. This is a false positive from the validator.

### A-8: wiki/people/suzanne-frank.md — $750/week, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** All mentions are inside CORRECTED blockquotes or explicitly marked as retracted.

### A-9: wiki/self/concepts/claude.md — $750/week, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** Mentions are in the context of documenting the correction.

### A-10: wiki/timeline/periods/2018-deep-cycle.md — $750/wk, $750
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** All mentions are inside CORRECTED blockquotes.

---

## Queue B — Phantom Source Errors

### B-1: wiki/mind/synthesis/bond-switch-2015.md — annie_group_chat_may31-june1_2026.csv
- **Status:** FALSE_POSITIVE
- **Evidence:** Mention is in prose discussing the file as being empty/header-only. The file exists (68 bytes) but is header-only. The wiki page is correctly documenting this.

### B-2: wiki/mind/synthesis/dan-annie-fallout-verdict.md — END_FIGHT_full.csv
- **Status:** FIXED
- **Evidence:** Removed from `sources:` in frontmatter. The file is empty (68 bytes) and was superseded by THE END FIGHT.csv (589 real rows).

### B-3: wiki/self/message-corpora/master-message-dump.md — annie_group_chat_may31-june1_2026.csv, END_FIGHT_full.csv, annie_group_chat_relaxed.csv
- **Status:** FALSE_POSITIVE
- **Evidence:** Mentions are in tables documenting source coverage and correctly identifying these files as empty/header-only.

### B-4: wiki/self/message-corpora/source-coverage-index.md — annie_group_chat_may31-june1_2026.csv, END_FIGHT_full.csv, annie_group_chat_relaxed.csv, messenger_export_THREADKEY_HERE.csv
- **Status:** FALSE_POSITIVE
- **Evidence:** Mentions are in tables documenting source coverage and correctly identifying these files as empty/header-only.

### B-5: wiki/timeline/events/end-fight.md — END_FIGHT_full.csv
- **Status:** FIXED
- **Evidence:** Removed from `sources:` in frontmatter. Superseded by THE END FIGHT.csv.

### B-6: wiki/timeline/events/group-chat-closure.md — END_FIGHT_full.csv
- **Status:** FIXED
- **Evidence:** Removed from `sources:` in frontmatter. Superseded by THE END FIGHT.csv.

---

## Queue C — Broken Wikilinks

### C-1: wiki/self/concepts/astrology-star-signs.md — wiki/self/concepts/dan-as-scorpio
- **Status:** FIXED
- **Evidence:** Target page doesn't exist. Changed to wiki/self/dan-frank (the page that exists and covers Dan's astrological profile).

### C-2: wiki/timeline/2015-annie-read-wiki-impact-analysis.md — wiki/…
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** This is a literal `[[wiki/…]]` in prose discussing the lack of cross-links. It's not a wikilink — it's a placeholder in prose. Ambiguous whether it should be removed or kept as-is.

### C-3: wiki/timeline/annie-read-notes.md — wiki/… (3 instances)
- **Status:** INTENTIONALLY_UNRESOLVED
- **Evidence:** Same as above — literal placeholders in prose discussing cross-links.

---

## Summary

| Category | Total | Fixed | False Positive | Intentional | Verified Valid |
|---|---|---|---|---|---|
| Retracted strings | 10 | 1 | 0 | 8 | 1 |
| Phantom sources | 6 | 3 | 3 | 0 | 0 |
| Broken wikilinks | 3 | 1 | 0 | 2 | 0 |
| **Total** | **19** | **5** | **3** | **10** | **1** |

---

## Files Modified

- wiki/people/ally-lubin.md — Fixed retracted string
- wiki/people/annie-ulmer-personality-assessment.md — Fixed sources → synthesizes
- wiki/people/suzanne-frank-personality-assessment.md — Fixed sources → synthesizes
- wiki/people/diane-moore.md — Fixed broken wikilink
- wiki/self/concepts/ally-and-dan-love-as-destiny.md — Fixed sources → synthesizes
- wiki/self/concepts/astrology-star-signs.md — Fixed broken wikilink
- wiki/self/message-corpora/master-message-dump.md — Removed broken links
- wiki/mind/synthesis/dan-annie-fallout-verdict.md — Removed phantom source
- wiki/timeline/events/end-fight.md — Removed phantom source
- wiki/timeline/events/group-chat-closure.md — Removed phantom source
- DIGEST.md, OPEN.md, RECENT.md — Regenerated
- llm/* — Regenerated

---

## raw/ Directory

0 files modified. All changes are to wiki/ and llm/ directories.
