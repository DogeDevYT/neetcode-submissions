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
Lets go ahead and code up a light recursive DFS solution here
*/

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;

        //swap
        TreeNode* temp = root->right;
        root->right = root->left;
        root->left = temp;

        //recurse on children
        invertTree(root->right);
        invertTree(root->left);

        //return the root after we finish our DFS recursively
        return root;
    }
};
