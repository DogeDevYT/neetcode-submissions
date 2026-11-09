"""
Ok so this was just a hack for the XOR operator:
basically since XORing 2 identical numbers results in 0, we just need to XOR the entire array to get
the only number that won't match up i.e. the single number, since every other number will find its pair and cancel
out
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            res = res ^ curr
        return res