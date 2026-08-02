"""
Ok this problem seems really similar to number of islands problem from before, except this time we recurse with a relation of 1 + maxArea(grid(left, right, down, up)) and set current one to zero

Lets try a flood fill dfs approach first, for an extra challenge, lets not use recursion, but pure iterative dfs
with stack.
"""

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        stack = deque()
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])

        
        max_island_area = 0

        def dfs(row, col):
            #because we're changing max_island_area inside dfs, python assumes it has local scope so we need
            #to force interpreter to realize its scope is outside this function
            nonlocal max_island_area
            curr_island_area = 0
            stack.append((row, col))
            #remember to set the current island as 0 to prevent infinite loop
            grid[row][col] = 0

            while stack:
                r, c = stack.pop()

                #one major change is that we need to make sure we're incrementing our current island area
                #for the comparison at the end
                curr_island_area += 1

                #basically the idea is we add this to our visiting stack if we find a piece of land mass on the grid
                if r + 1 < NUM_ROWS and grid[r + 1][c]:
                    stack.append((r + 1, c))
                    grid[r + 1][c] = 0
                if r - 1 >= 0 and grid[r - 1][c]:
                    stack.append((r - 1, c))
                    grid[r - 1][c] = 0
                if c + 1 < NUM_COLS and grid[r][c + 1]:
                    stack.append((r, c + 1))
                    grid[r][c + 1] = 0
                if c - 1 >= 0 and grid[r][c-1]:
                    stack.append((r, c-1))
                    grid[r][c - 1] = 0
            
            #now that we've effectively explored the entire landmass, we can set max island area
            max_island_area = max(max_island_area, curr_island_area)

            return #dont froget to return
        
        #iterate through every single cell until we find an island 

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]:
                    dfs(r, c)
        
        return max_island_area