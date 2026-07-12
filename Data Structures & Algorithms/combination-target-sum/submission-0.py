"""
We can solve this problem much like the subsets problem that came before it. Basically we have a decision
tree on weather or not to include a certain number in our nums array and we just have to check weather or not it can 
be included but the trick is this time since we can pass in the same number an unlimited amount of times, we just
pass in the same nums array over and over but just decrement target
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curr_sum, curr_target):
            #base case 1 - we've found a solution
            if curr_target == 0:
                res.append(curr_sum.copy())
                return #always need a return!
            
            #base case 2 - we've overshot the array or subtracted too much
            if index >= len(nums) or curr_target < 0:
                return

            #decision to INCLUDE the current element and stay at current index
            curr_sum.append(nums[index])
            dfs(index, curr_sum, curr_target - nums[index])

            #decision to SKIP the current element and move onto next number
            curr_sum.pop()
            dfs(index + 1, curr_sum, curr_target)
        
        dfs(0, [], target)
        return res


