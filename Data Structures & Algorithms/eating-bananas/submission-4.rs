impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut l: i32 = 1;
        let mut r: i32 = piles.iter().copied().max().unwrap();

        let mut result: i32 = r;

        while l <= r {
            let k: i32 = (l + r) / 2;
            let mut total_time: i64 = 0;

            for pile in &piles {
                // Good use of the ceiling division trick!
                total_time += (pile + k - 1) as i64 / k as i64;
            }

            if total_time <= h as i64 {
                result = k;
                r = k - 1;
            } else {
                l = k + 1;
            }
        }
        result
    }
}