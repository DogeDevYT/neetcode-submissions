/*
I think the solution here is to simply have a hashmap to store letter combinations and all we need to to
is iterate through these while backtracking.
*/

#include <unordered_map>
#include <string>
#include <vector>

class Solution {
private:
    std::unordered_map<int, std::vector<char>> phone_map = {
        {2, {'a', 'b', 'c'}},
        {3, {'d', 'e', 'f'}},
        {4, {'g', 'h', 'i'}}, 
        {5, {'j', 'k', 'l'}},
        {6, {'m', 'n', 'o'}},
        {7, {'p', 'q', 'r', 's'}},
        {8, {'t', 'u', 'v'}},
        {9, {'w', 'x', 'y', 'z'}}
    };

    void backtrack(string digits, int i, vector<string>& res, vector<char> curr) 
    {
        //base case for backtracking where our index hijts the end
        if (i == digits.size()) 
        {
            res.push_back(std::string(curr.begin(), curr.end()));
            return;
        }

        int digit = digits[i] - '0'; //remember we're getting a character, not a string!

        for (char option : phone_map[digit]) 
        {
            curr.push_back(option);
            backtrack(digits, i + 1, res, curr);
            curr.pop_back();
        }
    }
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        std::vector<std::string> res = {};
        std::vector<char> curr = {};
        
        backtrack(digits, 0, res, curr);
        return res;
    }
};
