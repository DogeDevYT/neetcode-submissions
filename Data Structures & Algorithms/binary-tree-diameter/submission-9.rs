use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;
use std::cmp::max;

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_diameter = 0;
        
        // 1. Key by the RefCell pointer type directly
        let mut heights: HashMap<*const RefCell<TreeNode>, i32> = HashMap::new();
        let mut visited: Vec<(Rc<RefCell<TreeNode>>, bool)> = Vec::new();

        if let Some(r) = root {
            visited.push((r.clone(), false));
        }

        while let Some((node_rc, is_visited)) = visited.pop() {
            // Get the raw pointer to the RefCell container
            let node_ptr = Rc::as_ptr(&node_rc);

            if is_visited {
                let borrowed_node = node_rc.borrow();
                
                // 2. Just pass the child Rc references straight to Rc::as_ptr!
                let left_h = borrowed_node.left.as_ref()
                    .map(|l| *heights.get(&Rc::as_ptr(l)).unwrap_or(&0))
                    .unwrap_or(0);
                    
                let right_h = borrowed_node.right.as_ref()
                    .map(|r| *heights.get(&Rc::as_ptr(r)).unwrap_or(&0))
                    .unwrap_or(0);
                
                max_diameter = max(max_diameter, left_h + right_h);
                heights.insert(node_ptr, 1 + max(left_h, right_h));
            } else {
                // Safely scope out the clones to drop the runtime borrow before mutating the stack
                let (left_child, right_child) = {
                    let borrowed = node_rc.borrow();
                    (borrowed.left.clone(), borrowed.right.clone())
                };

                visited.push((node_rc.clone(), true));

                if let Some(r) = right_child {
                    visited.push((r, false));
                }
                if let Some(l) = left_child {
                    visited.push((l, false));
                }
            }
        }
        max_diameter
    }
}