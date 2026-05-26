use std::collections::HashSet;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        //initialize our window HashSet so that we can add/remove elements
        let mut window: HashSet<i32> = HashSet::new();

        let mut l: usize = 0;

        for r in 0..nums.len() 
        {
            //if our window length > k, move l right to shrink
            if (r - l) as i32 > k 
            {
                window.remove(&nums[l]);
                l += 1;
            }

            //if we find number in our hashset, return true
            if window.contains(&nums[r]) 
            {
                return true;
            }

            //add our current element to hash set
            window.insert(nums[r]);
        }

        false
    }
}
