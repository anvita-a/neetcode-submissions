class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for i in s:
            if i.isalnum():
                s_list.append(i.lower())
        alnum_s = "".join(s_list)
        return (alnum_s == alnum_s[::-1])
        