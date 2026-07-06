class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append("N") # Mark null nodes explicitly
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(res) # No CHUNGUS needed, just a clean comma-separated string

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        # Use an iterator so we can consume values one by one across recursive calls
        vals_iter = iter(vals) 
        
        def dfs():
            val = next(vals_iter)
            if val == "N":
                return None
            
            # Create the node (converting back to an integer!)
            node = TreeNode(int(val))
            # Because it's preorder, the next tokens in the iterator 
            # belong exactly to the left subtree, then the right subtree
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()