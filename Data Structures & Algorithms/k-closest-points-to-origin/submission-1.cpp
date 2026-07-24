/*
We can solve this problem pretty easily with a priority queue (cpp implmeentation of max heap). This natively
computes ordinance on 1st pair and then uses 2nd as tiebreaker
*/

#include <vector>
#include <queue>

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        std::priority_queue<std::pair<int, std::vector<int>>> max_heap;

        //use a constant reference to not copy 2 vectors every time
        for (const auto& point : points) 
        {
            int dist = point[0]*point[0] + point[1]*point[1];

            max_heap.push({dist, point});

            if (max_heap.size() > k) max_heap.pop();
        }

        std::vector<std::vector<int>> ret = {};

        while (!max_heap.empty()) 
        {
            ret.push_back(max_heap.top().second);
            max_heap.pop();
        }

        return ret;
    }
};
