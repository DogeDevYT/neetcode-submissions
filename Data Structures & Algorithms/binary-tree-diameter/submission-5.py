# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Uhhh tbh lets just do a basic recursive DFS solution again to start with

Got the inefficnet O(n^2) time complexity but I think I can do better with O(n)
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #use our helper function
        self.max_diameter = 0

        self.node_height(root) #use our helper function update

        return self.max_diameter
    #helper function to get hte height of a certain node
    def node_height(self, root: Optional[TreeNode]):
        if root == None: return 0

        #get heihgts of left and right children
        l_height = self.node_height(root.left)
        r_height = self.node_height(root.right)

        #update self.max_diameter in case one of children has the highest diameter
        self.max_diameter = max(self.max_diameter, l_height + r_height)

        return 1 + max(l_height, r_height)
