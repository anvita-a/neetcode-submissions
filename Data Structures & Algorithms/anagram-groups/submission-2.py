from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in anagram_dict:
                anagram_dict[key].append(i)
            else:
                anagram_dict[key] = [i]
        return list(anagram_dict.values())



        