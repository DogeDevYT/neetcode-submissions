"""
We want to build up the answer from smaller amounts
Heres the solution to my understanding:
1. Create a dp array dp where dp[a] represents the minimum coins needed ot make amount a
2. Initilize:
a) dp[0] = 0 (0 coins to make amount 0)
b) all other values as a large number (amount + 1)
3. For every amount a from 1 to amount:
For each coin c:
    if a - c >= 0:
        update dp[a] = min(dp[a], 1 + dp[a - c])
4. If dp[amount] is still large, return -1
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize our dp array as all a large number (amount + 1)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        print(dp)
        
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
