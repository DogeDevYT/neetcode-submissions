"""
Looking through the hints, it looks like we need to use a backtracking algorithm but also keep track of j (partition index)
when j reaches end of index we return.

When we reach an index j, we need to check one of the 2 options:

1. partition at index j and start new string at j + 1 if palindrome
2. keep iterating at i
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        curr = []

        def backtrack(start):
            # base case 1 - j == len(s)
            if start == len(s):
                res.append(curr.copy())
                return
            
            #ok my mistake was instead of backtrackign index by index manually we can use a loop to code this up
            #efficiently
            for end in range(start, len(s)):
                substring = s[start: end + 1]

                if substring == substring[::-1]:
                    curr.append(substring) #choose
                    backtrack(end + 1) #call backtrack function
                    curr.pop() #unchoose
            
        backtrack(0)
        return res

