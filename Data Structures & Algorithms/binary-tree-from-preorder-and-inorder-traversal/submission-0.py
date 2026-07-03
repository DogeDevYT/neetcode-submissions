# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
After watching the neetcode I realized we need to focus on actually making the partitions using 2 key facts:

1. pre order traversal is root, left, right so we can use this to find the root, but we still dont know
left/right partition so we use the in order traversal to do so.

2. In in-order traversal we look for our root element from pre order and use that to split in relation to left/right
subtrees

3. after we get the partition and know where our subarrays/subtrees are we can recurse and execute the function as
planned.
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder or not inorder:
            return None #we got to the leaves here
        

        #root node is first value in preorder array
        root = TreeNode(preorder[0])

        #get our index of partition of elements based off of in order array
        mid = None

        for index in range(len(inorder)):
            if inorder[index] == root.val:
                mid = index
        
        #now that we have our partitions, we can recursively call subtrees based off elements
        #skip 0 index for root and go all up until, and including mid ofr preorder sublist
        #we need to take all elements from inorder up until mid for left subtree (mid is perfect partition of root)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


        