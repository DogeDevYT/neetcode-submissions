"""
Ok, so the most optimal way to implement this would be a min-heap with k elements. If we make it so that we get the 
Kth largest from the min heap, its O(1). However inserting m elements would require log(n) each. which means insertion
has mlog(n) time complexity.
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) #runs in O(n)

        #restrict to size k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: #only remove when we have too many elements
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0] #always return min index (0)
