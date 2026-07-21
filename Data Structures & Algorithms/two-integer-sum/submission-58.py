class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        indexed_nums = enumerate(nums)
        nums_sorted = sorted(indexed_nums, key=lambda x: x[1])
        print(nums_sorted)
        while i < j:
            if nums_sorted[i][1] + nums_sorted[j][1] > target:
                j -= 1
            if nums_sorted[i][1] + nums_sorted[j][1] < target:
                i += 1
            if nums_sorted[i][1] + nums_sorted[j][1] == target:
                return sorted([nums_sorted[i][0], nums_sorted[j][0]])