class Solution:
    def climbStairs(self, n: int) -> int:
        #base case
        prev1 = 1
        prev2 = 1

        #start with base case
        for curr in range(2, n + 1):
            temp = prev1
            prev1 = prev2 + prev1
            prev2 = temp
        
        return prev1

        
