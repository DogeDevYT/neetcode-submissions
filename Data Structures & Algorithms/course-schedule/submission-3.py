from collections import deque

"""
I think the main point of Kahn's algorithm is to repeatedly process nodes by using a queue/bfs structure where we
remove nodes with no indegree and check at the end if theres anything left, implying a cycle
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #we take into account the indegree (number of incoming edges and keep removing the ones that have an)
        #indegree of zero
        indegree = [0] * numCourses
        #keep an adjacency list of each course node
        adj = [[] for i in range(numCourses)]

        #process all our prereqs into our adjaceny and indgree list
        for u, v in prerequisites:
            indegree[v] += 1
            adj[u].append(v)
        
        #we can effectively implement kahns algorithm with bfs because its queue structure is perfect for processing
        #nodes and removing from our prereq representation graph
        #if you think about we're really just topological sorting

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            u = q.popleft()
            finish += 1
            for v in adj[u]:
                indegree[v] -= 1
                #if we dont have any more incoming edges we can append to bfs queue (kahn's algorithm)
                if indegree[v] == 0:
                    q.append(v)
        
        return finish == numCourses #this is how we check if theres any "nodes" left