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
Ok, since we're need to:

1. find root from pre order traversal
2. use index of root in inorder to get split for left/right subtrees
3. recurse down to construct full tree.

we can also use left/right bounds on a helper function and a hashmap to take advantage of the in order nature of splittin gin order
to find absolute location of the elements we want to track in pre order
*/

#include <unordered_map>
#include <ranges> //need this for std::views::enumerate

class Solution {
private:
    std::unordered_map<int, int> lookup;

    int pre_idx = 0; //use an index to track where in the preorder array we're tracking a root (which root basically)

    //helper function to handle our left/right bounded dfs with absolute positions of pre order
    TreeNode* construct(vector<int>& preorder, int in_left, int in_right) 
    {
        if (in_left > in_right) return nullptr;

        //grab current root value using our preorder trackign index
        int root_val = preorder[pre_idx];
        TreeNode* root = new TreeNode(root_val);

        //move preorder index forward for hte next recursive call
        pre_idx++;

        //instant lookup for what is our preorder root index in our in order traversal
        int mid = lookup[root_val];

        /*
        Recurse using boundaries instead of slicing lists
        Left subtree boundaries: from current in_left up to mid - 1
        */
        root->left = construct(preorder, in_left, mid - 1);

        /*
        Right subtree boundaries: from mid + 1 up to current in_right
        */
        root->right = construct(preorder, mid + 1, in_right);

        return root;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        //enumerate through all the in order vector and populate hashmap
        for (auto [idx, value] : std::views::enumerate(inorder)) 
        {
            lookup[value] = idx;
        }

        return construct(preorder, 0, inorder.size() - 1);
    }
};
