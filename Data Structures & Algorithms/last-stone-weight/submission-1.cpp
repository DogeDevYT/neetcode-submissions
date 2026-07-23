/*
Ok so we need to get this working with a max-heap, since we're using cpp we can use a priority queue without a comparator
since its by-default max heap implemenntation of priority queue
*/

#include <queue>

class Solution {
private:
    std::priority_queue<int> pq;
public:
    int lastStoneWeight(vector<int>& stones) {
        //populate priority queue
        for (int stone : stones) 
        {
            pq.push(stone);
        }

        while (pq.size() > 1) 
        {
            int y = pq.top();
            pq.pop();
            int x = pq.top();
            pq.pop();

            if (x != y) pq.push(y - x);
        }

        if (!pq.empty()) 
        {
            return pq.top();
        }
        else 
        {
            return 0;
        }
    }
};
