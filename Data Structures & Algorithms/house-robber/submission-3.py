"""
lets try top down first:

the recurrence relation in question
profit[i] = max(nums[i] + profit[i - 2], profit[i-1])

base case would be smth like i < 0: return 0

Lets try to store max profit at some house i to memoize and fix the repeated recursion TLE
"""
class Solution:
    def __init__(self):
        self.max_profit = {}
    def dp(self, nums, i):
        #base case
        if i < 0: return 0

        if i in self.max_profit:
            return self.max_profit[i]

        #utilize memoization to prevent repated computations
        self.max_profit[i] = max(nums[i] + self.dp(nums, i - 2), self.dp(nums, i-1))

        return self.max_profit[i]
    def rob(self, nums: List[int]) -> int:
        return self.dp(nums, len(nums)-1)