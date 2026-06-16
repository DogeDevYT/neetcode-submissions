class Solution {
public:
    /*
    Ok I think I got the "ramps" pattern for rotated arrays that are sorted for Binary Search.

    Basically we need to check if nums[left] <= nums[mid] because we're trying to find teh inflection point, in other
    words, the point where its sorted. After we find this we can make a decision to check for the 

    false start (initial condition true): check if nums[left] <= target <= nums[mid]: set right to mid - 1
    true start (initial condition true): check if nums[mid] <= target <= nums[right]: set left to mid + 1

    and if the false start/true start conditions are false, we can set l to mid + 1, r to mid - 1 respectively 
    */
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) 
        {
            int mid = (l + r) / 2;

            //dont forget to actually check for element
            if (nums[mid] == target) return mid;

            if (nums[l] <= nums[mid]) 
            {
                if (nums[l] <= target && target <= nums[mid]) 
                {
                    r = mid - 1;
                } else 
                {
                    l = mid + 1;
                }
            } else 
            {
                if (nums[mid] <= target && target <= nums[r]) 
                {
                    l = mid + 1;
                } else 
                {
                    r = mid - 1;
                }
            }
        }
        return -1; //element DNE
    }
};
