#!/usr/bin/env python3
"""Tests for bin/wiki-plain, the READER'S DIGEST layer.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

Two properties are pinned here and neither is cosmetic.

  * **The moratorium guard.** `CLAUDE.md` carries a standing operator directive
    about a living person, and this tool is where it stops being something a
    session has to remember. It shipped with a real hole: the pattern was
    `\\bannie\\b`, which looks tighter than the one in the tool today and is
    wrong — `_` is a word character, so the trailing boundary fails against
    `annie_metadata_24h.csv`, the filename that material is cited by throughout.
    `read-receipt-forensics` carries that filename twice and read as ELIGIBLE
    FOR TRANSLATION until it was caught by hand. A guard whose failure mode is
    silent permission gets a test.

  * **Staleness.** A twin records the version of the page it was written
    against. When the page moves past it, the twin is a confident, readable,
    wrong account of what the wiki now says, aimed at the reader least equipped
    to catch it — so it has to fail the gate rather than merely look old.

The real corpus is never touched: every case builds a two-file tree in a temp
directory and points the module's roots at it.
"""
import importlib.util
import os
import re
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "bin", "wiki-plain")


def load_module():
    """bin/wiki-plain has no .py extension, and no import-time side effects."""
    spec = importlib.util.spec_from_loader(
        "wiki_plain", importlib.machinery.SourceFileLoader("wiki_plain", SCRIPT)
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


wp = load_module()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


PAGE = """---
title: "A Page"
page_type: synthesis
date_modified: {modified}
---

# A Page

{body}
"""

TWIN = """---
plain_of: wiki/{slug}
title: "A Page"
source_modified: {against}
---

# A Page

{body}
"""


class Tree:
    """A throwaway wiki/ + plain/ pair with the module pointed at it."""

    def __init__(self):
        self.dir = tempfile.TemporaryDirectory()
        self.root = self.dir.name
        self._saved = (wp.WIKI, wp.PLAIN)
        wp.WIKI = os.path.join(self.root, "wiki")
        wp.PLAIN = os.path.join(self.root, "plain")
        os.makedirs(wp.WIKI)
        os.makedirs(wp.PLAIN)

    def page(self, slug, body="Ordinary prose.", modified="2026-08-28"):
        write(os.path.join(wp.WIKI, f"{slug}.md"), PAGE.format(modified=modified, body=body))

    def twin(self, slug, body="Plain prose.", against="2026-08-28"):
        write(
            os.path.join(wp.PLAIN, f"{slug}.md"),
            TWIN.format(slug=slug, against=against, body=body),
        )

    def close(self):
        wp.WIKI, wp.PLAIN = self._saved
        self.dir.cleanup()


class TreeCase(unittest.TestCase):
    def setUp(self):
        self.t = Tree()
        self.addCleanup(self.t.close)

    def one(self, slug="mind/x"):
        pages = wp.load()
        self.assertEqual([p.slug for p in pages], [slug])
        return pages[0]

    def errors(self):
        """`check`'s findings, without its printing."""
        import io
        import contextlib

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = wp.cmd_check(None)
        return code, buf.getvalue()


class TestMoratoriumPattern(unittest.TestCase):
    """The regex itself, independent of any tree."""

    def test_catches_the_underscored_filename(self):
        # The original bug. `\\bannie\\b` does not match this and it must.
        self.assertTrue(wp.MORATORIUM.search("annie_metadata_24h.csv"))

    def test_catches_the_ordinary_forms(self):
        for text in ("Annie", "annie", "Annie's page", "ANNIE", "annies"):
            with self.subTest(text=text):
                self.assertTrue(wp.MORATORIUM.search(text))

    def test_catches_the_surname(self):
        self.assertTrue(wp.MORATORIUM.search("wiki/people/annie-ulmer"))
        self.assertTrue(wp.MORATORIUM.search("Ulmer"))

    def test_does_not_catch_unrelated_words(self):
        for text in ("granny", "uncanny", "companies", "Vulmer"):
            with self.subTest(text=text):
                self.assertIsNone(wp.MORATORIUM.search(text))


class TestRuleOne(TreeCase):
    """A page substantially about her gets no twin at all."""

    def test_body_mentions_at_the_threshold_stay_eligible(self):
        self.t.page("mind/x", body="Annie once. " * wp.INCIDENTAL)
        self.assertFalse(self.one().excluded)

    def test_body_mentions_past_the_threshold_exclude(self):
        self.t.page("mind/x", body="Annie once. " * (wp.INCIDENTAL + 1))
        self.assertTrue(self.one().excluded)

    def test_frontmatter_excludes_at_any_density(self):
        # One mention, in `sources:` — the page is built on that material
        # however sparingly its body says so.
        write(
            os.path.join(wp.WIKI, "mind/x.md"),
            "---\ntitle: \"A Page\"\ndate_modified: 2026-08-28\n"
            "sources:\n  - raw/self/annie_metadata_24h.csv\n---\n\n# A Page\n\nProse.\n",
        )
        self.assertTrue(self.one().excluded)

    def test_a_clean_page_is_eligible(self):
        self.t.page("mind/x")
        self.assertFalse(self.one().excluded)

    def test_a_twin_on_an_excluded_page_fails_the_gate(self):
        self.t.page("mind/x", body="Annie. " * 10)
        self.t.twin("mind/x")
        code, out = self.errors()
        self.assertEqual(code, 1)
        self.assertIn("moratorium", out)

    def test_new_refuses_an_excluded_page(self):
        self.t.page("mind/x", body="Annie. " * 10)
        args = type("A", (), {"slug": "mind/x"})()
        err = sys.stderr
        sys.stderr = open(os.devnull, "w")
        try:
            self.assertEqual(wp.cmd_new(args), 2)
        finally:
            sys.stderr.close()
            sys.stderr = err
        self.assertFalse(os.path.exists(os.path.join(wp.PLAIN, "mind/x.md")))

    def test_next_never_proposes_an_excluded_page(self):
        self.t.page("mind/x", body="Annie. " * 10)
        todo = [p for p in wp.load() if not p.twin and not p.excluded]
        self.assertEqual(todo, [])


class TestRuleTwo(TreeCase):
    """No file in this layer names her, whatever its source page says."""

    def test_a_twin_naming_her_fails_even_on_a_clean_page(self):
        self.t.page("mind/x")  # source is spotless
        self.t.twin("mind/x", body="Then Annie arrived.")
        code, out = self.errors()
        self.assertEqual(code, 1)
        self.assertIn("moratorium", out)

    def test_a_clean_twin_on_a_clean_page_passes(self):
        self.t.page("mind/x")
        self.t.twin("mind/x")
        self.assertEqual(self.errors()[0], 0)


class TestStaleness(TreeCase):
    def test_matching_dates_are_current(self):
        self.t.page("mind/x", modified="2026-08-28")
        self.t.twin("mind/x", against="2026-08-28")
        self.assertFalse(self.one().stale)
        self.assertEqual(self.errors()[0], 0)

    def test_a_moved_page_makes_the_twin_stale(self):
        self.t.page("mind/x", modified="2026-09-01")
        self.t.twin("mind/x", against="2026-08-28")
        self.assertTrue(self.one().stale)
        code, out = self.errors()
        self.assertEqual(code, 1)
        self.assertIn("STALE", out)

    def test_a_twin_with_no_recorded_source_is_stale(self):
        self.t.page("mind/x", modified="2026-08-28")
        write(
            os.path.join(wp.PLAIN, "mind/x.md"),
            "---\nplain_of: wiki/mind/x\ntitle: \"A Page\"\n---\n\n# A Page\n\nProse.\n",
        )
        self.assertTrue(self.one().stale)

    def test_a_missing_twin_is_not_an_error(self):
        # Coverage is campaign work. Only a BROKEN twin fails the gate.
        self.t.page("mind/x")
        self.assertEqual(self.errors()[0], 0)


class TestOrphansAndPointers(TreeCase):
    def test_a_twin_with_no_page_above_it_fails(self):
        self.t.twin("mind/ghost")
        code, out = self.errors()
        self.assertEqual(code, 1)
        self.assertIn("ORPHAN", out)

    def test_bookkeeping_files_are_not_orphan_twins(self):
        # plain/DECLINED.md records pages considered and declined. It is not a
        # twin of anything and must not read as one.
        self.t.page("mind/x")
        write(os.path.join(wp.PLAIN, "DECLINED.md"), "# Declined\n\nA reason.\n")
        code, out = self.errors()
        self.assertEqual(code, 0, out)
        self.assertNotIn("ORPHAN", out)

    def test_a_real_orphan_still_fails_alongside_bookkeeping(self):
        self.t.page("mind/x")
        write(os.path.join(wp.PLAIN, "DECLINED.md"), "# Declined\n")
        self.t.twin("mind/ghost")
        code, out = self.errors()
        self.assertEqual(code, 1)
        self.assertIn("ORPHAN", out)
        self.assertIn("ghost", out)

    def test_a_mismatched_plain_of_fails(self):
        self.t.page("mind/x")
        write(
            os.path.join(wp.PLAIN, "mind/x.md"),
            "---\nplain_of: wiki/mind/somewhere-else\ntitle: \"A Page\"\n"
            "source_modified: 2026-08-28\n---\n\n# A Page\n\nProse.\n",
        )
        code, out = self.errors()
        self.assertEqual(code, 1)
        self.assertIn("plain_of", out)


class TestAudit(TreeCase):
    """The anti-slop referee. Every rule is arithmetic, so every rule is testable."""

    def audit(self, slug="mind/x"):
        return wp.audit_page(self.one(slug))

    def good_twin(self, extra=""):
        """A twin that should pass: page figures kept, honest half present."""
        return (
            "The short version: he moved 4 times between 1892 and 1988.\n\n"
            "## What would prove this wrong\n\nA relative who left and stayed away.\n\n"
            "## What we still don't know\n\nNobody checked the cousins.\n\n"
            + extra
            + "\nThis is the plain-English version of the full entry.\n"
        )

    def base_page(self):
        return (
            "He moved 4 times between 1892 and 1988, across 130 years.\n\n"
            "## Gaps\n\nThe collaterals are unchecked.\n"
        )

    def test_a_faithful_twin_passes(self):
        self.t.page("mind/x", body=self.base_page())
        self.t.twin("mind/x", body=self.good_twin())
        errors, _ = self.audit()
        self.assertEqual(errors, [], errors)

    def test_a_number_not_in_the_page_is_fabrication(self):
        self.t.page("mind/x", body=self.base_page())
        self.t.twin("mind/x", body=self.good_twin("He owned 250 paintings.\n"))
        errors, _ = self.audit()
        self.assertTrue(any("FABRICATED" in e and "250" in e for e in errors), errors)

    def test_single_digits_are_not_fabrication(self):
        # Ordinary prose counts things; "two origins" is not invented evidence.
        self.t.page("mind/x", body=self.base_page())
        self.t.twin("mind/x", body=self.good_twin("There are 2 reasons.\n"))
        errors, _ = self.audit()
        self.assertFalse(any("FABRICATED" in e for e in errors), errors)

    def test_a_number_the_page_spells_out_is_not_fabrication(self):
        # The page writes "thirty-five years"; the twin writing "35" is a
        # rendering choice, not a new quantity.
        self.t.page("mind/x", body=self.base_page() + "\nThirty-five years passed.\n")
        self.t.twin("mind/x", body=self.good_twin("35 years passed.\n"))
        errors, _ = self.audit()
        self.assertFalse(any("FABRICATED" in e for e in errors), errors)

    def test_year_shorthand_is_not_fabrication(self):
        self.t.page("mind/x", body=self.base_page() + "\nHe worked there 2011-2012.\n")
        self.t.twin("mind/x", body=self.good_twin("He worked there in 2011-12.\n"))
        errors, _ = self.audit()
        self.assertFalse(any("FABRICATED" in e for e in errors), errors)

    def test_apparatus_must_not_leak(self):
        for leak in ("[[wiki/people/x]]", "raw/self/notes.md", "knowledge: earned"):
            with self.subTest(leak=leak):
                self.t.twin("mind/x", body=self.good_twin(leak + "\n"))
                self.t.page("mind/x", body=self.base_page())
                errors, _ = self.audit()
                self.assertTrue(any("APPARATUS" in e for e in errors), (leak, errors))

    def test_filler_phrases_fail(self):
        self.t.page("mind/x", body=self.base_page())
        self.t.twin("mind/x", body=self.good_twin("It's important to note this.\n"))
        errors, _ = self.audit()
        self.assertTrue(any("FILLER" in e for e in errors), errors)

    def test_dropping_the_honest_half_fails(self):
        self.t.page("mind/x", body=self.base_page())
        self.t.twin(
            "mind/x",
            body="He moved 4 times between 1892 and 1988 across 130 years. "
            "See the full entry.\n",
        )
        errors, _ = self.audit()
        self.assertTrue(any("HONEST HALF" in e for e in errors), errors)

    def test_a_summary_is_too_short(self):
        self.t.page("mind/x", body=self.base_page() + ("filler word here. " * 400))
        self.t.twin("mind/x", body=self.good_twin())
        errors, _ = self.audit()
        self.assertTrue(any("TOO SHORT" in e for e in errors), errors)

    def test_missing_pointer_back_fails(self):
        self.t.page("mind/x", body=self.base_page())
        self.t.twin(
            "mind/x",
            body="He moved 4 times, 1892 to 1988, 130 years.\n\n"
            "## What would prove this wrong\n\nA relative who stayed away.\n",
        )
        errors, _ = self.audit()
        self.assertTrue(any("POINTER" in e for e in errors), errors)

    def test_grade_level_rises_with_harder_prose(self):
        easy = wp.grade_level("The dog ran. The cat sat. He went home.")
        hard = wp.grade_level(
            "The epistemological ramifications of institutional intransigence "
            "necessitate a reconsideration of methodological presuppositions "
            "underlying contemporary interpretative frameworks."
        )
        self.assertLess(easy, hard)
        self.assertLess(easy, 8)


class TestWiredIntoTheChain(unittest.TestCase):
    """The gate is only a gate if the pre-commit chain actually runs it."""

    def test_wiki_check_gates_on_wiki_plain(self):
        with open(os.path.join(ROOT, "bin", "wiki-check"), encoding="utf-8") as fh:
            source = fh.read()
        block = re.search(r"^GATE = \[(.*?)^\]", source, re.S | re.M)
        self.assertIsNotNone(block, "GATE table not found in bin/wiki-check")
        self.assertIn("wiki-plain", block.group(1))

    def test_wiki_check_gates_on_the_audit_too(self):
        # A slop twin has to block a commit, not merely print a warning.
        with open(os.path.join(ROOT, "bin", "wiki-check"), encoding="utf-8") as fh:
            source = fh.read()
        block = re.search(r"^GATE = \[(.*?)^\]", source, re.S | re.M)
        self.assertIn('"audit"', block.group(1))

    def test_the_dispatch_watches_the_plain_tree(self):
        # A merged translation that does not wake the portal waits an hour,
        # which is the latency notify-portal.yml exists to remove.
        path = os.path.join(ROOT, ".github", "workflows", "notify-portal.yml")
        with open(path, encoding="utf-8") as fh:
            self.assertIn("'plain/**'", fh.read())


if __name__ == "__main__":
    unittest.main(verbosity=2)
