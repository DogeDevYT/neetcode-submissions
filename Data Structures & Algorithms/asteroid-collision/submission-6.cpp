#include <stack>
#include <algorithm> //for std::reverse

class Solution {
public:
    /*
    Ok for this problem, I got the algorithm super fast but the implementation
    of having repeated stack pops was super unintiutive and I needed to look
    at solution
    */
    vector<int> asteroidCollision(vector<int>& asteroids) {
        std::stack<int> s;

        for (int asteroid : asteroids) 
        {
            //we need to iterate over the stack while
            //our current asteroid < 0 and top of stack > 0
            //since that means we have an imbalance
            while (!s.empty() && asteroid < 0 && s.top() > 0) 
            {
                //store the difference of having our negative 
                //new element and positive top of stack
                int diff = asteroid + s.top();

                if (diff < 0) 
                {
                    //new asteroid bigger; SMASH top of stack
                    s.pop();
                } else if (diff > 0) 
                {
                    //asteroid on stack bigger; smash new asteroid
                    asteroid = 0;
                } else 
                {
                    //smash both
                    asteroid = 0;
                    s.pop();
                }
            }
            //if we still have a new asteroid remaining, add it to stack
            if (asteroid) s.push(asteroid);
        }
        

        //while our stack is non-empty push to vector
        std::vector<int> sol;
        
        while (!s.empty()) 
        {
            sol.push_back(s.top());
            s.pop();
        }

        //reverse handle stack ordering
        std::reverse(sol.begin(), sol.end());

        return sol;
    }
};