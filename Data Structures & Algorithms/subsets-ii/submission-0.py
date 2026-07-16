"""
I think the main difficulty with this problem is that we need to find a way
to ignore the duplicate elements in our subsets so that we dont accidently
include them twice.

I think an easy way to get around this would be to sort all the elements first
and then simply check to see if the current element is the same as the next one
and if it is keep skipping (use a while loop) along with naive backtracking
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] #denotes our final result
        curr = [] #denotes our current 

        #very important - sort array first so that we can implement
        #duplicate skipping logic
        nums = sorted(nums)

        def backtrack(index):
            #base case 1 - reach end of array therefore we have valid
            #subset
            if index == len(nums):
                res.append(curr.copy())
                return #dont forget to return

            #decision to include current element
            curr.append(nums[index])
            #backtrack
            backtrack(index + 1)

            curr.pop()
            #skip duplicates
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1)
        backtrack(0)
        return res