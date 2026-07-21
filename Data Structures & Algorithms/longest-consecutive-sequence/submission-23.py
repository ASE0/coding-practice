class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 1

        sortedNums = sorted(set(nums))
        highest = 0
        current = 0
        for e in range(len(sortedNums[:-1])):
            if sortedNums[e + 1] == sortedNums[e] + 1:
                if current == 0:
                    current = 1
                current += 1
            else:
                highest = max(current, highest)
                current = 0
        return max(current, highest)