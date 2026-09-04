#!/usr/bin/env python3
"""Tests for bin/wiki-crosslink, the source-mention instrument.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

Three properties are pinned here and none of them is cosmetic.

  * **The moratorium guard, on BOTH sides of the output.** `CLAUDE.md` carries a
    standing operator directive about a living person, and this tool is one of
    the two places it stops being something a session has to remember. It
    shipped enforcing the refusal in two places — scanning her page, and the
    `--queue` — and in neither of the two places where her page comes back as a
    *candidate*, which is a worklist entry whichever column it lands in. A scan
    of `wiki/interests/concert-record/index` on 2026-09-04 offered her page as a
    target with 101 mentions. A guard whose failure mode is silent permission
    gets a test, exactly as `bin/wiki-plain`'s did.

  * **The guard's deliberate narrowness.** It refuses pages that ARE about her
    and not pages that merely name her, because porting `bin/wiki-plain`'s
    body-mention threshold across would withhold 197 of 497 pages for no safety
    gained. That is a decision, not an oversight, so it is pinned in both
    directions — a test that only checked the refusal would be satisfied by a
    guard that refused everything.

  * **Contested names.** A string two pages both claim is evidence for neither.
    `@alexisarmel` sits in one person's `aliases:` and in another's infobox
    `handles:`, and 85 rows about the first were rendered as 101 mentions of the
    second with nothing on the output to read them by. The index always knew;
    the renderer did not say.

The real corpus is never touched except where a test says so: the matcher and
guard cases build small page trees in a temp directory.
"""
import importlib.machinery
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


class Moratorium(unittest.TestCase):
    def setUp(self):
        self.m = load_module()

    def test_refuses_a_page_that_is_about_her(self):
        self.assertTrue(self.m.under_moratorium(page("Annie (Anne Louise Ulmer)")))
        self.assertTrue(self.m.under_moratorium(page("Someone", aliases=["Annie"])))
        self.assertTrue(self.m.under_moratorium(page("Ellen Ulmer")))

    def test_does_not_refuse_a_page_that_merely_names_her(self):
        """The narrowness is the decision. 197 of 497 pages name her in passing."""
        txt = page("Golf", body="He played with Annie in 2019. Ulmer came too.")
        self.assertFalse(self.m.under_moratorium(txt))
        self.assertEqual(self.m.mentions_moratorium(txt), 2)

    def test_target_set_covers_her_pages_only(self):
        pages = {
            "wiki/people/annie-ulmer.md": page("Annie (Anne Louise Ulmer)"),
            "wiki/interests/golf.md": page("Golf", body="Annie liked it."),
        }
        got = self.m.note_moratorium_targets(pages)
        self.assertEqual(got, {"wiki/people/annie-ulmer"})

    def test_render_withholds_her_page_as_a_candidate(self):
        """The leak. She was refused as a scan SUBJECT and served as a TARGET."""
        self.m.note_moratorium_targets(
            {"wiki/people/annie-ulmer.md": page("Annie (Anne Louise Ulmer)")}
        )
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
        self.assertEqual(n, 1)
        self.assertNotIn("annie-ulmer", out)
        self.assertIn("withheld under the standing directive", out)


class MatcherBehaviour(unittest.TestCase):
    def setUp(self):
        self.m = load_module()
        self.m.MORATORIUM_TARGETS.clear()

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
