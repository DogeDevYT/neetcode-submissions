"""
Ok this seems like another multi-source BFS question. we can start off by taking a count of all the rotten fruits
and then do quick sanity check if one of them is rotten at all then we can start processing

I think I figured it out, when we increment time, we dont do so on every pop, we need to increment whenever we
hit our entire "level" of queue like that one tree problem
"""

EMPTY = 0
FRESH = 1
ROTTEN = 2

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        #iterate over entire grid, while adding rotten fruits as sources of our multi source bfs
        # and having fresh oranges iterate our counter
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH:
                    fresh += 1
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
        
        #add fresh > 0 for skipping unecessary operations
        while q and fresh > 0:
            time += 1
            """
            We need to have the level of rot transferred at each iteration before advancing our timestamp value
            """
            for i in range(len(q)):
                row, col = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for direction in directions:
                    dr, dc = direction

                    new_r = row + dr
                    new_c = col + dc

                    #skip out of bounds
                    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS: continue

                    #skip non fresh parts
                    if grid[new_r][new_c] != FRESH: continue

                    #mark out and add to queue for next cycle
                    grid[new_r][new_c] = ROTTEN
                    q.append((new_r, new_c))
                    fresh -= 1
        
        #if we have fresh left, we need to return -1 becuase its impossible
        if fresh > 0:
            return -1
        return time 