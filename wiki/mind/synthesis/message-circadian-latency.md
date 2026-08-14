---
domain: mind
page_type: synthesis
knowledge: earned
status: active
date_created: 2026-07-15
date_modified: 2026-08-13
sources:
  - raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv
  - /Volumes/MUSIC/PHASE B RAW/LEVIATHAN_FULL_CORPUS.csv
  - raw/self/dox-md/OMNI_FORENSIC_DOSSIER.md
  - raw/self/dox-scan/all_imessages_complete_dump.txt
  - raw/self/message-csv/imessage_export_deep_20260813.csv
tags: [digital-footprint, relationships, attachment, infidelity, ai-collaboration]
connections:
  - page: wiki/mind/concepts/attachment-model
    type: evidences
    claim: "RETRACTED 2026-08-13 — the '9x reply-latency asymmetry' this edge carried does not exist and its sign was backwards; what the corpus actually shows is that in every measured relationship thread the counterparty answers Dan FASTER than he answers her, so reply latency indexes whether a thread is live, not how central the person is, and the attachment model gets no timing signature from it."
  - page: wiki/mind/concepts/contact-gini
    type: parallels
    claim: "The two metrics come apart rather than converging: Gini's volume concentration on Annie replicates on every source, while the temporal-synchrony half retracted here does not — every live thread in the corpus is near-synchronous, so concentration is carried entirely by volume and duration and not at all by reply speed."
  - page: wiki/people/annie-ulmer
    type: evidences
    claim: "RETRACTED 2026-08-13 — the '9-minute mutual latency' figure appears in no source; recomputed, Annie is the FASTER party (median 0.28 min against Dan's 0.38, 2015-2018, 62,987 thread rows) and opens 384 of 709 active days to Dan's 325, which makes her the pursuing side of the timing record rather than the delayed one the page had described."
  - page: wiki/self/message-corpora/master-message-dump
    type: component-of
    claim: "An analytical cut of the corpus that page documents, and the worked example of its central hazard: this page's headline finding was produced by treating LEVIATHAN_FULL_CORPUS.csv as a superset when it is missing roughly 80% of Dan's 2025 outbound."
  - page: wiki/mind/synthesis/attachment-trauma-bond
    type: evidences
    claim: "RETRACTED 2026-08-13 — the '16-44-hour inbound medians' quantifying a terminal-phase asymmetry are an artifact of missing outbound rows; on the fuller record the 2025 Annie thread runs 10,595 Dan to 10,174 Annie with both medians under a minute, so the terminal phase shows no measurable timing asymmetry and the bond thesis must rest on content rather than latency."
  - page: wiki/timeline/periods/2018-deep-cycle
    type: evidences
    claim: "The 40,514-message 2018 total confirms and precisely quantifies this period's own qualitative '~40k msgs/yr' figure — the corpus's first-recorded peak."
  - page: wiki/timeline/periods/2025-collapse
    type: evidences
    claim: "The 41,278-message 2025 total — within 2% of the 2018 peak — gives this period its first precise whole-corpus volume figure, confirming the collapse year matched the deep-cycle year for raw output even as the content shifted from relationship crisis to relationship termination."
---


# Message Corpus — Circadian Rhythm, Reply Latency, and Volume Trajectories

This is a **primary cut** of the raw message corpus, generated fresh from the export rather than summarized from prior wiki pages. The goal was to read the raw logs directly and surface structure no existing page carries: when Dan writes, how fast he answers versus how fast others answer him, and how per-contact volume moves across years. Of those three, **the circadian curve survived audit intact and the other two did not** — the reply-latency finding is retracted below and the yearly volume arc is corrected, both for the same underlying reason: the file this page called a superset is a lossy subset.

> **SOURCE RANKING, CORRECTED [2026-08-13].** The original pass named
> `LEVIATHAN_FULL_CORPUS.csv` (`/Volumes/MUSIC/PHASE B RAW/`, 181,650 rows,
> 2011-03-18 → 2026-06-09) as **ground truth** because its `sender` field is
> unambiguous (`Me (Dan)` vs the contact handle), sidestepping the known
> `direction`-field bug in `MASTER_MESSAGES_DB_DUMP.csv`. Clean attribution is not
> completeness, and the two were conflated. Leviathan is **missing roughly 80% of
> Dan's outbound in 2025**: on thread `+12124702449` for calendar 2025 it holds
> **Dan 2,114 / Annie 10,141**, where `all_imessages_complete_dump.txt` holds
> **Dan 10,595 / Annie 10,174** for the same thread and year while only running
> through 2025-08-10. The correct ranking for this page's questions is:
> `raw/self/dox-scan/all_imessages_complete_dump.txt` (217,573 dated lines, local
> time, best available for 2019–2025) > `raw/self/message-csv/imessage_export_deep_20260813.csv`
> (186,671 rows, **UTC**, whole-device, the only source covering 2026) >
> Leviathan/`MASTER_MESSAGES_DB_DUMP.csv`/`OMNI_FORENSIC_DOSSIER.md`, which are
> three renderings of one lossy extraction and agree with each other precisely
> because of it. Full provenance: `raw/self/message-csv/README_20260813_exports.md`.

> **Method note / data hygiene:** phone numbers in some derived sources are masked (`+172****6811` etc.). Matching there was done by **substring on the file's actual bytes** (e.g. `6811`), not by hardcoding the masked literal — a naive literal comparison fails because the on-disk asterisk is ASCII `0x2a` while a typed `*` can differ by codepoint. Every figure re-derived in the 2026-08-13 audit is stated with its file, timezone, thread key, direction and denominator, per `EXTRACTION_SPEC.md`'s provenance preflight.

## The headline, RETRACTED: there is no reply-latency asymmetry, and its sign was backwards

> **RETRACTED [2026-08-13] — this page's headline finding is withdrawn in full, not
> narrowed.** The claim was thesis-level: that Dan answers everyone in 1–5 minutes
> while they answer him on an hour-to-day clock, that "the *inbound* delay is what
> differentiates them, and it scales with how peripheral the person is," and that
> "everything else is Dan broadcasting into a slow or silent void." **Every one of
> those sentences has its sign reversed.** Recomputed under the page's own stated
> method — next opposite-speaker message in the same thread — on three files
> independently, the counterparty answers Dan *faster than he answers her* in every
> single pair in the table, including on Leviathan, the page's own declared source.
> The printed inbound medians (9.0, 19.0, 22.0, 346, 2,648 and 968 minutes) appear
> in no source under any handle definition tried.

**What the same method actually returns.** Thread-keyed on the chat target, next
opposite-speaker message, medians in minutes. Two independent files, stated
separately rather than averaged:

| Thread / window | file | rows | Dan answers (median) | they answer (median) | who is faster |
| :--- | :--- | ---: | ---: | ---: | :--- |
| `+17244346811` (Annie), 2015–2018 | dump, local | 62,987 | 0.38 | **0.28** | Annie, 1.35× |
| `+17244346811` (Annie), 2015–2018 | Leviathan | 62,784 | 0.4 | **0.3** | Annie |
| `+17249204125`, 2019 | dump, local | 9,001 | 0.50 | **0.33** | them, 1.5× |
| `+17243223678`, 2018 | dump, local | 5,787 | 3.50 | **1.83** | them, 1.9× |
| `+17243228715` (Suz), all years | dump, local | 29,235 | 1.10 | **0.78** | Suz, 1.4× |
| `+12124702449` (Annie NYC), 2025 | dump, local | 20,769 | 0.92 | **0.53** | Annie, 1.7× |
| `+13307038747` (Kristin), 2025 | Leviathan | 20,014 | 0.2 | 0.2 | tie |

The p90 columns move the same way: Dan's 90th-percentile reply to Annie 2015–18 is
0.29 h against her 0.10 h. The old table's "n (Dan replies)" column was not a reply
count either — 2,120 and 3,446 are Leviathan's *total Dan-sent rows* in those
threads, matching to the row; the actual number of Dan-reply pairs on
`+12124702449` is 916, not 2,120.

**The method is not what broke.** Run unchanged against
[[wiki/people/menore|Menore]] — the 2018–2025 delivery line — it returns Dan 0.53
min against Menore 6.68 min across 4,413 rows, reproducing that page's independently
measured 6.6/0.5 figures to two decimals. So the procedure does find a slow
counterparty when one exists, and the single genuinely slow channel in the corpus is
the *paid transactional* one. That is the exact inverse of the retracted rule, under
which slowness marked peripherality.

**Diagnosed cause 1 — the two latency columns are transposed.** Reading the table
forward rather than as labelled reproduces the shape of the printed "them → Dan"
column as *Dan's own* delay, on the two threads where a reconstruction is possible
(`+13307038747` at ~731 min against a printed 968; `+17243228715` at ~245 min
against a printed 346). The numbers are of the right order and the wrong owner. On
its own this would have inverted the finding while leaving the magnitudes roughly
intact.

**Diagnosed cause 2 — the source is missing Dan's outbound, which inflates every
inbound delay.** Leviathan holds Dan 2,114 / Annie 10,141 on `+12124702449` for 2025;
`all_imessages_complete_dump.txt` holds Dan 10,595 / Annie 10,174 for the same thread
and year while stopping on 2025-08-10. Roughly four of every five of Dan's outbound
rows are gone from the file the page trusted. Any measure of the form "time since Dan
last spoke" grows without bound as his messages are deleted from the record, which is
how a 0.53-minute median becomes 2,648. The two causes compound: transposition put
the hours on the wrong party, and the missing outbound manufactured the hours.

**Internal contradiction, requiring no recomputation.** The paragraph under the old
table described Annie as "the near-synchronous Annie channel (median 9 min both
ways)" while the table directly above it printed 1.0 min for Dan and 9.0 min for
Annie. The page contradicted itself in adjacent lines and the contradiction was
never caught, because the number was doing rhetorical rather than evidentiary work.

### What replaces it

Reply latency does not discriminate relationships in this corpus. **Every live
thread converges to a sub-minute median in both directions**; the variation between
threads (0.28 to 3.5 min) is smaller than the variation the retracted table claimed
*within* a single pair. What latency measures is whether a thread is currently live,
not how central the person on the other end is — which is why the one thread with a
real gap is a dealer answering a customer.

Centrality in this corpus is therefore carried entirely by **volume and duration**,
which is what [[wiki/mind/concepts/contact-gini|Contact Gini]] already measures and
which replicates on every source. The two metrics do not converge on one
singularity, as this page's frontmatter used to claim; the temporal half simply does
not exist.

**Prediction.** Any thread in this corpus with more than ~500 messages in a
twelve-month window will return a two-sided median under 4 minutes, regardless of
who the counterparty is or what year it falls in. **Falsifier:** a
relationship-scale thread — not a delivery or business line — where the
counterparty's median exceeds Dan's by more than 3× on
`all_imessages_complete_dump.txt`. One such thread and the "latency is liveness, not
closeness" reading is wrong.

### Day initiation — direction confirmed, figures restated

The one timing asymmetry that does survive is about who speaks first, and it runs
the opposite way to the retracted thesis. On `all_imessages_complete_dump.txt`,
thread-keyed on `+17244346811`, local time, 2015-01-01 → 2019-12-31, counting the
direction of the first message on each day with any traffic: **709 active days,
Annie opens 384 (54.2%), Dan opens 325.** By year: 2015 Annie 13/21 (61.9%), 2016
Annie 45/103, 2017 Annie 126/235, 2018 Annie 199/348 (57.2%). Annie is both the
faster responder and the more frequent initiator across the whole relationship —
the reverse of a man broadcasting into a void.

## Annie volume trajectory (merged handle, 2015–2018)

The merged Annie thread (the handle that is both sender and thread-target) gives the cleanest yearly arc of the central relationship:

| Year | Dan sent | Annie sent (received) |
| :--- | :--- | :--- |
| 2015 | 7,241 | 6,394 |
| 2016 | 6,420 | 6,149 |
| 2017 | 7,151 | 7,409 |
| 2018 | 10,821 | 11,194 |
| 2019 | 2 | 0 |

The 2018 peak (10,821 / 11,194) is the "deep cycle" the wiki already names — the highest annual volume of the decade. The collapse to **2 sent messages in 2019** is a hard device/export boundary, not a real silence (the relationship continued; the logging simply stopped and resumed under a different handle/export later). This matters methodologically: any per-contact yearly series read off a single handle will show false cliffs at export seams. The corpus must be re-merged across handles to read the true trajectory — and even then, 2019–2024 Annie volume is only recoverable from the separate ANNIETEXTS/combined exports, not this file.

## Circadian rhythm — Dan writes all day, peaks at night

> **RE-CHECKED [2026-08-13] — this section reproduced exactly and is preserved
> unchanged.** It was re-run in the same audit that retracted the latency finding
> above, because a section sharing a defective source is suspect until tested rather
> than false by association. Every count in the table below re-derives to the row
> from Leviathan's 70,123 Dan-sent messages, and the shape replicates on files
> Leviathan is not a subset of: night share (00:00–05:59) is **15.5%** for 2015–2018
> on the deep 2026-08-13 export converted UTC→America/New_York (n=46,298 Dan-sent)
> and **15.5%** on `all_imessages_complete_dump.txt` in native local time
> (n=59,976) — against the 15.6% printed here for the full record. The era drift
> survives too: 2025–26 night share is 12.8% on the deep export and 7.6% on the dump
> through 2025-08-10, both well below the 15.5% baseline, so the "less nocturnal in
> the collapse" direction holds on three files even though the printed 10.4% is
> file-specific. One caveat is now on the record: the **22:00 single-loudest-hour**
> claim is source-sensitive — 22:00 leads on Leviathan (7.5%) and on the deep export
> (7.2%) but 18:00 leads on the dump for 2015–18. The **17:00–23:00 peak window** is
> what holds everywhere, and that is the load-bearing claim.

Dan's own sent messages by hour (local time), over the full record:

| Hour | Count | Share | Hour | Count | Share |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 00:00 | 3,299 | 4.7% | 12:00 | 2,897 | 4.1% |
| 01:00 | 2,567 | 3.7% | 13:00 | 3,349 | 4.8% |
| 02:00 | 1,831 | 2.6% | 14:00 | 3,532 | 5.0% |
| 03:00 | 1,288 | 1.8% | 15:00 | 3,318 | 4.7% |
| 04:00 | 1,091 | 1.6% | 16:00 | 3,566 | 5.1% |
| 05:00 | 880 | 1.3% | 17:00 | 4,297 | 6.1% |
| 06:00 | 626 | 0.9% | 18:00 | 4,917 | 7.0% |
| 07:00 | 686 | 1.0% | 19:00 | 5,152 | 7.3% |
| 08:00 | 1,061 | 1.5% | 20:00 | 5,066 | 7.2% |
| 09:00 | 1,558 | 2.2% | 21:00 | 4,511 | 6.4% |
| 10:00 | 2,211 | 3.2% | 22:00 | 5,272 | 7.5% |
| 11:00 | 2,728 | 3.9% | 23:00 | 4,420 | 6.3% |

- Peak window is **17:00–23:00** (early evening through late night), with 22:00 the single loudest hour (7.5%).
- **Night share (00:00–05:59) = 15.6%** of all Dan's sent output — a heavily nocturnal writer, but not exclusively; daytime carries the majority.
- No weekday effect: distribution across days is flat (Mon 13.5% → Sun 16.0%), so this is not a work-week pattern — it is a continuous, always-on output channel.

### Era split — the rhythm shifts toward daylight in the collapse

Comparing the Annie-era window (2015–2018) to the 2025–2026 collapse window:

| Window | Night share (00–05) | Note |
| :--- | :--- | :--- |
| Annie era (2015–18) | **15.5%** | nocturnally peaked; 22:00 is the loudest hour |
| Collapse (2025–26) | **10.4%** | daytime share grows; loudest hours move to 17:00–20:00 |

The later window is *less* nocturnal — more of the output migrates into the working afternoon. One reading: as the relationship degraded and the drug-supply / logistical tether took over, the writing became more diurnal (coordinated, task-driven) and less the insomniac 2am flood of the early bond. This is a new, corpus-native signal — no existing page charts the circadian shape, let alone its era drift.

## Burstiness — Dan writes in tight machine-gun runs

- Of all gaps between Dan's consecutive sent messages, **62.7% are under 2 minutes** — he writes in dense bursts, not spaced-out replies.
- The longest observed run of consecutive sends with gaps under 10 minutes is **284 messages** — a single unbroken output storm.
- Median inter-send gap is **1.0 minute**; mean is 114 minutes (dragged up by the long silences between bursts). The distribution is bimodal: either he is firing continuously or he is dark for hours.

This burst profile is the behavioral fingerprint of the [[wiki/mind/concepts/attachment-model|fusion mode]]: when the attachment system is active, output is continuous and immediate; when it is not, the channel goes quiet. The floods at relationship onset (Dec 2015) and termination (2025–26), already documented on [[wiki/mind/synthesis/bond-switch-2015]], are the extreme tails of this same burst distribution.

## Yearly volume arc, 2015–2026 — an export's coverage, not a life's output

> **CORRECTED [2026-08-13] — the "arc label" column described an artifact.** The
> prior version read this table as a behavioral trajectory and named 2021–2022 "the
> corpus's hardest floor — a near-total communication blackout," with 2021 as
> "Near-total silence" and 2022 as "Dead channel." **There was no blackout.** The
> table is a row-count of one lossy extraction, and the audit found that
> `OMNI_FORENSIC_DOSSIER.md`'s yearly totals are identical, year for year, to the
> 2026-08-13 whole-device deep export's — 13,819 / 20,221 / 17,551 / 40,514 /
> 20,153 / 6,311 / 280 / 954 / 4,376 / 41,278 all match to the row. They are not two
> sources agreeing; they are one extraction counted twice. Against
> `all_imessages_complete_dump.txt` every year before 2025 is understated, several
> of them by a factor of six.

| Year | printed here (OMNI) | deep export 2026-08-13, UTC→NY | `all_imessages_complete_dump.txt`, local |
| :--- | ---: | ---: | ---: |
| 2015 (from Nov 12) | 13,819 | 13,819 | 14,408 |
| 2016 | 20,221 | 20,221 | **34,589** |
| 2017 | 17,551 | 17,551 | 21,824 |
| 2018 | 40,514 | 40,514 | **48,697** |
| 2019 | 20,153 | 20,153 | 24,781 |
| 2020 | 6,311 | 6,311 | 10,339 |
| 2021 | 280 | 280 | **1,465** |
| 2022 | 4 | 6 | **0** |
| 2023 | 954 | 954 | **5,156** |
| 2024 | 4,376 | 4,376 | **28,463** |
| 2025 | 41,278 | 41,278 | 27,850 *(source stops 2025-08-10)* |
| 2026 | 9,896 *(Q1)* | 21,207 *(to Aug 13)* | — *(source stops 2025-08-10)* |

**2021 through mid-2023 is a hole in both exports, and it is an export artifact.**
`all_imessages_complete_dump.txt` holds **zero rows between 2021-04-27 20:31:40 and
2023-08-09 00:54:11** — one unbroken 833.2-day window. The deep 2026-08-13 export,
converted to America/New_York, has the same hole at slightly different edges
(2021-04-07 08:04 → 2023-08-11 15:06, 856 days) broken by a single 6-message island
on the evening of **2022-12-31**, every one of them outbound and two of them
literally the word `test`. Six messages and two of them a connectivity check is what
a device produces when someone is testing a phone, not what a year of a life
produces.

The falsifier is in the wiki already. [[wiki/self/location-history|The Google
location record]] logs **806 place visits in 2022** — the year the message corpus
scores at four — plus 257 in 2021 and 728 in 2023, ~1,791 across the three years.
[[wiki/work/au-zaatar|Au Za'atar]] employment ran continuously from March 2021 to
August 2024 across the entire hole, ~690 estimated shifts and 445 visits logged to
the restaurant itself. A man working five nights a week in Manhattan did not send
four text messages in a calendar year. The 2024 row makes the same point without
needing the location data at all: 4,376 against the dump's 28,463 in the one year
both files cover and neither is missing.

What survives, restated with its scope: **2018 and 2025 are the corpus's twin
peaks.** That holds on both files independently — 40,514 vs 41,278 on the deep
export, and 48,697 in 2018 against 27,850 in 2025 on a dump that stops in August, so
the dump is on pace to agree. The precise figures given to
[[wiki/timeline/periods/2018-deep-cycle]] and
[[wiki/timeline/periods/2025-collapse]] should carry their file, since the two
sources differ by 8,000 messages on 2018. Note also that this table counts raw
volume across all contacts, not the Annie-specific figures above; the two should not
be conflated.

There is a second, larger and differently-shaped void in the same corpus that is
**not** the same artifact: SMS traffic stops entirely for nearly four years,
2020-07-30 → 2024-05-24, with inbound SMS stopping earlier still on 2020-05-28.
Both boundaries replicate to the second across the deep export and the dump, and
iMessage runs normally on either side. Details and the disabled-forwarding reading
are on [[wiki/self/message-corpora/master-message-dump]].

## Volume concentration (re-derived, matches prior Gini)

Across the corpus, Annie's two handles dominate. This primary cut re-confirms the [[wiki/mind/concepts/contact-gini|Contact Gini]] finding from raw: of Dan's 70,123 sent messages **in Leviathan**, the top contact (+172****6811) alone is 31,635 (45%). That denominator is now known to be short by roughly 8,500 of Dan's 2025 outbound rows, which sit overwhelmingly on the `+12124702449` Annie handle — so the concentration figure is if anything *understated*, and the direction of the error runs with the finding rather than against it. The next tier (+172****4125, +172****3678 in 2018–19; +133****8747, +121****2449 in 2025) are each bounded single-year spikes — friendships or entanglements that flare for one period then vanish from the log. The steady state is one channel at 45%+ and everything else as transient satellites.

## What this page still adds, after the 2026-08-13 audit

- The **circadian curve** and its **era drift** (15.5% nocturnal in the Annie era, falling in the collapse window on all three files) — timing data no other page carries, and the one original finding that reproduced exactly.
- The **62.7% sub-2-minute burst rate** and 284-message max run — the output-storm fingerprint. Measured on Leviathan and therefore inheriting its 2025 outbound loss; the burst rate is likely understated for 2025 and the finding is flagged rather than restated.
- **Day initiation on the Annie thread**: 709 active days 2015–2019, Annie opening 384 (54.2%) to Dan's 325.
- The **merged Annie 2015–2018 volume arc** with the 2019 export-cliff called out as an artifact, not a silence — the same class of error the rest of this page turned out to be making at larger scale, first noticed here and then not generalized.
- Two documented failure modes, which are now the page's most reusable content: a **transposed-column reversal** that survived because the number was doing rhetorical work, and a **lossy file mistaken for a superset** because its attribution was clean.

## Gaps / caveats

- Annie's 2019–2024 volume is not in Leviathan (handle/export seam); the true decade arc needs the ANNIETEXTS / combined_annie_logs exports merged in. The 2019 "2 messages" is an export boundary, not a real gap.
- Reply-latency uses the "next opposite-speaker message in the same thread" method. In high-burst threads it slightly over-states *both* parties' speed symmetrically, which is why the retracted asymmetry cannot be rescued by appealing to it.
- The burstiness section has not been re-derived on `all_imessages_complete_dump.txt` and is the remaining unaudited quantitative claim on this page.
- `+13307038747` is **Kristin Prentiss** ([[wiki/people/kristin]]) and `+12124702449` is Annie's NYC handle; both were "inferred from volume timing" in the original pass and are now identified. `+17243228715` is Suz. The 2026-08-13 export carries unmasked handles, so the masked-substring method described above is no longer necessary for new work.
- `LEVIATHAN_FULL_CORPUS.csv` lives in `/Volumes/MUSIC/PHASE B RAW/`, not filed under `raw/` — its on-disk path is cited directly above. It should not be used as a completeness reference for any window after 2024.
