# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We can get around the issue of finding the kth smallest by simply doing in order traversal at each node.

I.e. get to smallest (leftmost) then hit up center then right, and then we keep going throughout
and recurse up for however many values we need.
"""
class Solution:
    def __init__(self):
        self.elements = []
        self.k = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        #call our helper function to traverse in order for only up to k values and then return the kth value
        return self.inOrder(root)
    def inOrder(self, root: Optional[TreeNode]):
        if not root: return None #skip null nodes
        
        if root.left:
            left_res = self.inOrder(root.left)
            if left_res:
                return left_res
        
        self.elements.append(root.val)
        self.k -= 1

        if self.k == 0: return root.val

        if root.right:
            right_res = self.inOrder(root.right)
            if right_res:
                return right_res