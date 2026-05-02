#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //create array of seen
        std::unordered_map<int, int> seen;

        //iterate for every num in nums
        for (int i = 0; i < nums.size(); i++) 
        {
            //get the complement (target sum - current)
            int complement = target - nums[i];

            //check if we already found the element we needed
            if (seen.contains(complement)) 
            {
                return {seen[complement], i};
            }

            //if we haven't seen an element, add it to array
            if (!seen.contains(nums[i])) 
            {
                seen[nums[i]] = i;
            }
        }
    }
};
