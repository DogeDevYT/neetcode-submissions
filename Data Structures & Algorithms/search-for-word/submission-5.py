"""
I think we can try a basic backtracking solution where we call our backtracking
function on each cell in the board and move up/down/left/right until we find
the element we're looking for or hit a base case of going out of bounds or
hitting a cell we've already seen or a cell that has a word that doesn't
make sense.
"""

class Solution:
    def __init__(self):
        self.seen = set([])
        self.n = -1
        self.m = -1
    def backtrack(self, board, word, row, col):
        if not word:
            return True #base case for empty word

        #check for bounds base case
        if row < 0 or row >= self.n or col < 0 or col >= self.m:
            return False
        
        #check for seen in current word base case
        if (row, col) in self.seen:
            return False
        
        #check if first character valid
        if board[row][col] != word[0]:
            return False
        
        if len(word) == 1:
            return True #we found last character to be True
            # and since the last character matches we can stop
    
        self.seen.add((row, col))

        ret = self.backtrack(board, word[1:], row - 1, col) or self.backtrack(board, word[1:], row + 1, col) or self.backtrack(board, word[1:], row, col - 1) or self.backtrack(board, word[1:], row, col + 1)

        #dont forget to actually backtrack here!
        self.seen.remove((row, col))
        
        return ret
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n = len(board)
        self.m = len(board[0])

        for r in range(len(board)):
            for c in range(len(board[0])):
                self.seen = set([])#reset
                if self.backtrack(board, word, r, c):
                    return True
        return False 
        #if we get to return above it means we definitely wont find
        #word