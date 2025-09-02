# Basic Hash Cracker 🔑

A simple Python tool to crack MD5 and SHA1 hashes using a wordlist.
This project is perfect for learning hashing, password security, and brute-force techniques in cybersecurity.

Features

Supports MD5 and SHA1 hashes.

Uses a custom wordlist (like rockyou.txt) for cracking.

Stops immediately when the password is found.

Handles large wordlists with proper encoding (latin-1).

Prints clear messages if hash not found or file missing.

Installation

Clone the repository:

git clone https://github.com/your-username/Basic-Hash-Cracker.git


Navigate to the project folder:

cd Basic-Hash-Cracker


Make sure you have Python 3 installed.

Usage

Run the script:

python hash_cracker.py


Enter the hash value to crack:
e.g., 5f4dcc3b5aa765d61d8327deb882cf99

Enter the hash type (md5/sha1):
e.g., md5

Enter the path to the wordlist file:
e.g., rockyou.txt or mini_wordlist.txt

Example Output:

✅ Password found: password

Example Wordlist

You can use a mini wordlist for testing:

123456
password
letmein
admin
welcome


Or use the famous rockyou.txt for full testing.

Notes

Large wordlists may take time to brute-force.

Only attempt cracking hashes you are authorized to test.

Encoding is set to latin-1 for compatibility with common wordlists.

License

This project is for educational purposes only. Unauthorized use on others’ data is strictly prohibited.
