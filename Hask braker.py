import hashlib

def crack_hash(hash_to_crack, hash_type, wordlist_file):
    hash_to_crack = hash_to_crack.lower()  
    try:
        with open(wordlist_file, 'r', encoding="latin-1") as f:
            for word in f:
                word = word.rstrip('\r\n').strip()
                if hash_type == "md5":
                    hashedword = hashlib.md5(word.encode('latin-1')).hexdigest()
                elif hash_type == "sha1":
                    hashedword = hashlib.sha1(word.encode('latin-1')).hexdigest()
                else:
                    print("Unsupported hash type")
                    return

                if hashedword == hash_to_crack:
                    print(f"✅ Password found: {word}")
                    return  
        print("❌ Hash not found in wordlist")
    except FileNotFoundError:
        print("⚠️ Wordlist file not found")

hash_value = input("Enter the hash value to crack: ").strip()
hash_type = input("Enter the hash type (md5/sha1): ").strip().lower()
wordlist_file = input("Enter the path to the wordlist file: ").strip()

crack_hash(hash_value, hash_type, wordlist_file)
