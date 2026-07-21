class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = set()
        for i in range(len(nums)):
            target = nums[i]
            trgt = -target
            sorted_subset = sorted(nums[:i] + nums[i+1:])
            k = 0
            j = len(sorted_subset) - 1
            while k < j:
                if sorted_subset[k] + sorted_subset[j] > trgt:
                    j -= 1
                elif sorted_subset[k] + sorted_subset[j] < trgt:
                    k += 1
                else:
                    final_list.add(tuple(sorted([target, sorted_subset[k], sorted_subset[j]])))
                    k += 1
                    j -= 1
        return [list(triplet) for triplet in final_list]