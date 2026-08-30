#!/usr/bin/env python3
"""Tests for bin/aesgcm.py — the sealed transport under the intake ledger.

Run:  python3 -m unittest discover -s tests -v     (from the repo root)

WHY THIS FILE IS PARANOID. Everything else in this repository fails loudly when
it is wrong: a lint gate goes red, a projection drifts, a number looks absurd.
Cryptography written by hand fails *quietly* — a subtly wrong GHASH still
produces ciphertext-shaped bytes, still round-trips against itself, and still
looks exactly like it works right up until the day something else has to read it
or an attacker does.

So this suite never checks the implementation against itself. It checks it
against NIST's published vectors, which are the same numbers every other AES
implementation on earth agrees on, and against the property that actually
matters here: that a wrong passphrase raises rather than returning plausible
garbage.

The interoperability half — that `js/boss-sync.js` in the leviathan repo and
this module open each other's blobs — cannot run here, because it needs a
browser. It was verified in both directions before either side shipped, and the
format is pinned below so a change on this side breaks a test rather than a
phone.
"""
import importlib.util
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "bin"))
import aesgcm as A  # noqa: E402


class TestAESBlock(unittest.TestCase):
    """FIPS-197 Appendix C.3 — the canonical AES-256 block."""

    def test_the_published_block(self):
        key = bytes.fromhex("000102030405060708090a0b0c0d0e0f"
                            "101112131415161718191a1b1c1d1e1f")
        pt = bytes.fromhex("00112233445566778899aabbccddeeff")
        self.assertEqual(A._encrypt_block(A._expand_key(key), pt).hex(),
                         "8ea2b7ca516745bfeafc49904b496089")

    def test_it_refuses_a_key_that_is_not_256_bits(self):
        with self.assertRaises(ValueError):
            A._expand_key(b"\x00" * 16)


class TestGCMVectors(unittest.TestCase):
    """NIST SP 800-38D, the AES-256 cases. Ciphertext AND tag, both directions."""

    CASES = [
        ("0" * 64, "0" * 24, "", "", "", "530f8afbc74536b9a963b4f1c4cb738b"),
        ("0" * 64, "0" * 24, "0" * 32, "",
         "cea7403d4d606b6e074ec5d3baf39d18", "d0d1c8a799996bf0265b98b5d48ab919"),
        ("feffe9928665731c6d6a8f9467308308feffe9928665731c6d6a8f9467308308",
         "cafebabefacedbaddecaf888",
         "d9313225f88406e5a55909c5aff5269a86a7a9531534f7da2e4c303d8a318a721c3c0c95956809532"
         "fcf0e2449a6b525b16aedf5aa0de657ba637b391aafd255", "",
         "522dc1f099567d07f47f37a32a84427d643a8cdcbfe5c0c97598a2bd2555d1aa8cb08e48590dbb3da"
         "7b08b1056828838c5f61e6393ba7a0abcc9f662898015ad",
         "b094dac5d93471bdec1a502270e3cc6c"),
        ("feffe9928665731c6d6a8f9467308308feffe9928665731c6d6a8f9467308308",
         "cafebabefacedbaddecaf888",
         "d9313225f88406e5a55909c5aff5269a86a7a9531534f7da2e4c303d8a318a721c3c0c95956809532"
         "fcf0e2449a6b525b16aedf5aa0de657ba637b39",
         "feedfacedeadbeeffeedfacedeadbeefabaddad2",
         "522dc1f099567d07f47f37a32a84427d643a8cdcbfe5c0c97598a2bd2555d1aa8cb08e48590dbb3da"
         "7b08b1056828838c5f61e6393ba7a0abcc9f662",
         "76fc6ece0f4e1768cddf8853bb2d551b"),
    ]

    def test_encrypt_matches_the_vectors(self):
        for k, iv, pt, aad, ct, tag in self.CASES:
            with self.subTest(iv=iv, aad=bool(aad)):
                out = A.encrypt(bytes.fromhex(k), bytes.fromhex(iv),
                                bytes.fromhex(pt), bytes.fromhex(aad))
                self.assertEqual(out.hex(), ct + tag)

    def test_decrypt_returns_the_plaintext(self):
        for k, iv, pt, aad, ct, tag in self.CASES:
            with self.subTest(iv=iv):
                out = A.decrypt(bytes.fromhex(k), bytes.fromhex(iv),
                                bytes.fromhex(ct + tag), bytes.fromhex(aad))
                self.assertEqual(out.hex(), pt)

    def test_a_long_iv_takes_the_ghash_path(self):
        """Not 12 bytes, so J0 is derived by GHASH rather than by concatenation."""
        key, iv = bytes.fromhex("11" * 32), bytes.fromhex("22" * 20)
        blob = A.encrypt(key, iv, b"the long-iv branch has its own code")
        self.assertEqual(A.decrypt(key, iv, blob), b"the long-iv branch has its own code")


class TestAuthentication(unittest.TestCase):
    """The tag is the whole check. It has to actually reject."""

    def setUp(self):
        self.key = bytes.fromhex("33" * 32)
        self.iv = bytes.fromhex("44" * 12)
        self.sealed = A.encrypt(self.key, self.iv, b"a night, sealed", b"aad")

    def test_a_flipped_bit_in_the_ciphertext_is_refused(self):
        for i in (0, 5, len(self.sealed) - 1):
            bad = bytearray(self.sealed)
            bad[i] ^= 1
            with self.subTest(byte=i), self.assertRaises(ValueError):
                A.decrypt(self.key, self.iv, bytes(bad), b"aad")

    def test_changed_aad_is_refused(self):
        with self.assertRaises(ValueError):
            A.decrypt(self.key, self.iv, self.sealed, b"different")

    def test_a_truncated_blob_is_refused_rather_than_indexed_into(self):
        with self.assertRaises(ValueError):
            A.decrypt(self.key, self.iv, b"\x00" * 8)


class TestBlobFormat(unittest.TestCase):
    """The envelope js/gate.js already opens. Changing it strands every phone."""

    def test_it_round_trips(self):
        blob = A.seal("a night in kabukicho", b'{"id":"x"}\n', iterations=1000)
        self.assertEqual(A.unseal("a night in kabukicho", blob), b'{"id":"x"}\n')

    def test_the_wrong_passphrase_raises_rather_than_returning_garbage(self):
        blob = A.seal("right", b"secret", iterations=1000)
        with self.assertRaises(ValueError):
            A.unseal("wrong", blob)

    def test_the_shape_is_the_one_the_browser_expects(self):
        blob = A.seal("pw", b"x", iterations=1000)
        self.assertEqual(blob["kdf"], "PBKDF2-SHA256")
        self.assertEqual(blob["v"], 1)
        for k in ("salt", "iv", "ct"):
            self.assertIn(k, blob)
        import base64
        self.assertEqual(len(base64.b64decode(blob["salt"])), 16)
        self.assertEqual(len(base64.b64decode(blob["iv"])), 12)

    def test_the_default_iteration_count_is_the_sites(self):
        """250k is what data/leviathan.enc uses. A quieter number is a weaker file."""
        self.assertEqual(A.ITER, 250_000)

    def test_two_seals_of_the_same_text_differ(self):
        """Fresh salt and IV every time — otherwise the log leaks by comparison."""
        a = A.seal("pw", b"same", iterations=1000)
        b = A.seal("pw", b"same", iterations=1000)
        self.assertNotEqual(a["ct"], b["ct"])
        self.assertNotEqual(a["salt"], b["salt"])
        self.assertNotEqual(a["iv"], b["iv"])

    def test_a_blob_missing_a_field_is_named_not_crashed(self):
        with self.assertRaises(ValueError):
            A.unseal("pw", {"salt": "AA==", "iv": "AA=="})


if __name__ == "__main__":
    unittest.main()
