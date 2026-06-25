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
guh iterative dfs GO
*/

#include <deque>
#include <utility> //for pair

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        //create our vector with nodes to visit
        std::deque<std::pair<TreeNode*, TreeNode*>> to_visit = {std::make_pair(p, q)};

        while (!to_visit.empty()) 
        {
            //get our values
            TreeNode* n1 = to_visit.front().first;
            TreeNode* n2 = to_visit.front().second;

            to_visit.pop_front();

            //edgge cases:
            //1: p and q both dont exist => continue because we have to chekc our other nodes
            //2: p exists but q doens't exit => return false because q doesn' thave value
            //3: p doesn't exist but q exists -> return false because p doesn't have value
            
            //and then finally we have to actually evaluate in the else case

            if (!n1 && !n2) 
            {
                continue;
            } else if (n1 && !n2) 
            {
                return false;
            } else if (!n1 && n2) 
            {
                return false;
            } else 
            {
                //check equality on singular node
                if (n1->val != n2->val) return false;

                //otherwise append both nodes to list
                to_visit.push_back(std::make_pair(n1->left, n2->left));
                to_visit.push_back(std::make_pair(n1->right, n2->right));
            }
        }
        return true;
    }
};
