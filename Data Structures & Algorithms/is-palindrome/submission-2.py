class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lst = []
        for i in s:
            if i.isalnum():
                s_lst.append(i.lower())
        l = 0
        r = len(s_lst) - 1
        while l < r:
            if s_lst[l] != s_lst[r]:
                return False
            l += 1
            r -= 1
        return True