class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        I'm ngl this one was actually deceptively difficult so what we have to do is convert
        everything to a set and then run a while loop to check for some element x such that

        x-1 exists in the set

        and we keep running that while loop until that isn't true anymore while incrementing our depth (max length)
        and we just highkey return the maximum of that

        edit:

        we can optomize this by chekcing
        x + 1 exists in the set 
        and only starting when our x - 1 eleemnt doesn't exist, that we we wont iterate over every elemenet
        """

        nums = set(nums)


        #visualizing this as a recursion stack where we keep going down enough so that 
        # we can find the "base case" i.e. element DNE
        maxDepth = 0
        for num in nums:
            if num - 1 not in nums:
                #now start the iteration counting
                currDepth = 1
                #store copy for modifcaiton
                numCopy = num
                while numCopy + 1 in nums:
                    numCopy += 1
                    currDepth += 1
                maxDepth = max(maxDepth, currDepth) #take max depth


        #return max depth
        return maxDepth
            
