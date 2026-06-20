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
Recursive DFS solution: In any other language this would be light work,
no reaction. But Rust is a little different with its memory safety so I had
to lookup solution
*/
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        //make a reference to root as node
        if let Some(node) = root.as_ref() 
        {
            //we need to borrow this node so we can perform operations
            let mut node_ref = node.borrow_mut();
            //get refernce to left and right nodes to swap around poiunters
            let left = node_ref.left.take();
            let right = node_ref.right.take();
            //we do things a little differently around here ahhhh
            //millenial burger resturaunt ahh lanaguge
            node_ref.left = right;
            node_ref.right = left;

            //recursively call inversion on children
            Self::invert_tree(node_ref.left.clone());
            Self::invert_tree(node_ref.right.clone());
        }
        root
    }
}
