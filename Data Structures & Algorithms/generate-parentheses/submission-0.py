"""
I think the method here is to run naive backtracking like with subsets but we have to choose weather to open/close
parenthesis by tracking curr open and curr closed, basically check if both <= n
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(currOpen, currClosed):
            #base case where we have same amoutn of currOpena dn curr closed == n
            if currOpen == currClosed == n:
                res.append("".join(curr))
                return
            
            #we need to backtrack a little differently here, since we're always guarenteed to have well formed
            #parenthesis if we backtrack open first we need to run that first and then just run < n checks for 
            #both open and closed 

            if currOpen < n:
                curr.append("(")
                backtrack(currOpen + 1, currClosed)
                #undo choice
                curr.pop()
            
            #leave it as less than currOpen so that we dont create un well formed parenthesis
            if currClosed < currOpen:
                curr.append(")")
                backtrack(currOpen, currClosed + 1)
                #undo choice
                curr.pop()
            
        backtrack(0, 0)
        return res