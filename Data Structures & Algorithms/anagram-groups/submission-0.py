class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #initialize hashmap to store sorted string where its stored like
        # sorted string: <list of strings corresponding>

        result = defaultdict(list)
        
        #iterate thrgouh and sort
        for s in strs:
            sortedS = ''.join(sorted(s))
            result[sortedS].append(s)
        
        return list(result.values())