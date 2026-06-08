impl Solution {
    /*
    Honestly this problem just sucks all around theres no way I would
    be able to get this on an actual interview even with getting the hint
    to treat each node in teh array like a  linked list value

    that last part about using a second slow pointer to isolate the 
    entrance of the cycle, and thus finding our return value
    */
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        let mut slow: usize = 0;
        let mut fast: usize = 0;

        loop 
        {
            slow = nums[slow] as usize;
            fast = nums[nums[fast] as usize] as usize;

            if nums[slow] == nums[fast] { break; }
        }

        //now isolate entrance
        let mut slow2: usize = 0;

        loop 
        {
            slow2 = nums[slow2] as usize;
            slow = nums[slow] as usize;

            if slow == slow2 
            {
                return slow as i32;
            }
        }
    }
}
