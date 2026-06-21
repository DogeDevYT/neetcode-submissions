# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Seems like simple recursive DFS but I'll try iterative with Stack as well

got stack, iterative DFS,

lets get BFS now as well
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()

        if root: q.append(root)

        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            depth += 1
        return depth
