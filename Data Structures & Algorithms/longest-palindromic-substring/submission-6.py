"""
I remember an easy way to check palindromes is to repeatedly check if first
and last characters match. Lets try an brute force solution for now and then
see if we can optomize with dynamic programming

Brute force solution done, time to memorize for DP

Ok, now that we tried going top down, we should try going bottom up, i.e. expanding from a character outwards
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #check to make sure we have valid string
        if not s:
            return ""
        
        start = 0
        max_len = 0

        #this method expands our palindromic patterns
        #while our first character is equal to our last one
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            #return length of valid palindrome we find
            return right - left - 1
        
        #iterate over all possibilities for expansion
        for i in range(len(s)):
            #cover odd length substrings
            len1 = expand(i, i)
            #cover even length substrings
            len2 = expand(i, i + 1)
        
            #take the max length one and use that to set our bounds
            current_max = max(len1, len2)

            if current_max > max_len:
                max_len = current_max
                #calculate starting index based on the center i
                start = i - (current_max - 1) // 2
        
        return s[start: start + max_len]