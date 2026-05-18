class Solution:
    """
    Update: we can use 2 pointer to process these prefix/postfix sums

    basically we move the smaller of the 2 left/right pointers inwards while left < right

    we can do this INSTEAD of traditional prefix/postfix
    """
    def trap(self, height: List[int]) -> int:
        #precompute length of list for easy refernce later
        n = len(height)

        #set left/right pointers
        l, r = 0, n-1

        #set left/right maxes to be 0 at start
        left_max, right_max = 0, 0

        #total
        total_water = 0

        #start using 2 pointer loop to fast calulate
        while (l < r):
            #assign left/right maxes accordingly
            left_max = max(height[l], left_max)
            right_max = max(height[r], right_max)

            #now we check which side is the "bottleneck", or in other words
            # which side is smaller so we can compute the water for that side

            if height[l] < height[r]:
                #left side is bottleneck
                gurt = left_max - height[l]
                total_water += gurt
                l += 1
            else:
                #right side is bottleneck
                gurt = right_max - height[r]
                total_water += gurt
                r -= 1
        return total_water


        
        