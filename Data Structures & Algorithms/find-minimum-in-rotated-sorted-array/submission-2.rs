use std::cmp::min;

 /*
    Ok so I think I need to reframe my thinking from finding the actual target NUMBER and rather finding the inflection
    point where the array has been shifted. What I mean is that I need to check for when the current number is greater
    than or equal to the left bound because if this is true, we're in the Ramp A basically where there are 2 ramps

    Ramp A = false start where we have rotatted n indicies forward
    Ramp B = true start where we need to find the first element here.

    we check by utilizing a preliminary check at first where we see if the left bound is less than the right bound
    (since we start at start/end of array we'll know we're in correct zone once this is true)

    and if its not then we check if current mid >= nums[left bound] and if so we need to move left bound to current
    + 1 because that means we're still on the A Ramp (since we start off at 0 and len - 1 for l and r respectively
    we know that we would be in the false start/ramp a area)

    otherwise we just need to move right bound to mid - 1 since then we know we're dead on the correct zone
    */
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut l: i32 = 0;
        let mut r: i32 = (nums.len() as i32) - 1;

        let mut lowest: i32 = nums[0];

        while l <= r 
        {
            //check if we're in the true ramp's start segment so we can just pull first element
            if nums[l as usize] < nums[r as usize] 
            {
                lowest = min(lowest, nums[l as usize]);
                break;
            }

            //time to do our ramp finding trick
            let mid: i32 = (l + r) / 2;

            //update lowest based off of mid
            lowest = min(lowest, nums[mid as usize]);

            if nums[mid as usize] >= nums[l as usize] 
            {
                l = mid + 1;
                //we're checking if middle is greater than left bound because then this would mean we're starting at
                //false start for left bound
            } else 
            {
                //now since left bound > mid we know were at true start
                //and thus can shrink right bound by half
                r = mid - 1;
            }
        }
        lowest
    }
}
