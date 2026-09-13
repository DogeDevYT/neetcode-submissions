#include <vector>

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int N = edges.size();

        vector<int> parent(N + 1), rank(N + 1, 1);

        for (int i = 0; i < N; i++) 
        {
            parent[i] = i;
        }

        for (int i = 0; i < N; i++) 
        {
            rank.push_back(1);
        }

        //iterate through edges and unpack
        for (auto edge : edges) 
        {
            int n1 = edge[0];
            int n2 = edge[1];

            if (!dsu(parent, rank, n1, n2)) 
            {
                return {n1, n2};
            }
        }
    }
private:

    int find(vector<int>& parent, int n1) 
    {
        int p = parent[n1];

        while (p != parent[p]) 
        {
            parent[p] = parent[parent[p]];
            p = parent[p];
        }

        return p;
    }

    bool dsu(vector<int>& parent, vector<int>& rank, int n1, int n2) 
    {
        int p1 = find(parent, n1);
        int p2 = find(parent, n2);

        if (p1 == p2) return false;

        //optomize rank
        if (rank[p1] > rank[p2]) 
        {
            parent[p2] = p1;
            rank[p1] += rank[p2];
        } else 
        {
            parent[p1] = p2;
            rank[p2] += rank[p1];
        }

        return true;
    }
};
