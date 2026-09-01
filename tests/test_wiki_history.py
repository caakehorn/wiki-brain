#!/usr/bin/env python3
"""Tests for bin/wiki-history — the log reader and the date gate.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

These build real git repositories in a temp directory rather than mocking the
log, because every interesting thing this tool does is a question about what git
actually reports: how a rename appears in `--name-status -M`, what a delete
looks like, which of `git status --porcelain`'s shapes name a path. A fake log
would agree with whatever this file believes about git, which is the belief
under test.

THE GATE IS THE POINT, AND ITS EXEMPTIONS ARE THE POINT OF THE GATE. Two of them
are load-bearing and both have a test here:

  * A page edited in the working tree is exempt. A session mid-pass has bumped
    `date_modified` for a commit it has not made yet, so the date is ahead of the
    log by construction. Without the exemption the gate fires on every honest run
    and gets removed.
  * A date BEHIND the log is not an error. A link cleanup across forty pages
    moves none of them, and those pages are right not to have bumped.
"""
import importlib.machinery
import importlib.util
import io
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "bin", "wiki-history")


def load_module():
    """bin/wiki-history has no .py extension, and no import-time side effects."""
    spec = importlib.util.spec_from_loader(
        "wiki_history", importlib.machinery.SourceFileLoader("wiki_history", SCRIPT)
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


wh = load_module()

PAGE = """---
title: "{title}"
page_type: synthesis
date_modified: {modified}
---

# {title}

{body}
"""


class Repo:
    """A throwaway git repository with a wiki/ tree in it."""

    def __init__(self, path):
        self.path = path
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "t@example.com")
        self.git("config", "user.name", "Tester")

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", self.path, *args], capture_output=True, text=True, check=True
        ).stdout

    def write(self, slug, *, title="A Page", modified="2026-01-01", body="text"):
        full = os.path.join(self.path, "wiki", f"{slug}.md")
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(PAGE.format(title=title, modified=modified, body=body))

    def commit(self, subject, when="2026-02-01T12:00:00+00:00"):
        self.git("add", "-A")
        env = dict(os.environ, GIT_AUTHOR_DATE=when, GIT_COMMITTER_DATE=when)
        subprocess.run(
            ["git", "-C", self.path, "commit", "-q", "-m", subject],
            check=True,
            env=env,
            capture_output=True,
        )


class Fixture(unittest.TestCase):
    """Points the module's module-level ROOT/WIKI at a temp repo for one test."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Repo(self.tmp.name)
        self._root, self._wiki = wh.ROOT, wh.WIKI
        wh.ROOT = self.tmp.name
        wh.WIKI = os.path.join(self.tmp.name, "wiki")

    def tearDown(self):
        wh.ROOT, wh.WIKI = self._root, self._wiki
        self.tmp.cleanup()

    def check(self):
        """Run the gate, returning (exit code, what it printed)."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = wh.cmd_check(None)
        return code, buf.getvalue()


class TestHistory(Fixture):
    def test_one_commit_is_one_revision(self):
        self.repo.write("mind/a")
        self.repo.commit("ingest: a")
        revs = wh.history()
        self.assertEqual(list(revs), ["wiki/mind/a.md"])
        self.assertEqual(len(revs["wiki/mind/a.md"]), 1)

    def test_revisions_come_back_newest_first(self):
        self.repo.write("mind/a", body="one")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        self.repo.write("mind/a", body="two")
        self.repo.commit("climb: a", when="2026-03-01T12:00:00+00:00")
        revs = wh.history()["wiki/mind/a.md"]
        self.assertEqual([r[3] for r in revs], ["climb: a", "ingest: a"])

    def test_a_rename_keeps_the_history_under_the_new_name(self):
        self.repo.write("mind/old", body="x" * 400)
        self.repo.commit("ingest: old")
        self.repo.git("mv", "wiki/mind/old.md", "wiki/mind/new.md")
        self.repo.commit("lint: rename")
        revs = wh.history()
        self.assertNotIn("wiki/mind/old.md", revs)
        self.assertEqual(len(revs["wiki/mind/new.md"]), 2)
        # The older revision remembers where the file actually was, which is what
        # makes `<sha>:<path>` resolve for it.
        self.assertEqual(revs["wiki/mind/new.md"][1][5], "wiki/mind/old.md")

    def test_a_delete_is_not_counted_as_a_version(self):
        """There is no file at that commit to show, and the portal's derivation
        drops it too. Two readings of one log must not disagree on a count."""
        self.repo.write("mind/a")
        self.repo.commit("ingest: a")
        os.remove(os.path.join(self.tmp.name, "wiki", "mind", "a.md"))
        self.repo.commit("delete: a")
        self.assertEqual(len(wh.history().get("wiki/mind/a.md", [])), 1)

    def test_the_operation_is_read_off_the_subject(self):
        self.assertEqual(wh.op_of("ingest: a source"), "ingest")
        self.assertEqual(wh.op_of("constitution-pass: x"), "constitution-pass")
        self.assertEqual(wh.op_of("feat(wiki): x"), "feat")
        self.assertIsNone(wh.op_of("Edit people/kristin from the portal"))
        self.assertIsNone(wh.op_of("Merge pull request #225"))


class TestTheGate(Fixture):
    def test_a_clean_repository_passes(self):
        self.repo.write("mind/a", modified="2026-02-01")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        code, out = self.check()
        self.assertEqual(code, 0)
        self.assertIn("0 error(s)", out)

    def test_a_page_dated_after_its_last_commit_fails(self):
        self.repo.write("mind/a", modified="2027-01-01")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        code, out = self.check()
        self.assertEqual(code, 1)
        self.assertIn("mind/a", out)
        self.assertIn("2027-01-01", out)

    def test_a_page_dated_before_its_last_commit_passes(self):
        """The commonest case in the real repository, and honest: a link
        cleanup touches a page without changing what it says."""
        self.repo.write("mind/a", modified="2026-01-01")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        self.repo.write("mind/a", modified="2026-01-01", body="a link was removed")
        self.repo.commit("lint: drop a dead link", when="2026-06-01T12:00:00+00:00")
        code, _ = self.check()
        self.assertEqual(code, 0)

    def test_an_uncommitted_edit_is_exempt(self):
        """The exemption the gate is worthless without."""
        self.repo.write("mind/a", modified="2026-02-01")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        # A session mid-pass: the page is revised and dated today, uncommitted.
        self.repo.write("mind/a", modified="2027-01-01", body="revised")
        self.assertIn("wiki/mind/a.md", wh.uncommitted())
        code, out = self.check()
        self.assertEqual(code, 0, out)

    def test_a_staged_edit_is_exempt_too(self):
        self.repo.write("mind/a", modified="2026-02-01")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        self.repo.write("mind/a", modified="2027-01-01", body="revised")
        self.repo.git("add", "-A")
        self.assertIn("wiki/mind/a.md", wh.uncommitted())
        self.assertEqual(self.check()[0], 0)

    def test_a_brand_new_uncommitted_page_is_exempt(self):
        self.repo.write("mind/a", modified="2026-02-01")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        self.repo.write("mind/brand-new", modified="2027-01-01")
        self.assertIn("wiki/mind/brand-new.md", wh.uncommitted())
        self.assertEqual(self.check()[0], 0)

    def test_a_page_with_no_date_modified_is_not_the_gates_business(self):
        """bin/wiki-lint owns whether frontmatter is complete. This gate only
        asks whether a date that exists is supported by the log."""
        full = os.path.join(self.tmp.name, "wiki", "mind", "a.md")
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write("---\ntitle: A\n---\n\n# A\n\ntext\n")
        self.repo.commit("ingest: a")
        self.assertEqual(self.check()[0], 0)


class TestShallow(Fixture):
    def test_the_gate_passes_rather_than_failing_on_what_it_cannot_see(self):
        """A shallow log does not reach the first version of any page. Failing
        would make every shallow CI checkout red for a reason nobody could fix
        from the working tree."""
        self.repo.write("mind/a", modified="2027-01-01")
        self.repo.commit("ingest: a", when="2026-02-01T12:00:00+00:00")
        original = wh.shallow
        wh.shallow = lambda: True
        try:
            code, out = self.check()
        finally:
            wh.shallow = original
        self.assertEqual(code, 0)
        self.assertIn("shallow", out)


class TestUncommittedParsing(Fixture):
    def test_a_rename_reports_the_new_name(self):
        """`git status --porcelain` writes `R  old -> new`; the file on disk —
        and so the one that could carry a wrong date — is the new one."""
        self.repo.write("mind/old", body="y" * 400)
        self.repo.commit("ingest: old")
        self.repo.git("mv", "wiki/mind/old.md", "wiki/mind/new.md")
        pending = wh.uncommitted()
        self.assertIn("wiki/mind/new.md", pending)

    def test_a_path_with_a_space_survives_the_quoting(self):
        self.repo.write("mind/a")
        self.repo.commit("ingest: a")
        self.repo.write("mind/two words")
        self.assertIn("wiki/mind/two words.md", wh.uncommitted())


if __name__ == "__main__":
    unittest.main()
