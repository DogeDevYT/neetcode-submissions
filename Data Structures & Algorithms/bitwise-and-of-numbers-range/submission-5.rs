impl Solution {
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        let mut right = right;
        while right > left {
            right &= right-1;
        }
        right
    }
}
