# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
This should be a simple bfs moment but we'll see
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #maintain a list of all nodes to visit for bfs
        to_visit = []
        if root: to_visit.append(root) #add root if viable

        sol = []

        #iterate over the list and append elements to solution array
        while to_visit:
            curr = [] #store current nodes to append to solution

            levelLen = len(to_visit)
            for i in range(levelLen):
                node = to_visit[i]

                curr.append(node.val)

                if node.left:
                    to_visit.append(node.left)
                if node.right:
                    to_visit.append(node.right)
            to_visit = to_visit[levelLen:]
            sol.append(curr)
        return sol

