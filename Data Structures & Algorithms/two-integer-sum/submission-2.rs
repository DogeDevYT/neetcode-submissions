use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new(); //initialize new HashMap

        //iterate over all elements in nums
        //dereference n ahead of time
        for (i,&n) in nums.iter().enumerate() 
        {
            //store complement (target sum - current number)
            let complement = target - n;

            //check if complement exists and return
            if let Some(&index) = seen.get(&complement) 
            {
                return vec![index as i32, i as i32];
            }

            //if it doesn't exist, add it to hashmap
            seen.insert(n, i);
        }

        //fallback return
        return vec![];
    }
}
