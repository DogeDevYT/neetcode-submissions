/*
Ok yeah this problem shouldn't be any trouble at all. All we need to do is to basically just a min heap implmeented
with a priority queue and special comparator of size "k" and just return the top of the heap after adding everything
using the special push (reheap down)
*/

#include <queue>
#include <vector>

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        /*
        this constructor goes <pq type, container type, comparator>
        */
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;

        for (auto num : nums) 
        {
            pq.push(num);
        }

        //make it size k by manually removing everything
        while (pq.size() > k) 
        {
            pq.pop();
        }

        //peek at top
        return pq.top();
    }
};
