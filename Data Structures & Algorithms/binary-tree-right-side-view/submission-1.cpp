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
Lets get our cpp bfs solution working with queue for fast movements fr

basically we just add the last element in our bfs traversal into the solution vector because its guarenteed
to work since we need the rightmost element in a level and bfs is level-order traversal
*/

#include <queue>
#include <vector>

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        //queue to track our nodes to visit/visit next
        std::queue<TreeNode*> to_visit;

        //create our return vector
        std::vector<int> sol;

        //add our root if its valid
        if (root) to_visit.push(root);

        //hit our bfs
        while (!to_visit.empty()) 
        {
            //store our current length because cpp dynamically recomputes size of vectors (queue is a vector)
            //while in for loops
            int level_len = to_visit.size();
            int target = level_len - 1; //store last elemnt index

            //iterate over every node in our level
            for (int i = 0; i < level_len; i++) 
            {
                TreeNode* curr = to_visit.front();

                //check if we're on rightmost element
                if (i == target) sol.push_back(curr->val);

                //remove current element from queue
                to_visit.pop();

                //add on children if applicable for next level
                // rmeember - > left first
                if (curr->left) to_visit.push(curr->left);
                if (curr->right) to_visit.push(curr->right);
            }
        }

        return sol;
    }
};
