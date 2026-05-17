#include <algorithm>
#include <vector>

class Solution {
public:
    /*
    We can easily transform this problem to an instance of 2 sum where we use our current number

    we iterate through every number, assume index i:

    we need to find 2 indicies with numbers: j, k such that
    -nums[i] = nums[j] + nums[k]

    or in other words, -nums[i] is target and we have to run a 2 sum with left/right pointers
    */
    vector<vector<int>> threeSum(vector<int>& nums) {

        //don't forget to sort the array!
        std::sort(nums.begin(), nums.end());

        //store length
        int n = nums.size();

        //create solution vector
        std::vector<vector<int>> solution;

        //iteate through all numbers
        for (int i = 0; i < nums.size(); i++) 
        {
            //skip duplciate values of i
            if (i > 0 && nums[i] == nums[i-1]) continue;

            //get our target
            int target = -nums[i];

            //start our 2 pointer approach forrealskis
            // make sure to start left at index i + 1 to take avantage of our sorted order
            int l = i + 1, r = n - 1;

            // 2 pointer
            while (l < r) 
            {
                //store sum
                int sum = nums[l] + nums[r];
                if (sum < target) 
                {
                    l++;
                } else if (sum > target) 
                {
                    r--;
                } else 
                {
                    //new vector
                    std::vector<int> subsol = {nums[i], nums[l], nums[r]};
                    solution.push_back(subsol);

                    //dont forget to increment/decrement pointers!

                    //my initial solution assumed the left and right pointers wouldn't have duplciat elements
                    //we can fix this while pushing them forward/backward
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--; 
                    // (there may be multple combinations)

                    //edge case - one more
                    l++;
                    r--;
                }
            }
        }
        return solution;
    }
};
