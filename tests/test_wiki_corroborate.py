#!/usr/bin/env python3
"""Tests for bin/wiki-corroborate, the message-record join.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

Four properties are pinned here and none is cosmetic.

  * **`absent` is not `uncovered`.** `absent` means the window was read and
    holds nothing — a real result. `uncovered` means the corpus does not reach
    that date at all: 2012-2014 hold nothing and 2022 holds four rows. Letting
    one stand in for the other publishes the archive's silence as the world's,
    which is the same error `bin/wiki-traits` refuses between `silent` and
    `unreviewed` and `bin/wiki-claims` refuses between `ended` and `lapsed`.
    The tool refuses BOTH directions, and both refusals are pinned.

  * **A citation is verified before it is stored.** `record` loads the window
    and checks every `--row` against the archive. A ledger whose rows cannot be
    found is worse than no ledger: it looks like evidence.

  * **The gate reads the diff, and reads the right lines.** Diff hunks count
    from the top of the FILE; `dated_claims` walks the BODY. The offset between
    them is load-bearing and its failure mode is silent — the gate reads the
    wrong lines, finds nothing, and passes. It shipped broken for exactly that
    reason and was caught by a deliberate test edit rather than by any output.

  * **The gate is narrow on purpose.** A date the page already carried is
    inherited debt, not this commit's fault; re-wording the sentence around it
    must not go red, or the gate gets switched off within a week and the whole
    mechanism is decorative. 378 pages carry such debt today.

The real corpus is read only where a test says so; the ledger is never touched.
"""
import contextlib
import io
import importlib.machinery
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "bin" / "wiki-corroborate"


def load():
    loader = importlib.machinery.SourceFileLoader("wiki_corroborate", str(TOOL))
    spec = importlib.util.spec_from_loader("wiki_corroborate", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


wc = load()


class Coverage(unittest.TestCase):
    """The floor under the word 'absent'."""

    def setUp(self):
        self.cov = {"union": {"2013": 0, "2017": 21836, "2022": 4, "2026": 16116},
                    "computed": "2026-09-06", "corpora": {}}

    def test_a_thin_year_is_not_covered(self):
        self.assertFalse(wc.is_covered("2022-06-01", self.cov))
        self.assertFalse(wc.is_covered("2013-04-02", self.cov))

    def test_a_real_year_is_covered(self):
        self.assertTrue(wc.is_covered("2017-11-26", self.cov))
        self.assertTrue(wc.is_covered("2026-01-01", self.cov))

    def test_the_threshold_is_a_floor_not_a_quality_bar(self):
        self.assertGreaterEqual(wc.COVERED_MIN_ROWS, 100)

    def test_the_real_coverage_table_is_committed(self):
        """`record` refuses to guess at coverage, so the projection must exist."""
        self.assertTrue(wc.COVERAGE.exists(),
                        "corroborate/coverage.json is missing — run `coverage --write`")
        cov = json.loads(wc.COVERAGE.read_text(encoding="utf-8"))
        self.assertIn("2017", cov["union"])
        for gap in ("2012", "2013", "2014"):
            self.assertNotIn(gap, cov["union"],
                             "%s has rows now — the coverage story in CLAUDE.md, "
                             "EXTRACTION_SPEC.md and the skill needs updating" % gap)


class DatedClaims(unittest.TestCase):
    PAGE = ("---\ndomain: mind\ndate_modified: 2026-09-01\n---\n\n"
            "# A Page\n\n"
            "He moved on 2017-11-26 and stayed.\n"
            "The fall was in ~late 2017?, nobody is sure.\n"
            "Written up in November 2019 by somebody else.\n"
            "date_range_end: 2020-01-01 should not count.\n")

    def test_iso_month_and_hedged_dates_are_all_found(self):
        got = {d for d, _p, _h, _l, _n in wc.dated_claims(self.PAGE)}
        self.assertIn("2017-11-26", got)
        self.assertIn("2019-11", got)
        self.assertIn("2017", got)

    def test_a_hedge_is_marked(self):
        hedged = {d for d, _p, h, _l, _n in wc.dated_claims(self.PAGE) if h}
        self.assertIn("2017", hedged)
        self.assertNotIn("2017-11-26", hedged)

    def test_frontmatter_machinery_is_not_a_claim(self):
        """`date_range_end:` says what a page covers, not what happened."""
        got = {d for d, _p, _h, _l, _n in wc.dated_claims(self.PAGE)}
        self.assertNotIn("2020-01-01", got)

    def test_added_only_counts_file_lines_not_body_lines(self):
        """The offset that shipped broken. Its failure mode is silent."""
        body_line = self.PAGE.split("\n").index("He moved on 2017-11-26 and stayed.") + 1
        got = {d for d, _p, _h, _l, _n in wc.dated_claims(self.PAGE, added_only={body_line})}
        self.assertEqual(got, {"2017-11-26"},
                         "dated_claims read the wrong line — the frontmatter "
                         "offset is what makes the gate see a diff at all")


class TheGateDoesNotFireOnItself(unittest.TestCase):
    """Two false-positive classes, both of which the gate shipped with.

    Each was found by running the gate on the pass that introduced the feature,
    and each teaches the same lesson in a different place: a date is not a claim
    just because it is a date. Left in, they make the gate fire on its own
    output and on the command it just told you to run — which is how a
    mandatory step becomes noise and then becomes disabled.
    """

    def test_a_rule_9_marker_date_is_bookkeeping_not_a_claim(self):
        page = ("---\ndomain: x\n---\n\n"
                "> **CORROBORATED [2026-09-06]:** the fall was on 2017-11-26.\n"
                "> **GAP CLOSED [2026-08-18].** Something else.\n"
                "> **REVISED [2026-07-13]:** it ran until February 2025.\n")
        got = {d for d, _p, _h, _l, _n in wc.dated_claims(page)}
        self.assertIn("2017-11-26", got, "prose inside the block is still a claim")
        self.assertIn("2025-02", got)
        for marker_date in ("2026-09-06", "2026-08-18", "2026-07-13"):
            self.assertNotIn(marker_date, got,
                             "%s is the date the WIKI changed, like date_modified"
                             % marker_date)

    def test_a_date_inside_backticks_is_an_argument_not_a_claim(self):
        page = ("---\ndomain: x\n---\n\n"
                "Window: `bin/wiki-corroborate window 2017-11-26 --days 1`.\n"
                "He moved on 2019-04-02.\n")
        got = {d for d, _p, _h, _l, _n in wc.dated_claims(page)}
        self.assertEqual(got, {"2019-04-02"})

    def test_a_code_span_crossing_a_line_still_blanks(self):
        """Wrapped commands are the common case in a blockquote."""
        body = "Probe: `bin/wiki-corroborate probe x --since 2018-07-01 --until\n2018-12-31` — 3 matches.\n"
        self.assertNotIn("2018-07-01", wc.blank_code(body))
        self.assertNotIn("2018-12-31", wc.blank_code(body))

    def test_blanking_preserves_line_numbers(self):
        """`added_only` matches diff line numbers, so nothing may shift."""
        body = "a\n`x 2018-07-01\n2018-12-31`\nb\n"
        self.assertEqual(len(wc.blank_code(body).split("\n")), len(body.split("\n")))


class RecordRefusals(unittest.TestCase):
    """Every refusal here exists because the alternative looks like evidence."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "bin").mkdir()
        (self.tmp / "bin" / "wiki-corroborate").write_text(
            TOOL.read_text(encoding="utf-8"), encoding="utf-8")
        (self.tmp / "bin" / "mine-messages").write_text(
            (ROOT / "bin" / "mine-messages").read_text(encoding="utf-8"), encoding="utf-8")
        (self.tmp / "corroborate").mkdir()
        (self.tmp / "corroborate" / "coverage.json").write_text(json.dumps({
            "computed": "2026-09-06", "corpora": {},
            "union": {"2017": 21836, "2013": 0, "2022": 4},
        }), encoding="utf-8")
        (self.tmp / "wiki" / "people").mkdir(parents=True)
        (self.tmp / "wiki" / "people" / "x.md").write_text(
            "---\ndomain: people\n---\n\n# X\n", encoding="utf-8")
        import shutil
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def run_tool(self, *args):
        return subprocess.run([sys.executable, str(self.tmp / "bin" / "wiki-corroborate"), *args],
                              capture_output=True, text=True, cwd=str(self.tmp))

    def record(self, **kw):
        args = ["record", "--page", "wiki/people/x",
                "--claim", kw.get("claim", "He was at the house that whole night"),
                "--date", kw.get("date", "2017-11-26"),
                "--outcome", kw["outcome"],
                "--because", kw.get("because", "the thread says so")]
        for r in kw.get("rows", []):
            args += ["--row", r]
        return self.run_tool(*args)

    def test_absent_is_refused_outside_coverage(self):
        r = self.record(outcome="absent", date="2013-04-02")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("uncovered", (r.stdout + r.stderr).lower())

    def test_uncovered_is_refused_inside_coverage(self):
        """The other direction. A refusal that only runs one way is half a rule."""
        r = self.record(outcome="uncovered", date="2017-11-26")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("absent", (r.stdout + r.stderr).lower())

    def test_a_positive_outcome_must_cite_rows(self):
        r = self.record(outcome="corroborated")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("cite", (r.stdout + r.stderr).lower())

    def test_absent_may_not_cite_rows(self):
        r = self.record(outcome="absent", rows=["2017-11-26 00:06 Sent +1"])
        self.assertNotEqual(r.returncode, 0)

    def test_a_row_outside_the_window_is_refused(self):
        r = self.record(outcome="corroborated", rows=["2017-12-25 10:00 Sent +1"])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("window", (r.stdout + r.stderr).lower())

    def test_a_malformed_row_is_refused(self):
        r = self.record(outcome="corroborated", rows=["some time that evening"])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("timestamp", (r.stdout + r.stderr).lower())

    def test_because_is_required(self):
        r = self.run_tool("record", "--page", "wiki/people/x", "--claim",
                          "He was at the house that whole night", "--date",
                          "2017-11-26", "--outcome", "absent", "--because", "  ")
        self.assertNotEqual(r.returncode, 0)

    def test_an_absent_record_is_accepted_and_projects(self):
        r = self.record(outcome="absent")
        self.assertEqual(r.returncode, 0, r.stderr)
        state = json.loads((self.tmp / "corroborate" / "records.json").read_text())
        self.assertEqual(len(state["records"]), 1)
        self.assertEqual(list(state["records"].values())[0]["outcome"], "absent")


class CitationsAreVerified(unittest.TestCase):
    """Against the real archive: a row that does not exist cannot be cited."""

    def test_an_invented_timestamp_is_refused(self):
        if not (ROOT / "raw" / "self" / "dox-scan" / "all_imessages_complete_dump.txt").exists():
            self.skipTest("message corpus not present")
        r = subprocess.run(
            [sys.executable, str(TOOL), "record", "--page", "wiki/meta/index",
             "--claim", "A claim nobody should be able to cite for",
             "--date", "2017-11-26", "--outcome", "corroborated",
             "--row", "2017-11-26 03:59 Sent +19999999999",
             "--because", "testing that the verifier bites"],
            capture_output=True, text=True, cwd=str(ROOT))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("no message exists", (r.stdout + r.stderr).lower())


class TheGate(unittest.TestCase):
    def test_a_record_must_contain_its_own_date(self):
        rec = {"date": "2017-11-26", "window": {"from": "2017-11-25", "to": "2017-11-27"}}
        self.assertTrue(wc.covers(rec, "2017-11-26"))
        self.assertFalse(wc.covers(rec, "2018-01-01"))

    def test_month_precision_matches_by_month(self):
        rec = {"date": "2017-11", "window": {"from": "2017-11-01", "to": "2017-11-30"}}
        self.assertTrue(wc.covers(rec, "2017-11"))
        self.assertFalse(wc.covers(rec, "2017-12"))

    def test_generated_pages_are_exempt(self):
        for slug in ("wiki/timeline/master-timeline", "wiki/meta/corroboration"):
            self.assertIn(slug, wc.GENERATED)

    def test_the_gate_runs_clean_on_the_committed_tree(self):
        r = subprocess.run([sys.executable, str(TOOL), "check"],
                           capture_output=True, text=True, cwd=str(ROOT))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class WiredIntoTheChain(unittest.TestCase):
    def test_wiki_check_gates_on_it(self):
        src = (ROOT / "bin" / "wiki-check").read_text(encoding="utf-8")
        self.assertIn('["wiki-corroborate", "check"]', src)

    def test_wiki_check_regenerates_the_page(self):
        """The page is gated on drift, so its generator belongs in GENERATE."""
        src = (ROOT / "bin" / "wiki-check").read_text(encoding="utf-8")
        self.assertIn('["wiki-corroborate", "page"]', src)

    def test_the_operation_is_in_claude_md(self):
        doc = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertIn("### CORROBORATE", doc)
        self.assertIn("bin/wiki-corroborate check", doc)

    def test_the_skill_is_routed(self):
        idx = (ROOT / "skills" / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("message-record-primacy", idx)


if __name__ == "__main__":
    unittest.main()
