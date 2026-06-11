impl Solution {
    pub fn reverse_k_group(mut head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode::new(0));
        let mut tail = &mut dummy;
        
        while head.is_some() {
            // 1. Try to extract k nodes from the head of the list
            let mut group_head = None;
            let mut group_tail = &mut group_head;
            let mut count = 0;
            
            while count < k && head.is_some() {
                // Take ownership of the current head node
                let mut next_node = head.take();
                // Advance the original head pointer to the next element
                head = next_node.as_mut().unwrap().next.take();
                
                // Append this node to our temporary k-group list
                *group_tail = next_node;
                group_tail = &mut group_tail.as_mut().unwrap().next;
                count += 1;
            }
            
            // 2. Decide whether to reverse or leave as-is
            if count == k {
                // We successfully gathered k nodes. Reverse them!
                let reversed_group = Self::reverse_list(group_head);
                
                // Attach the reversed group to our main dummy tail
                tail.next = reversed_group;
                
                // Advance the main tail pointer to the end of this new group
                while tail.next.is_some() {
                    tail = tail.next.as_mut().unwrap();
                }
            } else {
                // Less than k nodes left! Attach them exactly as they were
                tail.next = group_head;
                break;
            }
        }
        
        dummy.next
    }
    
    // Standard iterative list reversal helper
    fn reverse_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        while let Some(mut node) = head {
            head = node.next.take(); // Disconnect next
            node.next = prev;        // Reverse link
            prev = Some(node);       // Move prev forward
        }
        prev
    }
}