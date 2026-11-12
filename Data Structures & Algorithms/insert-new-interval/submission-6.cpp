/*
So after solving this problem in Python, I think the key thing to keep in mind is that for the linear search solution we can just do the following:

1) add all the intervals that are completely before the new interval (end time < start time of new interval)
2) merge all the intervals that are connected to new interval (while start time < end time of new interval)
    a) we can merge them together using the minimum of all our starts and the maximum of all our ends
3) whatever interval is left after that we can just add to our solution
*/

#include <vector>
#include <algorithm>

//dont do this in production, but its fine for one and done files
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        //create our solution 2d vector
        vector<vector<int>> solution;
        //need this for quick reference
        int n = intervals.size();
        //use this to index during our while loops
        int i = 0;

        while (i < n && intervals[i][1] < newInterval[0]) 
        {
            solution.push_back(intervals[i]);
            i++;
        }

        //remember we want to compare END of new interval to find ones that are intersecting if they're greater than
        // or equal to current intervals START value
        while (i < n && newInterval[1] >= intervals[i][0]) 
        {
            newInterval[0] = min(intervals[i][0], newInterval[0]);
            newInterval[1] = max(intervals[i][1], newInterval[1]);
            i++;
        }
        solution.push_back(newInterval);

        //add all remaining intervals
        while (i < n) 
        {
            solution.push_back(intervals[i]);
            i++;
        }

        return solution;
    }
};
