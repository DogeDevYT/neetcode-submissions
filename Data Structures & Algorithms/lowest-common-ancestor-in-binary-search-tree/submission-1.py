# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Ok so after reading a couple of hints I got an idea: since we're using a binary
search tree, we only need to keep recursing until we find a split point: i.e.

where we can't progress in the same direction to get towards a couple of nodes

I guess this is basically dfs?
"""
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #store target values
        pTarget, qTarget = p.val, q.val

        curr = root

        while curr:
            goLeft = curr.val > pTarget and curr.val > qTarget and curr.left != p and curr.left != q
            goRight = curr.val < pTarget and curr.val < qTarget and curr.right != p and curr.right != q

            if goLeft:
                curr = curr.left
            elif goRight:
                curr = curr.right
            else:
                return curr

