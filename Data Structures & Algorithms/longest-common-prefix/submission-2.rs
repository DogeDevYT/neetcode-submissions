impl Solution {
    /*
    ok this one shouldn't be too hard. all we need to do is vertically
    iterate over the columns in a string and return the first string
    at its length OR one where the current character doesn't match
    the current character of hte first string
    */
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        //cover the edge case where input string is empty
        if strs.is_empty() 
        {
            return String::new();
        }

        let first_str = &strs[0];

        for i in 0..first_str.len() 
        {   
            let current_byte = first_str.as_bytes()[i];

            //use &strs so we borrow vector instead of consuming
            for s in &strs 
            {
                //check if we've reached end of current string or if
                //characters dont match
                if i == s.len() || s.as_bytes()[i] != current_byte 
                {
                    return first_str[0..i].to_string();
                }
            }
        }
        //return first string
        strs[0].clone()
    }
}
