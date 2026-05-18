#include <algorithm>

class Solution {
public:
    /*
    Basically we can use 2 pointer instead of prefix/postfix sums outright in a way that 2 pointer
    finds the "bottlenecks" of lesser height that we were trying to do with prefix/postfix sums

    move left/right pointers inwards while left < right
    */
    int trap(vector<int>& height) {
        int n = height.size();

        int l = 0; 
        int r = n - 1;

        //store maximums for left/right so we can use this for our calculation of trapping rainwater
        int left_max = 0; 
        int right_max = 0;

        //store this for calculation later
        int total_water = 0;

        //start using 2 pointer loop to fast calculate
        while (l < r) 
        {
            //store left/right maxes accordingly
            left_max = std::max(left_max, height[l]);
            right_max = std::max(right_max, height[r]);

            //check if "bottleneck" is left or right side accordingly
            if (height[l] < height[r]) 
            {
                //left side is bottleneck
                total_water += left_max - height[l];
                l++;
            } else 
            {
                //right side is bottleneck
                total_water += right_max - height[r];
                r--;
            }
        }

        return total_water;
    }
};
