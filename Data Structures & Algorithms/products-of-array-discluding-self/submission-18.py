class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            product = 1
            print(nums[:i] + nums[i + 1:])
            for num in nums[:i] + nums[i + 1:]:
                product *= num
            output.append(product)
        return output