impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        // Use an empty String instead of Vec<String> for the tracking state
        let mut curr_combo = String::new();
        let mut res: Vec<String> = Vec::new();

        Self::backtrack(n, 0, 0, &mut curr_combo, &mut res);

        res
    }

    fn backtrack(n: i32, curr_open: i32, curr_closed: i32, curr_combo: &mut String, res: &mut Vec<String>) {
        // Base case
        if curr_open == curr_closed && curr_open == n {
            // .clone() copies the current string state so we can save it into res
            res.push(curr_combo.clone());
            return;
        }

        // Decision to add an opening parenthesis
        if curr_open < n {
            curr_combo.push('('); // Use single quotes for a char
            Self::backtrack(n, curr_open + 1, curr_closed, curr_combo, res);
            curr_combo.pop();     // Cleans up the last char
        }

        // Decision to add a closing parenthesis
        if curr_closed < curr_open {
            curr_combo.push(')');
            Self::backtrack(n, curr_open, curr_closed + 1, curr_combo, res);
            curr_combo.pop();     // Cleans up the last char
        }
    }
}