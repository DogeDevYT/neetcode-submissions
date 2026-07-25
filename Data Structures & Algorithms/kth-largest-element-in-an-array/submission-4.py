"""
So right away, I see a cop out solution where we sort first and then return index k

Ok, the acutal solution looks like a min-heap of size k where we just pop the top off the stack because
thats guarenteed to be the kth largest element in a heap of size k
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        #populate our heap to trim to size k later
        for num in nums:
            heapq.heappush(min_heap, num)
        
        #trim until size k
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return min_heap[0] #return top
