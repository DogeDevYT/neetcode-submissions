use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        //create a hash set (rusts implementation of set)
        let numsSet: HashSet<i32> = nums.into_iter().collect();

        //create max depth variable
        let mut maxDepth: i32 = 0;

        //iteate over all the numbers in our set
        //make sure to iterate over &numsSet to make sure we dont destroy
        for num in &numsSet 
        {   
            //make a copy of our num so we dont' destroy it on accident
            let mut numCopy: i32 = *num;
            //we want to run our iteration loop on increments so we can prune a lot of cases
            if !numsSet.contains(&(numCopy - 1)) 
            {
                //current depth to compare later
                let mut currDepth: i32 = 1; 

                //rust doesn't have pre-increment or post increment so we have to do thi the normla way
                while numsSet.contains(&(numCopy + 1)) 
                {
                    currDepth += 1;
                    numCopy += 1;
                }

                //set maxDepth to the max of maxDeptha nd currDepth
                maxDepth = std::cmp::max(maxDepth, currDepth);
            }
        }
        //return maxDepth using just rust inference
        maxDepth
    }
}
