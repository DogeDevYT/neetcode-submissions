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

/*
Lets just get our basic chud bfs algorithm going now
*/

#include <vector>
#include <queue>

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        //create our ordering list to visit
        std::queue<TreeNode*> to_visit;

        //add our root if its valid
        if (root) to_visit.push(root);

        //create vec for solution array
        std::vector<std::vector<int>> sol;

        while (!to_visit.empty()) 
        {
            //get size of curent bfs vec
            int bfs_len = to_visit.size();

            //initalize vec of current elements to add to the solution vec
            std::vector<int> curr;

            for (int i = 0; i < bfs_len; i++) 
            {
                TreeNode* node = to_visit.front();
                to_visit.pop(); //move queue along

                curr.push_back(node->val);

                if (node->left) to_visit.push(node->left);
                if (node->right) to_visit.push(node->right);
            }

            sol.push_back(curr);
        }
        return sol;
    }
};
