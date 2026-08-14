#include <queue>
#include <vector>

/*
If we work from outside in, its going to be much easier becuase we can just flood fill the connected portions to our outside things with 'G'
*/

class Solution {
private:
    int ROWS;
    int COLS; 
    void ff_dfs(vector<vector<char>>& board, int row, int col) 
    {
        queue<pair<int, int>> to_visit;

        to_visit.push({row, col});
        //mark curr
        board[row][col] = 'G';

        while (!to_visit.empty()) 
        {
            auto item = to_visit.front();
            to_visit.pop();

            int r = item.first;
            int c = item.second;

            vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

            for (auto direction : directions) 
            {
                int dr = direction.first;
                int dc = direction.second;

                int new_r = r + dr;
                int new_c = c + dc;

                //check dimensions
                if (new_r < 0 || new_r >= ROWS || new_c < 0 || new_c >= COLS) continue;

                //check to see if we have an 'O' character
                if (board[new_r][new_c] != 'O') continue;

                to_visit.push({new_r, new_c});
                board[new_r][new_c] = 'G';
            }
        }
    }
public:
    void solve(vector<vector<char>>& board) {
        //update values for rows and columns
        ROWS = board.size();
        COLS = board[0].size();

        //iterate through top and bottom runs and run ff_dfs
        for (int c = 0; c < COLS; c++) 
        {
            //top row
            if (board[0][c] == 'O') ff_dfs(board, 0, c);
            //bottom row
            if (board[ROWS - 1][c] == 'O') ff_dfs(board, ROWS - 1, c);
        }

        //iterate through left and right columns
        for (int r = 0; r < ROWS; r++) 
        {
            //left row
            if (board[r][0] == 'O') ff_dfs(board, r, 0);
            //right row
            if (board[r][COLS - 1] == 'O') ff_dfs(board, r, COLS - 1);
        }

        //iterate through board and update previous columsn accordingly
        for (int r = 0; r < ROWS; r++) 
        {
            for (int c = 0; c < COLS; c++) 
            {
                if (board[r][c] == 'O') board[r][c] = 'X';
                if (board[r][c] == 'G') board[r][c] = 'O';
            }
        }
    }
};
