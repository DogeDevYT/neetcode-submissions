class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #initialize left/right pointers
        l, r = 0, len(heights) - 1

        #store our max area
        max_area = 0

        #iterate over whole area to find absolute best
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])

            max_area = max(max_area, width*height)

            #move the smaller one towards center

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                #both are same so we should decrement r and increment l
                l += 1
                r -= 1
        return max_area
