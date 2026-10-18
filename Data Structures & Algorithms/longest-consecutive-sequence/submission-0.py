class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        run = 0
        start = 0
        for i in set_nums:
            if i-1 in set_nums:
                continue
            else:
                start = i-1
            
            while start + 1 in set_nums:
                run += 1
                start += 1

            if run > longest:
                longest = run
            run = 0
        return longest
            

