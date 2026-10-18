class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for i in set_nums:
            run = 0
            if i-1 in set_nums:
                continue
            start = i-1
            
            while start + 1 in set_nums:
                run += 1
                start += 1

            longest = max(longest, run)
            
        return longest
            

