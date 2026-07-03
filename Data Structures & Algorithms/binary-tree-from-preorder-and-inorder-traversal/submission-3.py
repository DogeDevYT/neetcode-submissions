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

Lets try getting this working with a hashmap
"""

class Solution:
    def __init__(self):
        self.lookup = {}
        self.pre_idx = 0 #we use a pointer to track what root we're currently looking at in pre order
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #populate hashmap
        for index, val in enumerate(inorder):
            self.lookup[val] = index
        
        #call recursive helper using boundary pointers from (0 to len - 1)
        return self.construct(preorder, 0, len(inorder) - 1)
    def construct(self, preorder: List[int], in_left: int, in_right: int) -> Optional[TreeNode]:
        # Base case: if our left boundary crosses our right boundary, the subtree is empty
        if in_left > in_right:
            return None
        

        # 1. Grabbing the current root value using our preorder tracking index
        root_val = preorder[self.pre_idx]
        root = TreeNode(root_val)
        
        # Move the preorder index forward for the next recursive call
        self.pre_idx += 1

        # 2. O(1) Instant Lookup for the partition index
        mid = self.lookup[root_val]
        
        # 3. Recurse using boundaries instead of slicing lists
        # Left subtree boundaries: from current in_left up to mid - 1
        root.left = self.construct(preorder, in_left, mid - 1)
        
        # Right subtree boundaries: from mid + 1 up to current in_right
        root.right = self.construct(preorder, mid + 1, in_right)

        return root


        