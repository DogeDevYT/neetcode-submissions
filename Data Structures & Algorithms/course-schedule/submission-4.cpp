/*
I think the alternate solution to this course scheduling problem is Kahn's algorithm. We can solve this by 
keeping track of what courses have 0 indegree and repeatedly removing those from our graph and effectively
checking if theres anything left when our bfs queue is empty.

However, since we dont technically have a graph to topological sort, we will be using an adjaceny list and 
indegree list to simulate a graph
*/

#include <queue>
#include <vector>

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        //use this to keep track of the degree of "in" edges for each "node" (course integer)
        vector<int> indegree(numCourses);
        //keep an adjaceny list of each course node
        vector<vector<int>> adj(numCourses);

        //process each prereq into our adjaceny list and indegree list
        for (auto edge : prerequisites) 
        {
            int u = edge[0];
            int v = edge[1];
            indegree[v] += 1;
            adj[u].push_back(v);
        }

        //we can process this easily with bfs
        queue<int> q;

        //initial population
        for (int c = 0; c < numCourses; c++) 
        {
            if (indegree[c] == 0) q.push(c);
        }

        //this will track how many nodes we've effectively removed from our graph
        int finish = 0;

        while (!q.empty()) 
        {
            int u = q.front();
            q.pop();

            finish++;

            for (int v : adj[u]) 
            {
                indegree[v]--;

                //if we dont have any more incoming edges we can push to bfs queue for kahns algorithm
                if (indegree[v] == 0) q.push(v);
            }
        }

        //check to see if we've removed enough courses from our graph
        return finish == numCourses;
    }
};
