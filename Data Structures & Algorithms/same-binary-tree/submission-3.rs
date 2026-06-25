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

impl Solution {
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut stack = vec![(p, q)];

        while let Some((n1, n2)) = stack.pop() 
        {
            match (n1, n2) 
            {
                (None, None) => continue,
                (Some(a), Some(b)) => 
                {
                    let a = a.borrow();
                    let b = b.borrow();

                    if a.val != b.val 
                    {
                        return false;
                    }

                    stack.push((a.right.clone(), b.right.clone()));
                    stack.push((a.left.clone(), b.left.clone()));
                }
                _ => return false, //add a catch all default case for rust to return false for (!p and q) and (p and !q)
            }
        }

        true
    }
}
