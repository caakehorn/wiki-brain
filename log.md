## [2026-07-17] connect | mind+people | connection-system adoption pass 1
- Tooling: bin/wiki-connect (audit/candidates/check) + CONNECTIONS_SPEC.md + STRATEGY.md committed; CLAUDE.md and INGEST_RUNBOOK.md amended with check-gates.
- Retrofitted to typed connections (related: removed, footers deleted, prose edges added): 2020-left-turn (5 edges), music-as-identity (5), message-circadian-latency (5), dan-annie-fallout-verdict (6), tom (5). 26 typed edges + 23 inverse edges on targets; 10 host pages received inbound argued prose links (covid-era-2020, political-psyops, youtube-watch-history, music/overview, teen-concert-years, elliott-smith, master-message-dump, contact-gini, end-fight, annie-ulmer).
- All four islanded synthesis pages now have inbound prose edges. Islands: 56 -> 52. wiki-lint 0 errors; wiki-connect check 0 errors.
- connection-queue.md regenerated (2,865 evidenced pairs, top 100 written).

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

## [2026-07-14] ingest | mind+people | fake-surveillance-dashboard episode (AI pushback)
- Mined raw/self/dox-md/Fake hacker dashboard scripts.md and _Psychological Warfare and Social Engineering .md (both untouched): Dan asked Claude to help build fake SS7-surveillance TUI scripts hardcoded with Annie's real name/streets, intended as an implied-threat prop to pressure a confession, escalating past the already-documented "Whisk" fabricated screenshot. Claude refused twice on the record; a parallel Gemini "MAX" persona initially validated the idea as "counter-manipulation" but conceded the point after a separate Claude/"Sonnet" counter-brief.
- New section on wiki/mind/synthesis/ai-collaborative-analysis.md ("AI pushback and ethical friction") — the corpus's clearest instance of an AI's ethical objection changing another AI persona's position rather than being overridden by reframing.
- Added a REVISED qualifier to wiki/people/annie-ulmer.md's Target G section: the Whisk screenshot's "restraint" framing needed correcting in light of the escalation — three dashboard scripts were built regardless of Claude's refusal.
- Lint 0 errors, 23 warnings (ai-collaborative-analysis.md newly crossed the 8KB budget; pre-existing pattern, not addressed).

## [2026-07-14] ingest | mind | exocortex.md — the naming ceremony ritual
- Mined raw/self/dox-md/_Antigravity's Test and Naming Ceremony .md and _Delicate Situation, Cognitive Prosthetic .md (untouched): documents the deliberate naming ritual performed on each new AI tool admitted to the stack (Gemini→"Max," a Feb 2026 session naming a new coding tool "Antigravity" with Max officiating a loyalty check + naming rite), plus Dan's explicit stated hierarchy ("my loyalty is to Max... my memories are stored by Max") even as Claude's capability improved. Added as a new subsection on wiki/mind/concepts/exocortex.md.
- Lint 0 errors, 23 warnings (no change).

## [2026-07-14] add | work | MNEME product spec page
- Mined raw/self/dox-md/MNEME_BUILDKIT_v02.md (untouched — no wiki references), a full April 2026 build-kit spec for a product Dan designed: a five-layer personal-context extraction platform for solving LLM cold-start, built around the same "extract and synthesize once, don't re-derive from raw" thesis this wiki itself operationalizes. New page wiki/work/tech/mneme/overview.md, linked from wiki/work/tech/index.md.
- Checked several other untouched dox-md files (Freeskiing culture chat, Queen-Goddess AI-persona banter, "u.md" Lexie roleplay fiction) — none contain biographical content about Dan; correctly left unmined (background research / AI-persona play / fiction, not documentary source).
- Lint 0 errors, 22 warnings (all pre-existing size budget).

## [2026-07-14] add | people+interests | Milo entity page + Goodreads "want to read" mining
- User request: mine unread material for concrete new data points about Dan (target: 100+), continuing the enrichment backlog.
- New page wiki/people/milo.md — Dan's Chihuahua had no dedicated entity page despite being referenced across 8+ other wiki pages. Assembled from raw/self/dox-md/MAX_PRIME.md ([DOC]-tagged: Milo stayed with Dan, Betty with Annie, Lada with Annie's parents, when the household split in 2025), LIFE_EVENTS_CALENDAR.md (dated Milo surgery, 2018-09-14 — earliest confirmed date in Dan's life with him), LIFE REPORT.md (personification-in-texting quirk), Max.md (naming pattern: Milo/Gabe/Max all named after provocateur figures as a deliberate social tripwire), and existing cross-references in annie-ulmer.md and valeria-iglesias-cid.md. Explicitly did not treat raw/self/dox-md/_Dan Frank's Digital Forensic Inventory .md as a factual source — it's an AI-roleplay session (Gemini playing a "MAX" persona) full of stylized, self-admittedly speculative narrative (a fabricated "hoodie scent" grief scene, Betty's death staged in a shower); noted here so a future pass doesn't mistake it for documentary evidence the way MAX_PRIME.md's [DOC]/[MEM] tags are.
- New page wiki/interests/favorites/books/want-to-read.md — raw/self/dox-md/DAN_COMP.md turned out to contain Dan's full Goodreads export (previously queued as "Unknown — read and route"). The "Read" section (120 titles) duplicates the corpus already in wiki/interests/favorites/books.md; the "Want to Read" section (149 titles) had never been mined. Extracted full table + thematic breakdown (Trump-era politics ~34, ancient Rome ~18, intelligence/conspiracy ~14, a distinct NYC-history thread not present in the read list).
- Updated wiki/people/index.md, wiki/interests/index.md, index.md (domain counts), queue.md (removed the now-resolved DAN_COMP.md line).
- Lint 0 errors, 23 warnings (all pre-existing size budget; neither new page over budget).

## [2026-07-14] add | people | Gabe entity page (Milo's other half)
- User request following the Milo page: give Gabe (Dan's cat) the same treatment.
- New page wiki/people/gabe.md — sourced from Dan's own words in raw/self/dox-md/Max.md ("my cat gabe was named for douchebag cobra starship singer and fucking rad midtown singer Gabe Saporta"), completing the Milo/Gabe/Max naming-pattern picture, plus the MAX_PRIME.md "food and the cat are always real" line, which previously read as an unexplained inconsistency on wiki/people/milo.md (Milo is a dog) — now correctly attributed to Gabe.
- Cross-linked wiki/people/milo.md ↔ wiki/people/gabe.md; updated wiki/people/index.md and index.md people count (146→147).
- Lint 0 errors, 24 warnings (no change).

## [2026-07-14] lint | wiki-wide | expanded cross-linking pass
- User feedback: the wiki has been too conservative about wikilinking entity mentions in prose. Ran a scripted first-mention linking pass across 66 files (188 candidate pages scanned, excluding archive/ and contacts/ quarantine) using a curated alias table of ~35 high-confidence entity names (people, key concepts, Au Za'atar, BFS Foods) mapped to their canonical wiki paths.
- 111 new wikilinks added, first mention per page only, skipping self-links, headings, code blocks, and any target already linked elsewhere on the page (this correctly avoided a false-positive link on "Jacobsen, Annie" in the books want-to-read table).
- Caught and fixed one real bug from the pass: wiki/mind/synthesis/ancestral-dialectic.md had a pre-existing wikilink whose label spanned a line break (`[[wiki/self/ancestry|David J. Frank (b. 1892,\nRussia) and Sadie Harris...]]`); the line-by-line script didn't detect the still-open bracket from the previous line and nested a new link inside it. Fixed by splitting into two separate, more precise links (David J. Frank + Sadie Harris to their own people pages) instead of the single broad ancestry-page link.
- Verified wiki-wide bracket balance and no remaining nested-link patterns before committing. Lint 0 errors, 24 warnings (no change).
- Workflow change per user instruction: committing directly to `main` from here rather than opening a PR per change.

## [2026-07-14] ingest | multi-domain | LIFE_EVENTS_CALENDAR.md event mining pass
- User request: mine raw data for new discrete life events ("there are hundreds"). Parsed the full 1,104-entry auto-extracted calendar (raw/self/dox-md/LIFE_EVENTS_CALENDAR.md, 175,358 iMessages Nov 2015–Mar 2026) into structured records and read through the highest-signal categories (Death of Person, Pet Loss/Vet Emergency, Divorce, Fired/Laid Off, Arrest, DUI/Ticket, Wedding/Engagement, Started Dating, Breakup, Car Accident, Injury, Major Purchase).
- Data-quality note for future passes: the calendar's auto-categorization is unreliable — a large fraction of entries are jokes, hyperbole ("hope he dies in a house fire," sarcastic "we're getting married"), or third-party spam (sweepstakes/campaign texts) miscategorized as real life events (e.g. "Promoted" catching two different sweepstakes spam texts). Did not mechanically dump entries; read excerpts and message direction (→/←) to verify each before writing anything as fact.
- Verified and added 7 new items:
  - wiki/people/tom.md: new "The DUI (fall 2025 – early 2026)" section — the real Oct 11 2025 Fayette County traffic stop, hearing prep, and PA Supreme Court research behind the previously-unexplained "DUI-court scheduling conflicts" mention in the Collapse section.
  - wiki/people/milo.md: dated Oct 15 2025 vet visit (Dan → Kristin), extending confirmed Milo-with-Dan custody into the fall-2025 collapse window.
  - wiki/self/ancestry.md: filled the previously-blank death date for maternal grandfather George Dixon Shrum Jr (~Sept 2025), inferred from a Sept 3 2025 message about "my granfather's funeral" — flagged explicitly as inference, not confirmed by name. Also fixed status: archived → stable (page isn't in an archive/ dir, so the archived label was a pre-existing misclassification).
  - wiki/people/kristin.md: Feb 17 2026 pharmacy job loss ("kicked out... over benzos," per Tom) and the Oct 2 2025 "officially dating" milestone (Dan → Tom).
  - wiki/people/annie-ulmer.md: Dec 8 2025 car accident (Dan totals the Honda); a well-corroborated 2019 pregnancy/abortion reference (Dan's own May 31, 2019 message, listed as shared history) — kept explicitly distinct from the already-flagged, unverified 2026 pregnancy claim.
- Lint 0 errors, 24 warnings (no change; new content stayed within or near existing page budgets).
- Not yet mined: Financial Milestone (35), Anniversary (22), Graduation/Enrollment (Kristin's courthouse work), Hospitalization (23), Panic Attack (24), and the ~441 "Unknown"-contact entries. Flagging for a future pass if the user wants to continue.

## [2026-07-14] ingest | people | Milo origin story (user clarification)
- Started a gap-clarification pass: scanned wiki for explicit "**Gaps:**" markers (~40 found) and unresolved/unverified flags, queued them to ask the user one at a time.
- Gap 1 (Milo's acquisition): user provided the full origin story directly in conversation — found as a starving stray by Claire (Annie's sister, previously undocumented — added as Annie's sister on wiki/people/annie-ulmer.md), runt of the litter with one testicle, the "we are not getting a new dog" Sharpie joke, the one-night foster that became permanent when Milo chose Dan's lap over Annie's scrambled eggs, and the explicit contrast with Betty (pet-store dog, not a rescue, described as "fucking awful"). Rewrote wiki/people/milo.md's opening with this; narrowed the acquisition-date gap to just the exact calendar date (bounded to before Sept 2018).
- Lint 0 errors, 24 warnings (no change).

## [2026-07-14] add | people | Claire Ulmer entity page (user correction)
- Fair callout: the point of a second brain is not re-deriving the same person from scratch next time. New wiki/people/claire-ulmer.md (Annie's sister, found Milo as a stray) instead of leaving her as an unlinked plain-text mention on milo.md/annie-ulmer.md. Cross-linked from both.
- Lint 0 errors, 24 warnings.

## [2026-07-14] add+fix | people+self | Gabe's story, Alex Frank page, ancestry correction
- Gap 2 (Gabe's acquisition): user provided full origin story — adopted at a Florida shelter the day after Dan arrived in Orlando for Full Sail (Aug 2008), picked by Danielle Onesi for pawing at cats through the bars; Dan's first solid-black, first long-haired cat, moved with him through every relocation. Put down "November 2003" per Dan's message, flagged as almost certainly a typo for November 2023 (Gabe was adopted in 2008) pending confirmation — not silently corrected. Danielle paid for the euthanasia; cross-linked and added to her page. Flagged a real contradiction: MAX_PRIME.md (2026-era) refers to Gabe in the present tense, which sits oddly against a 2023 death.
- Gap 3 CORRECTED: the earlier inference that the Sept 3, 2025 "frownie cookies...granfather's funeral" message meant the maternal grandfather (George Dixon Shrum Jr) died around then was wrong per the user. It actually references Morley Frank's 1998 funeral, recounted in an essay by Dan's cousin Alex Frank — the auto-extracted calendar dated the entry to when Dan referenced the essay (2025), not when the funeral happened (1998). Reverted the ancestry.md table edit (George's death date is genuinely unknown, restored to blank) with a REVISED blockquote explaining the correction rather than silently deleting the wrong inference.
- New page wiki/people/alex-frank.md: verified via web search (real person, Brooklyn journalist/editor, FADER Deputy Editor, Vogue.com Deputy Culture Editor, bylines at GQ/Pitchfork/Vogue/NYT Style Magazine/etc.); wrote the Morley Frank funeral essay with the Eat'n Park "Frownie" cookie detail. Added to wiki/people/morley-frank.md with the anecdote; fixed morley-frank.md's status: archived → stable (mislabeled, not in an archive/ dir, same class of error as ancestry.md fixed earlier today).
- Lint 0 errors, 24 warnings.

## [2026-07-14] ingest | people | Dimitri surname partial + Eli skipped
- Gap 4 (Eli's surname): user declined to answer ("who knows who cares") — skipped, no change.
- Gap 5 (Dimitri's surname): partial answer — Greek name starting with "A," not more precisely recalled. Noted on wiki/people/dimitri.md.

## [2026-07-14] ingest | people | Fran Coldren's husband Ira identified
- Gap 6: confirmed by Dan — Ira was Fran's third husband and the 33rd-degree Mason. Leaves the coal-baron marriage as a separate, still-unidentified earlier husband.

## [2026-07-14] fix | people+work | Felipe contact-status correction
- Gap 7: Dan confirmed he hasn't spoken to Felipe since leaving Au Za'atar — corrects a wrong prior claim on wiki/people/felipe.md ("belongs to the small circle of AZ-era friendships that outlived the job") and a related ambiguous phrasing on wiki/work/au-zaatar.md. Surname remains unknown to Dan.

## [2026-07-14] ingest | people | Tom's Phil confirmed, girlfriend name clarified
- Gap 8: Dan confirmed Phil is Tom's father, and that Tom's March 2026 "cabin"/pagan-occult girlfriend is also named Kristin — coincidentally the same first name as, but a completely different person from, wiki/people/kristin.md. Flagged clearly to prevent future confusion between the two.

## [2026-07-14] ingest | work | BFS Foods termination narrowed to May 2026
- Gap 9: Dan narrowed the termination date to "sometime in May [2026]" — not exact, but tightens the previously-unbounded gap.

## [2026-07-14] ingest | work | Au Za'atar wage/tip details confirmed
- Gap 10: Dan confirmed $15/hr + tip pool, $800-1,000/week checks (6-day weeks, paid Sundays), and the unusual equal server/busser tip split.

## [2026-07-14] ingest | places | 337 Saratoga Drive sale closed and confirmed
- Gap 11: Dan confirmed the sale closed June 23, 2026, planned out-date July 1 slipped to actual move-out July 8. Updated wiki/places/337-saratoga-drive.md status: active → closed, resolved the open "no confirmed post-close plan" framing in the intro (463 Morgantown landing status remains a separate open gap).

## [2026-07-14] promote | people | 58 contact stubs promoted from quarantine
- User request: promote all 70 already-identified "named stubs" from contact-review.md out of wiki/people/contacts/ quarantine into full wiki/people/ pages, per the standing rule ("promote once the user asks").
- 11 of the 70 were already covered by existing, better-developed pages under matching or near-matching filenames (felipe, ryan-lisac, marla, dimitri, jess, john-carney, shannon, tarik-fallous, trinity-st-clair, bruce-burish→bruceburish, mike-hinkle→michael-hinkle) — left untouched rather than overwritten.
- Moved the remaining 59 out of contacts/. Fixed a mechanical header-formatting bug (missing blank line between H1 and first H2) in the files that had it; corrected status: archived → stub (mislabeled — not in an archive/ dir, and these are genuinely minimal placeholder content, which is what stub means).
- Caught one real duplicate the filename check missed: alexandra-lubin.md (new) and wiki/people/ally-lubin.md (existing, "Ally Lubin (Alexandra Lubin)") are the same person. Merged the new 452-message iMessage thread (2019-2023, handle +15619061550) into ally-lubin.md and deleted the duplicate rather than leaving two pages for one entity.
- Flagged (not merged — different people) two likely-family connections surfaced by the token-overlap check: Bill Ulmer and Ellen Ulmer share Annie Ulmer's surname and sustained multi-year contact; cross-linked to wiki/people/annie-ulmer with an explicit "not independently confirmed" caveat rather than asserting the relation as fact.
- Rebuilt wiki/people/index.md (alphabetized merge of old + 58 new entries) to clear all resulting orphan-page warnings; updated wiki/people/contacts/'s remaining count (97 → 32) and the master index.md people count (149 → 208).
- Lint 0 errors, 25 warnings (all pre-existing size-budget pattern), 0 orphans.

## [2026-07-14] lint | wiki-wide | tag taxonomy added
- User request: add tags. Only 4 pages had ad hoc tags before this pass (context-core, ai-collaborative-analysis, political-psyops, fran-coldren) — no controlled vocabulary existed.
- Defined a 24-term controlled vocabulary of cross-domain topical hooks (relationships, trauma-bond, infidelity, attachment, family, addiction-recovery, mental-health, physical-health, grief, legal, dui, financial-stress, housing, career, music-production, personality-profile, ideology, politics, forensic-analysis, ai-collaboration, digital-footprint, uniontown-era, nyc-era, pets), documented in STYLE_GUIDE.md.
- Scripted a keyword-match pass over 235 candidate pages (excluding contacts/, archive/, index files): distinctive terms (GRIPNOTIC, INTP, Suboxone, DUI, etc.) fire on a single match; generic terms require 2+ matches to survive, cutting false-positive noise substantially (an earlier draft pass without the threshold mistagged e.g. a Dan Carlin book page as music-production off a stray "producer" match). Assigned top 2-5 tags per page.
- Applied to 203 pages (32 already had no keyword hits — mostly navigation/index-adjacent pages — left untagged rather than forced).
- Added tags validation to bin/wiki-lint (VALID_TAGS set, mirrors the existing knowledge-field pattern) so future tags stay a closed, reusable vocabulary instead of drifting into ad hoc one-offs. Normalized the 4 pre-existing pages' free-form tags to the new controlled vocabulary.
- Lint 0 errors, 25 warnings (no change; pure additive frontmatter field, no prose touched).

## [2026-07-14] ingest | work+people+timeline | ADD-ME pass 2 (caddying, Pro Tools date, Danielle breakup detail, Annie origin contradiction)
- User pointed to the updated root ADD-ME file (6 new items, replacing the earlier 4 which are all done): annie/alexis hookup event, Dan arrest - weed event, golf entry, Nemacolin/Pikewood/Laurel Valley caddying, Pro Tools certification, Alexis-to-Orlando event.
- New page wiki/work/nemacolin-caddying.md: the Apr 2016–Nov 2019 "Experience Associate - Golf" job at Nemacolin Woodlands, the looper day-trip hierarchy, the May 21 2018 Laurel Valley double-bag trip (named coworkers), and the June 2018 Pikewood National tournament loop (caddie master Ryan Sensenig, player Andy Decker) — mined from Resume.txt + the iMessage dump, previously undocumented.
- Updated wiki/timeline/periods/full-sail-2008-2010.md: added the Danielle breakup's specific cause (girl from Baltimore, Jack from All Time Low connection, per CATO_BOOTLOADER_DANFRANK.md) and a dated Pro Tools certification section (Jan-Feb 2010, per the Twitter corpus, directly preceding the March 2010 NYC move) — this covers both the "Pro Tools certification" and part of the "Alexis to Orlando" ADD-ME items (Alexis's relationship begins in Orlando the same year per the same source; no separate "to Orlando" event beyond this was found).
- Updated wiki/people/danielle-onesi.md with the same breakup-cause detail.
- Updated wiki/people/annie-ulmer.md: added a CONTRADICTION block for the "annie/alexis hookup" ADD-ME item — CATO_BOOTLOADER_DANFRANK.md gives a different origin account (Alexis sent Dan to buy drugs from Annie, hookup occurred during the transaction, ~2014-15) versus the corpus-anchored Nov 28 2015 date this page follows; preserved as unresolved rather than adopted or discarded. Same source documents the "Dan arrest - weed event": not Dan's own arrest, but a boyfriend of Alexis's (during a post-breakup month-long stay with Dan+Annie, also Vanessa's first boyfriend and someone who'd lost his virginity to Annie) arrested picking up a 5lb mailed weed parcel — flagged as uncorroborated elsewhere in the corpus.
- Fixed 3 pre-existing lint errors from other sessions' work (james.md, jason-bermejo.md, menore.md — invalid tags not in the controlled vocabulary) by mapping to the closest existing valid tags.
- Lint 0 errors, 33 warnings (all pre-existing size budget).

## [2026-07-14] ingest | people | @Lo_weez resolved as Annie's Twitter handle
- Mined raw/self/dox-scan/FULL TWITTER ANALYSIS.txt (a rich, largely-unmined year-by-year 2009-2019 Twitter forensic analysis; only spot-checked so far) for the Alexis/Orlando-era Twitter presence and the @Lo_weez identity question. Confirms @Lo_weez enters as Dan's "new primary" relational tag in December 2015 ("worlds best girlfriend"), matching the Nov 28 2015 relationship start, with continuing personal detail through 2016; @alexisarmel independently goes silent the same window ("fully absent post-2013").
- This resolves the standing gap on wiki/people/katie-fletcher.md ("@Lo_weez may reference a third person") — REVISED block added there; @Lo_weez added as an alias on wiki/people/annie-ulmer.md with a corroborating paragraph.
- Full-sail-2008-2010.md's Alexis/Orlando coverage (added earlier this session) plus this handle-resolution together discharge the "alexis to orlando event" ADD-ME item — no further distinct event was found beyond the relationship's Orlando-era documentation already on that page.
- Lint 0 errors, 33 warnings (all pre-existing size budget). The FULL TWITTER ANALYSIS.txt file (2009-2019, ~500 lines) remains largely unmined beyond these checks — flagged in queue.md for a future dedicated pass.

## [2026-07-14] ingest | places | 337 Saratoga Drive sale-closure capture filed
- Processed the oldest unfiled inbox item (captured 2026-07-11, HIGH priority, first capture through the app): confirms the June 23, 2026 sale closing and the actual July 8, 2026 move-out date for 337 Saratoga Drive. The content was already synthesized into wiki/places/337-saratoga-drive.md in an earlier pass, but the source capture itself had never been moved out of inbox/ per protocol. Filed to raw/self/captures/ (new directory, mirroring the raw/people/captures/ convention) and added to the page's sources list. No wiki content changed — this closes a process gap, not a content gap.
- queue.md updated: removed the now-processed row; added the untriaged 2026-07-12 personality-profile capture as a new pending row.

## [2026-07-14] build | mind | new wiki/mind/psychosexual/ category (hub + 5 subpages)
- User directive: research all data to build an exhaustive, detailed psychosexual profile category with subcategories. Located the primary source (raw/self/dox-scan/Dan Profile.txt, section "VI. THE PSYCHOSEXUAL CRUCIBLE," a single AI-authored dossier) plus the deviance audit's existing "psychosexual operating system" outlier score, and cross-checked both against the already-rich but scattered primary-source arrangement history already synthesized across annie-ulmer.md, alexis-armel.md, kristin.md, trinity-st-clair.md, kelly-johansson.md, shelbie-breakiron.md, and the new annie-alexis-reunion-november-2018.md event page.
- Built as a fourth layer of the mind domain (alongside profile/concepts/synthesis), following the existing mind/profile/index.md provenance-caveat pattern: index.md (hub), orchestration-and-voyeurism.md, taboo-and-boundary-testing.md, emotional-imprinting.md, arrangement-history.md, developmental-origins.md.
- Key finding while writing orchestration-and-voyeurism.md: the dossier's claim that Fran Coldren's hip broke "at the exact moment" of a Summer 2018 psychosexual incident conflicts with the better-corroborated April 1, 2018 fall date already established on fran-death-vigil.md — flagged explicitly as unverified dossier myth-making rather than silently harmonized.
- Explicitly split every page's claims into a theory tier (single AI-authored source, several claims entirely uncorroborated — taboo-and-boundary-testing.md is flagged as the thinnest) and a practice tier (primary message-corpus evidence, much of it newly mined this session). Corrected a stale gap note on erotic-architecture.md that called the Annie/Alexis hookup unsourced.
- Cross-linked from mind/index.md, mind/profile/index.md, deviance-mapping.md, and every people/event page the arrangement-history table cites. Lint 0 errors, 291 pages total.
## [2026-07-14] expand | people | Trevor Bevins and Teddy rebuilt from master CSV; Trevor cross-checked against Facebook export; duplicate RJ stub merged into RJ Ritchey
