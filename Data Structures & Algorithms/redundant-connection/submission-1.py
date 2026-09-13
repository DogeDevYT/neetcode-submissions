class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)] #ith node -> parent (1 - n)
        rank = [1] * (N + 1)

        #recursively find parent
        def find(n):
            if n != par[n]:
                par[n] = find(par[n]) #path compression
            return par[n]
        #try to combine 2 sets
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            #perform union by rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            #return true if n1 and n2 weren't already connected
            return True
        

        #go edge by edge and unpack the 2 nodes and keep trying our DSU until we find something
        #that has same parent, therefore redunant edge, therefore we need to return
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]