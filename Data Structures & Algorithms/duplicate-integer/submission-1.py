class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        refList = []
        for i in nums:
            if i not in refList:
                refList.append(i)
            else:
                return True
        return False