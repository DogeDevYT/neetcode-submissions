"""Ok now lets get our topological sort with DFS"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[crs] += 1 #we're building a reverse graph to take advantage of dfs
            adj[pre].append(crs)
        
        output = []

        def dfs(node):
            output.append(node)
            indegree[node] -= 1

            for crs in adj[node]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    dfs(crs)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        
        return output if len(output) == numCourses else []