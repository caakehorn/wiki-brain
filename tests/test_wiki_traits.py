"""Tests for bin/wiki-traits — the trait-corpus map and the filter it produces.

The expensive half (`mine`) reads four corpora and is not exercised here. What
is tested is every rule that stops the tool publishing a confident wrong answer,
because the first run of this tool did exactly that and the caps below are the
fix. Read the module's PROXY_REVIEW comment before changing any of them.
"""
import os
import re
import unittest
from importlib.machinery import SourceFileLoader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
wt = SourceFileLoader("wiki_traits", os.path.join(ROOT, "bin", "wiki-traits")).load_module()


class VerdictCap(unittest.TestCase):
    """An unreviewed proxy may report silence and nothing else.

    This is the rule that stopped `CONTRADICTED LOAD` on the Fe deficit — an
    instruction to re-read 37 pages — from being published off a regex whose
    every match was Dan being comforted.
    """

    def test_unreviewed_cannot_confirm(self):
        self.assertEqual(wt.verdict("high", 9.0, 5000, "unreviewed"), "unreviewed")

    def test_unreviewed_cannot_contradict(self):
        """The load-bearing one. INVERTED is the heaviest verdict in the system
        and the cheapest to manufacture."""
        self.assertEqual(wt.verdict("high", 0.05, 5000, "unreviewed"), "unreviewed")

    def test_unreviewed_may_still_report_silence(self):
        """A genuine null from an unreviewed proxy is still a null."""
        self.assertEqual(wt.verdict("high", 1.0, 5000, "unreviewed"), "silent")

    def test_capped_result_is_never_reported_as_silence(self):
        """The regression against a future "simplification".

        `silent` is a finding — an instrument ran and the corpus carried
        nothing. A capped `unreviewed` is the absence of one. Returning `silent`
        here would claim a measurement that never happened, and would collapse
        `UNREVIEWED LOAD` into `UNSUPPORTED LOAD` in the filter table, which
        tells a synthesis the corpus was checked when it was not.
        """
        for ratio in (9.0, 1.4, 0.05):
            self.assertNotEqual(wt.verdict("high", ratio, 5000, "unreviewed"), "silent",
                                f"a capped verdict at ratio {ratio} was reported as silence")

    def test_the_three_states_are_three_values(self):
        """silent / unreviewed / no-instrument are distinct epistemic positions:
        an instrument ran and found nothing; none ran; every one built was read
        and found to measure something else."""
        self.assertEqual(len({"silent", "unreviewed", "no instrument"}), 3)
        for r in ("load-bearing", "present", "dormant"):
            cells = {wt.QUADRANT[(b, r)]
                     for b in ("silent", "unreviewed", "no instrument")}
            self.assertEqual(len(cells), 3,
                             f"two of the three states share a cell at reach={r}")

    def test_broken_is_excluded_outright(self):
        for ratio in (9.0, 1.0, 0.05):
            self.assertEqual(wt.verdict("high", ratio, 5000, "broken"), "excluded")

    def test_sound_reports_the_real_verdict(self):
        self.assertEqual(wt.verdict("high", 9.0, 5000, "sound"), "SUPPORTED")
        self.assertEqual(wt.verdict("high", 0.05, 5000, "sound"), "INVERTED")

    def test_too_few_survives_every_status(self):
        """A small-n result is not upgraded by review; it is still too few."""
        self.assertEqual(wt.verdict("high", 9.0, 3, "sound"), "too few")


class ReviewRegister(unittest.TestCase):
    def test_every_broken_entry_names_what_breaks_it(self):
        """A `broken` verdict with no reason is unauditable — the next reader
        cannot tell a real finding from somebody clearing a row."""
        for key, (status, note) in wt.PROXY_REVIEW.items():
            if status == "broken":
                self.assertTrue(len(note) > 40, f"{key} has no substantive reason")

    def test_statuses_are_from_the_fixed_vocabulary(self):
        for key, (status, _) in wt.PROXY_REVIEW.items():
            self.assertIn(status, ("sound", "broken"),
                          f"{key}: unreviewed is the absence of an entry, not a value")

    def test_review_keys_match_real_proxies(self):
        """A review entry whose facet::label does not exist reviews nothing and
        silently leaves the real proxy unreviewed."""
        real = {f"{f}::{l}" for f, s, d, l, p in wt.load_predictions()}
        for key in wt.PROXY_REVIEW:
            self.assertIn(key, real, f"{key} matches no proxy in psychometrics")

    def test_proxy_status_defaults_to_unreviewed(self):
        self.assertEqual(wt.proxy_status("nonexistent", "nothing")[0], "unreviewed")


class Quadrant(unittest.TestCase):
    def test_every_band_pair_has_a_cell(self):
        """A missing pair is a KeyError at exactly the moment somebody runs the
        filter on a trait in a state nobody anticipated."""
        bands = ("supported", "message-only", "silent", "inverted", "too few",
                 "unreviewed", "no instrument")
        for b in bands:
            for r in ("load-bearing", "present", "dormant"):
                self.assertIn((b, r), wt.QUADRANT, f"no cell for ({b}, {r})")

    def test_every_cell_has_a_weight(self):
        """A cell with no policy tells a synthesis nothing, which is the one
        thing this tool exists to avoid."""
        for cell in set(wt.QUADRANT.values()):
            self.assertIn(cell, wt.WEIGHT, f"cell {cell!r} has no WEIGHT policy")

    def test_unmeasurable_load_never_reads_as_permission(self):
        """The four cells where the wiki leans on something the instrument
        cannot speak to must all forbid using it as a mechanism."""
        for cell in ("UNSUPPORTED LOAD", "UNREVIEWED LOAD", "NO INSTRUMENT / LOAD",
                     "CONTRADICTED LOAD"):
            w = wt.WEIGHT[cell].lower()
            self.assertTrue(
                any(k in w for k in ("do not", "never", "stop")),
                f"{cell} does not forbid anything: {w!r}")

    def test_no_instrument_is_distinct_from_silent(self):
        """"Silent" implies an instrument ran and found nothing. "No instrument"
        means none exists. Collapsing them would claim a measurement."""
        self.assertNotEqual(wt.QUADRANT[("silent", "load-bearing")],
                            wt.QUADRANT[("no instrument", "load-bearing")])


class Reach(unittest.TestCase):
    def test_generated_pages_excluded(self):
        """The map names every trait by construction, so counting it would make
        it an input to itself and reach would climb on every regeneration."""
        self.assertIn("wiki/mind/profile/trait-corpus-map.md", wt.GENERATED)
        pages = {p for p, _ in wt.wiki_pages()}
        self.assertNotIn("wiki/mind/profile/trait-corpus-map.md", pages)

    def test_reach_bands_are_ordered(self):
        self.assertGreater(wt.REACH_LOAD_BEARING, wt.REACH_PRESENT)


class Replication(unittest.TestCase):
    def test_quantile_is_not_the_median(self):
        """At the median, half of all proxies replicate by construction and the
        column carries no information. The first build shipped that."""
        self.assertGreater(wt.REPLICATION_QUANTILE, 0.5)

    def test_replication_requires_hits(self):
        self.assertGreaterEqual(wt.REPLICATION_MIN_HITS, 1)


class Traits(unittest.TestCase):
    def test_every_trait_owns_real_facets(self):
        facets = {f for f, s, d, l, p in wt.load_predictions()}
        for tid, t in wt.TRAITS.items():
            for f in t["facets"]:
                self.assertIn(f, facets, f"{tid} claims unknown facet {f!r}")

    def test_every_trait_names_an_existing_home_page(self):
        for tid, t in wt.TRAITS.items():
            self.assertTrue(os.path.exists(os.path.join(ROOT, t["home"])),
                            f"{tid} home page {t['home']} does not exist")

    def test_wiki_patterns_compile(self):
        for tid, t in wt.TRAITS.items():
            re.compile(t["wiki"], re.I)

    def test_no_wiki_pattern_matches_constitution_boilerplate(self):
        """`left` matched "**Checked, left standing**" — present on every
        synthesis page — and inflated liberalism's reach to 202 pages."""
        boiler = "| Historical precedent | **Checked, left standing.** The 2005 hinge"
        for tid, t in wt.TRAITS.items():
            self.assertIsNone(re.search(t["wiki"], boiler, re.I),
                              f"{tid}'s wiki pattern matches constitution boilerplate")


class Page(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(wt.MEASURED):
            self.skipTest("no traits/measured.json — run `bin/wiki-traits mine`")
        self.rendered = wt.render()

    def test_no_confidence_percentage(self):
        """The standing rule. A percentage needs a denominator of things that
        could have disconfirmed, and silence is not one of them."""
        body = self.rendered.split("## The map")[-1]
        bad = re.findall(r"\b\d{1,3}(?:\.\d+)?\s?%", body)
        self.assertEqual(bad, [], f"a percentage reached the page: {bad}")

    def test_states_that_reach_is_not_evidence(self):
        self.assertIn("not evidence", self.rendered.lower())

    def test_states_the_asymmetry(self):
        self.assertIn("not falsification", self.rendered.lower())

    def test_declares_itself_generated(self):
        self.assertIn("GENERATED", self.rendered)

    def test_names_facebook_as_an_unmeasured_register(self):
        """An absent register that the page does not name reads as a corpus
        that was fully covered."""
        self.assertIn("Facebook", self.rendered)

    def test_render_is_deterministic(self):
        strip = lambda s: re.sub(r"^date_modified:.*$", "", s, flags=re.M)
        self.assertEqual(strip(self.rendered), strip(wt.render()))


if __name__ == "__main__":
    unittest.main()
