# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Seems like simple recursive DFS but I'll try iterative with Stack as well
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0 #edge case where we dont have any nodes

        #create a stack to store elements to visit
        #update: instead of storing straight elmeents, lets store a tuple of:
        #(node, depth) that way we can track the current maximum depth
        to_visit = [(root, 1)]

        max_depth = -1

        while to_visit:
            node, depth = to_visit.pop()

            max_depth = max(max_depth, depth)

            if node.right:
                to_visit.append((node.right, depth + 1))
            if node.left:
                to_visit.append((node.left, depth + 1))
        
        return max_depth
