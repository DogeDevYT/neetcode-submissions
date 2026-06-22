# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Uhhh tbh lets just do a basic recursive DFS solution again to start with

Got the inefficnet O(n^2) time complexity but I think I can do better with O(n)

Got O(n) time complexity by making use of dfs helper function to constantly update self.max_diameter

Lets get O(n) iterative DFS

I think we need to use a dual data structure approach here where we have the hashmap to store height of induvidual
nodes and a stack to store nodes we visited
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        max_diameter = 0
        stack = [(root, False)] #stores nodes we visited and calculated height for
        heights = { None: 0 } #maps treeNode -> height

        while stack:
            node, visited = stack.pop() #standard LIFO stack

            #skip nodes which are None
            if node == None: continue

            if visited:
                """
                if we visited this node before it means we've already stored the heights of our 
                left and right child in heights dictionary so then all we have to do is update max_diamater
                and calculate this nodes height and save it in heights dictionary since we're going 
                "bottom up" now
                """
                max_diameter = max(max_diameter, heights[node.left] + heights[node.right])
                heights[node] = 1 + max(heights[node.left], heights[node.right])
            else:
                """
                Since we want to evaluate this in post order (left,right,root)
                we need to push the right node onto stack before left and root needs to be before right
                """
                stack.append((node, True))
                #left and right children need to be added to root as false so they can be explored
                stack.append((node.right, False))
                stack.append((node.left, False))
        return max_diameter
