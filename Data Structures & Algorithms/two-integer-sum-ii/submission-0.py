class Solution:
    """
    This ones really easy:

    2 options:
    - brute force calculate the possibilities for each number
    - take advantage of how list is sorting in ascending order so left/right pointer approach works here
    really good

    not going to bother with brute force right now since 2 pointer approach works
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        #since we're going to find a solution guaranteed while loop doens't really matter
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target: 
                r -= 1
            else:
                #normally you would want to have a check or something ot prevent infinite loops but
                # we dont need to worry about hatt
                
                return [l + 1, r + 1]
        
        return []