class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)):
            if sortedNums[-1] >= target - sortedNums[i]:
                for j in range(i + 1, len(nums)):
                    if sortedNums[i] + sortedNums[j] == target:
                        first = nums.index(sortedNums[i])
                        nums[first] = ''
                        second = nums.index(sortedNums[j])
                        return [min(first, second), max(first, second)]