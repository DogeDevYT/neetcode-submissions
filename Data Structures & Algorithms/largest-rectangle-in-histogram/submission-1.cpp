#include <stack>

class Solution {
public:

    /*
    Ok I figured it out now, we need to use a stack to store all of our indicies here and we 
    repeatedly check for local maximums by popping the 2nd most recent if most recent < 2nd most recent

    Our absolute minimum will be calculated at hte end as maximum width as well. 

    Looks like fixing height and shifting width was the method
    */
    int largestRectangleArea(vector<int>& heights) {
        //initialize empty stack to store indicies
        std::stack<int> indicies;
        int max_area = 0;

        //append 0 to end of heights array to guarentee every bar gets popped -> 
        //absolute minimum gets accounted for

        heights.push_back(0);

        //iterate through every index
        for (int i = 0; i < heights.size(); i++) 
        {
            int current_height = heights[i];

            //while heights is not empty and current height > height of bar on top of stack
            while (!indicies.empty() && current_height < heights[indicies.top()]) 
            {
                //pop top index from stack
                int h_index = indicies.top();
                indicies.pop();

                int height = heights[h_index];

                /*
                width: calculate right/left boundries

                right: simply use index we found to be smaller than this

                left: -1 if stack is empty or new top index of stack
                */

                int width;

                if (indicies.empty()) 
                {
                    width = i;
                } else 
                {
                    width = i - indicies.top() - 1;
                }

                max_area = std::max(max_area, height * width);
            }
            //append current index to stack
            indicies.push(i);
        }
        return max_area;
    }
};
