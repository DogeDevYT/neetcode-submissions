/*
ok so I think teh solution here is to use multi-source BFS becuase we can work outwards from the inner treasure parts
and mark all the squares
*/

#include <cmath> //std::pow
#include <queue>
#include <vector>

class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        //going to be using const
        int constexpr WATER = -1;
        int constexpr TREASURE = 0;
        const int LAND = std::pow(2, 31) - 1;

        //create const for number of rows and columsn
        const int NUM_ROWS = grid.size();
        const int NUM_COLS = grid[0].size();

        //create our bfs queue and populate it with multiple treasure sources
        queue<pair<int, int>> q;

        for (int row = 0; row < NUM_ROWS; row++) 
        {
            for (int col = 0; col < NUM_COLS; col++) 
            {
                if (grid[row][col] == TREASURE) q.push({row, col});
            }
        }

        //now we can start our multi source BFS
        while (!q.empty()) 
        {
            auto item = q.front();
            q.pop();

            int row = item.first;
            int col = item.second;

            //allign all the new slots based off of current distance
            int curr_dist = grid[row][col];

            vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

            for (auto direction : directions) 
            {
                int dr = direction.first;
                int dc = direction.second;

                int new_r = row + dr;
                int new_c = col + dc;

                //check bounds
                if (new_r < 0 || new_r >= NUM_ROWS || new_c < 0 || new_c >= NUM_COLS) continue;

                //check to make sure we haven't run into water, treasure, or already filled grid slot
                if (grid[new_r][new_c] != LAND) continue;

                grid[new_r][new_c] = curr_dist + 1;
                q.push({new_r, new_c});
            }
        }
    }
};
