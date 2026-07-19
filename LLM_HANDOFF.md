# LLM Model Coordination & Handoff Log

**Purpose:** This file acts as a centralized brain and handoff document for different AI models working on the Wiki Rewrite Project. Because this project is being handled across multiple sessions and potentially different models, this file ensures continuity, tracks recent file changes, and dictates the immediate next steps.

**Standing ingest instruction:** If you were told to "ingest," "keep going on the wiki," "do the Phase B pass," or any open-ended synthesis task, **read `INGEST_RUNBOOK.md` (repo root) first and follow it exactly** — it is the complete reproduction-grade workflow and overrides ad-hoc improvisation.

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
**Raw-mining pass (2026-07-14):** Started the requested direct extraction
from `raw/`, beginning with high-volume people threads rather than cosmetic
rewrites. `wiki/people/trevor.md` is now Trevor Bevins's caddying-era and
later market-era profile, cross-checked against his Facebook export;
`wiki/people/teddy.md` is now an evidence-limited profile of the recurring
Uniontown pharmaceutical supply relationship; and `wiki/people/rj.md` was
identified as a duplicate of RJ Ritchey, merged into
`wiki/people/rj-ritchey.md`, then removed. Continue the same process for the
remaining high-volume template stubs, treating the master CSV direction field
as unreliable and using named Facebook or dedicated exports to resolve
identity when available.

**Maintenance repair (2026-07-14):** `bin/wiki-lint` is clean again (0 errors).
Two zero-byte, accidentally nested duplicate files under `wiki/wiki/` were
removed; their canonical pages were already present. Stale links on the Jason
Bermejo and Menore pages now point to current pages. `app.py` now handles a
timed-out or unavailable Git command without failing the Git-status endpoint;
the local tree, Git-status, and file endpoints were smoke-tested successfully.
The remaining 29 lint messages are page-size warnings, not broken links or
metadata errors; treat the intentionally oversized hub/archive pages according
to the existing page-budget policy rather than bulk-trimming them.

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
### [2026-07-19] - Session: app.py v3 — Wikipedia-style interface rebuild (operator directive)
* **Model:** Claude Fable 5 (Claude Code, remote), branch `claude/wikipedia-style-interface-09l3jd`
* **Summary:**
  - **Front-end of `app.py` rebuilt as a close Wikipedia (classic Vector skin) imitation** per operator request ("clone the wikipedia format as closely as we can"): left panel with wireframe-globe logo ("WikiBrain / The Dan Frank Encyclopedia") + Navigation/Domains/Tools/Project-files portals; Page·Discussion and Read·Edit·View history·More▾ tab rows; serif headings with rule underlines; numbered collapsible TOC; frontmatter `infobox:` rendered as a floating Wikipedia infobox (incl. `image:`/`image_caption:`); wikitables; red links for missing pages (click → create-page editor with frontmatter template); aliases hatnote; `sources:` rendered as a References section; `connections:` rendered as a typed-edge navbox; Categories bar from domain/page_type/status/importance; hash-based deep links with back/forward support.
  - **In-interface editing is the point:** Edit tab + per-section `[edit]` links open a Wikipedia-style edit page (toolbar: bold/italic/wikilink/H2/table/**image**, edit summary field logged to log.md, Show preview, Save). **Picture support:** the Image toolbar button uploads to `assets/uploads/` (new `/api/upload-image`, served back via new `/api/asset`) and inserts `![caption](assets/uploads/…)`; a standalone image line renders as a right-floated thumbnail with caption, inline images render in place.
  - **New server endpoints:** `/api/asset` (image serving), `/api/upload-image`, `/api/history` (git log --follow per page → View history tab), `/api/recent` (Special:RecentChanges); `/api/save` now supports `create:` (new pages under wiki/) + `summary:`; fixed the old bug where the UI offered editing of queue/task/contact-review/LLM_HANDOFF but the server rejected the save.
  - Capture (@-targets + drop-upload), Ingest (pack/apply), and Export survive as Special: pages; Move (rename with link rewriting), Sync, and the public-repo warning kept. Verified headless-Chromium screenshots of index + annie-ulmer (infobox, TOC, hatnote, blockquote reflow all correct); all endpoints curl-tested; wiki-lint 0 errors, wiki-connect check 0 errors.
* **Handoff Note:** No wiki content was touched. The renderer strips a leading body `# H1` into the display title — pages keep their current shape. `assets/uploads/` is committed (not gitignored) so embedded pictures travel with the repo. Possible next steps: infobox editing UI, image support in capture notes, diff view in View history.
### [2026-07-18] - Session: LAST FABLE DAY — junction trio complete, primary-count verification, long-tail triage, post-Fable governance
* **Model:** Claude Fable 5 (Claude Code, remote), branch `claude/wiki-analysis-redesign-cyjqsb`
* **Summary:**
  - **Junction backlog CLEAR — all 3 remaining junction pages written (earned):** `supply-network` (node succession Johnny→Tim→Tom + Menore; reliability inversion — distance disciplines, intimacy licenses failure; redundancy decay; terminal-phase inversion with Dan as Annie's supplier), `estate-money-spine` (two family source-lines, Adams trusteeship, the dated Aug 21/22 2020 order-then-guilt join, six-month lump-survival rule, ~$119–123K Annie drain ≈ the entire estate, Suz as switchboard), `block-unblock-loop` (the dependency rule: a block holds iff nothing still flows through the channel; 8-case table incl. Rick's held amputation and Menore's clean geographic closure; June 1 closure = live test). ~30 typed edges + inverses across ~25 member pages.
  - **Menore metrics (operator-requested):** availability 99.3% (455/458), median reply 6.6 min (the "60-second SLA" was Dan's own speed), ~280 confirmed deliveries, request→arrival median ~95 min, **1,458-day dark gap May 2020→May 2024 found** (CONTRADICTION flagged vs "sustained operations" + au-zaatar 2021–24 claim, now scoped to primary-confirmed May–Aug 2024), formal farewell ending 48h before the PA move.
  - **Primary-count verification of the fallout-verdict aggregates:** 74/17/11 abuse triple + 0-severance CONFIRMED EXACTLY → [RAW-CSV]; 1,512 love-affirmations confirmed to lexicon precision; **187:4 DEFLATED by base-rate control (97.2% of ALL her messages are request-adjacent at ±24h) and INVERTED by the directional test** — REVISED blocks on verdict/annie-ulmer + pointers; **180 "I'm sorry" / "apologizes least" NOT reproduced** (plain recount: 435 through Aug 2025) — REVISED on conflict-architecture; 127/110 + 94-burst order-consistent, still [DERIVED]; 299 unlocated; Eli text + 768 re-confirmed absent.
  - **Long-tail triage executed: islands 45 → 20.** steve-kezmarsky rewritten (deceased 2018 — real page); 8 minor supply nodes + 6 caddie-cohort pages + manuel/fastly wired via new host-page sections; 7 stubs demoted to contacts/ (incl. zach-hendricks+zaco merge); brandon.md deleted. **All remaining verdicts recorded in `LONG_TAIL_TRIAGE.md` (new, repo root) — settled, execute don't re-litigate.**
  - **Governance for the post-Fable era:** CLAUDE.md rule 4 + STYLE_GUIDE substance rule 4 now settle the page-budget question (advisory on hubs/junctions; LONGER entries standing); INGEST_RUNBOOK §11 codifies the storytime workflow; **STRATEGY.md gains "Running on lesser models"** (what to execute freely vs never attempt; the junction trio named as the model of the product).
* **Handoff Note (updated — post-merge follow-up on same branch):** PR #50 MERGED. A follow-up commit then landed on the restarted branch: **pre-2015 timeline reconstruction** — corrected 2010s.md (NYC-1 ended May 2013, not 2014; Alexis was Full-Sail-era, not "webcam-met") and added NEW `uniontown-return-2013-2015.md` for the genuinely-uncovered SLOPPP/MOGZART/Alexis-endgame stretch. **KEY FINDING: MASTER_DUMP_PART_1_ARCHAIC.csv is misnamed — it has NO pre-2015 content (corpus starts ~Nov 2015). Do NOT re-attempt pre-2015 from message data; it only exists in context-core/Facebook/dox.** Priorities for the next model, in order: (1) execute LONG_TAIL_TRIAGE.md MINE list (sam 374 / davey-fitzpatrick 382 / vaughn 228 / nick-mattie 170 + jason-bermejo opener); (2) storytime candidates per INGEST_RUNBOOK §11; (3) related:→connections retrofit + connection-queue top-down; (4) inbox items (3 pending since 07-11/12). llm/ regenerated — keep regenerating after every content pass.
### [2026-07-18] - Session (cont.): llm/ access point + Gemini-_00 finale + Photo Thread PT II (Fran vigil corrections)
* **Model:** Claude Fable 5 (Claude Code, remote), branch `claude/second-brain-overhaul-og2s2c`
* **Summary:**
  - **bin/llm-publish shipped (PR #46, merged):** public LLM access point at `https://caakehorn.github.io/wiki-brain/llm/index.txt` — any URL-fetching model can read every page (corpus.txt ~384k tokens, per-page .txt mirrors, manifest.json). Regenerate + commit llm/ after every content pass (rule now in CLAUDE.md). Also fixed invalid known_for YAML on 30 people pages.
  - **Gemini-_00 finale mined (21 points):** message_1.json parse REVISED the Valeria IG-thread shape (six-week 2022 burst, 3,830 msgs in June alone, 3-yr silence, 4-msg Jul 2025 coda; 2023–24 tail was iMessage) and measured 52% of Dan's outgoing IG msgs in the 22:00–01:00 ET post-exit window. "It never destabilized" attested claim added. wiki/self/chats/gemini-00.md DELETED — both Au Za'atar storytime chat pages now retired, content fully absorbed.
  - **Photo Thread PT II mined (23 points + operator correction):** fran-death-vigil.md restructured — TWO falls (filmed 8AM/keno spill ~late 2017; "Down Goes Frazier" = night of Mar 7–8 2018, dated by Vicki/Marla ambulance rows) and the death-date contradiction RESOLVED (Apr 1 admission / Apr 4 death). Vigil ran on a shift rotation (Vicki, Marla, Dan, Annie; Suz visited Apr 2) — Dan+Annie were alone only at the death moment itself, per operator. vicki.md rewritten from stub (un-islanded, one of the 17 unstarted done); contacts/marla.md dup deleted; fran-coldren gains 1959 LaGorce ace + Everglades tarpon + Fred-Adams-was-Ira's-law-partner confirmation (open item settled).
* **Handoff Note:** Storytime workflow continues to work. Next candidates: gemini-07 (Suzy call), gemini-13 (Bacharach), gemini-18, gemini-21, j6-chat, 9-11-chat, and the remaining dox-md storytimes (Cash register shortage, Drawer shortage, Little Caesars). Operator wants entries LONGER than current standard. Estate/money-spine junction now has its trustee node (Fred Adams / Ira estate). Islands: interest pages + vicki cleared; people/ long tail remains.

### [2026-07-18] - Session: connective-tissue adoption (PR #44 merged) + era-markers junction + Gemini-_02 storytime mining
* **Model:** Claude Fable 5 (Claude Code, remote), branch `claude/second-brain-overhaul-og2s2c`
* **Summary:**
  - Applied the operator's uploaded connective-tissue patch (4 commits: wiki-connect tooling, CONNECTIONS_SPEC, STRATEGY, passes 1–2) — merged to main as PR #44.
  - **Pass A (PR #45):** NEW junction `wiki/mind/synthesis/interests-as-era-markers.md` (fixed intake rate ⇒ subject-rotation is the era signal; marker series 2007→2024; film-canon control case; 2021–23 named as the missing-marker gap). Retrofitted all 5 islanded interest pages (roman-republic, opie-and-anthony, film-canon, golf, video-games) to typed edges; inbound prose on 6 hosts. **Islands 52→47.** Fixed bot-review findings (leftover footer, wikilinks).
  - **Gemini storytime mining (operator-directed, 50 points approved):** mined the Au Za'atar genesis convo start-to-finish, entered all points (main sink: full prose rewrite of 2021-2023-employment-block.md), then **deleted wiki/self/chats/gemini-02.md** with all inbound links repaired. Real research finds: Valeria's +56 iMessage channel (2023 NYC return, Nov 2024 re-contact told to Annie's handle — partially closes the "did Annie know" gap, contact through Jul 2025); Menore's legit-taxi cover; candidate DJ handle +19293235324.
  - Gates 0 errors throughout (wiki-lint + wiki-connect check).
* **Handoff Note:** The storytime-mining workflow is operator-approved and repeatable: scrape convo → ~50 data points → operator approval → research → enter → delete the chat page. **Next candidates: gemini-00 (Au Za'atar finale), gemini-07, gemini-18, gemini-21, j6-chat, 9-11-chat.** Also still open: 47 islanded pages (people/ long tail), connection-queue top-down, and 3 junction pages (supply network; estate/money spine — note the spec's "Rick/PNC trust" naming is unsupported in raw, the real thread is trustee Judge Fred Adams / Ira estate "capital veins" per _Photo Thread PT II_; block/unblock loop generalized).

### [2026-07-17] - Session: CONNECTION SYSTEM ADOPTION (pass 2) — synthesis layer complete
* **Model:** Claude Fable 5 (CATO)
* **Summary:** All 13 mind/synthesis pages now run on typed `connections:` (pass 1 did the four islanded ones; this pass did the remaining nine). ~45 new typed edges with claims, ~37 inverse edges on targets, all claims drawn from verified page-body content. Notable edges: intake-constancy `resolves` phenomenology-lens (output-combusts/intake-ticks correction now queryable); intake-constancy `causes` contact-gini (nocturnal signature as the structural substrate of isolation); psyops `instance-of` forensic-method; totality `contextualizes` 2025-collapse with a prose edge (this was the #1-scored pair in the mined queue). bond-switch edges preserve the 768-figure provenance gap in claim language.
* **Resume point:** remaining ~52 islanded people/ pages (inbound prose edges or logged demotion/merge decisions), then connection-queue.md top-down (regenerated), then the four junction pages (supply network, estate/money spine, block/unblock generalization, interests-as-era-markers) — verify against raw before writing. Gates: wiki-lint 0 errors, wiki-connect check 0 errors.


### [2026-07-17] - Session: CONNECTION SYSTEM ADOPTION (pass 1) + strategy legibility layer
* **Model:** Claude Fable 5 (CATO)
* **Summary:** Implemented the typed-connection system per operator directive. New binding docs: `CONNECTIONS_SPEC.md` (typed edges with claims, controlled vocabulary, retrofit protocol) and `STRATEGY.md` (plain-language top-down strategy for any incoming model, incl. the three unbreakable rules for limited models). New tool: `bin/wiki-connect` (audit / candidates / check — stdlib only). CLAUDE.md + INGEST_RUNBOOK.md amended: `bin/wiki-connect check` is now a commit gate next to wiki-lint; every ingest must write `connections:` blocks.
* **Retrofits (pass 1):** the four islanded synthesis pages (dan-annie-fallout-verdict, 2020-left-turn, music-as-identity, message-circadian-latency) + tom.md converted: `related:` deleted, `## Related` footers deleted, 26 typed edges with claims written, 23 inverse edges added on targets, 10 host pages given inbound argued prose links. All claims drawn from page-body-verified content; no new facts introduced. Islands 56 → 52; wiki-lint 0 errors; wiki-connect check 0 errors (151 warnings = the bare-footer retrofit backlog, expected).
* **Resume point:** Phase 2 of the connective-tissue directive (see CLAUDE_CODE_CONNECTIVE_TISSUE_PROMPT if supplied, else CONNECTIONS_SPEC retrofit protocol). Next targets in order: remaining ~48 islanded pages (people/ long tail — each needs inbound prose edges or an explicit demotion/merge decision), then the other 9 synthesis pages, then `connection-queue.md` top-down (regenerated 2026-07-17: 2,865 evidenced pairs). Junction-page candidates (supply network, estate/money spine, block/unblock generalization, interests-as-era-markers) remain unwritten — verify against raw before writing.


### [2026-07-16] - Session: missing-meaning expansion — 5 new interest/mind pages from raw/
* **Model:** Hermes (tencent/hy3)
* **Summary:** Per user directive ("open documents to a random place, read, analyze, connect, link, write" — 5–8 genuinely missing life elements, not FOB-adjacent tangents). Note: `/Volumes/MUSIC/PHASE B RAW` is currently throwing I/O errors and is unmountable — worked entirely from in-repo `raw/` (which is complete). Mined `raw/self/dox-scan/Dan Profile.txt`, `all_imessages_complete_dump.txt`, and `FAVS MASTERLIST.csv`. Wrote 5 new pages, each led with lived experience + dated raw evidence, gaps sections, cross-linked into indexes:
  - `wiki/interests/stand-up-comedy.md` — 2019 NYC live-club run (dated attendance list: Normand/Gillis/Soder/Dillon/Gaffigan etc.), own standup ambition (2017–2019 open-mic goal, "Nad Knarf" stage name), Philly 2018 special taping.
  - `wiki/interests/film-canon.md` — the thin 11-title movies list re-read as an evangelized canon + partner compatibility test; Kubrick completism; Eyes Wide Shut arc (completion target → voyeurism self-lens 2019 → "favorite Christmas movie" 2023); King of Comedy/Taxi Driver self-portrait pair.
  - `wiki/interests/roman-republic.md` — 2024 full-immersion ancient-history year (Carlin→Holland→Goldsworthy→Plutarch, dated reads), Caesar/Carlin evangelism to contacts, great-man-theory link.
  - `wiki/interests/opie-and-anthony.md` — the #1 most-watched thing in the entire YouTube history (2012–13 shock-radio archive binge, ~450 archive watches); the idiom + live-comedy-taste pipeline.
  - `wiki/mind/synthesis/2020-left-turn.md` — dated COVID-lockdown radicalization (self-narrated 2020-08-22: "i took a HARD turn left"), Bernie 2020 on-ramp (donor SMS flood), Chapo/Hasan/ContraPoints/Thoughtslime pipeline, Marx/Kropotkin reading, union-busting class-guilt.
* **Lint:** `bin/wiki-lint: 310 pages, 1 error` — the 1 error is the known pre-existing `wiki/wiki/people/steve-kezmarsky.md` nested-dup (NOT this session). `git diff --check` clean. Committed as c63e0cc on branch `feat/suzanne-frank-rewrite`. PR opened per user request.
* **Handoff Note:** MUSIC volume dead this session — if Phase B staging is needed later, remount/repair `/Volumes/MUSIC` first. Many more thin favorites pages remain ("appears on a top list" catalog lines) — same technique applies.

### [2026-07-15] - Session: ingest pass — tattoo artist (single inbox capture)
* **Model:** Hermes Agent (tencent/hy3:free, local)
* **Summary:**
  - Processed the one untracked inbox item `2026-07-15_195532_tattoo-artist.md`. Filed it to `raw/self/captures/`.
  - Fact: Dan's three Brooklyn tattoos (flapper girl, rose, gravestone) were done by **Ian Weidrick of Allied Tattoo, Brooklyn**.
  - Extended `wiki/self/tattoos.md`: updated table (artist + Brooklyn placement for all three traditional pieces), added a paragraph in "The traditional pieces" resolving the March 2019 artist/location and clarifying that "Chris at the Edge" (Annie's March 2019 msg) was a comparison shop, not the artist. Trimmed the gravestone gap accordingly. Frontmatter: date_modified → 2026-07-15, added the new raw source.
  - `bin/wiki-lint`: **0 errors** (pre-existing size warnings only). One commit on `feat/wiki-wikipedia-chrome`. No push/PR (not requested).
* **Handoff Note:** Traditional cluster now has a confirmed NYC-era artist/shop. Still-open tattoo gaps: exact dates for gravestone + flapper, body placement for every piece, total count. If a Weidrick/Allied session receipt or photo surfaces it could settle whether rose/flapper/gravestone were one session or several.

### [2026-07-15] - Session: CAPSTONE — Dan/Annie fallout verdict ("was he correct to feel wronged?")
* **Model:** Hermes Agent (tencent/hy3:free, local)
* **Summary:**
  - Operator asked for total synthesis + analysis of the Dan/Annie fallout and a direct verdict on whether he was correct to feel wronged. Read the full earned corpus: annie-ulmer.md, eli-incident, group-chat-closure, march-2026-terminal-phase, april-may-2026-final-weeks, attachment-model, conflict-architecture, 2025-collapse, tuquick, bond-switch-2015.
  - **NEW page:** `wiki/mind/synthesis/dan-annie-fallout-verdict.md` (earned, ~14KB). Lead verdict: **yes, correct to feel wronged — but the diagnosis→behavior gap is his.** Held both columns per operator's standing directive (sycophancy OFF, engage the gap, primary evidence = Dan's own data).
  - **The wrong (documented, her act):** (1) concealed Eli affair inside an *authorized* non-monogamy framework she went outside of; (2) gaslighting of accurate perception rated by corrective sources as the worst moral failure — the autumn-2024 "controlling" label was formally RETRACTED because his vigilance was accurate detection; (3) 187:4 love-to-request instrument he named in real time; (4) concurrent defamation campaign + 2 private denials.
  - **The gap (his architecture):** conflict engine with no domain selector / no halt condition; attachment model with 299 love affirmations / 0 severance signals (cannot self-close); 127 exits / 110 re-engagements (87% relapse) training her to ignore limits; he was the supply-chain architect; the arrangement was his design; Whisk→fake-surveillance escalation.
  - **Verified primary quotes against raw CSV:** "sic semper lupanis" (2026-06-01 00:27:49, Sent, her handle), "i am extremely sorry" (2026-06-05 00:37:42, Received), March 1 laundry response (2026-03-01 22:17:48, Received), Whisk "Nice. Real mature" (2026-01-05 23:02:51) — all reproduce exactly. Eli intro text is dossier-sourced (MasterRecord_FINAL), not in the on-disk CSVs scanned; flagged as such.
  - **Independent validation noted:** Tuquick defected June 15, called her "a compulsive liar with a drug addiction" — converged on Dan's decade-long read.
  - Wired into mind/index.md (synthesis list) + cross-linked from annie-ulmer.md and attachment-trauma-bond.md.
  - `bin/wiki-lint`: **0 errors** (37 pre-existing size warnings). One commit on `feat/wiki-wikipedia-chrome`.
* **Handoff Note:** This is the operator's explicit question answered in totality — treat as the capstone of the Annie synthesis cluster. **PROVENANCE PASS (2026-07-15, follow-up):** operator asked every conclusion cited to RAW TEXT. Rewrote the page with inline footnotes and a provenance legend ([RAW-CSV] / [RAW-DUMP] / [DOSSIER] / [DERIVED]). Verified verbatim rows this pass against `imessage_2124702449_both_all_now.csv`, `annie_all_time_logs.csv`, `THE END FIGHT.csv`, `imessage_export_7248123683_20260624.csv`, `all_imessages_complete_dump.txt`. **Two corrections forced by the raw:** (1) the dossier-cited "March 2025 admission" is actually `2025-02-23 14:28:42 | Sent` in the dump — misdated AND the raw direction tag contradicts the "Annie wrote it" reading (sender-attribution-unresolved, flagged). (2) The March 2026 "YES DAN" confession + "I misunderstood the conversation" retraction is NOT in any on-disk CSV/dump — dossier-only; the 42 "Yes Dan" rows in the dump are unrelated 2015–2024 confirmations. Items still [DOSSIER]/[DERIVED] (Eli intro text, "you're literally fucking insane", Jan 24 procurement line, Mar16 retraction, and the aggregate counts 187:4 / 299:0 / 127:110 / 1,512:232:180 / 94-burst) are explicitly flagged for a primary-row pass. Do NOT push/PR unless asked.

### [2026-07-15] - Session: CAPSTONE — Dan/Annie fallout verdict ("was he correct to feel wronged?")
* **Model:** Hermes Agent (tencent/hy3:free, local)
* **Summary:**
  - Operator redirected: instead of verifying already-synthesized stats, do **original primary analysis straight from the raw logs**. Chose the message corpus.
  - **Source:** `MASTER_MESSAGES_DB_DUMP.csv` (175,358 rows, 2011-03-18→2026-03-25) cross-checked against the sender-tagged superset `LEVIATHAN_FULL_CORPUS.csv` (`/Volumes/MUSIC/PHASE B RAW/`, 181,650 rows, 2011-03-18→2026-06-09). Used LEVIATHAN's unambiguous `sender` field (`Me (Dan)` vs handle) as ground truth to bypass the known `direction`-field bug.
  - **Data-hygiene catch:** phone numbers are masked; literal-comparison of the masked handle `+172****6811` against the file bytes FAILED (file uses ASCII `0x2a` asterisk; a typed `*` differs by codepoint). Fixed by substring-matching on the file's actual bytes. All counts recomputed from raw rows.
  - **NEW page:** `wiki/mind/synthesis/message-circadian-latency.md` — genuine primary findings:
    - **9× reply-latency asymmetry:** Dan answers everyone in 1–5 min (median); inbound replies scale from Annie 9 min → 2018-19 friends 19–22 min → 2025 contacts **16–44 hours**. The inbound delay — not outbound speed — is the axis of relational centrality.
    - **Merged Annie 2015–2018 volume arc:** 7,241/6,394 (15) → 10,821/11,194 (18 peak) → **2 msgs in 2019 = export-cliff artifact, not silence** (handle/export seam; true 2019–24 arc needs ANNIETEXTS/combined exports).
    - **Circadian curve:** peaks 17:00–23:00 (22:00 loudest, 7.5%); night share 15.6%; no weekday effect (flat 13.5–16%). **Era drift:** nocturnal share falls 15.5% (2015–18) → 10.4% (2025–26) — output migrates to daytime in the collapse window.
    - **Burstiness:** 62.7% of Dan's inter-send gaps <2 min; longest unbroken run = 284 consecutive sends; median inter-send 1.0 min. The fusion-mode output-storm fingerprint.
    - Re-confirmed Contact Gini from raw (top handle = 45% of 70,123 sent).
  - All numbers traced to the raw corpus; tables hold only numbers; plain-human prose per STYLE_GUIDE.
  - `bin/wiki-lint`: **0 errors** (37 pre-existing size-budget warnings). One focused commit on `feat/wiki-wikipedia-chrome`.
* **Handoff Note:** This is a fresh primary cut, not a verify pass. Natural next primary cuts from the same raw: (a) merge ANNIETEXTS.csv + combined_annie_logs to rebuild the true 2015–2026 Annie arc and recompute latency across the full decade (the 2019–24 gap is the one real hole); (b) per-contact latency for ALL 498 handles (only ~6 computed here) to build a full relational-centrality ranking; (c) the browser-history and Spotify/YouTube raw cuts the operator listed as alternates. Do NOT push/PR unless asked.

### [2026-07-15] - Session: bootloader relationship-chronology (cluster #1) — single-bond switch
* **Model:** Hermes Agent (tencent/hy3:free, local) — per INGEST_RUNBOOK.md cluster #1
* **Summary:**
  - Extended the already-filed `raw/self/dox-md/THE_DAN_FRANK_BOOTLOADER.md` into the wiki (source was filed by the 2026-07-15 bootloader session; this pass mines it, per the "4 filed sources NOT yet exhausted" handoff note).
  - **NEW page:** `wiki/mind/synthesis/bond-switch-2015.md` — the 2015 Alexis→Annie **single-bond switch** thesis: same-week transfer (Alexis cheating Nov 28 2015 → Annie met Nov 29), the sx/sp "one singular bond slot" mechanism, and the **155 Virginia Avenue lair-continuity** (the apartment leased during the Alexis years that Annie moved into — the transfer was a swap, not a relocation). Carries a [JOIN] finding: max-output-under-max-attachment-activation appears at BOTH ends of the Annie corpus.
  - **Verified numbers (Lesson 1 discipline):** recomputed the bootloader's Dec 2015 onset flood directly from `raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv` — **728 / 682 / 363 / 679 sent on Dec 10–13 2015** reproduces EXACTLY (the Dec 12 dip to 363 is real).
  - **Caught + flagged a provenance gap:** the bootloader's headline termination figure "**768 messages sent 2026-05-31**" is **NOT reproducible from any on-disk corpus** — `MASTER_MESSAGES_DB_DUMP.csv` ends 2026-03-25 (no May/June rows), and the dedicated closure export `imessage_ALL_both_2026-05-31_2026-06-02.csv` shows only **265 Sent / 482 total** that day. Flagged the 768 figure as unverified; the on-disk source export for it is not present and must be located before it's cited as corpus-verified.
  - **Extended (no bulldozing):** `wiki/mind/synthesis/attachment-trauma-bond.md` (new "single-bond switch" subsection — Alexis as control case, lair-continuity origin of the trauma bond), `wiki/people/annie-ulmer.md` (arc intro + verified onset flood + cross-links), `wiki/people/alexis-armel.md` (control-case framing + 155 Virginia lair anchor), `wiki/mind/index.md` (wired the new synthesis page).
  - All touched pages: frontmatter `status→active`, `date_modified→2026-07-15`, new `raw/self/dox-md/THE_DAN_FRANK_BOOTLOADER.md` source added, new `related:` links (bond-switch-2015, 155-virginia-ave, alexis-armel).
  - `bin/wiki-lint`: **0 errors** (37 pre-existing size-budget warnings). One focused commit on `feat/wiki-wikipedia-chrome`.
* **Handoff Note:** Cluster #1 done. Still open from the runbook's §8: (2) browser-history relational-name traces (`browser_history_analysis.txt` §8 — Tom most-searched/safe, Annie search-invisible, Alexis/Kristin post-hoc forensic) only partially ported; (3) message-corpora people-thread pull (ANNIETEXTS.csv 9.9MB, *FULL CORPUS* CSVs — ~17 unstarted stub pages: nick-mattie, rod-banks, sam, shannon, slim, steve-kezmarsky, tan-calabrese, urpaaa, vaughn, vicki, zach-clabaugh, zach-hendricks/zaco [merge], zach); (4) remaining unfiled Phase B RAW sources. The bootloader's nine corpus findings are only partially ported — Finding 3 (onset/termination flood bracket) is now substantiated, but Findings 1–2, 4–9 should be checked against existing pages before assuming coverage. Do NOT push/PR unless the operator asks.

### [2026-07-14] - Session: ADD-ME swarm synthesis + new mind/psychosexual/ category
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Summary:**
  - Synthesized six findings surfaced by a separate agent's ADD-ME scan
    (annie/alexis hookup, caddying job detail, golf, Pro Tools cert,
    Alexis-to-Orlando, the Zac Shumar weed arrest — the last already
    covered from the prior session) into the wiki, verifying every claim
    directly against raw sources rather than trusting the swarm's
    paraphrase. New page: wiki/timeline/events/annie-alexis-reunion-november-2018.md
    (a full six-week arc, Oct-Dec 2018, including a $3,000 cash-offer
    origin disclosed to Emaly Minerd — corrects shelbie-annie-threesome-april-2019.md's
    "earliest instance" claim via REVISED blockquote). New page:
    wiki/interests/golf.md (three-generation family lineage through Fran
    Coldren, Dan's own playing history, golf as a decade-long relationship
    touchstone with Annie start to end). Expanded wiki/work/nemacolin-caddying.md
    (corrected a May 21 vs May 23 date/detail conflation) and
    wiki/timeline/periods/full-sail-2008-2010.md (Pro Tools tweets,
    Alexis's physical Orlando presence).
  - Processed the oldest neglected inbox item (337 Saratoga Drive
    sale-closure capture) — a pure process-gap fix, content was already
    synthesized.
  - **New category: wiki/mind/psychosexual/** — hub (index.md) + 5
    subpages (orchestration-and-voyeurism, taboo-and-boundary-testing,
    emotional-imprinting, arrangement-history, developmental-origins),
    per explicit user directive to build an exhaustive psychosexual
    profile from all available data. Built from raw/self/dox-scan/Dan
    Profile.txt's "Psychosexual Crucible" section plus the pre-existing
    deviance-mapping.md outlier score, cross-checked against the
    already-rich arrangement history scattered across annie-ulmer.md,
    alexis-armel.md, kristin.md, trinity-st-clair.md, kelly-johansson.md,
    and shelbie-breakiron.md. Every page explicitly splits **theory**
    (single AI-authored dossier, several claims entirely uncorroborated)
    from **practice** (primary message-corpus evidence) — this
    provenance discipline is the main thing to preserve if this cluster
    gets extended further. Caught and flagged one internal contradiction
    (a dossier "cosmic irony" timing claim about Fran Coldren's fall that
    conflicts with the better-sourced date on fran-death-vigil.md) rather
    than silently harmonizing it.
  - Six-plus focused commits, each pushed individually. Lint 0 errors
    throughout, 291 pages total at session's current point.
* **Handoff Note:** The psychosexual cluster's `taboo-and-boundary-testing.md`
  is explicitly flagged as the thinnest page in the wiki — a single
  unelaborated sentence with zero primary corroboration. If richer source
  material ever surfaces (a primary account, not another AI dossier), that
  page should be rewritten from it rather than extended. The second Google
  Drive folder mentioned in queue.md (which reportedly contains a
  dedicated "SEXUAL PROFILE" file) never landed in raw/ — worth checking
  again before assuming this cluster is as complete as it can get.
### [2026-07-14] - Session: direct raw extraction, people-thread pass
* **Summary:** Replaced three template-level people records with roughly 16 KB
  of source-grounded prose. Trevor's 1,095-message master thread and named
  Facebook export establish his identity as Trevor Bevins, the 2018 Nemacolin
  caddying friendship, his exit to Sand Valley, later financial strain, and
  2021 meme-stock contact. Teddy's 1,077-message thread establishes a
  recurring 2018–20 Uniontown informal pharmaceutical-supply relationship
  while retaining limits around product identification, speaker attribution,
  and uncorroborated claims. The 518-message `+17249844280` thread resolved
  the duplicate `rj.md` as RJ Ritchey; its canonical page now covers the
  February 2019 boundary, July Manhattan visit, golf/work context, and later
  political/media conversation.
* **Verification:** `bin/wiki-lint` remains at 0 errors (29 pre-existing
  page-budget warnings); `git diff --check` passes.

### [2026-07-15] - Session: Phase B cross-corpus synthesis pass (bootloader + browser-history joins)
* **Model:** Hermes Agent (tencent/hy3:free, local) — autonomous extended pass per user directive
* **Summary:**
  - Ingested 4 Phase B RAW sources into raw/ (filed, not duplicated):
    `raw/self/concepts/TOTALITY_SYNTHESIS_2026-06-10.md`,
    `raw/self/dox-md/THE_DAN_FRANK_BOOTLOADER.md`,
    `raw/self/dox-md/THE_DAN_FRANK_MANUAL.md`,
    `raw/self/dox-md/DAN_COGNITIVE_PROFILE.txt`.
  - **User correction caught + verified (key event):** the "~7 YouTube watches/day"
    figure from the Totality doc was a miscomputation. Computed the real rate
    directly from the raw `YOUTUBE WATCH HISTORY (2010-2025).html` export:
    **17,426 timestamped events / 1,505 active days = 11.58/day** (2007-2025).
    Corrected intake-constancy.md + totality-themes.md; added provenance blockquote.
    The browser-history corpus later *independently* corroborated the fixed-rate
    thesis on the search side (20.2 actions/active day over 5,391 days).
  - **Synthesis writes (~5,000 words, all extensions, no bulldozing):**
    - `wiki/mind/synthesis/totality-themes.md` — +430 lines of cross-corpus
      [JOIN] findings: two-constants intake metabolism, migration grammar
      (Rick-file amputation rhyme, identity reorganization has syntax), relational
      channel map (intensity = closure not volume), housing clock (3-yr
      diagnosis→behavior gap), LLM-venue-vs-conflict-architecture join, output-
      port bandwidth war, precarity ledger, lens stress-test, and the 4:1
      distribution-to-tooling ratio independently confirmed from the search corpus.
    - `wiki/mind/synthesis/ai-collaborative-analysis.md` — +106 lines on
      "the venue is shaped like the hole": why the system migrated to LLMs this
      hard, both edges, what it means for this tool.
    - `wiki/mind/synthesis/intake-constancy.md` — NEW page (137 lines),
      the fixed-rate intake metabolism as a primary architectural fact; later
      extended with browser-history cross-validation (search constant upgraded
      [DOC]-grade).
    - `wiki/mind/concepts/contact-gini.md` — 0.961 made mechanical across
      the full 181,585-message corpus (498 contacts, top-1 28%, top-3 62%,
      only 12 ever >1k msgs) + topological redundancy consequence.
    - `wiki/mind/concepts/conflict-architecture.md` — the 414-message Grok-loop
      as literal mechanical mirror of the no-domain-selector flaw ("Dan's Law
      pointing at Dan, in code"); the 1,512 "I love you" vs 232 "fuck you"
      vs 180 apologies triad (reassurance dominance, not contrition); REVISED
      blockquotes where the full corpus sharpens the Annie-subset figures.
  - **Fixes:** corrupted OCR spellings in source text cleaned in wiki copy;
    broken `[[wiki/self/concepts/TOTALITY_SYNTHESIS...]]` wikilink corrected to
    the raw/ path (raw links pass lint, wiki/ links are checked).
  - `bin/wiki-lint` 0 errors throughout (37 pre-existing size-budget warnings).
    3 focused commits, branch `feat/wiki-wikipedia-chrome`.
* **Handoff Note:** The 4 filed Phase B sources are NOT yet exhausted — the
  bootloader's nine corpus findings and the browser doc's §8 (relational-name
  search traces: Tom most-searched/safe, Annie search-invisible, Alexis/Kristin
  post-hoc forensic) are only partially ported. `DAN_COGNITIVE_PROFILE.txt` is
  the CONTEXT_CORE_EXPANDED spine already well-ingested (duplication risk, not a
  gap). Next natural passes: (1) finish porting the bootloader's relationship-
  chronology corrections (Nov 2015 single-bond switch + 155 Virginia Ave lair-
  continuity) into attachment-trauma-bond.md / annie-ulmer.md; (2) the
  message-corpora people-thread pull (ANNIETEXTS.csv 9.9MB, *FULL CORPUS*
  CSVs) — handoff log lists ~17 unstarted stub pages still open. The user's
  standing directive: one source-cluster per pass, fully read → synthesized →
  committed, compounding forward; target 10-30 total hours of this ingest.

### [2026-07-14] - Session: repository cleanup and app hardening
* **Summary:** Removed two accidental empty duplicates under `wiki/wiki/`,
  repaired five stale internal links across `jason-bermejo.md` and `menore.md`,
  and made the app's Git-status path tolerate command timeouts and unavailable
  remotes. `py_compile`, `bin/wiki-lint` (0 errors), `git diff --check`, and
  localhost API smoke tests all passed. The 29 remaining lint messages are
  pre-existing size-budget warnings.
* **Handoff Note:** Preserve current uncommitted user edits in
  `wiki/.obsidian/`, `wiki/people/danielle-onesi.md`, and `.README.md.swp`.
  No content rewrite or inbox ingestion was performed in this maintenance pass.

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
