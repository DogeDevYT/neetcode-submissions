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
Ok now lets try converting this into iterative dfs with cpp using a stack and a hashmap for post-order
traversal processing
*/

#include <unordered_map>
#include <stack>
#include <utility> //for pair
#include <algorithm> //max

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (!root) return 0; //for empty case

        int max_diameter = 0;
        std::stack<std::pair<TreeNode*, bool>> visited; //stores nodes we visited and calculated height for
        std::unordered_map<TreeNode*, int> heights; //stores node to height hashmap

        // add base case
        heights[nullptr] = 0;
        visited.push(std::make_pair(root, false));

        while (!visited.empty()) 
        {
            TreeNode* node = visited.top().first;
            bool is_visited = visited.top().second;

            visited.pop();

            //skip nodes that dont have a reference
            if (!node) continue;

            if (is_visited) 
            {
                /*
                if we visited this node before it means we've already stored the heights of our 
                left and right child in heights dictionary so then all we have to do is update max_diamater
                and calculate this nodes height and save it in heights dictionary since we're going 
                "bottom up" now
                */
                max_diameter = max(max_diameter, heights[node->left] + heights[node->right]);
                heights[node] = 1 + max(heights[node->left], heights[node->right]);
            } else 
            {
                /*
                Since we want to evaluate this in post order (left,right,root)
                we need to push the right node onto stack before left and root needs to be before right
                */
                visited.push(std::make_pair(node, true));
                //left and right children need to be added to root as false so they can be explored
                visited.push(std::make_pair(node->left, false));
                visited.push(std::make_pair(node->right, false));
            }
        }
        return max_diameter;
    }
};
