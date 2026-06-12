class Solution {
public:
    /*
    We can repeat our same basic binary search here 

    remember to have our left and right pointers <= each other so we account for arrays with single elements
    we also need to remember that we should be calculating midpoint by doing (left + right) / 2 (cpp has integer divison)
    */
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) 
        {
            int mid = (left + right) / 2;

            int gurt = nums[mid];

            if (gurt < target) 
            {
                left = mid + 1;
            } else if (gurt > target) 
            {
                right = mid - 1;
            }
            else 
            {
                return mid;
            }
        }
        return -1;
    }
};
