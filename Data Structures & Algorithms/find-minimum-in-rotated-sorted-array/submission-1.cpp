#include <algorithm>

class Solution {
public:
    /*
    Ok so I think I need to reframe my thinking from finding the actual target NUMBER and rather finding the inflection
    point where the array has been shifted. What I mean is that I need to check for when the current number is greater
    than or equal to the left bound because if this is true, we're in the Ramp A basically where there are 2 ramps

    Ramp A = false start where we have rotatted n indicies forward
    Ramp B = true start where we need to find the first element here.

    we check by utilizing a preliminary check at first where we see if the left bound is less than the right bound
    (since we start at start/end of array we'll know we're in correct zone once this is true)

    and if its not then we check if current mid >= nums[left bound] and if so we need to move left bound to current
    + 1 because that means we're still on the A Ramp (since we start off at 0 and len - 1 for l and r respectively
    we know that we would be in the false start/ramp a area)

    otherwise we just need to move right bound to mid - 1 since then we know we're dead on the correct zone
    */
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;

        int lowest = nums[0];

        while (l <= r) 
        {
            //check if we're in the correct true start segment so we can just pull first element
            if (nums[l] < nums[r]) 
            {
                lowest = std::min(lowest, nums[l]);
                break;
            }

            //now we can actually do our ramp finding trick
            int mid = (l + r) / 2;

            //update lowest
            lowest = std::min(lowest, nums[mid]);

            if (nums[mid] >= nums[l]) 
            {
                l = mid + 1;
                //we're checking if middle is greater than nums l becuase we're starting at hte false start
            }
            else 
            {
                r = mid - 1;
                //if our left bound is greater than middle we know we're on right ramp so we can isolate our
                //actual number by closing out on right bound
            }
        }
        return lowest;
    }
};
