class Solution {
public:
    /*
    PATTERN MATCH GO:

    Basically we just do 2 rounds of binary search:
    
    round 1:
    check for rows' first entry being less than target and rows' last entry being more than target

    round 2:
    do binary search on the induvidual row and find element
    */
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        //store m and n for later
        int m = matrix.size();
        int n = matrix[0].size();

        //binary search on the row itself
        int l = 0;
        int r = m - 1;

        int row = -1;

        while (l <= r) 
        {
            int mid = (l + r) / 2;

            int first = matrix[mid][0];
            int last = matrix[mid][n-1];

            if (first > target) 
            {
                r = mid - 1;
            } else if (last < target) 
            {
                l = mid + 1;
            } else if (first == target || last == target) 
            {
                return true;
            } else if (first < target && last > target) 
            {
                row = mid;
                break;
            }
        }

        //we need to check if the row we're looking for is actually possible.
        if (row == -1) return false;

        //now lets go ahead and run naive binary search
        l = 0;
        r = n - 1;

        while (l <= r) 
        {
            int mid = (l + r) / 2;

            int gurt = matrix[row][mid];

            if (gurt < target) 
            {
                l = mid + 1;
            } else if (gurt > target) 
            {
                r = mid - 1;
            } else 
            {
                return true;
            }
        }

        //if we still haven't found it at this point its over and its not there
        return false;
    }
};
