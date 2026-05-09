class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        I now remember how to do this the efficient way: we have to use prefix/postfix products.

        i.e. we have an array to store the prefix products (the product of each number up to that point)
        and another one for postfix (the product of each number after that point)

        and simply multiply each one at that index

        update: I just realized we can do it with one array by filling it with pre first and then post
        """

        solution = []

        #populate with pre
        for i in range(len(nums)):
            if i > 0:
                solution.append(solution[i-1]*nums[i-1])
            else:
                solution.append(1) #first element
        
        #keep a "running product" becuase we can't rely on in-array products anymore
        running_product = 1

        #populate with post while decrementing from last element
        for i in range(len(nums) - 1, -1, -1):
            if i > len(nums) - 2:
                solution[i] *= running_product #first element
            else:
                running_product *= nums[i+1]
                solution[i] *= running_product
        
        return solution