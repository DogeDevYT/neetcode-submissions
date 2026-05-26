#include <set>

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        //create our window of things to see
        std::set<int> window;

        int l = 0;

        for (int r = 0; r < nums.size(); r++) 
        {
            //if our window > k, move l right to shrink
            if (r - l > k) 
            {
                window.erase(nums[l]);
                //forgot to increment left pointer how silly
                l++;
            }

            //if we find the number in our window, return true
            if (window.contains(nums[r])) return true;

            //add our number to seen
            window.insert(nums[r]);
        }

        //if we get here we need to return false
        return false;
    }
};