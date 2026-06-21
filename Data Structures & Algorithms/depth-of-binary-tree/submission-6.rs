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

//lets use an iterative DFS approach

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut to_visit: Vec<(Rc<RefCell<TreeNode>>, i32)> = Vec::new();

        if let Some(actual_node) = root 
        {
            to_visit.push((actual_node, 1));
        }

        let mut max_depth: i32 = 0;

        while let Some((node, depth)) = to_visit.pop() 
        {
            max_depth = max(max_depth, depth);

            //borrow node
            let node_borrow = node.borrow();

            if let Some(ref left_child) = node_borrow.left
            {
                to_visit.push((left_child.clone(), depth + 1));
            }

            if let Some(ref right_child) = node_borrow.right
            {
                to_visit.push((right_child.clone(), depth + 1));
            }
        }
        max_depth
    }
}
