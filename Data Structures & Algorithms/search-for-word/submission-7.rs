impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let rows = board.len();
        let cols = board[0].len();
        let word: Vec<char> = word.chars().collect();
        let mut path = HashSet::new();

        for r in 0..rows {
            for c in 0..cols {
                if Self::dfs(&board, &word, r as i32, c as i32, 0, &mut path) {
                    return true;
                }
            }
        }
        false
    }

    fn dfs(
        board: &Vec<Vec<char>>, word: &[char],
        r: i32, c: i32, i: usize,
        path: &mut HashSet<(i32, i32)>,
    ) -> bool {
        if i == word.len() { return true; }
        if r < 0 || c < 0 || r >= board.len() as i32
            || c >= board[0].len() as i32
            || board[r as usize][c as usize] != word[i]
            || path.contains(&(r, c))
        {
            return false;
        }

        path.insert((r, c));
        let res = Self::dfs(board, word, r + 1, c, i + 1, path)
            || Self::dfs(board, word, r - 1, c, i + 1, path)
            || Self::dfs(board, word, r, c + 1, i + 1, path)
            || Self::dfs(board, word, r, c - 1, i + 1, path);
        path.remove(&(r, c));
        res
    }
}