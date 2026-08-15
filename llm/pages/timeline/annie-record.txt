---
domain: timeline
page_type: chronology
status: active
knowledge: earned
date_created: 2026-08-15
date_modified: 2026-08-15
sources:
  - exports/annie-corpus.csv (built by bin/annie-corpus from the sources below)
  - raw/self/message-csv/imessage_7244346811+7249204125+2124702449_both_all_now.csv
  - raw/self/message-csv/imessage_7244346811_both_all_now.csv
  - raw/self/message-csv/imessage_2124702449_both_all_now.csv
  - raw/self/message-csv/imessage_ALL_both_all_now.csv
  - raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv
tags: [timeline, annie, chronology, primary-source]
connections:
  - page: wiki/people/annie-ulmer
    type: evidences
    claim: "The day-by-day event record of the relationship, read directly out of the 97,768-message two-sided corpus rather than inferred from dossiers — this is the evidentiary floor the Annie page's claims are supposed to rest on."
  - page: wiki/timeline/index
    type: component-of
    claim: "The hand-read chronology of the single relationship that dominates the corpus, kept separate from the mechanically generated master timeline because its entries are read and judged rather than extracted."
---

# The Annie Record — a read chronology

Every event here was found by **reading the messages**, in order, in small
windows. Nothing on this page was pattern-matched or extracted by a script.
That is the point: the two mechanical attempts at a timeline (2026-08-14 and
its 2026-08-15 replacement) both produced pages where a large share of the
"events" were prose fragments, edit stamps and corpus metadata, because a date
next to a sentence is not an event and no regex can tell the difference.

**Method.** `bin/annie-corpus build` merges every export carrying Annie traffic
into one de-duplicated, chronologically sorted corpus; `bin/annie-corpus read
FROM TO` prints a window. A window is read in full, the events in it are
identified by judgement, and each is written down with the verbatim line that
establishes it. Where a reading is uncertain it says so.

## What the record actually covers

**97,768 unique messages, 2015-11-28 → 2026-06-05**, across Annie's four
handles — `+17244346811` (2015-11 → 2018-12), `+17249204125` (2018-12 →
2020-06, opened with *"I texted her yesterday from my new number!"*),
`alulmer28@gmail.com` (2020-07 → 2020-10), and `+12124702449` (2022, then
2025-03 → 2026-06).

| Stretch | Coverage |
|---|---|
| 2015-11-28 → 2020-10 | **dense** — the relationship's first five years, near-daily |
| 2020-11 → 2024-12 | **empty — 5 messages in four years** |
| 2025-03 → 2026-06-05 | **dense** — the collapse and closure |

> **The 2020–2024 hole is a hole in the record, not a quiet period in the
> relationship.** Four years of a ten-year relationship have no surviving
> two-sided message data in any export in `raw/`. Nothing on this page should be
> read as evidence that little happened then, and no synthesis built on this
> page may treat the gap as an observation. (Per `EXTRACTION_SPEC.md`: a zero is
> data only when the system could have observed a one.)

## Reading progress

| Read through | Messages read | Of 97,768 | Events recorded |
|---|---|---|---|
| **2015-11-29** | 1,136 | 1.2% | 25 |

**Resume at `bin/annie-corpus read 2015-11-30`** (403 messages). Size the next
window with `bin/annie-corpus days 2015-12` — December 2015 is 12,000 messages
across 31 days and is the onset flood, so it will take several sessions on its
own.

**Rate note for whoever picks this up:** two days of reading produced 25 events,
several of which correct or date claims the wiki has carried for months. The
first day of a relationship is unusually dense, so this rate will fall — but the
2026-08-14 mechanical pass produced *zero* of these 25 from the same underlying
material, because none of them are stated anywhere as a dated sentence. They
only exist as things two people did.

---

## 2015

### November

**2015-11-28 — Annie's birthday, and the affair is already running.**
The corpus opens mid-relationship, not at a beginning. Annie's first surviving
message is *"Fuck my friends. Fuck birthday dinner. Fucking going drinking. I
wanna be with you"* (18:47), and Dan closes the night with *"has to give y one
more happy bday"* (23:50) — **fixing Annie's birthday as November 28**, and
establishing that the first day of the record is a day she abandoned her own
birthday dinner for him.

**2015-11-28 — the relationship predates the record and both of them know it.**
Dan is already calling her *"the love of my life"* (18:49) and Annie answers
*"I've known that since day one"* (18:56) — "day one" is already in the past
tense on the first day of the corpus. This corroborates the ~Nov 24
introduction inferred from Annie's *"HAPPY ONE WEEK SINCE LEX HANDED YOU TO
ME"* (Dec 1) and confirms the November 29 golf-course meeting is a **first
in-person meeting**, not a first contact.

**2015-11-28 — the affair is deliberately concealed from Alexis, and Annie is
told she is safe.** *"I'm like reluctant to say it because it makes me look
dumb / But Alexis doesn't know that you have any part in this. She thinks I'm
just creeping you / So you don't need to worry as much as you might have
thought"* (19:01). Concealment is managed as reassurance — the disclosure is
framed as a favour to her rather than as a deception of Alexis. This is the
earliest instance in the corpus of a pattern the later record makes central.

**2015-11-28 — Alexis is living in the house, and the household is volatile.**
Dan's plan for the evening includes going home to *"make sure she's not
stealing or destroying my stuff"* (18:49); at 19:20 he is *"walking into the
house now. Gonna hide phone so it doesn't get broked"*; at 23:53, *"Just hid my
phone while I was here to prevent drama and violence."* Three independent lines
in one evening place Alexis physically in Dan's house on 2015-11-28 and
describe an expectation of property damage. **This is the primary evidence that
the "Alexis was in Florida in November 2015" reading was false** (see
[[wiki/mind/synthesis/bond-switch-2015]]).

**2015-11-28 — Annie names the fear that the next ten years will test.**
*"Im scared that since you've been together so long that you'll just go right
back to her because I'm just a little fling"* (19:03). Dan: *"I'll show you
every day that I've seen the light."* The relationship's founding anxiety is
displacement by a prior attachment — stated by Annie, on day one, unprompted.

**2015-11-28 — the 2009 Alexis infidelity is disclosed, as a contrast case.**
*"I love this it's the exact opposite way I started my last relationship"* →
*"Like I truly trust you"* → *"Lex cheated on me 2 weeks in after I moved her
to fla"* (19:07–19:08). Read in sequence this is unambiguous: Dan is describing
how the **previous** relationship began, in 2009 in Florida. Filed at
[[wiki/people/alexis-armel]]; the misdating of this line to 2015 is corrected
at [[wiki/mind/synthesis/bond-switch-2015]].

**2015-11-28 — drugs are shared, casual and constitutive from day one.**
*"Waiting for the yak to arrive"* (18:49, cocaine); *"It's better than drugs"* /
Annie: *"Drugs just put the cherry on top"* / Dan: *"Dan & Annie + Drugs = Heart
attack"* (19:13–19:14). Substance use is not a later development in this
relationship — it is present in the first hour of the record, as shared idiom.

**2015-11-28 — Gabe the cat is in the household** (*"No!!!!! Gabeyyyyy"*,
*"Gabe would eat her for breakfast"*, 18:50–18:52), and Annie already claims him
(*"Yassss gabes my babe"*). The cat [[wiki/people/danielle-onesi|Danielle]]
picked out in Orlando in 2008 is present at the start of the Annie era.

**2015-11-28 — the merger idiom is established in the first hour.** *"You're
done for"* / *"Kidnap me for life"* / *"The kind where the kidnapper is also
simultaneously kidnapped"* (18:54–19:00); *"Well yes! You own me remember"*
(19:12); *"Because I'm you in girl form clearly"* (19:17); *"We see life the
same"* (19:19). The single-slot, total-merger register the whole relationship
runs on is fully formed on day one — it is not something that develops.

**2015-11-29, ~01:52–02:29 — the golf-course meeting, in real time.** The
best-known event in the relationship's mythology is in the record as it
happens, not as a retelling. Dan: *"K I'm on gold course"* (01:52) → *"I'm on 3
tee"* (01:57) → Annie: *"Okay waiting for him to drive away"* / *"Okay walking
now"* (01:57–01:58) → both home by 02:30. **The rain is confirmed from Annie's
own side, later the same day:** *"I normally would have been sassy about it
raining, or sitting in wet grass, or my hair getting wet. But with you none of
it mattered AT ALL. I would have slept out there with you"* (15:07). She
cracked her phone's glass screen protector in the grass (02:29–02:41).
The location is the **3rd tee** of the Uniontown Country Club course.

**2015-11-29, 03:28 — the "instantly changed my life" line is said to Annie,
not about her.** *"I met someone that instantly changed my life and showed me
that I was really unhappy"* — the wiki has carried this quote for months
without its address. He is saying it **to her**, an hour after the meeting.
The follow-on is the substantive half and was never quoted: *"And I was alright
with that for so long that I forgot I was sad"* (03:29), and later *"I had NO
idea how miserable I was"* (15:21).

**2015-11-29, 03:23–03:24 — the dossiers' "YOU ARE MY EVERYTHING" is dated.**
Annie: *"You are my full life."* (03:23) → *"YOU ARE MY EVERYTHING"* (03:24).
The dossier baseline on
[[wiki/timeline/periods/2015-2016-annie-relationship-start]] places these on
"day two"/"day three" of the record; they are in fact **hours after the first
in-person meeting**, in the same overnight burst.

**2015-11-29 — Annie was leaving someone too, and says so.** *"my fam and dude
are here and are going to force me to leave with them"* (01:35); Dan refers to
him as *"turd boy"* (02:49); Annie: *"I don't like him. At all."* → **"I am
going to get rid of him just like you just did"** (02:50–02:52). **The switch
was mutual and simultaneous.** Every prior account of this week — including
[[wiki/mind/synthesis/bond-switch-2015]]'s twenty-four-hour analysis and its
2026-08-02 correction about whose exit it was — treats Annie as unattached.
She was not. The man is unnamed in this window.

**2015-11-29 — Alexis is in the house all day, and the eviction is stalling.**
*"She's upstairs I didn't go up after I got back"* (03:33); *"She's still...
here....ughhhh"* (14:38); *"I just walked upstairs and she's on the phone with
some dude"* (18:40). Annie, repeatedly: *"THEN WHY ISNT SHE GONE YET"* (18:41).
Packing had begun by 01:25 (*"she's packing"*) but she does not leave.

**2015-11-29, 14:54 — Dan's own read on why Alexis can't leave: supply.**
*"Ahhhh I know why she isn't leaving / Or like HASNT left / ...she doesn't have
another drug source"* (14:54). Whatever else was binding that household, Dan
named procurement as the operative tie in real time — the earliest instance in
the corpus of the mechanism [[wiki/mind/synthesis/supply-network]] documents a
decade later, applied to the *departing* partner.

**2015-11-29, 14:39 — Dan took Alexis's house key.** *"She left her key out
yesterday and I snagged it"* — i.e. on Nov 28. Annie had suggested exactly this
the previous night (*"And take her key"*, 01:30).

**2015-11-29 — the marriage frame arrives within hours, with a passport as its
only obstacle.** *"Let's go get married in London or Prague"* / *"Honeymoon in
France or Greece"* / *"DJ gigs in Ibiza"* (03:44–03:45); Annie: *"I'm packing as
we speak"* → *"Gotta get a passport first though"* (03:45–03:46). Earlier the
same night Annie tries the surname on: *"I am Anne Frank"* → Dan: *"Anne and Dan
Frank / Has a the best ring to it"* (02:54–02:55). This dates the "passport
refs" the period page mentions without sourcing.

**2015-11-29 — Annie's own baseline, volunteered.** *"I haven't been happy in
years / Beyond years"* → *"I've been so down for so long"* (03:39–03:40); later,
*"this is the me that I've been waiting for someone to bring out of me"* /
*"I don't have to pretend"* (15:19). Annie enters the relationship describing a
years-long depression, on day two, unprompted.

**2015-11-29, 03:17 — a pre-Dan nude leak, and the Twitter handle.** Annie:
*"Had to change it cause my nudes got leaked from shit"*, giving `@Lo_weez`.
This is a distinct, earlier episode from the MyFreeCams history already on
[[wiki/people/annie-ulmer]] and from the 2018 blackmail retrospective — worth
separating rather than folding into either.

**2015-11-29, 03:10–03:12 — the relationship goes public the same night.**
Annie: *"Wait. I tweeted earlier.... ' #dannie kbye '"* (03:10); Dan adds her on
Twitter (03:12) and considers a new Snapchat account (04:23). The couple-name
hashtag **#dannie** exists within hours of the first meeting.

**2015-11-29, 18:37 — the friend group already knows.** *"That's rhe 3rd friend
to ask me that / Like CLOSE friend"* — three close friends independently asked
Dan whether he was leaving Alexis, before he had told anyone.

**2015-11-29, 19:11–19:16 — the affair runs out of Suz's and Fran's houses.**
With Alexis still occupying 155 Virginia, Dan proposes *"Suz's is empty"* and
then *"We can hang at my grandmas even? I would need to get a key from suz...
she's in bed and there's a comfy room on the other side of the house"*. Pickup
is arranged away from the house — *"walk to the corner of Cecil"* / *"the top of
Belmont circle"*. [[wiki/places/117-belmont-circle|Fran's house]] is a venue for
the affair in its first week, three years before Dan becomes her paid caregiver
there.

**2015-11-29, 19:13 — the drug offer, and its refusal to be a condition.**
*"Btw we can ALWAYSALWAYS not do drugs if that ever crossed your mind / Like
it's totally inconsequential to me. Its all bout you"* — Dan explicitly
de-couples the relationship from use on day two. Read against 2015-11-28's
*"Dan & Annie + Drugs = Heart attack"* and everything downstream, this is the
corpus's earliest statement of a boundary that did not hold.

**2015-11-29 — Zachariah Harshman is the cover story and the alibi.** *"Harshman
leaving soon, so I'll have him drop me and say I'm going to his house"* (01:33);
*"Just me and Harshman here now"* (03:56); *"Oh hey Zac"* (04:14). Zach is
physically present through the first night and is the mechanism by which Dan
leaves the house — context for the December 23 confrontation that
[[wiki/people/zachariah-harshman]] records as the switch's social fallout.

*(2015-11-30 not yet read — 403 messages. Resume there.)*
