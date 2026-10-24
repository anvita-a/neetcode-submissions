class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        expected_sum = sum(range(0, len(nums) + 1))
        return expected_sum - actual_sum

        