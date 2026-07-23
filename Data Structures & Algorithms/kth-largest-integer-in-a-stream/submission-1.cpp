/*
Yeah honestly for this problem, we'd be better off using min-heap (priority queue in cpp) of size k so that if we
get the kth largest from the min-heap, its O(1). However inserting m elements would require log(n) time each. Therefore,
inserting m elements would have mlog(n) time complexity in total. 
*/

#include <queue>
#include <vector>
#include <functional> //needed for std::greater

class KthLargest {
private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    int heap_k;
public:
    KthLargest(int k, vector<int>& nums) {
        //populate heap
        for (int num : nums) 
        {
            min_heap.push(num);
        }

        //set k
        heap_k = k;

        //restrict to size k
        while (min_heap.size() > heap_k) min_heap.pop();
    }
    
    int add(int val) {
        min_heap.push(val);

        //only remove when we have too many elements that have just been added
        if (min_heap.size() > heap_k) min_heap.pop();

        return min_heap.top();
    }
};
