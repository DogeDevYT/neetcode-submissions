class Solution:
    """
    Ok finally got it. I think I know how we're supposed to pattern match here. We have to get the max of the list
    becuase we know its going to be an upper bound for how fast koko can eat bananas and we binary search that with
    a lower bound of sum where we just assume 1 or smth
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r #return this later

        while l <= r:
            k = (l + r) // 2
            
            totalTime = 0

            #we can use this to easily get the amount of time per pile to eat at current speed
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            
            if totalTime <= h:
                res = k
                r = k - 1

                #we get our return value to be k and keep going to see if theres a potentially better solution
            else:
                l = k + 1
        return res
            
