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
Yeah so basically we're trying to find a split point where we can't leverage
the BST prooperty of left less right more than current node to efficiently
search for hte split point where we either:

A. have to go different directions for children values 
OR
B. one of our left/right children is p or q so we can just return our current node

we can solve this quite easily with iteration
*/

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        //get target values
        int pVal = p->val;
        int qVal = q->val;

        TreeNode* curr = root;

        while (curr) 
        {
            bool goLeft = (curr->val > pVal) && (curr->val > qVal);// && (curr->left != p) && (curr->left != q);
            bool goRight = (curr->val < pVal) && (curr->val < qVal);// && (curr->right != p) && (curr->right != q);

            if (goLeft) 
            {
                curr = curr->left;
            } else if (goRight) 
            {
                curr = curr->right;
            } else 
            {
                return curr;
            }
        }
    }
};
