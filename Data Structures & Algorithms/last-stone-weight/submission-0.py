"""
I think we can easily solve htis problem with a max-heap data structure

edit: I have to use negative values to get max heap behavior with min heap
"""

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #invert heap to emulate max heap behavior with min heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        #run the stones smash heap while 2 remain
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap) #heaviest stone
            x = -heapq.heappop(max_heap) #2nd heaviest stone

            if y != x:
                #push remaining weight onto heap
                heapq.heappush(max_heap, -(y - x))
        
        #return last stones weight or 0 if none left
        return -max_heap[0] if max_heap else 0