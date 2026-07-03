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
Lets get this working with a helper function for inorder traversal for recursive dfs
*/

#include <vector>

class Solution {
private:
    int kVal = -1;
    std::vector<int> vals;
    int in_order(TreeNode* root) 
    {
        if (!root) return -1;

        if (root->left) 
        {
            int left_res = in_order(root->left);
            if (left_res != -1) 
            {
                return left_res;
            }
        }

        vals.push_back(root->val);
        kVal--;

        //actually return our value fr if our k val == 0
        if (kVal == 0) 
        {
            return vals.back();
        }

        if (root->right) 
        {
            int right_res = in_order(root->right);
            if (right_res != -1) 
            {
                return right_res;
            }
        }
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        kVal = k;
        return in_order(root);
    }
};
