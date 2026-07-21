"""
I think after prooompting gemini and reading the hints I have an idea how to solve this. Since we want to avoid
placing queens in attacking squares, we can simplify by iterating in row major order and keeping track of:

1) columns under attack (since we're iterating in row major order)
2) positive diagonals (r + c), this will be the same value for all diagonals /
3) negative diagonals (r - c), this will be same value fo rall negative diagonals \

and basically we backtrack over these hash sets until we find something that works. After that I guess we just form
our return matrix chessboard thing.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set([])
        pos_diag = set([])
        neg_diag = set([])

        # Create a proper 2D list of characters: [['.', '.', '.', '.'], ...]
        board = [["."] * n for _ in range(n)]

        res = []

        def backtrack(r):
            #base case - we've reachend end of board so we just exit
            if r == n:
                # Convert character grid to list of strings: ["Q...", "..Q.", ...]
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            #check for fail conditions
            #i.e. checking to make sure we haven't placed a queen in current column, pos/neg diagonal
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                #place queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                board[r][c] = "Q"

                #backtrack
                backtrack(r + 1)

                #remove for backtrack
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

                board[r][c] = "."
        backtrack(0)
        return res
