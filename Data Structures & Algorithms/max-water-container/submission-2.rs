use std::cmp; // for cmp::min and cmp::max

impl Solution {
    /*
    yeah I just pattern matched 2 poniter to this specfically:

    - move the smaller of the 2 heights towards center, or both if they're teh same height
    - do this until left pointer crosses right pointer
    - go over entire heights array
    - while doing this make sure to take max area
    */
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = heights.len() - 1;

        let mut max_area: i32 = 0;

        while l < r 
        {
            let width: i32 = (r as i32) - (l as i32);

            let height: i32 = cmp::min(heights[l], heights[r]);

            max_area = cmp::max(max_area, width*height);

            if heights[l] < heights[r] 
            {
                l += 1;
            } else if heights[r] < heights[l] 
            {
                r -= 1;
            } else 
            {
                l += 1;
                r -= 1;
            }
        }

        max_area
    }
}
