impl Solution {
    pub fn four_sum(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        //sort numbers
        nums.sort();

        //store length
        let n: usize = nums.len();

        //intialize solution array
        let mut sol: Vec<Vec<i32>> = Vec::new();

        for i in 0..n 
        {
            //skip duplicate values at index i
            if i > 0 && nums[i] == nums[i-1] 
            {
                continue;
            }

            //iterate through j nested
            for j in (i+1)..n 
            {
                //skip duplicate values at index of j
                if j > i + 1 && nums[j] == nums[j-1] 
                {
                    continue;
                }

                //intialize left/right pointers
                let mut l: usize = j + 1;
                let mut r: usize = nums.len() - 1;

                while l < r 
                {
                    let curr: i64 = (nums[l] as i64 + nums[r] as i64 + nums[i] as i64 + nums[j] as i64) as i64;

                    //edit pointers accordingly
                    if curr < target as i64
                    {
                        l += 1;
                    } else if curr > target as i64 
                    {
                        r -= 1;
                    } else 
                    {
                        let gurt: Vec<i32> = vec![nums[i], nums[j], nums[l], nums[r]];
                        sol.push(gurt);

                        //in case we get same element over and over again
                        while l < r && nums[l] == nums[l + 1] 
                        {
                            l += 1;
                        }

                        while l < r && nums[r] == nums[r-1] 
                        {
                            r -= 1;
                        }

                        //increment pointers one more time to normalize
                        l += 1;
                        r -= 1;
                    }
                }
            }
        }
        sol
    }
}
