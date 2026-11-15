class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        r = len(height) - 1
        leftmax = 0
        rightmax = 0
        while l < r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if height[l] < height[r]:
                water += leftmax - height[l]
                l += 1
            else:
                water += rightmax - height[r]
                r -= 1
        return water

