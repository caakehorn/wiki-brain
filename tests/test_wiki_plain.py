#!/usr/bin/env python3
"""Tests for bin/wiki-plain, the READER'S DIGEST layer.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

Two properties are pinned here and neither is cosmetic.

  * **The moratorium is lifted, and stays lifted.** From 2026-08-23 to
    2026-09-06 this tool refused a twin for any page about one living person,
    and no `plain/` file could name her at all. The operator lifted the
    directive in full on 2026-09-06. `TestTheMoratoriumIsLifted` pins the
    absence of the refusal, because the failure mode of a lifted rule is a
    later session reinstating it from memory — the rule was described in four
    files as mechanical and non-negotiable, and three of them have been edited
    since.

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


class TestTheMoratoriumIsLifted(TreeCase):
    """The refusal is gone, and a test says so rather than nothing saying so.

    Every assertion here failed before 2026-09-06 and is expected to keep
    passing. If a later session reintroduces the guard, these break and the
    breakage names the directive that no longer exists.
    """

    def test_no_moratorium_symbols_remain(self):
        for name in ("MORATORIUM", "INCIDENTAL", "held_back", "WITHHELD"):
            with self.subTest(name=name):
                self.assertFalse(hasattr(wp, name),
                                 f"bin/wiki-plain still defines {name}")

    def test_a_page_about_her_is_translatable(self):
        self.t.page("mind/x", body="Annie. " * 40)
        p = self.one()
        self.assertTrue(wp.lane_eligible(p, "major") or p.words < 900)
        self.assertIn(p.slug, [q.slug for q in wp.load() if not q.twin])

    def test_new_scaffolds_a_page_about_her(self):
        self.t.page("mind/x", body="Annie. " * 40)
        args = type("A", (), {"slug": "mind/x"})()
        self.assertEqual(wp.cmd_new(args), 0)
        self.assertTrue(os.path.exists(os.path.join(wp.PLAIN, "mind/x.md")))

    def test_a_twin_may_name_her(self):
        self.t.page("mind/x", body="Annie. " * 40)
        self.t.twin("mind/x", body="Then Annie arrived.")
        code, out = self.errors()
        self.assertEqual(code, 0, out)


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


# ---------------------------------------------------------------------------
# THE TWO LANES
#
# Two writers work this backlog at once — a strong model on the dense findings,
# a weak free one on the short pages — and `next` ranked by word count with no
# filter, so both were handed the same page. The split is arithmetic in the tool
# rather than a convention each writer is trusted to remember, which means it is
# a thing that can be wrong, which means it gets tests.
#
# The floor under the free lane is the part that had to be measured rather than
# chosen. Ordering that lane smallest-first walked it straight into a 16-word
# archived stub and then a run of concert records that are a date and a lineup
# table. Neither has a finding to restate and neither carries falsifiers, so the
# referee's honest-half rule fails every attempt: the agent burns its three
# tries and gives up, on a page nobody wanted translated.
# ---------------------------------------------------------------------------


LANE_PAGE = """---
title: "A Page"
page_type: {page_type}
status: {status}
date_modified: 2026-08-28
---

# A Page

{body}
"""


class LaneCase(unittest.TestCase):
    def setUp(self):
        self.t = Tree()
        self.addCleanup(self.t.close)

    def page(self, slug, n_words, page_type="synthesis", status="stable"):
        """A page whose measured length is exactly `n_words`.

        `words()` counts the whole body, and the body starts with the `# A Page`
        heading — three tokens the caller did not ask for. Padding is trimmed by
        that much and the result asserted, because a fixture that misses the
        boundary by three words tests the wrong side of it and still passes.
        """
        heading = len("# A Page".split())
        write(
            os.path.join(wp.WIKI, f"{slug}.md"),
            LANE_PAGE.format(
                page_type=page_type,
                status=status,
                body=" ".join(["word"] * (n_words - heading)),
            ),
        )
        measured = wp.Page(slug).words
        assert measured == n_words, f"fixture is {measured} words, wanted {n_words}"

    def lanes(self):
        pages = wp.load()
        return (
            [p.slug for p in wp.lane_queue(pages, "major")],
            [p.slug for p in wp.lane_queue(pages, "free")],
        )


class TestLaneBoundaries(LaneCase):
    def test_the_boundary_is_inclusive_at_the_bottom_of_major(self):
        self.page("mind/big", wp.MAJOR_MIN_WORDS)
        self.page("mind/small", wp.MAJOR_MIN_WORDS - 1)
        major, free = self.lanes()
        self.assertEqual(major, ["mind/big"])
        self.assertEqual(free, ["mind/small"])

    def test_the_floor_is_inclusive_at_the_bottom_of_free(self):
        self.page("mind/at", wp.FREE_MIN_WORDS)
        self.page("mind/under", wp.FREE_MIN_WORDS - 1)
        major, free = self.lanes()
        self.assertEqual(free, ["mind/at"])
        self.assertEqual(major, [])
        self.assertEqual([p.slug for p in wp.below_floor(wp.load())], ["mind/under"])

    def test_the_lanes_are_disjoint(self):
        for i, n in enumerate((320, 700, 1200, 5000)):
            self.page(f"mind/p{i}", n)
        major, free = self.lanes()
        self.assertEqual(set(major) & set(free), set())
        self.assertEqual(len(major) + len(free), 4)


class TestLaneHoldouts(LaneCase):
    def test_people_are_in_neither_lane(self):
        self.page("people/somebody", 1200)
        self.page("people/somebody-else", 400)
        self.assertEqual(self.lanes(), ([], []))

    def test_generated_dataset_pages_are_in_neither_lane(self):
        """A twin of a generated page is stale the next time its generator runs."""
        self.page("meta/skills", 1200, page_type="dataset")
        self.assertEqual(self.lanes(), ([], []))

    def test_index_pages_are_in_neither_lane(self):
        """Navigation carries no falsifiers, so the referee fails every attempt."""
        self.page("self/index", 1200, page_type="index")
        self.assertEqual(self.lanes(), ([], []))

    def test_archived_pages_are_in_neither_lane(self):
        self.page("mind/pinned", 1200, status="archived")
        self.assertEqual(self.lanes(), ([], []))

    def test_a_twin_already_written_leaves_the_queue(self):
        self.page("mind/done", 1200)
        self.t.twin("mind/done")
        self.assertEqual(self.lanes(), ([], []))


class TestLaneOrder(LaneCase):
    def test_major_is_densest_first(self):
        for slug, n in (("mind/a", 1000), ("mind/b", 3000), ("mind/c", 2000)):
            self.page(slug, n)
        self.assertEqual(self.lanes()[0], ["mind/b", "mind/c", "mind/a"])

    def test_free_is_smallest_first(self):
        """The free lane's writer is weak; keep it on pages it can finish."""
        for slug, n in (("mind/a", 800), ("mind/b", 320), ("mind/c", 500)):
            self.page(slug, n)
        self.assertEqual(self.lanes()[1], ["mind/b", "mind/c", "mind/a"])


class TestLaneRefusal(LaneCase):
    """`task --lane` refuses out of lane, and refuses rather than advises.

    An agent told to work the free lane and handed a 4,900-word synthesis will
    attempt it. Checking the caller's word rather than the page is how a lane
    becomes advisory, and an advisory lane is not a lane.
    """

    def task(self, slug, lane):
        import argparse
        import contextlib
        import io

        args = argparse.Namespace(slug=slug, lane=lane, synthesis=False)
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = wp.cmd_task(args)
        return code, err.getvalue()

    def test_out_of_lane_is_refused(self):
        self.page("mind/huge", 4000)
        code, err = self.task("mind/huge", "free")
        self.assertEqual(code, 2)
        self.assertIn("not in the free lane", err)

    def test_in_lane_is_handed_over(self):
        self.page("mind/small", 400)
        code, _ = self.task("mind/small", "free")
        self.assertEqual(code, 0)

    def test_the_lane_is_the_only_refusal_left(self):
        """Since 2026-09-06 the lane is the whole of it — no directive above it."""
        write(
            os.path.join(wp.WIKI, "mind/hers.md"),
            LANE_PAGE.format(page_type="synthesis", status="stable",
                             body="Annie " * 40 + " ".join(["word"] * 4000)),
        )
        code, err = self.task("mind/hers", "free")
        self.assertEqual(code, 2)
        self.assertIn("not in the free lane", err)
        self.assertNotIn("moratorium", err)


class TestReport(LaneCase):
    """The generated campaign page.

    Two properties, and the first is the one that bites. The report is a page in
    `wiki/` like any other, so counting itself puts the render in a loop: writing
    the file changes the page count, which changes what the file should say,
    which fails the drift check on the very next run.
    """

    def render(self):
        return wp.render_report(wp.load())

    def write_report(self):
        import argparse
        import contextlib
        import io

        with contextlib.redirect_stdout(io.StringIO()):
            wp.cmd_report(argparse.Namespace(check_only=False))

    def test_the_report_path_follows_the_roots(self):
        """Frozen at import, it would point at the real corpus from a temp tree."""
        self.assertTrue(wp.report_page().startswith(wp.WIKI))

    def test_the_report_is_a_fixpoint(self):
        self.page("mind/a", 1200)
        self.write_report()
        first = read_text(wp.report_page())
        self.write_report()
        self.assertEqual(first, read_text(wp.report_page()))

    def test_the_report_excludes_itself_from_its_own_figures(self):
        self.page("mind/a", 1200)
        before = self.render()
        self.write_report()
        self.assertEqual(before, self.render())

    def test_a_hand_edited_report_fails_the_gate(self):
        self.page("mind/a", 1200)
        self.write_report()
        with open(wp.report_page(), "a", encoding="utf-8") as fh:
            fh.write("\nCoverage is 100%.\n")
        code, out = self.errors()
        self.assertEqual(code, 1)
        self.assertIn("readers-digest.md is behind the tree", out)

    def test_a_tree_with_no_report_is_not_an_error(self):
        """The page is campaign bookkeeping, not something every tree must carry."""
        self.page("mind/a", 1200)
        code, _ = self.errors()
        self.assertEqual(code, 0)

    def errors(self):
        import contextlib
        import io

        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = wp.cmd_check(None)
        return code, buf.getvalue()


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()
