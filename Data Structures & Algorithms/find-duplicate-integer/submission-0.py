class Solution:
    """
    Off the top of my head I see 2 ways to do this: we can either use a hash map to store 
    all numbers and reference to check for duplicates which is an O(n) time complexity but also
    O(n) space complexity but if we want a constant time space complexity, we can sort which is O(nlogn)
    and then check to see if the next element is the number we need

    Lets go with the sorting route becuase thats the simplest to code
    """
    def findDuplicate(self, nums: List[int]) -> int:
        #sort
        nums = sorted(nums)

        #iterate over every number and check if its equal to the next one
        for i in range(len(nums) - 1):
            #reference current and next numbers
            curr = nums[i]
            nxt = nums[i+1]

            #if we have a situation where the current one is hte next one
            #which is guanreteed by sorting, we can then return the current number
            if curr == nxt:
                return curr
        