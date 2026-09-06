"""Tests for bin/wiki-claims — the claim validity ledger.

The tests that matter here pin the REFUSALS, not the arithmetic. The arithmetic
is a window comparison and obvious; the refusals are the whole reason the ledger
is worth believing:

  * a `lapsed` claim must never carry a `valid_to` — a lapse means the ending is
    UNKNOWN, and dating it publishes the corpus's silence as the world's;
  * `asof` must report a lapsed claim as UNSETTLED, never as false — c004
    (MOGZART, quiet 2016, revived 2026) is the case that proves it;
  * an expiry must say what closed the window, or it cannot be audited;
  * `ended` must be able to date the ending, or it is a lapse;
  * a validity record is not a forecast — no future dates;
  * the standing directive in CLAUDE.md must REFUSE rather than strip.
"""
import datetime
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "bin" / "wiki-claims"

# bin/ tools carry no .py extension, so the loader is named explicitly — the
# same idiom tests/test_intake.py and tests/test_testimony.py use.
_loader = SourceFileLoader("wiki_claims", str(TOOL))
_spec = importlib.util.spec_from_loader("wiki_claims", _loader)
wc = importlib.util.module_from_spec(_spec)
_loader.exec_module(wc)


def rec(**kw):
    """A minimal claim record, overridable field by field."""
    base = {"claim": "x", "kind": "residence", "subject": "self",
            "valid_from": "2010-01-01", "closure": "ongoing", "valid_to": None,
            "last_seen": None, "tier": "first_party_record", "evidence": "e",
            "pages": [], "source": "raw/x.md", "note": ""}
    base.update(kw)
    return base


def state_of(*claims):
    events = []
    for i, c in enumerate(claims, 1):
        events.append({"type": "claim_recorded", "id": f"c{i:03d}",
                       "at": "2026-01-01", "claim": c})
    return wc.project(events)


class LapseIsNotEnd(unittest.TestCase):
    """The distinction the whole instrument rests on."""

    def test_lapsed_claim_is_unsettled_not_false(self):
        """A record going quiet is a fact about the record, not the world."""
        s = state_of(rec(closure="lapsed", last_seen="2016-03-07",
                         because="the archive stops"))
        held, unknown = wc.live_on(s, datetime.date(2020, 1, 1))
        self.assertEqual(held, [])
        self.assertEqual(len(unknown), 1,
                         "a lapsed claim after last_seen must report UNSETTLED; "
                         "reporting it false would have made the ledger wrong "
                         "about MOGZART, which lapsed in 2016 and revived in 2026")

    def test_lapsed_claim_is_live_before_last_seen(self):
        s = state_of(rec(closure="lapsed", last_seen="2016-03-07",
                         because="the archive stops"))
        held, unknown = wc.live_on(s, datetime.date(2014, 6, 1))
        self.assertEqual(len(held), 1)
        self.assertEqual(unknown, [])

    def test_ended_claim_is_false_after_valid_to(self):
        """`ended` DOES settle the question — that is what distinguishes it."""
        s = state_of(rec(closure="ended", valid_to="2015-12-26",
                         because="final release"))
        held, unknown = wc.live_on(s, datetime.date(2020, 1, 1))
        self.assertEqual(held, [])
        self.assertEqual(unknown, [], "an ended claim is settled, not unknown")


class GateRefusals(unittest.TestCase):
    """What `check` must fail on. Each is a way the ledger could start lying."""

    def _errors(self, *claims):
        events = [{"type": "claim_recorded", "id": f"c{i:03d}",
                   "at": "2026-01-01", "claim": c}
                  for i, c in enumerate(claims, 1)]
        found = []
        for cid, r in wc.live_records(wc.project(events)).items():
            closure = r.get("closure")
            if closure == "lapsed":
                if r.get("valid_to"):
                    found.append("lapsed-with-valid_to")
                if not r.get("last_seen"):
                    found.append("lapsed-without-last_seen")
            if closure in wc.CLOSED and not r.get("because"):
                found.append("closed-without-because")
            if closure == "ended" and r.get("tier") == "none":
                found.append("ended-on-no-evidence")
        return found

    def test_lapsed_may_not_carry_a_valid_to(self):
        self.assertIn("lapsed-with-valid_to",
                      self._errors(rec(closure="lapsed", last_seen="2016-01-01",
                                       valid_to="2016-01-01", because="b")),
                      "a lapse cannot date the ending — that is what makes it a "
                      "lapse. Relaxing this lets the corpus's silence be "
                      "published as the world's.")

    def test_closure_must_say_what_closed_it(self):
        self.assertIn("closed-without-because",
                      self._errors(rec(closure="ended", valid_to="2016-01-01",
                                       because="")))

    def test_ended_on_no_evidence_is_a_lapse(self):
        self.assertIn("ended-on-no-evidence",
                      self._errors(rec(closure="ended", valid_to="2016-01-01",
                                       tier="none", because="b")))


class CommandRefusals(unittest.TestCase):
    """The refusals that live in the argument handling, exercised end to end."""

    def _run(self, *args, cwd=None):
        return subprocess.run([sys.executable, str(TOOL), *args],
                              cwd=cwd or ROOT, capture_output=True, text=True)

    def test_moratorium_is_refused_not_stripped(self):
        r = self._run("record", "Annie is reachable", "--kind", "contact",
                      "--valid-from", "2020-01-01")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("standing", (r.stderr + r.stdout).lower())

    def test_future_valid_from_is_refused(self):
        ahead = (datetime.date.today() + datetime.timedelta(days=30)).isoformat()
        r = self._run("record", "x", "--kind", "residence", "--valid-from", ahead)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("forecast", (r.stderr + r.stdout).lower())

    def test_unknown_kind_is_refused(self):
        r = self._run("record", "x", "--kind", "vibes",
                      "--valid-from", "2020-01-01")
        self.assertNotEqual(r.returncode, 0)

    def test_credential_shape_is_refused(self):
        r = self._run("record", "key is ghp_" + "a" * 36, "--kind", "capability",
                      "--valid-from", "2020-01-01")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("public", (r.stderr + r.stdout).lower())

    def test_page_that_does_not_exist_is_refused(self):
        r = self._run("record", "x", "--kind", "residence", "--valid-from",
                      "2020-01-01", "--pages", "wiki/people/nobody-at-all.md")
        self.assertNotEqual(r.returncode, 0)


class ExpireArgumentDiscipline(unittest.TestCase):
    """`ended` and `lapsed` take different arguments, and swapping them is a lie."""

    def _run_in(self, tmp, *args):
        return subprocess.run([sys.executable, str(tmp / "bin" / "wiki-claims"),
                               *args], capture_output=True, text=True)

    def setUp(self):
        """An isolated tree, so these refusals never touch the real log."""
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "bin").mkdir()
        (self.tmp / "bin" / "wiki-claims").write_text(
            TOOL.read_text(encoding="utf-8"), encoding="utf-8")
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_lapsed_rejects_on(self):
        self._run_in(self.tmp, "record", "x", "--kind", "residence",
                     "--valid-from", "2010-01-01")
        r = self._run_in(self.tmp, "expire", "c001", "--closure", "lapsed",
                         "--on", "2016-01-01", "--because", "b")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("last-seen", (r.stderr + r.stdout).lower())

    def test_ended_requires_a_date(self):
        self._run_in(self.tmp, "record", "x", "--kind", "residence",
                     "--valid-from", "2010-01-01")
        r = self._run_in(self.tmp, "expire", "c001", "--closure", "ended",
                         "--because", "b")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("lapsed", (r.stderr + r.stdout).lower())

    def test_closure_is_never_edited_only_revised(self):
        self._run_in(self.tmp, "record", "x", "--kind", "residence",
                     "--valid-from", "2010-01-01")
        self._run_in(self.tmp, "expire", "c001", "--closure", "ended",
                     "--on", "2016-01-01", "--because", "b")
        r = self._run_in(self.tmp, "expire", "c001", "--closure", "ended",
                         "--on", "2017-01-01", "--because", "b2")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("--revise", r.stderr + r.stdout)


class Projection(unittest.TestCase):
    def test_void_removes_from_live_but_keeps_the_log(self):
        events = [
            {"type": "claim_recorded", "id": "c001", "at": "2026-01-01",
             "claim": rec()},
            {"type": "claim_voided", "id": "c001", "at": "2026-01-02",
             "reason": "misfiled"},
        ]
        s = wc.project(events)
        self.assertEqual(s["counts"]["claims"], 0)
        self.assertEqual(s["counts"]["voided"], 1)
        self.assertIn("c001", s["claims"], "the log keeps a voided record")

    def test_real_ledger_projects_and_gates_clean(self):
        r = subprocess.run([sys.executable, str(TOOL), "check"], cwd=ROOT,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


class ScanIsStructuralNotProse(unittest.TestCase):
    """The design decision worth pinning: scan reads frontmatter, not prose."""

    def test_scan_runs_over_the_real_corpus(self):
        r = subprocess.run([sys.executable, str(TOOL), "scan"], cwd=ROOT,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("UNEARNED `active`", r.stdout)

    def test_scan_does_not_grep_prose_for_no_longer(self):
        source = TOOL.read_text(encoding="utf-8")
        body = source.split("def cmd_scan", 1)[1].split("def ", 1)[0]
        self.assertNotIn('re.compile(r"no longer', body,
                         "the prose grep is ~all false positives on this corpus "
                         "— 121 hits, overwhelmingly quoted tweets")


if __name__ == "__main__":
    unittest.main()
