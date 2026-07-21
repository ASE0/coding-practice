class Solution:
    def trap(self, height: List[int]) -> int:
        j, k = 0, len(height) - 1
        leftMax, rightMax = height[j], height[k]
        result = 0

        while j < k:
            if leftMax < rightMax:
                j += 1
                leftMax = max(leftMax, height[j])
                result += leftMax - height[j]
            else:
                k -= 1
                rightMax = max(rightMax, height[k])
                result += rightMax - height[k]
        return result