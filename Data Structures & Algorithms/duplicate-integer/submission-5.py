class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a set of seen elements
        seen = set()

        #searched through every single element check if we've already seen it
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        #we have found NO elements that already exist so we are guarenteed false
        return False