#include <algorithm>

class Solution {
public:
    /*
    If we look at everything like a system of equations where each (position, speed) pair 
    is (y intercept, slope) respectively, we realize that the car with highest y intercept automatically 
    becomes the right most car on the numberline. 

    By also thinking about it for a bit, we realize that we have to merge the cars from right to left
    becuase 
    */
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        //create our intial pairs using std::pair
        std::vector<std::pair<int, int>> pairs;

        for (int i = 0; i < position.size(); i++) 
        {
            pairs.push_back({position[i], speed[i]});
        }
        std::sort(pairs.rbegin(), pairs.rend());

        //create our stack -- std::stack is not optimal here since we need to peek at 2nd
        //elemnt from top so we need to use vector instead
        std::vector<double> carfleet;

        //iterate through our stack in a reverse fashion 
        for (auto& p : pairs) 
        {
            carfleet.push_back((double) (target - p.first) / p.second);

            if (carfleet.size() >= 2 &&
                    carfleet.back() <= carfleet[carfleet.size() - 2]) 
                    {
                       carfleet.pop_back(); // pop most 2nd recent element since we know
                       //its not  going to be included
                    }
        } 
        return carfleet.size();
    }
};
