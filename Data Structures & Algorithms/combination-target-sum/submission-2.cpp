/*
We can solve this problem by using kinda the same decision tree type backtracking as the subsets problem that 
came before it. Basically we just have to decide on 2 choices: 

1) take the number and stay on teh same index (remember to decrement target)
2) skip the number and move onto next index

and remembering to check for the followin base cases:
1) we've hit the target, append our current vector to solution and return
2) we've hit end of array, return
3) we've decremented below 0 for target sum, return
*/
class Solution {
private:
    void backtrack(int index, vector<int>& curr_sum, int curr_target, vector<int> nums, vector<vector<int>>& result) 
    {
        if (curr_target == 0) 
        {
            result.push_back(curr_sum);
            return;
        }

        if (curr_target < 0 || index >= nums.size()) return;

        //decision to include and keep on same index
        curr_sum.push_back(nums[index]);
        backtrack(index, curr_sum, curr_target - nums[index], nums, result);

        //decision to skip and increment index
        curr_sum.pop_back();
        backtrack(index + 1, curr_sum, curr_target, nums, result);
    }
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        std::vector<std::vector<int>> result = {};
        std::vector<int> curr_sum = {};

        backtrack(0, curr_sum, target, nums, result);
        return result;
    }
};
