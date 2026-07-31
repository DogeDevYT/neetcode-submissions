/*
Ok, after reading the hints about splitting into 2 halves, I got a devious idea. There are 2 cases here:

1) Odd Number of elements:

In this case, after dividing the array into 2 halves, we simply return the last/first element from the left/right half
depending on which is bigger.

2) Even Number of Elements:

In this case, we need to make a max heap out of the left half and min heap out of the right half so that we can pop
from these heaps in O(1).

Balancing the heaps/addition:

Since we can't rely on sorting, we need to account for adding the elements in O(logn) using the heaps. We can do this
by checking if our number is > top of min heap. otherwise we push into max heap.

If the size difference becomes > 1. We resolve this by popping an element from larger heap and putting in smaller heap.
*/

#include <queue>
#include <vector>

class MedianFinder {
private:
    //priority_queue<type, container, comparator>
    priority_queue<int, vector<int>, std::greater<int>> min_heap;
    priority_queue<int> max_heap;
public:
    MedianFinder() {
        min_heap = {};
        max_heap = {};
    }
    
    void addNum(int num) {
        if (min_heap.size() > 0 && num > min_heap.top()) 
        {
            //push to right half
            min_heap.push(num);
        } else 
        {
            //push to left half
            max_heap.push(num);
        }

        //size returns type size_t so we can't use this for our difference checks becuase
        //it will always be > 0 and throw off rebalancing detection
        int size_diff = static_cast<int>(min_heap.size()) - static_cast<int>(max_heap.size());

        std::cout << "Size Diff: " << size_diff << std::endl;

        if (size_diff > 1) 
        {
            max_heap.push(min_heap.top());
            min_heap.pop();
        } else if (size_diff < -1) 
        {
            min_heap.push(max_heap.top());
            max_heap.pop();
        }
    }
    
    double findMedian() {
        int total_size = min_heap.size() + max_heap.size();

        if (total_size % 2 == 0) 
        {
            int lower = max_heap.top();
            int higher = min_heap.top();

            return (lower + higher) / 2.0; //remember to divide by floating point literal to 
            //force float division
        } else 
        {
            if (min_heap.size() > max_heap.size()) 
            {
                return min_heap.top();
            } else 
            {
                return max_heap.top();
            }
        }
    }
};
