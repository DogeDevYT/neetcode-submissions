class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        This isn't a particularly smart solution but we can get around the product of an array 
        except for current index by simply multiplying out all the possible combinations fo reach index 
        each time
        """
        solution = []

        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                if i != j:
                    curr *= nums[j]
            solution.append(curr)

        return solution