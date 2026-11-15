class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        lst = []
        for i in range(len(sort_nums)):
            if i >= 1 and sort_nums[i-1] == sort_nums[i]:
                continue
            fixed = sort_nums[i]
            two_sum = -fixed
            l = i + 1
            r = len(sort_nums) - 1
            while l < r:
                if sort_nums[l] + sort_nums[r] < two_sum:
                    l += 1
                elif sort_nums[l] + sort_nums[r] > two_sum:
                    r -= 1
                else:
                    lst.append([sort_nums[l], sort_nums[r], fixed])
                    while l < r and sort_nums[l+1] == sort_nums[l]:
                        l += 1
                    while r < len(sort_nums)-1 and sort_nums[r-1] == sort_nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return lst
                    


       


        
        