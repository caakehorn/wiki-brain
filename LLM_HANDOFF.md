# LLM Model Coordination & Handoff Log

**Purpose:** This file acts as a centralized brain and handoff document for different AI models working on the Wiki Rewrite Project. Because this project is being handled across multiple sessions and potentially different models, this file ensures continuity, tracks recent file changes, and dictates the immediate next steps.

---

## 🛑 INSTRUCTIONS FOR INCOMING MODELS
1. **Read this file first** to understand the current state of the project.
2. **Check `task.md`** in the root directory for the granular task checklist.
3. **Check `STYLE_GUIDE.md`** (or `CLAUDE.md`) for the strict formatting and prose rules.
4. **When you finish your session**, update the **Session Log** below with a brief, clear summary of what files you modified and what your last action was. Update the **Current Focus** section so the next model knows exactly where to pick up.
5. **Pull all items in `ADD-ME.md` and append these items to the current ingest queue or the current prompt query**

---

## 🎯 Current Project Status
- **Phase 1 (Core Spine):** Complete (`context-core.md`, `overview.md`, `index.md`).
- **Phase 2 (Concepts):** Complete. All concepts rewritten to prose and stabilized.
- **Contact Stubs Issue:** Resolved. 97 stubs cross-referenced against `contacts.csv`; 73 renamed; collisions merged. 2 more (danielle-onesi, alexi-armel) merged into primary pages 2026-07-11. ~22 unidentified `contact-xxxxxx` stubs remain (await user identification).
- **STYLE_GUIDE.md now EXISTS** (repo root) — it is the binding page-format spec. The extended frontmatter that earlier sessions introduced (title/aliases/tags/importance/changelog + LLM Quick Brief) is now official; invented page_types like `author-stub` are banned (use `status: stub`). `bin/wiki-lint` must pass (0 errors) before every commit.
- **Phase 3 (Synthesis):** 5 of 12 done (forensic-methodology, attachment-trauma-bond, totality-themes, ai-collaborative-analysis, political-psyops).

## 🚀 Current Focus & Next Steps
**NEW USER DIRECTIVE (2026-07-14, in progress):** The user is walking through `wiki/people/` rewriting every swarm-template stub page (the "Corpus Dimensions / Domain: Self / Part of the long-tail..." boilerplate matching the old christian-hanson.md pattern) into full prose per STYLE_GUIDE.md. 47 of 64 identified stubs are done (see `wiki/people/index.md` for the current one-liner per page — anything still reading "Contact identified via Google Contacts as..." is unstarted). Remaining unstarted: nick-mattie, rj, rod-banks, sam, shannon, slim, steve-kezmarsky, tan-calabrese, teddy, trevor, urpaaa-at-yahoo-com, vaughn, vicki, zach-clabaugh, zach-hendricks, zach, zaco (zach-hendricks and zaco are the same person/handle — merge, don't do both). Method: `python3 dump_contact.py <handle>` style full-corpus pull per contact (see scratchpad script pattern), not just the one sample line the swarm left — write the real relationship/story, not just corpus stats.

**IMPORTANT — direction-field bug:** the `direction` column in `MASTER_MESSAGES_DB_DUMP.csv` is unreliable for most rows (many/most say "Received" regardless of actual sender). Every page written this session notes this explicitly and reconstructs speaker from content. Keep doing this.

**Also in progress: random sampling pass.** Per user request, pulling random 30-40-row windows from anywhere in the 184k-row master CSV (not just the target contact) to surface surprise content and add it to whichever existing page it belongs to. This has already resolved two real contradictions (Fran's April 1 vs April 4, 2018 death date — settled to April 4 via caregiver Marla's dated messages; and the "boyfriend arrested picking up mailed weed" passage on annie-ulmer.md, previously flagged uncorroborated, now cross-referenced to Alexis's independently-documented Valentine's Day 2017 arrest via new-jim-shaffer.md) and added real texture to annie-ulmer.md, kristin.md, tom.md, vanessa-frank.md, fran-coldren.md (2020 estate distribution, $144,069.31), and the March 2026 terminal-phase timeline (filled the March 17–31 gap). If continuing this pass: keep the `random_pull.py` script pattern (random offset + N-row window from the master CSV), read for anything not already in the target page, and check before adding (`grep` the wiki for the key term first — most windows now re-hit already-documented ground, so the strike rate is dropping).

**NEW USER DIRECTIVE (2026-07-13, overrides phase order):** The user judged the wiki's articles "absolutely terrible" in priorities and depth. Three standing orders:
1. **Importance-first structure** — big life events get real articles (e.g. the 2015 arrest now has `wiki/legal/2015-retail-theft-arrest.md`); trivia gets folded in (the BFS drawer dispute is now one page at `wiki/work/bfs-foods.md`, not four).
2. **DENSE pages, mined from raw/** — pages must carry actual content (all personality results with detailed breakdowns now live in `wiki/mind/profile/` — 7 pages incl. a dedicated INTP page). Do not restyle old wiki text; go back to raw sources.
3. **The breadth pass: "thousands of individually trivial missing things."** Named example (done): SLOPPP's page now has its full reconstructed discography + history, mined from Facebook-export share links, Twitter analysis, and message dumps. EVERY comparable page should get this treatment: alias pages, people pages, favorites pages, event pages. Mine raw/ link slugs, the LIFE_EVENTS_CALENDAR, the FB export HTML, and the message CSVs for concrete facts (dates, titles, counts, quotes). GitHub (PR #2, branch claude/wiki-article-restructure-agac7x) is the authoritative copy — push after every chunk.

Then: remaining Phase 3/4 work per task.md, and the chats/ pages cleanup (they still contain /tmp paths and HTML-comment agent chatter).

**NEW USER DIRECTIVE (2026-07-11):** The user judges current page content "an okay start" but wants a deeper pass: pages "omit or look over the most important information" and the categorization needs redesign. Phase 9 added to task.md — a content-depth audit that goes back to raw/ sources per page instead of only polishing prose. When rewriting any page from here on, do not just restyle the existing text: re-read the page's raw/ sources and ask what the *most important* facts are, then lead with those.

**Contact stubs:** `contact-review.md` (repo root) lists all 23 unnamed stubs with handles/samples for the user to name or DELETE (5 pre-marked as automated/spam). Process the user's decisions when they say so.

**Subscription-independent ingestion now exists:** `INGEST_PROTOCOL.md` + `bin/ingest-pack` / `bin/ingest-apply` let ANY chat LLM run an ingestion via copy-paste. If you are not Claude Code, this is also how you can apply multi-file changes safely.

Standing rules learned this cycle:
- Commit your work before ending a session — do not leave the tree dirty.
- Never write exports/corpus files into the repo root (exports/ is gitignored).
- Process inbox capture notes (especially `targets:` corrections and `[BRACKET]` operator instructions) BEFORE rewriting the pages they touch — see STYLE_GUIDE.md "Capture-note handling."
- Renames must update every inbound link (`grep -r` before and after) and merge any matching `contacts/` stub.

---

## ⭐ THE SUBSTANCE STANDARD (read before rewriting anything)
STYLE_GUIDE.md now has a **Substance rules** section that outranks all
formatting rules. Core test: the first paragraph must answer the stranger's
question (person → who is this to Dan + current state + defining thing;
event → what happened + what changed). Order by consequence, not
chronology. Say load-bearing conclusions plainly. Name gaps explicitly.
**Match the exemplars:** `wiki/people/annie.md`, `wiki/people/suz.md`,
`wiki/timeline/events/eli-incident.md` — these were written at the target
quality bar; imitate their shape exactly. A page that is tidy but leads
with corpus statistics instead of the story is a FAILED page.

## 📝 Session Log (Newest First)

### [2026-07-14] - Session: deep-dive expansion of random-pull findings (+ two misattribution corrections)
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Summary:**
  - User directive: every finding added during the prior random-pull phase
    (see the two 2026-07-14 entries below this one) had to be expanded
    into a full reconstructed story using additional raw sources, not left
    as a one-paragraph mention. Worked through the full list:
    kristin.md (Sept 9 meth/homelessness disclosure reframed as a joint
    digital-archaeology session — deactivated Twitter @kpdope, Wayback
    Machine, ChatGPT photo-sorting offer; Sept 2 astrology thread expanded
    with real chart detail, corrected to show Kristin as the astrology
    expert teaching Dan, not the reverse; Sept 19 "Jeff" mention traced
    through its full trigger-to-partial-retraction arc), tom.md,
    march-2026-terminal-phase.md (Feb 21 and Mar 19-20 gap incidents fully
    reconstructed day-by-day), shelbie-annie-threesome-april-2019.md +
    shelbie-breakiron.md (May 1 2019 fight reconstructed as a full day,
    revealing the arrangement's reciprocal retaliation logic), and
    casey-bondarenka.md / 2015-2016-annie-relationship-start.md (Nov 29
    2015 pivot quote).
  - **Two of these turned out to be misattributions, not just thin
    summaries — corrected, not just expanded:**
    1. tom.md's Oct 28 2025 "returned to music production after 7 years"
       detail was actually Dan describing himself, not Tom (confirmed
       against wiki/interests/music/overview.md's GRIPNOTIC timeline and
       against consistent lowercase-vs-punctuated texting-style patterns
       between the two speakers throughout the thread).
    2. vanessa-frank.md's Bernie 2020 NH-canvassing / Suz-pushback
       paragraph was actually Dan's own outbound (Sent) messages, not
       Vanessa's — flagged with a `REVISED` blockquote per house style.
  - **New export limitation documented (distinct from the known
    direction-field bug):** `Sent` rows in `MASTER_MESSAGES_DB_DUMP.csv`
    carry an empty `contact_handle` — the recipient of any Dan-authored
    message can only be inferred from timing/content, never read directly
    off the row, and a same-week counter-example (an unrelated NYC contact
    getting an identically-styled Sent message minutes after a Vanessa
    exchange) shows proximity-based recipient inference is not reliable
    either. Any future work reconstructing "who Dan was Sent-texting"
    should treat this as real uncertainty, not just note the existing
    Received-side direction bug.
  - Lint 0 errors throughout. Six focused commits, each pushed individually
    to `claude/wiki-people-rewrite-bik7ou`.
* **Handoff Note:** The full "expand every random-pull finding" punch list
  from the prior session is now done. Two paths open next, per the user's
  last explicit choice ("keep random pulling" over finishing stubs): (1)
  resume random 30-40-row CSV sampling for new findings, watching
  specifically for more Sent-row misattributions like the two caught this
  session — worth a second look at anything from the earlier random-pull
  batch that reads suspiciously fluent/lowercase and was attributed to a
  contact rather than Dan; or (2) if redirected, the ~17 unstarted stub
  pages are still listed in the 2026-07-14 entry below (nick-mattie, rj,
  rod-banks, sam, shannon, slim, steve-kezmarsky, tan-calabrese, teddy,
  trevor, urpaaa-at-yahoo-com, vaughn, vicki, zach-clabaugh,
  zach-hendricks/zaco [same person, merge don't duplicate], zach).

### [2026-07-13] - Session: dossier corpus propagated to all linked pages (PR #7)
* **Model:** Claude Fable 5 (Claude Code, remote)
* **Summary:**
  - Follow-up to the annie-ulmer.md rewrite (PR #6, merged). Fixed a
    gemini-code-assist review comment on #6: the March 2025 admission quote
    has inverted pronouns ("you lied to me... cheated on me" reads as an
    accusation of Dan) — kept verbatim, attributed the reading to the
    dossiers explicitly rather than asserting it silently.
  - Propagated the fully-read DanAnnie dossier corpus into every page that
    shares the material: eli-incident.md, eli.md (exact Jan 9 2025 text,
    arrangement-violation framing), attachment-model.md,
    conflict-architecture.md (final counts, confession-trap mechanism, full
    monthly volume table), attachment-trauma-bond.md (quantified trajectory
    section), dec-2025-spike.md + group-chat-closure.md (corrected Dec 2025
    volume: 4,657 = 2,391+2,266, was miscounted 2,248 in the old page),
    2015-2016-annie-relationship-start.md (dossier origin baseline),
    march-2026-terminal-phase.md (eulogy/gas-station re-entry, bathroom
    incident convergence detail), au-zaatar.md (involuntary job-loss per
    Amendment 2), suzanne-frank.md (social colonization), tuquick.md
    (Target G ambiguity sharpened), tom.md (arrangement context),
    2025-collapse.md (financial substrate summary).
  - queue.md: dossier-synthesis item marked DONE (remove on next cleanup).
  - PR #6 merged before this work started; opened fresh PR #7 (draft) per
    the merged-PR restart protocol. Lint 0 errors throughout.
* **Handoff Note:** The corpus is now propagated to every page identified
  as directly referencing the same dossiers. Not yet touched: forensic-method
  concept page and any people/ stub pages that only tangentially mention
  Annie — check those only if the user asks for a further pass. PR #7 is
  being watched; check its status before starting new Annie-adjacent work.

### [2026-07-13] - Session: annie-ulmer.md full-completeness rewrite (user directive)
* **Model:** Claude Fable 5 (Claude Code, remote)
* **Summary:**
  - User directive: rewrite annie-ulmer.md using ALL available data, as complete
    as possible. Discharged the HIGH queue item: read all six FINAL/amended
    DanAnnie dossiers end-to-end for the first time, plus CorrectiveAddendum,
    ulmer_dui_megadoc, DUI affidavit, and the Gemini-_07 Target G forensics.
  - Full rewrite of `wiki/people/annie-ulmer.md` (now 24KB, deliberately over
    budget as the critical hub): new Who She Was section (MFC history, family,
    genuine-early-love baseline, love-language trajectory 5.3%→0.1%→2.7%);
    the 2018–2024 arrangement (smashonista, jealousy kink, Tom incident
    revised coercion→exhaustion-within-consent per Part XIII); the corrected
    central thesis per CorrectiveAddendum (gaslighting of *accurate*
    perception = the central moral event; autumn-2024 "controlling" framing
    retracted, GPS dual-reading partial credit withdrawn with a REVISED flag);
    terminal-phase mechanism catalog (187:4, 44 moral-debt pivots, 13
    weaponized apologies, controlled void, social colonization); Target G
    section (Jan 4 2026 Suzy call, Whisk psyop, 10-day blackout, spoofed-number
    corrected assessment); full DUI legal record (docket MJ-14101-CR-0000631-2025,
    4 counts, MDJ Jason A. Cox); expanded timeline, metrics, and gaps.
  - queue.md updated (dossier item HIGH→MEDIUM, remaining = propagate corpus
    into attachment-trauma-bond / conflict-architecture / eli-incident).
  - Lint 0 errors. Branch `claude/annie-ulmer-profile-ja1fte` (separate PR).
* **Handoff Note:** The dossier corpus is now fully mined for the Annie page
  but NOT yet for the synthesis/concept pages — that propagation is the next
  natural chunk. If the page must be trimmed later, the arrangement and Target
  G sections are the best split candidates (own pages).

### [2026-07-13] - Session: Second-brain principle encoded (earned vs derived knowledge)
* **Model:** Claude Opus 4.8 (Claude Code, remote)
* **Summary:**
  - User's insight: the point of this system (vs. a RAG) is that synthesis is
    stored and compounds — the wiki reflects *what has been read and understood*,
    not an index of sources to re-read. The old charter line "wiki/ … all
    regenerable from raw/" contradicted this (pure cache/RAG framing).
  - **CLAUDE.md:** new section "Why this is a second brain, not a RAG" —
    distinguishes **derived** content (mechanical, regenerable) from **earned**
    content (reasoned once, not literally in raw/, NOT regenerable → revise,
    never re-derive). Fixed the wiki/ bullet. Strengthened QUERY: reason *from*
    the wiki first, only re-open raw/ when the wiki is silent or a source is
    newer.
  - **STYLE_GUIDE.md:** registered optional `knowledge: earned | derived | mixed`
    frontmatter field with usage rules (absent = mixed).
  - **bin/wiki-lint:** validates `knowledge` value when present (VALID_KNOWLEDGE);
    unknown values now error. Lint 0 errors / 17 warnings (all pre-existing size).
  - **Seeded the convention:** all 6 `mind/synthesis/` pages tagged
    `knowledge: earned`; `people/annie-ulmer.md` tagged `mixed` as the exemplar
    of the mixed case.
* **Handoff Note:** Convention is defined + demonstrated, not mass-applied. On
  any normal pass, tag the page you touch: `synthesis`/most `concept` pages are
  `earned`; people/event pages are `mixed`; pure count/catalog/timeline pages are
  `derived`. Do not bulk-migrate in one pass. The principle is now the top-level
  frame in CLAUDE.md — respect it: build on earned synthesis, don't bulldoze it.

### [2026-07-13] - Session: Great Restructure (mind/self/legal) + enrichment start
* **Model:** Claude Fable 5 (Claude Code, remote)
* **Summary:**
  - Re-architected mind/self/legal per user directive. NEW `wiki/mind/profile/` cluster (7 dense pages: hub/intp/enneagram-5w4/big-five-psychometrics/socionics-and-attitudinal/deviance-mapping/linguistic-profile) mined from FULL PROFILE 2026 + Dan Profile.txt.
  - Merges: 5 forensic pages → `mind/concepts/forensic-method`; 4 prompt-artifact pages → `mind/concepts/exocortex`; aesthetic-politics → political-psyops; work-power-dynamics → vertical-authority-skepticism (rewritten); family-heritage-and-roots → self/ancestry; financial-market-era → `timeline/periods/2020-2021-market-era`; millennial-digital-witness rewritten.
  - Legal: NEW `legal/2015-retail-theft-arrest` (Combos incident, ARD Feb 17 2016, Judge Wagner); 463-morgantown 3 pages → 1; BFS moved to `work/bfs-foods` (merged 4 pages); NEW `work/au-zaatar`. self/notes/ dissolved; jimmy-pop → `interests/rock-irrelevance-thesis`.
  - Enrichment: SLOPPP full discography (23 dated releases from FB export slugs; "Goodbye Demo" Dec 26 2015 = project end); MOGZART catalog + confirmed 2026 revival (Odd Mob DnB remix Mar 4 2026, status→active); self/overview rewritten biography-first.
  - bin/wiki-lint: added missing `profile` page_type. Lint 0 errors. All work on PR #2 (draft), branch `claude/wiki-article-restructure-agac7x`.
* **Handoff Note:** Continue the breadth pass (see Current Focus). GRIPNOTIC/mogged-up pages not yet enriched. self/index still auto-generated-style; chats/ pages still dirty.

### [2026-07-11] - Session: Annie Data Audit (source-completeness check)
* **Model:** Claude Fable 5 (Claude Code)
* **Summary:**
  - User flagged semi-correct info in annie.md. Root cause found: the page was synthesized from `DanAnnie_MasterRecord_March16.docx` while SIX newer dossiers in `raw/self/dox-scan/` (MasterRecord_FINAL, TenYears_WithAmendments, TheoryOfEverything_Updated, CompleteRecord_Final, CompleteAnalysis_Final, MoralAnalysis_SFW) were never read. "2"-prefixed variants are byte-identical dupes.
  - Fixed on annie.md: 94 burst events were misattributed to Annie (they are Dan's "crash-outs," each preceded by her silence); phantom source `raw/self/imessage/annie_full_archive.csv` replaced with the real dual-handle CSV (88,549 rows); record scope corrected (all-platform 126,683 msgs, Nov 28 2015 – Mar 16 2026); three ACCEPTED financial amendments folded in (oscillatory funding history); 187:4 ratio + 12 crisis statements + 36.5h silences + social colonization added; June 5 2026 post-closure apology recorded.
  - New page: `wiki/timeline/events/march-2026-terminal-phase.md` (laundry response, bathroom incident, confession + retraction).
  - queue.md: HIGH item — full synthesis of the 6 dossiers into attachment-trauma-bond / conflict-architecture / eli-incident; MEDIUM — locate 4 compiled source files absent from disk (Dan_Annie_Full_Text.txt etc.).
* **Handoff Note:** Lesson for all rewrites: check dox-scan for FINAL/amended versions before trusting any dated dossier. annie.md is 12KB (over budget, tolerated as critical hub — trim on next pass if it grows).

### [2026-07-11] - Session: Substance Standard + Exemplars (Fable quota burn)
* **Model:** Claude Fable 5 (Claude Code)
* **Summary:**
  - Added **Substance rules** to STYLE_GUIDE.md (first-paragraph test, consequence ordering, plain conclusions, gaps-as-content). These propagate automatically into every `bin/ingest-pack` prompt.
  - Rewrote three exemplars to the target bar: `annie.md` (metrics wall demoted, gaslighting-outweighed-affair thesis leads, LLM Quick Brief added), `suz.md` (verbatim Gemini transplants removed; her co-authorship of the 2004-05 rupture — previously buried in a timeline row — now leads; Suzy-call node, housing contingencies, dual-role structure), `eli-incident.md` (lead paragraph + status fix).
  - /fewer-permission-prompts: added ./bin/wiki-lint variant + ingest-pack/export-corpus to project allowlist.
* **Handoff Note:** Rewrites from here must meet the substance bar, not just the prose bar. Remaining: 7 Phase 3 synthesis pages, Phase 4 people (fran-whyel, rick-frank, tom, eli, anita...), contact-review.md decisions pending user.

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
