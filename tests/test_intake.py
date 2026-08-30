#!/usr/bin/env python3
"""Tests for bin/intake, the intake ledger.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

What is pinned here is the honesty of the arithmetic, because that is the only
part of this tool that can be wrong without looking wrong. A dose average is a
number; a reader cannot tell by looking whether it quietly absorbed a gram
nobody weighed. So:

  * **Unquantified events never enter a quantity statistic**, and never stop
    counting as events. This is the whole reason the third measurement type
    exists — a ledger that drops the event when the scale is absent loses the
    behavioural record silently, and one that guesses at the number loses
    something worse.

  * **Closing will not invent a distribution for what it cannot see.** Open
    3.5 g, log 2.45 g, and the unit does not close until somebody says what
    happened to the rest. If the answer is `final_intake`, the remainder is
    written as an explicitly estimated event and named as a remainder wherever
    it shows up — never folded into the measured total.

  * **The log is append-only and corrections are additive.** A corrected event
    still stands in the file with the correction beside it; the projection can
    be deleted and rebuilt to the byte.

  * **The projection cannot silently drift** from the log, which is what makes
    it safe for `bin/wiki-check` to treat as a gate.

The real ledger is never touched: every case builds one in a temp directory.
"""
import importlib.util
import json
import os
import re
import sys
import tempfile
import unittest
from importlib.machinery import SourceFileLoader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "bin", "intake")


def load():
    """bin/intake has no .py extension; load it the way app.py does."""
    loader = SourceFileLoader("intake_ledger", SCRIPT)
    spec = importlib.util.spec_from_loader("intake_ledger", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


m = load()


class LedgerCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        self.L = m.Ledger(self.root)
        self.L.write_substances(list(m.DEFAULT_SUBSTANCES))
        self.ops = m.Ops(self.L)
        self.addCleanup(self.tmp.cleanup)

    def unit(self, substance="cocaine", qty=3.5, unit="g", at="2026-08-01 12:00"):
        return self.ops.new_unit(substance, qty, unit, at)

    def reload(self, ref=1):
        return self.L.find_unit(ref)


class TestQuantities(LedgerCase):
    def test_units_convert_inside_a_family(self):
        self.assertAlmostEqual(m.convert(180, "mg", "g"), 0.18)
        self.assertAlmostEqual(m.convert(1, "l", "ml"), 1000)

    def test_units_never_convert_across_families(self):
        """'2 tab' is not 2 g and a millilitre is not a milligram."""
        with self.assertRaises(m.LedgerError):
            m.convert(5, "ml", "mg")
        with self.assertRaises(m.LedgerError):
            m.convert(2, "tab", "g")

    def test_a_quantity_without_a_unit_is_refused(self):
        with self.assertRaises(m.LedgerError):
            m.parse_quantity("3.5")

    def test_mixed_units_land_in_the_units_own_scale(self):
        self.unit()
        self.ops.log_intake(1, 180, "mg", "measured", occurred_at="2026-08-01 13:00")
        self.assertAlmostEqual(self.reload()["analysis"]["quantified_total"], 0.18)


class TestSubstanceCatalog(LedgerCase):
    def test_a_substance_off_the_catalog_is_refused_not_invented(self):
        """The select box degrades back into free text the moment this passes."""
        with self.assertRaises(m.LedgerError):
            self.ops.new_unit("something novel", 1, "g")

    def test_adding_one_records_an_event_and_is_then_usable(self):
        self.ops.L.add_substance("Kratom", "other", "g")
        types = [e["type"] for e in self.L.read_events()]
        self.assertIn("substance_added", types)
        self.assertEqual(self.ops.new_unit("kratom", 10, "g")["substance"], "Kratom")

    def test_duplicates_are_refused(self):
        with self.assertRaises(m.LedgerError):
            self.ops.L.add_substance("Cocaine")


class TestUnquantifiedEvents(LedgerCase):
    """The behavioural record survives the scale being in another room."""

    def setUp(self):
        super().setUp()
        self.unit()
        self.ops.log_intake(1, 0.2, "g", "measured", occurred_at="2026-08-01 13:00")
        self.ops.log_intake(1, 0.4, "g", "measured", occurred_at="2026-08-01 15:00")
        self.ops.log_intake(1, descriptor="one line", occurred_at="2026-08-01 17:00")
        self.a = self.reload()["analysis"]

    def test_it_counts_as_an_event(self):
        self.assertEqual(self.a["events"]["total"], 3)
        self.assertEqual(self.a["events"]["unquantified"], 1)

    def test_it_contributes_nothing_to_any_quantity(self):
        self.assertAlmostEqual(self.a["quantified_total"], 0.6)
        self.assertAlmostEqual(self.a["dose"]["mean"], 0.3)
        self.assertEqual(self.a["dose"]["n"], 2)

    def test_it_still_shapes_the_timing(self):
        """Two intervals, not one — the event happened even if the gram did not."""
        self.assertEqual(self.a["interval"]["n"], 2)

    def test_coverage_is_reported_next_to_the_numbers(self):
        self.assertAlmostEqual(self.a["coverage"], 2 / 3)
        self.assertIn("2 of 3", m.coverage_line(self.a))

    def test_a_descriptorless_unquantified_event_is_refused(self):
        with self.assertRaises(m.LedgerError):
            self.ops.log_intake(1)


class TestEstimates(LedgerCase):
    def test_estimated_is_counted_but_kept_separate_from_measured(self):
        self.unit()
        self.ops.log_intake(1, 0.2, "g", "measured", occurred_at="2026-08-01 13:00")
        self.ops.log_intake(1, 0.2, "g", "estimated", occurred_at="2026-08-01 14:00")
        a = self.reload()["analysis"]
        self.assertAlmostEqual(a["measured_total"], 0.2)
        self.assertAlmostEqual(a["estimated_total"], 0.2)
        self.assertAlmostEqual(a["quantified_total"], 0.4)
        self.assertTrue(a["remaining_is_estimate"])

    def test_an_estimate_defaults_to_a_stated_confidence(self):
        self.unit()
        self.ops.log_intake(1, 0.2, "g", "estimated", occurred_at="2026-08-01 13:00")
        self.assertEqual(self.reload()["intakes"][0]["confidence"], "medium")


class TestCorrections(LedgerCase):
    def setUp(self):
        super().setUp()
        self.unit()
        self.ev, _ = self.ops.log_intake(1, 0.5, "g", "measured", occurred_at="2026-08-01 13:00")

    def test_a_correction_supersedes_the_value(self):
        self.ops.correct(self.ev["id"], {"quantity": 0.05, "unit": "g"},
                         reason="decimal entry error")
        self.assertAlmostEqual(self.reload()["analysis"]["quantified_total"], 0.05)

    def test_the_original_survives_in_the_log(self):
        """Nothing is edited in place — that a typo happened is itself evidence."""
        self.ops.correct(self.ev["id"], {"quantity": 0.05, "unit": "g"}, reason="typo")
        raw = self.L.events_path.read_text()
        self.assertIn('"quantity": 0.5', raw)
        self.assertIn("typo", raw)
        rec = self.reload()["intakes"][0]
        self.assertEqual(rec["corrections"][0]["from"]["quantity"], 0.5)
        self.assertEqual(rec["corrections"][0]["to"]["quantity"], 0.05)

    def test_a_correction_without_a_reason_is_refused(self):
        with self.assertRaises(m.LedgerError):
            self.ops.correct(self.ev["id"], {"quantity": 0.05}, reason="")

    def test_a_voided_event_leaves_the_totals_but_not_the_log(self):
        self.ops.void(self.ev["id"], reason="logged against the wrong unit")
        a = self.reload()["analysis"]
        self.assertEqual(a["events"]["total"], 0)
        self.assertEqual(a["events"]["voided"], 1)
        self.assertAlmostEqual(a["quantified_total"], 0.0)
        self.assertIn("wrong unit", self.L.events_path.read_text())


class TestAdjustments(LedgerCase):
    def test_a_spill_leaves_the_unit_without_becoming_a_dose(self):
        self.unit()
        self.ops.log_intake(1, 0.5, "g", "measured", occurred_at="2026-08-01 13:00")
        self.ops.adjust(1, 0.3, "g", "spill", occurred_at="2026-08-01 14:00")
        a = self.reload()["analysis"]
        self.assertAlmostEqual(a["quantified_total"], 0.5)   # not 0.8
        self.assertAlmostEqual(a["adjusted_total"], 0.3)
        self.assertAlmostEqual(a["remaining"], 2.7)
        self.assertEqual(a["dose"]["n"], 1)


class TestClosure(LedgerCase):
    def setUp(self):
        super().setUp()
        self.unit()
        for hour, qty in ((13, 0.2), (15, 0.4), (17, 0.3)):
            self.ops.log_intake(1, qty, "g", "measured",
                                occurred_at=f"2026-08-01 {hour}:00")

    def test_it_refuses_to_close_over_an_unexplained_remainder(self):
        """This is the rule the whole design exists to enforce."""
        with self.assertRaises(m.LedgerError) as ctx:
            self.ops.close_unit(1, "consumed")
        self.assertIn("unaccounted", str(ctx.exception))

    def test_a_discrepancy_is_recorded_and_never_absorbed_into_the_doses(self):
        u, _, _ = self.ops.close_unit(1, "consumed", resolution="discrepancy",
                                      closed_at="2026-08-02 09:00")
        self.assertAlmostEqual(u["analysis"]["quantified_total"], 0.9)
        self.assertAlmostEqual(u["analysis"]["dose"]["mean"], 0.3)
        self.assertEqual(u["reconciliation"]["resolution"], "discrepancy")
        self.assertAlmostEqual(u["reconciliation"]["unaccounted"], 2.6)

    def test_a_final_intake_is_estimated_and_flagged_as_a_remainder(self):
        u, _, _ = self.ops.close_unit(1, "consumed", resolution="final_intake",
                                      closed_at="2026-08-02 09:00")
        a = u["analysis"]
        self.assertAlmostEqual(a["quantified_total"], 3.5)
        self.assertAlmostEqual(a["measured_total"], 0.9)      # never inflated
        self.assertAlmostEqual(a["reconciliation_total"], 2.6)
        self.assertEqual(a["events"]["measured"], 3)
        self.assertEqual(a["events"]["estimated"], 1)
        self.assertIn("written off at close", m.render_report(u))

    def test_a_balanced_unit_closes_without_being_asked(self):
        self.ops.log_intake(1, 2.6, "g", "measured", occurred_at="2026-08-01 19:00")
        u, _, _ = self.ops.close_unit(1, "consumed")
        self.assertEqual(u["reconciliation"]["resolution"], "balanced")

    def test_closing_writes_an_immutable_capture_under_raw(self):
        u, capture, _ = self.ops.close_unit(1, "consumed", resolution="discrepancy")
        self.assertTrue(capture.exists())
        self.assertEqual(capture.parent, self.L.captures)
        self.assertIn(u["id"], capture.read_text())

    def test_a_closed_unit_refuses_further_intake_until_reopened(self):
        self.ops.close_unit(1, "consumed", resolution="discrepancy")
        with self.assertRaises(m.LedgerError):
            self.ops.log_intake(1, 0.1, "g")
        self.ops.reopen(1, reason="closed it by mistake")
        self.ops.log_intake(1, 0.1, "g")
        self.assertEqual(self.reload()["status"], "active")


class TestOverdrawn(LedgerCase):
    def test_logging_past_the_opening_quantity_is_flagged_not_hidden(self):
        self.unit(qty=1, unit="g")
        self.ops.log_intake(1, 1.5, "g", "measured", occurred_at="2026-08-01 13:00")
        u = self.reload()
        self.assertTrue(u["analysis"]["overdrawn"])
        self.assertEqual(u["analysis"]["remaining"], 0.0)
        _, warnings = m.check(self.L)
        self.assertTrue(any("more logged against it" in w for w in warnings))

    def test_a_final_intake_cannot_be_used_to_paper_over_it(self):
        self.unit(qty=1, unit="g")
        self.ops.log_intake(1, 1.5, "g", "measured", occurred_at="2026-08-01 13:00")
        with self.assertRaises(m.LedgerError):
            self.ops.close_unit(1, "consumed", resolution="final_intake")


class TestChronology(LedgerCase):
    def test_an_event_before_the_unit_existed_withholds_the_figures(self):
        """A negative span is a wrong timestamp, not a short unit."""
        self.unit(at="2026-08-01 12:00")
        self.ops.log_intake(1, 0.2, "g", "measured", occurred_at="2026-07-30 10:00")
        a = self.reload()["analysis"]
        self.assertTrue(a["chronology_error"])
        self.assertIsNone(a["duration_seconds"])
        self.assertIsNone(a["rate_per_day"])
        _, warnings = m.check(self.L)
        self.assertTrue(any("before it was received" in w for w in warnings))


class TestProjection(LedgerCase):
    def test_it_rebuilds_identically_from_the_log_alone(self):
        self.unit()
        self.ops.log_intake(1, 0.2, "g", "measured", occurred_at="2026-08-01 13:00")
        self.ops.log_intake(1, descriptor="one line", occurred_at="2026-08-01 14:00")
        before = json.loads(self.L.units_path.read_text())["units"]
        self.L.units_path.unlink()
        after = self.L.write_projection()["units"]
        self.assertEqual(before, after)

    def test_a_hand_edited_projection_fails_the_gate(self):
        self.unit()
        self.L.units_path.write_text('{"event_count": 0, "units": []}')
        errors, _ = m.check(self.L)
        self.assertTrue(any("drifted" in e for e in errors))

    def test_the_log_is_append_only(self):
        self.unit()
        first = self.L.events_path.read_text()
        self.ops.log_intake(1, 0.2, "g", "measured", occurred_at="2026-08-01 13:00")
        self.assertTrue(self.L.events_path.read_text().startswith(first))


class TestGate(LedgerCase):
    def test_no_ledger_is_clean_and_silent(self):
        with tempfile.TemporaryDirectory() as blank:
            self.assertEqual(m.check(m.Ledger(blank)), ([], []))

    def test_a_torn_line_is_an_error_not_a_traceback(self):
        self.unit()
        with open(self.L.events_path, "a") as fh:
            fh.write('{"type": "intake_logged"\n')
        errors, _ = m.check(self.L)
        self.assertTrue(errors and "not JSON" in errors[0])

    def test_an_event_against_an_unknown_unit_is_an_error(self):
        self.unit()
        with open(self.L.events_path, "a") as fh:
            fh.write(json.dumps({"id": "x", "type": "intake_logged", "timestamp": "2026-08-01",
                                 "occurred_at": "2026-08-01", "unit_id": "nope",
                                 "data": {}, "source": {}}) + "\n")
        errors, _ = m.check(self.L)
        self.assertTrue(any("unknown unit" in e for e in errors))

    def test_it_warns_when_an_ignore_line_contradicts_a_tracked_ledger(self):
        """The check reversed with the decision, and this is what it reversed to.

        It used to fire when the data was NOT ignored, because the repository
        was public. The repository is private, those lines are gone on purpose,
        and warning about their absence on every run is how a gate becomes
        something people scroll past.

        The live risk is the other direction: an ignore line back in place while
        the file is here with data in it means somebody started reverting to
        public and stopped halfway — and by then the history already carries the
        ledger, so the ignore line is protecting nothing.

        Note what neither version could ever catch. `.gitignore` governs
        `git add`; the portal writes through GitHub's contents API from a
        browser and that API commits an ignored path without complaint. The
        guard for that path is in the portal, which reads the repository's
        visibility and refuses to sync while it is public.
        """
        self.unit()
        (self.L.root / ".gitignore").write_text("exports/\n")
        _, warnings = m.check(self.L)
        self.assertFalse(any("gitignore" in w for w in warnings),
                         "a private repo tracking its own ledger is the intended state")

        (self.L.root / ".gitignore").write_text("intake/events.jsonl\n")
        _, warnings = m.check(self.L)
        self.assertTrue(any("gitignore" in w for w in warnings),
                        "an ignore line over a ledger that is here with data in it")


class TestCrossUnit(LedgerCase):
    def test_stats_span_units_and_respect_measurement_coverage(self):
        self.unit(qty=2, unit="g", at="2026-08-01 12:00")
        self.ops.log_intake(1, 0.5, "g", "measured", occurred_at="2026-08-01 13:00")
        self.ops.log_intake(1, descriptor="one line", occurred_at="2026-08-01 14:00")
        self.ops.close_unit(1, "consumed", resolution="discrepancy",
                            closed_at="2026-08-01 20:00")
        self.unit(qty=2, unit="g", at="2026-08-10 12:00")
        self.ops.log_intake(2, 1.0, "g", "measured", occurred_at="2026-08-10 13:00")
        st = m.cross_stats(self.L.project())
        self.assertEqual(st["units"], 2)
        self.assertEqual(st["events"], 3)
        band = st["substances"][0]
        self.assertEqual(band["events"], 3)
        self.assertEqual(band["quantified"], 2)
        self.assertEqual(band["dose"]["n"], 2)
        self.assertEqual(band["under24"], 1)

    def test_filters_narrow_the_window(self):
        self.unit(at="2026-08-01 12:00")
        self.unit(at="2026-09-01 12:00")
        self.assertEqual(m.cross_stats(self.L.project(), since="2026-08-15")["units"], 1)
        self.assertIsNone(m.cross_stats(self.L.project(), substance="nicotine"))


class TestPhases(LedgerCase):
    def test_phases_are_cut_by_quantity_not_by_clock(self):
        """Four equal doses split 1 / 2 / 1 across the quartile bands."""
        self.unit(qty=4, unit="g")
        for hour in (13, 14, 15, 23):
            self.ops.log_intake(1, 1.0, "g", "measured", occurred_at=f"2026-08-01 {hour}:00")
        phases = self.reload()["analysis"]["phases"]
        self.assertEqual([p["events"] for p in phases], [1, 2, 1])
        self.assertEqual(sum(p["quantity"] for p in phases), 4.0)


class TestCrossOriginBoundary(unittest.TestCase):
    """The one cross-origin hole in the local app, pinned shut.

    ボスの部屋 (boss.html, in the leviathan site) renders this ledger from
    another origin, so `/api/intake*` has to answer one. That is a security
    boundary and it gets tests: an allowlist rather than a wildcard, localhost
    always, everything else refused, and — the one that would be silent if it
    broke — *no other path on this server* answering a foreign origin at all.
    """

    def setUp(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("wapp", os.path.join(ROOT, "app.py"))
        self.app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.app)

    def test_the_site_origin_is_allowed(self):
        self.assertEqual(self.app.intake_cors_origin("https://caakehorn.github.io"),
                         "https://caakehorn.github.io")

    def test_localhost_is_always_allowed(self):
        for o in ("http://127.0.0.1:8099", "http://localhost:3000"):
            self.assertEqual(self.app.intake_cors_origin(o), o)

    def test_everything_else_is_refused(self):
        for o in ("https://evil.example", "https://caakehorn.github.io.evil.example",
                  "null", "", None):
            self.assertIsNone(self.app.intake_cors_origin(o))

    def test_it_is_never_a_wildcard(self):
        self.assertNotIn("*", self.app.DEFAULT_INTAKE_ORIGINS)
        with open(os.path.join(ROOT, "app.py"), encoding="utf-8") as fh:
            src = fh.read()
        self.assertNotIn('"Access-Control-Allow-Origin", "*"', src)
        # Credentials are never allowed: an allowlisted origin gets to call the
        # endpoints, never to ride along on anything this browser already holds.
        self.assertNotIn("Access-Control-Allow-Credentials", src)

    def test_the_env_var_can_close_it_completely(self):
        old = os.environ.get("WIKI_INTAKE_ORIGINS")
        os.environ["WIKI_INTAKE_ORIGINS"] = ""
        try:
            self.assertIsNone(self.app.intake_cors_origin("https://caakehorn.github.io"))
            # localhost still works, so Special:Intake and the CLI are unaffected
            self.assertIsNotNone(self.app.intake_cors_origin("http://127.0.0.1:8477"))
        finally:
            if old is None:
                del os.environ["WIKI_INTAKE_ORIGINS"]
            else:
                os.environ["WIKI_INTAKE_ORIGINS"] = old

    def test_only_the_intake_paths_carry_the_headers(self):
        """cors() returns early on every other route — the wiki, capture, git
        sync and the file reader all stay strictly same-origin."""
        with open(os.path.join(ROOT, "app.py"), encoding="utf-8") as fh:
            src = fh.read()
        block = re.search(r"def cors\(self\):(.*?)def do_OPTIONS", src, re.S).group(1)
        self.assertIn('self.path.startswith("/api/intake")', block)
        self.assertIn("return", block.split("\n")[3])


class TestContract(unittest.TestCase):
    def test_help_runs(self):
        import subprocess
        out = subprocess.run([sys.executable, SCRIPT, "--help"], capture_output=True,
                             text=True, cwd=ROOT)
        self.assertEqual(out.returncode, 0, out.stderr)
        for cmd in ("new", "log", "close", "report", "stats", "check", "rebuild"):
            self.assertIn(cmd, out.stdout)

    def test_the_app_and_the_cli_share_one_implementation(self):
        """Special:Intake must import bin/intake, never restate its arithmetic."""
        with open(os.path.join(ROOT, "app.py"), encoding="utf-8") as fh:
            src = fh.read()
        self.assertIn('SourceFileLoader("intake_ledger"', src)
        self.assertIn("def intake_action(", src)


if __name__ == "__main__":
    unittest.main()
