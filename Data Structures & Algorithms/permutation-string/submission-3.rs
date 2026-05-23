use std::collections::HashMap;

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        // 1. Fast return fail if s1 is longer than s2
        if s1.len() > s2.len() {
            return false;
        }

        // 2. Populate the frequency map for s1
        let mut freq: HashMap<char, i32> = HashMap::new();
        for c in s1.chars() {
            *freq.entry(c).or_insert(0) += 1;
        }

        // 3. Convert s2 to a Vec<char> for fast O(1) indexing
        let s2_chars: Vec<char> = s2.chars().collect();

        // 4. Pre-populate the differential window map with the first len(s1) characters
        let mut diff: HashMap<char, i32> = HashMap::new();
        for c in s2_chars.iter().take(s1.len()) {
            *diff.entry(*c).or_insert(0) += 1;
        }

        // 5. Initialize our sliding pointers
        let mut l: usize = 0;
        let mut r: usize = s1.len() - 1;

        // 6. Slide our window across s2
        while r < s2_chars.len() {
            // Check if the current window is an exact match
            if freq == diff {
                return true;
            }

            // Remove the character leaving on the left side
            let left_char = s2_chars[l];
            if let Some(count) = diff.get_mut(&left_char) {
                *count -= 1;
                if *count == 0 {
                    diff.remove(&left_char); // Crucial for correct map comparison
                }
            }

            // Move pointers forward together
            l += 1;
            r += 1;

            // Add the new character entering on the right side
            if r < s2_chars.len() {
                let right_char = s2_chars[r];
                *diff.entry(right_char).or_insert(0) += 1;
            }
        }

        // If we clear the loop, no permutation matches were found
        false
    }
}