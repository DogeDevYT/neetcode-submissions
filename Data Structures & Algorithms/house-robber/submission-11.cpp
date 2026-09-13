/*
Ok lets try a top-down DFS approach first. perfect now lets try bottom up. now lets try O(1) memory bottom up
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
        int rob1 = 0, rob2 = 0;

        for (int i = 0; i < nums.size(); i++) 
        {
            int maxRob = max(rob1 + nums[i], rob2);

            rob1 = rob2;
            rob2 = maxRob;
        }

        return rob2;
    }
};
