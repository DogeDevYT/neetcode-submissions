impl Solution {
    /*
    We can easily transform this problem to an instance of 2 sum where we use our current number

    we iterate through every number, assume index i:

    we need to find 2 indicies with numbers: j, k such that
    -nums[i] = nums[j] + nums[k]

    or in other words, -nums[i] is target and we have to run a 2 sum with left/right pointers
    */
    //add mut so we can sort in-place
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        //sort the numbers
        nums.sort();

        //store length
        let n: usize = nums.len();

        //create our solution vector
        let mut solution: Vec<Vec<i32>> = Vec::new();

        //iterate through all numbers
        for i in 0..n 
        {
            //skip duplicate values of i
            if i > 0 && nums[i] == nums[i-1] 
            {
                continue;
            }

            //get target
            let target: i32 = -nums[i];

            //2 pointer approach start
            let mut l: usize = i + 1;
            let mut r: usize = n - 1;

            //iterate while left pointer < right pointer
            while l < r 
            {
                //store sum
                let sum: i32 = nums[l] + nums[r];

                if sum < target 
                {
                    l += 1;
                } else if sum > target 
                {
                    r -= 1;
                } else 
                {
                    //target found

                    solution.push(vec![nums[i], nums[l], nums[r]]);

                    //dont forget to search for non duplicates
                    while l < r && nums[l] == nums[l + 1] 
                    {
                        l += 1;
                    }

                    while l < r && nums[r] == nums[r-1] 
                    {
                        r -= 1;
                    }

                    //iterate one more time
                    l += 1;
                    r -= 1;
                }
            }
        }

        solution
    }
}
