use std::cmp;

impl Solution {
    /*
    Basically we can use 2 pointer instead of prefix/postfix sums outright in a way that 2 pointer
    finds the "bottlenecks" of lesser height that we were trying to do with prefix/postfix sums

    move left/right pointers inwards while left < right
    */
    pub fn trap(height: Vec<i32>) -> i32 {
        let n: usize = height.len();

        let mut l: usize = 0;
        let mut r: usize = n - 1;

        //store maximum for left/right so we can use this for our 
        //calculation of trapping rainwater
        let mut left_max: i32 = 0;
        let mut right_max: i32 = 0;

        //store for for calculating water
        let mut total_water: i32 = 0;

        //start using 2 pointer loop to fast calculate
        while l < r 
        {
            //store left/right maxes accordingly
            left_max = cmp::max(left_max, height[l]);
            right_max = cmp::max(right_max, height[r]);

            //check if "bottleneck" is left or right side specifically
            if height[l] < height[r]
            {
                //left side is bottlneeck
                total_water += left_max - height[l];
                l += 1;
            } else 
            {
                //right side is bottlneeck
                total_water += right_max - height[r];
                r -= 1;
            }
        }

        total_water
    }
}
