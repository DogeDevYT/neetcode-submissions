class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost) + 1)]

        for curr in range(2, len(cost) + 1):
            dp[curr] = min(dp[curr-1] + cost[curr -1], dp[curr-2] + cost[curr-2])
        
        print(dp)
        
        return dp[len(cost)]