"""
I remember an easy way to check palindromes is to repeatedly check if first
and last characters match. Lets try an brute force solution for now and then
see if we can optomize with dynamic programming

Brute force solution done, time to memorize for DP
"""
class Solution:
    def __init__(self):
        self.memo = {}

    #repeatedly recurse into itself and repeatedly check first and last
    #character for matching/not matching
    def is_palindrome(self, s: str) -> bool:
        #base case for empty string or string of length 1
        if not s or len(s) == 1: 
            return True

        #check if we already have the string in the memo
        if s in self.memo:
            return self.memo[s]
        
        #recurse into itself
        first = s[0]
        last = s[len(s) - 1]

        slice = s[1:len(s) - 1]

        self.memo[s] = first == last and self.is_palindrome(slice)

        return self.memo[s]
    def longestPalindrome(self, s: str) -> str:
        #store longest palindromic substring
        # and use to perform operations
        lps = ""

        #use a sliding window approach to efficiently go through
        #substring combinations

        left = 0
        for right in range(1, len(s) + 1):
            while not self.is_palindrome(s[left:right]):
                left += 1
            
            if len(s[left:right]) > len(lps):
                lps = s[left:right]
            
            #reset when we're starign next
            left = 0
        
        return lps