impl Solution {
    /*
    Just use 2 pointers for increment/decrement
    */

    pub fn is_palindrome(s: String) -> bool {
        //initalize left/right pointers
        let mut l: usize = 0;
        let mut r: usize = s.len() - 1;

        //iterate while left and right pointers haven't cross each other
        while l <= r 
        {
            let left = s.chars().nth(l).unwrap();
            let right = s.chars().nth(r).unwrap();

            if l < r 
            {
                if !left.is_alphanumeric()
                {
                    l += 1;
                } else if !right.is_alphanumeric() 
                {
                    r -= 1;
                } else if !left.eq_ignore_ascii_case(&right) 
                {
                    return false;
                } else 
                {
                    //characters match
                    r -= 1;
                    l += 1;
                }
            } else 
            {
                //since we have same character, they're guarenteed to be equal
                break;
            }
        }
        //guarenteed tobe true now
        true
    }
}
