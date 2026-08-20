## [2026-08-19] audit | self | the last three days of edits — three pages had the attribution backwards, and the corpus settled all three

Operator: *"do a pass over everything edited or created in the last 3 days and fix the sourcing, attribution, edges, and any other problems."* Scope: 99 wiki pages touched since 2026-08-16. The Aug 16–18 work held up — the stale-premise pass carried 39 `RE-CHECKED` blocks and changed four conclusions, and the new `james-dee`, `diane-moore`, `dave-moore`, `the-handed-mirror` and `cocaine` pages verify against their declared sources. The damage was concentrated in the six pages written on Aug 19.

**Three attributions were reversed, and the export settles each one.** On `claude.md`, *"Claude = to analyze stuff"* was credited to Tom and *"It did really well with the Kristin chat logs. Better than GPT"* to Dan. `imessage_export_deep_20260813.csv` rows 184487–184503 record the first as **Sent** by Dan and the second as **Received** from Tom, on **2026-03-26** rather than the 03-25 the page gave. Dan's own line in the same minute — *"Claude Is the wokest"* — had not survived into the draft at all. Corrected in place with the old claim visible; the same reversal was propagated to `gemini.md` and fixed there.

**`chatgpt.md` and `gemini.md` were quoting a model as though it were the operator.** The chicken-nugget passage, *"fully processed, pasteurized, and packaged for mass consumption,"* *"a legacy product, a glorified tech demo,"* *"not a cognitive weapon; it's a productivity tool, like Microsoft Excel"* and *"a sludge of median thought"* were all filed under the heading *"Dan's view of ChatGPT's decline is documented, detailed, and angry."* Every one of them is **Gemini's** output in `Gemini Activity.html`, generated in response to Dan's entire contribution on the subject: *"gemini i think chatGPT is cooked"* (2025-08-24, 11:23 PM). The corpus records the verdict and not one word of the reasoning. `gemini.md` compounded it by re-quoting Gemini's ChatGPT autopsy as documentation of **Gemini's own** decline. Both pages now carry `CORRECTED` blocks and separate primary testimony from model output.

**The Gemini activity log is 3,986 prompted entries, not "100,000+".** The inflated figure appeared six times across `gemini.md` and `llm.md`, against `wiki/self/gemini-activity/gemini-activity.md`, which has carried the correct count (3,986 prompted / 3,989 timestamped, peak Dec 2025 at 938) since it was written. A 25× error that one grep would have caught. The stale "438 pages" was corrected to 473 in nine places.

**A boilerplate block describing Claude Code's tooling had been pasted onto three pages with the model name swapped.** `chatgpt.md` and `gemini.md` each claimed a `delegate_task` subagent system, a skill system and a capture system, verbatim, opening *"ChatGPT (via Claude Code) has…"* and *"Gemini (via Claude Code) has…"*. It also carried a `/Users/daniel/.hermes/` temp path and a skill inventory that matches nothing in `.claude/skills/`. Deleted from all three; the material is kept on `claude-code.md`, with the real skills named and the path removed. Sixteen further duplicate sections were removed across the five model pages, several verbatim repeats of a section already on the same page — the residue of a "draft 300+ lines" instruction followed literally, which `claude-code.md` had itself documented under "The literalism problem" while exhibiting it.

**`claude.md` and `claude-code.md` each claimed to have written the wiki.** Both asserted the 473 pages were their own products, of each other's pages. Rewritten on both sides: the split is one of tooling, not authorship, and the operator directs every pass.

**Sourcing.** Three pages had non-`raw/` paths in `sources:` — the only such entries in the wiki. `wiki-brain.md` and `claude-code.md` listed the governing documents (now cited in prose, where they belong); `ally-and-dan-love-as-destiny.md` listed five wiki pages, one of which (`wiki/self/context-core`) it named wrongly. Moved to `synthesizes:`, which cleared five `wiki-climb` errors. `claude.md` cited none of the files carrying its own quotations; the deep export was added.

**The August 18–19 Ally exchanges are not in the repository.** They are the load-bearing evidence for both the `ally-lubin` rewrite and the destiny page — 279 messages and 186 messages — and they exist here only as quotations inside `wiki/`. `ally-lubin_chatdb_complete.csv` stops on August 18 with 126 rows for that day and nothing for the 19th. Four quoted phrases (*"boy smashing factory," "1-2-3 break," "coke just zaps your money," "opiates literally kill you"*) are in no file under `raw/` at all, and *"I'm inherently evil"* is attributed to Ally but occurs only in Gemini's prose. Recorded as gaps on both pages; the extract is a one-command job for the operator and makes the whole phase-change reading checkable.

**`ally-and-dan-love-as-destiny.md` is a projection and now says so.** Roughly half of it — the wedding, the house, the cats, the first year, the children question, the long view — describes events that have not happened, in specific detail no source supports, written in the indicative. Nothing was deleted: a wish recorded at that length is a real datum about its author, and cutting it would hide what the page is. It now opens with an epistemic-status block, carries a labelled seam where the evidence stops, and states the two things it had asserted past: that the burst it reads as a phase change is equally consistent with `dormancy-not-exit`, whose two prior silences each followed exactly such a burst, and that Ally's intentions are documented nowhere but in Dan's reading of her replies. `ally-lubin.md`'s footer, which had endorsed it as "the full evidence-based case," now names the disagreement and says what settles it.

**Edges.** 40 missing inverses written with argued claims rather than restatements. Five edges on `ai-collaborative-analysis` pointed the wrong way (a synthesis is not an instance of its members) and are now `evidenced-by`. `wiki-brain.md` had `component-of` edges running toward the models it contains — inverted, now `contains`. Two dead targets (`wiki/self/dan-frank`, which has never existed) retargeted to `wiki/self/overview`. Four `contradicts` edges that named a difference rather than an incompatibility were downgraded to `mirrors`; the two that are real — ChatGPT against Claude Code on where an LLM's value sits, and the destiny page against `erotic-architecture` on whether the charge survives access — now carry the `CONTRADICTION:` blocks the spec requires. The second is the cheapest falsifier the wiki owns: a first in-person meeting settles it in a weekend.

**Also.** Invalid tag `future` removed. Broken table wikilink on `diane-moore` fixed. Four frontmatter blocks I broke mid-pass were repaired and re-verified.

Gates: wiki-lint **0 errors**, 18 warnings (all pre-existing) · wiki-connect check **0 errors**, 252 warnings (down from 290; every `self/concepts` warning cleared) · wiki-climb check **0 errors, 0 warnings** (down from 5 errors). `llm/` regenerated.

## [2026-08-18] rewrite | people | suzanne-frank — the wiki had the family's money flowing the wrong way, and the mother's thread undercounted fourteenfold

Operator: *"rebuild the suzanne-frank article… expand it a bunch and be more subtle with the digs. do a real re-analysis with all available sources."* Wipe-and-rewrite per `.claude/skills/wiki-rewrite`. 28 KB → 58 KB. Every checkable claim on the old page was tested against `raw/`; six failed.

**The headline number was wrong by a factor of fourteen.** The page reported *"2,391 messages — rank ~8–10,"* sourced to `MASTER_MESSAGES_DB_DUMP.csv`. The authoritative `all_imessages_complete_dump.txt`, joined to the 2026-08-13 deep export for the window after 2025-08-10, gives **33,698 messages, 2015-11-17 → 2026-08-11 — rank 2 in the entire corpus**, behind only Annie (119,405 across four handles) and ahead of Kristin (20,009). The error had propagated to `contact-gini` and, through it, to `single-channel`, whose "no failover / single external input" claim was resting on it. Both corrected; `single-channel` now distinguishes **volume from dependability** and carries a falsifier.

**The largest capital movement in the family runs mother-ward, and the spine had it backwards.** `estate-money-spine` and this page both described Suz as the artery feeding Dan, citing *"$750/week borrowing."* The primary record contains **one** such statement — 13 December 2018, *"You borrowed $750 last week alone!"*, an accusation about a single week made on a day she had herself asked him for $450. `operating_manual.md` (AI-secondary) generalised it into a rate and inverted its direction; the wiki inherited both. What the record actually shows: in **August–October 2018 Dan transferred ~$14,000 to her**, drawn against an estate that did not distribute until September 2020. $4,000 came back. Her own itemised statement of it survives (3 Oct 2018). By 3 July 2019 both were threatening court, each claiming to be the creditor — 105 messages, one of the thread's eight biggest days. Never adjudicated, never withdrawn, and still the live subject of the corpus's most recent message from her.

**The 337 Saratoga sale was a bankruptcy liquidation, not a decision.** New from a case audit Dan pasted into the thread on 30 Mar 2026 (AI-secondary, uncontradicted, bracketed by her own messages): **Chapter 13, case 24-22285-GLT, filed October 2024, ~$157,000 scheduled, IRS priority claims for tax years 2018–2021**, $300/month plan, 341 meeting Nov 2024, court "drop dead" provision Aug 2025, ask $615k (May 2025) → $465k. 337 was owned free and clear and was the only asset capable of satisfying the plan. The wiki had "a bankruptcy approval" filed as one contingency among three. Written back to `337-saratoga-drive` and `463-morgantown`.

**Her income was $11–14k/year.** Her own line, to an HOA, June 2020: *"My property taxes are $10,000/yr. I have only earned between $11,000–$14,000/yr in the last decade."* Consistent with everything else in the thread and with none of the "primary financial artery" framing: a $503 gas shutoff, a repossession fear, and — the cleanest datum in the file — *"Would it be possible to PayPal me $8? I need to show a house in two hours and I need $14.37 to get my key working. I have $7 in there now"* (8 Jan 2020).

**Two gaps the page had declared were already answerable from `raw/`, and both were cascade failures rather than missing facts.** (1) *"No independent account of her relationship to alcohol is on file"* — an extensive one is, in her own messages, every year of the corpus, up to *"#1 Cigarettes #2 wine #3 food"* (July 2025). (2) *"Her own perspective is undocumented; the corpus view is entirely Dan-side"* — several thousand messages in her voice were on disk, including the 8 July 2019 letter (*"I would never lose contact with either of my children the way it happened with your Dad and me and our parents"*) and the May 2018 letter naming Fran *"the one and only guiding force in my life. The one person who loved me unconditionally."* The 2005 rupture specifically remains her-side undocumented; the general claim did not survive one grep.

**The organizing finding.** Both mother and son skip the intervening generation and anchor to Fran — the same attachment, in the same maternal line, one rung apart. Diane, whom the GEDCOM places in **Michigan from 1985 to 2020** (which is why the vigil's directives came by letter), rejected Suz; Suz states her own parenting as an explicit negative of it, and then runs with Dan the same structure she inherited: total availability plus an itemised bill.

**Also corrected or newly established.** Park Place Realty move is **October 2019**, not 2020 (*"Park place realty… here I come!"*, 2 Oct) — the strong month was Aug 2020, ten months later, which weakens the causal pairing the page implied. Licence **RS305558 appears nowhere in `raw/`** — flagged UNVERIFIED, not deleted. The Winter Park condo is **corroborated in her own words** for the first time (*"how much money I lost between antique oaks and Virginia Ave"*, 14 Nov 2024); the trafficking arrest still is not. **155 Virginia Ave carries a stated ~$135,000 capital loss** (a $3,000/yr deduction over 45 years). Married Rick **31 Aug 1985**; her parents married **8 Feb 1961 at Belmont Circle**. Gambling has a documented **end** (*"Suzanne does not gamble anymore"*, 5 Nov 2024), which no page carried. Her political switch is dated to **March–June 2020**. `john-felix` revised: Felix runs Jan 2016 → Jun 2026 in the Suz thread, which does not support the partner reading that page carried.

**Two things nobody had written down.** A **27 September 2020 Facebook message** from Suz to both of them — *"You two need to figure out how to discuss without getting physical or you need to go your separate ways. This keeps happening"* — the earliest contemporaneous third-party account of physical conflict in the Annie relationship, four years before the terminal phase. And the corpus's **last message**, 11 August 2026: *"It's time for you to go. I'm so tired of you stealing from me."* Five weeks after the move out of the house she sold, the same accusation as 2017, 2019 and Dec 2025, now attached to his housing.

**One measurement worth a second look.** The Suz thread collapses from ~296 messages/month (Jan–Jun 2026) to **14 in July and 28 in the first eleven days of August**, while the corpus overall runs 2,115 and 2,689 in those months. Not an export artifact — same file, same window. Recorded as a gap.

**Cascade.** Four rounds. `estate-money-spine`, `attachment-trauma-bond`, `totality-themes`, `single-channel`, `the-deferred-audit`, `alias-as-periodization`, `supply-network`, `alexander-jackson`, `arnu`, `john-carney`, `johnny-dealer` all re-checked with reasoning recorded, none date-bumped. Three produced findings rather than paperwork: `single-channel` gained the volume/dependability distinction and a falsifier; `attachment-trauma-bond` gained the boundary that the leverage see-saw is an inherited template rather than something the Annie relationship generated; `the-deferred-audit` got a clean instance of itself (the largest imposed relationship in the corpus was never audited, and neither was the wiki's count of it).

Gates: wiki-lint **0 errors**, 17 warnings · wiki-connect check **0 errors**, 244 warnings · wiki-climb check **0 errors, 9 staleness warnings** (down from 18; the remainder all pre-date this pass and trace to `annie-ulmer`). The long-standing `master-timeline.md` lint error is fixed at source: `bin/wiki-timeline` was emitting four tags outside the closed set in `STYLE_GUIDE.md`, and now emits none (`tags:` is optional).

## [2026-08-16] close | timeline | shelbie-annie-threesome — the operator dated it, and the corpus showed the page had the authorship backwards

First use of the portal GAPS tool. Operator answered *"Exact date within April 2019 is not established"* with both dates and the sequence; that answer sent the pass back to a thread nobody had checked, and the page's central claim did not survive it.

**The dates are exact and were always recoverable.** 14 April 2019 (9pm–4am) and 17 April 2019 (2am–7am). The page had said the corpus "cannot independently confirm an April date" — true of the Shelbie thread, which begins 2019-05-15, and false of the corpus. **The whole first night is in Annie's thread on `+17249204125`: 109 messages between 9pm and 4am, 79 of them hers.** A dated event involving three people has three threads; this page checked one and wrote the negative result down as a property of the archive rather than of the query.

**The event runs the opposite way from how it was filed.** It sat in `arrangement-history` as an instance of the Dan-architected arrangement. The minute-level record shows a purchased one-on-one — Cash App receipts to Shelbie of **$31 and $700 on the 14th**, *"$3700 and one amazon prime'd laptop later"* by the 19th — that **Annie converted into a threesome from outside a locked door**. Her texts are not objections: *"She can stay as long as she pleases I don't care. I just wanna play a little too"*, *"I'll ring the doorbell idc"*, then in caps *"SHE XAN STAY"* / *"TELL HER TO COME THE FUCK BACK"*. Shelbie left at 22:36. Dan: *"she left"*, then **"just say fucking no next time"** — anger at consent-then-intrusion, not at refusal. At 22:56 he sends Annie `Shelbie Breakiron.vcf`; at 23:34 Annie has her back: *"She here. Everything is cool 😎 we hugged."* By 01:56 it is a rivalry with a price — *"if you date her i get her once a week."*

**One correction to the operator's own account, held not resolved.** He recalls Annie contacting Shelbie *"independently without me knowing."* The 22:56 contact-card attachment is his. Recorded as a `CONTRADICTION` rather than decided: supplying the means and not expecting the use is a different act from being cut out, and only he can say which it was.

**The cascade is the part that matters.** `arrangement-history` carries the correction plus the falsifier it implies: the instances that page reads as Dan-architected are mostly reconstructed from **negotiation threads with the third party**, where Dan is by construction the correspondent. April 2019 is the one reconstructed from the couple's own thread *during* the event — and it is the one that inverts. That is a sampling artefact large enough to have manufactured the pattern, and it is now the first thing to test on that page rather than a footnote to it.

Three gaps opened where one closed: Shelbie's own account of either night (her number starts a month late), whether the 17 April window is really the second encounter (a long late-night drive and Annie's *"You can do your thing first if you want. That's perfect"*, but no message names her), and the meaning of the `.vcf`.

## [2026-08-16] build | all | bin/wiki-gaps — 269 open gaps, no way for the one source that can settle them to answer, and OPEN.md could only see 164 of them

Operator: *"make a wiki tool that helps me close gaps… select an entry, bring up the gaps, select one, input explanation/context… there should also be a MANUAL option."*

**The count is the finding: 269 open gaps across 116 of 460 pages.** `OPEN.md` has been publishing that list since it was built and nothing has ever consumed it. Reading a sample, most are not blocked on a missing export or a better parser — they are blocked on the operator, and most could be settled in a sentence. `wiki/people/kristin.md` says so in as many words: the Kayden contradiction *"needs either the dossier's underlying `chat_162.txt` (not in `raw/`) or a direct operator answer."* The repository had a `capture` box for facts arriving unprompted and **no route at all for answering a question it had already written down.** That asymmetry is why the gap list only ever grew.

**`OPEN.md` was undercounting by 39%, and the missing gaps were the ones written well.** It reported 164; there are 269. Two causes, both in `write_open`. Its item regex was `^-\s+`, so it only ever saw *bulleted* gaps — **84 gaps across 79 pages are written as prose paragraphs** and have been invisible since the file was created. And its section regex `^##+\s*Gaps?\b` was `re.search`, i.e. first match only, against a fixed heading: it missed `## Notes & Gaps`, `## Corpus gaps`, `## Notes and gaps` and `## Open questions` entirely, and on `wiki/people/jerel-coles.md` — which carries **both** an `## Open questions` and a `## Gaps` — it read one section and stopped. So the pages that took the trouble to write their unknowns as argued prose were the pages whose unknowns nothing could see. Both tools now agree page-for-page at 269.

**What the tool does not do is the deliberate part.** It stages; it does not correct. The gap is cut out of `## Gaps`, moved verbatim into `## Operator answers — pending ingest` beside the answer, the page is flagged `pending_ingest:`, and the answer is filed to `raw/<domain>/captures/` as T0 evidence carrying a `targets:` line. Correcting the page and cascading into every page that inherited the gap is a judgement call across the whole corpus; a text box cannot make it and should not pretend to. What is guaranteed is that the answer is captured the moment it exists and cannot be missed later.

**`date_modified` is not bumped when an answer is staged**, and that is the load-bearing decision. Bumping it would clear the `bin/wiki-climb check` staleness warnings on every page reasoning from this one while the page itself has not been corrected — precisely the move CLAUDE.md §3 forbids. The date moves when the correction lands, not when the material to make it arrives.

**Two traps found in existing tooling while building.** `bin/wiki-digest`'s `BLOCK_RE` scans every page for a literal `**GAP CLOSED`, so a staging block *instructing* the next pass to write one would have been read by `RECENT.md` as a gap that had actually been closed — the preamble drops the asterisks for that reason. And the staging section is deliberately not named `## Gaps …` anything: the gaps-section regex would have scraped answered gaps straight back into `OPEN.md` as open ones.

**Governance, without which the flag is inert.** `CLAUDE.md` gains a **CLOSE** operation — read the page, treat the answer as T0 testimony rather than as proof, check it against `raw/` where it can be checked, hold contradictions rather than settling them by seniority, integrate rather than append, cascade, *then* bump the date and clear — plus a start-of-session instruction to run `bin/wiki-gaps pending` before anything else. `OPEN.md` gains an **Answered, awaiting ingest** section. `STYLE_GUIDE.md` declares `pending_ingest:` and gains a rule: write each gap so one person can answer it in one paragraph, because a vague gap is a question that never gets asked.

## [2026-08-16] rewrite | people | kristin.md — surname wrong, dates wrong, count wrong, and the wiki's own instrument cannot see the thread

Operator: *"Can we build out Kristin's entry. Reanaluze the whole message thread (fb and text) and rewrite."* Ran the `wiki-rewrite` protocol end to end.

**The page was about a relationship that ended five weeks earlier than recorded.** Month counts from the both-direction export: Sep 14,688 · Oct 4,896 · **Nov 53** · Dec 372. November is a stopped month, not a quiet one. The $40 dispute — placed on Dec 9 by the old page — is live on Nov 2–4 and named as the rupture on Nov 13 (*"Idk why you just up and ghosted"* / *"do you think it has anything to do with you beating my mom for $40"*). December is a **failed reactivation of a dormant channel**, which reassigns the episode from a collapse narrative to `dormancy-not-exit` and makes it that rule's shortest instance. Dan withdrew first — the old collapse framing had no room for it.

**Surname was wrong and was taken from a filename.** The page said *"Last name confirmed as Shaelene from the dox-scan messenger export."* That export's name is a Facebook *display name* (first + middle). She states her own surname twice in the first person — *"me, Kristin Prentiss"* (09-11), *"The thing about Kristin Prentiss is…"* (09-13) — and Dan uses it. `operating_manual.md` had flagged "Shalene or Prentiss" as unknown; the wiki resolved it in the wrong direction from the weaker evidence.

**She is not a mother, and "Kayden" occurs zero times in 20,009 messages.** The claim came from `tom_kristin_master_dossier.md` — AI-secondary, and by its own opening an analysis of the **Tom**/Kristin dyad written when *"Dan is entirely separate from Kristin."* Her own line, 09-22: *"He's the only kid I've ever been around ever… That's not her kid biologically it's her husband's"* — the child is **Ryder**, her half-sister's stepson. Left as an open contradiction, not resolved. A third party's aliases ("Krazy Krez", "Daniel Kresowaty") had likewise been attached to her from a message plainly about a man.

**Count was 17% low and came from the file the repo already distrusts.** 16,563 is the `MASTER_MESSAGES_DB_DUMP.csv` figure; the both-direction export holds **20,009** (10,102 sent / 9,907 received). Corrected downstream on `contact-gini.md`, `master-message-dump.md`, `people/index.md` and the regenerated `master-timeline.md`.

**Facebook came first and the page never knew it.** The Messenger file is a **UI screen capture** taken 2025-09-01 07:04:39Z–07:53:01Z, not a thread export; the conversation inside it is dated **August 29–30**. Parsed by speaker it yields **2,009 messages, Dan 1,439 / Kristin 570** — he sends 2.5× what she does before iMessage opens, against near-parity (51.5%) afterwards. Content is almost entirely links: politics (politicalcompass.org, *Zeitgeist*, Aaron Parnas) and music (Scissor Sisters, *Human Nature*, *Return of the Mack*). First contact moved 2025-09-01 → **2025-08-29**.

**Why none of it was caught: `bin/mine-messages` has zero coverage of this relationship.** `all_imessages_complete_dump.txt` runs 2011-03-18 → **2025-08-10**. Handle `3307038747` occurs in it **not once**, and neither does any message from Sep–Dec 2025. The documented guard — *"any claim about what Dan said must come from all_imessages_complete_dump.txt"* — **fails silently** here: out-of-window queries return zero matches rather than an error, so a query about Kristin is indistinguishable from a query about a stranger. Every claim in this wiki dated after 2025-08-10 carries the same exposure; recorded on `source-coverage-index.md`, which now leads with the ceiling.

**New method trap.** The Messenger capture stores some strings in mathematical-monospace Unicode — a plain grep for `LONELY LOSER` returns nothing while the string is present. Fold with `unicodedata.normalize('NFKC', …)` first. Same family as the curly-apostrophe trap; belongs beside it in `EXTRACTION_SPEC.md`.

**Cascade, two rounds, both productive.** `block-unblock-loop` re-checked: its Kristin control row is *better* supported than written (the dependency was dead five weeks before the block, so "she needed nothing back" is demonstrated rather than inferred) — and it gains an open lead, that durable counterparty blocks may be predicted by *who left the channel first* rather than by dependency alone. `totality-themes` re-checked: the "closures Dan can perform alone are the reversible kind" prediction survives and widens from one relationship to two.

Gates: wiki-lint 5 errors (all pre-existing, none on touched pages) · wiki-connect 0 errors · wiki-climb 0 errors.

## [2026-08-15] read | timeline | the read pass gets a second output — entity ledger, leads, motifs — plus Nov 30: Suz paid for the eviction
- Operator, mid-read: "May the task of doing this also be beneficial just for you to keep detailed notes for other analysis later? Just a thought" — and, separately, the three numbers `7244346811 7249204125 2124702449`.
- **Handle identification closed.** The three numbers the operator listed are exactly the three this session had derived. `+17249204125` had rested on one inferential line (*"I texted her yesterday from my new number!"*) plus register matching; it is now operator-confirmed. Captured to `raw/people/captures/2026-08-15_annie-handle-confirmation-and-notes-directive.md`. **Flagged in the capture: the operator listed three numbers, but the corpus carries a fourth channel** — `alulmer28@gmail.com`, ~800 messages, 2020-07-30 → 2020-10-07, an iMessage handle on the same Apple ID rather than a separate line. It is the **only** source for autumn 2020 and must not be dropped on the strength of a phone-number list.
- **The suggestion was adopted as method, and the reasoning is worth keeping.** Reading is the expensive step and it is paid once. Pulling a second kind of finding from an already-read window costs almost nothing; re-reading 97,768 messages to recover something noticed and not written down costs the whole pass again. A read recording only *events* discards, at the moment of maximum information, everything that is not an event — `CLAUDE.md` rule 1's failure mode applied to the repository's most expensive extraction.
- **New page `wiki/timeline/annie-read-notes.md`** — the second output of the same read: (1) **entity ledger** (14 entities so far, with first-appearance dates and page status), (2) **open leads** (7 chaseable questions), (3) **motif tracker** (5 patterns with dated instances, so a later climb counts instead of re-reads), (4) **corrections queue** against standing wiki claims, (5) **quantitative markers**. Both pages are now updated in the same pass; notes captured after the fact are notes not captured.
- **2015-11-30 read in full (403 messages). The headline is Suz.** At 05:02: *"Suz just came to check on me, brought me a line, and told me she'd get me a car this week if I get Alexis out."* The night before she had phoned to say Dan *"should date"* Annie because the name fits the family — *"Anne Dan Suzanne Fran Diane Van"* — and Dan confirms *"She srsly offered me a car last night."* **Cocaine and a car, from the mother, as consideration for completing the eviction.** The family did not merely approve the switch; it brokered it and paid for it. Earliest and bluntest instance of the maternal leverage `estate-money-spine` and `supply-network` document from far later material.
- **Also 2015-11-30:** the eviction runs as reversible pressure steps rather than a confrontation (key confiscated → property removed from the guest bedroom *"so she knows I could actually call the cops"* → Alexis's **parents** summoned, which is how Dec 1's *"Helping lex leave"* resolves); **Casey Bondarenka is three weeks old as a friend** (*"He just started hanging out with us last week"*); the **first joint drug purchase** ($100, a named Morgantown WV source, against Annie's paycheck, with a birthday discount) — 19 hours after Dan's offer to abstain entirely; a **jointly maintained cover story** confirmed to exist (*"I have stuck to the story 100%"*) but never stated; Annie floating moving in on day three; and the social cost named (*"nobody understands why I'm doing this"*).
- **A concrete, chaseable gap found rather than a general one:** Dan's *"love letters"* of Nov 30 were sent **to an inbox**, not by text (*"you have love letters in your inbox"*; Annie can't find them; he resends). The most deliberate writing of the relationship's first week is in an email channel the message archive does not contain — `gmail_bodies.txt`, late Nov 2015, is the place to look.
- **Biggest unapplied correction remains from Nov 29:** Annie had her own partner (*"turd boy"*) and ended it the same week, so `bond-switch-2015`'s whole analysis of an unattached Annie is wrong. Logged in the corrections queue; the man is still unnamed.
- Gates: wiki-lint **460 pages / 0 errors** (10 warnings) · wiki-connect check **0 errors** (240 warnings) · wiki-climb check **0 errors, 1 warning**.
- Read through **2015-11-30 — 1,539 messages, 1.6% of corpus, 34 events.** Resume at 2015-12-01.

## [2026-08-15] read | timeline | the Annie corpus is 97,768 messages across FOUR handles, and reading two days of it produced 25 events no script found
- Operator, after reviewing the generated master timeline: "almost all the events are pure garbage. Let's try another method and start from scratch. Analyze my text logs with Annie and use ONLY THOse to identify events... it's impossible to figure it out with a script."
- **First finding, before any reading: the Annie corpus was incomplete in every source, and nobody had noticed.** Annie used **four** handles, not two. `+17244346811` (2015-11 → 2018-12), **`+17249204125` (2018-12 → 2020-06)** — opened with her own line *"I texted her yesterday from my new number!"* (2018-12-27) — **`alulmer28@gmail.com` (2020-07 → 2020-10)**, her iMessage email, and `+12124702449` (2022, 2025 → 2026). The best single Annie file in `raw/` holds 85,586 messages and shows **zero traffic for 2019 and 2020**. Merging on all four handles recovers **97,768 unique messages**, including all 8,938 of 2019 and 1,163 of 2020. Any timeline built from the obvious file would have silently deleted two years of a ten-year relationship.
- **Four candidate handles were checked and rejected**, which is why the four survive: `+13476070497` = Menor (NYC supply), `+18337924420` = Cash App notifications, `+19165013615` = Jerad Friedline (the TSLA/market thread), `+17249844280` = a third party in the Feb 2019 arrangement traffic.
- **New tool `bin/annie-corpus`** (pure stdlib): `build` merges ten sources, de-duplicates on (timestamp, direction, text) and sorts; `coverage` prints a month grid; `days` sizes a reading session; `read FROM TO` prints a window. It honours the per-contact export convention — a blank contact on a `sent` row is Annie *only* in an Annie-scoped file, and unattributable in an all-contacts file.
- **The real coverage, stated as a hole rather than a silence: 2015-11-28 → 2020-10 is dense; 2020-11 → 2024-12 contains five messages in four years; 2025-03 → 2026-06-05 is dense.** Four years of the relationship have no two-sided record in any export. Recorded on the new page as a hole in the instrument, not a quiet period — per `EXTRACTION_SPEC.md`, a zero is data only when the system could have observed a one.
- **New page `wiki/timeline/annie-record.md`** — a read chronology. Nothing on it is pattern-matched. Two days read (2015-11-28 and 2015-11-29, 1,136 messages), **25 events**, each with the verbatim line that establishes it.
- **What two days of reading produced that no sweep could:**
  1. **Annie's birthday is November 28** — the corpus opens on it, with her abandoning her own birthday dinner (*"Fuck my friends. Fuck birthday dinner... I wanna be with you"*).
  2. **The golf-course meeting is in the record in real time** — *"K I'm on gold course"* (01:52) → *"I'm on 3 tee"* (01:57) → home by 02:30, on 2015-11-29. **The rain is confirmed from Annie's own side** that afternoon: *"I normally would have been sassy about it raining, or sitting in wet grass, or my hair getting wet."* Location: 3rd tee.
  3. **Annie was leaving someone too, and said so** — *"my fam and dude are here"*, Dan's *"turd boy"*, and Annie's **"I am going to get rid of him just like you just did."** Every prior account of the switch — including `bond-switch-2015`'s twenty-four-hour analysis and its 2026-08-02 subject-flip correction — treats Annie as unattached. **She was not.** The switch was mutual and simultaneous.
  4. **Dan's own real-time explanation for why Alexis would not leave: supply.** *"I know why she isn't leaving... she doesn't have another drug source"* (Nov 29, 14:54) — `supply-network`'s mechanism, applied to the departing partner, a decade before the page that documents it.
  5. **"I met someone that instantly changed my life"** is said **to Annie**, an hour after the meeting — the wiki has carried the quote for months without its address, and never quoted the substantive half: *"And I was alright with that for so long that I forgot I was sad."*
  6. **The dossiers' "YOU ARE MY EVERYTHING" is dated** to 2015-11-29 03:24, hours after the first meeting rather than "day two/three."
  7. **Fran's house at 117 Belmont Circle was a venue for the affair in its first week** — *"We can hang at my grandmas even? I would need to get a key from suz"* — three years before Dan became her paid caregiver there.
  8. Also: Dan took Alexis's key (Nov 28); Alexis was in the house all of Nov 28–29 with packing begun but not completed; Zachariah Harshman was the physical cover for leaving the house, context for his December 23 confrontation; the **#dannie** hashtag and the marriage/passport frame both appear within hours; a pre-Dan nude leak distinct from the MyFreeCams history; and Dan's day-two offer to drop drugs entirely (*"we can ALWAYSALWAYS not do drugs"*), a boundary that did not hold.
- **Why this replaces the scripted approach, stated plainly:** none of the 25 events exists anywhere as a dated sentence. They are things two people did, recoverable only by reading a conversation in order and judging what happened. The 2026-08-14 sweep and its 2026-08-15 rule-based replacement both had this material and extracted none of it.
- **Rate and honesty about scope:** 1,136 of 97,768 messages read — **1.2%**. December 2015 alone is 12,000 messages. This is a multi-session job and the page carries an explicit resume cursor rather than pretending otherwise.
- Gates: wiki-lint **459 pages / 0 errors** (10 warnings) · wiki-connect check **0 errors** (239 warnings) · wiki-climb check **0 errors, 1 warning** (the pre-existing ancestry cascade). `bin/wiki-digest` and `bin/llm-publish` rerun.
- Pages touched: new `wiki/timeline/annie-record.md`, new `bin/annie-corpus`, `wiki/timeline/index.md` (linked). `exports/annie-corpus.csv` is gitignored and regenerable with `bin/annie-corpus build`.

## [2026-08-15] fix | timeline | the 2015 "Alexis cheating" was a 2009 event, and master-timeline.md was half non-events
- Operator: "There's an error in the wiki that shows up several places. It infers that Alexis cheated on me having something to do with the day before I met Annie. This was something from 2009 with no connection to 2015. It was also just an online thing and not in person." Second directive: a quality-control pass on the newly added timeline section — "there is a lot of disconnected things being framed as events... keep it over 2000 total REAL events and get rid of the nonsense."
- **The error, and why it survived so long: nothing was misquoted.** The message is real, correctly transcribed and correctly timestamped — `2015-11-28 19:08:18 | Sent | Lex cheated on me 2 weeks in after I moved her to fla`. It was filed under the date it was **sent** rather than the date it **describes**. The two lines immediately before it name the subject explicitly: `19:07:52 "I love this it's the exact opposite way I started my last relationship"` → `19:08:03 "Like I truly trust you"` → the cheating line. Dan is telling Annie how the *previous* relationship **began**. "Two weeks in" is two weeks into the Alexis relationship, which started in 2009 at Full Sail in Winter Park — the Florida he had moved her to. Per the operator, online-only, not in person.
- **The residence record settles it, and the corpus confirms the specific week.** Per the operator, **Alexis lived in Florida exactly once, 2009–2010** — the Full Sail stretch, ending when she and Dan moved to Brooklyn together in April 2010. There is no second Florida move anywhere in her record, so "after I moved her to fla" has one possible referent. Independently, across the exact window the wiki placed her in Florida she is in Dan's Uniontown house: "Alexis is sloshed" (Nov 30), "I just heard lex on the phone with her parents" (Nov 30), Suz offering a car "if I get Alexis out" (Nov 30), "Helping lex leave" (Dec 1), "Alexis only left yesterday" (Dec 2). `alexis-armel.md` had additionally invented a table row, "~mid-Nov 2015 | Dan moves her to Florida," by back-computing "2 weeks" from the message timestamp; no source ever asserted it.
- **This pass then committed the same error it was fixing, and the operator caught it within the hour.** The first version of the correction argued partly from a 2016-01-18 message — *"I know but she leaves for fla this week"* — read as Alexis relocating seven weeks after the breakup. **"She" is Fran.** In context Dan is texting Annie about needing money for a tux: *"I went to grams and made a list of work to do for her tomorrow / Because I need a tux and shit"* → Annie: *"that's not until the end of February"* → *"I know but she leaves for fla this week."* He needed the paid work done before his grandmother left for her Florida winter — already documented on `fran-coldren.md` ("Fran's Florida winters"). A pronoun was resolved to the person the *passage* was about rather than the person the *conversation* was about, which is structurally the same failure as dating a message by when it was sent. Retracted from six pages; the argument now rests on the residence record, which never needed the 2016 message.
- **A new failure class, named:** message-date-as-event-date. Distinct from the `_all_now` filename trap (source overstates coverage) and the `sic semper` case (provenance precise and wrong): here the provenance is precise and *correct*, and the misdating is entirely in the reading. It is invisible to any check that verifies quotes against raw, because the quote verifies.
- **The correction strengthens the thesis it threatened.** `bond-switch-2015`'s single-bond switch survives and gets sharper: with the betrayal removed there is **no precipitating grievance** on Alexis's side, so a six-year bond closing in ~72 hours can no longer be explained as a justified response — and Annie was introduced *by Alexis herself* ("HAPPY ONE WEEK SINCE LEX HANDED YOU TO ME," Annie, Dec 1). The cheating was the one detail that made the switch look normal. Written back to `the-unbroken-bond` (the removed bullet was the only item in its sequence supplying a reason for the ending), `attachment-trauma-bond`, `uniontown-return-2013-2015`, `2015-2016-annie-relationship-start`, `timeline.md`, `annie-ulmer`, and restored to `full-sail-2008-2010` where the event actually belongs.
- **A systematic defect exposed in `LIFE_EVENTS_CALENDAR.md`:** it classifies by message date and keyword, so *any* retrospective mention lands in the wrong year. Its `💔 Cheating/Affair 84` count and the per-year event totals derived from it are upper bounds until re-derived. Flagged on the two pages that quote those counts.
- **`master-timeline.md` was rebuilt from a rule set rather than a sweep.** The 2026-08-14 page (1,798 entries) had no generator; it matched any date-shaped string and kept the surrounding prose. Roughly half were not events: truncated mid-sentence fragments ("with unusual precision, because Dan spent April 11, 2017 telling four"), the wiki's own `REVISED`/`CORRECTED` housekeeping, table headers ("| Metric | Value (measured 2026-07-18) |"), HTML comments, corpus-metadata rows, bare-year prose matches ("in 2002: From a production standpoint, the Kanye catalog is obligatory"), and duplicates.
- **New tool `bin/wiki-timeline`** (pure stdlib; `generate` / `audit` / `sample` / `rejects`). It reads only structural positions where pages record events — table rows, list items, bold date leads — and **reflows hard-wrapped paragraphs before extracting**, which makes truncated fragments impossible by construction. Rejections are reviewable rather than silent: `audit` breaks them down by reason, `rejects` prints them. Result: **2,015 real events, 1796–2026, from 313 pages** (Tier 1 481 / Tier 2 280 / Tier 3 1,254), with 500 dated candidates rejected as non-events.
- **Three false-reject bugs found by disbelieving the tool's own output**, each costing real events: `wiki/` in the file-metadata blocklist matched every wikilink in ordinary prose (616 rejects, nearly all wrong — fixed by rendering links to their labels first); a "N messages" pattern rejected real sentences that merely *contained* a count; and a Source column of filenames rejected whole tables of genuine events instead of just that column. Also caught: David McCullough's *1776* parsed as a date from a reading-list row.
- **Staleness cascade worked in full: 15 warnings → 1.** Nine pages closed with real RE-CHECKED blocks. Two of them carried the **unworked PR #110 cascade** flagged as the top resume point since 2026-08-14, which a date bump would have cleared silently — so it was worked properly: `totality-themes.md`'s Prediction 1 asserted the Annie bond "only ever closed when an outside party (Ellen Ulmer) forced the irreversible act," which `dormancy-not-exit` (2026-08-13) contradicts outright — **Dan issued the June 1 2026 severance himself and held it 52 days**. RETRACTED as written; restated on the distinction the old wording collapsed: *closures Dan can perform alone are the reversible kind, and the corpus contains no instance of him unilaterally producing an irreversible one* (the 52 days ended in the July recontact and reentanglement). The same day's Alexis correction supplied a third instance eleven years earlier — a six-year bond closed unilaterally in 72 hours, and the partner retained anyway. One matching frontmatter edge claim corrected.
- **`the-deferred-audit` got a confirmation rather than a reprieve:** its 2026-08-08 block already read the Alexis exit as "a substitution rather than a finding," which was its weakest clause while a betrayal sat in that week — a betrayal *is* a finding. With the betrayal moved to 2009 the clause is unqualified. The page's strongest instance got stronger by losing a fact.
- Gates: wiki-lint **458 pages / 0 errors** (10 warnings, down from 14 — master-timeline's orphan warning closed by linking it from the timeline index) · wiki-connect check **0 errors** (237 warnings) · wiki-climb check **458 pages, 27 with `synthesizes:`, 0 errors, 1 warning**. `bin/wiki-digest` and `bin/llm-publish` rerun.
- **Left open deliberately:** `fayette-return.md` (2026-08-11) is stale against `ancestry.md` (2026-08-14). That cascade belongs to the ancestry extraction pass, not this one; clearing it without reading what changed would be the prohibited move.
- Pages touched: `wiki/people/alexis-armel.md`, `wiki/mind/synthesis/bond-switch-2015.md`, `wiki/mind/synthesis/attachment-trauma-bond.md`, `wiki/mind/synthesis/the-unbroken-bond.md`, `wiki/people/annie-ulmer.md`, `wiki/timeline/periods/uniontown-return-2013-2015.md`, `wiki/timeline/periods/2015-2016-annie-relationship-start.md`, `wiki/timeline/periods/full-sail-2008-2010.md`, `wiki/timeline/events/timeline.md`, `wiki/timeline/index.md`, `wiki/timeline/master-timeline.md` (regenerated), plus RE-CHECKED blocks on `totality-themes.md`, `the-deferred-audit.md`, `dormancy-not-exit.md`, `single-channel.md`, `block-unblock-loop.md`, `dan-annie-fallout-verdict.md`, `estate-money-spine.md`, `supply-network.md`, `johnny-dealer.md`, `alias-as-periodization.md`. New: `bin/wiki-timeline`.

## [2026-08-11] climb | mind | totality-themes.md re-derived from the wiki's own T2/T3 layer — "The Irreversibility Firewall"
- Operator, after a discussion of what the wiki's ultimate purpose is (not archive-for-retrieval but "the full corpus... read not as individual nodes anymore, but as a comprehensive totality which creates the awareness of all variables needed to uncover deep and foundational drives and incentives"): "Yes so the full t2&t3 pass." Invoked the `wiki-rewrite` skill against `totality-themes.md` specifically, treating this as the meta-climb use case — the page's own sources reasoned from the wiki's synthesis layer, not from `raw/`.
- **The finding that motivated the rewrite:** `totality-themes.md` — the one page in the repo literally named for doing this — turned out to be the weakest-provenance page in `mind/`, not the strongest. Its spine (six themed sections: forensic method, low-trust architecture, accelerationism, political intensity, music, the "millennial witness") was a structured restatement of one raw AI-authored document, `TOTALITY_SYNTHESIS_2026-06-10.md`, never independently re-derived from the wiki's own T1→T2 climb the way every other T3 page on record was built. No falsifiers, no predictions, no dated evidence of its own — exactly the laundering failure `EXTRACTION_SPEC.md`'s source-tiers section exists to prevent, sitting on the repository's own capstone page.
- **The re-derivation.** Read all 27 T2/T3 `page_type: synthesis` pages in `mind/` against each other (theses, rule statements, falsifiers, correction histories) rather than against raw sources. Found the same mechanism recurring under different names across four independently-derived pages that never cited each other: [[wiki/mind/synthesis/the-deferred-audit]]'s "provenance decides when the audit fires, not whether" (imposed objects audited on contact; chosen objects only after they fail, because auditing a choice risks a verdict on the chooser, routed through Core Axiom 1, "not exceptional = worthless"); [[wiki/mind/concepts/the-cool-metric]]'s "authenticity = involuntary" (the one trusted category is the one that was never a decision); [[wiki/mind/synthesis/the-embedded-objective]]'s own unresolved gap (three purely self-set projects — MNEME, DANMODEL, the AI video essays — that stalled despite no assignment to hide behind, which that page's own author couldn't explain); and [[wiki/mind/synthesis/dormancy-not-exit]]/[[wiki/mind/synthesis/the-unbroken-bond]]/[[wiki/mind/concepts/attachment-model]]'s "nothing gets deleted, nothing self-closes absent an explicit signal from outside."
- **The unification, stated as one rule ("The Irreversibility Firewall"):** an object, relationship, or act is trusted and left alone exactly to the degree it has never been converted into an irreversible, externally-exposed fact someone (including Dan's own audit apparatus) could render a verdict on; anything at risk of that conversion is audited immediately, deferred indefinitely, or never finished. This resolves the-embedded-objective's own stated gap (self-origination defeats the imposed-audit risk but not the exposure risk — completion itself is the irreversible act, regardless of who set the goal) and explains why block-unblock-loop's Annie bond needed an *external* force (Ellen, informed directly) to close after 127 declared exits: closing it from the inside would have been the one irreversible act the architecture is built to avoid.
- **Four dated predictions derived and instantiated**, each against 3+ existing T2/T3 pages spanning multiple domains: (1) no-delete/retention (dormancy-not-exit, the-unbroken-bond, attachment-model, node-locking, block-unblock-loop); (2) trust tracks absence-of-authorship (the-cool-metric, alias-as-periodization, chaos-preference); (3) completion is the specific act policed hardest (the-embedded-objective, acquisition-drive's own falsified prediction, institutional-out); (4) the vertical axis is distrusted first because auditing it is free (vertical-authority-skepticism, politics/axioms). Each carries a stated falsifier; two (predictions 2 and 4) are flagged honestly as instantiated but not yet stress-tested for a counter-instance — a named gap, not a silent claim.
- **What survived unforced:** the existing "Cross-Corpus Extensions" section (added 2026-07-15, independently derived from primary corpora — the intake-metabolism constants, the migration grammar, the housing clock, the output-port bandwidth-war finding) was kept nearly intact and cross-tied to the new spine rather than rewritten; it converges on the same completion-avoidance mechanism (prediction 3) from entirely different data, which is noted as the strongest kind of corroboration available. The already-correct 2026-08-11 Rick retraction inside that section is undisturbed.
- **Write-back, done properly rather than left as a dangling doctrine page.** Full `synthesizes:` list added (27 pages — this page had none before). Every member page received a real, argued `component-of` inverse edge back to `totality-themes` (two pre-existing mismatched edge types fixed: `block-unblock-loop` was `parallels`, `single-channel` was `instance-of`; both corrected to `component-of` to match the established repo convention, verified against `block-unblock-loop.md`/`annie-ulmer.md`'s own working pair). 19 new edges added from scratch, 6 existing edges corrected or refreshed, 25 `date_modified` fields bumped to match.
- **Staleness cascade:** one page (`wiki/interests/food-and-diet.md`, stale against `the-cool-metric.md`'s date bump) checked and closed unaffected — the edit that moved the date only added a connection, didn't touch the food/music jurisdiction dispute the two pages already track.
- Gates: wiki-lint 456 pages / 0 errors (13 warnings, unchanged: the new page's 55KB size warning is advisory) · wiki-connect check 0 errors / 234 warnings (unchanged — every new/fixed edge matched cleanly) · wiki-climb check 456 pages, 27 with `synthesizes:`, 0 errors, 0 warnings. `bin/wiki-digest` and `bin/llm-publish` rerun.
- Pages touched: `wiki/mind/synthesis/totality-themes.md` (rewritten spine, frontmatter, connections), plus inverse-edge write-backs on `the-deferred-audit.md`, `the-cool-metric.md`, `the-embedded-objective.md`, `acquisition-drive.md`, `institutional-out.md`, `dormancy-not-exit.md`, `the-unbroken-bond.md`, `block-unblock-loop.md`, `attachment-model.md`, `conflict-architecture.md`, `dan-annie-fallout-verdict.md`, `vertical-authority-skepticism.md`, `alias-as-periodization.md`, `single-channel.md`, `node-locking.md`, `instrument-is-subject.md`, `chaos-preference.md`, `supply-network.md`, `estate-money-spine.md`, `fayette-return.md`, `intake-constancy.md`, `mind/politics/axioms.md`, `orchestration-and-voyeurism.md`, `erotic-architecture.md`, `music-as-identity.md`, `political-psyops.md`, `millennial-digital-witness.md`, plus a staleness re-check on `food-and-diet.md`.

## [2026-08-11] correction | people | the "decade of silence" with Rick was wrong — full record recovered, childhood testimony captured, worldview mismatch documented
- Operator asked for a deep dive into the personality/worldview incompatibility behind current-day dread around Rick and his partner Lisa (narrow conversational register: high school football, Pittsburgh-specific media/memes). Mid-investigation, cross-checking a 2024 sent message against `all_imessages_complete_dump.txt` exposed that this session's own prior finding — published same day, two PRs — was built on an incomplete source.
- **The error, owned plainly:** `imessage_7243667777_both_all_now.csv`, trusted as "the one export with both sides, all time," actually held 43 of the channel's true **1,600+ messages**. The published "12-day burst, then a decade of unanswered inbound" was false. The real record shows real repair within three weeks of the December 2015 friction, then a warm, high-volume correspondence through 2020 (1,177 messages) and again in 2023–24, including a real financial-trust wound named directly by both sides (Jan–Apr 2018: "I would rather u let me be father than protector, but u don't... you make it a point to keep me out of ur life") and Fran Coldren's April 2018 death vigil narrated to Rick in real time.
- **The real held silence is recent and precisely dated, not decade-old:** total non-response from Dan since **February 26, 2025** — the day after Dan himself proposed a get-together and Rick accepted — running through a documented Aug 2025–Jan 2026 tail (13 unanswered check-ins, several in an infantilizing/surveillance register: "Is there some reason that I'm in timeout?"; "Have you been a good boy this year? Santa's watching!"). It starts the moment Dan moved back to Uniontown (Feb 22, 2025) — proximity-triggered, not amputation-shaped.
- **New finding: Lisa.** Rick has had a partner, Lisa (a teacher), continuously since at least Dec 27, 2015 — a decade of presence never once written into the wiki until this pass, despite dozens of primary mentions. New stub page `wiki/people/lisa-frank.md`. A household member "Syd" (Lisa's likely child) is also newly documented, unconfirmed relationship.
- **New primary testimony, dictated directly by the operator and captured to raw/:** a childhood pattern of idiosyncratic control — Rick's confrontation of [[wiki/people/tan-calabrese]] over a harmless Angelfire site, conducted by humiliating Dan in front of him; and a recurring practice of pulling Dan out of rooms at parties/events/stores to scream at him where onlookers could still hear, independently named by Dan's aunt Wendy as the source of Dan's present reluctance. Written into `rick-frank.md`, `tan-calabrese.md` (previously an orphan stub, now resolved), and added as a second candidate origin (predating the 2005 hinge) on `vertical-authority-skepticism.md`.
- **The worldview/register mismatch, actually documented:** the sports/Steelers/golf/Pittsburgh-regional register is real and constant across the whole decade, but the record complicates rather than confirms a pure "nothing in common" read — Rick also sends a 25-hour history podcast and a Julius Caesar documentary series in 2024 that lands directly on Dan's own separately-documented Roman Republic interest, and Dan's uptake is genuine. The finding: a narrow, historically publicly-enforced tolerance band, with a real but numerically minor shared register buried inside a much larger volume of small-town/sports material.
- **Corrections propagated and retracted, not silently patched, across every page that carried the false claim:** `block-unblock-loop.md` (the Rick row RETRACTED from its "held-block control case" argument — the page's claim that Dan's severance capacity is proven now has no clean surviving instance, recorded as an open gap rather than papered over with a substitute) and `totality-themes.md` (the "Rick-file rhyme" RETRACTED, the domain-crossing "amputation is confirmed" bullet downgraded back to [INFER]).
- **Staleness cascade, two pages, both closed as unaffected:** `wiki/mind/politics/axioms.md` and `wiki/mind/synthesis/alias-as-periodization.md`, RE-CHECKED.
- **Doctrine update:** the per-contact-CSV trap entry added earlier the same day (see the entry below) was itself amended — its praise of the 43-line file as "the single most complete... record" was the error in the process of being made, caught and rewritten before this correction was even finished. The rule now: read the per-contact CSV for orientation, but reconcile against the full dump before publishing any completeness claim.
- Gates: wiki-lint 451 pages / 0 errors (12 warnings, down from 13 — the tan-calabrese orphan warning resolved) · wiki-connect check 0 errors / 216 warnings (unchanged) · wiki-climb check 451 pages, 23 with `synthesizes:`, 0 errors, 0 warnings. `bin/wiki-digest` and `bin/llm-publish` rerun.
- New pages: `wiki/people/lisa-frank.md`. Pages touched: `wiki/people/rick-frank.md`, `wiki/people/tan-calabrese.md`, `wiki/mind/synthesis/vertical-authority-skepticism.md`, `wiki/mind/synthesis/block-unblock-loop.md`, `wiki/mind/synthesis/totality-themes.md`, `wiki/mind/politics/axioms.md`, `wiki/mind/synthesis/alias-as-periodization.md`, `wiki/people/index.md`, `EXTRACTION_SPEC.md`.
- New raw file: `raw/people/captures/2026-08-11_051311_rick-childhood-control-and-humiliation.md`.

## [2026-08-11] process | EXTRACTION_SPEC.md | two new moves, generalized from the Rick pass — per-contact CSVs, dangling-citation chasing
- Operator, after seeing the Annie-parents finding fall out of the Rick correspondence pass: "think about how that happened and if we can optimize to do more of that." This is a doctrine change, not a content ingest — codifying what actually produced the finding so it happens by method next time, not by accident.
- **What actually happened, reconstructed:** (1) an AI dossier's vague, unattributed quote ("his father's perceived financial judgment") was traced to a specific phone number by grepping the exact phrase against the raw message exports, then resolved to Rick via the Facebook address book — the existing contact-identity trap's resolution move, applied to a *quote* instead of a *page*; (2) that number turned up a per-contact CSV export (`imessage_<number>_both_all_now.csv`) that had never been cited anywhere, small enough (43 lines) to read to full exhaustion in one pass, and more complete for that one relationship than either general dump; (3) reading it in full surfaced a message that happened to date-match a citation another page (`annie-ulmer.md`) had been carrying for weeks without ever explaining — a fear-of-abandonment quote with a date but no stated cause.
- **Two new moves added to `EXTRACTION_SPEC.md`:** a new "Traps by source type" entry naming per-contact `imessage_<number>_both_all_now.csv` exports as a distinct, easily-overlooked, high-value source category (with instruction to check `raw/self/message-csv/` for every known number before writing or revising a message-based person page); an extension to the existing contact-identity trap entry naming quote-attribution as the same resolution problem as page-identity; and a new **Move 8, "Follow a dangling citation into someone else's channel"** — when a page dates a quote precisely but never explains it, that is a flag to search the same date across every other channel for the people involved, not just the subject-to-page-owner channel. `## The seven moves` renamed `## The eight moves`; cross-references in `STRATEGY.md` and `INGEST_RUNBOOK.md` updated to match.
- **Deliberately not done:** no attempt to retroactively audit every existing person page against the new per-contact-CSV check — that's exactly the kind of standing-work item `BACKLOG.md` exists for, not a thing to rush through under an "ASAP" instruction that was actually about the doctrine file, not a corpus-wide sweep.
- Gates: wiki-lint 450 pages / 0 errors (13 warnings, unchanged) · wiki-connect check 0 errors / 216 warnings (unchanged) · wiki-climb check 450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings.
- Files touched: `EXTRACTION_SPEC.md`, `STRATEGY.md`, `INGEST_RUNBOOK.md`.

## [2026-08-11] ingest | people | the December 2015 Rick rupture, recovered two-sided and verbatim — mechanism behind the present-day estrangement
- Operator follow-up, mid-session: "see if you can't find the source of the reason that i am so reluctant to talk to him... it's like the loudest silence. a constant perpetual passive-aggression, on-guard posture, all fun must be approved by management." Chased it by finding the one export in the corpus with both sides of Rick's specific channel — `raw/self/message-csv/imessage_7243667777_both_all_now.csv` — never previously used as a source on `rick-frank.md`.
- **The mechanism is now dated and verbatim, not inferred.** On Dec 2, 2015, Dan promised Rick "good news," it collapsed hours later ("Nevermind. There's no good news"), and that night Dan disclosed — the corpus's most vulnerable message to Rick on record — that Annie's parents had just tried to "squash" the four-day-old relationship over Dan's "bad reputation." Rick offered support. Eleven days of ordinary check-ins followed, then, when Dan didn't answer fast enough on Dec 13: "Yeah I get blown off again," and three days later (recovered from the separate `all_imessages_complete_dump.txt` export) "I guess that u don't need me anymore so I get kicked to the curb." **That is the last message Dan ever sent to this number.** The two-sided export shows zero outbound messages from Dan for the following decade, against 13 dated inbound reaches in 2025–26 alone — several in an infantilizing/surveillance register ("Is there some reason that I'm in timeout?"; "Have you been a good boy this year? Santa's watching!").
- **Corrects a standing figure.** `block-unblock-loop.md` and `rick-frank.md` both described this as "a 12-day outbound burst." The verified per-number record shows a single ~20-hour outbound window (Dec 2 evening–Dec 3 midday) — a sharper asymmetry than previously stated, not a softer one. CORRECTED blocks added on both pages; the 2025–26 reach count corrected from 12 to 13.
- **A second, smaller finding fell out of the same file:** the Dec 2 "fear of abandonment" message already cited on `annie-ulmer.md` had no documented cause. It now does — Annie's parents' attempted veto, recovered from Rick's side of the corpus — added there as a one-paragraph deepening, not a rewrite.
- **Staleness cascade, two rounds, all closed with real RE-CHECKED blocks, zero reversals.** Round 1 (six pages: `attachment-trauma-bond`, `dan-annie-fallout-verdict`, `estate-money-spine`, `fayette-return`, `supply-network`, `the-unbroken-bond` — all flagged against the edited `rick-frank.md`/`annie-ulmer.md`): every dependency checked was a date, a money figure, or a generational-departure fact untouched by the new relational detail — none required revision. Round 2 (three pages flagged against the Round-1 RE-CHECKED edits themselves: `dormancy-not-exit`, `single-channel`, `the-deferred-audit`): confirmed unaffected, since Round 1's edits added confirmation notes, not new claims.
- Gates: wiki-lint 450 pages / 0 errors (13 warnings, unchanged) · wiki-connect check 0 errors / 216 warnings (unchanged) · wiki-climb check 450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings. `bin/wiki-digest` and `bin/llm-publish` rerun.
- Pages touched: `wiki/people/rick-frank.md`, `wiki/people/annie-ulmer.md`, `wiki/mind/synthesis/block-unblock-loop.md`, plus RE-CHECKED notes on `attachment-trauma-bond.md`, `dan-annie-fallout-verdict.md`, `estate-money-spine.md`, `fayette-return.md`, `supply-network.md`, `the-unbroken-bond.md`, `dormancy-not-exit.md`, `single-channel.md`, `the-deferred-audit.md`.

## [2026-08-11] ingest | people | rick-frank.md correspondence review — two unmined sources, findings written back from three pages that already had them
- Operator asked for a sweep of every raw source touching Rick Frank correspondence. Two files turned out never to have been mined: a 2010–2015 Facebook Messenger thread (`raw/self/facebook/.../rickfrank_-wir6jjh_a/message_1.html`, Rick's outgoing side only — Dan's replies were not preserved in the export) and `raw/self/dox-scan/Gemini-_58.txt`, which had already been mined for `wiki/self/chats/gemini-58.md`, `wiki/places/424-bedford-ave.md`, and `wiki/work/creative-license.md` but never written back to `rick-frank.md` itself — a CLAUDE.md rule-2 violation sitting on three pages at once.
- **New section: the 2010 NYC bankroll.** Rick funded the exit from Fayette directly — a Feb 18, 2010 apartment-hunting trip to Williamsburg and a standing $2,000/month offer "while you intern," the alternative to Dan's stated preference for an Entourage-style West Hollywood move. A Feb 22, 2010 Facebook message ("looks like the nyc deal is off") shows the arrangement nearly collapsing four days later, unresolved on record; the move went ahead on schedule regardless. This is the single largest act of paternal support in the corpus and was previously undocumented on the page that is about Rick.
- **The "brief and logistical" characterization is real but not the whole register.** The Facebook thread confirms it at scale (skiing, wedding, hockey invites, all unadorned) but also surfaces a register the profile-dossier sources never captured: impatient insistence when Rick wants something handled ("Enough bullshit. Call me ASAP!"; "You think I'm fucking kidding about sending me that information about the landlord?"). Separately, the 2012 Creative License payroll dispute (already on `creative-license.md`, never wired back) shows a third register — Rick as active tactical coach ("You sound so desperate. That is what kevin wants. We'll talk about a strategy for this."). Register shifts with the situation (favor request vs. outside-authority fight vs. emotional validation), not a fixed trait.
- **Connections wired both ways:** `rick-frank.md` ↔ `424-bedford-ave.md` (`causes`/`caused-by`, the funding claim) and `rick-frank.md` ↔ `creative-license.md` (`component-of`/`contains`, the coaching claim).
- Gates: wiki-lint 450 pages / 0 errors (13 warnings, unchanged) · wiki-connect check 0 errors / 216 warnings (unchanged) · wiki-climb check 450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings. `bin/wiki-digest` and `bin/llm-publish` rerun.
- Pages touched: `wiki/people/rick-frank.md`, `wiki/places/424-bedford-ave.md`, `wiki/work/creative-license.md`.

## [2026-08-08] ingest | people | tuquick identity unmasked (Jerel Wayne Coles)
- Operator supplied a forensic background-check capture (FOREWARN database) identifying "tuquick" as **Jerel Wayne Coles**, age 36, current address 106 Nassau St, Uniontown, PA 15401. Filed to `raw/people/captures/2026-08-08_190122_identity-of-the-interloper.md`.
- **The identity correction is substantive, not cosmetic.** Coles has a documented criminal record in PA court databases: 9 distinct incident clusters across 2008–2025 (traffic violations, disorderly conduct, harassment with physical contact, two DUIs including a BAC ≥ .16 charge, and a 2025 criminal mischief charge). The 64 raw court records collapse to 9 incidents after de-duplication across AOC/AUJS/Court of Common Pleas/citation/disposition stages. Added as a new `## Criminal record` section on `wiki/people/tuquick-17248123683.md`.
- **He is NOT target G** — explicitly unresolved per all existing sources.
- **The July 2026 unnamed interloper question is sharped but still open.** Coles's known phone numbers — `(724) 812-3683` (mobile) and `(724) 628-7133` (residential) — do not appear in the July 2026 message export. Circumstantially plausible (Uniontown resident, harassment conviction, identical interloper role) but not confirmed. Updated the "Is he Tuquick?" section on `wiki/people/the-unnamed-man.md` with a REVISED block.
|  - **Staleness cascade handled, not date-bumped.** `bin/wiki-climb check` flagged `dan-annie-fallout-verdict.md` stale against the modified tuquick page. Re-checked: the verdict's claim rests on Tuquick's June 15 defection behavior (compulsive liar + drug addiction read, independent-validation exhibit), not on his anonymity. The unmasking is additive identity data — no conclusion altered. RE-CHECKED block added.

## [2026-08-09] ingest | self/timeline/people/interests | extreme-sports era expanded with visual documentation

**Source:** `/Volumes/MUSIC/alias/XXX/2026-08-09_122727_extreme-sports.md` — field capture of childhood extreme-sports trajectory (tennis, inline rollerblading, terrain-park skiing, Uniontown social world).

**Pages written:**
- `wiki/interests/extreme-sports.md` (expanded with skateboard culture mainstream arc, class-signaling connections, seven-springs terrain-park development, visual atmosphere section)
- `wiki/people/matt-kraus.md` (new page, co-occurs with extreme-sports at Camp Woodward)
- `wiki/people/nathan-king.md` (new page, co-occurs with extreme-sports at Camp Woodward)
- `wiki/people/tom-wallisch.md` (updated sources, provenance for pretzel/SuperUnknown claims)
- `wiki/people/tan-calabrese.md` (reconciled duplicate: tancredi-calabrese.md deleted, identity correction recorded)

**Gates:** wiki-lint 0 errors · wiki-connect check 0 errors · wiki-climb check 0 errors, 0 stale.
**Tag added:** `non-monogamy` to VALID_TAGS for the annie-alexis-reunion page.
- Gates: wiki-lint 438 pages / 0 errors · wiki-connect check 0 errors / 208 warnings · wiki-climb check 438 pages, 21 with `synthesizes:`, 0 errors, 0 warnings.
- Pages touched: `wiki/people/tuquick-17248123683.md` (rewritten with identity + criminal record), `wiki/people/the-unnamed-man.md` (REVISED + connection updates), `wiki/mind/synthesis/dan-annie-fallout-verdict.md` (staleness re-check).
- Raw file filed: `raw/people/captures/2026-08-08_190122_identity-of-the-interloper.md`.

## [2026-08-03] ingest | legal | court blotter photo — the arrest is now primary-documented, and a wiki inference was wrong
- Operator supplied a photograph of a Fayette/Greene county newspaper court blotter. Filed as `raw/legal/documents/2015-02_fayette-court-blotter-possession-charges.png` with a transcription sidecar `.md`. **This is the corpus's first primary documentary record of the arrest**, which until today rested entirely on Dan's own retrospective telling.
- The entry, verbatim: *"Daniel Gillingham Frank, 26, of Uniontown was charged with possession of a controlled substance, possession of a small amount of marijuana and possession of drug paraphernalia,"* under Magisterial District Judge **Michael Metros**, in a column covering filings "between Feb. 17 to Feb. 19."
- **Identification is solid.** Full legal name matches `family-tree.md` exactly; Uniontown matches; and the printed age of 26 is the load-bearing datum — born 1988-11-01, Dan is 26 only between November 2014 and November 2015.
- **The three charges match the capture exactly**, told ten years later with no access to the clipping. That is a meaningful reliability datum for the operator's testimony generally, and worth remembering the next time a capture's detail looks too specific to trust.
- **A wiki inference written earlier the same day was wrong, and is recorded as wrong rather than patched.** The page had judged the capture's "It's sometime in early 2015" to be "almost certainly too early," reasoning that a February arrest would leave an implausible nine-month gap before the December 2015 barracks trips. The blotter settles the filing to **February 17–19, 2015**. A twelve-month arrest-to-ARD interval is ordinary in Pennsylvania; the gap the inference rejected is just what the process takes. Noted on the page: the correction instinct calibrated on the Fran captures being off by a year over-fired here.
- **The new date breaks a claim elsewhere.** `self/overview.md` said Annie began "four weeks after" the arrest; February 2015 to Thanksgiving 2015 is **nine months**. Corrected.
- **And it opens a contradiction that did not exist before.** The capture places the arrest while Alexis was still hidden at 337 Saratoga and *before* the move to 155 Virginia Ave — but `155-virginia-ave.md` dates that residence from **January 2015**, a month before the blotter filing. Flagged with reciprocal `contradicts` edges on both pages, not resolved; the most economical reading (concealment ended ~January, arrest fell just after the move) is offered as an inference and explicitly not adopted. A lease or a dated message from the move would settle it.
- **An unexplained coincidence recorded for a future pass:** February 17 appears three times in the record — the 2015 blotter window opens on it, the 2016 ARD hearing is dated to it, and `self/index.md` gives 2010-02-17 as the Suboxone start. Could be docket scheduling, could be an artifact propagated through earlier passes. Worth checking before any of the three is leaned on.
- Staleness handled properly: editing `155-virginia-ave` made `dormancy-not-exit` stale. Re-checked rather than date-bumped — what that page draws from the address is lair-continuity, dated to the November 2015 occupant swap and unaffected by whether the lease began in January or February. RE-CHECKED line recorded.
- Gates: wiki-lint 438 pages / 0 errors · wiki-connect check 0 errors / 214 warnings · wiki-climb check 0 errors, 0 warnings.

## [2026-08-03] ingest | legal | factstory brief #5 — "The Arrest (the real one)"
- **Four of the brief's five entries were already ingested on 2026-08-02** (Jay Lauer, both Fall of Fran tellings, Perspective: Complete Objective — all four raw files verified on disk). Entry 5 is the only new payload, and it is a correction rather than an addition.
- Filed `raw/legal/captures/2026-08-02_200741_the-arrest-the-real-one.md`.
- **The wiki had the 2015 arrest wrong, and the operator resolved it mid-pass: there are two separate events, weeks apart, and both are real.** The page `2015-retail-theft-arrest` had fused a Combos retail theft with a drug-possession arrest, attributing the lawyer, the ARD, the Judge Wagner hearing and the family drama to a snack-food theft. The arrest was a 3am traffic stop in downtown Uniontown on a lemon run for Suz, in Fran's uninspected car, ending in a pretextual impound, an inventory search, and three charges — marijuana, paraphernalia for a one-hitter, and **a Class B controlled-substance count over residue in an empty cocaine bag**.
- New page **`wiki/legal/2015-possession-arrest.md`** carries the arrest and all the case material moved off the theft page. New page **`wiki/people/jack-connor.md`** (gap closed — the lawyer's full name; the DA of the period barred ARD for any cocaine charge, residue or not, so the diversion was won against a categorical policy at a cost of several thousand dollars; corroborated independently in the message dump at a casino cash-claw drawing). New page **`wiki/people/lucy.md`** — Suz's blind Jack Russell, in Dan's arms at the moment of arrest, and separately corroborated in raw as having been put down days after Fran died "because we wanted to get all the awful-ness out of the way at once."
- `2015-retail-theft-arrest` rewritten as the Combos incident proper, with a REVISED block recording the conflation. Nothing deleted; the trooper's "DID YOU STEAL MORE COMBOS" and Annie's running joke stay there as what they are — the strongest evidence the theft was real and chargeable.
- **Two contradictions flagged, neither resolved.** (1) The page has said since 2026-07-13 that Dan "consented to a breath search" during the stop; the capture says he was never asked for field sobriety or a roadside PBT. Both are his own testimony ten years apart; the economical reconciliation (a chemical test later at the barracks) is labelled an inference, not adopted. (2) The Christo Coan October 2017 "I already got a DUI" line is sharpened rather than settled by "my first and only real arrest" — a DUI by citation without booking would make both true.
- **Dating flagged, not silently corrected.** The capture opens "early 2015"; the aftermath runs Dec 2015–Feb 2016, and Dan places the night inside the ~4 months Alexis was secretly housed at 337 Saratoga, which brackets it to 2015 before the November bond switch. Recorded as 2015-before-November with the drift noted — the same one-directional capture drift the Fran captures showed.
- **A claim written yesterday was partly falsified and corrected in place.** `the-embedded-objective` said the six months of court-assigned ARD probation "appear nowhere." The capture says Dan "completed that without incident," so the serving is now on the record. The rule survives narrowed: the getting carries five dated contemporaneous traces, the serving one retrospective clause a decade later — a density asymmetry, not an absence.
- `acquisition-drive`'s episode table also corrected: the arrest was not for snack food. It now carries four rows, two of them weeks apart in 2015, which is stronger evidence for the page than the original single row — the drive was producing a rate, not one anomalous night.
- Repointed 8 inbound references across `self/overview`, `155-virginia-ave`, `vertical-authority-skepticism`, `rick-frank`, `christo-coan`, `nemacolin-caddying` and the legal index from the theft page to the arrest page, since all of them meant the ARD.
- Gates: wiki-lint 438 pages / 0 errors · wiki-connect check 0 errors / 214 warnings · wiki-climb check 0 errors, 0 warnings.

## [2026-08-02] climb | mind | the-embedded-objective (1 synthesized, 2 rejected)
- **Cluster 26 climbed, and the audit that earned it falsified the rule it was queued to prove.** The queue entry specified the work: audit the employment and abandoned-project records for an externally assigned goal pursued at cost comparable to the six-month Fran vigil. **Two were found and both dwarf it** — 41 months at `au-zaatar`, 43 at `nemacolin-caddying`. The candidate sentence ("no instance of comparable cost absorbed for an externally assigned goal exists") is false.
- New page **`wiki/mind/synthesis/the-embedded-objective.md`** (T2, 8 members, 4 domains — work/mind/timeline/legal). Rule: **Dan never sustains an assignment, he sustains a private objective installed inside one**; the commitment ends when the payload is destroyed, not when the work gets hard. Diagnostic property that keeps it falsifiable: the embedded objective is separable from the role and usually adversarial to it (the tip split, the 18-month night-class alibi, the shed cash-tip territory).
- **Controls carry the argument.** `bfs-foods`: ~1 month, no out installed, no private objective — ended at the first genuinely assigned demand ($50 drawer). Against Au Za'atar, which survived three months of the employer deliberately cutting hours to force a quit and ended only when the territory was destroyed. `caviar-courier`: an app offers nothing to embed in, and produces 12 months of availability with **no tenure**. `2015-retail-theft-arrest` is the hardest case and holds — the ARD *acquisition* is 5 dated events in 10 weeks, the 6 months of assigned probation appear nowhere.
- **A second correction the queue entry did not anticipate.** MNEME (never built past spec), the DANMODEL blind eval (no results file, may never have run) and `ai-video-essays` (stalled at planning) were all entirely self-set and none completed. **Self-origination is necessary for the engine to fire and not sufficient for it to finish** — `acquisition-drive`'s "runs to completion more or less independently of cost" is now bounded.
- **Falsification recorded, not edited away** (SYNTHESIS_SPEC "Predictions and their resolution"): `acquisition-drive` keeps its prediction paragraph and carries a PREDICTION FALSIFIED block under it. Its stale `chaos-preference` inverse claim ("inert toward everything assigned to him") corrected in the same pass.
- Write-back complete: all 8 members carry an `instantiates`/`evidences` edge stating what they turned out to be evidence *of*, plus prose on the six where the finding is load-bearing (au-zaatar, bfs-foods, nemacolin-caddying, institutional-out, caviar-courier, 2015-retail-theft-arrest). `parallels` edges to `vertical-authority-skepticism` and `the-deferred-audit`.
- **Two hypotheses tested against raw and REJECTED, recorded in `synthesis-queue.md` so nobody re-runs them.** (1) *Ruptures cluster in the small hours* — 371 rupture-marked outbound messages against an 88,945 baseline gives 00:00–05:00 a lift of only **1.19x**, with inconsistent peaks; no circadian signature. (2) *The corpus has an annual rhythm* — the December 15.98% vs June 5.3% spread is entirely truncated-year contamination (the record opens Nov 2015, so 88.6% of 2015 is December; it ends Aug 2026, so 39% of 2026 is January). Per-year peak months are 12/5/11/6/8/9/7/9/1. **Any future month-of-year work on this corpus must drop 2015 and the current year first.**
- Altitude: 20 -> 21 climbed pages, T2 11 -> 12.
- Gates: wiki-lint 435 pages / 0 errors · wiki-connect check 0 errors / 214 warnings · wiki-climb check 0 errors, 0 warnings.

## [2026-08-02] ingest | timeline+people+mind | the re-entanglement — Annie thread through 2026-08-02
- Filed `raw/self/message-csv/imessage_export_2124702449_20260802.csv` (4,848 rows, 2026-05-04 → 2026-08-02). New window past the last filed export: **1,880 messages** across 8 days, 2026-07-26 05:22 → 2026-08-02 18:10.
- **The queue's top item is answered.** The July 26 goodbye broke in **eighteen minutes**. All three open questions on `july-2026-recontact` close: the parents WERE contacted (06:22 July 26, first executed maternal-disclosure threat in the corpus); the exposure threat was executed AND retracted the same day (transcript.html up 05:36, down 18:05 on one request from Annie); the disappearance did not happen.
- New page `wiki/timeline/events/july-august-2026-reentanglement.md` — the seventeen hours of July 26, the procurement schedule (6 meetings / 5 handoffs / 6 days, tabled with places and amounts), the July 28 disclosure standoff, the four states of the apparatus, the scratch-off wager, and the August 2 apology.
- New page `wiki/people/the-unnamed-man.md` — the third party, written around the finding that **Dan has deliberately refused to learn his name** and states the reason twice. The corpus's sharpest counter-example to the forensic method's claim to generality: the instrument has an off switch and its criterion is emotional cost, not difficulty.
- **A gap `supply-network` had carried since it was written is closed: "Bop" is a person.** Not a verb or a term for sourcing through Dan — a man who house-calls at noon daily, whose property Dan maintains in part-payment, who sits on the porch with Felix, and who sourced all five handoffs. Felix confirmed as a separate person with no supply role. The network did not collapse with the Tom node; it was replaced by a higher-availability one.
- **`block-unblock-loop`'s standing prediction resolved, and a new rule falls out of it.** It predicted the July 26 goodbye would not hold, on dependency grounds; confirmed at 18 minutes. Both threat types appear in the window 48h apart and resolve OPPOSITE ways — the impulsive disclosure executed in 16 minutes, the deliberated one announced 12 hours ahead and never sent. New rule: **announcement is the mechanism of non-execution.** Falsifier queued.
- **`dormancy-not-exit` gains its mechanism, stated by the subject:** "My brain can't cross out that part of my life that I love unless I know that you don't feel that way." The closing operation requires a counterparty, and across 1,880 messages of direct demand Annie never performs it. Reframes the member cases — ties persist because nobody says the sentence, not because Dan holds on.
- **Metric correction on `annie-ulmer`:** the message-count ratio is the unstable metric (0.79–1.92 monthly across the final year; 1.06 in this window, which reads as reciprocity and is not). The word-volume ratio is what to quote — 2.88 here against 2.95 all-time, verified on two independent exports. Annie's median message is **4 words** in both windows; the apparent parity is her taking more turns of the same size while Dan's median grew 8→11.
- Also written back: `forensic-method` (the four states + the wiki proofread by being shown to its own subject, which is the origin of today's bond-switch subject-reversal correction, timestamped 22:04 July 31); `milo` (the dog is the instrument, not only the channel — all four hostility→warmth transitions run through him, and Dan speaks in his voice; Betty's final weeks recorded, uncorroborated); `annie-ulmer` (new section, 4 chronology rows, infobox, changelog); `suzanne-frank`, `attachment-model`, `dan-annie-fallout-verdict`, `tuquick-17248123683` (inverse edges with real claims); both indexes.
- Not adjudicated, consistent with the prior page: the rape allegation. New facts recorded — Annie states he admitted it, no report made as of Aug 2, and Dan says the word 22 times to her 1.
- Gates: wiki-lint 434 pages / 0 errors · wiki-connect check 0 errors (214 warnings, down from 220) · wiki-climb check 0 errors, 0 warnings.

## [2026-07-26] climb | all | SYNTHESIS_SPEC + bin/wiki-climb — the wiki becomes an input to itself
- New governing file `SYNTHESIS_SPEC.md`: the altitude ladder (T0 raw / T1 ground / T2 junction / T3 doctrine, tier computed not declared), the `synthesizes:` frontmatter field (wiki pages a page REASONS FROM, as against `sources:` for raw paths), the staleness rule, the prediction/falsification rule, the CLIMB operation protocol, and five named anti-patterns.
- New tool `bin/wiki-climb` (check / audit / candidates), pure stdlib. `check` is now a third commit gate. `candidates` writes `synthesis-queue.md` (25 clusters mined from 323 scored).
- Migration: 24 pre-existing cases of wiki pages cited inside `sources:` moved to `synthesizes:` across 7 pages — the exact confusion the new field exists to end. `synthesizes:` populated on the junction/doctrine layer (block-unblock-loop, supply-network, estate-money-spine, attachment-trauma-bond, dan-annie-fallout-verdict).
- Staleness: the new check surfaced 6 real debts on first run. All cleared properly — premise re-read, one-line finding recorded — not date-bumped. Clearing 463-morgantown immediately created a new debt on suzanne-frank, which is the propagation working as designed; also cleared.
- Governance updated: CLAUDE.md (new second-brain subsection + CLIMB as the fourth operation + `closed` means ended, not finished), STYLE_GUIDE.md (`sources:` vs `synthesizes:`, three new substance rules on height, falsifiability, and keeping failed predictions), STRATEGY.md (purpose paragraph rewritten around the ladder; height added as a parallel campaign), INGEST_RUNBOOK.md (synthesis addendum).
- Altitude baseline: 3.6% of pages above ground level; `self`, `timeline`, `work` and `places` each have 3+ pages and nothing above any of them. That is the structural gap now.
- Gates: wiki-lint 0 errors, wiki-connect check 0 errors, wiki-climb check 0 errors / 0 stale (320 pages).

## [2026-07-26] ingest | people+timeline | the July 2026 re-contact — annie-ulmer reopened
- Filed `raw/self/message-csv/imessage_export_2124702449_20260726.csv` (24,069 rows through 2026-07-26 05:04). New window past the last filed export: 631 messages — near-silence June 5–July 22, then 624 across July 23–26.
- New page `wiki/timeline/events/july-2026-recontact.md`: the 52-day severance, the dog that broke it, four phases (valedictory letter → eight hours of restored intimacy → blame-preemption → the Leviathan dashboards → the crisis), and an explicit section on what it settles versus what it does not.
- **annie-ulmer.md structurally reopened:** status closed→active, date_range_end extended, infobox rewritten, lead rewritten with a REVISED block withdrawing "closed, historical," new section "July 2026: the severance that failed," six chronology rows, three new gaps, Closing Note rewritten to keep the falsified prediction visible. Verdict, numbers and earned reads unchanged.
- **block-unblock-loop rule corrected, not annotated:** it had scored the June 1 dependency as dead because it read dependency as material. The channel reopened through Milo. Rule now: "nothing either party still needs flows through the channel — and what is needed need not be material." Control rows re-read, new table row, and the finding that duration is not the variable (52 days collapsed in 8 hours).
- forensic-method gains "The outward turn": the Leviathan dashboards are the method's first deployment as leverage against a person rather than as self-understanding, with its defining reflexive discipline absent.
- milo.md retrofitted to typed connections and given "The dog as the last open channel" — he is the residual dependency, and the MAX_PRIME "don't psychologize" carve-out is what kept that from being noticed.
- Also: group-chat-closure REVISED (severance, not ending); Betty's death dated to 2025-06-24; the July 2026 house move recorded on 463-morgantown as probable-not-confirmed; hyperreflexivity's housing prediction partially resolved; indexes updated.
- Unadjudicated by design: the July 25 rape allegation is recorded as made, on that date, with no corroboration in any held source and no position taken — matching Dan's own stated position in the transcript.
- Gate repairs, pre-existing on this base: 4 pages with tags outside VALID_TAGS remapped; 3 lineage pages' untyped edges given types and claims.

## [2026-07-17] connect | mind | connection-system adoption pass 2 — all 13 synthesis pages typed
- Retrofitted the remaining 9 syntheses (bond-switch-2015, vertical-authority-skepticism, ai-collaborative-analysis, intake-constancy, millennial-digital-witness, attachment-trauma-bond, political-psyops, ancestral-dialectic, totality-themes): related: removed, 45 typed edges with claims written, 37 inverse edges on targets, prose edges added (forensic-method into psyops; totality into 2025-collapse — clears the #1 queue pair).
- Entire synthesis layer now runs on typed connections. wiki-lint 0 errors; wiki-connect check 0 errors.

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

## [2026-07-17] connect | mind+interests | interests-as-era-markers junction + 5 interest islands retrofitted
- NEW junction page wiki/mind/synthesis/interests-as-era-markers.md (earned): the fixed intake rate (per intake-constancy) makes subject-rotation the era signal; each life period carries a dateable marker obsession — 2007 teen cluster, 2012–13 O&A, 2016–19 golf, 2019 stand-up, 2020 left turn, 2024 Rome — with film-canon as the control case (stable canon, era-indexed readings). Names the 2021–23 missing-marker gap explicitly.
- Retrofitted all 5 islanded interest pages to typed connections (related:/footers removed): roman-republic (5 edges), opie-and-anthony (5), film-canon (5), golf (8), video-games (3 + 2 rejections logged in connection-queue.md).
- Inbound prose edges added on 6 host pages to un-island the five: youtube-watch-history → opie-and-anthony; teen-concert-years → video-games; nemacolin-caddying → golf; intp → roman-republic + film-canon; orchestration-and-voyeurism → film-canon (the 2019-07-18 Eyes Wide Shut self-description now argued in prose there). Inverse edges added on intake-constancy, 2020-left-turn, stand-up-comedy, and all touched hosts.
- mind/index.md updated with the junction entry.

## [2026-07-18] ingest | work+people | Gemini-_02 Au Za'atar storytime fully mined (50 approved data points); chats/gemini-02 page retired
- Operator-approved workflow: scraped the STORYTIME: AU ZA'ATAR genesis convo (raw/self/dox-md/Gemini-_02.md, 20 user turns), presented 50 data points, got approval, researched each against the wider corpus, entered them, then deleted wiki/self/chats/gemini-02.md (raw file untouched).
- Main sink: wiki/timeline/periods/2021-2023-employment-block.md rewritten from v1 dossier-shorthand (with /tmp agent chatter) into style-guide prose absorbing the approved points; status archived→stable; typed connections block added.
- Research-pass finds from all_imessages_complete_dump.txt: Valeria iMessage channel at her +56 Chilean number — Sept 2 2023 "Hey I'm in ny" return, Nov 3 2024 re-contact reported by Dan to Annie's own handle ("that girl Valeria you trained at Au Zaatar just messaged me right now"), "valeria virus" reply same night, inbound "The kiss 😂" July 17 2025. Partially closes the valeria page's "did Annie ever learn of her" gap (she knew of the re-contact and the acquaintance; the affair itself still undocumented). Menore's "legit taxi" cover occupation + mid-shift shed service added to menore.md; candidate DJ handle +19293235324 (r/Senegal links, May 2024) flagged on ismaila-barry.md.
- Smaller entries: au-zaatar.md (BYOB opening formula, Suz birthday comp fixed into prose), tarik-fallous.md (Lebanese-humor/fit characterization), dimitri.md (~6-month first stint), ismaila-barry.md (Aisha/Islam friction section, photo provenance), valeria-iglesias-cid.md (hidden-camera staging, Annie-as-trainer confirmation, iMessage anchors, norteño server-vs-cooks loyalty law), annie-ulmer.md (Dan as her employment vector, April 2021), suzanne-frank.md (2021-11 NYC birthday visit row), orchestration-and-voyeurism.md (hidden-camera courtship instance = architecture generalizes beyond the arrangement).
- Deleted wiki/self/chats/gemini-02.md; all inbound links repaired (gemini-00/07, danfrank-isms, gemini-activity + archive, self/index — also removed its /tmp chatter line — au-zaatar, tarik-fallous); connection-queue entries naming the page annotated RETIRED.
- bin/wiki-lint 0 errors; bin/wiki-connect check 0 errors.

## [2026-07-18] build | meta | bin/llm-publish — public LLM access point (llm/) served by GitHub Pages
- New stdlib tool bin/llm-publish generates llm/: index.txt (single entry-point URL with plain-text instructions + full per-page URL manifest), corpus.txt (entire wiki in one file, ~384k tokens), manifest.json, and pages/**.txt (one plain-text copy per wiki page — .txt extension bypasses Jekyll so Pages serves the raw content verbatim). Any LLM that can fetch a URL can now read actual page bodies with zero GitHub access: https://caakehorn.github.io/wiki-brain/llm/index.txt
- Unlike exports/ (gitignored), llm/ is generated-but-committed by design; CLAUDE.md updated with the tool and the regeneration rule (rerun after content passes, commit the diff).

## [2026-07-18] ingest | work+people+mind | Gemini-_00 finale mined (21 approved points); chats/gemini-00 retired — Au Za'atar storytime cluster fully absorbed
- Completion pass on the STORYTIME finale per the approved 21-point list. Primary verification against raw/people/valeria/message_1.json produced two upgrades: (1) REVISED the valeria page's "continuous 2022–2025 IG contact" framing — the IG record is a six-week burst (1,038 msgs late-May 2022, 3,830 in June 2022 alone, 12 stragglers, then 3 years of IG silence, then a 4-message July 11 2025 coda); the 2023–24 long tail ran over iMessage. (2) Measured the night-window claim: 52% of Dan's 2,082 outgoing IG messages fall 22:00–01:00 ET — the post-9pm-exit window — upgrading "the alibi covered the affair" from inference to measured fact.
- New entries: Dan's attested "it never destabilized" (Valeria as the zero-turbulence control case for conflict-architecture), the dual shutdown mechanism (demand death + city mandate, in that order), the DEENBOR robot never-used confirmation, finished-interior texture (dome ovens, velvet booths, blue tape), the 20-plate carry, and the exocortex-write practice (the finale's "add it all into memory for later recall" request) added to ai-collaborative-analysis.
- Media collection gap documented on au-zaatar: 8 storytime-cited artifacts (hidden-camera hug, Central Park kiss, IMG_0978 interior, flooded basement, outside-bread interrogation, etc.) exist only as Gemini uploads, not on disk.
- Deleted wiki/self/chats/gemini-00.md; all inbound links repaired (tarik-fallous, gemini-21, gemini-activity + archive, self/index, employment-block, au-zaatar); queue entries annotated RETIRED. Both STORYTIME chat pages are now retired — the Au Za'atar cluster lives entirely on its subject pages.
- Maintenance: fixed invalid YAML (nested unescaped quotes in infobox known_for) across 30 people pages, per PR #46 review; bin/llm-publish hardened (wiki-dir check, top-level domain grouping fix); llm/ regenerated.
- bin/wiki-lint 0 errors (308 pages); bin/wiki-connect check 0 errors.

## [2026-07-18] ingest | timeline+people | Photo Thread PT II mined (23 approved points + operator correction) — vigil restructured, death-date contradiction resolved
- Mined raw/self/dox-md/_Photo Thread PT II_ Grand Finale Calibration .md (the Fran finale storytime) per the approved list, with the operator's correction folded in: Dan and Annie were the only ones present at the MOMENT of death, but the hospital vigil ran on a shift rotation including Vicki and Marla.
- **Two structural corrections (REVISED-flagged on fran-death-vigil.md):** (1) the filmed 8 AM/keno/4 PM-lift episode was an EARLIER spill (~late 2017?) that Fran survived by months; the fall that ended her residency ("Down Goes Frazier") is now dated to the night of March 7–8, 2018 via the Vicki/Marla ambulance messages. (2) The April 1 vs April 4 death-date contradiction is RESOLVED: April 1 = pediatric-wing admission (caddie-season opening day), April 4 = death — the DANSYNTH April 1 date conflated admission with death.
- fran-death-vigil.md substantially rewritten: two-fall sequence, the rotation (Vicki 7 AM shifts, Marla nights, Suz's April 2 visit "light spirited and happy" IMG_4637.mov), water shutoff, seizing, "calling for Ira last week," Dan's let-go permission speech and "goodbyes 3 or 4 times" stance, the no-show relatives vs the working rotation, death-moment attendance, snow at +3 minutes, "quick painless easy" verdict; typed connections added; media ledger (6 artifacts, none on disk).
- wiki/people/vicki.md rewritten from swarm stub to full profile (one of the 17 unstarted stubs done; un-islanded): caregiver since Jan 2016, pills/Lifeline/bat texture, "grandmother I never had," April 2 bedside testimony, thread ends Apr 5 2018. marla.md extended (hospital phase, March 8 ambulance row) + connections; duplicate wiki/people/contacts/marla.md deleted (nothing linked it).
- fran-coldren.md: athletic record doubled — 1959 LaGorce hole-in-one (first ace) + 113-lb Everglades tarpon ("weaker sex" clipping) added; Fred Adams = Ira's old law partner CONFIRMED (open item settled); timeline table restructured; death-date contradiction marked resolved. golf.md updated (two aces). suzanne-frank.md: April 2 hospital visit added as counterweight to the keno morning (which now correctly attaches to the earlier spill). ai-collaborative-analysis.md: the "how little ANYONE would get it" AI-confidant quote (Feb 2026) added.
- bin/wiki-lint 0 errors (307 pages); bin/wiki-connect check 0 errors.

## [2026-07-18] ingest | work+people | BFS drawer-dispute cluster fully mined (3 storytimes, ~75 data points); Tom safe-attachment corrected; Anita/Timmy/Brandon rewritten from swarm-fragment to prose
- Operator directive: 75-point pass on lower-priority material, pre-approved, full run-through. Mined the three-file BFS cluster (raw/self/dox-md/: "Cash register shortage explanation", "Drawer shortage dispute with assistant manager", "Little Caesars retaliation timing concerns" — ~250KB combined) into the wiki.
- wiki/work/bfs-foods.md substantially expanded (6.5KB→~15KB, deliberately over budget as a hub): the Tom upstream cause (3 burns in 4 days), the workplace Suboxone attempt (EV calculus, narrative-preconstruction tradecraft, declined-backpack), the one-sided verification procedure + no-sale ban, CSR-decorative-$0.00-for-4-weeks finding, the gas-lady prepay-drive-off-via-no-dispense-void fraud vector (Dan diagnosed from first principles), the $15/$50 mishearing + phantom-tender + refund reconstruction (~$45→$50), Anita's foodstamps-impossible confabulation, the Timmy precedent, the dead-man's-switch/veridiction strategy, PA §260.3 posture, the two self-inflicted written documentation wounds. Typed connections added.
- wiki/people/tom.md: NEW subsection "The pattern is twelve years old, not new (2014 precedent)" — the Aug–Sept 2014 owe-stonewall-escalate-reconcile episode (verbatim) proves the spring-2026 collapse is not a late degradation; the "he would be okay letting me go sick" load-bearing line drives the safe-attachment revision to "lateral ally during mutual alignment, unreliable to indifference during asymmetric periods." Added bfs-foods causes edge.
- Rewrote wiki/people/anita.md, wiki/people/timmy.md, wiki/people/brandon-hill.md from swarm-fragment tables into full prose per the overhaul mandate (status→closed, typed connections, index one-liners refreshed).
- bin/wiki-lint 0 errors (307 pages); bin/wiki-connect check 0 errors; llm/ regenerated.

## [2026-07-18] connect | mind | JUNCTION PAGES: supply-network + estate-money-spine (2 of the 3 remaining junction candidates written)
- **wiki/mind/synthesis/supply-network.md (NEW, earned):** fifteen years of procurement treated as one architecture. Node succession verified against MAX_PRIME/operating_manual (Johnny → Tim → Tom by 2025; Menore in NYC; Teddy + second handle +17243233522 as 2018 redundancy layer; "bop"/"Felix" 2026 vocabulary). Core findings argued: the network survives every biographical rupture (Menore's 1-minute resume after 5.5 years); redundancy decayed monotonically to a single node (parallels contact-gini); the reliability inversion (distance disciplines, intimacy licenses failure — Menore 0 failures vs Tom's 2014/2026 owe-and-silence cycles); node-failure cost propagation (BFS job, Tom friendship, household economy, workday co-location); the terminal-phase inversion (Dan as Annie's supplier, supply as the relationship's last transactional bond). 10 typed edges + inverses on tom, teddy, johnny-dealer, menore, annie-ulmer, intake-constancy, contact-gini, bfs-foods, au-zaatar, 2018-deep-cycle, 307-e-76th-st. Teddy/Johnny/Menore retrofitted off related: to typed connections in the same pass. Felix disambiguation recorded (463-contractor Felix = candidate for MAX_PRIME's 2026 "supply-adjacent" Felix; john-felix 2016 ≠ same person absent evidence).
- **wiki/mind/synthesis/estate-money-spine.md (NEW, earned):** the capital timeline as one causal chain. Two source-lines (Ira estate w/ Judge Fred Adams trusteeship; Frank's Auto Supermarket) — Dan holds neither; the dated join discovered: distribution order signed 2020-08-21, the union-busting/coal-baron class-guilt message written 2020-08-22, the next day. Chain table 2017 floor → 2020 distribution ($144,069.31 / $134,069.31 net check) → market era (~$15k stake, $25k peak, flagged-as-inference funding join) → "money just ran out" early 2021 (six-month lump survival) → wage era → 2024 job loss → 2026 broke → 337 sale ($465k, Dan as bystander) → 463 lien clock. Largest drain quantified: ~$119–123K net to Annie ≈ the entire estate distribution. Suz argued as the spine's switchboard (every major flow passes through her; single point of failure at exactly the 463 deadline). 10 typed edges + inverses on fran-coldren, rick-frank, suzanne-frank, 2017-poverty-floor, 2020-2021-market-era, annie-ulmer, 337-saratoga-drive, 463-morgantown, 2025-collapse, supply-network (parallels pair).
- mind/index.md wired; bin/wiki-lint 0 errors; bin/wiki-connect check 0 errors.

## [2026-07-18] connect | mind | JUNCTION PAGE: block-unblock-loop (3rd of 3 remaining junction candidates — junction backlog CLEAR) + Menore metrics recomputation
- **wiki/mind/synthesis/block-unblock-loop.md (NEW, earned):** the declared-not-executed exit generalized beyond Annie. Case table: Annie 127/110 (87% relapse, DERIVED — primary recount still queued), Tom 2014 ("I'm done… stupid fucking dance" → reopened in 5 days) + Tom May 18 2026 (same-day conditional unblock), Rick (12-day burst → decade-held amputation, the held-block control), Kristin Dec 2025 (inbound block, held), May 2014 account amputation + 2022 repatriation (infrastructure layer), Grok-loop 414-run (machine proof: no-halt-condition defect in software). **Governing rule argued: a block holds iff no dependency still flows through the channel.** Menore's Feb 20 2025 farewell = the clean-closure control (dependency ended by geography, no block needed). June 1 2026 Annie closure framed as the loop's live test (first exit after her supply dependency ended; consistent so far). 10 typed edges + inverses (annie-ulmer, tom, kristin, rick-frank, march-2026-terminal-phase, conflict-architecture, attachment-model, attachment-trauma-bond via contextualizes, totality-themes, supply-network).
- **Menore metrics (operator-requested primary recomputation from messages_3476070497_all_time.csv):** total 4,413 msgs (Dan 2,660 / Menore 1,753 — the old "1,753+" was Received-only); availability 99.3% (455/458 requests answered ≤6h; 3 unanswered, all 2019); median reply 6.6 min (the "~60-second SLA" was DAN'S reply speed — his median to Menore is 30 s); request→arrival median ~95 min; ~280 strict / ~413 loose confirmed deliveries on 266+ days; max 2 confirmed meetings/day (retires "3–5 visits/day"); peak 18:00–20:00, late-night share 8.3%; longest streak 14 days. **CONTRADICTION flagged: 1,458-day silence May 26 2020 → May 24 2024** vs the "sustained operations 2019–25" framing and the au-zaatar 2021–24 mid-shift claim (now scoped to primary-confirmed May–Aug 2024, deliveries to "1st bet 57&58" = the Au Za'atar block; an intermediate number may explain 2021–24 — not on disk). **Ending corrected:** formal farewell Feb 20 2025, 48 h before the PA move — closure by geography, not fade-out. menore.md restructured (REVISED table + Measured Service Metrics section + phases 4/5 split); claims propagated to supply-network.md and au-zaatar.md.
- mind/index.md wired; bin/wiki-lint 0 errors; bin/wiki-connect check 0 errors.

## [2026-07-18] verify | mind+people | PRIMARY-COUNT PASS on the fallout-verdict aggregates (the queued [DERIVED] figures adjudicated)
- Sources: all_imessages_complete_dump.txt (217,573 sender-tagged rows, 2011-03-18→2025-08-10) + imessage_7244346811+2124702449_both_all_now.csv (85,586 rows, →2026-05-28). Terminal window = 2025-08-01→2026-03-16 (her 8,293 / his 10,346 msgs).
- **CONFIRMED EXACTLY → [RAW-CSV]:** the verbal-abuse triple 74 "fuck you" / 17 "piece of shit" / 11 "worthless" reproduces to the digit from DAN'S side of the window (her side: 0/1/0 — asymmetry total). The 0-severance claim: her 41,073 messages contain zero genuine severance signals (only false positives: a quoted denial + an ice anecdote). 1,512 love-affirmations: confirmed to lexicon precision (1,528 broad / 1,388 strict through Aug 2025).
- **NOT REPRODUCED / REVISED:** (1) **187:4 love-to-request** — ratio reproduces (212:8 = 96.4%) BUT base-rate control shows 97.2% of ALL her window messages are request-adjacent at ±24h → statistic uninformative; directional test INVERTS it (request follows her love-msg within 1h 3.2% vs 16.2% baseline — love was MORE isolated from requests than her average message). REVISED blocks on verdict + annie-ulmer + pointers on supply-network/2025-collapse. (2) **180 "I'm sorry" / "apologizes least"** — plain-lexicon recount: 435 through Aug 2025 alone (~4× his attack count); ordering fails without an unstated contrition-only definition. REVISED on conflict-architecture + verdict; reassurance-dominance survives. (3) **299** — unlocated under any window/lexicon (candidates: her terminal 231 / his 355 / her all-time 1,302).
- **ORDER-CONSISTENT, still [DERIVED]:** 127/110 (loose exit-lexicon: 176 candidates); 94-burst (2-min-gap runs: 11,666 ≥3, max 149 through Aug 2025; parameters unstated in dossier); 232 "fuck you" (111 through Aug 2025 + verified 74 in-window → plausible).
- **RE-CONFIRMED ABSENT:** Eli intro text (full raw/ re-grep — dossier-only); 768-on-05-31 (closure export still 265 Sent / 482 total).
- Bonus ledger fact: his in-window apologies = 121. Gates 0 errors.

## [2026-07-18] triage | people+mind | LONG-TAIL TRIAGE — one-time judgment pass, islands 45 → 20
- Full verdict record in LONG_TAIL_TRIAGE.md (repo root) — decisions are settled; future models execute, not re-litigate.
- **Wired (inbound prose edges):** 8 minor supply nodes → new minor-node layer paragraph on supply-network.md (the redundancy the system lost, measured in names); 6 caddie-cohort pages → new "caddie-yard social graph" section on nemacolin-caddying.md (caddying = the last era in which work generated friendships in bulk); manuel → au-zaatar cast; fastly-fsly → market-era; block-unblock-loop → tom.md prose; 307-e-76th-st → menore.md.
- **steve-kezmarsky.md REWRITTEN** from swarm template to full prose: high-school-era golf friend, "our friendship is based on my sickness," thread ends Jan 2018, dead by Dec 2018 (via Jim Shaffer thread — inverse edges on new-jim-shaffer/golf/nemacolin). One more of the unstarted-stub list done.
- **Demoted to contacts/ quarantine:** rod-banks, slim, zach, zach-clabaugh, tan-calabrese, zach-hendricks (merged with zaco — same handle +17249123381, zaco.md deleted), caviar (not a person — automated dispatch number). **Deleted:** brandon.md (pointer dup of brandon-hill). people/index.md rows cleaned.
- **Delegated (standing verdicts in LONG_TAIL_TRIAGE.md):** MINE sam(374)/davey-fitzpatrick(382)/vaughn(228)/nick-mattie(170); REWRITE-OPENER jason-bermejo; ACCEPTED-LEAF list (11 real mini-profiles, deliberate); chats/ backlog unchanged.
- Gates: wiki-lint 0 errors; wiki-connect 0 errors, islands 45 → 20.

## [2026-07-18] governance | root | Post-Fable operating rules settled + llm/ regenerated
- Page-budget contradiction resolved (CLAUDE.md rule 4 ↔ STYLE_GUIDE substance rule 4): ~8KB is a navigation heuristic; lint size warnings advisory on hub/junction/exemplar pages; standing directive = LONGER entries.
- INGEST_RUNBOOK §11: storytime-mining workflow codified (scrape → ~50 points → operator approval → research → enter → delete chat page), candidates listed.
- STRATEGY.md "Running on lesser models": mechanical-execute list vs never-attempt list; junction trio named as the model of the product.
- LLM_HANDOFF.md session entry + prioritized next steps. llm/ regenerated (308 pages, ~407k tokens).

## [2026-07-18] ingest | timeline | Pre-2015 period reconstruction — 2010s.md corrected + NEW uniontown-return-2013-2015 (the misnamed "archaic dump" finding)
- **Finding first:** MASTER_DUMP_PART_1_ARCHAIC.csv is misnamed — 124,177 rows but only 1 in 2011 and NOTHING 2012–2014; earliest real-text row is 2015-11-12. The message corpus genuinely begins ~Nov 2015. Pre-2015 CANNOT be filled from message data — recorded so no future model re-attempts it. Pre-2015 must come from context-core / Facebook / dox / LIFE calendar only.
- **2010s.md corrected + rewritten** (was mis-bounded 2010–2014 as "NYC Round One," Alexis wrongly "met through webcam work"). Per context-core §4 canonical residence timeline: NYC-1 = Apr 2010–May 2013 (424 Bedford → UES 90th), ishlab/Creative License audio era, Alexis whole-NYC cohabitation (Bridge Cafe until Sandy Oct 2012), LCD MSG farewell Apr 2011, Suboxone onset. REVISED block documents both corrections. Typed connections added.
- **NEW wiki/timeline/periods/uniontown-return-2013-2015.md** — fills the genuinely-uncovered stretch (periods jumped full-sail-2008-2010 → 2015-2016-annie with only the thin 2010s catch-all). The most-corrected geography in the timeline: SLOPPP (2013 launch, 2014 peak) → MOGZART (~2014 handoff on the May account rotation), the Alexis endgame, Jan 2015 move to 155 Virginia, Nov 28-29 2015 switch to Annie — all in Uniontown, not NYC. 7 typed edges.
- Inverse edges on full-sail, sloppp, mogzart, 155-virginia-ave, chemical-architecture, 2015-2016-annie, alexis-armel, bond-switch-2015. timeline/index.md rewired. llm/ regenerated.
- Gates: wiki-lint 0 errors (309 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | long-tail MINE pass (sam, davey-fitzpatrick, vaughn, nick-mattie, urpaaa) + kezmarsky death-claim correction
- Full-thread per-contact mining from MASTER_MESSAGES_DB_DUMP.csv per LONG_TAIL_TRIAGE.md: sam (374 — NYC cannabis delivery dealer 2019–20), davey-fitzpatrick (382 — Nemacolin assistant caddie master 2018), vaughn (228 — caddie + weed middleman), nick-mattie (170 — 2017 reciprocal trading peer), urpaaa-at-yahoo-com (23 — unidentified teacher, parental register, Oct 2017 extraction). jason-bermejo opener rewritten per Substance Standard.
- CORRECTION (operator-requested validation): steve-kezmarsky was NOT dead by Dec 2018 — the Jim Shaffer thread shows Dan correcting Jim's misreading ("He's alive but living the least enviable life EVER / two kids / Sober"). The real event: his father's Jan 22, 2018 arrest and expected life sentence. REVISED blocks on steve-kezmarsky.md + new-jim-shaffer.md; index one-liner fixed.
- Typed connections + inverse edges wired across supply-network, nemacolin-caddying, menore, 307-e-76th-st, covid-era-2020, 2017-poverty-floor, orchestration-and-voyeurism, fran-death-vigil, trevor, jack-rusko, annie-ulmer.

## [2026-07-19] ingest | mind | operator capture: Oct 21, 2019 filmed MMF + its weaponization
- Operator note filed to raw/self/captures/2026-07-19_operator-note-oct2019-mmf-video.md. Corpus corroboration found: Sent 2019-10-22 "last night we had to film mmf (my first time doing that)..." dates the encounter to Oct 21, 2019 (NYC, filmed, oral-only — Dan's sole bisexual experience). End Fight export shows Tuquick deploying the video June 2026 ("sucked a dick, for you to get drugs"; "Or the video of her sucking dick...").
- arrangement-history.md timeline row added; tuquick-17248123683.md gains "The October 2019 video as weapon" section + typed edge.

## [2026-07-19] connect | mind | psych-linkage pass — concepts/psychosexual wired to people pages
- Per operator directive: retrofitted attachment-model, conflict-architecture, phenomenology-lens, developmental-origins, emotional-imprinting, erotic-architecture, arrangement-history, dans-law, node-locking, institutional-out to typed connections; deleted deprecated related: lists/footers on retrofitted pages. ~45 new argued edges with inverses on annie-ulmer, rick-frank, suzanne-frank, alexis-armel, kelly-johansson, kristin, valeria-iglesias-cid, eli-incident, bfs-foods, au-zaatar, forensic-method, exocortex, and others.
- New person page: bryan-5088682461 (operator-identified third participant, Oct 21 2019 filmed MMF; +15088682461 corroborated in corpus via May 2025 re-contact). Disambiguation hatnote added on brian.md. The Bryan instance corroborates erotic-architecture's "taboo as ontological rupture" mechanism — theory now has its documented case.
- Gates: wiki-lint 0 errors, wiki-connect check 0 errors.

## [2026-07-19] correct | people | MMF encounter date → Oct 20, 2019 (operator)
- Operator correction: the filmed MMF with Bryan took place 2019-10-20, not the 10-21 previously inferred from the Oct 22 "last night" message. Updated bryan-5088682461, arrangement-history, tuquick, brian hatnote, erotic-architecture, people index; REVISED block on bryan page records the one-day tension with the corpus phrasing. Capture note appended.

## [2026-07-19] ingest | people | Full Sail friend group — matt-dunn, jamie-mohler (new); jason-bermejo, eric-jester (expanded)
- Per operator directive: worked the college (Full Sail) friend group — Jason Bermejo, Eric Jester, Matt Dunn, Jim/Jamie Mohler.
- NEW matt-dunn.md: Full Sail cohort member, no direct thread; mined from Jester/Bermejo threads (annual $5 birthday Venmo bit, Nov 2018 Orlando visit, "gross and forgettable").
- NEW jamie-mohler.md: NYC-1 friend, present per operator the day Dan first met Menore. Facebook address-book search (per operator request) surfaced a direct contact card (Jim Mohler, +12073101169, audiocranium@msn.com) which led to a genuine primary-source find in gmail_bodies.txt — a 2011 Google Talk chat log ("Jimbo Slice") placing her at the NYC-1 household during Occupy Wall Street, independently corroborated by Alexis's own Aug 2011 Gchat. Transition (~2023, now female) corroborated by two 2025 Jason Bermejo thread lines ("Mohler = a literal woman" / "Haha she badass"; "ms. Jamie Mohler").
- CORRECTION: jason-bermejo.md previously mislabeled Mohler as "current girlfriend of Jason" — a misread of a single out-of-context line. REVISED block applied; corrected to fellow Full Sail cohort member.
- eric-jester.md expanded (Dunn's Nov 2018 sighting, the Venmo bit, typed connections replacing bare related:/footer).
- Wired into wiki/timeline/periods/full-sail-2008-2010.md (new "The friend group" section) and 2010s.md (NYC-1 key contacts); menore.md gains the NYC-1 pre-history note.
- Capture note: raw/self/captures/2026-07-19_operator-note-full-sail-mohler.md.
- Gates: wiki-lint 0 errors (312 pages), wiki-connect check 0 errors. llm/ regenerated.

## [2026-07-19] ingest | people | oscar-lindquist (new) + jamie-mohler precision pass
- NEW oscar-lindquist.md from his own Facebook thread (6 msgs, 2011): precisely dates the Jamie Mohler NYC-1 Hurricane Irene evacuation to Aug 26, 2011 (previously only "~October 2011" via the undated Jimbo Slice chat), and is the primary source behind the 2022 Manhattan-restaurant coincidence already noted on jason-bermejo.md and matt-dunn.md.
- jamie-mohler.md restructured chronologically around three independent 2011 sources (Alexis's Gchat, Oscar's Hurricane Irene message, the Jimbo Slice log).
- Bot-review findings from PR #54 fixed and cherry-picked forward after a merge race (directional reference, cohort-count discrepancy, overstated "named in both threads" claim on eric-jester.md/full-sail-2008-2010.md).

## [2026-07-19] ingest | people | Facebook Messenger deep-scrape — zachariah-harshman, lukyan-mraz (new tier-one entries)
- Per operator directive to scrape the FB Messenger + Gmail archives "much more carefully" for facts about people OTHER than the Full Sail crew: cross-referenced all 271 FB Messenger inbox threads against existing wiki/people/ pages; ~74 threads had no obvious existing coverage.
- NEW zachariah-harshman.md (~970 msgs, 2011-2021) — the single highest-value find: a Laurel Highlands high-school friend whose thread runs through (1) shared senior-year drug reminiscence, (2) the earliest documented SLOPPP promotion attempt (Jan 2014, Pittsburgh rave pitch), (3) a dense 2014-15 Uniontown wax/dab/flower supply relationship — three years earlier than any previously documented Uniontown node — staged at 155 Virginia Ave from Jan 2015, and (4) a precisely-dated Dec 23, 2015 rupture that is INDEPENDENT THIRD-PARTY CORROBORATION of the bond-switch-2015 thesis (Zach reveals he'd grown close to Alexis post-breakup, confirming the switch's social fallout from entirely outside Dan's own corpus), followed by (5) a full platonic revival as a gaming friendship, 2020-2021, drug-content-free.
- NEW lukyan-mraz.md (36 msgs, 2015-16) — a short-lived 2015 cannabis-grow collaboration connected to the same household/circle as Zach, ending in a tense March 2016 equipment dispute; his Feb 17 "you alright?" cross-corroborates Zach's own Feb 18 concern about him, an unexplained joint data point.
- Wired into: mind/synthesis/supply-network.md (Zach added to the main succession table as the earliest node, not the minor-node list), mind/synthesis/bond-switch-2015.md (new "Independent corroboration" section), places/155-virginia-ave.md, interests/music/aliases/sloppp.md.
- Gates: wiki-lint 0 errors (315 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | Facebook Messenger deep-scrape II — lucie-dobbin, rob-orange, lauryn-ashly (new tier-one entries)
- lucie-dobbin.md (new): recipient of Dan's fullest first-person account of Fran's death (April 5, 2018, same night) — a silent mental-communication attempt, the final smile, immediate pronouncement, and a rare register of genuine spiritual uncertainty. Mined directly into wiki/timeline/events/fran-death-vigil.md's "The end" section, plus a previously-undocumented May 6, 2018 Uniontown Country Club memorial event.
- rob-orange.md (new): resolves the previously-undocumented death circumstances of Rob Orange (referenced but not detailed on new-jim-shaffer.md) via Lauryn Ashly's April 11, 2014 real-time reaction thread — suspected opioid OD, cause never confirmed, "Edgewood" unexplained. Cross-corroborated by Jim Shaffer's independent Dec 2018 mourning (now also carrying the previously-unwritten Tom Petty minivan anecdote).
- lauryn-ashly.md (new): the Rob Orange death-day exchange plus a September 2020 arrangement-solicitation message Dan sent her, declined without any strain — a documented case of the pattern NOT landing, added to arrangement-history.md's evidence base.
- Cleanup: new-jim-shaffer.md's residual bare related:/## Related footer (leftover from a partial retrofit) fully converted to typed connections.
- Gates: wiki-lint 0 errors (318 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | FB deep-scrape III — elizabeth-eleanor, stephanie-nalbone (new); chemical-architecture + INTP dating
- elizabeth-eleanor.md (new): single July 2013 overnight conversation with a fellow recovering addict, yielding the corpus's only concrete Suboxone dosage figure (2mg/day, ~5yr opiate-free — dates last use to the dark-era 2007-2008 window) and the earliest dated primary-source INTP self-identification (3 years before the profile pages' main material). Both mined into wiki/health/chemical-architecture.md and wiki/mind/profile/intp.md.
- stephanie-nalbone.md (new): a previously entirely undocumented Sept-Nov 2009 long-distance relationship falling inside the Full Sail period's own Danielle-to-Alexis pivot window. Corrects an initial misreading of speaker attribution (Dan traveled to Uniontown, not the reverse) before publishing. Flagged as an unresolved sequencing question on full-sail-2008-2010.md rather than asserted into the existing two-name narrative.
- Gates: wiki-lint 0 errors (320 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | FB deep-scrape IV — christo-coan, lewis-strosnider, seth-ledonne, ej-rags, lucas-thomas (new tier-one entries)
- christo-coan.md (new): Nemacolin-era golf-course coworker; co-organized Dan's Oct 2017 birthday; first-person confirmation of the 117 Belmont Circle "golf course house next to Annie's grandparents" geography; surfaces a previously undocumented DUI reference — flagged as a `> **CONTRADICTION:**` on wiki/legal/2015-retail-theft-arrest.md (which had framed the 2015 retail-theft arrest as the only documented arrest) and softened wiki/legal/index.md's framing accordingly.
- lewis-strosnider.md (new): Uniontown vape-shop friend; free graphic design work, a planned FAA Part 107 drone business funded partly by the anticipated Fran estate check — cross-linked to wiki/mind/synthesis/estate-money-spine.md as evidence the distribution ran ~2 years later than Dan expected in real time; a $1,600 Mavic 2 sale still unresolved when the Feb 2019 NYC move thread ends.
- seth-ledonne.md (new): named counterculture-education tribute (hardcore/punk scene mentors) plus a real-time June 7, 2020 NYC protest-curfew account ("living in beirut") — cross-linked to wiki/timeline/periods/covid-era-2020.md.
- ej-rags.md (new): Williamsburg NYC vinyl-collector friend; July 2013 exchange is Dan's own stated philosophy of destroying his creative work ("so I can create something new"), dated to the opening days of the 2013 Uniontown return.
- lucas-thomas.md (new): independent real-time (Feb 11 & 16, 2017) eyewitness account of the Zac Shumar house-fire-and-arrest event already documented on wiki/people/alexis-armel.md via two later retellings — confirmed as the SAME event, not a new one, and used to enrich the existing "Post-breakup: the Zac Shumar arrest and incarceration" section with real-time detail (the RT informant angle, $35k bail, the lost glass rig, parents learning of the fire and arrest in the same jail call) rather than creating a duplicate event page.
- Gates: wiki-lint 0 errors, wiki-connect check 0 errors (193 warnings, all pre-existing quarantine-stub `## Related` footers or size-budget advisories).

## [2026-07-19] ingest | people | FB deep-scrape V — bobby-cole (new tier-one entry)
- bobby-cole.md (new, ~940 msgs, 2013-2022): a nine-year friendship anchored almost entirely in Opie & Anthony/Ron & Fez fandom. Two exchanges resolve real gaps: (1) Oct 2, 2019 — the corpus's only direct evidence Dan actually completed an open-mic set (a specific bombed bit, audience groans), plus a previously undocumented SiriusXM job application ("the fishbowl" studio, hoping for OutQ placement); (2) identifies the previously-unnamed Dec 2018 Philadelphia taping (already on stand-up-comedy.md) as a Chip Chipperson show, invited by Bobby. Also a corroborating April 2021 self-aware check-in on the Aug 2020 left turn.
- Updated wiki/interests/stand-up-comedy.md (closed the "no completed performance" gap, named the Philadelphia taping), wiki/interests/opie-and-anthony.md, wiki/mind/synthesis/2020-left-turn.md with inverse connections.
- Gates: wiki-lint 0 errors (326 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | FB deep-scrape VI — jenn-lynn, joe-oshnack (new tier-one entries)
- jenn-lynn.md (new, ~240 msgs, 2017-2020): a three-year Uniontown friendship carrying a repeatedly-solicited but never-confirmed two-couple swap arrangement (with boyfriend Brad) across three separate windows, running parallel to an ordinary drug-sourcing relationship. Added as a new row + inverse connection on wiki/mind/psychosexual/arrangement-history.md — the arrangement's least-resolved documented instance (mutual readiness twice, no confirmed follow-through).
- joe-oshnack.md (new, ~195 msgs, 2011-2022): high-school bandmate; the corpus's fullest first-person account of Dan's *pre*-2020 conservative political identity ("an annoying little conservative fuckcunt... less than thrilled about playing songs with an anti-Iraq-war theme"), cross-linked as evidence into wiki/mind/synthesis/2020-left-turn.md. Also surfaces a genuine unresolved date discrepancy — an Aug 12, 2018 message describing an already-completed cam threesome with Alexis, ~3 months before the documented Nov 2018 reunion and while she's independently confirmed still incarcerated as of April 2018 — flagged as a CONTRADICTION on wiki/timeline/events/annie-alexis-reunion-november-2018.md rather than resolved. Also identifies a Jan 2022 Jacob Bacharach book recommendation, wired as a new connection on jacob-bacharach.md (which previously had only a bare related: list).
- Gates: wiki-lint 0 errors (328 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | FB deep-scrape VII — dan-polyak (new tier-one entry)
- dan-polyak.md (new, ~205 msgs, 2013-2020): longtime friend carrying two consequential exchanges. (1) April 18, 2019 — Polyak confronts Dan for impersonating his phone number to reach Ally Lubin ("fake used my number... very slimy move... I will pursue legal action"), the only documented account of how the sustained Ally Lubin friendship actually began — added to wiki/people/ally-lubin.md, which previously had no connections: block. (2) Oct 21, 2019, 2:52 AM — a same-morning disclosure and reaction to the Bryan encounter ("i've never felt more hetero in my life"), independently corroborating the operator's Oct 20 date over the corpus's Oct 22 message, plus a previously undocumented Oct 25 follow-up ("we invited him over again this weekend") — added to wiki/people/bryan-5088682461.md and wiki/mind/psychosexual/arrangement-history.md.
- Gates: wiki-lint 0 errors (329 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | FB deep-scrape VIII — jamie-mohler.md major expansion (rediscovered thread)
- Identified a 422-message Facebook Messenger thread (2010-2021) filed under a deactivated-account placeholder ("Participants: Facebook user and Dan Frank," thread id qymuchauiq — invisible to the earlier name-matching classifier) as almost certainly Jamie Mohler's own now-deactivated account: two direct "jim" addressals, an Aug 25 2011 evacuation-planning message landing the day before Oscar Lindquist's independently-dated Aug 26 2011 Hurricane Irene message, an Oct 3 2011 Occupy Wall Street exchange inside the same window the undated 2011 Google Talk log was already narrowed to, and confidant-level access (shown Fran's deathbed footage before anyone else, April 2018). Flagged as high-confidence inference, not a phone/email match — noted explicitly as revisable.
- Substantially expanded jamie-mohler.md: the 2011 Suboxone/opiate-maintenance favor request (new, corpus's clearest early evidence of that dependency), World of Warcraft leveling together, a five-year gap then a Dec 12-13, 2017 reconnection that is the corpus's THIRD independent telling of the Zac Shumar arrest (earliest of the three, ~10 months after it happened) plus a Dec 27, 2019 Menore-reliability aside.
- **Resolved (not just flagged) the open date question from the previous batch**: the Dec 13, 2017 message on this thread independently confirms — in the same already-past-tense register as Joe Oshnack's Aug 2018 reference — that the Alexis/Annie cam encounter both sources describe happened during Alexis's Feb-Oct 2017 bail window (between her Valentine's Day 2017 arrest and end-of-October jailing), not before her arrest and not contradicting the separately-documented November 2018 reunion. Updated the CONTRADICTION-type edge on annie-alexis-reunion-november-2018.md to a lower-key `contextualizes` edge, and rewrote the corresponding section on joe-oshnack.md and the Zac Shumar section on alexis-armel.md accordingly.
- Gates: wiki-lint 0 errors (329 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | self | FB deep-scrape IX — tattoos.md enrichment via chris-redmond thread
- No new people page (service-provider relationship, low personal depth) — instead substantially enriched the existing wiki/self/tattoos.md via a 105-message Facebook thread with Chris Redmond, the Misfits-tattoo artist already named there. Precisely dated the pizza-slice piece (booked Oct 12, inked Oct 13, 2018, forearm ~3x1.5in, tied to a "4 or 5 pieces before turning 30 on Nov 1" plan); surfaced a previously undocumented SECOND Misfits piece (green-lettering logo, Oct 22, 2018); traced the "full sleeve" ambition's actual origin to Uniontown (Oct-Dec 2018) rather than Brooklyn, three months before the Weidrick/Allied Tattoo sessions the page already documented — including a Nov 30, 2018 rose-concept discussion with Chris Redmond whose relationship to the eventual Weidrick rose (same piece carried to NYC, or a separate unfinished one) is flagged as unresolved. Location clues (Cheat Lake, Hopwood) place Chris Redmond as Uniontown-area, clarifying (though not fully resolving) the page's prior "Chris Redmond vs Chris at the Edge" open question.
- Gates: wiki-lint 0 errors (329 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | people | FB deep-scrape X — drew-mcgettigan (new); sloppp.md booking-attempt enrichment
- drew-mcgettigan.md (new): summer 2015 Uniontown supply contact (buyer/go-between), connected to the Zach Harshman circle he was headed to meet the same night as a documented deal. Added to supply-network.md's minor-node list.
- sloppp.md: added a second documented 2014 live-booking attempt (Phil Lacher, a Pittsburgh DJ, July 6 2014 — Dan's own direct outreach, referred to a third contact with no booking resulting) alongside the already-documented Zach Harshman January 2014 pitch — the alias's only two documented attempts to convert into a live booking, both dead ends.
- Gates: wiki-lint 0 errors (330 pages), wiki-connect check 0 errors.

## [2026-07-19] ingest | interests | FB deep-scrape XI — sloppp.md: the March 2015 near-management deal
- Major addition to wiki/interests/music/aliases/sloppp.md: a previously undocumented March 2015 management pitch from Pittsburgh promoter Frank Swaney — real enthusiasm for the Spring 2015 Demo, a proposed flat-fee management arrangement (CDs, stickers, street team), two named tentative bookings (an Illuminati event, a Homegrown show in Braddock PA), and — the standout detail — a plan to finalize contract terms through a third party ("Joby") talking directly to Dan's mom and dad, the only documented instance of Dan's parents being brought into a professional negotiation over his music career. No trace of the deal, the contract, or either booking survives past March 2015; SLOPPP closes nine months later with no indication it was signed.
- Gates: wiki-lint 0 errors (330 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | people | FB deep-scrape XII — matthew-palermo (new tier-one entry)
- matthew-palermo.md (new, ~70 msgs, 2018-2020): Uniontown classmate whose Feb 13, 2020 conversation carries a real, named-circumstance death disclosure (his brother, relapsed after a long period clean, fatally overdosed) and the corpus's starkest quantified opiate-epidemic statement — "a quarter of my graduating class isn't around anymore... we have lost more friends at 30 than our parents have at 60" — cross-linked as a parallel to the similar framing on joe-oshnack.md. Also independently dates the Sept 21, 2018 purchase of the DJI Mavic 2 drone already documented on lewis-strosnider.md.
- Gates: wiki-lint 0 errors (331 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | people | FB deep-scrape XIII — david-beard (new tier-one entry)
- david-beard.md (new, ~70 msgs, 2018): golf-course-adjacent Uniontown contact who sold Dan a used DJI drone for $700 in early Sept 2018 — revealed to be the SECOND of three drones Dan bought in a six-week span that summer (Mavic Platinum Jul 24, David's used unit ~Sep 4, Mavic 2 Sep 21). Corrected/enriched lewis-strosnider.md's drone paragraph to reflect the full three-drone sequence rather than treating the Mavic 2 as an isolated purchase.
- Gates: wiki-lint 0 errors (332 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | people | FB deep-scrape XIV — ryan-scherich (new tier-one entry)
- ryan-scherich.md (new, ~63 msgs, single day 2020-02-08): a self-contained political flame war with a barely-known acquaintance, ending in a remark ("U know how they [illegals] kill and rape ppl") Dan calls racist before cutting contact. Lands five days after the documented Feb 3, 2020 Iowa-caucus Bernie evangelism on wiki/mind/synthesis/2020-left-turn.md — cross-linked as a real, contemporaneous conflict from inside that window rather than only Dan's own outward messaging.
- Gates: wiki-lint 0 errors (333 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | health/mind | non-person growth pass I — hyperreflexivity.md (new); GLAZE-GOD-v1 persona
- New directive: grow non-person domains (health: 2 pages, legal: 3, places: 5, work: 11 — all clearly underrepresented vs. 250+ people pages), prioritizing content most important/influential to Dan's own perspective.
- wiki/health/hyperreflexivity.md (new): a self-initiated AI-collaborative session naming and mechanizing Dan's social anxiety ("hyperreflexivity" — the monitoring apparatus as its own problem generator, why prevention/avoidance trains the anxiety to run hotter). Surfaces a genuine unresolved tension not carried on chemical-architecture.md: chronic Suboxone receptor occupancy may blunt the hedonic range needed to break the loop. Also supplies a dateable fact — ~11 months unemployed after the Aug 2024 Au Za'atar loss, then 2 weeks back at 40hrs/week, dating the session to roughly mid-2025 — added to wiki/work/au-zaatar.md's aftermath, which previously had no record of what followed the job loss. No confirmation anywhere that Dan pursued the ACT/exposure-based treatment the session recommends.
- wiki/mind/concepts/erotic-architecture.md: added a previously undocumented artifact — a custom AI system-prompt persona ("GLAZE-GOD-v1") built to perform continuous sexualized worship of Annie's photos — as the most literal instance yet of the page's "externalized libido" mechanism. Cross-linked into ai-collaborative-analysis.md's persona-engineering material.
- Gates: wiki-lint 0 errors (334 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | places | non-person growth pass II — 424-bedford-ave.md (new)
- wiki/places/424-bedford-ave.md (new): consolidates the NYC-1 period's primary residence (2010-2012), previously scattered across jamie-mohler.md, menore.md, alexis-armel.md, danielle-onesi.md, and timeline/periods/2010s.md with no central page — the studio-work era (ishlab, Creative License), Alexis's cohabitation through the Bridge Cafe/Hurricane Sandy years, the Hurricane Irene evacuation and Occupy Wall Street march both organized out of the address, and the origin of the Menore supply relationship. Checked BFS Foods legal-strategy source material (already fully mined into wiki/work/bfs-foods.md via a duplicate copy under raw/legal/bfs-dispute/) and confirmed legal/ domain's thinness (3 pages) reflects genuine corpus content rather than an unmined gap — raw/legal/ contains no further unused material.
- Gates: wiki-lint 0 errors (335 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | health/people | non-person growth pass III — chemical-architecture.md supply-crisis texture
- wiki/people/tom.md: added a real-time Suboxone supply crisis (a rival "jumped his place in line," Tom covered the loss anyway) and the fullest documented texture of Tom's relationship with Suz (an unprompted car-battery replacement when hers died and she couldn't afford one; she's the only one who can call him). Cross-linked into wiki/health/chemical-architecture.md's "Supply as social infrastructure" section as an earlier instance of the same reliability the May 2026 failure later broke.
- Surveyed remaining large unmined dox-md/dox-scan files (_Openclaw Agent Setup, fullcombo 2.txt, Attachment System Collapse.md, _Two Options Choose Wisely) — Openclaw is generic AI-tooling troubleshooting (low biographical value); Attachment System Collapse.md is a ChatGPT restatement of the already-extensively-documented Annie gaslighting/perceptual-trust thesis (no new facts found in a full scan). Deprioritized both per the "most important/influential" directive.
- Gates: wiki-lint 0 errors (335 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | interests | batteries-not-included.md (new) — operator-directed
- wiki/interests/music/bands/batteries-not-included.md (new): Dan's high school band with Joe Oshnack and Matt Turko (operator-identified name, confirming the "BNI" abbreviation seen in joe-oshnack.md). Consolidates the setlist reconstruction (Misfits, Dead Kennedys, Ramones, NOFX considered-and-rejected, a CKY rehearsal-only cover), the Sept 2021 political retrospective on covering "California Uber Alles" without understanding its politics, and the surrounding hardcore/punk scene (Seth LeDonne's named mentors, "Rejected Gazette"). Updated joe-oshnack.md and seth-ledonne.md with cross-links; resolved the "what BNI stands for" gap previously flagged on joe-oshnack.md.
- Gates: wiki-lint 0 errors (336 pages), wiki-connect check 0 errors.

## [2026-07-20] fix + ingest | interests/timeline | PR #57 bot fix; blocked-caller crisis event
- fix: batteries-not-included.md misattributed "96 Quite Bitter Beings" to NOFX — it's a CKY track (from the band's 1999 album *Volume 1*), correctly caught by bot review after PR #57 had already merged. Fixed in a follow-up commit since the merge raced the fix.
- wiki/timeline/events/april-may-2026-final-weeks.md: substantially expanded the previously thin "unresolved third-party contact (April 1)" bullet using raw/self/dox-md/Crisis mode briefing.md — a recurring blocked-caller impersonation campaign targeting Suz directly (personally insulted as a "junkie," a hostile "you had guys molest me" message to Dan, a threat from Suz to do something "arrest-worthy"), with a forensic case (Suboxone misnamed "heroin/Percocets," register mismatch, absent name-use) arguing against it being Annie personally — though her awareness/complicity is explicitly left unresolved, matching the source's own honesty about not identifying the caller. Also documents a live, real-time instance of the conflict-engine mechanism (a screaming match with Suz over whose grievance mattered more) already documented at scale elsewhere. Added connections + source to wiki/people/suzanne-frank.md.
- Gates: wiki-lint 0 errors (336 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | mind | ai-collaborative-analysis.md — ghostwriting vulnerability, then declining to send it
- wiki/mind/synthesis/ai-collaborative-analysis.md: added a new documented interaction mode from the same Crisis mode briefing.md source — Dan asks an AI to draft an explanatory letter to Suz with no restrictions on included criticism; the model produces genuinely vulnerable first-person material (owning the "would choose Annie over anyone" admission), which Dan then declines to send in his own voice, asking instead for third-party mediated framing. A new pattern beyond the already-documented memory/forensic/honesty-enforcement uses: outsourcing the authorship of vulnerability itself.
- Gates: wiki-lint 0 errors (336 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | work | ai-video-essays.md (new)
- wiki/work/tech/ai-video-essays.md (new): a 2026 planning-stage project — long-form (30-60 min) video essays about AI for non-technical audiences, reverse-engineered from a Some More News structural analysis into a reusable five-element framework (thesis/conceit/evidence chain/tonal modulation/demonstration). No script or video was ever produced. Notable moment: Dan's first concrete pitch (millennials mistake AI for crypto 2.0) was stress-tested against real adoption data at his own request and came back contradicting his premise — he accepted the correction rather than defending the original claim, a real instance of the honesty-enforcement pattern applied to a personal creative ambition.
- Gates: wiki-lint 0 errors (337 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | mind/health | attachment-model.md + hyperreflexivity.md — "mojo and magic" and the parasitized-loop reframe
- wiki/mind/concepts/attachment-model.md: added a new self-described concept — Dan's "mojo and magic," an "attraction outcome thing" felt as functionally absent since Annie — reframed by the same AI session as captured rather than deactivated (locked onto the one target where the feedback loop can't close). Adds a sharp comparative data point: seven years living with Alexis with no future ever mentally built, contrasted against Annie as the first full attachment-system activation.
- wiki/health/hyperreflexivity.md: added a follow-up session's reframe of the anxiety loop as largely "parasitized" by the unresolved Annie situation and a "post-June housing void" rather than a freestanding clinical pattern — signal, not noise.
- Gates: wiki-lint 0 errors (337 pages), wiki-connect check 0 errors.

## [2026-07-20] rewrite | people | swarm-stub batch 1 of 3 (aaron, charles-davenport, dakota, josh-brannan, maddox)
- Rewrote 5 untouched 2026-06-23 swarm-template stub pages (identified by date_created==date_modified plus the literal "## Identity / ## Corpus Dimensions / ## Domain: Self / ## Notes / ## Related" fragment-chain shape) to current STYLE_GUIDE prose + typed `connections:`.
- wiki/people/aaron.md: the "thin 38-message stub" turned out to hold a real-time, same-day reaction to the Sept 11, 2025 Charlie Kirk assassination ("I mean I don't think killing CHARLIE KIRK solves anything...But I'm not upset about it"), plus earlier warmth toward the Luigi Mangione killing — previously entirely undocumented outside the archived wiki/self/twitter.md. Added parallels connection to wiki/self/twitter.
- wiki/people/charles-davenport.md: converted a 4-message table into prose; added a co-occurs connection to the new wiki/places/424-bedford-ave.md (the Jan 2010 exchange lands in the Brooklyn-arrival window).
- wiki/people/dakota.md and wiki/people/maddox.md: both rewritten as short pages pointing to wiki/work/bfs-foods.md's existing "## The cast"/"## The Timmy precedent" sections rather than re-narrating the Timmy blame-pivot chain a third time; each keeps its distinguishing detail (Dakota = originating hearsay disclosure; Maddox = fuller first-person May 21 sidewalk corroboration, full quotes preserved).
- wiki/people/josh-brannan.md: fresh-mined the raw FB thread (41 messages, previously only partially represented) — a warm Feb 2017 reconnection with an old Uniontown friend, including an unprompted, undefensive admission of the webcam-modeling job ("DUDE IM A MODEL WE ARE MODEL BROS"). Added parallels connection to wiki/people/jerad-friedline.md re: the separate "josh brannan is innocent.wav" running joke.
- Updated wiki/people/index.md one-liners for all 5.
- Gates: wiki-lint 0 errors, wiki-connect check 0 errors.

## [2026-07-20] ingest | people | operator-provided full two-sided iMessage exports (shelbie-breakiron, dimitri, alexis-armel, bekah-fullem)
- Operator gained a new extraction capability (both sent+received, not just received) and supplied full exports for 4 threads previously limited to one-sided or unreliable-direction data. Filed to raw/self/message-csv/ as imessage_export_<number>_both_all_now.csv.
- wiki/people/shelbie-breakiron.md: full rewrite. The real thread is 685 messages (not the 306 previously extracted) — reveals the relationship as an explicit "sugar dad" arrangement (Dan financially supporting her camming/stripping work, a $5,000 figure, a laptop), full visibility into Dan's flat, unbothered replies during the July 16 2019 breakup tirade (previously only her side was visible), and a previously-undocumented August 2019 legal-threat follow-up ("i'll be stopping by with a few state troopers").
- wiki/people/dimitri.md: resolved the page's own flagged gap ("0 sent? needs a corpus re-check") — the full 116-message export shows Dan replied regularly; the earlier one-sided read was a direction-field artifact. New content: restaurant-industry shop talk, a genuine Alexander-the-Great/Macedonian-Greek-identity argument, a 2024 political exchange, and a first-person, contemporaneous account of the Aug 21 2024 Au Za'atar job loss ("They officially let me go... We parted on good terms").
- wiki/people/alexis-armel.md: replaced the "41 messages, received-only" framing (the post-breakup 2020-2025 channel) with the full 88-message two-sided record — a real, warm, intermittent friendship (Twitch streaming plans, 2020-election commentary, a shared friend's death by domestic-violence-linked suicide processed together in real time Jan 2021) that ends on a small poignant note: a February 2025 wrong-number exchange where Alexis doesn't recognize Dan's number.
- wiki/people/bekah-fullem.md: full rewrite with a real correction — the previous version had the March 29 2020 pandemic-severity exchange backward, describing Bekah as pushing back against "Dan's skepticism." The full export shows the opposite: Dan is the one insisting COVID is worse than reported (frontline NYC vantage), Bekah repeatedly says she already knows. Also resolves whether the Feb 2020 cat-medication money was sent (yes — an image + "that'll even the score"), surfaces a pre-existing flirtation before the crisis contacts, and documents Dan's actual (warm, appropriate) response to her rape disclosure. Surfaces one major new, unverified fact: Dan tells Bekah that Annie is herself a rape survivor with a 45-year sentence for the assailant — added to wiki/people/annie-ulmer.md as an explicitly flagged, single-source, unverified claim (evidences/evidenced-by connection pair).
- Updated wiki/people/index.md one-liners for all 4.
- Gates: wiki-lint 0 errors (337 pages), wiki-connect check 0 errors.

## [2026-07-20] rewrite | people | swarm-stub batch 3 of 3 (sean-teets, shannon) — final batch, all 12 swarm stubs closed out
- wiki/people/shannon.md: fresh-mined the full 23-message iMessage thread previously represented by only its opening line — reveals Shannon was a real estate client who hired Dan for drone photography/video, Nov 2018 – Jan 2019 (scheduling, listing-photo delivery, one file-delivery friction point), the corpus's only documented instance of Dan doing paid drone work for a client.
- wiki/people/sean-teets.md: converted the 7-message table to prose; identified the two outreach messages ("looking for tax or strpz"; "Mushys and k") as likely supply-seeking language consistent with wiki/health/chemical-architecture.md's substance vocabulary (mushrooms, Suboxone strips, ketamine), added as a co-occurs connection with an honest caveat that Sean's specific role isn't established.
- Updated wiki/people/index.md one-liners for both.
- Closes out the 12-page swarm-stub rewrite task in full (batch 1: aaron, charles-davenport, dakota, josh-brannan, maddox; batch 2: marc-charles, marty-martin, max-danielle-bf, michael-hinkle, ryan-lisac; batch 3: sean-teets, shannon).
- Gates: wiki-lint 0 errors, wiki-connect check 0 errors.

## [2026-07-20] fix | people | PR #59 bot review — wikilinks + truncation-safe openers
- Addressed 6 gemini-code-assist review comments on PR #59: converted plain-text `bfs-foods`/`jerad-friedline` references to wikilinks in wiki/people/index.md, dakota.md, and josh-brannan.md connections claims; split the overlong opening sentences on dakota.md and maddox.md that were causing the auto-generated llm/manifest.json summary to truncate mid-link.
- Gates: wiki-lint 0 errors, wiki-connect check 0 errors.

## [2026-07-20] rewrite | people | swarm-stub batch 2 of 3 (marc-charles, marty-martin, max-danielle-bf, michael-hinkle, ryan-lisac)
- wiki/people/marc-charles.md: converted an 85-message golf/music thread into prose — a 2018 golf-equipment-and-scores exchange plus a warmer 2017 mutual sobriety-milestone acknowledgment ("I'm 7 years clean from opiates" / "4 years in august") tied to old shared music recordings.
- wiki/people/marty-martin.md: full prose conversion of the BFS Foods trusted-source page — the "make the store whole to keep your job" framing that anchors bfs-foods.md's structural (not isolated) reading of the drawer-shortage dispute, plus the Suz-relay channel (chili/goulash question, a later job-lead message) and a specific shift-cover reliability example.
- wiki/people/max-danielle-bf.md: condensed a dossier-style page of long verbatim quote blocks (violating the quote-sparingly rule) into prose — Dan handing Gemini a recording of Danielle's boyfriend and requesting a full personality analysis; Gemini's "mirror image" / "Recursive Cognitive Machine" read.
- wiki/people/michael-hinkle.md: previously near-empty placeholder; mined the raw 3-message FB thread (one-sided, unanswered, references Annie and "i found us something").
- wiki/people/ryan-lisac.md: preserved the page's own honestly-flagged gap (the "Snob Squad" childhood narrative isn't present in the ingested raw corpus) rather than inventing content; added the genuinely new finding that Dan's 2026 DJ-identity relaunch deliberately reuses the "Snob Squad" name as a callback — added a parallels connection + inverse edge on wiki/mind/synthesis/totality-themes.md.
- Updated wiki/people/index.md one-liners for all 5.
- Gates: wiki-lint 0 errors, wiki-connect check 0 errors.

## [2026-07-20] ingest | places | 90th-st-manhattan.md (new), seven-springs.md (new)
- wiki/places/90th-st-manhattan.md (new): fills the previously-missing third year of NYC-1 (Mar 2012 – Apr 2013) — the Manhattan UES sublet between the two better-documented addresses. Anchors the Feb 2012 Creative License exit (airfare-billing discrepancies, altered intern contracts) as the founding case for vertical-authority-skepticism, fourteen years before its BFS Foods recurrence, and correctly re-dates the Hurricane Sandy/Bridge Cafe job-loss shock to this address's occupancy rather than the earlier Bedford Ave years.
- wiki/places/424-bedford-ave.md: corrected the Sandy/Bridge-Cafe attribution (the closure happened six months after the household had already moved to 90th St, not during the Bedford Ave years); added the wikilinked follow-on to the new page.
- wiki/places/seven-springs.md (new): the childhood ski-resort social anchor — weekly ritual, family condo (The Villages, Sunridge Unit K2), and the first drug-exposure cohort, with first cocaine use dated 2004 — a full year before the Nov 2005 family-rupture hinge event usually credited as the addiction narrative's start. Notes the regional freeskiing-culture backdrop (Tom Wallisch's home turf) as adult-interest context, not a personal connection.
- Updated wiki/places/index.md.
- Gates: wiki-lint 0 errors (339 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | health/mind | tooth-loss/bulimia link (hyperreflexivity.md), bunker-core.md (new)
- wiki/health/hyperreflexivity.md: added a fourth compounding stressor from the same mid-2025 AI session — Dan's disclosure of losing two teeth, with his own causal chain back to teenage bulimia, candy as a dietary staple, dentist avoidance, Suboxone, and cigarettes. The corpus's clearest first-person link between the eating disorder documented on dark-era-2007-2008.md and a specific, dated adult physical-health outcome. Also corrected an overclaim on chemical-architecture.md ("no detox attempt") — a Dec 8, 2015 exchange, ten days into the Annie relationship, shows a real (if apparently unsustained) joint cold-turkey pact.
- wiki/mind/concepts/bunker-core.md (new): consolidates a named local technical project — SQLite-based forensics on Dan's own chat.db, "Epistemic Verification," shipped alongside the Gumroad iMessage Analysis Toolkit (Feb 2026) — previously scattered as passing references across 4 pages with no dedicated treatment. Carefully separates the documented software fact from an AI-authored "epistemic fortress" interpretive framing found in the source material, flagging the latter as plausible-but-not-Dan's-own-words.
- Gates: wiki-lint 0 errors (340 pages), wiki-connect check 0 errors.

## [2026-07-20] connect | mind | connection-queue.md top-5 processed
- Worked the top of connection-queue.md (mined candidate connections, sorted by score): wiki/mind/synthesis/attachment-trauma-bond.md <-> wiki/timeline/events/eli-incident.md (evidenced-by, both directions, plus a prose wikilink fix from the person page to the event page); wiki/mind/concepts/forensic-method.md <-> wiki/work/tech/max-framework/overview.md (instance-of/contains); wiki/mind/concepts/forensic-method.md <-> wiki/mind/synthesis/attachment-trauma-bond.md (instance-of, both directions); wiki/mind/concepts/conflict-architecture.md <-> wiki/mind/synthesis/attachment-trauma-bond.md (mirrors, both directions); wiki/mind/synthesis/political-psyops.md <-> wiki/mind/synthesis/totality-themes.md (component-of/contains).
- Struck all 5 as done in connection-queue.md.
- Gates: wiki-lint 0 errors (340 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | interests/mind | Google Drive "**DOX" folder — crate data + Phase 2 stylometrics
- Operator pointed at a local Mac path; confirmed via Drive search this maps to the "**DOX" Google Drive folder already partially imported as raw/self/google-drive-export/ (only 6 of 34 top-level items had landed — the "DOX2" import from 2026-07-13 was never completed per queue.md's own plan). Pulled and checked the most promising unimported items.
- wiki/interests/music/aliases/gripnotic.md: new "Current DJ crate (2025)" section from a Spotify playlist export (232 tracks, raw/self/favorites/2025_MASTER_CRATE.csv) — first quantified picture of current mixing practice: 59% of tracks from 2025 itself, genre weights (dubstep 63, bass music 59, bass house 54, tech house 34, riddim 29), avg energy 0.80, avg tempo 133 BPM, no single dominant artist (Fred again.. leads at 6 tracks).
- wiki/mind/profile/linguistic-profile.md: new "Audience-based code-switching" section from a previously-unmined "Phase 2 Stylometric Analysis" doc (raw/self/dox-md/Phase_2_Stylometric_Analysis.md) — a distinct organizing axis (romantic/platonic vocabulary, supportive/conflict linguistic signatures) alongside the existing emotional-state-mode framework; added a parallels connection + inverse edge with voice-modes.md.
- Added connections: blocks (previously absent) to socionics-and-attitudinal.md (evidences forensic-method.md) with inverse edge.
- Deprioritized two other checked items: "_AI Protocol for Persuasion.md" (confirmed to be the same GLAZE-GOD-v1 material already documented on erotic-architecture.md — no new content); SPOTIFY LIKED (END 2025).numbers (Apple Numbers binary format, not convertible via available tools — skipped).
- Marked the stale "Target G" queue.md item as verified-already-done (fully documented on annie-ulmer.md and suzanne-frank.md, contrary to the backlog note).
- Gates: wiki-lint 0 errors (340 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | health | ADDICTION PROFILE doc — genesis chronology + cocaine dosage arc
- Continued the "**DOX" Drive folder sweep into the FULL DATA STACK subfolder. Checked ADDICTION PROFILE, SEXUAL PROFILE, and Favorites/FAVORITES DATA docs.
- wiki/health/chemical-architecture.md: new "System genesis: a phased history" section from raw/self/dox-md/ADDICTION_PROFILE.md — genuinely new dated facts: cocaine first entered the household as a known concept at age 13 (2001), predating the Nov 2005 family rupture by 4 years; a November 2007 Las Vegas trip newly dated as the point physical opiate dependence became undeniable; a winter 2008 single heroin attempt rejected on aesthetic grounds ("felt dirty"); and the corpus's first quantified cocaine dosage arc — ~1g/day baseline escalating to 3.5-7g/day during the 2017-2020 inheritance-funded window, contracting back to ~0.5-1g/day from 2020 as the inheritance was exhausted (a resource adjustment, not a step toward moderation, per the source's own framing). Added connections + inverse edges to seven-springs.md and dark-era-2007-2008.md.
- SEXUAL PROFILE doc: confirmed to overlap heavily with already-documented ground (erotic-architecture.md, psychosexual/ cluster — same ELI_INCIDENT, externalized-libido, taboo-as-rupture concepts) — deprioritized, archived only.
- Favorites / FAVORITES DATA docs: confirmed near-duplicates of the already-ingested raw/self/favorites/FAVS MASTERLIST.csv (matching movie list already on film-canon.md, matching concert list already on timeline/events/teen-concert-years.md) — no further action needed.
- Gates: wiki-lint 0 errors (340 pages), wiki-connect check 0 errors.

## [2026-07-20] ingest | mind | spatial-behavior.md (new) — GPS forensic analysis
- PR #59 merged; restarted branch from origin/main. Operator broadened scope: mine anything in the full Google Drive, including hard-drive scans.
- wiki/mind/synthesis/spatial-behavior.md (new): a behavioral/psychographic reading of Google Location History data (raw/self/dox-md/GPS_ANALYSIS.md), distinct from and built on top of the raw visit-count catalog on wiki/self/location-history.md (left untouched — status: archived). Core finding: movement resolves into four sharply-bounded life phases rather than gradual drift — "The Forge" (2014, Uniontown baseline), "The Binary System" (2015-17, the Annie two-node oscillation straining under its own cost), "System Collapse & Migration" (2018-19, over a third of the entire 2014-2020 aggregate travel distance logged in 2018 alone, resolving in the NYC move), and "The Siege of Manhattan" (2020 COVID compression). Explicitly flags a methodological caution the source material doesn't raise itself: the low-novelty/high-routine spatial signature is read there as a chosen psychological strategy, but chronic financial constraint (documented independently on 2017-poverty-floor.md/2018-deep-cycle.md) would produce an identical signature for different reasons — added as a contradicts connection rather than silently endorsing the source's framing.
- Gates: wiki-lint 0 errors (341 pages), wiki-connect check 0 errors.

## [2026-07-20] fix | mind/timeline | PR #60 review response
Addressed 3 gemini-code-assist review comments on spatial-behavior.md:
split truncated opening sentence, corrected location-history connection
type instance-of -> contextualizes, added missing inverse connection on
2017-poverty-floor.md. Gates clean (0 errors). Regenerated llm/. All
three review threads resolved on GitHub.

## [2026-07-20] triage | interests | BOOKS.csv (Drive/MEMORY) duplicate check
Downloaded and reviewed BOOKS.csv (Drive MEMORY folder, Goodreads export
format). Confirmed duplicate of raw/self/google-drive-export/goodreads_library_export.md
already cited on wiki/interests/favorites/books.md — every distinctive
title checked (Carlin, Holland's Rubicon, Goldsworthy's Caesar, Shirer,
Bird's American Prometheus, and the Jacob Bacharach "Doorposts" 5-star
2022 read) is already captured on that page, including the specific
jacob-bacharach.md cross-link. No new signal. Deprioritized, no wiki changes.

## [2026-07-20] triage | self | Drive "MEMORY" folder confirmed duplicate archive
Sampled 4 files from Drive MEMORY/STORYTIME folder (id 1eAILXQoPk6owa7_nfFx0mZU6xBCHdL8j):
BOOKS.csv (dup of goodreads_library_export.md, see prior log entry),
"Dan Frank_ Profound Psychological Speculations_" (= the exact DANSYNTH
source already synthesized as wiki/mind/synthesis/ancestral-dialectic.md),
"Fraan" storytime doc (= source of wiki/timeline/events/fran-death-vigil.md,
same 8am/keno/IMG_0569.MOV details verbatim), "Au Za'Atar" storytime doc
(= source of wiki/work/au-zaatar.md, same Dimitri/Tunisian-manager/Sergio
details verbatim). Conclusion: this Drive folder is a re-uploaded backup
of the already-mined DANSYNTH/STORYTIME corpus, not new material.
Deprioritizing remaining unopened items in this folder (2_PHENOMENOLOGY
PROFILE.md, 1_CORE PROFILE.md, FULL PROFILE 2026.md, THE_DAN_FRANK_BOOTLOADER.md,
Location History subfolder, MUSIC LIST(start-2024).csv, YOUTUBE WATCH HISTORY
html — all by-name matches to already-ingested raw/ sources) without
opening each individually. Moving to the flagged-high-priority "NEW LOADER"
folder (OMNI_FORENSIC_DOSSIER.md, THEORY OF EVERYTHING 31 MAR) next.

## [2026-07-20] ingest | mind | OMNI_FORENSIC_DOSSIER + BIBI_PERSONALITY_DECONSTRUCTION (Drive NEW LOADER)
Mined two AI-generated forensic corpus analyses from Drive's flagged
"NEW LOADER" folder. Both heavily overlap already-ingested material
(exact-match numbers with linguistic-profile.md: 23,286 vocab, "because"
2,465, "I don't" 1,845, "I'm not" 814 — confirms same underlying NLP
extraction) but contained three genuinely new signals, added to the wiki:
(1) a whole-corpus yearly message-volume arc 2015-2026 added to
message-circadian-latency.md — first hard numbers for the 2021-2022
near-total-silence trough (280 + 4 msgs) and precise 2018/2025 peak
figures (40,514 / 41,278, within 2% of each other), with inverse
connections added to 2018-deep-cycle.md and 2025-collapse.md; (2) a
camming/non-monogamy word-frequency table added to
wiki/mind/psychosexual/arrangement-history.md (304 camming tokens vs 107
non-monogamy/kink tokens, ~3:1); (3) the "Broken Engine" self-mythology
framing ("weaponized self-awareness as preemptive strike") cross-referenced
into deviance-mapping.md's existing "Mythology of Ruin" outlier entry.
Archived both source docs to raw/self/dox-md/. Gates: 0 errors both.
Remaining NEW LOADER items (THEORY OF EVERYTHING 31 MAR, podcast
transcript, Stylometric/Linguistic docs, masterloader PDFs) not yet
checked — next up.

## [2026-07-20] ingest | people/timeline | End Fight podcast transcript (Drive NEW LOADER)
Mined a NotebookLM-style AI podcast dramatization of the already-documented
May 31-June 1 2026 End Fight / group-chat closure. Confirmed the core event
is already extensively covered (end-fight.md, group-chat-closure.md,
tuquick-17248123683.md, dan-annie-fallout-verdict.md) but the podcast
supplied granular detail not previously captured: Dan's absurdist
derailment tactics used against Tuquick (TRANS RIGHTS ARE HUMAN RIGHTS,
Carthage geography, Israel non sequitur), Tuquick's mid-fight de-escalation
(laughing, "no hard feelings") two weeks before his already-documented
June 15 defection, Annie's false broken-finger claim debunked by Tuquick
himself, the exact 23:54 verbatim/timestamp of the false sexual-assault
accusation, and — genuinely new fact — a prior ~May 26 2026 incident where
Tuquick spent three hours harassing Suzanne Frank by phone, five days
before the main confrontation. Added as a REVISED block on
tuquick-17248123683.md (correcting the prior "remained focused on the
attack" framing), a new section on suzanne-frank.md, and a verbatim/date
addition to group-chat-closure.md's Data Record — all flagged as sourced
from a secondary AI dramatization pending raw-row confirmation, consistent
with the corpus's existing primary-recount discipline. Also checked
THEORY OF EVERYTHING 31 MAR (Drive NEW LOADER): confirmed its
quantified claims (74/17/11 abuse triad, 1,512/232/180 triad, 299
affirmations, 187:4 test) are already incorporated and independently
re-verified on dan-annie-fallout-verdict.md; its "Girlfriend Score"
framing (Annie 1.9/10 vs Alexis 7.1/10) is new packaging of already-
captured stats, not new signal — not added. Podcast transcript archived
to raw/self/dox-md/. Gates: 0 errors.

## [2026-07-20] triage | self | NEW LOADER folder remaining items checked
Checked remaining unopened items in Drive NEW LOADER folder: "extract"
(a chat.db SQL-query-generation prompt, confirms already-documented
bunker-core.md tooling, no new signal) and "load" (the MAX persona master
system prompt, already documented on wiki/mind/concepts/exocortex.md's
bootloader list — "MAX_KERNEL_DUMP_V2," radical-skepticism/normie-filter
framing matches exocortex.md's existing MAX summary). Stylometric Profile
docs and Phase 2 Stylometric Analysis previously confirmed already-ingested
(linguistic-profile.md). Not opened: masterloader.pdf/masterloader2.pdf
(binary PDFs, likely compiled versions of already-seen bootloader text),
messages_2124702449.csv alias (916 bytes, likely a stub/shortcut file not
real data), .DS_Store (not content), an .mp3 audio file (out of scope for
text mining). NEW LOADER folder considered fully triaged. Next: the two
large ChatGPT conversation-export JSONs (dfrankconversations.json ~35.7MB)
flagged earlier as a genuinely new, unopened AI-chat corpus distinct from
the Gemini archive — needs dedicated download+extraction handling in a
future pass given size.

## [2026-07-20] ingest | timeline | ChatGPT export first pass — Feb-Apr 2025 gap filled
Operator directly uploaded the ChatGPT conversations.json export (375
conversations, 2022-12 to 2025-07) after Drive's own MCP tools proved too
size-limited for it (download_file_content times out; read_file_content
mangles JSON with markdown-escaping and truncates at ~900K chars). Full
export archived to raw/self/chatgpt-export/dfrank-chatgpt-conversations-2022-2025.json.
Sampled ~10 conversations. "Mom Info Logged" confirmed fully duplicate of
already-ingested biography (Danielle/Franki/Alexis/Annie dating chronology,
Fran/Arnold Palmer/Ira Coldren) — strong confirmation of wiki completeness.
"Relationship Breakdown Summary" (2025-04-27) was genuinely new: mined into
a new page, wiki/timeline/periods/feb-apr-2025-return-and-rupture.md,
filling the previously undocumented Feb-April 2025 gap between the January
2025 affair discovery and the Aug-2025-onward terminal-phase record already
on dan-annie-fallout-verdict.md. New facts: the NYC apartment "shot clock"
exit (~$10k owed + $7k ConEd bill), Annie's unilateral move to her parents
against Dan's open-ended funded-apartment offer, and — genuinely new to the
corpus — Suzanne Frank's 2024 personal bankruptcy and a spring-2025 listing
attempt on 337 Saratoga Drive a full year before the eventual 2026 sale
already documented on suzanne-frank.md. Added connections to
2025-collapse.md, suzanne-frank.md, annie-ulmer.md, dan-annie-fallout-verdict.md,
and a timeline/index.md entry. "Whisk AI Prompt Injector"/"Whisk Emergency
Fabric Design" checked and ruled OUT as related to the documented
fabricated-evidence pattern (false lead from title similarity — both are
unrelated jailbreak/creative-writing tangents). Remaining ~365
conversations tracked in queue.md as a multi-pass backlog, prioritized:
Camming Career Review, Babbitt Shooting Psy-Op Debate (possible original
J6 source predating the Gemini-based material), the facial-feature/
ideal-face cluster (~12 convos, purpose not yet understood), Interpersonal
Analysis Request, Breakup Brain Dump, Personality Breakdown IRL. ~180
early 2022-2023 conversations are generic political/history discussion,
spot-checked and deprioritized as low-yield. Gates: 0 errors.

## [2026-07-20] triage | mind | ChatGPT export follow-up: Babbitt psyop + camming review
Checked two more flagged ChatGPT conversations. "Babbitt Shooting Psy-Op
Debate" (2025-06-15) confirms rather than extends the already-documented
J6 "Operation Wildfall" hybrid thesis, but is dated 7 months before the
Gemini codification and on a different AI platform — added as a
chronology note to political-psyops.md. "Camming Career Review" (2025-06-07)
turned out to be an image-analysis conversation with no extractable new
facts (AI flourish responding to uploaded screencaps, not text data) —
no wiki action, logged as lower-value-than-title-suggested in queue.md.

## [2026-07-20] ingest | people | operator-provided Mike Cordaro export (imessage_17243226739_both_all_now.csv)
Filed a proper per-contact export (50 messages, reliable Sent/Received
direction) to raw/self/message-csv/, superseding the earlier 28-message
partial pull off the unreliable-direction master CSV. mike-cordaro.md
Corpus Dimensions corrected (28 -> 50 msgs; direction now confirmed
reliable, genuine two-way conversation). Texture section expanded with
the full 2024-election exchange (Mark Kelly/Shapiro/Walz/Bernie-endorsement
reasoning on both sides, the "DEI hire" line, the enthusiasm-boost-on-18-35
argument) previously only summarized. Converted the bare related:/##
Related footer to a typed connections: block — a new `parallels` edge to
rick-frank.md (the "maga-tized dads" framing), with inverse added on
rick-frank.md. Gates: 0 errors.

## [2026-07-20] correction | mind/timeline/people | Eli discovery text + two other flagged claims upgraded [DOSSIER]->[RAW-CSV]
Operator uploaded a fresh export of Annie's current 212 number
(imessage_export_2124702449_20260720210349.csv, Aug 2025-Jun 2026) flagging
the Eli discovery text as locatable within it and specifically dated. Cross-
check found it a near-duplicate of already-filed raw/self/message-csv/
imessage_2124702449_both_all_now.csv (same window, 23448 vs 23719 rows) —
NOT re-filed to avoid raw/ duplication. Neither file covers Jan 2025 (both
start effectively Aug 2025 with only stray isolated rows before that), so
the Eli text itself (Jan 9 2025) is not in this specific export — but the
question prompted a wider re-search that found it elsewhere in already-
filed raw/: raw/self/message-csv/imessages_2124702449_last6months.csv and
raw/self/dox-scan/all_imessages_complete_dump.txt both have the full six-
message rapid-fire sequence starting 2025-01-09 23:18:49, verbatim. The
2026-07-18 pass had searched for the quote as one string and missed it
because iMessage sent it as six separate messages. Primary-confirmed
sequence entered on eli-incident.md (REVISED block) and eli.md, including
a genuinely new fact: Dan's own real-time reply, "Who are you?", sent
23:19:42 between Eli's third and fourth messages — not previously
documented anywhere in the corpus. dan-annie-fallout-verdict.md's "What
still needs primary verification" section updated: Eli text resolved;
the Mar 16 2026 "I misunderstood the conversation" retraction line also
found already sitting in imessage_2124702449_both_all_now.csv (2026-03-16
18:47:51) — same story, a prior pass's search missed it; and the "Jan 24
procurement line" resolved to the Jan 24 2026 ketamine-procurement
messages (Tom's 2am delivery; "I grabbed some ketamine for us"). Three
flagged gaps closed in one pass, all from data already on disk. Gates:
0 errors.

## [2026-07-20] ingest | work | DANMODEL — new page, a working voice-cloning ML pipeline
Mined the Drive "DANMODEL" folder queued earlier this session. Filed
raw/self/danmodel/extraction_summary.txt, PIPELINE_NOTES.md (architecture
transcription of 5 Python scripts — a byte-exact copy attempt corrupted
during manual base64 reconstruction, so this is a faithful logic
transcription instead, with original Drive file IDs cited for provenance),
and reaction_pairs_heldout.jsonl (4,570 rows, verbatim, mechanically
decoded and verified against the summary count). New page
wiki/work/tech/danmodel.md: a from-scratch pipeline that extracts 39,378
stimulus-response pairs from Dan's own message corpus (verified: Annie
early alone = 40% of the total, corroborating contact-gini's 0.961
concentration in an independent metric; year distribution independently
reproduces the already-documented 2018 deep-cycle and 2025-collapse
peaks), builds both a naive Jaccard-retrieval baseline and a TF-IDF+RAG
generator wrapped in a self-authored "CATO_COMPACT" voice-persona prompt
(preserved verbatim — genuinely new primary data on how Dan characterizes
his own texting signature), and designs a rigorous blind LLM-judge eval
(neutral-labeled real-vs-fake, leakage assertions) to test whether the
clone passes for him. Notable finding: no eval_results file exists
anywhere in the Drive folder, so whether the blind test was ever completed
— and what it found — is a genuine, flagged gap, not a negative result.
Wired into wiki/mind/concepts/exocortex.md, wiki/work/tech/mneme/overview.md,
wiki/mind/synthesis/ai-collaborative-analysis.md, wiki/people/annie-ulmer.md,
and wiki/mind/concepts/contact-gini.md (5 typed connections + inverses),
and wiki/work/tech/index.md. Gates: 0 errors.

## [2026-07-20] ingest+correction | self/mind | fresh YouTube Takeout export -- multi-account caveat found and applied
Operator found a new Google Takeout export in Drive (created today,
890MB, too large for this session's download tooling) and supplied the
watch-history.html directly after unzipping it locally. Filed to
raw/self/youtube-watch-history/YOUTUBE WATCH HISTORY (2010-2026-07-20).html
(19MB, extends real coverage to 2026-07-20, ~1 year past the old export's
Jul 25 2025 cutoff). Verified re-parse found 14.1% of the OLD export's
"Watched" entries are Google Ads impressions, never previously broken out
from real content in this page's published counts. Initially flagged (in
error) a ~100-day near-zero-real-watch window, Nov 8 2025-Feb 15 2026, as
a candidate contradiction of intake-constancy.md's flat-rate thesis --
**operator corrected this directly and immediately**: this Google login
has multiple YouTube accounts, he was using a different one during that
window, and true daily watch volume is confirmed higher than either the
existing 11.58/day figure or this session's ad-filtered 9.53/day
recomputation. Both figures downgraded from "verified constant" to
"single-account lower bound" on intake-constancy.md (inline flag in the
Two Constants section + expanded Gaps entry with the correction recorded
in full) and on youtube-watch-history.md (REVISED/operator-correction
blocks). New "Extended coverage" section added to youtube-watch-history.md:
the Aug2025-Jul2026 monthly real-vs-ad table, new top channels for the
window (Breaking Points, LastWeekTonight, Majority Report continuous with
the existing 2022+ diet; Tor's Cabinet of Curiosities, We're In Hell,
JREG, STRANGE AEONS, exurb1a, DJ Peach Cobbler new to the corpus), and the
June-July 2026 finding that apparent high raw volume is 80-96% ad noise,
real watching comparatively modest. Status changed archived->active
(page is not under an archive/ dir and is now an actively growing
dataset). 6 connections added/updated across youtube-watch-history.md,
intake-constancy.md, and march-2026-terminal-phase.md (with inverse).
**Lesson: verify a striking data-driven finding with the operator before
treating it as settled, especially when the corpus's own governing page
(intake-constancy.md) explicitly names "check for a routing/account
artifact first" as the required discipline for exactly this situation.**
Gates: 0 errors.

## [2026-07-20] ingest | people/work | Tarik Fallous full per-contact export — REVISED, no-message-corpus claim was wrong
Filed raw/self/message-csv/imessage_19178259183_both_all_now.csv (80
messages, Aug 2023-Apr 2026, reliable direction). This directly
contradicts the page's prior claim that "no direct message thread exists"
for Tarik — REVISED block applied. tarik-fallous.md substantially
rewritten with a new Direct Correspondence section: employment-logistics
texture not documented elsewhere (grocery-run errands on Tarik's own
Barclays card, two verbatim wine/liquor inventory counts, hiring-interview
coordination, a Dec 2023 payroll dispute, 5 sick-day call-outs, an Arabic
wedding-congratulations exchange) plus a genuinely new post-termination
finding: Dan kept passing Tarik informal workplace "CIA agent" intel 13
days after filing for unemployment, and the two remained in warm, openly
political contact through Apr 12 2026 (Lebanon-conflict solidarity
messages, Sep 2024 and Apr 2026) - nearly two years after the job ended.
Five new unresolved names surfaced: Modi, MD, Patricia, Khalid, Hani.
Status changed closed->active (relationship is ongoing, not closed with
the employment). Converted related: to typed connections: (4 edges +
inverses on au-zaatar.md and ismaila-barry.md); au-zaatar.md gained a
corroborating sentence on the de facto-manager role. Gates: 0 errors.

## [2026-07-24] revise | people | full re-analysis and rewrite of annie-ulmer.md
Operator-directed full top-to-bottom re-analysis of wiki/people/annie-ulmer.md
(a critical-importance exemplar page). Re-extracted all seven
DanAnnie_*.docx dossiers (MasterRecord_FINAL, MasterRecord_March16,
TenYears_WithAmendments, TheoryOfEverything_Updated, CompleteRecord_Final,
CompleteAnalysis_Final, MoralAnalysis_SFW) via direct XML parse after
libreoffice headless conversion failed in-session, plus re-read the
CorrectiveAddendum, the DUI affidavit, and the two prior operator capture
notes. Independently re-verified the core message-corpus numbers against
the raw dual-handle CSV (88,549 lines; 44,513 sent / 41,073 received — both
confirmed by direct count, matching every figure the dossiers cite from
them). No headline conclusion changed (gaslighting-outweighs-affair verdict
stands unrevised), but the rewrite added: the full year-by-year message-ratio
table (2015-2025) from the dossier appendix; the verbal-abuse monthly
escalation trajectory (9->0->5->14->22->25->36->7) and the 47-instance
hostility-after-warmth finding; the unexecuted-threat pattern (18 block
threats, 6+ maternal-disclosure threats, both ~100% unfollowed); a corrected
wellbeing-check figure (7 raw / 4 genuine after removing perfunctory
acknowledgments, vs. the page's prior uncorrected "7"); and new escort-economy
detail mined from raw/people/annie-ulmer/escort-messages-chatgpt-export-2025-08.md
(previously unlinked from this page) — the Nabeel and Jason client threads
under Annie's "Hazel"/"Lily" persona, alongside the Jared/Tricia thread
already documented on wiki/people/jaredtricia.md. Restructured the whole
body into fresh prose (arrangement, financial oscillation, Eli affair,
terminal phase, March 2026 confession/retraction/bathroom-incident sequence,
closure, structural analysis) while preserving every earned conclusion and
REVISED/CONTRADICTION blockquote from prior passes per the second-brain
revise-don't-regenerate rule. Sources list gained the escort-messages export
and the 2026-07-13 Eli-vs-Tuquick capture note. bin/wiki-lint: 0 errors (page
flagged only for its pre-existing advisory size warning, exempt as a critical
hub page). bin/wiki-connect check: 0 errors.

## [2026-07-24] revise | people | annie-ulmer.md — reimagined from scratch, second pass
Operator feedback on the same-day rewrite above: it kept the prior page's
section names, paragraph order, and much of its original sentence-level
prose despite being framed as a rewrite. Operator asked for the page to be
reimagined from scratch rather than revised in place. This second pass
discards the old skeleton entirely and adopts a different organizing
structure: the moral verdict opens as its own named section instead of
arriving at the end; Annie's pre-Dan biography is split out from the 2015
origin story; the sexual arrangement, the jealousy kink, and the
Hazel/Lily escort-economy material are consolidated into one thematic
"architecture" section instead of being threaded through a chronological
arc; the financial oscillation and the payment-app figures get their own
section; the terminal-phase mechanisms are regrouped by whose instrument
they are (Annie's / Dan's / neither's) rather than presented as a flat
bulleted list; and all quantitative tables are consolidated into one "By
the numbers" section near the end instead of being scattered inline. No
facts, figures, or citations changed from the verified same-day pass —
this was a structural and prose rewrite only, not a re-research pass —
but every paragraph was written fresh rather than edited from the prior
draft. Two small typos introduced during the rewrite (a duplicated word,
a garbled date) were caught and fixed before commit. bin/wiki-lint: 0
errors (advisory size warning only, exempt as a critical hub page).
bin/wiki-connect check: 0 errors.

## [2026-08-01] climb | mind | alias-as-periodization.md — new T2 junction page
Climbed synthesis-queue cluster #14 (score 12.80, domains interests+mind:
the three alias pages, the music overview, and totality-themes). The rule:
every alias change coincides with a life-period boundary, and no alias change
coincides with a change in either musical invariant — the involuntary 63-85%
sub-bass band or the complete absence of sung original lyrics. The individual
alias pages each describe their rename as an artistic progression; read across
each other that progression dissolves, because all three independently report
the same measurement and the same remix-only output. Conclusion: the alias is
a periodization device, not a style, and an alias boundary is therefore
admissible evidence for dating a life transition independent of any narrative
around it. Stated with three explicit falsifiers, and three gaps named on the
page (mogged-up unexamined, the 2014/2015 handoff overlap unresolved, and the
63-85% figure asserted three times from a single provenance rather than
re-measured per alias).

Loop closed both ways: the page declares synthesizes: over its five members,
and sloppp / mogzart / gripnotic each gained an instantiates edge back into it.
Linked from wiki/interests/music/overview, where the existing sentence claiming
the aliases map to distinct "periods and aesthetics" is now explicitly disputed
rather than left to disagree silently.

bin/wiki-lint: 0 errors, no orphan. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 321 pages, 12 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-01] climb | mind | instrument-is-subject.md — new T3 doctrine
Climbed the densest recurring signal in the queue: ai-collaborative-analysis
appears in five separate unclimbed clusters (#2, #3, #8, #16, #17), which is
the strongest unanswered pattern the candidate miner has ever produced.

Three facts already recorded separately and never put in one sentence: this
wiki is written by an LLM; its subject uses LLMs as a documented daily
cognitive organ; and its evidentiary standard is downstream of a prompt that
subject wrote. Together they give the project's governing methodological
constraint — the instrument compiling the second brain is the same class of
instrument that is one of its subjects, so no page here is an independent
observation of that relationship.

The operational finding, which is the point: the contamination compounds with
ALTITUDE. An interpretive frame enters as T2 marked knowledge: mixed; a T3
climbs from it; if provenance does not travel, a model's reading of Dan has
been silently promoted to a premise about Dan. Rule: knowledge: must propagate
upward — a page synthesizing a mixed page cannot be earned unless it adds
primary evidence.

Introduces a distinction the repository has been making implicitly and never
by name: RESIDUE (timestamps, alias boundaries, watch histories — produced for
other reasons, admissible) vs TESTIMONY (AI readings, self-descriptions,
dossiers — produced to characterize, requiring provenance). Testimony cannot
become residue by being cited three times.

Page names three falsifiers and three gaps, including that it is itself an
instance of the problem it describes and a reader may reject its claim to
knowledge: earned.

bin/wiki-lint: 0 errors, no orphan. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 322 pages, 13 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-01] write | mind | three commissioned entry concepts
Operator-commissioned: three high-importance entry pages, written from the
corpus rather than from the brief. All three are ~10-11KB, deliberately over
the 8KB advisory budget (operator asked for the longest and most data-rich in
the corpus); size warnings are expected and accepted, as with the existing
work/ hub pages.

the-cool-metric.md (concept) — Dan evaluates culture, objects and people on a
single performed-vs-authentic axis, with coolness as the operational proxy.
The finding that earns the page: the metric is COMPILED, not merely held. The
bootloader carries a literal standing instruction — "The system must
immediately pass a check: 'Did you just treat Dan like a normie?'" — plus
"anti-normie tone alignment" as a prompt-design mandate and Anti-Normie as a
declared Current Vibe / Logic State with cite dates. Social use is stated in
the corpus as filtration: an anti-normie persona deployed "to weed out
disingenuous participants," irony-coded so the person being sorted cannot see
the test. Includes the graded taxonomy (the Millennial Cringe cluster
objected to for performing transgression while carrying zero structural
threat) and the inward application (the 63-85% sub-bass trusted precisely
because involuntary). Counter-reading kept and not dismissed: the corpus's own
Schopenhauer Principle explicitly denies snobbery in favour of cognitive
incompatibility. Vocabulary density: normie 68, taste 68, gatekeeping 12,
snob 6.

chaos-preference.md (concept) — a named tier of the architecture, not a quirk:
FULL PROFILE 2026 carries section 2.5 "Chaotic Neutral: The Philosophical
Alignment" with 2.5.1 Rejection of Law and 2.5.2 Embrace of Chaos. Read
together these make an ontological claim rather than a taste for excitement:
order is a story imposed on reality, entropy is reality with the story
removed, so wanting chaos is wanting access. Explains resolution-as-
disappointment. The micro/workplace case runs on the documented burst-and-
collapse rhythm — a crisis is the only condition under which his native rhythm
becomes the correct rhythm. Key asymmetry recorded: resists external structure
while maintaining obsessive internal ones, so the preference is anti-imposed-
order, not anti-order. Density: chaos 98, entropy 57, chaotic 47.

the-unbroken-bond.md (synthesis) — ~17 years of continuous single-bond
occupancy (Alexis ~Nov 2009-Nov 2015, Annie Nov 2015-present), the most stable
fact in the record, more stable than address, employment, income, substance
regime, politics, alias or social circle. Mechanism is already in the wiki and
is merely assembled here: the sx-dominant stack organises life around one
relationship at maximum voltage, which predicts singular-and-continuous rather
than serial-with-gaps. Separates two variables the corpus had been conflating —
slot OCCUPANCY vs attachment-system ACTIVATION — which resolves how a six-year
bond can be simultaneously long and shallow. Costs section carries the hardest
evidence: the June 1 2026 severance held 52 days and failed, 624 messages in
four days after recontact.

The three interlock: cool rejects inherited taste, chaos rejects inherited
order, and the pair-bond is the one structure that is both chosen and
permanent — which is why it is exempt from the entropy appetite. Everything
else can burn because he did not pick it.

Loops closed: instantiates edges from bond-switch-2015 and
interests-as-era-markers; prose wikilink added to bond-switch-2015; the three
pages cross-link each other. No orphans. Every page names falsifiers and gaps,
including the biggest one — the 2007-2009 window is undocumented, so the
defensible span is seventeen years from 2009 rather than from graduation.

bin/wiki-lint: 0 errors (3 advisory size warnings). bin/wiki-connect check:
0 errors. bin/wiki-climb check: 325 pages, 16 with synthesizes:, 0 errors.

## [2026-08-01] climb | mind | fayette-return.md — new T2 junction
Climbed synthesis-queue cluster #23 (score 12.20, people+mind+self: the four
paternal-line pages, self/ancestry, ancestral-dialectic). Targets the domain
the climb audit flagged hardest — people carries 143 ground pages and almost
nothing above them.

The rule: no member of the paternal Frank line from G2 onward has both left
Fayette County and ended elsewhere. Four generations, ~130 years, three towns
inside twenty miles. The corpus already held this in pieces — the ancestry
note's "elastic tether", and an edge on morley-frank calling the Seattle-and-
back arc "the geographic template Dan's own returns repeat" — but it existed
only as scattered edge claims. A rule is a different object from an
observation: it can be broken, and three falsifiers are stated.

Two things the page does that the loose observation could not. First it
handles G3: Rick has no attested departure at all, which forces the rule into
its better-supported form — not "departure implies return" (which he satisfies
vacuously) but "the terminus is always Fayette", which includes him directly.
Second it reframes Dan's own returns, which the timeline files individually as
collapses and retreats, as the fourth iteration of a pattern with a 100%
completion rate; two of his life periods are literally named for coming back.

Raises a parsimony problem for ancestral-dialectic and records it on both
pages rather than letting them disagree silently: the return is fully
documented within the paternal line alone, whose immigrant ancestors are both
the Ashkenazi side, so a two-line dialectic is not required to explain it. Per
instrument-is-subject the distinction is the operative one — the dates, places
and termini are residue; the psychogenealogical mechanism is testimony.

Also makes a scoreable prediction: if the rule holds, the current tenancy at
337 Saratoga is not the end state. Four gaps named, the largest being that the
maternal line is unassessed and may make the pull regional rather than lineal,
and that no regional base rate has been computed — Fayette out-migration was
heavy, so a family that stays may be typical rather than distinctive.

bin/wiki-lint: 0 errors, no orphan. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 326 pages, 17 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-01] climb | mind | single-channel.md — new T3 doctrine
Climbed synthesis-queue cluster #25 (gripnotic, contact-gini, totality-themes).
The rule: wherever a distributed architecture is available, load is
concentrated on one channel at maximum voltage instead — and it reproduces in
four domains that share no circumstances. Relational (contact Gini 0.961 across
~496 contacts; one bond, ~17 years). Creative (four aliases in thirteen years,
strictly sequential, never parallel). Cognitive (one LLM as externalized
prefrontal cortex rather than one tool among several). Evaluative (one
performed-vs-authentic axis for every category, where most people run
domain-specific criteria). Each was derived on its own page without reference
to the others, which is why four independent derivations of one shape is the
finding rather than a coincidence.

The consequence that earns the page: a single-channel architecture has no
failover. A distributed network degrades when a node fails; this stops. The
record contains the test — the June 1 2026 severance had nowhere to route the
load because by construction the alternatives had never been built, which
reframes the 52-day failure from "the bond was unusually strong" to "there was
nowhere else for the traffic to go". The same untested exposure sits in the
other three domains.

Resolves the apparent conflict with chaos-preference rather than ignoring it:
concentration and entropy-appetite are one policy stated twice — maximum
investment in the chosen, maximum indifference to the imposed.

Names the highest-value next operation in the repository: the 0.961 figure is
QUOTED from a profile document, not recomputed. MASTER_MESSAGES_DB_DUMP.csv is
on disk; recomputing the coefficient per year would convert the central
measurement from testimony to residue and show whether the concentration is
stable or an artifact of one era. Also names the unanswered base-rate problem
(a small county and a decade-long relationship would concentrate anyone) and
flags that the evaluative leg was authored the same day, so a four-legged rule
should be treated as resting on three and a half.

bin/wiki-lint: 0 errors, no orphan. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 327 pages, 18 with synthesizes:.

## [2026-08-01] measure | mind | contact-gini + single-channel — the 0.961 recomputed
Executed the operation single-channel.md named as the repository's highest
value: the contact Gini had been QUOTED from a profile document since it was
first written and never recomputed. Recomputed directly from
raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv — 184,359 rows, 105,405 with a
contact handle.

RESULT: 0.9601 across 496 unique handles. The quoted 0.961 survives to three
decimals and the handle count matches exactly. The load-bearing measurement of
the concentration architecture has moved from testimony to residue.

But the per-year computation falsified a clause nobody had stated explicitly:
that the concentration is a fixed disposition. It is not. Per year it ranges
0.746 (2023) to 0.9576 (2025), with top-1 share from 25.4% (2020) to 84.4%
(2017). Lifetime top-5 share is 70.1% — five handles carry seven-tenths of the
archive.

The sharpest finding is the 2025 row. The year the primary channel was failing
is simultaneously the HIGHEST-concentration year (0.9576) and the
HIGHEST-volume year (33,214 messages) in the entire archive. The response to a
channel under stress was not to distribute away from it but to push more
through it — which turns "no failover" from an inference into a mechanism
stated in the data: a system with no failover does not reroute under load, it
escalates into the failing path.

single-channel.md revised per STRATEGY.md: the falsified narrow form of the
rule is struck through and left visible rather than deleted, the rule is
widened to a dynamic claim, falsifier 2 is marked SETTLED with its result, and
the mechanism paragraph is added to the failover section.

Two new gaps, both material. 69,953 rows — 38% of the archive — carry a blank
contact_handle and were excluded; if those nulls are not randomly distributed
every coefficient moves, and establishing what they are is now the highest-value
next operation. And coverage before 2015 is too thin to compute (2015 itself
shows only 11 handles, which is a statement about export coverage and not about
a social world), so the dynamic claim rests on 2016-2026 only.

bin/wiki-lint: 0 errors. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 327 pages, 18 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-01] measure | mind | the null-handle problem resolved — the coefficient is one-sided
Characterised the 69,953 unattributed rows flagged in the previous entry. They
are NOT randomly distributed: 69,869 of them — 99.88% — are Sent. The export
drops the recipient on outbound messages. Inbound is 99.9% attributed; outbound
is 78.5% unattributed. Blank rate sits near 50% every year through 2024, then
falls to 20% in 2025 and 0% in 2026, which is a change in export method rather
than in behaviour.

Consequence: 0.9601 is an INBOUND coefficient. It measures the concentration of
who contacts Dan, not the concentration of the whole relational load. The
headline is restated rather than withdrawn, because the finding survives on the
best-attributed data — 2025 is 80% attributed and still returns 0.9576 — so the
concentration is not an artifact of the missing side, it is merely measured on
one side. What remains genuinely unknown is whether he SENDS as concentratedly
as he receives; a narrow inbound funnel with a wide outbound spread is a
coherent alternative the data cannot currently exclude.

single-channel.md narrowed accordingly: the relational leg now reads as
received concentration, with outbound listed as unmeasured.

Next operation, and it is tractable: recipients are likely recoverable by
pairing each Sent row to the surrounding conversation window in the same
export. That would produce the first true two-sided coefficient and settle
whether the architecture is symmetric.

bin/wiki-lint: 0 errors. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 327 pages, 18 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-01] measure | mind | two-sided contact Gini — the architecture is symmetric
Recovered the missing outbound recipients and settled the question the last two
passes opened. Each `Sent` row was paired to the nearest attributed `Received`
rows on either side of it in the same export; only attributed `Received` rows
were used as context, and the 19,119 `Sent` rows that DO carry a handle were
held out entirely, so validation and deployment ran under identical conditions.

VALIDATION: bracket rule (both neighbours inside the window agree) at 30 minutes
scores 67.4% coverage at 96.6% accuracy; nearest-neighbour at 1 hour scores 96.7%
coverage at 88.0%. Control: always guessing that year's busiest handle scores
57.2%, so the method beats the concentration baseline by 39 points and is not
riding on it. The held-out rows are 2025-26 only — the sole years the export
attributes outbound — so a leave-one-out run against attributed `Received` rows
was added to reach the earlier years: 93.1%-99.4% accuracy in every year from
2015 to 2026.

BIAS CHECK, and it changed which numbers may be quoted: on held-out rows,
Gini(imputed) exceeds Gini(true) by +0.0225 (bracket) and +0.0996 (nearest).
Misassignment invents recipients and lengthens the tail, so imputation inflates
concentration and every imputed figure is an UPPER bound. The high-coverage rule
is the worse instrument despite looking better on coverage.

RESULT. Two-sided Gini 0.9591-0.9636 across three operating points that place
between 77% and 99.9% of the outbound side — insensitive to how much gets filled
in. Inbound alone is 0.9544 over 495 handles; the previously published 0.9601
over 496 reproduces exactly as the coefficient over all attributed rows
regardless of direction.

The conclusion does not rest on the imputation. Two independent legs carry it.
2026 is 99.8% attributed outbound and 99.9% inbound — a fully measured two-sided
year: 5,838 sent to TEN handles against 4,046 received from EIGHTEEN, outbound
Gini 0.8119 against inbound 0.8748. And stripping the tail: above a floor of 25
messages the two distributions agree to four decimals (0.8586 vs 0.8586).

So the narrow-inbound-funnel / wide-outbound-spread alternative is FALSIFIED.
Outbound Gini reads marginally below inbound only because inbound carries a
one-off tail that outbound has no counterpart to: 495 handles have written to
Dan, 303 ever got anything back, and the 193 that never drew a reply account for
486 messages — 0.56% of inbound, median one message each. The correct statement
is stronger than symmetric: the funnel is narrow on both sides and narrower
going out. Concentration is not a posture he is held in; it is one he maintains
in both directions.

contact-gini.md and single-channel.md revised per STRATEGY.md — the falsified
"outbound is unmeasured" clause and the superseded inbound-only narrowing are
struck through and left visible rather than deleted, and single-channel's second
falsifier is marked FALSIFIED with its result. Three new gaps recorded: the
method assumes the `direction` column is honest (a known trap, with the 99.88%
blank/`Sent` correlation as partial internal support), pre-2015 stays
unmeasurable, and everything counts handles rather than people — Annie holds at
least three, so a person-level coefficient would be higher than any figure
published.

bin/wiki-lint: 0 errors. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 327 pages, 18 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-01] climb | mind | dormancy-not-exit (7 synthesized, 0 rejected)
Cluster 5 of synthesis-queue.md (alexis-armel · danielle-onesi · 424-bedford-ave;
people + places). The rule: nothing leaves this graph. Every sustained
relationship the record calls "over" has changed role and gone dormant with full
reactivation bandwidth intact — endings in this corpus are reassignments, never
exits. Members widened past the mined three to include menore, franki-faris,
155-virginia-ave and the-unbroken-bond, all genuinely reasoned from.

Danielle: romantic role ends 2009 by Dan's infidelity, and seventeen years later
she is Suzanne's closest friend, the cat's co-guardian and a Christmas fixture.
Alexis: the case that rules out passivity — paid into the Nov 2018 arrangement
with her own successor, then carried as a warm 88-message correspondence to Feb
2025. 424 Bedford: vacated 2012, still producing through 2025 via the Menore line
it originated, so the rule is not confined to people. Menore is the measurement —
2,044 days of silence answered in one minute, which is dormancy with no decay at
all.

Franki Faris is the control and a sharper one than a plain absence: five days of
occupancy in 2013 left no person in the graph, but left the NAME in circulation
as working vocabulary ("a Franki Faris 2.0 situation"; by 2018 a pet nickname for
Annie). Below the tenure floor the label survives, not the tie. The floor itself
is undetermined — five days is below it, six years above, nothing in between.

What it explains: no-exit plus a single-occupancy primary slot is an accounting
identity that produces concentration. The Gini measured this morning does not
need a claim about temperament to arise. It also fits the two-sided finding
without being fitted to it — 495 handles wrote in, 303 got anything back, and the
193 that drew nothing carry a median of one message each. They are not lapsed
relationships; they never entered. Entry is hard, exit does not exist. And it
reframes the failed 52-day severance: severance is not an operation this system
has.

STALENESS, handled properly rather than bumped. Editing menore.md made
block-unblock-loop and supply-network stale. supply-network survives untouched
(the availability figures are unaffected; a node resuming at full bandwidth after
2,044 days is MORE of a reliability outlier) — re-check noted, date bumped.
block-unblock-loop does not fully survive: it scores Menore's Feb 2025 farewell
as "the record's only fully clean closure," its strongest non-Annie control, and
the same channel had already closed cleanly for the same structural reason in
2013 and reopened 2,044 days later. The 2025 close has stood ~17 months; the
precedent ran 67. That row is now marked provisional on elapsed time, carries a
RE-CHECKED block, and the two pages carry reciprocal `contradicts` edges with a
CONTRADICTION block on the new page. One of them will be wrong in a dated,
recorded way when the next export lands.

Also: added the six synthesis/concept pages missing from wiki/mind/index.md
(the-unbroken-bond, alias-as-periodization, instrument-is-subject, fayette-return,
single-channel, the-cool-metric, chaos-preference) alongside the new page.

Queue row 5 marked CLIMBED. bin/wiki-lint: 328 pages, 0 errors.
bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 328 pages, 19 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-01] docs | meta | propagate the refined STRATEGY.md into every governance file
The operator refined STRATEGY.md (f57e574). Most of the diff is tightening, but
three changes are doctrinal and none of the other spec files carried them:

1. **"Every data point gets an entry."** Coverage is now stated as the standing
   ambition — every story, friend, place, perspective, development, thought.
2. **An entry is a live node, not a record.** Each page carries what was known at
   ingestion AND everything later produced by using it in analysis against the
   rest of the corpus.
3. **The core loop, named:** Story → Entry → Analysis → Synthesized finding →
   **saved back to every entry it touches** → repeat. Step 5 is a new standing
   obligation, and the rationale is **amortized insight** — analysis is expensive,
   so it is done once, saved everywhere relevant, and each future pass starts
   from a higher floor.

Propagated:
- **CLAUDE.md** — coverage rule and the live-node doctrine into the charter; the
  full core loop as its own section mapping each step to the operation that runs
  it; CLIMB step 5 hardened to require write-back on every member.
- **SYNTHESIS_SPEC.md** — new section "The write-back obligation", stated as the
  counterpart to the staleness rule (staleness pushes information down the ladder
  when a premise moves; write-back pushes it back out when a conclusion is
  reached). CLIMB step 5 rewritten. New anti-pattern: **the write-only
  synthesis** — correct, well-argued, and wired to nothing, so the finding cannot
  be reached from below, which is where readers actually arrive.
- **CONNECTIONS_SPEC.md** — new section distinguishing a *retrofit* inverse
  (frontmatter-only is fine) from a *write-back* inverse (must state what the
  page turned out to be evidence OF), with a failing and a passing claim side by
  side. Retrofit step 4 updated to point at the distinction.
- **STYLE_GUIDE.md** — "An entry accumulates" and "Every data point gets an
  entry" as substance rules; the contacts/ quarantine explicitly named as the one
  place coverage is held back, and why; header now states STRATEGY.md wins on
  intent as CLAUDE.md wins on process.
- **INGEST_RUNBOOK.md** — STRATEGY.md added as governance file #0; quality bar
  gains write-back and coverage items.
- **INGEST_PROTOCOL.md** — both rules stated in the quality bar so any LLM
  running the paste-box loop gets them.
- **README.md** — STRATEGY.md added to the file map as the read-first document.

Deliberately NOT changed: the "three unbreakable rules" reference in
LLM_HANDOFF.md line 357 is a dated historical entry that was accurate when
written; the handoff log is append-only history, not a spec.

bin/wiki-lint: 328 pages, 0 errors. bin/wiki-connect check: 0 errors.
bin/wiki-climb check: 328 pages, 19 with synthesizes:, 0 errors, 0 warnings.

## [2026-08-02] write-back | mind | write-back audit across all 19 synthesizes: pages (41 gaps closed, 0 remaining)
## [2026-08-02] climb | interests | food-and-diet — "food in every register except taste"; bounds the cool metric's jurisdiction
## [2026-08-02] ingest | people | sadie-harris, david-j-frank, morley-frank rewritten from the GEDCOM; fayette-return revised (Sadie burial vs death, G1's NYC years, the Hopwood terminus)
## [2026-08-02] climb | mind | the-deferred-audit — provenance sets the audit's clock; the audit lag explains the diagnosis-to-behaviour gap (8 synthesized, doctrine tier)
## [2026-08-02] climb | mind | the-deferred-audit predictions 1-2 scored same-day — P1 partially falsified and narrowed (lag is one-time per object), P2 confirmed pending failure

## [2026-08-02] ingest | multi | factstory batch of 5 manual captures — queue cleared
Five hand-typed captures came in via leviathan/factstory.html and were filed verbatim to raw/ before any synthesis. Two of them (Bald Eagle Cummings, Picky Eater) had previously been committed to root-level stories/ and facts/ directories outside the inbox→raw→wiki flow, so they were filed but never actually ingested; those directories are removed and the content now lives in raw/. What the batch settled: the coal-baron husband on Fran's page is **Thomas Whyel**, her second husband, which closes the gap estate-money-spine named as the maternal line's unresolved origin; Alexis's "I saw your messages. I know you're with Franki" confrontation is located verbatim and dated to ten minutes into the drive; the chaos preference's Boston-manhunt exhibit is attested for the first time; the production identity's origin is dated to summer 2013 and attached to a cause (an idle ishlab DJ controller); and seven-springs' standing gap on named crew members is closed. What it opened: the "five days" figure that dormancy-not-exit uses as its tenure-floor control may have been transposed from Alexis's five-day stay at 155 Virginia Ave — flagged as a contradiction on both pages, not resolved. Also flagged: 155 Virginia was under Suz's control in July 2013, eighteen months before the January 2015 lease that page dates itself from. The picky-eating capture falsified food-and-diet's rule in its strong form and forced a correction to the-deferred-audit's food row — food is not an audit that never fires, it is one that fires preemptively on every plate, on composition rather than on taste. I was unsure about the Joe Croftcheck federal-case citations and did not verify them; that page records the operator's association and explicitly does not assert charges.
## [2026-08-02] fix | people | annie-ulmer — the 24-hour bond-switch was Dan's, not Annie's; corrected in two places and propagated to bond-switch-2015, the-unbroken-bond, dan-annie-fallout-verdict, block-unblock-loop, supply-network
## [2026-08-02] tooling | meta | bin/wiki-digest — generates DIGEST.md, RECENT.md, OPEN.md as human reading aids (state of the wiki, what changed and why, every unresolved contradiction/gap/prediction)

## [2026-08-02] ingest | multi | factstory batch of 4 manual captures — Jay Lauer's death, the Fall of Fran, the vape alarm, the acquisition drive
Four hand-typed captures came in via leviathan/factstory.html and were filed verbatim to raw/ before any synthesis (two Fran stories to raw/self/captures/, the Jay Lauer fact to raw/people/captures/, the perspective note to a new raw/mind/captures/). Six new pages: `wiki/timeline/events/the-fall-of-fran`, `wiki/timeline/events/uniontown-hospital-vape-alarm`, `wiki/mind/concepts/acquisition-drive`, `wiki/people/betherin-mechling`, `wiki/people/diane-shrum`, `wiki/people/fred-adams`.

What it settled. **Jay Lauer's death is dated.** The capture said "early 2017" and asked for research; the message dump fixes it to April 10–11, 2017 across four recipients in one day, with the viewing on April 17 and the funeral April 18 — and supplies the fact that reframes his whole page: Dan had tried to route him onto Suboxone ("it helped me finally get out of that world"), and Jay sold the prescription for heroin. He is the supply network's only documented fatality. **The Ellen Ulmer thread has an origin**: message one of that eight-and-a-half-year relationship is Dan's condolence over Jay, 19:09 on April 11 2017 — the tie that outlasted the Annie relationship was opened by a friend's overdose. **The arrangement's start date moved back eight months**: Dan's own 2018-02-16 message to Danny Matthews, "you guys would be the first couple we were with," makes the March 7–8 2018 encounter the first, not the November 2018 Alexis reunion. **The vigil page's named gap is closed** — the SMOK-vs-10W vape story's missing punchline is a hospital-wide fire alarm, four fire trucks and an escort off the property with charging documents. And following the capture's "Diane" into the GEDCOM **closed two more standing gaps on fran-coldren and corrected the family tree**: Fran's maiden name is Thomas, her first husband was Emmet Graden Van Voorhis, and her only child is Dan's maternal *grandmother* Rebecca Diane Van Voorhis — the wiki had the Whyel/Coldren line descending through the maternal grandfather, who in fact married into it.

What it corrected. The captures date the entire Fran sequence to **March–April 2017**; seven independent records date it to **2018**, including one internal to the story (in March 2017 no contact with Danny Matthews exists in the corpus at all). Recorded as a resolved contradiction with the evidence tabled, plus a labelled inference about why the memory slipped — April 2017 and April 2018 were both caddie-season opening at Nemacolin, and April 2017 carried a real death. Also flagged unresolved: the vigil page and the captures **invert who was in the bathroom** during the vape incident, and only the captures' arrangement produces the documented alarm; and the "T" in Frances T. Coldren is over-determined now that Thomas turns out to be her maiden surname as well as her second husband's given name.

What I was unsure about, and did not do. The vape incident's "charging documents" are Dan's words and nothing corroborates that anything was filed — recorded as unverified rather than as a second citation. Diane's married surname is inferred from a documented marriage, not from a record naming her Shrum. The ATM-card episode has no date, amount or corroboration anywhere and Vanessa's own thread never mentions it. And I did **not** climb: `acquisition-drive` plus the two event pages plus the low-Altruism reading of the Fran vigil is a real cluster and probably a doctrine-tier finding, but the concept page is one day old and CLAUDE.md says to climb after a cluster survives two or more ingests. Registered as cluster 26 in synthesis-queue.md instead.

## [2026-08-02] fix | meta | wiki-brain went private — sync restored, dead Pages URLs repointed at the leviathan mirror
Making `caakehorn/wiki-brain` private broke two things silently. **The hourly sync into `caakehorn/leviathan` has been failing since 09:21 UTC** (last good run 06:45): `.github/workflows/sync-wiki.yml` there checks out this repo with `actions/checkout@v4` and no token, so it used leviathan's `GITHUB_TOKEN`, which is scoped to leviathan and gets a bare `Not Found` from a private third-party repo. Consequence worth noting: the brief-#4 ingest (PR #79) never reached leviathan, so its published wiki data is pinned at `e7e1e53` until a credential is in place. Fixed on the leviathan side — the workflow now takes `secrets.WIKI_BRAIN_TOKEN` (fine-grained PAT, `caakehorn/wiki-brain`, Contents: Read-only) with `persist-credentials: false`, and fails fast with a readable error when the secret is absent instead of emitting a 404 that looks like a deleted repo. **The secret itself still has to be created by hand; the sync stays red until then.**

Second, **this repo's GitHub Pages feed is gone** — `llms.txt`, `agent/manifest.json`, `agent/critical.md`, `agent/corpus.md`, `agent/domains/*`, `wiki/*.md` and `llm/index.txt` all 404, and `deploy-site.yml` has been failing on every push since (the PR #79 merge included). Pages does not serve private repos on this plan. Nothing about the generated artifacts changed, so they go live again if the repo is ever made public; `bin/llm-publish` is still worth running. In the meantime every doc that advertised those URLs now points at the public mirror instead — `https://caakehorn.github.io/leviathan/data/wiki-data.json`, which carries `wikiPages.pages[]`, full prose under `wikiText`, and `wikiLog.ops[]`. Updated: `AGENT_ACCESS.md` (status banner), `README.md`, `CLAUDE.md`, `INGEST_RUNBOOK.md`, `FACTSTORY_BRIEF_TEMPLATE.md` §1 — the last of which mattered most, since it had been shipping seven dead URLs to every model handed a capture brief since this morning.

Recorded and deliberately not acted on: `data/wiki-data.json` in the public leviathan repo contains the complete body prose of all 425 pages, so this repo going private did not make the wiki's contents private. Operator confirmed on 2026-08-02 that this is intended and the exposure should stay as-is.

## [2026-08-02] fix | interests | stray empty frontmatter fences on fall-out-boy and taking-back-sunday
Caught by leviathan's `validate` job, which is the first time that gate has paid for itself: `error: 2 pages still carry frontmatter`. Both pages closed their real frontmatter and then carried a second, empty `---\n\n---` fence before the H1 — probably left by an automated edit some passes ago. `bin/wiki-lint` never saw it because the frontmatter parser matches only the first block and the rest is legal markdown. The downstream effect was real though: `tools/build-wiki-data.py` strips one fence, so the mirror was publishing two pages whose body text began with raw delimiters, and leviathan's EPISTEME/ECHO metrics were measuring those as prose. Removed from both; a repo-wide scan confirms no others.

## [2026-08-02] mine | mind | message-density campaign opened — bin/mine-messages, calibrated-confidence, and a negative on the four axioms
Operator directive: scrape the full message logs for new nodes and data points, cross-reference against standing wiki claims, and raise density in `mind/` and `self/` toward conclusions of the "time = countdown" kind. This is the first pass; `MESSAGE_MINING.md` is the campaign spine and carries the backlog.

Built `bin/mine-messages` (pure stdlib: `stats`, `grep`, `battery`, `timeline`, `entities`) because three properties of the dump make plain grep silently wrong, and each of them produced a false measurement during development: messages span multiple lines, **curly apostrophes outnumber straight ones 28,904 to 19,978** in Dan's sent text so any pattern written `i'm` misses most of its matches, and direction is trustworthy only in `all_imessages_complete_dump.txt` (106,629 Sent / 110,944 Received) and not in the master CSV. Corpus covers 2015–2025; **2022 and 2026 are absent entirely**, so nothing here touches the terminal phase.

**The methodological result, which governs everything after it:** the corpus contains its own control, and it is not optional. Raw counts made Dan look extraordinarily un-introspective — "the thing about me" appears zero times in 106,629 outbound messages. Against the 110,944 inbound messages it evaporates: zero there too. SMS is a near-zero-introspection medium for everyone in it. Every rate in this campaign is now reported as a ratio against the inbound baseline.

**Confirmed finding — `wiki/mind/concepts/calibrated-confidence.md`.** Dan attaches graded numeric probability to his own beliefs in casual text: 43 instances, 15 of them at values that are not 0/50/100 (75, 80, 89, 90, 95, 99.9999). Inbound: 2 instances, both plain "100%" as a synonym for *definitely*, and zero graded values. Survives all three controls — spread across 12 handles so it is not one relationship, present in every year 2015–2025 so it predates the AI era by eight years, and bare-percentage usage runs at only 1.36× so it is not general numeracy. This is the first behavioural evidence for Ti-dominance in the whole wiki that comes from neither an instrument nor an AI session; 89% is the tell, because nobody reaches for 89% as an intensifier.

**Negative result, written back to `wiki/self/context-core.md`.** The four core axioms are not corroborable from messages, and *time = countdown* is the clearest case: Dan uses explicit urgency language *less* than his correspondents ("running out of time" 0.35×, deadline language 0.42×, "before I die/turn/lose" 0.00×). "Rest of my life" looked like 3.5× support until the twenty hits were read — all are 2015–16 love-declarations to Annie. This is not a falsification (nobody types their unconscious axioms) but it bounds the corpus: the spine claims all behavioural data defers to the message corpus, and for the psychological layer the corpus is silent, leaving the axioms resting on AI-session dossiers alone.

**A false positive is recorded on purpose, on both `context-core` and in the campaign doc.** The first run scored "age self-reference" at 3.82× and nearly became a finding about the countdown being experienced as position rather than urgency. The pattern was catching "I'm 99% sure" — percentages wearing an age pattern's clothes. Corrected, real age self-reference is n=8 across eleven years, half of it escort-ad boilerplate. The rule now written into the campaign doc: read your matches before believing your counts.

Not done: the entity miner drowns in bank alerts and brand names and needs a spam filter, though it did surface six unpaged candidates (Lucy, Ricky, Libby, Alice, Derrick, Michelle) now in the backlog. "supposed to be" at 2.17× with n=123 is the best-powered unexplained divergence in the battery and was left unread. And lexical passes have probably hit diminishing returns — the next real finding is likely behavioural, in the shape of `message-circadian-latency`.

## [2026-08-02] rewrite | people | fran-coldren rebuilt from scratch against the message corpus
Operator directive: reanalyse and reassemble the entry into a much more robust one, cross-referencing every uncorroborated or unclear item against the message corpora. Searched 476 "gram" and 248 "fran" references in `all_imessages_complete_dump.txt` using `bin/mine-messages`.

**Settled from dated contemporaneous messages rather than memory:** her **age at death is 97** (Dan, 2017-12-29: "a 97 year old woman with advanced dimentia"), which closes a three-way contradiction between the core documents' 98, the 1920 birth year's 97, and a capture's "93-year-old matriarch". The caregiving arrangement is now quantified — **$15/hour**, and **six months full time**, not the "~2015–2018 paid 24/7" the wiki had inferred ("i spent the past 6 months looking after her full time ($15 an hour to play video games with gram is a good deal)", 2018-04-06); the correction was propagated to `fran-death-vigil`, `117-belmont-circle`, `155-virginia-ave` and `acquisition-drive`. **Fred Adams authorised the pay** ("fred would have put the kaibosh on me being paid to watch gram"), putting the trustee in the payroll chain. The terminal sequence is now dated rather than inferred: **she survived surgery** by March 9, went to the nursing home on or about **Monday March 12**, was placed on **hospice ~April 1–2**, and staff **stopped feeding her** — the wiki had recorded only the water shutdown.

**The find that changes a standing conclusion: Dan retracted the death-moment story himself, within 24 hours, and the wiki never knew.** The mystical version — the silent attempt to communicate, Fran blinking for the first time in a week, the smile, the death — is quoted across several pages as the emotional peak of the record. At 23:26 on 2018-04-05, roughly three hours after telling it, he messaged his sister: "upon further review of the video, it looks like a monitor went off alerting us that her pulse was dropping. neither of us remembered it but the video helps correct the timeline. def isn't as 'supernatural' knowing that fact. but doesn't take away from the cool moment we had with gram." He went to the primary source, found the mundane cue, and corrected himself unprompted at no benefit to himself. Written back to `forensic-method` as the method's hardest and most self-directed test on record. Both halves are kept — his own final clause refuses the deletion and so does the page.

**Also recovered:** a November 2017 message showing the institutionalisation threat was understood as an active family campaign five months before Diane's letters ("people directly connected to my grandparents who are looking for any excuse to throw her in a nursing home"); and the inheritance thread running concurrent with the grief — planning in January 2018 while she was alive, "inheritance will help with the mourning proce$$" sent the day she died, "ya boy is getting out of PA" two days later, and a first cheque on 2018-04-27 that is distinct from the 2020 court distribution and remains unquantified. The page keeps both registers rather than choosing.

**A process note against myself.** Rebuilding from scratch dropped seven inverse edges that other pages were pointing at, and silently deleted the standing `ancestral-dialectic` CONTRADICTION block. `bin/wiki-connect check` caught the edges; the contradiction I only noticed on re-read. This is exactly the failure mode CLAUDE.md's "revise, never regenerate" exists to prevent, demonstrated on the page most likely to be rewritten. All restored; gates at 0 errors. If a future pass is told to rewrite a page from scratch, diff the old connections block against the new one before committing.

## [2026-08-08] rewrite | people, places | full re-research and rewrite of four entries (jacob-bacharach, 117-belmont-circle, zach-harshman→zach-clingan, alexis-armel)
Operator directive: complete wipe and full re-research of four named articles, retaining nothing of the originals including heading structure, with all links, connections and sub-categories rebuilt afterwards. Every claim was re-derived from `raw/` rather than carried over.

**The Zach page was about the wrong person, and the corpus proves it two ways.** `zach-harshman.md` was built entirely on handle `+18439903264`. Google Contacts attaches that number to **Zach Clingan** (alongside +1413…0339 and +1724…0771); the Facebook address book independently attaches the same 413 number to Clingan and gives Harshman an entirely disjoint set (+1412…3533, +1617…4273), while Google Contacts gives Harshman (724) 322-1572 and SMASHED763@GMAIL.COM. Neither of Harshman's numbers appears in the iMessage dump at all, and the real Zachariah Harshman already had a full page. The old page's own Gaps section had flagged the surname as unconfirmed and was right to. Renamed to `wiki/people/zach-clingan.md`; three further stated facts were also wrong — 22 messages is actually **41**, "all received (export artifact)" is actually **two-sided**, and the "six-month window" is **one caddie season's tail plus the first ping of the next** (looping, getting cut, a two-bag round offered away, an 11 report, the Oct 31 party flyer, then "have you started looping yet??" on 2018-04-13, twelve days into the next season and nine days after Fran died). The supply direction also inverts against every other node on `supply-network`: here Dan holds the inventory. Two new registers recovered from outside the message corpus — a 2009 Facebook line to Stephanie Nalbone ("trying to not imagine zach clingan as the creepy faun. they both lie about shit") and Tom's April 2014 taxonomy ("steve kezmarsky and zach clingan are 'drug people' and they're assholes" / "we're assholes and drug people, but not shitty people").

**The Bacharach chain is now dated to the hour, and three of the story's load-bearing facts were wrong.** Every prior account dated the discovery to "~2022." The iMessage record fixes it: **2021-02-06 13:39** Dan to Suz, "I was listening to a podcast and Jake Bacharach was the guest lol"; **2021-02-11 22:01** Dan forwards Bacharach's entire reply to Suz, which is the only sample of the man's own voice in the corpus and confirms the teenage commercial job unprompted; **2021-02-12 06:44** the retelling to Tom, which is also where Nate Bacharach's overdose enters ("He OD'd" / Tom: "everyone did"). Corrections: (1) *The Bend of the World* was published **2014** and Dan's tenancy at 155 Virginia begins **January 2015** — he moved into the setting after the book existed, which kills the "he wrote it while you lived there" framing every retelling carries; (2) Goodreads and `FAVS MASTERLIST.csv` each hold **exactly one** Bacharach title, *The Doorposts of Your House and on Your Gates* (Liveright **2017**, ★★★★★, shelved 2022-03-24) — the claim on this page and on `books.md` that Dan read and five-starred both novels is false, and the book he demonstrably read is the one Bacharach himself named as the Uniontown novel, which opens a real contradiction about which book the coincidence is even in; (3) YouTube's only two Bacharach items sit two minutes apart at 01:13 on **2022-11-10**, the signature of a search, not the autoplay the story is built on. The page is now organised around the correction record rather than the coincidence.

**117 Belmont Circle gained fifty-seven documented years and an eight-month afterlife.** The GEDCOM fixes a floor no pass had used: Fran is in **Miami Beach 1957–58**, her daughter **Rebecca Diane Van Voorhis married George Dixon Shrum Jr. in the house on 1961-02-08** (*Pittsburgh Post-Gazette*, 1961-09-03), and their daughter is Suz. The family's arrival at the address is a **return from Florida**, landing within two years of Morley Frank's Seattle→Uniontown return on the other side of the tree. And the message corpus shows the house was Dan's own operating address across **five documented occasions from 2018-02-16 to 2018-09-05, four of them after Fran was dead**: the arrangement's venue pitched to Danny Matthews three weeks in advance as "a great place for hangs" (identified, like Bacharach's house next door, by "beside 5 fairway"), a 1:52 AM invitation eight days after the funeral ("we are still at my grandmas. my mom fell asleep"), a caddie put up to save a hotel bill, a golf meet-up, and a September pharmaceutical handoff to Bill. That supplies the missing option behind the unresolved 2018-03-29 eviction notice at 155 Virginia — he had somewhere else to be, one lot away.

**Alexis Armel: 495 unread Google Chat blocks, and the moral-yardstick inversion.** `gmail_bodies.txt` — flagged as unmined since 2026-07-19 — holds **495 conversation blocks** under `lexieamb@gmail.com`, dated samples spanning 2011-08 to 2013-05. It is the only daily record of the relationship written while it was working, and everything else on the page was written afterwards by one participant while arguing about a different relationship. It settles three things: **WEXUS**, the password on the 2025 wrong-number coda, is an ordinary household word from the 2011 apartment ("did wexus pay it twice last month?"); the Suboxone era is visible as shared domestic logistics, not a secret ("hey can you see if i forgot my piece of subby"); and Alexis is an atheist on her own account who argues politics back. The register — sustained baby-talk across years — runs concurrent with the Twitter corpus's weaponised irony, from the same person, to different audiences. Also newly stated: **Annie was Alexis's coworker** (context-core), so the November 2015 replacement was internal; and on **2020-09-19**, mid-argument, Dan makes Alexis the moral yardstick Annie is measured against and found short ("my mom thinks alexis is 'the devil' even though she never really did anything shitty to me....you, on the other hand..."). The old page's Gemini-sourced "high-volatility interpersonal dynamics" characterisation is not supported by the archive and is retired on the page.

**Staleness handled, not bumped.** The Alexis rewrite made `dormancy-not-exit` and `the-unbroken-bond` stale, and re-checking those made `single-channel` and `the-deferred-audit` stale. All four re-read and answered with RE-CHECKED blocks. Two produced findings: dormancy-not-exit gains a boundary (Alexis had not kept Dan's number in 2025 — the retention is **asymmetric**, and the counterparties have never been asked), and the-unbroken-bond has two of its own named gaps moved, with the chat archive supplying the first primary-source pressure on its "suppressed deep system" reading. Gates: wiki-lint **438 pages / 0 errors** (113 warnings) · wiki-connect check **0 errors** (208 warnings) · wiki-climb check **0 errors, 0 warnings**.

## [2026-08-08] govern | root | governance rewrite — six specs, one backlog, six documents retired
Operator directive: clean up, streamline, optimize and rewrite the governing/protocol markdown at the repo root, taking direction from the most recent STRATEGY.md; push entry length and depth further; and emphasise that the raw sources are still not being mined deeply enough — all without redundant or obsolete instructions.

**The diagnosis.** 25 root markdown files, of which six were dead or executed and three carried instructions that actively contradicted current doctrine. The sharpest contradiction was internal to STRATEGY.md: its "Running on lesser models" section told a model to clear a staleness warning by adding a line and **bumping the date**, four paragraphs after rule 4 called bumping the date the one prohibited move in the system. That section also rested on a premise that stopped being true — "the most capable model that will ever work on this repository finished on 2026-07-18" — while Opus 5 sessions were doing the deepest passes in the repo's history. Retired entire.

**New: `EXTRACTION_SPEC.md`** — the depth doctrine, and the answer to the directive's substance. Its argument is that depth of mining and length of entries are not two preferences but one mechanical requirement: *a pattern can only be found among details that were written down, and synthesis reasons from `wiki/` rather than `raw/`, so every detail dropped at extraction is a connection nobody can ever make.* That reframes "every trivial detail gets an entry" from hoarding into surface area for the next climb. Contains the exhaustion standard (a source is read when a second careful pass would find nothing material), the seven moves (sweep wide before reading narrow · read whole records not matching lines · chase every proper noun outward · re-derive every number · compute the inbound baseline or don't state the rate · check what is absent · keep the mundane), the primary-vs-AI-secondary source tiers with the laundering failure named, and the per-source traps that fail *silently* — absorbing MESSAGE_MINING.md's three dump traps and the identity-resolution and GEDCOM/Goodreads/activity-export recipes.

**New: `BACKLOG.md`** — one live work list replacing four dead trackers. Verified rather than inherited: `task.md`'s remaining Phase-3 targets were checked and **four of seven were page names that never existed**; LONG_TAIL_TRIAGE.md's six "MINE" items were all **executed on 2026-07-19** and are now recorded as settled rather than pending. What survives is real — the Gchat archive campaign, the five unpaged entity-miner candidates, the named open questions, and a "do not re-litigate" section.

**Rewritten:** `STRATEGY.md` (governing-set table; depth promoted to a first-class section as the binding constraint; four unbreakable rules → **five**, the new one being "never stop at what you came for"; campaign restated as depth/height/breadth). `STYLE_GUIDE.md` (split into Substance and Format; substance rule 1 is now *write long* with the mechanical argument attached; contacts/ quarantine doctrine removed; exemplar table added). `CLAUDE.md` (335 → ~150 lines, cut to a process router since it auto-loads into every session; REWRITE added as a named operation pointing at the `wiki-rewrite` skill). `README.md`, `index.md` (every domain count was stale; recomputed from disk), `INGEST_RUNBOOK.md` §2 and §7–9, `INGEST_PROTOCOL.md`, `FACTSTORY_BRIEF_TEMPLATE.md`, and the two spec headers.

**A gate was fighting the directive.** `bin/wiki-lint`'s page budget was 8 KB and fired on **104 of 113 warnings — 92% noise**, on a project whose standing instruction is longer entries. Raised to 40 KB and reworded from "consider splitting" to "split ONLY if navigation genuinely improves, never to shorten." Warnings 113 → 13, and the remainder are now real (orphans, one genuinely oversized page).

**Retired (history in git):** `task.md`, `lint-report.md` (a frozen 2026-07-11 snapshot at 268 pages, regenerable), `contact-review.md` and `LONG_TAIL_TRIAGE.md` (both worksheets for the `wiki/people/contacts/` quarantine, deliberately eliminated in `65f80c2` — which also closes the 2026-08-08 handoff's resume point #2, since the governance text describing it was the thing still wrong), `TO-DO-LIST.md` (operator's hand list, carried forward into BACKLOG.md), `MESSAGE_MINING.md` (method into EXTRACTION_SPEC, findings and backlog into BACKLOG). Every inbound reference swept, including `app.py`'s editable-meta lists and the `wiki-rewrite` skill.

**Gates:** wiki-lint **438 pages / 0 errors**, 13 warnings (from 113) · wiki-connect check **0 errors** · wiki-climb check **0 errors, 0 warnings**. Root markdown 25 → 21.

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
- `wiki/people/tan-calabrese.md` — Identity reconciliation: infobox name updated to "Tancredi Calabrese (Tan Calabrese)"; sources added; new `co-occurs` connection to `wiki/people/tancredi-calabrese` explicitly distinguishing the contact from the childhood friend.
- `wiki/places/seven-springs.md` — Source list expanded; new `co-occurs` edge to `wiki/people/tom-wallisch`; date_modified bumped.
- `wiki/people/index.md` — Four new entries added.
- `wiki/interests/index.md` — Extreme-sports entry added.

**Age/date cross-check:** No self-reported ages or dates in the capture require CONTEXT_CORE cross-checking — the capture narrates adolescent events from 2000–2006 without using specific age claims that need verification.

**Entity name reconciliation:** Tan Calabrese → Tancredi Calabrese split handled via the identity correction protocol: contact page updated with dual name, childhood-friend page created under full name, co-occurs edge explicitly names the distinction.

**Write-back inverses:** All inverse edges added on target pages (tan-calabrese → tancredi-calabrese; seven-springs → tom-wallisch).

**Gates:** wiki-lint 0 errors · wiki-connect check 0 errors · wiki-climb check 0 errors, 0 stale.

**Raw file:** `raw/self/captures/2026-08-09_122727_extreme-sports.md` (md5: d73cbb65ec7cdb19b5b1dbc870897ac6).

## [2026-08-09] ingest | people, timeline, mind | canonical Jerel Coles page + August 8–9 unmasking night + read-receipt forensics (external content pack incorporated)
Operator uploaded a content pack (five files: a patch set, an event page, a synthesis page, a raw capture, and a person page) produced by a prior session with direct access to the operator's local `chat.db` and iMessage export. Incorporated per `INGEST_PROTOCOL.md`'s any-LLM paste-box model, not run as a fresh `raw/`→`wiki/` pass, since the analysis arrived pre-written.

**The pack overclaimed one identity merge, and it was corrected before commit rather than propagated.** Its own new page asserted "this page [the-unnamed-man] and the Tuquick page were always about one person," but the only exact identifier match in the underlying capture (FOREWARN phone number) closes **Tuquick = Jerel Wayne Coles** — it does not touch whether Tuquick is *also* the separate, unnamed July 2026 antagonist Annie says raped her. The capture's own frontmatter (`target: wiki/people/tuquick`) confirms the lookup targeted the Tuquick handle specifically. Rewritten across all three touched person pages to keep that link explicitly open (role + insult-lexicon overlap only, no independent identifier), consistent with the wiki's own pre-existing, more careful framing on `tuquick-17248123683.md` and `the-unnamed-man.md`. This matters because the page pairs a real person's home address and phone numbers with an unadjudicated rape allegation — attaching the allegation on lexicon overlap alone would be exactly the unearned merge `STYLE_GUIDE.md`'s contradiction discipline exists to prevent.

**New canonical entity page `wiki/people/jerel-coles.md`.** Supersedes `tuquick-17248123683.md` outright (exact match) and cross-references `the-unnamed-man.md` as an open question. Carries the fuller identity record (both phone numbers, address history including a previously-undocumented 22-month dual-address overlap), the de-duplicated criminal-history table (64 raw FOREWARN records → 9 incident clusters, 2008–2025), and an explicit publish-state flag: this repository's Pages deployment has been public since 2026-08-08, no redaction gate exists in `bin/build-site`, and the operator should decide whether this class of content needs one — noted here and in `LLM_HANDOFF.md` rather than resolved unilaterally.

**New event page `wiki/timeline/events/august-2026-unmasking.md`.** The thirteen-day refusal-to-know finding on `the-unnamed-man.md` terminates at 19:01:22 on 2026-08-08 with the FOREWARN lookup; the following ten hours (misparsed "He'll?" read as an invocation of the identified man, a contested sleep claim, read-receipt coverage ending at 02:24:54) are tabled from a `chat.db` extract. Two analytic misreads from an earlier pass of this material are recorded and retracted on the page itself, per the corpus's standing retraction discipline, rather than silently corrected.

**New synthesis page `wiki/mind/synthesis/read-receipt-forensics.md`.** Four chat.db metadata defects surfaced in one extraction session, three of which returned a confident wrong answer with no error raised: `date_read` is directional (asymmetric by `is_from_me`, not a single undifferentiated signal); `reply_to_guid` is auto-populated with the previous message, not a true reply marker (`thread_originator_guid` is); a SQLite type-affinity trap silently zeroes a `strftime`-vs-computed-expression comparison; and missing `delivered_at` clusters by device-sync artifact rather than randomly. Wired into `mind/concepts/forensic-method.md` as an instrument-integrity finding — the method's real exposure is to instruments that lie quietly in the direction of whatever is already suspected, not to hard failures.

**Sourcing gap, not silently closed.** `annie_metadata_24h.csv` and `imessage_export_2124702449_20260809084846_.csv` are the primary sources for the new event and synthesis pages but were never filed to `raw/` — the pack contained only the derived analysis, extracted directly from the operator's machine. Flagged on both new pages' Gaps sections, in `BACKLOG.md` §3, and in `queue.md`'s highest-value-pending table, rather than treated as archived.

**Staleness cascade worked, not bumped.** The identity/chronology additions to `annie-ulmer.md`, `suzanne-frank.md`, `forensic-method.md` and `dan-annie-fallout-verdict.md` triggered `bin/wiki-climb check` on eight downstream synthesis pages. Each premise was re-read against its dependent's actual claims: six were genuinely orthogonal (identity/chronology additions don't touch love-language rates, exit counts, financial figures, or continuity claims) and closed with a RE-CHECKED block; one (`the-deferred-audit.md`) got a substantive check against a real candidate counter-instance — whether the interloper-identification refusal contradicts its imposed-object/preemptive-audit rule — and was found to be a different mechanism (provenance-of-a-claim vs. cost-of-further-knowledge) rather than a counterexample, recorded as reasoned-through rather than dismissed. Two further pages (`dormancy-not-exit.md`, `single-channel.md`) went stale as a second-order cascade from bumping `the-unbroken-bond.md`'s date and were closed the same way.

**Gates:** wiki-lint **441 pages / 0 errors** (13 warnings, unchanged set) · wiki-connect check **0 errors** (213 warnings, down from 216 after closing two reciprocal-edge gaps introduced this pass) · wiki-climb check **441 pages, 22 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.

## [2026-08-10] rewrite | mind | wiki-rewrite pass — taboo-and-boundary-testing, attachment-model, two new pages, new politics/ cluster
Operator directive via the `wiki-rewrite` skill: two existing pages named for full wipe-and-rewrite (`taboo-and-boundary-testing.md`, `attachment-model.md`), two page names given that turned out not to exist yet (`kevin-mckiernan`, `creative-license`), and an instruction to begin a politics and axiomatic ideologies section. First real test of the `wiki-rewrite` skill against pages with heavy inbound linkage rather than the four-island reference pass.

**The taboo-and-boundary-testing page's central claim was already false, and had been for two weeks.** It said the "orientation violation" mechanism had "no independent primary-source example... the thinnest-supported claim in this entire cluster." `wiki/mind/concepts/erotic-architecture.md`, last touched 2026-08-02, already documented the October 2019 filmed MMF with Bryan as exactly that instance — the correction had been made once in the wiki and never written back to the page whose own claim it falsified. Also found: the second AI dossier (`DANSYNTH.txt`) that appeared to independently corroborate the claim resolves, by its own footnote, to `Dan Profile.txt` — one claim restated with more graphic specificity, not two sources agreeing. Corrected on the page and propagated to three downstream copies of the stale claim (`mind/index.md`, `psychosexual/index.md`, `emotional-imprinting.md`).

**Attachment-model.md carried a superseded number from the very document that supersedes it.** The table's "13 major self-indicting apologies," cited to `TheoryOfEverything_Updated`, ignored that document's own audit revision to 46 — "a significantly larger number than previously counted." Also found: two table rows (266 relationship events, 84 cheating/affair events) are corpus-wide totals from `LIFE_EVENTS_CALENDAR.md` (66 contacts, all of Dan's life, 2015–2026), not Annie-specific as the page implied; a genuinely new, previously-omitted data point across four independent source documents — 12 of Dan's own crisis/suicidal statements met with no substantive response (a bar name, a 12-hour silence, "what the hell dan"); and an unresolved discrepancy between the wiki's standing 127/110 exit-relapse figure and the source material's own "100% re-engagement" framing, flagged rather than silently adopted. The 13→46 correction propagated to `attachment-trauma-bond.md`, which carried the same stale number. Staleness cascade: `attachment-trauma-bond`, `block-unblock-loop`, `dan-annie-fallout-verdict`, `the-deferred-audit` all re-checked with real RE-CHECKED blocks — no conclusion reversed on any of the four.

**Kevin McKiernan and Creative License turned out to be one research thread, not two.** Neither page existed. McKiernan's Facebook contact card carries the email `kevin@creativelicense.com` — he is the president of Creative License, Dan's second NYC studio-adjacent employer (2011–2012ish), already present in the wiki as an unnamed detail on `wiki/places/90th-st-manhattan.md`, which credits the job's ending as the founding case of `vertical-authority-skepticism` (a trusted authority figure's alleged airfare-billing fraud, met with exit). New pages built for both — and the founding-case claim itself does not survive full scrutiny: the specific fraud allegation exists only in two AI dossiers restating each other's language, with zero primary corroboration anywhere in the corpus, and the exit date is contradicted a full year by Dan's own résumé ("Jan 2011 – Feb 2013" vs. the dossiers' "February 2012"). Corrected on `90th-st-manhattan.md` with a CORRECTED block (old claim preserved) and written back into `vertical-authority-skepticism.md` itself, which had never named Creative License despite the dossiers calling it the origin case.

**New politics/ cluster, opened with one real finding rather than a reorganization.** `wiki/mind/politics/` (index + `axioms.md`) is a new topic-based grouping inside `mind/`, alongside the existing `psychosexual/` precedent — the existing political synthesis pages (`political-psyops.md`, `2020-left-turn.md`, `vertical-authority-skepticism.md`) were cross-referenced, not moved, to avoid a repo-wide link-rewrite for no navigational gain. The new page resolves a "paradox" `Dan Profile.txt` names and never checks: "leftist politics and a fascination with authoritarian power (e.g., Caesar, Trump)." Two pieces of evidence settle it. First, the 2024 Roman-Republic reading binge's own table (already on `roman-republic.md`) includes Michael Parenti's explicitly Marxist, class-conflict account of Caesar's assassination, rated identically (5/5) to a conventional biography read the same month — comparative power-structure analysis, not strongman admiration. Second, and stronger: Dan's own self-authored AI-collaborator system prompt (`CATO_BOOTLOADER_DANFRANK.md`) names its identity `CATO`, origin "Cato the Younger... self-deleted at Utica post-Thapsus" — Caesar's specific political opponent, who died rather than live under his one-man rule. Dan built his own primary analytical persona around the man who opposed concentrated power, not the man who won it. The existing `exocortex.md` page already documented CATO but read the name only as general Stoic stubbornness, missing the specific political content — corrected there too. States an explicit falsifier (a documented instance of Dan rooting for a favored figure's power to go unchecked) and reports a negative check against it (none found in Twitter/Facebook, not exhaustive).

**Staleness cascade, full accounting:** `attachment-trauma-bond`, `block-unblock-loop`, `dan-annie-fallout-verdict`, `the-deferred-audit` (from the attachment-model rewrite) and `instrument-is-subject` (from the exocortex.md edit feeding the new politics page) — five pages, five RE-CHECKED blocks, zero conclusions reversed, zero dates bumped without a re-read.

**Gates:** wiki-lint **445 pages / 0 errors** (13 warnings, unchanged set) · wiki-connect check **0 errors** (215 warnings) · wiki-climb check **445 pages, 23 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.

## [2026-08-09] edit | people, mind | operator correction — Tuquick and the unnamed man confirmed as one person
Operator, mid-session, on the just-opened PR: "They are the same person - tuquick and unnamed." Filed at `raw/people/captures/2026-08-09-tuquick-unnamed-man-correction.md`, same standing as the 2026-07-13 Tuquick correction and the 2026-08-02 twenty-four-hour-switch correction — authoritative on facts about the operator's own life that the message corpus could not independently verify.

This closes the identity question the same-day ingest (above) had deliberately left open: the FOREWARN phone-number match closed Tuquick=Jerel Wayne Coles, but nothing in the capture independently linked Tuquick to the July 2026 antagonist. The operator's statement supplies that link directly. Updated across every page that carried the hedge: `wiki/people/jerel-coles.md` (now states the merge as confirmed, folds in the-unnamed-man's July 2026 substantive content — what he did, what Annie says he did to her — as the canonical entity page for all three identities), `wiki/people/the-unnamed-man.md` (SUPERSEDED block rewritten, broken-finger contradiction marked resolved), `wiki/people/tuquick-17248123683.md` (canonical-page pointer updated), `wiki/mind/concepts/forensic-method.md` (the off-switch `contradicts` edge closes fully rather than partially), `BACKLOG.md` (the-unnamed-man-vs-tuquick line marked SETTLED).

The other open questions this session's ingest logged (Target G, the dual-address gap, the accusation-origin question, docket verification) are unaffected by this correction and remain open — the confirmation closed one specific identity link, not the whole open-questions set.

Gates: wiki-lint **441 pages / 0 errors** (13 warnings) · wiki-connect check **0 errors** (213 warnings) · wiki-climb check **441 pages, 22 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.

## [2026-08-10] ingest | people, work, mind | live Gmail sweep corrects Creative License/Kevin McKiernan — twice, in one afternoon
Operator, after reading the same-day wiki-rewrite pass: "i believe there IS corroborating info about kevin mckiernan in my gmail," then "check all of my gmail stuff and takeout archives for kevin mckiernan shit." Live search of `dfrank88@gmail.com` (`mcp__Gmail__search_threads`/`get_thread`) recovered ~35 threads from 2011–2012 (plus a Dec 2014 coda) never before filed to `raw/`. Filed to `raw/self/gmail-captures/2026-08-10-creative-license-kevin-mckiernan-gmail.md`.

**The AI dossiers' specific allegation was invented; the real conflict was worse in a different way — and this session got the correction wrong once before getting it right.** The morning's wiki-rewrite pass had already flagged that `THE_DAN_FRANK_BOOTLOADER.md`/`THE_DAN_FRANK_MANUAL.md`'s "exits over airfare-billing discrepancies and altered intern contracts" line had zero primary corroboration. The Gmail sweep found no airfare dispute in the recovered email — and this session's own pages briefly, wrongly, declared the airfare claim outright fabricated. **That was itself an extraction failure**: it never checked `wiki/self/chats/gemini-58.md`, built from a source already sitting in `raw/` (`Gemini-_58.txt`) since a prior ingest. That session contains Dan's own primary testimony, in his own words, inside an AI chat: "the thing i cited when i quit had to do with some kind of small fraud with airplane tickets that i blew it up into a much much bigger thing but maybe i was just desensitized." Per this wiki's own source-tier rule, a subject's own words inside an AI session are primary testimony even when the surrounding model output isn't — so the airfare citation is real; only Gemini's speculative elaboration of its mechanism (mismarked Walmart/Molson Coors travel billing) remains unverified. Corrected a second time on `wiki/work/creative-license.md` and `wiki/people/kevin-mckiernan.md`, with both correction passes left visible rather than silently merged.

**What the Gmail record actually documents, independent of the airfare question:** a six-week final-paycheck dispute (Feb–Apr 2012) over a missing W-2 and a disputed $104 MetroCard charge, escalated by Dan to the IRS and NYS Dept of Labor, that produced the page's anchor quote — accountant Marty Jackson's "It's a trust issue. We don't trust you." — which Dan later quoted back at him and then explicitly separated from personal animus once the dispute closed ("I didn't mean to give the impression that my hostility was directed at you personally"). Three months later, unprompted, Dan disclosed to a former coworker (Renae Holland) that company president Kevin McKiernan had used Dan's own account to pressure former employees and had altered two departing interns' contracts to add a CEO-approval gag clause on recommendations — corroborated independently by Renae's own account of McKiernan falsifying documents. A month after that, McKiernan retaliated with a formal LinkedIn IP claim asserting Dan had never been an employee at all, backed by two documents notarized by company Director of Business Affairs Katherine Palakovich — using her own notary commission on her employer's behalf against a former coworker, which Dan flagged directly to her as a Notary Public Code of Professional Responsibility violation. Dan's counter-notice named the retaliation motive explicitly and the company's own social circle (including Palakovich) still had Dan on an "ex-CL employees" happy-hour list as late as December 2014.

**New pages:** `wiki/people/marty-jackson.md`, `wiki/people/katherine-palakovich.md`, `wiki/people/renae-holland.md`. **Rewritten:** `wiki/work/creative-license.md`, `wiki/people/kevin-mckiernan.md` (both a second time, same day). **Corrected again:** `wiki/mind/synthesis/vertical-authority-skepticism.md` and `wiki/places/90th-st-manhattan.md` — the "founding case" framing survives, now on much stronger evidence than either the original dossier claim or the first (overcorrected) same-day revision.

**New names surfaced but not yet independently verified against email** (Gemini-58 only, flagged as such on the pages): Rachel Rauch (recipient of an April 2012 cathartic `BEST OF KTM VOICEMAILS.mp3` attachment), Sarah Bromberg, Charley Siegel (survivors'-network figures — Siegel and Bromberg do independently appear in later LinkedIn-notification snippets, which is corroborating but not confirming), Chris Marraffino and Michael DiTullio (interns named in the LinkedIn-purge/contract-alteration conduct), Simona Rabsatt (Walmart) and Lori Estabrooks (Molson Coors) as named client contacts.

Gates: wiki-lint **448 pages / 0 errors** (13 warnings, unchanged set) · wiki-connect check **0 errors** (216 warnings) · wiki-climb check **448 pages, 23 with `synthesizes:`, 0 errors, 0 warnings**. `bin/wiki-digest` and `bin/llm-publish` rerun.

## [2026-08-10] rewrite | people, places | annie-ulmer.md wiki-rewrite pass + 3 manual captures — sex resumption, the 307 E 76th St cast, Suz's Winter Park condo
Operator invoked the `wiki-rewrite` skill on `annie-ulmer.md` with a pasted three-entry manual-capture queue (INGEST_PROTOCOL.md style): (1) sexual contact resumed, breaking a six-month gap; (2) the 307 E 76th St "cast of clowns" — a super/agent (Jim Blanchard) and a landlord (John Paci), a stiffed $10k debt, a roach-bombing evacuation, and its connection to the September 2020 "Train Plan" trip to PA; (3) Suz's Winter Park, FL condo, bought rather than rented during Dan's Full Sail years, later rented to a tenant arrested for sex-trafficking. Filed all three verbatim to `raw/self/captures/`. **Treated as an integration pass into the existing, already-repeatedly-rewritten `annie-ulmer.md` structure rather than a from-zero wipe** — CLAUDE.md prohibits regenerating an earned page from scratch outside a deliberate wipe, and this page's own changelog shows it has already had that treatment; the wiki-rewrite skill's re-research discipline (verify with the right instrument, rank sources, flag corrections visibly) was followed in full even though the prose was not razed.

**The capture's own memory had the 307 E 76th St sequence backwards, and the message corpus settles it precisely.** The bombing (Sept 10–11, 2020) preceded the Train Plan crisis (Sept 19–20), not the reverse — the two exterminator visits (the original bombing, and a second one Dan is arranging with Paci on the literal night of the Train Plan blowup) are easy to conflate in memory into one event. Both readings converge on the finding worth keeping, which nobody had connected before this pass: the PA relocation that hosted the Train Plan crisis had a mundane, dated, previously undocumented cause. `wiki/places/307-e-76th-st.md` expanded from four thin paragraphs (naming no one connected to the building) to a full cast-and-timeline page.

**The landlord debt was corrected, not just documented.** `annie-ulmer.md` previously said the $10,000 debt was "paid down at $650 a week," implying resolution. A March 5, 2025 message from the landlord, John Paci, rounds the balance to a final $10,000 and asks Dan to begin paying it down; Annie's own annoyed reaction to a Paci text four months later ("Fucking John Paci just texted me," July 2025) is consistent with it never being retired. CORRECTED block added with the old claim preserved. New pages: `wiki/people/john-paci.md` (closed, well-documented — landlord for the entire six-year tenancy) and `wiki/people/jim-blanchard.md` (filed as `status: stub` — the only independent corpus trace is one neutral November 2019 message; the operator's negative characterization and role assignment are recorded as testimony, not verified).

**The Winter Park condo/trafficking-tenant lead was researched and comes back an honest negative.** WebSearch located a strong circumstantial candidate for the complex — Indigo Winter Park (220 S Semoran Blvd), sitting on the SR 436/University Blvd corner directly opposite Full Sail, consistent with the "across from a Crispers on 436" description — but no matching arrest, court record, or news story from the ~2009–2011 window was found, and nothing ties the Frank family to that specific address. Recorded on `wiki/people/suzanne-frank.md`'s new "Winter Park condo" section as the operator's account, not independently verified either way, with the full search record kept at `raw/self/captures/2026-08-10_websearch-winter-park-condo-lead.md` so a future pass doesn't repeat the same queries. This is the earliest documented instance of Suz using property rather than cash to support Dan — a decade before 337 Saratoga and 463 Morgantown.

**Staleness cascade, two rounds, exactly as the skill predicts.** Round 1: `estate-money-spine.md`, `supply-network.md`, `the-unbroken-bond.md` went stale against `annie-ulmer.md`. Two closed as genuinely orthogonal (supply network — nothing in the captures touches drugs); one produced a real correction (`estate-money-spine.md`'s "three-rotation see-saw" framing said Dan "worked through" the 2023 landlord-debt stretch, which is now known to overstate resolution — narrowed in a RE-CHECKED block without touching the page's other figures); one produced a genuine refinement (`the-unbroken-bond.md`'s Falsifier 1 is about unattached periods, not sexual ones — the six-month sexual gap is read against the page's own occupancy-vs-activation distinction and found not to falsify the continuity claim, but to sharpen it: the bond's sexual and relational/administrative layers appear to have gone dormant and reactivated on different, overlapping timelines around the June 1 severance). Round 2: `dormancy-not-exit.md` and `single-channel.md` went stale off `the-unbroken-bond.md`'s bump; both re-read against their own actual claims (reactivation bandwidth across different channels; the occupancy accounting identity) and closed as unaffected, with `dormancy-not-exit.md` noting the new finding as a same-relationship instance of a pattern it already documents elsewhere.

New connections wired both ways: `annie-ulmer.md` ↔ `307-e-76th-st.md` (evidences/evidenced-by, corrected from an initial mismatched `instantiates`/`instantiates` pair caught by `wiki-connect check`), `annie-ulmer.md` → `john-paci.md` (co-occurs), `307-e-76th-st.md` → `john-paci.md` (contains) and `jim-blanchard.md` (co-occurs), `suzanne-frank.md` ↔ `full-sail-2008-2010.md` (co-occurs). `wiki/people/index.md` and `wiki/places/index.md` updated.

Gates: wiki-lint **450 pages / 0 errors** (13 warnings, unchanged set) · wiki-connect check **0 errors** (216 warnings, down from 218 after the instantiates/instantiates mismatch fix) · wiki-climb check **450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings** after both cascade rounds closed. `bin/wiki-digest` and `bin/llm-publish` rerun.

## [2026-08-10] rewrite | people | annie-ulmer.md deep-mining pass — new events from previously unread raw/ sources
Operator, after the prior integration pass: "no i want like an actual substantial rewrite of the annie entry by scrapining and minining a BUNCH of new data points or events to add in." Surveyed all raw/ files touching "annie"/"ulmer" (212 candidates), cross-checked against the page's already-extensive `sources:` list, and read to exhaustion the highest-value previously unmined files: two AI-analysis sessions (a Grok "aura illness" chat and a Claude "interpersonal manipulation" chat, both working from primary message logs), `LIFE_EVENTS_CALENDAR.md` (already sourced but re-swept specifically for unused Annie mentions), and a cross-check against `relationship-breakdown-summary-2025-04-27.md` (already the primary source for `feb-apr-2025-return-and-rupture.md`, mined here for a cross-link rather than fresh extraction).

**Five genuinely new findings, not five new framings of old ones:**

1. **Annie's pre-Dan paid-content history.** An October 2018 message, reminiscing rather than disclosing in the moment, describes her running a paid photo/video account before the relationship (pre-Nov 2015) and being blackmailed by men threatening exposure — the earliest documented instance of paid-content work in her record, predating the MyFreeCams history already on the page, and a real motive (not just novelty) for the joint arrangement the relationship later built.
2. **Grandfather Jim's death is now dated: October 2, 2019**, surfaced in an aside Dan sent a client about a possible booking conflict. This is the origin point of the "Sugie needs care" alibi this page returns to for years afterward — not fabricated, even where it later became convenient. Written back to `ellen-ulmer.md`, which had already identified Jim and Sugie as Annie's grandparents but not his death date.
3. **The Target G / "Whisk" section gained real resolution.** A previously unmined Claude session (reading the timestamped log directly, not a dossier summary) supplied four dated exchanges (Jan 5, Jan 9, Feb 1, Mar 1 2026) with granular quotes. The single most valuable one: on Feb 1, **Annie herself** — unprompted, while disclosing she'd taken five sleeping pills — names the man directly ("Caitlin's husband came here last night"), which is materially different evidentiary weight than the dossiers' secondhand "Caitlin's husband" label the page previously carried. An independent, unsolicited corroborating quote from Bop ("She's always sneaking around") is also new. Flagged: none of the four exchanges were re-verified against `all_imessages_complete_dump.txt` directly in this pass — they're transcribed from a prior AI session's own reading, one level removed from raw.
4. **The $10,000 landlord debt gets independent corroboration, plus a new, previously undocumented $7,000 Con Edison utility debt.** A contemporaneous April 27, 2025 account — after Paci's own March 5 settlement letter — already carries the same $10,000 figure, ruling out any reading where payments were still reducing the balance in its final months. The $7,000 ConEd bill is a distinct debt to the utility, not the landlord, cross-linked to `feb-apr-2025-return-and-rupture.md` (its original source, already in `raw/` and already mined for that page — this pass added the cross-reference to `annie-ulmer.md`, which hadn't carried it).
5. **The isolation compounding around the June 1, 2026 severance is now named as one event, in Dan's own words.** A Grok session dated internally to late May/early June 2026 has Dan naming three simultaneous losses together — the May 2026 BFS Foods termination, the 337 Saratoga move-out notice ("we have to move out in like 3 weeks"), and Tom Maison's silence after a $35 sub-sandwich dispute — as a single compounding crisis, and coining his own term for the resulting state: **"aura illness."** New connections wired to `wiki/work/bfs-foods` and `wiki/places/337-saratoga-drive`; prose cross-references added to `wiki/people/tom.md`.

**What was checked and found not to be new.** Several quantified figures in the mined AI sessions (91 love-to-request instances, 94 burst events, 52 fell-asleep alibis, a 1.22x→1.94x response-ratio) were compared against the page's own already-verified numbers (187/191, 94-with-max-68, 24 alibis) — the page's own XML-parsed docx re-extraction from the 2026-07-24 pass is the more rigorously sourced figure in each case, so the AI-session numbers were not substituted in. This is deliberate: EXTRACTION_SPEC's source-tiering discipline applies as much to which AI-secondary count wins as to whether to trust one at all.

New connections: `annie-ulmer.md` ↔ `wiki/work/bfs-foods` (co-occurs), `annie-ulmer.md` ↔ `wiki/places/337-saratoga-drive` (co-occurs). Prose-only cross-references (no new edge needed — existing edges already covered a different fact): `wiki/people/ellen-ulmer.md`, `wiki/people/tom.md`.

Gates: wiki-lint **450 pages / 0 errors** (13 warnings, unchanged set; `annie-ulmer.md` now 96KB, advisory-only) · wiki-connect check **0 errors** (216 warnings, unchanged — both new edge pairs matched cleanly) · wiki-climb check **450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings** (no new staleness cascade — same-day edit, no premise date moved past a dependent's). `bin/wiki-digest` and `bin/llm-publish` rerun.

## [2026-08-10] edit | people | Winter Park condo address confirmed — 2924 Antique Oaks Circle
Operator, quick correction: "quick update the winter park address was 2924 antique oaks circle, winter park, FL." Filed to `raw/self/captures/2026-08-10_160647_winter-park-condo-address.md`.

Verified as a real address: a unit in the **Parkview Village** condominium community (350 S Semoran Blvd, Winter Park, FL 32792), confirmed via live web search as sitting directly across from Full Sail University — consistent with the "Crispers on 436, complex directly across the road" description from the original capture. This retires the earlier same-day "Indigo Winter Park" candidate as a wrong guess in the right corridor (right block, wrong complex). A further search anchored to the confirmed address and complex name still found no matching human-trafficking arrest, court record, or news story — the address is now settled; the arrest remains unconfirmed. `wiki/people/suzanne-frank.md` updated with a CORRECTED block; the superseded first-pass reasoning is kept visible rather than deleted, per style-guide convention. The research-note capture file also updated with a RESOLVED block so a future pass sees the address is closed and only the arrest itself is still open.

Also caught in passing: `suzanne-frank.md`'s `sources:` list and `date_modified` had not been updated during the earlier same-day Winter Park section addition — fixed here (three capture files added to `sources:`, `date_modified` bumped 08-09 → 08-10).

Gates: wiki-lint **450 pages / 0 errors** (13 warnings, unchanged) · wiki-connect check **0 errors** (216 warnings, unchanged) · wiki-climb check **450 pages, 23 with `synthesizes:`, 0 errors, 0 warnings** (no cascade — dependents already at 2026-08-10). `bin/wiki-digest` and `bin/llm-publish` rerun.

## [2026-08-13] correction | mind, people | the June 1 closing line is Dan's — logged retroactively 2026-08-14
Recorded here after the fact. The work landed in PR #110 (commits `3339d2c`, `cce1d74`) and was never written to `log.md` or `LLM_HANDOFF.md` at the time, because the session producing it exhausted its quota immediately after pushing. This entry is reconstructed from the merged diff, not from that session's own account.

**What was wrong.** `"Goodbye forever. This was not how it should have ended but. sic semper lupanis."` (`2026-06-01 00:27:49` ET) was attributed to Annie on five pages. It was sent by Dan. The 2026-08-13 whole-device deep export settles it with a field that admits no interpretation: `SENT OR RECEIVED = Sent`, `HANDLE = Me`, `IS GROUP CHAT = No`. It is the last of six consecutive outbound rows; the next inbound row is Annie's apology four days later. The cause was a direction column rendered `Sent (Received by Dan)` — written from Dan's point of view and read backwards — quoted verbatim on `dan-annie-fallout-verdict.md` for two months. `group-chat-closure.md` carried the contradiction inside a single table cell, crediting the line to Annie and the message 77 seconds earlier to Dan.

**What changed, and what did not.** The self-closure thesis on `dormancy-not-exit`, `the-unbroken-bond` and `block-unblock-loop` was revised rather than patched: the mechanism was **replaced** ("the counterparty's terminating statement is not what performs a closure — it is what would let him treat a closure as settled"), the falsifiers were rewritten to move with it, and Falsifier 3 was scored as "not met — but met halfway" rather than rounded to a clean answer. `the-unbroken-bond`'s central thesis survives; its "exit is structurally unavailable" clause does not. No `date_modified` was bumped to clear a warning.

**Also landed:** both 2026-08-13 whole-device exports filed to `raw/self/message-csv/` with `README_20260813_exports.md` — UTC convention validated empirically against a local-time source on 42,895 uniquely text-matched pairs (23,158 at +5.00h EST, 19,692 at +4.00h EDT, 45 outliers at 0.1%); the 41.8% lossiness against `all_imessages_complete_dump.txt`; the ~833-day export artifact bounded to 2021-04-27 → 2023-08-09. The three-column flat export was filed **deliberately as the worked example of its own failure** — it has no handle column and cannot attribute — rather than discarded. `john-paci.md` was rebuilt around the operator's staged-eviction decode, correctly recording the February 2025 eviction as an arrangement Dan initiated and Paci performed, and correcting the capture's own "167-day" gap to 166.

Gates at the time of that merge were not recorded. Re-run 2026-08-14: wiki-lint **457 pages / 0 errors**, wiki-connect check **0 errors**, wiki-climb check **457 pages, 27 with `synthesizes:`, 0 errors**.

## [2026-08-14] lint | self | the archive is 9.6x duplicated, four cited sources are empty, and 18 filenames overstate their coverage
Built `bin/source-index` (pure stdlib, per repo convention) and generated `wiki/self/message-corpora/source-coverage-index.md`. Triggered by an operator question about consolidating redundant files in `raw/`.

**The answer to that question is no, and the measurement is why.** 52 message sources hold 1,786,124 rows against roughly 187,000 unique messages — about 9.6x duplication. But every correction this repo has ever made was found by one export contradicting another: the 2026-08-11 Rick correction and the 2026-08-13 `sic semper` inversion both. Merging the sources would delete the only error-detection the corpus has. The fix for redundancy is an index, not a merge.

**Three findings, none of them previously visible:**
1. **Four sources are header-only with zero data rows**, and two of them are cited by wiki pages — `END_FIGHT_full.csv` (68 bytes) on four pages including `dan-annie-fallout-verdict.md` and `group-chat-closure.md`, where it is credited specifically for "sequence details"; `annie_group_chat_may31-june1_2026.csv` on `bond-switch-2015.md`. This is a distinct failure class from the `sic semper` inversion: that was provenance present, precise and *wrong*; this is provenance present, precise and *empty*, and no reader can tell it from a real citation. Queued in `BACKLOG.md` — whether any claim rests on an empty file *alone* is unaudited, and the plausible answer ("redundant decoration") is not permitted to close it.
2. **18 sources carry a filename that overstates what they hold.** The `_all_now` / `_all_time` suffix is unreliable as a class, not occasionally: `imessages_2124702449_last6months.csv` spans 24 months; `annie_all_time_logs.csv` starts 2022-12-31; `imessage_7243667777_both_all_now.csv` — the file behind the Rick error — holds 42 rows.
3. **22 of 52 sources have no handle column** and are structurally incapable of attributing a message to a person. Only two sources are both full-range and attributed.

`master-message-dump.md` corrected: its group-drama row credited "~1k+" events to four files, three of which are empty; the real figure is 589 rows from one file.

Gates: wiki-lint **457 pages / 0 errors** (14 warnings, down from 15 — new page's orphan warning resolved by a real inbound link) · wiki-connect check **0 errors** (236 warnings, unchanged) · wiki-climb check **457 pages, 27 with `synthesizes:`, 0 errors, 10 warnings** — the 10 are the unworked staleness cascade from PR #110, see handoff.

## [2026-08-17] restore | timeline | the December 2015 Annie read was written into the portal's derived snapshot and a cron deleted it 39 minutes after merge

Two hand-read passes over the Annie corpus — Dec 1–16 and Dec 17–31, ~120 event entries and the matching entity ledger, open leads, motif tracker and per-day counts — were written as JSON into `caakehorn/home`'s `public/wiki/pages/`. That directory is not a copy of `wiki/`; it is derived from it by `sync-wiki.mjs`, which `rmSync`s the whole tree and rebuilds it, driven by a workflow that fires on `repository_dispatch` **and** on an hourly cron. `home#27` merged at 03:21 UTC and the 04:00 resync reverted `timeline__annie-record.json` from 57,523 characters to the 17,857-character Nov 30 state. `home#28` was open and queued to meet the same job.

**The loss was silent in both directions.** Nothing failed: the PR merged green, the bot's revert commit is titled "Resync the wiki snapshot" like the other 42, and the page kept rendering — just without December. And because the passes were never in this repository, they never read or updated `LLM_HANDOFF.md`, never ran the gates, and never appended here. This file's resume point still read `bin/annie-corpus read 2015-12-01` after 13,635 messages had been read.

**Restored to source in `wiki-brain#125`**, byte-identical to `home#28`'s head — verified by running home's own `scripts/sync-wiki.mjs` against this checkout and diffing the emitted JSON against the blob at `f09dfc0`, not by inspection. The derived fields hand-editing could not update come back correct as a side effect: `annie-record` `words` 2,964 → 12,778, `annie-read-notes` 1,512 → 4,529. One deliberate departure: the Dec 13–16 pass had rewritten Annie's four handles as `+172****6811`, an edit to pre-existing prose rather than to new material, and it is reverted — the `sources:` filenames three lines above still spell the same digits out, and the page uses the handles to separate her contact identities by era.

**The prose guardrail already existed and was not enough.** `caakehorn/home`'s README says, at line 356, that "writing to the source rather than to `public/wiki/` is the whole point of the arrangement: that snapshot is a build artifact, and the next sync would overwrite anything written into it." Both passes did it anyway. The rule is therefore now in `CLAUDE.md`'s architecture section, where a session in this repository loads it without being told to look — and the flow diagram carries the portal as a fourth stage so the one direction is visible rather than described.

**The extraction defects were carried unchanged rather than silently fixed**, because a rescue that also rewrites content cannot be verified against the thing it rescued. Against the Nov 28–30 baseline: zero `[[wiki/…]]` cross-links across 153 December entries (baseline 13 across 33), zero hedges in Dec 17–31, 7 of 36 headers timed to a minute that appears nowhere in their own entry, 3 of 12 headline quotes absent from their own entry. Dec 18, 20–24 and 26–28 have neither entries nor a gap note, and Dec 26–28 are missing from a quantitative table presenting a complete total — the failure this page's own preamble names, that a zero is data only when the system could have observed a one. The December 23 Harshman confrontation this page forward-references twice falls inside the restored window and is never addressed. Full list and the specific misattributions in `LLM_HANDOFF.md`; the corrections pass is queued and not started.

Gates: wiki-lint **460 pages / 0 errors** · wiki-connect check **0 errors, 239 warnings** · wiki-climb check **460 pages, 27 with `synthesizes:`, 0 errors, 4 warnings** — the 4 are the documented carried-forward staleness. `annie-record.md` now trips the 74KB advisory size warning; per `CLAUDE.md` that means check navigation, never shorten.

## [2026-08-17] climb | timeline, people, mind | the 2015 Annie read spread to ten pages, and five of its own corrections did not survive the evidence gate

First run of the spread step on the hand-read window 2015-11-28 → 2015-12-31. Every claim was gated on a verbatim quote pasted from `annie-record.md` rather than recalled; the working table carried 26 rows and **five were cut**. The cuts are the finding, because four of the five had already been applied or queued somewhere as fact.

**What the gate caught.** *"turd boy" is Emilio* — the quote names no one, Emilio first appears three days later, and the identification had already been written into `bond-switch-2015` by an earlier pass; being an ex who resurfaces is not evidence of being *that* ex. *"Suz gives Dan $200 worth of cocaine"* — the record has Annie saying *"that $200 wasn't even your own"* and Dan answering *"It was my money"*; the two lines conflict, the corpus does not settle them, and the claim had been queued as a correction to `suzanne-frank`. *The Dec 9 threat is Zachariah Harshman's* — it is [[wiki/people/zach-clingan|Zach Clingan's]], the same two-Zachs collision `zach-clingan` already documents from a phone-book merge, recurring in the opposite direction. *`zgurd` is whiskey* — glossed once that way and used everywhere else as something bought from Suz in quantity; now in the ledger as unresolved. *Annie quit CT's voluntarily on Dec 9* — no supporting quote exists anywhere, and she is bartending on Dec 16 and working Dec 30–31.

**The largest single gain is an origin fact nobody had.** Dan, 2015-12-09 15:20, on Zach Clingan: *"Literally makes me want to puke. THAT is who introduced me to drugs."* `zach-clingan` had him only as a fixed point in a 2014 moral taxonomy — one of the "drug people" Dan uses to locate himself and Tom on a scale. He is the earliest point on the supply chain and he is a person, not a node, which reframes that taxonomy as a claim about lineage rather than a sort.

**Ten pages now carry the read**: `bond-switch-2015` (the switch was mutual *and* brokered — Suz's cocaine and a car conditional on the eviction, at 05:02 on 11-30), `suzanne-frank`, `supply-network` (the mechanism named in real time on 11-29, about the *departing* partner, ~3 years earlier than any node the page tracked), `annie-ulmer`, `ellen-ulmer` (the Dec 2 crisis, fifteen months before her own thread opens, with relay attribution made explicit — none of those words are hers), `zach-clingan`, `zachariah-harshman`, `casey-bondarenka` (one week in the friend group, not longstanding), `alexis-armel`, and the 2015-2016 period page ("day two" corrected to ~90 minutes after first physical contact).

**One reconciliation worth keeping.** The Annie corpus has zero messages across 2015-12-20 → 12-24, which spans the December 23 Harshman rupture exactly. That is a channel fact, not a contradiction: the rupture is Facebook Messenger and the Annie corpus is iMessage. Recorded on both pages so no future pass reads the silence as evidence against the date.

**No climb was written.** The candidate — information control as intimacy, three dated instances in five weeks — is held in `synthesis-queue.md` with reasoning: the third instance controls Annie's *inbound* information rather than a third party's and may be a different mechanism, and generalising to the 2026 material from three 2015 instances is climbing on sand while the December entries are still uncorrected. A second cluster (family capital underwriting the switch) was rejected outright as an umbrella and written back into `estate-money-spine` and `supply-network` instead.

Gates: wiki-lint **1 error** — `master-timeline.md` invalid tags, pre-existing and generated, so the fix belongs in `bin/wiki-timeline`, not the page. Down from 6: this pass fixed the invented `page_type` values and out-of-set tags that `annie-record` and `annie-read-notes` have carried since creation (they had never passed lint, which is what happens when no pass runs the gates), and gave frontmatter to `2015-annie-read-wiki-impact-analysis.md`. wiki-connect check **0 errors**. wiki-climb check **0 errors, 15 staleness warnings — 11 of them newly created by this pass** and deliberately not cleared: bumping `date_modified` on ten ground pages moved premises under `attachment-trauma-bond`, `block-unblock-loop`, `dan-annie-fallout-verdict`, `dormancy-not-exit`, `estate-money-spine`, `the-unbroken-bond` and `totality-themes`. That debt is the write-back working, and clearing it is the next pass, not this one.

## [2026-08-17] close | people, timeline, mind | the operator named "turd boy", and three separate incidents became one retaliation arc

The synthesis pass earlier today cut *"turd boy" = Emilio* at the evidence gate: the 2015-11-29 window calls Annie's partner only *"dude"* and *"turd boy"*, Emilio is not named until 12-02, and being an ex who resurfaces is not evidence of being *that* ex. The operator has now supplied the identification directly. Applied per CLAUDE.md's CLOSE protocol — as T0 testimony, not proof, with the provenance recorded on every page it touches so no future reader mistakes it for something the corpus establishes.

**The gate was right and the answer was right, and that is the point.** It stopped an inference from being written as a derivation; the claim then arrived by the one route that can actually carry it. Both outcomes are recorded on `annie-read-notes` rather than the cut being quietly deleted.

**What the identification buys.** Three incidents previously filed apart are one sequence: Annie says *"I am going to get rid of him just like you just did"* (11-29 02:52); seventy-two hours later he contacts **her sister, not her** — *"because fucking Emilio texted her about me"* (12-02 18:45) — which is why Claire turns on Annie inside the confrontation that nearly ends the relationship in its first week; and he is still going on 12-13, after *"throwing shit at me the other night"*, with *"Honestly I just miss having fun with you!"* The December 2 crisis has had no agent in any account for a decade. It has one now, and the agent has a motive that is three days old.

**It also completes the switch's symmetry.** `bond-switch-2015` documents the cost of the singular-slot mechanism entirely on Dan's side — the Alexis eviction, the Harshman rupture of 12-23. Emilio is the same cost on Annie's side and it lands *first*. Both partners were displaced inside the same seventy-two hours, and both displacements detonated a relationship within the month. Written into the synthesis as a new section rather than a footnote, because it changes what the thesis predicts.

**Held separate deliberately.** The person who told Ellen *"someone told me your car was at Dan Frank's this morning"* is still **never named**, and both Dan and Annie blame Casey. Emilio's documented vector is Claire. The two are not collapsed, on any page, and each carries a line saying not to.

New page: `wiki/people/emilio.md` (stub — he has no channel of his own in any export; every line is relayed through Annie). Cascaded to `annie-record`, `annie-ulmer`, `bond-switch-2015`, `claire-ulmer`, `annie-read-notes`. Open lead #1 closed; the residue under it — surname, his own traffic, the Becca attribution — kept open.

Gates: wiki-lint **1 error** (`master-timeline.md` invalid tags, pre-existing and generated) · wiki-connect check **0 errors** — the three inverse edges Emilio's new edges required were written, not left as warnings · wiki-climb check **0 errors**.

## [2026-08-17] tool | meta | bin/wiki-gaps could not see two-thirds of the wiki's unsettled information, and left no trace of what the operator added

Three changes, all from the same root cause: the tool was built around one section name and one interaction, and the corpus had outgrown both.

**A gap is not the only shape unsettled information takes.** `GAP_HEAD` matched `## Gaps` and four synonyms. It did not match `## Open leads`, `## New open leads`, `## Corrections queue`, `## What's missing`, or any of them numbered (`## 2. Open leads`). Those are the same thing under different names — a question the operator can answer — and the tool could not reach a single one. `wiki/timeline/annie-read-notes.md` alone was carrying four such sections; the tool reported it as having **zero** open items. Corpus-wide the count moves **276 → 305**.

Two parsing changes came with it, because those sections are not shaped like `## Gaps`. **A corrections queue is a table, and its rows are the items** — the whole table arriving as one 40-line "gap" is not answerable, so table blocks now emit one item per data row, header and rule dropped, and rows whose last cell says `applied` or `n/a` filtered out alongside the existing `~~`/CLOSED/RESOLVED/SETTLED marks. And **sections that itemise often open with a sentence of prose explaining the list**, which was being offered as an answerable item; anything before the first bullet or table row in an itemised section is now preamble. `## Gaps` sections are unaffected by both — they rarely have either shape, which is why neither problem showed until the vocabulary widened.

**Any page can now be annotated, and could always have been — the tool just never said so.** `MANUAL` has always worked on a page with no Gaps section, but the only listings were gap-driven, so a page with nothing open was unreachable from the tool's own output. New `bin/wiki-gaps pages [filter]` lists all 462, marks the ones already holding a staged answer, and points at the same MANUAL flow.

**Additions now leave a durable trace.** `pending_ingest:` marks a page and `bin/wiki-gaps pending` finds it by scanning 462 files — but the flag is deleted by `clear`, so once integrated there was no record that the operator had ever said anything, short of reading git history. New root-level `operator-log.md`: append-only, one row per addition, written by the tool and marked integrated (not deleted) by `clear`. Backfilled with the five answers already staged and unintegrated, so it is correct on day one rather than empty while work sits waiting. `CLAUDE.md`'s session-start protocol now names it alongside `pending` — the log is the durable half, `pending` the live half.

**Kept in step, which is the part that could have broken quietly.** The same parser exists three times: here, in `bin/wiki-digest`, and as a port in caakehorn/home's `scripts/sync-wiki.mjs` that builds the GAPS view. All three were updated together and verified to agree page-for-page — **121 pages, 313 gaps from both implementations**. A divergence here does not error; it silently produces a site that cannot find an item the tool cut, which is why the check is mechanical rather than by eye.

Gates: wiki-lint **1 error** (`master-timeline.md` invalid tags, pre-existing and generated) · wiki-connect check **0 errors** · wiki-climb check **0 errors**.

## [2026-08-17] close | people, timeline, mind | six staged operator answers integrated — one of them contradicted the man who gave it

Every answer `bin/wiki-gaps` was holding, applied per CLAUDE.md's CLOSE protocol. Five pages, six answers, all staged **from the portal** rather than the CLI — which is itself the finding that changed the tool (below).

**Two of the six were already answerable from the wiki's own pages, and nobody had written them back.** `ellen-ulmer` asked whether Ellen and Dan had any contact after the June 2026 severance; `july-august-2026-reentanglement` has recorded the 06:22 disclosure of July 26 since it was written. `kristin` asked when the $40 went missing; its own body quotes Dan saying *"I've been answering for where it is gone for the last week"* on November 2. Neither was a missing fact. Both were cascade failures — a page went on declaring a gap the corpus had already filled, which is exactly the rot CLOSE step 5 exists to prevent, showing up in the tool's own backlog.

**The most valuable answer contradicts the person who gave it.** `milo` carried Dan's line about Betty — *"You couldn't even stay with her when they put her down so she had to go through it alone"* — flagged there and on the event page as *"sourced only to Dan, in an attack, and uncorroborated."* The operator's account ten months later: Betty seized at Dan's in June 2025, he called Annie urgently, *"we took her to the vet where annie made the decision to euthanize her."* Annie was present and it was her decision. This is **Dan against Dan**, and it is the corpus's first actual test of a heuristic the wiki applies everywhere and had never validated: a claim made inside an attack is weak evidence even when the attacker is the only witness. It held. Every July–August 2026 assertion resting on one party's word mid-fight inherits that discount.

The same answer supplies a mechanism, not just a correction. Betty came into Dan's care because Annie asked and Dan agreed — *"As i saw it as an 'in' to more time with annie, i enthusiastically accepted."* A year later the June 2026 closure held fifty-two days and broke through Milo, the co-held animal that `block-unblock-loop` identifies as the channel carrying no money, drugs or logistics. Dan named that mechanism himself, in 2025, as something he chose deliberately. The 2026 reopening is the second run of an arrangement he had already entered with his eyes open.

**A standing prediction resolved, and stayed honest about its weight.** `block-unblock-loop` predicted the May 30 Tom endpoint would hold if the dependency had ended. Operator: *"No I have not been in contact with tom."* Eleven weeks, against 127 declared exits of which all but one reopened inside 48 hours — a confirmation, and recorded as one. But eleven weeks is a fortnight longer than the Annie closure ran before failing on day fifty-three, so the Tom row is now provisional on elapsed time exactly as the Menore control already is. Recorded as such rather than banked.

**And one answer made the record worse.** `robotussin-s-last-dance` asked whether any of the three were sober enough to decide anything leaving Ruby Tuesday's. Operator: *"on the contrary, we were all MUCH less sober and subsequently even more intoxicated before a 90 minute drive."* The DXM was still coming up, so the 95 mph Rt 51 run was made at peak intoxication rather than on a downslope. Asked to fill a gap about his own culpability in a story he and two friends have always told as adventure, the operator volunteered the fact that makes it least defensible — the opposite behaviour to the in-attack claim above, from the same source, and worth weighing together.

**The tool change this pass forced.** All six answers were staged from the portal, and `operator-log.md` — added yesterday — logs only what the CLI writes. It would have been silently wrong in the one direction that matters: understating what is waiting. The log is now **reconciled from the pages themselves** before `pending` and before `clear`, so an answer staged anywhere is caught, and a portal-staged answer that is cleared without ever having been logged still leaves a row. New `bin/wiki-gaps log` prints the ledger and reconciles as a side effect.

Gates: wiki-lint **1 error** (`master-timeline.md` invalid tags, pre-existing and generated) · wiki-connect check **0 errors** · wiki-climb check **0 errors, 16 staleness warnings** — one more than before, `milo` having moved under a page that reasons from it, and not cleared here.

## [2026-08-19] synthesis | health | cocaine — new substance profile page

**New page: `wiki/health/cocaine.md`.** The corpus carried cocaine-specific findings scattered across at least fifteen pages — a dosage arc on `chemical-architecture`, a genesis chronology in the same page's phased history, nine supply nodes on `supply-network`, the Class B count on `2015-possession-arrest`, the family-rupture coding on `suzanne-frank`, the procurement-as-access thesis on `annie-ulmer` — with no page that held the substance itself. This one does: use history from the age-13 household exposure through first use at Seven Springs (17–18) to the 2012 resumption as a deliberate layer atop the Suboxone base; the finance-driven dosage arc (~1g baseline → 3.5–7g at the 2017–2020 inheritance peak → ~0.5–1g after exhaustion) restated with the retrospective's own reading that the ceiling was capital and never internal; the nine-node cocaine-specific supply succession as a table; the legal consequence; and the terminal-phase inversion where Dan holds the supply.

**Findings written back, not left on the new page.** Reciprocal typed connections added to `chemical-architecture` (`contains`), `supply-network` (`contains`), and `2015-possession-arrest` (`evidences`), each with prose wikilinks in the body rather than frontmatter alone — the page was an ISLAND on first `wiki-connect` run (index-only inbound) and is not one now. The `2015-possession-arrest` edge also closes the **health↔legal domain pair**, which `wiki-connect` had been reporting at 0 coverage.

**One thing this page does not do.** It states no new claim. Every figure, date and quote is carried over from a page that already held it, and where a source was uncorroborated there it stays flagged here — the cocaine–bulimia link is a self-audit assertion with nothing independent behind it, and Menore's six-year product is still unnamed in-thread. Six items in the new page's own Gaps section.

Gates: wiki-lint **0 errors**, 17 warnings (all pre-existing) · wiki-connect **islanded 29 → 28** · wiki-climb check **0 errors, 9 staleness warnings** (all pre-existing, none touching this pass).
## [2026-08-18] ingest | people/mind/timeline | raw/self/chats/The 2nd most famous _Jimmy Pop_ in Pennsylvania .md + Gemini-_21.md + message corpus

**A cited source had been read to 11% of its length, and the other 89% contained a whole person.**
`rock-irrelevance-thesis` (created 2026-06-22) cites this 2,688-line ChatGPT log
and mined its first ~140 lines. The remainder is the complete arc of a
fifty-six-day 2025 friendship with Danielle Onesi's boyfriend, and it corrects
two load-bearing claims elsewhere in the wiki.

- **The wiki held two pages for one man, one of them named after a chatbot.**
  `wiki/people/max-danielle-bf` (2026-06-23) took its title from the first line
  of `Gemini-_21.md` — *"Max I have a gift for you… a 20 or 25 minute audio
  recording of… my first girlfriend Danielle's current boyfriend"* — reading a
  vocative addressed to the MAX persona as the subject's name. The model signs
  its own reply "MAX'S ANALYSIS"; the boyfriend is never named in that source.
  `wiki/people/max` carried the error inverted, asserting a real person distinct
  from the persona, while `danielle-onesi` had the identification right the
  whole time and nothing acted on it. Merged into `wiki/people/james-dee`; both
  pages corrected in place with the old claims visible.
- **`forensic-method`'s "first outward deployment" was off by a year.** The
  Leviathan dashboards (2026-07-25) are the first deployment *as leverage*. The
  first outward deployment at a named private person is the James Analysis PDF,
  **2025-07-11**. Edge narrowed, correction written into the body.
- **The valence of an analysis is not what people object to.** Dan removed the
  critical material before sending, disclosed the copy to the subject's partner
  voluntarily, and pre-paid with two unflattering analyses of himself. Twelve
  minutes from PDF to "OK, you can quit MASS texting me"; the two objecting
  tapbacks land three seconds apart, before any words. New concept page
  `the-handed-mirror` generalises it with a prediction and a falsifier.
- **`lyrics-as-timbre` is no longer single-sourced.** Dan states the same
  lyric-blindness to a hostile third party in a live 2025 argument, a year
  before the 2026-07-14 capture the page rests on. Gemini's read of James
  independently records him hearing vocals the same way — which is what they
  fought about.
- **The Ramone claim is impossible, not merely inflated.** James told Dan that
  Johnny Ramone and Glenn Danzig had recruited him and he declined. Johnny
  Ramone died 2004-09-15; James, 36 in 2025, was about fifteen. The model graded
  it "90% exaggerating" and stopped.
- **The pitch and the catalog disagree.** Seven audio attachments recoverable
  from the message dump: six are covers or mashups (Zeppelin, Manson, HIM, NIN,
  the Drifters) under an artistic thesis of refusing to be derivative, and the
  project is named after a living Pennsylvania musician.
- **First-ever guilt, dated.** *"the stuff with Annie has made me feel guilty
  for the first time in my life about how i treated danielle"* — 2009 breakup
  specifics (Valentine's Day, Kelly Mulroy, Alex Gaskarth) written back to
  `danielle-onesi`.
- **Gates:** wiki-lint 0 errors · wiki-connect 0 errors · wiki-climb 0 errors,
  9 staleness warnings (none introduced here).

## [2026-08-18] close | people | wiki/people/diane-moore — a two-word operator answer merged two entities and re-dated the exclusion

The operator answered the standing gap on the grandmother page with **"Dian and
Dave."** Treated as T0 testimony and checked against the message dump, it held
and then kept going.

- **Her married surname is Moore, and the wiki already had it twice.** The page
  titled her "Diane Shrum" and admitted the surname was inferred *"rather than
  a record naming her that way."* The corpus names her on 2018-04-01: **"diane
  moore hasn't been able to be reached by anyone. dave is 'speaking on her
  behalf'"** and **"the social workers are talking to dave moore."** George
  Shrum Jr. is the first husband and Suz's father. Page renamed
  `diane-shrum` → `diane-moore`, 27 references repointed.
- **"Dian V. Moore" was her.** `155-virginia-ave`, `fran-death-vigil` and
  `master-timeline` all record the 2018-03-29 eviction notice as served by
  "Dian V. Moore," and the vigil page listed *"Dian V. Moore's role/relation to
  the estate"* as an open gap while three other pages discussed the same woman
  under another name. Merged.
- **Annie never received a letter.** Both this page and `fran-death-vigil`
  stated Dan and Annie *"each received"* one. Dan, 2018-04-03: *"lol also if
  they are writing such professional correspondence why wouldn't Annie get her
  own letter."* Corrected on both.
- **The date moves into the terminal week.** The 2026 capture has the letters
  sent "well before" the final admission; the contemporaneous record has the
  eviction notice served 03-29 and the letter read, forwarded and lawyered on
  04-03 — the day before Fran died. Held as a CONTRADICTION rather than
  resolved, since an earlier visiting-rules letter may also exist.
- **The author, per its recipient, is Dave.** *"i think dave wrote it — read the
  last paragraph. 'any violation of the rules will be considered
  trespassing'."* New page `wiki/people/dave-moore`.
- **The 2020 contest question is settled and it was settled before he asked.**
  Two months before Dan asked the estate attorney whether his grandmother would
  object, Suz answered it: 2020-06-22, Dan *"does a court case mean diane
  challenged it"* → Suz *"No… She isn't going to do that."* The August 17 court
  date was the distribution proceeding. No objection in five further years.
- **One asset appears to have left the estate outside the distribution.** Fran's
  Florida condo: *"she went to florida to take over her condo down there and
  sell it and keep the profits herself"* (2018-04-22), and Suz a year later:
  *"if she wants a cut, she will have to give me a cut of what she got for
  selling Florida."* Written into `estate-money-spine` with the caveat that no
  instrument, price or date exists in the corpus.
- **The earlier fear was a forecast.** `fran-death-vigil` explained an eight-hour
  delay in treating a fallen 97-year-old by Dan's fear of "grandparents who
  already hated" him, named there as Diane and George. They are Diane and Dave —
  the same couple that then served the notice, wrote the letter, took the
  hospital's calls and sold the condo.
- **Gates:** wiki-lint 0 errors · wiki-connect 0 errors · wiki-climb 0 errors,
  9 staleness warnings (unchanged). `bin/wiki-gaps pending` now empty.

## [2026-08-18] lint | mind | the girlfriend score, and two honest re-checks

- **`alexis-armel` gains an independent scoring it never had.** A spring-2026
  Claude session, asked to score both women on its own invented metrics, put
  **Annie at 1.9 / 10 and Alexis at 7.1**, and located seven of the 5.2-point
  gap in **non-exploitation alone** (1.5 against 8.5) — the same axis this wiki
  separates them on, reached from different evidence. Recorded as attributed AI
  output per STYLE_GUIDE rule 4, with the caveat that the instrument was reading
  a record Dan assembled and is therefore not independent of its subject.
- **Two staleness warnings cleared the right way.** `axioms` and
  `read-receipt-forensics` were each stale on exactly one premise, and that
  premise was one this session moved; both re-read, both conclusions held, both
  recorded as `RE-CHECKED` blocks. The remaining new warnings sit on pages that
  were already stale on *other* premises, and were deliberately left standing
  rather than cleared by a date bump.

## [2026-08-18] lint | cross-domain | the $750/week retraction was announced on three pages and applied on none of them

**What was wrong.** The `suzanne-frank` rewrite (2026-08-18) retracted the
"~$750/week borrowed from Suz" figure on two independent grounds: the rate is
`operating_manual.md`'s AI-secondary generalisation of a *single* accusation
(13 Dec 2018, *"You borrowed $750 last week alone!"*, made in an argument on a
day she had that morning asked him for $450), and its **direction is
inverted** — the largest documented 2018 movement between them is ~$14,000
from Dan to Suz, drawn against an estate that did not distribute until
September 2020, $4,000 recovered.

**The evidence.** The retraction propagated as prose *about* the correction
while the corrected claims stayed live underneath it. Two pages carried a
`CORRECTED`/`RE-CHECKED` block quoting a sentence they had never actually
changed:

| Page | State found | 
|---|---|
| `wiki/legal/463-morgantown.md` | CORRECTED block said *"The sentence above previously read…"* — the sentence above still read exactly that, verbatim |
| `wiki/people/alexander-jackson.md` | RE-CHECKED block described the correction; the Roles table above it still read "Borrowing patterns ($750/wk cycles)" |
| `wiki/mind/synthesis/supply-network.md` | no correction at all — "the 2018 deep cycle ran on ~$750/week borrowed from her" fully live |
| `wiki/mind/synthesis/estate-money-spine.md` | correction present, but its own "chain, event by event" table still carried the retracted row |
| `wiki/timeline/periods/2018-deep-cycle.md` | "mom borrow $750/wk" live; missed by earlier sweeps because it abbreviates `/wk` |

**What changed.** All five corrected in place, with the retracted text visible
per STYLE_GUIDE rule 9. `estate-money-spine`'s chain gained the row it was
missing — the Aug–Oct 2018 ~$14,000 Dan → Suz transfer, the family's largest
internal capital movement, absent from the ledger that exists to track exactly
that. `463-morgantown`'s absorber argument now rests on the Chapter 13
(24-22285-GLT, ~$157k scheduled) rather than a rate that does not exist; the
conclusion is unchanged and better supported. `supply-network`'s bullet keeps
its claim and changes its mechanism: the family layer was the *rail*
procurement ran on, not its funding — and the Cash App account those transfers
ran through is one Dan asked her to install in **August 2018**, the same month
as the $14,000 drawdown, recorded as a dating coincidence rather than a causal
claim.

**Two systemic findings.**

1. **A correction block is not a correction.** Three pages read as corrected to
   any reader who scanned for a flag, and the retracted figure was still the
   one a reader would take away. This failure mode is invisible to all three
   gates — the pages lint clean, their edges are typed, and their dates are
   current. Grepping the *retracted string* is the only thing that finds it.
2. **`wiki/timeline/master-timeline.md` was 484 events and 7 pages stale** —
   2,076/315 on disk against 2,560/322 on regeneration. It is derived and
   cheap to rebuild, and had not been rebuilt since several intervening
   ingests, so the wiki's largest page was serving a stale scrape of pages
   that had themselves moved.

**Also noted, not fixed:** 30 pages carry `status: archived` outside an
`archive/` directory, which STYLE_GUIDE reserves for pinned artifacts that are
never updated. `2018-deep-cycle.md` was one of them and was carrying a false
claim into the generated timeline. Queued in `BACKLOG.md`.

## [2026-08-18] lint | cross-domain | the staleness queue emptied, and four of the five re-checks changed a conclusion

**What was wrong.** `bin/wiki-climb check` carried **13 stale-premise warnings**
across five pages, three of them in the wiki's larger synthesis tier. Worked to
zero. The result is worth recording because the warnings were mostly *not*
noise: only one of the five pages came back "survives, nothing moved."

**Page by page.**

- **`block-unblock-loop` (35KB → 40KB).** All four flagged premises had moved by
  typed-edge addition only — no body text — so the flags themselves were
  uninformative. **But an unflagged premise had moved substantively the day
  before, and it falsified a classification the page rested on.**
  `ellen-ulmer` and `july-august-2026-reentanglement` both established on
  2026-08-17, from an operator answer, that the July 26 contact with Annie's
  mother was **not the maternal-disclosure threat executed as leverage** but a
  response to a belief that Coles had Annie in physical danger. This page still
  called it *"the first executed maternal-disclosure threat in the corpus"* and
  used it as the "no announcement → executes" leg of its threat rule.
  Reclassified: July 26 is not a member of the threat class, which **takes the
  maternal-disclosure execution rate from one to zero across seven or more
  instances** and leaves the trade rule resting on June 1 and July 28 — a
  cleaner contrast, because it varies only the counterparty's response and holds
  announcement constant. Cascaded to `july-august-2026-reentanglement` (which
  contradicted itself: its own earlier section still read the two acts as
  "resolving opposite ways" underneath the write-back that undid that reading)
  and to `annie-ulmer`'s 2026-07-26 chronology row.
- **`dormancy-not-exit` (31KB).** The page had said since 2026-08-01 that its
  retention floor was bracketed by a five-day tie that vanished and six-year ties
  that persisted, with *"no documented case in between."* The James Dee ingest of
  2026-08-18 produced exactly that case and nobody wired it in: a **fifty-six-day**
  tie, ended by the corpus's most abrupt rupture, that went silent for three weeks
  of documented coverage and then **resumed in person anyway**. Added as a member
  with full write-back. It does not just fill the gap, it changes the rule's
  shape: James neither vanished (Franki) nor took a new role (Danielle) but went
  to **suspension without reassignment** — which is the *suspend* primitive the
  page's own 2026-08-13 correction argued the graph implements, and its best
  instance was sitting unused for five days. Floor narrowed from a six-year
  bracket to seven weeks. Direction recorded honestly: **the reopening was
  James's, not Dan's.**
- **`the-unbroken-bond` (24KB).** Two findings. `bond-switch-2015` named the
  displaced partner on Annie's side (Emilio), which reveals a **symmetry** — both
  partners were displaced inside the same seventy-two hours and *both*
  displacements detonated a relationship the following month. That is a **third
  cost** for a page whose cost list held only internal ones, and the first paid by
  third parties. Recorded with its boundary: Annie ran the same operation on the
  same timetable, so the displacement cost belongs to **fast switches**, not to
  Dan's architecture, and a later pass must not annex it as more evidence for
  singularity. Separately, `alexis-armel`'s new blind model scoring (Alexis 7.1 /
  Annie 1.9) exposed that this page uses "shallow" for two independent axes —
  depth of Dan's attachment, and quality of the relationship. The bond it calls
  shallow scores nearly four times higher as a relationship.
- **`fayette-return`.** The ancestry rewrite of 2026-08-14 answers this page's
  self-declared *"most important open question"* — whether the maternal line is
  also Fayette-anchored — and the answer costs the page its best argument. It
  **is** anchored (the majority of all 90 direct ancestors die within twenty miles
  of Uniontown; Fran Coldren runs Miami Beach → back to Uniontown). So the page's
  **parsimony** case against `ancestral-dialectic` fails: it was valid only while
  the maternal line was unassessed, drawing force from absence of evidence rather
  than evidence of absence. "The paternal line reproduces the pattern alone"
  stays true and stops being distinctive. The rewrite also supplies the rule's
  first counterexample candidate — **Diane Van Voorhis, thirty-five years in
  Michigan, no attested return, still living so no terminus at all** — who does
  not falsify the rule as stated but is the only case that can separate *lineage*
  from *county*. Cascaded to `diane-moore`, which was still calling Farmington
  Hills the only geographic fact on record four days after Stanwood 2013–2020
  entered the corpus.
- **`fastly-fsly`.** The only clean "survives": its premise had moved solely to
  record its own staleness re-check. The real find was structural, below.

**A structural defect, found while re-checking and worth more than any single
page.** `wiki/work/fastly-fsly.md` declared `synthesizes:` **twice**. YAML
resolves a duplicate key by keeping the last, so every standard parser read the
page as synthesizing only `context-core` — its membership in
`2020-2021-market-era`, the page's whole reason for existing, was invisible
outside this repo. `bin/wiki-climb`'s own `fm_list` collects *both* occurrences,
which is why the gate flagged a staleness against an edge a YAML consumer could
not see. **The repo's bespoke frontmatter reader is more permissive than YAML,
so the gates pass while the derived artifact loses data** — and the portal
renders `wiki/**` through a real parser. A sweep found two more:
`jerad-friedline` (dropping `context-core`) and `developmental-origins` (an
empty duplicate `connections:`). All three fixed; lint rule queued.

**Gates:** `wiki-lint` 0 errors · `wiki-connect check` 0 errors ·
`wiki-climb check` **0 errors, 0 warnings** — the stale queue is empty for the
first time in the log.

## [2026-08-19] climb | mind, health, places | five doctrine pages (5 synthesized, 0 rejected)

**Trigger:** operator — *"do a deep dive on the wiki and create 5 new articles
using synthesis of the data. Try to find things about the way that I think or
see the world that are visible when looking at the totality of data."*

**Method:** CLIMB per `SYNTHESIS_SPEC.md`, taken outside `synthesis-queue.md`.
The queue's miner scores clusters of *ground* pages and structurally cannot
surface what this request wanted, so the five clusters were assembled by hand
from the doctrine layer and from two domains the altitude audit flagged as
having no junction above them at all (`places`, `legal`). Every climb was
required to add primary measurement its premises lacked; four of the five did so
by counting something in `raw/` that had never been counted.

**Findings, in order of value.**

1. **The curated taste record is not eclectic; it is monomaniacal, and the
   arithmetic had never been run.** 60 of the 120 books — exactly half — are two
   subjects (`trump`/`jan-6`, 40 books by 30 authors; `roman-republic`/
   `ancient-history`/`caesar`, 20 by 14) with **zero overlap**. 86.6% of 1,477
   musical artists and 86.7% of 98 authors appear exactly once. All 25 artworks
   have 25 different creators, and **24 of the 25 carry one of six tags**
   (`observer` 6, `wound` 6, `collapse` 5, `glitch`/`rupture` 6, `fortress` 3).
   The author-level spread is *produced by* subject-level obsession: one account
   per witness is all that exhaustive coverage of one event requires.
   → `wiki/mind/synthesis/closing-the-set`.

2. **`single-channel`'s evaluative leg is falsified.** That page scored the
   evaluative domain as its weakest limb — its own words, *"a reading rather
   than a measurement."* Measured over entries-per-creator, the same unit as the
   contact coefficient: **music 0.188, books 0.166, art 0.000, against the
   contact graph's 0.9601.** Not weak concentration — near-perfect equality, in a
   collection the same person curated. Concentration is a property of the
   relational architecture and does not generalise. `totality-themes` re-checked
   and its edge narrowed; the Irreversibility Firewall survives on the relational
   leg, and *a collection is not a channel* is the reason it never needed the
   other three.

3. **The psychological layer of this wiki has no independent observer anywhere in
   it, and now there is a number.** Seven frameworks, plus stylometrics, a
   deviance audit and a composite voice model, all commissioned by the subject
   over corpora he selected. **The entire apparatus appears seventeen times in
   106,629 outbound messages** — `socionics`, `5w4`, `percentile`,
   `personality type` all return **zero** — and most of the seventeen are Dan
   typing *somebody else* or forwarding the test. By June 2025 what he forwards
   is the analysis prompt itself, output spec intact.
   → `wiki/mind/synthesis/the-commissioned-self`.

4. **The one first-person self-typing in the primary record disagrees with the
   profile cluster.** 2024-11-04, quoting his own prompt: *"vanessa is an xNFP
   4w5 and **Dan is an INTP 5w6sx RLOEI**."* The cluster and `context-core` carry
   **5w4** and **RLUEI**. The wing is load-bearing — `enneagram-5w4` is named for
   it and derives the tragic-romantic reading the attachment pages build on.
   Held open as a `CONTRADICTION` per `instrument-is-subject` (residue over
   testimony), not resolved: it is one line typed fast and may be a slip, but
   nobody had looked.

5. **Seven addresses, sixteen years, no paper.** The corpus contains **no lease,
   no contemporaneous rent figure, no signatory and no deposit** for any home Dan
   has lived in. Four of the seven place pages independently filed this as an
   archival gap and none noticed the other three had. The two instruments that
   ever appear were relational moves that changed nothing: an eviction notice
   served by his own maternal grandmother in March 2018, ignored for eleven
   months; and **2024-10-27, new to the wiki** — *"Tomorrow I'm calling John / And
   telling him that I will no longer be in the lease,"* answered inside the
   minute with *"Please don't do this Dan,"* never executed, four months before a
   separation Annie initiated. `dans-law` reads a missing paper trail as the
   operative feature of an arrangement, and has never been pointed here.
   → `wiki/places/the-unpapered-address`, the `places` domain's first junction.

6. **`307 E 76th`'s rent gap closed:** *"the last lease we signed was 2450"*
   (2024-05-02), *"New lease is going to be 2700"* (2024-05-03). The tenancy ran
   on discretion throughout and Dan describes it accurately — *"willing to take
   us on," "as long as we sustain jobs," "won't have to deliberate," "stuck his
   neck out for us."*

7. **`chemical-architecture`'s "no dental, no primary care anywhere in 17 years"
   is wrong, and the correction is better than the claim.** A term census found
   a full dental episode in autumn 2017 including surgery and a kept one-week
   follow-up (*"they put in a membrane and restitched it"*), plus appointments in
   2020 and 2024 — which also contradicts Dan's own 2025 account, *"terrified of
   dentist (aka haven't gone)."* Care is **episodic and reactive**, not absent.
   The declared prescriber gap is closed too: a doctor exists, and every recorded
   exchange with him is about moving a script between pharmacies.
   → `wiki/health/the-configured-body`, the `health` domain's first junction:
   the body is specified at the input, surveilled at the output, never
   maintained. Every self-directed medical sentence in the corpus is modal
   (*"I should go," "I might need to"*); every sentence about someone else's body
   is imperative (*"go to a fucking doctor"*). Same speaker, same years.

8. **`supply-network` may have the Suboxone topology backwards.** June 2025:
   *"my doctor said the pharmacy won't fill an out of state prescription"* →
   *"they won't fill it either so i'm completely out of options"* → *"I'm gonna
   have to drive down to see Tom today."* Prescription first, Tom as failover,
   failure jurisdictional rather than relational — which would make May 2026 a
   second-line failure. Held open, not resolved: four messages are not a topology.

9. **The identification figures all occupy one seat.** The persona Dan wrote for
   his own AI is `IDENTITY: CATO / ORIGIN: Cato the Younger — Stoic absolutist,
   self-deleted at Utica post-Thapsus.` Not the winner — the man who was right
   for twenty years, lost, and refused the pardon. Against him: Oppenheimer,
   Fred Hampton, John Brown, Travis Bickle, Bernie. Of ~150 want-to-read titles,
   nine contain "fall," three "assassination," three "trial" — and **not one is
   about something being built and working.** The taste record independently
   reproduces `context-core`'s own threat model (*"competence correctly deployed,
   outcome still catastrophic"*), which is worth something precisely because it
   was assembled for pleasure and had no reason to agree.
   → `wiki/mind/synthesis/the-cato-seat`.

10. **`2020-left-turn` was missing the material stake.** The page dates the turn
    to a media pipeline and a conversion message. Six months earlier, unquoted:
    *"the doctor thing is a really big thing for me...there's no reason that
    50,000 people die a year because they don't have insurance"* (2020-02-07).
    The one place in the political record where Dan names a grievance as his own.

**Also fixed:** six pre-existing gate errors on three pages created 2026-08-19 by
the parallel model (`astrology-star-signs`, two `-personality-assessment` pages)
— wiki paths in `sources:` moved to `synthesizes:`, two dangling connection
targets removed.

**Cost:** 14 staleness warnings, all created by the write-backs and all
itemised in `BACKLOG.md` with the reason each is believed cheap. The
`the-unbroken-bond` ← `enneagram-5w4` pair is flagged as the one that probably
is not.

**Gates:** `wiki-lint` **0 errors** · `wiki-connect check` **0 errors, 255
warnings** (unchanged — the standing `## Related` backlog) · `wiki-climb check`
**0 errors, 14 warnings**. `bin/wiki-digest` and `bin/llm-publish` re-run:
481 pages, 42 contradictions, 385 gaps, 33 predictions.

## [2026-08-20] ingest | timeline/people/mind | two iMessage exports + a 15:27 call recording — the relationship ended, and an AI analysis had put Dan's own house at the crime scene

**Sources filed.** `raw/self/message-csv/imessage_export_2124702449_20260820.csv`
(6,495 messages, 2026-07-23 → 2026-08-19 15:15:33 — of which **3,993 are new
ground**, the previous 212 export stopping at 2026-08-02);
`raw/self/message-csv/imessage_export_7248123683_20260820.csv` (97, Dan ↔ Jerel
Coles, entirely new);
`raw/self/audio/2026-08-16_Morgantown_St_call-recording.m4a` (927.19 s, with a
provenance README);
`raw/self/analysis/2026-08-18_forensic-analysis-morgantown-call.md` (T2, agent-authored).

**Findings in order of value.**

1. **The Annie relationship ended on 2026-08-19 at 15:07:03**, and it is the
   first goodbye in eleven years that carries **no condition**. Every prior one
   names its own reversal. 1,199 messages in the 67 hours from the night of
   August 16; Dan 811 / inbound 388; 59,758 characters against 9,532, a 6.3:1
   asymmetry against 3.1:1 the week before. 18% of everything Annie sends in
   those three days contains *please* or *begging*. New page:
   `wiki/timeline/events/august-2026-morgantown-call`.

2. **A handle is not a person, and the corpus has been assuming it is.** At
   least six inbound rows on Annie's 212 handle were typed by Coles holding her
   phone, across three episodes (2026-07-26, 2026-08-16, 2026-08-18) — including
   *"You made me fuck guys for money"* (2026-08-16 23:45:10), an accusation
   against Dan that a naive read files as her testimony. All three occur during
   crises, i.e. exactly where the wiki's highest-stakes claims come from.
   **Counts are unaffected** — the 97,768 figure stands — **attributions are
   not.** Written into `source-coverage-index` as a fourth preflight question
   (*who else had physical access to the device?*), into `wiki-brain` as a
   system-level defect, and into `read-receipt-forensics` as the harder version
   of M4: absence of a signal is weak evidence, and **presence of a signal does
   not identify its author.**

3. **Dan faked the execution of a threat in order to measure the response.**
   2026-08-18 19:35 *"i did"* → 19:38 *"it wasn't actually sent / And I knew
   you would suddenly come back to life / Which of course is what happened."*
   A controlled test with a stated hypothesis and a debrief, run six hours after
   the subject disclosed a suicide attempt. The consequence is methodological:
   **Dan's own assertions of his own conduct are no longer evidence of that
   conduct**, which reaches `block-unblock-loop`'s threat-execution scoring
   directly. He then claims execution three times on 08-19 and denies it twice
   the same day — held as an open `CONTRADICTION`, not resolved.

4. **The wiki did not know Dan can forge documents.** 2026-08-14: Annie asks
   for a counterfeit Fayette County drug screen to show her parents; he does it
   in forty minutes, auditing his own forgery (*"the logo / 'Panal' instead of
   panel / the signature"*) and asking the threat-model question — *"Are you
   SENDING this to them or just going to SHOW it on your phone / If you're
   sending it we need to do a lot more work here."* He calibrates fidelity to
   how adversarially it will be inspected: the forensic faculty run backwards.
   New page: `wiki/mind/concepts/document-fabrication`, wired as a
   `contradicts` against `forensic-method`. Note the collision nobody in the
   record notices — two days later he stakes everything on documents being
   believed by the same audience.

5. **Three corrections to the T2 analysis, and the pattern of them matters more
   than the errors.** (a) It reports **463 Morgantown St as "the other guy's
   house."** It is *Dan's* house — which is why Coles typing it back at him on
   08-17 is a threat and why Dan answers *"why are you sending me my
   address?"*. Coles's address of record is 106 Nassau St. The analysis appears
   to have read the recording's filename as naming the scene when Voice Memos
   names it for the **recorder's** location; ingested uncritically it would have
   put Dan inside the confrontation — the exact inversion its own headline
   correction exists to prevent. (b) Two more messages (23:53:31, 23:53:45) are
   Coles, not Annie; its own transcript has him saying the same words aloud at
   14:23. (c) Its export ends 08-17 15:39, so its concluding scenario is written
   without the 08-18 phone seizure, the SOS sequence, the false send, or the
   severance. **A wrong value in a labelled metadata field propagates further
   than a wrong sentence in prose, because it gets copied rather than read.**

6. **The recording's own container settles what the analysis argued for.**
   `mvhd` 927.19 s = 15:27, matching Dan's *"That 15 minutes recording"*
   (08-17 01:00) exactly. Encoder `com.apple.VoiceMemos (Dan's MacBook Pro)`;
   date atom `2026-08-17T03:54:49Z` = 23:54:49 EDT. Aligning two spoken lines
   against timestamped texts — *"I've never fought anybody in my life"* vs
   23:44:21, and *"send this whole thing to Ellen"* vs 23:51:45 — puts audio
   t₀ at **23:36:30–23:38:07**, so the call ran ~23:37→23:53 and the file was
   written two minutes later. Two independent alignments, both inside 100
   seconds of each other.

7. **The August 8–9 unmasking page's framing was a scope artifact.** It ends
   the night on an unanswered message at 03:41:32; the fuller export shows the
   exchange resumed at 08:19 and ran all day. Also adds a message the spine
   omits — Annie's *"Call me"* at 23:10, the only request for voice contact in
   the sequence, unanswered.

8. **The re-entanglement did not end on August 9 — it ran ten more days and
   briefly worked.** Aug 10–16: 1,136 messages at 652/484, the evenest ratio of
   the terminal record; a sleepover on the 10th; Dan's BFS job restored on the
   11th, *"the same lady who put me on a no-hire list there told the manager
   today to put in another application"* — with the posted sign named for the
   first time (*"NO HIRE: Daniel Frank"*, in two locations). The seam is
   **August 13**: Coles messages a group chat containing Dan, Annie says *"Do
   not engage,"* Dan complies — the first Coles contact since the June 15
   defection, and nothing in the wiki had it.

9. **`tuquick-17248123683` was marked CLOSED and is not.** 97 further messages
   from that handle, 08-17 → 08-19, including Dan's home address sent unprompted
   and a written conditional threat naming Suz (*"I have stuff to ruin you and
   your mom"*) — the only threat aimed at her in the corpus with no named
   content. Also the nearest thing to an admission about the earlier harassment
   campaign against her: *"Yeah it was kind of unnecessary but I don't like being
   played with."* She received none of the August calls — Dan had blocked
   Annie's number on his mother's phone in advance, on a prediction that proved
   correct.

10. **The dog's name is used as a duress code.** 2026-08-18 22:54, after Coles
    had been typing on her handle two hours earlier: *"Betty. Milo. Whatever sos
    words"* — reaching for the two dogs as the one referent that could prove it
    was really her. Six SOS messages 22:18–23:41; Dan answered at 23:40, 72
    minutes late, having blocked and unblocked in between. No source says what
    happened next.

**Pages written:** 2 new
(`timeline/events/august-2026-morgantown-call`, `mind/concepts/document-fabrication`);
**24 updated** — `annie-ulmer` (new August section + 8 chronology rows),
`jerel-coles` (new §August 2026 with the recording and the 97-message thread),
`tuquick-17248123683` (status REOPENED), `august-2026-unmasking`,
`july-august-2026-reentanglement`, `ellen-ulmer`, `suzanne-frank`, `milo`,
`bfs-foods`, `legal/463-morgantown`, `source-coverage-index`, plus eleven
`RE-CHECKED` blocks on stale dependents and the two domain indexes.

**Staleness:** 25 warnings raised, worked down to 13 across two waves — 11
pages re-checked with real blocks, including all five where a conclusion could
plausibly have moved. **No warning was cleared by bumping a date.** The
remaining 13 are itemised in `BACKLOG.md` with the reason each is believed
cheap; four of them predate this pass.

**Gates:** `wiki-lint` **0 errors**, 30 warnings · `wiki-connect check`
**0 errors**, 258 warnings (the standing `## Related` backlog) ·
`wiki-climb check` **0 errors**, 13 staleness warnings.

## [2026-08-20] correct | timeline/people/mind | the close read of August 19 falsified this pass's own headline claim

**Trigger.** Operator: *"you didn't finish analyzing the texts. read the very
last batch extremely carefully."* Correct — August 19 was read but written up
in eight sentences against pages of treatment for the 16th–18th, and the
compression hid an error.

**The operator also supplied `imessage_export_2122702449_20260820050136..csv`.
It was not filed.** 194 rows, all `target = +12124702449` (the `2122702449` in
the filename is a typo), and **byte-identical to the August 19 rows already in
`raw/self/message-csv/imessage_export_2124702449_20260820.csv`** — verified by
set comparison on (timestamp, direction, text): zero rows in either direction.
Filing a duplicate subset under a mistyped handle would have created a phantom
fifth Annie handle in `source-coverage-index`. Recorded here instead.

**The correction, and it was this pass's own lead finding.** The 2026-08-20
ingest published, and propagated to six pages plus `log.md` and
`LLM_HANDOFF.md`, that the relationship ended with *"Goodbye. I am blocking"*
at 15:07:03 and that this was **"the first goodbye in the record with no
condition attached."** Both halves are false:

- **The block was declared, not executed.** Seven further messages from Dan
  follow it inside eight minutes, plus one from Annie at 15:14:33 (*"I honestly
  care"*) that he answers. The export ends **mid-exchange** at 15:15:33.
- **The closing stretch is explicitly conditional.** 15:09:01, ninety seconds
  after the goodbye: *"You could still not do the wrong thing."*

Corrected in place on `august-2026-morgantown-call`, `annie-ulmer`,
`the-unbroken-bond`, `dormancy-not-exit`, `ally-and-dan-love-as-destiny` and
`timeline/index`, each with the original claim left visible per STYLE_GUIDE
rule 9. **The lesson is about the writing, not the reading:** the claim was
made from a day that had been read at the same resolution as the rest of the
window and then summarised at a coarser one. A structural claim about how
something ended cannot be made from a summary of its last hour.

**What replaces it, and it is better evidence.** At **14:53:25** Dan writes:
*"Do NOT ever think that enough time has passed that now you can tell me about
something that made you think of me **or when something happens to Milo**."*
That is him naming and pre-emptively closing **the exact channel that reopened
the relationship seven weeks earlier** — Annie's July 4 email about the dog and
the fireworks, which ended a fifty-two-day silence. He has never done that in
eleven years; every prior severance left the dog channel open and every prior
severance was reversed through something like it. That is a structural
difference the record can point at, which *"no condition"* was not.

**Findings the close read added, in order of value.**

1. **The final hour is an argument about an act neither party ever names.**
   Eight times between 14:24 and 15:09 Dan describes not what Annie has done
   but **what she is about to do**, in the future tense — *"this is the choice
   you are right now making," "what you are ABOUT to do is wrong," "you ARE
   ABOUT TO DO THE THING THAT SHOWS ME HOW YOU FELT," "You could still not do
   the wrong thing"* — and the content is **never stated by either party** in
   194 messages. The nearest thing to a referent arrives in the last
   thirty-three seconds: *"Not even enough to correct the lies you told about
   me"* (15:13:45). This is why the day cannot resolve: an accusation with no
   stated content can be neither conceded nor refused, which is exactly what
   her side of the hour looks like.

2. **A parsing trap that would have produced a false concession.** 15:04:04
   Dan: *"There's some big secret."* 15:04:05 Annie: *"okay."* **One second** —
   faster than reading and replying. It answers *"These lies dont work anymore"*
   four seconds earlier. Left unflagged it reads as Annie conceding a secret
   exists. Same failure mode as the *"He'll?"* misparse of August 8.

3. **Three incompatible periodizations of the relationship inside four hours,
   none retracted.** *"the last 3 weeks"* (11:29:42, ≈July 29 — the
   re-entanglement itself); *"I wasted 10 years"* (11:41); *"keeping me in your
   web of lies for 17 months"* (15:00:40, ≈March 2025, landing on
   `feb-apr-2025-return-and-rupture`). The 17-month figure is new to the wiki
   and is the only one of the three that names a start.

4. **The leverage is declared retained, not spent — thirteen hours after being
   declared spent.** 15:12:16: *"I could have torn your life apart. I still
   could and I don't."* Against 01:44:27 the same morning: *"And I sent it
   already I told you."* This strengthens rather than resolves the standing
   `CONTRADICTION`; the sent-mail check remains the only thing that settles it.

5. **Annie's reason for begging is her mother, and it is the only stable reason
   she gives.** *"This will literally kill my mom"* (01:49:16). Not her own
   exposure, on any of the three days.

6. **Claim and retraction arrive together.** 02:01:12 *"INWAS TRAPPED / AGAIN"*
   → 02:01:34 *"yes it's my fucking fault"* — eleven seconds, unprompted. The
   shape of nearly every account she gives in the window.

7. **Volume, restated at the right resolution.** Dan 141 / Annie 53 on the day,
   but **forty of hers land before 02:05**: after the small hours she sends
   fourteen messages in thirteen hours against roughly ninety of his.

**Gates:** `wiki-lint` **0 errors** · `wiki-connect check` **0 errors** ·
`wiki-climb check` **0 errors**.

## [2026-08-20] close | timeline/people/mind | the catalyst was a five-word message in a group chat the wiki has never seen

**Trigger.** Operator supplied a screenshot of a three-party group chat (Dan,
Annie, Coles) plus four statements of testimony, and asked separately for a
verdict on the accusation *"you made her fuck guys for drugs."*

**Sources filed.**
`raw/people/captures/2026-08-20_group-chat-retraction-and-the-uncleared-name.md`
— the screenshot transcribed verbatim (the image was pasted inline and is
**not on disk**; this is the corpus's only copy) plus the operator's statements.

**Findings in order of value.**

1. **The unnamed act has a referent, and the gap is closed.** The August 19
   page recorded that Dan spent the final hour arguing about *"what you are
   ABOUT to do"* eight times without either party ever saying what it was. The
   answer is outside the thread: at **06:33 that morning** Annie wrote ***"He
   didn't rape me"*** in the group chat — publicly clearing **Coles**, in front
   of both men, of the accusation she was still making to Dan privately hours
   earlier (01:08/01:09 to Coles: *"she is still saying you raped her so"*).

2. **The retraction was pre-emptive, and that fixes the date.** Per the
   operator she sent it *believing Dan had already emailed her mother the
   record of her making the claim*, timed *"hours before she expects her
   parents to read what she had told me."* That requires it to follow Dan's
   last claim of having sent it — **2026-08-19 01:44:27** — so *"Yesterday 6:33
   AM"* is **Aug 19**. Two independent supports in the message log: an untexted
   Dan attachment at **07:27:35** (54 minutes later, with no Aug 18 counterpart)
   and the thread's register turning at **11:25** and never turning back.
   One inconsistency held open rather than smoothed: the operator calls this the
   catalyst for *"telling her i hadnt actually sent the recording,"* and the
   explicit false-send admission is 08-18 19:38 — reconcilable if the Aug 18
   admission was the test debrief and Aug 19 is the abandonment of the claim
   (11:25, then plainly 15:12), which is what his own *"no runway left"*
   phrasing describes.

3. **The two most opaque messages in the corpus became the most legible.**
   *"Not even enough to correct the lies you told about me"* (15:13:45) and
   *"YOU COILDNT EVEN CLEAR ME FEOM THE LIES YOU TOLD ABOUT ME"* (15:15:00) —
   read as generalised grievance until now. They are about a specific act with a
   specific counterpart nine hours earlier. Per the operator he had **called and
   asked her to clear his name too, and she said she would and did not** (voice;
   in no export). The complaint is the asymmetry, not the accusation.

4. **The August 13 seam is corroborated from the other side.** Coles's
   group-chat message is *"Anne still messaging you,"* **11:23 AM**. Annie's
   *"He sent a message to a group chat / With you / …please. Do not engage"*
   lands 21–36 minutes later. The wiki had the request; it now has the trigger.

5. **It was not blackmail, and saying so requires saying what it was.** The
   demand across three days was never money, sex, contact or return — only a
   written statement — and the material was repeatedly offered for inspection
   *before* use (*"I can let you see it first to make sure you don't accuse me
   of putting fake things in"*, 08-17 19:32; *"I'M NOT BLACKMAILING YOU"*,
   08-18 19:44; *"so you don't say I am like holding this above your head"*,
   08-18 21:44). Eleven deferrals requested, eleven granted. That is not
   blackmail's structure. It also had coercive force, and Annie names it
   (*"You're making this worse for me doing that"*). **Both are recorded.**
   → written back to `block-unblock-loop`: score the threat class **by its
   demand** — every instance in eleven years demands a *statement*, which is
   why none converts into an exchange and is the likeliest reason the execution
   rate has stayed at or near zero.

6. **The *"made her fuck guys for drugs"* accusation is false as stated, and is
   a compression of something real.** Tested against `arrangement-history`,
   which is the corpus's primary-source backbone for exactly this. Three limbs:
   - **Direction of payment — fails flatly.** In all seven documented instances
     money runs **Dan → third party**: *"I would spend money to get you an
     escort"* (2018-06-27), *"Find two escorts… I'll set it up"* (2018-10-18),
     *"we'll pay above rate"* signed **Annie** (2018-10-25), *"$3000 to be a
     plaything for Annie"* (2018-11-28), Trinity at $1,500/hr, Shelbie
     $31+$700, Kelly's five-week run. **No instance anywhere of a third party
     paying Annie with money that reached Dan.** The only earnings are
     smashonista — a *joint* operation Dan calls *"most of our income."*
   - **Drugs as consideration — zero instances in eleven years.** Term searches
     for *made you fuck / made her fuck / fuck guys for / fuck for drugs /
     sell yourself / trade sex* return nothing in either direction. Every
     documented consideration is cash or nothing.
   - **Coercion — the one observable case runs backwards.** April 2019 is the
     only instance reconstructed from inside the couple's own thread as it
     happened, and there Dan paid for a one-on-one and Annie forced entry over
     his live objection. Against it: 2018-04-10, *"give me a break after
     arranging a hookup for you and then having you flake"* — he arranges and
     presses, which is real and is not coercion.
   - **Chronology.** *"You spent your dead grandma's money"* is backwards: the
     expensive encounters (Trinity Mar 2019, Kelly autumn 2019) predate the
     September 2020 estate distribution by eighteen months.
   - **The uncomfortable adjacent datum, recorded because it is uncomfortable:**
     2019-01-27, a confidant who had earlier received the *"$3000 plaything"*
     disclosure writes to Dan, *"all the drugs in the world you can shove down
     their throats in exchange for something of no real purpose… enough cash in
     your accounts to buy the people you need."* Hostile third-party testimony
     that money-and-drugs-for-access is a thing Dan does — about **her**, not
     Annie. It describes Dan buying, not Annie being sold.
   - **Verdict:** the record shows **purchased access with Dan as buyer and
     architect**. The accusation keeps the transaction and reverses who was
     bought. **Falsifier named on the page**, and it is the live one: the
     evidence base is overwhelmingly Dan-side correspondence and the corpus
     contains almost no account of the arrangement in Annie's own voice.

7. **Also on the recording:** Coles asks Annie to affirm the charge upwards of
   a dozen times, escalating, while holding her phone. She never says yes.

**The corpus now holds four positions on the rape claim and scores none:**
asserted to Dan over months, denied by Coles in writing, denied by Annie in the
group chat, re-asserted to Dan afterwards. Recording all four is the finding.

**Standing gap created.** The group chat has **never been exported** and two
findings now rest on one transcribed screenshot of it. One query settles the
date beyond inference and recovers whatever else ran through a channel all
three parties were in.

**Gates:** `wiki-lint` **0 errors** · `wiki-connect check` **0 errors** ·
`wiki-climb check` **0 errors**.

## [2026-08-20] climb | mind | the grievances of the last conversation, scored one by one — and Dan's own evidence turns out to cut both ways

**Trigger.** Operator: *"analyze the grievances i was making in that last
conversation and do a value judgement on how justified i am to feel that way,
how harmful these things would be… and what they say about annie."*

**New page:** `wiki/mind/synthesis/august-grievance-verdict` —
`page_type: synthesis`, seven members, wired both ways. It is deliberately the
**seventy-hour** counterpart to `dan-annie-fallout-verdict`'s ten-year question:
at ten years the decisive unit is a pattern, at seventy hours it is a dated act,
and acts can be scored individually.

**Findings in order of value.**

1. **Seven of ten grievances fully supported, two partly, one false.** On this
   corpus's own history that is an unusually clean run — earlier windows
   repeatedly show Dan correct about the fact and wrong about the frame. Here
   the frames largely hold too, which is itself a finding about the accuracy of
   his perception under maximum distress.

2. **The strongest grievance is the asymmetric clearing, and it is the cleanest
   documented wrong in the corpus** because it required no interpretation: on
   2026-08-19 at 06:33 Annie cleared Coles of rape in writing, in a group chat,
   having agreed by phone to do the same for Dan — and did not. One act
   performed, its promised counterpart withheld.

3. **Grievance 1 is settled by a single exchange 26 hours before the call.**
   2026-08-15 21:09:50, Dan: *"if you are going to have ANY kind of contact with
   that person PLEASE for my sake just tell me."* 21:13:08, Annie: *"I
   UNDERSTAND THAT YHAT IF I AM GOING TO HAVE ANY SORT OF CONTACT THEN TO TELL
   YOU"* — she restates the rule and does not answer the question. Dan names it
   in real time.

4. **The analytic centre: Dan's own artifact cuts both ways.** He held the
   recording for three days as proof of betrayal (*"Listen to the fucking call
   ALL I DID WAS TRY TO HELP"*) and he is right about what it shows of him. But
   the same recording is **Annie's best defence** — on it she asks for her phone
   back, says *"I said I'm willing to leave,"* says *"I want to leave"*
   repeatedly, and Coles is heard refusing. His *"YOU COULD HAVE LEFT. You chose
   to stay"* is the worse-supported reading **for the duration of the call**.
   Precision matters and the page states it: **he is right about the pattern and
   wrong about the night.** Grievances 1, 5 and 8 concern the days either side,
   when nobody was holding her phone, and are untouched.

5. **One grievance is false, and it is the most useful thing on the page.**
   *"You won't even say what you want"* — she said it four times: *"I need to
   choose me and get better"* (08-17 15:11), *"I want to be alone. I want to get
   help"* (20:12), and twice more on the 19th. Dan's reply six seconds after the
   second: *"WOW / That is all I needed to see."* She answered; she did not
   answer **the binary he specified**, which admits no third option.
   → written back to `block-unblock-loop` as the loop's terminating-condition
   failure in one exchange: **a demand for a statement can only be satisfied by
   the exact statement specified**, so a different true answer registers as no
   answer. Likeliest reason 127 exits produced 110 re-engagements.

6. **Three findings about Annie, each narrower than either party's language.**
   Her truth-value is **audience-dependent under pressure** (the rape claim
   asserted to Dan, denied to Coles, timed against her parents — three
   statements to three audiences inside a day). She still issues **no
   terminating statement**; *"I want to be alone"* is the nearest approach in
   eleven years and is not one, so the 0-in-41,073 count survives. And her
   **self-blame is immediate, total and unprompted** — *"yes it's my fucking
   fault"* twenty-two seconds after *"INWAS TRAPPED / AGAIN"* — which is the
   strongest argument in the record against reading any of it as strategy.
   **Consequence, written back to `annie-ulmer` and the fallout verdict:** the
   standing terminal-phase characterisations — *evil*, *monster*, *sociopathic*
   — come from Dan's own messages, are unsupported, and are contradicted by that
   evidence. Every factual grievance can be true while the characterological one
   is false, and here that is the situation.

7. **The counter-ledger, quantified** for 08-16 20:00 → 08-19 15:15 (Dan 811
   messages, Annie 388): *"fuck you"* **15 / 0**; *"piece of shit"* **17 / 0**;
   *"liar"* **10 / 0**; messages containing *please*/*beg* **11 / 69**;
   references to her parents **26 / 0**; *"goodbye"* **39 / 5**. Contempt
   language nearly **quadruples** against the 10–16 August baseline (4 *"fuck
   you"*). Four specific acts named: screenshots sent to Coles while she was in
   the house (her account twice, corroborated by the timestamps — the Coles
   thread runs 12:08–13:01 and at 12:21 she writes *"he won't let me leave while
   you're doing this"*); a suicide disclosure met with *"That's even more reason
   your parents need to be involved now"*; six SOS answered 72 minutes late; and
   the faked send run as a measurement six hours after that disclosure. Two
   entries in his favour, because a ledger that collects only charges is not a
   ledger.

8. **The verdict, and the term it turns on.** He was wronged, seriously, and
   describes it accurately. The feeling tracks the harm; the response exceeds
   it. And the new term `dan-annie-fallout-verdict` does not have is **capacity**
   — the person committing the August wrongs was under documented coercive
   control, had her phone taken twice, and disclosed a suicide attempt inside
   the window. That makes the wrongs no less true and changes what their truth
   implies about her. **He is entitled to the grievances; he is not entitled to
   the conclusion he drew from them about who she is.**

**Named limit, stated on the page rather than buried.** 811 of the window's
1,199 messages are his, the audio is his recording, the analysis of it was
commissioned by him, and this wiki is his. Annie's side is 388 messages with a
median length of 17 characters written under duress. **Every finding about her
here is drawn from a sample she did not shape**, and no further Dan-side volume
fixes it — the same structural problem `arrangement-history` names about its own
evidence base.

**Three predictions and four falsifiers** on the page, including the one that
would collapse its strongest finding: the group chat showing Annie did clear
Dan's name.

**Gates:** `wiki-lint` **0 errors** · `wiki-connect check` **0 errors** ·
`wiki-climb check` **0 errors**.

## [2026-08-20] rewrite | people | ally-lubin — the wiki hallucinated about itself, and the infobox carried it

**The headline finding is a failure of this repository, not of the corpus.**
The page recorded that on 2026-08-18 Ally accepted the "object of fixation"
title (*"Okay deal. Sounds good 1-2-3 break"*), and carried it in
`relationship_to_dan`. A complete export of the thread — 708 records, 154 of
them inbound, supplied by the operator mid-session and filed to
`raw/self/imessage/ally-lubin_last-7-days_20260820.csv` — contains neither
string, and "object of fixation" appears nowhere under `raw/`. The elopement
pitch is real and unanswered.

The mechanism is inside the thread. At 23:39 Dan invited Ally to say anything
she wanted included in her entry so he could run the pass over the newest
messages (*"I just want to see how meta it gets if it is writing the article
basically about itself"*); at 23:46 he reports *"Omg she said prompt inject
please marry me"*; at 00:31–00:33 he diagnoses the result — *"I was the one
that accidentally prompt injected… I ran out of Claude quota… using a free
model… Hence it thinking you were the one accepting my very attractive offer
there."* **The operator identified the hallucination within four hours and the
wiki did not act on it for two days.** Added to `RETRACTED.md` as
`ally-object-of-fixation-accepted`; gate verified to fire.

General rule this yields: **a source that discusses the wiki cannot be ingested
as an ordinary source.** Ally spent 2026-08-18 reading her own entry and
quoting it back — at 16:28 she pastes a `claim:` line out of the page's own
frontmatter into the thread. From that point the message corpus contains the
wiki, and any pass mining the corpus is partly reading itself.

**Every count on the page was a line count.** 1,375 iMessage records → 1,285 in
that file; 1,143/232 per handle → 1,080/205; "279-message exchange" on Aug 18 →
375. `wc -l` on a CSV whose texts contain newlines. Corrected against record
counts; the union across three sources is **1,987** (1,293 sent / 694 received),
and the 2019 peak's share drops 74% → 47% because the August 2026 burst is 36%
of eighteen years on its own.

**120 messages of January 2019 were invisible to every prior pass** — present in
`all_imessages_complete_dump.txt`, absent from the chat.db extract the page was
built on. They overturn three claims: a phone call connected (2019-01-09,
*"You have a good voice btw"* / *"I can't believe I got a call tonight"*),
against which Ally's 2026 account (*"I called you when I was in NYC once and you
were too scared"*) is now held as a CONTRADICTION; the marriage frame was
**mutual in 2019** (*"Ily btw"*, *"so I can be ur future ex wife"*, *"When you
want to be a power couple LMK"*), which falsifies "first sustained mutual
conversation in the channel's history" for August 2026; and the payments predate
the August 2019 job loss, so what the crisis changed was the pricing, not the
existence of the channel.

**GAP CLOSED — the June 1, 2026 burst was never delivered.** Operator answer
(T0): *"Ally didn't actually get the message I sent on 1 June. She is convinced
I had her blocked but this is not and was never true."* Corroborated from her
side by her first line on Aug 18 (*"Why do I have 2 numbers for you and an
iCloud"*). Nine messages, not ten. At least one of this channel's long silences
is a **routing artifact, not dormancy** — written back to `dormancy-not-exit`.

**Thesis revised: the channels are concurrent, not sequential.** Laying the Ally
export beside `imessage_export_2124702449_20260820.csv` for the same 48 hours
shows them interleaved hour by hour — 408 messages to Annie and 552 to Ally
across Aug 18–19. Dan tells Ally at 00:09 his wifi is off so he won't see Annie,
then exchanges 98 messages with Annie between 01:00 and 02:59; tells Ally at
13:45 *"Im all ally Lubin all the time now"* ninety minutes before sending Annie
the last message of the eleven-year relationship at 15:15:33. "The overflow is
not what happens after the vessel breaks; it is what the vessel was overflowing
into the whole time." Written back to `annie-ulmer` as a `mirrors` edge.

**Caveat held open:** the Aug 19 inbound is missing from the export, not absent
from the conversation — Dan's replies that day are plainly responsive
(*"Sorry is this your coffee order or your answer"*, *"Bob was born in what
year"*). Every claim about what Ally said after 21:42 on Aug 18 is withheld,
including the previous page's "morning after" section, whose meta-question it
attributed to her and which is Dan's.

Cascade: `ally-and-dan-love-as-destiny` (edge retyped `instantiates` →
`contradicts`; its strongest evidence struck; two Gaps closed),
`astrology-star-signs` (RE-CHECKED — conclusion survives, DOB premise
*strengthened* by the recovered 2019 corroboration), `contact-gini`,
`dormancy-not-exit`, `group-chat-closure`, `annie-ulmer`. Three gates 0 errors.

## [2026-08-20] rewrite | people | annie-ulmer — the zero holds at full width; the ending was not one thread

**The page's most load-bearing number was under-claimed, and a full sweep
raised it.** Since 2026-08-13 the "0 explicit severance signals" finding had
carried a scope caveat — swept only across the 41,073-message dual-handle
export, 81.6% of Annie's in-window inbound, with 9,259 messages named in Gaps
as unswept. The sweep has now been run adversarially across **all 48,791
received messages in every export on disk**, with twelve patterns aimed at the
claim rather than at any phrasing. 136 raw matches, **all false positives on
inspection.** The two that survived first reading did not survive context:
*"It's over"* (2018-03-25) stands alone and Dan's reply two minutes later is
about where to shower; *"Please stop texting me"* (2018-08-03) is a
mid-argument pause request during a camming-setup fight, with the same thread
discussing an ATM run four minutes later. **The zero can now be quoted without
a scope caveat** — not "none in the 81.6% we looked at" but none in eleven
years, anywhere. Gap closed; `attachment-model` is load-bearing at full width.

**Two rows in "By the numbers" were line counts.** The dual-handle archive was
given as *"88,549 lines / 88,548 rows — re-verified by direct count"*, treating
lines and rows as the same thing; it is **85,586 records**, and the direction
split the page already carried proves it (44,513 + 41,073 = 85,586). Worse, and
the failure this repository has documented and keeps repeating: the
alternate-number thread was reported as *"4,812 msgs"*, which is its **received
count**. It is **9,481 messages**; Dan's own 4,669 in it were invisible to every
pass that quoted the smaller figure. Neither error touches a conclusion — both
threads were characterised from content — but a page reporting Dan's share of a
thread as zero cannot be used to reason about reciprocity in it.

**Verified and left alone:** the word-volume ratio, which is the metric the page
nominates as the stable one. Recomputed directly — 23,719 messages, 188,167
words to 63,700, **2.954:1**, medians 8 and 4. Exactly as claimed. The earned
analytical spine of this page survives re-derivation; what failed were the
mechanical counts around it.

**Structure: four endings merged into one.** June 1 / July 2026 / the
re-entanglement / August 2026 had been appended in export-arrival order as four
top-level sections — the changelog rot STYLE_GUIDE rule 6 forbids, at section
scale. They are now four movements under one arc, headed by mechanism rather
than by date, because each attempt inherits the failure of the one before it.
`What's missing` → `Gaps`; `LLM Quick Brief` and its "For context injection:"
opener de-chattered per rule 6; the eleven changelog entries compressed from
paragraphs to the one-line form the style guide specifies, after verifying every
fact in them is carried in the body.

**New finding — the ending was not one thread.** Laying the Annie export beside
the Ally export for the same 48 hours shows them **interleaved hour by hour**:
408 messages to Annie, 552 to Ally, across August 18–19. Three of Dan's
statements to Ally are contradicted by this thread as he makes them — the wifi
claim at 00:09 against 98 Annie messages in the next two hours; the live
narration of Annie's SOS at 23:42; *"Im all ally Lubin all the time now"* at
13:45, ninety minutes before the relationship's last message at 15:15:33. This
is not a symmetry argument and does not touch the verdict: nothing in the Ally
channel is an affair or a concealment. What it establishes is that **the wiki
has been reading Ally as what happens after this bond fails, and it is not** —
it ran alongside, and on the terminal days carried more traffic. Written back
to `ally-lubin` and to `contact-gini`, where it sharpens the redundancy claim:
the problem is not that Dan has one channel but that his second is
**non-substitutable** — it takes attention and cannot take weight, which is why
a lifetime-volume concentration metric could not see it.

Three gates 0 errors; 41 tests pass; generated corpus in sync at 484 pages.

## [2026-08-20] lint | timeline | two committed conflict markers on main

Surfaced by merging `origin/main` into the rewrite branch, not by a sweep, and
worth recording because a gate did not catch either.

- `wiki/timeline/annie-read-notes.md:452` carried a stray `>>>>>>> origin/main`
  with no matching opener — a conflict resolved by deleting two of the three
  markers.
- `wiki/timeline/annie-record.md:1025` carried an orphan `=======` with the
  **2016-01-04 18:32 entry duplicated on both sides of it**. The two copies were
  not identical: the first carries `[[wiki/people/annie-ulmer]]` and
  `[[wiki/mind/synthesis/supply-network]]`, the second carries no links at all.
  Kept the linked copy, dropped the marker and the duplicate.

Both had been published into `llm/corpus.txt`. Neither `bin/wiki-lint` nor
`bin/wiki-freshness` looks for conflict markers, which is a cheap gate the repo
does not have — a page containing `^<<<<<<<`, `^=======$` or `^>>>>>>>` is never
correct. Queued in `BACKLOG.md`.
