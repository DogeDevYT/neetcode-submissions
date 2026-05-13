#include <stack>

class Solution {
public:
    /*
    For this problem, we need to use a monotonically increasing stack. This one was super hard to wrap
    my head around first but then I realized I could run a while loop using our stack and having the top
    element be less than current temperature to repeatedly assign a decrementing value.
    */
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size(); //store size of vector for readability

        //create vector to return as solution
        std::vector<int> answer(n, 0);
        //store our indicies in a stack
        std::stack<int> indiciesStack;

        //iterate from left to right
        for (int i = 0; i < temperatures.size(); i++) 
        {
            while (!indiciesStack.empty() && temperatures[i] > temperatures[indiciesStack.top()]) 
            {
                int prev_index = indiciesStack.top();
                indiciesStack.pop();
                answer[prev_index] = i - prev_index;
            }
            indiciesStack.push(i);
        }
        return answer;
    }
};
