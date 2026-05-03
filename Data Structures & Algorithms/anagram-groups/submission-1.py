class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Ok for this approach, lets have the key of the hashmap be
        the frequency of each character's letters
        e.g.
        a-z
        00100...00001 is the key

        and have the value be the list of strings that match
        """

        result = defaultdict(list)
        
        #iterate thrgouh and get character frequencies as key
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        
        return list(result.values())