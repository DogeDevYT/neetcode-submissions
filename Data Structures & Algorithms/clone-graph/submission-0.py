"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
I think this should just be an easy recursive dfs type approach but lets see here. 

Ok I've been thinkgin about this wrong, we need to use a hashmap to get the behavior of the nodes and returning
references correctly
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            copy = Node(node.val)
            #forgot to set the visited map!
            visited[node] = copy

            for new_node in node.neighbors:
                #forgot to correctly assign the neighbors in the copy node
                copy.neighbors.append(dfs(new_node))
            
            return copy
        
        if node:
            return dfs(node)
        else:
            return None
            