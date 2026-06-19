impl Solution {
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        let mut curr: i64 = left as i64;
        let mut idx: i64 = left as i64;

        while idx < right as i64
        {
            curr &= idx + 1;
            idx += 1;
        }
        return curr as i32;
    }
}
