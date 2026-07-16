/*
Basically this whole problem revolves around sorting the list to begin with
and then basically run our naive backtracking approach while checking 
with a while loop for duplicate elements
*/
impl Solution {

    pub fn subsets_with_dup(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        //sort
        nums.sort();

        let mut curr_combo: Vec<i32> = Vec::new();
        let mut res: Vec<Vec<i32>> = Vec::new();

        Self::backtrack(&nums, 0, &mut curr_combo, &mut res);

        res
    }

    fn backtrack(
        nums: &[i32], 
        mut index: usize, 
        curr_combo: &mut Vec<i32>, 
        res: &mut Vec<Vec<i32>>
    ) 
    {
        if index == nums.len() 
        {
            res.push(curr_combo.clone());
            return;
        }

        //decision to take
        curr_combo.push(nums[index]);
        Self::backtrack(nums, index + 1, curr_combo, res);

        //decision to skip
        curr_combo.pop();

        //skip duplicate elements
        while index + 1 < nums.len() && nums[index] == nums[index + 1] 
        {
            index += 1;
        }

        Self::backtrack(nums, index + 1, curr_combo, res);
    }
}
