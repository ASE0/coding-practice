class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j, k = 0, len(heights) - 1
        area = min(heights[j], heights[k]) * (k)
        while j < k:
            if heights[j] < heights[k]:
                j += 1
            else:
                k -= 1
            area = max(min(heights[j], heights[k]) * (k - j), area)
        return area