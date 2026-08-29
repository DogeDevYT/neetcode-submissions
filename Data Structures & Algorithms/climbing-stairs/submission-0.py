class Solution:
    def __init__(self):
        self.stored = {}
    def climbStairs(self, n: int) -> int:
        #base cases

        #overshot
        if n < 0:
            return 0
        
        #only one possibilty left
        if n == 0 or n == 1:
            return 1
        
        #memoized dp!
        if n in self.stored:
            return self.stored[n]
        

        self.stored[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return self.stored[n]

        
