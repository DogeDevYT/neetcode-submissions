from collections import deque

"""
Lets try using Kahn's algorithm here
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #indegree list
        indegree = [0] * numCourses

        #adjaceny list
        adj = [[] for i in range(numCourses)]

        for u, v in prerequisites:
            indegree[v] += 1
            adj[u].append(v)
        

        #populate the queue with all our items
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
            
        finish = 0
        solution_maybe = []

        while q:
            u = q.popleft()
            finish += 1
            solution_maybe.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        #reverse because the graph is tracking the course to its prerequisites, not the other way around
        solution_maybe = solution_maybe[::-1]
        
        print(solution_maybe)
        
        return solution_maybe if finish == numCourses else []