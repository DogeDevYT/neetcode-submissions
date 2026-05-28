#include <algorithm>
#include <vector>

class Solution {
public:
    /*
    Yeah so for this one honestly I think we just need to have a simple nested for loop such that
    for i in range(nums)
    for j in range(i + 1, nums)

    we basically use left/right pointer after sorting for 2 sum such that

    target = nums[i] + nums[j] + nums[l] + nums[r]
    */
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        //sort everything beforehand
        std::sort(nums.begin(), nums.end());

        std::vector<vector<int>> sol;

        for (int i = 0; i < nums.size(); i++) 
        {
            //skip duplicate values at index of i
            if (i > 0 && nums[i] == nums[i-1]) continue;

            for (int j = i + 1; j < nums.size(); j++) 
            {
                //skip duplicate values at index j
                if (j > i + 1 && nums[j] == nums[j-1]) continue;

                //initalize left/right pointers
                int l = j + 1;
                int r = nums.size() - 1;

                while (l < r) 
                {
                    //cover integer overflow bug
                    long long curr = (long long) nums[l] + nums[r] + nums[i] + nums[j];
                    //edit pointers accordingly
                    if (curr < target) 
                    {
                        l++;
                    } else if (curr > target) 
                    {
                        r--;
                    } else 
                    {
                        std::vector<int> gurt = {nums[i], nums[j], nums[l], nums[r]};
                        sol.push_back(gurt);

                        //in case we get the same element
                        while (l < r && nums[l] == nums[l+1]) l++;
                        while (l < r && nums[r] == nums[r-1]) r--;

                        //increment pointers to keep searching - one more time
                        l++;
                        r--;
                    }
                }
            }
        }
        return sol;
    }
};