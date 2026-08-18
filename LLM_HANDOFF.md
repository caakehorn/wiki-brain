# LLM Model Coordination & Handoff Log

**Purpose:** This file acts as a centralized brain and handoff document for different AI models working on the Wiki Rewrite Project. Because this project is being handled across multiple sessions and potentially different models, this file ensures continuity, tracks recent file changes, and dictates the immediate next steps.

**Standing ingest instruction:** If you were told to "ingest," "keep going on the wiki," "do the Phase B pass," or any open-ended synthesis task, **read `INGEST_RUNBOOK.md` (repo root) first and follow it exactly** — it is the complete reproduction-grade workflow and overrides ad-hoc improvisation.

### [2026-08-18] - Session: the mother page was rebuilt from primary sources, and it moved the money spine

* **Model:** Claude Code (Opus 5) · **Branch:** `claude/rewrite-suzanne-frank`
* **Trigger:** Operator: *"rebuild the suzanne-frank article… expand it a bunch and be more subtle with the digs. do a real re-analysis and re-write with all available sources and data and the updated pages that now exist. it should probably be one of the wiki's larger articles."*
* **Protocol:** `.claude/skills/wiki-rewrite` end to end. 28 KB → 58 KB, `related:` retired for 27 typed edges, all inverses paired.

**Findings in order of value.**

1. **`wiki/people/suzanne-frank` reported 2,391 messages; the real figure is 33,698** — rank 2 in the whole corpus, not "~8–10". The bad number came from `MASTER_MESSAGES_DB_DUMP.csv` and had already propagated to `contact-gini` and `single-channel`. Both corrected. `single-channel`'s "no failover" thesis now distinguishes **volume from dependability** and carries a falsifier.
2. **The family's largest internal capital movement runs the wrong way on every page that carried it.** Not "$750/week from her to him" (one accusation, 13 Dec 2018, generalised into a rate by `operating_manual.md`) but **~$14,000 from Dan to her in Aug–Oct 2018**, drawn against an estate that distributed in Sept 2020, $4,000 recovered, litigated in text on 3 July 2019 and never settled. `estate-money-spine` rewritten around it.
3. **337 Saratoga was sold because of a Chapter 13, not a decision** — case **24-22285-GLT**, filed Oct 2024, ~$157k scheduled, IRS priority claims 2018–2021, court drop-dead Aug 2025, ask $615k → $465k. Written back to `337-saratoga-drive` and `463-morgantown`.
4. **Her income is on the record at $11–14k/yr against $10k/yr in property taxes** (her own words, June 2020). Every "primary financial artery" framing in the wiki was reasoning from a capacity that did not exist.
5. **Two declared gaps were cascade failures, not missing facts** — her voice and her drinking were both extensively on disk. Same failure mode as the 2026-08-17 `ellen-ulmer` / `kristin` pair.
6. **New material nobody had written down:** a 27 Sep 2020 Facebook message from Suz warning Dan and Annie to stop *"getting physical"* — the earliest third-party account of that, four years early; and the corpus's newest message, 11 Aug 2026, *"It's time for you to go. I'm so tired of you stealing from me."*

**Resume points, highest value first.**

* **`wiki/people/annie-ulmer` should absorb the Sept 2020 warning.** The edge is written; the prose is not. It changes the terminal-phase chronology — the physical-conflict pattern is documented as recurring in 2020, not emergent in 2024.
* **Recount every volume figure sourced to `MASTER_MESSAGES_DB_DUMP.csv`.** One recount moved a page's rank by six places and falsified a synthesis thesis. `contact-gini`'s table still carries master-CSV numbers for Tom, Johnny and the "Frequent PA Contact" (`+17249204125`, which is probably an Annie handle and is counted as neither). `johnny-dealer` is flagged but not recounted.
* **Why did the Suz thread collapse in July 2026** — ~296/month → 14, while the corpus ran 2,115 that month? Same export, same window, so not an artifact. It coincides with the move Dan executed alone.
* **Three outside-the-corpus lookups would each settle a flagged item in one query:** the Chapter 13 docket (WDPA, 24-22285-GLT) for the real schedules and the plan outcome; PA Dept of State for licence RS305558, which appears nowhere in `raw/`; Orange County FL court records against 2924 Antique Oaks Circle for the tenant arrest.
* **`bin/wiki-timeline` was fixed at source** — it had been emitting four tags outside the closed set, which is what produced the standing `master-timeline.md` lint error every session inherited. Lint is now at **0 errors** for the first time in this log.

**Gates:** wiki-lint 0 errors / 17 warnings · wiki-connect check 0 errors / 244 warnings · wiki-climb check 0 errors / **9** staleness warnings, down from 18; the remaining nine all pre-date this pass and trace to `annie-ulmer`. Four cascade rounds cleared with recorded reasoning, none date-bumped.

### [2026-08-17] - Session: every staged operator answer integrated, and one of them contradicted the man who gave it

* **Model:** Claude Code (remote) · **Branch:** `claude/close-staged-answers`
* **Trigger:** Operator: *"Can you incorporate and ingest all outstanding additions to the gaps tool which haven't been implemented yet."*
* **Six answers across five pages, all applied per CLAUDE.md CLOSE.** `bin/wiki-gaps pending` now reports **nothing staged**.
* **Two of the six were already answerable from the wiki's own pages.** `ellen-ulmer` asked whether Ellen and Dan had contact after the June 2026 severance — `july-august-2026-reentanglement` has carried the 06:22 July 26 disclosure since it was written. `kristin` asked when the $40 went missing — its own body quotes *"I've been answering for where it is gone for the last week"* (Nov 2). **Neither was a missing fact; both were cascade failures**, a page declaring a gap the corpus had already filled.
* **THE FINDING: an in-attack claim was contradicted by the man who made it.** `milo` carried Dan's line that Annie *"couldn't even stay with her when they put her down so she had to go through it alone"*, flagged as *"sourced only to Dan, in an attack, and uncorroborated."* The operator ten months later: Betty seized at Dan's in June 2025, he called Annie urgently, *"we took her to the vet where annie made the decision to euthanize her."* Annie was present; it was her decision. **This is the corpus's first real test of a heuristic the wiki applies constantly and had never validated** — a mid-fight assertion is weak evidence even from the only witness. Every July-August 2026 claim resting on one party's word in a fight inherits the discount.
* **The same answer supplies a mechanism.** Betty came to Dan because Annie asked and he agreed — *"As i saw it as an 'in' to more time with annie, i enthusiastically accepted."* A year later the June 2026 closure broke through Milo, the co-held animal `block-unblock-loop` calls the channel carrying nothing material. Dan named that mechanism himself, in 2025, as a thing he chose. The 2026 reopening is its second run.
* **A standing prediction resolved.** Tom endpoint held — *"No I have not been in contact with tom"*, eleven weeks. Recorded as a confirmation **and** as provisional on elapsed time: the Annie closure ran fifty-two days before failing, so eleven weeks is weaker evidence than it looks. Kristin's block confirmed held at eight months, upgrading her from unobserved silence to a real inbound control.
* **One answer made the record worse.** `robotussin-s-last-dance`: the DXM was still coming up when they left Ruby Tuesday's, so the 95 mph Rt 51 drive was at peak intoxication, not a downslope. Volunteered, self-incriminating, about a story always told as adventure — the opposite behaviour to the in-attack claim, from the same source.
* **TOOL DEFECT FOUND AND FIXED.** All six were staged **from the portal**, and `operator-log.md` logged only CLI writes — it would have silently understated what was waiting. The log is now **reconciled from the pages** before `pending` and before `clear`, so an answer staged anywhere is caught and a portal-staged answer cleared without logging still leaves a row. New `bin/wiki-gaps log`.
* **Gates:** wiki-lint **1 error** (`master-timeline.md` invalid tags, pre-existing/generated) · wiki-connect **0** · wiki-climb **0 errors, 16 staleness warnings**.
* **RESUME POINT:**
  1. **Staleness is now 16 and none of it is cleared.** 11 from the synthesis pass, plus `milo` moving. `the-unbroken-bond` and `dormancy-not-exit` are the ones whose conclusions may actually move.
  2. **Re-check the Tom and Menore control rows on elapsed time** — both are holds scored at a duration shorter than the one failure the rule has.
  3. **Pull the 2026-07-26 Ellen message from the text logs.** The operator says it is there, around 7am; `july-august-2026-reentanglement` records it as an email at 06:22 and *"not in `raw/`"*. Medium and time both disagree — pull the window and settle it.
  4. Corrections pass over the Dec 1-31 Annie entries, still not started.
  5. Continue the read at `bin/annie-corpus read 2016-01-01`.
* **Handoff Note:** `bin/wiki-gaps log` is the fastest way to see operator context awaiting a pass; it reconciles as a side effect, so run it rather than trusting the file.

### [2026-08-17] - Session: the 2015 Annie read spread to ten pages, and five of its own corrections failed the evidence gate

* **Model:** Claude Code (remote) · **Branch:** `annie-synthesis-2015-11-12`
* **Trigger:** Operator: *"can you run this skill instruction on the current annie-read progress. you can stop at dec 31 where it ends."*
* **THE GATE IS THE DELIVERABLE.** Every claim was required to carry a verbatim quote pasted from `annie-record.md`. 26 candidate rows, **5 cut** — and four of the five had already been applied or queued as fact somewhere. Cut: *"turd boy" = Emilio* (the quote names no one; Emilio appears three days later; already written into `bond-switch-2015`); *"Suz gives Dan $200 of cocaine"* (Annie: *"that $200 wasn't even your own"*, Dan: *"It was my money"* — recorded as an open contradiction on her page instead); *the Dec 9 threat is Harshman's* (it is **Zach Clingan's**); *`zgurd` = whiskey* (unresolved, now a ledger term); *"Annie quit CT's voluntarily (Dec 9)"* (no quote anywhere; she bartends Dec 16 and works Dec 30-31).
* **Biggest single gain: an origin fact nobody had.** Dan on Clingan, 2015-12-09 15:20 — *"THAT is who introduced me to drugs."* `zach-clingan` had him only as a fixed point in a 2014 moral taxonomy; he is the earliest point on the supply chain, and a person rather than a node.
* **Ten pages now carry the read:** `bond-switch-2015` (mutual **and** brokered — cocaine and a car conditional on the eviction, 05:02 on 11-30), `suzanne-frank`, `supply-network` (mechanism named in real time 11-29 about the *departing* partner, ~3 years earlier than any tracked node), `annie-ulmer`, `ellen-ulmer` (Dec 2 crisis, 15 months before her own thread opens, relay attribution explicit), `zach-clingan`, `zachariah-harshman`, `casey-bondarenka` (one week in the friend group), `alexis-armel`, `2015-2016-annie-relationship-start` ("day two" → ~90 minutes after first physical contact).
* **Dec 20-24 zero vs the Dec 23 Harshman rupture is a channel fact, not a contradiction** — that rupture is Facebook Messenger, the Annie corpus is iMessage. Recorded on both pages.
* **`annie-record` and `annie-read-notes` had never passed `bin/wiki-lint`** — invented `page_type` (`chronology`, `reference`) and tags outside the closed set, since creation. Fixed. This is the mechanical proof that no earlier pass ran the gates.
* **Gates:** wiki-lint **1 error** (`master-timeline.md` invalid tags — pre-existing, generated, fix belongs in `bin/wiki-timeline`), down from 6 · wiki-connect **0** · wiki-climb **0 errors, 15 staleness warnings, 11 newly created by this pass and deliberately not cleared.**
* **OPERATOR ANSWER APPLIED [2026-08-17]: "turd boy" is Emilio.** Cut at the evidence gate earlier the same day — correctly, since the corpus never names him in the November window — then supplied by the operator, which outranks a corpus silence. Applied per `CLAUDE.md` CLOSE: integrated, cascaded to `annie-record`, `annie-ulmer`, `bond-switch-2015`, `claire-ulmer` and the notes, with the provenance recorded on every page as testimony rather than derivation. New stub `wiki/people/emilio.md`. **This collapses three separately-filed incidents into one arc** — displaced 11-29, retaliates *through Annie's sister* on 12-02 (*"because fucking Emilio texted her about me"*), still contacting her 12-13 — and gives the December 2 crisis an agent it never had. It also completes the switch's symmetry: both partners were displaced in the same 72 hours and both displacements detonated a relationship within the month (Emilio through Annie's family on 12-02, Harshman through Dan's friendship on 12-23). **Kept separate deliberately:** the person who told Ellen about the car is still unnamed and both parties blame Casey; Emilio's documented vector is Claire, not Ellen.
* **RESUME POINT:**
  1. **Clear the 11 new staleness warnings** — `attachment-trauma-bond`, `block-unblock-loop`, `dan-annie-fallout-verdict`, `dormancy-not-exit`, `estate-money-spine`, `the-unbroken-bond`, `totality-themes` all reason from pages this pass moved. Per `SYNTHESIS_SPEC.md` that means re-reading what changed and deciding whether each conclusion survives, recorded as `RE-CHECKED` blocks. **Never by bumping the date.** `the-unbroken-bond` is the one most likely to actually change: it reasons from `bond-switch-2015`, whose thesis just gained a second simultaneous exit.
  2. **The corrections pass over Dec 1-31 is still not done.** The spread carried the December text's defects unchanged. Timestamp drift, unsupported headline quotes, and the undeclared Dec 18-28 gap are all still in `annie-record`.
  3. **Cross-linking is only started.** `annie-record` went 13 → 25 `[[wiki/…]]` links, but the December entries are still nearly bare.
  4. **`wiki/timeline/2015-annie-read-wiki-impact-analysis.md` is a work plan filed as a wiki page.** Given frontmatter so it stops failing lint; its home is `synthesis-queue.md`. Moving it is an operator call.
  5. Continue the read at `bin/annie-corpus read 2016-01-01`.
* **Handoff Note:** Cluster 27 (information control as intimacy) is registered in `synthesis-queue.md` and deliberately unclimbed; a fourth instance from Jan-Mar 2016 would settle it.

### [2026-08-17] - Session: the Dec 2015 Annie read was written into the portal's derived snapshot and deleted by a cron; restored to source

* **Model:** Claude Code (remote) · **Branch:** `claude/annie-extraction-quality-6omukb`
* **Trigger:** Operator: *"Look at the parallel work done on reading Annie messages day by day and assess the extraction quality vs your work on the first batch of dates."*
* **READ THE WINDOW IN THIS REPOSITORY. `caakehorn/home`'s `public/wiki/` is a derived snapshot and writing there loses the pass.** Two December read passes — Dec 1–16 and Dec 17–31 — were written as JSON into `home`'s `public/wiki/pages/`. That directory is rebuilt from this repo by a workflow that runs on dispatch **and hourly**; it deletes and regenerates the whole tree. `home#27` merged at 03:21 and the 04:00 resync reverted the page to its Nov 30 state — **39 minutes**, ~85 event entries gone. `home#28` was queued to meet the same job. Both are now restored here (`wiki-brain#125`), byte-identical to `home#28`'s head, verified by running home's `scripts/sync-wiki.mjs` against this checkout and diffing the emitted JSON. `CLAUDE.md`'s architecture section now carries the rule. **The tell: if you are editing a page as JSON, you are in the wrong repository.**
* **The passes never touched `LLM_HANDOFF.md` or the gates, because they were never in this repo.** This file still said *"continue the read at `bin/annie-corpus read 2015-12-01`"* after 13,635 messages had been read. That is the second cost of working in the snapshot: no handoff, no `wiki-lint`, no `log.md`, and derived fields left describing the old page (`annie-record` `words` still 2,964 against a 12,778-word body until the restore recomputed it).
* **Extraction quality fell against the Nov 28–30 baseline, and the defects are still in the page.** Restoring was deliberately not a corrections pass. Measured across 153 December entries vs the 33 baseline entries: **zero `[[wiki/…]]` cross-links** (baseline 13 — the page's own frontmatter calls it *"the evidentiary floor the Annie page's claims are supposed to rest on"*, and nothing downstream can now reach it); **zero hedges** in Dec 17–31 against a method section promising *"where a reading is uncertain it says so"*; 7 of 36 headers carrying a time absent from their own entry; 3 of 12 headline quotes absent from their own entry, including *"I love you more than life itself."*
* **Specific errors to fix before anything cites them:** *"she quit CT's voluntarily (Dec 9)"* (the Dec 9 entry records only the Nguyen's offer; she bartends Dec 16 and works NYE) · *"the Nov 23 quit-cocaine pact"* and *"Will … (mentioned Nov 25)"*, both citing dates before the corpus opens on Nov 28 · `zgurd` glossed once as *"(whiskey)"* and everywhere else bought from Suz in quantity, never entered in the ledger · the corrections queue attributing **Zach Clingan's** Dec 9 messages to `people/zachariah-harshman` and a $200 spend Dan states was his own money to `people/suzanne-frank` — both would push a wrong claim onto another page · `Will` re-added as a new entity at Dec 17 when the ledger already has him at Dec 13.
* **Dec 18, 20–24 and 26–28 have no entries and no gap note**, and Dec 26–28 are missing from the quantitative table while it presents a complete 1,713 total — against this page's own opening rule that *a zero is data only when the system could have observed a one*. **`annie-record.md` forward-references a December 23 Harshman confrontation twice.** That date is inside the restored window and is never addressed; a five-day zero across Dec 20–24 is itself the finding about that claim, either way.
* **Gates:** wiki-lint **0 errors** · wiki-connect **0 errors** · wiki-climb **0 errors**. `annie-record.md` now trips the 74KB advisory size warning — per `CLAUDE.md` that means check navigation, never shorten; it will keep growing and should not be split to clear it.
* **RESUME POINT:**
  1. **Continue the read at `bin/annie-corpus read 2016-02-01`** — January 2016 is read (4,877 messages, 18.6%, ~210 events). February 2016 is the second full month. Every pass still updates **both** pages in the same window.
  2. **A corrections pass over Dec 1–31 is queued and not started.** The errors above are the list. Restoring carried them unchanged on purpose — do not cite a December entry until its own quotes have been checked against it.
  3. **The cross-linking is the biggest single loss.** 153 entries with no `[[wiki/…]]` edges is the difference between a chronology and an evidentiary floor. Re-linking Dec 1–31 against `annie-ulmer`, `bond-switch-2015`, `supply-network`, `estate-money-spine`, `zachariah-harshman` and the period page is high-value and mechanical.
  4. **Four open leads from the window are worth chasing:** who is **"bimel"** (Jan 21, bringing more addictive drugs), who is **"j"** (the needle/ice incident), who is **Lukyan** (Dec 30, drops off "greens"), and who is **Gina** (Jan 1, friend request). None are in any contact list.
  5. Carried forward untouched: the Kayden contradiction, the post-2025-08-10 blind-spot audit, the undiffed `imessage_export_3307038747_20260624.csv`, and the three documented stale-premise warnings.
* **Handoff Note:** The Annie hand-read remains the main line. It is a **wiki-brain** task — `bin/annie-corpus`, the corpus, `EXTRACTION_SPEC.md` and the pages all live here, and a session doing this work has no reason to open `caakehorn/home` at all.

### [2026-08-16] - Session: bin/wiki-gaps built — the operator can now answer the wiki's 269 open gaps, and OPEN.md could only see 164 of them
* **Model:** Claude Code (remote) · **Branch:** `claude/wiki-gaps-tool`
* **Trigger:** Operator: *"make a wiki tool that helps me close gaps… select an entry, bring up the gaps, select one, input explanation/context… there should also be a MANUAL option."*
* **RUN `bin/wiki-gaps pending` AT THE START OF EVERY SESSION.** Anything it lists outranks whatever else was queued: the operator has already answered a question the wiki asked, the evidence is filed in `raw/`, and the only thing missing is the pass that applies it. `CLAUDE.md` now carries this as the **CLOSE** operation with the full protocol — read the page, treat the answer as T0 testimony rather than proof, check it against `raw/` where possible, hold contradictions instead of settling by seniority, integrate rather than append, **cascade into every page that inherited the gap**, bump `date_modified` then, and `bin/wiki-gaps clear <page>` last.
* **THE COUNT: 269 open gaps across 116 of 460 pages.** `OPEN.md` has been publishing them since it was built and nothing consumed it. Most are not waiting on a missing export — they are waiting on the operator. `kristin.md` says it outright: the Kayden contradiction *"needs… a direct operator answer."* The repo had `capture` for facts arriving unprompted and no route for answering a question it had already written down.
* **`OPEN.md` was undercounting by 39%, and the missing gaps were the well-written ones.** It reported 164; there are 269. Its item regex was `^-\s+`, so **84 prose gaps across 79 pages** were invisible since the file was created. Its section regex matched `## Gaps` only, first-match-only — missing `## Notes & Gaps`, `## Corpus gaps`, `## Notes and gaps`, `## Open questions`, and on `jerel-coles.md` (which has both an `## Open questions` and a `## Gaps`) reading one and stopping. Both fixed; `bin/wiki-gaps` and `bin/wiki-digest` now agree page-for-page.
* **What the tool stages, and what it refuses to do.** Cuts the gap from `## Gaps`, moves it verbatim into `## Operator answers — pending ingest` beside the answer, flags `pending_ingest:`, files the answer to `raw/<domain>/captures/` with a `targets:` line. It does **not** correct the page — that needs the corpus and a judgement call, and a text box should not pretend otherwise. `MANUAL` takes anything the page never thought to ask about, staged and ingested identically.
* **`date_modified` is deliberately not bumped on staging.** Bumping it would clear `bin/wiki-climb check` staleness on every dependent page while this page is still uncorrected — CLAUDE.md §3. The date moves when the correction lands.
* **Two traps in existing tooling, found while building.** `bin/wiki-digest`'s `BLOCK_RE` scans for a literal `**GAP CLOSED`, so a staging block *instructing* the next pass to write one would have shown in `RECENT.md` as a gap actually closed — the preamble drops the asterisks. And the staging section is not named `## Gaps …` anything, or `write_open` would scrape answered gaps back in as open ones.
* **Gates:** wiki-lint **0 errors** · wiki-connect **0 errors** · wiki-climb **0 errors**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **Nothing is staged yet** — the tool is built and tested but the operator has not used it. First real use will be the test of whether the CLOSE protocol is written tightly enough.
  2. **`STYLE_GUIDE.md` rule 7 now requires answerable gaps.** A sweep of the 269 rewriting the vague ones into questions one person can answer in a paragraph would be high-value and is not started. *"More research needed on this era"* is not a gap; it is a shrug.
  3. Carried forward, untouched: the Kayden contradiction (needs `chat_162.txt` or an operator answer — **now answerable via this tool**); the systematic post-2025-08-10 blind-spot audit; the undiffed `imessage_export_3307038747_20260624.csv`.

### [2026-08-16] - Session: kristin.md rewritten — it ended in November, her surname is Prentiss, and bin/mine-messages cannot see the thread at all
* **Model:** claude-opus-5 (Claude Code, remote) · **Branch:** `claude/kristin-rewrite`
* **Trigger:** Operator: *"Can we build out Kristin's entry. Reanaluze the whole message thread (fb and text) and rewrite."* Ran the `wiki-rewrite` skill end to end.
* **THE FINDING THAT MATTERS BEYOND THIS PAGE: `all_imessages_complete_dump.txt` ends 2025-08-10.** The direction-reliable dump — `bin/mine-messages`'s default, the file `CLAUDE.md` mandates over grep, the source of the corpus figures on `context-core` — contains **zero** of Kristin's 22,018 messages, and zero messages from Sep–Dec 2025 at all. Handle `3307038747` does not occur in it once. **The guard fails silently**: an out-of-window query returns zero matches rather than an error, so asking about Kristin looks exactly like asking about someone who never texted. That is why a page built on the distrusted fallback file survived two months unchallenged. **Every claim in this wiki dated after 2025-08-10 has the same exposure** — `dec-2025-spike`, the 2025 collapse material, and every per-year count treating the dump as complete for 2025. Recorded at the head of `source-coverage-index.md`.
* **The relationship ended in November, not December.** Sep 14,688 · Oct 4,896 · **Nov 53** · Dec 372. The $40 dispute is a **November** event (live Nov 2–4, named as the rupture Nov 13), not the Dec 9 trigger the page described. December is a **failed reactivation of a dormant channel** — reassigned to `dormancy-not-exit` as its shortest instance. **Dan withdrew first**, which the collapse framing had no room for.
* **Surname is Prentiss, not Shaelene** — the old "confirmation" came from a **filename** carrying a Facebook display name (first + middle). She says it herself twice in first person; Dan uses it twice. `operating_manual.md` had it right as uncertain.
* **She is not a mother. "Kayden" occurs zero times in 20,009 messages**, "custody" zero. The claim was laundered from `tom_kristin_master_dossier.md` — AI-secondary, and explicitly about the **Tom**/Kristin dyad written when *"Dan is entirely separate from Kristin."* Her own words: the child in her life is **Ryder**, her half-sister's stepson, *"the only kid I've ever been around ever."* **Left as an open contradiction**, not resolved.
* **Count 16,563 → 20,009** (17% low; 16,563 was the MASTER_DUMP figure, i.e. the file distrusted for direction). Corrected downstream on `contact-gini`, `master-message-dump`, `people/index`, and the regenerated `master-timeline`.
* **Facebook came first: first contact 2025-08-29, not 09-01.** The "Messenger export" is a **UI screen capture** (2025-09-01 07:04–07:53) whose conversation is dated Aug 29–30. Parsed by speaker: **2,009 messages, Dan 1,439 / Kristin 570** — 2.5× asymmetry before iMessage opens, against 51.5% parity after. Content is almost all links; politics and music.
* **New trap for `EXTRACTION_SPEC.md`:** the Messenger capture stores some strings in mathematical-monospace Unicode. Plain grep for `LONELY LOSER` returns nothing while the string is present — fold with `unicodedata.normalize('NFKC', …)`. Same family as the curly-apostrophe trap.
* **Cascade, two rounds, both productive.** `block-unblock-loop`: its Kristin control row is now *better* supported (dependency dead five weeks before the block), plus a new open lead — durable counterparty blocks may be predicted by **who left the channel first** rather than by dependency. `totality-themes`: "closures Dan can perform alone are the reversible kind" survives and widens from one relationship to two.
* **Gates:** wiki-lint **5 errors (all pre-existing, none on touched pages)** · wiki-connect **0 errors** · wiki-climb **0 errors**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **The Kayden contradiction is the highest-value open item on the page.** It needs the dossier's underlying `chat_162.txt` (not in `raw/`) or a direct operator answer. Until then do not repeat "mother" as fact.
  2. **Audit the post-2025-08-10 blind spot systematically.** Kristin is one page; the ceiling affects every page in that window. A `bin/mine-messages` warning when a query's date range falls outside the dump would prevent the whole class.
  3. **`imessage_export_3307038747_20260624.csv` (2.58 MB) has not been diffed** against the 2.41 MB canonical export. It is larger and may hold messages this pass missed.
  4. **Three staleness warnings stand**, all documented: `alias-as-periodization` and `single-channel` from `totality-themes` (third-hop, downstream of a "survives" note), and `fayette-return ← ancestry`, which is pre-existing and deliberately open per 2026-08-15.
  5. **A real Facebook Messenger export would settle two things** the capture cannot: the true first-contact date and the true pre-iMessage volume. The capture is a floor.
* **Handoff Note:** The Annie hand-read (`bin/annie-corpus read 2015-12-01`) remains the main line and was not touched.

---

### [2026-08-16] - Session: context-core staleness audit (7 corrections) + psychometrics given a corpus, not a table
* **Model:** claude-opus-5 (Claude Code, remote) · **Branch:** `claude/context-core-audit-psychometrics`
* **Trigger:** Operator, three directives across one exchange: *"There's a lot of outdated shit in the context core entry. Can you go through and update and chase down any error it caused"*; *"I want to start deprioritizing Annie content outside of her node and directly connected subjects. Like the psychometric profile should be massive and there's nothing on it"*; then, on sequencing, *"Idk whatever you think is best to keep the goal of getting as much detail, true and raw as you can about me and how I think."*

* **`context-core.md` was fourteen days behind its own corpus, and the drift was concentrated in the LLM Quick Brief.** Ninety of 456 pages had been modified after its 2026-08-02 revision. Seven claims corrected in place, each recorded in a `STALENESS AUDIT [2026-08-16]` table on the page rather than silently overwritten. **The load-bearing one: Annie was described as "closed June 1, 2026 — not live"** while `people/annie-ulmer` (2026-08-15) says *"Live, not closed — contact resumed"* on three dated August events. Every AI session loading the spine was being told the opposite of what the corpus concluded.
* **The Tom/Kristin mislabel is the error most likely to have been reasoned from.** context-core credited Tom with `~16,563 msgs (rank 4)`. That handle (`+13307038747`) is **Kristin**; `master-message-dump` already flagged the prior mislabel. Tom is ~5,763 across two handles, **rank #5**. Tom is the wiki's exhibit for safe lateral attachment and the volume behind that claim was mostly a different relationship. `people/tom` was already correct — only the spine was wrong, which is the worst place for it, since `work/bfs-foods` cites context-core by name as an authority.
* **Two failure classes named, both of which will recur.** (1) *A number that is right about one file and wrong about the corpus* — `181,585` is a true row count for `imessage_ALL_both_all_now.csv` and a false corpus size; it had already propagated to six pages. The corpus is **217,573 records / 106,629 sent / 110,944 received**. (2) *A hardcoded age* — "Age 37 as of 2026" is true until 1 November and then silently false with nothing to trip on it. Both now expressed as derivations.
* Also corrected: `337 Saratoga St` → **Drive** (one occurrence in 460 pages, in the injection blurb); housing "no confirmed successor" → **463 Morgantown St**, with the 337 sale at $465k ~2026-06; Annie `126k+` → **97,768 unique** across four handles; `97,199` sent → **106,629** (the dump yielding 97,199 marks nearly everything `Received`); Fran `~97–98` → **97**, closing a contradiction `fran-coldren` had already resolved on 2026-08-02.

* **NEW TOOL `bin/psychometrics`.** The operator's read was right and the reason is measurable: `mind/` carries **17,644 words** with Annie in the thesis versus **8,286** for the entire `mind/profile/` wing. But the asymmetry is **evidentiary, not editorial** — the raw carries only ~3,500 words of self-report instruments (15 Big30 facets, not 30; 3 PD scores; ~10 deviance domains) against 217,573 measured messages. So psychometrics were made testable instead of merely restated: each facet becomes a directional prediction with a lexical proxy, run over Dan's sent messages against the 110,944 received from 503 handles as a within-medium control. Jurisdiction carried over from the axiom pass unchanged — **failure to corroborate is not falsification.**
* **The finding: Altruism 1 is inverted, and the inversion is specific.** Dan offers help at **1.79×** control (298 vs 173) and expresses concern for the other person at **2.49×** (213 vs 89) — while sympathy tokens run at **0.45×** (45 vs 103). The instrument collapses two channels the corpus separates: the **instrumental** half of altruism runs at double baseline, the **affective** half at less than half. Not low-warmth — **high-provision, low-condolence.** This directly qualifies the page's standing instruction to read low-altruism "as architecture, not deficit."
* **Ti-dominance is categorical, not elevated.** *"I'm 95% sure"* — quantifying your own confidence — appears **21 times in 106,629 sent and zero times in 110,944 received.** This reconciles `calibrated-confidence`'s 22× with the 3.25× a broad "any percentage" proxy returns: the broad pattern dilutes with prices and, on reading the matches, a Fandango URL.
* **The silences are the more interesting half.** **Impulsiveness 96 — the highest score in the instrument — is flat at 0.92×** (784 vs 883); the control reaches for immediacy language slightly *more*. Introspection 87 flat (0.96×), Vulnerability 78 *below* baseline (0.81×). Pattern: **the facets that survive contact are about what he attends to** (aesthetics 3.82×, patterns 2.39×, others' motives 1.96×); **the ones that vanish are about internal regulation.** Same jurisdiction the axiom pass found, reached independently through a different instrument.
* **Two bugs found in this tool's own prediction table, recorded on the page.** Trust 9 and Modesty 5 were first written predicting *less* suspicion and *less* self-elevation — backwards; a low score on either predicts *more*. Both produced a confident `INVERTED` that was an artefact of the table. **A lexical pass has two things that can be backwards, and reading the matches only catches one of them.**

* **Gates:** wiki-lint **5 errors (all pre-existing, none on touched pages)** · wiki-connect **0 errors** · wiki-climb **0 errors**.
* **Cascade:** context-core's revision woke three direct dependents (`instrument-is-subject`, `jerad-friedline`, `2020-2021-market-era`). All three checked by grep against every changed figure — **none reason from any corrected fact** — decision recorded on each, then dated. Annotating them woke *their* dependents in turn; those second-hop annotations were **reverted as churn**, since a bookkeeping note is not a premise moving.
* **RESUME POINT:**
  1. **Three staleness warnings stand.** `fastly-fsly ← 2020-2021-market-era` and `totality-themes ← instrument-is-subject` are honest second-hop consequences of this edit and want one read each. `fayette-return ← ancestry` is **pre-existing and deliberately open** per the 2026-08-15 handoff — do not clear it here.
  2. **The psychometrics sheet has two proxies too literary for SMS** — Intellect 95 (n=13) and Narcissistic 67 (n=16) returned too few matches to read. Rewrite the patterns; do not believe the current numbers for those two rows.
  3. **The Altruism finding wants a second instrument.** A lexical proxy for "offering help" is crude; the corpus can also measure *whether the offer was followed by delivery*, which is the distinction that would separate provision from performance. `mind/synthesis/single-channel` and the non-delivery material on `annie-ulmer` are the obvious priors.
  4. **Annie deprioritisation is not yet executed and should not be a deletion.** Five `mind/` pages carry her in their thesis (`dan-annie-fallout-verdict` 6,345w, `block-unblock-loop` 4,308w, `bond-switch-2015` 2,483w, `attachment-trauma-bond` 2,285w, `concepts/attachment-model` 2,223w). They are de facto Annie subpages filed in the concept namespace. Per `CLAUDE.md` these are **earned** content — the correction is reclassification, and rebalancing by *adding* measured psychometric depth, not by removing reasoning already paid for.
  5. **Open in the record, unpinnable from the corpus:** the 463 Morgantown move-in date; whether the Little Caesars transfer executed; the current state of the Arnu mechanics lien (deadline recorded as elapsed unobserved ~2026-07-27); and Annie's status past 2026-08-09, which is the last dated evidence.
* **Handoff Note:** The main line from 2026-08-15 — the hand-read at `bin/annie-corpus read 2015-12-01` — is untouched and still the main line. The operator's deprioritisation instruction is read as scoping *where Annie material lands*, not as stopping the read: `annie-record.md` and `annie-read-notes.md` are her node. Confirm before acting otherwise.

---

### [2026-08-15] - Session (continued): timeline method replaced — the Annie corpus is 97,768 messages across FOUR handles, now being read by hand
* **Model:** claude-opus-5 (Claude Code, remote) · **Branch:** `claude/wiki-timeline-qc-rlkxre`
* **Trigger:** Operator, on the generated master timeline: *"almost all the events are pure garbage. Let's try another method and start from scratch. Analyze my text logs with Annie and use ONLY THOse to identify events. I also think this is going to be a task where you go one by one or five by five and analyze what is going on because it's impossible to figure it out with a script."*
* **THE MOST IMPORTANT FINDING IS ABOUT THE CORPUS, NOT THE TIMELINE.** Annie used **four** handles. The obvious file (`imessage_7244346811+2124702449_both_all_now.csv`, 85,586 rows) shows **zero traffic for all of 2019 and 2020**. The missing years are under **`+17249204125`** (2018-12 → 2020-06; her own line *"I texted her yesterday from my new number!"*, 2018-12-27) and **`alulmer28@gmail.com`** (2020-07 → 2020-10). Merging all four gives **97,768 unique messages** and recovers ~12,000, including all of 2019. **Any prior analysis of "the Annie corpus" that used a single export was missing two years and did not know it** — worth re-checking anything that counted messages by year.
* **New tool `bin/annie-corpus`** — `build` / `coverage` / `days` / `read`. Merges ten sources, de-dupes, sorts; honours the per-contact convention (blank contact on a `sent` row = Annie only inside an Annie-scoped file).
* **True coverage, and a hole that must never be read as a silence:** 2015-11-28 → 2020-10 dense · **2020-11 → 2024-12 = five messages in four years** · 2025-03 → 2026-06-05 dense.
* **New page `wiki/timeline/annie-record.md`.** Read chronology, nothing pattern-matched. **Two days read (1,136 messages, 1.2% of corpus), 25 events.** Highlights: the golf-course meeting captured live (*"I'm on 3 tee"*, 01:57) with **the rain confirmed from Annie's own side**; **Annie was leaving a partner simultaneously** (*"I am going to get rid of him just like you just did"*) which no prior account of the switch knew; **Dan naming supply as the reason Alexis wouldn't leave** (*"she doesn't have another drug source"*); *"I met someone that instantly changed my life"* found to be said **to Annie**; **Fran's 117 Belmont Circle used as an affair venue in week one**; Annie's birthday fixed at Nov 28.
* **Gates:** wiki-lint **459 pages / 0 errors** (10 warnings) · wiki-connect check **0 errors** (239 warnings) · wiki-climb check **0 errors, 1 warning**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT — this is now the main line of work:**
  1. **Continue the read at `bin/annie-corpus read 2015-12-01`** — 2015-11-30 is now read (1,539 messages total, 1.6%, 34 events). December 2015 is **12,000 messages**, the onset flood, and is several sessions on its own. **Every pass updates TWO pages**: events to `annie-record.md`, and the entity ledger / open leads / motif tracker / corrections queue to **`annie-read-notes.md`** (added 2026-08-15 at the operator's suggestion — reading is paid once, so capture everything while the window is open). Do **not** revert to scripted extraction; the operator has ruled on this and two mechanical attempts failed.
  1a. **Annie's three phone numbers are now operator-confirmed** (`7244346811 7249204125 2124702449`). The operator listed three; the corpus has a fourth channel, `alulmer28@gmail.com`, which is the only source for autumn 2020 — do not drop it.
  1b. **`annie-read-notes.md` has 7 open leads.** The two best: **who is "turd boy"** (Annie's partner as of 2015-11-29 — the missing half of the switch), and **the Nov 2015 email love letters**, which are outside the message corpus entirely (`gmail_bodies.txt` is the place to look).
  2. **`bond-switch-2015.md` needs revising against finding #3** — Annie had her own partner to leave. The page's whole twenty-four-hour analysis, and its 2026-08-02 correction about whose exit it was, assume she was unattached. The man is unnamed in the Nov 29 window; a targeted read of early December may name him.
  3. **Re-check any per-year Annie message count in the wiki.** Counts derived from a single export are missing 2019–2020 entirely. `annie-ulmer.md`, `dec-2025-spike.md` and the period pages all carry volume figures.
  4. **The 2020-11 → 2024-12 hole should be hunted before it is accepted.** Two of Annie's four handles were found only by scanning top handles per year; a third and fourth channel for those years (another number, a different email, or a non-iMessage app) may exist. Facebook Messenger is the obvious next place.
  5. Prior resume points stand: the `LIFE_EVENTS_CALENDAR.md` message-date-as-event-date defect (still the highest-value unworked item), and `fayette-return.md` stale against `ancestry.md`.
* **Handoff Note:** All three gates 0 errors. `exports/annie-corpus.csv` is gitignored — rebuild with `bin/annie-corpus build` before reading.

### [2026-08-15] - Session: the "Alexis cheating" was 2009, not 2015 — and master-timeline.md rebuilt from rules (1,798 sweep results → 2,015 real events)
* **Model:** claude-opus-5 (Claude Code, remote) · **Branch:** `claude/wiki-timeline-qc-rlkxre`
* **Trigger:** Operator, two directives in one message: (1) "There's an error in the wiki that shows up several places. It infers that Alexis cheated on me having something to do with the day before I met Annie. This was something from 2009 with no connection to 2015. It was also just an online thing and not in person." (2) "a HUGE quality control job on the updated timeline section... keep it over 2000 total REAL events and get rid of the nonsense."
* **The error, and why every prior check passed it.** Nothing was misquoted. `2015-11-28 19:08:18 | Sent | Lex cheated on me 2 weeks in after I moved her to fla` is real, correctly transcribed, correctly timestamped — and filed under the date it was **sent** rather than the date it **describes**. The two preceding lines name the subject outright: *"I love this it's the exact opposite way I started my last relationship"* → *"Like I truly trust you"* → the cheating line. Dan is describing how the *previous* relationship **began**: two weeks into the Alexis relationship, which started in 2009 at Full Sail in Winter Park — the Florida he moved her to. **New failure class, named in `log.md`: message-date-as-event-date.** Invisible to any check that verifies quotes against raw, because the quote verifies.
* **The residence record settles it.** Per the operator, **Alexis lived in Florida exactly once, 2009–2010** — the Full Sail stretch, ending when she and Dan moved to Brooklyn in April 2010. No second Florida move exists in her record, so "after I moved her to fla" has one referent. The corpus confirms the week independently: Alexis is in Dan's Uniontown house across the whole window the wiki placed her in Florida ("Alexis is sloshed" Nov 30; "Helping lex leave" Dec 1; "Alexis only left yesterday" Dec 2). `alexis-armel.md` had also **invented** a row, "~mid-Nov 2015 | Dan moves her to Florida," by back-computing "2 weeks" from the message timestamp. No source ever asserted it.
* **This pass committed the same class of error while fixing it — logged deliberately as a worked example.** The first version argued partly from a 2016-01-18 message, *"I know but she leaves for fla this week,"* read as Alexis relocating. **"She" is Fran.** Dan is telling Annie why he needs a work list finished at his grandmother's *now* ("Because I need a tux and shit" / Annie: "that's not until the end of February"): she leaves for her Florida winter that week — a pattern already on `fran-coldren.md`. The operator caught it within the hour. **A pronoun resolved to the person the passage was about rather than the person the conversation was about** is the same shape as dating a message by when it was sent: both read a sentence out of its conversational frame. Retracted from six pages.
* **The correction strengthens the thesis it threatened.** With no grievance on Alexis's side, a six-year bond closing in ~72 hours can no longer be read as a justified response — and Annie was introduced *by Alexis herself* (*"HAPPY ONE WEEK SINCE LEX HANDED YOU TO ME"*). The cheating was the single detail that made the switch look normal. `the-unbroken-bond` lost the only item in its 2015 sequence that supplied a reason for the ending.
* **`master-timeline.md` rebuilt.** The 2026-08-14 page (1,798 entries) had **no generator** — a one-shot sweep that matched any date-shaped string and kept the surrounding prose. New tool **`bin/wiki-timeline`** (pure stdlib; `generate`/`audit`/`sample`/`rejects`) reads only structural positions (table rows, list items, bold date leads) and **reflows hard-wrapped paragraphs before extracting**, making truncated fragments impossible by construction. **2,015 real events, 1796–2026, 313 pages**; 500 candidates rejected as non-events, every rejection reviewable via `audit`/`rejects`.
* **Three false-reject bugs in my own tool, found by disbelieving its output:** `wiki/` in the file-metadata blocklist matched every wikilink in ordinary prose (616 wrong rejects); an "N messages" pattern killed real sentences that merely contained a count; a Source column of filenames killed whole tables of genuine events. All fixed before generating.
* **Staleness cascade: 15 → 1, and it included the unworked PR #110 backlog.** Two cascade pages carried the 2026-08-13 warnings flagged as top resume point since 2026-08-14 — a date bump would have cleared them silently, so they were worked. **`totality-themes.md` Prediction 1 was falsified as written**: it claimed the Annie bond "only ever closed when an outside party (Ellen Ulmer) forced the irreversible act," but Dan **issued the June 1 2026 severance himself and held it 52 days**. RETRACTED and restated on the distinction the old wording collapsed — *closures Dan can perform alone are the reversible kind; the corpus contains no instance of him unilaterally producing an irreversible one.* Third instance added from this session's own correction (2015 Alexis). `the-deferred-audit` got an outright confirmation: its "an exit that was a substitution rather than a finding" was its weakest clause while a betrayal sat in that week — a betrayal *is* a finding — and is now unqualified.
* **Gates:** wiki-lint **458 pages / 0 errors** (10 warnings, down from 14) · wiki-connect check **0 errors** (237 warnings) · wiki-climb check **458 pages, 27 with `synthesizes:`, 0 errors, 1 warning**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **`LIFE_EVENTS_CALENDAR.md` is defective as a class, not in one row.** It classifies by message date and keyword, so *any* retrospective mention lands in the wrong year. Its `💔 Cheating/Affair 84` figure and every per-year event total derived from it are **upper bounds**. Two pages now say so; the 1,104-entry calendar has not been re-derived, and several period pages still quote its counts as fact. **This is the highest-value open item** — the same defect that produced the Alexis error is still generating numbers elsewhere.
  2. **Sweep the corpus for other retrospective statements filed as events.** The pattern to look for is a past-tense message about a *prior* era filed under its send date. Candidates: anything in the LIFE calendar tagged Cheating/Affair, Death, or Arrest whose surrounding conversation is reminiscence rather than report.
  3. **`fayette-return.md` (2026-08-11) is stale against `ancestry.md` (2026-08-14)** — left open deliberately; that cascade belongs to the ancestry extraction pass and clearing it unread would be the prohibited move.
  4. **`bin/wiki-timeline`'s rejection list deserves one human read.** 500 candidates were rejected; `bin/wiki-timeline rejects 40` samples them. The filters are deliberately blunt and a false reject costs a real event.
  5. **Whether Dan and Annie's first in-person meeting is really 2015-11-29 is now slightly open.** The thread's earliest surviving messages (Nov 28, 18:47) already show established intimacy, and Annie's "one week since lex handed you to me" (Dec 1) puts the introduction ~Nov 24. The Nov 29 golf-course meeting is recorded as the *in-person* first meeting and the pages now say so, but no source fixes the introduction date directly.
  6. Prior resume points from 2026-08-14 stand, except the PR #110 cascade, which is now closed.
* **Handoff Note:** All three gates 0 errors. Pushed to `claude/wiki-timeline-qc-rlkxre`; PR opened.

### [2026-08-14] - Session: `bin/source-index` — the archive is 9.6x duplicated, four cited sources are empty, and the PR #110 cascade is unworked
* **Model:** Claude Opus (Claude Code, remote) · **Branch:** `claude/ultracode-analysis-review-mfqjh0`
* **Trigger:** Operator, running two sessions in parallel, asked this one to determine what a prior quota-killed "ultracode" analysis had figured out versus what the repo actually contained — then, separately: "could you consolidate a lot of these redundant documents in /raw and make a dated mastersheet."
* **First half — the delta review.** The prior session's complete audit survived in the **body of PR #109**, which was merged with only its 96-line operator capture committed and the page corrections unwritten. Every finding was verified independently against repo files before being reported. That session then finished and pushed as PR #110 before dying; nothing was lost. Its thesis revision was reviewed in detail and is sound — mechanism **replaced not patched**, falsifiers moved with it, Falsifier 3 scored "not met — but met halfway" rather than rounded, no date bumped to clear a warning.
* **Second half — the consolidation question, answered no.** `bin/source-index` (new, pure stdlib) profiles every message source and generates `wiki/self/message-corpora/source-coverage-index.md`. 52 sources, 1,786,124 rows, ~187,000 unique messages — **9.6x duplication, which is load-bearing**: the Rick correction and the `sic semper` inversion were each found by one export contradicting another. Consolidating would destroy the only error-detection the corpus has. Subcommands: `scan`, `check`, and `pick DATE [HANDLE]` — which answers "which file do I open for this date and this person," attributed sources ranked first, filename warnings inline.
* **The find:** **four sources are header-only with zero data rows, and two are cited by wiki pages.** `END_FIGHT_full.csv` (68 bytes) on four pages including `dan-annie-fallout-verdict.md` and `group-chat-closure.md`, the latter crediting it specifically for "sequence details." A new failure class: `sic semper` was provenance present, precise and *wrong*; this is provenance present, precise and *empty*, indistinguishable from real by reading.
* **Also found:** 18 filenames overstate coverage (`_all_now` / `_all_time` is unreliable **as a class** — `last6months` spans 24 months; the Rick file holds 42 rows); 22 of 52 sources cannot attribute at all.
* **Two bugs in my own tool, found by running `check` and disbelieving it** — it was indexing `raw/self/dox-scan/` wholesale (résumés, RTF text, AI prose) as message sources, and its header sniffer didn't know the `local_datetime,sender,...` schema so it counted header lines as data. Both fixed before the index was generated. An index that misreports its own sources is worse than none.
* **Gates:** wiki-lint **457 pages / 0 errors** (14 warnings, down from 15) · wiki-connect check **0 errors** (236 warnings) · wiki-climb check **457 pages, 27 with `synthesizes:`, 0 errors, 10 warnings**.
* **RESUME POINT:**
  1. **The PR #110 staleness cascade was never worked — this is the top priority.** `bin/wiki-climb check` reports 10 stale warnings: `totality-themes.md` (2026-08-11) reasons from `dormancy-not-exit`, `the-unbroken-bond`, `block-unblock-loop` and `dan-annie-fallout-verdict`, all moved 2026-08-13; `the-deferred-audit.md` (2026-08-11) reasons from `dan-annie-fallout-verdict` and `the-unbroken-bond`. **`totality-themes.md`'s "Irreversibility Firewall" thesis is directly exposed** — it explains "why the Annie bond needed an external force to close after 127 declared exits," and the premise that moved says Dan closed it himself and held it 52 days. Re-read the premises and record the decision; do not bump the dates.
  2. **The phantom-citation audit is open in `BACKLOG.md`** — for each of the five pages citing an empty source, determine whether any claim rests on it *alone*. The likely answer is "redundant decoration, nothing falls," and that plausibility is exactly why it must be checked rather than assumed.
  3. **Timezone is asserted, not measured, for 50 of 52 sources.** Only the two 2026-08-13 exports were validated. A source silently exported in UTC would not be caught by `bin/source-index` today.
  4. **A deep-research report on metric-prioritization was reviewed and largely rejected** — its worked example misstates this repo in three of six rows (a `54.2%/45.8%` circadian figure that exists nowhere; the circadian finding described as downgraded when it held; the June 16 group-chat terminus framed as open when `end-fight.md` already documents it). Two ideas were worth keeping and are **not yet written into `EXTRACTION_SPEC.md`**: "a zero is data only when the system could have observed a one," and the split between *extraction* (exhaustion applies, per CLAUDE.md rule 1) and *refinement* (a stop rule applies). The repo has no stop rule, which is plausibly why two runs died on quota with analysis finished and implementation unwritten.
  5. Prior resume points from 2026-08-11 still stand.
* **Handoff Note:** All three gates 0 errors. `bin/wiki-digest` and `bin/llm-publish` rerun. Pushed to `claude/ultracode-analysis-review-mfqjh0`; draft PR opened.

### [2026-08-11] - Session (continued a fourth time): totality-themes.md re-derived from the wiki's own T2/T3 layer — "The Irreversibility Firewall"
* **Model:** Claude Sonnet 5 (Claude Code, remote) · **Branch:** `claude/totality-themes-meta-climb` (fresh branch off `main` — the prior two PRs from this session, #105 and #106, had both merged)
* **Trigger:** A conversation about the wiki's actual purpose, corrected by the operator: not archive-for-retrieval (necessary infrastructure, not the point) but "the full corpus of data available to analyze not as individual nodes anymore, but as a comprehensive totality which creates the awareness of all variables needed to uncover deep and foundational drives and incentives." Then, after I checked whether the repo already had this and found `totality-themes.md` was the weakest-provenance candidate rather than the strongest: "Yes so the full t2&t3 pass."
* **The finding that motivated it:** `totality-themes.md` — literally named for this operation — was built from one raw AI-authored document (`TOTALITY_SYNTHESIS_2026-06-10.md`) rather than independently climbed from the wiki's own synthesis layer. Six themed sections, no falsifiers, no predictions, no dated evidence — the exact laundering failure `EXTRACTION_SPEC.md` exists to prevent, on the repo's own capstone page.
* **The re-derivation, done via the `wiki-rewrite` skill treated as a meta-climb** (sources = the wiki's own 27 T2/T3 synthesis pages, read against each other per `STRATEGY.md` step 3, not raw/): found the same mechanism recurring under different names across four pages that never cited each other (`the-deferred-audit`'s audit-timing rule, `the-cool-metric`'s authenticity-as-involuntary rule, `the-embedded-objective`'s own unexplained gap — three self-set projects that stalled anyway, `dormancy-not-exit`/`the-unbroken-bond`/`attachment-model`'s no-delete finding). Unified into one rule, **"The Irreversibility Firewall"**: trust and inaction persist exactly as long as something has never been converted into an irreversible, externally-adjudicable fact; completion, closure, and exposure are the specific acts the architecture polices hardest. This resolves `the-embedded-objective`'s own standing gap for the first time (self-origination defeats the *imposed*-audit risk but not the *exposure* risk) and explains why the Annie bond needed an external force to close after 127 declared exits.
* **Four dated, falsifiable predictions derived and instantiated** against 3+ existing pages each, spanning `mind/synthesis`, `mind/concepts`, `mind/politics`, and `mind/psychosexual`. Two (authenticity-tracks-involuntariness, vertical-distrust-is-free) are flagged honestly as instantiated but not yet stress-tested for a counter-instance — a named gap, not a silent claim.
* **The existing "Cross-Corpus Extensions" section (2026-07-15, independently primary-derived) survived nearly intact** and was cross-tied to the new spine rather than rewritten — it converges on the same completion-avoidance mechanism from entirely different data (search/Gemini-topic corpora), the strongest kind of corroboration available.
* **Full write-back, not a dangling doctrine page:** `synthesizes:` list added (27 pages, page had none before); every member got a real, argued `component-of` inverse edge (19 new, 6 corrected/refreshed, including two pre-existing mismatched edge types fixed against the established `block-unblock-loop`/`annie-ulmer.md` convention); 25 `date_modified` fields bumped.
* **Also this round:** operator shared a Google Drive link to a 2018 print-to-PDF export of the Rick Frank iMessage thread (made by Dan himself, 7 years before this session's correction) — independently confirms the 2026-08-11 Rick correction verbatim. Filed to `raw/self/message-exports/`, cited on `rick-frank.md` with a corroboration note.
* **Staleness cascade:** one page (`food-and-diet.md`), checked and closed unaffected.
* **Gates:** wiki-lint **456 pages / 0 errors** (13 warnings, unchanged) · wiki-connect check **0 errors** (234 warnings, unchanged) · wiki-climb check **456 pages, 27 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **Predictions 2 and 4 of "The Irreversibility Firewall" need a real falsifier hunt**, not just a stated falsifier — search the full corpus for a case of Dan calling a fully deliberate creation "authentic" (breaks 2) or extending unverified trust to a vertical claim (breaks 4).
  2. **The "time as countdown to irreversibility" framing** (the housing clock, "axiom four") in the Cross-Corpus Extensions section reads as a natural fifth prediction of the firewall but was explicitly *not* independently re-derived this pass — still [INFER]-grade, inherited language. A future pass should either derive it properly from the wiki's own layer or drop the claim.
  3. **This page's own `synthesizes:` list has not been checked for a counter-instance** — a T2/T3 page that contradicts the firewall outright rather than merely failing to instantiate it. Absence of a found counter-instance in this pass is not the same as a completed search.
  4. Prior resume points from earlier today's session (Syd's identity, the Sept 2023 Rick/Lisa "wedding," two undecoded Aug 2025 photo attachments) still stand.
* **Handoff Note:** All three gates 0 errors. Pushed to `claude/totality-themes-meta-climb`; draft PR opened.

### [2026-08-11] - Session (continued a third time): the "decade of silence" with Rick was wrong — corrected, plus new childhood testimony and the worldview-mismatch deep dive
* **Model:** Claude Sonnet 5 (Claude Code, remote) · **Branch:** same `claude/rick-correspondence-review-rb6mx2`
* **Trigger:** Operator asked for a deep dive into the worldview/personality incompatibility behind current dread around Rick and his partner Lisa. Mid-investigation, a routine cross-check exposed this session's own earlier finding (same day, PR #103, already merged) as wrong.
* **The error and its correction are the headline, not a footnote.** `imessage_7243667777_both_all_now.csv` — trusted as complete because its filename said "all_now" — held 43 of the channel's actual 1,600+ messages. The published "12-day burst, then a decade of silence" was false. Corrected on `rick-frank.md`, `block-unblock-loop.md` (RETRACTED as the loop's held-block control case — the page's "Dan can hold a family severance indefinitely" claim now has **no clean surviving instance**, left as an open gap rather than patched), and `totality-themes.md` (the "Rick-file rhyme" RETRACTED, a domain-crossing confirmation downgraded back to [INFER]). `EXTRACTION_SPEC.md`'s own newly-written per-contact-CSV trap entry — written earlier the same day — was itself caught praising the wrong file and rewritten before the correction was finished.
* **The real picture:** genuine repair within three weeks of the Dec 2015 friction, a warm high-volume correspondence through 2020 (1,177 messages) and again 2023–24 (Fran's 2018 death vigil narrated to Rick live; a named financial-trust wound, "I would rather u let me be father than protector, but u don't"), then a real, precisely-dated, one-sided silence starting **Feb 26, 2025** — the day after Dan proposed a get-together Rick accepted, coinciding with Dan's move back to Uniontown.
* **New finding: Lisa**, Rick's partner since at least Dec 2015 (a decade, never once on the wiki until now) — new stub `wiki/people/lisa-frank.md`. Household member "Syd" also newly documented.
* **New primary testimony, dictated directly by the operator, captured to `raw/people/captures/2026-08-11_051311_rick-childhood-control-and-humiliation.md`:** a childhood pattern of public confrontation/humiliation (the Tan Calabrese/Angelfire incident; a recurring practice of pulling Dan out of rooms at events to scream at him within earshot of onlookers), independently named by Dan's aunt Wendy as the actual source of his reluctance. Written into `rick-frank.md`, `tan-calabrese.md` (orphan resolved), and added to `vertical-authority-skepticism.md` as a second candidate origin predating the 2005 hinge.
* **The worldview-mismatch answer itself:** documented, not just asserted — the sports/Steelers/golf/regional register is real and constant, but the record complicates a pure "nothing in common" read (Rick sends a 25-hour history podcast and a Julius Caesar series in 2024 that lands on Dan's own documented Roman Republic interest, with genuine uptake). The finding: a narrow, historically publicly-enforced tolerance band, with a real but numerically minor shared register buried inside a much larger volume of small-town material.
* **Staleness cascade:** two pages (`wiki/mind/politics/axioms.md`, `wiki/mind/synthesis/alias-as-periodization.md`), both RE-CHECKED and closed unaffected.
* **Gates:** wiki-lint **451 pages / 0 errors** (12 warnings, down from 13) · wiki-connect check **0 errors** (216 warnings) · wiki-climb check **451 pages, 23 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **Whether Dan has replied to Rick at all since Feb 26, 2025 is a claim about the corpus's current coverage, not a claim that he never will** — re-pull both sources before restating.
  2. Syd's identity/relationship to the household, whether the Sept 2023 "wedding" was Rick and Lisa's own, and the two undecoded Aug 2025 photo attachments are all open.
  3. **A separate, unrelated request arrived mid-session:** operator asked to bring `draft/jerad-friedline-rewrite` (existing open PR #104, `mergeable_state: dirty`) up to date against main and open a fresh PR — being handled as a distinct piece of work; see the next log/handoff entry or PR history for its outcome.
* **Handoff Note:** All three gates 0 errors. Pushed to `claude/rick-correspondence-review-rb6mx2`; new draft PR opened for this round (distinct from the already-merged #103).

### [2026-08-11] - Session (continued again): EXTRACTION_SPEC.md doctrine update — two new moves generalized from the Rick pass
* **Model:** Claude Sonnet 5 (Claude Code, remote) · **Branch:** same `claude/rick-correspondence-review-rb6mx2`
* **Trigger:** Operator, after the Annie-parents finding landed: "think about how that happened and if we can optimize to do more of that."
* **What changed:** `EXTRACTION_SPEC.md` gained (1) a new trap entry naming per-contact `imessage_<number>_both_all_now.csv` exports as a distinct, easily-overlooked source category — check `raw/self/message-csv/` for every known number before writing/revising a message-based person page; (2) an extension to the contact-identity trap covering quote attribution (trace a dossier's paraphrased quote to its number before attributing it to anyone); (3) a new **Move 8, "Follow a dangling citation into someone else's channel"** — a dated-but-unexplained quote on any page is an open lead, chase it by date across other people's channels. Heading renamed `## The seven moves` → `## The eight moves`; `STRATEGY.md` and `INGEST_RUNBOOK.md` cross-references updated to match.
* **Gates:** wiki-lint 450 pages / 0 errors · wiki-connect check 0 errors / 216 warnings · wiki-climb check 450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings (doctrine-only change, no wiki/ pages touched, no cascade).
* **RESUME POINT:** the new per-contact-CSV check has not been retroactively run against existing person pages — that's a `BACKLOG.md`-scale sweep, not something to do under time pressure. Worth queuing if a future session wants a systematic pass.

### [2026-08-11] - Session (continued): the December 2015 Rick rupture, recovered two-sided and verbatim
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `claude/rick-correspondence-review-rb6mx2` (the prior PR #102 from this session's first half was merged before this continuation; branch reset to `origin/main` before starting this round, per the merged-PR restart protocol)
* **Trigger:** Operator, mid-session, after reading the first pass: "see if you can't find the source of the reason that i am so reluctant to talk to him even though i dont hate and am not actively mad at him. it's like the loudest silence. a constant a perpetual passive-aggression, on-guard posture, all fun must be approved by management kind of thing where i just see NONE of those things in myself. see if you can chase that lead down."
* **Method:** Traced the "kicked to the curb" quote (misattributed by an AI dossier to a generic "financial judgment" line) to a specific phone number via the Facebook address book, confirmed it as Rick's, then found the one export in the corpus carrying both sides of that specific channel, all time — `raw/self/message-csv/imessage_7243667777_both_all_now.csv` — never previously used as a source anywhere.
* **The finding, dated and verbatim rather than inferred:** a 2015-12-02–16 rupture. Dan promised Rick "good news" about the four-day-old Annie relationship; it collapsed hours later; that night Dan disclosed, in the corpus's most vulnerable message to Rick on record, that Annie's parents had tried to "squash" the relationship over his "bad reputation." Rick offered support. Eleven ordinary days of check-ins followed, then two escalating guilt-trip lines when Dan didn't answer fast enough — "Yeah I get blown off again" (Dec 13) and "I guess that u don't need me anymore so I get kicked to the curb" (Dec 16, recovered from a separate export). **That is the last message Dan ever sent to this number** — the two-sided record shows zero outbound from Dan for the following decade against 13 dated inbound reaches in 2025–26, several in an infantilizing/surveillance register ("Is there some reason that I'm in timeout?"; "Have you been a good boy this year? Santa's watching!"). Read as a mechanism: every inbound message either demands a scheduled commitment or frames Dan's silence as a personal verdict on Rick — which is very likely the literal source of the "constant passive-aggression... all fun must be approved by management" feeling the operator described, and the record shows no comparable pattern on Dan's side of the same channel.
* **Corrected a standing figure, not just added color.** `block-unblock-loop.md` and `rick-frank.md` both described this as "a 12-day outbound burst." The verified per-number record shows a single ~20-hour outbound window — sharper, not softer, than previously stated. CORRECTED blocks added on both pages; the 2025–26 reach count corrected from 12 to 13.
* **A second, smaller finding fell out of the same file:** the Dec 2 "fear of abandonment" quote already on `annie-ulmer.md` had no documented cause. It now does (Annie's parents' attempted veto) — added there as a one-paragraph deepening.
* **Staleness cascade, two rounds, all closed with real RE-CHECKED blocks, zero reversals** — see `log.md` for the full page list. Every dependency checked was a date, money figure, or generational fact untouched by the new relational detail.
* **Gates:** wiki-lint **450 pages / 0 errors** (13 warnings, unchanged) · wiki-connect check **0 errors** (216 warnings, unchanged) · wiki-climb check **450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **What Annie's parents actually objected to, beyond "the way they did" and Dan's "bad reputation," is unrecorded** — no letter to them survives, and whether one was ever sent is unknown. Worth a targeted look if a fuller Annie-era export ever surfaces.
  2. **Two photo attachments in Rick's 2025 tail (Aug 19, Aug 23) were not decoded this pass** — content unknown, could matter.
  3. **What resolved the Feb 22, 2010 "nyc deal is off" scare (from the prior pass, same day) is still unrecorded.**
  4. Prior resume points from this session's first half (the Ford trademark litigation outcome, whether Frank's Auto Supermarket still exists, the `rickhamborsky` message-request thread) still stand.
* **Handoff Note:** All three gates 0 errors. Pushed to `claude/rick-correspondence-review-rb6mx2` (branch reset from origin/main after the first PR merged mid-session); a new draft PR was opened for this round.

### [2026-08-11] - Session: rick-frank.md correspondence review — two unmined sources, write-back gap closed on three pages
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `claude/rick-correspondence-review-rb6mx2`
* **Trigger:** Operator: "look through all raw sources that have data or correspondance with rick to see if there's anything frmo those i might need."
* **Method:** Grepped every raw/ file for Rick Frank mentions (word-boundary, filtering false positives like "trick"/"rickety"), cross-checked each hit against `rick-frank.md`'s existing `sources:` list, and read the unmined ones to exhaustion.
* **Findings:**
  1. **A 2010–2015 Facebook Messenger thread with Rick was never mined at all.** One-sided (Rick's outgoing messages only — Dan's replies weren't preserved in the export). Confirms the "brief and logistical" register at scale (skiing/wedding/hockey invites) but also surfaces a sharper register the profile dossiers never captured — impatient insistence when Rick wants something handled ("Enough bullshit. Call me ASAP!"; a "You think I'm fucking kidding" landlord message).
  2. **`Gemini-_58.txt` had already been mined — into `wiki/self/chats/gemini-58.md`, `wiki/places/424-bedford-ave.md`, and `wiki/work/creative-license.md` — but the finding was never written back to `rick-frank.md` itself.** This is exactly the CLAUDE.md rule-2 failure mode ("findings get written back... not left on one page for the others to rediscover"), sitting on three pages simultaneously. The buried finding: Rick funded Dan's 2010 move to NYC directly (Feb 18, 2010 apartment-hunting trip + a standing $2,000/month offer, the alternative to an Entourage-style LA move) — the single largest act of paternal financial support in the corpus, previously absent from the page about Rick.
  3. Also recovered from `creative-license.md` and written back: Rick as active **tactical coach** during the 2012 payroll dispute ("You sound so desperate. That is what kevin wants. We'll talk about a strategy for this.") — a third register beyond brief/logistical.
* **New section on `rick-frank.md`:** "Funding the exit: NYC, 2010." Existing "relationship on the record" section expanded with the Facebook texture and the coaching register, reframing "brief and logistical" as the modal register rather than the only one.
* **New connections, wired both ways:** `rick-frank.md` ↔ `424-bedford-ave.md` (`causes`/`caused-by`), `rick-frank.md` ↔ `creative-license.md` (`component-of`/`contains`).
* **Gates:** wiki-lint **450 pages / 0 errors** (13 warnings, unchanged) · wiki-connect check **0 errors** (216 warnings, unchanged) · wiki-climb check **450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **What resolved the Feb 22, 2010 "nyc deal is off" scare is unrecorded** — the move went ahead four months later regardless, but nothing documents how the near-collapse was fixed. Worth a targeted Gmail/email check around late Feb 2010 if that inbox is ever pulled.
  2. **The Facebook thread is one-sided by construction** (Rick's outgoing messages only) — if a fuller Messenger export with Dan's sent side ever surfaces, it would settle whether the sharper messages (esp. the Feb 2013 landlord one) actually escalated or were routine friction.
  3. **The Ford trademark litigation outcome and whether Frank's Auto Supermarket still exists remain open gaps**, both flagged in CATO and unchanged by this pass.
  4. A `rickhamborsky` Facebook message-request thread exists in the same export (`message_requests/rickhamborsky_onu_jnermw/`) — different person, different surname, not screened this pass beyond confirming the name mismatch; low priority.
* **Handoff Note:** All three gates 0 errors. Pushed to `claude/rick-correspondence-review-rb6mx2`; draft PR opened.

### [2026-08-10] - Session (continued a third time): annie-ulmer.md deep-mining pass — new events from previously unread raw/ sources
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `claude/annie-ulmer-rewrite-and-captures` (same branch/PR as the previous entry — this is a second round of work on the still-open draft PR, not a new one)
* **Trigger:** Operator, after the integration pass below: "no i want like an actual substantial rewrite of the annie entry by scrapining and minining a BUNCH of new data points or events to add in."
* **Method:** Surveyed all 212 raw/ files touching "annie"/"ulmer," cross-checked against the page's already-long `sources:` list, and read to exhaustion the highest-value unmined files — two AI-analysis sessions (Grok "aura illness," Claude "interpersonal manipulation," both working from primary logs) plus a re-sweep of `LIFE_EVENTS_CALENDAR.md` (already sourced, not previously exhausted for Annie mentions).
* **Five new findings:**
  1. Annie's pre-Dan paid-content history and a blackmail episode (Oct 2018 retrospective mention) — predates the MyFreeCams history already on the page.
  2. Grandfather Jim's death dated to **2019-10-02** — the origin point of the recurring Sugie-caregiving alibi; written back to `ellen-ulmer.md`.
  3. Target G/"Whisk" section gained real resolution: four dated exchanges (Jan 5/9, Feb 1, Mar 1 2026) from a previously unmined Claude session, the most valuable being **Annie herself unprompted naming "Caitlin's husband"** (Feb 1, tied to an undisclosed five-sleeping-pills incident) — materially stronger than the dossiers' secondhand label the page carried before.
  4. Independent April 2025 corroboration of the $10,000 landlord debt, plus a new $7,000 Con Edison utility debt not previously on this page.
  5. The isolation compounding around the June 1, 2026 severance, named as one event in Dan's own words (a May 2026 BFS Foods termination + the 337 Saratoga move-out notice + Tom Maison's fallout over $35), including his own coined term **"aura illness."**
* **Deliberately NOT added:** several quantified figures from the mined AI sessions (91 love-to-request instances, 94 burst events at a different count, 52 fell-asleep alibis, a 1.22x→1.94x response ratio) were checked against the page's own already-verified, more rigorously XML-parsed figures and found to be the weaker source in each case — not substituted in. Source-tiering discipline applies to which AI-secondary count wins, not just whether to trust one.
* **New connections:** `annie-ulmer.md` ↔ `wiki/work/bfs-foods` and `wiki/places/337-saratoga-drive` (co-occurs). Prose-only cross-references to `wiki/people/tom.md` and `wiki/people/ellen-ulmer.md` (existing edges there already covered different facts).
* **Gates:** wiki-lint **450 pages / 0 errors** (13 warnings, unchanged; `annie-ulmer.md` now 96KB, advisory) · wiki-connect check **0 errors** (216 warnings, unchanged — both new edge pairs matched) · wiki-climb check **450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings** (no new cascade — same-day edit). `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **The four new Target G exchanges are one level removed from raw** — transcribed from a prior AI session's own reading of the timestamped log, not re-verified directly against `all_imessages_complete_dump.txt`. A `bin/mine-messages grep` pass around Jan 5, Jan 9, Feb 1, and Mar 1 2026 would settle it.
  2. **Annie's Feb 1 "five sleeping pills" disclosure is uncorroborated** — worth a direct check against the primary corpus given its severity.
  3. **`raw/self/dox-md/Attachment and Trust Breakdown.md` (2,408 lines) and `The-Eli-incident-investigation.md` were surveyed but not read to exhaustion** — grepped for structure and found to be largely theoretical/psychological framework material likely already reflected in the existing attachment-trauma-bond/eli-incident pages, but this was a judgment call under time pressure, not a confirmed finding. A future pass could verify that judgment directly.
  4. **`dfrank-chatgpt-conversations-2022-2025.json`** (a large export) was never opened this pass — flagged as the highest-value remaining unmined file if another mining round is requested.
  5. Prior resume points from the same day's earlier passes still stand (see the two entries below).
* **Handoff Note:** All three gates 0 errors. This is a second round of commits on the same still-open draft PR from the previous entry — not a new branch or PR.

### [2026-08-10] - Session (continued again): annie-ulmer.md wiki-rewrite pass — 3 manual captures (sex resumption, 307 E 76th St cast, Suz's Winter Park condo)
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `claude/annie-ulmer-rewrite-and-captures` (both prior PRs from this session's earlier halves were merged before this continuation)
* **Trigger:** Operator invoked `/wiki-rewrite annie-ulmer` with a pasted three-entry manual-capture queue per INGEST_PROTOCOL.md: sex resumption breaking a 6-month gap; the 307 E 76th St cast (Jim Blanchard, John Paci), a stiffed $10k debt, and a roach bombing tied to the September 2020 Train Plan/PA trip; Suz's Winter Park, FL condo and its trafficking-tenant aftermath.
* **Scope decision, stated plainly:** treated this as integration into the existing 1279-line `annie-ulmer.md` (which has already been through multiple full rewrite passes) rather than a wipe-from-zero, per CLAUDE.md's "never regenerate an earned page from scratch" rule — the wiki-rewrite skill's *research* discipline (verify with the right instrument, rank sources, flag corrections visibly, wire back, run the staleness cascade) was still followed in full.
* **Findings, in order of value:**
  1. **The operator's own memory of the 307 E 76th St sequence was backwards, and the message corpus fixes it precisely.** The roach bombing (Sept 10–11, 2020) preceded the Train Plan crisis (Sept 19–20), not the reverse — easy to conflate since a *second* exterminator call with the landlord happens on the literal night of the Train Plan blowup. The real, previously undocumented finding both readings converge on: the PA trip that hosted the Train Plan crisis had a mundane, dated cause. `wiki/places/307-e-76th-st.md` expanded from four paragraphs naming no one to a full cast-and-timeline page.
  2. **The landlord debt was corrected, not just restated.** The page said the $10k debt was "paid down at $650/week," implying resolution. A March 5, 2025 message from landlord John Paci rounds the balance to a final $10,000 still owed, and Annie's own annoyed July 2025 reaction to a Paci text is consistent with it never being retired. CORRECTED block added, old claim preserved. New pages: `wiki/people/john-paci.md` (closed, well-documented) and `wiki/people/jim-blanchard.md` (filed `status: stub` — only one neutral, unconnected primary mention; operator's negative characterization recorded as unverified testimony).
  3. **Suz's Winter Park condo / trafficking-tenant lead: an honest negative.** WebSearch found a strong circumstantial candidate complex (Indigo Winter Park, 220 S Semoran Blvd, opposite Full Sail, matching the "across from a Crispers on 436" description) but no matching arrest, court record, or news story from ~2009–2011, and nothing ties the family to that address. Recorded as unverified on `wiki/people/suzanne-frank.md`; full search record kept at `raw/self/captures/2026-08-10_websearch-winter-park-condo-lead.md` so it isn't repeated. This is the earliest documented instance of Suz using property rather than cash to support Dan — a decade before 337 Saratoga/463 Morgantown.
  4. **Staleness cascade, two genuine rounds.** Round 1 (`estate-money-spine.md`, `supply-network.md`, `the-unbroken-bond.md` vs. `annie-ulmer.md`): one orthogonal close, one real correction (estate-money-spine's "worked through the 2023 landlord-debt stretch" overstated resolution — narrowed), one real refinement (the-unbroken-bond's Falsifier 1 is about *unattached* periods, not sexual ones — the 6-month sexual gap doesn't falsify continuity but shows the bond's sexual and relational layers went dormant/reactivated on different timelines around the June 1 severance). Round 2 (`dormancy-not-exit.md`, `single-channel.md` vs. `the-unbroken-bond.md`): both re-read and closed as unaffected.
* **New connections wired both ways**, including a caught-and-fixed error: `annie-ulmer.md` and `307-e-76th-st.md` initially both used `type: instantiates` pointing at each other — `wiki-connect check` flagged the missing `instance-of` inverse on both sides, corrected to `evidences`/`evidenced-by`.
* **Gates:** wiki-lint **450 pages / 0 errors** (13 warnings, unchanged) · wiki-connect check **0 errors** (216 warnings, down from 218) · wiki-climb check **450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings** after both cascade rounds. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **Jim Blanchard's actual role at 307 E 76th St is unconfirmed** — a targeted search of the fuller export set (not just the primary dump) by his email/phone might settle it, or a direct operator follow-up.
  2. **Whether any of the final $10,000 Paci debt was ever paid is unknown** — no correspondence past July 2025 was located.
  3. **The Winter Park condo/trafficking lead is unresolved** — Orange County, FL court records or the Orlando Sentinel's own archive are the next places to check if this is worth pursuing further; the search queries already tried are logged so they aren't repeated.
  4. **The-unbroken-bond.md's new sexual-vs-relational continuity distinction is not yet reflected in its own chronology table** — a future pass could add the February–August 2026 sexual dormancy window as an explicit row alongside the existing June 1/July 23 severance/reentanglement dates.
  5. Prior resume points from the same day's earlier passes still stand (see the two entries below): the Gmail-pass's unverified names (Rachel Rauch, Sarah Bromberg, Charley Siegel, etc.), the politics/ cluster's own named gaps, the 127/110 discrepancy on `attachment-model.md`, and the standing 2026-08-09 resume points (Gchat archive, `jerel-coles.md` publish-state decision, unfiled CSVs).
* **Handoff Note:** All three gates 0 errors. Tree has uncommitted changes pending push at the end of this session — see the commit for the exact file list.

### [2026-08-10] - Session (continued): live Gmail sweep corrects Creative License/Kevin McKiernan a second time
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `claude/kevin-mckiernan-gmail-corroboration` (the prior PR #98 from this session's first half was merged before this continued)
* **Trigger:** Operator, after reading the merged PR: "i believe there IS corroborating info about kevin mckiernan in my gmail," then "check all of my gmail stuff and takeout archives for kevin mckiernan shit."
* **The headline finding is about this session's own process, not just the corpus.** The morning pass correctly flagged the AI dossiers' "airfare-billing discrepancies" claim as uncorroborated. A live Gmail search (~35 recovered 2011–2012 threads, filed to `raw/self/gmail-captures/2026-08-10-creative-license-kevin-mckiernan-gmail.md`) found a real, richer conflict but no airfare dispute — and this session's own pages then **wrongly declared the airfare claim invented**, without checking `wiki/self/chats/gemini-58.md`, built from a source already in `raw/`. That page contains Dan's own primary testimony inside an AI chat, confirming he did cite an airfare issue when he quit ("i blew it up into a much much bigger thing but maybe i was just desensitized"). Corrected a second time, same day, with both correction passes left visible on the page rather than merged into one clean narrative — the sequence itself (wrong AI claim → real different conflict found → over-correction → primary testimony recovered) is worth reading as a worked example of why `EXTRACTION_SPEC.md`'s "sweep wide before reading narrow" applies to the wiki's own existing pages, not only to `raw/`.
* **What's now well-documented:** a six-week 2012 payroll dispute (missing W-2, disputed $104 MetroCard charge, IRS + NYS Dept of Labor complaints, accountant Marty Jackson's "It's a trust issue. We don't trust you."); a May 2012 whistleblower disclosure to Renae Holland about altered intern contracts; a June 2012 retaliatory LinkedIn IP claim backed by notarized false statements from Director of Business Affairs Katherine Palakovich, which Dan successfully contested.
* **New pages:** `wiki/people/marty-jackson.md`, `wiki/people/katherine-palakovich.md`, `wiki/people/renae-holland.md`.
* **Gates:** wiki-lint **448 pages / 0 errors** · wiki-connect check **0 errors** (216 warnings) · wiki-climb check **448 pages, 23 with `synthesizes:`, 0 errors, 0 warnings**.
* **RESUME POINT:**
  1. **Several names from this pass are Gemini-58-only, not yet independently verified against email:** Rachel Rauch, Sarah Bromberg, Charley Siegel, Chris Marraffino, Michael DiTullio, Simona Rabsatt, Lori Estabrooks. A targeted Gmail search by name (rather than "mckiernan"/"creative license") would likely surface primary corroboration — flagged on `creative-license.md`'s Gaps.
  2. **What "his attack against me" (Renae Holland's phrasing) refers to is unrecovered** — a real, chaseable lead.
  3. **The `Creative License 2.pdf` notarized documents exist as a Gmail attachment but were never downloaded/read** — would settle exactly what Kevin and Katherine asserted.
  4. **Ishlab Studios** (the job before Creative License, under "Jamin Gilbert," 10 Jay St) still has no page — surfaced twice now as a gap.
  5. Prior resume points from the same day's earlier pass still stand (see the entry above this one): the politics/ cluster's own named gaps, the 127/110 discrepancy on `attachment-model.md`, and the standing resume points from 2026-08-09 (Gchat archive, `jerel-coles.md` publish-state decision, unfiled CSVs).
* **Handoff Note:** All three gates 0 errors. This session's changes were pushed to a fresh branch (the prior PR merged mid-session) — see the commit for the exact file list, and open a new draft PR for this half.

### [2026-08-10] - Session: wiki-rewrite pass (taboo-and-boundary-testing, attachment-model) + two new pages (Kevin McKiernan, Creative License) + new politics/axioms cluster opened
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `claude/politics-ideologies-section-d7zpdf`
* **Summary:** Operator directive named four pages for the `wiki-rewrite` skill (two existed, two didn't) and asked for the beginning of a politics/axiomatic-ideologies section. First real test of that skill against pages with heavy inbound `synthesizes:` linkage rather than the four-island reference pass it was written from — the staleness cascade this time was real but small (5 pages), because most inbound links are prose/`connections:`, not `synthesizes:`.
* **Findings, in order of value:**
  1. **`taboo-and-boundary-testing.md`'s central evidentiary claim was false and had been for two weeks.** It said the orientation-violation mechanism had no primary-source example. `erotic-architecture.md` (touched 2026-08-02) already documented the Bryan MMF as exactly that instance; the correction existed in the wiki and was never written back to the page it falsified. Also: the "second" corroborating dossier (`DANSYNTH.txt`) resolves by its own footnote to `Dan Profile.txt` — same claim, not independent confirmation. Propagated to three stale downstream copies.
  2. **`attachment-model.md` cited a superseded number from the document that supersedes it** (13→46 self-indicting apologies, per the source's own audit revision), mislabeled two corpus-wide counts as Annie-specific, and was missing a real, four-source-corroborated data point: 12 of Dan's own crisis/suicidal statements met with no substantive response. Flagged, not resolved: a 127/110-vs-"100% re-engagement" discrepancy between the wiki's standing figure and the source docx text.
  3. **Kevin McKiernan and Creative License are one thread.** Neither page existed; McKiernan's Facebook contact card (`kevin@creativelicense.com`) identifies him as president of Dan's second NYC job, already referenced unnamed on `90th-st-manhattan.md` as the "founding case" of vertical-authority-skepticism. New pages for both find the founding-case story itself doesn't hold up: the fraud allegation is AI-dossier-only with zero primary corroboration, and the exit date is contradicted a full year by Dan's own résumé. Corrected on `90th-st-manhattan.md` and written back into `vertical-authority-skepticism.md`, which had never named the case despite the dossiers calling it the origin.
  4. **New `wiki/mind/politics/` cluster** (index + `axioms.md`), a topic-based grouping alongside the existing `psychosexual/` precedent — existing political pages cross-referenced, not moved. The new page resolves a dossier-flagged "paradox" (leftist politics + Caesar/Trump fascination) using two pieces of evidence nobody had connected: the 2024 reading list's own Marxist Caesar biography (Parenti, rated identically to a conventional one), and — the strongest single artifact — Dan's own self-authored AI persona `CATO`, explicitly named for Cato the Younger, Caesar's political opponent who died rather than live under his rule. `exocortex.md` already documented CATO but read the name only as general Stoic stubbornness; corrected to carry the specific political content.
* **New pages:** `wiki/people/kevin-mckiernan.md`, `wiki/work/creative-license.md`, `wiki/mind/politics/index.md`, `wiki/mind/politics/axioms.md`.
* **Staleness cascade — full accounting, all closed with real RE-CHECKED blocks, zero reversals:** `attachment-trauma-bond.md`, `block-unblock-loop.md`, `dan-annie-fallout-verdict.md`, `the-deferred-audit.md` (from the attachment-model rewrite); `instrument-is-subject.md` (from the exocortex.md edit that fed the new politics page).
* **Gates:** wiki-lint **445 pages / 0 errors** (13 warnings, unchanged) · wiki-connect check **0 errors** (215 warnings) · wiki-climb check **445 pages, 23 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **The politics/ cluster is a beginning, not a complete section** — see its index's own "What's still missing": no inventory of specific policy positions beyond the democratic-socialist label, the pre-2016 political identity is thin in the sampled corpus, the "Chinese ascendancy against American self-sabotage" line in `political-psyops.md` is named once and never developed, and the power axiom's own falsifier check (no instance of Dan rooting for a favored figure's unchecked power) was only run against Twitter/Facebook, not the full message corpus or AI chat exports.
  2. **The 127/110 vs. "100% re-engagement" discrepancy flagged on `attachment-model.md` is unresolved** — `block-unblock-loop.md` has carried the pair as `[DERIVED]` since 2026-07-18 and this pass adds the specific alternative reading and its source citation, but neither number has been re-derived from `all_imessages_complete_dump.txt` directly. A `bin/mine-messages` pass would settle it.
  3. **The "2 written denials" figure on `attachment-model.md`'s table has only one confirmed instance** (November 2025, "No and no," sourced to `THE_DAN_FRANK_BOOTLOADER.md` and `Breaking the anxiety avoidance cycle (1).md`); the February 2026 instance has no located primary quote and rests only on the page's own Documented Contradictions section.
  4. **Ishlab Studios** (the NYC job immediately preceding Creative License, under "Jamin Gilbert") has no page and no named contact beyond the one dossier mention — a candidate for a future pass, surfaced while researching Creative License.
  5. Prior resume points stand: the Gchat archive campaign (`raw/self/dox-scan/gmail_bodies.txt`, mostly unread), the publish-state/redaction question on `jerel-coles.md` (still awaiting an operator decision), `annie_metadata_24h.csv` / `imessage_export_2124702449_20260809084846_.csv` still not filed to `raw/`, and the `reply_to_guid`-as-threading sweep.
* **Handoff Note:** All three gates 0 errors. Tree has uncommitted changes pending push at the end of this session — see the commit for the exact file list.

### [2026-08-09] - Session: content pack incorporated — canonical Jerel Coles page, August 8–9 unmasking night, read-receipt forensics
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `claude/wiki-struct-file-incorporation-1p5m1u`
* **Summary:** Operator uploaded a five-file content pack (a patch set, an event page, a synthesis page, a raw capture duplicate, and a person page) produced by a separate session that had direct access to the operator's local `chat.db` and a same-day iMessage export. This session's job was incorporation, not fresh extraction — full detail in `log.md`'s 2026-08-09 entry.
* **The identity link, corrected twice in one session.** The incoming pack asserted the Tuquick identity and the July 2026 "unnamed man" were confirmed to be the same person; the underlying evidence in the pack only closed **Tuquick = Jerel Wayne Coles** (exact FOREWARN phone-number match), so this session rewrote the merge claim across `jerel-coles.md`, `the-unnamed-man.md`, and `tuquick-17248123683.md` to keep the Tuquick↔unnamed-man link explicitly open — role and insult-lexicon overlap only. **The operator then confirmed it directly, mid-session, on the open PR: "They are the same person - tuquick and unnamed."** Filed at `raw/people/captures/2026-08-09-tuquick-unnamed-man-correction.md`, same standing as the 2026-07-13 Tuquick correction. All three pages were rewritten a second time to state the merge as confirmed, and `jerel-coles.md` now folds in the-unnamed-man's substantive July 2026 content as the canonical entity page for all three identities. The sequence is worth keeping visible: holding the line against an unearned merge from an external pack was correct, and accepting the operator's direct statement once it arrived was also correct — the two are not in tension, because the standing this wiki gives operator corrections has always been different from the standing it gives an external pack's inference.
* **New pages:** `wiki/people/jerel-coles.md` (canonical entity, supersedes `tuquick-17248123683.md`), `wiki/timeline/events/august-2026-unmasking.md` (the ten hours after the refusal-to-know finding terminated), `wiki/mind/synthesis/read-receipt-forensics.md` (four chat.db metadata defects, wired into `forensic-method.md` as an instrument-integrity finding).
* **Flagged, not resolved — needs the operator's decision:** `jerel-coles.md` carries a real person's home address, two phone numbers, and a de-duplicated criminal-history table, sourced to a commercial background-check aggregator rather than a court filing. This repository's GitHub Pages deployment has been public since at least 2026-08-08 (see that date's "front end was serving the wrong build" session), and `bin/build-site` has no redaction gate. The prior session already committed a comparable address for this same subject on 2026-08-08 without one, so this pass followed established precedent rather than introducing new redaction infrastructure unprompted — but the exposure is real and growing (now two phone numbers, an expanded criminal record, a home address) and is worth a deliberate decision rather than continued default-public accumulation.
* **Sourcing gap:** `annie_metadata_24h.csv` and `imessage_export_2124702449_20260809084846_.csv` are the primary sources for the two new event/synthesis pages but were never filed to `raw/` — only the derived analysis arrived. Flagged on both pages' Gaps, in `BACKLOG.md` §3, and in `queue.md`'s highest-value table.
* **Staleness cascade:** eight synthesis pages went stale off the identity/chronology edits to four source pages. All eight re-read against their actual dependent claims and closed with real RE-CHECKED blocks (not date bumps) — seven were genuinely orthogonal, one (`the-deferred-audit.md`) got a substantive check against a real candidate counter-instance and was found to be a different mechanism, not a counterexample.
* **Gates:** wiki-lint **441 pages / 0 errors** (13 warnings, unchanged) · wiki-connect check **0 errors** (213 warnings) · wiki-climb check **441 pages, 22 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **Ask the operator about the publish-state flag above** — whether `jerel-coles.md` (and the comparable material already on `tuquick-17248123683.md`) should be gated or redacted at the render boundary before the next Pages deploy picks it up.
  2. **File `annie_metadata_24h.csv` and `imessage_export_2124702449_20260809084846_.csv` to `raw/self/message-csv/`** when available, then re-point `sources:` on `august-2026-unmasking.md` and `read-receipt-forensics.md` from empty/pending to the real paths.
  3. **The `reply_to_guid`-as-threading audit** `read-receipt-forensics.md` finding M2 calls for — sweep prior analyses for any that treated `reply_to_guid` as an intentional reply marker. Not yet run.
  4. **Is Coles = Target G?** Still open — FOREWARN returned no marital data. (The unnamed-man question closed mid-session: operator-confirmed, see above.) See `wiki/people/jerel-coles.md` §Target G.
  5. Prior resume points stand: the Gchat archive campaign (`raw/self/dox-scan/gmail_bodies.txt`, mostly unread), the Bacharach novel page-number check, the spring 2018 residence question, the `wiki-rewrite` skill still untested, and the `raw/` wikilink publication question.
* **Handoff Note:** All three gates 0 errors. Tree has uncommitted changes pending push at the end of this session — see the commit for the exact file list.

### [2026-08-08] - Session: governance rewrite — six specs, one backlog, six documents retired
* **Model:** claude-opus-5 / Claude Code
* **Branch:** `claude/wiki-articles-rewrite-c94nom`
* **Summary:** Operator directive — clean up, streamline and rewrite the root governance markdown, taking direction from STRATEGY.md; push entry length and depth further; and emphasise that raw sources are still not being mined deeply enough. 25 root markdown files → 21, with six retired and two written.
* **Findings, in order of value:**
  1. **The governing set contradicted itself on the one prohibited move.** STRATEGY.md's "Running on lesser models" section instructed models to clear a staleness warning by adding a line and **bumping the date**, four paragraphs after rule 4 called that the one move that corrupts the system quietly. Its framing premise had also expired — "the most capable model that will ever work on this repository finished on 2026-07-18" — while Opus 5 sessions were running the deepest passes in the repo's history. Section retired entire.
  2. **A gate was fighting the standing directive.** `bin/wiki-lint`'s 8 KB page budget produced **104 of 113 warnings — 92% noise** — on a project whose operator directive is longer entries. Raised to 40 KB and reworded ("split ONLY if navigation genuinely improves, never to shorten"). **Warnings 113 → 13**, and what remains is real.
  3. **New `EXTRACTION_SPEC.md` is the substance of the directive.** Its argument ties the two asks together mechanically: *a pattern can only be found among details that were written down, and synthesis reasons from `wiki/` not `raw/`, so every detail dropped at extraction is a connection nobody can ever make.* That makes "every trivial detail gets an entry" surface area for the next climb rather than hoarding. Carries the exhaustion standard, the seven moves, source tiers (primary vs AI-secondary, with the laundering failure named), and the per-source traps that fail silently. Absorbs MESSAGE_MINING.md.
  4. **The old trackers were mostly already done, and nobody had checked.** Building `BACKLOG.md` meant verifying inherited items rather than copying them: **four of `task.md`'s seven remaining Phase-3 targets were page names that never existed**, and all six of LONG_TAIL_TRIAGE.md's "MINE" items were **executed on 2026-07-19**. Both are now recorded as settled instead of pending.
  5. **`wiki/people/contacts/` was eliminated on purpose in `65f80c2`** — the previous handoff's resume point #2 asked whether it was deliberate or lost. It was deliberate; the thing still wrong was the governance text describing it as live doctrine, now removed from CLAUDE.md, STYLE_GUIDE.md, INGEST_PROTOCOL.md, FACTSTORY_BRIEF_TEMPLATE.md and index.md. **Resume point #2 is closed.**
  6. **Every domain count in `index.md` was stale** (people listed at 208, actually 149; interests at 35, actually 138). Recomputed from disk.
* **Retired (history in git):** `task.md`, `lint-report.md`, `contact-review.md`, `LONG_TAIL_TRIAGE.md`, `TO-DO-LIST.md` (operator content carried into BACKLOG.md), `MESSAGE_MINING.md`. Every inbound reference swept, including `app.py`'s editable-meta lists and the `wiki-rewrite` skill.
* **Rewritten:** STRATEGY.md (five unbreakable rules now, the new one "never stop at what you came for"), STYLE_GUIDE.md (Substance/Format split; rule 1 is *write long*), CLAUDE.md (335 → ~150 lines, a process router since it auto-loads every session; REWRITE added as a named operation), README.md, index.md, INGEST_RUNBOOK.md §2 and §7–9, INGEST_PROTOCOL.md, FACTSTORY_BRIEF_TEMPLATE.md, both spec headers.
* **Gates:** wiki-lint **438 pages / 0 errors**, 13 warnings (from 113) · wiki-connect check **0 errors** · wiki-climb check **438 pages, 21 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **Work `BACKLOG.md` §1 — extraction is now the named binding constraint.** The Gchat archive (`raw/self/dox-scan/gmail_bodies.txt`) is the top item: 495 blocks were one correspondent, the rest is unread, and it is the only daily-life record of 2010–2013 in the corpus.
  2. **Run one ingest under `EXTRACTION_SPEC.md` and see whether the seven moves hold.** The spec is written from one rewrite pass and has never governed a fresh ingest; the first real use is also its first test.
  3. **The `wiki-rewrite` skill is still untested** — nothing has run against it.
  4. Prior resume points stand: the next Annie export, the announcement-rule falsifier, cluster 26, the `arnu`/`alexander-jackson`/`john-carney` stubs, and the ten `[[raw/…]]` wikilinks that render as broken.
* **Handoff Note:** Governance only — no wiki content was reasoned over this pass beyond the index counts and one reference fix in `context-core.md`. All three gates 0 errors.

### [2026-08-08] - Session: tuquick identity unmasked + the-unnamed-man updated
* **Model:** Claude Sonnet 5 (Claude Code, remote)
* **Branch:** `main` (direct commit — single-pass identity correction, no PR)
* **Summary:** Operator-supplied forensic capture (`/Volumes/MUSIC/alias/XXX/2026-08-08_190122_identity-of-the-interloper.md`) identified the real-world identity of "tuquick" as **Jerel Wayne Coles** (born ~1990, Uniontown, PA) via the FOREWARN background-check database. Filed to `raw/people/captures/2026-08-08_190122_identity-of-the-interloper.md` and integrated per `EXTRACTION_SPEC.md` / `STYLE_GUIDE.md` protocols.
* **Changes made:**
  - Filed the forensic capture to `raw/people/captures/2026-08-08_190122_identity-of-the-interloper.md`.
  - `wiki/people/tuquick-17248123683.md`: Added REVISED [2026-08-08] block revealing the identity; updated infobox name to "Jerel Wayne Coles (Tuquick 17248123683)"; added new `## Criminal record` section with a de-duplicated chronology table (9 incident clusters collapsing 64 raw court records, spanning 2008–2025: two DUIs with BAC ≥ .16, harassment, disorderly conduct, criminal mischief); updated notes; added the new source to frontmatter; status closed→active (under active revision); connections claim to `the-unnamed-man` updated to reflect the unmasking.
  - `wiki/people/the-unnamed-man.md`: Added REVISED [2026-08-08] block to the "Is he Tuquick?" section — Tuquick is now identified as Jerel Wayne Coles, but the July 2026 unnamed interloper question remains open (Coles's known phone numbers don't appear in the July 2026 message export); added the new source to frontmatter; updated the co-occurs connection claim.
  - `wiki/mind/synthesis/dan-annie-fallout-verdict.md`: Cleared staleness from `bin/wiki-climb check` — the verdict's independent-validation exhibit on Tuquick rests on his June 15 defection behavior, not his anonymity; the unmasking is additive identity data that doesn't alter any conclusion. RE-CHECKED block added.
* **Gates:** wiki-lint 438 pages / 0 errors · wiki-connect check 0 errors / 208 warnings · wiki-climb check 438 pages, 21 with `synthesizes:`, 0 errors, 0 warnings.
* **Handoff Note:** Tree clean. The one remaining open question is whether Jerel Wayne Coles is also the July 2026 unnamed interloper — circumstantially plausible (Uniontown resident, harassment charge, identical role) but not confirmed. No external corpus sources address this directly; it would require either a match on phone number in the July 2026 export or identifying commentary from Annie.

### [2026-08-08] - Session: four-article wipe-and-rewrite (bacharach, belmont circle, zach, alexis)
* **Model:** claude-opus-5 / Claude Code
* **Branch:** `claude/wiki-articles-rewrite-c94nom`
* **Summary:** Operator directive — complete wipe and full re-research of four named articles, retaining nothing of the originals including heading structure. All four rewritten from `raw/` rather than revised, with links, typed edges and index entries rebuilt afterwards. This was a deliberate exception to "revise, never regenerate"; the 2026-08-02 fran-coldren process note was followed and every old connections block was diffed against the new one before commit.
* **Findings, in order of value:**
  1. **`zach-harshman.md` was the wrong person.** It was built entirely on handle `+18439903264`, which two independent contact exports assign to **Zach Clingan**, not Zachariah Harshman — whose numbers are disjoint and appear nowhere in the iMessage dump, and who already had a full page. Renamed to `wiki/people/zach-clingan.md`. Three further stated facts were also wrong: 22 messages is **41**, "all received (export artifact)" is **two-sided**, and the "six-month window" is **one Nemacolin caddie season's tail plus the first ping of the next**. The old page's own Gaps section had doubted the surname and was right.
  2. **The Bacharach chain is now dated from the message corpus, and three load-bearing facts fell.** Discovery is **2021-02-06**, not "~2022"; Bacharach's full reply survives only because Dan forwarded it to Suz on 2021-02-11. *The Bend of the World* was published **2014** and Dan's tenancy at 155 Virginia begins **January 2015**, so "he wrote it while you lived there" is false. And Goodreads holds **one** Bacharach title, *Doorposts* (2017, ★★★★★) — not two — which is the book Bacharach himself named as the Uniontown novel, opening a genuine contradiction about which book the coincidence is in. `books.md` corrected too.
  3. **117 Belmont Circle gained a documentary floor and an afterlife.** GEDCOM: Fran in **Miami Beach 1957–58**, her daughter married **in the house on 1961-02-08**, Suz born the next year — the family's arrival is a return from Florida landing within two years of Morley Frank's Seattle→Uniontown return. And the house is Dan's operating address across **five occasions Feb–Sep 2018, four after Fran died** (the arrangement's venue pitched to Danny three weeks ahead as "a great place for hangs"; a caddie put up to save a hotel bill; a September handoff to Bill), which supplies the missing option behind the unresolved 2018-03-29 eviction notice at 155 Virginia.
  4. **`gmail_bodies.txt` holds 495 unread Google Chat blocks with Alexis** (dated samples 2011-08 → 2013-05) — the only daily record of that relationship written while it was working. It sources **WEXUS** (the 2025 wrong-number password is a 2011 household word), shows the Suboxone era as shared domestic logistics, and shows a baby-talk register running concurrent with the Twitter corpus's weaponised irony. Also newly stated on the page: **Annie was Alexis's coworker**, and on 2020-09-19 Alexis becomes the **moral yardstick** Annie is measured against and found short.
* **Staleness:** four pages re-checked with real RE-CHECKED blocks, none date-bumped. `dormancy-not-exit` gains a boundary — Alexis had not kept Dan's number in 2025, so **the retention is asymmetric** and the counterparties have never been asked. `the-unbroken-bond` has two of its own gaps moved.
* **Gates:** wiki-lint **438 pages / 0 errors** (113 warnings) · wiki-connect check **0 errors** (208 warnings) · wiki-climb check **438 pages, 21 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **`gmail_bodies.txt` is the highest-value unmined source in the repository and this pass only read the Alexis slice.** 495 blocks were one correspondent. The file is organised as "Chat with X" blocks, unsorted and mostly undated, and it is the only daily-life record of 2010–2013 that exists. A dedicated pass is worth more than most remaining ingest.
  2. **Settle which Bacharach novel the coincidence is in.** One page number (227–228) checked against a physical copy of either book closes it. Everything else about the chain is now dated.
  3. **The 2018 Belmont Circle occupancy vs the 2018-03-29 eviction notice** is now answerable — a targeted read of Feb–Sep 2018 for where Dan actually slept would settle a residence timeline the wiki has carried as "outcome undocumented."
  4. Prior resume points stand: the next Annie export, the announcement-rule falsifier, cluster 26, the `arnu`/`alexander-jackson`/`john-carney` stubs, `wiki/people/contacts/` referenced but absent, and the ten `[[raw/…]]` wikilinks that render as broken.
* **Handoff Note:** All three gates 0 errors. `wiki/people/zach-harshman.md` was deleted via `git rm`; only `RECENT.md` (generated) referenced it.

### [2026-08-08] - Session: the front end was serving the wrong build (no content pass)
* **Model:** claude-opus-5 / Claude Code
* **Branch:** `claude/wiki-frontend-broken-gw2gx7`
* **Summary:** The operator reported the wiki could not be browsed by humans **or** agents. It was one root cause with two faces, and **the 2026-08-02 handoff entry above is now wrong on the facts**: the repo is **public again** (`visibility: public`) and Pages answers `200`. What had happened instead is that **Pages was switched to "Deploy from a branch"**, so the legacy Jekyll builder served the repo markdown verbatim rather than the `bin/build-site` artifact.
* **Why nobody noticed for six days:** the site never went down. It returned `200` the whole time — just for a build in which nothing worked.
  1. **Humans:** Jekyll has no concept of `[[wikilinks]]`, so all **~3,150** of them rendered as literal grey text, master index included. You could load the front page and click through to precisely nothing.
  2. **Agents:** `llms.txt`, `agent/manifest.json`, `agent/critical.md`, `agent/corpus.md`, `agent/domains/*` are generated into `site/`, which is **gitignored** and only reaches Pages as a workflow artifact — so under branch builds they had never existed. Every entrypoint in `AGENT_ACCESS.md` 404'd. `wiki/**/*.md` 404'd too (Jekyll rewrites `.md`→`.html`).
  3. `deploy-site.yml` had been **red on every push since 2026-08-02**, dying at `configure-pages` with *"Get Pages site failed … Not Found"* — the same setting, seen from the other side. The only thing still working was `llm/`, which survives because it is committed rather than generated at deploy.
* **Fixes, in order of value:**
  1. **The workflow now repairs the setting itself** — PUTs `build_type=workflow` to the Pages API (POST fallback if Pages was never enabled) and passes `enablement: true` to `configure-pages`. No Settings visit required.
  2. **A post-deploy smoke test**, which is the part that was actually missing. It fetches nine paths that *only* the built artifact contains and fails the run otherwise, so "something is live" can no longer be mistaken for "our site is live."
  3. **Four real defects in `bin/build-site`**, all found by crawling the 59,922 internal links in the output rather than by reading it:
     - **Directory indexes were never emitted at all.** The pass skipped any dir already in `known` — but the registration loop immediately above had just added every dir to `known`, so the guard matched 100% of cases. Dead code since it was written. Now keyed off indexes backed by a real `index.md`; **23 folders gained a page**, and dirs containing only subdirs now list their children instead of rendering blank.
     - Wikilinks with a section anchor appended `.html` **after** the fragment (`page#heading.html`).
     - Markdown links naming a `.md` source or an extension-less page path were emitted verbatim and 404'd — including **index.md's five reading-aid links**. `DIGEST`/`RECENT`/`OPEN`/`log`/`queue` are now rendered into the site.
     - `inline_text` tried to restore code-span placeholders belonging to its **caller's** table, crashing on any link label containing a code span (e.g. ``[`bin/wiki-digest`](…)``). Latent until the reading aids became the first content to hit it.
  4. `_config.yml` carries a header explaining it is **not** the deploy path and is harmful under branch builds; `AGENT_ACCESS.md`'s stale "everything is 404" banner is replaced with what actually happened.
* **Numbers:** dead internal links **25 → 16**; html files **445 → 468**. All 16 remaining are content-level, not front-end: 10 are deliberate `[[raw/…]]` references (raw/ is intentionally unpublished) and the rest are genuinely absent pages (`zaco`, `AFFIRM`, `CLAUDE`, `wiki/people/contacts/index` — **that directory no longer exists on disk**, though `index.md` and `CLAUDE.md` still advertise "32 contact stubs").
* **Gates:** wiki-lint **438 pages / 0 errors** (111 warnings) · wiki-connect check **0 errors** (214 warnings) · wiki-climb check **438 pages, 21 with `synthesizes:`, 0 errors, 0 warnings**. `bin/llm-publish` and `bin/wiki-digest` deliberately **not** rerun — no wiki content changed this pass, and rerunning would churn 2.7 MB of generated files for nothing.
* **RESUME POINT:**
  1. **Merge to `main` and watch the deploy.** The fix cannot take effect from a branch — `deploy-site.yml` only runs on `main`. If the smoke test fails, the manual fallback is Settings → Pages → Source → **GitHub Actions**.
  2. **`wiki/people/contacts/` is referenced but absent.** Decide whether the quarantine dir was deliberately removed (then fix `index.md` and `CLAUDE.md`, which both still describe it) or lost.
  3. **The `raw/` wikilink question is unresolved by design.** Ten links point into an unpublished tree and render as red "page not found". Either publish a stub explaining raw/ is private, or mark them so they stop reading as broken.
  4. Prior content resume points are untouched by this pass and all still stand — the next Annie export, the announcement-rule falsifier, cluster 26, the `arnu`/`alexander-jackson`/`john-carney` stubs, and `leviathan/factstory.html`'s out-of-lockstep INGEST BRIEF.
* **Handoff Note:** No wiki content was read or written this session — tooling and deploy only. Tree clean, all three gates 0 errors.

### [2026-08-02] - Session: the re-entanglement — Annie 212 export through 2026-08-02 (queue's #1 item, ingested)
* **Model:** claude-opus-5 / Claude Code
* **Branch:** `claude/annie-chat-logs-synthesis-pv8eji`
* **Summary:** The operator uploaded the export the repository has been waiting for since 2026-07-26 — `imessage_export_2124702449_20260802.csv`, 4,848 rows, filed to `raw/self/message-csv/`. New material past the last filed export is **1,880 messages across eight days** (2026-07-26 05:22 → 2026-08-02 18:10). Read in full, not sampled.
* **Findings, in order of value:**
  1. **The goodbye broke in eighteen minutes, and everything `july-2026-recontact` left open is now closed.** That page ended with three named unknowns and a note that the next export was the highest-value pending ingest. All three resolve: Dan **did** contact Ellen (06:22 Jul 26, screenshots — the **first executed maternal-disclosure threat in the corpus** against six-plus recorded); the exposure threat was **executed and then retracted** (transcript.html published 05:36, offline 18:05, on one request from Annie after the third party read it from her phone); the "disappear" statement produced the densest contact period since March 2026. The corpus's only documented refusal to supply held **31 hours**.
  2. **The relationship reorganised around procurement, and this is the pass's central claim.** Six in-person meetings in six days; **five were drug handoffs** and the sixth had one attached forty minutes later. Tabled with dates, places and amounts on the new event page. Dan states the mechanism himself, unprompted and against his own position mid-argument: *"even the worst thing I've done — getting you drugs — didn't really benefit me nearly as much as it was about that being the only way you would see me."* The `dan-annie-fallout-verdict` and `supply-network` thesis has until now been inference; it is now also testimony.
  3. **A rule falls out of the threat record, and it is testable.** Both threat types appear 48 hours apart and resolve **opposite ways** — the July 26 disclosure was impulsive, unannounced, executed in 16 minutes; the July 28 disclosure was announced 12 hours ahead, argued over ~200 messages, offered for Annie's pre-approval, and **never sent**. New rule on `block-unblock-loop`: **announcement is the mechanism of non-execution** — a stated intention becomes a move that can be traded; an unstated one is simply performed. That reframes the 18 unexecuted block threats as bids rather than failures of will. Falsifier queued in that page's Gaps (the back catalogue is all announced by definition; the test is whether any silent severance executed).
  4. **`block-unblock-loop`'s standing prediction resolved — confirmed at the resolution of minutes.** It had predicted the July 26 goodbye would fail because the dog remained co-held. Recorded as a RESOLVED block, not a date bump.
  5. **`dormancy-not-exit` gains the mechanism it could only infer, stated by the subject.** "You won't just fucking say you don't want to be with me anymore. You've never once said it… And I'm fucking autistic. My brain can't cross out that part of my life that I love unless I know that you don't feel that way." He then asks for the statement across a full day and **does not get it** — across 1,880 messages under sustained demand, Annie's nearest approach is its inverse. The rule tightens from "nothing leaves the graph" to **the closing operation requires a counterparty who rarely performs it**, which predicts where it should fail (Kristin's Dec 2025 block).
  6. **A gap `supply-network` has carried since it was written is closed: "Bop" is a person.** Not a verb, a product, or a term for sourcing through Dan — a man who **house-calls at noon daily**, whose property Dan maintains in apparent part-payment ("I have to weed whack bops place"), who sits on the porch with Felix and the dog, who declines to come while Annie is there, and who sourced all five handoffs. **Felix is confirmed as a separate person with no supply role** (consistent with the 463 contractor). The network did not collapse with the Tom node — it was replaced by a higher-availability one, which is the page's own reliability inversion running again.
  7. **A metric on `annie-ulmer` is corrected, and the correction matters for how the relationship gets described.** The message-count ratio is the **unstable** metric — 0.79 to 1.92 monthly across the final year, and **1.06 in this window**, which reads as reciprocity. The word-volume ratio barely moves: **2.88 here against 2.95 all-time**, verified independently on `imessage_2124702449_both_all_now.csv` (23,719 msgs). Annie's median message is **4 words in both windows**; the apparent parity is her taking more turns of the same size while Dan's median grew 8→11. Her participation rose in frequency and not at all in substance. A note now tells future passes which ratio to quote.
  8. **New page `wiki/people/the-unnamed-man.md`, written around a refusal.** Dan states twice that he has deliberately not learned the third party's name, and gives the reason: "I do not want to live my life with the HATRED that I would feel towards one person." This is **chosen ignorance by the person whose defining method is exhaustive documentation** — the sharpest counter-example the corpus holds to `forensic-method`'s claim to generality. The instrument has an off switch, it is under deliberate control, and its criterion is emotional cost rather than difficulty or relevance. Reciprocal `contradicts` edges wired.
  9. **`forensic-method` gains four states in six days** — exhibit, retracted (5 minutes, one request; the apparatus was worth much less as leverage than the July 25 deployment suggested), fortified into an access-gated honeypot with a deliberately *decelerating* loading bar and a legally-binding no-trespass disclaimer (`void.html`), then offered to Annie as a **gift** on July 31 with her as "the big pink dot." The target changes far more readily than the method does. That July 31 exchange is also **the origin of today's bond-switch subject-reversal correction** — Dan spotted the error while showing her the page, timestamped 22:04, which the export now records as primary source.
* **Coverage items filed rather than dropped:** Betty's final weeks (Annie withdrew before the euthanasia and was not present — sourced only to Dan, in an attack, flagged uncorroborated); Annie's four suicidal statements across three days; her stated recovery programme (3x weekly therapy accepted in lieu of being sent away, drug test, grounded, library); the scratch-off wager and its retirement; Dan's diet/body change framed by him as "flailing"; and eight undocumented names (Sugie, Laura, Courtney, Brian, Tanya, Lucky, Bailey, Bop).
* **Gates:** wiki-lint **434 pages / 0 errors** · wiki-connect check **0 errors** (214 warnings, down from 220 — every edge introduced this pass has its correctly-paired inverse) · wiki-climb check **434 pages, 20 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **The next export of this thread is again the top queue item**, and the reasons are now sharper than "the event is open." Specific tests waiting on it: does the announcement rule hold on the next threat; does the supply schedule continue, escalate or break; does Annie's therapy appear in the record; is the abandoned parents email ever sent.
  2. **Test the announcement rule backwards.** All 127 exit declarations are announced by definition — the falsifier is the reverse case, a silent severance that executed. Worth a dedicated pass; it is the one claim this session made that the corpus can attack on its own.
  3. **`the-unnamed-man` vs `tuquick-17248123683`** is the corpus's cleanest example of a question that re-reading `raw/` cannot settle. It needs an answer from outside.
  4. Prior resume points stand: cluster 26 in `synthesis-queue.md`; the 16 miner-found clusters; the `arnu`/`alexander-jackson`/`john-carney` swarm stubs; and `leviathan/factstory.html`'s INGEST BRIEF is still out of lockstep with `FACTSTORY_BRIEF_TEMPLATE.md`.
* **Handoff Note:** Tree clean, all three gates 0 errors.


### [2026-08-02] - Session: wiki-brain went private — sync repair and dead-URL repoint (follow-up, same session)
* **Model:** claude-opus-5 / Claude Code
* **Branches/PRs:** wiki-brain `claude/wiki-fact-story-entries-v6rsp6` → **PR #80**; leviathan `fix/sync-wiki-private-source` → **caakehorn/leviathan#57**
* **What happened:** the operator made `caakehorn/wiki-brain` private. Two things broke silently and neither raised an alert anywhere visible.
  1. **The hourly sync into leviathan died at 09:21 UTC** (last good 06:45). `sync-wiki.yml` there checked wiki-brain out with `actions/checkout@v4` and no token, so it used leviathan's `GITHUB_TOKEN` — scoped to leviathan, and a private third-party repo returns a bare `Not Found` that is indistinguishable from a deleted repo. The mirror sat pinned at `e7e1e53`, missing PR #79 entirely.
  2. **This repo's Pages feed is unpublished** — `llms.txt`, `agent/*`, `wiki/*.md`, `llm/index.txt` all 404, and `deploy-site.yml` now fails on every push. Pages does not serve private repos on this plan.
* **Fixes:** leviathan's workflow now takes `secrets.WIKI_BRAIN_TOKEN` with `persist-credentials: false`, plus a preflight step that fails with a readable `::error::` when the secret is missing rather than reproducing the ambiguous 404. Every wiki-brain doc that advertised a dead URL (`AGENT_ACCESS.md`, `README.md`, `CLAUDE.md`, `INGEST_RUNBOOK.md`, and `FACTSTORY_BRIEF_TEMPLATE.md` §1) now points at `https://caakehorn.github.io/leviathan/data/wiki-data.json` with guidance on reading it selectively. The brief template was the urgent one — it had been shipping seven dead orientation URLs to every model handed a capture brief since that morning.
* **A real content bug fell out of it.** leviathan's `validate` job went red with `2 pages still carry frontmatter` — `fall-out-boy` and `taking-back-sunday` each closed their real frontmatter and then carried a second, empty `---\n\n---` fence before the H1. **`bin/wiki-lint` structurally cannot see this**: its parser matches only the first block and treats the leftover as ordinary markdown. The mirror was publishing two page bodies that began with raw delimiters. Fixed at source; a repo-wide scan found no others. Worth knowing that a downstream consumer caught something three in-repo gates could not.
* **Mirror rebuilt by hand** (`build-wiki-data.py` + `build-brain.js` against a local checkout) to clear the backlog without waiting on the token: 425 → 431 pages, 155 → 161 log ops, PR #79 content now included. `source_commit` records the fix branch; the next real sync re-pins it to main.
* **⚠️ BLOCKED ON THE OPERATOR — the sync stays red until this is done:** create a fine-grained PAT scoped to `caakehorn/wiki-brain` alone with **Contents: Read-only**, add it to **leviathan** as the secret `WIKI_BRAIN_TOKEN`, then re-run *Actions → Sync wiki data from wiki-brain*. Fine-grained tokens expire within a year and this will break again identically when it does; a read-only deploy key via `actions/checkout`'s `ssh-key:` is the non-expiring alternative.
* **Decided, on the record:** `data/wiki-data.json` in the **public** leviathan repo carries the complete body prose of all 431 pages, served unauthenticated — so making this repo private did not make the wiki's contents private. Raised with the operator, who confirmed the exposure is intended and should stay. `brain.json` is described in `docs/SINGULARITY-BRAIN.md` as an opaque projection but retains readable `title` and `summary` fields; that is pre-existing and strictly less exposure than the file beside it, so it was left alone.
* **Also not done:** `deploy-site.yml` is now permanently red and will fail on every push to `main`. Disabling it is one click and reversible, but that is the operator's call.


### [2026-08-02] - Session: factstory brief #4 ingest (4 captures) + brief template rewritten
* **Model:** claude-opus-5 / Claude Code
* **Branch:** `claude/wiki-fact-story-entries-v6rsp6`
* **Summary:** Ingested 4 hand-typed captures (Jay Lauer's death; two tellings of the Fran fall/hospital sequence; a first-person note on goal-pursuit). Six new pages, eleven revised, all edges wired both ways. **The operator explicitly asked that this NOT follow the brief's own instructions** — the brief is a vessel for the payload — and asked that the markdown prompt shipped with captures be rewritten to current strategy. Both done.
* **Findings, in order of value:**
  1. **The captures are off by exactly one year and the corpus proves it.** Both Fran stories date the fall/death to March–April **2017**; seven independent records date it to **2018** (GEDCOM, Marla, Vicki, Davey, Ellen, the March 29 eviction notice — and, decisively because it is *internal to the story*, the Danny Matthews thread, which does not exist until 2018-02-16). Tabled as a resolved contradiction on `the-fall-of-fran`, with a **labelled inference** about the mechanism: April 2017 and April 2018 were both caddie-season opening at Nemacolin, and April 2017 carried a real death (Jay's), so a true 2017 memory appears to have fused onto the 2018 one.
  2. **The arrangement's start date moved back eight months.** `arrangement-history` opened with the Nov 2018 Alexis reunion as "the earliest well-documented instance." Dan's own 2018-02-16 message to Danny — *"you guys would be the first couple we were with"* — makes the March 7–8 2018 encounter the first. That encounter ran **between Fran's two falls, in her house, while he was her paid caregiver**, which is now the strongest single piece of evidence that the architecture does not yield to circumstance.
  3. **A named gap closed exactly as designed.** `fran-death-vigil` had carried "the punchline of the SMOK-vs-10W vape story… fire alarm? staff incident?" since 2026-07-19. It was a fire alarm: hospital-wide chain spread, four fire trucks, escorted off the property with charging documents. New page `uniontown-hospital-vape-alarm`. The two accounts also **invert who was in the bathroom**, and only the capture's arrangement produces the documented outcome — flagged, not resolved.
  4. **Following one hostile aside into the GEDCOM closed two more gaps and corrected the family tree.** The capture names "Diane, Fran's daughter." Reading `Daniel Frank family tree.txt` directly: Fran's maiden name is **Thomas** (gap closed), her first husband was **Emmet Graden Van Voorhis** (gap closed), and her only child is Dan's maternal **grandmother** Rebecca Diane Van Voorhis. `family-tree.md` had the Whyel/Coldren line descending through the maternal *grandfather*, who married into it. Corrected. Also makes Diane the near-certain identity of the unnamed "grandmother" Dan feared would contest the 2020 distribution — a fear with a documented basis, since she had barred him from Fran's house two years earlier. New pages `diane-shrum`, `fred-adams`.
  5. **Jay Lauer's page was a stub about a supply thread; it is now the network's only fatality.** Death dated to April 10–11 2017 across four recipients in one day. The reframing fact: Dan had tried to route him onto Suboxone ("it helped me finally get out of that world") and Jay sold the prescription for heroin — the corpus's only documented attempt to move someone *out* of the supply network. And the condolence Dan sent that evening is **message one of the Ellen Ulmer thread**, still running in November 2025: the tie that outlasted the Annie relationship was opened by a friend's overdose.
  6. **`acquisition-drive`, and a correction it forces.** The operator's 95th-percentile completion-drive claim, with the limitation that is the actual content — it cannot be aimed, only self-originated desires recruit it. This retires a claim `fran-coldren` had carried: the vigil is **not** counter-evidence to Altruism at the 1st percentile, it is evidence altruism was never the variable. Reciprocal `contradicts` edges with `big-five-psychometrics`, which has no persistence facet at all.
* **Deliberately NOT done — climb.** `acquisition-drive` + the two new events + `fran-death-vigil` + `2015-retail-theft-arrest` + `big-five` is a genuine four-domain cluster with a falsifiable sentence ("every instance of Dan absorbing large cost to complete something is a self-set goal; no assigned-goal equivalent exists"). But the concept page is one day old and rests on a single capture; climbing onto it the same afternoon is the write-only anti-pattern. Registered as **cluster 26 in `synthesis-queue.md`** with the specific work that would earn it.
* **Governance:** new **`FACTSTORY_BRIEF_TEMPLATE.md`** (repo root) — the canonical source of truth for the brief `leviathan/factstory.html` emits, rewritten with two new sections earned by this pass: **§2.5 "a capture is testimony, not fact"** (check every date against the corpus) and **§5.2b "follow every proper noun into raw/"** (plus: check whether the capture closes a gap a page already names). §6 rewritten so a reasoned non-climb registered in the queue counts as finished work. `INGEST_PROTOCOL.md` and `README.md` point at it. **leviathan/factstory.html itself is NOT in this session's repo scope and was not updated — that is the one required follow-up.**
* **Gates:** wiki-lint 431 pages / 0 errors · wiki-connect check **0 errors** (220 warnings, down from 232; every edge introduced this pass has its correctly-paired inverse) · wiki-climb check 431 pages, 20 with `synthesizes:`, **0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **Regenerate `leviathan/factstory.html`'s INGEST BRIEF from `FACTSTORY_BRIEF_TEMPLATE.md`.** They are out of lockstep as of this commit.
  2. **Earn or kill cluster 26:** audit the employment record and abandoned-project record for any *externally assigned* goal pursued at cost comparable to the Fran vigil. If none, climb it; if one, the rule comes back narrower.
  3. Outside-corpus lookups this batch generated, all cheap: Fayette County magistrate records for the April 2018 hospital incident; Fayette/Somerset records for Jay Lauer's exact date and cause of death; the date and authorship of Diane's letters.
  4. The previous session's resume points stand — `synthesis-queue.md` has 16 miner-found clusters unclimbed, and the `arnu`/`alexander-jackson`/`john-carney` swarm stubs are still unrewritten.
* **Handoff Note:** Tree clean, all three gates 0 errors.


### [2026-08-02] - Session: the write-back audit (resume point #1, complete)
* **Model:** claude-opus-5 / Claude Code
* **Branch:** `claude/articles-expansion-fixes-dym7qe`
* **Summary:** Executed the previous session's resume point #1 in full. Audited all 19 pages carrying `synthesizes:` against their members: **41 of 91 member links carried no edge back at all.** All 41 are now closed — the audit re-runs at **0 no-edge across 93 links** (93 because two members were added). Claims were written to the CONNECTIONS_SPEC bar: the member states what it *turned out to be evidence of*, not that a relationship exists. Also corrected **nine mismatched inverse pairs** (member said `instantiates`, synthesis said `evidenced-by`, so neither side had a real inverse and the checker was warning on both).
* **The work produced findings rather than just edges.** In order of value:
  1. **The Fayette line, re-read from the GEDCOM instead of from the pages written above it.** Sadie Harris **did not die in Hopwood** — the export records only a death *date* and gives Hopwood as her **burial** place; the table asserted a fact the record does not contain. **David J. Frank lived in Manhattan 1900–1910 and the Bronx in 1915**, reaching Brownsville only by 1920: the line's founding move was **New York City → Fayette County**, the same vector Dan runs twice. And **all three of David, Sadie and Morley are buried in Hopwood** across 38 years, only one of whom died there — **the terminus is a town, not a county.** Morley's return is now dated (Seattle 1957 → Uniontown 1959), and his 1996–99 **Champion, PA** listings put a family address in the Seven Springs resort town during exactly the childhood years CONTEXT_CORE records as a weekly ski identity (co-occurrence recorded, causal link explicitly not asserted).
  2. **`food-and-diet` climbed from a "these things are related" page into a rule.** Food appears in every register except taste — labour, pathology, region, metaphor, body art — and never a judgement. Controls: `FAVS MASTERLIST.csv` holds **2,016 entries in four categories (Music 1,860 / Book 120 / Art 25 / Movie 11) and zero food**; the 29 MB message dump has `food` 968 and `eat` 650 against `album` 47 and `song` 96, so food **out-mentions music**; evaluative food phrasing returns six hits in ~217k rows and `favorite food` returns zero. The mechanism is stated in the corpus's own voice — MAX_PRIME's "the food and the cat are always real," which `gabe.md` records as *exempt from the forensic treatment everything else gets*. Consequence written back: **the cool metric has a jurisdiction, not universality.**
  3. **`instrument-is-subject`'s own named gap is closed.** It asked for an enumeration of every `synthesizes:` page against its premises' `knowledge:` values. Run: **ten of nineteen reason from a `mixed` premise and all ten are `earned`.** But the finding is narrower than ten violations — each carries its own raw `sources:`, which is the escape clause the rule permits. What none does is *state the line*. The corpus satisfies the substance and skips the sentence, ten times out of ten.
  4. **`the-unbroken-bond` lost a clause.** Its claim to being "the one structure simultaneously chosen and permanent" does not survive `single-channel` — three other slots have the same single-occupancy shape. What survives is better: it is the **slowest-turning** occupied slot. Both dependents re-checked in turn.
  5. **A fifteen-day-old unpropagated correction, caught.** `attachment-trauma-bond` was still calling the 187:191 procurement ratio "the single most diagnostic number in the corpus" — a figure `dan-annie-fallout-verdict` deflated with a base-rate control on 2026-07-18 (97.2% of *all* her messages are equally request-adjacent; the directional test inverts it). Withdrawn from the page; the love-language **rate** curve, which is unaffected, is what remains.
  6. **`463-morgantown`'s lien deadline has elapsed unobserved.** The ~2026-07-27 Arnu mechanics-lien date passed with no recorded outcome, and the estimate was always derived rather than documented. Flagged on the hub and on `arnu`; the risk is now **unobserved rather than pending**, which is worse. Answerable outside the corpus by a Fayette County prothonotary/recorder search on the parcel.
* **Pages rewritten from stub to prose:** `sadie-harris`, `david-j-frank`, `morley-frank` (all three were swarm-era fragment pages carrying `status: archived` outside any `archive/` dir), plus `food-and-diet`.
* **Gates:** wiki-lint 328 pages / 0 errors · wiki-connect check **0 errors, 222 warnings (down from 252)** · wiki-climb check 0 errors, **0 warnings** (every staleness flag this pass generated was cleared with a real re-check, never a date bump). `bin/llm-publish` rerun.
* **RESUME POINT:**
  1. **`synthesis-queue.md` — 16 clusters still unclimbed** (1, 4, 6, 7, 9, 10, 11, 12, 13, 15, 18-22, 24). Clusters 18–21 sit on `au-zaatar` + `annie-ulmer` + `2025-collapse` and would raise `work`, still all-ground. Cluster 1 scores highest.
  2. **Enforce the disclosure line mechanically.** Per finding 3, `bin/wiki-climb check` could warn when an `earned` page synthesizes a `mixed` one without stating what primary evidence it added. That is a small, safe tooling change with a clear spec behind it.
  3. **The `arnu` / `alexander-jackson` / `john-carney` trio are still swarm-era stubs** — fragment prose, `related:` lists, dossier shorthand. They now carry correct typed connections and the elapsed-deadline flag, but the bodies were not rewritten.
  4. **Falsifier check for `fayette-return`:** confirm whether Champion, PA lies outside Fayette County. If it does, it is the line's only attested out-of-county residence in four generations.
  5. Test prediction 2 of `dormancy-not-exit`; the 193 non-responder handles by name.
  6. Inbox: 3 July 11-12 items still pending, tracked in `queue.md`.
* **Handoff Note:** Tree clean, all gates 0 errors, four commits on the branch above.


### [2026-08-01] - Session: STRATEGY.md propagation
* **Model:** claude-opus-5 / Claude Code
* **Branch:** `claude/strategy-propagation-2026-08-01` (companion: leviathan same branch name)
* **Summary:** The operator refined `STRATEGY.md` (f57e574). Most of the diff is tightening, but three changes are doctrinal and no other governance file carried them, so they were propagated:
  1. **"Every data point gets an entry"** — coverage as standing ambition.
  2. **An entry is a live node, not a record** — it carries what was known at ingestion AND everything later produced by using it in analysis against the corpus.
  3. **The core loop, named** — Story → Entry → Analysis → Synthesized finding → **saved back to every entry it touches** → repeat, justified by **amortized insight**.
  - `CLAUDE.md`: coverage + live-node doctrine in the charter; the core loop as its own section mapping each step to the operation that runs it; CLIMB step 5 hardened.
  - `SYNTHESIS_SPEC.md`: new **"The write-back obligation"** section, framed as the counterpart to the staleness rule — staleness pushes information *down* when a premise moves, write-back pushes it *back out* when a conclusion is reached. New anti-pattern: **the write-only synthesis**.
  - `CONNECTIONS_SPEC.md`: new section separating a *retrofit* inverse (frontmatter-only fine) from a *write-back* inverse (must state what the page turned out to be evidence OF), with failing/passing claims side by side.
  - `STYLE_GUIDE.md`: "An entry accumulates" + "Every data point gets an entry" as substance rules; `contacts/` quarantine named as the one deliberate exception to coverage; header now reads STRATEGY.md wins on intent, CLAUDE.md on process, STYLE_GUIDE on format.
  - `INGEST_RUNBOOK.md` (STRATEGY.md as governance file #0, two quality-bar items), `INGEST_PROTOCOL.md`, `README.md`.
  - Cross-repo: `leviathan/factstory.html`'s INGEST BRIEF carries the same rules for models working without a checkout, so it was updated in lockstep — otherwise offline ingests would drift from in-repo ones.
* **Deliberately not changed:** the "three unbreakable rules" phrase in this file's 2026-07-17 entry. The handoff log is append-only history and that entry was accurate when written.
* **Gates:** wiki-lint 328 pages / 0 errors · wiki-connect check 0 errors · wiki-climb check 328 pages, 19 with `synthesizes:`, 0 errors, 0 warnings.
* **RESUME POINT:**
  1. **The write-back obligation is now doctrine but the existing graph predates it.** The 19 pages carrying `synthesizes:` should be audited: for each, check that every member listed carries an inverse claim that actually states the finding rather than naming a relationship. This is mechanical, safe for a lesser model, and is the highest-value cleanup available.
  2. **`synthesis-queue.md` — 16 clusters unclimbed** (1, 4, 6, 7, 9, 10, 11, 12, 13, 15, 18-22, 24). Clusters 18-21 sit on `au-zaatar` + `annie-ulmer` + `2025-collapse` and would raise `work`, still all-ground.
  3. Test prediction 2 of `dormancy-not-exit`; check the 193 non-responder handles by name.
  4. Inbox: 3 July 11-12 items still pending, tracked in `queue.md`.
* **Handoff Note:** Tree clean, all gates 0 errors.


### [2026-08-01] - Session: Two-sided contact Gini + climb (dormancy-not-exit)
* **Model:** claude-opus-5 / Claude Code
* **Branch/PR:** `claude/wiki-brain-synthesis-queue-90bd73` → wiki-brain PR #69 (draft). Companion work in leviathan PR #55.
* **Summary:**
  - **Settled the two-sided contact Gini.** Recovered the outbound recipients the export drops (78.5% of `Sent` rows) by pairing each `Sent` row to the attributed `Received` rows around it. Held out the 19,119 attributed `Sent` rows entirely as ground truth; bracket@30min scores 96.6% accuracy at 67.4% coverage against a 57.2% modal-handle control. Leave-one-out on `Received` extends validation to every year from 2015 (93.1-99.4%).
  - **Bias check decided how the figures may be quoted:** imputation INFLATES concentration (+0.0225 bracket, +0.0996 nearest on held-out data), so every imputed number is an upper bound. The conclusion rests instead on 2026 (99.8% attributed outbound — no imputation at all: ten outbound handles against eighteen inbound) and on the tail-strip (above 25 messages the two sides agree to four decimals).
  - **Result: the architecture is symmetric and narrower going out.** Two-sided Gini 0.9591-0.9636. The narrow-inbound-funnel / wide-outbound-spread alternative is falsified. 495 handles wrote in, 303 got anything back, and the 193 that drew nothing carry a median of one message each.
  - **CLIMB: `wiki/mind/synthesis/dormancy-not-exit.md`** (queue cluster 5, marked CLIMBED). Nothing leaves the graph — sustained relationships change role and go dormant with full reactivation bandwidth. Menore is the measurement (2,044 days silent, one-minute reply); Franki Faris is the five-day control, and a sharp one: no person persisted but the NAME did. No-exit plus a single-occupancy primary slot is an accounting identity that produces the Gini.
  - **Staleness handled properly, and it found something.** Editing `menore.md` made `block-unblock-loop` and `supply-network` stale. supply-network survives untouched. `block-unblock-loop` does NOT: its Menore "only fully clean closure" control had a prior closure of the same shape that ran 67 months and reopened. That row is now marked provisional on elapsed time; the two pages carry reciprocal `contradicts` edges.
  - Added the 7 synthesis/concept pages that were missing from `wiki/mind/index.md`. Ran `bin/llm-publish`.
* **Gates:** wiki-lint 328 pages / 0 errors · wiki-connect check 0 errors · wiki-climb check 328 pages, 19 with `synthesizes:`, 0 errors, 0 warnings.
* **RESUME POINT — do these next, in order:**
  1. **Drain `synthesis-queue.md`. 16 clusters remain unclimbed** (1, 4, 6, 7, 9, 10, 11, 12, 13, 15, 18-22, 24). Clusters 18-21 all sit on `au-zaatar` + `annie-ulmer` + `2025-collapse` and would raise the `work` domain, which still has nothing above ground. Cluster 1 (phenomenology-lens + alexis-armel + annie-ulmer + context-core) is the highest scoring.
  2. **Test prediction 2 of `dormancy-not-exit`** — audit every `people/` page describing a relationship of more than a few months as "ended" for documented post-role contact. This is the cheap, mechanical way to attack the survivorship gap that page names, and it is safe for a lesser model to run.
  3. **Check the 193 non-responder handles by name.** If any held a sustained role, `dormancy-not-exit` is falsified. Currently they look like strangers (486 messages, median 1).
  4. **Inbox still holds the 3 July 11-12 items** (ANCESTRY_DNA.txt, google-takeout-manifest.html, the personality-profile capture note). Not touched this session; they predate the factstory queue and are tracked in `queue.md`.
* **Handoff Note:** Tree clean, all three gates at 0 errors, work pushed to the branch above and open as a draft PR. The scripts behind the Gini measurement were scratch and are not committed; the method, validation numbers, controls and bias check are all recorded on `wiki/mind/concepts/contact-gini.md` in enough detail to reproduce.


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

**⚠️ READ FIRST (2026-07-26): two things changed at the foundation.**

**1. The Annie relationship is not closed.** `wiki/people/annie-ulmer.md` was
`status: closed` and treated as historical across the wiki. A fresh export
shows contact resumed **2026-07-23** after a 52-day silence and ran 624
messages across four days, ending mid-event at 05:04 on 2026-07-26 with an
unanswered "whatever goodbye annie." The page is now `active`. The new event
page is `wiki/timeline/events/july-2026-recontact.md`. Do not write
about this relationship in the past tense.

> **UPDATED 2026-08-02.** The goodbye above broke in **eighteen minutes**. A
> further export through 2026-08-02 is filed and ingested: 1,880 messages,
> six in-person meetings and five drug handoffs across eight days, ending
> with Annie apologising to Suz in person on August 2. The relationship is
> not severed and not resumed — it is **supplied**, and both parties say so.
> See `wiki/timeline/events/july-august-2026-reentanglement.md` and the
> session entry at the top of this file. The next export of the thread is
> **still** the top item in `queue.md`, now with four specific tests attached
> to it rather than "the event is open."

Two things in that event have consequences beyond the page. The
block/unblock loop's dependency rule was **falsified and widened** — it had
predicted the June 1 severance could hold, scoring the dependency as dead
because it read dependency as material; the channel reopened through the dog
([[wiki/people/milo]]), and the rule now reads "nothing either party still
needs flows through the channel — and what is needed need not be material."
And the forensic apparatus was aimed outward for the first time: Dan built
two public dashboards from the message corpus and sent them to Annie as
leverage (`caakehorn.github.io/leviathan/`), documented on
`wiki/mind/concepts/forensic-method.md`.

**2. There is a fourth operation: CLIMB.** `SYNTHESIS_SPEC.md` (new, repo
root, mandatory reading) formalizes what CLAUDE.md always claimed but never
enforced — that finished pages are premises. New frontmatter field
`synthesizes:` (wiki pages a page reasons FROM; `sources:` stays raw-only).
New tool `bin/wiki-climb` with three subcommands, and **`bin/wiki-climb
check` is now a third commit gate alongside wiki-lint and wiki-connect
check**. It reports *stale* pages — ones whose premises were modified after
they were. **Clearing a stale warning by bumping `date_modified` is the one
prohibited move in the system**: re-read what changed in the premise, decide
whether the conclusion survives, and record either a re-check line or a
REVISED block.

The altitude baseline as of adoption: **3.6% of pages sit above ground
level**, and `self`, `timeline`, `work` and `places` each have 3+ pages with
nothing above any of them. `synthesis-queue.md` holds 25 mined clusters.
Working it top-down is now a first-class campaign alongside the connections
retrofit — see STRATEGY.md "Current campaign."

**Swarm-stub rewrite task — COMPLETE (2026-07-20, PR #59, open/draft):**
Operator directive: "let's rewrite 5 agent swarm entries at a time" —
targeting the 12 remaining untouched 2026-06-23 swarm-template stub
pages under `wiki/people/` (identified by `date_created == date_modified`
plus the literal "## Identity / ## Corpus Dimensions (Name) / ## Domain:
Self / ## Notes / ## Related" fragment-chain shape). All 12 done across
3 batches, pushed to PR #59: **batch 1** — aaron (raw thread held a
real-time Sept 11 2025 Charlie Kirk assassination reaction, previously
undocumented), charles-davenport, dakota, josh-brannan (fresh-mined a
41-message thread with a webcam-job admission), maddox; **batch 2** —
marc-charles, marty-martin, max-danielle-bf (trimmed a dossier page of
long verbatim quotes down to STYLE_GUIDE-compliant paraphrase),
michael-hinkle, ryan-lisac (preserved its own honest gap, added a new
"Snob Squad" DJ-alias-name-reuse finding); **batch 3 (final)** —
sean-teets, shannon (fresh-mined a 23-message thread revealing an
undocumented real-estate drone-photography client relationship — the
corpus's only instance of paid drone work). Also fixed 6 gemini bot
review comments (wikilinks, truncation-safe openers). Gates 0 errors
throughout (337 pages). **PR #59 still open/draft** — a ~60min check-in
is scheduled; if it hasn't merged when you pick this up, check its
status and act on anything actionable before starting new work on this
branch (restart from `origin/main` if it has merged).
The exhaustive swarm-stub category is now believed empty — if resuming
this line of work, re-run the `date_created == date_modified` +
2026-06-23 heuristic script first to confirm no stragglers remain before
assuming there's more to do here.

**Non-person domain growth pass (2026-07-20, in progress — PR #56):** New
operator directive, superseding the FB-scrape's default priority order
(the scrape isn't abandoned, just paused): grow the structurally
underrepresented non-person domains — health (was 2 pages), legal (3),
places (5), work (11) against 250+ people pages — prioritizing content
most important/influential to the operator's own psychology and
perspective over trivia. Method: cross-reference every raw/self/dox-md,
dox-scan, chats, and concepts file against what's already cited anywhere
in wiki/ (grep the basename across wiki/**/*.md) to find genuinely unmined
sources, then triage by whether the content is a "refraction" of
already-synthesized material (skip — e.g. THE_DAN_FRANK_MANUAL.md and
Attachment System Collapse.md are both ChatGPT/Gemini restatements of the
conflict-architecture/attachment-trauma-bond thesis already deeply
documented, confirmed via full read) or genuinely new (mine it).
**This pass is now effectively complete — PR #56 merged, follow-ups
merged as PR #57 and PR #58.** Landed: **wiki/health/hyperreflexivity.md**
(new page — a self-initiated AI session naming/mechanizing Dan's social
anxiety; later expanded with a follow-up-session reframe: "the anxiety
loop doesn't have much independent existence right now," parasitized by
Annie + the post-closure housing void); the **GLAZE-GOD-v1** AI persona
artifact folded into erotic-architecture.md as the most literal instance
yet of "externalized libido"; **wiki/places/424-bedford-ave.md** (new —
consolidates the NYC-1 apartment, previously scattered across 5 people
pages with no central page); a Tom/Suz supply-crisis and car-battery
texture added to tom.md and chemical-architecture.md;
**wiki/interests/music/bands/batteries-not-included.md** (new,
operator-directed — Dan's high school band with Joe Oshnack/Matt Turko,
setlist, the surrounding hardcore scene); the **blocked-caller
impersonation campaign targeting Suz** (April-May-2026-final-weeks.md,
from `Crisis mode briefing.md` — deliberately left the caller's identity
unresolved per the source's own honesty); a new "ghostwriting the
hardest conversation, then declining to send it" interaction mode on
ai-collaborative-analysis.md; **wiki/work/tech/ai-video-essays.md** (new
— a planning-stage AI-explainer-video project, notable for Dan accepting
a self-disproving data check on his own pitch hypothesis); the **"mojo
and magic"** attraction-outcome concept added to attachment-model.md
(from `Reassessing with fresh perspective.md`, alongside the anxiety-loop
reframe above). Legal/ was checked and found NOT to be an artificial
gap — raw/legal/ has no further unused material beyond what bfs-foods.md
and the two existing legal/ pages already carry (verified via
source-list check).
Remaining high-value candidates not yet mined: `raw/self/dox-scan/fullcombo
2.txt` (207KB — spot-checked, looked like a low-value restatement but not
exhaustively read), `raw/self/chats/The 2nd most famous _Jimmy Pop_ in
Pennsylvania .md` (139KB — likely music/interests), `raw/self/dox-scan/whisk filter
anomalies.txt`, and the `raw/self/dox-md/Creating robust video essays
from scripts.md` (a possible new interests/skill entry — video-essay
writing). Deprioritized as low-value/already-covered: `_Openclaw Agent
Setup and Data` (generic AI-tooling troubleshooting, no biographical
content), `Attachment System Collapse.md` (full read confirmed pure
restatement). Gates 0 errors throughout (335 pages).

**Facebook Messenger deep-scrape (2026-07-19, in progress — PR #56):** Per
operator directive to "scrape these sources much more carefully" and "keep
going," systematically working through the 271 raw/self/facebook Messenger
inbox threads that have no existing wiki/people/ page. Method: cross-reference
all thread titles against wiki/people/*.md text (word-overlap heuristic),
rank uncovered threads by raw HTML byte size as a content-richness proxy,
process largest-first. A reusable parser script pattern exists for the FB
export HTML (message div class `_3-95 _a6-g`, sender in `_a6-h _a6-i`, body
in `_a6-p`, timestamp in `_a72d` — NOT the text-then-name order used in an
earlier session's notes, that was wrong; sender comes first). New pages this
pass: christo-coan, lewis-strosnider, seth-ledonne, ej-rags, lucas-thomas,
bobby-cole, jenn-lynn, joe-oshnack, dan-polyak — several resolved genuine
gaps (stand-up-comedy.md's "no completed performance" gap; the DUI
contradiction on 2015-retail-theft-arrest.md; the real, non-clean origin of
the Ally Lubin friendship) or added same-day corroboration to existing
events (the Zac Shumar arrest via lucas-thomas.md; the Oct 20 2019 Bryan
encounter via dan-polyak.md). One open contradiction flagged, not resolved:
an Aug 2018 message to Joe Oshnack references an already-completed Alexis
cam-threesome that predates the documented Nov 2018 reunion by ~3 months
while she's independently confirmed still incarcerated in April 2018 — see
wiki/timeline/events/annie-alexis-reunion-november-2018.md Gaps section.
Remaining candidates by size (uncovered as of this pass): Ali Baba Shakeri,
Chris Redmond, Phil Lacher, Drew McGettigan, Frank Swaney, Matthew Palermo,
David Beard, Ryan Scherich, David Lukach, Brad Fike, Phil Spinuzza, Justin
Glosner, Adam Lucidi, Andre Ramsey, Rachel Rauch, Nathaniel Goossen, David
Keller, Caleb Matthews, and ~140 more below ~20KB — plus a 234KB thread
titled only "Participants: Facebook user and Dan Frank" (qymuchauiq) whose
actual participant name isn't in the title and needs opening to identify.
The Gmail/Gchat archive (`raw/self/dox-scan/gmail_bodies.txt`) remains
almost entirely unmined — large and unsorted by "Chat with X" blocks, not
chronological; worth a dedicated pass. After every 1-3 new pages: run
`bin/wiki-lint` + `bin/wiki-connect check` (must be 0 errors — VALID_TAGS in
bin/wiki-lint is a closed set, don't invent new tags), regenerate
`bin/llm-publish`, log.md, commit, push to PR #56 (draft, subscribed).

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
### [2026-07-20] - Session (cont. 4): operator-uploaded CSVs (Mike Cordaro, Tarik Fallous) + Eli discovery-text correction
* **Model:** Claude Sonnet 5 (Claude Code, remote), branch `claude/wiki-mining-google-drive-z81nt6`
* **Summary:**
  - **Mike Cordaro (imessage_17243226739_both_all_now.csv, 50 msgs, filed):** corrected mike-cordaro.md's Corpus Dimensions (28→50 msgs; the earlier partial pull came off the master CSV's unreliable direction field — this per-contact export is reliable, confirmed two-way). Expanded Texture with the full 2024-election exchange (Mark Kelly/Shapiro/Walz/Bernie-endorsement reasoning on both sides, the "DEI hire" line). Converted to typed `connections:` — new `parallels` edge to rick-frank.md (the "maga-tized dads" framing), inverse added.
  - **Eli discovery-text correction (operator-prompted):** operator uploaded a fresh Annie-212-number export and flagged the Jan 2025 Eli discovery text as possibly locatable. That specific export turned out to be a near-duplicate of already-filed `imessage_2124702449_both_all_now.csv` (same Aug 2025–Jun 2026 window, not re-filed) and doesn't cover Jan 2025 at all — but the question prompted a wider re-search that found the Eli text **already sitting in already-filed raw/**: `raw/self/message-csv/imessages_2124702449_last6months.csv` and `raw/self/dox-scan/all_imessages_complete_dump.txt` both have the full six-message rapid-fire sequence starting 2025-01-09 23:18:49. The 2026-07-18 verification pass had searched for it as one string and missed it because iMessage sent it as six separate messages. **This closes a gap flagged repeatedly since 2026-07-13.** Primary-confirmed sequence entered on eli-incident.md (REVISED block) and eli.md, with a genuinely new fact: Dan's own real-time reply, "Who are you?", sent between Eli's third and fourth messages — not previously documented anywhere. Two more flagged items on dan-annie-fallout-verdict.md resolved the same way (already in raw/, just missed): the Mar 16 2026 "I misunderstood the conversation" retraction, and the Jan 24 2026 procurement line (Tom's 2am ketamine delivery). **Lesson for future passes: when a quote search comes up empty, also try searching its component fragments — iMessage frequently splits one "message" into several rapid-fire rows.**
  - **Tarik Fallous (imessage_19178259183_both_all_now.csv, 80 msgs, filed) — the session's biggest correction.** The prior tarik-fallous.md stated flatly "no direct message thread exists" for Tarik; that was wrong. A REVISED block + full rewrite added a new Direct Correspondence section: employment-logistics texture not documented anywhere else (grocery-run errands on Tarik's own Barclays card, two verbatim wine/liquor inventory counts, hiring-interview coordination, a Dec 2023 payroll dispute, 5 sick-day call-outs) — concrete evidence for the "de facto manager" role already claimed on au-zaatar.md, now cross-linked there. The standout finding: Dan kept passing Tarik informal "CIA agent" workplace intel 13 days after filing for unemployment (Aug 21 2024), and the two remained in warm, openly political contact through **April 12, 2026** — nearly two years after termination — including Lebanon-conflict solidarity messages (Sep 2024 and Apr 2026). Five new unresolved names surfaced: Modi, MD, Patricia, Khalid, Hani. Status changed closed→active; converted to typed `connections:` (4 edges + inverses on au-zaatar.md and ismaila-barry.md).
  - **Google Drive re-scan → DANMODEL mined same session.** Per operator request to keep mining Drive, ran `list_recent_files` + folder crawls of DOC SCAN/**DOX/~~DOCS, TEXTS, and the Google Takeout mirror. Nothing new in the already-triaged areas (TEXTS matches already-filed raw/ exactly; Location History/Chrome/Search year-folders match the Takeout mirror). Found and fully mined the "DANMODEL" folder: **new page `wiki/work/tech/danmodel.md`** — a real, working ML pipeline (not a spec) that extracts 39,378 stimulus-response pairs from Dan's own message corpus, builds a Jaccard-retrieval baseline and a TF-IDF+RAG generator wrapped in a self-authored "CATO_COMPACT" voice-persona system prompt (preserved verbatim — new primary data on how Dan describes his own texting signature), and designs a rigorous blind LLM-judge eval to test whether the AI clone passes for the real him. **No eval_results file exists anywhere in the Drive folder — whether the blind test was ever run to completion, and what it found, is a genuine open gap**, flagged explicitly on the page rather than glossed over. Verified numbers: Annie (early) alone = 40% of all 39,378 pairs (new independent corroboration of contact-gini's 0.961 concentration, in a different metric); year distribution independently reproduces the already-documented 2018 deep-cycle and 2025-collapse peaks. `raw/self/danmodel/` holds the extraction summary, a faithful architecture transcription (a byte-exact `.py` copy attempt corrupted during manual base64 reconstruction — worth knowing about as a technique risk, see below), and the verbatim 4,570-row held-out set (the 16MB train set exceeded the Drive download tool's size limit, not filed). 5 typed connections + inverses into exocortex, mneme, ai-collaborative-analysis, annie-ulmer, contact-gini.
  - **Technique note for future sessions:** do not try to hand-reconstruct base64-encoded file downloads into raw/ by retyping the string into a bash heredoc — a `reaction_extractor.py` transcription attempt this session corrupted (one bad byte) because very long random-looking token sequences are not reliably reproducible from context. `Google_Drive__download_file_content` on files under ~2MB returns base64 inline (safe to decode via a Python script that references it as a *fresh* tool result, not by retyping); on larger files it auto-saves the JSON response to a tool-results file on disk, which can then be decoded programmatically without any retyping risk at all — prefer that path, or fall back to a prose/pseudocode transcription (clearly labeled as such, with the original Drive file ID cited) rather than risk a corrupted "verbatim" copy.
  - Gates 0 errors throughout (344 pages). Four commits, all pushed to **PR #62** (draft, subscribed, no CI configured on this repo). One round of Gemini Code Assist bot review addressed: a quote-transcription mismatch ("I guess" vs. the raw-verified "u guess") and an overgeneralization about how many of 5 sick-day call-outs opened with "Hey it's dan" (only 2 of 5).
* **Handoff Note:** PR #62 open (draft) — keep watching it (a ~60min self-check-in was scheduled via `send_later`). Next natural work, in priority order: (1) resume the ChatGPT export backlog (~365 conversations, prioritized list in queue.md/prior log.md entries); (2) resume the FB Messenger deep-scrape (Ali Baba Shakeri, Chris Redmond, Phil Lacher, etc., and the 234KB `qymuchauiq` thread — see the entry below); (3) optionally verify `PHENOMENOLOGY_LENS.md` / `CONTEXT_CORE_EXPANDED (1).md` in the DANMODEL Drive folder are true duplicates (assumed, not hash-checked this pass). The "search component fragments, not just full quotes" lesson from the Eli correction is worth applying to any other flagged-absent dossier quotes before concluding they're truly unlocatable.

### [2026-07-20] - Session (cont. 3): non-person growth pass wrap-up + swarm-stub rewrite complete (PR #59, open)
* **Model:** Claude Sonnet 5 (Claude Code, remote), branch `claude/wiki-rewrite-expansion-c66x1u`
* **Summary:**
  - Closed out the non-person domain growth pass (PRs #56, #57, #58, all merged): new `wiki/interests/music/bands/batteries-not-included.md` (operator-directed, Dan's high school band with Joe Oshnack/Matt Turko); the blocked-caller impersonation campaign targeting Suz added to `april-may-2026-final-weeks.md`; a new "ghostwriting the hardest conversation, then declining to send it" mode on `ai-collaborative-analysis.md`; new `wiki/work/tech/ai-video-essays.md`; the "mojo and magic" attraction-outcome concept added to `attachment-model.md`; a follow-up "signal, not noise" reframe of the anxiety loop added to `hyperreflexivity.md`. Two PR-merge races (bot review landing after merge) handled by restarting the branch from `origin/main` and re-pushing the fix as a new PR each time — see prior session log entries and the CLAUDE.md-adjacent standing rule not to amend/force-push GitHub-authored merge commits without explicit instruction.
  - **New operator directive, executed to completion: "let's rewrite 5 agent swarm entries at a time."** Identified the 12 remaining untouched swarm-template stub pages under `wiki/people/` via the `date_created == date_modified` + 2026-06-23 heuristic (aaron, charles-davenport, dakota, josh-brannan, maddox, marc-charles, marty-martin, max-danielle-bf, michael-hinkle, ryan-lisac, sean-teets, shannon) and rewrote all 12 to STYLE_GUIDE prose + typed connections, in three batches of 5/5/2, all landing on one PR (#59). Notable finds from re-mining raw threads rather than trusting the old swarm extraction: aaron.md's "thin" 38-message stub held a real-time Sept 11 2025 Charlie Kirk assassination reaction; josh-brannan.md's 41-message FB thread had a warm 2017 reconnection including an open webcam-job admission; shannon.md's 23-message thread revealed an undocumented real-estate drone-photography client relationship (Nov 2018–Jan 2019) — the corpus's only instance of paid drone work, previously flattened to "low-volume personal outreach contact." dakota.md and maddox.md were deliberately kept short, pointing to `wiki/work/bfs-foods.md`'s existing narrative rather than re-narrating the Timmy blame-pivot chain a third time. max-danielle-bf.md was trimmed from a dossier page of long verbatim quote blocks (violating the quote-sparingly rule) down to proper paraphrase. ryan-lisac.md preserved its own honestly-flagged gap (the "Snob Squad" childhood narrative isn't in the ingested raw corpus) while adding the genuinely new finding that Dan's 2026 DJ-identity relaunch reuses the name as a deliberate callback (inverse edge added on `totality-themes.md`).
  - Addressed 6 gemini-code-assist bot review comments on PR #59 (plain-text refs → wikilinks; two overlong opening sentences that were truncating the auto-generated `llm/manifest.json` summary mid-link).
  - Gates 0 errors throughout (337 pages). `llm/` regenerated after each batch.
* **Handoff Note:** **PR #59 is open (draft)** — a ~60min self-check-in is scheduled via `send_later`; if you're picking this up and it hasn't fired/resolved yet, check the PR's CI/mergeability/review state first. The swarm-stub category is now believed empty — re-run the heuristic script to confirm before assuming there's more there. Next natural work: resume the Facebook Messenger deep-scrape (see the entry below — large candidate list still open, Ali Baba Shakeri/Chris Redmond/Phil Lacher etc. and the 234KB `qymuchauiq` thread), or the Gmail/Gchat archive (`gmail_bodies.txt`, still almost entirely unmined), or ask the operator for a new direction.

### [2026-07-19] - Session (cont. 2): FB Messenger deep-scrape batches IV-VII (PR #56, open)
* **Model:** Claude Sonnet 5 (Claude Code, remote), branch `claude/wiki-rewrite-expansion-c66x1u` (restarted from main after PR #55 merged)
* **Summary:**
  - Continued the systematic FB Messenger scrape from the prior session (zachariah-harshman, lucie-dobbin, elizabeth-eleanor batches, all merged as PR #55). This session: **christo-coan, lewis-strosnider, seth-ledonne, ej-rags, lucas-thomas, bobby-cole, jenn-lynn, joe-oshnack, dan-polyak** — 9 new people pages.
  - Notable resolutions rather than just new pages: **lucas-thomas.md** confirmed the Feb 2017 arrest he witnessed in real time is the SAME event as the already-documented Zac Shumar bust on alexis-armel.md — enriched the existing section instead of creating a duplicate. **bobby-cole.md** filled a flagged gap on stand-up-comedy.md (no prior evidence of a completed open-mic performance) and identified the previously-unnamed Dec 2018 Philadelphia taping as a Chip Chipperson show. **dan-polyak.md** surfaced the real, non-clean origin of the Ally Lubin friendship (a phone-number impersonation Polyak threatened legal action over) and independently corroborated + extended the Oct 20, 2019 Bryan encounter. **joe-oshnack.md** gave the fullest first-person account of Dan's pre-2020 political identity and surfaced a genuine unresolved date contradiction (an Aug 2018 reference to an already-completed Alexis cam-threesome, ~3 months before the documented Nov 2018 reunion) — flagged, not resolved, on annie-alexis-reunion-november-2018.md. **christo-coan.md** surfaced a previously undocumented DUI reference, flagged as a contradiction on 2015-retail-theft-arrest.md.
  - Corrected the FB export HTML parser understanding from a prior session's (wrong) note: sender name comes BEFORE the message text in the DOM (`_a6-h _a6-i` then `_a6-p`), not after. Reusable parser script pattern noted in Current Focus above.
  - Bot review (Gemini Code Assist) on PR #56 caught one real issue among mostly grammar/formatting nits: lewis-strosnider.md had asserted an invented specific date ("February 12, 2019") for the NYC move that isn't sourced anywhere else in the wiki — the actual message only supports "~6 weeks from Feb 1," pointing to mid-March; corrected to not overclaim precision.
  - `bin/llm-publish` rerun and committed after the batch.
  - Gates 0 errors throughout (329 pages as of the last batch).
* **Handoff Note:** PR #56 still open (draft) — keep pushing to it until told to stop or it merges. The ranked candidate list and script pattern are preserved in Current Focus above; just re-run the classifier (cross-reference thread titles against wiki/people/*.md, rank uncovered by file size) since new pages shift what counts as "covered." The 234KB `qymuchauiq` thread (title "Participants: Facebook user and Dan Frank" — real name not in the title) is worth opening next; it's the largest remaining unknown. gmail_bodies.txt is still essentially unmined.

### [2026-07-19] - Session (cont.): Full Sail friend group — matt-dunn, jamie-mohler (new pages); jason-bermejo correction
* **Model:** Claude Sonnet 5 (Claude Code, remote), branch `claude/wiki-rewrite-expansion-c66x1u` (restarted from main after PR #53 merged)
* **Summary:**
  - Per operator directive: expanded pages for the Full Sail college friend group — Jason Bermejo, Eric Jester, Matt Dunn, Jim/Jamie Mohler.
  - **NEW `matt-dunn.md`** — no direct thread exists; built entirely from Jester's and Bermejo's own threads (the annual $5 birthday Venmo bit — "Every damn year… Of course I pay it" — and a Nov 2018 sighting back at the Orlando campus).
  - **NEW `jamie-mohler.md`** — the session's best find. Operator stated Jamie (formerly Jim, transitioned ~2023) was in NYC with Dan right after college and present the day Dan first met [[wiki/people/menore]]. Per operator instruction, searched the Facebook Messenger corpus specifically for Mohler content: no dedicated thread existed, but the **address book export** (synced 2021) had a direct contact card — Jim Mohler, `+12073101169`, `audiocranium@msn.com`. Cross-searching that phone number against `raw/self/dox-scan/gmail_bodies.txt` surfaced a genuine primary source: a **2011 Google Talk log** ("Jimbo Slice") — Dan inviting him to march with the Occupy Wall Street crowd, Crown Royal, the J train, apartment buzzer code — independently corroborated by **Alexis's own August 2011 Gchat** asking whether "Mohler" was coming over. This upgrades the NYC-1 co-residency claim from operator-attested-only to primary-source-confirmed (the specific "present the day Dan met Menore" detail remains operator-only — no thread documents that meeting itself). The 2023 transition is corroborated by two casual 2025 lines in Jason's thread ("Mohler = a literal woman" / "Haha she badass"; "ms. Jamie Mohler") — written throughout using her current name/pronouns per both the corpus's own current usage and direct operator instruction, with historical quotes preserved verbatim.
  - **CORRECTION:** `jason-bermejo.md` previously listed "Jamie Mohler — Current girlfriend of Jason" — a misread of a single line pulled without its surrounding context. In full context it's Dan ranking which Full Sail friends his mother remembers, not a relationship status. REVISED block applied; Mohler is a cohort member, not a partner.
  - `eric-jester.md` expanded (the Dunn sighting, the Venmo bit, `related:`→typed `connections:`); wired into `wiki/timeline/periods/full-sail-2008-2010.md` (new "The friend group" section) and `2010s.md` (NYC-1 key contacts); `menore.md` gains a note on the pre-2018 NYC-1 origin of the friendship.
  - Two capture notes filed this session: `2026-07-19_operator-note-full-sail-mohler.md` (the original directive + the Facebook/Gmail search findings appended as a follow-up).
  - Gates 0 errors throughout (312 pages); `llm/` regenerated.
* **Handoff Note:** The Facebook Messenger export is worth searching this way again — cross-referencing the address-book contact cards against `gmail_bodies.txt` (a large, unsorted personal Gchat/email archive that doesn't appear to have been systematically mined) surfaced a real primary source neither the iMessage corpus nor the Facebook message threads themselves contained. Other address-book names without a known iMessage thread could plausibly resolve the same way. Gaps still open: Matt Dunn has zero direct primary source (everything is secondhand via Jester/Bermejo); Jamie's current surname/location/occupation are undocumented; the exact date of the 2011 chat log isn't preserved (dated only to ~October 2011 by internal Occupy/Jewish-holiday evidence).

### [2026-07-19] - Session: long-tail MINE pass + kezmarsky correction + Oct-2019 MMF capture + psych-linkage retrofit
* **Model:** Claude Fable 5 (Claude Code, remote), branch `claude/wiki-rewrite-expansion-c66x1u`
* **Summary:**
  - **LONG_TAIL_TRIAGE MINE list executed in full.** Five swarm-template stubs rewritten as real prose pages from complete per-contact thread pulls (`MASTER_MESSAGES_DB_DUMP.csv`, speaker reconstructed from content per the direction-bug rule): **sam** (374 — NYC cannabis delivery dealer 2019–20 servicing 307 E 76th; fired Dan as a customer Feb 2020, resumed May 2020; adds the buyer-side half of the reliability inversion — Menore tolerated what Sam punished), **davey-fitzpatrick** (382 — Nemacolin assistant caddie master 2018, the "X report" scheduling channel; independent Apr 5 2018 corroboration of Fran's death date; final conversation = Dan announcing the NYC move Nov 2 2018), **vaughn** (228 — caddie + weed middleman, short-weight disputes, Feb 2018 orchestration-adjacent night flagged evidence-limited), **nick-mattie** (170 — spring-2017 reciprocal trading peer with hand-kept ledger; May 2 2017 handoff dates Annie's supply facilitation a year earlier than previously documented), **urpaaa-at-yahoo-com** (unidentified teacher, parental register, went with Dan to the Oct 6 2017 tooth extraction; Rick fits style/auto-trade fluency but teaching conflicts — identity left as the operator-resolvable gap). **jason-bermejo** opener rewritten per Substance Standard.
  - **CORRECTION (operator-requested validation): steve-kezmarsky was NOT dead.** The page's death claim misread the Dec 9 2018 Jim Shaffer thread — Jim's "Wait... he's dead?" is immediately corrected by Dan: "He's alive but living the least enviable life EVER / two kids / Sober / Dad going to jail for the rest of his life." Real event: the father's Jan 22 2018 arrest ("They picked up mr Kezmarsky today" — Annie) + April "he's fucked" legal exchange. REVISED blocks on steve-kezmarsky.md and new-jim-shaffer.md; index one-liner fixed; the Jan-2018 "it took this happening" gap on Steve's page is now closed (= the arrest).
  - **Operator captures synthesized (2 mid-session statements, filed to `raw/self/captures/2026-07-19_operator-note-oct2019-mmf-video.md`):** the Oct 21 2019 NYC filmed MMF (Dan's sole bisexual experience, oral only) — corpus-corroborated by Sent 2019-10-22 "last night we had to film mmf (my first time doing that)…"; new arrangement-history timeline row; tuquick page gains "The October 2019 video as weapon" (closure-night taunts 23:07:06 + 23:17:25 documented). Third participant identified: **NEW page `bryan-5088682461`** (gay man, first female encounter that night; +15088682461 corroborated via unanswered May 2025 "babyboy" re-contact; NOT the escort-client brian.md — hatnote added). The Bryan instance corroborates erotic-architecture's "taboo as ontological rupture" mechanism — its strongest theory-to-instance match.
  - **Psych-linkage retrofit (operator directive "connect psychological entries to people entries"):** attachment-model, conflict-architecture, phenomenology-lens, developmental-origins, emotional-imprinting, erotic-architecture, arrangement-history, dans-law, node-locking, institutional-out converted to typed `connections:` (~45 argued edges + inverses into annie-ulmer, rick-frank, suzanne-frank, alexis-armel, kelly-johansson, kristin, valeria-iglesias-cid, bryan, eli-incident, bfs-foods, au-zaatar, forensic-method, exocortex…). Deprecated `related:` lists deleted on all retrofitted pages.
  - Gates 0 errors throughout; llm/ regenerated (310 pages).
* **Handoff Note:** MINE list is now EMPTY — long-tail people/ work remaining is only the ACCEPTED-LEAF set (do not churn). Psych-linkage continuation: `mind/profile/` pages still on `related:` (intp, big-five-psychometrics, socionics-and-attitudinal, linguistic-profile, voice-modes, deviance-mapping partially) plus `taboo-and-boundary-testing` (standing verdict: connections only, no rewrite without richer primary source) and the two psychosexual/profile index pages. Next priorities per prior handoff: storytime candidates (gemini-07/13/18/21/58, j6-chat, 9-11-chat, pinned chats), connection-queue top-down. Open operator-resolvable question: urpaaa@yahoo.com identity (teacher, parental register, LH football partisan — one line from Dan settles it).

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
  - Fixed `.git/index-lock` issue and committed changes.

## [2026-08-09] ingest | self/extreme-sports, people, places, interests | childhood extreme-sports era captured

**Source:** `/Volumes/MUSIC/alias/XXX/2026-08-09_122727_extreme-sports (1).md` — operator-supplied manual capture from a direct-drop mount.
**Filed to:** `raw/self/captures/2026-08-09_122727_extreme-sports.md`

**Pages written:**
- `wiki/interests/extreme-sports.md` — New interest page: Tanner Hall era freeskiing culture, Seven Springs terrain-park development, 4Bi9 Media scene, Vans Skatepark birthday trips, Camp Woodward summers, class-signaling angle.
- `wiki/people/matt-kraus.md` — New person: Dan's closest documented childhood friend; Vans Skatepark co-attendee, Seven Springs condo neighbor, Woodward attendee.
- `wiki/people/nathan-king.md` — New person: Woodward attendee for three years with Dan and Matt Kraus.
- `wiki/people/tancredi-calabrese.md` — New person: childhood friend who planned Windell's Whistler ski-camp trips.
- `wiki/people/tom-wallisch.md` — New person: regional Seven Springs scene figure who became the 2007–2012 era-defining freeskiing athlete.

**Pages updated:**
- `wiki/people/tan-calabrese.md` — Identity correction: tancredi-calabrese.md (the forked page) deleted, merged into this page as the childhood friend. Infobox name updated; sources added; new `co-occurs` connection to `wiki/people/tom-wallisch.md` explicitly distinguishing the contact from the childhood friend.
- `wiki/places/seven-springs.md` — Source list expanded; new `co-occurs` edge to `wiki/people/tom-wallisch`; date_modified bumped; terrain-park development section added.
- `wiki/people/index.md` — Four new entries added.
- `wiki/interests/index.md` — Extreme-sports entry added.

**Age/date cross-check:** No self-reported ages or dates in the capture require CONTEXT_CORE cross-checking — the capture narrates adolescent events from 2000–2006 without using specific age claims that need verification.

**Entity name reconciliation:** Tan Calabrese → Tancredi Calabrese split handled via the identity correction protocol: contact page updated with dual name, childhood-friend page created under full name, co-occurs edge explicitly names the distinction.

**Write-back inverses:** All inverse edges added on target pages (tan-calabrese → tancredi-calabrese; seven-springs → tom-wallisch).

**Gates:** wiki-lint 0 errors · wiki-connect check 0 errors · wiki-climb check 0 errors, 0 stale.

**Raw file:** `raw/self/captures/2026-08-09_122727_extreme-sports.md` (md5: d73cbb65ec7cdb19b5b1dbc870897ac6).
