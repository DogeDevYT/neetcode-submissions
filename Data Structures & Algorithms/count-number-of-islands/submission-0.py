"""
Ok I think I know how to solve this problem, basically we just need to run a recursive dfs/backtracking approach
on each cell and mark a base case where we can't find any more 1s around us, we increment our count of islands.

I think I got it, we repatedly jump around and mark things as 0 so we can increment everything at the end to prevent
duplication
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])

        def dfs(row, col):
            grid[row][col] = '0'

            if row + 1 < NUM_ROWS and grid[row + 1][col] == '1':
                dfs(row + 1, col)
            if row - 1 >= 0 and grid[row - 1][col] == '1':
                dfs(row - 1, col)
            if col + 1 < NUM_COLS and grid[row][col + 1] == '1':
                dfs(row, col + 1)
            if col - 1 >= 0 and grid[row][col - 1] == '1':
                dfs(row, col - 1)
            
            return #rememeber this is our base case!
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands
        