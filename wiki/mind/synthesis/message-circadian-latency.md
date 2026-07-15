---
domain: mind
page_type: synthesis
knowledge: earned
status: active
date_created: 2026-07-15
date_modified: 2026-07-15
sources:
  - raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv
  - /Volumes/MUSIC/PHASE B RAW/LEVIATHAN_FULL_CORPUS.csv
related:
  - wiki/mind/synthesis/bond-switch-2015
  - wiki/mind/synthesis/attachment-trauma-bond
  - wiki/mind/concepts/contact-gini
  - wiki/people/annie-ulmer
  - wiki/mind/concepts/attachment-model
tags: [digital-footprint, relationships, attachment, infidelity, ai-collaboration]
---

# Message Corpus — Circadian Rhythm, Reply Latency, and Volume Trajectories

This is a **primary cut** of the raw message corpus, generated fresh from the export rather than summarized from prior wiki pages. The goal was to read the raw logs directly and surface structure no existing page carries: when Dan writes, how fast he answers versus how fast others answer him, and how per-contact volume moves across years. Source is the full iMessage/SMS corpus — `MASTER_MESSAGES_DB_DUMP.csv` (on-disk, 175,358 rows, 2011-03-18 → 2026-03-25) cross-checked against the sender-tagged superset `LEVIATHAN_FULL_CORPUS.csv` (`/Volumes/MUSIC/PHASE B RAW/`, 181,650 rows, 2011-03-18 → 2026-06-09). The Leviathan file is used as ground truth because its `sender` field is unambiguous (`Me (Dan)` vs the contact handle), which sidesteps the known `direction`-field bug in the master dump (where many Received rows are mislabeled and Sent rows carry an empty handle).

> **Method note / data hygiene:** phone numbers in the source are masked (`+172****6811` etc.). Matching was done by **substring on the file's actual bytes** (e.g. `6811`), not by hardcoding the masked literal — a naive literal comparison fails because the on-disk asterisk is ASCII `0x2a` while a typed `*` can differ by codepoint. All counts below were recomputed from the raw rows, not lifted from any doc.

## The headline: a 9× reply-latency asymmetry with Annie

The single most diagnostic new finding is the gap between how fast Dan answers and how fast the other person answers *him*.

| Pair | Dan → them (median) | Them → Dan (median) | Dan → them p90 | Them → Dan p90 | n (Dan replies) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Annie** (merged handle, 2015–18) | **1.0 min** | **9.0 min** | 0.7 h | 4.2 h | 31,612 |
| +172****4125 (2019) | 2.0 min | 19.0 min | 4.2 h | 15.8 h | 5,684 |
| +172****3678 (2018) | 4.0 min | 22.0 min | 3.6 h | 9.0 h | 3,626 |
| +172****8715 (long-tail) | 3.0 min | 346.0 min (~5.8 h) | 6.4 h | 43.7 h | 221 |
| +121****2449 (2025–26) | 5.0 min | 2,648 min (~44 h) | 8.2 h | 142.7 h | 2,120 |
| +133****8747 (2025) | 1.0 min | 968 min (~16 h) | 0.3 h | 69.0 h | 3,446 |

Dan answers almost everyone within **1–5 minutes**. The people he messages answer him on a completely different clock: Annie at 9 minutes (already 9× his speed), the 2018–19 friends at 19–22 minutes, and the 2025 contacts at **16 to 44 hours**. This is the attachment system made audible as a timing series. Dan's outbound responsiveness is uniform and near-instant across every relationship — the *inbound* delay is what differentiates them, and it scales with how peripheral the person is. The near-synchronous Annie channel (median 9 min both ways) is the relational singularity; everything else is Dan broadcasting into a slow or silent void.

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

## Volume concentration (re-derived, matches prior Gini)

Across the corpus, Annie's two handles dominate. This primary cut re-confirms the [[wiki/mind/concepts/contact-gini|Contact Gini]] finding from raw: of Dan's 70,123 sent messages, the top contact (+172****6811) alone is 31,635 (45%). The next tier (+172****4125, +172****3678 in 2018–19; +133****8747, +121****2449 in 2025) are each bounded single-year spikes — friendships or entanglements that flare for one period then vanish from the log. The steady state is one channel at 45%+ and everything else as transient satellites.

## What this adds that no existing page had

- A quantified **reply-latency asymmetry** (Dan ~1–5 min vs others 9 min to 44 h) as a direct measure of relational centrality — the inbound delay is the axis of differentiation, not the outbound speed.
- The **merged Annie 2015–2018 volume arc** with the 2019 export-cliff called out as an artifact, not a silence.
- The **circadian curve** and its **era drift** (15.5% → 10.4% nocturnal) — entirely new timing data.
- The **62.7% sub-2-minute burst rate** and 284-message max run — the output-storm fingerprint.

## Gaps / caveats

- Annie's 2019–2024 volume is not in this file (handle/export seam); the true decade arc needs the ANNIETEXTS / combined_annie_logs exports merged in. The 2019 "2 messages" is an export boundary, not a real gap.
- Reply-latency uses the "next opposite-speaker message in the same thread" method. In high-burst threads this slightly over-states Dan's reply speed (he may send 10 then get 1 back) but the *order-of-magnitude* asymmetry is robust across every contact.
- Phone handles are masked; identity of the non-Annie contacts (+133****8747 = a 2025 figure; +121****2449 = a 2025–26 figure) is inferred from volume timing and the wiki's existing people pages, not from unmasked data.
- `LEVIATHAN_FULL_CORPUS.csv` lives in `/Volumes/MUSIC/PHASE B RAW/`, not yet filed under `raw/` — its on-disk path is cited directly above.
