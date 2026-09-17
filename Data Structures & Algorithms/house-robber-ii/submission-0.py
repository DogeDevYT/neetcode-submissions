"""
gain = max(nums[i] + dfs(i+2), dfs(i+1))

we can work around the situation with having circular queues by just having 2 lists: one excluding last element
and one excluding first element
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        #we're just going to have house robber I code here instead
        def hr(arr):
            memo = [-1] * len(arr)

            def dfs(i):
                if i >= len(arr): return 0

                if memo[i] != -1: return memo[i]

                memo[i] = max(dfs(i + 1), arr[i] + dfs(i + 2))
                return memo[i]
            
            return dfs(0)
        
        return max(hr(nums[:n-1]), hr(nums[1:]))