# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Ok, turns out this problem is going to be a lot harder than I thought.
we can take advantage of of the values having to be less than initial ones.

In my previous code I was assuming all children would naively behave like sorted binary search trees when they 
wouldn't. We can fix this by taking note of range.
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #implement helper function to store ranges of possible values rather than current values
        return self.dfs_range(root, float('-inf'), float('inf'))
    def dfs_range(self, root: Optional[TreeNode], left: int, right: int) -> bool:
        if not root:
            #empty nodes fit criteria
            return True
        elif not (left < root.val < right):
            #we need to check our current node based off of our passed down limits
            return False
        else:
            #go ahead and check our children as well
            return self.dfs_range(root.left, left, root.val) and self.dfs_range(root.right, root.val, right)
        