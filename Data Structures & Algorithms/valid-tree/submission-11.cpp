/*
Ok, I think I figured out the "gimmick" to this problem: we need to store adjacency lists for both
u and v when an edge is [0,1] like 0: 1 AND 1: 0 becuase we have undirected edges
*/

#include <unordered_map>
#include <vector>
#include <set>
#include <queue>

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        //trivial proof
        if (n == 0) return true;

        unordered_map<int, vector<int>> adj;

        for (vector<int> edge : edges) 
        {
            int u = edge[0];
            int v = edge[1];

            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        //iterate through and create our dfs traversal
        set<int> visit;

        //create our visit q using only 
        queue<pair<int, int>> q;
        q.push({0, -1});

        while (!q.empty()) 
        {
            auto item = q.front();
            q.pop();
            int curr = item.first;
            int parent = item.second;

            //return false because loop detected
            if (visit.contains(curr)) return false;

            visit.insert(curr);

            //need to visit all the neighbors
            for (int v : adj[curr]) 
            {
                //skip the node we just came from to prevent false negatives
                if (v == parent) continue;

                //check if its valid, if not, return false
                q.push({v, curr});
            }
        }

        //proof by exhaustion
        return visit.size() == n;
    }
};
