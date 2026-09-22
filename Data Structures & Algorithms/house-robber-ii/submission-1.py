class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        #create sub method for 1d house robber
        #profit[i] = max(profit[i+1], nums[i] + profit[i+2])
        def hr1(nums: List[int]) -> int:
            dp = [-1] * len(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            
            return dp[len(nums) - 1]
        
        return max(hr1(nums[1:]), hr1(nums[:len(nums)-1]))