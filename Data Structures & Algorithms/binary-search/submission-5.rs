impl Solution {
    /*
    We can repeat our same basic binary search here 

    remember to have our left and right pointers <= each other so we account for arrays with single elements
    we also need to remember that we should be calculating midpoint by doing (left + right) / 2 (cpp has integer divison)
    */
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        //accoutn fo redge case
        if nums.len() == 0 
        {
            return -1;
        }

        let mut left: i32 = 0;
        let mut right: i32 = (nums.len() - 1) as i32;

        while left <= right 
        {
            let mid: i32 = (left + right) / 2;

            let gurt: i32 = nums[mid as usize];

            if gurt < target 
            {
                left = mid + 1;
            } else if gurt > target 
            {
                right = mid - 1;
            } else 
            {
                return mid;
            }
        }
        -1
    }
}
