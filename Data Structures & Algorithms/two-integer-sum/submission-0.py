class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in diff_dict:
                diff_dict [nums[i]] = i
            else:
                if i > diff_dict[target - nums[i]]:
                    return [diff_dict[target - nums[i]], i]
                else:
                    return [i, diff_dict[target - nums[i]]]
        