/*
ok yeah I think we can solve this quite simply using a similar method to insert interval previously.

The only hard part would be sorting this properly in c++
*/

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        //sort intervals in ascending order based on start index
        //using lambda function
        sort(intervals.begin(), intervals.end(), [](const vector<int>& one, const vector<int>& two) {
            return one[0] < two[0];
        });

        //now we can create our final return solution vector
        vector<vector<int>> solution;

        //use this as our previous vector to be merged with to merge intervals
        vector<int> prev = intervals[0];

        //read start/end from new intervals without modifying
        for (auto interval : intervals) 
        {
            int start = interval[0];
            int end = interval[1];

            if (start <= prev[1]) 
            {
                prev[0] = min(prev[0], start);
                prev[1] = max(prev[1], end);
            } else 
            {
                //flush previous element to solution array
                solution.push_back({prev[0], prev[1]});
                //update previous element to current
                prev = {start, end};
            }
        }

        //flush prev one more time
        solution.push_back({prev[0], prev[1]});

        return solution;
    }
};
