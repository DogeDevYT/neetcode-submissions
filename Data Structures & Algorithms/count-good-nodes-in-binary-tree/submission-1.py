# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maxNode: float = -float('inf')) -> int:
        if root == None:
            return 0

        ret = 0

        if root.val >= maxNode:
            ret += 1
        
        maxCopy = max(maxNode, root.val)

        ret += self.goodNodes(root.left, maxCopy) + self.goodNodes(root.right, maxCopy)

        return ret
