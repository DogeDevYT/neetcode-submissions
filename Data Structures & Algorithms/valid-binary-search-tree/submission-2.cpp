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
Lets get our previous plan of having a max/min amount to be searching for with recursive dfs
*/

//since we're guarented to eb greater than -1001 and less than 1001
#define NEG_MAX -10000000000
#define POS_MAX 10000000000

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return dfsRange(root, NEG_MAX, POS_MAX);
    }
    bool dfsRange(TreeNode* root, int left, int right) 
    {
        if (!root) 
        {
            return true;
        } else if (!((left < root->val) && (root->val < right))) 
        {
            return false;
        } else 
        {
            return dfsRange(root->left, left, root->val) && dfsRange(root->right, root->val, right);
        }
    }
};
