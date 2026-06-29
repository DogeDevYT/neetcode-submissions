use std::collections::VecDeque;
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut sol = Vec::new();
        if root.is_none() { return sol; }

        let mut to_visit = VecDeque::new();
        to_visit.push_back(root.unwrap());

        while !to_visit.is_empty() {
            let level_len = to_visit.len();

            for i in 0..level_len {
                // Remove the node from the front of the queue
                let curr_rc = to_visit.pop_front().unwrap();
                
                // Borrow the node to access its fields
                let curr_node = curr_rc.borrow();

                // If this is the last node in the level, add to sol
                if i == level_len - 1 {
                    sol.push(curr_node.val);
                }

                // Add children to the queue
                if let Some(left) = curr_node.left.clone() {
                    to_visit.push_back(left);
                }
                if let Some(right) = curr_node.right.clone() {
                    to_visit.push_back(right);
                }
            }
        }
        sol
    }
}