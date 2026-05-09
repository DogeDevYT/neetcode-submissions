impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        /*
        I now remember how to do this the efficient way: we have to use prefix/postfix products.

        i.e. we have an array to store the prefix products (the product of each number up to that point)
        and another one for postfix (the product of each number after that point)

        and simply multiply each one at that index

        update: I just realized we can do it with one array by filling it with pre first and then post
        */
        
        //initialize array of n nums with i32 type
        let mut solution = vec![0; nums.len()];

        //populate solution vector with prefix products
        for i in 0..nums.len() 
        {
            if i > 0 
            {
                solution[i] = solution[i-1]*nums[i-1];
            }
            else 
            {
                //first element
                solution[i] = 1;
            }
        }

        let mut running_product = 1;
        solution[nums.len()-1] *= running_product;

        //populate solution vector with postfix products
        // by iterating in reverse with a running product
        for i in (0..nums.len()-1).rev() 
        {
            running_product *= &nums[i+1];
            solution[i] *= running_product;
        }

        //no semicolon - shorthand for return
        solution
    }
}
