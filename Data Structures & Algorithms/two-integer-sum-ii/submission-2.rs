impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut l: usize = 0;
        let mut r: usize = numbers.len() - 1;

        let mut answer: Vec<i32> = vec![0; 2];

        while l < r 
        {
            let sum = numbers[l] + numbers[r];

            if sum < target 
            {
                l += 1;
            } else if sum > target 
            {
                r -= 1;
            } else 
            {
                answer = vec![(l as i32) + 1, (r as i32) + 1];
                return answer;
            }
        }

        return answer;
    }
}
