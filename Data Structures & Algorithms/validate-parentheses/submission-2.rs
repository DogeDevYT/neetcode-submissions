use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        //Rust doesn't have a standalone "stack" library instead it builds on top of Vec
        let mut stack = Vec::new();

        //same slop, just store closing combinations from open
        let closeToOpen = HashMap::from([
            ('}', '{'),
            (']', '['),
            (')', '(')
        ]);

        //iterate through charaters
        for c in s.chars() 
        {
            /*
            rust is a little strange in that each stack.pop() returns an Option<char>

            which could mean either a Some(char) or None type, so we have to account fo rhtis
            */

            //closing bracket
            if let Some(&opening_bracket) = closeToOpen.get(&c) 
            {
                if stack.pop() != Some(opening_bracket) 
                {
                    return false;
                }
            } else 
            {
                //opening bracket
                stack.push(c);
            }
        }

        stack.is_empty()
    }
}
