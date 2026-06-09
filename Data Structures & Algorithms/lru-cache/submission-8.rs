use std::collections::HashMap;

struct LRUCache {
    cap: usize,
    map: HashMap<i32, usize>,
    entries: Vec<(i32, i32)>, 
    prev: Vec<usize>,
    next: Vec<usize>,
    free_slots: Vec<usize>, // Tracks unlinked slots we can reuse
    head: usize, 
    tail: usize, 
}

impl LRUCache {
    pub fn new(capacity: i32) -> Self {
        // Index 0: Dummy Head, Index 1: Dummy Tail
        let entries = vec![(0, 0), (0, 0)];
        let prev = vec![0, 0]; // tail.prev (idx 1) is head (idx 0)
        let next = vec![1, 1]; // head.next (idx 0) is tail (idx 1)

        Self {
            cap: capacity as usize,
            map: HashMap::new(),
            entries,
            prev,
            next,
            free_slots: Vec::new(),
            head: 0,
            tail: 1,
        }
    }

    fn detatch(&mut self, idx: usize) {
        let p = self.prev[idx];
        let n = self.next[idx];
        self.next[p] = n;
        self.prev[n] = p;
    }

    fn attach_before_tail(&mut self, idx: usize) {
        let p = self.prev[self.tail];
        self.next[p] = idx;
        self.prev[idx] = p;
        self.next[idx] = self.tail;
        self.prev[self.tail] = idx;
    }

    pub fn get(&mut self, key: i32) -> i32 {
        if let Some(&idx) = self.map.get(&key) {
            self.detatch(idx);
            self.attach_before_tail(idx);
            return self.entries[idx].1;
        }
        -1
    }

    pub fn put(&mut self, key: i32, value: i32) {
        if let Some(&idx) = self.map.get(&key) {
            self.entries[idx].1 = value;
            self.detatch(idx);
            self.attach_before_tail(idx);
        } else {
            // Find or create an available index slot
            let idx = if let Some(reused_idx) = self.free_slots.pop() {
                self.entries[reused_idx] = (key, value);
                reused_idx
            } else {
                let new_idx = self.entries.len();
                self.entries.push((key, value));
                self.prev.push(0);
                self.next.push(0);
                new_idx
            };

            self.map.insert(key, idx);
            self.attach_before_tail(idx); // Fixed: Make sure to link it!

            if self.map.len() > self.cap {
                let lru = self.next[self.head];
                self.detatch(lru);
                self.map.remove(&self.entries[lru].0);
                self.free_slots.push(lru); // Fixed: Recycle the index slot
            }
        }
    }
}