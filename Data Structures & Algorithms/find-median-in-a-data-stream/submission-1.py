"""
Ok, after reading the hints about splitting into 2 halves, I got a devious idea. There are 2 cases here:

1) Odd Number of elements:

In this case, after dividing the array into 2 halves, we simply return the last/first element from the left/right half
depending on which is bigger.

2) Even Number of Elements:

In this case, we need to make a max heap out of the left half and min heap out of the right half so that we can pop
from these heaps in O(1).

Balancing the heaps/addition:

Since we can't rely on sorting, we need to account for adding the elements in O(logn) using the heaps. We can do this
by checking if our number is > top of min heap. otherwise we push into max heap.

If the size difference becomes > 1. We resolve this by popping an element from larger heap and putting in smaller heap.
"""
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if len(self.min_heap) > 0 and num > self.min_heap[0]:
            print("adding " + str(num) + " to min heap")
            heapq.heappush(self.min_heap, num)
        else:
            print("adding " + str(-num) + " to max heap")
            heapq.heappush(self.max_heap, -num)

        print("min heap: " + str(self.min_heap) + " max heap: " + str(self.max_heap))
        
        #now we need to rebalance if our sizes are too off
        size_diff = len(self.min_heap) - len(self.max_heap)

        print("size diff: " + str(size_diff))

        if size_diff > 1:
            print("rebalancing (removing from min heap)")
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif size_diff < -1:
            print("rebalancing (removing from max heap)")
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        total_size = len(self.min_heap) + len(self.max_heap)
        #print("min heap: " + str(self.min_heap) + " max heap: " + str(self.max_heap) + " total_size: " + str(total_size))

        if total_size % 2 == 0:
            #looks like this was causing the issue
            # i.e. when we pop from heaps they're gone forever 
            # I can't believe I missed that instead of using peek
            lower = -self.max_heap[0]
            higher = self.min_heap[0]

            return (lower + higher) / 2
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]


        