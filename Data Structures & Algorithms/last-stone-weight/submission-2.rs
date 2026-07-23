/*
Ok this should just be a basic max-heap implementation which should be pretty easy to just code up
last question was more difficult becuase we needed to initialize a whole struct
*/

use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut max_heap = BinaryHeap::new();

        //populate max heap
        for stone in stones 
        {
            max_heap.push(stone);
        }

        //run the stone smashing code
        while max_heap.len() > 1 
        {
            let y = max_heap.pop().unwrap();
            let x = max_heap.pop().unwrap();

            if y != x 
            {
                max_heap.push(y - x);
            }
        }

        if max_heap.len() > 0 
        {
            return *max_heap.peek().unwrap();
        }

        0
    }
}
