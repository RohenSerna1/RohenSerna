from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for i in strs:
        sorted_word = ''.join(sorted(i))

        anagrams[sorted_word].append(i)

    return list(anagrams.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))