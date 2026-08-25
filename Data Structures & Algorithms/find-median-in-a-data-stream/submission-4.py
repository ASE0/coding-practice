class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float:
        median = 0
        self.stream = sorted(self.stream)
        if len(self.stream) % 2 == 0:
            median = (self.stream[(len(self.stream) // 2) - 1] + self.stream[(len(self.stream) // 2)]) / 2
        else:
            median = self.stream[len(self.stream) // 2]
        return median
        