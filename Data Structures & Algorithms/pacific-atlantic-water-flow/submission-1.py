"""
I think a really simple recursive dfs solution would be good here to check if we had a direction (Atlantic/Pacific)
and keep recursing down until we either get to the ocean or are unable to move
"""

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return [] #base case for emtpy grid
        
        pacific, atlantic = set(), set()

        ROWS, COLS = len(heights), len(heights[0])

        def bfs(row, col, visit, prev):
            q = deque()

            q.append((row,col,prev))

            while q:
                r, c, prev = q.popleft()

                #cover base conditions of out of bounds, already visited, or can't flow up in reverse
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or heights[r][c] < prev:
                    continue
                
                #add our current element to the visited array 
                visit.add((r, c))

                curr_height = heights[r][c]

                #xplore our 4 directions
                q.append((r+1, c, curr_height))
                q.append((r-1, c, curr_height))
                q.append((r, c-1, curr_height))
                q.append((r, c+1, curr_height))
        
        #iterate over all our edge tiles and run our dfs algorithm
        for c in range(COLS):
            #top row - pacific
            bfs(0, c, pacific, heights[0][c])
            #bottom row - atlantic
            bfs(ROWS - 1, c, atlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            #left row - pacific
            bfs(r, 0, pacific, heights[r][0])
            #right row - atlantic
            bfs(r, COLS - 1, atlantic, heights[r][COLS-1])
        
        #return intersection
        return list(pacific & atlantic)

