class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        I now remember how to do this the efficient way: we have to use prefix/postfix products.

        i.e. we have an array to store the prefix products (the product of each number up to that point)
        and another one for postfix (the product of each number after that point)

        and simply multiply each one at that index
        """

        pre = []
        post = []

        #populate pre array
        for i in range(len(nums)):
            if i > 0:
                pre.append(pre[i-1]*nums[i-1])
            else:
                pre.append(1) #first element

        #populate post array
        for i in range(len(nums) - 1, -1, -1):
            if i > len(nums) - 2:
                post.insert(0, 1) #first element
            else:
                post.insert(0, post[0]*nums[i+1])

        solution = []
        #allright, now lets make hte solution array
        for i in range(len(nums)):
            solution.append(pre[i]*post[i])
        
        return solution