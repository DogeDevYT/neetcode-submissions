impl Solution {
    /*
    Ok I think I got the "ramps" pattern for rotated arrays that are sorted for Binary Search.

    Basically we need to check if nums[left] <= nums[mid] because we're trying to find teh inflection point, in other
    words, the point where its sorted. After we find this we can make a decision to check for the 

    false start (initial condition true): check if nums[left] <= target <= nums[mid]: set right to mid - 1
    true start (initial condition true): check if nums[mid] <= target <= nums[right]: set left to mid + 1

    and if the false start/true start conditions are false, we can set l to mid + 1, r to mid - 1 respectively 
    */
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = nums.len() - 1;

        while (l <= r) 
        {
            let mid: usize = (l + r) / 2;

            //dont forget to actually check for element
            if nums[mid] == target 
            {
                return mid as i32;
            }

            if nums[l] <= nums[mid] 
            {
                if nums[l] <= target && target <= nums[mid] 
                {
                    r = mid - 1;
                } else 
                {
                    l = mid + 1;
                }
            } else 
            {
                if nums[mid] <= target && target <= nums[r] 
                {
                    l = mid + 1;
                } else 
                {
                    r = mid - 1;
                }
            }
        }
        -1
    }
}
