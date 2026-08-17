---
domain: timeline
page_type: report
status: active
knowledge: earned
date_created: 2026-08-15
date_modified: 2026-08-17
sources:
  - exports/annie-corpus.csv (built by bin/annie-corpus from the sources below)
  - raw/self/message-csv/imessage_7244346811+7249204125+2124702449_both_all_now.csv
  - raw/self/message-csv/imessage_7244346811_both_all_now.csv
  - raw/self/message-csv/imessage_2124702449_both_all_now.csv
  - raw/self/message-csv/imessage_ALL_both_all_now.csv
  - raw/self/message-csv/MASTER_MESSAGES_DB_DUMP.csv
tags: [relationships, forensic-analysis, uniontown-era]
connections:
  - page: wiki/people/emilio
    type: evidences
    claim: "Everything known about Emilio is relayed through Annie in this record — the November window calls him only \"dude\" and \"turd boy\", and he has no channel of his own in any export."
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
| **2015-12-31** | 13,635 | 13.9% | 186 |

Each pass produces **two** outputs: events here, and everything else —
entity ledger, open leads, motif tracking, corrections queue — on
[[wiki/timeline/annie-read-notes]]. Update both in the same pass; notes
captured after the fact are notes not captured.

**Resume at `bin/annie-corpus read 2016-01-01`.** January 2016 is the first full month of the relationship — Annie starts Nguyen's (Jan 1), and the holiday flood ends. December 2015 is the onset
flood — 12,000 messages across 31 days — and it will take several sessions.

**Rate note for whoever picks this up:** the first 34 days of the relationship produced ~160 events from 13,635 messages, several of which correct or date claims the wiki has carried for months.
The first days of a relationship are unusually dense, so this rate will fall —
but the 2026-08-14 mechanical pass produced *zero* of these from the same
underlying material, because none of them are stated anywhere as a dated
sentence. They only exist as things two people did.

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
She was not. The man is unnamed in this window; the operator identifies him as
[[wiki/people/emilio|Emilio]] (2026-08-17), which is testimony rather than
something this record establishes — the same man who texts Claire on Dec 2 and
is still contacting Annie on Dec 13.

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

**2015-11-30, 05:02 — Suz supplies cocaine and offers a car, conditional on
evicting Alexis.** *"Suz just came to check on me, brought me a line, and told
me she'd get me a car this week if I get Alexis out."* Read literally: the
mother arrives at 5 AM, provides the drug, and attaches a vehicle to the
completion of the eviction. The night before she had phoned to say Dan
*"should date"* Annie because the **name** fits — *"I.e. Anne Dan Suzanne Fran
Diane Van"* (13:48–13:49), and Dan confirms *"She srsly offered me a car last
night."* **The family did not merely approve the switch; it brokered it, and
paid.** This is the earliest and least ambiguous instance in the corpus of the
maternal leverage [[wiki/mind/synthesis/estate-money-spine]] and
[[wiki/mind/synthesis/supply-network]] document from much later material.

**2015-11-30 — the eviction is run as a sequence of pressure steps, not a
confrontation.** Key confiscated (Nov 28) → *"I got everything out of my guest
bedroom / So she knows I could actually call the cops"* (00:35) → *"Everything
is super packed up / Mirrors are down"* (13:26) → *"I just heard lex on the
phone with her parents / I think they're coming for her soon"* (13:42). Each
step is reversible and none is a scene. Alexis's **parents** collect her, which
is how the Dec 1 *"Helping lex leave"* resolves.

**2015-11-30 — Casey Bondarenka is three weeks old as a friend.** *"Casey will
never stfu here"* / *"He just started hanging out with us last week"*
(13:47–13:48). He is at the house buying beer for Alexis at 00:39, drives Dan
to get his e-cig fixed at 13:44, and is the subject of an unresolved
*"Casey saga"* that Dan moves to a phone call at 23:00 (*"It is bombastic"*).
The wiki's inference that Casey received the Nov 29 *"Things are collapsing
with lex"* text is consistent with his documented presence all week.

**2015-11-30, 14:23–14:25 — the first joint drug purchase.** *"Can I pitch in
100 for morgantown?"* → Annie: *"Gotta see what my paycheck are. We can just go
all on one and he will throw in more for my bday."* A named Morgantown WV
source, $100 from Dan against Annie's paycheck, with a birthday discount. Dan's
day-two offer to abstain entirely (*"we can ALWAYSALWAYS not do drugs"*) is 19
hours old at this point.

**2015-11-30 — a jointly maintained cover story is confirmed to exist.**
*"And jsyk I have stuck to the story 100% so you don't need to worry about
saying something wrong"* (22:21). Both parties are running an agreed narrative
to third parties; its content is never stated in the text. Same register as
Nov 28's *"you don't need to worry as much as you might have thought"* —
concealment delivered to Annie as care.

**2015-11-30 — Dan is writing love letters by email, and none of them are in
the corpus.** *"Whenever you wake up, you have love letters in your inbox"*
(06:51); Annie can't find them (10:39, 13:20); Dan resends (13:22) and she
replies *"Definitely just made me tear up / I've never read anything so sweet
in my life"* (13:23–13:24). **The most deliberate writing of the first week
went through an email channel the message archive does not contain** — a
concrete, chaseable gap rather than a general one.

**2015-11-30 — Annie floats moving in, on day three.** *"Okay lemme pack up my
life and death and start moving my shit in. lol lolol jkjkjkjk"* → Dan: *"NO
JK!!!!"* (13:28–13:29). She is at 155 Virginia that evening while the handover
is still in progress (*"Do U wanna bail or stay here when she goes"*, 19:22).

**2015-11-30 — the social cost is named the same week.** *"It's weird here
because nobody understands why I'm doing this"* → *"My friends do a little bit
I haven't been able to tell them / That like I'm NOT out getting my dick
sucked"* (22:09–22:10). Three close friends had already asked (Nov 29, 18:37).
Context for [[wiki/people/zachariah-harshman]]'s December 23 confrontation.

**2015-11-30 — a laptop goes missing during the move-out.** Dan forgets to
retrieve it (13:44–13:45); by 22:05 *"Harshman talked to her and found out that
I shouldn't worry about the laptop / But... it shouldn't be missing in the
first place."* Resolution unrecorded.

*(2015-11-30 read in full. Resume at 2015-12-01.)*

### December

**2015-12-01, ~00:06 — the night after the eviction.** Dan is with Harshman
(*"Go sleep! I'm here with Harshman and feel much better"*). He tells Annie
about the "Casey story" he never got to tell her. At 02:49: *"And Annie Ulmer......
I love you so much"* — the first declaration in the record that is not a
response to hers.

**2015-12-01, 03:24 — the kitten arrives.** *"Forgot to mention that the kitten
arrives tomorrow, Willie Nelson! Perfect timing."* A second cat joins the
household.

**2015-12-01, ~04:51–05:06 — Alexis leaves, and the laptop is recovered by
force.** Dan wakes early: *"I think she's leaving really early this am I am
so excitedddd."* Then, at 05:04: *"Got my head bashed against the cabinet and
pretended to call the cops. Laptop retrieved."* When Alexis won't give it up,
*"I did both of ye lines she had out"* — did her cocaine. She hits his head
against the blue shelves. He still has bruises from a prior incident (*"I still
have bruises from the last time"*, 05:10). He tells Alexis: *"And now that I
have laptop we can put her in the file of 'ex's'"* (05:12).

**2015-12-01, 05:15 — Dan fell in love the day he met her.** *"I fell in love
with you the day I met you"* (05:15); Annie: *"You have no idea / How hard it
was / To not try to talk to you / The first time I saw you"* (05:15–05:16).

**2015-12-01, ~08:00–09:30 — the eviction is formalized.** Dan: *"She will be
out by 1pm"* (08:25). Annie: *"HAPPY ONE WEEK SINCE LEX HANDED YOU TO ME
❤️❄️❤️❄️"* (09:37) — dating the introduction to **Nov 24, 2015**. Dan walks
to Sunoco in the rain; Annie offers to pick him up. After 1pm it's *"open-door
Annie policy"* / *"Key holder"* (09:33). He didn't sleep (*"Nah but it was a
good night for that. Also I wasn't sure if I would be literally murdered in my
sleep"*, 09:34).

**2015-12-01 — Dan asks Annie on a first date.** *"Can we do date this week"*
(09:39); *"I'm gonna plan / The best first date"* (09:40). Annie: *"We can it
all"* (09:40). The plan is the first formal date.

**2015-12-01 — Annie's eye is scratched.** Annie wakes with a scratch under
her eye — she assumes Alexis got her in her sleep (*"Omg did lex punch my eye
in my sleep"*, 12:12). Dan: *"She got ya!"* Annie: *"Fuck"*.

**2015-12-01 — Casey is removed from the house.** Dan: *"Im calling Vanessa to
make sure Casey doesn't come here anymore"* (10:34). Casey left *"70000 things
here"* including *"6 bottles of e liquid, one complete e cig, strobe light, HIS
WALLET"* (10:35–10:36). Vanessa confirms Casey is no longer welcome.

**2015-12-01, ~11:00–12:00 — Rick and the job search.** Dan: *"I might have
an interview already boo / Vapor Hut hahah"* (11:11–11:12). Annie's mom says
*"today is job search day"* (10:28). Annie is off work (*"DONNA CALLED ME OFF
WORK"*, 10:23) — Alexis is working instead (*"lex is working"*, 10:25).

**2015-12-01, ~14:32 — Annie arrives.** Annie walks to Dan's; they are together
by mid-afternoon. The first day of the open-door policy begins.

*(2015-12-01 read in full. Resume at 2015-12-02.)*

**2015-12-02 — the relationship is one day old and the parents already know.**
Annie wakes at 12:47: *"Omg I like you so much"* — the first message of the day
and a re-declaration after a night apart. Dan responds: *"I was sending the exact.
Same. Thing."* The whole day is written in the register of a relationship far
older than 48 hours.

**2015-12-02, ~13:00–13:30 — the first photos are exchanged.** Dan sends a photo
(*"First photo"*, 13:06); Annie: *"YIKES / I LOOK TRAINWRECK / HIGH AF"*. Dan:
*"Ahhhh you so purdy!"* Annie sends a photo of Betty (*"Little pookie"*,
13:27). Dan: *"I have to meet this lady"* (13:28).

**2015-12-02, ~13:33 — Casey is asked to stay away.** Dan drafts a message to
Casey: *"Frank u. Just don't want to hurt his feelings or have him think that
I'm mad at him. He's just too much to be hanging around."* Annie approves
(*"I completely agree"*, 13:38). Casey is being managed out of the friend group.

**2015-12-02, ~14:01 — Dan's favorite picture.** *"OMFG my favorite picture
ever in my life I love you so much Annie Ulmer"* (14:01).

**2015-12-02, ~14:03 — Suz says something about Annie.** *"You'll be happy when
you see what suz said about you"* (14:03); *"AWE SUZ"* (14:07). Suz is actively
promoting Annie to the family.

**2015-12-02, ~15:08 — the food pact.** Both have barely eaten. Annie: *"I've
lost ten pounds no lie in the past week / No lie. My boobs are like gone hahaha"*
(15:11). They make a pact to eat healthier — *"Let's make a food pact today"*
(15:14). Dan starts cooking; Annie goes home to make rice for her mom.

**2015-12-02, ~16:05 — Dan calls Rick.** Dan: *"I'm gonna call Rick in a few
minutes"* (16:05); Annie: *"I'm proud of you"* (16:11). Dan scripts the call:
*"Broke off with lex, hanging out with Annie, she's great and makes me think
about things more clearly"* (16:10). Rick becomes the family mediator.

**2015-12-02, ~16:31 — Annie comes over.** *"Here I come :)"* (16:31). Dan is
doing laundry and Zach is smoking a blunt. Annie arrives; they clean together.

**2015-12-02, ~18:39 — the crisis begins.** ([[wiki/people/ellen-ulmer]], [[wiki/people/claire-ulmer]]) Dan: *"I'm in love"* (18:39).
Annie: *"Problem / Big problem / My mom / I called her back / She's like someone
told me your car was at Dan Frank's this morning"* (18:43–18:44).

**2015-12-02, 18:44–18:50 — the confrontation is relayed in real time.** Ellen
is *"almost crying"*: *"my stomach is doing flip flops right now do you have any
idea what he has done"*. Annie lies: *"uh I was with his gf"*. Then Claire
jumps on Annie — *"because fucking Emilio texted her about me"*. Then Annie's
dad runs upstairs screaming. Ellen: *"he has a bad past do you know what he's
done to his family"* (18:47). Ellen: *"am I going to have to treat you like a
12 year old and have you home by 9 every night"* (18:49).

**2015-12-02, 18:50–19:30 — the worst-case scenario, and Dan's confession.**
Annie: *"god yeah I'm gonna get sent the fuck away / Kill ne / Fucking just
kill me"* (from july-2026-recontact, echoed here in the early register). Dan:
*"I took $500 from my grandma one time and got caught / But that's the worst
thing I've ever done in my life"* (19:17–19:18). Annie: *"I'd rather lose all
of them then to not be with you"* (19:00).

**2015-12-02, ~19:30–20:30 — the Romeo and Juliet hour.** Dan: *"This just
turned into Romeo and Juliet"* (20:07). Annie's dad demands to know who told;
Annie refuses: *"He said it doesn't matter"* (20:07). Annie: *"Swear to god I'll
turn my phone off, leave it here on the counter for them. And move out"* (20:09).
Dan talks her down: *"I won't let you cut them off"* (20:23).

**2015-12-02, ~20:40 — the church idea.** Annie: *"Like would you want to go to
church or something with me Sunday. I dont know. Then just explain this to then"*
(20:40). Dan: *"Annie I would do anything you think would make this better"*
(20:40).

**2015-12-02, 22:41 — Dan writes a letter to Annie's parents.** *"I'm gonna write
a letter to your parents and send it to you. If you think it will help and when
you're ready you can give it to them"* (22:41–22:42).

**2015-12-02, 23:16 — Suz intervenes.** Suz arrives at Dan's, upset, bringing
cleaning supplies. She wanted Rick to know Dan was doing better. *"And my parents
had to take it and ruin it"* (23:26).

**2015-12-02, 23:36–23:59 — Rick's offer.** ([[wiki/people/rick-frank]]) Dan: *"I just got the weirdest
message from Rick"* (23:36). Rick: *"Call me tomorrow. I will help you fix this"*
(23:56). Annie: *"Rick will fix this / He and my dad are buds"* (23:57). Rick
is positioned as the family mediator. Dan: *"He also is chomping at the bit for
an angle to get involved in my life"* (23:57).

*(2015-12-02 read in full. Resume at 2015-12-03.)*

**2015-12-03 — the letter is drafted.** Dan: *"Do u wanna read the first draft
of my letter"* (01:28). The letter: *"I'm reaching out to you because I would
like to ask for your permission to see your daughter, Anne"* (01:37). Suz
annotates it *"like a HS english paper"* (14:01). Dan redrafts it.

**2015-12-03, ~03:19–04:57 — the poetry burst.** Annie: *"bb! Omg I love you"*
(03:19). Dan, at 04:35: *"I'm all alone I'm in my room I don't know what to do
I feel my heart beat in my chest It only beats for you"* — a poem, unprompted.
Annie: *"I fucking love you"* (04:46). Dan: *"I didn't know what love was until
I met you / I thought I did."* (04:54). Dan: *"I crave you. And I feel you crave
me."* (04:56).

**2015-12-03, ~05:04 — the unlocked door.** *"I unlocked the back Dior just in
case, but I have a lot of alarms set. Please come wake me up if you don't hear
back."* Annie comes over early.

**2015-12-03, ~09:30 — Annie arrives.** *"Hi hi hi / 930"* (09:30); *"I just woke
up / I'm running around like a nut / But I'm coming!"* (09:32–09:33). She walks
to Dan's. They are together by mid-morning.

**2015-12-03, ~11:21 — the "YOU'RE MY EVERYTHING" echo.** Annie: *"I love you"*
(11:21); Dan: *"I love you so much holy fuck / My heart is racing from being
around you"* (11:21–11:22). Annie: *"YOURE MY EVERYTHING"* (11:24). Then: *"my dad
/ Fuckingn face timed me / Said it was 'on accident'"* (11:24–11:25). Annie
covers: *"I said did you get the pic yet? He said no? I said hmm must be taking
long to go through"* (11:25–11:26).

**2015-12-03, ~11:27 — the Annie box.** Dan: *"Omg you left pen straw here / Into
the Annie box it goes"* (11:27). A box of Annie-mementos exists from day six.

**2015-12-03, ~11:29 — the experiment.** Annie: *"Did you try the experiment"*
(11:29); *"A+++"* (11:30). Dan: *"Wow nice I didn't even study"* (11:30). The
experiment is unstated but the result is positive.

**2015-12-03, ~12:00 — the Christmas present.** Dan: *"I'm about to order your
Christmas present right now / And trust me / You are gonna flip shit / It's
something you reallllyyyy want"* (12:25). Annie: *"TELL MEEEEEEE"*. Dan: *"ON
DECEMBER 25"* (12:25–12:26). Hints: *"you really want it / You could use it to
make money but you could also use it to relax"* (13:06–13:08).

**2015-12-03, ~12:28 — Rick's message.** *"RT just messaged me"* (12:28). RT
reports that Alexis is working at the bar tonight. Dan: *"A TOOTH ISSUE"* (13:32)
— Alexis's excuse for being late.

**2015-12-03, ~12:37 — the Salvation Army.** Annie's mom signed her up to ring
bells. Dan: *"I'm supposed to do that tonight! / But of course / My mom got
roped into doing it for work"* (12:37–12:38). They plan to do it together.

**2015-12-03, ~12:42 — three weeks without cigs.** Dan: *"Hey today is 3 weeks
without cigs / Woooo"* (12:42). Annie: *"Weeheeee!!"* (12:42).

**2015-12-03, ~13:52 — Alexis is using Dan.** Dan: *"I was actually scared to
ask lex to quit doing drugs with me because I knew she would leave if I stopped
/ And it's so nice / To know that like, you couldn't be further from that"*
(13:52–13:54). Annie: *"She was using you Dan"* (13:53).

**2015-12-03, ~14:00 — Annie goes to work.** Dan goes to the office with his mom
(*"it's like take your son to work day"*, 14:00). Annie goes to the bar. Donna
is there. Alexis is late. Annie is nervous.

**2015-12-03, ~14:32–15:40 — Alexis arrives at the bar.** Donna: *"is this the
first time you two are face to face"* (14:44). Alexis shows the kitchen guys
Annie's pics online (14:55). Donna: *"how dare you take the man she was going
to marry"* (15:01). Annie: *"I WASNT PLANNING ON TAKING HIM"* (15:01). Alexis
refuses to walk past the bar where Annie is standing (17:05).

**2015-12-03, ~16:28 — Dan texts Alexis.** Dan: *"she messaged me a little bit
ago / it wasn't pretty"* (16:28). Alexis: *"happy 7 years. enjoy your herpes.
bye"* (16:29). Dan shows Annie. Dan drafts a text to Alexis: *"Hey, I know you
don't want to hear from me or see me, but I really want to ask you to please lay
off Anne"* (16:48). Annie edits it: *"I remembered that you and she are supposed
to work together tonight / I don't want any problems between you two"* (16:50–16:51).
Dan sends it (16:56). Alexis's phone goes off at the bar.

**2015-12-03, ~17:00 — the fireplace.** Alexis tries to turn on the fireplace
in the bar — *"fireplace fail"* (17:05). Scott (a friend) hits on her. Donna
disappears. The new girl (mini-Donna) arrives.

**2015-12-03, ~17:10 — the threesome joke.** Annie: *"I was actually convinced
in the beginning that / Y'all wanted a threesome 😂"* (17:10). Dan: *"nah...
just you / she is so sexually repressed, that it would never have happened"*
(17:11–17:12).

*(2015-12-03 read in full. Resume at 2015-12-04.)*

**2015-12-04 — no messages in the record.** Either a genuine no-contact period
(Annie grounded at her parents') or a data gap. The next window is Dec 8.

**2015-12-08 — Annie is sick (withdrawal).** Annie: *"Maybe three hours all
together / I literally laid there in tears"* (09:14). Dan: *"This is why I still
have to take those fucking things / Because I felt like what you're describing
for months at a time"* (09:18–09:19). Annie: *"Coca is like drinking milk compared
to this"* (09:29). Dan takes care of her.

**2015-12-08, ~10:00 — the Combo incident.** Dan: *"I'm at the state police
barracks / Scarrrry stuff haha"* (12:23). He picks up copies of the lost
paperwork. Dan: *"Fuckin combos / I learnt me lesson!"* (12:26–12:27).

**2015-12-08, ~10:45 — the surprise.** Dan: *"I have something to give you
before work"* (09:04); *"It's not drugs lol"* (09:04). Annie: *"A kiss?!"*
(09:08). Dan: *"A more tangible present"* (09:11). Annie comes over before
work.

**2015-12-08, ~11:00 — Dave from CT's calls.** Dan: *"Dave from CT's just called
me looking for Alexis"* (14:58). Dan: *"I was like 'uh...we're not together
anymore so I truthfully have no idea where she would be'"* (14:59). Dan wanted
to say: *"'Do you remember the prettier bartender? I can tell you where SHE is
right now tho'"* (14:59).

**2015-12-08, ~13:00 — Annie comes over.** Annie: *"I gots the cutest guy in da
world"* (11:30). Dan: *"And I gots the prettiest girl in the world / Together we
unstoppable"* (11:37). They spend the afternoon together.

**2015-12-08, ~15:00 — the VS fashion show.** Annie: *"Tonight's the VS fashion
show"* (09:33); *"And tomorrow is Jill's bday / I forgot we're having a girls
night for it all tonight"* (09:34). Annie goes to the fashion show with friends.

**2015-12-08, ~19:00 — Dan DJ's.** Dan: *"I dj'd for a bit and now I'm working
on a track for caribou"* (20:36). He's at a studio with friends.

**2015-12-08, ~23:00 — the quit-cocaine pact.** Annie: *"I need a better job. I
need to stop buying dirty shit"* (23:05). Dan: *"I will promise (pinky) to not
ever suggest it or talk about it"* (23:08). Annie: *"I can't lose you / I don't
want to risk anything at all"* (23:10). Dan: *"I promise you. You won't hear
anything about it from me"* (23:29). They both agree to quit together.

*(2015-12-08 read in full. Resume at 2015-12-09.)*

**2015-12-09 — Annie comes over before work.** Annie: *"I'm coming down to see
my boo"* (11:07). Dan: *"I have presents / For yew"* (10:49). Annie: *"Why!!! /
Because it's Wednesday / And you deserve presents everyday that ends in 'U' / 'Y'"*
(10:50–10:51). Dan gives her "lil stuffz."

**2015-12-09, ~11:30 — Dan runs errands.** Dan: *"I have to run out / To go fix
the combos incident"* (11:08–11:09). Suz picks him up to get a present for Annie.
Dan: *"Suz is picking me up and taking me to get something for lil ol you"*
(11:39).

**2015-12-09, ~11:48 — Jason at CMU.** Dan: *"Jason is rapping at CMU tomorrow
for my sisters art show / I might DJ for his set"* (11:48–11:49).

**2015-12-09, ~11:51 — the Christmas tree.** Dan: *"After you go to work I'm gonna
go get a tree with suz"* (11:51). Dan: *"Next year / We will have OUR Christmas
tree"* (11:51–11:52).

**2015-12-09, ~13:00 — the surprise at Annie's house.** Dan: *"I'm done already
ahah"* (11:39). Annie: *"I'm finishing up getting ready"* (13:37). Dan: *"Hmmm
there's probably a surprise waiting for you / When you go to leave for work"*
(13:00–13:01). Annie: *"I hope you are the surprise"* (13:02). Dan: *"I bet the
surprise is already waiting / At your house"* (13:01–13:02).

**2015-12-09, ~13:55 — Annie comes over.** Annie: *"I wuvs you"* (13:45). Dan:
*"Holy prettiest girl I've ever seen"* (13:45). Annie: *"It's da makeup. Don't let
it fool you"* (13:46). Dan: *"I know what you look like / And I also know that you
are the prettiest girl / Make up or not"* (13:46–13:47).

**2015-12-09, ~13:55 — Alexis on IG.** Dan: *"Hahah right after I put that pic on
ig / Alexis put something up that says 'one is more fun'"* (13:55–13:56). Alexis
texts Annie: *"You don't need to come in"* (13:57). Annie quits CT's.

**2015-12-09, ~14:00 — the new job.** Annie: *"My dad said he ate at nyguens for
lunch. And they told him they will be starting me the first of January"* (14:00).
Annie gets a job at Nguyen's starting Jan 1.

**2015-12-09, ~14:42 — Olive Garden.** Dan: *"Can we go to Olive Garden tonight? /
I want salad and bread sticks / Soooo bad"* (14:42–14:43). Annie: *"And soup😍"*
(14:42). Dan: *"It will be our almost first date"* (14:43).

**2015-12-09, ~15:17 — Zach Clingan texts Annie.** ([[wiki/people/zach-clingan]] — *not* [[wiki/people/zachariah-harshman]]) Annie: *"Issue / Zach clingan
just texted me saying 'I have to talk to you' / And said he's going to call me"*
(15:17–15:18). Dan: *"Oh good / My arch rival / Glad he's in the mix too"*
(15:18–15:19). Dan: *"WHY can't we be left alone / Fuck / Literally makes me
want to puke. THAT is who introduced me to drugs"* (15:19–15:20).

**2015-12-09, ~15:37 — Dan confronts Zach.** Dan: *"I just talked to him / Told
him he doesn't know me and to stay the fuck out of my life / And to not threaten
you"* (15:37–15:38). Zach calls Annie: *"have you lost your damn mind / And to
keep my eyes open"* (15:38–15:39). Zach: *"he had his ex move out and you were
there the next day. That makes you look like shit and he's going to treat you
like it"* (15:39).

**2015-12-09, ~15:45 — Dan sends Zach a pic.** Dan: *"He's knows EXACtly what's
going to happen but has no clue who would do it?"* (15:46). Dan sends Zach a
picture (of his middle finger, implied).

**2015-12-09, ~16:00 — the stripper joke.** Annie: *"I'm going to become a
stripper / I give up / They make bank"* (14:49). Dan: *"Can I just pay you / To
be my private stripper"* (14:49–14:50).

**2015-12-09, ~19:00 — Annie gets a bat.** Annie: *"Okay there is something in
my room / Squeaking / Like an old wheel would / But it's not a wheel / It's like
an animal / And I'm scared"* (20:21–20:22). Annie's dad thinks it's a bat. They
can't find it.

**2015-12-09, ~21:00 — Suz meets Annie.** Suz is at Dan's, asking about Annie.
Dan: *"She is like / The biggest #dannie supporter"* (21:37). Suz: *"We need to
get you some preppier clothes / So I can impress you HAHAHAH"* (21:38).

*(2015-12-09 read in full. Resume at 2015-12-10.)*

**2015-12-10 — the "first night" story.** Dan tells Annie about the first night:
*"when you messaged me the next morning about driving to va, do you remember that
lex texted you / And I grabbed the phone / And pretended like it was me / And
that I was kidding"* (19:57–19:58). Annie: *"I was nervous to even text you that
day"* (19:58). Dan: *"I'm so glad you did / Because I needed every possible sign
to believe that you were into me"* (19:58–19:59).

**2015-12-10, ~19:20 — the marriage talk.** Dan: *"I already want to marry you"*
(19:19). Annie: *"Time doesn't mean anything / You could date someone for (In your
case) 7 years / And not even feel the thought of marriage / And then you meet
someone and you feel it instantly"* (19:19–19:20). Dan: *"I feel 100% more
connected to you immediately"* (19:20).

**2015-12-10, ~19:30 — the ex warning.** Annie: *"Just scares me / Cause before /
I did that... With my ex / And there was another girl there / And I just never
wanna let myself walk in to that again"* (19:37–19:38). Dan: *"Well I understand
why that scares you / And I want you to know / That never in a million billion
years"* (19:38–19:39).

**2015-12-10, ~19:45 — the memento box.** Dan: *"I have notes from you / And pen
straws / And snowflakes you made me / You know STUFF THAT MEANS SOMETHING /
Irreplaceable stuff / Things we can show our kids"* (19:48–19:50). Annie: *"Trust
me I have stuff from you all shoved in here too"* (19:50).

**2015-12-10, ~20:10 — the jacuzzi.** Annie: *"Do you has tub"* (20:12). Dan:
*"Suz has jacuzzi tub / And is going on 3 day vaca / In a couple weeks / And I'm
taking care of Lucy / Sooooo / Lots of jacuzzi baths"* (20:13–20:14). Annie:
*"And lots of Dannie time"* (20:14).

**2015-12-10, ~20:55 — the Eddie's rumor.** Annie: *"Rumor at cts was that I was
leaving there to go work at eddies / Bahahhaha / I never once said that / It got
around to my dad and he was like you are NOT allowed to work there. Like flipped
shit"* (20:57–20:58).

**2015-12-10, ~20:56 — Dan's honesty about cocaine.** Dan: *"Also wanted to note
that I am NOT getting more from her"* (20:56). Annie: *"Getting more from her
what"* (20:58). Dan: *"Oh I was just letting you know I wasn't getting more
coca"* (20:58). Annie: *"Its fine bahahah I wasn't even thinking that"* (20:58).

**2015-12-10, ~21:00 — the 90% rule.** Dan: *"I like the 90% thing / It doesn't
have to be that black and white / But I really want us to keep having almost all
of our time without it"* (21:02–21:03). Annie: *"I was going to suggest the same
thing"* (21:00).

**2015-12-10, ~21:30 — Suz the supporter.** Suz is at Dan's, asking about Annie.
Dan: *"She is like / The biggest #dannie supporter"* (21:37). Dan: *"I have to
scream at her from running around town bragging about you"* (21:38).

**2015-12-10, ~21:40 — the church joke.** Suz asks if she should start going to
church. Dan: *"I said / MOM NO / I'm trying to impress them"* (21:39–21:40).
Annie: *"SHE CAN / SO / Church is for all"* (21:40).

*(2015-12-10 read in full. Resume at 2015-12-11.)*

**2015-12-11 — first full no-problems day.** Dan: *"Guess what! You fell asleep
which means we had our first full no-problems day. I'm going to go dream about
you. I love you"* (00:43).

**2015-12-11, ~11:23 — the Christmas present arrives.** Dan: *"I need to sign
for a certain large package"* (11:30). Annie: *"WHAT"* (11:30). Dan: *"Well there's
an even BIGGER package / For you!"* (11:30–11:31). Annie: *"Oh b / You don't need
to do that"* (11:31). Dan: *"Idgaf what you say / I love you / And want to give
you da best xmas evarrrrrr"* (11:31–11:32).

**2015-12-11, ~11:28 — Annie's bracelet.** Dan: *"You do lots of amazing things
for me / Make me bracelets"* (11:28). Annie makes Dan a bracelet.

**2015-12-11, ~11:29 — Annie's Christmas ideas.** Annie: *"I can't wait to do
this thing for Christmas for yew / I have like ten ideas / But need to figure
out how to do it all together babahha"* (11:29–11:30).

**2015-12-11, ~11:43 — Louis CK.** Dan: *"Do you know who Louis CK is?"* (11:43).
Annie: *"I do not / WhyV hahah"* (11:50). Dan tells her about the comedian.

*(2015-12-11 read in full. Resume at 2015-12-12.)*

**2015-12-12 — the "best night" plan.** Dan: *"So the stuff is here but I'm
waiting for you to be almost ready to take it from her so we can do it all
together / Take your time / We are gonna have the BEST night"* (15:49).

**2015-12-12, ~16:15 — Annie comes over.** Annie: *"Awe b I'm so excited / Sorry
i passed out / I guess I a wittle sleepy!"* (16:13–16:15). Dan: *"You'll be all
rested for me / So I can smother your face / And kiss you for hours"* (16:16).

**2015-12-12, ~16:17 — Betty is in trouble.** Annie: *"Heck no / She's in trouble /
She bit me twice today and my mom / For no reason"* (16:17–16:18). Betty the
chihuahua is banned from the visit.

**2015-12-12, ~16:45 — the pickup plan.** Dan: *"Probably have you get me at suz's /
Depending on who is ready first"* (16:44–16:45). Annie: *"Okie dokie"* (16:45).
Annie: *"Here I come"* (17:19). Annie: *"Leggo lover boy"* (17:25).

**2015-12-12, ~16:56 — the title.** Dan: *"You're the best bestfriend/fuckbuddy/
life partner / A guy could ask for"* (16:56).

*(2015-12-12 read in full. Resume at 2015-12-13.)*
**2015-12-13, ~10:06 — Annie's eye is swollen, and Dan loves it.** Annie wakes with a scratch under her eye — "LOOKS LIKE I GOT PUNCHED" (10:06). Dan: *"Are you taking Ambien and then attending street fights after you fall asleep"* (10:08). Annie blames Ambien. Dan: *"That might be my fav picture of you / Ever / Ms big eyes"* (10:09). The Ambien explanation is consistent with Annie's known use — she takes it to sleep, and Dan connects it to a pattern of mishaps. Whether the swelling is from Ambien or something else (the prior night's party at Suz's), Dan treats it as endearing rather than alarming.

**2015-12-13, ~10:10 — Dan hung out with Claire, and it went well.** Dan: *"Ahhh im so relieved we finally hung with Claire last night / Big steps u no"* (10:10). Claire is Annie's sister, and this is the first documented instance of Dan meeting Annie's extended family. The fact that Annie doesn't express surprise or anxiety about it suggests Claire is already in Dan's corner, or at least not hostile. This is the earliest meeting between Dan and Annie's siblings in the record.

**2015-12-13, ~10:40 — Dan names the friends who abandoned him.** Annie asks if his friends' distance is her fault. Dan: *"NOOOO / it's shu and Alexis / You are my best friend / And you are all I will ever need to be 100% happy"* (10:39–10:40). The three friends who asked about the breakup (Nov 29, 18:37) have gone silent. Dan names Suz and Alexis as the cause — "shu" is likely Zachariah Harshman, who "never returned my call" (22:15). Dan frames the abandonment as proof that Annie is all he needs, reframing social isolation as romantic clarity.

**2015-12-13, ~11:10 — The MyFreeCams discussion, and Dan's support.** Annie: *"if we ever move away from this hell hole / I'm gonna do mfc again. Fuq it"* (11:11). Dan: *"I think that sounds amazing / And I am SO ready to get out of here"* (11:12). Annie names her idol — a cammer whose boyfriend is supportive. Dan: *"It's not cheating / So what would anyone have to be upset about"* (11:13). This is the earliest explicit discussion of Annie's camming history and Dan's stated support for her returning to it. Read against the "passport refs" from Nov 29, it's part of the same "move away and build a life" fantasy.

**2015-12-13, ~11:51 — Dan proposes, sort of.** Dan: *"Okay so your tweet / Is why we are getting married"* (11:51). Annie: *"Yes!!!! I won!"* The proposal is framed as a joke, but the substance is real: Dan is saying Annie's humor is what made him want to marry her. This is the second marriage-reference (after Nov 29's "Anne and Dan Frank") but the first time Dan explicitly says "married" in a declarative, non-hypothetical way.

**2015-12-13, ~15:30 — Annie is trapped at the triathlon party.** Annie: *"WILLS HERE / he pulled in the drive"* (15:34). Will is her brother (mentioned Nov 25). She's been at her family's triathlon Christmas party all day — *"I just don't wanna be social"* (10:52). By 17:43 she's panicking: *"HELP / I MADE THE MISTAKE OF SAYING IM GOING TO SEE ZAC / THEN CLAIRE CALLED ME OUT"* (17:43–17:44). She tried to use Zach as an excuse but Claire caught the lie. Dan tells her to wait it out. This is the first documented instance of Annie being unable to leave a family gathering to see Dan — a pattern that recurs.

**2015-12-13, ~17:54 — Dan runs errands for Fran while Annie waits.** Suz wants Dan to pick up dinner for Fran. Dan: *"She wants me to pick up dinner for Fran / And then when I drop it off she is just gonna take me back"* (17:54). Dan is doing caregiving labor for Fran (his grandmother) while Annie is trapped at her parents'. The simultaneity is notable — both of them are stuck in family obligations, texting through it.

**2015-12-13, ~21:08 — Emilio texts Annie, and she tells him off.** Annie: *"FUCKINGG Emilio just texted me / In gonna go off on him about throwing shit at me the other night"* (21:07–21:08). Emilio is the same man from Dec 2 — *"because fucking Emilio texted her about me"* (Dec 2, 18:45). He threw gum wrappers at Annie. Now he texts: *"Honestly I just miss having fun with you!"* (22:23). Annie is furious. Dan: *"This kid is so stupid that he hardly seems alive"* (22:20). Annie tells Emilio she has a boyfriend now (22:40). This is the first documented instance of Annie explicitly claiming the "boyfriend" title to a third party.

**2015-12-13, ~22:45 — Dan reads Bruce's message about Alexis.** Bruce (friend/manager at CT's) tells Annie: *"Chris was gonna talk to you about Dan....then lexi jumped the gun and ask me to text you Wednesday and tell you this...Chris is tired of lexi"* (21:47). Alexis tried to go through Bruce to get to Annie — another instance of Alexis managing the social fallout of the switch. Bruce calls Alexis "a bitch" (21:53). The CT's staff is splitting toward Annie and away from Alexis.

**2015-12-13, ~22:50 — The "official" question.** Dan: *"So so so so are we (or if not can we be) ~official~ / Because I didn't know and it's all I want ever in the world"* (22:49). Annie doesn't answer directly — she's asleep. But the question is on the record. Dan's "official" ask is the first time either of them names the relationship status as something that needs declaring. Read against Annie's "I told someone to leave me alone cause I have a boyfriend" (22:39), she's already acting official — Dan just doesn't know it yet.

*(2015-12-13 read in full. Resume at 2015-12-14.)*

**2015-12-14, ~10:35 — Morning sex, and the Alexis contrast.** Annie: *"I love you!!!!"* (10:35). Dan: *"Holy geez you made me happy / Just like you always do / And we got 1.5 fucks in"* (10:37). They've been having sex twice a morning — "1.5" means one full and one partial. Annie then references Alexis: *"Lex slept in the bed for days after we first fucked lol"* (10:48). Dan: *"I like couldn't even go in the room for 4 days when that was all happening / I was living out of the LIVING room"* (10:49). The contrast is explicit: with Alexis, Dan couldn't be in the same room after sex; with Annie, he's having it twice a morning. This is Dan's own read on how different the two relationships are, stated in real time.

**2015-12-14, ~10:51 — Alexis asked Dan for help, and he refuses.** Annie: *"I can't believe she asked you that last night / Sickening"* (10:51). Dan: *"I didn't even see it until this morning / But how the fuck would she EVER think / I would want to help her out ever for anything"* (10:51–10:52). The content of Alexis's request is never stated, but Dan's reaction is categorical: *"I'm not actively trying to fuck her life up but I would neeeever do a single thing to HELP her"* (10:52). This is the earliest post-eviction statement of Dan's policy toward Alexis — non-intervention, non-assistance.

**2015-12-14, ~11:53 — The property exchange.** Dan: *"And my dick is property of Anne Ulmer / Lock and key"* (11:53). Annie: *"And my pussy is property of Dan Frank"* (11:53). This is the fullest expression of the merger idiom — not just "I own you" but "my body parts are legally yours." The register is playful but the underlying claim is total. Read against Nov 28's "Kidnap me for life," it's the same impulse articulated in sexual terms.

**2015-12-14, ~12:19 — Dan gets a recording session at Vapor Hut.** Dan: *"the owner is paying me for a recording session THIS THURSDAY"* (12:19). This is Dan's first documented music-income since the switch — the Vapor Hut job (Nov 1 interview) hasn't started, but the owner is already paying him for studio work. The "tighter I get with that dude the better" (12:20) suggests Dan is cultivating the relationship deliberately.

**2015-12-14, ~17:43 — Annie comes over, and the cocaine pact holds.** Annie: *"Oh hey / Day two no coca for me"* (17:43). Dan: *"Good jerb! With the exception of the line you forgot, I've been well behaved too!"* (17:44). The Nov 23 quit-cocaine pact is holding — two days in. Dan frames the one missed line as an exception. Annie: *"This way our tolerance will go down and when we do do it, allllllll the gates will open"* (18:09). They're abstaining strategically, not morally.

**2015-12-14, ~18:55 — Annie is not on the CT's schedule.** Annie: *"So they posted this weeks schedule... And I'm not on it.. But some bitxh named Koral is"* (18:55). Suz's guy's girlfriend's daughter (Koral) was just hired at CT's. Annie: *"Fuck her / Im pissed / Like I need to fucking work"* (18:57–18:58). Dan: *"Let's go there on her shift / And you can boop her nose"* (18:57–18:58). Annie needs money — she quit CT's voluntarily (Dec 9) but now needs the income. The schedule change is the first concrete consequence of her quitting.

**2015-12-14, ~23:00 — The "peep" roleplay.** Annie: *"Peepin / Hard"* (15:35). She's peeping through Dan's window. Dan: *"Come snug me / And say peep over and over"* (15:36). They spend hours on this — "peep" becomes their word for peeping/trespassing/looking. Dan: *"I won't ever get sick of it / Promise"* (15:36). This is the earliest documented instance of their shared language evolving into something sexual — "peep" will recur.

*(2015-12-14 read in full. Resume at 2015-12-15.)*

**2015-12-15 — The "everything led up to this" day.** A quieter day — 662 messages, but fewer discrete events. Dan cooks (chicken vesuvio, the spicy lemon wine sauce dish he learned from Suz). They watch *Soaked in Bleach* (the Kurt Cobain documentary). Dan gives Annie the Netflix login: *"Francoldren@gmail.com 117Coldren"* (22:19). Annie: *"CAUSE WE ARE BOYFRIEND/GIRLFRIEND"* (22:21). The Netflix account is in Fran's name — Dan is sharing his grandmother's account with Annie as a relationship milestone. This is the second "official" marker (after Dec 13's question) — Annie claims the title unprompted.

**2015-12-15, ~21:19 — "And I am yours / For all of time."** Annie: *"And I am yours / For all of time / I can't wait to experience life together"* (17:59). Dan: *"Think about where we could be by next Christmas"* (18:01). This is the first "for all of time" declaration in the record — the merger idiom in its most permanent register. Read against Nov 28's "Kidnap me for life," it's the same impulse but in Annie's voice, unprompted.

**2015-12-15, ~22:24 — Dan's "November 24" dating.** Dan: *"I had no idea what love was until November 24, 2015"* (20:35). This is the first time he explicitly names the introduction date in a declarative statement (Annie named it first on Dec 1: "HAPPY ONE WEEK SINCE LEX HANDED YOU TO ME"). Dan's "November 24" is a precise, unprompted corroboration of the timeline the wiki inferred from Annie's Dec 1 message.

*(2015-12-15 read in full. Resume at 2015-12-16.)*

**2015-12-16, ~15:04 — Dan cleans cars at Suz's.** Dan is working — cleaning cars at his mother's office. Annie: *"Look at you!! / It's such a nice day for cleaning out cars"* (15:16). Dan: *"I will be free as a bird"* (15:05). This is the first documented instance of Dan doing manual labor for Suz's business — the "I have to weed whack bops place" of the later Supply Network, but for his mother, and paid in cash. Suz gives him two $50's (16:44).

**2015-12-16, ~16:41 — Suz calls Annie "your girlfriend."** ([[wiki/people/suzanne-frank]]) Dan: *"SAVE ONE OF THOSE FOR YOUR GIRLFRIEND / (Because she gave me two 50's)"* (16:43). Annie: *"SHE CALLED ME YOUR GIRLFRIEND / IM IN LOVE IM IN LOVE"* (16:46). Dan: *"OMG she was calling you my girlfriend for the past 2 weeks"* (16:46). This is the first documented instance of Suz using the title. Dan had been correcting her ("I kept reminding her that I don't know how that works but not to be presumptuous"), but Suz ignored him. Annie's reaction — all-caps joy — is the strongest positive response to a family-approval signal in the record.

**2015-12-16, ~16:41 — Annie gets a shift at CT's.** Annie: *"BRUCE JUST SAID IM BARTENDING FRIDAY / COUSIN FUCKING CHRISTMAS"* (16:44). The same Cousin Christmas she declined on Dec 13 is now her first scheduled shift back. Dan: *"Cousin Christmas >>>>>> CTS"* (22:00). Annie also babysits Friday morning (16:36). She's stacking income — Nguyen's starts Jan 1, but CT's fills the gap.

**2015-12-16, ~20:54 — The pregnancy scare.** Annie: *"Cause I'm over two weeks late / I don't want this / I need another test"* (20:54–20:58). She hasn't had her period in two weeks. The last time she and her ex hooked up was over a month ago, during ovulation. Dan: *"Look those tests are scary accurate. There's all kinds of weird cycle stuff that happens when you switch your birth control / Take another test and you'll feel better"* (21:05). Annie is panicked. Dan is calm, factual, reassuring. This is the first pregnancy scare in the record.

**2015-12-16, ~21:15 — Dan's "no matter what" declaration.** Dan: *"Do you know that I love you no matter what? / And that no matter what happens now or in the future that I will be right there with you to give you support you've always given me?"* (21:15). Annie: *"But this is so much bigger / I would never ever expect you to"* (21:19–21:21). Dan: *"You are the LOVE OF MY LIFE / Even if you straight rejected me because of this whole thing / It's not like I can go back internally"* (21:21). This is the first time Dan says "love of my life" since Nov 28 — and this time it's conditional on a potential pregnancy with another man. Annie: *"I would never and WILL NEVER leave you / I'm in this forever"* (21:23).

**2015-12-16, ~21:29 — "You're the only thing that makes life seem like magic again."** Dan: *"Anne you're the only thing that makes life seem like magic again. You're the only thing that makes me feel like the cloud of 'bad' that i lived in for over a decade, has been lifted"* (21:29). This is Dan's most explicit statement of what Annie does for him — not just "makes me happy" but "makes life seem like magic again." The "cloud of 'bad'" language is the first time Dan describes his pre-Annie life as a sustained negative state rather than a series of incidents.

**2015-12-16, ~22:26 — The Tarantino movie date.** Dan: *"We need to see the new Tarantino movie"* (22:26). Annie: *"I never saw ANY of those"* (22:28). Dan: *"So I guess we'll have to watch all the best movies of all time as well"* (22:29). This is the first documented instance of them planning a shared cultural activity — not just "hanging out" but a specific movie date. The "watch all the best movies of all time" is Dan's first statement of a future that includes shared domestic life.

**2015-12-16, ~22:32 — Annie's trust issues, and Dan's response.** Annie: *"Just know how much you and I have both had trust issues in the past / And I want you to know everything"* (22:43). Dan: *"You handle this kind of stuff SO well with me / And you've done everything exactly how I'd expect someone who really loves me to do"* (22:43). This is the first explicit discussion of trust issues — Annie names it, Dan confirms it's mutual. Annie's "I want you to know everything" is the first statement of radical transparency as a relationship value.

**2015-12-16, ~22:38 — Dan asks for Annie's shoe size.** Dan: *"What size shoes do you wear"* (18:41). Annie: *"7.5"* (18:42). Dan: *"Okie thank ya"* (18:42). Annie: *"WHY"* (18:43). Dan: *"Mayyyybe I was just updating your contact!"* (18:51). Annie: *"I THINK YOU ARE FIBBING"* (18:44). Dan is buying her a gift — the shoe size is for shoes. Annie's "I THINK YOU ARE FIBBING" is the first time she accuses him of lying about a gift, but she's smiling about it.

*(2015-12-16 read in full. Resume at 2015-12-17.)*

**2015-12-17, ~00:48 — "I fell asleep in middle of sayin goodnight I love you boyfriend!"** Annie's first message of the day — she fell asleep while saying goodnight. Dan: *"It's raining It's pouring My girlfriend Is snoring"* (07:12). Annie: *"Actually i believe i just grind my teeth"* (07:58). This is the first documented instance of Annie's sleep issues in the record — teeth grinding and snoring.

**2015-12-17, ~11:12 — Annie is broke, and Dan wants to help.** ([[wiki/mind/synthesis/estate-money-spine]], [[wiki/places/117-belmont-circle]]) Annie: *"So I'm literally counting all the change I have / This is what my life has come to"* (11:12–11:15). Dan: *"I wanna help!"* (11:36). Annie: *"Wanna roll change with me?"* (11:28). Dan: *"Of course!! / I'd do anything with ya"* (11:29). Annie rolls change. Dan gives her money from Fran later that day: *"I got da monayyyy / Fran to the rescue"* (17:39–17:40). This is the earliest documented instance of Annie's post-switch financial stress — she quit CT's (Dec 9), Nguyen's doesn't start until Jan 1, and she's counting change.

**2015-12-17, ~17:14 — "I can't wait to be your house wife."** Annie: *"I love every single day with you / I can't wait to be your house wife"* (17:14). Dan: *"Yeah let's do that ASAP"* (17:15). Annie: *"And cook and clean all day every day for you"* (17:15). Dan: *"Nahhh well pay someone for that. You can mani pedi etc"* (17:15–17:16). Annie: *"No no no / I enjoy those things"* (17:16). This is the first explicit "house wife" discussion — Annie framing domestic labor as desire, Dan reframing it as something to outsource so Annie can enjoy herself.

**2015-12-19, ~01:58 — Email confusion, and Betty peeping.** A brief window: 16 messages. Annie's email coming through Emil's (2am). Betty peeping. Minimal content — a data gap or genuine quiet period.

> **Gap note:** Dec 18–24 have no entries (Dec 17 and Dec 19 have minimal traffic). This is a data gap — no traffic or missing exports. Per EXTRACTION_SPEC.md: a zero is data only when the system could have observed a one.

**2015-12-25, ~08:15 — Merry Christmas.** Dan: *"Hi / Merry Christmas perfect"* (08:15). Annie: *"Merry Christmas worlds best boyfriend!!!!"* (08:15). Annie opens gifts: turntable, record, clothes, makeup, Kate Spade purse (10:18–10:19). Dan: *"There it is"* (recognizing the Kate Spade). Annie: *"First thing he played was the album from you and we listened all during breakfast"* (10:54). The turntable and record are from Will (Annie's brother). Dan: *"2015 is my fav Christmas of all time / It's better than my kid Christmases when I'd get mad toys and stuff / Last year I think I woke up at 3pm / On Christmas and couldn't have given less of a fuck that it was happening / I bought gifts for nobody / Idk everything just feels super different / YOU did this!"* (10:32–10:39). This is Dan's most explicit statement of what Christmas means to him — the contrast between last year (alone, 3pm wakeup, no gifts) and this year (with Annie).

**2015-12-25, ~11:28 — Fran's nosebleed, and Dan's hospital break-out story.** Fran gets a nosebleed from too much zgurd (whiskey). Dan: *"I tried to break her out of the hospital one time because she asked me to / Every time I ask her to do some crazy ass favor me / She ALWAYS comes through / So when the time came that I got asked / Come on how do I say no / I mean I wasn't really taking her out / But I made her think j was"* (11:28–11:30). This is the earliest documented instance of Dan's caregiving relationship with Fran — he visits her in the hospital, she asks for favors, he can't say no.

**2015-12-25, ~13:30 — Annie tells family about the hair appointment.** Annie: *"I told my family / They were like are you serious / They got so excited"* (13:30). The hair appointment is for Dan — Annie is getting her hair done so she can cut Dan's hair. This is the first documented instance of Annie's family knowing about the relationship in a positive context — they're excited.

**2015-12-25, ~14:32 — Annie bored at family dinner, Dan keeps her company.** Annie: *"I'm gonna need zgurd to get through this fucking family dinner with my dads fam"* (14:32). Dan: *"From suz"* (14:33). Annie: *"Get me out of here"* (18:46). Dan: *"I'm boreder than bored at suz's"* (18:50). Annie comes to Suz's after dinner. Suz brings zgurd. Dan: *"I got a second wind"* (20:50). Annie: *"OMG OMG ONG / CAN YOU BURN IT ON A DISK"* (18:49) — she wants a movie burned to DVD. They hang at Suz's.

**2015-12-29, ~13:32 — Dan has zgurd, and Annie peeps.** Dan: *"hi bb / my phone died 😟 / i'm atmy moms office / got zgurd"* (13:32). Annie: *"YOU PEEPIN?"* (13:48). Dan caught her: *"aw i caught u / peepy girlfriend / detective dan"* (13:48). Annie peeping at Dan's house. This is the second documented "peep" instance (first was Dec 14).

**2015-12-29, ~14:12 — Ex boyfriend drama (Becca).** Annie: *"I knew it was ex boyfriend issues / Over it"* (14:12–14:17). Becca is the ex's new girlfriend. Annie is over it. Dan is supportive.

**2015-12-29, ~17:43 — Annie tells Dan about the needle incident.** ([[wiki/mind/synthesis/supply-network]]) Annie: *"Speaking of.... I forgot to tell you this / One of the last times I was over at j's / There was some dude there / He literally gave me and chunk of ice... / I didn't ask for it / I didn't say no. / He just gave me it"* (17:43–17:52). Dan: *"Oh my! That's intense / I mean I've never done it but someone giving it to you is intense"* (17:48–17:52). Dan: *"Were you asking if I wanted to try? Or just telling me about it?"* (17:52). Annie: *"I guess both"* (17:52). Dan: *"First of all I always appreciate your honesty. You really do everything possible to make sure that I know I can trust your completely / I'll think about it b. It's a possibility. Btw- you should feel good that I gave you ^that answer. For the first time in my adult life I feel happy, and I'm not using drugs to derive smiles"* (17:53–17:56). Annie: *"I'm a sponge when it comes to peer pressure / I just suck it all in and don't give a fuck"* (18:08). Dan: *"I just wanna make sure that you have the same strength to face adversity / Because you'll know that there's someone who looks at you like a goddess...and thinks you're perfect / And wants to make sure you don't feel used or manipulated"* (18:11–18:14). This is the most extensive discussion of boundaries and drug use in the record — Dan acknowledges the appeal but worries about "adding (or subtracting) anything else from the equation."

**2015-12-29, ~18:23 — "You're the only thing that makes life seem like magic again."** Dan: *"Anne you're the only thing that makes life seem like magic again. You're the only thing that makes me feel like the cloud of 'bad' that i lived in for over a decade, has been lifted"* (18:23). This is a restatement of the Dec 16 "magic" line, but in the context of the needle discussion — Dan is saying Annie does for him what drugs never could.

**2015-12-29, ~19:08 — Dan gets zgurd, Annie stresses about money.** Suz gives Dan zgurd. Annie stressed about spending. Dan: *"Do u know how much I spent on that stuff today? / $200"* (23:46–23:47). Annie: *"Exactly... / Some people can't even get $200 to pay their rent. / If I had $200 right now I'd pay my damn dentist bill / And that $200 wasn't even your own"* (23:47–23:48). Dan: *"It was my money"* (23:50). Annie: *"We gotta really cut back for real this time"* (23:24). This is the earliest documented instance of Annie naming the cost of cocaine as a problem — she's been saying "cut back" since Dec 14, but this is the first time she names $200 as the specific amount.

**2015-12-29, ~23:23 — "I want stability. Jobs."** ([[wiki/mind/synthesis/supply-network]], [[wiki/people/suzanne-frank]]) Annie: *"I don't want you having to take people's money. I don't want that. / I want to grow / I want stability / Our own money / Jobs / I don't want to fall into a deeper hole than we already our in"* (23:25–23:28). Dan: *"I want that too and I feel bad for making it easier for us to have it all the time"* (23:28). Annie: *"You may have had to provide lex with drugs too much / And I'm not like that"* (23:43). This is Annie's most explicit statement of what she wants — stability, jobs, money, growth — and her first direct comparison with Alexis around drug provision.

**2015-12-29, ~23:44 — "Let's cut this shit out so we can be really happy."** Dan: *"I'm sorry if I've used drugs as a perk. I've just really been consumed with trying to impress you or provide stuff"* (23:42). Annie: *"I don't need all that. I have you / And you are all I need"* (23:43). Dan: *"You couldn't be further from her in that regard. You're conscientious and considerate / But let's cut this shit out so we can be really happy"* (23:44–23:45). This is Dan's most explicit statement of cutting back — not just "cut back" but "cut this shit out."

**2015-12-30, ~00:18 — "Thank you for being the best friend and best girlfriend imaginable."** Dan: *"Goodnight and try to remember how happy you've made me. You really deserve to go to sleep with a smile / Thank you for being the best friend and best girlfriend imaginable"* (00:18–00:18). Annie: *"I am smiling now / You're my best friend / And the best boyfriend ever"* (00:18–00:19).

**2015-12-30, ~01:29 — Lukyan drops off greens.** Dan accidentally sends Annie a message meant for Lukyan: *"Cmon in / Oops meant to send to Lukyan. He's dropping off some greens for our 'stay away from coca' plan"* (01:29–01:30). This is the first documented instance of "Lukyan" — he's dropping off marijuana (greens) as part of the cocaine-avoidance plan.

**2015-12-30, ~11:55 — Annie is working NYE.** Annie: *"Wow. I'm working New Year's Eve / I guess it's a good thing.. I need money bad"* (11:55–12:03). Bruce says Annie should "help" bar NYE. Annie: *"Better mean me and another girl behind the bar. Or I'll be pissed"* (12:22).

**2015-12-30, ~12:13 — "You're being a pain."** Bruce to Annie: *"You're being a pain"* (13:21). Annie furious. Dan: *"YOU are being a pain?! / After the bullshit they put you through the last two weeks??"* (13:21–13:22). Annie: *"See if I show up tomorrow"* (13:22). Annie's mom is not happy. Dan: *"Good lets start a boycott / Online petition / Awareness campaign"* (13:25).

**2015-12-30, ~13:05 — Dan gets groceries, ceiling leak.** Dan gets Hawaiian rolls from Aldi. Annie: *"The ceiling is soaked / Holding water and getting heavy"* (17:53–17:54). Dan doesn't understand what she wants him to do. Annie: *"You need like a plastic tube container thing / Tub / To put under it"* (17:55). Ceiling leak from toilet upstairs. Dan: *"It's not as bad as I thought"* (17:56).

**2015-12-30, ~17:04 — Annie on edge, Dan offers cocaine.** Annie: *"Well I freakin want ❄️"* (17:04). Dan: *"We're being good kids for at least one day! / Well I am at least lol / I need to prove to you that I want to do it!"* (17:05–17:06). Dan: *"What about tomorrow! We'll get some for nye"* (17:07). Annie: *"Well I'll be fucking work"* (17:07). Dan offers to get something. Annie talks him down. Dan: *"I really do want you to know I was serious about the stuff I said last night / So I will leave it up to you. If you want to get something just tell me and we'll figure out how to make that happen"* (17:12).

**2015-12-30, ~17:34 — Chuck and Luke procurement.** Annie stressed about spending. Dan: *"Did you see about what we could do for chuck"* (17:16) — Chuck is a contact who might come through. Dan: *"Luke is gonna have it ready / Make sure chuck brings something for us"* (18:57–18:58). Dan: *"320 is a friend price. It should be 350 / So if he can hook us up with something that would be extra extra dope"* (19:11). Annie stressed. Dan: *"Need to let Luke know"* (19:18). Annie cancels. Dan: *"Someone wanted 25% of what we were going to get / So there's lots left and he said he already called Zach to arrange for more"* (19:30). Dan gets weed from Luke. Annie: *"Cool I'll come get you. Then bank. Then Luke. Then home"* (19:33).

**2015-12-30, ~21:55 — Cooking and couscous.** Dan makes cookies and couscous. Annie: *"Nom nom"* (22:28). Dan: *"I'm baked and there's food here / It was bound to happen"* (22:03–22:04). Annie: *"Cookies and couscous / Today is sponsored by the letter c"* (22:04). Dan: *"You trying to put on a ski mask and head to sheetz huh? / Like an old time bandit"* (22:05).

**2015-12-30, ~22:30 — "I will fix it" (haircut).** Dan: *"I love you Annie and I feel like the luckiest guy ever / And you slayed it on my haircut / Promise it's perfect"* (22:33). Annie: *"Argh I hope / I will fix it"* (22:33–22:34). Dan: *"It is. Pinky. come watch skins with me sometime"* (22:34). Annie: *"Hehehh it's a date"* (22:34).

**2015-12-30, ~22:32 — Flowers from Dan.** Annie: *"I love you beeb thank you for being here for me. And thank you the flowers :)"* (22:32). This is the first documented instance of Dan giving Annie flowers.

**2015-12-31, ~09:00 — New Year's Eve morning.** Dan: *"Good morning wonderful girlfriend"* (08:55). Annie: *"I am lovely"* (08:56). Dan: *"Suz said she's getting her NYE zgurd at 1pm"* (09:03). Annie: *"B 😩 / I'm so sorry I have to work"* (09:04–09:05). Dan: *"It's fine I promise / I mean I'll miss you of course / But I understand!"* (09:05).

**2015-12-31, ~10:24 — Dan's bad dream.** Dan: *"I had a bad dream a minute aging / You didn't like me again / And it was turriblw"* (10:24–10:25). This is the earliest documented instance of Dan's abandonment anxiety — he dreams Annie doesn't like him anymore.

**2015-12-31, ~10:30 — "This is the first time in my whole life that I am happy to leave this past year behind."** Annie: *"This is the first time in my whole life that I am happy to leave this past year behind"* (09:52). This is Annie's most explicit statement of what 2015 meant to her — the year she met Dan, the year she wants to leave behind.

**2015-12-31, ~13:39 — Vapor Hut trip.** Dan makes a quick trip to Vapor Hut: *"VAPPPPORHUT"* (13:41). Annie: *"My boyfriend 😻😻😻😒 / Minus that last one"* (13:41). Dan: *"I'm about to make a quick trip to vaporhut"* (13:39). He gets new coils for his vape.

**2015-12-31, ~16:11 — "Some girl here wants to meet u."** Dan: *"Some girl here wants to meet u / I love u bye have fun"* (16:11–16:12). A girl at CT's wants to meet Annie. Dan has to leave.

**2015-12-31, ~16:31 — Annie is serving, not bartending.** Annie: *"The other bar tender just goes I just talked to Chris he said you're serving unless the bar gets busy / Dear lord Suz hurry before I lose my shit / I'm fucking livid / Beyond livid / I haven't worked in weeks / And they can't just put me behind the bar?"* (16:31–16:53). Dan: *"OMFGGGG / are you KIDDDDING ME / They tricked you!!"* (16:31–16:33). Annie was told she'd be bartending; now she's serving. Dan is furious on her behalf.

**2015-12-31, ~17:22 — Dan gets zgurd from Suz.** Dan: *"Okay so I have really good news and KINDA bad news / Good news is that I got the zgurd / Bad news is I'm coming down alone"* (17:29–17:31). Dan: *"She only had 300 total so I got like 120"* (17:44). Dan comes down to CT's.

**2015-12-31, ~20:10 — "Swear this is my last night."** Annie: *"Everyone is being so fucking sassy / Russ keeps yelling at me / Saying I'm not gonna make any tips / Swear this is my last night"* (20:09–20:10). Annie: *"That club wants me to work as a cocktail waitress starting tomorrow"* (20:10). Dan: *"What the FUCK is wrong with everybody there / Like they all suck so bad"* (20:10).

**2015-12-31, ~21:11 — Annie makes money.** Annie: *"I did find a check for me / $60 some / And I made like $80 off two tables / Probably more than I would have made off the bar"* (21:11–21:14). Dan: *"Whoa look at you go"* (21:12).

**2015-12-31, ~21:31 — "We gotta watch the ball drop somewhere."** Annie: *"We gotta watch the ball drop somewhere"* (21:33). Dan: *"Where do You want togo"* (21:41). Annie: *"Somewhere"* (21:44). Dan: *"Chris is gonna call you / He wants you to dj / Say you can't / So we can leave / And go elsewhere"* (21:54–21:55). Annie wants Dan to say no to DJing so they can leave together.

**2015-12-31, ~22:10 — Annie cashes out.** Annie: *"Dj has arrived / I cashed out in my tips. / I said I'm peacing out when Chris asked me to wait on him and Robyn"* (22:10–22:10). Annie quits for the night.

**2015-12-31, ~22:20 — "I love you more than life itself."** Dan: *"I love you too / I had pressed end before I heard you I'm sorry / I love you a lot / Sorry"* (22:20–22:22). Dan: *"I love you Annie I had pressed end before I heard you I'm sorry"* (22:20). Annie: *"It's okay!!!"* (22:23).

*(2015-12-31 read in full. Resume at 2016-01-01.)*

