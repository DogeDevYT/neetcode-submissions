# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Ok I had to lookup solution for this problem since it was super hard but basically I think we have to dfs downwards
"""

class Solution:
    def __init__(self):
        self.res = []
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = [root.val]

        #populate result array
        self.dfs(root)
        return self.res[0]
    #helper function to return the maximum value of the current path as a dfs algorithm
    def dfs(self, root: Optional[TreeNode]) -> int:
        #base case
        if not root: return 0

        #recursively compute left/right downward paths
        left_max = self.dfs(root.left)
        right_max = self.dfs(root.right)

        #ignore negative downward paths
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        #replace the top of this with the global max path
        self.res[0] = max(self.res[0], root.val + left_max + right_max)
        #return the value for children recursive stack
        return root.val + max(left_max, right_max)


    