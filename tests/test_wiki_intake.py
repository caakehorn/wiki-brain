#!/usr/bin/env python3
"""Tests for bin/wiki-intake, the analysis side of the intake ledger.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

The ledger is written by `/ledger` in caakehorn/home and read here, and the two
implementations share no code on purpose — a contract held by a shared helper is
not tested by two programs using the helper. What tests it is two independent
folds of the same log agreeing on the same numbers.

So the fixture below is deliberately **the same worked unit** that
`scripts/check-ledger.mjs` asserts over in the other repository, with the same
expected figures written out literally:

    3.5 g, four measured doses (0.18 0.22 0.31 0.14), one estimate (0.20),
    one event logged without a figure, one dose logged twice and voided, one
    entered as 0.5 g and corrected to 0.05 g, and 0.1 g spilled.

    → 0.90 g measured · 1.10 g quantified · 2.30 g unaccounted
    → mean quantified dose 1.10 ÷ 6, and NOT 3.5 ÷ 7

If these two files ever disagree, one of the folds is wrong and the dataset is
not worth what it claims to be worth. That is the whole reason both exist.

The refusals are tested as refusals — each one stated as the thing that must NOT
happen — because every one of them is a failure that produces a plausible number
rather than an error.

The real corpus is never touched: each case writes a shard into a temp directory
and points the module's DIR at it.
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# bin/wiki-intake has no .py extension, so it is loaded by path the same way the
# other tool tests in this directory load theirs.
_spec = importlib.util.spec_from_loader(
    "wiki_intake",
    importlib.machinery.SourceFileLoader("wiki_intake", os.path.join(ROOT, "bin", "wiki-intake")),
)
wiki_intake = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wiki_intake)


SOURCE = {"app": "home", "tool": "intake-ledger", "v": 1}
UNIT = "unit_TESTFIXTURE00000000000000"


def _events():
    """The worked unit, in log order. Mirrors scripts/check-ledger.mjs."""
    rows = []
    n = [0]

    def add(**event):
        # `loggedAt` must increase strictly. The log is folded in that order so
        # that a correction lands after what it corrects, and a fixture whose
        # stamps wrap around the hour makes a void arrive before its target and
        # read as an orphan — which is exactly the bug the ordering prevents in
        # production, found here by writing the fixture carelessly first.
        n[0] += 1
        hour, minute = divmod(n[0] * 3, 60)
        stamp = f"2026-08-29T{10 + hour:02d}:{minute:02d}:00-04:00"
        rows.append({
            "id": f"evt_TESTFIXTURE{n[0]:014d}",
            "loggedAt": stamp,
            "source": SOURCE,
            **event,
        })
        return rows[-1]

    add(type="unit_opened", unit=UNIT, substance="cocaine", quantity=3.5, uom="g",
        receivedAt="2026-08-29T09:42:00-04:00")
    for q in (0.18, 0.22, 0.31, 0.14):
        add(type="intake_logged", unit=UNIT, occurredAt=f"2026-08-29T1{len(rows)}:00:00-04:00",
            measurement="measured", quantity=q, uom="g")
    add(type="intake_logged", unit=UNIT, occurredAt="2026-08-29T15:30:00-04:00",
        measurement="estimated", quantity=0.2, uom="g", confidence="medium")
    add(type="intake_logged", unit=UNIT, occurredAt="2026-08-29T16:10:00-04:00",
        measurement="unquantified", descriptor="one line")
    doubled = add(type="intake_logged", unit=UNIT, occurredAt="2026-08-29T16:15:00-04:00",
                  measurement="measured", quantity=0.2, uom="g")
    slipped = add(type="intake_logged", unit=UNIT, occurredAt="2026-08-29T17:25:00-04:00",
                  measurement="measured", quantity=0.5, uom="g")
    add(type="intake_voided", target=doubled["id"], reason="double tap on the log button")
    add(type="intake_corrected", target=slipped["id"], reason="decimal entry error",
        patch={"quantity": 0.05})
    add(type="unit_adjusted", unit=UNIT, occurredAt="2026-08-29T17:35:00-04:00",
        quantity=0.1, uom="g", direction="out", kind="spill", reason="knocked the tray")
    return rows


class LedgerCase(unittest.TestCase):
    """A temp `data/intake/` holding whatever the case needs."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.saved = wiki_intake.DIR
        wiki_intake.DIR = self.dir
        self.addCleanup(self.restore)

    def restore(self):
        wiki_intake.DIR = self.saved
        shutil.rmtree(self.dir, ignore_errors=True)

    def write(self, events, shard="events-2026-08.jsonl"):
        with open(os.path.join(self.dir, shard), "w", encoding="utf-8") as handle:
            for event in events:
                handle.write(json.dumps(event) + "\n")

    def fold(self, events=None):
        self.write(events if events is not None else _events())
        rows, problems = wiki_intake.load(self.dir)
        self.assertEqual(problems, [], "the fixture should parse cleanly")
        units, orphans = wiki_intake.project(rows)
        self.assertEqual(orphans, [])
        return units[0]


class TestTheWorkedUnit(LedgerCase):
    def test_counts_the_live_events_only(self):
        unit = self.fold()
        # 4 measured + 1 estimated + 1 unquantified + 1 corrected = 7 live.
        self.assertEqual(unit["tally"]["events"], 7)
        self.assertEqual(unit["tally"]["voided"], 1)
        self.assertEqual(unit["tally"]["unquantified"], 1)

    def test_totals_match_the_other_implementation(self):
        t = self.fold()["tally"]
        self.assertAlmostEqual(t["measuredQuantity"], 0.90, places=9)
        self.assertAlmostEqual(t["quantifiedQuantity"], 1.10, places=9)
        self.assertAlmostEqual(t["adjustedOut"], 0.10, places=9)

    def test_a_correction_replaces_the_figure_and_keeps_the_original(self):
        unit = self.fold()
        corrected = [i for i in unit["intakes"] if i["corrections"]][0]
        self.assertEqual(corrected["quantity"], 0.05)
        self.assertEqual(corrected["corrections"][0]["before"]["quantity"], 0.5)
        self.assertEqual(corrected["corrections"][0]["reason"], "decimal entry error")

    def test_a_voided_event_stays_in_the_log(self):
        unit = self.fold()
        voided = [i for i in unit["intakes"] if i["voided"]]
        self.assertEqual(len(voided), 1)
        self.assertEqual(len(wiki_intake.live(unit)), 7)


class TestTheRefusals(LedgerCase):
    """Each of these is a plausible wrong number this tool must not produce."""

    def test_the_remainder_is_a_bound_not_a_figure(self):
        t = self.fold()["tally"]
        # 3.5 − 1.10 quantified − 0.10 spilled = 2.30, and it is a ceiling: the
        # event logged without a figure took an unknown positive amount.
        self.assertAlmostEqual(t["remainingAtMost"], 2.30, places=9)
        self.assertFalse(t["remainingExact"])

    def test_the_bound_is_exact_only_with_nothing_untallied(self):
        events = [e for e in _events() if e.get("measurement") != "unquantified"]
        self.assertTrue(self.fold(events)["tally"]["remainingExact"])

    def test_the_mean_dose_is_never_the_unit_over_the_event_count(self):
        unit = self.fold()
        amounts = [a for _, a in wiki_intake.doses(unit)]
        self.assertEqual(len(amounts), 6)
        mean = sum(amounts) / len(amounts)
        self.assertAlmostEqual(mean, 1.10 / 6, places=9)
        # The number a careless fold produces: 3.5 ÷ 7 = 0.5.
        self.assertNotAlmostEqual(mean, 3.5 / 7, places=3)

    def test_an_unquantified_event_counts_but_never_sums(self):
        unit = self.fold()
        without = [i for i in unit["intakes"] if i["measurement"] == "unquantified"][0]
        self.assertIsNone(without["quantity"])
        self.assertIn(without, wiki_intake.live(unit))
        self.assertEqual(unit["tally"]["measured"] + unit["tally"]["estimated"], 6)

    def test_an_unconvertible_dose_is_counted_named_and_excluded(self):
        events = _events()[:1] + [{
            "id": "evt_TESTFIXTUREMIXED0000000000",
            "type": "intake_logged",
            "loggedAt": "2026-08-29T18:00:00-04:00",
            "unit": UNIT,
            "occurredAt": "2026-08-29T18:00:00-04:00",
            "measurement": "measured",
            "quantity": 2,
            "uom": "tab",
            "source": SOURCE,
        }]
        t = self.fold(events)["tally"]
        self.assertEqual(t["events"], 1)
        self.assertEqual(t["quantifiedQuantity"], 0.0)
        self.assertEqual(t["unconvertible"], 1)
        self.assertFalse(t["remainingExact"])


class TestValidation(LedgerCase):
    def test_refuses_what_the_projection_would_have_to_guess(self):
        base = {"id": "evt_x", "loggedAt": "2026-08-29T13:42:00-04:00", "source": SOURCE}
        bad = [
            ({**base, "type": "intake_logged", "unit": UNIT,
              "occurredAt": base["loggedAt"], "measurement": "unquantified", "quantity": 0.2},
             "an unquantified intake may not carry a quantity"),
            ({**base, "type": "intake_logged", "unit": UNIT,
              "occurredAt": base["loggedAt"], "measurement": "measured", "quantity": 0.2},
             "a quantified intake must carry a uom"),
            ({**base, "type": "intake_logged", "unit": UNIT, "occurredAt": "2026-08-29 13:42",
              "measurement": "measured", "quantity": 0.2, "uom": "g"},
             "an instant without an offset"),
            ({**base, "type": "intake_corrected", "target": "evt_y", "patch": {"quantity": 1}},
             "a correction without a reason"),
            ({**base, "type": "unit_opened", "unit": UNIT, "substance": "x",
              "quantity": -1, "uom": "g", "receivedAt": base["loggedAt"]},
             "a negative quantity"),
        ]
        for event, why in bad:
            with self.subTest(why=why):
                self.assertIsNotNone(wiki_intake.validate(event), why)

    def test_accepts_the_fixture(self):
        for event in _events():
            self.assertIsNone(wiki_intake.validate(event), event["type"])

    def test_a_corrupt_line_is_named_not_swallowed(self):
        path = os.path.join(self.dir, "events-2026-08.jsonl")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write("{not json\n")
            handle.write(json.dumps(_events()[0]) + "\n")
        events, problems = wiki_intake.load(self.dir)
        self.assertEqual(len(events), 1)
        self.assertEqual(len(problems), 1)
        self.assertIn("not JSON", problems[0])

    def test_a_duplicated_line_is_collapsed_by_id(self):
        rows = _events()
        self.write(rows + [rows[1]])
        events, problems = wiki_intake.load(self.dir)
        self.assertEqual(problems, [])
        self.assertEqual(len(events), len(rows))


class TestUnitsOfMeasure(unittest.TestCase):
    def test_conversions(self):
        self.assertEqual(wiki_intake.convert(3.5, "g", "mg"), 3500)
        self.assertAlmostEqual(wiki_intake.convert(1, "oz", "g"), 28.349523125, places=9)
        self.assertEqual(wiki_intake.convert(3, "tab", "ct"), 3)

    def test_dimensions_never_mix(self):
        self.assertIsNone(wiki_intake.convert(1, "g", "ml"))
        self.assertIsNone(wiki_intake.convert(1, "g", "tab"))
        self.assertIsNone(wiki_intake.convert(1, "tab", "cap"))


class TestOverdrawnUnits(LedgerCase):
    def test_the_log_claiming_more_than_the_unit_held_is_a_finding(self):
        """Not clamped to zero: it means a dose was double-logged, or the
        initial weight was wrong, and that is worth surfacing."""
        events = _events()[:1] + [{
            "id": "evt_TESTFIXTUREOVER00000000000",
            "type": "intake_logged",
            "loggedAt": "2026-08-29T18:00:00-04:00",
            "unit": UNIT,
            "occurredAt": "2026-08-29T18:00:00-04:00",
            "measurement": "measured",
            "quantity": 9,
            "uom": "g",
            "source": SOURCE,
        }]
        t = self.fold(events)["tally"]
        self.assertEqual(t["remainingAtMost"], 0.0)
        self.assertAlmostEqual(t["unaccounted"], -5.5, places=9)


class TestTime(LedgerCase):
    def test_the_local_hour_survives_the_offset(self):
        # 03:40-04:00 is 07:40Z. The local hour is 3, and that is the fact the
        # dataset is actually asked for.
        self.assertEqual(wiki_intake.local_hour("2026-08-29T03:40:00-04:00"), 3)
        self.assertEqual(wiki_intake.local_hour("2026-08-29T07:40:00Z"), 7)

    def test_the_densest_window_straddles_midnight(self):
        times = ["2026-08-30T23:00:00-04:00", "2026-08-30T23:40:00-04:00",
                 "2026-08-31T01:10:00-04:00", "2026-08-31T03:50:00-04:00",
                 "2026-08-31T14:00:00-04:00"]
        self.assertEqual(wiki_intake.densest_window(times, 6)["events"], 4)


if __name__ == "__main__":
    unittest.main()
