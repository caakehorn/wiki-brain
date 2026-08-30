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
from pathlib import Path
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

    def test_it_warns_when_the_data_is_not_gitignored(self):
        """The repository is public; an un-ignored ledger is one `git add` away.

        This check was briefly reversed — made to fire when the data WAS ignored
        — on the stated ground that the repository had been made private. It had
        not been: an anonymous read of the GitHub API on 2026-08-30 returned
        `private: false`, `visibility: public`. So the direction here follows the
        guard in `.gitignore`, and that guard follows a visibility somebody
        actually checked rather than one the docs asserted.

        The failure this catches is not hypothetical. On the same day, in a
        session that had deliberately emptied the ledger and was watching for
        exactly this, a routine `git add -A` still staged `events.jsonl` and
        `units.json` the moment the ignore lines were absent.

        Note what it cannot catch, because it is easy to trust too far.
        `.gitignore` governs `git add`, so this covers the CLI and the local app.
        GitHub's contents API ignores it completely, and that is how the portal
        writes from a browser; that path is guarded in the portal, which reads
        the repository's visibility and refuses to sync while it is public.
        """
        self.unit()
        (self.L.root / ".gitignore").write_text("exports/\n")
        _, warnings = m.check(self.L)
        self.assertTrue(any("NOT in .gitignore" in w for w in warnings),
                        "a public repo holding an un-ignored ledger is the live risk")

        (self.L.root / ".gitignore").write_text("intake/events.jsonl\n")
        _, warnings = m.check(self.L)
        self.assertFalse(any("gitignore" in w for w in warnings),
                         "guarded is the intended state and must stay quiet")

    def test_the_repo_ships_the_guard_it_documents(self):
        """The real `.gitignore` carries all three paths, not just the log."""
        text = (Path(ROOT) / ".gitignore").read_text(encoding="utf-8")
        for path in ("intake/events.jsonl", "intake/units.json", "raw/health/intake/"):
            self.assertIn(path, text, f"{path} is not guarded")


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


class TestPresets(LedgerCase):
    """One tap, and it still cannot lie about what kind of number it produced."""

    def test_a_preset_logs_as_an_estimate_never_a_measurement(self):
        """Nobody weighed a line. The type has to say so."""
        self.ops.new_unit("cocaine", 3.5, "g", "2026-08-01 12:00")
        ev, u = self.ops.log_preset(1, "line", occurred_at="2026-08-01 13:00")
        self.assertEqual(ev["data"]["measurement_type"], "estimated")
        self.assertEqual(ev["data"]["quantity"], 0.1)
        self.assertEqual(u["analysis"]["events"]["measured"], 0)
        self.assertEqual(u["analysis"]["events"]["estimated"], 1)

    def test_the_confidence_records_how_wide_the_spread_is(self):
        self.ops.new_unit("cannabis", 3.5, "g", "2026-08-01 12:00")
        ev, _ = self.ops.log_preset(1, "one-hitter", occurred_at="2026-08-01 13:00")
        self.assertEqual(ev["data"]["confidence"], "medium")   # a fixed bowl repeats
        self.ops.new_unit("cocaine", 3.5, "g", "2026-08-01 12:00")
        ev2, _ = self.ops.log_preset(2, "line", occurred_at="2026-08-01 13:00")
        self.assertEqual(ev2["data"]["confidence"], "low")     # a line does not

    def test_the_note_travels_onto_the_event(self):
        """The cigarette figure is content, not dose, and every row says so."""
        self.ops.new_unit("nicotine", 240, "mg", "2026-08-01 12:00")
        ev, _ = self.ops.log_preset(1, "cigarette", occurred_at="2026-08-01 13:00")
        note = ev["data"]["note"]
        self.assertIn("CONTENT", note)
        self.assertIn("1-1.5 mg", note)

    def test_a_pack_of_twenty_depletes_exactly(self):
        """20 cigarettes at 12 mg content is a 240 mg unit, to the milligram.

        This is why the preset carries content rather than absorbed dose: a pack
        has to be able to run out. Logging ~1.2 mg of absorbed nicotine against
        it twenty times would leave 216 mg in an empty box.
        """
        self.ops.new_unit("nicotine", 240, "mg", "2026-08-01 12:00")
        for i in range(20):
            self.ops.log_preset(1, "cigarette", occurred_at=f"2026-08-01 {12 + i % 12}:00")
        a = self.reload()["analysis"]
        self.assertAlmostEqual(a["quantified_total"], 240)
        self.assertAlmostEqual(a["remaining"], 0)
        rec = self.ops.reconciliation(self.reload())
        self.assertFalse(rec["needs_answer"])

    def test_a_users_note_is_kept_alongside_the_presets(self):
        self.ops.new_unit("caffeine", 900, "mg", "2026-08-01 12:00")
        ev, _ = self.ops.log_preset(1, "coffee", note="second one, bad night")
        self.assertIn("second one, bad night", ev["data"]["note"])
        self.assertIn("95-165 mg", ev["data"]["note"])

    def test_a_preset_from_another_substance_is_refused(self):
        self.ops.new_unit("cannabis", 3.5, "g", "2026-08-01 12:00")
        with self.assertRaises(m.LedgerError) as ctx:
            self.ops.log_preset(1, "cigarette")
        self.assertIn("one-hitter", str(ctx.exception))

    def test_a_substance_with_no_presets_says_so(self):
        self.ops.new_unit("buprenorphine", 8, "mg", "2026-08-01 12:00")
        with self.assertRaises(m.LedgerError) as ctx:
            self.ops.log_preset(1, "anything")
        self.assertIn("no presets", str(ctx.exception))

    def test_presets_can_be_named_by_label_too(self):
        self.ops.new_unit("caffeine", 900, "mg", "2026-08-01 12:00")
        ev, _ = self.ops.log_preset(1, "A COFFEE")
        self.assertEqual(ev["data"]["quantity"], 150)


class TestCoverageWording(unittest.TestCase):
    """The line answers two questions, and the second one was missing.

    A table logged entirely by one-tap presets has full coverage and not a
    single measurement on it. The old wording said "all N events carry a
    quantity" and stopped, which reads as reassurance for a column that is
    entirely estimates — the exact shape of false confidence this ledger exists
    to refuse. Presets made it common, so it is pinned here.

    `js/boss-web.js` mirrors this string exactly and a cross-implementation
    check compares the two, so a change here is a change there.
    """

    @staticmethod
    def a(total, measured, estimated, unquantified):
        return {"events": {"total": total, "measured": measured, "estimated": estimated,
                           "unquantified": unquantified, "voided": 0},
                "coverage": (measured + estimated) / total if total else None}

    def test_all_estimates_never_reads_as_reassurance(self):
        line = m.coverage_line(self.a(4, 0, 4, 0))
        self.assertIn("none was weighed", line)
        self.assertIn("all 4 are estimates", line)

    def test_a_mix_names_both_halves(self):
        line = m.coverage_line(self.a(3, 1, 1, 1))
        self.assertIn("2 of 3", line)
        self.assertIn("1 weighed, 1 estimated", line)

    def test_all_weighed_says_so(self):
        self.assertIn("every one weighed", m.coverage_line(self.a(5, 5, 0, 0)))

    def test_the_singular_reads_like_english(self):
        self.assertEqual(m.coverage_line(self.a(1, 1, 0, 0)),
                         "the one event carries a quantity, and it was weighed")
        self.assertIn("it is an estimate", m.coverage_line(self.a(1, 0, 1, 0)))

    def test_nothing_logged(self):
        self.assertEqual(m.coverage_line(self.a(0, 0, 0, 0)), "no events logged")


class TestShippedCatalog(unittest.TestCase):
    """The five the operator named, and the presets they carry."""

    def test_the_catalog_is_the_five(self):
        ids = {s["id"] for s in m.DEFAULT_SUBSTANCES}
        self.assertEqual(ids, {"cocaine", "cannabis", "nicotine", "caffeine", "buprenorphine"})

    def test_the_units_are_the_ones_asked_for(self):
        want = {"cocaine": "g", "cannabis": "g", "nicotine": "mg",
                "caffeine": "mg", "buprenorphine": "mg"}
        got = {s["id"]: s["default_unit"] for s in m.DEFAULT_SUBSTANCES}
        self.assertEqual(got, want)

    def test_the_four_presets_carry_the_agreed_quantities(self):
        want = {"line": (0.1, "g"), "one-hitter": (0.05, "g"),
                "cigarette": (12, "mg"), "coffee": (150, "mg")}
        got = {p["id"]: (p["quantity"], p["unit"])
               for s in m.DEFAULT_SUBSTANCES for p in s.get("presets", [])}
        self.assertEqual(got, want)

    def test_every_preset_is_an_estimate(self):
        """If one ever ships as `measured`, the whole coverage figure is a lie."""
        for s in m.DEFAULT_SUBSTANCES:
            for p in s.get("presets", []):
                with self.subTest(preset=p["id"]):
                    self.assertEqual(p["measurement_type"], "estimated")
                    self.assertIn(p["confidence"], ("high", "medium", "low"))

    def test_the_shipped_file_matches_the_defaults(self):
        import json
        with open(os.path.join(ROOT, "intake", "substances.json"), encoding="utf-8") as fh:
            shipped = json.load(fh)["substances"]
        self.assertEqual({s["id"] for s in shipped},
                         {s["id"] for s in m.DEFAULT_SUBSTANCES})
        by_id = {s["id"]: s for s in shipped}
        for d in m.DEFAULT_SUBSTANCES:
            with self.subTest(substance=d["id"]):
                self.assertEqual(by_id[d["id"]].get("presets", []), d.get("presets", []))


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
