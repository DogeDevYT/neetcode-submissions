"""
I think we can solve this really easly using brute force and string reversion so lets start with that
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        #store count of palindromes
        palindrome_count = 0

        #we can use the same extend method from previous iterations to check for palindromes
        #i.e. we keep going left and right while palindrome is valid
        def extend(left, right):
            count = 0 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        #get our O(n^2 algoirthm by using our extension palindrome trick)
        for i in range(len(s)):
            palindrome_count += extend(i, i)
            palindrome_count += extend(i, i+1)
        
        return palindrome_count