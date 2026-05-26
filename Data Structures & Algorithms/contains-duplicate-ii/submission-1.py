class Solution:
    """
    Ok, we can solve this by using a sliding window of size k and move
    that around and repeatedly search for duplicates in a certain portion of
    the area
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        #initilize sliding window pointers
        l = 0
        r = 0

        #do intiialize slide to k
        while r < k:
            #create a set to iterate over the numbers and check if it exist
            seen = set()

            #iterate through the window to find seen
            for i in range(l, r + 1):
                if nums[i] in seen:
                    return True
                else:
                    seen.add(nums[i])
            
            #iterate pointers
            r += 1

        #slide
        while r < len(nums):
            #create a set to iterate over the numbers and check if it exist
            seen = set()

            #iterate through the window to find seen
            for i in range(l, r + 1):
                if nums[i] in seen:
                    return True
                else:
                    seen.add(nums[i])
            
            #iterate pointers
            l += 1
            r += 1
        
        return False