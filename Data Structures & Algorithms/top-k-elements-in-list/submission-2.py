class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Ok, for the most efficient solution, we can use bucket sort such that
        we create n buckets for number of elements, 
        corresponding to the frequncy of an element,
        and we populate
        these buckets with the respective items from our frequency hashmap
        """

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        #create n buckets for frequencies
        buckets = [[] for _ in range(len(nums) + 1)]
    
        for (key,value) in freq.items():
            buckets[value].append(key) #populate buckets
        
        #start iterating from "the other end" to find hte k largest elements
        solution = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution