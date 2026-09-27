/*
we can expand outwards here and make it far easier for us to solve in O(n^2)
*/

#include <algorithm>

using namespace std;

class Solution {
private:
    int expand(string s, int l, int r) 
    {
        while (l >= 0 && r < s.size() && s[l] == s[r]) 
        {
            l--;
            r++;
        }

        //return length of valid palindrome we find
        return r - l - 1;
    }
public:
    string longestPalindrome(string s) {
        //check to make sure we have valid string
        if (s == "") return "";

        int start = 0;
        int max_len = 0;

        for (int i = 0; i < s.size(); i++) 
        {
            //odd
            int len1 = expand(s, i, i);
            //even
            int len2 = expand(s, i, i+1);

            //take the max of both
            int current_max = max(len1, len2);

            //update max length
            if (current_max > max_len) 
            {
                max_len = current_max;
                //update based off bounds for max length
                start = i - (current_max - 1) / 2;
            }
        }

        //return longest palindrome
        return s.substr(start, max_len);
    }
};
