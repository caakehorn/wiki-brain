#!/usr/bin/env python3
"""Tests for bin/wiki-lessons, the gate over the cross-agent skill corpus.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

What is pinned here, and why each one earns a test.

  * **INDEX drift.** `INDEX.md` is generated from the skill files. It shipped on
    2026-08-30 hand-maintained, with a `Status` column duplicating each skill's
    own `status:` frontmatter — two sources of truth for one fact — and it had
    already drifted from the files by the time anything checked. Generation is
    only a fix if the gate notices when the committed file is not what the
    generator would write, so that exact comparison is pinned.

  * **The superseded-but-still-routed case.** `PROTOCOL.md` §6 replaces a skill
    by declaring `supersedes:`. If the old file stays routed, the router returns
    both and an agent follows whichever it reads first — two live instructions
    for one situation, with nothing to indicate which is current. That is the
    one defect in this subsystem that actively misleads rather than merely
    failing to help, so it is an error rather than a warning.

  * **A skill absent from CHANGELOG.md.** §6 requires every state transition
    recorded with its date and reason. An instruction that entered the corpus
    with no such account cannot be weighed by a later reader — it is
    indistinguishable from one somebody added on confidence. Two of the section's
    original skills were in exactly that state.

  * **Scaffold text surviving into a committed skill.** The failure is silent in
    the worst way: the file parses, routes, and is handed to an agent as an
    instruction that says "REPLACE — imperative steps".

The real `skills/` tree is never touched: every case builds a small tree in a
temp directory and points the module's roots at it.
"""
import importlib.machinery
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "bin", "wiki-lessons")


def load_module():
    """bin/wiki-lessons has no .py extension, and no import-time side effects."""
    spec = importlib.util.spec_from_loader(
        "wiki_skills", importlib.machinery.SourceFileLoader("wiki_skills", SCRIPT))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SKILL = """---
status: {status}
scope: repo
triggers:
  - {trigger}
sources:
  - CLAUDE.md
validated: {validated}
supersedes: [{supersedes}]
---

# {title}

## Instruction

Do the specific thing.

## Why

Because the specific failure happened on a specific date.

## Validation

Run the specific command.
"""


class Harness(unittest.TestCase):
    """A throwaway skills/ tree with the module pointed at it."""

    def setUp(self):
        self.mod = load_module()
        self.dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.dir, ignore_errors=True)
        self.skills = os.path.join(self.dir, "skills")
        os.makedirs(os.path.join(self.skills, "repo"))
        self.mod.SKILLS = self.skills
        self.mod.INDEX = os.path.join(self.skills, "INDEX.md")
        self.mod.INBOX = os.path.join(self.skills, "INBOX.md")
        self.mod.CHANGELOG = os.path.join(self.skills, "CHANGELOG.md")
        self.changelog("# Skill Changelog\n\n- repo/a.md\n- repo/b.md\n")

    def write(self, slug, status="active", trigger="editing commands",
              validated="2026-01-01", supersedes="", title="A rule"):
        path = os.path.join(self.skills, *slug.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(SKILL.format(status=status, trigger=trigger, validated=validated,
                                  supersedes=supersedes, title=title))
        return path

    def changelog(self, text):
        with open(self.mod.CHANGELOG, "w", encoding="utf-8") as fh:
            fh.write(text)

    def scan(self):
        return self.mod.cmd_scan(None)

    def check(self):
        return self.mod.cmd_check(None)

    def errors(self):
        """Run check and return the ERROR lines it printed."""
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = self.mod.cmd_check(None)
        lines = [ln[6:] for ln in buf.getvalue().splitlines() if ln.startswith("ERROR ")]
        return code, lines


class TestWellFormed(Harness):
    def test_clean_corpus_passes(self):
        self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        code, errs = self.errors()
        self.assertEqual(errs, [])
        self.assertEqual(code, 0)

    def test_missing_required_section_fails(self):
        path = self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        with open(path, encoding="utf-8") as fh:
            text = fh.read().replace("## Validation", "## Notes")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("## Validation" in e for e in errs), errs)

    def test_unknown_status_fails(self):
        self.write("repo/a.md", status="pretty-good")
        self.write("repo/b.md")
        self.scan()
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("is not one of" in e for e in errs), errs)

    def test_future_validated_date_fails(self):
        self.write("repo/a.md", validated="2099-01-01")
        self.write("repo/b.md")
        self.scan()
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("in the future" in e for e in errs), errs)

    def test_missing_frontmatter_key_fails(self):
        path = self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        with open(path, encoding="utf-8") as fh:
            text = fh.read().replace("scope: repo\n", "")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("`scope:`" in e for e in errs), errs)

    def test_scaffold_text_fails(self):
        """A committed scaffold routes an agent to an instruction that says REPLACE."""
        self.write("repo/b.md")
        path = os.path.join(self.skills, "repo", "a.md")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        args = type("A", (), {"slug": "repo/a"})()
        self.mod.cmd_new(args)
        self.changelog("# Skill Changelog\n\n- repo/a.md\n- repo/b.md\n")
        self.scan()
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("scaffold" in e for e in errs), errs)


class TestIndexDrift(Harness):
    def test_hand_edited_index_fails(self):
        self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        with open(self.mod.INDEX, "a", encoding="utf-8") as fh:
            fh.write("\n| `repo/invented.md` | anything | active | 2026-01-01 |\n")
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("out of step" in e for e in errs), errs)

    def test_new_skill_without_rescan_fails(self):
        """A skill added and committed without rescanning is unrouted."""
        self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        self.write("repo/c.md")
        self.changelog("# Skill Changelog\n\n- repo/a.md\n- repo/b.md\n- repo/c.md\n")
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("out of step" in e for e in errs), errs)
        self.scan()
        code, errs = self.errors()
        self.assertEqual(errs, [])
        self.assertEqual(code, 0)

    def test_scan_is_idempotent(self):
        self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        with open(self.mod.INDEX, encoding="utf-8") as fh:
            first = fh.read()
        self.scan()
        with open(self.mod.INDEX, encoding="utf-8") as fh:
            self.assertEqual(first, fh.read())

    def test_retired_skill_leaves_the_routed_table(self):
        self.write("repo/a.md", status="retired")
        self.write("repo/b.md")
        self.scan()
        with open(self.mod.INDEX, encoding="utf-8") as fh:
            index = fh.read()
        routed = index.split("## History")[0]
        self.assertNotIn("repo/a.md", routed)
        self.assertIn("repo/a.md", index.split("## History")[1])


class TestSupersession(Harness):
    def test_superseded_but_still_active_fails(self):
        """The case that actively misleads: two live rules for one situation."""
        self.write("repo/a.md", status="active")
        self.write("repo/b.md", status="active", supersedes="repo/a.md")
        self.scan()
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("superseded by" in e for e in errs), errs)

    def test_superseded_and_retired_passes(self):
        self.write("repo/a.md", status="retired")
        self.write("repo/b.md", status="active", supersedes="repo/a.md")
        self.scan()
        code, errs = self.errors()
        self.assertEqual(errs, [])
        self.assertEqual(code, 0)

    def test_supersedes_a_file_that_does_not_exist_fails(self):
        self.write("repo/a.md")
        self.write("repo/b.md", supersedes="repo/ghost.md")
        self.scan()
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("not a skill file" in e for e in errs), errs)


class TestChangelog(Harness):
    def test_skill_absent_from_changelog_fails(self):
        self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        self.changelog("# Skill Changelog\n\n- repo/a.md\n")
        code, errs = self.errors()
        self.assertEqual(code, 1)
        self.assertTrue(any("CHANGELOG" in e and "repo/b.md" in e for e in errs), errs)

    def test_empty_changelog_fails(self):
        self.write("repo/a.md")
        self.write("repo/b.md")
        self.scan()
        self.changelog("")
        code, errs = self.errors()
        self.assertEqual(code, 1)


class TestRouting(Harness):
    def test_route_matches_triggers_and_skips_history(self):
        self.write("repo/a.md", trigger="editing bin/wiki-lint", title="Lint rule")
        self.write("repo/b.md", status="retired", trigger="editing bin/wiki-lint",
                   title="Old lint rule")
        self.scan()
        import io
        import contextlib
        buf = io.StringIO()
        args = type("A", (), {"task": ["editing", "bin/wiki-lint", "today"]})()
        with contextlib.redirect_stdout(buf):
            self.mod.cmd_route(args)
        out = buf.getvalue()
        self.assertIn("repo/a.md", out)
        self.assertNotIn("repo/b.md", out)

    def test_route_with_no_match_refuses_to_invent(self):
        self.write("repo/a.md", trigger="editing bin/wiki-lint")
        self.write("repo/b.md")
        self.scan()
        import io
        import contextlib
        buf = io.StringIO()
        args = type("A", (), {"task": ["baking", "sourdough"]})()
        with contextlib.redirect_stdout(buf):
            self.mod.cmd_route(args)
        self.assertIn("not permission to invent", buf.getvalue())


class TestInbox(Harness):
    def test_unvalidated_candidates_are_counted(self):
        with open(self.mod.INBOX, "w", encoding="utf-8") as fh:
            fh.write("# Skill Inbox\n\n## Seed candidates\n\n"
                     "### 2026-08-30 — A thing that happened\n\n"
                     "- **Status:** inbox\n\n"
                     "### 2026-08-29 — A promoted thing\n\n"
                     "- **Status:** promoted\n")
        pending = [c for c in self.mod.inbox_candidates()
                   if c.status in ("inbox", "provisional")]
        self.assertEqual([c.title for c in pending], ["A thing that happened"])

    def test_entry_template_is_not_a_candidate(self):
        """The template documents the shape; counting it would be a phantom item."""
        with open(self.mod.INBOX, "w", encoding="utf-8") as fh:
            fh.write("# Skill Inbox\n\n## Entry template\n\n"
                     "### YYYY-MM-DD — short title\n\n- **Status:** inbox | provisional\n\n"
                     "## Seed candidates\n\n"
                     "### 2026-08-30 — A real one\n\n- **Status:** provisional\n")
        titles = [c.title for c in self.mod.inbox_candidates()]
        self.assertEqual(titles, ["A real one"])


class TestRealCorpus(unittest.TestCase):
    """The committed skills/ tree must itself pass, and stay routed."""

    def test_repository_skills_pass_the_gate(self):
        import io
        import contextlib
        mod = load_module()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = mod.cmd_check(None)
        self.assertEqual(code, 0, buf.getvalue())

    def test_committed_index_is_what_scan_would_write(self):
        mod = load_module()
        with open(mod.INDEX, encoding="utf-8") as fh:
            self.assertEqual(mod.index_text(mod.load()), fh.read())

    def test_every_skill_is_reachable_by_its_own_trigger(self):
        """A trigger nobody can match is a skill nothing routes to."""
        mod = load_module()
        for skill in mod.load():
            if not skill.routed:
                continue
            self.assertTrue(skill.triggers, "%s has no triggers" % skill.slug)


if __name__ == "__main__":
    unittest.main()
