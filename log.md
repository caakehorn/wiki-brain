# Operation Log

_Append-only. Format: `## [YYYY-MM-DD] <operation> | <domain> | <description>`_

---

## [2026-07-11] build | all | v2 repository created: structure, capture tool, export tool, CLAUDE.md
## [2026-07-11] build | all | single-file app (app.py): browse, search, capture, upload, inbox management, export UI at localhost:8477
## [2026-07-11] build | all | Personal Wiki.app bundle for Dock launching (Contents/MacOS/launch starts app.py once, opens/focuses browser)
## [2026-07-11] migrate | all | Full migration from ~/wiki project: 562MB raw/ (3,166 files), 261 wiki pages remapped self/legal/tech/music/favorites → 9-domain scheme (legal added), 11 pages link-fixed, indexes rebuilt, wiki-lint/search/status ported, 2 new inbox items, lint 0 errors / 22 size warnings queued
## [2026-07-11] build | all | app: @-mention page targeting in Capture (targets: frontmatter) + in-place page editor with edit logging
## [2026-07-11] edit | people | human edit via app: wiki/people/felix.md
## [2026-07-11] edit | people | human edit via app: wiki/people/mary-kate.md
## [2026-07-11] edit | people | human edit via app: wiki/people/mary-kate.md
## [2026-07-11] edit | people | human edit via app: wiki/people/mary-kate.md
## [2026-07-11] edit | people | human edit via app: wiki/people/mary-kate.md
## [2026-07-11] ingest | people | capture corrections: danielle.md → danielle-onesi.md (full name Danielle Onesi, "Dee"; merged contacts/danielle-onesi stub, 44-msg corpus)
## [2026-07-11] ingest | people | capture corrections: lex.md → alexis-armel.md (aliases Lex/Alexis/Alexi Armel; merged contacts/alexi-armel stub, 41-msg inbound-only corpus; first-mention Alexis links added in 12 pages)
## [2026-07-11] lint+build | all | coordination stabilization: STYLE_GUIDE.md written, 8 page_type errors fixed, corpus untracked from root, pipe-link rendering in app
## [2026-07-11] build | all | LLM-agnostic ingestion loop: INGEST_PROTOCOL.md + bin/ingest-pack + bin/ingest-apply (subscription-independence)
## [2026-07-11] lint | people | contact-review.md generated: 23 unnamed stubs listed for user triage, 5 pre-marked automated/spam
## [2026-07-11] style | all | substance standard: STYLE_GUIDE substance rules + 3 exemplar rewrites (annie, suz, eli-incident)
## [2026-07-11] audit | people | annie.md source audit: phantom annie_full_archive.csv replaced with real dual-handle CSV (88,549 rows); burst-event misattribution fixed (Dan's crash-outs, not Annie's); 3 accepted financial amendments + 187:4 ratio + crisis-statement record folded in from unread FINAL dossiers; march-2026-terminal-phase event page created; June 5 apology recorded
## [2026-07-12] build | all | GUI v2: collapsible sidebar, page rename with wiki-wide link rewrite, in-GUI ingest loop (pack/copy/apply), git sync pill + public-repo warning banner
## [2026-07-12] rename | people | wiki/people/annie.md -> wiki/people/annie-ulmer.md (45 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/aaron.md -> wiki/people/aaron-gaither.md (2 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/bruceburish.md -> wiki/people/bruce-burish.md (2 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/felix.md -> wiki/people/john-felix.md (5 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/johnny-dealer.md -> wiki/people/johnny-anderson.md (3 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/kristin.md -> wiki/people/kristin-prentiss.md (2 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/marc-charles.md -> wiki/people/marc-umbel.md (3 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/max-danielle-bf.md -> wiki/people/james-onesi.md (5 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/shannon.md -> wiki/people/shannon-muma.md (2 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/suz.md -> wiki/people/suzanne-frank.md (25 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/trin.md -> wiki/people/trinity-st-clair.md (2 pages relinked) via app
## [2026-07-12] edit | people | human edit via app: wiki/people/trinity-st-clair.md
## [2026-07-12] rename | people | wiki/people/annie.md -> wiki/people/annie-ulmer.md (45 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/suz.md -> wiki/people/suzanne-frank.md (25 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/trin.md -> wiki/people/trinity-st-clair.md (2 pages relinked) via app
## [2026-07-12] enrich | people | mined MASTER_MESSAGES_DB_DUMP.csv for top non-Annie contacts: kristin (+corpus texture, fixed librarian error via CONTRADICTION flag), tom (phloxenheim AI-collab thread + political banter), jerad-friedline (full rewrite: verbatim FSLY $200k tip, Tesla calls, Josh Brannan origin), vanessa-frank (full rewrite: political kinship, family back-channel); corrected +13476070497 roster mislabel (dealer, not family)
## [2026-07-12] rename | people | wiki/people/fran-whyel.md -> wiki/people/fran-coldren.md (14 pages relinked) via app
## [2026-07-12] rename | people | wiki/people/jackson-alexander.md -> wiki/people/alexander-jackson.md (12 pages relinked) via app

## [2026-07-13] restructure | mind+self+legal+work | major re-architecture
- legal: 463-morgantown 3 fragments → one page; BFS dispute moved out of legal into wiki/work/bfs-foods (merged 4 pages incl. drawer-dispute event + bfs-bootloader note); NEW wiki/legal/2015-retail-theft-arrest (mined from raw message dumps: Combos incident, ARD Feb 17 2016, Judge Wagner, expungement).
- work: NEW au-zaatar page (41-month NYC job promoted from a self/note).
- mind: NEW profile/ cluster (7 dense pages: hub, intp, enneagram-5w4, big-five-psychometrics, socionics-and-attitudinal, deviance-mapping, linguistic-profile) mined from FULL PROFILE 2026 + Dan Profile.txt; 5 forensic pages merged → concepts/forensic-method; 4 prompt-artifact pages merged → concepts/exocortex; aesthetic-politics folded into political-psyops; work-power-dynamics folded into vertical-authority-skepticism (rewritten); family-heritage-and-roots folded into self/ancestry; financial-market-era → timeline/periods/2020-2021-market-era; millennial-digital-witness rewritten to prose.
- self: notes/ dissolved (dispersed to work/, mind/, interests/rock-irrelevance-thesis).
- bin/wiki-lint: added missing 'profile' page_type (per STYLE_GUIDE).

## [2026-07-13] ingest | people | operator correction: Eli vs Tuquick
- Capture filed: raw/people/captures/2026-07-13-eli-vs-tuquick-correction.md
- Eli affair = NYC, sometime 2024 → Feb 2025 departure. Tuquick = the interloper Annie left Dan for + June 1 2026 group-chat counterpart. Tuquick ?= Target G (unknown).
- Updated: eli.md, tuquick-17248123683.md, annie-ulmer.md, group-chat-closure.md, eli-incident.md, attachment-model.md (REVISED flags where framing changed).

## [2026-07-13] ingest | self+people+places+timeline+work | DANSYNTH (part 1 of many)
- New raw: raw/self/dansynth/DANSYNTH.txt (278KB Gemini chat export, Feb 2026 sessions) + dansynth-scrape-phases-2-7.md (user's ~5% fact scrape).
- fran-coldren rewritten (golf record, 117 Belmont, Palmer, $100/yr gift protocol, caregiving years); NEW timeline/events/fran-death-vigil; NEW places/117-belmont-circle; 155-virginia updated (Belmont adjacency, Mar 29 2018 eviction notice); NEW people/katie-fletcher; valeria narrowed to 2021–22 + Feb 15 2026 JSON audit; suzanne + high-school nexus with Annie's father + keno morning; annie start date pinned Nov 28 2015; au-zaatar corrected (Midtown 58th & 1st, Mar 2021 start, Aug 2024 shed tear-down ending, full cast).
- CONTRADICTIONS flagged: Fran death Apr 1 vs Apr 4; Bacharach novel setting 337 Saratoga vs 155 Virginia; Franki-vs-Katie sequencing.
- Remaining: ~95% of DANSYNTH unmined — queued.

## [2026-07-13] ingest | work+people+mind | Au Za'atar chat trilogy + Valeria IG corpus
- New raw: raw/self/dansynth/{TheWaitersVisibleHigh,AuZaatarsFinalShift,FromSidewalkShedtoAnalyticalProwess,TheOnlyThingDanSlings}.md; raw/people/valeria/message_1.json (4,884 IG msgs, 2022-05-28 → 2025-07-11).
- valeria-iglesias-cid rewritten from primary corpus: hostess at Au Za'atar; winter 2021–22 affair; Concepción departure; 300-account brute-force search; contact alive to Jul 2025 (REVISED the earlier 2021–22-only window); Feb 15 2026 audit as closure.
- au-zaatar enriched (de facto manager era, "WAS HE HIGH?" review, Thanksgiving 2023 near-firing, Sergio mediation transcript, factions, red apron→white Uniqlo) + CORRECTED: Annie's zero-notice firing was at a DIFFERENT restaurant, not Au Za'atar.
- NEW wiki/mind/concepts/institutional-out.md — the always-installed absence mechanism (migraine protocol, night class), from Dan's verbatim self-statement.
