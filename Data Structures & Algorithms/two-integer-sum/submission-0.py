class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create hashmap of seen characters
        seen = {}

        #iterate through all numbers
        for i, num in enumerate(nums):
            #get complement 
            complement = target - num

            #check complement
            if complement in seen:
                return [seen[complement], i] 

            #add current to seen if not there
            if num not in seen:
                seen[num] = i