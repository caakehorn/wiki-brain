---
domain: self
page_type: report
status: archived
date_created: 2026-06-22
date_modified: 2026-06-23
sources: ["raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv", "raw/self/message-csv/annie_all_time_logs.csv", "raw/self/message-csv/MASTER_DUMP_PART_1_ARCHAIC.csv", "raw/self/message-csv/imessage_2124702449_both_all_now.csv", "raw/self/message-csv/imessage_3307038747.csv", "raw/self/message-csv/* (37 total CSVs)", "raw/self/dox-md/operating_manual.md", "raw/self/context-core/CONTEXT_CORE_EXPANDED.md", "raw/self/facebook/facebook-ihatedanfrank/messages/", "raw/self/dox-md/_ⒺⓍⓉⓇⒶⒸⓉ ⓂⒺⓈⓈⒶⒼⒺⓈ Pinned chat.md", "raw/self/dox-md/Gemini-_18.md"]
related: ["wiki/self/context-core", "wiki/self/twitter", "wiki/self/youtube-watch-history", "wiki/self/favorites", "wiki/mind/synthesis/forensic-methodology", "wiki/mind/concepts/contact-gini", "wiki/mind/synthesis/attachment-trauma-bond", "wiki/self/facebook/messages", "wiki/timeline/events/timeline", "wiki/timeline/periods/2015-2016-annie-relationship-start", "wiki/people/annie"]
---

# Master Message Corpora (iMessage Dumps)

**Sources ingested from /Users/daniel/Documents/**DOX/DOC SCAN/CSV/**

## Corpus Dimensions

| Dump | Rows | Approx. Messages | Date Range (sampled) | Notes |
|------|------|------------------|----------------------|-------|
| MASTER_MESSAGES_DB_DUMP.csv | 184,359 | 175k+ | 2011-03-18 to 2026+ | Full master dump; columns: timestamp,contact_handle,direction,text,subject,service,date_read,error,is_read,is_delivered |
| MASTER_DUMP_PART_1_ARCHAIC.csv | 124,178 | 124k | 2011-03-18 to ~2015+ | Archaic/partial dump overlapping master |
| annie_all_time_logs.csv | 25,538 | 25k+ | 2015–2026 (2026 samples dominant in extract) | Annie-specific logs; timestamp,direction,text. Includes END FIGHT "Goodbye forever" 2026-06-01 |
| imessage_2124702449_both_all_now.csv | 23,720 | 23k+ | Recent full (Annie NYC handle) | datetime_local,direction,contact,service,kind,has_attachments,chat_name,text |
| imessage_3307038747*.csv (both_all_now + variants) | 16,563+ | 16,563 | 2025-09-01 to 2025-12-10 | Kristin (+13307038747; Tom's friend, potential romantic; intense flirty/sexual 2025 thread; "boner Ave", "I love you stupid", "kristin hole", "only cum to kristin rule") |
| imessage_export_3307038747_20260624.csv | 21,727 | ~21k | 2025-09 to 2025-12-10 | Kristin terminal phase extension, documenting the $40 dispute, IP/Wi-Fi hacking threats, and her blockade citing IC3/Homeland Security |
| imessage_*_both_all_now.csv variants (multiple) | 10k+ combined | Various | 2025-2026 slices | Sent/received splits, group, last-6mo, ALL both |
| messages_3476070497_all_time.csv | 4,414 | 4k | 2018-11 samples | Specific contact/thread |
| dan_imessages_2015-2018.csv | 1,074 | 1k | 2015-12 to 2018 | Early period slice |
| THE END FIGHT.csv / END_FIGHT_full.csv + annie_group_* | ~1k+ | ~1k | 2026 group drama + closure | Group chat drama (may31-june1, relaxed), fight sequences |
| interspersed_messages.csv, targeted_extraction.csv etc. | Various | ~5k+ | Targeted | Targeted extractions, messenger exports |
| imessage_export_7248123683_20260624.csv | 2,993 | ~3k | 2026-05-31 to 2026-06-16 | June 15-16 End Fight extension, capturing Dan sending AI analysis and Tuquick defection |

**Total raw message events across dumps:** 300k+ entries (overlaps in master/partial/Annie). Sent iMessages 97,199 (2015–2025) per core; 37 CSVs total provide sent/received, thread-specific, group, and time-slice granularity. Master row count ~184k in primary dump.

## Key Structural Notes
- Direction: sent/received indicators.
- Handles: phone numbers and emails (e.g. +1724... for PA area).
- Service: iMessage/SMS indicators in some dumps.
- Subjects/threads for group chats.

## Contact Distribution (from MASTER_MESSAGES_DB_DUMP.csv analysis)
Top handles by volume (approximate counts; Annie dual handles dominant):

| Rank | Handle | Count | Notes / Tie |
|------|--------|-------|-------------|
| 1 | +17244346811 | 31,177 | Early Annie Ulmer (PA) primary; high relationship volume |
| 2 | +12124702449 | 17,145 | Later Annie (NYC/212) ; ongoing 10yr thread |
| 3 | +13307038747 | 16,563 | Kristin (Tom's friend, potential romantic interest; intense flirty/sexual 2025 thread) [CORRECTED from prior mislabel as Jerad?/Tom cross in thread CSV row] |
| 4 | +17249204125 | 4,812 | Frequent PA contact |
| 5 | +17249987341 | 4,160 | Tom (+17249987341 per operating_manual) — supply/anchor |
| 6 | annieulmr@aol.com | 3,645 | Annie email variant |
| 7 | +17243223678 | 3,462 | Johnny (dealer era per manual) |
| 8 | +17243228715 | 2,391 | Suz (mom) |
| 9 | +13476070497 | 1,753 | Additional family/friend |
| 10 | phloxenheim@gmail.com | 1,603 | Email contact |
| 11 | +17249204125 | 4,812 | Frequent PA contact (heavy Johnny/Annie logistics facilitation 2018-19; "Hi b I gots a new phone") |
| 12 | +17248808111 | ~long multi-year | Extended family/gossip thread (mom, gram, dad, [[wiki/people/alexis-armel|Alexis]], Annie, voting, CMU play refs) |
| 13 | +13476070497 | 1,753 | Additional family/friend |
| 14 | +17243223678 | 3,462 | Johnny (dealer) |

**Gini insight tie-in:** Extreme concentration in Annie handles (combined >48k in sampled) + few core nodes (Tom, Suz, early dealers) demonstrates high contact Gini; see [[wiki/mind/concepts/contact-gini]]. Updates prior tallies with full master extraction. 66 contacts total referenced in calendar events align with long-tail distribution.

## Voice Patterns (Stylometric from CSVs + operating_manual + core)
- Burst cadence confirmed across dumps: short phrasal messages, 3-7 discrete bursts per exchange; avg ~8.36 words/message.
- Lowercase dominant (80%+); ALL-CAPS for emphasis peaks (9k+ instances noted core).
- Ellipsis `...` as mid-thought breath; no terminal periods often; run-on with commas/ellipses.
- Lexical diversity high: 23k+ unique words.
- From operating_manual and slices: "literally", "like", profanity as intensifier, "lol"/"lmao", informal slang ("idk", "gonna", "ya"); code-switch to fuller sentences with family.
- Specific thread markers: rapid multi-message clusters in emotional (Annie fights, 2025 collapse); tender/affectionate in early/Feb 2025.
- FB cross: Similar informal voice in Facebook messages threads (Annie primary documented).

## Specific Thread Examples
- **Annie Dual-Thread (PA 1724 + NYC 2124):** 48k+ combined volume. End sequence in annie_all_time_logs: 2026-06-01 "Goodbye forever. This was not how it should have ended but. sic semper lupanis." + received apologies. Ties to group drama CSVs and THE END FIGHT.
- **Tom (+17249987341):** ~4k messages; anchor for drugs, excursions (Ohiopyle), wall-of-despair sharing (Aug 2025 per manual).
- **Early 2015-2018 slices (dan_imessages_2015-2018.csv):** Relationship genesis, poverty floor markers (debt, moved, panic).
- **Group chats:** annie_group_chat_drama.csv, may31-june1_2026, relaxed variants; interspersed with END FIGHT sequences.
- **Work (BFS recent):** Targeted extracts reference drawer dispute patterns, but primary in notes/bfs-bootloader.

## Ties to FB Annie Thread
FB export (raw/self/facebook/.../messages/) contains documented Annie thread alongside early NYC/golf/music acquaintances (pre- and parallel to iMessage). 403 threads total; Annie primary signal node. Cross-correlates with iMessage Annie handles for attachment sequences, 10-year span confirmation. See [[wiki/self/facebook/messages]] for FB-specific thread profiles, [[wiki/self/facebook]] for posts/groups/events cross. FB messages provide complementary 2007-2022 surface; iMessage fills 2015-2026 depth. Used in contact-gini and attachment synthesis.

## Relation to Context Core
Directly underpins §2 Voice: 97k sent iMessages, 8.36 words avg, 23,286 unique words, burst cadence, lowercase 80%+, ALL-CAPS for emphasis (9,282 instances), ellipsis as breath.
These dumps enable the stylometric analysis referenced in core sources (CATO_BOOTLOADER, stylometric_analysis).

## Forensic Value
- Enables attachment sequences, love-to-request counts (prior 145 mentioned), burst events (94 prior), contact Gini calculations. Dual Annie handles + Tom/Suz concentration support high-inequality social graph.
- Date granularity supports period pages (e.g. 2017 poverty floor, Dec 2025 spike, 2021-2023 employment block, 2015-2016 genesis, 2025 collapse). 2025-2026 slices (imessage_ALL_both_*, last6months) map directly to collapse/spike.
- Overlaps with location history, YouTube political consumption, Twitter output for full behavioral picture. FB Annie thread cross provides pre-2015 digital footprint + group interactions.
- From LIFE_EVENTS_CALENDAR (1,104 events): Relationship 266, Financial 105, Health 108 heavily represented in message volume spikes.

## FB Cross and Recent Work
Ties FB ihatedanfrank archive (groups/your_posts_in_groups, events/event_invitations, friends, messages inbox with Annie) into message corpora. Recent FB ingest (facebook-ihatedanfrank zip + html extracts) adds events/groups context for periods (e.g. early relationship markers, political, location). See [[wiki/self/facebook]], [[wiki/self/facebook/messages]], [[wiki/self/facebook/friends]], [[wiki/self/facebook/posts]].

## Named Contact Pages

Named contacts extracted from the master dump that have their own page but do not meet the full-person-page threshold. They exist as lightweight entity pages rather than in the hash-stub quarantine:

[[wiki/people/aaron]] · [[wiki/people/brian]] · [[wiki/people/bruceburish]] · [[wiki/people/james]] · [[wiki/people/jess]] · [[wiki/people/josh-brannan]] · [[wiki/people/marla]] · [[wiki/people/michael-hinkle]] · [[wiki/people/ryan-lisac]] · [[wiki/people/shannon]] · [[wiki/people/trin]] · [[wiki/people/urpaaa-at-yahoo-com]] · [[wiki/people/zaco]]

The 97 auto-generated hash stubs (contacts ≥20 msgs, non-spam) are quarantined in [[wiki/people/contacts/]]. Two high-volume unidentified handles remain flagged for future ID: +17249204125 (~4.8k msgs, PA facilitation) and +17248808111.

## Next Steps in Ingest
Further dumps (imessage_*_both_*.csv variants) provide sent/received splits, last-6-months slices, group chat drama (annie_group_chat_drama.csv), THE END FIGHT. Full FB posts/groups cross for events.

Cross-references: [[wiki/self/context-core]], [[wiki/mind/synthesis/forensic-methodology]], [[wiki/mind/concepts/contact-gini]], [[wiki/mind/synthesis/attachment-trauma-bond]], [[wiki/timeline/events/drawer-dispute]] (work context in timeline), [[wiki/timeline/events/timeline]], prior dox-scan analyses, [[wiki/timeline/periods/2017-poverty-floor]], [[wiki/timeline/periods/2025-collapse]] etc..

**Sources:** raw/self/message-csv/* (37 files), raw/self/dox-md/operating_manual.md, raw/self/context-core/CONTEXT_CORE_EXPANDED.md, raw/self/facebook/facebook-ihatedanfrank/messages/ and groups/events htmls for cross.
