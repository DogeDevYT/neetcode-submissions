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
lets get this dfs binary search with node working in the big rust now too
*/

impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let pVal = p.unwrap().borrow().val;
        let qVal = q.unwrap().borrow().val;

        let mut curr = root;

        //now we start out chud iteration
        while let Some(node) = curr 
        {
            let val = node.borrow().val;

            let goLeft: bool = val > pVal && val > qVal;
            let goRight: bool = val < pVal && val < qVal;

            if goLeft 
            {
                curr = node.borrow().left.clone();
            } else if goRight 
            {
                curr = node.borrow().right.clone();
            } else 
            {
                return Some(node);
            }
        }

        None //default value type
    }
}
