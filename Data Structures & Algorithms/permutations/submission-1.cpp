/*
We can implement this problem by taking advantage of the fact that all elements are unique and we can just have a set
of elements that we visited in our current path and iterate over all elements every time and just pick another element
and backtrack based off that.
*/

#include <set>
#include <vector>

class Solution {
private:
    void backtrack(vector<int> nums, set<int>& used, vector<int>& curr_path, vector<vector<int>>& res) 
    {
        if (curr_path.size() == nums.size()) 
        {
            res.push_back(curr_path);
            return;
        }

        //need to iter over all numbers every time to generate solutions
        for (int i = 0; i < nums.size(); i++) 
        {
            if (used.contains(nums[i])) continue; //skip numbers we already used in path

            //decision to take current number
            used.insert(nums[i]);
            curr_path.push_back(nums[i]);

            //backtrack
            backtrack(nums, used, curr_path, res);

            //decision to not take current number
            used.erase(nums[i]);
            curr_path.pop_back();
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        std::set<int> used = {};
        std::vector<std::vector<int>> res = {};
        std::vector<int> curr_path = {};

        backtrack(nums, used, curr_path, res);
        return res;
    }
};
