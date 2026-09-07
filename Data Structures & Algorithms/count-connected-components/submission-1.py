"""
for i in 0..n-1:
    bfs
    visited = {0, 1, 2}
    increment our total island count

    visited = {0,1,2}
    bfs
    visited = {0, 1, 2}
"""
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #store the count of islands
        islands = 0

        #generate adjacency list
        adj = [[] for i in range(n)]

        for u,v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        #create a set of nodes we visited
        visited = set()

        def bfs(curr_node, parent):
            to_visit = deque()
            to_visit.append((curr_node, parent))

            #utilize data structure behavior to not stop iterating until we've fully traversed graph
            while to_visit:
                curr, curr_parent = to_visit.popleft()

                if curr in visited: continue

                #remember to add the current node to visited
                visited.add(curr)

                for v in adj[curr]:
                    if v == parent: continue
                    if v in visited: continue #skip adding nodes we've already seen

                    to_visit.append((v, curr))
        
        for u in range(n):
            if u not in visited:
                bfs(u, -1)
                islands += 1
        
        return islands

        
