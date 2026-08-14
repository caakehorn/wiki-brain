---
domain: self
page_type: report
status: stable
date_created: 2026-06-22
date_modified: 2026-08-13
sources: ["raw/self/message-csv/imessage_export_deep_20260813.csv", "raw/self/message-csv/imessage_export_flat_20260813.csv", "raw/self/message-csv/README_20260813_exports.md", "raw/self/dox-scan/all_imessages_complete_dump.txt", "raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv", "raw/self/message-csv/annie_all_time_logs.csv", "raw/self/message-csv/MASTER_DUMP_PART_1_ARCHAIC.csv", "raw/self/message-csv/imessage_2124702449_both_all_now.csv", "raw/self/message-csv/imessage_3307038747.csv", "raw/self/message-csv/* (37 total CSVs)", "raw/self/dox-md/operating_manual.md", "raw/self/context-core/CONTEXT_CORE_EXPANDED.md", "raw/self/facebook/facebook-ihatedanfrank/messages/", "raw/self/dox-md/_ⒺⓍⓉⓇⒶⒸⓉ ⓂⒺⓈⓈⒶⒼⒺⓈ Pinned chat.md", "raw/self/dox-md/Gemini-_18.md"]
related: ["wiki/self/context-core", "wiki/self/twitter", "wiki/self/youtube-watch-history", "wiki/self/favorites", "wiki/mind/concepts/forensic-method", "wiki/mind/concepts/contact-gini", "wiki/mind/synthesis/attachment-trauma-bond", "wiki/self/facebook/messages", "wiki/timeline/events/timeline", "wiki/timeline/periods/2015-2016-annie-relationship-start", "wiki/people/annie-ulmer"]
tags: [digital-footprint, nyc-era, relationships, financial-stress, trauma-bond]
connections:
  - page: wiki/mind/concepts/calibrated-confidence
    type: instance-of
    claim: "The campaign's first finding, and the demonstration of what this corpus is actually for: behavioural signatures Dan never knew were being counted, not the self-report he was never going to type into a text message."
  - page: wiki/self/context-core
    type: contextualizes
    claim: "The corpus cannot corroborate the four core axioms — SMS is a near-zero-introspection medium for everyone in it, with 'the thing about me' appearing zero times in 217,573 messages in either direction — so the spine's claim that all behavioural data defers to this corpus has a jurisdiction, and the psychological layer sits outside it."
  - page: wiki/people/johnny-dealer
    type: evidenced-by
    claim: "The rank-7 handle in this dump, at 3,462 messages, resolves to a 2018-era dealer — which is the clearest demonstration that raw volume in this corpus measures logistical load rather than closeness."
  - page: wiki/timeline/periods/2021-2023-employment-block
    type: evidences
    claim: "The ~833-day export hole lands almost exactly on that period, which is what made three years of restaurant work look like a communication blackout; the location record's 806 place visits in 2022 against this corpus's four is the cleanest single falsifier of the silence reading anywhere in the wiki."
  - page: wiki/mind/synthesis/message-circadian-latency
    type: contains
    claim: "The circadian/latency page is a primary analytical cut of this corpus, and the worked demonstration of the ranking below: its circadian finding reproduced on three files while its headline latency finding was retracted in full on 2026-08-13, because it had treated a lossy extraction as a superset on the strength of clean attribution."
---


# Master Message Corpora (iMessage Dumps)

**Sources ingested from /Users/daniel/Documents/**DOX/DOC SCAN/CSV/**

## Read this before citing any number on this page

There is no single "the corpus." There are several partial extractions of one
device history, they disagree with each other by up to a factor of six on the same
calendar year, and at least one of them is in a different timezone from every other
source in the repository. Every count below inherits whichever file produced it.
This section is the ranking and the two structural holes; it sits first because
skipping it is how [[wiki/mind/synthesis/message-circadian-latency]] lost its
headline finding on 2026-08-13.

### Source ranking [DERIVED, 2026-08-13]

| Rank | File | Rows | Time | Covers | Use for |
|---|---|---:|---|---|---|
| 1 | `raw/self/dox-scan/all_imessages_complete_dump.txt` | 217,573 dated lines | **local** | 2011-03-18 → 2025-08-10 | anything 2019–2025; the completeness reference |
| 2 | `raw/self/message-csv/imessage_export_deep_20260813.csv` | 186,671 | **UTC** | 2011-03-19 → 2026-08-13 | 2026, and anything needing unmasked handles, chat IDs or GUIDs |
| 3 | `raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv`, `LEVIATHAN_FULL_CORPUS.csv`, `raw/self/dox-md/OMNI_FORENSIC_DOSSIER.md` | ~175–184k | local | 2011 → 2026 | attribution-clean sampling only — **never completeness** |
| — | `raw/self/message-csv/imessage_export_flat_20260813.csv` | 186,671 | UTC | same as rank 2 | **nothing.** No handle column; it cannot attribute any message to any person |

Rank 3 is one tier because the three files are three renderings of a single lossy
extraction rather than three sources: `OMNI_FORENSIC_DOSSIER.md`'s yearly totals
match the rank-2 export's row for row (13,819 / 20,221 / 17,551 / 40,514 / 20,153 /
6,311 / 280 / 954 / 4,376 / 41,278), so their agreement is not corroboration. The
concrete cost of the confusion: on thread `+12124702449` for calendar 2025,
Leviathan holds **Dan 2,114 / Annie 10,141** while the rank-1 dump holds **Dan
10,595 / Annie 10,174** for the same thread and year despite stopping on 2025-08-10.
Roughly four in five of Dan's outbound rows are absent from the file, which silently
inflates any measure of the form "time since Dan last spoke." Clean attribution was
mistaken for completeness. Provenance detail:
`raw/self/message-csv/README_20260813_exports.md`.

### The UTC convention [RAW-CSV]

**`imessage_export_deep_20260813.csv` timestamps are UTC. Every other message source
in this repository is America/New_York.** This was validated on 42,895 uniquely
text-matched pairs against `imessage_7244346811+7249204125+2124702449_both_all_now.csv`:
23,158 land at exactly +5.00 h (EST), 19,692 at +4.00 h (EDT), 45 outliers (0.1%).
Convert before comparing any figure from that file to a published one — an
unconverted timestamp shifts four or five hours, which is enough to move a message
across midnight and corrupt any per-day, per-hour or circadian count. In that file,
`HANDLE == 'Me'` marks outbound.

### The ~833-day hole, 2021-04 → 2023-08 [RAW-CSV]

Both independent extractions lose the same block of time in the middle of the
record, and it is an artifact rather than silence.

| File | Last row before | First row after | Span |
|---|---|---|---|
| `all_imessages_complete_dump.txt` (local) | 2021-04-27 20:31:40 | 2023-08-09 00:54:11 | **833.2 days, unbroken** |
| `imessage_export_deep_20260813.csv` (UTC→NY) | 2021-04-07 08:04:35 | 2023-08-11 15:06:11 | 856 days, one island |

The island is six messages on the evening of **2022-12-31**, 19:06–19:41 local, all
six outbound and two of them literally the word `test` — the signature of someone
checking that a handset sends, not of a year of correspondence. The two files also
disagree about the hole's edges in both directions, so neither is a subset of the
other and neither is authoritative about the boundary.

Three independent records inside the window contradict the silence reading. The
[[wiki/self/location-history|Google location export]] logs **806 place visits in
2022**, the year the message record scores at four to six, plus 257 in 2021 and 728
in 2023 (~1,791 across the three years). [[wiki/work/au-zaatar|Au Za'atar]]
employment ran continuously from March 2021 to August 2024 straight through the
hole, ~690 estimated shifts with 445 visits logged to the restaurant. And 2024 — a
year outside the hole entirely, which both files cover — is recorded as 4,376
messages in the rank-3 family against **28,463** in the rank-1 dump, showing the
same loss operating where no silence is even claimed.

The likeliest mechanism is a device or restore boundary: a handset used from spring
2021 to summer 2023 whose message store never merged into the current database,
with the present database assembled from a pre-2021 backup plus everything after
August 2023. That is a hypothesis about hardware, not a finding; what is established
is the negative — **the window is missing from the export, not from the life.**

### The bidirectional SMS void, 2020-05 → 2024-05 [RAW-CSV]

A second, larger and differently-shaped gap, and it is not the same artifact. SMS
traffic — only SMS; iMessage runs normally on both sides of it — stops for nearly
four years, and the boundaries replicate **to the second** across both extractions:

| Direction | Last before | First after | Span |
|---|---|---|---|
| Inbound SMS | 2020-05-28 11:13:26 | 2024-05-23 22:02:52 | 1,456.5 days |
| Outbound SMS | 2020-07-30 08:09:58 | 2024-05-24 18:18:31 | 1,394.4 days |
| Either | 2020-07-30 08:09:58 | 2024-05-23 22:02:52 | 1,393.6 days |

Identical timestamps in two separately-produced files means the void is in the
underlying store, not in either extraction pass. The shape is diagnostic: inbound
stops **63 days before** outbound. That is what a settings change looks like rather
than a service outage — green-bubble traffic stops arriving first, then stops being
sent. The reading consistent with the evidence is **SMS Text Message Forwarding
disabled** across that span, so SMS lived only on the handset and never reached the
store the exports were taken from. It follows that **every non-iMessage contact is
invisible for those four years**, which is a coverage limit on any 2020–2024
analysis of who Dan was talking to, and it is a different limit from the hole above:
the two overlap in 2021–2023 but neither explains the other.

**Consequences for existing pages.** Any claim of the form "the channel went quiet
in 2021–2022," "the corpus's hardest floor," or "near-total silence" is describing
an export and must be re-derived or withdrawn. The correction is worked through on
[[wiki/mind/synthesis/message-circadian-latency]],
[[wiki/timeline/periods/2021-2023-employment-block]],
[[wiki/people/rick-frank]], [[wiki/self/overview]] and
[[wiki/self/context-core]].

## Corpus Dimensions

| Dump | Rows | Approx. Messages | Date Range (sampled) | Notes |
|------|------|------------------|----------------------|-------|
| imessage_export_deep_20260813.csv | 186,671 | 186k | 2011-03-19 to 2026-08-13 | Whole-device, 15 cols, 499 handles, 598 chats, unmasked. **UTC.** `HANDLE=='Me'` is outbound. Lossy vs the dox-scan dump — 41.8% of that file's records are absent |
| imessage_export_flat_20260813.csv | 186,671 | 186k | same extract | 3 cols, attribution stripped. **Never usable for attribution**; retained only as the worked example behind a documented 2026-08-13 misattribution |
| MASTER_MESSAGES_DB_DUMP.csv | 184,359 | 175k+ | 2011-03-18 to 2026+ | Full master dump; columns: timestamp,contact_handle,direction,text,subject,service,date_read,error,is_read,is_delivered. Rank 3 — sampling only |
| MASTER_DUMP_PART_1_ARCHAIC.csv | 124,178 | 124k | 2011-03-18 to ~2015+ | Archaic/partial dump overlapping master |
| annie_all_time_logs.csv | 25,538 | 25k+ | 2015–2026 (2026 samples dominant in extract) | [[wiki/people/annie-ulmer|Annie]]-specific logs; timestamp,direction,text. Includes END FIGHT "Goodbye forever" 2026-06-01 |
| imessage_2124702449_both_all_now.csv | 23,720 | 23k+ | Recent full (Annie NYC handle) | datetime_local,direction,contact,service,kind,has_attachments,chat_name,text |
| imessage_3307038747*.csv (both_all_now + variants) | 16,563+ | 16,563 | 2025-09-01 to 2025-12-10 | [[wiki/people/kristin|Kristin]] (+13307038747; Tom's friend, potential romantic; intense flirty/sexual 2025 thread; "boner Ave", "I love you stupid", "kristin hole", "only cum to kristin rule") |
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
| 9 | +13476070497 | 1,753 | NYC delivery dealer ("Menore", 2018–2020) |
| 10 | phloxenheim@gmail.com | 1,603 | Email contact |
| 11 | +17249204125 | 4,812 | Frequent PA contact (heavy Johnny/Annie logistics facilitation 2018-19; "Hi b I gots a new phone") |
| 12 | +17248808111 | ~long multi-year | Extended family/gossip thread (mom, gram, dad, [[wiki/people/alexis-armel|Alexis]], Annie, voting, CMU play refs) |
| 13 | +13476070497 | 1,753 | NYC delivery dealer ("Menore", 2018–2020) |
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
- **Work (BFS recent):** Targeted extracts reference drawer-dispute patterns; the full record is at [[wiki/work/bfs-foods]].

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

[[wiki/people/aaron]] · [[wiki/people/brian]] · [[wiki/people/bruceburish]] · [[wiki/people/james]] · [[wiki/people/jess]] · [[wiki/people/josh-brannan]] · [[wiki/people/marla]] · [[wiki/people/michael-hinkle]] · [[wiki/people/ryan-lisac]] · [[wiki/people/shannon]] · [[wiki/people/trinity-st-clair]] · [[wiki/people/urpaaa-at-yahoo-com]] · [[wiki/people/zaco]]

The 97 auto-generated hash stubs (contacts ≥20 msgs, non-spam) are quarantined in [[wiki/people/contacts/]]. Two high-volume unidentified handles remain flagged for future ID: +17249204125 (~4.8k msgs, PA facilitation) and +17248808111.

## Next Steps in Ingest
Further dumps (imessage_*_both_*.csv variants) provide sent/received splits, last-6-months slices, group chat drama (annie_group_chat_drama.csv), THE END FIGHT. Full FB posts/groups cross for events.

Cross-references: [[wiki/self/context-core]], [[wiki/mind/concepts/forensic-method]], [[wiki/mind/concepts/contact-gini]], [[wiki/mind/synthesis/attachment-trauma-bond]], [[wiki/work/bfs-foods]] (work context in timeline), [[wiki/timeline/events/timeline]], prior dox-scan analyses, [[wiki/timeline/periods/2017-poverty-floor]], [[wiki/timeline/periods/2025-collapse]] etc..

**Sources:** raw/self/message-csv/* (37 files), raw/self/dox-md/operating_manual.md, raw/self/context-core/CONTEXT_CORE_EXPANDED.md, raw/self/facebook/facebook-ihatedanfrank/messages/ and groups/events htmls for cross.

A primary analytical cut of this corpus — circadian rhythm, reply latency, and per-contact volume trajectories — lives at [[wiki/mind/synthesis/message-circadian-latency]]. It sidestepped the master dump's `direction`-field bug via the Leviathan `sender` field, which worked; it then treated Leviathan as complete, which did not, and its reply-latency headline was retracted in full on 2026-08-13. Read that retraction alongside the ranking at the top of this page: the two documents are the same lesson from opposite ends.
