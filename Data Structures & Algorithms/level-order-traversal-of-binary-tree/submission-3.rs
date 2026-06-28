use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut sol = Vec::new();
        let mut to_visit = VecDeque::new();

        if let Some(node) = root {
            to_visit.push_back(node);
        }

        while !to_visit.is_empty() {
            let mut curr_level = Vec::new();
            let level_len = to_visit.len();

            for _ in 0..level_len {
                // Pop the Rc pointer from the front
                if let Some(rc_node) = to_visit.pop_front() {
                    // Use a block to ensure the borrow is dropped immediately after use
                    {
                        let node = rc_node.borrow();
                        curr_level.push(node.val);
                        
                        // Push children to the back of the queue as new Rc clones
                        if let Some(left) = &node.left {
                            to_visit.push_back(Rc::clone(left));
                        }
                        if let Some(right) = &node.right {
                            to_visit.push_back(Rc::clone(right));
                        }
                    }
                }
            }
            sol.push(curr_level);
        }
        sol
    }
}