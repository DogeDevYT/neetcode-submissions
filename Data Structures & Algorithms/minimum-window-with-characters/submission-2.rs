impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        if t.is_empty() {
            return String::new();
        }

        let s = s.as_bytes();
        let mut count_t: HashMap<u8, i32> = HashMap::new();
        for &c in t.as_bytes() {
            *count_t.entry(c).or_insert(0) += 1;
        }

        let mut res = (0usize, 0usize);
        let mut res_len = usize::MAX;

        for i in 0..s.len() {
            let mut count_s: HashMap<u8, i32> = HashMap::new();
            for j in i..s.len() {
                *count_s.entry(s[j]).or_insert(0) += 1;

                let flag = count_t.iter().all(|(&c, &cnt)| {
                    *count_s.get(&c).unwrap_or(&0) >= cnt
                });

                if flag && (j - i + 1) < res_len {
                    res_len = j - i + 1;
                    res = (i, j);
                }
            }
        }

        if res_len == usize::MAX {
            String::new()
        } else {
            String::from_utf8(s[res.0..=res.1].to_vec()).unwrap()
        }
    }
}