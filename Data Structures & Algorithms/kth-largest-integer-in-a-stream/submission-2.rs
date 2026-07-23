/*
Ok so the idea is we have a min-heap of size k because then we could just return the top, which is an O(1) 
operation. However adding m elmeents with O(logn) time complexity each would result in O(mlogn) time complexity
*/
use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct KthLargest {
    min_heap: BinaryHeap<Reverse<i32>>,
    k: usize,
}

impl KthLargest {
    pub fn new(k: i32, nums: Vec<i32>) -> Self {
        //populate our struct type
        let k = k as usize;
        let mut min_heap = BinaryHeap::new();

        //populate using data structure
        for num in nums 
        {
            min_heap.push(Reverse(num));
            if min_heap.len() > k 
            {
                min_heap.pop();
            }
        }
        KthLargest { min_heap, k }
    }

    pub fn add(&mut self, val: i32) -> i32 {
        self.min_heap.push(Reverse(val));

        //push when we have too many values
        if self.min_heap.len() > self.k 
        {
            self.min_heap.pop();
        }
        self.min_heap.peek().unwrap().0
    }
}
