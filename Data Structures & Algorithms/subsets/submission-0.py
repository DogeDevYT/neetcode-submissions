class Solution:
    """We need to use backtracking to solve this
    we can solve this by using a nested dfs approach here. to achieve our backtracking
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        #we can think of i as the current element to visit
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res