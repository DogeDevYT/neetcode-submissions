# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Uhhh tbh lets just do a basic recursive DFS solution again to start with
"""
class Solution:
    #define this like a real class that we can iterate on
    def __init__(self):
        self.max_diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        #previously we were tracking the max diameter by assuming it would be at the root, this is wrong
        #because there are some cases where this isn't true, we can get around this by 
        #keeping track of max diameter at each node's children

        #call our method on children
        d_left = self.diameterOfBinaryTree(root.left)
        d_right = self.diameterOfBinaryTree(root.right)

        #update max diameter based on the left and right hand node's children
        self.max_diameter = max(self.max_diameter, self.node_height(root.left) + self.node_height(root.right))

        return self.max_diameter
    #helper function to get hte height of a certain node
    def node_height(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        return 1 + max(self.node_height(root.left), self.node_height(root.right))
