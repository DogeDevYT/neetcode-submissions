use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        /*
        For this solution we will first be creating a frequency table 

        and then sort
        these items into n buckets such that we have one bucket
        for each "frequency" from 1 to n.

        We can then iterate through the sorted buckets backwards for 
        the first k elements
        */

        let n = nums.len();
        let mut freq = HashMap::new();

        //populate frequency map
        for num in nums 
        {
            //instead of searching twice, once for key, and once for incrementing
            //we can just use rust's entry feature to save time/space
            *freq.entry(num).or_insert(0) += 1;
        }

        //create buckets
        //We use vec of vecs
        let mut buckets: Vec<Vec<i32>> = vec![vec![]; n+1];

        //fill buckets
        //we can consume frequency here becuase we wont use it again
        for (num, count) in freq 
        {
            buckets[count as usize].push(num);
        }

        //Collect the results
        let mut solution = Vec::new();

        //iterate backwards with .rev()
        for i in (0..buckets.len()).rev() 
        {
            //now we have to borrow so we dont consume
            for &num in &buckets[i] 
            {
                solution.push(num);

                if solution.len() == k as usize 
                {
                    return solution;
                }
            }
        }

        //we'll never get here so it doesn't matter
        return solution;
    }
}
