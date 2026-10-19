/*
Ok I think the plan for what to do here is to create a dp array and iterate intilize it such that dp[a] represents
the minimum cost of reaching that (or amount + 1 if its impossible) and we go through all indicies in our dp
array and can go through all coin possibilities and check if the previous dp entry for this coin is lower than current
cost
*/

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;

        for (int a = 1; a <= amount; a++) 
        {
            for (int c = 0; c < coins.size(); c++) 
            {
                if (coins[c] <= a) dp[a] = min(dp[a], dp[a - coins[c]] + 1);
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
};
