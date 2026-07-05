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
We can recursively calculate the global max by passing around an integer tracking variable
*/

impl Solution {
    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, res: &mut i32) -> i32 
    {
        match root 
        {
            None => 0,
            Some(node) => 
            {
                let node = node.borrow();
                let left_max = Self::dfs(&node.left, res).max(0);
                let right_max = Self::dfs(&node.right, res).max(0);
                *res = (*res).max(node.val + left_max + right_max);
                node.val + left_max.max(right_max)
            }
        }
    }

    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res = root.as_ref().unwrap().borrow().val;
        Self::dfs(&root, &mut res);
        res
    }
}
