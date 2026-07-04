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

/*
We can basicaly run our idea of using the preorder traversal to find root and then finding root in
inorder traversal to partition left/right subtrees. The faster way would be to do this using hashmaps
*/

use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;

impl Solution {
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        //create our hashmap
        let mut indicies: HashMap<i32, i32> = HashMap::new();

        //populate
        for (i, &val) in inorder.iter().enumerate() 
        {
            indicies.insert(val, i as i32);
        }

        //this is the index of our pre-order root
        let mut pre_idx: usize = 0;
        Self::dfs(&preorder, &indicies, &mut pre_idx, 0, inorder.len() as i32 - 1)
    }

    /*
    This is our helper method to recursively construct the left/right subtrees of our binary tree based on
    the pre order and in order structure
    */
    fn dfs (
        preorder: &[i32],
        indicies: &HashMap<i32, i32>,
        pre_idx: &mut usize,
        l: i32, 
        r: i32
    ) -> Option<Rc<RefCell<TreeNode>>> 
    {
        //if l > r, it means we've hit leaf node and we should stop
        if l > r 
        {
            return None;
        }

        let root_val = preorder[*pre_idx];
        *pre_idx += 1;
        let mid = *indicies.get(&root_val).unwrap();

        let left_val = Self::dfs(preorder, indicies, pre_idx, l, mid - 1);
        let right_val = Self::dfs(preorder, indicies, pre_idx, mid + 1, r);


        let mut root = TreeNode::new(root_val);
        root.left = left_val;
        root.right = right_val;
        Some(Rc::new(RefCell::new(root)))
    }
}
