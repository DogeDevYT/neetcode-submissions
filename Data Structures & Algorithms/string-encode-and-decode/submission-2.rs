impl Solution {
    /*
    For this solution, we will use a delimiter approach such that we store the length of the encoded string
    and the delimiter "#" in this case, to then encode with length of string and then delimiter itself
    and then the actual string repeated for every string in the array

    so it would look like 

    cat, hat, rat

    3#cat3#hat3#rat
    */

    pub fn encode(strs: Vec<String>) -> String {
        let mut solution = String::new();

        for word in strs 
        {
            // format! turns the length and delimiter into a string automatically
            solution.push_str(&format!("{}#", word.len()));
            solution.push_str(&word);
        }

        //no semicolon means return
        solution
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut decoded = Vec::new();
        let mut i = 0;

        //use s.len() to know when to stop
        while i < s.len() 
        {
            //find the index of the next "#" from teh index of the string
            // use .find() on a string slice
            let j = s[i..].find("#").unwrap() + i; 

            //extract the length digits and parse as usize
            let length: usize = s[i..j].parse().unwrap();

            //move i to start of string 
            i = j + 1;

            //extract word using slice
            let word = s[i..i + length].to_string();
            decoded.push(word);

            //move i to start of length prefix
            i += length;
        }
        decoded
    }
}
