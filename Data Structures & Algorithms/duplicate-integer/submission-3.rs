use std::collections::HashMap;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        //initialize hashmap for seen elements
        let mut seen = HashMap::new();

        for num in nums.iter() 
        {
            if seen.contains_key(num) 
            {
                return true;
            }
            else 
            {
                seen.insert(num, 1);
            }
        }

        //if we get here that means we didn't find anything
        return false;
    }
}
