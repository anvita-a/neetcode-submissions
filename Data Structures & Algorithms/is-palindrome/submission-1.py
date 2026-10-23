class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for i in s:
            if i.isalnum():
                s_list.append(i.lower())
        alnum_s = "".join(s_list)
        l = 0
        r = len(alnum_s) - 1
        while l < r:
            if alnum_s[l] != alnum_s[r]:
                return False
            l += 1
            r -= 1
        return True
        