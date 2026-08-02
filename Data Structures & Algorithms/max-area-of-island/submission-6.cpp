/*
ok this problem should be similar to number of islands problem except this time we need to be mindful we remove our
vertex (set it to zero) when we append a new visiting square to our array and remmeber to increment each time. 

I will code this up with flood fill dfs/bfs
*/

#include <queue>
#include <algorithm>

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_island_area = 0;

        for (int r = 0; r < grid.size(); r++) 
        {
            for (int c = 0; c < grid[r].size(); c++) 
            {
                if (grid[r][c]) 
                {
                    max_island_area = std::max(max_island_area, floodFillBFS(grid, r, c));
                }
            }
        }

        return max_island_area;
    }

    //this method returns the flood fill style dfs area of an island while setting it to zero so we dont
    //accidently double count
    int floodFillBFS(vector<vector<int>>& grid, int row, int col) 
    {
        queue<pair<int, int>> to_visit;

        to_visit.push({row, col});
        grid[row][col] = 0;

        const int NUM_ROWS = grid.size();
        const int NUM_COLS = grid[0].size();

        int island_area = 0;

        while (!to_visit.empty()) 
        {
            auto item = to_visit.front();
            to_visit.pop();

            int r = item.first;
            int c = item.second;

            island_area++;

            if (r + 1 < NUM_ROWS && grid[r + 1][c]) 
            {
                to_visit.push({r + 1, c});
                grid[r + 1][c] = 0;
            }
            if (r - 1 >= 0 && grid[r - 1][c]) 
            {
                to_visit.push({r - 1, c});
                grid[r - 1][c] = 0;
            }
            if (c + 1 < NUM_COLS && grid[r][c + 1]) 
            {
                to_visit.push({r, c + 1});
                grid[r][c + 1] = 0;
            }
            if (c - 1 >= 0 && grid[r][c - 1]) 
            {
                to_visit.push({r, c - 1});
                grid[r][c-1] = 0;
            }
        }

        return island_area;
    }
};
