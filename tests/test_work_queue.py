#!/usr/bin/env python3
"""Tests for bin/wiki-work — the mandatory outstanding-work list.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)
      python3 tests/test_work_queue.py -v           (from anywhere)

Pure stdlib, per repo convention. `bin/wiki-work` has no .py extension and its
module body is all definitions, so it can be loaded whole with importlib and
then pointed at a temporary repository — see `load_tool` and `fake_repo`.

The properties under test are the ones the list's usefulness rests on, and each
one is here because getting it wrong is silent:

  - a parked question is an obligation and a struck one is not, because a
    question that stops being listed while its status is still `pending` is a
    promise to somebody outside this repository that nothing is keeping
  - a red gate outranks everything, which is the case that was live on `main`
    on 2026-08-21 and that nothing surfaced
  - `check` never fails, because a gate that blocks unrelated work gets an
    escape hatch and then stops being mandatory at all
  - standing work is counted, never enumerated, because a 130-row table that
    duplicates four other files is the problem this tool exists to solve
"""
import contextlib
import importlib.util
import io
import os
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_tool():
    """Import bin/wiki-work as a module. Its body is definitions only."""
    spec = importlib.util.spec_from_loader(
        "wiki_work", importlib.machinery.SourceFileLoader("wiki_work", str(ROOT / "bin" / "wiki-work")))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


work = load_tool()


@contextlib.contextmanager
def fake_repo(**files):
    """Point the tool at a temporary repository containing exactly `files`.

    Keys are repo-relative paths, values are file bodies (dedented). The module
    holds its paths as module-level constants, so they are swapped for the
    duration and restored afterwards.
    """
    saved = (work.ROOT, work.WIKI, work.SAGE, work.WORK)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name, body in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(textwrap.dedent(body).lstrip("\n"), encoding="utf-8")
        work.ROOT, work.WIKI = root, root / "wiki"
        work.SAGE, work.WORK = root / "sage" / "questions", root / "WORK.md"
        try:
            yield root
        finally:
            work.ROOT, work.WIKI, work.SAGE, work.WORK = saved


QUESTION = """
---
id: 2026-08-21_120000_test
asked: 2026-08-21T12:00:00Z
asker: Ally
status: %s
---

## Question

Can he actually be monogamous?

## Answer
"""


class ParkedQuestions(unittest.TestCase):
    def test_pending_question_is_an_obligation(self):
        with fake_repo(**{"sage/questions/q.md": QUESTION % "pending"}):
            items = work.find_sage()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].kind, "sage")
        self.assertEqual(items[0].priority, 1)
        self.assertIn("monogamous", items[0].what)
        self.assertIn("asked by Ally", items[0].what)
        self.assertEqual(items[0].since, "2026-08-21")

    def test_answered_and_declined_questions_are_not(self):
        for status in ("answered", "declined"):
            with fake_repo(**{"sage/questions/q.md": QUESTION % status}):
                self.assertEqual(work.find_sage(), [], status)

    def test_a_question_with_no_status_is_treated_as_pending(self):
        """A malformed file must fail towards being listed, never away from it."""
        body = QUESTION % "pending"
        with fake_repo(**{"sage/questions/q.md": body.replace("status: pending\n", "")}):
            self.assertEqual(len(work.find_sage()), 1)

    def test_an_unsigned_question_says_so(self):
        body = (QUESTION % "pending").replace("asker: Ally\n", "")
        with fake_repo(**{"sage/questions/q.md": body}):
            self.assertIn("unsigned", work.find_sage()[0].what)

    def test_no_sage_directory_is_not_an_error(self):
        with fake_repo(**{"log.md": "# log\n"}):
            self.assertEqual(work.find_sage(), [])


PAGE = """
---
domain: people
title: Someone
status: active
%s
---

# Someone
"""


class StagedAnswers(unittest.TestCase):
    def test_pending_ingest_flag_is_listed(self):
        with fake_repo(**{"wiki/people/x.md": PAGE % "pending_ingest: 2026-08-16"}):
            items = work.find_staged(work.FLAG_OPERATOR, "close")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].since, "2026-08-16")
        self.assertIn("people/x", items[0].what)

    def test_sage_pending_is_a_separate_flag(self):
        """The two staging kinds must never collapse into one.

        An operator answer is T0 first-person testimony; a sage finding is
        synthesis about the corpus. A page carrying one must not be reported as
        carrying the other.
        """
        with fake_repo(**{"wiki/people/x.md": PAGE % "sage_pending: 2026-08-21"}):
            self.assertEqual(work.find_staged(work.FLAG_OPERATOR, "close"), [])
            self.assertEqual(len(work.find_staged(work.FLAG_SAGE, "sage-close")), 1)

    def test_an_unflagged_page_is_not_listed(self):
        with fake_repo(**{"wiki/people/x.md": PAGE % "importance: high"}):
            self.assertEqual(work.find_staged(work.FLAG_OPERATOR, "close"), [])


class PortalEdits(unittest.TestCase):
    LOG = """
    # log

    ## [2026-07-11] edit | people | human edit via app: wiki/people/old.md
    ## [2026-08-20] lint | wiki | a sweep that normalised everything before it
    ## [2026-08-21] edit | people | human edit via app: wiki/people/fresh.md
    """

    def test_only_edits_after_the_last_lint_sweep_are_listed(self):
        with fake_repo(**{"log.md": self.LOG}):
            items = work.find_portal_edits()
        self.assertEqual(len(items), 1)
        self.assertIn("wiki/people/fresh.md", items[0].what)
        self.assertEqual(items[0].since, "2026-08-21")

    def test_with_no_lint_recorded_every_edit_is_outstanding(self):
        log = "\n".join(ln for ln in self.LOG.splitlines() if "lint" not in ln)
        with fake_repo(**{"log.md": log}):
            self.assertEqual(len(work.find_portal_edits()), 2)


class StandingWork(unittest.TestCase):
    def test_the_ingest_queue_counts_only_unchecked_boxes(self):
        with fake_repo(**{"queue.md": """
            # queue
            - [x] done already
            - [ ] HIGH: export the group chat
            - [ ] MED: mine the CSVs
            some prose that is not a checkbox
        """}):
            n, examples = work.count_queue()
        self.assertEqual(n, 2)
        self.assertEqual(examples[0], "HIGH: export the group chat")

    def test_climbed_clusters_drop_out_of_the_synthesis_queue(self):
        with fake_repo(**{"synthesis-queue.md": """
            | # | score | domains | members |
            |---|---|---|---|
            | 1 | 14.15 | mind, people | [[wiki/mind/a]] · [[wiki/people/b]] |
            | 2 | 13.95 | mind, work | [[wiki/mind/c]] | **CLIMBED -> [[wiki/mind/d]]**
        """}):
            n, examples = work.count_synthesis_queue()
        self.assertEqual(n, 1)
        self.assertIn("cluster 1", examples[0])

    def test_typed_and_done_pairs_drop_out_of_the_connection_queue(self):
        with fake_repo(**{"connection-queue.md": """
            ## [14.0] wiki/a.md <-> wiki/b.md **(DONE 2026-07-20)**
            - type: evidenced-by — added.

            ## [12.9] wiki/c.md <-> wiki/d.md
            - shared source: `raw/x`
            - [ ] type: ______  claim: ______

            ## [12.6] wiki/e.md <-> wiki/f.md
            - type: mirrors — added.
        """}):
            n, examples = work.count_connection_queue()
        self.assertEqual(n, 1)
        self.assertIn("wiki/c.md", examples[0])

    def test_standing_work_is_counted_never_enumerated(self):
        """The whole point of the split: 130 rows in one table is not a list."""
        queue = "# queue\n" + "\n".join("- [ ] item %d" % i for i in range(130))
        with fake_repo(**{"queue.md": queue}):
            items = work.standing()
            self.assertEqual(len(items), 1)
            self.assertEqual(items[0].count, 130)
            work.write_work([], items)
            written = work.WORK.read_text(encoding="utf-8")
        self.assertEqual(written.count("| 5 | ingest |"), 1)
        self.assertNotIn("item 42", written)


class TheBanner(unittest.TestCase):
    def _check(self, **files):
        with fake_repo(**files):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = work.cmd_check()
        return code, out.getvalue()

    def test_check_never_fails_even_with_obligations_outstanding(self):
        """A red banner must not become a red gate. See the module docstring."""
        code, text = self._check(**{"sage/questions/q.md": QUESTION % "pending"})
        self.assertEqual(code, 0)
        self.assertIn("OUTSTANDING WORK", text)
        self.assertIn("never blocks a commit", text)

    def test_check_is_quiet_when_there_is_nothing_to_say(self):
        code, text = self._check(**{"log.md": "# log\n"})
        self.assertEqual(code, 0)
        self.assertIn("no obligations", text)


class NoDoneCommand(unittest.TestCase):
    def test_done_refuses_and_explains(self):
        """There is deliberately no way to mark an item complete by hand.

        A list that can be ticked off independently of the thing it describes can
        lie, and the first lie it would tell is that a parked question has been
        answered.
        """
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = work.main(["done", "sage-whatever"])
        self.assertEqual(code, 2)
        self.assertIn("there is no `done`", out.getvalue())


class AgainstTheRealRepository(unittest.TestCase):
    """The tool has to survive this repository, not only a fixture."""

    def test_scan_and_check_run_clean(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(work.cmd_check(), 0)
        self.assertTrue(out.getvalue().strip())

    def test_every_kind_has_a_priority_and_an_operation(self):
        for kind, (priority, operation) in work.KINDS.items():
            self.assertIsInstance(priority, int, kind)
            self.assertTrue(operation.strip(), kind)

    def test_obligations_outrank_standing_work(self):
        highest_standing = min(p for p, _ in work.STANDING.values())
        lowest_obligation = max(p for p, _ in work.OBLIGATIONS.values())
        self.assertLess(lowest_obligation, highest_standing)


if __name__ == "__main__":
    unittest.main()
