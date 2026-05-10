impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows: Vec<HashSet<char>> = vec![HashSet::new(); 9];
        let mut cols: Vec<HashSet<char>> = vec![HashSet::new(); 9];
        let mut squares: Vec<HashSet<char>> = vec![HashSet::new(); 9];

        for r in 0..9 {
            for c in 0..9 {
                if board[r][c] == '.' { continue; }
                let val = board[r][c];
                let square_idx = (r / 3) * 3 + c / 3;

                if !rows[r].insert(val)
                    || !cols[c].insert(val)
                    || !squares[square_idx].insert(val)
                {
                    return false;
                }
            }
        }

        true 
    }
}
