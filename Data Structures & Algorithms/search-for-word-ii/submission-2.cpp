#include <unordered_map>
#include <string>
#include <set>
#include <vector>
#include <utility>

using namespace std;

class TrieNode 
{
public:
    std::unordered_map<char, TrieNode*> children;
    bool isWord;

    TrieNode() 
    {
        isWord = false;
    }

    void addWord(std::string word) 
    {
        if (word.empty()) 
        {
            isWord = true;
            return;
        }

        char c = word[0];
        if (!children.contains(c)) children[c] = new TrieNode();
        children[c]->addWord(word.substr(1));
    }
};

class Solution {
public:
    // Fixed: row and column passed by value (int, not int&)
    void dfs(int row, int column, TrieNode* node, std::string& word, 
        std::set<std::string>& result, 
        std::set<std::pair<int, int>>& visit,
        int ROWS,
        int COLS,
        vector<vector<char>>& board) 
    {
        if (row < 0 || column < 0 || row >= ROWS || column >= COLS || 
            visit.contains(std::make_pair(row, column)) || 
            !node->children.contains(board[row][column])) return;

        visit.insert(std::make_pair(row, column));
        TrieNode* curr = node->children[board[row][column]]; // The current node we stepped onto
        word += board[row][column];

        if (curr->isWord) { // Fixed: checking curr instead of node
            result.insert(word);
            curr->isWord = false; // Optional optimization to avoid duplicate checking
        }

        int up = row + 1;
        int down = row - 1;
        int right = column + 1;
        int left = column - 1;

        // Fixed: Passing 'curr' instead of 'node' so the tree traversal actually moves forward
        dfs(up, column, curr, word, result, visit, ROWS, COLS, board);
        dfs(down, column, curr, word, result, visit, ROWS, COLS, board);
        dfs(row, right, curr, word, result, visit, ROWS, COLS, board);
        dfs(row, left, curr, word, result, visit, ROWS, COLS, board);

        // Fixed: Backtrack both the visited set AND the passed string reference
        word.pop_back(); 
        visit.erase(std::make_pair(row, column));
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();

        for (string w : words) 
        {
            root->addWord(w);
        }

        int ROWS = board.size();
        int COLS = board[0].size();

        std::set<std::string> res = {};
        std::set<std::pair<int, int>> visit = {};

        for (int r = 0; r < ROWS; r++) 
        {
            for (int c = 0; c < COLS; c++) 
            {
                std::string start = "";
                dfs(r, c, root, start, res, visit, ROWS, COLS, board);
            }
        }

        // Fixed: type cast to vector<string>
        return std::vector<std::string>(res.begin(), res.end());
    }
};