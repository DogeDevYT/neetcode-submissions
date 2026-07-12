/*
We can get around this backtracking solution by basically visualizing it as a type of dfs
where each branch is a decision of weather or not to include an element
*/
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut subset: Vec<i32> = Vec::new();
        Self::dfs(&nums, 0, &mut subset, &mut res);
        res
    }

    // our acutal dfs
    fn dfs(nums: &[i32], i: usize, subset: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) 
    {
        if i >= nums.len() 
        {
            res.push(subset.clone());
            return;
        }

        //this is the option where we include da element
        subset.push(nums[i]);
        Self::dfs(nums, i+1, subset, res);

        //option where we DONT include the elemtn
        subset.pop();
        Self::dfs(nums, i + 1, subset, res);
    }
}
