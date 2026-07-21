class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        round_ = 0
        while l <= r:
            round_ += 1
            print(f"round: {round_}")
            m = (r + l) // 2
            if nums[m] == target:
                print("done")
                return m
            if m == l:
                if target == nums[r]:
                    return r
                else:
                    return -1
            if nums[m] > nums[l]:
                print("--")
                if target >= nums[l] and target <= nums[m]:
                    print("---")
                    r = m
                else:
                    print("----")
                    l = m
            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m
                else:
                    r = m
            print(nums[l], nums[r])
            print(f"m: {m}, l: {l}, r: {r}")