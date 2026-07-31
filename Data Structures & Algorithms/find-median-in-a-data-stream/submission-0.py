"""
Naive approach first
"""
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        #just plain appending to list
        self.arr.append(num)

    def findMedian(self) -> float:
        if len(self.arr) == 1:
            return self.arr[0]

        #just sort in O(nlogn) and return median that way
        self.arr = sorted(self.arr)

        print(self.arr)

        if len(self.arr) % 2 == 0:
            lower = self.arr[(len(self.arr) // 2) - 1]
            higher = self.arr[len(self.arr) // 2]
            return ((lower + higher) / 2)
        else:
            return self.arr[len(self.arr) // 2]


        