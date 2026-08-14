/*
Ok so basically the main thing we need to realize here is that we need to basically keep a hashmap of
each prereq combination and then run dfs on this for every node, marking the ones that are valid
*/

#include <unordered_map>
#include <vector>
#include <set>

class Solution {
private:
    unordered_map<int, vector<int>> prereqs;
    set<int> visited;
    bool dfs(int u) 
    {
        //base case - we've already seen elment so we need to return false
        if (visited.contains(u)) return false;

        //base case - we've hit a prereq sequence that works (no prereqs on this) - return true
        if (prereqs[u].empty()) return true;

        //add our current node that we're visiting to list
        visited.insert(u);

        //traverse all prereq children in DAG
        for (int v : prereqs[u]) 
        {
            //if the dfs for one of the children turns out to be bust we need to return false
            if (!dfs(v)) return false;
        }

        //backtrack and memoize to save compute
        visited.erase(u);
        prereqs[u] = {}; //can mark this node as safe becuase we know its prereq chain is safe

        //if we get here we know our node is good and we can return true
        return true; 
    }
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        //populate hashmap of prereqs
        for (int i = 0; i < numCourses; i++) 
        {
            prereqs[i] = {};
        }

        for (auto prereq : prerequisites) 
        {
            int u = prereq[0];
            int v = prereq[1];

            prereqs[u].push_back(v);
        }

        //now we can use our dfs node on every course using our prereqs hashmap
        for (int c = 0; c < numCourses; c++) 
        {
            if (!dfs(c)) return false;
        }

        //guarenteed to work here
        return true;
    }
};
