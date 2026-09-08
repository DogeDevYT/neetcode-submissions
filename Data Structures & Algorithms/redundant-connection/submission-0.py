class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def find(self, node):
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        #already connect, cycle detected!
        if pu == pv: return False

        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu] 
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #we can use our DSU algorithm to find the first isntance of a unable to be connected (cycle)
        #and then return that

        dsu = DSU(len(edges))

        for u,v in edges:
            if not dsu.union(u, v):
                return [u,v]