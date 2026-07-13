/*
blah blah blah same general idea as combo sum I except we always increment index now and we sort candidates at start
and skip duplicate  values with while loop
*/

impl Solution {
    fn backtrack(candidates: &[i32], mut i: usize, curr_combo: &mut Vec<i32>, res: &mut Vec<Vec<i32>>, curr_target: i32) 
    {
        if curr_target == 0 
        {
            res.push(curr_combo.clone());
            return;
        }

        if curr_target < 0 || i >= candidates.len() 
        {
            return;
        }

        //choose to include
        curr_combo.push(candidates[i]);
        Self::backtrack(candidates, i + 1, curr_combo, res, curr_target - candidates[i]);

        //choose to skip
        curr_combo.pop();

        //skip over duplicate elemetns
        while i + 1 < candidates.len() && candidates[i] == candidates[i + 1] 
        { 
            i += 1; 
        }

        Self::backtrack(candidates, i + 1, curr_combo, res, curr_target);
    }
    pub fn combination_sum2(mut candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        candidates.sort();

        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut combo: Vec<i32> = Vec::new();

        Self::backtrack(&candidates, 0, &mut combo, &mut res, target);

        res
    }
}
