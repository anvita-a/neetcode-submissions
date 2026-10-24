class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        max_window = 0
        window_dict = {}
        while r < len(s):
            if s[r] not in window_dict:
                window_dict[s[r]] = r
                r += 1
                
            else:
                pos = window_dict[s[r]]
                while l <= pos:
                    if s[l] in window_dict:
                        window_dict.pop(s[l])
                    l += 1
                window_dict[s[r]] = r
                r += 1

            window = r - l 
            max_window = max(window, max_window)
        return max_window









        