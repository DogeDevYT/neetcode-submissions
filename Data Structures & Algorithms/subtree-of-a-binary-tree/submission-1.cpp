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
lets just get our basic O(m*n) iterative dfs + helper function going
*/
class Solution {
private:
    //recursive helper method to check equality
    bool checkNode(TreeNode* root, TreeNode* subRoot) 
    {
        //create other variable to reference root and subroot for easy typing
        TreeNode* r = root;
        TreeNode* sr = subRoot;

        if (!r && !sr) 
        {
            //this is a base case where we recurse into node that DNE for both which means we haven to 
            //return true
            return true;
        } else if (!r && sr) 
        {
            //node dne but subnode exists, clear return false base case
            return false;
        } else if (r && !sr) 
        {
            //node exists but subnode dns, clear return false base case
            return false;
        } else 
        {
            //just recurse into all children tbh
            return (r->val == sr->val) && checkNode(r->left, sr->left) && checkNode(r->right, sr->right);
        }
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        //iterative dfs
        
        std::vector<TreeNode*> visited = {root};

        while (!visited.empty()) 
        {
            TreeNode* node = visited.back();
            visited.pop_back();

            if (!node) continue; //skip null things

            if (checkNode(node, subRoot)) return true;

            //add our stuff to visiting array
            visited.push_back(node->left);
            visited.push_back(node->right);
        }

        //we have literally traversed our entire tree so we should now be guaurenteed a not found
        return false;
    }
};
