#include <unordered_map>
#include <algorithm>

class Solution {
public:

    /*
    Ok for this problem, we can use sliding window but in a slightly different
    way to best time to buy/sell stock.

    We can keep a hash map of all the last index of a character and just
    jump to n + 1 index where n is the last
    */
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> char_map;

        int n = s.size();

        int left = 0;
        int right = 0;

        int longest_str = 0;

        while (right < n) 
        {
            char curr = s[right];

            if (char_map.contains(curr) && char_map[curr] >= left) 
            {
                left = char_map[curr] + 1;
            }

            char_map[curr] = right;

            longest_str = std::max(longest_str, right - left + 1);

            right++;
        }
        return longest_str;
    }
};
