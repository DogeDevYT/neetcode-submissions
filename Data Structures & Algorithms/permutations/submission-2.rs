/*
I think the idea here is to just iterate over all numbers at every chance because we're building permutations with
unique elements. I can get away with using a set to denote already used elements for that aforementioned reason.
Backtracking structure is a little different but since we have to create all possible elements im not sure how I would
speed this up any.
*/

use std::collections::HashSet;

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut curr_path: Vec<i32> = Vec::new();
        let mut used: HashSet<i32> = HashSet::new();

        Self::backtrack(&nums, &mut used, &mut curr_path, &mut result);

        result
    }

    fn backtrack(nums: &[i32], used: &mut HashSet<i32>, curr_path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) 
    {
        //exit if we have enough elements to form a permutation - base case
        if curr_path.len() == nums.len() 
        {
            res.push(curr_path.clone());
            return;
        }

        //need to iterate over every number in order to build a permutation
        //using .iter() to borrow and not consume
        for num in nums.iter() 
        {
            if used.contains(num) 
            {
                continue; //skip elements we already used
            }

            //decision to include current number
            //pass a value instead of reference
            used.insert(*num);
            curr_path.push(*num);

            //backtrack
            Self::backtrack(nums, used, curr_path, res);

            //decision to not include current number RIGHT NOW
            used.remove(num);
            curr_path.pop();
        }
    }
}
