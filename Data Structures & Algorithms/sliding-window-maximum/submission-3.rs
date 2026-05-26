use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        //create queue of indicies for later
        let mut q: VecDeque<usize> = VecDeque::new();

        //create output vector
        let mut output: Vec<i32> = Vec::new();

        //iterate through all numbers in vector
        for i in 0..nums.len() 
        {
            /*
            maintain monotonic property by removing numbres from back
            becuase that means they wont be included in the sliding window
            maximum to begin with because we want the maximum of each
            */

            while let Some(&back_idx) = q.back() 
            {
                if nums[back_idx] < nums[i] 
                {
                    q.pop_back();
                } else 
                {
                    break;
                }
            }

            //push current element to end of queue
            q.push_back(i);

            //remove front index from queue since its constantly asking
            //from MAX from list
            if let Some(&front_idx) = q.front() 
            {
                if front_idx + (k as usize) <= i
                {
                    q.pop_front();
                }
            }

            //while sliding window is built up, we can start adding to
            //output
            if let Some(&front_idx) = q.front() 
            {
                if i >= (k as usize) - 1 
                {
                    output.push(nums[front_idx]);
                }
            }
        }
        output
    }
}
