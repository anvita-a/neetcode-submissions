from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dicts = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            anagram_dicts[key].append(i)
        anagrams = []
        for j in anagram_dicts.values():
            anagrams.append(j)
        return anagrams



        