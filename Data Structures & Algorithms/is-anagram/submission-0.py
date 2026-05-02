from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create counters to store frequency
        count1 = Counter(s)
        count2 = Counter(t)
        #check equality on counters (frequency)
        return count1 == count2