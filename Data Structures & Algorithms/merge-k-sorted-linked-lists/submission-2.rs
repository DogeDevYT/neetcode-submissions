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

/*
Basically we need to leverage the merge capabilitiers of merge sort by repeatedly sorting togther 2 LLs
and using a helper function to merge the 2 lists together for us
*/
impl Solution {
    //helper function chud
    fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> 
    {
        //create our dummy node that we can reference at the end to return the pointer to our new merged LL
        let mut dummy: Box<ListNode> = Box::new(ListNode::new(0));

        //reference our tail pointer to be dummy so that we can perform operations
        let mut tail = &mut dummy.next;

        //iterate over both while they're still having elements
        while list1.is_some() && list2.is_some()
        {
            if list1.as_ref().unwrap().val < list2.as_ref().unwrap().val 
            {
                //take ownership of list1, attatch it to tail
                *tail = list1;
                //advance list1 to the next Node in teh LL
                list1 = tail.as_mut().unwrap().next.take();
            } else 
            {
                //do the same with list 2 in this case
                *tail = list2;
                list2 = tail.as_mut().unwrap().next.take();
            }

            //advance tail regardless
            tail = &mut tail.as_mut().unwrap().next;
        }

        //add our remainder back to our combined dummy LL
        // Attach the remaining non-empty list
        *tail = if list1.is_some() { list1 } else { list2 };

        //return our next pointer to our dummy node which is the real start of the LL
        dummy.next
    }
    pub fn merge_k_lists(mut lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        //acount for edge case where we have no lists
        if lists.is_empty() 
        {
            return None;
        }

        //iterate over merging the lists until the length is <2
        while lists.len() > 1 
        {
            //create a temp array to store this iteration of hte merged lists
            let mut merged_lists: Vec<Option<Box<ListNode>>> = Vec::new();

            //iterate in 2s to merge and stuff
            for i in (0..lists.len()).step_by(2) 
            {
                //remember to use .take() to move ownership from lists to the vectors we're combining
                let mut curr: Option<Box<ListNode>> = lists[i].take();

                let mut nxt: Option<Box<ListNode>> = None;

                //if we have a list node, add it to the computation, otherwise just use a nullptr
                if (i+1) < lists.len() 
                {
                    nxt = lists[i + 1].take();
                }

                //append combined lists to merged lists
                merged_lists.push(Self::merge_two_lists(curr, nxt));
            }

            lists = merged_lists; //reset pointer to new merged lists
        }

        lists[0].take() //return first element in array by pulling out first list from vector
    }
}
