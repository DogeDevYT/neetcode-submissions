// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev: Option<Box<ListNode>> = None;
        let mut curr = head;

        // while let safely unpacks the Option until it hits None
        while let Some(mut node) = curr {
            // .take() leaves a None in node.next and extracts the actual Box<ListNode>
            let nxt = node.next.take(); 
            
            // Point the current node backward to our previous chain
            node.next = prev;
            
            // Move prev forward by wrapping our current node back into a Some
            prev = Some(node);
            
            // Move curr forward to the next node we bookmarked
            curr = nxt;
        }

        prev
    }
}
