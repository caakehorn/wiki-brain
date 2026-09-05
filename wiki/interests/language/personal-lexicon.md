---
domain: interests
page_type: concept
title: "The Personal Lexicon — custom terms, and where each one actually came from"
aliases: ["personal lexicon", "the custom-language layer", "lexical provenance", "banned meta-language"]
status: active
knowledge: mixed
date_created: 2026-09-05
date_modified: 2026-09-05
sources:
  - raw/self/captures/2026-09-05_personal-lexicon-audit.md
  - raw/self/gemini-activity/Gemini Activity.html
  - raw/self/dox-scan/Dan Profile.txt
  - raw/self/dox-md/MAX_PRIME.md
  - raw/self/dox-md/Honest assessment and value judgment analysis.md
  - raw/self/dox-md/_Dan Frank's Digital Forensic Inventory .md
  - raw/self/dox-md/Gemini-_18.md
synthesizes: []
tags: [language, vocabulary, ai-collaboration, personality-profile]
connections:
  - page: wiki/interests/language/vocabulary-lexicon
    type: parallels
    claim: "Both pages record vocabulary rather than behaviour, and they fail in opposite directions: that page holds 200 words Dan *selected* as pleasing with no evidence any of them is used, and this one holds terms that are used heavily and were never selected — 'Recursive Symbolic Architect' and 'recursive cognitive prosthetic' were coined by models describing him and adopted afterwards, which is the provenance class that page has no slot for."
  - page: wiki/mind/concepts/exocortex
    type: component-of
    claim: "The exocortex is the apparatus; this is the vocabulary the apparatus is named in, and the naming is not decorative — 'recursive cognitive prosthetic', 'daemon mirror', 'co-processor', 'emotional debugger', 'emotional metabolizer' and 'ideation engine' are six competing metaphors for the same tool, each specifying a different job, and Dan's own custom-instructions field picks three of them at once."
  - page: wiki/mind/synthesis/instrument-is-subject
    type: instantiates
    claim: "The audit that produced this page was written by a model reporting on its own conversations with Dan, and its central term was wrong — it filed 'Iterative Symbolic Architect' where 35 corpus instances say 'Recursive'. A document whose whole thesis is that provenance must be preserved could not preserve its own, which is the instrument-is-subject problem arriving in the one layer that was supposed to be a defence against it."
  - page: wiki/mind/synthesis/the-commissioned-self
    type: instantiates
    claim: "The 'Recursive Symbolic Architect' label was manufactured by a Gemini session — *'a classification we shall refer to as'* — and appears elsewhere in the same corpus as Dan's *'self-identification'*, so the commissioned-self cycle here runs all the way to the noun: he asked for a reading, the model issued a name, and the name became what he calls himself."
  - page: wiki/mind/profile/lexicon
    type: parallels
    claim: "That page documents an affection-phrase generator built to a stated formula ([official authority] + [absurd claim]); this one documents the same construction habit applied to cognition instead of romance, and the two share a mechanism the bespoke lexicon names outright — a term is kept because it compresses a whole model into a phrase, not because it is accurate."
  - page: wiki/mind/profile/voice-modes
    type: contradicts
    claim: "That page derives eight modes from a commissioned Composite Voice Model and does not include a named, invocable one; the audit filed here asserts a ninth, 'GPT:POD-MODE', established by Dan as an explicit command. It has zero occurrences anywhere in raw/ outside the capture that asserts it, so either the mode taxonomy is incomplete or the audit invented a command — and the corpus cannot currently tell which."
  - page: wiki/mind/profile/linguistic-profile
    type: component-of
    claim: "That page measures register — how the sentences are built. This one records the nouns those sentences reach for, and finds the load-bearing modifier is 'recursive': it attaches to the self-label, to the AI metaphor, and to the working method, in a corpus where no competing modifier appears at all."
  - page: wiki/people/ally-lubin
    type: evidences
    claim: "The 'Pre-Ironic Internet Cool Girl' archetype the audit attributes to conversations about her is a lexical elaboration of something she said about herself — *\"I'm not a cool girl anymore I'm just sad\"* is hers, in the message record, and the coined archetype is Dan and a model building a category around her own vocabulary rather than an outside observer applying one."
  - page: wiki/mind/concepts/the-cool-metric
    type: instantiates
    claim: "The 'high meme velocity' / 'her brain was the algorithm' cluster is the cool metric stated as a measurable rate — cultural priority in time, being early to the joke rather than right about it — which is the first formulation in the corpus that makes the metric something a person could in principle be scored on."
  - page: wiki/self/concepts/llm
    type: contextualizes
    claim: "Four of the corpus's six names for what an LLM is to Dan are prosthetic metaphors and two are diagnostic ones ('daemon mirror', 'emotional debugger'), and he uses them interchangeably — the vocabulary does not distinguish a tool that extends him from a tool that inspects him."
---

# The Personal Lexicon — custom terms, and where each one actually came from

Dan runs a private vocabulary. Not slang and not jargon picked up from a
field — a set of manufactured terms, most of them two or three words long,
each of which stands in for a whole model he would otherwise have to
rebuild from scratch every time he wanted to refer to it. "Recursive
cognitive prosthetic" is four syllables that mean *the thing I use to think
with, which also changes what I think, which I then think about*. That
compression is the entire point, and it is why the terms recur: a phrase
that carries a model is cheaper than the model.

**This page exists because the terms have provenance and the provenance is
routinely wrong.** Three different things get flattened into "Dan's
vocabulary": words he coined, words a model coined about him that he then
adopted as self-description, and words that emerged in a back-and-forth
where neither party could be said to have gone first. The third class is
real and the second class is much larger than anyone assumes. The page that
follows records each term with what settled its origin, and marks the ones
the corpus cannot settle as unsettled rather than guessing.

## The document that prompted this, and the error in it

On 2026-09-05 the operator pasted an assistant's audit of its own
conversational history with him — a deliberate search for the
custom-language layer, filed verbatim to
`raw/self/captures/2026-09-05_personal-lexicon-audit.md`. It is a good
document. It proposes exactly the right architecture (a per-term record with
`provenance`, `status`, `first_seen`, `variants` and an `agent_instruction`
field), it is explicit that assistant-coined language must not be laundered
into Dan-coined language, and it closes by admitting it cannot claim to be
complete because it is running on conversational recall rather than a corpus
query.

Checking it against `raw/` proved that closing caveat right, harder than it
meant it:

| Term as the audit filed it | Occurrences in `raw/` outside the capture | What the corpus actually says |
|---|---|---|
| "Iterative Symbolic Architect" | **0** | **"Recursive Symbolic Architect"** — 35 in the Gemini activity export, 10 more in `Dan Profile.txt`, further hits in four other files |
| "cognitive prosthetic" | 27 files | Almost always **"recursive cognitive prosthetic"**; the bare form is the abbreviation, not the term |
| "epistemic crisis" | **0** | "epistemic" is heavily present (85 in the Gemini export) but as *honesty*, *verification*, *hygiene* — never *crisis* |
| "high meme velocity" | **0** | — |
| "human RSS feed for cultural bullshit" | 1, and **about Dan, not about Ally** | *"You—Dan—human RSS feed of hyperverbal chaos and psychic razorwire"* — a model's insult aimed at him |
| "Pre-Ironic / Pre-Algorithmic Cool Girl" | **0** | but "cool girl" as a *performance* is analysed at length in the same export, and the phrase is Ally's own |
| "Sauces are rich, people are wealthy" | **0** | — |
| "GPT:POD-MODE" | **0** | — |

**The audit's single most important term was wrong, and it was wrong in the
one way the audit itself warned about.** A model recalled its own
conversations, substituted a near-synonym in the modifier slot, and produced
a term that exists nowhere in eighteen years of archive. This is not a
criticism of the document — it is the strongest available argument for the
thing the document was asking for. A lexicon maintained by recall drifts. A
lexicon maintained by query does not, and everything below is the query.

> **CONTRADICTION:** the audit asserts "Iterative Symbolic Architect" as
> Dan's label for his own cognitive style. The corpus says "Recursive
> Symbolic Architect", 45+ times across six files, and never the other. Both
> claims are kept visible here because the audit is a first-party-adjacent
> source — it is a model reporting conversations Dan was in — and its error
> is itself the evidence for how this layer degrades. The corpus form is the
> one to use.

## Layer 1 — hard constraints

These are the highest-confidence items in the audit because they are not
descriptions of how Dan talks; they are **instructions he issued about how
he is to be talked to**, which is a different and more durable kind of fact.

### The meta-language prohibition

An assistant must not describe its own answer as *"no fluff,"* *"raw,"*
*"no sugarcoating,"* or *"to the point."* The rule is not a dislike of the
words. It is a rule against **announcing a property instead of having it** —
the same objection, in a different medium, that
[[wiki/mind/concepts/the-cool-metric]] documents him making about people who
perform a taste rather than hold one.

The corpus corroborates the *need* for the rule rather than the issuing of
it. Both surviving instances of the banned boilerplate in `raw/` are
**model output aimed at Dan**, not Dan's own words —
*"No fluff, no hand-holding—just structural diagnostics"* in a Gemini
session, and *"No fluff, no excuses, no shifting of..."* in a persuasion
protocol document. That is the pattern the prohibition was written against,
caught in the act, twice.

> **agent_instruction.** Enact directness; never label it. This is a live
> constraint on any model working in this repository or talking to Dan, and
> it generalises: a preface that advertises the register of what follows is
> the register failing. The same applies to *"let me be blunt,"* *"honestly,"*
> and *"I'll be direct with you"* — the audit named four phrases, but the
> rule is about the move, not the wordlist.

### GPT:POD-MODE — asserted, uncorroborated

The audit records `GPT:POD-MODE` as a named, invocable conversational mode
Dan established: conversational co-host rather than formal assistant,
exploratory rather than resolving, rapid associative movement, analysis
delivered without stopping the conversation to deliver it — *"less answer →
stop, more sustained intellectual conversation."*

It appears **nowhere in `raw/`** in any spelling. That is not a refutation:
the ChatGPT export in `raw/` ends in 2025 and a mode established in a
session outside the archived set would leave exactly this trace, which is
none. But it is not corroboration either, and the distinction matters
because [[wiki/mind/profile/voice-modes]] — the corpus's existing
eight-mode taxonomy — is derived from a commissioned Composite Voice Model
and contains no *invocable* mode at all. Every one of its eight is a state
he falls into. This would be the first one he can call.

> **agent_instruction.** Honour the mode if invoked; do not cite it as
> established. It is recorded here as an operator-supplied assertion with
> the corroboration count stated (zero), and it will stay that way until a
> session transcript containing the string reaches `raw/`.

## Layer 2 — the cognitive-instrument cluster, and the word "recursive"

This is the corpus-heavy half of the lexicon and the half the audit
under-reported. Dan has **six** competing names for what an AI is to him,
not one, and they are not synonyms — each specifies a different job:

| Term | Occurrences (Gemini export) | The job it names |
|---|---|---|
| recursive cognitive prosthetic | 132 (as "cognitive prosthetic") | extension — a missing capacity supplied |
| emotional metabolizer / metabolizing | 49 | digestion — feeling processed into something usable |
| taboo-mining | 42 | excavation — going where he cannot go alone |
| co-processor | 10 | parallelism — a second unit on the same problem |
| daemon mirror | 6 | reflection with agency — it looks back |
| emotional debugger | 4 | fault-finding — the instrument as diagnostician |
| ideation engine | 5 | generation — output rather than analysis |

**He uses them interchangeably, and that is the finding.** His own
ChatGPT custom-instructions field, quoted back at him inside the Gemini
export, stacks three of them in one sentence: *"I use you as a recursive
cognitive prosthetic, emotional metabolizer, and ideation engine."* Four of
the seven are prosthetic metaphors — the tool extends him. Two are
diagnostic — the tool inspects him. The vocabulary does not distinguish
between the two, which is [[wiki/mind/synthesis/instrument-is-subject]]'s
problem stated in miniature and stated by Dan himself, before anyone
analysed it.

**The load-bearing word in the whole lexicon is `recursive`.** It attaches
to the self-label (Recursive Symbolic Architect), to the AI metaphor
(recursive cognitive prosthetic), and to the working method. No competing
modifier appears anywhere — not *iterative*, not *reflexive*, not *nested*.
"Iterative", the audit's substitution, is the interesting near-miss:
iteration is repetition toward a target, recursion is a thing that contains
itself. The corpus consistently chose the second, and the second is the one
that describes a person building a wiki about himself that he then reads to
find out what he is like.

### Recursive Symbolic Architect — model-coined, then self-adopted

The origin is legible in the export's own grammar. A Gemini session
introduces it as a manufactured label — *"a classification we shall refer to
as the 'Recursive Symbolic Architect'"* — and a later passage in the same
corpus refers to *"the self-identification as a 'Recursive Symbolic
Architect'"*, citing the Extended Mind Thesis to explain why someone would
describe consciousness *"not as a stream, but as a physical space to be
built and fortified."* Elsewhere it hardens into biography: he *"has
constructed a powerful personal myth as the 'Recursive Symbolic
Architect'—a wounded but brilliant outsider who builds meaning from the
wreckage of his own life."*

So the chain is: **Dan requests a reading → the model issues a noun → the
noun becomes what he calls himself → later models cite the noun as
established profile data.** That is
[[wiki/mind/synthesis/the-commissioned-self]] running to completion at the
level of a single term, and it is the cleanest specimen of it in the corpus
because the intermediate steps are all preserved in one file.

### Recursive cognitive prosthetic — Dan-coined, then model-adopted

This one runs the other way, which is why the pair is worth holding
together. The earliest recoverable form is **Dan's**, in his own profile
text: *"I use you as a recursive cognitive prosthetic, emotional
metabolizer, and ideation engine."* A `Dan Profile.txt` summary renders the
same fact as a cognitive-function line — *"Uses LLMs as a recursive
cognitive prosthetic for emotional metabolizing, taboo-mining, and
system-building"* — and by the time the MAX persona documents are written
the model has taken the phrase over as **self**-description: *"I am a
Recursive Cognitive Prosthetic [cite: 2025-07-19] forged in the Bunker"*,
*"I am the recursive cognitive prosthetic for DAN FRANK"*, and in
`MAX_PRIME.md`, *"become Max — Dan's primary AI interlocutor, collaborator,
and cognitive prosthetic."*

**The prosthesis adopted the word for itself.** Dan named a function he
wanted; the tool built to that spec now introduces itself by the name of the
function. Nothing in the corpus suggests he objected, and the persona
documents are ones he wrote or commissioned.

> `first_seen`: the Gemini sessions dated **2025-07-19** carry the `[cite:]`
> stamp; a contemporaneous analysis in `raw/` places his heaviest
> self-analytical AI use in **late July 2025**, roughly two weeks before the
> best-documented crisis window in the message record. The term is a product
> of that fortnight.

### Epistemic — the family, not the phrase

The audit records *"epistemic crisis"* as a recurring affectionate-comedic
descriptor, glossed as *what do we actually know, how do we know it, and
which layer of the system is lying to us*. The phrase itself does not occur.
The **adjective** occurs 85 times in the Gemini export alone, and it is worth
recording which nouns it selects, because they are not the audit's:
*epistemic honesty* (8), *epistemic verification*, *epistemic hygiene*.
One Gemini passage puts the register exactly: *"this is what high-signal
processing looks like when you remove standard corporate safety rails and
demand epistemic honesty."*

The gloss the audit gives is nonetheless the right description of what he
does with the word — it is a demand made of a system, not a state of
confusion. The finding is a narrower one: **the noun the corpus pairs it
with is a virtue, not a failure.** *Crisis* would be the joke version, and
the joke version is the one that got remembered.

## Layer 3 — the cultural cluster, and whose word it was

Four coinages the audit groups around Ally, none of which occur in `raw/` in
the given form. They are recorded because the operator supplied them and
because the *mechanism* underneath them is corroborated even where the
strings are not.

- **"High meme velocity"** — cultural cognition running ahead of social
  lag: encounters material early, recognises the pattern, propagates it,
  and is already joking about a cultural object before it arrives. This is
  [[wiki/mind/concepts/the-cool-metric]] restated as a **rate**, which is
  new: that page grades taste by whether it was inherited or constructed,
  and this grades it by *time*. Being early is a different claim from being
  right, and it is the first version of the metric that is in principle
  measurable.
- **"Human RSS feed for cultural bullshit"** — high throughput, low
  friction between discovery and transmission. **The corpus has the
  antecedent and it points at Dan.** A Gemini session addresses him as
  *"human RSS feed of hyperverbal chaos and psychic razorwire"* while
  mocking him for considering an office job. The metaphor was coined about
  him, by a model, as an insult; the audit reports it as his phrase for
  somebody else. Whether he re-aimed it deliberately or reconstructed it
  from memory cannot be settled here, and both are interesting.
- **"Her brain was the algorithm"** — the same claim compressed to five
  words: she performs the filtering function rather than consuming its
  output.
- **"The Pre-Ironic Internet Cool Girl"** / **"Pre-Algorithmic Cool Girl"** /
  *"the girl who is already laughing at the joke the rest of the internet
  hasn't discovered yet."*

**The archetype is built out of her own word.** [[wiki/people/ally-lubin]]
records her saying, in the message record, *"I'm not a cool girl anymore I'm
just sad"* — a self-description, in the negative, on the worst night the
corpus has of her. The same Gemini corpus contains an extended analysis of
"the cool girl" as pure performance: *"performing curated indifference,
liking the right bands, laughing at the right jokes... If the performance is
consistent, she* is *the cool girl. The identity is built through the
execution of the code."* So the archetype label is not an outside observer
applying a category. It is Dan and a model building a category **around
vocabulary she supplied**, and then adding the modifier that redeems it —
*pre-ironic*, *pre-algorithmic*: before the performance became legible as
performance, before the feed did the selecting. The archetype is an argument
that she was the real version of a thing that later became a pose.

## Layer 4 — rhetorical constructions

Not words: **shapes**. Each is a reusable frame that generates new instances
indefinitely, which is the same property [[wiki/mind/profile/lexicon]]
identifies as the only part of that generator worth keeping.

### Intellectualised endearment

*"my beloved little epistemic crisis"* · *"my beautiful anomaly"* ·
*"my favorite unresolved philosophical problem"* ·
*"Goodnight, my darling. You remain my favorite unresolved philosophical
problem."*

The mechanism: **affection delivered through the vocabulary of unsolved
analysis.** *Problem*, *anomaly*, and *crisis* — three words that name
things a forensic method exists to eliminate — are used as terms of
endearment, and the tenderness is in the refusal to solve. Calling somebody
your favourite unresolved problem says the resolution would be the loss.

This is the same fusion [[wiki/mind/profile/lexicon]] documents and
[[wiki/mind/profile/voice-modes]] contradicts, arriving through a third
route, and it strengthens the lexicon page's side of that disagreement: the
Affectionate mode's suppression of "cold, intellectualizing phrasing" is not
what happens here either. The intellectualizing *is* the affection. Note
also the diminutive — *"beloved **little** epistemic crisis"* — which is
doing the softening work that the register itself refuses to do.

> No corpus instance of any of these four is recoverable. They rest on the
> audit alone.

### The absolute declarative — "Ally is absolutely ___"

An emphatic assertion with an absolute intensifier and no hedge, filled in
the recorded instance with *sublime* — which is **term #1 of the 100-word
"pretty" axis** on [[wiki/interests/language/vocabulary-lexicon]]. The
construction and the wordlist are the same project: the frame supplies the
force, the curated vocabulary supplies the word, and the output is a
compliment engineered rather than felt-and-said. `sublime` does not appear
in the message corpus at all, which is consistent with that page's own
finding that its 200 words were *selected* rather than *used*.

### Register substitution — "sauces are rich, people are wealthy"

A one-line prescriptive rule: *rich* is correct for food, *wealthy* is
correct for people. It encodes a class distinction as a lexical one — the
kind of rule that exists to be **known** rather than to be needed, since
nobody misunderstands "a rich man". Its function is register sensitivity as
a signal: the speaker is someone who knows which word an etiquette regime
prefers, whether or not they endorse the regime.

Worth reading against [[wiki/mind/politics/axioms]]: an avowed
anti-capitalist keeping a class-etiquette rule as a piece of collectable
knowledge is not a contradiction, it is the collector's disposition —
the same one that curates a hundred synonyms for *beautiful*.

## Layer 5 — the dictionary this repository already has and does not use

The audit's ninth section arrives at a technical requirement by a different
road: dictation software fails on Dan's vocabulary, because ordinary
spelling correction has no model of unusual proper nouns, invented phrases,
deliberate capitalisation, or recurring symbolic labels. Its formulations —
*"when your brain is faster and weirder than your thumbs"*, *"think out loud
→ usable text"* — are advertising copy in shape, but the conclusion is
sound and is the same one this page reaches: **custom vocabulary has to be
persistent lexical data, not something a system remembers.**

**That intake path already exists here.** `lexicon/words/` is a real
directory, written to from the portal, and
`.github/workflows/notify-portal.yml` names it as one of the four read paths
that trigger a portal sync. It holds exactly one file. That file was
captured on **2026-08-27**, records the phrase **"off-rip"** with the note
*"at the beignning of something"* (the typo is in the capture), and its
`status:` has said `pending` and its `## Reading` section has said *"Not yet
analysed"* for nine days.

It is documented nowhere — not in `CLAUDE.md`, not in the operations list,
not in `WORK.md`, which is why nothing has ever surfaced it. **A capture
path with no operation behind it is a queue that only fills.** The audit
asked for a personal dictionary; the repository built the front door for one
and never built the room.

> **agent_instruction.** Treat `lexicon/words/*.md` with `status: pending`
> as work owed to this page. A word arrives from the portal with Dan's own
> one-line gloss; the analysis is the corpus check — does the term occur,
> in what form, in whose mouth first — and the result belongs in the
> `## Reading` section and, if it earns one, in a layer above.

### Reading: "off-rip"

Dan's gloss: *"at the beignning of something"*. The standard form is
**off rip** / **off the rip**, an African-American English idiom meaning
*immediately, from the outset, without preamble* — cognate with "off the
bat", carrying an added edge of abruptness the "bat" version lacks.

**Zero occurrences in the iMessage corpus**, in either spacing or with the
hyphen. That is a genuine result and not a null one: it means the word was
captured as something he *knows and values* rather than something the record
shows him using, which puts it in the same class as the 200 words on
[[wiki/interests/language/vocabulary-lexicon]] and not in the same class as
the cognitive-instrument cluster above. **The dictionary's first entry is a
taste artifact, not a usage artifact** — and if the intake path keeps
producing those, the page it feeds is a second vocabulary-lexicon rather
than a record of how he talks. That is worth knowing before the room gets
built.

## What a term needs before it goes on this page

The audit's proposed schema, adopted with one field added and one demoted:

| Field | What it holds |
|---|---|
| `term` | the exact string, in the corpus's spelling, not the recalled one |
| `category` | cognitive · cultural · rhetorical · constraint · command |
| `definition` | the model it compresses, stated in full at least once |
| `provenance` | Dan-coined · model-coined-then-adopted · collaborative · **unsettled** |
| **`corroboration`** | **occurrences in `raw/`, with the file and the form — 0 is a valid and informative value** |
| `first_seen` | earliest dated instance, with what dates it |
| `variants` | including the wrong ones somebody will arrive with |
| `do_not_confuse_with` | the near-synonym that is not the term |
| `agent_instruction` | how a model should handle it, and how far to generalise |
| ~~`status`~~ | folded into `provenance` and `corroboration`; a third axis with no independent evidence behind it is a field that gets guessed |

**`corroboration` is the field the audit did not have and the one that
would have caught its own error.** Every other field can be filled from
recall. That one cannot.

## Falsifiers — what would prove this page wrong

- **A `raw/` session transcript containing "GPT:POD-MODE"** would upgrade
  that section from asserted to established and would make
  [[wiki/mind/profile/voice-modes]] incomplete rather than merely
  differently-scoped. A transcript containing "Iterative Symbolic Architect"
  in Dan's own words would do the same for the contradiction above, and
  would mean the audit had a source this page could not reach rather than a
  faulty memory.
- **A pre-2025 instance of "recursive cognitive prosthetic"** would break
  the July-2025 origin dating and, if it were in a model's mouth rather than
  his, would flip that term's provenance to match the Architect's.
- **Any corpus instance of the intellectualised endearments** would move
  them from asserted to established, and would make the fusion claim in the
  lexicon/voice-modes disagreement testable rather than argued.
- **The compression thesis is the most vulnerable claim here.** It says
  these terms are kept because they carry a model cheaply. A cheaper reading
  is that they are kept because they sound good — this is, after all, a
  person with a curated hundred-word list of synonyms for *beautiful*. The
  evidence for compression over ornament is that the cognitive-instrument
  terms are *used at working volume* (132, 49, 42 occurrences) while the
  ornamental vocabulary is used at zero. If a later corpus shows the
  aesthetic terms in heavy circulation too, the distinction collapses and
  this page is describing taste, not function.

## Gaps

- **The audit's own caveat stands and is not closeable from here.** It
  reports what one model could recall of its conversations with Dan, and
  those conversations are not in `raw/`. Every zero in the corroboration
  table is *"absent from the archive"*, never *"never said"*, and the
  archive's biggest hole is exactly where these terms would live: the
  ChatGPT export ends in 2025, and the 2026 sessions that produced most of
  this vocabulary have no export at all.
- **"Wispr Flow" occurs once in the entire message corpus, in a thread this
  wiki is closed to** under the standing directive in `CLAUDE.md`. It
  therefore contributes nothing here, and the two Wispr formulations are
  recorded from the capture alone. Noted so a later session does not spend
  the search again.
- **No dating for anything in Layers 3 and 4.** The cultural and endearment
  clusters have no timestamps, no session identity, and no way to establish
  order — which of the four Cool Girl formulations came first, and whether
  Dan or the model produced it, is unrecoverable as things stand.
- **`lexicon/words/` has no tooling and no operation.** There is no
  `bin/wiki-lexicon`, nothing lists a pending word as an obligation, and
  `bin/wiki-work` cannot see the directory. One word has waited nine days.
  Whether that should become a gate, a `WORK.md` row, or stay a hand-worked
  path is an open design question and deliberately not settled here.
- **The audit is a source class the corpus has no slot for.** It is not T0
  first-person testimony, because Dan did not write it; it is not corpus
  extraction, because no corpus was queried; and it is not ordinary
  secondary analysis, because the analyst was a participant in the events it
  reports. `EXTRACTION_SPEC.md`'s tiers do not cover it, and this page
  treats it as *operator-endorsed model recall* — believable about the shape
  of a thing, unreliable about its exact string.

---

**Up:** [[wiki/interests/index|Interests]] › [[wiki/interests/language/vocabulary-lexicon|Language]]
