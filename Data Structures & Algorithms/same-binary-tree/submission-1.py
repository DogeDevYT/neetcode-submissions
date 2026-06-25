# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Tbh I think a really easy recursive equality check onm all nodes and children is in order with dfs

now lets try iterative dfs
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited = [(p, q)] #start at root and iterate through visited tree 

        #I think we can reuse some of out linked lists sorted logic here
        while visited:
            n1, n2 = visited.pop()

            if not n1 and not n2:
                continue
            elif not n1 and n2:
                return False
            elif n1 and not n2:
                return False
            else:
                #both are valid so we can perform iteartions on them
                if n1.val != n2.val:
                    return False
                else:
                    visited.append((n1.left, n2.left))
                    visited.append((n1.right, n2.right))
        return True #if we get to this point then that means we have everuything

        