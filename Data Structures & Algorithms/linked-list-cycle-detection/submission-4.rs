// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: *mut ListNode,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: std::ptr::null_mut(), val }
//     }
// }

impl Solution {
    /*
    yeah so for this one I was thinking we have 2 pointers: fast and slow.

    Basically we're guarenteed that if our slow pointer moves one step at a time
    and our fast pointer moves 2 steps at a time, the fast one will have to be intersecting the slow
    one at one stop, given that there is a cycle, otherwise the fast one will get to the end and the loop 
    will finish early
    */
    pub fn has_cycle(head: *mut ListNode) -> bool {
        // 1. Make the pointers mutable so they can be reassigned
        let mut fast: *mut ListNode = head;
        let mut slow: *mut ListNode = head;

        // 2. Use .is_null() instead of .is_some() for raw pointers.
        // 3. Wrap the dereferencing of raw pointers in unsafe blocks.
        while !fast.is_null() && unsafe { !(*fast).next.is_null() } 
        {
            unsafe {
                // Dereference raw pointers to access their fields
                fast = (*(*fast).next).next;
                slow = (*slow).next;
            }

            if fast == slow 
            {
                return true;
            }
        }
        
        // In Rust, you can just omit the "return" and the semicolon for the final expression
        false
    }
}
