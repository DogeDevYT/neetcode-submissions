"""
lets try top down first:

the recurrence relation in question
profit[i] = max(nums[i] + profit[i + 2], profit[i+1])

base case would be smth like i >= len(nums): return 0

Lets try to store max profit at some house i to memoize and fix the repeated recursion TLE
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums): return 0

            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        
        return dfs(0)