"""Tests for bin/wiki-testimony — the operator testimony veracity ledger.

The tests that matter here are the ones pinning the REFUSALS and the
SMALL-SAMPLE DISCIPLINE, not the arithmetic. The arithmetic is three lines and
obvious; the refusals are the whole reason the ledger is worth believing:

  * an `unfalsifiable` claim must score ZERO, or the number measures the
    corpus's gaps rather than the man;
  * a miss must name its failure mode and its slant, or the ledger degenerates
    into a tally that predicts nothing;
  * a class under MIN_N must be refused as a prior, or a one-of-one class gets
    quoted as a finding;
  * the standing directive in CLAUDE.md must REFUSE rather than strip.
"""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from importlib.machinery import SourceFileLoader

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "bin" / "wiki-testimony"

# bin/ tools carry no .py extension, so the loader has to be named explicitly —
# the same idiom tests/test_intake.py uses.
_loader = SourceFileLoader("wiki_testimony", str(TOOL))
_spec = importlib.util.spec_from_loader("wiki_testimony", _loader)
wt = importlib.util.module_from_spec(_spec)
_loader.exec_module(wt)


def rec(**kw):
    """A minimal testimony record, overridable field by field."""
    base = {"claim": "x", "classes": ["date"], "confidence": "confident",
            "channel": "capture", "specificity": 2, "load_bearing": False,
            "subject": "self", "speaker": "operator", "asserted": "2026-01-01",
            "about": "2020-01", "source": "raw/x.md", "pages": [], "note": "",
            "adjudication": None, "history": []}
    base.update(kw)
    return base


def adj(outcome, **kw):
    base = {"outcome": outcome, "tier": "first_party_record", "evidence": "e",
            "failure": [], "direction": "none", "magnitude": "", "slant": "",
            "at": "2026-01-02"}
    base.update(kw)
    return base


class TestScoring(unittest.TestCase):
    def test_unfalsifiable_scores_zero_and_is_excluded(self):
        """The single most important rule: the corpus's silence is not his failure."""
        rows = [rec(adjudication=adj("unfalsifiable", tier="none"))]
        self.assertEqual(wt.veracity(rows)["n"], 0)
        self.assertIsNone(wt.veracity(rows)["score"])

    def test_unadjudicated_is_excluded(self):
        self.assertEqual(wt.veracity([rec()])["n"], 0)

    def test_confirmed_and_refuted_are_symmetric(self):
        self.assertEqual(wt.veracity([rec(adjudication=adj("confirmed"))])["score"], 100)
        self.assertEqual(
            wt.veracity([rec(adjudication=adj("refuted", failure=["omission"],
                                              slant="neutral"))])["score"], 0)

    def test_partial_is_a_wash(self):
        rows = [rec(adjudication=adj("partial", failure=["omission"], slant="neutral"))]
        self.assertEqual(wt.veracity(rows)["score"], 50)

    def test_weight_scales_with_specificity_and_load_bearing(self):
        self.assertEqual(wt.weight(rec(specificity=1)), 1.0)
        self.assertEqual(wt.weight(rec(specificity=3)), 3.0)
        self.assertEqual(wt.weight(rec(specificity=2, load_bearing=True)), 3.0)

    def test_an_exact_load_bearing_miss_outweighs_a_vague_hit(self):
        """A wrong docket number must cost more than a right 'sometime in the 90s'."""
        rows = [rec(specificity=3, load_bearing=True,
                    adjudication=adj("refuted", failure=["magnitude"], slant="neutral")),
                rec(specificity=1, adjudication=adj("confirmed"))]
        self.assertLess(wt.veracity(rows)["score"], 50)


class TestCalibration(unittest.TestCase):
    def test_confident_and_right_beats_a_coin_flip(self):
        rows = [rec(confidence="certain", adjudication=adj("confirmed")) for _ in range(4)]
        self.assertGreater(wt.calibration(rows)["skill"], 0.5)

    def test_confidently_wrong_is_worse_than_a_coin_flip(self):
        rows = [rec(confidence="certain",
                    adjudication=adj("refuted", failure=["omission"], slant="neutral"))
                for _ in range(4)]
        self.assertLess(wt.calibration(rows)["skill"], 0)

    def test_a_correct_hedge_is_not_punished_as_hard_as_a_confident_miss(self):
        """The point of measuring calibration at all: the hedge is information."""
        hedged = wt.calibration([rec(confidence="unsure",
                                     adjudication=adj("refuted", failure=["omission"],
                                                      slant="neutral"))])
        certain = wt.calibration([rec(confidence="certain",
                                      adjudication=adj("refuted", failure=["omission"],
                                                       slant="neutral"))])
        self.assertGreater(hedged["skill"], certain["skill"])


class TestSmallSampleDiscipline(unittest.TestCase):
    def test_class_rate_is_shrunk_toward_the_global_rate(self):
        """A one-of-one class must not report 1.00 as though it were a finding."""
        rows = [rec(classes=["date"], adjudication=adj("confirmed")),
                rec(classes=["quantity"],
                    adjudication=adj("refuted", failure=["magnitude"], slant="neutral")),
                rec(classes=["quantity"],
                    adjudication=adj("refuted", failure=["magnitude"], slant="neutral"))]
        cls, glob = wt.by_class(rows)
        self.assertEqual(cls["date"]["rate"], 1.0)
        self.assertLess(cls["date"]["shrunk"], 1.0)
        self.assertGreater(cls["date"]["shrunk"], glob)

    def test_wilson_interval_is_wide_at_n_equals_one(self):
        lo, hi = wt.wilson(1, 1)
        self.assertLess(lo, 0.35)
        self.assertEqual(hi, 1.0)

    def test_wilson_of_nothing_spans_everything(self):
        self.assertEqual(wt.wilson(0, 0), (0.0, 1.0))

    def test_min_n_is_above_one(self):
        """Pins the intent: a prior needs more than a single case behind it."""
        self.assertGreaterEqual(wt.MIN_N, 3)
        self.assertGreaterEqual(wt.MIN_BUCKET, 3)


class TestMoratorium(unittest.TestCase):
    def test_the_pattern_matches_the_names_it_must(self):
        for name in ("Annie", "annie", "Ulmer", "ULMER", "Lo_weez"):
            self.assertTrue(wt.MORATORIUM.search(name), name)

    def test_the_pattern_does_not_match_unrelated_words(self):
        for name in ("Danielle", "Alexis", "annual", "vulnerable", "Suzanne"):
            self.assertIsNone(wt.MORATORIUM.search(name), name)

    def test_record_refuses_rather_than_strips(self):
        """Refuse, never sanitise: a stripped record is a record that got in."""
        with self.assertRaises(SystemExit):
            wt.moratorium_guard("a claim about Annie")


class TestProjection(unittest.TestCase):
    def test_a_revision_supersedes_without_erasing(self):
        events = [
            {"type": "testimony_recorded", "id": "t001", "at": "2026-01-01",
             "testimony": {"claim": "c", "classes": ["date"], "confidence": "certain"}},
            {"type": "testimony_adjudicated", "id": "t001", "at": "2026-01-02",
             "adjudication": adj("confirmed")},
            {"type": "adjudication_revised", "id": "t001", "at": "2026-01-03",
             "reason": "the corroborating export was the wrong account",
             "adjudication": adj("refuted", failure=["transposition"], slant="neutral")},
        ]
        state = wt.project(events)
        r = state["testimonies"]["t001"]
        self.assertEqual(r["adjudication"]["outcome"], "refuted")
        self.assertEqual(len(r["history"]), 1)
        self.assertEqual(r["history"][0]["was"]["outcome"], "confirmed")

    def test_a_voided_record_leaves_the_statistics_but_stays_in_the_log(self):
        events = [
            {"type": "testimony_recorded", "id": "t001", "at": "2026-01-01",
             "testimony": {"claim": "c", "classes": ["date"], "confidence": "certain"}},
            {"type": "testimony_voided", "id": "t001", "at": "2026-01-02",
             "reason": "not operator testimony — a derived count"},
        ]
        state = wt.project(events)
        self.assertIn("t001", state["testimonies"])
        self.assertEqual(state["counts"]["testimonies"], 0)
        self.assertEqual(live := wt.live_records(state), [])

    def test_third_party_speech_is_excluded_from_the_operator_score(self):
        events = [
            {"type": "testimony_recorded", "id": "t001", "at": "2026-01-01",
             "testimony": {"claim": "c", "classes": ["date"], "speaker": "suzanne",
                           "confidence": "certain", "specificity": 2}},
        ]
        state = wt.project(events)
        self.assertEqual(wt.live_records(state, speaker="operator"), [])
        self.assertEqual(len(wt.live_records(state, speaker="suzanne")), 1)


class TestCliRefusals(unittest.TestCase):
    """The refusals that keep the ledger predictive, exercised end to end."""

    def run_tool(self, *args, repo=None):
        """Run the COPY inside `repo`, never the real tool with a foreign cwd.

        The tool resolves its ledger from its own __file__, not from the working
        directory, so invoking the real script with cwd=<tempdir> writes into the
        live ledger. That is exactly what happened while these tests were being
        written, and it is what this signature exists to make impossible.
        """
        script = str(Path(repo) / "bin" / "wiki-testimony") if repo else str(TOOL)
        return subprocess.run([sys.executable, script, *args],
                              cwd=repo or ROOT, capture_output=True, text=True)

    def test_a_miss_must_name_its_failure_mode(self):
        with tempfile.TemporaryDirectory() as td:
            r = self._seed_and(td, "adjudicate", "t001", "--outcome", "refuted",
                               "--tier", "first_party_record", "--slant", "neutral")
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("failure", r.stderr)

    def test_a_miss_must_name_its_slant(self):
        with tempfile.TemporaryDirectory() as td:
            r = self._seed_and(td, "adjudicate", "t001", "--outcome", "refuted",
                               "--tier", "first_party_record", "--failure", "omission")
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("slant", r.stderr)

    def test_a_confirmation_on_no_evidence_is_not_a_confirmation(self):
        with tempfile.TemporaryDirectory() as td:
            r = self._seed_and(td, "adjudicate", "t001", "--outcome", "confirmed",
                               "--tier", "none")
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("unfalsifiable", r.stderr)

    def test_readjudicating_needs_an_explicit_revision(self):
        with tempfile.TemporaryDirectory() as td:
            self._seed_and(td, "adjudicate", "t001", "--outcome", "confirmed",
                           "--tier", "primary_document")
            r = self.run_tool("adjudicate", "t001", "--outcome", "refuted",
                              "--tier", "first_party_record", "--failure", "omission",
                              "--slant", "neutral", repo=td)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("superseded", r.stderr)

    def _seed_and(self, td, *args):
        """A throwaway repo with one recorded claim, then one command against it."""
        td = Path(td)
        (td / "bin").mkdir(parents=True, exist_ok=True)
        (td / "testimony").mkdir(parents=True, exist_ok=True)
        (td / "wiki" / "meta").mkdir(parents=True, exist_ok=True)
        (td / "bin" / "wiki-testimony").write_bytes(TOOL.read_bytes())
        self.run_tool("record", "--claim", "a claim", "--class", "date",
                      "--source", "raw/x.md", repo=td)
        return self.run_tool(*args, repo=td)


class TestLedgerIntegrity(unittest.TestCase):
    """The committed ledger itself, not a fixture."""

    def test_the_gate_is_green(self):
        r = subprocess.run([sys.executable, str(TOOL), "check"],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_the_log_is_valid_jsonl(self):
        log = ROOT / "testimony" / "events.jsonl"
        if not log.exists():
            self.skipTest("no ledger yet")
        for i, line in enumerate(log.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip():
                json.loads(line)

    def test_every_seeded_claim_cites_a_source(self):
        log = ROOT / "testimony" / "events.jsonl"
        if not log.exists():
            self.skipTest("no ledger yet")
        state = wt.project(wt.read_log())
        for tid, r in state["testimonies"].items():
            if r.get("voided"):
                continue
            self.assertTrue(r.get("source"),
                            f"{tid} has no source — a testimony with no record of "
                            f"where it was said is an assertion, not testimony")

    def test_no_record_names_a_person_under_the_directive(self):
        state = wt.project(wt.read_log())
        self.assertIsNone(wt.MORATORIUM.search(json.dumps(state, ensure_ascii=False)))


if __name__ == "__main__":
    unittest.main()


class TestSpeakerIsNotSilentlyThirdParty(unittest.TestCase):
    """`--speaker` exists so third-party testimony stays OUT of Dan's score, and
    every statistic here filters on `speaker == "operator"`. That is correct and
    it is silent: a first-person claim filed as `--speaker dan` vanishes from the
    score, the profile and the public page with nothing saying so.

    It had happened twice by the time anyone looked (2026-09-05) — **t017**, the
    May 2017 cocaine spend figure, filed `dan`, and **t020**, the $14,000 loan
    framing, filed `Dan`. The headline was being computed over 18 of 20 records
    and reporting no such thing; repairing them moved veracity 51 → 57.
    """

    def test_the_operator_s_own_aliases_normalise_on_entry(self):
        for name in ("dan", "Dan", "Dan Frank", "DANFRANK", "self", "operator",
                     " dan  "):
            self.assertEqual("operator", wt.normalise_speaker(name), name)

    def test_a_real_third_party_is_left_alone(self):
        for name in ("Suz", "Davey Fitzpatrick", "annie's mother"):
            self.assertEqual(name, wt.normalise_speaker(name))

    def test_absent_speaker_is_the_operator(self):
        self.assertEqual("operator", wt.normalise_speaker(None))
        self.assertEqual("operator", wt.normalise_speaker(""))

    def test_a_non_operator_record_is_excluded_from_every_statistic(self):
        """Pinning the behaviour that makes the warning necessary, not a bug."""
        state = {"testimonies": {
            "t1": rec(speaker="operator"),
            "t2": rec(speaker="Suz"),
        }}
        self.assertEqual(1, len(wt.live_records(state)))
        self.assertEqual(1, len(wt.live_records(state, speaker="Suz")))

    def test_check_names_a_record_no_statistic_will_ever_see(self):
        """The gate has to say it out loud — an unadjudicated one too, which is
        where the first version of this warning was placed wrong and missed
        t017 entirely."""
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            (td / "bin").mkdir(parents=True)
            (td / "testimony").mkdir(parents=True)
            (td / "wiki" / "meta").mkdir(parents=True)
            (td / "bin" / "wiki-testimony").write_bytes(TOOL.read_bytes())
            run = lambda *a: subprocess.run(
                [sys.executable, str(td / "bin" / "wiki-testimony"), *a],
                cwd=td, capture_output=True, text=True)
            # A hand-written event can still put a foreign speaker in the log,
            # which is why the gate checks rather than trusting the entry path.
            run("record", "--claim", "a claim", "--class", "date",
                "--source", "raw/x.md")
            log = td / "testimony" / "events.jsonl"
            ev = [json.loads(l) for l in log.read_text().splitlines() if l.strip()]
            ev[0]["testimony"]["speaker"] = "Suz"
            log.write_text("".join(json.dumps(e) + "\n" for e in ev))
            run("page")   # `check` errors on a missing page before it warns
            out = run("check")
            self.assertIn("speaker 'Suz'", out.stdout + out.stderr)
            self.assertIn("excluded", out.stdout + out.stderr)
            self.assertEqual(0, out.returncode, "a warning, never a gate failure")
