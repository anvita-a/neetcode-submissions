class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = {}
        for i in s:
            count_dict[i] = count_dict.get(i,0) + 1
        for j in s:
            if count_dict[j] == 1:
                return s.index(j)
        return -1
        