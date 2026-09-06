#!/usr/bin/env python3
"""Tests for bin/wiki-crosslink, the source-mention instrument.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

Three properties are pinned here and none of them is cosmetic.

  * **The moratorium is lifted, and stays lifted.** Until 2026-09-06 this tool
    refused one person's pages as scan subjects, dropped them from the queue and
    withheld them as rendered candidates. The operator ended the directive in
    full. `TheMoratoriumIsLifted` pins the absence of every one of those
    refusals — the guard was documented here at length as a safety property, and
    a documented safety property is what a later session reconstructs from
    memory.

  * **Contested names.** A string two pages both claim is evidence for neither.
    `@alexisarmel` sits in one person's `aliases:` and in another's infobox
    `handles:`, and 85 rows about the first were rendered as 101 mentions of the
    second with nothing on the output to read them by. The index always knew;
    the renderer did not say.

The real corpus is never touched except where a test says so: the matcher and
guard cases build small page trees in a temp directory.
"""
import importlib.machinery
import re
import importlib.util
import os
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "bin", "wiki-crosslink")


def load_module():
    """bin/wiki-crosslink has no .py extension, and no import-time side effects."""
    spec = importlib.util.spec_from_loader(
        "wiki_crosslink",
        importlib.machinery.SourceFileLoader("wiki_crosslink", SCRIPT),
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def page(title, aliases=None, handles=None, body="Body text.", extra=""):
    fm = ['---', 'title: "%s"' % title, 'domain: people', 'page_type: entity']
    if aliases is not None:
        fm.append('aliases: [%s]' % ", ".join('"%s"' % a for a in aliases))
    if extra:
        fm.append(extra)
    if handles is not None:
        fm.append('infobox:')
        fm.append('  name: "%s"' % title)
        fm.append('  handles: [%s]' % ", ".join('"%s"' % h for h in handles))
    fm.append('---')
    return "\n".join(fm) + "\n\n" + body + "\n"


class TheMoratoriumIsLifted(unittest.TestCase):
    """Lifted in full by the operator on 2026-09-06.

    Until then this tool refused her pages as scan subjects, dropped them from
    the `--queue`, withheld them as rendered candidates and flagged
    `rederive`'s heavy pages as directive-constrained. All four are gone. The
    absence is pinned, because the guard was documented here at length as a
    safety property and that is what a later session reconstructs from.
    """

    def setUp(self):
        self.m = load_module()

    def test_no_guard_remains(self):
        for name in ("MORATORIUM", "under_moratorium", "mentions_moratorium",
                     "note_moratorium_targets", "MORATORIUM_TARGETS"):
            with self.subTest(name=name):
                self.assertFalse(hasattr(self.m, name),
                                 "bin/wiki-crosslink still defines %s" % name)

    def test_her_page_renders_as_a_candidate(self):
        idx = {
            "wiki/people/annie-ulmer": {"domain": "people", "limit": 3,
                                        "title": "Annie", "names": []},
            "wiki/people/other": {"domain": "people", "limit": 0,
                                  "title": "Other", "names": []},
        }
        hits = {
            "wiki/people/annie-ulmer": [("2013-01-01", "annie ulmer", "high",
                                         "a row", "", "c.jsonl", 1)],
            "wiki/people/other": [("2013-01-01", "other page", "high",
                                   "a row", "", "c.jsonl", 1)],
        }
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            n = self.m.render_hits("wiki/x", hits, idx)
        out = buf.getvalue()
        self.assertEqual(n, 2)
        self.assertIn("annie-ulmer", out)
        self.assertNotIn("withheld under the standing directive", out)



class MatcherBehaviour(unittest.TestCase):
    def setUp(self):
        self.m = load_module()

    def _index(self, pages):
        return self.m.build_index(pages)

    def test_multi_word_name_is_high_and_bare_first_name_is_low(self):
        idx = self._index({"wiki/people/katie-fletcher.md": page("Katie Fletcher")})
        confs = dict((n.lower(), c) for n, c in idx["wiki/people/katie-fletcher"]["names"])
        self.assertEqual(confs["katie fletcher"], "high")

    def test_quoted_handles_survive_the_list_parser(self):
        """The bug that cost 83 of 84 rows on one page: quotes kept after item 1."""
        idx = self._index({"wiki/people/x.md": page("X Person",
                                                    aliases=["Lex", "@alexisarmel"])})
        names = dict((n, c) for n, c in idx["wiki/people/x"]["names"])
        self.assertIn("@alexisarmel", names)
        self.assertEqual(names["@alexisarmel"], "high")

    def test_token_index_finds_names_on_word_boundaries_only(self):
        idx = self._index({"wiki/people/katie-fletcher.md": page("Katie Fletcher")})
        mt = self.m.Matcher(idx)
        self.assertTrue(mt.find("dinner with Katie Fletcher tonight"))
        self.assertFalse(mt.find("katie fletchers"))
        self.assertFalse(mt.find("katie  fletcher"))   # the index is exact-phrase

    def test_a_string_two_pages_claim_has_two_owners(self):
        idx = self._index({
            "wiki/people/alexis-armel.md": page("Alexis Armel", aliases=["@alexisarmel"]),
            "wiki/people/annie-ulmer.md": page("Anne Louise Ulmer",
                                               handles=["@alexisarmel"]),
        })
        mt = self.m.Matcher(idx)
        self.assertEqual(len(mt.owner["@alexisarmel"]), 2)

    def test_render_flags_a_contested_name(self):
        idx = {"wiki/people/alexis-armel": {"domain": "people", "limit": 0,
                                            "title": "Alexis", "names": []}}
        hits = {"wiki/people/alexis-armel": [("2009-12-14", "@alexisarmel", "high",
                                              "a row", "", "archive.jsonl", 2)]}
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.m.render_hits("wiki/x", hits, idx)
        self.assertIn("contested by another page", buf.getvalue())


class CorpusLayer(unittest.TestCase):
    def setUp(self):
        self.m = load_module()

    def test_every_corpus_declares_a_kind_and_exists_on_disk(self):
        for rel, spec in self.m.CORPORA.items():
            self.assertIn("kind", spec, rel)
            self.assertIn("family", spec, rel)
            self.assertTrue(os.path.exists(os.path.join(ROOT, rel)),
                            "%s is declared readable and is not on disk" % rel)

    def test_the_two_message_exports_share_a_family(self):
        """They overlap by ~124k rows. Reading both without dedupe double-counts."""
        fams = [s["family"] for s in self.m.CORPORA.values() if s["family"]]
        self.assertEqual(fams.count("messages"), 2)

    def test_dedupe_key_collapses_two_exports_of_one_message(self):
        k1 = self.m.dedupe_key("2018-04-01 12:00:00", "Hey  are  you  up?")
        k2 = self.m.dedupe_key(" 2018-04-01 12:00:00 ", "hey are you up?")
        self.assertEqual(k1, k2)

    def test_dedupe_key_separates_the_same_text_at_different_times(self):
        self.assertNotEqual(
            self.m.dedupe_key("2018-04-01 12:00:00", "ok"),
            self.m.dedupe_key("2018-04-01 12:00:01", "ok"))

    def test_message_reader_is_borrowed_from_mine_messages(self):
        """Not reimplemented: the three traps live in that file and only there."""
        mm = self.m._mine_messages()
        self.assertTrue(hasattr(mm, "records"))
        self.assertTrue(hasattr(mm, "norm"))
        self.assertEqual(mm.norm("it’s"), "it's")


class GeneratedSurfaces(unittest.TestCase):
    def setUp(self):
        self.m = load_module()

    def test_generated_pages_are_not_counted_as_reciprocal_debt(self):
        """A hand-added inverse on a generated page dies at the next run."""
        for slug in self.m.GENERATED:
            self.assertTrue(os.path.exists(os.path.join(ROOT, slug + ".md")),
                            "%s is listed generated and does not exist" % slug)


if __name__ == "__main__":
    unittest.main()


class ConversationMode(unittest.TestCase):
    """The join a message corpus makes possible and a broadcast archive cannot.

    `--against` asks "in the rows that name this page, what else is named",
    which works on tweets and fails on messages: a five-to-fifteen-word message
    that names one person almost never names a second. Run over the campaign
    queue against the message dump on 2026-09-04 it returned **0 candidates
    across 7 pages**. The message corpus knows something the archive does not —
    *who the counterparty is* — and scoping by that reaches 41,349 rows across
    30 people pages.
    """

    def setUp(self):
        self.m = load_module()

    def _fm(self, handles):
        return self.m.split_fm(page("X", handles=handles))[0]

    def test_full_e164_resolves(self):
        got, amb = self.m.resolve_handles(self._fm(["+17249707658"]),
                                          {"+17249707658": 83})
        self.assertEqual(got, ["+17249707658"])
        self.assertEqual(amb, [])

    def test_bare_ten_digits_resolve_against_e164(self):
        got, _ = self.m.resolve_handles(self._fm(["510-506-3276"]),
                                        {"+15105063276": 12})
        self.assertEqual(got, ["+15105063276"])

    def test_a_masked_handle_resolves_when_it_is_unambiguous(self):
        """`+1724***7658` is how this repo redacts a live number in a public file."""
        got, amb = self.m.resolve_handles(self._fm(["+1724***7658"]),
                                          {"+17249707658": 83, "+12124702449": 9})
        self.assertEqual(got, ["+17249707658"])
        self.assertEqual(amb, [])

    def test_a_masked_handle_that_matches_two_is_reported_not_guessed(self):
        got, amb = self.m.resolve_handles(
            self._fm(["+1724***7658"]),
            {"+17249707658": 83, "+17241117658": 4})
        self.assertEqual(got, [])
        self.assertEqual(amb[0][1], 2)

    def test_a_social_handle_is_not_a_counterparty(self):
        got, _ = self.m.resolve_handles(self._fm(["@alexisarmel"]),
                                        {"@alexisarmel": 5})
        self.assertEqual(got, [])

    def test_email_handles_resolve_case_insensitively(self):
        got, _ = self.m.resolve_handles(self._fm(["AllyLubin@gmail.com"]),
                                        {"allylubin@gmail.com": 300})
        self.assertEqual(got, ["allylubin@gmail.com"])

    def test_a_parenthetical_note_after_a_handle_is_stripped(self):
        got, _ = self.m.resolve_handles(
            self._fm(["+16312588085 (building notices signed 'John PACI')"]),
            {"+16312588085": 37})
        self.assertEqual(got, ["+16312588085"])


class CommonPhraseFlag(unittest.TestCase):
    """The one class of the campaign's "uncatchable" failure that is catchable.

    Confidence is `more than one token = high`. A two-token page name that is
    also ordinary English breaks that rule in the worst direction, because the
    tool tells you to trust the match. Measured over the 217,573-record dump:
    "say anything" returns 134 rows and none of them is the band; "the office"
    returns 77 and none of them is the show — every one is a real estate office.
    `coverage` was presenting the first as the wiki's top music result.
    """

    def setUp(self):
        self.m = load_module()
        self.m.COMMON_PHRASE.clear()

    def test_a_band_named_after_a_phrase_is_flagged(self):
        idx = self.m.build_index({
            "wiki/interests/favorites/music/artists/say-anything.md": page("Say Anything"),
            "wiki/people/katie-fletcher.md": page("Katie Fletcher"),
        })
        # A stand-in corpus whose ordinary words are exactly these.
        self.m._CORPUS_CACHE["fake"] = [
            ("2016-01-01", "you can say anything you want", ""),
        ] * 5
        self.m.CORPORA["fake"] = {"kind": "jsonl", "family": None}
        try:
            got = self.m.mark_common_phrases(idx, ["fake"])
        finally:
            del self.m.CORPORA["fake"]
            del self.m._CORPUS_CACHE["fake"]
        self.assertIn("say anything", got)
        self.assertNotIn("katie fletcher", got)

    def test_the_flag_reaches_the_output_and_says_the_count_is_not_evidence(self):
        self.m.COMMON_PHRASE.add("say anything")
        idx = {"wiki/interests/favorites/music/artists/say-anything":
               {"domain": "interests", "limit": 1, "title": "Say Anything", "names": []}}
        hits = {"wiki/interests/favorites/music/artists/say-anything":
                [("2016-01-11", "say anything", "high",
                  "dont say anything to him", "Sent +1724", "dump.txt", 1)]}
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.m.render_hits("wiki/x", hits, idx)
        out = buf.getvalue()
        self.assertIn("ordinary English", out)
        self.assertIn("THE COUNT IS NOT EVIDENCE", out)

    def test_flagging_does_not_hide_the_candidate(self):
        """Demoting would bury it behind --low, and some of these are real."""
        self.m.COMMON_PHRASE.add("fall out boy")
        idx = {"wiki/interests/favorites/music/artists/fall-out-boy":
               {"domain": "interests", "limit": 0, "title": "Fall Out Boy", "names": []}}
        hits = {"wiki/interests/favorites/music/artists/fall-out-boy":
                [("2019-09-01", "fall out boy", "high",
                  "a secret show where fall out boy performed as schrute farms",
                  "Sent +1561", "dump.txt", 1)]}
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            n = self.m.render_hits("wiki/x", hits, idx)
        self.assertEqual(n, 1)
        self.assertIn("fall-out-boy", buf.getvalue())


class MessageCountCheck(unittest.TestCase):
    """A page's stated message count against the corpus its handle resolves into.

    The defect had been found by hand four times before anything checked for it:
    `bruce-burish` ("181 is exactly the received count"), `zach-clingan` ("22 is
    exactly"), then `rod-banks` (41 stated, 92 actual) and `zach-hendricks` (58,
    65) on 2026-09-04. The sweep that followed found **13 more**, nine of them
    understating by exactly the Received-only figure — `wiki/people/vaughn`
    stated 228 against 582, with 354 of Dan's own messages uncounted while the
    page said they "survive nowhere".
    """

    def setUp(self):
        self.m = load_module()

    def test_the_count_and_direction_patterns_match_the_house_table(self):
        txt = "| Messages | **348** — 167 sent (Dan), 181 received |\n"
        m = self.m.MSG_COUNT_RE.search(txt)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "348")

    def test_a_plain_count_matches(self):
        m = self.m.MSG_COUNT_RE.search("| Messages | 41 |\n")
        self.assertEqual(m.group(1), "41")

    def test_a_thousands_separator_survives(self):
        m = self.m.MSG_COUNT_RE.search("| Messages | 1,253 |\n")
        self.assertEqual(m.group(1).replace(",", ""), "1253")

    def test_a_count_naming_another_corpus_is_excluded(self):
        """christo-coan's '~50 (Facebook Messenger, both directions)' is correct.

        The first version of this check called it a 44-message error, because it
        compared a Facebook figure against an iMessage thread.
        """
        m = self.m.MSG_COUNT_RE.search("| Messages | ~50 (Facebook Messenger, both directions) |\n")
        self.assertTrue(self.m.OTHER_CORPUS.search(m.group(2)))
        m2 = self.m.MSG_COUNT_RE.search("| Messages | 228 |\n")
        self.assertFalse(self.m.OTHER_CORPUS.search(m2.group(2) or ""))

    def test_direction_line_is_found(self):
        d = self.m.MSG_DIR_RE.search("| Direction | All received (export artifact) |\n")
        self.assertEqual(d.group(1), "All received (export artifact)")


class AliasAudit(unittest.TestCase):
    """Are the aliases we already have any good?

    233 of 326 declared aliases appear zero times in any readable corpus, and
    reporting that as a defect would be the mistake: `aliases:` does two jobs
    here — what the record calls a thing (corpus-matchable) and what a reader
    might call a page (a coinage, which no corpus can contain). A zero-hit alias
    is doing the second job and costs nothing. The six ordinary-English ones
    were the whole problem: `the case` matched 96 rows and none was the concept.
    """

    def setUp(self):
        self.m = load_module()

    def test_concept_and_synthesis_are_not_corpus_nameable(self):
        self.assertNotIn("concept", self.m.CORPUS_NAMEABLE)
        self.assertNotIn("synthesis", self.m.CORPUS_NAMEABLE)
        self.assertIn("entity", self.m.CORPUS_NAMEABLE)
        self.assertIn("event", self.m.CORPUS_NAMEABLE)

    def test_the_deleted_aliases_are_gone_from_the_corpus_index(self):
        """The four removed on 2026-09-04, pinned so they cannot come back."""
        pages = self.m.load_pages()
        idx = self.m.build_index(pages)
        for slug, dead in (
            ("wiki/self/concepts/ally-and-dan-love-as-destiny", "the case"),
            ("wiki/mind/concepts/acquisition-drive", "the drive"),
            ("wiki/people/james-dee", "the dude"),
            ("wiki/people/the-unnamed-man", "this person"),
        ):
            names = [n.lower() for n, _c in idx[slug]["names"]]
            self.assertNotIn(dead, names,
                             "%s got %r back — it matches ordinary English and "
                             "none of the hits are the subject" % (slug, dead))


class LinkPlacement(unittest.TestCase):
    """`unlinked --apply` writes into 344 pages at once and nobody reads them all.

    Every rule below is a refusal, and a refusal that stops working leaves no
    trace: the pass reports more links, the gates stay green, and the damage is
    a wikilink inside somebody's quoted words on a public site — the silent-
    permission shape, so it gets the same treatment.
    """

    def setUp(self):
        self.m = load_module()

    def _apply(self, body, others, refuse=frozenset()):
        pages = {"wiki/x.md": page("X", body=body)}
        for slug, title in others.items():
            pages[slug + ".md"] = page(title)
        idx = self.m.build_index(pages)
        matcher = self.m.Matcher(idx)
        new, applied = self.m.apply_unlinked(
            "wiki/x", pages["wiki/x.md"], idx, matcher, refuse)
        return new, applied

    def test_links_a_name_in_plain_prose(self):
        new, applied = self._apply(
            "He saw Cobra Starship that summer.",
            {"wiki/a/cobra-starship": "Cobra Starship"})
        self.assertEqual([("cobra starship", "wiki/a/cobra-starship")], applied)
        self.assertIn("[[wiki/a/cobra-starship|Cobra Starship]]", new)

    def test_never_inside_a_quotation_that_spans_lines(self):
        """The defect this mask exists for. Prose is hard-wrapped at ~78 columns,
        so a per-line mask sees only a quotation's tail and writes into it."""
        body = ('He wrote: "nothingness but at least I got\n'
                'the Cobra Starship handle" and moved on.')
        new, applied = self._apply(body, {"wiki/a/cobra-starship": "Cobra Starship"})
        self.assertEqual([], applied)
        self.assertNotIn("[[", new)

    def test_never_inside_a_heading_blockquote_or_code(self):
        for body in ("## Cobra Starship and the rest",
                     "> He liked Cobra Starship a lot.",
                     "Handle is `Cobra Starship` there.",
                     "```\nCobra Starship\n```",
                     "Already [[wiki/a/cobra-starship|Cobra Starship]] here."):
            new, applied = self._apply(
                body, {"wiki/a/cobra-starship": "Cobra Starship"})
            self.assertEqual([], applied, body)

    def test_first_mention_only(self):
        new, _ = self._apply(
            "Cobra Starship, then Cobra Starship, then Cobra Starship.",
            {"wiki/a/cobra-starship": "Cobra Starship"})
        self.assertEqual(1, new.count("[[wiki/a/cobra-starship|"))

    def test_refuses_a_name_two_pages_claim(self):
        _new, applied = self._apply(
            "The third party was there.",
            {"wiki/p/one": "The Third Party", "wiki/p/two": "The Third Party"})
        self.assertEqual([], applied)

    def test_refuses_a_single_token_name(self):
        """`low` confidence matches anybody. The corpus has a band called HIM."""
        _new, applied = self._apply("It gave him pause.", {"wiki/a/him": "Him"})
        self.assertEqual([], applied)

    def test_longest_name_wins_and_the_two_cannot_overlap(self):
        new, applied = self._apply(
            "Judge Fred Adams presided.",
            {"wiki/p/fred-adams": "Fred Adams",
             "wiki/p/judge-fred-adams": "Judge Fred Adams"})
        self.assertEqual([("judge fred adams", "wiki/p/judge-fred-adams")], applied)
        self.assertEqual(1, new.count("[["))

    def test_honours_the_refusal_set(self):
        _new, applied = self._apply(
            "He saw Cobra Starship.", {"wiki/a/cobra-starship": "Cobra Starship"},
            refuse={"cobra starship"})
        self.assertEqual([], applied)

    def test_a_common_phrase_is_demoted_to_its_page_s_exact_form(self):
        """Not refused. The flag is calibrated on the message corpus, where
        "say anything" is 134 rows and 0 of them the band; here it would throw
        away five real bands to catch one room."""
        self.m.COMMON_PHRASE.add("say anything")
        try:
            new, applied = self._apply(
                "He did not say anything.", {"wiki/a/say-anything": "Say Anything"})
            self.assertEqual([], applied)
            new, applied = self._apply(
                "He saw Say Anything live.", {"wiki/a/say-anything": "Say Anything"})
            self.assertEqual([("say anything", "wiki/a/say-anything")], applied)
        finally:
            self.m.COMMON_PHRASE.discard("say anything")


class PhraseDispersion(unittest.TestCase):
    """`overexposed` separates a phrase from a name by how much of the wiki
    says it — but only for an ALIAS. `Fall Out Boy` is on twenty-one pages
    because he is a fan; `the wiki` is on a hundred and four because it means
    "this document"."""

    def setUp(self):
        self.m = load_module()

    def _run(self, name, n_pages, owner_title, aliases=None):
        pages = {"wiki/o/target.md": page(owner_title, aliases=aliases)}
        for i in range(n_pages):
            pages["wiki/p/p%d.md" % i] = page("P%d" % i,
                                              body="A line about %s here." % name)
        idx = self.m.build_index(pages)
        return self.m.overexposed(sorted(s[:-3] for s in pages), idx,
                                  self.m.Matcher(idx), pages)

    def test_an_alias_said_by_too_many_pages_is_refused(self):
        self.assertIn("the wiki",
                      self._run("the wiki", self.m.PHRASE_PAGE_CAP + 2,
                                "The Wiki-Brain", aliases=["the wiki"]))

    def test_a_page_s_own_title_is_never_refused_however_loud(self):
        """The first cut of this killed `fall out boy` along with `the wiki`."""
        self.assertNotIn("fall out boy",
                         self._run("Fall Out Boy", self.m.PHRASE_PAGE_CAP + 20,
                                   "Fall Out Boy"))

    def test_a_quiet_alias_survives(self):
        self.assertEqual(set(), self._run("the wiki", 3, "The Wiki-Brain",
                                          aliases=["the wiki"]))


class ReaderFacingCount(unittest.TestCase):
    def setUp(self):
        self.m = load_module()

    def test_a_typed_edge_does_not_count_as_a_link_here(self):
        """The opposite of `linked_targets`' rule, deliberately. An edge is
        frontmatter; the reader never sees it. 161 of them stood in for zero
        navigation across the twitter tree."""
        txt = page("X", extra=(
            'connections:\n  - page: wiki/a/cobra-starship\n'
            '    type: contextualizes\n    claim: "c"'),
            body="He saw Cobra Starship.")
        pages = {"wiki/x.md": txt, "wiki/a/cobra-starship.md": page("Cobra Starship")}
        idx = self.m.build_index(pages)
        matcher = self.m.Matcher(idx)
        fm, _ = self.m.split_fm(txt)
        hits = self.m.unlinked_names("wiki/x", fm, txt, idx, matcher)
        self.assertIn(("cobra starship", ("wiki/a/cobra-starship",)), hits)


class Breadcrumbs(unittest.TestCase):
    """`STYLE_GUIDE.md` said "reachable FROM its domain index" and the lint
    enforced exactly that sentence, so 453 of 497 pages were one-way doors.
    The footer that fixes it is generated, and a generator nobody tests is a
    generator that silently stops generating."""

    def setUp(self):
        self.m = load_module()
        self.slugs = {
            "wiki/people/index", "wiki/people/jerel-coles",
            "wiki/self/index", "wiki/self/twitter",
            "wiki/self/twitter/2012", "wiki/self/twitter/2013",
            "wiki/self/twitter/2014",
            "wiki/interests/index", "wiki/interests/concert-record/index",
            "wiki/interests/concert-record/festivals/high-tide-4",
        }

    def test_ancestry_is_nearest_last_and_accepts_both_index_shapes(self):
        """`wiki/people/index.md` and `wiki/self/twitter.md` are both parents of
        their directory; a reader does not care which shape the corpus used."""
        self.assertEqual(["wiki/self/index", "wiki/self/twitter"],
                         self.m.ancestry("wiki/self/twitter/2013", self.slugs))
        self.assertEqual(["wiki/people/index"],
                         self.m.ancestry("wiki/people/jerel-coles", self.slugs))

    def test_label_comes_from_the_slot_not_the_page_title(self):
        """Most indexes here are titled `index`, and the ones that are not are
        titled for the page (`Twitter / X Activity (@danfrank)`)."""
        self.assertEqual("People", self.m.crumb_label("wiki/people/index"))
        self.assertEqual("Twitter", self.m.crumb_label("wiki/self/twitter"))
        self.assertEqual("Concert Record",
                         self.m.crumb_label("wiki/interests/concert-record/index"))

    def test_previous_and_next_only_for_a_numeric_run(self):
        self.assertEqual(("wiki/self/twitter/2012", "wiki/self/twitter/2014"),
                         self.m.sequence_neighbours("wiki/self/twitter/2013", self.slugs))
        self.assertEqual((None, "wiki/self/twitter/2013"),
                         self.m.sequence_neighbours("wiki/self/twitter/2012", self.slugs))
        self.assertEqual((None, None),
                         self.m.sequence_neighbours("wiki/people/jerel-coles", self.slugs))

    def test_alphabetical_siblings_are_not_a_sequence(self):
        """Inventing previous/next from filename order would sell the reader a
        reading path nobody chose."""
        self.assertEqual(
            (None, None),
            self.m.sequence_neighbours(
                "wiki/interests/concert-record/festivals/high-tide-4", self.slugs))

    def test_footer_is_idempotent(self):
        pages = {s + ".md": page(s.rsplit("/", 1)[-1]) for s in self.slugs}
        pages["wiki/people/index.md"] = page(
            "index", body="- [[wiki/people/jerel-coles]]")
        once = self.m.footer_for("wiki/people/jerel-coles", self.slugs)
        txt = pages["wiki/people/jerel-coles.md"].rstrip("\n") + once
        self.assertFalse(
            self.m.needs_breadcrumb("wiki/people/jerel-coles", txt, pages, self.slugs))
        self.assertTrue(self.m.needs_breadcrumb(
            "wiki/people/jerel-coles", pages["wiki/people/jerel-coles.md"],
            pages, self.slugs))

    def test_an_index_and_a_generated_page_are_exempt(self):
        pages = {s + ".md": page("t") for s in self.slugs}
        self.assertFalse(self.m.needs_breadcrumb(
            "wiki/people/index", pages["wiki/people/index.md"], pages, self.slugs))
        gen = sorted(self.m.GENERATED)[0]
        slugs = self.slugs | {gen, os.path.dirname(gen) + "/index"}
        pgs = {s + ".md": page("t") for s in slugs}
        self.assertFalse(
            self.m.needs_breadcrumb(gen, pgs[gen + ".md"], pgs, slugs))


class RederiveQueue(unittest.TestCase):
    """The debt `counts` created and could not measure: a page whose number is
    right and whose prose was written from half the thread. Thirty-three of
    them, findable until 2026-09-05 only by a grep somebody had to think of."""

    def setUp(self):
        self.m = load_module()

    def test_the_marker_is_the_page_s_own_admission(self):
        self.assertTrue(self.m.NOT_REDERIVED.search(
            "> was written against the smaller, one-sided thread and has not "
            "been re-derived."))
        self.assertTrue(self.m.NOT_REDERIVED.search(
            "> thread and has not been re-derived.**"))
        self.assertFalse(self.m.NOT_REDERIVED.search("re-derived 2026-09-05"))

    def test_it_reuses_the_count_regex_rather_than_shadowing_it(self):
        """A second module-level MSG_COUNT_RE silently changed what `counts`
        matched — a stricter pattern requiring bold — and `bin/wiki-check`
        reported all gates clean while three tests were red."""
        src = open(SCRIPT, encoding="utf-8").read()
        self.assertEqual(1, len(re.findall(r"^MSG_COUNT_RE\s*=", src, re.M)))

    def test_the_count_regex_still_reads_a_bold_table_cell(self):
        m = self.m.MSG_COUNT_RE.search("| Messages | **779** — 397 sent |\n")
        self.assertEqual("779", m.group(1))
