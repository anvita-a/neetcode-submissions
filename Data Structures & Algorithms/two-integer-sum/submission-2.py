class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in diff_dict:
                diff_dict[nums[i]] = i
            else:
                small = min(i, diff_dict[target-nums[i]])
                large = max(i, diff_dict[target-nums[i]])
                return [small, large]

        