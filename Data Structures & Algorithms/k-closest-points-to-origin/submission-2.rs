use std::collections::BinaryHeap;

/*
I think the optimal way to do this is to create a max heap and then keep popping off that until we get
k elements remaining O(nlogn) time complexity though
*/

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut max_heap: BinaryHeap<(i32, Vec<i32>)> = BinaryHeap::new();

        for point in points 
        {
            let dist: i32 = point[0] * point[0] + point[1] * point[1];
            max_heap.push((dist, point));

            if max_heap.len() > k as usize
            {
                max_heap.pop();
            }
        }

        let mut ret: Vec<Vec<i32>> = Vec::new();

        // Idiomatic Rust: while let cleanly pops and unpacks until empty
        while let Some((_, point)) = max_heap.pop() {
            ret.push(point); // No clone needed! We own 'point' now.
        }

        ret
    }
}
