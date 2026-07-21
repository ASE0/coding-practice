class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if m == l:
                if target == nums[r]:
                    return r
                else:
                    return -1
            if nums[m] > nums[l]:
                if target >= nums[l] and target <= nums[m]:
                    r = m
                else:
                    l = m
            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m
                else:
                    r = m