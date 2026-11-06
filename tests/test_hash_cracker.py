import hashlib

import pytest

from hash_cracker import crack_with_wordlist, hash_word


def test_hash_word_matches_hashlib():
    assert hash_word("hello", "sha256") == hashlib.sha256(b"hello").hexdigest()


def test_unsupported_algorithm_raises():
    with pytest.raises(ValueError):
        hash_word("x", "md4")


def test_crack_finds_word(tmp_path):
    wl = tmp_path / "words.txt"
    wl.write_text("alpha\nbravo\ncharlie\n")
    target = hashlib.sha256(b"bravo").hexdigest()
    assert crack_with_wordlist(target, "sha256", str(wl)) == "bravo"


def test_crack_returns_none_when_absent(tmp_path):
    wl = tmp_path / "words.txt"
    wl.write_text("alpha\nbravo\n")
    assert crack_with_wordlist(hashlib.md5(b"zulu").hexdigest(), "md5", str(wl)) is None
