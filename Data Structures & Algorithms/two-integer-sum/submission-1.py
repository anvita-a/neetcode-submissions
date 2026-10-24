class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in diff_dict:
                diff_dict[nums[i]] = i
            else:
                key = target - nums[i]
                small = min(i, diff_dict[key])
                big = max(i, diff_dict[key])
                return [small, big]

        