impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut count = [0i32; 26];
        for &task in &tasks {
            count[(task as u8 - b'A') as usize] += 1;
        }

        let mut max_heap = BinaryHeap::new();
        for &cnt in &count {
            if cnt > 0 {
                max_heap.push(cnt);
            }
        }

        let mut time = 0;
        let mut q: VecDeque<(i32, i32)> = VecDeque::new();
        while !max_heap.is_empty() || !q.is_empty() {
            time += 1;

            if max_heap.is_empty() {
                time = q.front().unwrap().1;
            } else {
                let cnt = max_heap.pop().unwrap() - 1;
                if cnt > 0 {
                    q.push_back((cnt, time + n));
                }
            }

            if let Some(&(c, t)) = q.front() {
                if t == time {
                    q.pop_front();
                    max_heap.push(c);
                }
            }
        }

        time
    }
}