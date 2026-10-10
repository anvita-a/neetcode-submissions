class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict_s = {}
            dict_t = {}
            for i in s:
                dict_s[i] = dict_s.get(i, 0) + 1
            for j in t:
                dict_t[j] = dict_t.get(j, 0) + 1
            if dict_t == dict_s:
                return True
        return False
            
        