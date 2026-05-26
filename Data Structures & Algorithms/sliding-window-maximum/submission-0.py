class Solution:
    """
    Yeah I'm ngl I might just have to try brute force at first and then
    ask an LLM for the optomization. 
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #initialize list of numbers to store sliding window maxes
        window_maxes = []

        #slide through the window from 0 to len(nums) - k

        #start off with window from 0 to k
        l = 0
        r = k

        while r < len(nums) + 1:
            #store current maximum
            curr_max = float('-inf')

            #iterate through numbers and pick the maximum in the window
            for i in range(l, r):
                if nums[i] > curr_max:
                    curr_max = nums[i]
            
            #append current maximum to the window maxes
            window_maxes.append(curr_max)

            #slide window forward
            l += 1
            r += 1

        return window_maxes