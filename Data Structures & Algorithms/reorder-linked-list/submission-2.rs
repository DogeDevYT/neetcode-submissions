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
    In Rust we can't actually use fast/slow pointers like Python/C++ so we need to find the midpoint
    of the list and then split there, use reversal with helper method, and then interleave
    */
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        //count total nodes using immutable references
        let mut len = 0;
        let mut curr = head.as_ref();

        while let Some(node) = curr 
        {
            len += 1;
            curr = node.next.as_ref();
        }

        //dont need reordering for 0, 1, or 2 nodes
        if len <= 2 { return; }

        //move a mutable pointer to the end of the first half
        //for odd lengthes (5), first half has 3 nodes, for even (4), first half 
        let steps_to_mid = (len - 1) / 2;
        let mut curr_mut = head.as_mut();

        for _ in 0..steps_to_mid 
        {
            if let Some(node) = curr_mut 
            {
                curr_mut = node.next.as_mut();
            }
        }

        //sever second half from first half using .take()
        let mut list2 = None;
        if let Some(node) = curr_mut 
        {
            list2 = node.next.take();
        }

        //interleave list1 and list2 together:

        let mut list1 = head.take(); //take out head1 to work on it
        let mut list2 = Self::reverse(list2);

        //we will reconstruct final list into temporary head pointer
        let mut dummy = ListNode::new(0);
        let mut tail = &mut dummy;

        //iterate while there are still elements in both halves
        while list1.is_some() && list2.is_some() 
        {
            //take node from list 1, append to tail
            if let Some(mut l1_node) = list1 
            {
                list1 = l1_node.next.take(); //save the rest of list 1
                tail.next = Some(l1_node); //link to tail
                tail = tail.next.as_mut().unwrap(); //advance tail
            }

            //take node from list 2, append to tail
            if let Some(mut l2_node) = list2 
            {
                list2 = l2_node.next.take(); //save the rest of list 2
                tail.next = Some(l2_node); //link to tail
                tail = tail.next.as_mut().unwrap(); //advance tail
            }
        }

        //attatch any remaing nodes from list1 or list2
        if list1.is_some() 
        {
            tail.next = list1;
        } else 
        {
            tail.next = list2;
        }

        //put reordered list back in original head reference
        *head = dummy.next;
    }

    //helper method to reverse linked list in rust utilizing .take()
    fn reverse(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> 
    {
        let mut prev = None;
        let mut curr = head;

        while let Some(mut curr_node) = curr 
        {
            //take ownership of next node, leaving nothing in its place temporarily
            let nxt = curr_node.next.take();

            //point current node to previous node in the chain
            curr_node.next = prev;

            //move prev up to current node
            prev = Some(curr_node);

            //move curr to next node we saved
            curr = nxt;
        }

        //return prev
        prev
    }
}
