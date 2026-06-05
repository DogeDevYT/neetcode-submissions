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
    Ok after reading the 2 pointer solution with first and second
    it makes a lot more sense becuase then we can just keep the 
    first pointer n steps ahead of the second so we can stop when
    first == Null and remove the node at second

    In rust its a little bit differnt. We can' treally play with pointers
    but we can utilize .take() in order to use a 2 loops approach
    where we first find the steps from 1st to n
     and then 1st to end
     and then traverse 2nd to the point where we need to using
     tracked data from first
    and then take the next node and set that to our next node
    */
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        //Create dummy node to handle removing head node
        let mut dummy = Box::new(ListNode {val : 0, next: head});

        //advance pointer n steps ahead 
        //we'll use a shared reference "&" since "first" only needs to read
        let mut first = &dummy;

        for _ in 0..n 
        {
            if let Some(ref next_node) = first.next 
            {
                first = next_node;
            }
        }

        //count how many steps first can take until it hits the end
        //this tells us exactly how far second needs to advance
        //from dummy node
        let mut steps_to_move_second = 0;

        while let Some(ref next_node) = first.next 
        {
            steps_to_move_second += 1;
            first = next_node;
        }

        //move second (as a mutable reference) to the node
        //right before first
        let mut second = &mut dummy;
        for _ in 0..steps_to_move_second 
        {
            second = second.next.as_mut().unwrap();
        }

        //snip out the target node by using .take()
        //and stiching second.next to target.next
        if let Some(mut target_node) = second.next.take() 
        {
            second.next = target_node.next.take();
        }

        //return modified list, discarding dummy node 
        //wrapper utilizing memory consumption of rust
        dummy.next
    }
}
