class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            product = 1
            for num in range(len(nums)):
                if num == i:
                    continue
                product *= nums[num]
            output.append(product)
        return output