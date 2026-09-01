#!/usr/bin/env python3
"""Tests for bin/wiki-check, the mechanical housekeeping chain.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

The value of this script is entirely in two properties that are easy to break
and invisible when broken, so both are pinned here:

  * **Order.** Generators run before gates, and the scan runs last. Get this
    backwards and `bin/wiki-lint` inspects index counts that are about to
    change while `bin/wiki-freshness` asks a question whose answer is
    guaranteed stale — which is exactly the drift the chain exists to catch.
  * **--check-only writes nothing.** It is the mode CI and a reviewer use, and
    a mode that quietly regenerated would turn "is what is committed
    consistent?" into "it is now."

The chain is not executed here — that would run the real gates over the real
corpus and take seconds per test while coupling this file to the wiki's current
contents. The step tables are declarative, so they are read from source instead.
"""
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "bin", "wiki-check")


def load():
    """bin/wiki-check has no .py extension; read it as text."""
    with open(SCRIPT, encoding="utf-8") as fh:
        return fh.read()


def steps(source, name):
    """Pull the tool names out of one declarative step table."""
    block = re.search(rf"^{name} = \[(.*?)^\]", source, re.S | re.M)
    assert block, f"step table {name} not found"
    return re.findall(r'\(\["([a-z-]+)"', block.group(1))


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.src = load()

    def test_generators_precede_gates(self):
        """wiki-lint checks index drift; digest must have run first."""
        gen, gate = steps(self.src, "GENERATE"), steps(self.src, "GATE")
        self.assertIn("wiki-digest", gen)
        self.assertIn("llm-publish", gen)
        self.assertIn("wiki-timeline", gen)
        self.assertIn("wiki-lint", gate)
        self.assertNotIn("wiki-lint", gen)

    def test_timeline_generate_precedes_digest_and_publish(self):
        """wiki-timeline writes a wiki page; digest counts it and llm-publish copies it."""
        gen = steps(self.src, "GENERATE")
        self.assertLess(gen.index("wiki-timeline"), gen.index("wiki-digest"))
        self.assertLess(gen.index("wiki-timeline"), gen.index("llm-publish"))

    def test_freshness_is_a_gate_not_a_generator(self):
        """It reports drift and writes nothing — it must never be in GENERATE."""
        self.assertIn("wiki-freshness", steps(self.src, "GATE"))
        self.assertNotIn("wiki-freshness", steps(self.src, "GENERATE"))

    def test_all_three_gates_present(self):
        gate = steps(self.src, "GATE")
        for tool in ("wiki-lint", "wiki-connect", "wiki-climb"):
            self.assertIn(tool, gate, f"{tool} missing from the gate chain")

    def test_scan_runs_last(self):
        """WORK.md is recomputed after the repo has settled, not before."""
        self.assertEqual(steps(self.src, "SCAN"), ["wiki-work"])


class TestCheckOnly(unittest.TestCase):
    def setUp(self):
        self.src = load()

    def test_check_only_selects_gates_alone(self):
        """The read-only mode must not pick up a step marked as writing."""
        self.assertRegex(
            self.src, r"steps = list\(GATE\) if args\.check_only else GENERATE \+ GATE \+ SCAN"
        )

    def test_no_gate_step_claims_to_write(self):
        """Every GATE entry carries writes=False, so --check-only is safe."""
        block = re.search(r"^GATE = \[(.*?)^\]", self.src, re.S | re.M).group(1)
        self.assertNotIn("True", block, "a gate step is flagged as writing")


class TestContract(unittest.TestCase):
    def test_help_runs_and_documents_both_modes(self):
        out = subprocess.run(
            [sys.executable, SCRIPT, "--help"], capture_output=True, text=True, cwd=ROOT
        )
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("--check-only", out.stdout)
        self.assertIn("--quiet", out.stdout)

    def test_is_executable(self):
        self.assertTrue(os.access(SCRIPT, os.X_OK), "bin/wiki-check is not executable")


if __name__ == "__main__":
    unittest.main(verbosity=2)
