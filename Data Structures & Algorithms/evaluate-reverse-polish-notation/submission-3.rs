impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        //Rust doesn't have native stack support so we just call push() and pop() from Vec
        let mut numbers: Vec<i32> = Vec::new();

        //iterate through each token
        for token in tokens 
        {
            //check if token is operator
            if token == "+" || token == "-" || token == "/" || token == "*"
            {
                let mut b: i32 = numbers.pop().unwrap();
                let mut a: i32 = numbers.pop().unwrap();

                if token == "+" 
                {
                    numbers.push(a + b);
                } else if token == "-" 
                {
                    numbers.push(a - b);
                } else if token == "/" 
                {
                    numbers.push(a / b);
                } else if token == "*" 
                {
                    numbers.push(a * b);
                }
            } else 
            {
                //push to stack
                //turbofish operator!
                numbers.push(token.parse::<i32>().unwrap());
            }
        }

        //implicit return
        numbers.pop().unwrap()
    }
}
