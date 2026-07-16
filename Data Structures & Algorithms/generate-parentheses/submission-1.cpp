/*
basically we just run naive backtracking but make selections on opening/closing parenthesis
*/

#include <string>

class Solution {
private:
    void backtrack(int n, int currOpen, int currClosed, vector<string>& curr_combo, vector<string>& res) 
    {
        //base case where we've used up all our parenthesis and its time to return from backtracking
        if (currOpen == currClosed && currOpen == n) 
        {
            std::string outcome = "";

            for (auto gurt : curr_combo) outcome += gurt;
            res.push_back(outcome);
            return;
        }

        //backtrack with opening
        if (currOpen < n) 
        {
            curr_combo.push_back("(");
            backtrack(n, currOpen + 1, currClosed, curr_combo, res);
            curr_combo.pop_back();
        }

        if (currClosed < currOpen) 
        {
            curr_combo.push_back(")");
            backtrack(n, currOpen, currClosed + 1, curr_combo, res);
            curr_combo.pop_back();
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        std::vector<std::string> res = {};
        std::vector<std::string> curr_combo = {};

        backtrack(n, 0, 0, curr_combo, res);

        return res;
    }
};
