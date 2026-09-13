/*
Ok lets try a top-down DFS approach first
*/

#include <vector>
#include <algorithm> //max

// dont ever actually do this live but we're going to do this because we're speedmaxxing
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> memo(nums.size(), -1);

        return dp(nums, memo, 0);
    }

    int dp(vector<int>& nums, vector<int>& memo, int i) 
    {
        //base case - out of bounds
        if (i >= nums.size()) return 0;

        if (memo[i] != -1) return memo[i];

        memo[i] = max(dp(nums, memo, i+1), nums[i] + dp(nums, memo, i+2));
        return memo[i];
    }
};
