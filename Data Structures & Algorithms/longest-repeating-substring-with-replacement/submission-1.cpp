#include <vector>
#include <algorithm>

class Solution {
public:
    /*
    I had a lot of trouble understanding how sliding window applies here

    but after a lot of prooompting I think it goes like:

    we need to find out the maximum frequency of a character such that

    (right - left + 1) - max_freq <= k

    becuase it makes no sense to remove the most frequent character and
    replace with another
    */
    int characterReplacement(string s, int k) {
        //create our frequency map for current window
        std::vector<int> freq(26, 0);

        int left = 0;
        int max_len = 0;
        int max_freq = 0;

        //iterate through all eelemnts and move right to maximum possible
        for (int right = 0; right < s.size(); right++) 
        {
            //convert to frequency index and increment
            int char_idx = s[right] - 'A';
            freq[char_idx]++;

            //update max frequency
            max_freq = std::max(max_freq, freq[char_idx]);

            //while window is invalid, shrink it so that it matches:
            //(right - left + 1) - max_freq <= k
            while ((right - left + 1) - max_freq > k) 
            {
                //slide left pointer forward

                //remove from frequency map
                char_idx = s[left] - 'A';
                freq[char_idx]--;

                //slide
                left++;
            }

            //since we found maximum window, max length guarneteed to be valid
            max_len = std::max(max_len, right - left + 1);
        }
        return max_len;
    }
};
