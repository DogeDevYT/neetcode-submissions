impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        //create pairs of tuples basically for car fleet
        let mut pair: Vec<(i32, i32)> = position.into_iter()
            .zip(speed.into_iter())
            .collect();
        pair.sort_by(|a, b| b.0.cmp(&a.0));

        //create our stack from vec because rust doesn't have native stack implementation
        let mut stack: Vec<f64> = Vec::new();

        for (p, s) in pair 
        {
            stack.push((target - p) as f64 / s as f64); // time = (target - postion) / speed
            let len = stack.len();

            if len >= 2 && stack[len - 1] <= stack[len - 2] 
            {
                stack.pop();
            }
        }
        
        stack.len() as i32
    }
}
