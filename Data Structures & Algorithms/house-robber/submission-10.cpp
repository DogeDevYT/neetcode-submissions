/*
Ok lets try a top-down DFS approach first. perfect now lets try bottom up
*/

#include <vector>
#include <algorithm> //max

// dont ever actually do this live but we're going to do this because we're speedmaxxing
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;
        if (nums.size() == 1) return nums[0];

        vector<int> memo(nums.size(), -1);

        return dp(nums, memo, 0);
    }

    int dp(vector<int>& nums, vector<int>& memo, int i) 
    {
        memo[0] = nums[0];
        memo[1] = max(memo[0], nums[1]);

        for (int i = 2; i < nums.size(); i++) 
        {
            memo[i] = max(memo[i-1], nums[i] + memo[i-2]);
        }

        return memo[nums.size() - 1];
    }
};
