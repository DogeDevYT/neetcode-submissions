class Solution:
    """
    I had a lot of trouble understanding how sliding window applies here

    but after a lot of prooompting I think it goes like:

    we need to find out the maximum frequency of a character such that

    (right - left + 1) - max_freq <= k

    becuase it makes no sense to remove the most frequent character and
    replace with another
    """
    def characterReplacement(self, s: str, k: int) -> int:
        #frequency map for current window
        freq = [0] * 26
        left = 0
        max_len = 0
        max_freq = 0

        #slide window
        for right in range(len(s)):
            #convert to frequency index and increment
            char_idx = ord(s[right]) - ord('A')
            freq[char_idx] += 1

            #update max frequency
            max_freq = max(max_freq, freq[char_idx])

            #while the window is invalid, shrink it
            #(right - left + 1) - max_freq <= k
            while (right - left + 1) - max_freq > k:
                #slide left pointer forward

                #remove from frequency map
                char_idx = ord(s[left]) - ord('A')
                freq[char_idx] -= 1

                #slide
                left += 1
            
            #since we found maximum window, the max length 
            #guranteed to be valid
            max_len = max(max_len, right - left + 1)
        return max_len
