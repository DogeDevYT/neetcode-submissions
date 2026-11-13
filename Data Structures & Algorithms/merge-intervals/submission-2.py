"""
ok I think we can solve this one simply by reusing the merging logic from our last problem, insert intervals

ok actually we might have to start from prev and keep going from there
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #sort intervals by start time
        intervals.sort(key=lambda x: (x[0], x[1]))

        #placeholder new interval for merging purposes
        prev = intervals[0]

        #solution interval for final merged set
        solution = []

        for start, end in intervals:
            #merge intervals if new start < previous end   
            if start <= prev[1]:
                prev[0] = min(prev[0], start)
                prev[1] = max(prev[1], end)
            else:
                #flush prev to solution array and update prev to be equal to current
                solution.append(prev)
                prev = [start, end]
        
        #flush final prev
        solution.append(prev)
        
        return solution