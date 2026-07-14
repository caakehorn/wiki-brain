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

## [2026-07-13] ingest | people+work | AZ STORYTIME Part 1 + Kristin Chimera genesis addendum
- New raw: raw/self/dansynth/StorytimeAuZaatarAnalysis.md; raw/people/kristin/chimera-genesis-addendum.md.
- au-zaatar: founding section (interview charm, equal tip split, nightly shed build, opener slot / never closed once, owners' surveillance apartment, winter OUTDOOR-OUTDOOR service, caddie-style serving, Uniqlo Oxford). Annie correction refined: hostess at the ORIGINAL East Village AZ (Dan got her the job ~Apr 2021); fired zero-notice from there.
- Ismaila gap RESOLVED: Ismaila Barry = "DJ" — new people page; dimitri + felipe promoted from contacts/ with full identities.
- kristin.md: girlfriend-era genesis section (LONELY LOSER/ENIGMA nicknames, the rules, Danny as foundational myth, purity tests, trauma-bond 80% model, failure-state-is-success finding).

## [2026-07-13] rewrite | people | annie-ulmer.md full-completeness rewrite (user directive)
- Synthesized the complete DanAnnie dossier corpus for the first time: MasterRecord_FINAL (supersedes prior where conflicting), TenYears_WithAmendments (3 accepted amendments), TheoryOfEverything_Updated (terminal-phase mechanisms + bathroom incident), CompleteRecord_Final (Part XIII non-monogamy context), CompleteAnalysis_Final, MoralAnalysis_SFW, CorrectiveAddendum (gaslighting-of-accurate-perception as the central moral event; autumn-2024 "controlling" framing retracted), plus ulmer_dui_megadoc + affidavit and Gemini-_07 Target G forensics.
- New content on the page: Who She Was section (MFC history, family, early-love baseline + love-language trajectory table); the 2018–2024 arrangement (smashonista, jealousy kink, Tom incident REVISED coercion→exhaustion-within-consent); financial oscillation with all 3 amendments; Eli affair + Oct 19 2024 housewarming gaslighting quotes + Jan 9 2025 Eli text; terminal-phase mechanism catalog (anchor, semantic drift, crash-out trap, controlled void, 44 moral-debt pivots, 13 weaponized apologies, crisis non-response, social colonization); Target G section (Suzy call, Whisk psyop, 10-day blackout, spoofed-number corrected assessment); expanded legal record (docket MJ-14101-CR-0000631-2025, 4 counts, procedural dates, MDJ Cox); expanded timeline + gaps.
- REVISED flag added: GPS "dual reading" partial credit withdrawn per CorrectiveAddendum.
- Page is 24KB — over budget, tolerated deliberately per user directive ("use all available data, as complete as possible"); it is the wiki's critical hub page.
- Queue: HIGH dossier-synthesis item partially discharged (annie-ulmer done; attachment-trauma-bond / conflict-architecture / eli-incident enrichment from same corpus still pending).

## [2026-07-13] ingest | mind+people+timeline+work | dossier corpus propagated to linked pages
- Continuation of the annie-ulmer.md full rewrite: propagated the newly-read DanAnnie dossier corpus (MasterRecord_FINAL, TenYears_WithAmendments, TheoryOfEverything_Updated, CompleteRecord_Final, CorrectiveAddendum) into every page that references the same underlying material.
- Fixed gemini-code-assist review comment on PR #6: the March 2025 "you lied to me for months and cheated on me" quote has inverted pronouns; kept verbatim but attributed the reading explicitly to the dossiers rather than asserting it unflagged.
- Updated: eli-incident.md + eli.md (exact Jan 9 2025 11:18 PM text, arrangement-violation framing); attachment-model.md + conflict-architecture.md (final counts: 187:4, 13 weaponized apologies, 44 moral-debt pivots, verbal-abuse escalation trajectory, full monthly volume table, confession-trap mechanism); attachment-trauma-bond.md (quantified trajectory + financial-oscillation section, status stable); dec-2025-spike.md + group-chat-closure.md (corrected Dec 2025 volume 4,657 = 2,391+2,266, was miscounted 2,248; status stable); 2015-2016-annie-relationship-start.md (dossier origin baseline, status stable); march-2026-terminal-phase.md (eulogy/gas-station re-entry section, bathroom-incident Suboxone-crisis convergence); au-zaatar.md (involuntary job-loss mechanics per Amendment 2); suzanne-frank.md (social colonization section); tuquick-17248123683.md (Target G ambiguity sharpened — "Caitlin's husband" per Gemini-_07, not confirmed as Tuquick); tom.md (Tom-incident arrangement context); 2025-collapse.md (financial substrate summary).
- Lint 0 errors, 18 warnings (all pre-existing size). PR #7 (draft), branch claude/annie-ulmer-profile-ja1fte, opened fresh since PR #6 merged.

## [2026-07-13] ingest | people | tom.md — friendship collapse (Spring 2026)
- Mined imessage_ALL_both_all_now.csv (phloxenheim@gmail.com thread, Mar 24 - May 30 2026, the record's last dated Tom messages) for the arc of the friendship's collapse: mutual-support peak (Mar 31 suicidal-ideation talk-down), April supply delays compounding, May 15-16 no-show breaking point (Dan risks his job), May 18 block/unblock + $36 cash demand, May 29-30 renewed accusation + threat to route the dispute through Tom's father Phil (last message in the record).
- Reframed the page's lead characterization: "safe attachment, no forensic mode" now qualified — the same owe-and-silence pattern the page already documented is shown running to actual rupture rather than self-correcting. Status kept 'active' (unresolved, not closed) with a Gaps note that recovery past May 30 is undocumented.
- Lint 0 errors (19 warnings, all pre-existing size budget + tom.md joining at 11KB).

## [2026-07-13] add | people | franki-faris.md — new page, resolved Franki/Katie dating contradiction
- User asked why Franki Faris had no page and requested the full "2014 July 4" story. Investigated three conflicting date sources: Gemini-58.txt ("Summer 2013"), the DANSYNTH node ordering (Franki incident precedes Katie Fletcher's 2013 tenure), and CATO_BOOTLOADER_DANFRANK.md ("2014"). Primary dated evidence (July 9-31 2013 self-typology emails, Aug 14 2013 post-mortem email) confirms summer 2013; the CATO bootloader's "2014" is a later AI-reconstruction artifact and doesn't hold up. No source anywhere ties a specific "July 4" event to Franki — flagged as unsupported rather than fabricated.
- New page: the five-day 2013 rebound during a split from Alexis Armel, the Aug 14 2013 post-mortem, the transition to Katie Fletcher as interim, and later echoes where Dan explicitly used "Franki Faris 2.0" as his own shorthand for the Annie Ulmer relationship's origin (Dec 2015 messages) and later as a casual pet-nickname for Annie herself (2018).
- Updated wiki/people/katie-fletcher.md: replaced the standing CONTRADICTION/gap note with a REVISED block resolving the dating; added franki-faris to related. Added franki-faris to wiki/people/index.md. Marked the Franki/Katie order item resolved in queue.md.
- Lint 0 errors, 21 warnings (all pre-existing size budget).

## [2026-07-14] ingest+add | work+mind | Sergio-mediator correction, Dan Frank OS report mined
- Corrected wiki/work/au-zaatar.md: the Sergio-incident mediation was misattributed to Dimitri in the Gaps note; Dan's own follow-up in raw/self/dansynth/TheWaitersVisibleHigh.md names Ghassan (mostly) + Tarik (late) as the actual mediators, and clarifies the Tunisian manager was uninvolved and Sergio himself was short-tenured. REVISED block added.
- Mined raw/self/dansynth/DANSYNTH.txt lines 3440-3684 ("The Dan Frank OS: A Psychogenealogical Architecture of Collapse and Recursion" — a long-form Gemini deep-research report never previously synthesized into the wiki). New pages: wiki/mind/synthesis/ancestral-dialectic.md (Ashkenazi "syntax of suffering" vs. Appalachian "numbness of survival" as two inherited operating systems; the 95th-percentile Neanderthal-ancestry data point, new to the wiki; the four-phase collapse-cycle model matched against the Alexis and Annie eras; geography-as-gravity read alongside the existing relocation-as-reset speculation) and wiki/mind/concepts/erotic-architecture.md (sexuality as "recursive mythogenesis engine": externalized libido, taboo as ontological rupture, emotional consumption — including a previously undocumented fact, the "ANNIE_ALEXIS_HOOKUP_CORE," a facilitated Annie/Alexis encounter named only in this one retrospective source).
- Both new pages explicitly flagged (`knowledge: mixed`, Gaps sections) as synthesis of one AI-authored interpretive report, not verified biography. Linked from wiki/mind/index.md, wiki/mind/profile/index.md, wiki/people/annie-ulmer.md, wiki/people/alexis-armel.md (which also got a one-line note on the hookup fact).
- Lint 0 errors, 22 warnings (all pre-existing size budget).
