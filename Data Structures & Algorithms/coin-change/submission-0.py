"""
Ok I think we can solve this with a simple memoization first
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        """
        base cases:
        1) we've gotten < 0 return -1
        2) we've gotten exactly 0, return 1
        3) already in memo, return memo
        """
        def dfs(curr_amount: int) -> int:
            #going to have to hard code this failure case
            if curr_amount < 0:
                return 10001
            
            if curr_amount == 0:
                return 0
            
            if curr_amount in memo:
                return memo[curr_amount]
            
            min_cost = float('inf')
            
            #iterate through all possibilities and select least
            for coin in coins:
                min_cost = min(min_cost, 1 + dfs(curr_amount - coin)) 
            
            memo[curr_amount] = min_cost
            return memo[curr_amount]
        
        final_cost = dfs(amount)
        return final_cost if final_cost <= 10000 else -1