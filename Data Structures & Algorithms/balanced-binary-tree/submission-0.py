# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
I think this should be a simple dfs with a helper function called upon each
node recursively.
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #base case for empty node/child of leaf
        if root == None:
            return True

        #lets do a chud recursive node_height check
        l_height = self.node_height(root.left)
        r_height = self.node_height(root.right)

        return ((abs(l_height - r_height) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right))
    #helper method to get height of node
    def node_height(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        return 1 + max(self.node_height(root.left), self.node_height(root.right))
        