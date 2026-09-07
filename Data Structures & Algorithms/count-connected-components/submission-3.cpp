#include <vector>
#include <stack>
#include <set>
#include <unordered_map>

class Solution {
private:
    unordered_map<int, vector<int>> adj;
    set<int> visited;

    void dfs(int curr_node, int parent) 
    {
        stack<pair<int, int>> to_visit;

        to_visit.push({curr_node, parent});

        while (!to_visit.empty()) 
        {
            auto item = to_visit.top();
            to_visit.pop();

            int u = item.first;
            int prev = item.second;

            if (visited.contains(u)) continue;

            visited.insert(u);

            for (int v : adj[u]) 
            {
                if (v == prev) continue;
                if (visited.contains(v)) continue;

                to_visit.push({v, prev});
            }
        }
    } 
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        //initialize island counter
        int islands = 0;

        for (auto& item : edges) 
        {
            int u = item[0];
            int v = item[1];

            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        for (int u = 0; u < n; u++) 
        {
            if (!visited.contains(u)) 
            {
                dfs(u, -1);
                islands++;
            }
        }

        return islands;
    }
};
