#include <vector>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
private:
    void bfs(int start_r, int start_c, vector<vector<bool>>& visited, vector<vector<int>>& heights) {
        const int ROWS = heights.size();
        const int COLS = heights[0].size();

        // Stores {r, c, prev_height}
        queue<tuple<int, int, int>> to_visit;
        to_visit.push({start_r, start_c, heights[start_r][start_c]});

        while (!to_visit.empty()) {
            auto [r, c, prev] = to_visit.front();
            to_visit.pop(); // CRITICAL: Pop the element from the stack

            // Out of bounds check
            if (r < 0 || c < 0 || r >= ROWS || c >= COLS) continue;
            
            // Flow rule check (uphill reverse search) & visited check
            if (visited[r][c] || heights[r][c] < prev) continue;

            // Mark as visited
            visited[r][c] = true;

            int curr_height = heights[r][c];

            // Traverse 4 directions
            to_visit.push({r + 1, c, curr_height});
            to_visit.push({r - 1, c, curr_height});
            to_visit.push({r, c + 1, curr_height});
            to_visit.push({r, c - 1, curr_height});
        }
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) return {};

        const int ROWS = heights.size();
        const int COLS = heights[0].size();

        // 2D boolean grids are much faster than std::set in C++
        vector<vector<bool>> pacific(ROWS, vector<bool>(COLS, false));
        vector<vector<bool>> atlantic(ROWS, vector<bool>(COLS, false));

        // Iterate over top/bottom rows
        for (int c = 0; c < COLS; c++) {
            bfs(0, c, pacific, heights);               // Top row -> Pacific
            bfs(ROWS - 1, c, atlantic, heights);       // Bottom row -> Atlantic
        }

        // Iterate over left/right columns
        for (int r = 0; r < ROWS; r++) {
            bfs(r, 0, pacific, heights);               // Left column -> Pacific
            bfs(r, COLS - 1, atlantic, heights);       // Right column -> Atlantic
        }

        // Collect intersection of cells reachable by both oceans
        vector<vector<int>> result;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.push_back({r, c});
                }
            }
        }

        return result;
    }
};