"""
lets try top down first:

the recurrence relation in question
profit[i] = max(nums[i] + profit[i - 2], profit[i-1])

base case would be smth like i < 0: return 0

Lets try to store max profit at some house i to memoize and fix the repeated recursion TLE

ok now lets try bottom up DP
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        dp = [-1] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[len(nums)-1]