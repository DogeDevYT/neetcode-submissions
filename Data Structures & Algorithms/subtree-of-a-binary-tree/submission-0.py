# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""This seems like another simple dfs with a helper method maybe"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #actually lets try iterative dfs
        visited = [root]

        while visited:
            node = visited.pop()

            if not node: continue #skip null nodes


            if self.checkNode(node, subRoot):
                return True
            else:
                visited.append(node.left)
                visited.append(node.right)
        #if we've exhausted everything, return false
        return False
    #this function checks equality on a singular node
    #update: rework this to check deep equality (children as well) becuase I fail the nested case
    def checkNode(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if our root and its children DNE, automatically return false
        
        #make copy for easier typing
        p, q = root, subRoot

        if not p and not q:
            #match return true
            return True
        elif not p and q:
            #dont match return false
            return False
        elif p and not q:
            #dont match return false
            return False
        else:
            return (p.val == q.val) and self.checkNode(p.left, q.left) and self.checkNode(p.right, q.right)