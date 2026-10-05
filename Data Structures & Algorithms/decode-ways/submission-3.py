"""
Basically we can keep recursing down such that

ways(s) = ways(s[1:]) + ways(s[2:])

now lets try bottom up dp (building answer from back of list)

so we can have 
dp[i] = 0 iff s[i] == 0

else

dp[i] = dp[i + 1] + dp[i + 2]
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        #store a list of all the possible character combinations
        numbers = set()

        #populate set of numbers
        for num in range(1, 27):
            numbers.add(str(num))
        
        #work from from the back
        dp1, dp2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            temp = 0
            if s[i] == '0': #0 can't be processed by itself
                temp = 0
            else:
                temp = dp1 #push forward
            
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                temp += dp2
            
            temp, dp1, dp2 = 0, temp, dp1
        
        #return the first dp elemenmt
        return dp1
        
        