use std::cmp::*;

impl Solution {
    /*
    I had a lot of trouble understanding how sliding window applies here

    but after a lot of prooompting I think it goes like:

    we need to find out the maximum frequency of a character such that

    (right - left + 1) - max_freq <= k

    becuase it makes no sense to remove the most frequent character and
    replace with another
    */
    pub fn character_replacement(s: String, k: i32) -> i32 {
        //create our frequency map for current window
        let mut freq: Vec<i32> = vec![0; 26];

        let mut left: i32 = 0;
        let mut max_len: i32 = 0;
        let mut max_freq: i32 = 0;

        //iterate through all ements and move right to maximum possible
        for right in 0..s.len() 
        {
            //convert to frequency index and increment
            let mut char_idx: usize = (s.as_bytes()[right] - b'A') as usize;
            freq[char_idx] += 1;

            //update max frequency
            max_freq = max(max_freq, freq[char_idx]);

            //while window is invalid, shruink it so that it fits:
            // (right - left + 1) - max_freq <= k
            while ((right as i32) - left + 1) - max_freq > k 
            {
                //slide left pointer forward here

                //remove from frequency map
                char_idx = (s.as_bytes()[left as usize] - b'A') as usize;
                freq[char_idx] -= 1;

                //slide
                left += 1;
            }
            //since we found maximum valid window, max length is
            //guranreteed to nbe valid
            max_len = max(max_len, (right as i32) - left + 1);
        }
        max_len
    }
}
