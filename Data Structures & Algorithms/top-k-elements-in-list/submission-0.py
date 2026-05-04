import heapq

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        for this problem I'm thinking we could use a hasmap to store 
        a frequency table and then enumerate through that later to get
        the k most frequent elemnts
        """

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        """
        Lets use the min heap implementation of the priority queue
        from heapq
        """

        #create empty list to heapify later
        heapList = []
        
        for (key, value) in freq.items():
            sonimcrine = [value, key]
            heapList.append(tuple(sonimcrine))
        
        #heapify and pop all but the k largest elements
        heapq.heapify(heapList)
            
        #pop least common element from top of heap such that 
        #elements in heap <= k
        while len(heapList) > k:
            heapq.heappop(heapList)
        
        #now that we have our heap list we need to extract our result

        result = []

        for item in heapList:
            result.append(item[1])
    
        
        return result