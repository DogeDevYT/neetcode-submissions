"""
Ok, for this problem, I think we can create a specific object to denote 2 things: 

1) distance from origin (we can leave in squared form since we just want to compare magnitudes)
2) actual point coordanites

we can create this object for each point and then we can simply call Python's heapify to create
a min heap for this.

Ok update, we dont need a class we can just do this using a max heap implementation with tuples
if we leave it as
(-dist, point)
"""

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            dist = point[0]**2 + point[1]**2

            heapq.heappush(max_heap, (-dist, point))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [item[1] for item in max_heap]