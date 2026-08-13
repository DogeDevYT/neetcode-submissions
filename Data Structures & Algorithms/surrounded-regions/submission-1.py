"""
Ok I think a flood-fill dfs soultion would be good here since we need to isolate squares of surrounding regions to fill 
with Xs

update, way easier way to do this is to work from outside in like pacific water flow which would allow us to use
some sort of temporary charcter lets use 'G' for good to skip

now bfs
"""

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def ff_dfs(row, col):
            to_visit = deque()
            to_visit.append((row, col))
            #mark original cell immeidatly
            board[row][col] = 'G'

            while to_visit:
                r, c = to_visit.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for direction in directions:
                    dr, dc = direction

                    new_r = r + dr
                    new_c = c + dc

                    #check if this new visitation is within bounds
                    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
                        continue
                    
                    #check if we have correct type
                    if board[new_r][new_c] != 'O':
                        continue
                    
                    to_visit.append((new_r, new_c))
                    board[new_r][new_c] = 'G'
        
        #iterate through borders and mark O cells that are connected as G so we can skip later
        for c in range(COLS):
            #top row
            if board[0][c] == 'O':
                ff_dfs(0, c)
            #bottom row
            if board[ROWS-1][c] == 'O':
                ff_dfs(ROWS-1, c)

        for r in range(ROWS):
            #left column
            if board[r][0] == 'O':
                ff_dfs(r, 0)
            #right column
            if board[r][COLS-1] == 'O':
                ff_dfs(r, COLS-1)
        
        #iterate through board and mark every leftover O as X and every leftover G as O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'G':
                    board[r][c] = 'O'
                
        