/*
Ok so, if we tried naively brute forcing the entire problem, this would turn out terribly. I think teh optimal
solution is to keep hash sets of the columns we insert into (because we're doing row-major iteration), positive diagonal
(r + c) values and negative diagonal (r - c) values. We also need to keep a running copy of our boards (current), and
a copy of the total possible solutions (res)
*/

#include <set>

class Solution {
private:
    std::set<int> cols;
    std::set<int> pos_diag;
    std::set<int> neg_diag;

    void backtrack(vector<string>& board, vector<vector<string>>& res, int r, int n) 
    {
        //base case - row we're iterating in becomes n, so we need to append our result to res
        if (r == n) 
        {
            res.push_back(board);
            return;
        }

        //check for failing conditions i.e. Queen attacking current square
        for (int c = 0; c < n; c++) 
        {
            if (cols.contains(c) || pos_diag.contains(r + c) || neg_diag.contains(r - c)) continue;

            //place queen
            cols.insert(c);
            pos_diag.insert(r + c);
            neg_diag.insert(r - c);

            board[r][c] = 'Q';

            //backtrack
            backtrack(board, res, r + 1, n);

            //reverse backtrack
            cols.erase(c);
            pos_diag.erase(r + c);
            neg_diag.erase(r - c);

            board[r][c] = '.';  
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        //make our board
        std::string row = "";

        for (int r = 0; r < n; r++) row += '.';

        std::vector<std::string> board = {};

        for (int c = 0; c < n; c++) board.push_back(row);

        std::vector<std::vector<std::string>> result = {};

        backtrack(board, result, 0, n);
        return result;
    }
};
