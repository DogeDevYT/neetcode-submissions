use std::collections::HashMap;
use std::cmp::max;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let char_map: &mut HashMap<char, usize> = &mut HashMap::new();
        // Convert to Vec for fast O(1) indexing
        let chars: Vec<char> = s.chars().collect();
        let n: usize = chars.len();

        let mut l: usize = 0;
        let mut dist: i32 = 0;

        for r in 0..n {
            let curr: char = chars[r];

            // Update left pointer if duplicate is inside current window
            if let Some(&prev_idx) = char_map.get(&curr) {
                if prev_idx >= l {
                    l = prev_idx + 1;
                }
            }

            // Store or update the character's last seen position
            char_map.insert(curr, r);

            // Calculate max distance
            dist = max(dist, (r - l + 1) as i32);
        }

        dist
    }
}
