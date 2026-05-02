impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len()
        {
            return false;
        }
        //create 2 arrays of fixed length to store seen characters
        let mut seen: [i32; 26] = [0; 26];
        let mut seen2: [i32; 26] = [0; 26];

        //iterate over 1st string
        for x in s.bytes() 
        {
            //get item index by subtracting 97
            let index = (x - 97) as usize;
            seen[index] += 1;
        }

        for x in t.bytes()
        {
            let index = (x - 97) as usize;
            seen2[index] += 1;
        }

        return seen == seen2
    }
}