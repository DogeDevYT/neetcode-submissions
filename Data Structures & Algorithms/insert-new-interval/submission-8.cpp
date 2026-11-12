/*
So in our previous solution we used linear search to skip all the options
that weren't merged one by one now we can use binary search as follows:

1. use binary search to find correct position where newInterval swhoul dbe inserted based on start value
2. After we insert, its still sorted by start time
3. Then we can simply do a regular merge intervals pass
*/

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        //cover edge case where we have nothing so we dont 
        //crash on binary search
        if (intervals.empty()) return {newInterval};

        int n = intervals.size();
        int target = newInterval[0];
        int left = 0, right = n - 1;

        while (left <= right) 
        {
            int mid = (left + right) / 2;
            if (intervals[mid][0] < target) 
            {
                left = mid + 1;
            } else 
            {
                right = mid - 1;
            }
        }

        //insert at the location we found
        intervals.insert(intervals.begin() + left, newInterval);

        vector<vector<int>> res;
        for (const auto& interval : intervals) {
            if (res.empty() || res.back()[1] < interval[0]) {
                res.push_back(interval);
            } else {
                res.back()[1] = max(res.back()[1], interval[1]);
            }
        }

        return res;
    }
};
