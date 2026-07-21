class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = []

        for i in nums:
            hashmap[i] += 1
        print(hashmap.items())
        for j in range(k):
            print(j)
            print("--")
            targetVal = max(hashmap.values())
            print(max(hashmap.values()))
            print(targetVal)

            for key, value in hashmap.items():
                print(key, value)
                if value == targetVal:
                    print(key)
                    print(res)
                    res.append(key)
                    break

            hashmap.pop(res[-1])
        return res