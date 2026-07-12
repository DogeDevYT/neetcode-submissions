/*
We can solve this problem by using kinda the same decision tree type backtracking as the subsets problem that 
came before it. Basically we just have to decide on 2 choices: 

1) take the number and stay on teh same index (remember to decrement target)
2) skip the number and move onto next index

and remembering to check for the followin base cases:
1) we've hit the target, append our current vector to solution and return
2) we've hit end of array, return
3) we've decremented below 0 for target sum, return
*/
impl Solution {
    pub fn combination_sum(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut curr_sum: Vec<i32> = Vec::new();
        let mut nums = nums;

        nums.sort();

        Self::backtrack(&nums, 0, &mut curr_sum, &mut res, target);

        res
    }
    
    fn backtrack(nums: &[i32], i: usize, curr_sum: &mut Vec<i32>, res: &mut Vec<Vec<i32>>, curr_target: i32) 
    {
        if curr_target == 0 
        {
            res.push(curr_sum.clone());
            return;
        }

        if i >= nums.len() || curr_target < 0 
        {
            return;
        }

        curr_sum.push(nums[i]);
        Self::backtrack(nums, i, curr_sum, res, curr_target - nums[i]);

        curr_sum.pop();
        Self::backtrack(nums, i + 1, curr_sum, res, curr_target);
    }
}
