from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dicts = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            anagram_dicts[key].append(i)
        return list(anagram_dicts.values())



        