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


class DatasetChartTests(unittest.TestCase):
    """page_type: dataset requires a well-formed chart: block (STYLE_GUIDE.md)."""

    def errs(self, fm):
        return H["validate_dataset_chart"](textwrap.dedent(fm))

    def test_well_formed_chart_passes(self):
        self.assertEqual(self.errs("""\
            chart:
              kind: line
              title: "Messages per year"
              x: { label: "Year", type: category }
              y: { label: "Messages", type: number }
              series:
                - name: "Dan's messages"
                  points:
                    "2015": 281
                    "2016": 2453
            """), [])

    def test_missing_chart_block_is_an_error(self):
        errs = self.errs("domain: mind\npage_type: dataset\n")
        self.assertEqual(len(errs), 1)
        self.assertIn("requires a chart:", errs[0])

    def test_missing_kind_is_an_error(self):
        errs = self.errs("""\
            chart:
              title: "X"
              series:
                - name: "A"
                  points:
                    "2020": 1
            """)
        self.assertTrue(any("missing required 'kind'" in e for e in errs))

    def test_invalid_kind_is_an_error(self):
        errs = self.errs("""\
            chart:
              kind: pie
              title: "X"
              series:
                - name: "A"
                  points:
                    "2020": 1
            """)
        self.assertTrue(any("chart.kind 'pie' invalid" in e for e in errs))

    def test_missing_title_is_an_error(self):
        errs = self.errs("""\
            chart:
              kind: bar
              series:
                - name: "A"
                  points:
                    "2020": 1
            """)
        self.assertTrue(any("missing required 'title'" in e for e in errs))

    def test_empty_series_is_an_error(self):
        errs = self.errs("""\
            chart:
              kind: line
              title: "X"
              series: []
            """)
        self.assertTrue(any("at least one named series" in e for e in errs))

    def test_series_with_no_points_is_an_error(self):
        errs = self.errs("""\
            chart:
              kind: line
              title: "X"
              series:
                - name: "A"
            """)
        self.assertTrue(any("no non-empty points" in e for e in errs))

    def test_multiple_series_all_populated_passes(self):
        self.assertEqual(self.errs("""\
            chart:
              kind: line
              title: "X"
              series:
                - name: "A"
                  points:
                    "2020": 1
                - name: "B"
                  points:
                    "2020": 2
            """), [])


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


class WikilinkParsingTests(unittest.TestCase):
    """Thirteen correctly-authored links were reported broken: seven for the
    '\\|' pipe-escape that markdown tables require, and three for discussing
    wikilink syntax inside code spans."""

    LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")

    def targets(self, text):
        body = H["strip_code"](text)
        return [t.strip().rstrip("\\").strip().rstrip("/")
                for t in self.LINK_RE.findall(body)]

    def test_plain_link_parses(self):
        self.assertEqual(self.targets("see [[wiki/people/tom]]"), ["wiki/people/tom"])

    def test_piped_link_parses(self):
        self.assertEqual(self.targets("[[wiki/people/tom|Tom]]"), ["wiki/people/tom"])

    def test_table_pipe_escape_parses(self):
        """The regression: '\\|' is mandatory inside a table cell."""
        row = "| [[wiki/people/vanessa-frank\\|Vanessa]] | retyped |"
        self.assertEqual(self.targets(row), ["wiki/people/vanessa-frank"])

    def test_several_escaped_links_in_one_row(self):
        row = "| [[wiki/people/a\\|A]] | [[wiki/people/b\\|B]] |"
        self.assertEqual(self.targets(row), ["wiki/people/a", "wiki/people/b"])

    def test_anchor_link_parses(self):
        self.assertEqual(self.targets("[[wiki/people/tom#money]]"), ["wiki/people/tom"])

    def test_trailing_slash_stripped(self):
        self.assertEqual(self.targets("[[wiki/people/tom/]]"), ["wiki/people/tom"])

    def test_inline_code_link_ignored(self):
        self.assertEqual(self.targets("adds `[[wiki/...]]` links"), [])

    def test_fenced_block_link_ignored(self):
        self.assertEqual(self.targets("```\n[[wiki/people/example]]\n```\n"), [])

    def test_real_link_beside_code_example_still_found(self):
        text = "use `[[wiki/…]]` to reach [[wiki/people/tom]]"
        self.assertEqual(self.targets(text), ["wiki/people/tom"])

    def test_strip_code_preserves_line_count(self):
        """Offsets must survive so other checks keep reporting real line numbers."""
        text = "a\n```\nb\nc\n```\nd\n"
        self.assertEqual(H["strip_code"](text).count("\n"), text.count("\n"))

    def test_real_wiki_has_no_broken_links(self):
        """Regression: every wikilink in the wiki must resolve."""
        import glob
        keys = {os.path.relpath(p, ROOT)[:-3]
                for p in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True)}
        broken = []
        for p in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True):
            text = open(p, encoding="utf-8", errors="replace").read()
            body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
            for t in self.targets(body):
                if not t.startswith("wiki/"):
                    continue
                t = t[:-3] if t.endswith(".md") else t   # links may carry .md
                if t in keys or os.path.basename(t) in {os.path.basename(k) for k in keys}:
                    continue
                if os.path.isdir(os.path.join(ROOT, t)):
                    continue
                broken.append((os.path.relpath(p, ROOT), t))
        self.assertEqual(broken, [])


class IndexDriftTests(unittest.TestCase):
    """All nine domain counts in index.md were stale on 2026-08-20 — people
    advertised 150 against an actual 164."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        self.addCleanup(self.tmp.cleanup)

    def build(self, claimed, n_pages, extra=()):
        os.makedirs(os.path.join(self.root, "wiki", "people"), exist_ok=True)
        with open(os.path.join(self.root, "index.md"), "w") as f:
            f.write("| Domain | Covers | Pages | Index |\n|---|---|---|---|\n")
            f.write(f"| people | People | {claimed} | [[wiki/people/index]] |\n")
        for i in range(n_pages):
            with open(os.path.join(self.root, "wiki", "people", f"p{i}.md"), "w") as f:
                f.write("# p\n")
        with open(os.path.join(self.root, "wiki", "people", "index.md"), "w") as f:
            f.write("# index\n")
        for rel in extra:
            path = os.path.join(self.root, rel)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write("# x\n")

    def test_matching_count_is_clean(self):
        self.build(claimed=3, n_pages=3)
        self.assertEqual(H["index_count_drift"](self.root), [])

    def test_stale_count_detected(self):
        self.build(claimed=2, n_pages=5)
        self.assertEqual(H["index_count_drift"](self.root), [("people", 2, 5)])

    def test_domain_index_not_counted(self):
        """index.md itself is navigation, not a page."""
        self.build(claimed=3, n_pages=3)
        self.assertEqual(H["index_count_drift"](self.root), [])

    def test_archived_pages_excluded(self):
        """archive/ holds pinned artifacts, exempt from budgets and counts."""
        self.build(claimed=3, n_pages=3,
                   extra=["wiki/people/archive/old.md"])
        self.assertEqual(H["index_count_drift"](self.root), [])

    def test_missing_index_is_not_an_error(self):
        self.assertEqual(H["index_count_drift"](self.root), [])

    def test_real_index_is_current(self):
        """Regression: the wiki's front door must not misreport its size."""
        self.assertEqual(H["index_count_drift"](ROOT), [])


class MalformedFrontmatterBlockTests(unittest.TestCase):
    """A connections: block that loses its indent still looks fine but is
    invisible to wiki-connect, so the page silently carries no edges and every
    gate stays green. A whitespace-collapsing cleanup destroyed four edges that
    way on 2026-08-20 without tripping anything."""

    def find(self, text):
        return H["malformed_frontmatter_blocks"](text)

    WELL_FORMED = (
        "connections:\n"
        "  - page: wiki/people/tom\n"
        "    type: evidences\n"
        '    claim: "A claim long enough to be real."\n'
    )

    def test_well_formed_block_is_clean(self):
        self.assertEqual(self.find(self.WELL_FORMED), [])

    def test_unindented_list_item_detected(self):
        bad = self.WELL_FORMED.replace("  - page:", "- page:")
        self.assertEqual([r[1] for r in self.find(bad)], ["list item not indented"])

    def test_under_indented_field_detected(self):
        bad = self.WELL_FORMED.replace("    type:", " type:")
        self.assertIn("field under-indented", [r[1] for r in self.find(bad)])

    def test_sources_block_checked_too(self):
        bad = "sources:\n- raw/a.txt\n"
        self.assertEqual([r[0] for r in self.find(bad)], ["sources"])

    def test_synthesizes_block_checked_too(self):
        bad = "synthesizes:\n- wiki/people/tom\n"
        self.assertEqual([r[0] for r in self.find(bad)], ["synthesizes"])

    def test_block_ends_at_next_key(self):
        """A following top-level key must not be scanned as part of the block."""
        text = self.WELL_FORMED + "tags: [a, b]\n- not part of the block\n"
        self.assertEqual(self.find(text), [])

    def test_block_ends_at_frontmatter_close(self):
        text = self.WELL_FORMED + "---\n\n- an ordinary bullet in the body\n"
        self.assertEqual(self.find(text), [])

    def test_absent_blocks_are_clean(self):
        self.assertEqual(self.find("domain: people\ntags: [a]\n"), [])

    def test_real_wiki_is_clean(self):
        """Regression: every declared edge must actually be readable."""
        import glob
        dirty = []
        for p in glob.glob(os.path.join(ROOT, "wiki", "**", "*.md"), recursive=True):
            if self.find(open(p, encoding="utf-8", errors="replace").read()):
                dirty.append(os.path.relpath(p, ROOT))
        self.assertEqual(dirty, [])


def load_timeline_helpers():
    """Import bin/wiki-timeline's free functions without generating anything.

    Same trick as load_helpers(): the file is a script, so it is truncated at
    the first top-level statement that walks the wiki.
    """
    src = open(os.path.join(ROOT, "bin", "wiki-timeline"), encoding="utf-8").read()
    cut = src.index("def collect(")
    mod = {"__name__": "wiki_timeline_helpers",
           "__file__": os.path.join(ROOT, "bin", "wiki-timeline")}
    exec(compile(src[:cut], "bin/wiki-timeline", "exec"), mod)  # noqa: S102 - trusted repo file
    return mod


TL = load_timeline_helpers()


class TimelineRetractionFilterTests(unittest.TestCase):
    """The generated timeline must not resurrect a retracted claim.

    master-timeline.md copies sentences verbatim out of every page in the wiki.
    That copy lands outside the correction blockquote — and outside the
    `documented_on` exemption — that made the original legal, so a claim which
    is correctly quarantined on its source page becomes a live assertion in the
    generated file. This happened for real: wiki/self/concepts/claude.md
    narrates the suz-750-weekly retraction in ordinary prose under its
    `documented_on` exemption, and a regeneration lifted that sentence into the
    timeline, where bin/wiki-lint failed the build.
    """

    def test_ledger_patterns_are_loaded(self):
        self.assertTrue(TL["RETRACTED_PATTERNS"],
                        "generator loaded no retraction patterns — the filter is inert")

    def test_retracted_claim_is_rejected_as_an_event(self):
        text = ('Not "$750/week from her to him" but ~$14,000 from Dan to her '
                'in Aug-Oct 2018, drawn against an estate.')
        why = TL["reject_reason"](text, 1, "prose")
        self.assertIsNotNone(why, "retracted claim accepted as a timeline event")
        self.assertIn("retracted claim", why)

    def test_menore_transaction_language_is_rejected(self):
        text = ('Operational Security: deliberately sparse communication; no '
                'product names. "Need 8" is the entire transaction language.')
        why = TL["reject_reason"](text, 1, "prose")
        self.assertIsNotNone(why)
        self.assertIn("retracted claim", why)

    def test_ordinary_event_still_passes(self):
        text = "Dan moved to 46 Nevins St, Brooklyn on February 12, 2019."
        self.assertIsNone(TL["reject_reason"](text, 3, "prose"))

    def test_unrelated_dollar_figure_still_passes(self):
        """The filter inherits the ledger's precision — a bare $750 is not the claim."""
        text = "David Beard was owed $750 for the work he finished that August."
        self.assertIsNone(TL["reject_reason"](text, 1, "prose"))

    def test_generated_timeline_is_clean(self):
        """Regression: the committed timeline holds no retracted claim."""
        path = os.path.join(ROOT, "wiki", "timeline", "master-timeline.md")
        text = open(path, encoding="utf-8", errors="replace").read()
        hits = []
        for rid, pat in TL["RETRACTED_PATTERNS"]:
            for line in text.splitlines():
                if line.startswith(">"):
                    continue
                if pat.search(line):
                    hits.append((rid, line[:90]))
        self.assertEqual(hits, [])
