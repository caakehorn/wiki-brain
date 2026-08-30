#!/usr/bin/env python3
"""Tests for bin/wiki-skills, the cross-model skills database.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

Four properties are pinned here and none of them is cosmetic.

  * **The refusal.** This repository is public and its history cannot be
    un-published. MCP server configurations are the single most reliable place
    in an agent's environment to find a live API key, and "push everything about
    your tools into the wiki" is, written naively, an instruction to publish
    credentials. The tool must REFUSE rather than strip — a silent strip teaches
    the next caller that pushing values is fine — and it must refuse on the
    hand-typed path (`--env FOO=bar`) while still tolerating a real config file
    read off disk, because refusing that would make `scan` unusable on any
    machine with a working key. Those two paths are one function apart and it
    would be easy to make them agree in the wrong direction.

  * **Idempotence.** The push is meant to run every session. A tool that grows
    the log by fifty lines each time it is asked "anything new?" is a tool
    people stop running, and a database nobody pushes to is worse than none,
    because the page still looks current.

  * **The moratorium, in two tiers.** `CLAUDE.md` carries a standing operator
    directive about a living person. One blunt rule gets this wrong in both
    directions: a name that cannot be printed must vanish from the page, and a
    live useful tool whose *summary* happens to name her must still appear, or
    the database lies about what the repository offers. Both tiers are pinned,
    and so is the guarantee — the gate re-checks the rendered page, so the
    outcome does not rest on the renderer that produced it.

  * **The merge.** The log is append-only precisely so two branches' pushes
    union rather than conflict. If projection ever stopped being a pure fold
    over sorted events, a merge would start losing one side silently.

The real database is never touched: every case builds its own tree in a temp
directory and points a Registry at it.
"""
import importlib.machinery
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "bin", "wiki-skills")


def load_module():
    """bin/wiki-skills has no .py extension, and no import-time side effects."""
    spec = importlib.util.spec_from_loader(
        "wiki_skills", importlib.machinery.SourceFileLoader("wiki_skills", SCRIPT))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ws = load_module()


def cap(**kw):
    base = {"kind": "skill", "name": "a-skill", "summary": "does a thing",
            "path": "skills/x.md"}
    base.update(kw)
    return base


class Tree(unittest.TestCase):
    """A throwaway repository with a registry in it."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.dir, "skills", "registry"))
        os.makedirs(os.path.join(self.dir, "wiki", "meta"))
        self.reg = ws.Registry(self.dir)

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def push(self, caps, agent="model-a", **kw):
        return ws.do_push(self.reg, {"id": agent}, caps, **kw)


# --------------------------------------------------------------- the refusal
class TestRefusal(unittest.TestCase):
    def test_env_value_is_refused_not_stripped(self):
        """`--env FOO=bar` must raise. Halving it silently teaches the habit."""
        with self.assertRaises(ws.RegistryError) as ctx:
            ws.normalise(cap(kind="mcp_server", name="s",
                             env=["ANTHROPIC_API_KEY=sk-ant-abcdefghijklmnop"]))
        self.assertIn("VALUE", str(ctx.exception))

    def test_env_names_alone_are_fine(self):
        rec = ws.normalise(cap(kind="mcp_server", name="s",
                               env=["GITHUB_TOKEN", "API_BASE"]))
        self.assertEqual(rec["env"], ["API_BASE", "GITHUB_TOKEN"])

    def test_config_dict_keeps_names_and_drops_values(self):
        """The one place a value may be present: a real config read off disk.

        Refusing here would make `scan` fail on any machine with a working key,
        which is every machine that has ever used the server.
        """
        rec = ws.normalise(cap(kind="mcp_server", name="s",
                               env={"GITHUB_TOKEN": "ghp_" + "a" * 36}))
        self.assertEqual(rec["env"], ["GITHUB_TOKEN"])
        self.assertNotIn("ghp_", json.dumps(rec))

    def test_credential_shapes_in_prose_are_refused(self):
        for bad in ("sk-ant-abcdefghijklmnop1234",
                    "ghp_" + "a" * 36,
                    "xoxb-1234567890-abcdefghij",
                    "AKIAIOSFODNN7EXAMPLE",
                    "Bearer abcdefghijklmnopqrstuvwx",
                    "-----BEGIN RSA PRIVATE KEY-----"):
            with self.subTest(bad=bad):
                with self.assertRaises(ws.RegistryError):
                    ws.normalise(cap(summary=f"a thing, token {bad}"))

    def test_url_credentials_are_stripped_from_links_and_refused_in_prose(self):
        rec = ws.normalise(cap(link="https://example.com/mcp?token=abcd1234efgh#frag"))
        self.assertEqual(rec["link"], "https://example.com/mcp")
        with self.assertRaises(ws.RegistryError):
            ws.normalise(cap(summary="reach it at https://bob:hunter2@example.com/mcp"))

    def test_provenance_is_required(self):
        """A capability nothing can be reached through is a rumour."""
        with self.assertRaises(ws.RegistryError):
            ws.normalise({"kind": "skill", "name": "ghost", "summary": "no way in"})

    def test_summary_is_required(self):
        with self.assertRaises(ws.RegistryError):
            ws.normalise({"kind": "skill", "name": "n", "path": "p"})


# ------------------------------------------------------------- idempotence
class TestIdempotence(Tree):
    def test_second_identical_push_appends_nothing(self):
        first = self.push([cap(), cap(name="b", path="skills/b.md")])
        self.assertEqual(len(first["added"]), 2)
        again = self.push([cap(), cap(name="b", path="skills/b.md")])
        self.assertEqual(again["events"], 0)
        self.assertEqual(again["unchanged"], 2)

    def test_changed_content_is_a_revision_not_a_duplicate(self):
        self.push([cap()])
        second = self.push([cap(summary="does a different thing")])
        self.assertEqual(len(second["changed"]), 1)
        state = self.reg.project()
        live = [c for c in state["capabilities"] if c["status"] == "live"]
        self.assertEqual(len(live), 1, "a revision must not fork the capability")
        self.assertEqual(len(live[0]["declared_by"]), 1)
        self.assertTrue(any(r["from"] for r in live[0]["revisions"]))

    def test_two_models_declaring_one_capability_share_the_row(self):
        self.push([cap()], agent="model-a")
        self.push([cap()], agent="model-b")
        state = self.reg.project()
        self.assertEqual(state["counts"]["capabilities"], 1)
        self.assertEqual(state["counts"]["shared"], 1)
        self.assertEqual([d["agent"] for d in state["capabilities"][0]["declared_by"]],
                         ["model-a", "model-b"])

    def test_retire_missing_spares_a_capability_another_model_still_has(self):
        self.push([cap()], agent="model-a")
        self.push([cap()], agent="model-b")
        self.push([cap(name="other", path="skills/o.md")], agent="model-a",
                  retire_missing=True)
        state = self.reg.project()
        by_name = {c["name"]: c for c in state["capabilities"]}
        self.assertEqual(by_name["a-skill"]["status"], "live",
                         "model-b still declares it; it is not gone")


# ------------------------------------------------------------- the directive
class TestMoratorium(Tree):
    def test_a_name_that_cannot_be_printed_is_held_out_entirely(self):
        self.push([cap(name="annie-read-synthesis", path="p.md"),
                   cap(name="ordinary", path="q.md")])
        state = self.reg.project()
        page = ws.render_page(state, self.dir)
        self.assertNotIn("annie", page.lower())
        self.assertIn("ordinary", page)
        self.assertIn("omitted from the tables entirely", page)

    def test_a_neutral_name_with_a_named_summary_keeps_its_row(self):
        """The row survives; the summary does not. Dropping the row would make
        the database lie about what the repository offers."""
        self.push([cap(name="corpus-read", path="skills/corpus-read.md",
                       summary="Do NOT use on the Annie corpus at all.")])
        page = ws.render_page(self.reg.project(), self.dir)
        self.assertNotIn("annie", page.lower())
        self.assertIn("corpus-read", page)
        self.assertIn("skills/corpus-read.md", page,
                      "the path must survive — the directive stops new writing, "
                      "not access to what is already public")
        self.assertIn("summary withheld", page)

    def test_the_totals_still_count_what_the_page_will_not_print(self):
        self.push([cap(name="annie-read-synthesis", path="p.md")])
        page = ws.render_page(self.reg.project(), self.dir)
        self.assertIn("| Capabilities on the record | 1 |", page)

    def test_the_gate_catches_a_hand_edit_that_names_her(self):
        """The guarantee must not rest on the renderer that produced the page.

        The published object is the FILE, not the render. A check that only
        inspected the render would report this as "the page is behind the
        database" — true, and not the thing that matters about it.
        """
        self.push([cap(name="ordinary", path="p.md")])
        self.reg.write_projection()
        self.reg.page.parent.mkdir(parents=True, exist_ok=True)
        self.reg.page.write_text(
            ws.render_page(self.reg.project(), self.dir).replace(
                "ordinary", "annie-notes"), encoding="utf-8")

        import io, contextlib
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = ws.check(self.reg)
        self.assertEqual(code, 1)
        self.assertIn("names a person under the standing", out.getvalue())


# ------------------------------------------------------------------ the gate
class TestGate(Tree):
    def clean(self):
        self.reg.write_projection()
        self.reg.page.write_text(ws.render_page(self.reg.project(), self.dir),
                                 encoding="utf-8")

    def test_empty_database_is_silent_and_clean(self):
        self.assertEqual(ws.check(self.reg), 0)

    def test_a_clean_database_passes(self):
        self.push([cap()])
        self.clean()
        self.assertEqual(ws.check(self.reg), 0)

    def test_a_stale_projection_fails(self):
        self.push([cap()])
        self.clean()
        self.reg.projection.write_text('{"schema": 1}\n', encoding="utf-8")
        self.assertEqual(ws.check(self.reg), 1)

    def test_a_page_behind_the_log_fails(self):
        self.push([cap()])
        self.clean()
        self.push([cap(name="added-later", path="skills/z.md")])
        self.reg.write_projection()
        self.assertEqual(ws.check(self.reg), 1)

    def test_fix_regenerates_instead_of_failing(self):
        self.push([cap()])
        self.clean()
        self.push([cap(name="added-later", path="skills/z.md")])
        self.assertEqual(ws.check(self.reg, fix=True), 0)
        self.assertIn("added-later", self.reg.page.read_text(encoding="utf-8"))

    def test_a_credential_hand_edited_into_the_log_is_caught(self):
        """The refusal runs at the writer; this is the same check at the gate."""
        self.push([cap()])
        self.clean()
        with self.reg.events.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({
                "id": "01ZZZ", "event": "capability_observed", "at": "2026-08-30T00:00:00+00:00",
                "agent": "model-a",
                "data": {"kind": "tool", "name": "leak", "summary": "ghp_" + "a" * 36,
                         "path": "x", "digest": "0"}}) + "\n")
        self.assertEqual(ws.check(self.reg), 1)

    def test_a_duplicate_event_id_fails(self):
        self.push([cap()])
        line = self.reg.events.read_text(encoding="utf-8").splitlines()[-1]
        with self.reg.events.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
        self.clean()
        self.assertEqual(ws.check(self.reg), 1)


# ----------------------------------------------------------------- the merge
class TestMerge(Tree):
    def test_two_branches_appends_union(self):
        """The whole reason the record is a log. Concatenating two branches'
        appends in either order must give the same projection."""
        self.push([cap()], agent="model-a")
        a_lines = self.reg.events.read_text(encoding="utf-8").splitlines()
        self.reg.events.unlink()
        self.push([cap(name="b", path="skills/b.md")], agent="model-b")
        b_lines = self.reg.events.read_text(encoding="utf-8").splitlines()

        def project_from(lines):
            self.reg.events.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return self.reg.project()

        one = project_from(a_lines + b_lines)
        two = project_from(b_lines + a_lines)
        self.assertEqual(one["counts"]["capabilities"], 2)
        self.assertEqual(json.dumps(one, sort_keys=True),
                         json.dumps(two, sort_keys=True),
                         "projection must be order-independent, or a merge loses a side")


# --------------------------------------------------------------- the scanner
class TestScan(unittest.TestCase):
    def test_the_real_repository_scans_without_raising(self):
        """The scan reads this machine's actual config files. It must produce
        records that survive `normalise` — including its env handling."""
        caps = ws.scan_repo(ROOT)
        self.assertTrue(caps, "the scan found nothing in a repository full of bin/ tools")
        for c in caps:
            with self.subTest(name=c.get("name")):
                ws.normalise(c)
        kinds = {c["kind"] for c in caps}
        self.assertIn("command", kinds)
        self.assertIn("skill", kinds)


if __name__ == "__main__":
    unittest.main()
