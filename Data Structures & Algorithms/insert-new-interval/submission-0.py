"""
1. We first need to process intervals completely before newInterval
    - since these don't overlap, we can add them directly to the result
2. Next we need to get intervals that overlap with newInterval
    - While there is overlap, we can merge them by expanding newInterval
        new start = min(starts)
        new end = max(ends)
3. Intervals completely after the merged newInterval:
    - These also dont overlap so we can add them directly.
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        #add our completely merged interval
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res