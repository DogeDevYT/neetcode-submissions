/*
Allright this problem shouldn't be too difficult all we need to do here is just
run a naive backtracking algorithm on each of the possible movements and 
check for 5 possible base cases:

1. empty word - return true
2. out of bounds - return false
3. already seen element - return false
4. current character doesn't match word sequence - return false
5. last character matches - return true
*/

#include <utility>
#include <set>
#include <vector>
#include <string>

class Solution {
private:
    int n = -1, m = -1;
    std::set<std::pair<int, int>> seen;
    //make const to denote passing by value
    bool backtrack(const vector<vector<char>> board, const string& word, int row, int col) 
    {
        if (word.empty()) return true;

        if (row < 0 || row >= n || col < 0 || col >= m) return false;

        if (seen.contains(std::make_pair(row, col))) return false;

        if (board[row][col] != word[0]) return false;

        if (word.size() == 1) return true;

        seen.insert(std::make_pair(row, col));

        bool ret = backtrack(board, word.substr(1), row - 1, col) ||
            backtrack(board, word.substr(1), row + 1, col) ||
            backtrack(board, word.substr(1), row, col - 1) ||
            backtrack(board, word.substr(1), row, col + 1);

        seen.erase(std::make_pair(row, col));

        return ret;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        n = board.size();
        m = board[0].size();

        //row major iteration and calling our backtrack helper
        for (int r = 0; r < board.size(); r++) 
        {
            for (int c = 0; c < board[0].size(); c++) 
            {
                //reset seen to match new possible state
                seen = {};

                if (backtrack(board, word, r, c)) return true;
            }
        }

        return false;
    }
};
