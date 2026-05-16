class Solution:
    def isPalindrome(self, s: str) -> bool:
        #initialize left and right pointers
        l, r = 0, len(s) - 1

        #iterate while the whole string 
        while l <= r:
            if l < r:
                if not s[l].isalnum():
                    l += 1
                elif not s[r].isalnum():
                    r -= 1
                elif ord(s[l].lower()) != ord(s[r].lower()):
                    return False
                else:
                    l += 1
                    r -= 1
            else:
                l += 1
                r -= 1 # if we have the same character -> guarenteed to be equal
        
        return True
        