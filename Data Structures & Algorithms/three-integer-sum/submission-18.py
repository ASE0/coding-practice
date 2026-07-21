class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        print(num)
        result = []
        
        for i in range(len(num)):
            j = 0
            k = len(num) - 1
            while j < k:
                if num[j] + num[k] < (num[i] * -1) or j == i:
                    #print(j, k, num[j], num[k], num[i], i)
                    j += 1
                    #print("Updated j")
                elif num[j] + num[k] > (num[i] * -1) or k == i:
                    #print(j, k, num[j], num[k], num[i], i)
                    k -= 1
                    #print("Updated k")
                else:
                    if sorted([num[j], num[k], num[i]]) not in result:
                        result.append(sorted([num[j], num[k], num[i]]))
                    j += 1
                    k -= 1
        return result