/*
Ok, I think I know what to do here now. We need to use a multi-source BFS approach along with only iterating
our time value after each "level" of our queue is done.
*/

#include <queue>
#include <vector>

#define EMPTY 0
#define FRESH 1
#define ROTTEN 2

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int time = 0;
        int fresh = 0;

        const int ROWS = grid.size();
        const int COLS = grid[0].size();

        //iterate over grid and populate sources of multi-source bfs as rotting oranges
        for (int row = 0; row < ROWS; row++) 
        {
            for (int col = 0; col < COLS; col++) 
            {
                int curr = grid[row][col];

                if (curr == FRESH) 
                {
                    fresh++;
                } else if (curr == ROTTEN) 
                {
                    q.push({row, col});
                }
            }
        }

        //iterate while q isn't empty and we have a fresh orange left over to save computation time
        while (!q.empty() && fresh > 0) 
        {
            //since we're going to be modifying the length of q mid-run, we need to save its length
            size_t qlen = q.size();

            //we need to increment timestamp after each "level"
            for (int i = 0; i < qlen; i++) 
            {
                auto item = q.front();
                q.pop();

                int row = item.first;
                int col = item.second;

                vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

                for (auto direction : directions) 
                {
                    int dr = direction.first;
                    int dc = direction.second;

                    int new_r = row + dr;
                    int new_c = col + dc;

                    //check bounds
                    if (new_r < 0 || new_r >= ROWS || new_c < 0 || new_c >= COLS) continue;

                    //check to see if we selected the right type thing (fresh fruit)
                    if (grid[new_r][new_c] != FRESH) continue;

                    //mark and add the new item to our queue
                    grid[new_r][new_c] = ROTTEN;
                    fresh--;
                    q.push({new_r, new_c});
                }
            }
            time++;
        }

        if (fresh > 0) return -1;

        return time;
    }
};
