class Solution:
    """
    Ok I think the way we want to run this is that we should have a set of all visited nodes and then just 
    use DFS to make sure:

    1) there are no cycles
    2) the graph is fully connected (n-1 edges)
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        

        adj = {i:[] for i in range(n)}

        #populate adjanceny list
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set() #keep track of all nodes we visit
        def dfs(i, prev):
            if i in visit:
                return False #loop detected
            visit.add(i)

            #visit all neighbors
            for v in adj[i]:
                #skip the node we came from to prevent false negatives
                if v == prev:
                    continue
                
                #check if its valid, if not return false
                if not dfs(v, i):
                    return False
        
            #proof by exhaustion
            return True
        
        #we want to pass in -1 becuase we know that -1 will never exist in our chud graph
        #we also need to make sure the length of nodes we visited is the same as our total nodes
        #to guarentee full connectivity
        return dfs(0, -1) and n == len(visit)
                
            



        
        