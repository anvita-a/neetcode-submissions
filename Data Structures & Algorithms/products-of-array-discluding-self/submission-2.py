

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1] * l
        right = [1] * l
        for i in range(1, l):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(l-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        return [i * j for i, j in zip(left, right)]



