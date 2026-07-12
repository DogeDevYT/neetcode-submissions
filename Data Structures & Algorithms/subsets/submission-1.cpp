
/*
Since we're doing backtracking, I think we need to use dfs basically to get all possible combinations on our decision
tree of including/not including element, this seems to be motivation for dp
*/

#include <vector>

class Solution {
private:
    void dfs(int i, vector<int>& subset, vector<vector<int>>& res, vector<int>& nums) 
    {
        if (i >= nums.size()) 
        {
            res.push_back(subset);
            return;
        }

        //decision to include nums[i]
        subset.push_back(nums[i]);
        dfs(i + 1, subset, res, nums);

        //decision to skip nums[i]
        subset.pop_back();
        dfs(i + 1, subset, res, nums);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        std::vector<int> subset;
        std::vector<std::vector<int>> result;
        dfs(0, subset, result, nums);

        return result;
    }
};
