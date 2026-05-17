class Solution:
    """
    Ok, got the algorithm now, once we sort through the list of numbers, we can iterate through every index
    and find 2 numbers such that -nums[i] = nums[j] + nums[k]

    In other words, 2 SUM WITH -nums[i] as target
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort through numbers at start to leverage 2 pointer later
        nums.sort()

        #store this
        n = len(nums)

        #solution array
        solution = []

        for i in range(n):
            target = -nums[i]

            #now we can use left/right pointers to find our target

            #since our array is sorted, we only need to look FORWARD to find a sum of numbers = -nums[i]
            l, r = i + 1, n-1

            while (l < r):
                total = nums[l] + nums[r]

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    #on target!
                    solution.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1 #there could be multiple combinations of numbers we need
        #use conversion to set trick
        gurt = []

        #get rid of duplicates by converting to set then list from tuples
        return list(set(solution))
        