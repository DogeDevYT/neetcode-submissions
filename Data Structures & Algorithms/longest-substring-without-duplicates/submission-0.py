class Solution:
    """
    Ok for this problem, we can use sliding window but in a slightly different
    way to best time to buy/sell stock.

    We can keep a hash map of all the last index of a character and just
    jump to n + 1 index where n is the last 
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        #intiailze hashmap for comparison checking
        char_map = {}

        #store length of array
        n = len(s)

        #initialize left pointer
        left = 0

        #store length of longest string
        longest_str = 0

        #we were actually supposed to use right to index through array
        for right in range(n):
            curr = s[right]

            #if we find a duplicate AND it's inside the our current window
            if curr in char_map and char_map[curr] >= left:
                #jump to index + 1
                left = char_map[curr] + 1
            
            #update character's newest index
            char_map[curr] = right

            #calculate current difference in indicies and check if its max
            dist = right - left + 1
            longest_str = max(longest_str, dist)

        return longest_str




        