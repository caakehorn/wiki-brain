# Ingest Queue

_Items waiting for or in the middle of ingestion. `bin/capture status` lists the inbox._

## Inbox — pending ingestion

| Item | Priority | Notes |
|------|----------|-------|
| 2026-07-11_140000_ANCESTRY_DNA.txt | MEDIUM | Ancestry narrative (Frank/Harris, Gillingham/Van Voorhis lines) — expand wiki/self/ancestry.md; not previously in raw/ |
| 2026-07-11_140001_google-takeout-manifest.html | LOW | Google Takeout archive manifest — file to raw/self/, useful as export inventory |
| 2026-07-12_152457_add-individual-entry-for-personality-pro.md | MEDIUM | Not yet triaged — check content, likely targets wiki/mind/profile/ |
| Jared/Tricia Google Voice export (pending, from Dan) | MEDIUM | Full export requested for the "picture" story context; jaredtricia.md written from a partial ChatGPT-pasted transcript in the meantime — revisit once the fuller export lands |
| Nabeel thread (2019-05-14/19, ~confirmed genuinely Annie) | MEDIUM | New page candidate — rich paid-client thread, only partially transcribed in raw/people/annie-ulmer/escort-messages-chatgpt-export-2025-08.md; needs the full message export before writing a page |
| Jason thread ((516) 589-0711, 2020-06-10/17) | MEDIUM | New page candidate — "Lily"/"Annie" dual-alias client, boyfriend-filming negotiation; same status as Nabeel above |

## Carried over from old repo (raw/ present, synthesis pending)

| File | Priority | Notes |
|------|----------|-------|
| raw/self/dox-md/tom_kristin_master_dossier.md | MEDIUM | Expand wiki/people/tom.md; add Kristin people page |
| raw/self/dox-md/MAX_PRIME.md | MEDIUM | Populate wiki/work/tech/max-framework/overview.md |
| raw/self/dox-md/ulmer_dui_megadoc.md | LOW | Annie DUI detail — check for gaps vs existing pages |
| raw/self/dox-md/The-Eli-incident-investigation.md | LOW | Check against wiki/timeline/events/ |
| raw/self/dox-md/Annie 10-Year… Forensic Report.md | LOW | Supplement wiki/mind/synthesis/attachment-trauma-bond if gaps |
| raw/self/message-csv/MASTER_DUMP_PART_1_ARCHAIC.csv | RESOLVED (2026-07-18) | Misnamed — 124k rows but only 1 in 2011, nothing 2012–14; earliest real text 2015-11-12. Has NO pre-2015 content. Corpus genuinely starts ~Nov 2015. Do not re-attempt for pre-2015; overlaps master dump for 2015–19. |
| raw/self/message-csv/ (remaining CSVs) | LOW | Thread-specific slices |

## Re-synthesis queue (lint 2026-07-11: 22 oversized pages)

All pages over the 8 KB budget, mostly mind/synthesis and self/chats — see lint-report.md.
Worst offenders: ai-collaborative-analysis (21 KB, still contains v1 agent chatter in
frontmatter), forensic-methodology (20 KB), context-core (14 KB), youtube-watch-history (14 KB).

## External acquisitions

- Twitter @danfrank: only sampled — full archive via X Settings → Download archive → drop in inbox/
- iMessage chat.db: bin/export-imessage-template.sh existed in old repo but never ran (needs Full Disk Access)

## Completed

- **2026-07-11 migration:** 562 MB raw/ archive (3,166 files), 261 wiki pages remapped
  into 9 domains, indexes rebuilt, lint clean (0 errors). Old repo at `~/wiki project`
  untouched, now safe to archive.

## DanAnnie dossier corpus (discovered 2026-07-11 — page audit)

| Item | Priority | Notes |
|------|----------|-------|
| Full synthesis of 6 unread DanAnnie dossiers (raw/self/dox-scan/: MasterRecord_FINAL, TenYears_WithAmendments, TheoryOfEverything_Updated, CompleteRecord_Final, CompleteAnalysis_Final, MoralAnalysis_SFW; "2"-prefixed files are byte-identical dupes) | DONE | 2026-07-13: read into annie-ulmer.md (full rewrite), then propagated into eli-incident, eli, attachment-model, conflict-architecture, attachment-trauma-bond, dec-2025-spike, group-chat-closure, 2015-2016-annie-relationship-start, march-2026-terminal-phase, au-zaatar, suzanne-frank, tuquick, tom, 2025-collapse. Remove this row on next queue cleanup pass. |
| Locate compiled full-record files: Dan_Annie_Full_Text.txt, 1_year_triad_logs.csv, 7_days_212_logs.csv, 14_day_212_logs.csv | MEDIUM | Cited by dossiers, absent from disk — likely on the machine where the dossiers were generated. Drop into inbox/ when found |

## Google Drive DOX corpus import (2026-07-13, in progress)
- [ ] User pointed at a Google Drive folder (RTF:TXT / MD / CSV subfolders) mirroring raw/self/dox-scan + dox-md + message-csv. RTF:TXT and CSV subfolders are ~fully duplicate of existing raw/ (confirmed by filename diff — no action needed). The MD subfolder (+ a "New Folder With Items" nested subfolder) contains ~48 files NOT already in raw/self/dox-md/ — genuinely new chat exports.
- [ ] Background agent dispatched to download all 48 new files verbatim into raw/self/dox-md/ (mechanical only, no synthesis). Check `git status --short raw/self/dox-md/` for what landed; check for `.gdrive-fetch-failures.txt` in repo root for any that failed.
- [ ] HIGH: Once downloaded, synthesize the **BFS Foods / Little Caesars drawer-dispute cluster** into wiki/work/bfs-foods.md — this is the highest-value new material. Files: "Drawer shortage dispute with assistant manager.md" + "(1)" variant, "Cash register shortage explanation.md", "Little Caesars retaliation timing concerns.md" + "(1)" variant, "Reverse chronological context upload.md". These contain a self-correcting multi-session forensic thread (named actors Anita/Brandon/Timmy/Marty; Hypothesis A "manufactured shortage for clean termination" vs Hypothesis B "real register error from Suboxone-withdrawal impairment, both stay live"; corrects an inflated "orchestrated campaign" framing back down to "chaotic franchise + off-books extraction"; PA §260.3 wage-deduction law cited). Check for contradictions against the existing bfs-foods.md page before merging.
- [ ] MED: "Jacob Bacharach.md" — check against existing wiki/people/jacob-bacharach.md for new facts.
- [ ] MED: "The 2nd most famous 'Jimmy Pop' in Pennsylvania.md" — likely the source for wiki/interests/rock-irrelevance-thesis.md; check if that page already cites it or needs enrichment.
- [ ] MED: "___ The J6 Chat.md" + "copy" — check against existing wiki/self/chats/j6-chat.md.
- [ ] LOW: "Attachment System Collapse.md", "Analyzing manipulation and ethical intent in data.md", "Interpersonal manipulation...toxic dynamic.md" (+ dup), "Honest assessment...", "Uncompromising analysis...", "Reassessing decade-long relationship dynamics...", "Ethics of leaving without communication.md" — more Annie-gaslighting-mechanism report iterations; spot-check for any NEW finding not already in annie-ulmer.md/attachment-model.md/conflict-architecture.md (most content looks like re-derivations of what's already synthesized — the "91 love-to-request" / "44 crisis pivots" counts are PRIOR/lower than the final dossier's 187:4 and 44 already on the page; treat final dossiers as authoritative per their own supersession claims).
- [ ] LOW: MAX/bunker-core chats ("_Psychological Warfare and Social Engineering.md", "_Openclaw Agent Setup and Data.md", "MNEME_BUILDKIT_v02.md", "Max.md", "stylometric_analysis.md", "agent.md", "_Antigravity's Test and Naming Ceremony.md", "Fake hacker dashboard scripts.md") — route to wiki/work/tech/max-framework or mind/concepts/exocortex.
- [ ] LOW: misc pinned chats / one-offs ("_Queen-Goddess's Digital Orbit.md", "_Freeskiing's Early 2000s Cultural Revolution.md", "_Delicate Situation, Cognitive Prosthetic.md", "_Photo Thread PT II.md", "_Two Options, Choose Wisely.md", "_Deconstructing a Chaotic 24 Hours.md", "_Dan Frank's Digital Forensic Inventory.md", "Creating robust video essays from scripts.md", "_The Waiter's Visible High.md" [likely dup of dansynth/TheWaitersVisibleHigh.md], "_Grok's Nudity-Fueled Carnage Exposé.md", "_Lexie's Unpleasant Basement Descent.md", "u.md", "Extracting Sent and Received.md", "_✧✧ DANFRANK-ISM'S ✧✧ Pinned chat.md") — read and route on next general enrichment pass; none flagged as high-priority on title alone.

## Google Drive DOX2 corpus import (2026-07-13, second folder, in progress)
- [ ] User shared a second, larger Drive folder (root id 1aoKUSaqRiUWbRl0n8B0dxzUBK_yEjHHa). Structurally different from the first: 10 top-level files + 12 subfolders. Confirmed the user wants EVERYTHING archived, including location history and Chrome browser history, not just narrative text.
- [ ] Background agent dispatched to mirror the Drive folder tree into `raw/self/google-drive-export/` verbatim (docs → .md via read_file_content; JSON/binary/images → base64 download + decode). Priority order given to the agent: (1) ~35 modest docs (NEW LOADER, FULL DATA STACK, LOGS, suz, Gemini Chats/heart.pdf, iMessage Analysis Toolkit, top-level files), (2) ChatGPT 4o History subfolder (real ChatGPT conversation exports, genuinely new corpus vs. the existing Gemini-only chat archive), (3) art-reference images, (4) location-history year-folders (Semantic Location History-1, Semantic Location History 2, Location History (Timeline)/Semantic Location History — monthly JSON files per year, 2016 onward), (5) Takeout/Chrome (Bookmarks + a ~71MB History.json, likely to be skipped as oversized) and Takeout/Search.
- [ ] Check `raw/self/google-drive-export/` tree once the agent completes; check for `.gdrive2-oversized-skipped.txt` and `.gdrive2-fetch-failures.txt` in repo root for anything that didn't land.
- [ ] HIGH: Once landed, prioritize synthesis/routing for: `NEW LOADER/OMNI_FORENSIC_DOSSIER.md` and `NEW LOADER/THEORY OF EVERYTHING 31 MAR` (a dated Annie dossier variant not yet cross-checked against the final MasterRecord/TenYears dossiers already synthesized into annie-ulmer.md — verify it doesn't contain any NEWER superseding facts); `FULL DATA STACK/Full Personality Profile` + `SEXUAL PROFILE` + `Pattern Mapping` (cross-check against wiki/mind/profile/ cluster for gaps); the ChatGPT 4o History JSON exports (a parallel AI-chat corpus to the existing Gemini activity — may contain material not covered by wiki/self/chats/).
- [ ] LOW/ARCHIVAL ONLY: location-history JSON and Chrome History.json — explicitly archived per user request but NOT expected to be synthesized into narrative wiki pages; if ever needed for a places/ or self/location-history.md enrichment pass, mine from here.

## Enrichment backlog (2026-07-13, from user directive — "thousands of trivial missing things")
- [ ] HIGH: chats/ pages cleanup — remove /tmp paths + HTML-comment agent chatter; rewrite to prose (gemini-02/-18/-21 worst)
- [ ] HIGH: people primary cast depth pass (rick-frank, tom, eli, anita, fran-coldren...) — mine LIFE_EVENTS_CALENDAR + message CSVs per person, per the annie.md standard
- [ ] MED: GRIPNOTIC/MOGZART full release catalogs (needs SoundCloud/Spotify export ingest — ask user for exports)
- [ ] MED: places/ expansion: 12 Bryer Ave, Uniontown, NYC chapters, Ohiopyle, Seven Springs, Au Za'atar location page
- [ ] MED: health/ expansion: withdrawal-episodes page, somatic record, sleep/vampire schedule
- [ ] MED: timeline events that deserve articles: 2015 Combos arrest done; candidates from calendar — Fran deathwatch (2018), freezer phone, J6 watching, Feb 2025 return drive
- [ ] LOW: work/tech: Bunker Core page, MAX interview system page (CATO §PROJECTS has specs)
- [ ] LOW: dedupe `related:` lists created by the 2026-07-13 link rewrite (some pages now link forensic-method twice)
- [x] MED: "Target G" — VERIFIED 2026-07-20: this item is stale. The Jan 2026 Suzy-call/blackout male is already fully documented in prose on wiki/people/annie-ulmer.md ("Target G (January 2026)" section, incl. the "Caitlin's husband" identity clue and the unresolved Tuquick-identity question) and wiki/people/suzanne-frank.md ("The 'Suzy' call" section). No further ingest needed.
- [ ] HIGH: DANSYNTH full-depth ingest — the scrape covers ~5%; mine raw/self/dansynth/DANSYNTH.txt session-by-session (maxwellhill, photo-archive, Chappelle/Ket, Valeria JSON audit) for the remaining facts; resolve flagged contradictions (Fran death date, Bacharach house, Morley Seattle thread). Franki/Katie order RESOLVED 2026-07-13 (summer 2013, per wiki/people/franki-faris.md).
- [ ] MED: mine raw/people/valeria/message_1.json directly (4,884 IG msgs 2022–2025) for dated milestones (departure date to Chile, gap analysis, 2024–25 frequency) and raw/self/dansynth/TheWaitersVisibleHigh.md remainder (Sergio mediation transcript → possible sergio entity page)
- [ ] MED: raw/self/dox-scan/FULL TWITTER ANALYSIS.txt (~500 lines, year-by-year 2009-2019+ forensic Twitter analysis) — only spot-checked so far (Alexis/Orlando era, @Lo_weez resolution 2026-07-14); a full pass would likely surface more dated social-graph and voice-evolution detail per year

## ChatGPT conversations.json export (2026-07-20, first pass)
- [x] Located and downloaded the operator-referenced ChatGPT export (`5e1e05d7-.json`, 375 conversations, 2022-12-10 to 2025-07-01) via direct upload after Drive's MCP tools proved too size-limited (download_file_content times out >5MB; read_file_content mangles JSON with markdown-escaping and truncates at ~900K chars). Full 375-conversation title/date/msg-count index built at scratchpad `conversations_index.tsv` (not committed — regenerate from the uploaded json if needed).
- [x] Sampled and mined ~10 of 375: "Mom Info Logged" (confirmed FULLY DUPLICATE of already-ingested facts — Danielle/Franki/Alexis/Annie dating chronology, Fran/Arnold Palmer/Ira Coldren biography — no new signal, strong confirmation of wiki completeness on this thread); "Relationship Breakdown Summary" (2025-04-27, genuinely new — mined into new page wiki/timeline/periods/feb-apr-2025-return-and-rupture.md, filling the Feb-Apr 2025 gap between the Jan 2025 affair discovery and the Aug-2025-onward terminal-phase record); "Whisk AI Prompt Injector" / "Whisk Emergency Fabric Design" (both low-value tangents, NOT related to any fabricated-evidence tool despite the title similarity — false lead, no wiki action); Franks Auto/Suboxone Buzz/Zalgo meltdown/Caregiver Pay (skimmed, appear to restate already-documented facts, not deep-read).
- [ ] HIGH: "Camming Career Review" (2025-06-07, 22 msgs) — extracted to scratchpad, not yet read/cross-checked against erotic-architecture.md / arrangement-history.md.
- [ ] HIGH: "Babbitt Shooting Psy-Op Debate" (2025-06-15, 22 msgs) + earlier "Ashli Babbitt Sheepdipped." (2023-03-16) + "Jan 6 Intelligence Evidence." (2023-04-03, 31 msgs) — extracted to scratchpad, not yet cross-checked against wiki/self/chats/j6-chat.md and wiki/mind/synthesis/political-psyops.md; this ChatGPT thread predates the existing Gemini-based J6 material by ~2 years and may be the original source.
- [ ] MED: the facial-feature/ideal-face cluster (April-June 2025: "Facial Proportions Analysis/Request", "Ideal Face Breakdown", "Face Preference Analysis", "Facial Feature Reconstruction Prompt", "3D Face Model Specs/Code", "Head and Body Sketch" — roughly 12 conversations) — a recurring project not yet understood or cross-checked; unclear if this is dating-preference modeling, an AI-avatar project, or something else. Worth one dedicated pass to understand what it is before deciding relevance.
- [ ] MED: "Interpersonal Analysis Request" (2025-04-26, 73 msgs) and "Conflict Analysis Framework" (2025-04-28, 8 msgs) — likely adjacent/overlapping with the already-mined "Relationship Breakdown Summary"; check for additional non-duplicate detail.
- [ ] MED: "Breakup Brain Dump" (2025-05-24, 26 msgs), "Personality Breakdown IRL" (2025-06-01, 32 msgs), "Emotional Blowout Breakdown" (2025-06-07, 13 msgs) — later 2025 relationship/identity content, unread.
- [ ] LOW: ~180 early conversations (Dec 2022 - Oct 2023) are overwhelmingly generic political/history/ideology discussion (Trotsky, Bolshevism, Capitol riot hearings, Opie & Anthony, Napoleon, French Revolution, MBTI/INTP typology, election-probability modeling) — same register as already-documented political-psyops.md and the profile/ cluster; spot-checked several titles against existing pages, no contradiction found, low expected marginal yield. Deprioritized for a full read; worth a title-level rescan only if a specific gap is later identified.
- [ ] LOW: "Franks Auto Supermarket History" (x2), "Uniontown..." cluster (x4), "NYC..." history cluster (x6, April 2024) — local-history trivia conversations, low biographical yield expected, not yet confirmed duplicate.
- [x] Raw archival: the full source export is now saved at `raw/self/chatgpt-export/dfrank-chatgpt-conversations-2022-2025.json` (375 conversations, valid JSON, 9.5MB) plus two extracted single-conversation text files for the conversations actually mined (relationship-breakdown-summary-2025-04-27.md, mom-info-logged-2025-05-23.md). To extract any other conversation by id or title, parse the full json (see `conversations_index.tsv` regeneration note above) — do not re-fetch from Drive, its MCP tools cannot handle this file size.
- [ ] NOT YET LOCATED: the larger ~35.7MB `dfrankconversations.json` companion export (same title seen repeatedly in Drive search results, likely a superset or different account/date-range) — the operator uploaded only the ~9.5MB `conversations.json`-class file; ask for the larger one directly if a fuller pass is wanted, since Drive's own MCP tools cannot fetch it (session-expired on every attempt, confirmed 4x on different file IDs of the same size class).
