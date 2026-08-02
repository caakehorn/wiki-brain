# Message-Density Campaign

**Standing objective (operator, 2026-08-02):** scrape the full message logs for
new nodes and new data points, cross-reference the corpus against standing wiki
claims to corroborate or falsify them, and raise the density of **`mind/` and
`self/`** — aiming at conclusions of the *"time = countdown"* kind: compact,
load-bearing, falsifiable statements about how this mind works.

Instrument: **`bin/mine-messages`** (pure stdlib). Read its docstring before
using it; it exists because three properties of the dump make naive `grep`
silently wrong, and each of them has already produced a false measurement.

---

## The corpus, and which file to use

`raw/self/dox-scan/all_imessages_complete_dump.txt` is the **only** message
source with trustworthy direction. `MASTER_MESSAGES_DB_DUMP.csv` marks nearly
everything `Received`; any claim about what *Dan* said must come from the dump.

```
records 217,573  ·  sent 106,629 (4,554,904 chars)  ·  received 110,944  ·  503 handles
2015  7,634 S     2016 17,311 S     2017 10,950 S    2018 24,081 S    2019 11,606 S
2020  4,908 S     2021    599 S     2023  2,346 S    2024 12,746 S    2025 14,447 S
```

**2022 and 2026 are absent entirely.** Nothing mined here speaks to the terminal
phase, the June 2026 closure, or the July 2026 re-contact. Those live in the
per-thread exports under `raw/self/message-csv/`.

## The three traps

1. **Multi-line messages.** A record begins `TS|Sent|handle|…`; everything until
   the next such header belongs to it. Line-based grep miscounts and truncates.
2. **Curly apostrophes outnumber straight ones 28,904 to 19,978** in Dan's sent
   text. A pattern written `i'm` misses most of its own matches. `mine-messages`
   normalises; hand-written greps do not.
3. **Counting without reading.** See the method note below. This one cost a
   near-miss finding.

## Method: the inbound baseline is not optional

The corpus contains its own control. Every rate computed for Dan's outbound text
should be computed for the 110,944 inbound messages from 503 other people and
reported as a **ratio**, because most "findings" about how Dan writes are
actually findings about how people text.

The first pass demonstrated why. Raw counts made Dan look strikingly
un-introspective — "the thing about me" appears **zero** times in 106,629
outbound messages. Against the baseline it evaporates: it appears zero times
inbound too. SMS is a near-zero-introspection medium for everyone in it. What
survived the control was different and much sharper (below).

> **METHOD NOTE — read your matches before believing your counts.** The first
> run scored "age self-reference" at 3.82× baseline and nearly became a finding
> about the countdown axiom being experienced as *position rather than urgency*.
> The pattern was catching **"I'm 99% sure"** — percentages, not ages. Corrected,
> real age self-reference is n=8 across eleven years, half of it escort-ad
> boilerplate. Every lexical result in this campaign must be spot-read before it
> is written down.

---

## Findings so far

### 1. Calibrated confidence — CONFIRMED, 22× baseline
[[wiki/mind/concepts/calibrated-confidence]]. Dan attaches **graded numeric
probability to his own beliefs** in casual SMS: 43 instances, of which 15 use
values that are not 0/50/100 (75, 80, **89**, 90, 95, 99.9999). Across 110,944
inbound messages there are **2**, both plain "100%" used as a synonym for
*definitely*, and **zero** graded values. Survives all three controls: spread
across 12 handles, present in every year 2015–2025, and bare-percentage usage
generally runs at only 1.36× so it is not numeracy. First behavioural evidence
for Ti-dominance that does not come from an instrument or an AI session.

### 2. The four core axioms — NOT corroborable from messages
Recorded on [[wiki/self/context-core]]. *time = countdown* predicts urgency
language; Dan writes **less** of it than his correspondents ("running out of
time" 0.35×, "deadline/last chance/now or never" 0.42×, "before I die/turn/lose"
0.00×). "Rest of my life" looked like support at 3.5× until read: all twenty
hits are 2015–16 love-declarations to Annie.

This is **not** a falsification — unconscious axioms are not things people type —
but it establishes a jurisdiction. The spine says all behavioural data defers to
the message corpus; for behaviour that holds, for the psychological layer the
corpus is silent, and the axioms rest on AI-session dossiers alone.

---

## Backlog, roughly by expected value

1. **Test prediction 1 of `calibrated-confidence`.** Run the graded-confidence
   pattern over the Facebook Messenger export, `gmail_bodies.txt`, and the
   `raw/self/chats/` AI sessions. If Dan sits at inbound baseline in another
   channel, the finding is about iMessage, not about him, and must be narrowed.
2. **Hedging study.** The 43 hits come from one pattern. *"odds are," "there's a
   good chance," "I'd bet," "probably," "I doubt"* are unmeasured and would put
   the finding on a far larger base.
3. **New nodes.** `bin/mine-messages entities` currently drowns in bank alerts
   and brand names; it needs a spam filter. Real candidates already surfaced,
   none of which has a page: **Lucy** (67 msgs, 2015–18), **Ricky** (66,
   2015–20), **Libby** (83, 2024–25), **Alice** (50, 2023–25), **Derrick** (29),
   **Michelle** (31). Each needs the one-page-per-entity check against aliases
   before anything is written.
4. **"supposed to be" at 2.17× (n=123).** The best-powered unexplained
   divergence in the battery. An obligation/expectation frame running at twice
   baseline is a `mind/` finding waiting to be read.
5. **Behaviour, not vocabulary.** The corpus's real strength for `mind/` is what
   Dan *did* while unobserved — latency, initiation, abandonment, escalation,
   time-of-day. `message-circadian-latency` and `contact-gini` are the model.
   Lexical passes have now hit diminishing returns; the next big finding is
   probably behavioural.
6. **Corroboration sweep.** `OPEN.md` lists every live contradiction, gap and
   standing prediction. Many name a number or a date the corpus could settle.
   Work it top-down with `mine-messages grep`.

## Protocol for adding a finding

Same bar as everything else in the repo: a claim that survives being read cold,
with its control stated, its `n` visible, and a falsifier. State the negative
results too — finding #2 above is a negative and it changed how the spine should
be read. Log the pass in `log.md`, wire typed edges both ways
(`CONNECTIONS_SPEC.md`), and run all three gates.
