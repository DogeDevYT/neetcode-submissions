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
Allright lets go ahead and get this going as a chud DP solution with
hashmap
*/

#include <unordered_map> //hashmap
#include <algorithm> //max
#include <cmath> //abs

class Solution {
private:
    std::unordered_map<TreeNode*, int> heights;

    int nodeHeight(TreeNode* root) 
    {
        if (!root) return 0;
        if (heights.contains(root)) return heights[root];

        int rv = 1 + max(nodeHeight(root->left), nodeHeight(root->right));

        heights[root] = rv;
        return heights[root];
    }
public:
    bool isBalanced(TreeNode* root) {
        //base case for child of leaf node
        if (!root) return true;

        int left = nodeHeight(root->left);
        int right = nodeHeight(root->right);

        return ((std::abs(left - right) < 2) && isBalanced(root->left) && isBalanced(root->right));
    }
};
