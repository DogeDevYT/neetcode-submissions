# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

"""
Simple chud bfs basically. If we add the last node in our visited level to our solution array it works out fr
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #create our list to visit from
        to_visit = deque([])

        #solution array with all our node values
        sol = []

        if root: to_visit.append(root)

        while to_visit:
            level_len = len(to_visit)
            target_node = level_len - 1

            for i in range(level_len):
                node = to_visit[0]

                if i == target_node: sol.append(node.val)

                #we're popping the current node early because we need to check if we have the last element
                #remaining
                to_visit.popleft()


                #need to process left side first so we append left first
                if node.left:
                    to_visit.append(node.left)
                if node.right:
                    to_visit.append(node.right)
        return sol
