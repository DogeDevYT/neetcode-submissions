/*
Ok, lets try a flood-fill style dfs here in cpp. In short, we need to try and mark every character in the grid
that we have visited as inaccurate, and once we do this, we need to increment our original island as visited.

for an extra challenge lets, get this working without recursion
*/

#include <vector>
#include <queue>

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;

        //use our flood fill DFS function here
        for (int r = 0; r < grid.size(); r++) 
        {
            for (int c = 0; c < grid[0].size(); c++) 
            {
                if (grid[r][c] == '1') 
                {
                    islands++;
                    floodFillBFS(grid, r, c);
                }
            }
        }

        return islands;
    }

    void floodFillBFS(vector<vector<char>>& grid, int row, int col) 
    {
        const int NUM_ROWS = grid.size();
        const int NUM_COLS = grid[0].size();

        queue<pair<int, int>> to_visit;

        to_visit.push({row, col});

        while (!to_visit.empty()) 
        {
            auto node = to_visit.front();
            to_visit.pop();

            int r = node.first;
            int c = node.second;

            grid[r][c] = '0';
            if (r + 1 < NUM_ROWS && grid[r + 1][c] == '1') to_visit.push({r + 1, c});
            if (r - 1 >= 0 && grid[r-1][c] == '1') to_visit.push({r - 1, c});
            if (c + 1 < NUM_COLS && grid[r][c + 1] == '1') to_visit.push({r, c + 1});
            if (c - 1 >= 0 && grid[r][c-1] == '1') to_visit.push({r, c-1});
        }
    }
};
