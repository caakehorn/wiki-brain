# BACKLOG — the single live work list

One file, so there is one place to look. Replaces `task.md` (v1 phase tracker,
retired 2026-08-08 — four of its seven remaining targets were page names that
never existed), `TO-DO-LIST.md` (operator's hand list, carried forward below),
`LONG_TAIL_TRIAGE.md` (2026-07-18 verdicts, executed 2026-07-19 — see
"Settled" at the bottom), `contact-review.md` (a worksheet for a quarantine
that no longer exists) and the campaign backlog from `MESSAGE_MINING.md`.

**This is not the resume point.** `LLM_HANDOFF.md` holds the exact place the
last session stopped and what to do next. This file holds the standing work
that outlives any one session. Two machine-maintained queues sit alongside it:
`connection-queue.md` (mined edge candidates, `bin/wiki-connect candidates`)
and `synthesis-queue.md` (mined climb clusters, `bin/wiki-climb candidates`).

When you finish something here, delete the line — the file's value is that
everything in it is live. When you decide *not* to do something, leave it with
a one-line reason; a considered non-decision is knowledge, and it stops the
next model re-proposing it.

---

## 1. Extraction — the standing campaign

Per `EXTRACTION_SPEC.md`, this is the repository's binding constraint. In
rough expected-value order.

- **`raw/self/dox-scan/gmail_bodies.txt` — the Gchat archive.** The largest
  under-mined source in the repository. One correspondent's slice (495
  conversation blocks under `lexieamb@gmail.com`) was read 2026-08-08 and
  reorganised `alexis-armel`; the rest is unread. It is the only *daily-life*
  record of 2010–2013 anywhere in `raw/` — everything else from those years is
  retrospective. Blocks are keyed `Subject: Chat with <name>`, unsorted, and
  mostly undated (43 of 495 in the read slice carried a `Date:` header), so
  report sample ranges rather than spans.
- **Per-contact CSV sweep.** `raw/self/message-csv/imessage_<number>_both_all_now.csv` files exist per phone number and are the most complete two-sided record of individual relationships in the corpus, but no systematic check has been run for which person pages are missing theirs. The 2026-08-11 Rick pass found one (`imessage_7243667777_both_all_now.csv`) that had never been cited anywhere and that reversed a standing figure three pages had been carrying forward from an AI dossier. `ls raw/self/message-csv/*_both_all_now.csv`, resolve each number against a person page, and check it against that page's `sources:` list. See `EXTRACTION_SPEC.md`'s "Traps by source type" for the check to run per-page going forward.
- **Behavioural mining over lexical.** What Dan *did* while unobserved —
  latency, initiation, abandonment, escalation, time-of-day. `contact-gini` and
  `message-circadian-latency` are the model and the corpus's strongest findings.
  Lexical passes have hit diminishing returns.
- **Corroboration sweep against `OPEN.md`.** It lists every live contradiction,
  gap and standing prediction; many name a number or date the message corpus
  could settle. Work it top-down with `bin/mine-messages grep`.
- **Second passes over sources marked ingested.** Not redundant work: the first
  pass could not know what to look for, because the pages that would have told
  it what mattered had not been written. Every source re-read in the 2026-08-08
  pass yielded findings the original ingest missed.
- **Test prediction 1 of `calibrated-confidence`.** Run the graded-confidence
  pattern over the Facebook Messenger export, `gmail_bodies.txt` and the
  `raw/self/chats/` sessions. If Dan sits at inbound baseline in another
  channel, the finding is about iMessage rather than about him and must narrow.
- **Hedging study.** The 43 confirmed hits come from one pattern. *"odds are,"
  "there's a good chance," "I'd bet," "probably," "I doubt"* are unmeasured and
  would put the finding on a far larger base.
- **`bin/mine-messages entities` needs a spam filter** — it currently drowns in
  bank alerts and brand names. Real candidates already surfaced with no page:
  **Ricky** (66 msgs, 2015–20), **Libby** (83, 2024–25), **Alice** (50,
  2023–25), **Derrick** (29), **Michelle** (31). A sixth, **Lucy** (67,
  2015–18), needs the one-page-per-entity check first — `wiki/people/lucy.md`
  exists and is the household dog, so the miner may be catching messages
  *about* her.
- **`"supposed to be"` at 2.17× baseline (n=123)** — the best-powered
  unexplained divergence in the lexical battery. An obligation/expectation frame
  running at twice baseline is a `mind/` finding waiting to be read.

## 2. Structure and coverage

- **Lineage split** (operator, standing). Separate the ancestry/23andMe material
  into a **family-tree** entry and a **genealogy** entry; give the full
  Ancestry tree data and a visual; expand the 23andMe entry with the full
  chromosomal and region-specific data. A hybrid 23andMe × Ancestry analysis
  page is wanted too, **clearly labelled speculative**.
- **The `raw/` wikilink question.** Ten wikilinks point into `raw/`, which is
  deliberately unpublished, so they render as broken on the site. Either publish
  a stub explaining `raw/` is private, or mark them so they stop reading as
  errors. Unresolved by design since 2026-08-08.
- **Domain height.** Four domains — `self`, `timeline`, `work`, `places` — have
  three or more pages and nothing above any of them. `bin/wiki-climb audit`
  shows live progress; `synthesis-queue.md` holds the mined clusters.

## 3. Named open questions

Each of these is a specific thing the corpus or the outside world could settle.

- **Which Bacharach novel the coincidence is in.** Dan attributes the Virginia
  Avenue passage to *The Bend of the World* and cites pages 227–228; Bacharach's
  own 2021 message names *The Doorposts of Your House and on Your Gates*, and
  the reading log holds only the latter. One page number checked against a
  physical copy closes it. (`wiki/people/jacob-bacharach`)
- **Where Dan actually slept, spring–summer 2018.** He gave out 117 Belmont
  Circle five times between February and September 2018, four of them after
  Fran's death, while the residence timeline has him at 155 Virginia Ave until
  February 2019 and an eviction notice was served there on 2018-03-29. A
  targeted read of that window would settle a timeline the wiki carries as
  "outcome undocumented."
- **The announcement rule, tested backwards.** All 127 exit declarations are
  announced by definition; the falsifier is the reverse case — a silent
  severance that executed. The one claim the corpus can attack on its own.
- ~~**`the-unnamed-man` vs `tuquick-17248123683`**~~ — **SETTLED 2026-08-09.**
  A FOREWARN lookup identified Tuquick as **Jerel Wayne Coles** (exact
  phone-number match, 2026-08-08); the operator then confirmed directly that
  Tuquick and the July 2026 unnamed man are the same person ("They are the
  same person — tuquick and unnamed," filed at
  `raw/people/captures/2026-08-09-tuquick-unnamed-man-correction.md`).
  [[wiki/people/jerel-coles]] is now the canonical entity page for all three
  identities.
- **Is Coles = Target G?** FOREWARN returned no marital data. `wiki/people/annie-ulmer.md` §Target G names him only as "Caitlin's husband."
- **Why did Coles hold two addresses (Uniontown/Connellsville) for 22 months, 09/2024–07/2026?** Unexplained; see `wiki/people/jerel-coles.md` §Open questions.
- **Does the "video proof / unconscious" accusation originate with Coles (2026-07-26, from Annie's phone) or with Annie (2026-05-31, 23:54)?** Now answerable from logs already held; not yet run.
- **Independent docket verification of Coles's criminal record** via PA UJS (ujsportal.pacourts.us) — the FOREWARN capture is commercial-aggregator sourced, not court-verified.
- **The `annie_metadata_24h.csv` / `imessage_export_2124702449_20260809084846_.csv` sourcing gap.** [[wiki/timeline/events/august-2026-unmasking]] and [[wiki/mind/synthesis/read-receipt-forensics]] were written from a session with direct `chat.db` access; the underlying CSV exports were never filed to `raw/self/message-csv/`. File them, then re-point `sources:` on both pages. See `queue.md`.
- **`reply_to_guid`-as-threading audit.** [[wiki/mind/synthesis/read-receipt-forensics]] finding M2 voids any prior analysis that treated `reply_to_guid` as an intentional reply marker rather than an auto-populated field. No such prior analysis has been identified yet — sweep for one.
- **The `463-morgantown` mechanics-lien deadline** (~2026-07-27) elapsed with no
  recorded outcome, and the date was always derived rather than documented. The
  risk is now unobserved rather than pending, which is worse. A Fayette County
  prothonotary/recorder search on the parcel answers it.
- **Outside-corpus lookups, all cheap:** Fayette County magistrate records for
  the April 2018 hospital incident; Fayette/Somerset records for Jay Lauer's
  exact date and cause of death; the date and authorship of Diane's letters;
  whether Champion, PA lies outside Fayette County (if so it is the line's only
  attested out-of-county residence in four generations).

## 4. Tooling and hygiene

- **`leviathan/factstory.html`'s INGEST BRIEF is out of lockstep** with
  `FACTSTORY_BRIEF_TEMPLATE.md` and has been since 2026-08-02. That repo is not
  always in session scope; regenerate when it is.
- **Enforce the disclosure line mechanically.** `bin/wiki-climb check` could
  warn when an `earned` page synthesizes a `mixed` one without stating what
  primary evidence it added. Ten of nineteen pages satisfy the substance and
  skip the sentence. Small, safe, with a clear spec behind it.
- **Swarm-era stubs still unrewritten:** `arnu`, `alexander-jackson`,
  `john-carney` — fragment prose and dossier shorthand. They carry correct typed
  edges; the bodies were never done.
- **`leviathan`'s `WIKI_BRAIN_TOKEN`** is a fine-grained PAT that expires within
  a year and will break the hourly mirror sync identically when it does. A
  read-only deploy key via `actions/checkout`'s `ssh-key:` is the non-expiring
  alternative.

- **A `grep` gate for retracted strings** (opened 2026-08-18). Five pages were
  found carrying the retracted "$750/week" figure, two of them *underneath a
  correction block that quoted the sentence it had never changed*. No gate sees
  this: the pages lint clean, edges type-check, dates are current. A retracted
  claim is a string, and a pass that records one could register it in a
  `RETRACTED.md` ledger the gate then greps for across `wiki/`. This would have
  caught all five, including the `$750/wk` abbreviation that a `$750/week`
  sweep misses.
- **Regenerate `master-timeline` in the pre-commit block.** It was 484 events
  and 7 pages stale on 2026-08-18 because `bin/wiki-timeline generate` is not in
  CLAUDE.md's "before every commit" list, unlike `wiki-digest` and
  `llm-publish`. It is derived and cheap; there is no reason it should ever
  drift.
- **Lint duplicate frontmatter keys** (opened 2026-08-18). Three pages carried
  the same key twice, and because YAML keeps the *last* occurrence while
  `bin/wiki-climb`'s own reader collects *both*, the repo's gates and every
  standard parser disagreed about those pages' contents.
  `wiki/work/fastly-fsly.md` was silently dropping its membership in
  `2020-2021-market-era` — the page's entire reason for existing — and
  `wiki/people/jerad-friedline.md` was dropping `context-core`. The portal at
  `caakehorn/home` parses this frontmatter for real, so the derived snapshot was
  losing edges the gates said were present. All three are fixed; the check is
  four lines of Python and belongs in `bin/wiki-lint` so the class cannot
  recur. Worth auditing whether `fm_list`'s permissiveness hides anything else.
- **30 pages carry `status: archived` outside an `archive/` directory**, which
  `STYLE_GUIDE.md` reserves for pinned artifacts that are never updated. The
  status is being used to mean "finished" — the documented default for which is
  `stable`. This matters because it makes those pages look exempt from
  correction: `wiki/timeline/periods/2018-deep-cycle.md` was one of them and was
  feeding a false claim into the generated master timeline. Audit and re-status;
  `bin/wiki-lint` could then enforce the directory rule.

## 5. Settled — do not re-litigate

Kept because re-proposing these wastes a pass each time.

- **`wiki/people/contacts/` was eliminated on purpose** (commit `65f80c2`), and
  the quarantine concept with it. Stubs were promoted or merged. Any governance
  text still describing a contacts quarantine is stale; fix the text, do not
  recreate the directory.
- **The long-tail triage of 2026-07-18 is executed.** All six "MINE" targets
  (`sam`, `davey-fitzpatrick`, `vaughn`, `nick-mattie`, `urpaaa-at-yahoo-com`)
  and the `jason-bermejo` opener rewrite were completed 2026-07-19. The
  ACCEPTED-LEAF pages — annoying, bekah-fullem, brennan-meadows, bub, drew,
  jason-cole, josh-coccagna, kya-hansen, lisa-durbin, mike-cordaro,
  mohammed-bin-salman — are real prose pages, deliberately reachable from their
  index only. Do not churn them; revisit only if new raw evidence links them to
  a host page.
- **The swarm-stub category is believed empty.** All twelve 2026-06-23
  template stubs under `wiki/people/` were rewritten by 2026-07-20. Before
  resuming that line of work, re-run the `date_created == date_modified` +
  2026-06-23 heuristic to confirm, rather than assuming there is more.
- **`mind/psychosexual/taboo-and-boundary-testing`** is the known thinnest page.
  Rewrite only if a richer primary source surfaces; otherwise leave it.
- **`data/wiki-data.json` in the public `leviathan` repo carries the full body
  prose of every page, served unauthenticated.** Raised with the operator, who
  confirmed the exposure is intended. Making `wiki-brain` private did not make
  the wiki's contents private, and that is a decision, not an oversight.

## Phantom citations — sources cited but empty (opened 2026-08-14)

`bin/source-index` found four header-only files in `raw/self/message-csv/`,
two of them cited by wiki pages as though they carried evidence:

- **`END_FIGHT_full.csv`** (68 bytes, 0 rows) — cited on
  `wiki/self/message-corpora/master-message-dump.md`,
  `wiki/timeline/events/end-fight.md`,
  `wiki/timeline/events/group-chat-closure.md` (credited specifically for
  "sequence details"), and `wiki/mind/synthesis/dan-annie-fallout-verdict.md`.
- **`annie_group_chat_may31-june1_2026.csv`** (68 bytes, 0 rows) — cited on
  `wiki/mind/synthesis/bond-switch-2015.md`.
- `annie_group_chat_relaxed.csv` (57 bytes) and
  `messenger_export_THREADKEY_HERE.csv` (0 bytes) — not cited anywhere.

**The work, not yet done:** for each of the five citing pages, determine
whether any specific claim rests on the empty file *alone* rather than on a
co-cited non-empty source. Every one of those pages also cites
`THE END FIGHT.csv` (589 real rows) or `annie_all_time_logs.csv`, so the
likely finding is that the empty citations are redundant decoration and no
claim falls — but that is a hypothesis, not a result, and "likely redundant"
is exactly the reasoning that let the `sic semper` inversion stand for two
months. Do not close this by assuming.

Do **not** delete the empty files. `raw/` is immutable, and per the
2026-08-13 doctrine on artifacts that produced a documented failure, they are
retained as the worked example behind this backlog item.

---

## [2026-08-19] Fourteen cheap staleness re-checks left by the five-climb pass

`bin/wiki-climb check` reports **14 STALE warnings**, all created on 2026-08-19
by write-back edges from five new synthesis pages. They are recorded here rather
than cleared, because CLAUDE.md's one prohibited move is bumping a date to
silence a warning, and "the change was additive" is a hypothesis until somebody
reads it.

**The one that was not cheap has been worked already.**
`totality-themes` ← `single-channel` was a real premise movement — the
evaluative leg of the four-domain concentration claim was measured for the first
time and came back inverted (taste-record Gini 0.188 against the contact graph's
0.9601). The re-check is on `totality-themes`, the edge claim is narrowed, and
the Irreversibility Firewall's reading survives on the relational leg alone.

**The remaining fourteen are believed additive.** In each case the premise
gained a typed edge and, on five pages, a `CONTRADICTION` block; no figure, date
or conclusion the dependent reasons from was altered. Expected cost is one
grep per pair.

| Dependent | Premise that moved | Why it is believed cheap |
|---|---|---|
| `the-cool-metric` | `interests-as-era-markers` | Gained a set-closure section; the "admission criterion upstream of intake" claim is untouched |
| `dormancy-not-exit` | `424-bedford-ave`, `155-virginia-ave` | Both gained one edge into `the-unpapered-address`; lair-continuity is unaffected, though the 155 Virginia *lease holder* question is now live and bears on it |
| `read-receipt-forensics` | `forensic-method` | One edge added; no instrument-defect claim touched |
| `the-unbroken-bond` | `enneagram-5w4` | Gained a `CONTRADICTION` on the wing code — **this one may not be cheap**, since a 5w6 reading would change the sx/sp fusion account the bond page leans on |
| `alexander-jackson`, `arnu`, `john-carney`, `suzanne-frank` | `463-morgantown` | One edge plus a "seventh instance" section; no risk-table row changed |
| `suzanne-frank` | `337-saratoga-drive` | One edge; the Chapter 13 account is untouched |
| `jerad-friedline`, `2020-2021-market-era`, `fastly-fsly` | `context-core` | One edge added to the spine; no figure changed |

**Do the `the-unbroken-bond` ← `enneagram-5w4` pair first.** It is the only one
where the premise gained a contradiction rather than an addition.

## [2026-08-19] Collect what other people say Dan is like

Named as the missing control on `wiki/mind/synthesis/the-commissioned-self`. The
corpus holds 110,944 inbound messages from 503 handles and the wiki has **no
independent characterisation of Dan by anyone who is not either him or an
instrument he commissioned** — no clinician, no employer instrument, no
third-party account. A pass over inbound messages for second-person description
would give the psychological layer its first outside input, and it is cheap:
`bin/mine-messages grep --dir Received` over a small set of framings
(*"you always", "you're the kind of person", "that's so you"*) would produce a
first sample in an afternoon.

## [2026-08-19] Two one-query questions the housing synthesis cannot answer

`wiki/places/the-unpapered-address` establishes that no lease, rent figure or
signatory exists in the corpus for any of seven residences. Two of its gaps are
answerable from outside `raw/` and would outrank the whole page:

- A **Fayette County recorder/prothonotary search** on the 463 Morgantown parcel
  — settles the elapsed Arnu mechanics-lien deadline, which has been open since
  ~2026-07-27 and is already flagged on `wiki/legal/463-morgantown`.
- The **307 E 76th lease signatory**. The rent is now known ($2,450 → $2,700);
  the name is not, and it decides whether Dan was ever a named party to a
  residential lease at all or only ever an occupant.

## Staleness left open by the 2026-08-20 August-severance ingest

Thirteen `bin/wiki-climb check` warnings stand after that pass. **Nine are
its own**; four (`jerad-friedline`, `2020-2021-market-era`, `fastly-fsly` ←
`context-core`, and `the-cool-metric` ← `interests-as-era-markers`) predate it.
Eleven pages were re-checked properly during the pass, including the five where
a conclusion could plausibly have moved (`the-unbroken-bond`,
`dan-annie-fallout-verdict`, `ally-and-dan-love-as-destiny`,
`read-receipt-forensics`, `single-channel`) — each carries a real `RE-CHECKED`
block, none was cleared by bumping a date.

The nine below are believed cheap. **That belief is a hypothesis, not a
result**, and each states its reason so a later pass can disagree with the
reason rather than re-derive it:

| Dependent | Premise that moved | Why it is believed cheap |
|---|---|---|
| `health/the-configured-body` | `health/cocaine`, `supply-network`, `the-deferred-audit` | All three moved by `RE-CHECKED` block only. The body page's argument is about maintenance vs. surveillance, not about supply topology. |
| `interests/food-and-diet` | `work/bfs-foods` | BFS moved for the 2026-08-11 job restoration — an employment fact, not a food one. |
| `mind/synthesis/the-embedded-objective` | `work/bfs-foods` | **The least cheap of the nine.** BFS gained the posted `NO HIRE: Daniel Frank` sign, in two locations, and the reversal being initiated by the same person who imposed the ban. That is institutional-arbitrariness evidence and may be live for this page's argument. Do this one first. |
| `mind/synthesis/alias-as-periodization` | `totality-themes` | `totality-themes` moved by `RE-CHECKED` block only. |
| `mind/synthesis/closing-the-set` | `forensic-method` | `forensic-method` moved by two typed-edge additions and no prose. One of them points at `document-fabrication`, which is about production rather than intake. |
| `mind/synthesis/the-commissioned-self` (×2) | `instrument-is-subject`, `wiki-brain` | Both moved by `RE-CHECKED` block only. But note: `wiki-brain`'s new block is the handle-is-not-a-person defect, and `the-commissioned-self` counts first-person self-description across the corpus — if any of those counts run over Annie's 212 handle, the attribution caveat reaches them. Worth one check rather than an assumption. |
| `people/jerad-friedline`, `timeline/periods/2020-2021-market-era`, `work/fastly-fsly` | `self/context-core` | **Pre-existing, not from this pass.** Standing since 2026-08-19. |
| `mind/concepts/the-cool-metric` | `interests-as-era-markers` | **Pre-existing**, standing 8 days. |

## Standing items from the 2026-08-20 ingest

- **HIGH — transcribe `raw/self/audio/2026-08-16_Morgantown_St_call-recording.m4a`.**
  927 s of primary audio; the only account of it in the wiki is two removes from
  the source (a T2 agent analysis quoting a PDF that is not in `raw/`). Every
  quotation on `wiki/timeline/events/august-2026-morgantown-call` and
  `wiki/people/jerel-coles` becomes checkable the moment this exists. This is
  the single highest-value action available on the August material.
- **HIGH — did the email to Annie's parents ever send?** Dan asserts it three
  times on 2026-08-19 and denies it twice the same day, and he is documented
  faking exactly that claim the day before. One look at a sent-mail folder
  decides whether the maternal-disclosure threat's execution rate is zero or
  one. Held as a `CONTRADICTION` on the event page until then.
- **HIGH — export the Ally thread for 2026-08-13 → 20.** Named as missing by
  the 2026-08-19 audit and still missing.
  `wiki/self/concepts/ally-and-dan-love-as-destiny` is now making predictions
  across a severance it cannot see the other side of, and this pass added a
  slot-refill control to it that cannot be evaluated without the baseline.
- **MED — sweep the corpus for earlier third-party-handle episodes.** Three are
  documented (2026-07-26, 2026-08-16, 2026-08-18), all found by register alone.
  There is no column for this and no detector. Whether it happened before July
  2026 has never been asked.
- **MED — the two videos.** The "molesting" video and the October 2019 MMF
  video are both circulating as leverage between three people and neither has
  been examined by anyone writing this wiki. The claim that turns on the first
  — eyes open at 0:37 — is Dan's, stated to two audiences, uncorroborated.
- **MED — recover the three drug-screen images** (2026-08-14 13:17, 14:08,
  14:11). `wiki/mind/concepts/document-fabrication` rests entirely on the
  message thread describing them; the artifacts would settle how good the
  forgery actually was.
- **LOW — `wiki/people/index.md` is 23KB against an 8KB budget.** Standing lint
  warning, untouched by this pass.

- ~~**Add a conflict-marker gate to `bin/wiki-lint`.**~~ **DONE 2026-08-20.**
  Shipped as `find_corrupt_text()`, and widened once a second class of invisible
  junk turned up the same day: eight **assistant citation artifacts** (private-use
  codepoints U+E000–U+F8FF wrapping a `filecite`/`turn` reference) in
  `morgantown-call-three-participant-ethical-analysis.md`. They render as
  nothing, survive copy-paste, and assert a source that points nowhere. The gate
  now catches both, with eleven tests — including a regression test that the
  whole wiki stays clean, and negative tests proving a setext underline and an
  `=======`-with-trailing-content are not markers.
