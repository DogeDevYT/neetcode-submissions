from functools import cache

class Solution:
    #@cache
    def climbStairs(self, n: int) -> int:
        combos = 0

        #dp
        dp = [0 for i in range(n + 1)]

        #base case
        dp[0] = 1
        dp[1] = 1

        #start with base case
        for curr in range(2, n + 1):
            dp[curr] = dp[curr-1] + dp[curr-2]
        
        return dp[n]

        
