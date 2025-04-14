from collections import Counter

def ransomNote(rN: str, magazine: str) -> bool:
    ransom = Counter(rN)
    magazine = Counter(magazine)

    for letter, count in ransom.items():
        if magazine[letter] < count:
            return False
    return True

print(f"example 1:  {ransomNote("a", "b")}")
print(f"example 2:  {ransomNote("aa", "ab")}")
print(f"example 3:  {ransomNote("abc", "cbad")}")
print(f"example 4:  {ransomNote("aa", "aab")}")