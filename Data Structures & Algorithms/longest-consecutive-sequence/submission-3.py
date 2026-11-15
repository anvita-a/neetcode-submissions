class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_window = 0
        for i in set_nums:
            window = 0
            if i-1 in set_nums:
                continue
            start = i-1
            while start + 1 in set_nums:
                window += 1
                start += 1
            max_window = max(max_window, window)
        return max_window


