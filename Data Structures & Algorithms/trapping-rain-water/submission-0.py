class Solution:
    """
    Ok, for this problem, the key is realizing the height of rain water in an index, i, is:

    waterHeight[i] = min(height[l], height[r]) - height[i]

    Normally, you would try brute force on this by constantly searching for left/right but one trick
    we can do is store prefix and suffix maximums (man I think enormous zon really likes prefix/postfix
    shennagins)
    """
    def trap(self, height: List[int]) -> int:
        #precompute length of list for easy refernce later
        n = len(height)

        #the reason why we are setting prefix and suffix to 0 n times will be seen later
        prefix = [0] * n
        suffix = [0] * n

        #populate prefix
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i-1])
        
        #populate suffix
        suffix[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(height[i], suffix[i+1])
        
        #now that we have prefix and suffix calculatd, we can fiind the height of induvidual portions
        # and sum them up
        total = 0
        for i in range(n):
            total += min(suffix[i], prefix[i]) - height[i]

        return total
        