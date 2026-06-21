/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

//lets solve with BFS for funsies

#include <deque>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        std::deque<TreeNode*> q;

        if (root) q.push_back(root);

        int depth = 0;
        while (!q.empty()) 
        {
            size_t to_eval = q.size();
            //dont use size since its evaluating upon every loop
            for (int i = 0; i < to_eval; i++) 
            {
                TreeNode* node = q.front();
                q.pop_front();

                if (node->left) q.push_back(node->left);
                if (node->right) q.push_back(node->right);
            }
            
            ++depth;
        }
        return depth;
    }
};
