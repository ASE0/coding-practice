class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = []

        for i in nums:
            hashmap[i] += 1

        for j in range(k):
            targetVal = max(hashmap.values())

            for key, value in hashmap.items():
                print(key, value)
                if value == targetVal:
                    res.append(key)
                    break
            hashmap.pop(res[-1])
        return res