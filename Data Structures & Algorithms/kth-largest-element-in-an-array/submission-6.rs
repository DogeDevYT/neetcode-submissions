/*
We can get this working with a min heap of size k such that we add everything at the start, adn then just remove
at the end and return top
*/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        let mut min_heap = BinaryHeap::new();

        //we need to run this like a regular min heap but then run reverse at end
        for num in nums 
        {
            min_heap.push(Reverse(num));
        }

        //now we can pop in reverse until we get min heap of size k
        while min_heap.len() > k as usize
        {
            min_heap.pop();
        }

        //idiomatic rust way of doing this ig
        if let Some(Reverse(smallest)) = min_heap.peek() 
        {
            return *smallest;
        }

        return 0
    }
}
