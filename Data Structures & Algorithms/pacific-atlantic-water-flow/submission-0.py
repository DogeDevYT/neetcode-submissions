"""
I think a really simple recursive dfs solution would be good here to check if we had a direction (Atlantic/Pacific)
and keep recursing down until we either get to the ocean or are unable to move
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return [] #base case for emtpy grid
        
        pacific, atlantic = set(), set()

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(row, col, visit, prev):
            #cover base conditions of out of bounds, already visited, or can't flow up in reverse
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visit or heights[row][col] < prev:
                return
            
            #add our current element to the visited array 
            visit.add((row, col))

            curr_height = heights[row][col]

            #xplore our 4 directions
            dfs(row+1, col, visit, curr_height)
            dfs(row-1, col, visit, curr_height)
            dfs(row, col-1, visit, curr_height)
            dfs(row, col+1, visit, curr_height)
        
        #iterate over all our edge tiles and run our dfs algorithm
        for c in range(COLS):
            #top row - pacific
            dfs(0, c, pacific, heights[0][c])
            #bottom row - atlantic
            dfs(ROWS - 1, c, atlantic, heights[ROWS-1][c])

        for r in range(ROWS):
            #left row - pacific
            dfs(r, 0, pacific, heights[r][0])
            #right row - atlantic
            dfs(r, COLS - 1, atlantic, heights[r][COLS-1])
        
        #return intersection
        return list(pacific & atlantic)

