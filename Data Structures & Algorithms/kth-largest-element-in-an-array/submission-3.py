"""
So right away, I see a cop out solution where we sort first and then return index k
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]