#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // Fix 1: Koko can't eat 0 bananas per hour. Start at 1.
        int l = 1; 
        int r = *std::max_element(piles.begin(), piles.end()); // Standard way to get max before C++20 ranges

        int result = r;

        while (l <= r) 
        {
            // Fix 2: Prevent potential overflow during midpoint calculation
            int k = l + (r - l) / 2;

            // Fix 3: Use long long to prevent accumulation overflow
            long long total_time = 0;

            for (int pile : piles) 
            {
                // Fix 4: Clean integer-based ceiling division
                total_time += (pile + k - 1) / k;
            }

            if (total_time <= h) 
            {
                result = k;
                r = k - 1; 
            }
            else 
            {
                l = k + 1;
            }
        }
        return result;
    }
};