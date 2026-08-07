"""
Ok, now I finally got it. I was visualizing it wrong, if we run a multi-source BFS, we can add all our treasure nodes
as source and work our way outwards from there. If we do it like this, we can quickly populate all our grids by
modifying in place
"""

from collections import deque

#define constants for fast access
WATER = -1
TREASURE = 0
LAND = 2**31 - 1

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])

        q = deque()

        #we can create a multi-source bfs solution by adding in all our sources and then running our population algorithm
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if grid[row][col] == TREASURE:
                    q.append((row, col))
        
        while q:
            curr_r, curr_c = q.popleft()


            #set our direcitons correctly
            for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dr, dc = direction

                new_r = curr_r + dr
                new_c = curr_c + dc

                #skip invalid bounds
                if new_r < 0 or new_r >= NUM_ROWS or new_c < 0 or new_c >= NUM_COLS: continue

                #skip non land
                if grid[new_r][new_c] != LAND: continue

                #add new relevant element
                q.append((new_r, new_c))
                grid[new_r][new_c] = grid[curr_r][curr_c] + 1 
            

