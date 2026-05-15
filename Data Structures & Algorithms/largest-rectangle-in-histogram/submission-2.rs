use std::cmp;

impl Solution {
    pub fn largest_rectangle_area(mut heights: Vec<i32>) -> i32 {
        //initialize empty stack to store indicies
        //but rust doesn't have native stack implementation so just use Vec
        let mut stack: Vec<usize> = Vec::new();;

        let mut max_area: i32 = 0; //store max area

        //append 0 to end of heights
        heights.push(0);

        //iterate through every index
        for i in 0..heights.len() 
        {
            let current_height: i32 = heights[i];

            //while stack is not empty and current height > height of bar on top of stack
            while !stack.is_empty() && current_height < heights[*stack.last().unwrap() as usize] 
            {
                //pop top index from stack
                let h_index: usize = stack.pop().unwrap();

                let height: i32 = heights[h_index];

                /*
                width: calculate right/left boundries

                right: simply use index we found to be smaller than this

                left: -1 if stack is empty or new top index of stack
                */

                let width: i32;

                if stack.is_empty() 
                {
                    width = i as i32;
                } else 
                {
                    width = (i as i32) - (*stack.last().unwrap() as i32) - 1;
                }

                max_area = cmp::max(max_area, height * width);
            }
            //apend current index to stack
            stack.push(i);
        }
        max_area
    }
}
