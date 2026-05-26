#include <deque>
#include <vector>

class Solution {
public:
    /*
    Ok I figured it out now, we can leverage the monotonically decrasing
    queue to track elements and find maximums.

    I.e. if we find an element lesser than teh current minimum, we remove it
    asap because its guarenteed to not be included.

    and if we find an element thats greater than the least element in the
    max array we have to pop the lesser elements. 
    */
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        //initialize queue of indicies
        std::deque<int> q;

        std::vector<int> output;

        for (int i = 0; i < nums.size(); i++) 
        {
            //maintain monotonic property by removing numbers from back
            // becuase that means they wont be included in the sliding window
            //maximum to begin with because we want the maximum of each
            while (!q.empty() && nums[q.back()] < nums[i]) 
            {
                q.pop_back();
            }

            //append current element to the end of queue
            q.push_back(i);

            //remove front index from queue since its constantly asking
            //from MAX from list
            if (q.front() < i - k + 1) 
            {
                q.pop_front();
            }

            //when sliding window is built up, we cna start
            //adding to our output
            if (i >= k - 1) 
            {
                output.push_back(nums[q.front()]);
            }
        }
        return output;
    }
};
