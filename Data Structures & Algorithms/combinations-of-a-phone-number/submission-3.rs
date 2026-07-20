/*
Should be a simple solution to just have a hashmap to store letter combinations and all we need to do is iterate
through this while backtracking
*/

use std::collections::HashMap;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return vec![];
        }

        let phone_map: HashMap<char, &str> = HashMap::from([
            ('2', "abc"),
            ('3', "def"),
            ('4', "ghi"),
            ('5', "jkl"),
            ('6', "mno"),
            ('7', "pqrs"),
            ('8', "tuv"),
            ('9', "wxyz"),
        ]);

        let mut res = Vec::new();
        let mut curr = String::new();

        Self::backtrack(&digits, 0, &mut res, &mut curr, &phone_map);

        res
    }

    fn backtrack(
        digits: &str,
        i: usize,
        res: &mut Vec<String>,
        curr: &mut String,
        phone_map: &HashMap<char, &str>,
    ) {
        if i == digits.len() {
            res.push(curr.clone());
            return;
        }

        let ch = digits.as_bytes()[i] as char;

        if let Some(&letters) = phone_map.get(&ch) {
            for option in letters.chars() {
                curr.push(option);
                Self::backtrack(digits, i + 1, res, curr, phone_map);
                curr.pop();
            }
        }
    }
}