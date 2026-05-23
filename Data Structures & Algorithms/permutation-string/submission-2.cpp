#include <unordered_map>

class Solution {
public:
    /*
    Allright so my first instincts were to use a hashmap to store character
    frequency from the 1st string and then go ahead and slide that window
    across the 2nd string with the number of items in the hashmap
    */
    bool checkInclusion(string s1, string s2) {
        //fast return fail if s1 is longer than s2
        if (s1.size() > s2.size()) return false;

        std::unordered_map<char, int> freq;

        //populate frequency map of s1
        for (char c : s1) 
        {
            if (!freq.contains(c)) 
            {
                freq[c] = 1;
            } else 
            {
                freq[c]++;
            }
        }

        //intiialize differential hashmap for comparison with sliding window
        std::unordered_map<char, int> diff;
        for (int i = 0; i < s1.size(); i++) 
        {
            if (!diff.contains(s2[i])) 
            {
                diff[s2[i]] = 1;
            } else 
            {
                diff[s2[i]]++;
            }
        }

        //initialize our left/right pointers to slide our window
        int l = 0;
        int r = s1.size() - 1;

        //slide our window while our right pointer is within window
        while (r < s2.size()) 
        {
            if (freq == diff) 
            {
                return true;
            } else 
            {
                //slide our window with frequency map
                diff[s2[l]] -= 1;
                if (diff[s2[l]] == 0) 
                {
                    diff.erase(s2[l]);
                }

                l += 1;
                r += 1;

                if (r < s2.size()) 
                {
                    if (!diff.contains(s2[r])) 
                    {
                        diff[s2[r]] = 1;
                    } else 
                    {
                        diff[s2[r]]++;
                    }
                }
            }
        }

        //if we get here that means we've not found any matches
        return false;
    }
};
