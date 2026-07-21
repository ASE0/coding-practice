class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = []

        for i in nums:
            counts[i] += 1

        countValues = sorted(counts.items(), key=lambda x: x[1])
        print(countValues)
        countValues.reverse()

        for n in range(k):
            freq.append(countValues[n][0])
        return freq