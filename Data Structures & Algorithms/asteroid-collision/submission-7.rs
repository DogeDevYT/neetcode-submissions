impl Solution {
    /*
    Ok for this problem, I got the algorithm super fast but the implementation
    of having repeated stack pops was super unintiutive and I needed to look
    at solution
    */
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        //create our stack using vec becuase rust is DiFfErEnT
        let mut stack: Vec<i32> = Vec::new();

        //iterate through asteroids
        for asteroid in asteroids 
        {
            //store copy becuase rust will 100% not let me edit
            //iterable values in-iteration
            let mut a: i32 = asteroid;

            //we need to iterate over the stack while
            //our current asteroid < 0 and top of stack > 0
            //since that means we have an imbalance
            while !stack.is_empty() && a < 0 && *stack.last().unwrap() > 0 
            {
                //store diff between negative asteroid and positive stack
                //top
                let diff: i32 = a + stack.last().unwrap();

                if diff < 0 
                {
                    //asteroid bigger; remove top of stack
                    stack.pop();
                } else if diff > 0 
                {
                    //asteroid on stack bigger so we need to 
                    //ignore asteroid in free space
                    a = 0;
                } else 
                {
                    //both same size smash both
                    a = 0;
                    stack.pop();
                }
            }

            //if we have an asteroid to add thats left over, add it
            if a != 0 
            {
                stack.push(a);
            }
        }

        stack
    }
}
