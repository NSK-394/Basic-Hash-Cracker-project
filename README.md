# Basic Hash Cracker

![tests](https://github.com/NSK-394/Basic-Hash-Cracker-project/actions/workflows/tests.yml/badge.svg)

A small, educational dictionary-based hash lookup tool. Given a hash and a wordlist, it hashes each candidate word and reports the first match. It's a coursework demo of **why unsalted, fast hashes (MD5 and the SHA family) are a poor way to store passwords** — a laptop can test millions of candidates per second against them.

> **Legal & ethical use:** only run this against hashes from systems you own or are explicitly authorized to test (your own practice data, a CTF, a lab). It is not a tool for attacking other people's credentials.

## Features
- Dictionary attack against **MD5, SHA-1, SHA-256, SHA-512**
- Simple CLI with a selectable algorithm
- Clear exit codes (0 = found, 2 = not found) so it scripts cleanly

## Usage
```bash
# md5("password") -> look it up in a wordlist
python hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 wordlist.txt -a md5

# sha256
python hash_cracker.py <hexdigest> rockyou.txt -a sha256
```

## Why dictionary, not brute force
A dictionary attack works because real passwords are rarely random — they come from a predictable space (common passwords, names, leaked lists). That's the actual lesson here: the weakness is password *choice* and the use of fast, unsalted hashes, not raw compute. Proper password storage uses a slow, salted KDF (bcrypt, scrypt, Argon2) specifically to make this kind of lookup impractical.

## Limitations
- Dictionary lookup only — it finds a password only if it's in the wordlist you give it
- No salt handling (these demo hashes are unsalted; real systems should be salted)
- Single-threaded; it's a teaching tool, not a performance tool

## Tests
```bash
pip install pytest && pytest -q
```
