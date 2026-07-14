"""
I think we could run this like the other backtracking problems except this time we have a set of elements `used` and 
then we choose weather or not to include an element if its not in the set. We can get away with doing this
becuase we're guarenteed UNIQUE integers
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set([])

        def backtrack(curr_path):
            #base case - len(curr_path) == len(nums) meaning we've finished a permutation
            if len(curr_path) == len(nums):
                res.append(curr_path.copy())
                return
            
            #now we run our basic backtracking except we have to try every element since
            #permutations are all the way to stack up the same n number of elements
            for i in range(len(nums)):
                if nums[i] in used:
                    continue #skip over elements we've already covered
                
                #option to take
                curr_path.append(nums[i])
                used.add(nums[i]) 

                backtrack(curr_path) #recurse and fill next slot

                #option to take other num
                used.remove(nums[i])
                curr_path.pop()
        backtrack([])
        return res