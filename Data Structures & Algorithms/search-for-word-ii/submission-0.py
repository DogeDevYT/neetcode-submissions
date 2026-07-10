"""
Ok I think an easy way to solve this is to create a trie, parse all 
of our words into the trie and then keep going through
our tree for each cell and its respective neighbors
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def dfs(self, r, c, node, word, res, visit, ROWS, COLS, board):
        #quick boundary check
        if (r < 0 or c < 0 or r >= ROWS or
            c >= COLS or (r, c) in visit or
            board[r][c] not in node.children):
            return
        
        visit.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.isWord: res.add(word)

        self.dfs(r + 1, c, node, word, res, visit, ROWS, COLS, board)
        self.dfs(r - 1, c, node, word, res, visit, ROWS, COLS, board)
        self.dfs(r, c + 1, node, word, res, visit, ROWS, COLS, board)
        self.dfs(r, c - 1, node, word, res, visit, ROWS, COLS, board)

        visit.remove((r, c))
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        #iterate through every row/column and hit the dfs
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                self.dfs(r, c, root, "", res, visit, ROWS, COLS, board)
        
        return list(res)