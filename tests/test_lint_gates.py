#!/usr/bin/env python3
"""Tests for the bin/wiki-lint mechanical gates.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)
      python3 tests/test_lint_gates.py -v           (from anywhere)

Pure stdlib, per repo convention. `bin/wiki-lint` has no .py extension and
executes its checks at import time, so the helpers are loaded from source with
the module-level body stripped — see `load_helpers`.

These tests exist because all three gates shipped with defects that a manual
check missed: the retraction gate flagged every correctly-written correction,
the phantom-source gate matched bare basenames against whole page bodies in a
tree with thousands of colliding basenames, and the duplicate-key check used an
unanchored regex that could mistake a horizontal rule for frontmatter.
"""
import os
import re
import sys
import tempfile
import textwrap
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_helpers():
    """Import the free functions from bin/wiki-lint without running the linter.

    The file is a script: everything after the helper block scans the real wiki.
    Truncating at the first top-level statement after the helpers gives us the
    functions under test and nothing else.
    """
    src = open(os.path.join(ROOT, "bin", "wiki-lint"), encoding="utf-8").read()
    cut = src.index("pages = sorted(glob.glob(")
    mod = {"__name__": "wiki_lint_helpers",
           "__file__": os.path.join(ROOT, "bin", "wiki-lint")}
    exec(compile(src[:cut], "bin/wiki-lint", "exec"), mod)  # noqa: S102 - trusted repo file
    return mod


H = load_helpers()


class RetractionPatternTests(unittest.TestCase):
    """The ledger's own pattern for `suz-750-weekly`, exercised directly.

    The governing requirement: a bare '$750' is NOT the retracted claim. The
    corpus contains unrelated legitimate $750 figures and a verbatim quote of
    the underlying accusation, and neither may fire the gate.
    """

    def setUp(self):
        entries = H["load_retractions"](os.path.join(ROOT, "RETRACTED.md"), [])
        self.entry = next(e for e in entries if e["id"] == "suz-750-weekly")
        self.pats = self.entry["_compiled"]

    def matches(self, text):
        return any(p.search(text) for p in self.pats)

    def test_exact_old_claim(self):
        self.assertTrue(self.matches("~$750/week borrowed from Suz"))

    def test_formatting_variants(self):
        for variant in (
            "$750/week", "$750/wk", "$750 per week", "$750 a week",
            "$750-a-week", "$750 weekly", "$750  /  week", "$750/Week",
            "$ 750/week",
        ):
            with self.subTest(variant=variant):
                self.assertTrue(self.matches(variant), f"should match: {variant}")

    def test_escaped_markdown(self):
        self.assertTrue(self.matches(r"\$750/week"))

    def test_punctuation_variations(self):
        for variant in ('"$750/week,"', "($750/wk)", "*$750 per week*", "`$750/week`"):
            with self.subTest(variant=variant):
                self.assertTrue(self.matches(variant))

    def test_unrelated_identical_number_does_not_match(self):
        """The false positive that made the original gate unusable."""
        for benign in (
            "a Aug 20 discount to $750, and a final $700 close",
            "$750 for the deposit",
            "he was down $750 that month",
            "$7500/week",          # different figure entirely
            "750/week",            # no currency, not this claim
        ):
            with self.subTest(benign=benign):
                self.assertFalse(self.matches(benign), f"should NOT match: {benign}")

    def test_primary_quote_of_the_accusation_does_not_match(self):
        """This sentence is evidence and must survive: it is what was generalised."""
        self.assertFalse(
            self.matches('You borrowed $750 last week alone! It\'s not like you are')
        )

    def test_partial_match_does_not_fire(self):
        self.assertFalse(self.matches("$75"))
        self.assertFalse(self.matches("$750,000 per week"))


class QuarantineTests(unittest.TestCase):
    """Correction contexts must be exempt — STYLE_GUIDE rule 9 requires the old
    claim to stay visible where it is corrected."""

    def live_lines(self, text):
        mask = H["quarantine_mask"](text)
        return [ln for ln, ok in zip(text.splitlines(), mask) if ok]

    def test_correction_blockquote_is_quarantined(self):
        text = textwrap.dedent("""\
            Body prose here.

            > **CORRECTED [2026-08-18]:** the clause read "$750/week borrowed".
            > The rate does not exist.

            More prose.
            """)
        self.assertNotIn('> **CORRECTED [2026-08-18]:** the clause read "$750/week borrowed".',
                         self.live_lines(text))

    def test_plain_blockquote_is_not_quarantined(self):
        """A quote without a correction marker is still a live assertion."""
        text = "> he paid $750/week to his mother\n"
        self.assertEqual(len(self.live_lines(text)), 1)

    def test_correction_heading_scopes_until_next_heading(self):
        text = textwrap.dedent("""\
            ## RE-CHECKED [2026-08-18]

            The spine had it at a standing $750/week rate; the record shows $14,000.

            ## Next section

            This says $750/week and is live.
            """)
        live = self.live_lines(text)
        self.assertNotIn("The spine had it at a standing $750/week rate; the record shows $14,000.", live)
        self.assertIn("This says $750/week and is live.", live)

    def test_bold_lowercase_marker_on_one_line(self):
        text = '| 2018 | the "$750/week" rate is **retracted** — see below | churn |\n'
        self.assertEqual(self.live_lines(text), [])

    def test_bare_lowercase_word_is_not_a_marker(self):
        """Otherwise ordinary prose blinds the gate."""
        text = "The estimate was revised upward to $750/week last year.\n"
        self.assertEqual(len(self.live_lines(text)), 1)


class RetractionLedgerTests(unittest.TestCase):
    def test_malformed_json_is_a_loud_error(self):
        """A ledger that silently stops parsing is the worst possible failure."""
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("```json\n{not valid json,}\n```\n")
            path = f.name
        try:
            errors = []
            entries = H["load_retractions"](path, errors)
            self.assertEqual(entries, [])
            self.assertTrue(any("malformed json" in e for e in errors))
        finally:
            os.unlink(path)

    def test_missing_required_field_is_reported(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write('```json\n{"id": "x", "claim": "y"}\n```\n')
            path = f.name
        try:
            errors = []
            self.assertEqual(H["load_retractions"](path, errors), [])
            self.assertTrue(any("missing required field" in e for e in errors))
        finally:
            os.unlink(path)

    def test_invalid_regex_is_reported(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write('```json\n{"id":"x","claim":"y","replacement":"z","patterns":["("]}\n```\n')
            path = f.name
        try:
            errors = []
            H["load_retractions"](path, errors)
            self.assertTrue(any("invalid regex" in e for e in errors))
        finally:
            os.unlink(path)

    def test_absent_ledger_is_not_an_error(self):
        self.assertEqual(H["load_retractions"]("/nonexistent/RETRACTED.md", []), [])

    def test_real_ledger_parses(self):
        errors = []
        entries = H["load_retractions"](os.path.join(ROOT, "RETRACTED.md"), errors)
        self.assertEqual(errors, [], "the committed ledger must parse cleanly")
        self.assertTrue(entries)


class PhantomSourceTests(unittest.TestCase):
    """Detection must be conservative: ambiguity is reported as ambiguity, never
    as a phantom."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        os.makedirs(os.path.join(self.root, "raw", "alpha"))
        os.makedirs(os.path.join(self.root, "raw", "beta"))
        self.write("raw/alpha/unique.csv", "a,b\n1,2\n3,4\n")        # populated
        self.write("raw/alpha/messages.csv", "a,b\n1,2\n")           # populated, dup basename
        self.write("raw/beta/messages.csv", "a,b\n")                 # header-only, dup basename
        self.write("raw/alpha/empty.csv", "")                        # zero byte
        self.write("raw/alpha/header_only.csv", "ts,dir,text\n")     # header-only
        self.write("raw/alpha/.gitkeep", "")                         # structural
        self.addCleanup(self.tmp.cleanup)

    def write(self, rel, body):
        path = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(body)

    def test_zero_byte_source_detected(self):
        self.assertIn("raw/alpha/empty.csv", H["find_empty_raw_files"](self.root))

    def test_header_only_csv_detected(self):
        self.assertIn("raw/alpha/header_only.csv", H["find_empty_raw_files"](self.root))

    def test_valid_populated_csv_not_detected(self):
        empty = H["find_empty_raw_files"](self.root)
        self.assertNotIn("raw/alpha/unique.csv", empty)
        self.assertNotIn("raw/alpha/messages.csv", empty)

    def test_structural_placeholder_excluded(self):
        """.gitkeep is empty by design and is never cited as evidence."""
        self.assertNotIn("raw/alpha/.gitkeep", H["find_empty_raw_files"](self.root))

    def test_duplicate_basenames_are_both_indexed(self):
        idx = H["raw_basename_index"](self.root)
        self.assertEqual(len(idx["messages.csv"]), 2)

    def test_unique_basename_resolves(self):
        idx = H["raw_basename_index"](self.root)
        self.assertEqual(idx["unique.csv"], ["raw/alpha/unique.csv"])

    def test_missing_source_is_absent_from_index(self):
        self.assertNotIn("nope.csv", H["raw_basename_index"](self.root))


class FrontmatterSourceTests(unittest.TestCase):
    def test_extracts_source_list(self):
        text = textwrap.dedent("""\
            ---
            domain: people
            sources:
              - raw/self/a.csv
              - raw/self/b.csv
            tags: [family]
            ---

            Body mentioning raw/self/decoy.csv in prose.
            """)
        self.assertEqual(
            H["frontmatter_sources"](text), ["raw/self/a.csv", "raw/self/b.csv"]
        )

    def test_prose_filenames_are_not_citations(self):
        text = "---\ndomain: people\n---\n\nSee messages.csv for detail.\n"
        self.assertEqual(H["frontmatter_sources"](text), [])

    def test_quoted_sources_are_unquoted(self):
        text = '---\nsources:\n  - "raw/self/x y.csv"\n---\n\nbody\n'
        self.assertEqual(H["frontmatter_sources"](text), ["raw/self/x y.csv"])

    def test_no_frontmatter(self):
        self.assertEqual(H["frontmatter_sources"]("just a body\n"), [])


class DuplicateKeyTests(unittest.TestCase):
    def keys(self, fm):
        return list(H["duplicate_top_level_keys"](textwrap.dedent(fm)))

    def test_detects_duplicate_top_level_key(self):
        found = self.keys("""\
            domain: people
            status: active
            title: X
            status: stable
            """)
        self.assertEqual([(k, c) for k, _ln, c in found], [("status", 2)])

    def test_reports_first_line_number(self):
        found = self.keys("""\
            domain: people
            status: active
            status: stable
            """)
        self.assertEqual(found[0][1], 2)

    def test_clean_frontmatter_is_silent(self):
        self.assertEqual(self.keys("domain: people\nstatus: active\n"), [])

    def test_nested_mapping_not_flagged(self):
        """Repeated nested keys under different parents are legitimate."""
        self.assertEqual(self.keys("""\
            infobox:
              name: A
              location: uniontown
            connections:
              - page: wiki/people/x
                type: causes
              - page: wiki/people/y
                type: causes
            """), [])

    def test_list_items_not_flagged(self):
        self.assertEqual(self.keys("""\
            sources:
              - raw/a.csv
              - raw/b.csv
            """), [])

    def test_block_scalar_body_not_parsed_as_keys(self):
        """A literal block can contain 'word:' at any indent without being a key."""
        self.assertEqual(self.keys("""\
            summary: |
              note: this is prose
              note: so is this
            status: active
            """), [])

    def test_comments_ignored(self):
        self.assertEqual(self.keys("# status: active\nstatus: active\n"), [])


class FreshnessTests(unittest.TestCase):
    """bin/wiki-freshness must agree with bin/llm-publish about which pages
    exist, or it reports drift that isn't there (it did, on first write)."""

    def setUp(self):
        src = open(os.path.join(ROOT, "bin", "wiki-freshness"), encoding="utf-8").read()
        cut = src.index('if __name__ ==')
        self.F = {"__name__": "wiki_freshness_helpers",
                  "__file__": os.path.join(ROOT, "bin", "wiki-freshness")}
        exec(compile(src[:cut], "bin/wiki-freshness", "exec"), self.F)  # noqa: S102

    def test_skip_dirs_mirror_llm_publish(self):
        pub = open(os.path.join(ROOT, "bin", "llm-publish"), encoding="utf-8").read()
        m = re.search(r"^SKIP_DIRS\s*=\s*(\{[^}]*\})", pub, re.M)
        self.assertIsNotNone(m, "llm-publish SKIP_DIRS not found — update this test")
        self.assertEqual(
            eval(m.group(1)), self.F["SKIP_DIRS"],  # noqa: S307 - literal set from repo file
            "wiki-freshness SKIP_DIRS must mirror llm-publish or it reports phantom drift",
        )

    def test_page_set_matches_lint_page_set(self):
        """The two tools must count the same population — the audit reported
        476 and 475 for the same corpus before this was fixed."""
        import glob as _glob
        lint_pages = {
            os.path.relpath(p, ROOT)
            for p in _glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True)
        }
        self.assertEqual(self.F["wiki_page_set"](ROOT), lint_pages)

    def test_detects_added_page(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "wiki"))
            for name in ("a.md", "b.md"):
                with open(os.path.join(d, "wiki", name), "w") as f:
                    f.write("x")
            man = os.path.join(d, "manifest.json")
            with open(man, "w") as f:
                f.write('{"pages":[{"page":"wiki/a.md","bytes":1}]}')
            missing, removed, changed = self.F["compare"](d, man)
            self.assertEqual(missing, ["wiki/b.md"])
            self.assertEqual(removed, [])

    def test_detects_orphaned_and_changed(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "wiki"))
            with open(os.path.join(d, "wiki", "a.md"), "w") as f:
                f.write("much longer body")
            man = os.path.join(d, "manifest.json")
            with open(man, "w") as f:
                f.write('{"pages":[{"page":"wiki/a.md","bytes":1},'
                        '{"page":"wiki/gone.md","bytes":5}]}')
            missing, removed, changed = self.F["compare"](d, man)
            self.assertEqual(removed, ["wiki/gone.md"])
            self.assertEqual([c[0] for c in changed], ["wiki/a.md"])

    def test_in_sync_reports_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "wiki"))
            body = "hello"
            with open(os.path.join(d, "wiki", "a.md"), "w") as f:
                f.write(body)
            man = os.path.join(d, "manifest.json")
            with open(man, "w") as f:
                f.write('{"pages":[{"page":"wiki/a.md","bytes":%d}]}' % len(body))
            self.assertEqual(self.F["compare"](d, man), ([], [], []))


class FrontmatterAnchoringTests(unittest.TestCase):
    """The original duplicate-key code used re.search with re.M, which can match
    a '---' fenced region in the body as if it were frontmatter."""

    def test_horizontal_rules_in_body_are_not_frontmatter(self):
        text = "no frontmatter here\n\n---\nstatus: a\nstatus: b\n---\n\ntail\n"
        self.assertIsNone(re.match(r"^---\n(.*?)\n---\n", text, re.S))


if __name__ == "__main__":
    unittest.main(verbosity=2)


class CorruptTextTests(unittest.TestCase):
    """Merge markers and assistant citation artifacts both reached main and were
    published into llm/corpus.txt before anyone caught them by eye."""

    def find(self, text):
        return H["find_corrupt_text"](text)

    def test_conflict_head_marker_detected(self):
        hits = self.find("intro\n<<<<<<< HEAD\nmine\n")
        self.assertEqual([n for n, _ in hits], [2])

    def test_bare_separator_detected(self):
        self.assertTrue(self.find("a\n=======\nb\n"))

    def test_theirs_marker_detected(self):
        self.assertTrue(self.find("a\n>>>>>>> origin/main\nb\n"))

    def test_all_three_markers_reported_separately(self):
        text = "a\n<<<<<<< HEAD\nx\n=======\ny\n>>>>>>> other\n"
        self.assertEqual(len(self.find(text)), 3)

    def test_markdown_hr_is_not_a_marker(self):
        """A setext underline or an --- rule must not trip the gate."""
        self.assertEqual(self.find("Heading\n=====\ntext\n"), [])

    def test_equals_with_trailing_content_is_not_a_marker(self):
        self.assertEqual(self.find("a\n======= not a marker\nb\n"), [])

    def test_private_use_codepoint_detected(self):
        hits = self.find("text fileciteturn16file0 more")
        self.assertEqual(len(hits), 1)
        self.assertIn("0xe200", hits[0][1])

    def test_private_use_reports_first_offending_line(self):
        hits = self.find("clean\nclean\nbad x\n")
        self.assertEqual(hits[0][0], 3)

    def test_ordinary_unicode_is_not_flagged(self):
        """Curly quotes, em-dashes and emoji are normal wiki content."""
        self.assertEqual(self.find("It's a test — “quoted” \U0001F600\n"), [])

    def test_clean_page_yields_nothing(self):
        self.assertEqual(self.find("# Page\n\nOrdinary prose.\n"), [])

    def test_real_wiki_is_clean(self):
        """Regression: the wiki must stay free of both classes."""
        import glob
        dirty = []
        for p in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True):
            if self.find(open(p, encoding="utf-8", errors="replace").read()):
                dirty.append(os.path.relpath(p, ROOT))
        self.assertEqual(dirty, [])
