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
- **`the-unnamed-man` vs `tuquick-17248123683`** — partially settled 2026-08-09.
  A FOREWARN lookup identified Tuquick as **Jerel Wayne Coles** (see
  [[wiki/people/jerel-coles]]) via an exact phone-number match. Whether Coles
  is *also* the July 2026 unnamed-man antagonist is still open — no phone
  number for that man exists anywhere in the corpus to check against Coles's
  two known numbers, and the case rests on role and lexicon overlap only. Needs
  an answer from outside (a name from Annie, a photo, an independent
  identifier).
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
