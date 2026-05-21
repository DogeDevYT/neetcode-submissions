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
        left, right = 0, 0

        #store length of longest string
        longest_str = 0

        #move our sliding window until it reaches the end
        while right < n:
            curr = s[right]

            #if current character in hash_map and >= left pointer
            #we need to reset to last index of current character + 1
            if curr in char_map and char_map[curr] >= left:
                left = char_map[curr] + 1
            

            #update character map
            char_map[curr] = right

            #calculate distance and update current max
            longest_str = max(longest_str, right - left + 1)

            right += 1 #increment right pointer

        return longest_str




        