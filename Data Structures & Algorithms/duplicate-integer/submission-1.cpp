#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //initialize hashmap to store seen elements
        std::unordered_map<int, int> seen;

        //iterate through elements and check if its seen or not
        for (int num : nums) 
        {
            //not found
            if (seen.find(num) == seen.end()) 
            {
                seen[num] = 1;
            } else 
            {
                return true;
            }
        }

        //we didn't find anything after one pass, return false
        return false; 
    }
};