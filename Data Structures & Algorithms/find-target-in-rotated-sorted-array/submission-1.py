class Solution:
    """Pattern match from the 2 "ramps" find minimum element
    
    Basically we can work around the "inflection" point by comparing if 
    nums[left] <= nums[mid] so that we can then make a few key decisions on where to search next
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            #check if we've found our target
            if nums[mid] == target:
                return mid

            #this tells us what kind of ramp we're in
            # nums[l] <= nums[mid] means false start and the actual split happens later
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 #we haven't foun danyting