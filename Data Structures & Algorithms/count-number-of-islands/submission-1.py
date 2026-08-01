"""
Ok I think I know how to solve this problem, basically we just need to run a recursive dfs/backtracking approach
on each cell and mark a base case where we can't find any more 1s around us, we increment our count of islands.

I think I got it, we repatedly jump around and mark things as 0 so we can increment everything at the end to prevent
duplication

now lets try bfs flood fill
"""

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])



        def bfs(row, col):
            q = deque()

            #add our first elment to queue
            q.append((row, col))

            while q:
                r, c = q.popleft()

                grid[r][c] = '0'

                #dont forget python evaluates every string value not empty as truthy
                if r + 1 < NUM_ROWS and grid[r + 1][c] == '1':
                    q.append((r + 1, c))
                if r - 1 >= 0 and grid[r - 1][c] == '1':
                    q.append((r - 1, c))
                if c + 1 < NUM_COLS and grid[r][c + 1] == '1':
                    q.append((r, c + 1))
                if c - 1 >= 0 and grid[r][c - 1] == '1':
                    q.append((r, c - 1))
            
            return #rememeber this is our base case!
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        
        return islands
        