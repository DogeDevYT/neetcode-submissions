/*
Ok so this one seems like a simple extension on Combination Sum I in that we increment index no matter what
and we need to sort our candidates beforehand and keep skipping duplicate ones in order to achieve max speed.
*/

#include <vector>
#include <algorithm>

class Solution {
private:
    void backtrack(int index, vector<int> candidates, int target, vector<int>& combo, vector<vector<int>>& res) 
    {
        if (target == 0) 
        {
            res.push_back(combo);
            return;
        }

        if (target < 0 || index >= candidates.size()) return;

        //decision to include
        combo.push_back(candidates[index]);
        backtrack(index + 1, candidates, target - candidates[index], combo, res);

        //decision to skip
        combo.pop_back();

        //skip all duplicate elements
        while (index + 1 < candidates.size() && candidates[index] == candidates[index + 1]) index++;

        backtrack(index + 1, candidates, target, combo, res);
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        std::vector<std::vector<int>> res = {};
        std::vector<int> combo = {};

        std::sort(candidates.begin(), candidates.end());

        backtrack(0, candidates, target, combo, res);

        return res;
    }
};
