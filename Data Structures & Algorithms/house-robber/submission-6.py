"""
lets try top down first:

the recurrence relation in question
profit[i] = max(nums[i] + profit[i - 2], profit[i-1])

base case would be smth like i < 0: return 0

Lets try to store max profit at some house i to memoize and fix the repeated recursion TLE

ok now lets try bottom up DP

ok now lets try bottom up DP with no memoizaiton (2 variables only)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            newRob = max(rob2, rob1 + nums[i])

            #slide our window forward
            rob1 = rob2
            rob2 = newRob
        
        return rob2