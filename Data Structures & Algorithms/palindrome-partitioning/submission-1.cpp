/*
Ok, now that we solved in Python, we can translate pretty easyily to cpp using the same general format.

Ok so what we're doing is this: if we find a palindrome on a substring, we slice that out of our list and append
to our current results and keep on going with backtracking if we find palindromes otherwise we just keep going.
*/

#include <string>
#include <vector>

class Solution {
private:
    void backtrack(string s, int start, vector<string>& curr, vector<vector<string>>& result) 
    {
        //base case of our start being at end of list for our palindrome partiitoning
        if (start == s.size()) 
        {
            result.push_back(curr);
            return;
        }

        for (int end = start; end < s.size(); end++) 
        {
            int delta = end - start;
            std::string substring = s.substr(start, delta + 1);

            if (is_palindrome(substring)) 
            {
                curr.push_back(substring);
                backtrack(s, end + 1, curr, result);
                curr.pop_back();
            }
        }
    }

    //helper function to determine if a string is a palindrome using 2 pointer
    bool is_palindrome(string s) 
    {
        int l = 0, r = s.size() - 1;

        while (l <= r) 
        {
            if (s[l] != s[r]) return false;
            l += 1;
            r -= 1;
        }
        return true;
    }
public:
    vector<vector<string>> partition(string s) {
        std::vector<std::vector<std::string>> result = {};
        std::vector<std::string> curr = {};

        backtrack(s, 0, curr, result);

        return result;
    }
};
