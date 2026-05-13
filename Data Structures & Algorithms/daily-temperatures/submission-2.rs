impl Solution {
    /*
    For this problem, we need to use a monotonically increasing stack. This one was super hard to wrap
    my head around first but then I realized I could run a while loop using our stack and having the top
    element be less than current temperature to repeatedly assign a decrementing value.
    */
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let n = temperatures.len(); //store size of vec for readability

        //create answer vector to return
        let mut answer = vec![0; n];

        //create our stack utilizing vector becuase rust doesn't have native stack implementation
        let mut stack: Vec<i32> = Vec::new();

        //iterate from left to right
        for i in 0..n
        {
            //use last() as peek() or top() basically
            while !stack.is_empty() && temperatures[i] > temperatures[*stack.last().unwrap() as usize]
            {
                let mut prev_index: i32 = stack.pop().unwrap();
                answer[prev_index as usize] = (i - prev_index as usize) as i32;
            }
            stack.push(i as i32)
        }
        //implicit return
        answer
    }
}
