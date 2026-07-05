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
Ok, unlike previously where we just do recursionslop, we should just try to maintain global "max path"
and update a refernce varaible
*/

#include <vector>
#include <algorithm>

class Solution {
private:
    std::vector<int> result; //use this to store max path results in a stack like structure

    int dfs(TreeNode* root) 
    {
        //base case where we return nothing if we hit beyond a leaf
        if (!root) return 0;

        //recursively compute left/right downward paths
        int left_max = dfs(root->left);
        int right_max = dfs(root->right);

        //ignore negative downward paths
        left_max = std::max(left_max, 0);
        right_max = std::max(right_max, 0);

        //replace top of stack with global max path
        result[0] = std::max(result[0], root->val + left_max + right_max);
        //return the value for children recursive stack
        return root->val + std::max(left_max, right_max);
    }
public:
    int maxPathSum(TreeNode* root) {
        result.push_back(root->val);

        //populate result array
        dfs(root);
        return result[0];
    }
};
