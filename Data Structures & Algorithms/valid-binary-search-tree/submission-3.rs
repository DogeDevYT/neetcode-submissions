// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::rc::Rc;
use std::cell::RefCell;

/*
Lets get out helper function with dfs working now
*/
impl Solution {
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        //call our helper function
        return Self::dfs_range(root, None, None);
    }
    fn dfs_range(root: Option<Rc<RefCell<TreeNode>>>, min: Option<i32>, max: Option<i32>) -> bool {
        if let Some(node_rc) = root {
            let node = node_rc.borrow(); // Correctly borrow the RefCell
            
            // Check lower bound
            if let Some(min_val) = min {
                if node.val <= min_val { return false; }
            }
            
            // Check upper bound
            if let Some(max_val) = max {
                if node.val >= max_val { return false; }
            }

            // Recurse: update bounds
            Self::dfs_range(node.left.clone(), min, Some(node.val)) && 
            Self::dfs_range(node.right.clone(), Some(node.val), max)
        } else {
            true
        }
    }
}
