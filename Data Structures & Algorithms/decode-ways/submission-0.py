"""
Basically we can keep recursing down such that

ways(s) = ways(s[1:]) + ways(s[2:])
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        #store a list of all the possible character combinations
        numbers = set()

        #populate set of numbers
        for num in range(1, 27):
            numbers.add(str(num))
        
        #memoize solutions of ways to decode
        memo = {}
        
        #our actual recursive function
        def dfs(word):
            #if we get to base case we can add 1 becuase we're recombining
            if not word:
                return 1
            
            #use memoization
            if word in memo:
                return memo[word]
            
            #store total number of ways we can actually decode this
            #from our branching paths
            total = 0

            one = word[0]

            #cover case of one letter
            if one in numbers:
                total += dfs(word[1:])
            
            #cover case of 2 letters
            if len(word) >= 2 and word[:2] in numbers:
                total += dfs(word[2:])
            
            memo[word] = total
            return memo[word]
        
        return dfs(s)