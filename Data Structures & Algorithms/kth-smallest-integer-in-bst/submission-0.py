# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""Lets code up naive solution where we add all values from BST into array and iterate through that k times"""
class Solution:
    def __init__(self):
        self.elements = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #honestly just use recursive dfs
        self.dfs(root)

        print(self.elements)

        #now we can sort and iterate k times
        self.elements = sorted(self.elements)

        #iterate k times and get the element we need
        return self.elements[k-1]
    def dfs(self, root: Optional[TreeNode]):
        self.elements.append(root.val)
        if root.left:
            # we need to call the method rather than appending to the array because thats going to cause
            # null values to be injected
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)