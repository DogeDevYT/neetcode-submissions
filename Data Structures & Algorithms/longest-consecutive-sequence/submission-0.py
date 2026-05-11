class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I'm ngl this one was actually deceptively difficult so what we have to do is convert
        everything to a set and then run a while loop to check for some element x such that

        x-1 exists in the set

        and we keep running that while loop until that isn't true anymore while incrementing our depth (max length)
        and we just highkey return the maximum of that
        """

        nums = set(nums)


        #visualizing this as a recursion stack where we keep going down enough so that 
        # we can find the "base case" i.e. element DNE
        maxDepth = 0
        for num in nums:
            currNum = num
            currDepth = 1 #always start off at 1
            while currNum - 1 in nums:
                currNum -= 1
                currDepth += 1
            maxDepth = max(maxDepth, currDepth) #take the max of current depth and maximum depth
        
        return maxDepth
            
