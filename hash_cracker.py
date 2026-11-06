"""Educational dictionary-based hash lookup tool.

Given a hash and a wordlist, it hashes each candidate word and reports a match.
This is a coursework demo of why unsalted fast hashes (MD5/SHA-family) are a poor
way to store passwords. Use it only on hashes from systems you own or are
authorized to test, e.g. your own practice data or a CTF.
"""

from __future__ import annotations

import argparse
import hashlib

ALGORITHMS = ("md5", "sha1", "sha256", "sha512")


def hash_word(word: str, algorithm: str) -> str:
    if algorithm not in ALGORITHMS:
        raise ValueError(f"unsupported algorithm: {algorithm} (choose from {', '.join(ALGORITHMS)})")
    return hashlib.new(algorithm, word.encode("utf-8", "surrogatepass")).hexdigest()


def crack_with_wordlist(target_hash: str, algorithm: str, wordlist_path: str) -> str | None:
    """Return the first word in the wordlist whose hash matches, else None."""
    target = target_hash.strip().lower()
    with open(wordlist_path, encoding="latin-1") as f:
        for line in f:
            word = line.rstrip("\r\n")
            if hash_word(word, algorithm) == target:
                return word
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Dictionary-based hash lookup (educational)")
    ap.add_argument("hash", help="the hex digest to look up")
    ap.add_argument("wordlist", help="path to a newline-separated wordlist")
    ap.add_argument("-a", "--algorithm", default="md5", choices=ALGORITHMS)
    args = ap.parse_args(argv)

    try:
        found = crack_with_wordlist(args.hash, args.algorithm, args.wordlist)
    except FileNotFoundError:
        print(f"Wordlist not found: {args.wordlist}")
        return 1
    if found is None:
        print("No match found in wordlist")
        return 2
    print(f"Match: {found}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
