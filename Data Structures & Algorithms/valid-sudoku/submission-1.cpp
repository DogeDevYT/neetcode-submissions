#include <unordered_map>

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //initialize hash set of rows and cols
        std::unordered_map<int, std::unordered_set<char>> rows, cols;
        //initialize hash set involving a pair<int, int> type as key for squares (will be importnat later)
        std::map<std::pair<int, int>, std::unordered_set<char>> squares;

        //iterate over rows and columsn in one pass
        for (int r = 0; r < 9; r++) 
        {
            for (int c = 0; c < 9; c++) 
            {
                //skip current cell if its blank
                if (board[r][c] == '.') continue;

                std::pair<int, int> squareKey = { r / 3, c / 3 };

                //check if current element is in rows or columns
                if (
                    rows[r].count(board[r][c]) ||
                    cols[c].count(board[r][c]) ||
                    squares[squareKey].count(board[r][c])
                ) return false;

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[squareKey].insert(board[r][c]);
            }
        }
        return true;
    }
};
