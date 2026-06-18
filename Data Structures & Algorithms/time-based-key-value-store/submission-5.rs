use std::collections::HashMap;

/*
Ok for this problem I think we can solve this quite simply with a string that references a 
tuple (since we're using Rust)

and we can store the hashmap as <key, tuple (value, timestamp)> and just run binary search
with the actual timestamp
*/

struct TimeMap {
    // key maps to a vector of tuples: (value, timestamp)
    hashmap: HashMap<String, Vec<(String, i32)>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            hashmap: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        //use entry api to make this a one liner
        self.hashmap.entry(key).or_insert(Vec::new()).push((value, timestamp));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(arr) = self.hashmap.get(&key) 
        {
            //return empty array if required
            if arr.is_empty() 
            {
                return String::new();
            }

            // 2. Use signed integers for the bounds
            let mut l: isize = 0;
            let mut r: isize = (arr.len() as isize) - 1;
            let mut res: String = String::new();

            while l <= r {
                let mid = l + (r - l) / 2;
                let mid_idx = mid as usize; // Cast to usize only for the array indexing

                if arr[mid_idx].1 <= timestamp {
                    res = arr[mid_idx].0.clone();
                    l = mid + 1;
                } else {
                    r = mid - 1; // Safely becomes -1 if mid is 0!
                }
            }
            return res;
        }
        String::new() //return empty string
    }
}
