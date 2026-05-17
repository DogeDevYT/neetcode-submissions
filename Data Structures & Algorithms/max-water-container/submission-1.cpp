#include <algorithm>

class Solution {
public:
    /*
    yeah I just pattern matched 2 poniter to this specfically:

    - move the smaller of the 2 heights towards center, or both if they're teh same height
    - do this until left pointer crosses right pointer
    - go over entire heights array
    - while doing this make sure to take max area
    */
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;

        int max_area = 0;

        while (l < r) 
        {
            int width = r - l;
            int height = std::min(heights[l], heights[r]); //take minimum height of both

            max_area = std::max(max_area, width*height); //take max area
            
            if (heights[l] < heights[r]) 
            {
                l++;
            } else if (heights[r] < heights[l]) 
            {
                r--;
            } else 
            {
                //same height on both, just move both i guess
                l++;
                r--;
            }
        }

        return max_area;
    }
};
