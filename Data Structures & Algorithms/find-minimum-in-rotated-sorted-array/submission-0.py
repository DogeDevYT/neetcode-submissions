class Solution:
    """
    Ok I think we have to do slightly modified binary search in that we have 3 values:
    l, mid, and r

    we calculate mid as normal: (l+r)//2 but the difference here is that we pay attention to how the midpoint

    relates to either side, for example if mid < r we know the minimum element will be in the left part becuase we can
    rely on naive binary search since the array segment could be considered sorted and non rotated.

    however if l < mid the minimum element has to be in the right part since the left segment is sorted.
    """
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        lowest = nums[0]

        while l <= r:
            #check if our segment is sorted so we can just pull first element
            if nums[l] < nums[r]:
                lowest = min(lowest, nums[l])
                break

            mid = (l+r) // 2

            curr = nums[mid]
            lowest = min(lowest, curr)

            if curr >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return lowest