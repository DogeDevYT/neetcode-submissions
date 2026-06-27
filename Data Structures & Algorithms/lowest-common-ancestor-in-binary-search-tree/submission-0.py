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

        #exit if root is null
        if not root: return None

        goLeft = root.val > pTarget and root.val > qTarget
        goRight = root.val < pTarget and root.val < qTarget

        #we need to check discount: i.e. one of the nodes on left and right
        # != p or q
        goLeft = goLeft and root.left != p and root.left != q
        goRight = goRight and root.right != q and root.right != q

        if goLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        elif goRight:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            #now we've found the ancestor fr and we can return the current node
            return root
