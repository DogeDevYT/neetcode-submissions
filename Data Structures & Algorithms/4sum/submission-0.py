class Solution:
    """
    Yeah so for this one I think its a simple nested for loop such that

    for i in range(nums)
    for j in range(i + 1, nums)

    we basically use left/right pointer after sorting for 2 sum such that 

    -(nums[i] + nums[j]) = nums[left] + nums[right]
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sort
        nums = sorted(nums)

        sol = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                #initialize left/right pointers
                l = j + 1
                r = len(nums) - 1
                
                while (l < r):
                    curr = nums[l] + nums[r] + nums[i] + nums[j]
                    if curr < target:
                        l += 1
                    elif curr > target:
                        r -= 1
                    else:
                        #found return
                        sol.append((nums[i], nums[j], nums[l], nums[r]))
                        
                        #increment pointers to keep searching
                        l += 1
                        r -= 1
        return list(set(sol))