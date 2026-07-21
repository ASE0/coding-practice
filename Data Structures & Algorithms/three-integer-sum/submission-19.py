class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        result = []
        for i in range(len(num)):
            j = 0
            k = len(num) - 1
            while j < k:
                if num[j] + num[k] < (num[i] * -1) or j == i:
                    j += 1
                elif num[j] + num[k] > (num[i] * -1) or k == i:
                    k -= 1
                else:
                    if sorted([num[j], num[k], num[i]]) not in result:
                        result.append(sorted([num[j], num[k], num[i]]))
                    j += 1
                    k -= 1
        return result