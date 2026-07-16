/*
Ok so I think teh main reason this problem is hard is because we can have
duplicate entries so we can solve this by using the duplicate skipping
logic after sorting from the combinations problem
*/

#include <algorithm>
#include <vector>

class Solution {
private: 
    void backtrack(
        int index, 
        vector<int> nums, 
        vector<int>& curr_combo, 
        vector<vector<int>>& res) 
    {
        //return if we hit the end of the array
        if (index == nums.size()) 
        {
            res.push_back(curr_combo);
            return;
        }

        //decision to take
        curr_combo.push_back(nums[index]);
        backtrack(index + 1, nums, curr_combo, res);

        //decision to skip
        curr_combo.pop_back();

        //keep skipping duplicate elemnts
        while (index + 1 < nums.size() && nums[index] == nums[index + 1]) index++;

        backtrack(index + 1, nums, curr_combo, res);
    }
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        std::ranges::sort(nums);

        std::vector<int> curr_combo = {};
        std::vector<std::vector<int>> res = {};

        backtrack(0, nums, curr_combo, res);
        return res;
    }
};
