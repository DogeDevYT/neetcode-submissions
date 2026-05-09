class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
        I now remember how to do this the efficient way: we have to use prefix/postfix products.

        i.e. we have an array to store the prefix products (the product of each number up to that point)
        and another one for postfix (the product of each number after that point)

        and simply multiply each one at that index

        update: I just realized we can do it with one array by filling it with pre first and then post
        */

        //initialize solution vector
        std::vector<int> solution;

        //pouplate solution vector with prefix products
        for(int i = 0; i < nums.size(); i++) 
        {
            if (i < 1) 
            {
                solution.push_back(1); //first element
            } else 
            {
                solution.push_back(solution[i-1]*nums[i-1]);
            }
        }

        //initialize running product to account for not having postfix array to lookup from
        //anymore
        int running_product = 1;

        //iterate through in reverse and multiply by running product
        for (int i = nums.size() - 1; i >= 0; i--) 
        {
            if (i >= nums.size() - 1) 
            {
                solution[i] *= running_product; //first run through with last element in solution
            } else 
            {
                running_product *= nums[i+1];
                solution[i] *= running_product;
            }
        }

        return solution;
    }
};
