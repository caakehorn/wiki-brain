"""Tests for bin/wiki-secrets — the credential scan on what is about to be committed.

Two properties matter and both are about NOT being switched off:

  * it must catch the real shapes, in the diff and in untracked files;
  * it must NOT scan the tree, because raw/ holds 130,000 received messages and
    a corpus that size contains key-shaped strings that are not keys. A gate
    that fires on immutable archive material gets disabled, and a disabled gate
    protects nothing.

It must also never print a credential it found — this output lands in CI logs.
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOL = ROOT / "bin" / "wiki-secrets"


class Sandbox(unittest.TestCase):
    def setUp(self):
        import shutil
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        (self.tmp / "bin").mkdir()
        (self.tmp / "bin" / "wiki-secrets").write_text(
            TOOL.read_text(encoding="utf-8"), encoding="utf-8")
        self._git("init", "-q", ".")
        self._git("commit", "-q", "--allow-empty", "-m", "init")

    def _git(self, *a):
        return subprocess.run(["git", *a], cwd=self.tmp, capture_output=True,
                              text=True)

    def run_tool(self, *a):
        return subprocess.run([sys.executable,
                               str(self.tmp / "bin" / "wiki-secrets"), *a],
                              cwd=self.tmp, capture_output=True, text=True)


class CatchesRealShapes(Sandbox):
    CASES = {
        "github": "ghp_" + "a" * 36,
        "aws": "AKIA" + "B" * 16,
        "slack": "xoxb-" + "1" * 20,
        "google": "AIza" + "c" * 35,
        "openai": "sk-" + "d" * 30,
    }

    def test_each_shape_in_an_untracked_file(self):
        for name, value in self.CASES.items():
            with self.subTest(shape=name):
                f = self.tmp / f"{name}.md"
                f.write_text(f"key = {value}\n", encoding="utf-8")
                r = self.run_tool("check")
                self.assertEqual(r.returncode, 1, f"{name} not caught: {r.stdout}")
                f.unlink()

    def test_shape_in_a_tracked_modification(self):
        f = self.tmp / "page.md"
        f.write_text("clean\n", encoding="utf-8")
        self._git("add", "page.md")
        self._git("commit", "-q", "-m", "add")
        f.write_text("token = ghp_" + "a" * 36 + "\n", encoding="utf-8")
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 1, r.stdout)

    def test_never_prints_the_credential(self):
        secret = "ghp_" + "z" * 36
        (self.tmp / "leak.md").write_text(f"k={secret}\n", encoding="utf-8")
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 1)
        self.assertNotIn(secret, r.stdout + r.stderr,
                         "the finding must be redacted — this lands in CI logs")


class DoesNotScanTheTree(Sandbox):
    def test_already_committed_material_is_not_relitigated(self):
        """The design decision that keeps this gate switched on."""
        f = self.tmp / "archive.md"
        f.write_text("historical string ghp_" + "a" * 36 + "\n", encoding="utf-8")
        self._git("add", "archive.md")
        self._git("commit", "-q", "-m", "archived")
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 0,
                         "committed material must not fire the gate — a gate "
                         "that fires on immutable raw/ archive gets disabled")

    def test_clean_tree_is_clean(self):
        r = self.run_tool("check")
        self.assertEqual(r.returncode, 0, r.stdout)


class RealRepo(unittest.TestCase):
    def test_gates_clean_here(self):
        r = subprocess.run([sys.executable, str(TOOL), "check"], cwd=ROOT,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
