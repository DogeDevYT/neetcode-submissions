"""
Ok, lets run this one more time. Basically we need to have a list of prereqs for each course with an empty list
being a case case. Then we can run dfs on each node in the prereq list recursively. Once we model this as a DAG
it becomes a lot easier to visualize
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dictionary comprehensiont o create [] entires for all possible courses
        prereqs = {i: [] for i in range(numCourses)}

        #populate prereqs dictionary
        for edge in prerequisites:
            u = edge[0]
            v = edge[1]

            #update prereqs hashmap
            prereqs[u].append(v)
        
        visited = set()

        """
        basically we denote the current level of the dfs traversal with elements we've seen in our DAG
        and the current node
        """
        def dfs(u):
            #base case - we've hit an element we've already seen in our current DFS traversal
            #return false
            if u in visited:
                return False

            #base case - we've hit a prereq sequence that works, return true
            if not prereqs[u]:
                return True
            
            #call our function with all the prereqs
            visited.add(u)

            #traverse all prereq children in DAG
            for v in prereqs[u]:
                if not dfs(v):
                    return False
            
            #backtrack and memoize
            visited.remove(u)
            prereqs[u] = [] #we can mark this node as safe because we know its prereq chain is safe
            
            return True
        
        #now we need to call our function on all our possible courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
            

        