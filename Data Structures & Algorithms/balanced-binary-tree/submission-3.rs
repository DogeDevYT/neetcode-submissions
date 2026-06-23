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
use std::cmp::max;

/*
Instead of using memoized DP, we can get it working with a single-pass
O(n) approach
*/

impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool 
    {
        //if our helper function returns -1, that means the 
        //binary tree isn't balanced
        Self::check_height(&root) != -1
    }

    //Single-pass helper function
    fn check_height(root: &Option<Rc<RefCell<TreeNode>>>) -> i32 
    {
        match root 
        {
            //Base case - A node with height of 0
            None => 0,
            Some(node_rc) => 
            {
                //borrow node to safely look at children
                let node = node_rc.borrow();

                //check left subtree
                let left_h = Self::check_height(&node.left);
                if left_h == -1 
                {
                    //propogate unbalance error upwards
                    return -1;
                }

                //check right subtree
                let right_h = Self::check_height(&node.right);
                if right_h == -1 
                {
                    //propogate unbalance error upwards
                    return -1;
                }

                //check if current node violates balance condition
                if (left_h - right_h).abs() > 1 
                {
                    return -1; //propogate
                }

                //return actual subtree height if its balanced
                1 + max(left_h, right_h)
            }
        }
    }
}
