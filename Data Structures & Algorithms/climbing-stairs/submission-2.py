from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        #base cases

        #overshot
        if n < 0:
            return 0
        
        #only one possibilty left
        if n == 0 or n == 1:
            return 1
        

        return self.climbStairs(n-1) + self.climbStairs(n-2)

        
