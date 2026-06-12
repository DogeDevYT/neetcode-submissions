class Solution:
    """
    Basic 2 pointer binary search, nothing to see here
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        #this is literally the basic binary search icl so we need to keep repeating while the left pointer < 
        #right pointer

        #we need to change this to <= so that single element ranges
        #can still be processed
        while l <= r:
            mid = (l + r) // 2 #store the midpoint of both our pointers
            #get the element at the midpoint and evaluate weather its >, <, = the target
            gurt = nums[mid]

            if gurt > target:
                #since we have the midpoint being greater than target, we can move our right pointer to midpoint
                # - 1 to achieve a O(logn) time complexity
                r = mid - 1
            elif gurt < target:
                #in this situation, we have the midpoint being less than target so we can move our left pointer
                #to midpoint + 1 to achieve O(logn) time complexity
                l = mid + 1
            else:
                #target found, return
                return mid
        #in this situation, we've found nothing so we need to return -1
        return -1