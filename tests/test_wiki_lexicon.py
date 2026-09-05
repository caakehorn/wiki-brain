"""Tests for bin/wiki-lexicon — the measured lexicon.

The expensive half (`mine`) reads four corpora and is not exercised here.
What is tested is everything that can go quietly wrong without a corpus:
the log-odds statistic, the generated page's contract with its projection,
and the capture-file rules the gate enforces.
"""
import json
import os
import re
import tempfile
import unittest
from collections import Counter
from importlib.machinery import SourceFileLoader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wl = SourceFileLoader("wiki_lexicon", os.path.join(ROOT, "bin", "wiki-lexicon")).load_module()


class LogOdds(unittest.TestCase):
    def test_a_word_only_one_side_uses_scores_positive(self):
        """Filler is padded to equal mass on both sides so the shared word is
        genuinely shared. Without that padding a two-word corpus makes every
        proportion move when either count does, and the test measures the
        fixture rather than the statistic."""
        a = Counter({"summons": 300, "the": 5000, "filler": 94700})
        b = Counter({"summons": 1, "the": 5000, "filler": 94999})
        rows = dict((w, z) for z, w, _, _ in wl.logodds(a, b, 1))
        self.assertGreater(rows["summons"], 0)
        self.assertGreater(rows["summons"], rows["the"])

    def test_min_count_excludes_rare_terms(self):
        a = Counter({"rare": 3, "common": 500})
        b = Counter({"common": 500})
        terms = [w for _, w, _, _ in wl.logodds(a, b, 10)]
        self.assertNotIn("rare", terms)
        self.assertIn("common", terms)

    def test_prior_keeps_a_tiny_count_from_outranking_a_large_one(self):
        """The whole reason for the Dirichlet prior. A word used 11 times
        against 0 must not beat one used 3,000 times against 100."""
        a = Counter({"tiny": 11, "big": 3000, "filler": 90000})
        b = Counter({"tiny": 0, "big": 100, "filler": 90000})
        z = dict((w, s) for s, w, _, _ in wl.logodds(a, b, 5))
        self.assertGreater(z["big"], z["tiny"])

    def test_symmetric_input_scores_near_zero(self):
        a = Counter({"x": 400, "y": 400})
        b = Counter({"x": 400, "y": 400})
        for z, _, _, _ in wl.logodds(a, b, 1):
            self.assertLess(abs(z), 0.5)


class Ngrams(unittest.TestCase):
    def test_unigrams_bigrams_trigrams(self):
        t = ["can", "you", "stop", "by"]
        self.assertEqual([" ".join(g) for g in wl.ngrams(t, 1)],
                         ["can", "you", "stop", "by"])
        self.assertEqual([" ".join(g) for g in wl.ngrams(t, 2)],
                         ["can you", "you stop", "stop by"])
        self.assertEqual([" ".join(g) for g in wl.ngrams(t, 3)],
                         ["can you stop", "you stop by"])


class Tokenizer(unittest.TestCase):
    def test_keeps_contractions_and_hyphens_whole(self):
        self.assertEqual(wl.TOKEN.findall("i can't stop by, taboo-mining"),
                         ["i", "can't", "stop", "by", "taboo-mining"])

    def test_drops_bare_numbers_and_punctuation(self):
        self.assertEqual(wl.TOKEN.findall("18:30 -- 2019!"), [])


class GeneratedPage(unittest.TestCase):
    """The page is generated, so the only way it can be wrong is by drifting
    from its projection or by being hand-edited. Both are what `check` is for,
    and both are pinned here."""

    def setUp(self):
        self.d = json.load(open(os.path.join(ROOT, "lexicon", "measured.json")))

    def test_render_is_deterministic(self):
        self.assertEqual(wl.render_page(self.d), wl.render_page(self.d))

    def test_render_matches_the_committed_page(self):
        live = open(os.path.join(ROOT, wl.PAGE), encoding="utf-8").read()
        self.assertEqual(live, wl.render_page(self.d),
                         "wiki/interests/language/measured-vocabulary.md has drifted "
                         "from lexicon/measured.json — run `bin/wiki-lexicon page`")

    def test_carries_the_generated_marker(self):
        self.assertIn(wl.GENERATED, wl.render_page(self.d))

    def test_states_its_denominators(self):
        """A rate with no denominator is the failure bin/intake exists to
        prevent; this page must never print one."""
        page = wl.render_page(self.d)
        self.assertIn(f"{self.d['meta']['sent_tokens']:,}", page)
        self.assertIn(f"{self.d['meta']['received_tokens']:,}", page)
        self.assertIn(f"{self.d['meta']['ai_prompt_tokens']:,}", page)

    def test_chart_block_is_a_list_of_named_series(self):
        page = wl.render_page(self.d)
        self.assertIn("chart:", page)
        self.assertIn("  series:", page)
        for _, label in wl.CHART_SERIES:
            self.assertIn(f'- name: "{label}"', page)

    def test_no_year_below_the_floor_is_charted(self):
        for year, block in self.d["years"].items():
            self.assertGreaterEqual(block["tokens"], wl.MIN_YEAR_TOKENS,
                                    f"{year} is under the floor and should not be in years")

    def test_gemini_word_ranking_is_not_published(self):
        """His Gemini prompts carry pasted documents, so a frequency ranking
        over them returns `div`, `class`, `null`. Exact-term counts are immune;
        a ranking is not, and the projection must not carry one."""
        self.assertNotIn("register_gemini", self.d)


class Captures(unittest.TestCase):
    def test_check_rejects_analyzed_with_scaffold_reading(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "2026-01-01_000000_x.md")
            open(path, "w").write(
                '---\nid: x\nadded: 2026-01-01T00:00:00Z\nword: "x"\nkind: word\n'
                "status: analyzed\nanalyzed: 2026-01-02\ntargets: []\n---\n\n"
                "## Note\n\nn\n\n## Reading\n\n_Not yet analysed._\n")
            old = wl.WORDS
            try:
                wl.WORDS = tmp
                rows = wl.captures()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0]["fm"]["status"], "analyzed")
                self.assertIn("_Not yet analysed._", rows[0]["text"])
            finally:
                wl.WORDS = old

    def test_every_committed_capture_parses_and_is_well_formed(self):
        for c in wl.captures():
            self.assertTrue(c["fm"].get("word"), f"{c['path']} has no word:")
            self.assertIn(c["fm"].get("status", "pending"),
                          ("pending", "analyzed", "declined"), c["path"])
            if c["fm"].get("status") == "analyzed":
                self.assertTrue(c["fm"].get("analyzed"), c["path"])
                self.assertNotIn("_Not yet analysed._", c["text"], c["path"])


class ClusterCounts(unittest.TestCase):
    def test_every_cluster_term_has_all_three_voices(self):
        d = json.load(open(os.path.join(ROOT, "lexicon", "measured.json")))
        for term, row in d["cluster"].items():
            for voice in ("texting", "chatgpt_prompts", "gemini_prompts"):
                self.assertIn(voice, row, f"{term} missing {voice}")
                self.assertIsInstance(row[voice], int)

    def test_cluster_char_denominators_are_present(self):
        d = json.load(open(os.path.join(ROOT, "lexicon", "measured.json")))
        for voice in ("texting", "chatgpt_prompts", "gemini_prompts"):
            self.assertGreater(d["cluster_chars"][voice], 0)


class GeminiPromptSplit(unittest.TestCase):
    def test_the_boundary_pattern_takes_the_prompt_and_not_the_reply(self):
        """The one regex the by-voice counts depend on. If it ever matches past
        the date, every Gemini figure in the corpus silently becomes a
        both-voices count again — which is the exact error the personal-lexicon
        page carries a correction for."""
        cell = ('<div class="content-cell mdl-cell">Prompted\xa0what is a cognitive '
                'prosthetic<br>Jan 2, 2026, 11:00:17 PM EST<br><p>A cognitive '
                'prosthetic is a cognitive prosthetic, said the model.</p></div>')
        got = re.findall(wl.GEMINI_PROMPT, cell, re.S)
        self.assertEqual(len(got), 1)
        self.assertIn("what is a cognitive prosthetic", got[0])
        self.assertNotIn("said the model", got[0])


if __name__ == "__main__":
    unittest.main()
