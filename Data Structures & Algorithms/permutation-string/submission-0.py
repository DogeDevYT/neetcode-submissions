class Solution:
    """
    Allright so my first instincts were to use a hashmap to store character
    frequency from the 1st string and then go ahead and slide that window
    across the 2nd string with the number of items in the hashmap
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if s1 is longer than s2 we automatically fail
        if len(s1) > len(s2):
            return False

        freq = {}

        #populate frequency map
        for char in s1:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        #intialize differential hashmap for comparison with sliding window
        diff = {}
        for char in range(len(s1)):
            if s2[char] not in diff:
                diff[s2[char]] = 1
            else:
                diff[s2[char]] += 1
        
        #initialize our left/right pointers for sliding window
        l = 0 
        r = len(s1) - 1

        #slide our window while our right pointer 
        while (r < len(s2)):
            if diff == freq:
                return True
            else:
                #slide our window with frequency map
                diff[s2[l]] -= 1
                if diff[s2[l]] == 0:
                    del diff[s2[l]]
                l += 1
                r += 1
                
                if r < len(s2):
                    if s2[r] not in diff:
                        diff[s2[r]] = 1
                    else:
                        diff[s2[r]] += 1
        #if we get here that means we've nto found any matches
        return False

        