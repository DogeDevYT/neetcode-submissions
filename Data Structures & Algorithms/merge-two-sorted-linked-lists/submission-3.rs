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
    /*
    Ok after reading up the solution algorithm I get what we need to do now:

    - We maintain a dummy node to serve as the start of our list while we repeatedly iterate over
    over linked lists
    - We maintain the pointers such that when we add a new list to our dummy node origin: we iterate
    the pointer that we added to the next node
    - When one of the lists is empty, add the remaining one as the next element
    */
    pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut dummy: Box<ListNode> = Box::new(ListNode::new(0));
        let mut tail = &mut dummy;

        while let (Some(l1), Some(l2)) = (list1.as_ref(), list2.as_ref()) 
        {
            if l1.val < l2.val 
            {
                tail.next = list1;
                tail = tail.next.as_mut().unwrap();
                list1 = tail.next.take();
            } else 
            {
                tail.next = list2;
                tail = tail.next.as_mut().unwrap();
                list2 = tail.next.take();
            }
        }

        tail.next = if list1.is_some() {list1} else {list2};
        dummy.next
    }
}
