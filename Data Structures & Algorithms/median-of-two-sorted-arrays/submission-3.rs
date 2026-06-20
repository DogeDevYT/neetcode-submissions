use std::cmp::{min, max};

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // 1. Ensure `a` is the smaller array to avoid `j` underflowing
        let (a, b) = if nums1.len() <= nums2.len() {
            (&nums1, &nums2)
        } else {
            (&nums2, &nums1)
        };

        let total: usize = a.len() + b.len();
        let half: usize = total / 2;

        let mut l: usize = 0;
        let mut r: usize = a.len();

        while l <= r {
            let i: usize = l + (r - l) / 2;
            let j: usize = half - i;

            // 2. Use i32::MIN / MAX instead of f64 infinities to match array types
            let a_left = if i > 0 { a[i - 1] } else { i32::MIN };
            let a_right = if i < a.len() { a[i] } else { i32::MAX };
            
            let b_left = if j > 0 { b[j - 1] } else { i32::MIN };
            let b_right = if j < b.len() { b[j] } else { i32::MAX };

            // Check if partition is correct
            if a_left <= b_right && b_left <= a_right {
                // Odd total elements: the median is the smallest element on the right side
                if total % 2 == 1 {
                    return min(a_right, b_right) as f64;
                }
                // Even total elements
                return (max(a_left, b_left) as f64 + min(a_right, b_right) as f64) / 2.0;
            } else if a_left > b_right {
                // Prevent usize underflow: if i is 0, we can't move left anyway
                if i == 0 { break; }
                r = i - 1; 
            } else {
                l = i + 1; 
            }
        }
        
        0.0
    }
}